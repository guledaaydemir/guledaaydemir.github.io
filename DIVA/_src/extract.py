#!/usr/bin/env python3
"""Pull DIVA's real catalog, art and voice clips from the app repo into the website.

Run from anywhere:
    python3 DIVA/_src/extract.py [--app /Users/guledaaydemir/DIVA] [--photos <folder of 1.webp..20.webp>]

Writes:
    _src/data/app.json          catalog subset the page builder reads (EN + TR text)
    assets/covers/*.webp        CD covers (from the app's asset catalog)
    assets/img/*.webp           mood photos + app backdrops/textures
    assets/audio/*.m4a          demo clips cut from the app's studio voice packs
    assets/audio/demo.json      line timings for the karaoke demo
    assets/logo*.{webp,png}, favicon / touch icons
This folder starts with "_" so GitHub Pages (Jekyll) never publishes it.
"""
import argparse, hashlib, json, os, subprocess, tempfile, unicodedata, wave, struct

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../DIVA
SRC = os.path.join(SITE, "_src")

DEMO = {  # cd id -> catalog line indexes (intro is always first)
    "that_girl_energy": [3, 4, 6, 10],
    "rich_girl_frequency": [3, 6, 8, 9],
    "beauty_sleep_for_divas": [3, 4, 9, 11],
}
AUDIO_LANGS = ["en"]  # Turkish narration is paused in the app (2026-11-14), so the demo is English only
VOICES = ["velvet_whisper", "pink_muse", "runway_confidence", "after_dark"]
VOICE_FILE = {"runway_confidence": "runway_confidence"}

# Provided mood photos (1..20). 15 (car badge) and 17 (collage with a fashion-house logo) are left out.
PHOTOS = {
    1: "money-bag", 2: "vanity-roses", 3: "vanity-tray", 4: "pink-closet", 5: "diamond-bust",
    6: "walk-in-closet", 7: "skincare-satin", 8: "ceo-desk", 9: "gym-bag-coins", 10: "first-class-window",
    11: "penthouse-lounge", 12: "rhinestone-gym", 13: "rooftop-party", 14: "jet-set", 16: "poolside-muse",
    18: "lily-vanity", 19: "dream-body-neon", 20: "pilates-pink",
}
APP_ART = ["hero_muse", "backdrop_sunset", "backdrop_palms", "texture_leopard_pink", "texture_leopard_gold",
           "art_leopard_cd", "art_lips_star"]


def run(*cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def art_file(app, name):
    folder = os.path.join(app, "DIVA/Assets.xcassets/Art", name + ".imageset")
    for f in os.listdir(folder):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            return os.path.join(folder, f)
    raise FileNotFoundError(name)


def clip_key(text):
    return hashlib.sha256(unicodedata.normalize("NFC", text.strip()).encode("utf-8")).hexdigest()


def cut_lines(app, voice, lang, texts, out_m4a):
    """Cut each line from the voice pack, join with pauses, return line timings in seconds."""
    base = os.path.join(app, "DIVA/Resources/VoicePacks", f"voicepack_{voice}_{lang}")
    index = json.load(open(base + ".json"))
    rate = index["sampleRate"]
    gap, lead = 1.25, 0.6
    timings, pcm = [], bytearray()
    pcm += b"\x00\x00" * int(lead * rate)
    with tempfile.TemporaryDirectory() as tmp:
        for i, text in enumerate(texts):
            clip = index["clips"].get(clip_key(text))
            if clip is None:
                raise KeyError(f"{voice}/{lang}: no clip for {text!r}")
            wav = os.path.join(tmp, f"{i}.wav")
            pad = int(0.04 * rate)
            start = max(0, clip["start"] - pad)
            n = clip["length"] + 2 * pad
            run("ffmpeg", "-y", "-ss", f"{start / rate:.6f}", "-i", base + ".m4a", "-t", f"{n / rate:.6f}",
                "-af", "afade=t=in:d=0.02,areverse,afade=t=in:d=0.04,areverse", "-ac", "1", "-ar", str(rate),
                "-sample_fmt", "s16", wav)
            with wave.open(wav) as w:
                frames = w.readframes(w.getnframes())
            t0 = len(pcm) / 2 / rate
            pcm += frames
            timings.append([round(t0, 2), round(len(pcm) / 2 / rate, 2)])
            pcm += b"\x00\x00" * int((gap if i else gap + 0.35) * rate)
        joined = os.path.join(tmp, "all.wav")
        with wave.open(joined, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(bytes(pcm))
        run("ffmpeg", "-y", "-i", joined, "-c:a", "aac", "-b:a", "56k", "-movflags", "+faststart", out_m4a)
    return timings, round(len(pcm) / 2 / rate, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default="/Users/guledaaydemir/DIVA")
    ap.add_argument("--photos", default=None, help="folder with the 1.webp..20.webp mood photos")
    ap.add_argument("--skip-audio", action="store_true")
    a = ap.parse_args()
    app = a.app
    cat = json.load(open(os.path.join(app, "DIVA/Resources/ContentCatalog/seed_catalog.json")))

    # ---- catalog subset ----
    data = {"categories": [], "cds": [], "rituals": {}, "lines": {}, "demo": {}}
    for c in cat["categories"]:
        data["categories"].append({"id": c["id"], "title": c["title"]})
    for c in cat["cds"]:
        loc = c["localizations"]
        data["cds"].append({
            "id": c["id"], "category": c["categoryId"], "pro": c["isPremium"], "mood": c.get("mood"),
            "cover": c["cover"]["art"], "aura": c.get("defaultSoundscapeId"),
            **{L: {"title": loc[L]["title"], "subtitle": loc[L]["subtitle"], "summary": loc[L]["summary"]}
               for L in ("en", "tr")},
        })
        data["lines"][c["id"]] = {L: loc[L]["lines"] for L in ("en", "tr")}
    for r in cat["rituals"]:
        data["rituals"][r["kind"]] = {L: {"title": r["localizations"][L]["title"],
                                          "subtitle": r["localizations"][L]["subtitle"],
                                          "days": [d["theme"] for d in r["localizations"][L]["days"]],
                                          "intentions": [d["intention"] for d in r["localizations"][L]["days"]]}
                                      for L in ("en", "tr")}

    # ---- demo audio ----
    audio_dir = os.path.join(SITE, "assets/audio")
    demo_meta = {}
    for cd_id, idx in DEMO.items():
        c = next(x for x in cat["cds"] if x["id"] == cd_id)
        for L in ("en", "tr"):
            loc = c["localizations"][L]
            texts = [loc["intro"]] + [loc["lines"][i] for i in idx]
            data["demo"].setdefault(cd_id, {})[L] = texts
            if L not in AUDIO_LANGS:  # text kept as the on-page translation
                continue
            for v in VOICES:
                name = f"{cd_id}-{v}-{L}.m4a"
                if a.skip_audio and os.path.exists(os.path.join(audio_dir, name)):
                    continue
                timings, total = cut_lines(app, v, L, texts, os.path.join(audio_dir, name))
                demo_meta[f"{cd_id}/{v}/{L}"] = {"src": name, "t": timings, "d": total}
                print("audio", name, total, "s")
    if demo_meta:
        json.dump(demo_meta, open(os.path.join(audio_dir, "demo.json"), "w"), separators=(",", ":"))

    json.dump(data, open(os.path.join(SRC, "data/app.json"), "w"), ensure_ascii=False, indent=1)

    # ---- covers ----
    for c in cat["cds"]:
        src = art_file(app, c["cover"]["art"])
        out = os.path.join(SITE, "assets/covers", c["cover"]["art"].replace("cover_", "").replace("_", "-") + ".webp")
        run("magick", src, "-resize", "480x480^", "-gravity", "center", "-extent", "480x480", "-quality", "80", out)
    for r in ("backdrop_sunset", "cover_sleep"):
        pass

    # ---- app art ----
    for name in APP_ART:
        src = art_file(app, name)
        out = os.path.join(SITE, "assets/img", name.replace("_", "-") + ".webp")
        run("magick", src, "-resize", "800x>", "-quality", "78", out)

    # ---- mood photos ----
    if a.photos:
        for n, slug in PHOTOS.items():
            src = os.path.join(a.photos, f"{n}.webp")
            for w in (640, 1200):
                out = os.path.join(SITE, "assets/img", f"{slug}-{w}.webp")
                run("magick", src, "-resize", f"{w}x{w}>", "-quality", "76", out)

    # ---- logo + icons ----
    logo = art_file(app, "diva_logo")
    run("magick", logo, "-resize", "920x", "-quality", "88", "-define", "webp:alpha-quality=95", os.path.join(SITE, "assets/logo.webp"))
    run("magick", logo, "-resize", "460x", os.path.join(SITE, "assets/logo-460.png"))
    icon = os.path.join(app, "DIVA/Assets.xcassets/AppIcon.appiconset/AppIcon.png")
    for size, name in ((32, "favicon-32.png"), (180, "apple-touch-icon.png"), (512, "icon-512.png")):
        run("magick", icon, "-resize", f"{size}x{size}", os.path.join(SITE, "assets", name))
    print("done")


if __name__ == "__main__":
    main()
