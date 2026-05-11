---
layout: default
title: Cap Merchandise Spec
description: "Procurement and design spec for MKFC branded baseball caps."
---

# Cap Merchandise — Procurement & Design Spec

Working document for the MKFC branded baseball cap run. Captures product selection, design brief, and supplier details so the committee has a single reference before placing the order.

## Reference / Inspiration

North Melbourne Kangaroos "Split Script" Cap — New Era 9FORTY style, royal blue, white embroidered wordmark in bold italic.

- Reference product: <https://shop.nmfc.com.au/kangaroos-split-script-cap-kids-updating/>

MKFC is mirroring the visual style (royal blue + bold italic white wordmark), not the licensed NMFC product.

## Product

| Spec | Value |
|---|---|
| Supplier | Vistaprint Australia |
| Product | 6-Panel Baseball Cap (embroidered) |
| Product URL | <https://www.vistaprint.com.au/clothing-bags/hats/caps/vistaprint-6-panel-baseball-cap> |
| Colour | Royal Blue |
| Construction | 6-panel structured, 100% brushed cotton |
| Closure | Adjustable strap, one-size-fits-most |
| Decoration | Front-centre embroidery, single thread colour (white) |
| Embroidery size | 60 mm wide × 20 mm tall (3:1 horizontal aspect) |

### Notes on the colour choice

The MKFC brand guide was updated on 2026-05-11 to adopt Royal Blue (Pantone 286 C) as the primary colour, aligning with the AFL North Melbourne palette. The Vistaprint Royal Blue cap is now consistent with the brand guide rather than a one-off divergence.

**Reference Pantone 286 C, not the HEX, when communicating with the supplier.** Vistaprint's "Royal Blue" cap stock is a fixed inventory colour — they won't dye to spec — so the goal is to confirm their Royal Blue is the closest available match to Pantone 286 C. Ask Vistaprint (or any cap supplier) which Pantone number their Royal Blue stock corresponds to before placing the order; if it's materially different from 286 C, escalate to the committee before proceeding.

Note that NMFC's product photos render their cap shell at roughly `#0052AB` (a brighter, more vibrant blue) — this is a photographic artefact of studio lighting and compression, not a different brand colour. The physical fabric is dyed to Pantone 286 C.

## Final Wordmark

Approved 2026-05-11. Two-line stacked wordmark, designed for embroidery in white on the royal blue cap.

| Line | Text | Style |
|---|---|---|
| Top | MOORABBIN | **Bold upright** (non-italic) bold condensed sans-serif, uppercase, tracked to span the wordmark width. |
| Top right superscript | TM | Trademark mark, retained at committee request. |
| Bottom | KANGAS | **Bold italic** bold condensed sans-serif, uppercase, ~12° slant. Reference: NMFC "KANGAROOS" wordmark. |

Both lines roughly equal height and weight; the italic slant on KANGAS provides the visual contrast and AFL feel. Embroidery thread: single colour, pure white. The royal blue background visible in the artwork is for visualisation only — the cap shell supplies the blue.

### Artwork files

Stored in [`assets/merchandise/cap-artwork/`](/assets/merchandise/cap-artwork/) within this repo so they're persistent (the Canva pre-signed export URLs expire).

| File | Use |
|---|---|
| [`mkfc-cap-wordmark.pdf`](/assets/merchandise/cap-artwork/mkfc-cap-wordmark.pdf) | Send to Vistaprint / embroiderer — preferred format for digitisation. |
| [`mkfc-cap-wordmark.png`](/assets/merchandise/cap-artwork/mkfc-cap-wordmark.png) | 2000 × 2000 raster — visual reference and committee approval copy. |

Source Canva design (editable): <https://www.canva.com/d/gvWP-PJsl91xWY7> (design ID `DAHJWNy-oHs`).

### Embroidery considerations

- Single thread colour (pure white) keeps digitising simple and unit cost down.
- The strokes on bold italic letterforms — "K", "A", "G" — must be inspected on the digitised proof; counters can fill in if the stitch density is too high.
- Request a digital proof from Vistaprint **before** they run the batch.
- Vistaprint thread colours are approximate, not Pantone-matched — the white is unambiguous, the cap shell is the only colour where this matters.

## Next Steps

1. Order **one sample cap** from Vistaprint at the agreed spec — Royal Blue, ~60 × 20 mm white embroidery, using `mkfc-cap-wordmark.pdf`.
2. Confirm with Vistaprint which Pantone their Royal Blue stock corresponds to; flag to committee if it diverges materially from Pantone 286 C.
3. Inspect the sample for embroidery quality, thread weight, and letterform integrity at small size.
4. If sample approved, model pricing at 25 / 50 / 100 break points and place the bulk order.

## Decision Log

- **2026-05-11** — Initial spec drafted. Royal Blue selected to match NMFC visual reference. Two-line "MOORABBIN / KANGAS" stacked wordmark chosen, bold italic on bottom line.
- **2026-05-11** — MKFC brand guide updated to adopt Royal Blue (`#013087`, Pantone 286 C) as the primary colour. Cap colour now aligns with the brand guide rather than diverging from it.
- **2026-05-11** — Final wordmark approved and exported. MOORABBIN set upright bold; KANGAS bold italic; TM superscript retained. Artwork committed to `assets/merchandise/cap-artwork/`.
