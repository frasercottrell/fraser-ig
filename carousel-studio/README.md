# Carousel Studio

Renders Instagram carousels in the **blue caption bubble** style (reference:
[@briarcochran, "How to have an ungodly amount of creativity"](https://www.instagram.com/p/DeZiSoBG0Zf/)):
a candid behind-the-scenes photo, with white bold text in royal-blue rounded boxes on top. Every line
gets its own box, and the boxes merge into one stepped shape.

```
python3 carousel-studio/make_carousel.py carousel-studio/decks/<name>.txt
```

Output goes to `carousel-studio/out/<name>/`: `slide-01.png` … (1080×1350) plus `contact-sheet.jpg`.
Needs Python 3 + Pillow (`pip install pillow`).

## The design language

| | |
|---|---|
| Box colour | `#08019D` royal blue, sampled from the reference |
| Text | white, bold, sentence case, centred |
| Font | Helvetica Neue Bold on a Mac; falls back to the bundled Inter Display Bold everywhere else |
| Boxes | one rounded box per line, hugging the text, merged into a stepped shape with concave corners |
| Emphasis | underline **one** key word or phrase per block. Never bold, never colour |
| Photo | real BTS: cameras, laptops, the team working. Darkened a little so the text reads |
| Last slide | black and white photo + one big CTA box |

## Deck format

One plain `.txt` file per carousel. Slides are separated by `---`.

```
photo: office-camera.jpg
## How to have an ungodly amount of creativity.
- (Without Burning Out)
---
photo: team-laptop.jpg
# 1. Control Your Inputs
You must be _deliberate_ in what you take in.
Watching Dancing With The Stars is not going to make you more creative.
---
photo: desk.jpg
bw: yes
## Follow for more content like this.
```

**Text lines.** Each line becomes its own box group, wrapped automatically.

| Prefix | Size | Use for |
|---|---|---|
| `## ` | XL (74px) | cover hook, CTA |
| `# ` | header (58px) | "1. Control Your Inputs", short punchy one-liners |
| *(none)* | body (44px) | the workhorse |
| `- ` | small (32px) | subheads like "(Without Burning Out)", lists like "Minutes 0-15: …" |

`_word_` or `_a few words_` underlines that word or phrase. Lines starting with `//` are comments.

**Slide settings.** Optional `key: value` lines at the top of a slide, before any text:

| Setting | Default | What it does |
|---|---|---|
| `photo:` | placeholder | file in `carousel-studio/photos/`, or a path relative to the deck |
| `bw:` | no | `yes` makes the photo black and white |
| `darken:` | 0.18 | 0 to 1. Push up (0.3–0.4) on bright or busy photos |
| `focus:` | center | crop anchor: `top`, `center`, `bottom`, or 0–1 |
| `y:` | 0.5 | vertical centre of the text stack, 0 to 1. Move it off a face |

## Folders

- `decks/` the slide text for each carousel (commit these)
- `photos/` the photo library. Cloud sessions are wiped when they end, so a photo only stays available
  to future sessions if it's committed here
- `out/` rendered PNGs (gitignored, just re-render)
- `fonts/` bundled Inter Display Bold (SIL Open Font License, see `fonts/OFL.txt`)

Set `CAROUSEL_FONT=/path/to/font.ttf` to force a different font.
