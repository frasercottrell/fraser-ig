---
name: competitor-radar
description: Run Fraser's Competitor Radar. Scrape the cohort's recent reels, flag the ones that beat their own creator's median, write why-it-won reads into a pick list, then turn Fraser's picks into trial-reel packs (3 on-screen hooks, B-roll first frame, short caption, matching keyword). Use when Fraser says "run the radar", "/competitor-radar", "what should I post", "find me outliers", "write briefs for my picks", or wants proven topics for a trial-reel batch.
---

# Competitor Radar (Fraser's version)

Source spec: `Competitor-Radar.md` (the YouTube one). The loop is unchanged:

> cohort -> pull each account's recent reels -> flag the ones that beat that account's own median -> read why they won -> pick list -> hooks per pick.

What's different here is Step 5: Fraser's trial reels are B-roll + one on-screen line, not 60-90s scripts.

Files: `radar/cohort.json` (who we watch), `radar/radar.py` (scoring, spec math verbatim), `radar/picklist.md` (output),
`radar/cache/` (raw data, gitignored). Fraser's baseline: median ~640 plays a reel (2026-10-19 pull, 25 reels in window).

## Step 1: Fetch

**Cloud session (Apify MCP connected):** call `apify/instagram-reel-scraper` once with every handle in
`cohort.json` plus `self`:

```json
{"username": ["handle1", "handle2", "frasercottrell"], "resultsLimit": 40,
 "skipPinnedPosts": true, "onlyPostsNewerThan": "35 days"}
```

Set `callOptions.maxTotalChargeUsd` to about `0.003 x 40 x handles` (15 handles = ~$2). Long runs come back
RUNNING: poll `get-actor-run`, then page `get-dataset-items` with
`fields=shortCode,type,productType,ownerUsername,videoPlayCount,videoViewCount,likesCount,commentsCount,timestamp,isPinned,caption`.
Save the items as a JSON array at `radar/cache/raw-<YYYY-MM-DD>.json`.

**Local (HikerAPI):** `HIKER_API_KEY=...` in `.env`, then `python3 radar/radar.py fetch`.

## Step 2: Score

```
python3 radar/radar.py score --apify radar/cache/raw-<date>.json
```

After the **first** run with a new cohort, show Fraser the baselines table and suggest floors: `ABS_FLOOR_VIEWS`
~ the strongest account's median, `HYBRID_MIN_VIEWS` ~ double. Change them in `radar.py` only with his yes.

## Step 3: Reads (fill `radar/picklist.md`)

For each row, two lines under its `### N.` block:

1. **Why it won:** topic, the promise in line one, and the mechanism (number in the hook, contrarian claim, named
   tool, transformation, "nobody tells you this"). Caption + numbers + link only, unless transcripts were pulled
   (`includeTranscript: true`, ~$0.05 a reel; use only on rows Fraser is likely to pick).
2. **Fits Fraser?** yes/no + one line. Run it through `context/strategy.md`'s one test: does this deepen "he
   understands ad creative better than me"? Audience is e-com founders and heads of growth, above beginner. AI
   topics only if framed for operators. Hard no: Steven Bartlett / Huel.

Hand over the table + reads. **Fraser marks the Pick? column. He always has the final say.**

## Dead topics (Fraser's call: mark these "Fits Fraser? no" even when they outlie)

- 2026-10-19: Mac Mini / always-on AI agent setups ("I thought the Mac Mini hype was dumb..."). Trend is over.

## Step 4: Picks -> trial-reel packs

Before writing anything: read `hooks/LEDGER.md` (MISS 1-8, tested-won/lost map), the last few entries of
`context/results-log.md`, and `context/instagram-voice-patterns.md`. Then, per pick:

- **3 on-screen hooks.** Hook 1 adapts the winner's hook to Fraser's angle. Hooks 2 and 3 are different angles
  inside the three families (contrarian expertise / competitive gap / pattern recognition). Trial-reel bar from the
  ledger: 9-16 words, one line, viewer named + crowd proof + unresolved gap + "ads" in the line, plain statement
  not punchline, at most one tic. No two hooks share their first three words. Never mention the freebie in the hook (MISS 8).
  Never use Fraser's own stats as proof (MISS 7). Don't reuse facts from the last three batches (MISS 5).
- **First frame:** name the B-roll shot. Tight, centred, slightly odd, implies real ad production. Not wide studio, not Fraser sitting.
- **Caption:** short trial-reel standard (~70 words): one-line setup, compact list, one takeaway, CTA.
- **Keyword:** must match a live freebie (HOOKS, STATIC, YAP, FEET, FORMAT, SCRIPT, TRANSLATE, FOUNDER, AI Script).
  No match = follow-only CTA. Never invent a keyword with no delivery.
- **Hand-over format (MISS 6):** the hooks one line each, then shot / caption / keyword. No method notes.
- Run `python3 scripts/voice-lint.py` on the pack and fix real flags in his register. Lint passing is not the bar.

If Fraser wants a **talking head** off a pick instead, use the source doc's script prompt (3 hooks + 60-90s body
that works after any hook + one-word comment CTA), then `/talking-head-captions` for the caption.

## Step 5: Log it

Append every hook handed over to `hooks/LEDGER.md` (status `proposed`, parent = `radar <date> @creator <code>`).
When results come back, they go in `context/results-log.md` like any other reel. Commit to the default branch.

## The rule

Never record a topic because it might work. Record it because the radar showed it already did, for a real account,
against that account's own baseline.
