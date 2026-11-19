#!/usr/bin/env python3
"""Builds the website's images, fonts and video from the sources in MULA/_src (run before build.py when they change).

    python3 -I MULA/_src/assets.py

Sources (all real app material):
  shots/en/*.webp     iPhone screenshots of the app (sample garden), 900 px wide
  watch/*.png         Apple Watch screenshots
  widgets/*.png       widget renders from the app's Debug widget renderer
  art/*-poster.jpg    the app's plant posters (photo above, cut-paper portrait below), app icon, Premium art
  texture/*.png       the app's paper grain and fibre tiles
  fonts/*.ttf         Cormorant Garamond, Lora, Jost (SIL OFL), the app's own fonts
  video/launch-master.mp4   screen recording of the app's launch intro running into Today
"""
import os, shutil, subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(SRC)
OUT = os.path.join(SITE, "assets")
PLANTS = ["camellia", "monstera", "ficus", "hydrangea", "orchid", "pilea"]


def out(*p):
    path = os.path.join(OUT, *p)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def webp(im, path, q=82):
    im.save(path, "WEBP", quality=q, method=6)


def fit_w(im, w):
    return im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)


def rounded_mask(size, r):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), r, fill=255)
    return m


# ---------------------------------------------------------------- screenshots
def patch_lightmeter(im):
    """The Debug build shows "Simulated reading" where a real iPhone shows the live camera.
    Put a softly blurred window-light plant photo there, as the camera would show it."""
    s = im.width / 900
    box = tuple(round(v * s) for v in (45, 270, 854, 942))
    w, h = box[2] - box[0], box[3] - box[1]
    photo = Image.open(os.path.join(SRC, "art", "monstera-poster.jpg")).convert("RGB")
    photo = photo.crop((0, 0, photo.width, photo.height // 2))
    k = max(w / photo.width, h / photo.height)
    photo = photo.resize((round(photo.width * k) + 1, round(photo.height * k) + 1), Image.LANCZOS)
    photo = photo.crop((0, 0, w, h)).filter(ImageFilter.GaussianBlur(10 * s))
    photo = Image.blend(photo, Image.new("RGB", photo.size, (236, 224, 206)), 0.18)
    d = ImageDraw.Draw(photo)
    cx, cy, r = w / 2, h / 2, 46 * s
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(255, 255, 255), width=max(2, round(2 * s)))
    d.ellipse((cx - 4 * s, cy - 4 * s, cx + 4 * s, cy + 4 * s), fill=(255, 255, 255))
    im.paste(photo, box[:2], rounded_mask((w, h), round(58 * s)))
    return im


def shots():
    d = os.path.join(SRC, "shots")
    for lang in sorted(os.listdir(d)):
        for f in sorted(os.listdir(os.path.join(d, lang))):
            key = f.rsplit(".", 1)[0]
            im = Image.open(os.path.join(d, lang, f)).convert("RGB")
            if key == "lightmeter":
                im = patch_lightmeter(im)
            for w in (360, 720):
                webp(fit_w(im, w), out("img", "shots", lang, f"{key}-{w}.webp"), 80 if w == 720 else 78)
    print("shots ok")


# ---------------------------------------------------------------- watch, widgets
def watch():
    font = None
    for p in ("/System/Library/Fonts/SFNS.ttf", "/System/Library/Fonts/Helvetica.ttc"):
        if os.path.exists(p):
            font = ImageFont.truetype(p, 30)
            try:
                font.set_variation_by_name("Semibold")
            except Exception:
                pass
            break
    for f in ("list", "soil"):
        im = Image.open(os.path.join(SRC, "watch", f + ".png")).convert("RGB")
        d = ImageDraw.Draw(im)
        d.rectangle((246, 24, 360, 66), fill=(0, 0, 0))  # the simulator's real clock -> 09:41
        d.text((347, 45), "09:41", font=font, fill=(255, 255, 255), anchor="rm")
        webp(im, out("img", "watch", f + ".webp"), 86)
    print("watch ok")


def widgets():
    for f in sorted(os.listdir(os.path.join(SRC, "widgets"))):
        im = Image.open(os.path.join(SRC, "widgets", f)).convert("RGBA")
        name = f.rsplit(".", 1)[0]
        if name.split("-")[0] in ("circle", "rect", "inline"):
            # Lock Screen widgets render white on black before iOS tints them: keep the light as alpha
            lum = im.convert("L")
            im = Image.new("RGBA", im.size, (255, 255, 255, 0))
            im.putalpha(lum)
        webp(im, out("img", "widgets", name + ".webp"), 84)
        if im.width > 600:
            webp(fit_w(im, im.width // 2), out("img", "widgets", name + "-half.webp"), 82)
    print("widgets ok")


# ---------------------------------------------------------------- plant art, icon, textures
def art():
    for p in PLANTS:
        im = Image.open(os.path.join(SRC, "art", f"{p}-poster.jpg")).convert("RGB")
        for w in (480, 900):
            webp(fit_w(im, w), out("img", "art", f"{p}-poster-{w}.webp"), 80)
        half = im.height // 2
        photo, geo = im.crop((0, 0, im.width, half)), im.crop((0, half, im.width, im.height))
        for w in (480, 960):
            webp(fit_w(photo, w), out("img", "art", f"{p}-photo-{w}.webp"), 80)
            webp(fit_w(geo, w), out("img", "art", f"{p}-geo-{w}.webp"), 82)
    hero = Image.open(os.path.join(SRC, "art", "premium-hero.jpg")).convert("RGB")
    for w in (800, 1400):
        webp(fit_w(hero, w), out("img", "art", f"premium-{w}.webp"), 80)

    icon = Image.open(os.path.join(SRC, "art", "appicon.png")).convert("RGB")
    for s in (128, 256, 512):
        ic = icon.resize((s, s), Image.LANCZOS)
        mask = rounded_mask((s, s), round(s * 0.225))
        rgba = ic.convert("RGBA")
        rgba.putalpha(mask)
        webp(rgba, out("img", f"app-icon-{s}.webp"), 86)
    icon.resize((512, 512), Image.LANCZOS).save(out("icon-512.png"), optimize=True)
    icon.resize((180, 180), Image.LANCZOS).save(out("apple-touch-icon.png"), optimize=True)
    icon.resize((32, 32), Image.LANCZOS).save(out("favicon-32.png"), optimize=True)
    icon.resize((48, 48), Image.LANCZOS).save(out("favicon-48.png"), optimize=True)

    # the app softens its grain (PaperStrength); the web pages use it at about 40-55 %
    for f, name, k in (("grain.png", "paper", .42), ("grain-dark.png", "paper-dark", .55), ("fiber.png", "fiber", 1)):
        im = Image.open(os.path.join(SRC, "texture", f)).convert("RGBA")
        im.putalpha(im.getchannel("A").point(lambda a: round(a * k)))
        webp(im, out("img", name + ".webp"), 70)
    print("art ok")


# ---------------------------------------------------------------- fonts
FONTS = {
    "CormorantGaramond-MediumItalic.ttf": "cormorant-medium-italic.woff2",
    "CormorantGaramond-SemiBold.ttf": "cormorant-semibold.woff2",
    "Lora-Regular.ttf": "lora-regular.woff2",
    "Lora-Medium.ttf": "lora-medium.woff2",
    "Jost-Regular.ttf": "jost-regular.woff2",
    "Jost-Medium.ttf": "jost-medium.woff2",
}
# Latin, Latin-1, Latin Extended-A (Turkish ğ ı İ ş, Spanish ñ á é …), general punctuation, arrows, °, ·, €, ™
UNICODES = "U+0000-00FF,U+0100-017F,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2190-2193,U+2212,U+2215,U+FEFF,U+FFFD"


def fonts():
    for src, dst in FONTS.items():
        subprocess.run(["python3", "-I", "-m", "fontTools.subset", os.path.join(SRC, "fonts", src),
                        f"--unicodes={UNICODES}", "--flavor=woff2", "--layout-features=*",
                        f"--output-file={out('fonts', dst)}"], check=True)
    for f in os.listdir(os.path.join(SRC, "fonts")):
        if f.startswith("OFL"):
            shutil.copy(os.path.join(SRC, "fonts", f), out("fonts", f))
    print("fonts ok")


# ---------------------------------------------------------------- launch video
def video():
    master = os.path.join(SRC, "video", "launch-master.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", master, "-vf", "scale=540:-2", "-c:v", "libx264", "-crf", "25",
                    "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", out("video", "launch.mp4")], check=True)
    # poster = the finished emblem with the wordmark, just before the page fades into Today
    tmp = out("video", "_poster.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "3.1", "-i", master, "-frames:v", "1", tmp], check=True)
    im = Image.open(tmp).convert("RGB")
    webp(fit_w(im, 540), out("video", "launch-poster.webp"), 80)
    webp(fit_w(im, 720), out("img", "shots", "en", "launch-720.webp"), 80)
    webp(fit_w(im, 360), out("img", "shots", "en", "launch-360.webp"), 78)
    os.remove(tmp)
    print("video ok")


if __name__ == "__main__":
    shots()
    watch()
    widgets()
    art()
    fonts()
    video()
