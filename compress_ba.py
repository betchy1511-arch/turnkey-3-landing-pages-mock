"""One-shot: compress oversized B/A pngs → jpgs at ~1400px max."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
from pathlib import Path

BA = Path(__file__).parent / "images-ba"
MAX_W = 1400
QUALITY = 82

# Heavy files to recompress to JPG. Smaller existing JPGs left alone.
TARGETS = [
    "p1-ba1-after.png",
    "p3-ba1-before.png",
    "p3-ba1-after.png",
    "p3-ba2-before.png",
    "p3-ba2-after.png",
]

for name in TARGETS:
    src = BA / name
    if not src.exists():
        print(f"  skip  {name} (missing)")
        continue
    out = src.with_suffix(".jpg")
    before = src.stat().st_size
    img = Image.open(src)
    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")
    if img.width > MAX_W:
        new_h = int(img.height * MAX_W / img.width)
        img = img.resize((MAX_W, new_h), Image.LANCZOS)
    img.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    after = out.stat().st_size
    # Remove original png so refs only point at jpg
    if src.suffix.lower() == ".png" and out.suffix.lower() == ".jpg":
        os.remove(src)
    print(f"  ok   {name} -> {out.name}  {before/1024/1024:.2f}MB -> {after/1024/1024:.2f}MB")

print("\nDone.")
