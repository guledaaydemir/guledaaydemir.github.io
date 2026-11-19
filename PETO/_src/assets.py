#!/usr/bin/env python3
"""Copies PETO's own art and screenshots into PETO/assets, web-sized, and builds the pixel fonts and motifs.

    python3 -I PETO/_src/assets.py

Sources: the PETO Xcode project (APP below) for sprites, icons, app icons, the Premium hero and the fonts;
_src/shots/{en,tr,es}/*.png for the real screenshots (taken in the iOS Simulator with the sample household).
Run it again whenever the app's art or the screenshots change; build.py only reads what this script wrote.
"""
import glob, os, re, shutil
from PIL import Image

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(SRC)
OUT = os.path.join(SITE, "assets")
APP = os.path.expanduser("~/PETO")
ART = os.path.join(APP, "SharedArt/PixelArt.xcassets")
XC = os.path.join(APP, "PETO/Resources/Assets.xcassets")


def out(*p):
    path = os.path.join(OUT, *p)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def imageset(folder, name):
    files = glob.glob(os.path.join(folder, name + ".imageset", "*.png"))
    if not files:
        raise SystemExit(f"missing art: {folder}/{name}")
    return files[0]


# ---------------------------------------------------------------- screenshots
def shots():
    for lang in ("en", "tr", "es"):
        for src in sorted(glob.glob(os.path.join(SRC, "shots", lang, "*.png"))):
            key = os.path.splitext(os.path.basename(src))[0]
            im = Image.open(src).convert("RGB")
            for w in (360, 720):
                h = round(im.height * w / im.width)
                im.resize((w, h), Image.LANCZOS).save(out("img", "shots", lang, f"{key}-{w}.webp"), quality=86, method=6)
    print("shots ok")


# ---------------------------------------------------------------- sprites, icons, app icons
def art():
    for d in glob.glob(os.path.join(ART, "Sprites", "*.imageset")):
        name = os.path.basename(d)[:-9]
        Image.open(imageset(os.path.join(ART, "Sprites"), name)).save(out("img", "sp", name + ".webp"), lossless=True, quality=100)
    for d in glob.glob(os.path.join(ART, "Icons", "*.imageset")):
        name = os.path.basename(d)[:-9].replace("icon_", "")
        Image.open(imageset(os.path.join(ART, "Icons"), "icon_" + name)).save(out("img", "ic", name + ".webp"), lossless=True, quality=100)
    icon = Image.open(os.path.join(XC, "AppIcon.appiconset", "icon-1024.png")).convert("RGB")
    icon.resize((512, 512), Image.LANCZOS).save(out("icon-512.png"))
    icon.resize((180, 180), Image.LANCZOS).save(out("apple-touch-icon.png"))
    icon.resize((32, 32), Image.LANCZOS).save(out("favicon-32.png"))
    icon.resize((256, 256), Image.LANCZOS).save(out("img", "app-icon-256.webp"), quality=90)
    icon.resize((512, 512), Image.LANCZOS).save(out("img", "app-icon-512.webp"), quality=90)
    for key in ("standard", "night", "ocean", "sakura", "gold", "retroGreen", "halloween"):
        im = Image.open(imageset(XC, "iconpreview_" + key)).convert("RGB")
        im.resize((160, 160), Image.LANCZOS).save(out("img", "appicons", key + ".webp"), quality=90)
    hero = Image.open(imageset(XC, "paywall_hero"))
    hero.save(out("img", "premium-hero.webp"), quality=90, method=6)
    print("art ok")


# ---------------------------------------------------------------- fonts
def fonts():
    from fontTools.ttLib import TTFont
    f = TTFont(os.path.join(APP, "SharedArt/Fonts/PixelifySans.ttf"))
    f.flavor = "woff2"
    f.save(out("fonts", "pixelify-sans.woff2"))
    shutil.copyfile(os.path.join(APP, "SharedArt/Fonts/PixelifySans-OFL.txt"), out("fonts", "OFL.txt"))
    peto_pixel()
    print("fonts ok")


# Accents drawn above (rows y=800..1000) or below (y=-200..0) the 5x7 caps of the app's PixelFont.
ABOVE = {"acute": ["..#", ".#."], "grave": ["#..", ".#."], "dot": ["#"], "diaeresis": ["#.#"],
         "breve": ["#...#", ".###."], "circumflex": [".#.", "#.#"], "tilde": [".##.#", "#.##."]}
BELOW = {"cedilla": [".#.", "##."]}
COMPOSED = {"Á": ("A", "acute"), "É": ("E", "acute"), "Í": ("I", "acute"), "Ó": ("O", "acute"), "Ú": ("U", "acute"),
            "À": ("A", "grave"), "È": ("E", "grave"), "Ü": ("U", "diaeresis"), "Ö": ("O", "diaeresis"), "Ï": ("I", "diaeresis"),
            "Ğ": ("G", "breve"), "İ": ("I", "dot"), "Â": ("A", "circumflex"), "Î": ("I", "circumflex"), "Û": ("U", "circumflex"),
            "Ñ": ("N", "tilde"), "Ç": ("C", "cedilla"), "Ş": ("S", "cedilla")}
EXTRA = {"¿": None, "¡": None, "(": [".#", "#.", "#.", "#.", "#.", "#.", ".#"], ")": ["#.", ".#", ".#", ".#", ".#", ".#", "#."],
         "·": [".", ".", ".", "#", ".", ".", "."], "#": [".#.#.", "#####", ".#.#.", ".#.#.", "#####", ".#.#.", "....."],
         '"': ["#.#", "#.#", "...", "...", "...", "...", "..."], "’": [".#", ".#", "#.", "..", "..", "..", ".."],
         "—": ["......", "......", "......", "######", "......", "......", "......"], "×": [".....", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "....."],
         "♥": [".....", ".#.#.", "#####", "#####", ".###.", "..#..", "....."], "★": ["..#..", "..#..", "#####", ".###.", ".#.#.", "#...#", "....."]}


def peto_pixel():
    """Builds the PETO Pixel web font from the 5x7 bitmap table the app draws its titles with."""
    from fontTools.fontBuilder import FontBuilder
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    swift = open(os.path.join(APP, "PETO/DesignSystem/Pixel/PixelFont.swift"), encoding="utf-8").read()
    table = {}
    for ch, rows in re.findall(r'"(.)": Glyph\(rows: \[([^\]]*)\]\)', swift):
        table["'" if ch == "\\'" else ch] = re.findall(r'"([.#]+)"', rows)
    table.update({k: v for k, v in EXTRA.items() if v})
    table["¿"] = list(reversed(table["?"]))
    table["¡"] = list(reversed(table["!"]))
    table["'"] = table.get("'", ["#", "#", ".", ".", ".", ".", "."])
    U = 100  # one pixel

    def draw(pen, rows, top, dx=0):
        for r, line in enumerate(rows):  # one rectangle per horizontal run, so no seams between pixels
            for m in re.finditer(r"#+", line):
                x0, x1, y = (m.start() + dx) * U, (m.end() + dx) * U, top - (r + 1) * U
                pen.moveTo((x0, y)); pen.lineTo((x0, y + U)); pen.lineTo((x1, y + U)); pen.lineTo((x1, y)); pen.closePath()

    glyphs, cmap, adv = {".notdef": TTGlyphPen(None).glyph()}, {}, {".notdef": (500, 0)}
    names = {}

    def add(ch, base_rows, mark=None):
        name = f"uni{ord(ch):04X}"
        pen = TTGlyphPen(None)
        w = len(base_rows[0])
        draw(pen, base_rows, 700)
        if mark:
            m = ABOVE.get(mark) or BELOW[mark]
            dx = (w - len(m[0])) // 2
            draw(pen, m, 1000 if mark in ABOVE else 0, dx)
        glyphs[name] = pen.glyph()
        adv[name] = ((w + 1) * U, 0)
        names[ch] = name
        cmap[ord(ch)] = name
        if ch.lower() != ch and len(ch.lower()) == 1:
            cmap[ord(ch.lower())] = name

    for ch, rows in table.items():
        add(ch, rows)
    for ch, (base, mark) in COMPOSED.items():
        add(ch, table[base], mark)
    cmap[ord("ı")] = names["I"]  # dotless i
    cmap[ord("i")] = names["I"]
    cmap[0xA0] = names[" "]
    order = list(glyphs)
    fb = FontBuilder(1000, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics({n: adv[n] for n in order})
    fb.setupHorizontalHeader(ascent=1000, descent=-250)
    fb.setupNameTable({"familyName": "PETO Pixel", "styleName": "Regular"})
    fb.setupOS2(sTypoAscender=1000, sTypoDescender=-250, usWinAscent=1000, usWinDescent=250)
    fb.setupPost()
    os.makedirs(os.path.join(SRC, "fonts"), exist_ok=True)
    fb.save(os.path.join(SRC, "fonts", "peto-pixel.ttf"))  # for the social cards drawn by build.py
    shutil.copyfile(os.path.join(APP, "SharedArt/Fonts/PixelifySans.ttf"), os.path.join(SRC, "fonts", "PixelifySans.ttf"))
    fb.font.flavor = "woff2"
    fb.save(out("fonts", "peto-pixel.woff2"))


def sprite_catalog():
    """Writes _src/sprites.json: species -> [[variant key, name, premium], ...] in the app's order (first 4 free)."""
    import json
    swift = open(os.path.join(APP, "PETO/DesignSystem/Pixel/SpriteCatalog.swift"), encoding="utf-8").read()
    body = swift.split("static func variants(for species: Species)", 1)[1].split("\n    }\n", 1)[0]
    cat = {}
    for sp, block in re.findall(r"case \.(\w+): return \[(.*?)\n\s*\]", body, re.S):
        cat[sp] = [[k, n, p == "true"] for k, n, p in re.findall(r'key: "(\w+)", nameKey: "([^"]+)", isPremium: (true|false)', block)]
    assert len(cat) == 13 and all(len(v) == 8 for v in cat.values()), {k: len(v) for k, v in cat.items()}
    for sp, vs in cat.items():
        for k, _, _ in vs:
            assert os.path.exists(out("img", "sp", f"pet_{sp}_{k}.webp")), (sp, k)
    json.dump(cat, open(os.path.join(SRC, "sprites.json"), "w"), indent=1)


# ---------------------------------------------------------------- Turkish motifs as pixel SVG
PAL = {"k": "#4a2e12", "K": "#2b1d0e", "w": "#fdf6df", "W": "#ffffff", "b": "#1f4f9c", "l": "#5fa1e0", "t": "#3fb3b0",
       "r": "#d9372b", "R": "#a6324f", "g": "#3e8c3a", "G": "#2d6b2a", "y": "#e39a2e", "Y": "#f2d04b", "c": "#f5df93",
       "o": "#12305f", "s": "#9c6632", "S": "#5c3a18", "p": "#d64a86", "x": "#111111", "a": "#c9e4f5"}

MOTIFS = {
    "nazar": ["....oooo....", "..oobbbboo..", ".obbbbbbbbo.", ".obbWWWWbbo.", "obbWWllWWbbo", "obbWlxxlWbbo",
              "obbWlxxlWbbo", "obbWWllWWbbo", ".obbWWWWbbo.", ".obbbbbbbbo.", "..oobbbboo..", "....oooo...."],
    "tulip": [".....rr.....", "..r..rr..r..", "..rr.rr.rr..", "..rrrrrrrr..", "..rrrRrrrr..", "..rrrRRrrr..",
              "...rrRRrr...", "....rrrr....", ".....gg.....", "..g..gg.....", "..gg.gg..g..", "...gggg.gg..",
              ".....gggg...", ".....gg....."],
    "cini": ["bwwwwwwttwwwwwwb", "wwwwwwtbbtwwwwww", "wwwwwwtbbtwwwwww", "wwwwwwwttwwwwwww", "wwwwwwwbbwwwwwww",
             "wwwwwwwrrwwwwwww", "wttwwwrwwrwwwttw", "tbbtbrwwwwrbtbbt", "tbbtbrwwwwrbtbbt", "wttwwwrwwrwwwttw",
             "wwwwwwwrrwwwwwww", "wwwwwwwbbwwwwwww", "wwwwwwwttwwwwwww", "wwwwwwtbbtwwwwww", "wwwwwwtbbtwwwwww",
             "bwwwwwwttwwwwwwb"],
    "cay": ["..........", ".aaaaaaaa.", ".arrrrrra.", "..arrrra..", "...arra...", "...arra...", "..arrrra..",
            ".arrrrrra.", ".aarrrraa.", "..aaaaaa..", "yyyyyyyyyy", ".yyyyyyyy."],
    "bowl": ["............", "..ssSssSss..", ".sSssssssSs.", "kkkkkkkkkkkk", "kllllllllllk", ".kllWllWllk.",
             ".klllWWlllk.", "..kllllllk..", "...kkkkkk..."],
}


def kilim():
    """A 32x12 kilim band tile: stepped diamonds with hooks, between dark borders."""
    rows = []
    for y in range(12):
        line = ""
        for x in range(32):
            if y in (0, 11):
                line += "k"; continue
            if y in (1, 10):
                line += "y" if x % 4 < 2 else "k"; continue
            cx = 7.5 if x < 16 else 23.5
            d = abs(x - cx) + abs(y - 5.5)
            if d < 1.5: c = "w"
            elif d < 3: c = "b"
            elif d < 4: c = "w"
            elif d < 5.2: c = "k"
            else: c = "r"
            if c == "r" and (x in (0, 15, 16, 31)) and y in (4, 5, 6, 7): c = "y"
            line += c
        rows.append(line)
    return rows


def skyline():
    """A 192x30 Istanbul skyline silhouette: domes, minarets and the Galata tower."""
    W, H = 192, 30
    g = [["." for _ in range(W)] for _ in range(H)]

    def rect(x0, y0, x1, y1, c="S"):
        for y in range(max(0, y0), min(H, y1)):
            for x in range(max(0, x0), min(W, x1)):
                g[y][x] = c

    def dome(cx, base, r, c="S"):
        for y in range(base - r, base + 1):
            for x in range(cx - r, cx + r + 1):
                if (x - cx) ** 2 + ((y - base) * 1.15) ** 2 <= r * r:
                    if 0 <= y < H and 0 <= x < W:
                        g[y][x] = c

    def minaret(x, top):
        rect(x, top, x + 2, H)
        rect(x - 1, top + 6, x + 3, top + 7)
        g[top - 1][x] = g[top - 1][x + 1] = "S"; g[top - 2][x] = "S"

    rect(0, 26, W, H)
    # mosque 1
    rect(20, 20, 58, 26); dome(39, 20, 9); dome(26, 21, 4); dome(52, 21, 4); minaret(14, 8); minaret(62, 8)
    g[9 - 9][39] = "S"
    rect(39, 9, 40, 12)
    # houses
    for x, h in ((70, 18), (78, 16), (86, 19), (94, 17)):
        rect(x, h, x + 7, 26); rect(x - 1, h - 1, x + 8, h)
    # Galata tower
    rect(108, 9, 116, 26); rect(107, 12, 117, 13); dome(112, 9, 4); rect(111, 1, 113, 6)
    # mosque 2
    rect(128, 21, 160, 26); dome(144, 21, 8); dome(133, 22, 3); dome(155, 22, 3); minaret(124, 11); minaret(164, 11)
    rect(144, 10, 145, 13)
    for x, h in ((172, 19), (180, 17), (187, 20)):
        rect(x, h, x + 6, 26)
    return ["".join(r) for r in g]


def svg(rows, name, opacity=None):
    h, w = len(rows), len(rows[0])
    rects = []
    for y, line in enumerate(rows):
        x = 0
        while x < w:
            c = line[x]
            if c == ".":
                x += 1; continue
            x0 = x
            while x < w and line[x] == c:
                x += 1
            rects.append(f'<rect x="{x0}" y="{y}" width="{x - x0}" height="1" fill="{PAL[c]}"/>')
    op = f' opacity="{opacity}"' if opacity else ""
    data = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" shape-rendering="crispEdges"{op}>'
            + "".join(rects) + "</svg>")
    open(out("img", "px", name + ".svg"), "w").write(data)


def code_icons():
    """Exports the app's code-drawn 12x12 PixelIcon grids (scoop, drop, litter box, tank) as pixel SVGs, and the
    outfit and effect art as webp, so the site can show the new care types with the app's own pixels."""
    swift = open(os.path.join(APP, "PETO/DesignSystem/Pixel/PixelIcons.swift"), encoding="utf-8").read()
    pal = dict(re.findall(r'"(\w)": Color\(hex: 0x([0-9A-Fa-f]{6})\)', swift.split("func sprite(outline", 1)[1].split("return PixelSprite", 1)[0]))
    pal = {k: "#" + v.lower() for k, v in pal.items()}
    pal["B"] = "#4a2e12"
    for name in ("scoop", "drop", "litterBox", "tank"):
        block = re.search(r"case \." + name + r": return \[(.*?)\]", swift, re.S).group(1)
        rows = re.findall(r'"([^"]+)"', block)
        rects = []
        for y, line in enumerate(rows):
            for x, c in enumerate(line):
                if c != ".":
                    rects.append(f'<rect x="{x}" y="{y}" width="1" height="1" fill="{pal[c]}"/>')
        open(out("img", "ic", name + ".svg"), "w").write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 12" width="12" height="12" shape-rendering="crispEdges">{"".join(rects)}</svg>')
    for folder, prefix in (("Outfits", "outfit_"), ("Effects", "effect_")):
        for d in glob.glob(os.path.join(ART, folder, "*.imageset")):
            name = os.path.basename(d)[:-9]
            im = Image.open(imageset(os.path.join(ART, folder), name)).convert("RGBA")
            im.save(out("img", "ic", name + ".webp"), lossless=True, quality=100)
    print("code icons ok")


def motifs():
    for name, rows in MOTIFS.items():
        assert len({len(r) for r in rows}) == 1, name
        svg(rows, name)
    svg(kilim(), "kilim")
    svg(skyline(), "skyline")
    print("motifs ok")


if __name__ == "__main__":
    shots(); art(); fonts(); motifs(); code_icons(); sprite_catalog()
