#!/usr/bin/env python3
"""Copies the game's own art, screenshots and App Preview videos into HANE/assets, web-sized.

    python3 -I HANE/_src/assets.py            # images, icons, social cards
    python3 -I HANE/_src/assets.py --video    # also re-encode the App Preview videos (needs ffmpeg)

Source: the HANE Unity project (GAME below). Run it again whenever the game's art or screenshots change;
build.py only reads what this script wrote.
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(SRC)
OUT = os.path.join(SITE, "assets")
GAME = os.path.expanduser("~/HANE")
ART = os.path.join(GAME, "Assets/_Hane/Art")
SPR = os.path.join(ART, "Sprites")
STORE = os.path.join(GAME, "docs/app-store")
FONT = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"

ILLUSTRATIONS = {  # key -> file in Sprites/Illustrations
    "welcome": "illustration_welcome", "dream": "illustration_dream", "market": "illustration_market",
    "opening": "illustration_opening", "quarrel": "illustration_quarrel", "cat": "illustration_cat",
    "inspection": "illustration_inspection", "intro_goal": "intro_goal", "intro_order": "intro_order",
    "intro_serve": "intro_serve", "intro_bill": "intro_bill", "intro_games": "intro_games",
    "intro_incidents": "intro_incidents", "map": "map_turkiye",
}
SHOTS = {  # key -> file in screenshots/source/iphone-<lang>; missing ones fall back to English
    "room": "01_room", "cat": "02_cat", "map": "03_map", "quarrel": "04_quarrel", "ribbon": "05_ribbon",
    "dream": "06_dream", "staff": "07_staff", "welcome": "08_welcome", "ribbon_cut": "extra_ribbon_cut",
    "upgrades": "extra_upgrades", "games": "extra_games", "lshaped": "extra_lshaped_branch",
    "cat_mirmir": "extra_cat_mirmir",
}
SPRITES = {  # name -> (path under Sprites, height in px)
    # people (the demo and the character cards)
    "cirak": ("Characters/char_cirak", 220), "cirak_walk_a": ("Characters/char_cirak_walk_a", 220),
    "cirak_walk_b": ("Characters/char_cirak_walk_b", 220), "cirak_carry": ("Characters/char_cirak_carry", 220),
    "cirak_carry_walk_a": ("Characters/char_cirak_carry_walk_a", 220),
    "cirak_carry_walk_b": ("Characters/char_cirak_carry_walk_b", 220), "cirak_work": ("Characters/char_cirak_work", 220),
    "cirak_water": ("Characters/char_cirak_water", 220),
    "usta": ("Characters/char_usta", 220), "usta_work": ("Characters/char_usta_work", 220),
    "waiter": ("Characters/char_waiter", 220), "zabita": ("Characters/char_zabita", 220),
    "guest_1": ("Characters/char_guest_1", 220), "guest_2": ("Characters/char_guest_2", 220),
    "guest_3": ("Characters/char_guest_3", 220), "guest_4": ("Characters/char_guest_4", 220),
    "guest_5": ("Characters/char_guest_5", 220), "guest_6": ("Characters/char_guest_6", 220),
    "guest_boy": ("Characters/char_guest_boy", 200),
    **{f"guest_{i}_sit": (f"Characters/char_guest_{i}_sit", 200) for i in range(1, 7)},
    **{f"cat_{c}": (f"Characters/char_cat_{c}", 160) for c in ("mirmir", "pamuk", "aslan", "tekir", "karagoz")},
    **{f"cat_{c}_sitting": (f"Characters/char_cat_{c}_sitting", 160) for c in ("mirmir", "pamuk", "aslan", "tekir", "karagoz")},
    # drinks, food, equipment, games
    "tea_strong": ("Drinks/tea_strong", 160), "tea_light": ("Drinks/tea_light", 160),
    "turkish_coffee": ("Drinks/turkish_coffee", 160), "water": ("Drinks/water_glass", 160),
    "oralet_orange": ("Drinks/oralet_orange", 160), "oralet_lemon": ("Drinks/oralet_lemon", 160),
    "oralet_rosehip": ("Drinks/oralet_rosehip", 160), "oralet_cherry": ("Drinks/oralet_cherry", 160),
    "toast": ("Drinks/tost_cheese", 160), "empty_tea": ("Drinks/empty_tea", 120),
    "caydanlik": ("Equipment/copper_caydanlik", 220), "tray": ("Equipment/hanging_tea_tray", 200),
    "boiler": ("Equipment/industrial_tea_boiler", 220),
    "okey": ("Games/okey_tiles_scattered", 160), "cards": ("Games/card_deck", 160), "tavla": ("UI/icon_tavla", 160),
    # furniture and the room (demo)
    "table": ("Furniture/prop_table", 170), "table_okey": ("Furniture/prop_table_okey", 170),
    "chair": ("Furniture/prop_chair", 120), "counter": ("Furniture/prop_counter", 200),
    "plant": ("Furniture/prop_plant", 150), "plant_thirsty": ("Furniture/prop_plant_thirsty", 150),
    "door": ("Furniture/prop_door", 220), "cat_bowl": ("Furniture/prop_cat_bowl", 80),
    "awning": ("Furniture/awning_red", 200),
    # street
    "taxi": ("Street/street_taxi", 110), "minibus": ("Street/street_minibus", 120),
    "car_red": ("Street/street_car_red", 110), "dream_car": ("Street/prop_dream_car", 160),
    "lamp": ("Street/street_lamp", 260), "plane_tree": ("Street/street_plane_tree", 300),
    "cypress": ("Street/street_cypress", 280), "simit_cart": ("Street/street_simit_cart", 170),
    "fountain": ("Street/street_fountain", 180), "bench": ("Street/street_bench", 110),
    # icons
    **{n: (f"UI/{f}", 128) for n, f in {
        "i_kumbara": "icon_kumbara", "i_dream_car": "icon_dream_car", "i_megaphone": "icon_megaphone",
        "i_tray": "icon_tray", "i_broom": "icon_broom", "i_paw": "icon_paw", "i_umbrella": "icon_umbrella",
        "i_watering": "icon_watering_can", "i_shop": "icon_shop", "i_basket": "icon_basket", "i_map": "icon_map",
        "i_hammer": "icon_hammer", "i_zabita": "icon_zabita", "i_bank": "icon_bank", "i_scissors": "icon_scissors",
        "i_happy": "icon_face_happy", "i_angry": "icon_face_angry", "i_check": "icon_check", "i_hand": "icon_hand",
        "i_handshake": "icon_handshake", "i_exclamation": "icon_exclamation", "i_music": "icon_music",
        "i_gear": "icon_gear", "i_lock": "icon_lock", "star": "reputation_star", "coins": "wallet_coins",
        "ribbon_bow": "prop_ribbon_bow", "sparkles": "cleanliness_sparkles", "bubbles": "fx_bubbles",
        "ing_tea": "ing_tea", "ing_coffee": "ing_coffee", "ing_bread": "ing_bread", "ing_kasar": "ing_kasar",
        "ing_oralet": "ing_oralet", "ing_catfood": "ing_catfood",
    }.items()},
}


def out(*parts):
    path = os.path.join(OUT, *parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def fit_width(im, w):
    return im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)


def fit_height(im, h):
    return im if im.height <= h else im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def trim(im):
    box = im.getchannel("A").getbbox() if im.mode == "RGBA" else None
    return im.crop(box) if box else im


def webp(im, path, q=82):
    im.save(path, "WEBP", quality=q, method=6)


def illustrations():
    sizes = {}
    for key, name in ILLUSTRATIONS.items():
        im = Image.open(os.path.join(SPR, "Illustrations", name + ".png")).convert("RGBA" if key == "map" else "RGB")
        for w in (480, 960):
            r = fit_width(im, w)
            webp(r, out("img", "ill", f"{key}-{w}.webp"))
        r = fit_width(im, 960)
        sizes[key] = (r.width, r.height)
    return sizes


def shots():
    for lang in ("en", "tr"):
        for key, name in SHOTS.items():
            path = os.path.join(STORE, "screenshots/source", f"iphone-{lang}", name + ".png")
            if not os.path.exists(path):
                continue
            im = Image.open(path).convert("RGB")
            for w in (360, 720):
                webp(fit_width(im, w), out("img", "shots", lang, f"{key}-{w}.webp"), q=80)


def sprites():
    dims = {}
    for name, (rel, h) in SPRITES.items():
        im = trim(Image.open(os.path.join(SPR, rel + ".png")).convert("RGBA"))
        r = fit_height(im, h)
        webp(r, out("img", "sp", f"{name}.webp"), q=88)
        dims[name] = (r.width, r.height)
    for name, rel, w in (("floor-wood", "Illustrations/floor_wood", 256), ("floor-kilim", "Illustrations/floor_kilim", 360),
                         ("floor-patio", "Illustrations/floor_patio", 256), ("floor-asphalt", "Illustrations/floor_asphalt", 256),
                         ("wall-back", "Illustrations/wall_back", 1400)):
        webp(fit_width(Image.open(os.path.join(SPR, rel + ".png")).convert("RGB"), w), out("img", "tex", f"{name}.webp"), q=80)
    return dims


def logo_and_icons():
    logo = trim(Image.open(os.path.join(SPR, "Illustrations/logo_hane.png")).convert("RGBA"))
    for w in (360, 720):
        webp(fit_width(logo, w), out("img", f"logo-{w}.webp"), q=90)
    fit_width(logo, 600).save(out("img", "logo-600.png"), optimize=True)
    icon = Image.open(os.path.join(ART, "AppIcon/hane_app_icon.png")).convert("RGB")
    icon.resize((32, 32), Image.LANCZOS).save(out("favicon-32.png"))
    icon.resize((180, 180), Image.LANCZOS).save(out("apple-touch-icon.png"))
    icon.resize((512, 512), Image.LANCZOS).save(out("icon-512.png"))
    webp(icon.resize((256, 256), Image.LANCZOS), out("img", "app-icon-256.webp"), q=88)
    return logo


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    r = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (r.width - w) // 2, max(0, (r.height - h) // 3)
    return r.crop((x, y, x + w, y + h))


TAGLINES = {
    "en": ("The Turkish tea house tycoon", "iPhone & iPad · Offline · No ads"),
    "tr": ("Kıraathane işletme oyunu", "iPhone ve iPad · İnternetsiz · Reklamsız"),
    "es": ("La casa de té turca que diriges tú", "iPhone y iPad · Sin conexión · Sin anuncios"),
}


def social_cards(logo):
    welcome = Image.open(os.path.join(SPR, "Illustrations/illustration_welcome.png")).convert("RGB")
    title = None
    small = ImageFont.truetype(FONT, 28)
    for lang, (line1, line2) in TAGLINES.items():
        card = Image.new("RGB", (1200, 630), (92, 16, 18))
        glow = Image.new("RGB", (1200, 630), (150, 34, 30))
        mask = Image.new("L", (1200, 630), 0)
        ImageDraw.Draw(mask).ellipse((-200, -260, 900, 900), fill=255)
        card.paste(glow, (0, 0), mask.filter(ImageFilter.GaussianBlur(120)))
        art = cover(welcome, 470, 630)
        card.paste(art, (730, 0))
        shade = Image.new("L", (120, 630))
        for x in range(120):
            ImageDraw.Draw(shade).line((x, 0, x, 630), fill=int(255 * (1 - x / 120)))
        card.paste(Image.new("RGB", (120, 630), (110, 22, 22)), (730, 0), shade)
        lg = fit_width(logo, 560)
        card.paste(lg, (70, 92), lg)
        d = ImageDraw.Draw(card)
        size = 50
        while d.textlength(line1, font=ImageFont.truetype(FONT, size)) > 620:
            size -= 2
        title = ImageFont.truetype(FONT, size)
        d.text((76, 92 + lg.height + 34), line1, font=title, fill=(255, 236, 196))
        d.text((78, 92 + lg.height + 104), line2, font=small, fill=(235, 190, 110))
        d.rectangle((0, 618, 1200, 630), fill=(201, 150, 52))
        card.save(out("og", f"home-{lang}.jpg"), quality=86, optimize=True)
    badge = fit_width(logo, 300)
    for key, name in ILLUSTRATIONS.items():
        if key == "map":
            continue
        im = cover(Image.open(os.path.join(SPR, "Illustrations", name + ".png")).convert("RGB"), 1200, 630)
        im.paste(badge, (40, 630 - badge.height - 34), badge)
        im.save(out("og", f"{key}.jpg"), quality=84, optimize=True)


def videos():
    for lang in ("en", "tr", "es"):
        src = os.path.join(STORE, "app-preview", f"HANE_AppPreview_{lang}_886x1920.mp4")
        if not os.path.exists(src):
            continue
        dst = out("video", f"hane-{lang}.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-vf", "scale=432:-2", "-c:v", "libx264",
                        "-profile:v", "high", "-crf", "29", "-preset", "slow", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", "-c:a", "aac", "-b:a", "64k", "-ac", "1", dst], check=True)
        poster = out("video", f"hane-{lang}-poster.jpg")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "1.5", "-i", dst, "-frames:v", "1", "-q:v", "4", poster], check=True)


if __name__ == "__main__":
    print("illustrations", illustrations())
    shots()
    print("sprites", sprites())
    social_cards(logo_and_icons())
    if "--video" in sys.argv:
        videos()
    print("ok")
