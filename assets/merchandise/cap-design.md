---
layout: default
title: Cap design notes
permalink: /branding/cap-design/
description: "Working notes on translating the MKFC mark to embroidered caps."
---

# Cap design notes

Working notes for translating the MKFC mark onto a **royal blue cap** (royal blue `#013087`, Pantone 286 C). Supplements the main [Branding](/branding/) guide — refer there for the canonical palette, typography, and logo rules.

## Colour translation for a royal blue cap

The full-colour logo is built for light backgrounds. On a royal blue cap the royal blue of the cap *is* the brand colour, so the colour roles invert:

| Element on the original logo | Render on a royal blue cap |
|---|---|
| Brand royal blue `#013087` (kangaroo outlines, shield panels) | **White** — this becomes the main visible mark |
| White (kangaroo body, shield centre panel) | **Light blue `#C8D6F0`** — subtle fill |
| Silver shield bevel | Drop to **royal blue** (cap colour) — the 3D bevel does not embroider cleanly |
| Background | Cap royal blue |

Result: the kangaroo silhouette reads in white, the shield reads as a light-blue silhouette behind it, and the cap itself supplies the royal blue. **Three colours total** (royal blue, white, light blue) — the right ceiling for clean embroidery.

## Layout and proportions

- Cap front panel target is roughly **4.5″ × 2.25″ (60mm × 30mm)** — about a **2:1 to 2.4:1** aspect ratio. Design the artwork to that horizontal ratio rather than the square brand mark.
- The brand guide minimum embroidery width is **60mm**; do not go smaller.
- Two viable layouts:
  1. **Crest left + wordmark right** — kangaroo+shield on the left, "MOORABBIN KANGAROOS" white text on the right. Single line if width allows; otherwise stacked over two lines.
  2. **Split-script wordmark only** — small "MOORABBIN" above large "KANGAROOS" (or "KANGAS"); the bottom line uses the bold italic split-script style (white outline, top half blank/cap-colour, bottom half solid white). No crest. Use this when the embroiderer can do a clean two-tone fill on bold condensed letters.
- For very small placements (cap side, strap), drop the wordmark and use the kangaroo silhouette only.

## Supplying artwork to the embroiderer

- **Always provide a vector file** (SVG, AI, or EPS) where possible. Embroiderers digitise from vectors; raster (PNG/JPG) forces them to trace and introduces drift.
- If only raster is available, supply at **300 dpi or higher** at the final stitched size.
- Specify thread colours by Pantone where the supplier supports it: royal blue = **Pantone 286 C**, light blue = closest match to `#C8D6F0`, white = pure `#FFFFFF`. Madeira / Robison-Anton equivalents are acceptable.
- Embroidery cannot reproduce gradients, drop shadows, or the silver shield bevel — flatten these out before sending.
- Letter strokes and outlines below ~1.2mm at final size will not stitch cleanly. Keep outlines bold.

## Don't

- Don't keep the original blue-on-white colour scheme on a royal blue cap — the brand blue is too close to the cap colour and the mark disappears.
- Don't add a coloured "patch" background behind the logo that breaks the cap colour. The cap *is* the background.
- Don't introduce off-palette blues (navy, teal, sky) when matching threads; stick to the documented royal, mid, and light blues from the [Branding](/branding/) guide.

## Reference files

Generated cap-ready artwork (in repo root):

- `mkfc-cap-logo.png` / `.jpg` — crest-left + two-line wordmark
- `mkfc-cap-logo-split.png` / `.jpg` — split-script wordmark only ("MOORABBIN" / "KANGAROOS")

Generator scripts (`make_cap_logo.py`, `make_cap_logo_split.py`) sit next to the artwork; tweak colours, ratio, or font and re-run. Note: these reference files were generated against the previous deep-navy palette and will need regenerating to match the current royal blue palette.
