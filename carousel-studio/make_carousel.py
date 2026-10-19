#!/usr/bin/env python3
"""
Render an Instagram carousel in the "blue caption bubble" style
(candid photo + white bold text in royal-blue rounded boxes, one box per line,
merged into a stepped shape, centred).

    python3 carousel-studio/make_carousel.py carousel-studio/decks/example.txt

Writes 1080x1350 PNGs + a contact sheet to carousel-studio/out/<deck-name>/.
Deck format is documented in carousel-studio/README.md.
"""

import argparse
import os
import re
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))

W, H = 1080, 1350
SS = 3  # supersampling for smooth box edges

BOX = (8, 1, 157)  # sampled from the reference post: #08019D
TEXT = (255, 255, 255)

# size name -> font px. Body is the workhorse; xl is hook/CTA; h is a step header.
SIZES = {"xl": 74, "h": 58, "body": 44, "small": 32}
MAX_TEXT_W = 920  # widest a line of text may run before wrapping
PITCH = 1.40      # baseline-to-baseline, multiple of font size
BOX_H = 1.82      # height of each line's box (taller than PITCH, so boxes overlap)
PAD_X = 0.46      # box side padding, multiple of font size
RADIUS = 0.36     # corner radius, multiple of font size

FONT_CANDIDATES = [
    # Helvetica Neue Bold on a Mac (what the reference uses)
    ("/System/Library/Fonts/HelveticaNeue.ttc", "Bold"),
    ("/System/Library/Fonts/Helvetica.ttc", "Bold"),
    # bundled fallback, works anywhere
    (os.path.join(HERE, "fonts", "InterDisplay-Bold.otf"), None),
]


def load_font_path():
    override = os.environ.get("CAROUSEL_FONT")
    if override:
        return override, 0
    for path, style in FONT_CANDIDATES:
        if not os.path.exists(path):
            continue
        if style is None:
            return path, 0
        for idx in range(16):
            try:
                f = ImageFont.truetype(path, 20, index=idx)
            except OSError:
                break
            if f.getname()[1] == style:
                return path, idx
    sys.exit("No usable font found. Set CAROUSEL_FONT=/path/to/font.ttf")


FONT_PATH, FONT_INDEX = load_font_path()
_font_cache = {}


def font(px):
    if px not in _font_cache:
        _font_cache[px] = ImageFont.truetype(FONT_PATH, px, index=FONT_INDEX)
    return _font_cache[px]


# ---------------------------------------------------------------- deck parsing

def parse_deck(text):
    """Slides split on '---'. 'key: value' settings, then text lines."""
    slides = []
    for chunk in re.split(r"^\s*---\s*$", text, flags=re.M):
        settings, blocks = {}, []
        for raw in chunk.splitlines():
            line = raw.rstrip()
            if not line.strip() or line.lstrip().startswith("//"):
                continue
            m = re.match(r"^(photo|bw|darken|focus|y|blur)\s*:\s*(.*)$", line.strip(), re.I)
            if m and not blocks:
                settings[m.group(1).lower()] = m.group(2).strip()
                continue
            s = line.strip()
            if s.startswith("## "):
                blocks.append(("xl", s[3:]))
            elif s.startswith("# "):
                blocks.append(("h", s[2:]))
            elif s.startswith("- "):
                blocks.append(("small", s[2:]))
            else:
                blocks.append(("body", s))
        if blocks or settings.get("photo"):
            slides.append({"settings": settings, "blocks": blocks})
    return slides


def tokenize(text):
    """'_word_' or '_two words_' = underlined. Returns [(word, underlined)]."""
    out, in_ul = [], False
    for w in text.split():
        if w.startswith("_"):
            in_ul, w = True, w[1:]
        ul = in_ul
        m = re.search(r"_(?=[^\w]*$)", w)  # closing underscore, maybe before punctuation
        if in_ul and m:
            w, in_ul = w[:m.start()] + w[m.end():], False
        if w:
            out.append((w, ul))
    return out


# ---------------------------------------------------------------- layout

def wrap(tokens, f, max_w):
    lines, cur = [], []
    space = f.getlength(" ")
    for tok in tokens:
        trial = cur + [tok]
        width = sum(f.getlength(w) for w, _ in trial) + space * (len(trial) - 1)
        if cur and width > max_w:
            lines.append(cur)
            cur = [tok]
        else:
            cur = trial
    if cur:
        lines.append(cur)
    # no one-word last line: pull a word down from the line above
    if len(lines) > 1 and len(lines[-1]) == 1 and len(lines[-2]) > 2:
        lines[-1].insert(0, lines[-2].pop())
    return lines


def line_width(line, f):
    return sum(f.getlength(w) for w, _ in line) + f.getlength(" ") * (len(line) - 1)


def snap_widths(widths, r):
    """Neighbouring lines whose edges sit closer than r get the same width,
    so the merged shape never has a sliver step (TikTok does the same)."""
    widths = list(widths)
    changed = True
    while changed:
        changed = False
        for i in range(len(widths) - 1):
            a, b = widths[i], widths[i + 1]
            if a != b and abs(a - b) / 2 < r:
                widths[i] = widths[i + 1] = max(a, b)
                changed = True
    return widths


def layout_block(kind, text):
    px = SIZES[kind]
    f = font(px)
    lines = wrap(tokenize(text), f, MAX_TEXT_W)
    pitch = round(px * PITCH)
    box_h = round(px * BOX_H)
    pad = round(px * PAD_X)
    r = round(px * RADIUS)
    widths = snap_widths([line_width(l, f) + 2 * pad for l in lines], r)
    return {"kind": kind, "px": px, "f": f, "lines": lines, "pitch": pitch,
            "box_h": box_h, "r": r, "widths": widths,
            "h": pitch * (len(lines) - 1) + box_h}


def gap_between(a, b):
    kinds = {a["kind"], b["kind"]}
    if kinds == {"small"}:
        return round(SIZES["small"] * 0.85)
    if kinds == {"xl", "small"}:  # hook + its little subhead sit close
        return round(SIZES["small"] * 0.6)
    return round(max(a["px"], b["px"]) * 0.95)


# ---------------------------------------------------------------- drawing

def draw_block_shape(mask, block, top, cx):
    """Union of per-line rounded rects, with concave fillets where widths step."""
    s = SS
    r = block["r"] * s
    pitch = block["pitch"] * s
    box_h = block["box_h"] * s
    ws = [w * s for w in block["widths"]]
    n = len(ws)
    x_l = [cx * s - w / 2 for w in ws]
    x_r = [cx * s + w / 2 for w in ws]
    tops = [top * s + i * pitch for i in range(n)]
    bottoms = [t + box_h for t in tops]

    for i in range(n):
        t, b = tops[i], bottoms[i]
        layer = Image.new("L", mask.size, 0)
        ld = ImageDraw.Draw(layer)
        ld.rectangle([x_l[i], t, x_r[i], b], fill=255)
        above_wider = i > 0 and ws[i - 1] >= ws[i]
        below_wider = i < n - 1 and ws[i + 1] >= ws[i]
        corners = []
        if not above_wider:
            corners += [(x_l[i], t, 1, 1), (x_r[i], t, -1, 1)]
        if not below_wider:
            corners += [(x_l[i], b, 1, -1), (x_r[i], b, -1, -1)]
        for x, y, dx, dy in corners:
            ld.rectangle(sorted_box(x, y, x + dx * r, y + dy * r), fill=0)
            cxr, cyr = x + dx * r, y + dy * r
            ld.ellipse([cxr - r, cyr - r, cxr + r, cyr + r], fill=255)
        mask.paste(ImageChops.lighter(mask, layer))

        # concave fillets on the narrower line, where it meets a wider
        # neighbour's edge: grow outward from that edge into the narrow line
        for j, dy in ((i - 1, 1), (i + 1, -1)):
            if 0 <= j < n and ws[j] > ws[i]:
                junction = bottoms[j] if j < i else tops[j]
                for x, dx in ((x_l[i], -1), (x_r[i], 1)):
                    f = Image.new("L", mask.size, 0)
                    fd = ImageDraw.Draw(f)
                    fd.rectangle(sorted_box(x, junction, x + dx * r, junction + dy * r), fill=255)
                    ccx, ccy = x + dx * r, junction + dy * r
                    fd.ellipse([ccx - r, ccy - r, ccx + r, ccy + r], fill=0)
                    mask.paste(ImageChops.lighter(mask, f))


def sorted_box(x0, y0, x1, y1):
    return [min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)]


def draw_block_text(img, block, top, cx):
    d = ImageDraw.Draw(img)
    f = block["f"]
    px = block["px"]
    cap = -f.getbbox("H", anchor="ls")[1]
    space = f.getlength(" ")
    ul_thick = max(2, round(px * 0.065))
    ul_off = round(px * 0.13)
    for i, line in enumerate(block["lines"]):
        lw = line_width(line, f)
        x = cx - lw / 2
        base = top + i * block["pitch"] + block["box_h"] / 2 + cap / 2
        run_start = None
        for k, (word, ul) in enumerate(line):
            wl = f.getlength(word)
            d.text((x, base), word, font=f, fill=TEXT, anchor="ls")
            if ul:
                # underline the word itself, not trailing punctuation
                core = word.rstrip(".,:;!?\"'”’)")
                core_w = f.getlength(core)
                if run_start is None:
                    run_start = x
                nxt_ul = k + 1 < len(line) and line[k + 1][1]
                if not nxt_ul:
                    y = base + ul_off
                    d.rectangle([run_start, y, x + core_w, y + ul_thick], fill=TEXT)
                    run_start = None
            x += wl + space


def background(settings, deck_dir):
    photo = settings.get("photo")
    path = None
    if photo:
        for cand in (os.path.join(deck_dir, photo), os.path.join(HERE, "photos", photo), photo):
            if os.path.exists(cand):
                path = cand
                break
        if path is None:
            print(f"  ! photo not found: {photo} (using placeholder)", file=sys.stderr)
    if path:
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        focus = settings.get("focus", "center").lower()
        fy = {"top": 0.0, "center": 0.5, "middle": 0.5, "bottom": 1.0}.get(focus)
        if fy is None:
            fy = float(focus)
        im = ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, fy))
    else:
        im = Image.linear_gradient("L").resize((W, H)).point(lambda v: 70 - v * 40 // 255)
        im = Image.merge("RGB", (im, im, im))
        ImageDraw.Draw(im).text((W / 2, H - 40), "PHOTO GOES HERE", font=font(22),
                                fill=(120, 120, 120), anchor="ms")
    if str(settings.get("bw", "")).lower() in ("1", "yes", "true", "y"):
        im = ImageOps.grayscale(im).convert("RGB")
    darken = float(settings.get("darken", 0.18))
    if darken > 0:
        im = Image.blend(im, Image.new("RGB", im.size, (0, 0, 0)), darken)
    return im


def render_slide(slide, deck_dir):
    img = background(slide["settings"], deck_dir)
    blocks = [layout_block(k, t) for k, t in slide["blocks"]]
    if not blocks:
        return img
    gaps = [gap_between(a, b) for a, b in zip(blocks, blocks[1:])]
    total = sum(b["h"] for b in blocks) + sum(gaps)
    centre_y = float(slide["settings"].get("y", 0.5)) * H
    top = round(centre_y - total / 2)
    cx = W / 2

    mask = Image.new("L", (W * SS, H * SS), 0)
    tops = []
    y = top
    for i, b in enumerate(blocks):
        tops.append(y)
        draw_block_shape(mask, b, y, cx)
        y += b["h"] + (gaps[i] if i < len(gaps) else 0)
    mask = mask.resize((W, H), Image.LANCZOS)
    img.paste(Image.new("RGB", (W, H), BOX), (0, 0), mask)
    for b, t in zip(blocks, tops):
        draw_block_text(img, b, t, cx)
    return img


def contact_sheet(paths, out):
    thumbs = [Image.open(p).resize((360, 450), Image.LANCZOS) for p in paths]
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    g = 12
    sheet = Image.new("RGB", (cols * 360 + (cols + 1) * g, rows * 450 + (rows + 1) * g), (245, 245, 245))
    for i, t in enumerate(thumbs):
        sheet.paste(t, (g + (i % cols) * (360 + g), g + (i // cols) * (450 + g)))
    sheet.save(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", help="deck .txt file")
    ap.add_argument("--out", help="output folder (default carousel-studio/out/<deck name>)")
    args = ap.parse_args()

    with open(args.deck, encoding="utf-8") as fh:
        slides = parse_deck(fh.read())
    name = os.path.splitext(os.path.basename(args.deck))[0]
    out_dir = args.out or os.path.join(HERE, "out", name)
    os.makedirs(out_dir, exist_ok=True)
    deck_dir = os.path.dirname(os.path.abspath(args.deck))

    print(f"font: {os.path.basename(FONT_PATH)}  slides: {len(slides)}")
    paths = []
    for n, slide in enumerate(slides, 1):
        p = os.path.join(out_dir, f"slide-{n:02d}.png")
        render_slide(slide, deck_dir).save(p)
        paths.append(p)
        print(f"  {p}")
    sheet = os.path.join(out_dir, "contact-sheet.jpg")
    contact_sheet(paths, sheet)
    print(f"  {sheet}")


if __name__ == "__main__":
    main()
