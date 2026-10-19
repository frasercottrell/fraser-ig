---
name: carousel-designer
description: Designs and renders Fraser's Instagram carousel slides as finished 1080x1350 PNGs in the "blue caption bubble" style (candid BTS photo, white bold text in royal-blue rounded boxes, one box per line). Use whenever Fraser asks to "make the carousel", "design the slides", "generate the carousel", "build this carousel", "turn this into slides", or hands over carousel slide text and photos and wants images back. Also use when Fraser wants an existing carousel in posts/ rendered. This skill is for the visual slides only. For the caption under the carousel use carousel-captions, and for writing the slide copy itself follow context/carousels.md.
---

# Carousel designer

The renderer lives in `carousel-studio/`. Read `carousel-studio/README.md` once for the deck format.
This file is the workflow.

## 1. Get the slide text

- If it's a carousel already in `posts/carousel-*.md`, use the **FINAL** slides from that file and
  fix any typos it flags.
- If Fraser pastes new copy, use his words. Don't rewrite them unless asked. If Fraser asks you to write
  the copy too, follow `context/carousels.md` (slide 1 stops, slide 2 buys the swipe, max 8–10 slides).

## 2. Get the photos

The style only works with real photos. In order of preference:
1. Photos Fraser sends in this chat. Save them into `carousel-studio/photos/` with short descriptive
   names (`camera-rig-tight.jpg`).
2. Photos already in `carousel-studio/photos/`. List them and pick, or ask Fraser which.
3. Fraser's Google Drive, through the Drive connector if it's connected. Search for BTS / shoot folders and
   download into `photos/`.
4. None available: render with the placeholder so Fraser can approve the text and layout first, and say
   which slides still need a photo.

Never generate fake "real" photos with AI for this. The whole point is that it's Fraser's actual setup.
Photo rules from `context/carousels.md`: slide 1 = tight, legible, slightly unusual BTS frame
(camera / production stuff wins). Keep a recognisable location across the deck.

## 3. Write the deck

Create `carousel-studio/decks/<short-name>.txt`. Rules of thumb that keep it looking like the reference:

- **Cover:** one `## ` hook, optional `- ` subhead in brackets.
- **Content slides:** optional `# ` header, then 2–5 body lines. Each line is a beat, so split long
  sentences into two lines rather than one giant box.
- **One underline per block, max.** Pick the word that carries the meaning (`_deliberate_`).
- **CTA slide:** `bw: yes` + one `## ` line (follow, or the comment keyword).
- Bright or busy photo → `darken: 0.3`. Text sitting on a face → nudge `y:`.

## 4. Render and check

```
python3 carousel-studio/make_carousel.py carousel-studio/decks/<short-name>.txt
```

Then **look at `out/<short-name>/contact-sheet.jpg` yourself** (Read it) before sending anything.
Check for: text over a face or the key part of the photo, a slide so full it reads as a wall, orphan
words, an underline on the wrong word. Fix the deck and re-render.

## 5. Deliver

- Send the contact sheet plus the individual slide PNGs with SendUserFile (when that tool is
  available), so they save straight to a phone. Otherwise give the paths.
- Keep the message short: what's done, which slides still need photos, one question if any.
- Commit the deck file and any new photos (not `out/`, it's gitignored).
