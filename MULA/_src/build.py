#!/usr/bin/env python3
"""Builds the MULA website (EN / TR / ES) as static HTML for GitHub Pages, under /MULA/.

    python3 -I MULA/_src/assets.py     # first, when screenshots, art, fonts or the launch video changed
    python3 -I MULA/_src/build.py      # pages, social cards, sitemap.xml, llms.txt, llms-full.txt, css/js

Copy lives in _src/content/{en,tr,es}.py, guides in _src/guides/*.py (see guides/FORMAT.md), app facts in
_src/FACTS.md, the app's own per-season plant data in _src/species.json. Never hand-edit the generated HTML.

This folder is deliberately not linked from the main site, its sitemap or robots.txt yet.
"""
import glob, hashlib, html, json, math, os, re, runpy, shutil

from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(SRC)
ORIGIN = "https://guledaaydemir.github.io"
BASE = "/MULA/"
A = BASE + "assets/"
APP_ID = "6836519863"          # App Store id of "MULA: Plant Care"
PT = "128720446"               # provider token used on the other app sites
EMAIL = "solostaseraofficial@gmail.com"
AUTHOR = "Gül Eda Aydemir"
TODAY = "2026-11-19"
LANGS = os.environ.get("MULA_LANGS", "en,tr,es").split(",")
LOCALE = {"en": "en_US", "tr": "tr_TR", "es": "es_ES"}

PATHS = {
    "home": {"en": "", "tr": "tr/", "es": "es/"},
    "about": {"en": "about/", "tr": "tr/hakkinda/", "es": "es/acerca-de/"},
    "guides": {"en": "guides/", "tr": "tr/rehber/", "es": "es/guias/"},
    "faq": {"en": "faq/", "tr": "tr/sss/", "es": "es/preguntas-frecuentes/"},
    "support": {"en": "support/", "tr": "tr/destek/", "es": "es/soporte/"},
    "privacy": {"en": "privacy/", "tr": "tr/gizlilik/", "es": "es/privacidad/"},
    "terms": {"en": "terms/", "tr": "tr/kosullar/", "es": "es/terminos/"},
}
GUIDE_DIR = {"en": "guides/", "tr": "tr/rehber/", "es": "es/guias/"}
HINT = {"en": "This site is also in English", "tr": "Bu site Türkçe de var", "es": "Esta web también está en español"}


def _load(lang):
    t = runpy.run_path(os.path.join(SRC, "content", lang + ".py"))["T"]
    return t


C = {l: _load(l) for l in LANGS}
for l in LANGS:  # {email} placeholder everywhere
    C[l] = json.loads(json.dumps(C[l], ensure_ascii=False).replace("{email}", EMAIL))
GUIDES = sorted((runpy.run_path(p)["GUIDE"] for p in glob.glob(os.path.join(SRC, "guides", "*.py"))), key=lambda g: g["order"])
for g in GUIDES:
    PATHS[g["id"]] = {l: GUIDE_DIR[l] + g[l]["slug"] + "/" for l in LANGS}
GUIDE_IDS = {g["id"] for g in GUIDES}
SPECIES = json.load(open(os.path.join(SRC, "species.json")))
NICK = {"monstera": "Momo", "camellia": "Tsubaki", "ficus": "Nori", "hydrangea": "Ajisai", "orchid": "Ran", "pilea": "Mame"}

e = lambda s: html.escape(str(s), quote=True)
strip = lambda s: re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", s)).strip()
LINK = re.compile(r"\{\{link:([a-z0-9-]+)\}\}")


def url(page, lang, absolute=False):
    if page == "demo":
        return url("home", lang, absolute) + "#soil"
    u = BASE + PATHS[page][lang]
    return ORIGIN + u if absolute else u


def store(lang, place):
    return f"https://apps.apple.com/app/apple-store/id{APP_ID}?pt={PT}&ct=web-mula-{lang}-{place}&mt=8"


STORE_CANON = f"https://apps.apple.com/app/id{APP_ID}"


# ---------------------------------------------------------------- images
_dims = {}


def dims(rel):
    if rel not in _dims:
        with Image.open(os.path.join(SITE, rel.replace(BASE, "", 1))) as im:
            _dims[rel] = im.size
    return _dims[rel]


def shot_src(key, lang, w=720):
    rel = f"{A}img/shots/{lang}/{key}-{w}.webp"
    return rel if os.path.exists(os.path.join(SITE, rel.replace(BASE, "", 1))) else f"{A}img/shots/en/{key}-{w}.webp"


def shot_img(key, lang, alt, lazy=True, sizes="(max-width: 700px) 66vw, 300px"):
    s, b = shot_src(key, lang, 360), shot_src(key, lang, 720)
    w, h = dims(b)
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="{b}" srcset="{s} 360w, {b} 720w" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}"{load}>'


def phone(key, lang, alt, cls="", lazy=True, sizes="(max-width: 700px) 66vw, 300px"):
    if key == "widgets":
        return widgets_fig(lang, alt, cls)
    if key == "watch":
        return watch_fig(alt, cls)
    return f'<div class="phone {cls}"><div class="screen">{shot_img(key, lang, alt, lazy, sizes)}</div></div>'


def art_img(plant, alt, cls="", lazy=True, sizes="(max-width: 700px) 80vw, 380px"):
    s, b = f"{A}img/art/{plant}-poster-480.webp", f"{A}img/art/{plant}-poster-900.webp"
    w, h = dims(b)
    load = ' loading="lazy" decoding="async"' if lazy else ""
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{b}" srcset="{s} 480w, {b} 900w" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}"{load}>'


def half_img(plant, part, alt="", cls="", lazy=True, sizes="(max-width: 700px) 46vw, 260px"):
    s, b = f"{A}img/art/{plant}-{part}-480.webp", f"{A}img/art/{plant}-{part}-960.webp"
    w, h = dims(b)
    load = ' loading="lazy" decoding="async"' if lazy else ""
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{b}" srcset="{s} 480w, {b} 960w" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}"{load}>'


def widget_img(name, alt="", cls="", half=True):
    rel = f"{A}img/widgets/{name}{'-half' if half and os.path.exists(os.path.join(SITE, 'assets/img/widgets', name + '-half.webp')) else ''}.webp"
    w, h = dims(rel)
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{rel}" width="{w}" height="{h}" alt="{e(alt)}" loading="lazy" decoding="async">'


def widgets_fig(lang, alt, cls=""):
    return (f'<div class="widgets-fig {cls}" role="img" aria-label="{e(alt)}">'
            f'<div class="w-row">{widget_img("small-premium-light", "", "w-small", False)}{widget_img("medium-premium-light", "", "w-medium")}</div>'
            f'{widget_img("large-premium-light", "", "w-large")}'
            f'<div class="w-lock">{widget_img("circle-premium", "", "w-circle", False)}{widget_img("rect-premium", "", "w-rect", False)}</div></div>')


def watch_fig(alt, cls="", which="list"):
    rel = f"{A}img/watch/{which}.webp"
    w, h = dims(rel)
    return (f'<div class="watch {cls}"><div class="w-case"><img src="{rel}" width="{w}" height="{h}" alt="{e(alt)}" '
            f'loading="lazy" decoding="async"></div><i class="crown"></i></div>')


# ---------------------------------------------------------------- icons (line icons in the app's weight)
ICONS = {
    "drop": '<path d="M12 3.5c3 3.7 6 7.4 6 10.6A6 6 0 0 1 6 14.1c0-3.2 3-6.9 6-10.6z"/>',
    "leaf": '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14z"/><path d="M5 19c3-4 6-7 10-9"/>',
    "season": '<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17M3.5 12h17"/>',
    "frost": '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9"/><path d="M9.5 4.5 12 7l2.5-2.5M9.5 19.5 12 17l2.5 2.5"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/>',
    "camera": '<rect x="3" y="7" width="18" height="13" rx="3"/><path d="M8.5 7 10 4.5h4L15.5 7"/><circle cx="12" cy="13.5" r="3.5"/>',
    "book": '<path d="M5 4.5h10a3 3 0 0 1 3 3V20H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h10"/>',
    "suitcase": '<rect x="4" y="7" width="16" height="12.5" rx="2.5"/><path d="M9 7V5a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 5v2M9 7v12.5M15 7v12.5"/>',
    "widget": '<rect x="3.5" y="3.5" width="7" height="7" rx="2"/><rect x="13.5" y="3.5" width="7" height="7" rx="2"/><rect x="3.5" y="13.5" width="17" height="7" rx="2"/>',
    "watch": '<rect x="6" y="6" width="12" height="12" rx="3.5"/><path d="M8.5 6l1-3h5l1 3M8.5 18l1 3h5l1-3"/>',
    "wave": '<path d="M3 12h1.5M7 8.5v7M10.5 5v14M14 8v8M17.5 10v4M21 12h-1"/>',
    "moon": '<path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5z"/>',
    "check": '<path d="M5 12.5 10 17.5 19.5 7"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"/>',
    "user": '<circle cx="12" cy="8.5" r="3.5"/><path d="M5 20c1-3.5 3.8-5.5 7-5.5s6 2 7 5.5"/>',
    "phone": '<rect x="6.5" y="2.5" width="11" height="19" rx="3"/><path d="M10.5 5h3"/>',
    "spark": '<path d="M12 3c.6 4.6 2.4 6.4 7 7-4.6.6-6.4 2.4-7 7-.6-4.6-2.4-6.4-7-7 4.6-.6 6.4-2.4 7-7z"/>',
    "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="m4 7 8 6 8-6"/>',
    "bell": '<path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>',
    "home": '<path d="M4 11 12 4l8 7v8.5a1 1 0 0 1-1 1h-4.5V15h-5v5.5H5a1 1 0 0 1-1-1z"/>',
    "question": '<circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.3a2.5 2.5 0 1 1 3.4 2.4c-.7.3-1 .8-1 1.5v.5"/><circle cx="12" cy="16.8" r=".6"/>',
    "heart": '<path d="M12 20s-7-4.3-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.7-7 10-7 10z"/>',
    "grid": '<rect x="4" y="4" width="6.5" height="6.5" rx="3.25"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="3.25"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="3.25"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="3.25"/>',
    "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 3.5 5.4 3.5 8.5s-1 5.9-3.5 8.5c-2.5-2.6-3.5-5.4-3.5-8.5s1-5.9 3.5-8.5z"/>',
}


def icon(name, size=22, cls="ic"):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


APPLE = ('<svg class="apple" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.37 12.76c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.77-3.32-1.8-1.41-.14-2.76.84-3.47.84-.72 0-1.82-.82-3-.8-1.54.02-2.96.9-3.76 2.27-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.34 2.86 2.3 1.150-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 1.23-.02 2.01-1.12 2.76-2.23.87-1.28 1.230-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.65zM14.1 6.02c.63-.77 1.06-1.83.94-2.89-.91.04-2.01.61-2.66 1.37-.58.67-1.09 1.75-.96 2.790 1.02.08 2.05-.52 2.68-1.27z"/></svg>')


def store_badge(lang, place, cls="store"):
    t = C[lang]["badge"]
    return (f'<a class="{cls}" href="{e(store(lang, place))}" aria-label="{e(t["aria"])}">{APPLE}'
            f'<span><small>{e(t["top"])}</small><b>{e(t["big"])}</b></span></a>')


def tier(lang, t):
    return f'<span class="tag {t}">{e(C[lang][t])}</span>'


# ---------------------------------------------------------------- the launch emblem (rebuilt from LaunchIntro.swift)
def _leaf(base, tip, width):
    bx, by = base
    dx, dy = tip[0] - bx, tip[1] - by
    ln = max(1, math.hypot(dx, dy))
    nx, ny = -dy / ln, dx / ln
    k = width / 1.5

    def at(f, off):
        return f"{bx + dx * f + nx * off:.1f},{by + dy * f + ny * off:.1f}"
    return f"M{at(0, 0)} C{at(.22, k)} {at(.72, k)} {at(1, 0)} C{at(.72, -k)} {at(.22, -k)} {at(0, 0)}Z"


def _dome(cx, base, rx, ry, up=True):
    return f"M{cx - rx},{base} A{rx},{ry} 0 0 {1 if up else 0} {cx + rx},{base}Z"


LEAVES = [((246, 336), (118, 273), 58, "deep", 24), ((246, 258), (133, 195), 56, "olive", 24),
          ((250, 308), (369, 237), 52, "soft", -24), ((248, 220), (361, 130), 58, "deep", -24)]
ROOTS = [((248, 383), (252, 422), (243, 463)), ((247, 394), (222, 410), (190, 437)), ((249, 398), (276, 413), (303, 441)),
         ((246, 420), (230, 440), (221, 461)), ((250, 426), (267, 442), (274, 463)), ((210, 422), (199, 433), (193, 451)),
         ((286, 424), (296, 434), (299, 451))]
VB = "-80 -80 660 660"   # the 500-unit design box with the app's 80-unit margin


def _layer(cls, inner, anchor=None, defs=""):
    style = ""
    if anchor:
        style = f' style="--ox:{(anchor[0] + 80) / 6.6:.2f}%;--oy:{(anchor[1] + 80) / 6.6:.2f}%"'
    return f'<svg class="em-l {cls}"{style} viewBox="{VB}" aria-hidden="true">{defs}{inner}</svg>'


def emblem(uid="em"):
    """The MULA emblem as stacked layers, so each piece can drift into focus on its own like the app's intro."""
    g = uid
    sun = _layer("em-sun", f'<circle cx="152" cy="127" r="75" fill="url(#{g}-sun)"/>', (152, 127),
                 f'<defs><linearGradient id="{g}-sun" x1="100" y1="70" x2="210" y2="190" gradientUnits="userSpaceOnUse">'
                 f'<stop offset="0" stop-color="#DF7246"/><stop offset="1" stop-color="#EDA172"/></linearGradient></defs>')
    left = _layer("em-hl", f'<path d="{_dome(110, 435, 102, 88)}" fill="#B4B087"/>', (110, 400))
    blue = _layer("em-hb", f'<path d="{_dome(382, 432, 107, 107)}" fill="#94AAA8"/>', (382, 390))
    blush = _layer("em-hp", f'<path d="{_dome(392, 480, 68, 63)}" fill="#EDB08F"/>', (392, 455))
    stem = _layer("em-stem", '<path class="draw" pathLength="1" d="M248,386 L248,238 Q248,216 266,206" fill="none" '
                             'stroke-width="8" stroke-linecap="round"/>')
    leaves = "".join(_layer(f"em-leaf em-leaf{i} {c}", f'<path d="{_leaf(b, t, w)}"/>', b) for i, (b, t, w, c, _) in enumerate(LEAVES))
    roots = "".join(f'<path class="draw r{i}" pathLength="1" d="M{a[0]},{a[1]} Q{m[0]},{m[1]} {z[0]},{z[1]}" '
                    f'stroke-width="{3 if i < 3 else 2.2}"/>' for i, (a, m, z) in enumerate(ROOTS))
    bowl = _layer("em-bowl", f'<path d="{_dome(248, 381, 110, 110, False)}" fill="url(#{g}-bowl)"/>'
                             f'<g class="roots" fill="none" stroke="#F6E4D0" stroke-linecap="round">{roots}</g>', (248, 436),
                  f'<defs><linearGradient id="{g}-bowl" x1="248" y1="381" x2="248" y2="491" gradientUnits="userSpaceOnUse">'
                  f'<stop offset="0" stop-color="#D26B42"/><stop offset="1" stop-color="#BB5D36"/></linearGradient></defs>')
    orbit = _layer("em-orbit", '<path class="draw" pathLength="1" d="M152,52 Q262,-36 403,75" fill="none" stroke-width="1.6"/>'
                               '<circle class="dot" cx="403" cy="75" r="6" fill="#C14B23"/>')
    return f'<div class="emblem" aria-hidden="true">{sun}{left}{blue}{blush}{stem}{leaves}{bowl}{orbit}</div>'


def mark(size=30):
    """Small static emblem for the wordmark (the app's sprout glyph)."""
    leaves = "".join(f'<path d="{_leaf(b, t, w)}" class="{c}"/>' for b, t, w, c, _ in LEAVES)
    return (f'<svg class="mark" width="{size}" height="{size}" viewBox="40 0 420 500" aria-hidden="true">'
            f'<circle cx="152" cy="127" r="75" fill="#DF7246"/><path d="M248,386 L248,238 Q248,216 266,206" class="stem" fill="none" '
            f'stroke-width="12" stroke-linecap="round"/>{leaves}<path d="{_dome(248, 381, 110, 110, False)}" fill="#C9653D"/></svg>')


def wordmark(tag="span"):
    return f'<{tag} class="wordmark">{mark()}<span>MULA</span></{tag}>'


# ---------------------------------------------------------------- page frame
def head(lang, page, title, desc, og, og_alt, ld, og_type="website", extra=""):
    t = C[lang]
    canon = url(page, lang, True)
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(page, l, True)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{url(page, "en", True)}">'
    locs = "".join(f'<meta property="og:locale:alternate" content="{LOCALE[l]}">' for l in LANGS if l != lang)
    og_url = ORIGIN + og
    return f"""<!DOCTYPE html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="{AUTHOR}">
<meta name="theme-color" content="#f2e7d9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1b2a1e" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="MULA">
<meta property="og:locale" content="{LOCALE[lang]}">{locs}
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{og_url}">
<link rel="icon" type="image/png" sizes="32x32" href="{A}favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="{A}favicon-48.png">
<link rel="apple-touch-icon" href="{A}apple-touch-icon.png">
<link rel="preload" href="{A}fonts/cormorant-medium-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{A}fonts/jost-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A}mula.css?v={VER['css']}">
<link rel="alternate" type="text/plain" href="{BASE}llms.txt" title="{e(t['llms_title'])}">
<script>document.documentElement.className="js";try{{var m=localStorage.getItem("mula-theme");if(m)document.documentElement.dataset.theme=m}}catch(_){{}}{extra}</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":"))}</script>
</head>"""


TABS = [("home", "home"), ("about", "heart"), ("guides", "book"), ("faq", "question"), ("support", "mail")]


def header(lang, page):
    t = C[lang]
    cur = "guides" if page in GUIDE_IDS else page
    nav = "".join(f'<a href="{url(p, lang)}"{" aria-current=page" if cur == p else ""}>{e(t["nav"][p])}</a>' for p, _ in TABS[1:])
    langs = "".join(f'<a href="{url(page, l)}" hreflang="{l}" lang="{l}"{" aria-current=true" if l == lang else ""} title="{e(C[l]["lang_name"])}">{l.upper()}</a>' for l in LANGS)
    idx = next((i for i, (p, _) in enumerate(TABS) if p == cur), -1)
    tabs = "".join(f'<a href="{url(p, lang)}" data-i="{i}"{" aria-current=page" if cur == p else ""}>{icon(ic_, 22)}<span>{e(t["nav"][p])}</span></a>' for i, (p, ic_) in enumerate(TABS))
    theme = (f'<button type="button" class="mood" aria-label="{e(t["theme"])}" title="{e(t["theme"])}">'
             f'<span class="sun">{icon("sun", 18)}</span><span class="moon">{icon("moon", 18)}</span></button>')
    return f"""<body data-page="{e(page)}">
<a class="skip" href="#main">{e(t['skip'])}</a>
<div class="grain" aria-hidden="true"></div>
<header class="topbar"><div class="wrap">
<a class="brand" href="{url('home', lang)}" aria-label="{e(t['home_label'])}">{wordmark()}</a>
<nav class="topnav" aria-label="MULA">{nav}</nav>
<div class="tools"><div class="langs" role="group" aria-label="{e(t['language'])}">{langs}</div>{theme}
<a class="btn sm get" href="{e(store(lang, 'nav'))}">{APPLE}<span>{e(t['get'])}</span></a></div>
</div></header>
<nav class="tabbar" aria-label="MULA" style="--i:{idx}"><i class="disc" aria-hidden="true"></i>{tabs}</nav>
<main id="main">"""


def hills_svg(cls="hills"):
    return (f'<svg class="{cls}" viewBox="0 0 1440 220" preserveAspectRatio="none" aria-hidden="true">'
            '<circle class="h-sun" cx="1130" cy="92" r="46"/>'
            '<path class="h-orbit" d="M1010 70 Q1150 -10 1320 60" fill="none"/>'
            '<path class="h-sage" d="M-40 220 C 120 90 330 90 470 220Z"/>'
            '<path class="h-blue" d="M300 220 C 480 60 760 60 930 220Z"/>'
            '<path class="h-blush" d="M820 220 C 930 120 1080 120 1180 220Z"/>'
            '<path class="h-olive" d="M1080 220 C 1220 100 1380 100 1500 220Z"/></svg>')


def footer(lang, page, extra_js=""):
    t, f = C[lang], C[lang]["foot"]
    gl = "".join(f'<li><a href="{url(g["id"], lang)}">{e(g[lang]["title"].split(" — ")[0].split(" | ")[0])}</a></li>' for g in GUIDES[:6])
    apps = "".join(f'<li><a href="{e(u)}" rel="noopener">{e(n)}</a> <small>{e(d)}</small></li>' for n, d, u in f["apps"])
    hint = "".join(f'<a data-lang="{l}" lang="{l}" href="{url(page, l)}" hidden>{e(HINT[l])} →</a>' for l in LANGS if l != lang)
    return f"""</main>
<footer class="foot">
{hills_svg()}
<div class="foot-paper"><div class="wrap">
<div class="cols">
<div class="about-col"><a class="brand" href="{url('home', lang)}">{wordmark()}</a><p>{e(f['tagline'])}</p>{store_badge(lang, 'footer')}</div>
<div><h2 class="h5">{e(f['app'])}</h2><ul><li><a href="{url('home', lang)}">{e(t['nav']['home'])}</a></li><li><a href="{url('about', lang)}">{e(t['nav']['about'])}</a></li><li><a href="{url('demo', lang)}">{e(f['demo'])}</a></li><li><a href="{url('faq', lang)}">{e(t['nav']['faq'])}</a></li><li><a href="{url('support', lang)}">{e(t['nav']['support'])}</a></li></ul></div>
<div><h2 class="h5">{e(f['learn'])}</h2><ul>{gl}<li><a href="{url('guides', lang)}">{e(f['all_guides'])} →</a></li></ul></div>
<div><h2 class="h5">{e(f['help'])}</h2><ul><li><a href="{url('privacy', lang)}">{e(f['privacy'])}</a></li><li><a href="{url('terms', lang)}">{e(f['terms'])}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{BASE}llms.txt">llms.txt</a></li></ul>
<h2 class="h5">{e(f['more'])}</h2><ul>{apps}</ul></div>
</div>
<div class="foot-bar"><small>{e(f['made'])} {AUTHOR} · © 2026 · {e(f['apple'])}</small><div class="langs" role="group" aria-label="{e(t['language'])}">{''.join(f'<a href="{url(page, l)}" hreflang="{l}" lang="{l}"{" aria-current=true" if l == lang else ""}>{e(C[l]["lang_name"])}</a>' for l in LANGS)}</div></div>
</div></div></footer>
<div class="lang-hint" role="region" aria-label="{e(t['language'])}">{hint}<button type="button" aria-label="{e(t['close'])}">×</button></div>
<script src="{A}mula.js?v={VER['js']}" defer></script>{extra_js}
</body>
</html>
"""


def write(page, lang, body):
    path = os.path.join(SITE, PATHS[page][lang], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def section_head(kicker, h2, lead=None, extra="", cls=""):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="section-head reveal {cls}"><p class="kicker">{e(kicker)}</p><h2>{e(h2)}</h2>{lead_html}{extra}</div>'


# ---------------------------------------------------------------- structured data
PERSON = {"@type": "Person", "@id": ORIGIN + "/#person", "name": AUTHOR, "alternateName": "Gul Eda Aydemir",
          "jobTitle": "Independent iOS developer", "url": ORIGIN + "/", "email": "mailto:" + EMAIL,
          "sameAs": ["https://www.instagram.com/solo.stasera/", "https://apps.apple.com/developer/id1889159460"]}


def app_ld(lang):
    t, h = C[lang], C[lang]["home"]
    return {"@type": ["MobileApplication", "SoftwareApplication"], "@id": ORIGIN + BASE + "#app", "name": "MULA",
            "alternateName": t["store_name"], "description": h["description"], "url": url("home", lang, True),
            "image": ORIGIN + A + "icon-512.png", "applicationCategory": "LifestyleApplication",
            "applicationSubCategory": "Plant care", "operatingSystem": "iOS 17 or later, iPadOS 17 or later, macOS (Apple silicon), watchOS 10 or later",
            "availableOnDevice": ["iPhone", "Apple Watch"], "inLanguage": "en", "isAccessibleForFree": True,
            "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "category": "Free to download, optional in-app purchases"},
            "featureList": h["ld_features"], "keywords": h["ld_keywords"],
            "installUrl": STORE_CANON, "downloadUrl": STORE_CANON, "sameAs": [STORE_CANON],
            "screenshot": [ORIGIN + shot_src(k, lang) for k in ("today", "soil", "garden", "plant", "seasons", "lightmeter")]}


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def crumbs_html(items):
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span aria-hidden="true">·</span>'.join(f'<a href="{u.replace(ORIGIN, "")}">{e(n)}</a>' for n, u in items[:-1]) + "</nav>"


def links(s, lang):
    def link(m):
        if m.group(1) not in PATHS and m.group(1) != "demo":
            if os.environ.get("MULA_DRAFT"):
                return url("guides", lang)
            raise SystemExit(f"unknown link target {m.group(1)!r}")
        return url(m.group(1), lang)
    return LINK.sub(link, s)


def faq_ld(pairs, lang):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(links(a, lang))}} for q, a in pairs]}


def faq_html(pairs, lang):
    return '<div class="faq">' + "".join(f'<details class="reveal"><summary><span>{e(q)}</span><i aria-hidden="true"></i></summary><div><p>{links(a, lang)}</p></div></details>' for q, a in pairs) + "</div>"


def cta_box(lang, place):
    t = C[lang]["cta_box"]
    return (f'<aside class="cta-box reveal">{emblem_static()}<div><h3>{e(t["h"])}</h3><p>{e(t["p"])}</p>{store_badge(lang, place)}</div></aside>')


def emblem_static():
    return f'<img class="cta-icon" src="{A}img/app-icon-256.webp" width="96" height="96" alt="" loading="lazy" decoding="async">'


def page_hero(items, kicker, h1, lead, extra="", art=None):
    pic = f'<div class="ph-art reveal">{art}</div>' if art else ""
    return (f'<section class="page-hero"><div class="wrap{" with-art" if art else ""}"><div class="ph-copy">{crumbs_html(items)}<p class="kicker">{e(kicker)}</p><h1>{e(h1)}</h1>'
            f'<p class="lead">{lead}</p>{extra}</div>{pic}</div>{wave_svg("ph-wave")}</section>')


def wave_svg(cls="wave"):
    return (f'<svg class="{cls}" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M0,64 C240,8 420,8 640,52 C880,100 1120,112 1440,40 L1440,120 L0,120 Z"/></svg>')


# ---------------------------------------------------------------- home
def species_local(lang, sid):
    loc = C[lang].get("species", {}).get(sid, {})
    base = next(s for s in SPECIES if s["id"] == sid)
    return loc.get("common", base["common"]), loc.get("tips", base["tips"])


def demo_data(lang):
    t, h = C[lang], C[lang]["home"]
    plants = []
    for nick, sid, latin in h["faces"]:
        s = next(x for x in SPECIES if x["id"] == sid)
        common, tips = species_local(lang, sid)
        plants.append({"id": sid, "nick": nick, "latin": s["latin"], "common": common, "water": s["water"], "feed": s["feed"],
                       "min": s["min"], "max": s["max"], "tips": tips, "place": t["place"][s["placement"]],
                       "light": t["light"][s["light"]], "lightKey": s["light"]})
    every = [{"id": s["id"], "common": species_local(lang, s["id"])[0], "latin": s["latin"], "light": s["light"]} for s in SPECIES]
    return {"seasons": t["seasons"], "months": t["season_months"], "plants": plants, "all": every, "light": t["light"],
            "labels": {k: h[k] for k in ("seasons_water", "seasons_water_v", "seasons_feed", "seasons_feed_v", "seasons_rest",
                                         "seasons_temp", "seasons_temp_v", "light_value")},
            "soil": {"res": h["soil_res"], "btn": h["soil_btn"], "n": next(x for x in SPECIES if x["id"] == "monstera")["water"]},
            "lang": lang}


def guide_card(g, lang, i=0):
    gl = g[lang]
    return (f'<a class="g-card reveal" style="--i:{i % 6}" href="{url(g["id"], lang)}" data-cat="{g["category"]}">'
            f'<div class="g-art">{half_img(g["art"], "geo", "", "", True, "(max-width: 700px) 90vw, 360px")}</div>'
            f'<div class="g-copy"><p class="kicker">{e(gl["kicker"])}</p><h3>{e(gl["h1"])}</h3><p>{e(gl["description"])}</p>'
            f'<span class="more">{e(read_minutes(gl, lang))} {icon("arrow", 16)}</span></div></a>')


def read_minutes(gl, lang):
    n = max(3, round(len(strip(gl["body"]).split()) / 200))
    return C[lang]["article"]["read"].format(n=n)


def home(lang):
    t, h = C[lang], C[lang]["home"]
    ld = {"@context": "https://schema.org", "@graph": [
        PERSON, {"@type": "WebSite", "@id": ORIGIN + BASE + "#site", "name": "MULA", "url": ORIGIN + BASE, "inLanguage": LANGS, "publisher": {"@id": PERSON["@id"]}},
        {"@type": "WebPage", "@id": url("home", lang, True) + "#page", "url": url("home", lang, True), "name": h["title"], "description": h["description"], "inLanguage": lang,
         "isPartOf": {"@id": ORIGIN + BASE + "#site"}, "about": {"@id": ORIGIN + BASE + "#app"}, "primaryImageOfPage": ORIGIN + A + f"og/home-{lang}.jpg"},
        app_ld(lang), faq_ld(h["faq"], lang)]}
    intro_js = ('try{if(!sessionStorage.getItem("mula-intro")&&!matchMedia("(prefers-reduced-motion: reduce)").matches)'
                'document.documentElement.classList.add("intro")}catch(_){}')
    out = [head(lang, "home", h["title"], h["description"], A + f"og/home-{lang}.jpg", h["og_alt"], ld, extra=intro_js), header(lang, "home")]

    # launch intro: the app's opening page, rebuilt for the web
    out.append(f"""
<div class="launch" aria-hidden="true"><div class="launch-in">{emblem("li")}<p class="l-word">MULA</p><p class="l-tag">{e(t['intro']['tagline'])}</p></div>
<button type="button" class="l-skip" tabindex="-1">{e(t['intro']['skip'])}</button></div>""")

    badges = "".join(f"<li>{icon('check', 16)}{e(b)}</li>" for b in h["badges"])
    ribbon = "".join(f'<span>{e(species_local(lang, s["id"])[0])}</span><i aria-hidden="true">·</i>' for s in SPECIES)
    photo = half_img("monstera", "photo", "", "hero-photo", False, "100vw")
    out.append(f"""
<section class="hero" id="top">
<div class="hero-photo-wrap" aria-hidden="true">{photo}</div>
<div class="sheet">
<div class="sheet-wave" aria-hidden="true"></div>
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow"><span class="today">{e(h['eyebrow'])}</span><span class="season" data-seasons="{e(json.dumps(t['seasons'], ensure_ascii=False))}"></span></p>
<h1 class="display">{e(h['h1'])}</h1>
<p class="lead">{e(h['lead'])}</p>
<div class="cta-row">{store_badge(lang, 'hero')}<a class="btn ghost" href="#soil">{icon('drop', 18)}<span>{e(h['cta_demo'])}</span></a></div>
<ul class="badges">{badges}</ul>
</div>
<div class="hero-art">
<div class="phone hero-phone"><div class="screen"><video class="launch-video" muted playsinline loop preload="metadata" poster="{A}video/launch-poster.webp" width="540" height="1174" aria-label="{e(h['phone_alt'])}"><source src="{A}video/launch.mp4" type="video/mp4"></video></div></div>
<button type="button" class="replay" aria-label="{e(h['replay'])}">{icon('spark', 16)}<span>{e(h['replay'])}</span></button>
</div>
</div>
</div>
</section>
<div class="ribbon" role="region" aria-label="{e(h['ribbon_label'])}"><div class="track">{ribbon}{ribbon}</div></div>
""")

    # faces: photo / paper portrait cards
    cards = "".join(f"""<button type="button" class="face reveal" style="--i:{i}" aria-pressed="false" aria-label="{e(nick)} — {e(species_local(lang, sid)[0])}">
<span class="face-in"><span class="side front">{half_img(sid, 'photo', '', '', True, '(max-width: 700px) 44vw, 220px')}</span><span class="side back">{half_img(sid, 'geo', '', '', True, '(max-width: 700px) 44vw, 220px')}</span></span>
<span class="face-cap"><b>{e(nick)}</b><small>{e(latin)}</small></span></button>""" for i, (nick, sid, latin) in enumerate(h["faces"]))
    out.append(f"""
<section class="section faces-sec" id="garden"><div class="wrap">
{section_head(h['faces_kicker'], h['faces_h2'], e(h['faces_lead']))}
<div class="faces">{cards}</div>
<p class="hint reveal">{icon('spark', 14)} {e(h['faces_hint'])}</p>
</div></section>""")

    # soil demo
    opts = "".join(f'<button type="button" class="opt" data-a="{k}" aria-pressed="{"true" if k == "dry" else "false"}"><i class="radio" aria-hidden="true"></i><span><b>{e(a)}</b><small>{e(b)}</small></span></button>' for k, a, b in h["soil_opts"])
    pts = "".join(f'<li class="reveal" style="--i:{i}">{icon("check", 18)}<span>{e(p)}</span></li>' for i, p in enumerate(h["soil_points"]))
    out.append(f"""
<section class="section band soil-sec" id="soil"><div class="wrap split">
<div>{section_head(h['soil_kicker'], h['soil_h2'], e(h['soil_lead']))}<ul class="ticks">{pts}</ul></div>
<div class="soil-demo reveal" data-state="dry">
<div class="pot" aria-hidden="true"><svg viewBox="0 0 320 260"><defs><clipPath id="soilclip"><path d="M40 70 H280 L256 236 Q254 250 240 250 H80 Q66 250 64 236 Z"/></clipPath></defs>
<g class="plant"><path class="st" d="M160 74 C160 40 162 26 168 10"/><path class="lf1" d="M160 52 C130 30 104 34 92 44 C112 58 138 62 160 52Z"/><path class="lf2" d="M163 36 C186 12 214 12 226 22 C206 38 184 42 163 36Z"/></g>
<g clip-path="url(#soilclip)"><rect class="soil" x="30" y="70" width="260" height="190"/><g class="drops"><circle cx="90" cy="120" r="4"/><circle cx="150" cy="160" r="5"/><circle cx="210" cy="118" r="4"/><circle cx="120" cy="208" r="4"/><circle cx="230" cy="196" r="5"/><circle cx="180" cy="226" r="3.5"/></g>
<g class="soilroots"><path d="M160 74 Q164 130 152 190"/><path d="M160 96 Q130 116 104 150"/><path d="M161 102 Q192 124 214 160"/></g></g>
<path class="rim" d="M32 62 H288 V76 H32 Z"/><path class="potline" d="M40 76 L64 236 Q66 250 80 250 H240 Q254 250 256 236 L280 76"/>
<g class="finger"><path d="M206 -6 C206 30 206 60 204 92 Q202 104 192 104 Q182 104 182 92 L182 -6 Z"/></g></svg></div>
<div class="sheet-card">
<p class="caps">{e(h['soil_eyebrow'])}</p>
<h3 class="display">{e(h['soil_q'])}</h3>
<div class="opts" role="group" aria-label="{e(h['soil_q'])}">{opts}</div>
<p class="result" aria-live="polite">{e(h['soil_res']['dry'].format(n=next(x for x in SPECIES if x['id'] == 'monstera')['water'][2]))}</p>
<div class="confirm"><span class="cbtn"><svg class="tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5 10 17.5 19.5 7"/></svg><span class="clabel">{e(h['soil_btn']['dry'])}</span></span></div>
</div>
</div>
</div></section>""")

    # seasons demo
    chips = "".join(f'<button type="button" class="chip" data-p="{i}" aria-pressed="{"true" if i == 0 else "false"}">{half_img(sid, "geo", "", "chip-img", True, "48px")}<span>{e(nick)}</span></button>' for i, (nick, sid, _) in enumerate(h["faces"]))
    stabs = "".join(f'<button type="button" class="stab" data-s="{i}" aria-pressed="false"><b>{e(s)}</b><small>{e(m)}</small></button>' for i, (s, m) in enumerate(zip(t["seasons"], t["season_months"])))
    out.append(f"""
<section class="section seasons-sec" id="seasons"><div class="wrap">
{section_head(h['seasons_kicker'], h['seasons_h2'], e(h['seasons_lead']))}
<div class="season-demo reveal">
<div class="chips" role="group" aria-label="{e(h['seasons_pick'])}">{chips}</div>
<div class="year">
<div class="wheel" aria-hidden="true"><svg viewBox="0 0 200 200"><g class="ring"><path class="q q0" d="M100 100 L100 8 A92 92 0 0 1 192 100Z"/><path class="q q1" d="M100 100 L192 100 A92 92 0 0 1 100 192Z"/><path class="q q2" d="M100 100 L100 192 A92 92 0 0 1 8 100Z"/><path class="q q3" d="M100 100 L8 100 A92 92 0 0 1 100 8Z"/></g><circle class="hub" cx="100" cy="100" r="56"/></svg><div class="wheel-art"></div></div>
<div class="plan">
<p class="caps plan-h"><span class="p-name"></span> · <span class="p-latin"></span></p>
<div class="stabs" role="group">{stabs}</div>
<p class="tipline display"></p>
<div class="rows">
<div class="row">{icon('drop', 20)}<div><b>{e(h['seasons_water'])}</b><small class="v-water"></small></div></div>
<div class="row">{icon('leaf', 20)}<div><b>{e(h['seasons_feed'])}</b><small class="v-feed"></small></div></div>
<div class="row">{icon('sun', 20)}<div><b class="v-light"></b><small class="v-place"></small></div></div>
<div class="row">{icon('frost', 20)}<div><b>{e(h['seasons_temp'])}</b><small class="v-temp"></small></div></div>
</div>
<p class="note">{e(h['seasons_note'])}</p>
</div></div></div>
</div></section>""")

    # features
    feats = "".join(f'<article class="feat reveal" style="--i:{i % 4}"><span class="f-ic">{icon(ic_, 24)}</span><h3>{e(ti)}</h3><p>{e(tx)}</p>{tier(lang, tr)}</article>' for i, (ic_, ti, tx, tr) in enumerate(h["features"]))
    out.append(f"""
<section class="section band" id="features"><div class="wrap">
{section_head(h['features_kicker'], h['features_h2'])}
<div class="feats">{feats}</div>
</div></section>""")

    # real screens
    screens = "".join(f'<figure class="scr" style="--i:{i}">{phone(k, lang, cap, "", True, "(max-width: 700px) 62vw, 260px")}<figcaption>{e(cap)}</figcaption></figure>' for i, (k, cap) in enumerate(h["screens"]))
    out.append(f"""
<section class="section screens-sec" id="screens"><div class="wrap">
{section_head(h['screens_kicker'], h['screens_h2'], e(h['screens_lead']))}</div>
<div class="screens" tabindex="0" aria-label="{e(h['screens_h2'])}"><div class="screens-track">{screens}</div></div>
<div class="wrap scr-nav"><button type="button" class="round prev" aria-label="←">{icon('arrow', 18)}</button><button type="button" class="round next" aria-label="→">{icon('arrow', 18)}</button></div>
</section>""")

    # light demo
    out.append(f"""
<section class="section band light-sec" id="light"><div class="wrap split rev">
<div>{section_head(h['light_kicker'], h['light_h2'], e(h['light_lead']))}<p class="note reveal">{e(h['light_note'])}</p></div>
<div class="light-demo reveal">
<div class="window" aria-hidden="true"><div class="beam"></div><div class="lsun"></div><div class="frame"><i></i><i></i></div></div>
<label class="caps" for="lux-{lang}">{e(h['light_label'])}</label>
<input id="lux-{lang}" class="lux" type="range" min="0" max="1000" value="560" aria-valuetext="">
<div class="scale"><span data-k="low">{e(t['light']['low'])}</span><span data-k="bright">{e(t['light']['bright'])}</span><span data-k="direct">{e(t['light']['direct'])}</span></div>
<p class="l-name display"></p><p class="l-val"></p>
<p class="caps">{e(h['light_fits'])}</p><ul class="fits"></ul>
</div>
</div></section>""")

    # everywhere: notifications, widgets, watch, siri
    items = "".join(f'<li class="reveal" style="--i:{i}"><b>{e(a)}</b><span>{e(b)}</span></li>' for i, (a, b) in enumerate(h["every_items"]))
    phrases = "".join(f'<li>“{e(p)}”</li>' for p in h["siri_phrases"])
    out.append(f"""
<section class="section every-sec" id="everywhere"><div class="wrap">
{section_head(h['every_kicker'], h['every_h2'], e(h['every_lead']))}
<div class="every">
<div class="every-art reveal">{widgets_fig(lang, h['widgets_alt'])}{watch_fig(h['watch_alt'], 'every-watch', 'soil')}
<div class="siri" aria-hidden="true"><span class="orb"></span><ul class="phrases">{phrases}</ul></div></div>
<ul class="every-list">{items}</ul>
</div>
</div></section>""")

    # why
    why = "".join(f'<p class="reveal" style="--i:{i}">{e(p)}</p>' for i, p in enumerate(h["why_p"]))
    out.append(f"""
<section class="section band why-sec" id="why"><div class="wrap split">
<div class="roots-art reveal" aria-hidden="true">{emblem("why")}</div>
<div><div class="section-head reveal"><p class="kicker">{e(h['why_kicker'])}</p><h2>{e(h['why_h2'])}</h2></div>{why}
<p class="reveal"><a class="btn ghost" href="{url('about', lang)}"><span>{e(h['why_link'])}</span>{icon('arrow', 18)}</a></p></div>
</div></section>""")

    # plans
    free = "".join(f"<li>{icon('check', 16)}{e(x)}</li>" for x in h["plans_free"])
    prem = "".join(f"<li>{icon('spark', 16)}{e(x)}</li>" for x in h["plans_premium"])
    out.append(f"""
<section class="section plans-sec" id="plans"><div class="wrap">
{section_head(h['plans_kicker'], h['plans_h2'])}
<div class="plans">
<div class="plan-card reveal"><h3>{e(h['plans_free_h'])}</h3><ul>{free}</ul></div>
<div class="plan-card prem reveal" style="--i:1"><img class="prem-art" src="{A}img/art/premium-800.webp" width="800" height="533" alt="" loading="lazy" decoding="async"><h3>{e(h['plans_premium_h'])}</h3><ul>{prem}</ul></div>
</div>
<p class="note center reveal">{e(h['plans_note'])}</p>
</div></section>""")

    # privacy
    pp = "".join(f'<div class="pp reveal" style="--i:{i}">{icon(ic_, 26)}<h3>{e(a)}</h3><p>{e(b)}</p></div>' for i, ((a, b), ic_) in enumerate(zip(h["privacy_points"], ("user", "spark", "phone", "lock"))))
    out.append(f"""
<section class="section band privacy-sec"><div class="wrap">
{section_head(h['privacy_kicker'], h['privacy_h2'])}
<div class="pps">{pp}</div>
<p class="center reveal"><a class="link" href="{url('privacy', lang)}">{e(h['privacy_link'])} →</a></p>
</div></section>""")

    # guides
    cards = "".join(guide_card(g, lang, i) for i, g in enumerate(GUIDES[:6]))
    out.append(f"""
<section class="section" id="guides"><div class="wrap">
{section_head(h['guides_kicker'], h['guides_h2'])}
<div class="g-grid">{cards}</div>
<p class="center reveal"><a class="btn ghost" href="{url('guides', lang)}"><span>{e(h['guides_link'])}</span>{icon('arrow', 18)}</a></p>
</div></section>""")

    # faq + final
    out.append(f"""
<section class="section band" id="faq"><div class="wrap narrow">
<div class="section-head reveal"><h2>{e(h['faq_h2'])}</h2></div>
{faq_html(h['faq'], lang)}
<p class="center reveal"><a class="link" href="{url('faq', lang)}">{e(h['faq_more'])} →</a></p>
</div></section>
<section class="final"><div class="wrap">
<img class="final-icon reveal" src="{A}img/app-icon-256.webp" width="120" height="120" alt="MULA" loading="lazy">
<h2 class="display reveal">{e(h['final_h2'])}</h2><p class="lead reveal">{e(h['final_p'])}</p>
<div class="reveal">{store_badge(lang, 'final')}</div>
</div></section>
<script type="application/json" id="mula-data">{json.dumps(demo_data(lang), ensure_ascii=False, separators=(",", ":"))}</script>""")
    out.append(footer(lang, "home"))
    write("home", lang, "".join(out))


# ---------------------------------------------------------------- about
def about(lang):
    t, p = C[lang], C[lang]["about"]
    items = [(t["nav"]["home"], url("home", lang, True)), (p["kicker"], url("about", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "AboutPage", "name": p["title"], "description": p["description"], "url": url("about", lang, True),
          "inLanguage": lang, "about": {"@id": ORIGIN + BASE + "#app"}, "author": {"@id": PERSON["@id"]}}, app_ld(lang), crumbs_ld(items)]}
    out = [head(lang, "about", p["title"], p["description"], A + f"og/about-{lang}.jpg", p["h1"], ld), header(lang, "about")]
    secs = "".join(f'<section class="reveal"><h2>{e(hh)}</h2>{links(b, lang)}</section>' for hh, b in p["sections"])
    prin = "".join(f'<li class="reveal" style="--i:{i}"><b>{e(a)}</b><span>{e(b)}</span></li>' for i, (a, b) in enumerate(p["principles"]))
    out.append(page_hero(items, p["kicker"], p["h1"], e(p["lead"]), art=f'<div class="about-emblem">{emblem("ab")}</div>'))
    out.append(f"""
<div class="wrap about-grid"><article class="prose">{secs}</article>
<aside class="aside"><div class="panel sticky"><h2 class="h5">{e(p['principles_h'])}</h2><ol class="principles">{prin}</ol>{store_badge(lang, 'about')}</div></aside></div>
<div class="wrap">{cta_box(lang, 'about')}</div>
""")
    out.append(footer(lang, "about"))
    write("about", lang, "".join(out))


# ---------------------------------------------------------------- guides
SHOT = re.compile(r"\[\[shot:([a-z0-9_]+)\|(.*?)\]\]", re.S)
ART = re.compile(r"\[\[art:([a-z]+)\|(.*?)\]\]", re.S)
TIP = re.compile(r"\[\[tip\|(.*?)\]\]", re.S)
CHECK = re.compile(r"\[\[checklist\|(.*?)\]\]", re.S)


def render_body(body, lang, gid="x"):
    n = {"check": 0}
    a = C[lang]["article"]

    def shot(m):
        cap = m.group(2)
        return f'<figure class="shot reveal">{phone(m.group(1), lang, strip(cap), "sm")}<figcaption>{cap}</figcaption></figure>'

    def art(m):
        return f'<figure class="art reveal">{art_img(m.group(1), strip(m.group(2)))}<figcaption>{m.group(2)}</figcaption></figure>'

    def tip(m):
        return f'<aside class="tip reveal">{mark(34)}<div><b class="caps">{e(a["tip"])}</b><p>{m.group(1)}</p></div></aside>'

    def check(m):
        n["check"] += 1
        items = [x.strip() for x in m.group(1).split(";;") if x.strip()]
        lis = "".join(f'<li><label><input type="checkbox" data-key="{gid}-{n["check"]}-{i}"><span>{e(x)}</span></label></li>' for i, x in enumerate(items))
        return f'<div class="checklist reveal"><ul>{lis}</ul></div>'

    body = SHOT.sub(shot, body)
    body = ART.sub(art, body)
    body = TIP.sub(tip, body)
    body = CHECK.sub(check, body)
    body = body.replace("[[cta]]", cta_box(lang, "guide"))
    body = links(body, lang)
    body = re.sub(r"<p>\s*(<figure|<div class=\"checklist|<aside)", r"\1", body)
    body = re.sub(r"(</figure>|</aside>|</ul></div>)\s*</p>", r"\1", body)
    body = re.sub(r"<h2>(.*?)</h2>", lambda m: f'<h2 id="{slugify(m.group(1))}">{m.group(1)}</h2>', body)
    body = re.sub(r"<table>", '<div class="table"><table>', body).replace("</table>", "</table></div>")
    return body


def slugify(s):
    s = strip(s).lower()
    for x, y in (("ç", "c"), ("ğ", "g"), ("ı", "i"), ("ö", "o"), ("ş", "s"), ("ü", "u"), ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n"), ("’", ""), ("'", "")):
        s = s.replace(x, y)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def date_text(iso, lang):
    y, m, d = map(int, iso.split("-"))
    months = C[lang]["months"]
    return {"en": f"{months[m - 1]} {d}, {y}", "tr": f"{d} {months[m - 1]} {y}", "es": f"{d} de {months[m - 1]} de {y}"}[lang]


def guide_page(g, lang):
    t, a, gl = C[lang], C[lang]["article"], g[lang]
    items = [(t["nav"]["home"], url("home", lang, True)), (t["nav"]["guides"], url("guides", lang, True)), (gl["h1"], url(g["id"], lang, True))]
    words = len(strip(gl["body"]).split())
    upd = g.get("updated", TODAY)
    art = {"@type": "Article", "headline": gl["h1"][:110], "alternativeHeadline": gl["title"], "description": gl["description"], "inLanguage": lang,
           "image": ORIGIN + A + f"og/{g['id']}-{lang}.jpg", "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
           "datePublished": upd, "dateModified": upd, "mainEntityOfPage": url(g["id"], lang, True),
           "wordCount": words, "about": [gl["kicker"], {"@id": ORIGIN + BASE + "#app"}], "abstract": gl["answer"]}
    if gl["sources"]:
        art["citation"] = [{"@type": "CreativeWork", "name": n, "url": u} for n, u in gl["sources"]]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, art, faq_ld(gl["faq"], lang), crumbs_ld(items)]}
    out = [head(lang, g["id"], gl["title"], gl["description"], A + f"og/{g['id']}-{lang}.jpg", gl["h1"], ld, "article"), header(lang, g["id"])]
    take = "".join(f"<li>{icon('check', 16)}<span>{e(x)}</span></li>" for x in gl["takeaways"])
    body = render_body(gl["body"], lang, g["id"])
    toc = "".join(f'<li><a href="#{i}">{hh}</a></li>' for i, hh in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body))
    src = ""
    if gl["sources"]:
        src = f'<h2 id="sources">{e(a["sources"])}</h2><ol class="sources">' + "".join(f'<li>{e(n)} <a href="{e(u)}" rel="noopener">{e(u.split("//")[-1].rstrip("/"))}</a></li>' for n, u in gl["sources"]) + "</ol>"
    related = [x for x in GUIDES if x["id"] != g["id"]]
    related = sorted(related, key=lambda x: (x["category"] != g["category"], x["order"]))[:3]
    rel = "".join(guide_card(x, lang, i) for i, x in enumerate(related))
    meta = (f'<p class="meta">{e(a["by"])} <a href="{url("about", lang)}">{AUTHOR}</a> · {e(a["updated"])} '
            f'<time datetime="{upd}">{date_text(upd, lang)}</time> · {e(read_minutes(gl, lang))}</p>')
    hero_art = f'<figure class="g-hero-art">{art_img(g["art"], "", "poster", False, "(max-width: 900px) 60vw, 340px")}</figure>'
    out.append(page_hero(items, gl["kicker"], gl["h1"], e(gl["description"]), meta, hero_art))
    out.append(f"""
<div class="wrap article"><article class="prose">
<div class="answer reveal"><p class="caps">{e(a['answer'])}</p><p>{e(gl['answer'])}</p></div>
<h2 id="key-points">{e(a['takeaways'])}</h2><ul class="takeaways">{take}</ul>
<nav class="toc" aria-label="{e(a['toc'])}"><p class="caps">{e(a['toc'])}</p><ol>{toc}</ol></nav>
{body}
<h2 id="faq">{e(a['faq'])}</h2>{faq_html([(q, e(x)) for q, x in gl['faq']], lang)}
{src}
</article>
<aside class="aside"><div class="panel sticky">{phone(g['shot'], lang, gl['h1'], 'sm', True, '240px')}<p class="caps center">MULA</p>{store_badge(lang, 'guide-aside')}</div></aside>
</div>
<section class="section"><div class="wrap"><div class="section-head reveal"><h2>{e(a['related'])}</h2></div><div class="g-grid">{rel}</div></div></section>
""")
    out.append(footer(lang, g["id"]))
    write(g["id"], lang, "".join(out))


def guides_index(lang):
    t, p = C[lang], C[lang]["guides_page"]
    items = [(t["nav"]["home"], url("home", lang, True)), (t["nav"]["guides"], url("guides", lang, True))]
    lst = {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(g["id"], lang, True), "name": g[lang]["h1"]} for i, g in enumerate(GUIDES)]}
    ld = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "CollectionPage", "name": p["title"], "description": p["description"], "url": url("guides", lang, True), "inLanguage": lang}, lst, crumbs_ld(items)]}
    out = [head(lang, "guides", p["title"], p["description"], A + f"og/guides-{lang}.jpg", p["h1"], ld), header(lang, "guides")]
    cats = [c for c in t["cats"] if any(g["category"] == c for g in GUIDES)]
    chips = f'<button type="button" class="chip on" data-cat="all" aria-pressed="true">{e(p["all"])}</button>' + "".join(
        f'<button type="button" class="chip" data-cat="{c}" aria-pressed="false">{e(t["cats"][c])}</button>' for c in cats)
    cards = "".join(guide_card(g, lang, i) for i, g in enumerate(GUIDES))
    out.append(page_hero(items, p["kicker"], p["h1"], e(p["lead"])))
    out.append(f"""<div class="wrap"><div class="filters reveal" role="group">{chips}</div><div class="g-grid all">{cards}</div>{cta_box(lang, 'guides')}</div>""")
    out.append(footer(lang, "guides"))
    write("guides", lang, "".join(out))


# ---------------------------------------------------------------- faq, support, privacy, terms
def faq_page(lang):
    t, p = C[lang], C[lang]["faq_page"]
    items = [(t["nav"]["home"], url("home", lang, True)), (t["nav"]["faq"], url("faq", lang, True))]
    pairs = [qa for _, grp in p["groups"] for qa in grp]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, faq_ld(pairs, lang), crumbs_ld(items)]}
    out = [head(lang, "faq", p["title"], p["description"], A + f"og/faq-{lang}.jpg", p["h1"], ld), header(lang, "faq")]
    lead = e(p["lead"]).replace(EMAIL, f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    out.append(page_hero(items, p["kicker"], p["h1"], lead))
    groups = "".join(f'<section class="faq-group"><h2 class="reveal" id="{slugify(gname)}">{e(gname)}</h2>{faq_html(grp, lang)}</section>' for gname, grp in p["groups"])
    out.append(f'<div class="wrap narrow">{groups}{cta_box(lang, "faq")}</div>')
    out.append(footer(lang, "faq"))
    write("faq", lang, "".join(out))


def support_page(lang):
    t, p = C[lang], C[lang]["support"]
    items = [(t["nav"]["home"], url("home", lang, True)), (t["nav"]["support"], url("support", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "ContactPage", "name": p["title"], "description": p["description"], "url": url("support", lang, True), "inLanguage": lang,
          "mainEntity": {"@type": "Organization", "name": "MULA", "email": EMAIL, "founder": {"@id": PERSON["@id"]},
                         "contactPoint": {"@type": "ContactPoint", "email": EMAIL, "contactType": "customer support", "availableLanguage": ["English", "Turkish", "Spanish"]}}}, crumbs_ld(items)]}
    out = [head(lang, "support", p["title"], p["description"], A + f"og/support-{lang}.jpg", p["h1"], ld), header(lang, "support")]
    lead = e(p["lead"]).replace(EMAIL, f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    mail = f"mailto:{EMAIL}?subject={e(p['write_subject'])}"
    btns = f'<div class="cta-row"><a class="btn" href="{mail}">{icon("mail", 18)}<span>{e(p["write"])}</span></a><a class="btn ghost" href="{url("faq", lang)}"><span>{e(p["faq_link"])}</span>{icon("arrow", 18)}</a></div>'
    out.append(page_hero(items, p["kicker"], p["h1"], lead, btns))
    fixes = "".join(f'<details class="fix reveal"><summary><span>{e(q)}</span><i aria-hidden="true"></i></summary><div>{links(a, lang)}</div></details>' for q, a in p["fixes"])
    out.append(f"""<div class="wrap narrow"><h2 class="reveal">{e(p['h_fix'])}</h2><div class="faq">{fixes}</div>
<h2 class="reveal">{e(p['h_contact'])}</h2><div class="panel prose reveal">{p['contact']}</div>{cta_box(lang, 'support')}</div>""")
    out.append(footer(lang, "support"))
    write("support", lang, "".join(out))


def legal_page(lang, key):
    t, p = C[lang], C[lang][key]
    items = [(t["nav"]["home"], url("home", lang, True)), (p["h1"], url(key, lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "WebPage", "name": p["h1"], "description": p["description"], "url": url(key, lang, True),
          "inLanguage": lang, "dateModified": TODAY, "about": {"@id": ORIGIN + BASE + "#app"}}, crumbs_ld(items)]}
    out = [head(lang, key, p["title"], p["description"], A + f"og/{key}-{lang}.jpg", p["h1"], ld), header(lang, key)]
    secs = "".join(f"<h2>{e(h)}</h2>{links(b, lang)}" for h, b in p["sections"])
    badges = '<ul class="badges">' + "".join(f"<li>{icon('check', 16)}{e(b)}</li>" for b in p["badges"]) + "</ul>" if "badges" in p else ""
    out.append(page_hero(items, p["kicker"], p["h1"], e(p["lead"]), f'{badges}<p class="meta">{e(p["effective"])} <time datetime="{TODAY}">{date_text(TODAY, lang)}</time></p>'))
    out.append(f'<div class="wrap narrow"><div class="legal panel prose">{secs}</div></div>')
    out.append(footer(lang, key))
    write(key, lang, "".join(out))


# ---------------------------------------------------------------- social cards (1200x630)
FONT_DISPLAY = os.path.join(SRC, "fonts", "CormorantGaramond-MediumItalic.ttf")
FONT_SANS = os.path.join(SRC, "fonts", "Jost-Medium.ttf")
FONT_SERIF = os.path.join(SRC, "fonts", "Lora-Medium.ttf")


def og_card(name, title, kicker, art, lang, shot=None):
    path = os.path.join(SITE, "assets", "og", f"{name}.jpg")
    sig = hashlib.sha1(json.dumps([title, kicker, art, shot, lang, 5]).encode()).hexdigest()[:10]
    stamp = os.path.join(SRC, ".og-cache", f"{name}.sig")
    os.makedirs(os.path.dirname(stamp), exist_ok=True)
    if os.path.exists(path) and os.path.exists(stamp) and open(stamp).read() == sig:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    W, H = 1200, 630
    im = Image.new("RGBA", (W, H), "#f2e7d9")
    grain = Image.open(os.path.join(SRC, "texture", "grain.png")).convert("RGBA")
    grain.putalpha(grain.getchannel("A").point(lambda a: round(a * .45)))
    for y in range(0, H, grain.height):
        for x in range(0, W, grain.width):
            im.alpha_composite(grain, (x, y))
    im = im.convert("RGB")
    d = ImageDraw.Draw(im)
    # right: the plant poster as a rounded card, or a phone
    if shot:
        s = Image.open(os.path.join(SITE, shot_src(shot, lang).replace(BASE, "", 1))).convert("RGB")
        sh = 560
        sw = round(s.width * sh / s.height)
        s = s.resize((sw, sh), Image.LANCZOS)
        x0, y0 = W - sw - 90, 35
        bez = Image.new("RGB", (sw + 24, sh + 24), "#243528")
        m = Image.new("L", bez.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, bez.width - 1, bez.height - 1), 52, fill=255)
        im.paste(bez, (x0 - 12, y0 - 12), m)
        m2 = Image.new("L", s.size, 0)
        ImageDraw.Draw(m2).rounded_rectangle((0, 0, sw - 1, sh - 1), 42, fill=255)
        im.paste(s, (x0, y0), m2)
        right = x0 - 12
    else:
        p = Image.open(os.path.join(SRC, "art", f"{art}-poster.jpg")).convert("RGB")
        ph = 560
        pw = round(p.width * ph / p.height)
        p = p.resize((pw, ph), Image.LANCZOS)
        x0, y0 = W - pw - 70, 35
        sh_ = Image.new("L", (pw + 40, ph + 40), 0)
        ImageDraw.Draw(sh_).rounded_rectangle((20, 26, pw + 20, ph + 26), 30, fill=90)
        sh_ = sh_.filter(ImageFilter.GaussianBlur(14))
        im.paste(Image.new("RGB", sh_.size, "#5f4a36"), (x0 - 20, y0 - 20), sh_)
        m = Image.new("L", (pw, ph), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, pw - 1, ph - 1), 28, fill=255)
        im.paste(p, (x0, y0), m)
        right = x0
    # wordmark
    icon_im = Image.open(os.path.join(SRC, "art", "appicon.png")).convert("RGB").resize((64, 64), Image.LANCZOS)
    m = Image.new("L", (64, 64), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, 63, 63), 15, fill=255)
    im.paste(icon_im, (64, 58), m)
    f_w = ImageFont.truetype(FONT_SANS, 30)
    x = 148
    for ch in "MULA":
        d.text((x, 72), ch, font=f_w, fill="#243528")
        x += d.textlength(ch, font=f_w) + 14
    f_k = ImageFont.truetype(FONT_SANS, 20)
    d.text((64, 176), kicker.upper(), font=f_k, fill="#90937f", spacing=4)
    maxw = right - 64 - 50
    size = 76
    while True:
        f_t = ImageFont.truetype(FONT_DISPLAY, size)
        words, lines, cur = title.split(), [], ""
        for w_ in words:
            test = (cur + " " + w_).strip()
            if d.textlength(test, font=f_t) <= maxw:
                cur = test
            else:
                lines.append(cur)
                cur = w_
        lines.append(cur)
        if len(lines) * size * 1.08 <= 300 or size <= 40:
            break
        size -= 4
    y = 214
    for line in lines:
        d.text((62, y), line, font=f_t, fill="#243528")
        y += round(size * 1.08)
    f_s = ImageFont.truetype(FONT_SERIF, 22)
    d.text((64, H - 78), "Care · Grow · Bloom", font=f_s, fill="#5f6856")
    d.ellipse((64 + d.textlength("Care · Grow · Bloom", font=f_s) + 18, H - 70, 64 + d.textlength("Care · Grow · Bloom", font=f_s) + 30, H - 58), fill="#c2452f")
    im.save(path, quality=84, optimize=True, progressive=True)
    open(stamp, "w").write(sig)


def og_all():
    for lang in LANGS:
        t = C[lang]
        og_card(f"home-{lang}", t["home"]["h1"], t["home"]["eyebrow"], None, lang, shot="today")
        og_card(f"about-{lang}", t["about"]["h1"], t["about"]["kicker"], "camellia", lang)
        og_card(f"guides-{lang}", t["guides_page"]["h1"], t["guides_page"]["kicker"], "hydrangea", lang)
        og_card(f"faq-{lang}", t["faq_page"]["h1"], t["faq_page"]["kicker"], "pilea", lang)
        og_card(f"support-{lang}", t["support"]["h1"], t["support"]["kicker"], "orchid", lang)
        og_card(f"privacy-{lang}", t["privacy"]["h1"], t["privacy"]["kicker"], "ficus", lang)
        og_card(f"terms-{lang}", t["terms"]["h1"], t["terms"]["kicker"], "monstera", lang)
        for g in GUIDES:
            og_card(f"{g['id']}-{lang}", g[lang]["h1"], g[lang]["kicker"], g["art"], lang)


# ---------------------------------------------------------------- sitemap, llms.txt, static files
def sitemap():
    rows = []
    for page in PATHS:
        for l in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{url(page, x, True)}"/>' for x in LANGS)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url(page, "en", True)}"/>'
            prio = "1.0" if page == "home" else "0.8" if page in GUIDE_IDS or page in ("about", "guides") else "0.5"
            rows.append(f"<url><loc>{url(page, l, True)}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority>{alts}</url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8").write(xml)


def md(s):
    s = re.sub(r"\[\[shot:[a-z0-9_]+\|(.*?)\]\]", r"(Screenshot: \1)", s, flags=re.S)
    s = re.sub(r"\[\[art:[a-z]+\|(.*?)\]\]", r"(Illustration: \1)", s, flags=re.S)
    s = re.sub(r"\[\[tip\|(.*?)\]\]", r"> Tip: \1", s, flags=re.S)
    s = re.sub(r"\[\[checklist\|(.*?)\]\]", lambda m: "\n".join("- [ ] " + x.strip() for x in m.group(1).split(";;") if x.strip()), s, flags=re.S)
    s = s.replace("[[cta]]", "")
    s = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", s)
    s = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", s)
    s = re.sub(r"<li>(.*?)</li>", r"- \1\n", s, flags=re.S)
    s = re.sub(r"<t[hd]>(.*?)</t[hd]>", r"| \1 ", s)
    s = re.sub(r"</tr>", "|\n", s)
    s = re.sub(r"</p>", "\n\n", s)
    s = re.sub(r'<a href="([^"]+)">(.*?)</a>', r"\2", s)
    s = re.sub(r"</?(strong|b)>", "**", s)
    s = re.sub(r"</?em>", "*", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = LINK.sub(lambda m: url(m.group(1), "en", True) if m.group(1) in PATHS else "", s)
    s = html.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def llms():
    h = C["en"]["home"]
    L = lambda page: " | ".join(f"[{l.upper()}]({url(page, l, True)})" for l in LANGS)
    lines = [
        "# MULA — Calm Plant & Flower Care App for iPhone (soil-check watering reminders)", "",
        "> MULA (App Store name “MULA: Plant Care”) is a calm, paper-textured plant and flower care app for iPhone "
        "(iOS 17+) and iPad (iPadOS 17+), also on Apple silicon Macs, with an Apple Watch app (watchOS 10+), Home and Lock Screen widgets and Siri, made by independent "
        "developer Gül Eda Aydemir. Instead of telling you to water on a fixed day, it asks how the soil feels "
        "(“Dry” logs a watering, “A little moist” asks again in 2 days, “Wet” skips the round). Every plant has a "
        "four-season care plan (water and feeding intervals, feeding pauses in the resting season, Southern "
        "hemisphere switch). It knows 20 plants (monstera, camellia, rubber plant, hydrangea, moth orchid, Chinese "
        "money plant, snake plant, peace lily, pothos, lavender, aloe, rose, tulip, cactus, Boston fern, English ivy, "
        "begonia, poinsettia, rosemary, areca palm) and any other plant with a general plan. Also: Emergency Care for "
        "very late checks, on-device photo identification of plant kinds, a photo journal with cut-paper plant "
        "portraits and posters, calm reminder sounds and garden music, Light Paper and Dark Forest themes. MULA "
        "Premium (Annual with a 1-week free trial, or Lifetime) adds unlimited plants (free: 10), plan editing, "
        "Vacation mode with a care sheet for plant sitters, a camera light meter (lux estimate), frost and heat "
        "alerts from Apple Weather for balcony plants, and answer buttons on larger widgets and Apple Watch. No ads, "
        "no account, no tracking; the garden stays on the iPhone and in the user's own iCloud (backup, sync across "
        "devices, optional shared garden), with only anonymous usage statistics sent (Google "
        "Analytics for Firebase, can be turned off). App interface in English; website in English, "
        "Turkish and Spanish.", "",
        f"- App Store: {STORE_CANON}",
        f"- Website (EN): {url('home', 'en', True)}",
        f"- Türkçe: {url('home', 'tr', True)}",
        f"- Español: {url('home', 'es', True)}",
        f"- Full text of the guides: {ORIGIN}{BASE}llms-full.txt",
        f"- Developer contact: {EMAIL}", "",
        "## Pages", "",
        f"- Launch page: {L('home')}", f"- Why we made MULA: {L('about')}", f"- Guides: {L('guides')}",
        f"- FAQ: {L('faq')}", f"- Support: {L('support')}", f"- Privacy policy: {L('privacy')}", f"- Terms of use: {L('terms')}", "",
        "## Guides (with short answers)", "",
    ]
    for g in GUIDES:
        lines += [f"### {g['en']['h1']}", L(g["id"]), "", g["en"]["answer"], ""]
    lines += ["## Frequently asked", ""]
    for q, a_ in h["faq"]:
        lines += [f"- **{q}** {strip(links(a_, 'en'))}"]
    lines += ["", "## Key facts", "",
              "- Platforms: iPhone (iOS 17 or later), iPad (iPadOS 17 or later), Macs with Apple silicon (the iPad app, “Designed for iPad”) and Apple Watch (watchOS 10 or later). The same garden on every device with Sync with iCloud. The light meter needs a back camera, so not on Mac. No Android or web version.",
              "- Price: free to download; optional MULA Premium, Annual with a 1-week free trial or Lifetime (one purchase). Prices are shown in the App Store.",
              "- Free version: up to 10 plants and 5 photos per plant, all reminders and soil checks, seasonal plans (view), temperature check, photo identification, small and Lock Screen widgets, Apple Watch list, Siri.",
              "- Privacy: no ads, no account, no tracking, no MULA server; plants, photos and notes stay on the iPhone and in the person's own iCloud (iCloud backup and Sync with iCloud, both on by default and free; sharing a garden with others is Premium). Only anonymous usage statistics are sent (Google Analytics for Firebase; no advertising ID, never plant names, notes or photos; opt-out in Settings → Your garden → Share anonymous usage). Weather alerts send only a location rounded to about 1 km to Apple Weather.",
              "- Not professional horticultural advice: plans are starting points; MULA does not diagnose pests or diseases; photo identification names plant kinds, not exact species.",
              "- Developer: Gül Eda Aydemir (independent iOS developer), also makes Solo.Shots and Solora.", ""]
    open(os.path.join(SITE, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))

    full = [lines[0], "", lines[2], ""]
    for lang in LANGS:
        for g in GUIDES:
            gl = g[lang]
            full += [f"# {gl['h1']}", f"URL: {url(g['id'], lang, True)}", f"Language: {lang}", "", f"**{C[lang]['article']['answer']}:** {gl['answer']}", ""]
            full += ["- " + x for x in gl["takeaways"]] + ["", md(gl["body"]), "", f"## {C[lang]['article']['faq']}", ""]
            for q, a_ in gl["faq"]:
                full += [f"**{q}**", a_, ""]
            if gl["sources"]:
                full += [f"## {C[lang]['article']['sources']}", ""] + [f"- {n} {u}" for n, u in gl["sources"]] + [""]
            full += ["---", ""]
    open(os.path.join(SITE, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(full))


VER = {}


def static_files():
    for f in ("mula.css", "mula.js"):
        src = os.path.join(SRC, "static", f)
        data = open(src, "rb").read()
        if f.endswith(".css"):  # cache-bust the paper textures the stylesheet points at
            def bust(m):
                p = os.path.join(SITE, "assets", m.group(1))
                h = hashlib.md5(open(p, "rb").read()).hexdigest()[:8] if os.path.exists(p) else "0"
                return f"url({m.group(1)}?v={h})"
            data = re.sub(r"url\((img/[a-z-]+\.webp)\)", bust, data.decode()).encode()
            out = os.path.join(SITE, "assets", f)
            open(out, "wb").write(data)
            VER["css"] = hashlib.md5(data).hexdigest()[:8]
            continue
        VER[f.split(".")[1]] = hashlib.md5(data).hexdigest()[:8]
        shutil.copy(src, os.path.join(SITE, "assets", f))


def check():
    """Light sanity checks of the generated pages."""
    problems = []
    for root, _, files in os.walk(SITE):
        if "/_src" in root:
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            s = open(os.path.join(root, f), encoding="utf-8").read()
            for href in re.findall(r'(?:href|src)="(/MULA/[^"#?]*)', s):
                p = os.path.join(SITE, href.replace(BASE, "", 1))
                if href.endswith("/"):
                    p = os.path.join(p, "index.html")
                if not os.path.exists(p):
                    problems.append(f"{os.path.relpath(os.path.join(root, f), SITE)}: missing {href}")
            if "[[" in s or "{{" in s:
                problems.append(f"{os.path.relpath(os.path.join(root, f), SITE)}: unrendered token")
    for g in GUIDES:
        for l in LANGS:
            gl = g[l]
            if len(gl["title"]) > 60:
                problems.append(f"{g['id']}/{l}: title {len(gl['title'])} chars")
            if not 120 <= len(gl["description"]) <= 165:
                problems.append(f"{g['id']}/{l}: description {len(gl['description'])} chars")
    for l in LANGS:
        for k in ("home", "about", "guides_page", "faq_page", "support", "privacy", "terms"):
            p = C[l][k]
            if len(p["title"]) > 65:
                problems.append(f"{k}/{l}: title {len(p['title'])} chars")
    print("\n".join(sorted(set(problems))) or "check ok")


if __name__ == "__main__":
    static_files()
    for lang in LANGS:
        home(lang)
        about(lang)
        guides_index(lang)
        faq_page(lang)
        support_page(lang)
        legal_page(lang, "privacy")
        legal_page(lang, "terms")
        for g in GUIDES:
            guide_page(g, lang)
    og_all()
    sitemap()
    llms()
    check()
