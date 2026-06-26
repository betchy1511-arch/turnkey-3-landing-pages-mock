"""
Download finished-bath photos from Dimi's Google Drive folder, convert HEIC -> JPG,
save into the mock repo's images/ folder.

Filters out tiny thumbnails (<70KB) and skips the 'Customer name' subfolder
per Beth's instruction (Jun 26, 2026).
"""
import os
import sys
import io
import shutil
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

import gdown
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()

REPO = Path(r"C:\Users\betch\Documents\turnkey-3-landing-pages-mock")
SRC_DIR = REPO / "images-source-heic"
OUT_DIR = REPO / "images-finished-bath"
SRC_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)

# Files >70KB from the 'Finished bath' folder (skipping screenshots + art).
# (file_id, title, sizeBytes, mime)
FILES = [
    ("1gMROSIc-6UKFYSyF-ePCIZ2UNimmH1cW", "PHOTO-2023-11-14-12-50-53_a.heic", 82589, "heic"),
    ("1yiX35YwVVlZfcEH7cUH-Jqcz-yCWTaXs", "PHOTO-2023-11-14-12-50-49_a.heic", 112945, "heic"),
    ("1F_wrPiteEGFNrMRKtrYMgoV143yA0Ztj", "PHOTO-2023-11-14-12-50-49_b.heic", 114565, "heic"),
    ("1KK5s99l5LyFC26SjkfzPWQJtW2PGo3HI", "IMG_3187.heic", 182895, "heic"),
    ("1J7GOGoGv__-j92SqY4ZxUQdh9qZjnFsD", "IMG_3184.heic", 84182, "heic"),
    ("14kpUFY3miQk578A9v7z_82PhcIZDBQ_t", "PHOTO-2023-11-14-12-51-00_a.heic", 85321, "heic"),
    ("1Wsyy2FK6UmOofCF7DCY9sU8Tg74wp8VG", "PHOTO-2023-11-14-12-50-44.heic", 89624, "heic"),
    ("19t2k4CWcVnjdVvt9i6WN3wwnhHqS2hLg", "PHOTO-2023-11-14-12-51-02.heic", 78337, "heic"),
    ("17b4kj1uFdPsiMVIEvNYK2fgOgklaE3vU", "PHOTO-2023-11-14-12-50-27.heic", 94864, "heic"),
    ("1S4lOduxum65ImhVO9B5heQRYG46N2C7F", "PHOTO-2023-11-14-12-50-22_a.heic", 86663, "heic"),
    ("1gfZ8znLqsODbVxso3V0MIVtWJqkrI162", "PHOTO-2023-11-14-12-51-01_a.heic", 92082, "heic"),
    ("1s4mpYtvpvMkP6JPRiDP6gqM2vpJYMx5m", "PHOTO-2023-11-14-12-50-50_a.heic", 131867, "heic"),
    ("15ndM00uUpCjX7hd9jSTbfkqlsKeI-sKb", "IMG_4687.PNG", 4358186, "png"),
    ("1ImfX5tC_RkjniJpqtnB-KzbXZuxuvmEJ", "PHOTO-2023-11-14-12-50-48.heic", 74297, "heic"),
    ("1FVQ82UtJ3BVc9mI9457qIWJiPt69UM98", "PHOTO-2023-11-14-12-51-00_b.heic", 103361, "heic"),
    ("1LfSPzfuoiUamj_BaI3aynLF92Iz-1aZJ", "IMG_3186.heic", 197162, "heic"),
    ("1AyNkivfiNf9pzCU7htHTrFo_SLuLAOGz", "PHOTO-2023-11-14-12-50-50_b.heic", 114708, "heic"),
    ("1FtDkEIErySsTjsmP_jffC8pOAHWnNm7a", "PHOTO-2023-11-14-12-50-50_c.heic", 75543, "heic"),
    ("1MLniBz15IhGbVdn8Gv0ArVtOp7oF8QVM", "PHOTO-2023-11-14-12-51-01_b.heic", 90665, "heic"),
    ("1MgF6xmhkHHvnjDL9b3Af11bbMsCpiAeo", "PHOTO-2023-11-14-12-50-49_c.heic", 99280, "heic"),
    ("1cOD6QJDiuWC-Z0_5sZ9fPV9dzayfBqn3", "PHOTO-2023-11-14-12-51-01_c.heic", 106129, "heic"),
    ("1TLWpPTyIiTkka3eaSVZh0YpMxoEBllJb", "PHOTO-2023-11-14-12-51-01_d.heic", 92603, "heic"),
    ("1ROuuDa7BgYkk23E7h9cubKTVamM1sHnU", "PHOTO-2023-11-14-12-50-28.heic", 97172, "heic"),
    ("10k7n7nBeYbM0d8kyOHLbcyw8c8Ldz5ks", "PHOTO-2023-11-14-12-51-01_e.heic", 114366, "heic"),
]

print(f"[plan] {len(FILES)} files to download + convert")
print(f"[paths] src={SRC_DIR}  out={OUT_DIR}\n")

# 1. Download
downloaded = []
for fid, title, size, kind in FILES:
    src_path = SRC_DIR / title
    if src_path.exists() and src_path.stat().st_size > 1000:
        print(f"[skip-dl] {title} (already on disk)")
        downloaded.append((src_path, title, kind))
        continue
    url = f"https://drive.google.com/uc?id={fid}"
    try:
        gdown.download(url, str(src_path), quiet=True)
        print(f"[dl] {title} ({size/1024:.0f} KB)")
        downloaded.append((src_path, title, kind))
    except Exception as e:
        print(f"[ERR-dl] {title}: {e}")

print(f"\n[downloaded] {len(downloaded)}/{len(FILES)}")

# 2. Convert HEIC -> JPG (1600px max wide, q=85), copy PNG as-is but re-encode to JPG
print("\n[converting]")
converted = []
for src_path, title, kind in downloaded:
    stem = Path(title).stem
    out_path = OUT_DIR / f"{stem}.jpg"
    try:
        img = Image.open(src_path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        # Resize if huge
        max_w = 1600
        if img.width > max_w:
            ratio = max_w / img.width
            new_h = int(img.height * ratio)
            img = img.resize((max_w, new_h), Image.LANCZOS)
        img.save(out_path, "JPEG", quality=85, optimize=True)
        converted.append((out_path, img.size))
        print(f"[ok] {out_path.name}  {img.size[0]}x{img.size[1]}  {out_path.stat().st_size/1024:.0f} KB")
    except Exception as e:
        print(f"[ERR-conv] {title}: {e}")

print(f"\n[done] {len(converted)} JPGs in {OUT_DIR}")
