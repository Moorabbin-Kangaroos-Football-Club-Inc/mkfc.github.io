"""
Generate cap-ready versions of the MKFC logo.

Outputs (all on navy #01285E):
  mkfc-cap-logo.png           - shield + kangaroo on left, single-line text right
  mkfc-cap-logo-kangaroo.png  - kangaroo only + text (cleaner for embroidery)

Colour mapping for the navy cap:
  - Brand blue (kangaroo outlines, shield panels) -> WHITE  (the main mark)
  - Inside-white (kangaroo body, shield centre)   -> LIGHT BLUE  (#C4D1E5)
  - Silver shield bevel                            -> NAVY  (drops away)
  - Background                                     -> NAVY
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np

SRC = "mkfc-logo-cap.jpg"

NAVY = (1, 40, 94)
LIGHT_BLUE = (196, 209, 229)
WHITE = (255, 255, 255)

FONT_PATH = "/usr/share/fonts/opentype/urw-base35/NimbusSansNarrow-Bold.otf"


def recolor_shield(crop_arr):
    """Return an RGB array with the brand recolouring applied."""
    h, w, _ = crop_arr.shape
    r, g, b = crop_arr[..., 0], crop_arr[..., 1], crop_arr[..., 2]

    # Generous blue match (catches antialiased edges too)
    is_blue = (b.astype(int) - r.astype(int) > 30) & (b > 90) & (r < 140)
    is_white = (r > 215) & (g > 215) & (b > 215)

    # Outside-vs-inside white via flood fill from the corner
    mask = Image.fromarray((is_white.astype(np.uint8) * 255))
    ImageDraw.floodfill(mask, (0, 0), 128)
    flood = np.array(mask)
    is_outside_white = (flood == 128)
    is_inside_white = is_white & ~is_outside_white

    out = np.zeros_like(crop_arr)
    out[..., 0] = NAVY[0]
    out[..., 1] = NAVY[1]
    out[..., 2] = NAVY[2]
    # Default unclassified-inside pixels (silver bevel + JPEG noise) to LIGHT
    # BLUE so we don't leave navy specks inside the shield.
    is_inside = ~is_outside_white
    out[is_inside] = LIGHT_BLUE
    out[is_blue] = WHITE
    return out


def fit_font(text, max_w, max_h, font_path):
    lo, hi, best = 20, 800, 20
    while lo <= hi:
        mid = (lo + hi) // 2
        f = ImageFont.truetype(font_path, mid)
        bbox = f.getbbox(text)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if tw <= max_w and th <= max_h:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return best


def compose(shield_img, out_path, target_w=2400, target_h=1000, pad=30,
            shield_frac=0.42):
    """Shield on left taking shield_frac of width; text fills the rest."""
    canvas = Image.new("RGB", (target_w, target_h), NAVY)
    shield_max_w = int(target_w * shield_frac) - pad
    shield_max_h = target_h - 2 * pad
    scale = min(shield_max_w / shield_img.width,
                shield_max_h / shield_img.height)
    sw, sh = int(shield_img.width * scale), int(shield_img.height * scale)
    shield_resized = shield_img.resize((sw, sh), Image.LANCZOS)
    sx = pad + (shield_max_w - sw) // 2
    sy = (target_h - sh) // 2
    canvas.paste(shield_resized, (sx, sy))

    lines = ["MOORABBIN", "KANGAROOS"]
    text_x0 = pad + shield_max_w + 60
    text_w = target_w - text_x0 - pad
    # Each line gets ~45% of canvas height so both fit with a small gap.
    line_h_max = int(target_h * 0.42)
    fs_per_line = min(fit_font(t, text_w, line_h_max, FONT_PATH) for t in lines)
    font = ImageFont.truetype(FONT_PATH, fs_per_line)

    bboxes = [font.getbbox(t) for t in lines]
    heights = [b[3] - b[1] for b in bboxes]
    line_gap = int(fs_per_line * 0.10)
    block_h = sum(heights) + line_gap
    y_cursor = (target_h - block_h) // 2
    draw = ImageDraw.Draw(canvas)
    for line, b, h in zip(lines, bboxes, heights):
        tw = b[2] - b[0]
        tx = text_x0 + (text_w - tw) // 2
        draw.text((tx, y_cursor - b[1]), line, fill=WHITE, font=font)
        y_cursor += h + line_gap
    font_size = fs_per_line

    canvas.save(out_path + ".png", "PNG")
    canvas.save(out_path + ".jpg", "JPEG", quality=95)
    return font_size


# Load + crop shield region (above the original two-line text)
img = Image.open(SRC).convert("RGB")
arr = np.array(img)
shield_crop = arr[38:1235, 39:1205].copy()

shield_recolored = recolor_shield(shield_crop)
shield_img = Image.fromarray(shield_recolored)

fs = compose(shield_img, "mkfc-cap-logo")
print(f"mkfc-cap-logo: font {fs}px")
