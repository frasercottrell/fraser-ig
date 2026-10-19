#!/usr/bin/env python3
"""Competitor Radar: flag reels that beat their own creator's median, write picklist.md.

Spec: Competitor-Radar.md (Step 3). Two ways to get data in:

    # A) Apify (cloud sessions): the radar skill runs apify/instagram-reel-scraper
    #    and saves the dataset to radar/cache/raw-<date>.json, then:
    python3 radar/radar.py score --apify radar/cache/raw-2026-10-19.json

    # B) HikerAPI (local runs): HIKER_API_KEY in .env
    python3 radar/radar.py fetch          # pulls ~40 reels per creator, caches, scores

    python3 radar/radar.py score --cache radar/cache/hiker-2026-10-19.json   # re-score, no API spend
"""

import argparse
import json
import os
import statistics
import sys
import time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
COHORT_PATH = os.path.join(HERE, "cohort.json")
CACHE_DIR = os.path.join(HERE, "cache")
PICKLIST_PATH = os.path.join(HERE, "picklist.md")

WINDOW_MIN_AGE_H = 72        # younger than 3 days: still collecting views, skip
WINDOW_MAX_AGE_D = 30        # older than 30 days: says little about what works now
MIN_RATIO        = 5.0       # primary bar: 5x the creator's own median
HYBRID_RATIO     = 3.0       # secondary bar: 3x is enough...
HYBRID_MIN_VIEWS = 50_000    # ...when the reach is real
ABS_FLOOR_VIEWS  = 30_000    # every qualifier needs real reach

REELS_PER_CREATOR = 40
HIKER_BASE = "https://api.hikerapi.com/v1"


def load_cohort():
    with open(COHORT_PATH) as f:
        return json.load(f)


def load_env():
    path = os.path.join(os.path.dirname(HERE), ".env")
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


# ---------- normalising ----------

def _iso_to_epoch(ts):
    if isinstance(ts, (int, float)):
        return int(ts)
    try:
        return int(datetime.fromisoformat(str(ts).replace("Z", "+00:00")).timestamp())
    except ValueError:
        return 0


def normalise_apify(items):
    """apify/instagram-reel-scraper dataset -> {creator: [reel, ...]}"""
    out = {}
    for it in items:
        if it.get("error") or not it.get("shortCode"):
            continue
        if it.get("type") != "Video" and it.get("productType") != "clips":
            continue
        creator = (it.get("ownerUsername") or "").lower()
        views = it.get("videoPlayCount") or it.get("videoViewCount") or 0
        out.setdefault(creator, []).append({
            "code": it["shortCode"],
            "url": f"https://www.instagram.com/reel/{it['shortCode']}/",
            "views": int(views),
            "likes": int(it.get("likesCount") or 0),
            "comments": int(it.get("commentsCount") or 0),
            "caption": (it.get("caption") or "").strip(),
            "taken_at": _iso_to_epoch(it.get("timestamp")),
            "pinned": bool(it.get("isPinned")),
        })
    return out


def normalise_hiker_clip(clip):
    if clip.get("media_type") != 2 and clip.get("product_type") != "clips":
        return None
    cap = clip.get("caption_text") or (clip.get("caption") or {}).get("text") or ""
    return {
        "code": clip["code"],
        "url": f"https://www.instagram.com/reel/{clip['code']}/",
        "views": int(clip.get("play_count") or clip.get("view_count") or 0),
        "likes": int(clip.get("like_count") or 0),
        "comments": int(clip.get("comment_count") or 0),
        "caption": cap.strip(),
        "taken_at": _iso_to_epoch(clip.get("taken_at") or 0),
        "pinned": False,
    }


# ---------- fetching (HikerAPI) ----------

def _hiker_get(path, params, key):
    import requests
    for attempt in range(3):
        r = requests.get(f"{HIKER_BASE}{path}", params=params,
                         headers={"x-access-key": key}, timeout=60)
        if r.status_code in (401, 403):
            sys.exit(f"HikerAPI said {r.status_code}: bad or empty key. Check HIKER_API_KEY in .env.")
        if r.status_code == 404:
            return None
        if r.status_code >= 500:
            time.sleep(2 * (attempt + 1))
            continue
        r.raise_for_status()
        return r.json()
    return None


def fetch_hiker(creators):
    key = os.environ.get("HIKER_API_KEY")
    if not key:
        sys.exit("No HIKER_API_KEY. Put it in .env, or use the Apify route (see the radar skill).")
    out = {}
    for c in creators:
        handle = c["username"].lstrip("@").lower()
        profile = _hiker_get("/user/by/username", {"username": handle}, key)
        if not profile:
            print(f"  @{handle}: not found, skipped")
            continue
        reels, cursor = [], None
        while len(reels) < REELS_PER_CREATOR:
            params = {"user_id": profile["pk"]}
            if cursor:
                params["end_cursor"] = cursor
            page = _hiker_get("/user/clips/chunk", params, key)
            if not page or not page[0]:
                break
            reels += [r for r in (normalise_hiker_clip(x) for x in page[0]) if r]
            cursor = page[1]
            if not cursor:
                break
        out[handle] = reels[:REELS_PER_CREATOR]
        print(f"  @{handle}: {len(out[handle])} reels")
    return out


# ---------- scoring (the spec, verbatim logic) ----------

def find_outliers(reels_by_creator, now=None):
    now = now or time.time()
    outliers, baselines = [], {}
    for creator, reels in reels_by_creator.items():
        window = [r for r in reels
                  if WINDOW_MIN_AGE_H * 3600 <= now - r["taken_at"] <= WINDOW_MAX_AGE_D * 86400]
        if len(window) < 5:
            baselines[creator] = {"window": len(window), "median": None}
            continue  # not enough signal to trust a baseline
        median = statistics.median(r["views"] for r in window) or 1
        baselines[creator] = {"window": len(window), "median": int(median),
                              "max": max(r["views"] for r in window)}
        for r in window:
            ratio = r["views"] / median
            beats_bar = ratio >= MIN_RATIO or (ratio >= HYBRID_RATIO and r["views"] >= HYBRID_MIN_VIEWS)
            if beats_bar and r["views"] >= ABS_FLOOR_VIEWS:
                outliers.append({**r, "creator": creator, "ratio": round(ratio, 1),
                                 "median": int(median)})
    return sorted(outliers, key=lambda r: r["ratio"], reverse=True), baselines


# ---------- output ----------

def _k(n):
    return f"{n / 1_000_000:.1f}M" if n >= 1_000_000 else f"{n / 1000:.0f}k" if n >= 1000 else str(n)


def _about(caption):
    first = caption.split("\n")[0].strip().replace("|", "/")
    return (first[:70] + "...") if len(first) > 70 else first or "(no caption)"


def write_picklist(outliers, baselines, self_handle=None):
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [f"# Radar pick list - {date}", "",
             f"Floors: {MIN_RATIO}x median, or {HYBRID_RATIO}x with {_k(HYBRID_MIN_VIEWS)}+ views; "
             f"every pick {_k(ABS_FLOOR_VIEWS)}+ views. Window 3 to 30 days.", "",
             "| # | Ratio | Views | Creator | What it's about | Link | Pick? |",
             "|---|-------|-------|---------|-----------------|------|-------|"]
    for i, r in enumerate(outliers, 1):
        lines.append(f"| {i} | {r['ratio']}x | {_k(r['views'])} | @{r['creator']} | "
                     f"{_about(r['caption'])} | {r['url']} |  |")
    if not outliers:
        lines.append("| - | - | - | - | No outliers cleared the floors. See baselines below. | - | - |")

    lines += ["", "## Reads", "",
              "<!-- Claude fills one block per row: Why it won / Fits Fraser? -->", ""]
    for i, r in enumerate(outliers, 1):
        lines += [f"### {i}. @{r['creator']} - {r['ratio']}x ({_k(r['views'])} vs median {_k(r['median'])})",
                  f"> {_about(r['caption'])}", "", "- **Why it won:** ", "- **Fits Fraser?** ", ""]

    lines += ["## Baselines (for tuning the floors)", "",
              "| Creator | Reels in window | Median views | Best in window |",
              "|---------|-----------------|--------------|----------------|"]
    for c, b in sorted(baselines.items(), key=lambda kv: -(kv[1]["median"] or 0)):
        tag = " (you)" if c == (self_handle or "").lower() else ""
        med = _k(b["median"]) if b["median"] else "too few reels"
        best = _k(b["max"]) if b.get("max") else "-"
        lines.append(f"| @{c}{tag} | {b['window']} | {med} | {best} |")

    with open(PICKLIST_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")
    return PICKLIST_PATH


def run(reels_by_creator, cohort):
    self_handle = cohort.get("self")
    competitors = {c: r for c, r in reels_by_creator.items() if c != (self_handle or "").lower()}
    outliers, baselines = find_outliers(competitors)
    if self_handle and self_handle.lower() in reels_by_creator:
        _, mine = find_outliers({self_handle.lower(): reels_by_creator[self_handle.lower()]})
        baselines.update(mine)
    path = write_picklist(outliers, baselines, self_handle)

    print(f"\n{len(outliers)} outliers from {len(competitors)} creators -> {path}\n")
    for i, r in enumerate(outliers[:10], 1):
        print(f"{i:2d}. {r['ratio']:>5}x  {_k(r['views']):>6}  @{r['creator']:<20} {_about(r['caption'])}")
    meds = sorted(b["median"] for b in baselines.values() if b["median"])
    if meds:
        print(f"\nCohort medians: low {_k(meds[0])}, mid {_k(int(statistics.median(meds)))}, "
              f"high {_k(meds[-1])}. Floors set at {_k(ABS_FLOOR_VIEWS)} / {_k(HYBRID_MIN_VIEWS)}.")
        print("Rule of thumb: ABS_FLOOR_VIEWS ~ the strongest account's median, HYBRID_MIN_VIEWS ~ double it.")


def main():
    load_env()
    p = argparse.ArgumentParser(description="Competitor Radar")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch", help="pull reels via HikerAPI, cache, score")
    s = sub.add_parser("score", help="score a saved dataset (no API spend)")
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--apify", help="apify/instagram-reel-scraper dataset JSON")
    g.add_argument("--cache", help="a hiker-<date>.json cache from a previous fetch")
    args = p.parse_args()

    cohort = load_cohort()
    if args.cmd == "fetch":
        creators = list(cohort["creators"])
        if cohort.get("self"):
            creators.append({"username": cohort["self"]})
        data = fetch_hiker(creators)
        os.makedirs(CACHE_DIR, exist_ok=True)
        path = os.path.join(CACHE_DIR, f"hiker-{datetime.now().strftime('%Y-%m-%d')}.json")
        with open(path, "w") as f:
            json.dump(data, f)
        print(f"  cached -> {path}")
    elif args.apify:
        with open(args.apify) as f:
            data = normalise_apify(json.load(f))
    else:
        with open(args.cache) as f:
            data = json.load(f)
    run(data, cohort)


if __name__ == "__main__":
    main()
