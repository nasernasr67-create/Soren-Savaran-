"""Generate Android launcher icons from icon-512.png into android/app/src/main/res."""
import os, shutil
from PIL import Image, ImageDraw

res = "android/app/src/main/res"
src = Image.open("icon-512.png").convert("RGB")
sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}

# remove adaptive-icon xml so the plain PNGs below are used
shutil.rmtree(os.path.join(res, "mipmap-anydpi-v26"), ignore_errors=True)

for d, s in sizes.items():
    folder = os.path.join(res, "mipmap-" + d)
    os.makedirs(folder, exist_ok=True)
    im = src.resize((s, s), Image.LANCZOS)
    im.save(os.path.join(folder, "ic_launcher.png"))
    im.save(os.path.join(folder, "ic_launcher_foreground.png"))
    # round version
    mask = Image.new("L", (s * 4, s * 4), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, s * 4 - 1, s * 4 - 1], fill=255)
    mask = mask.resize((s, s), Image.LANCZOS)
    out = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    out.save(os.path.join(folder, "ic_launcher_round.png"))
print("icons ok")
