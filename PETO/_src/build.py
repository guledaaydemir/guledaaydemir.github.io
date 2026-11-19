#!/usr/bin/env python3
"""Builds the PETO website (EN / TR / ES) as static HTML for GitHub Pages, under /PETO/.

    python3 -I PETO/_src/assets.py     # first, when the app's art or the screenshots changed
    python3 -I PETO/_src/build.py      # pages, social cards, sitemap.xml, llms.txt, llms-full.txt, css/js

Copy lives in _src/content/{en,tr,es}.py, guides in _src/guides/*.py (see guides/FORMAT.md), app facts in
_src/FACTS.md. Never hand-edit the generated HTML.

Set APP_ID below to the App Store id as soon as Apple gives one: every store link, the Smart App Banner and
the structured data are built from that one value. While it is empty, store buttons show "coming soon".
"""
import glob, hashlib, html, json, os, re, runpy, shutil

from PIL import Image, ImageDraw, ImageFont

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(SRC)
ORIGIN = "https://guledaaydemir.github.io"
BASE = "/PETO/"
A = BASE + "assets/"
APP_ID = "6836239120"            # App Store id of PETO, digits only (e.g. "6812345678"). Empty = not on the store yet.
PT = "128720446"         # provider token used on the other app sites
EMAIL = "solostaseraofficial@gmail.com"
AUTHOR = "Gül Eda Aydemir"
TODAY = "2026-11-17"
LANGS = ["en", "tr", "es"]
APP_LANGS = ["en", "en-GB", "tr", "es", "es-MX", "pt-BR", "fr", "de", "it", "ja", "ko", "ar", "ru"]  # the app's own languages
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
SOON = {"en": "Coming soon to the App Store", "tr": "Çok yakında App Store'da", "es": "Muy pronto en el App Store"}

C = {l: runpy.run_path(os.path.join(SRC, "content", l + ".py"))["T"] for l in LANGS}
GUIDES = sorted((runpy.run_path(p)["GUIDE"] for p in glob.glob(os.path.join(SRC, "guides", "*.py"))), key=lambda g: g["order"])
for g in GUIDES:
    PATHS[g["id"]] = {l: GUIDE_DIR[l] + g[l]["slug"] + "/" for l in LANGS}
GUIDE_IDS = {g["id"] for g in GUIDES}
SPRITES = json.load(open(os.path.join(SRC, "sprites.json")))

e = lambda s: html.escape(str(s), quote=True)
strip = lambda s: re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", s)).strip()
LINK = re.compile(r"\{\{link:([a-z0-9-]+)\}\}")


def url(page, lang, absolute=False):
    if page == "demo":
        return url("home", lang, absolute) + "#demo"
    u = BASE + PATHS[page][lang]
    return ORIGIN + u if absolute else u


def store(lang, place):
    if not APP_ID:
        return "#get"
    return f"https://apps.apple.com/app/apple-store/id{APP_ID}?pt={PT}&ct=web-peto-{lang}-{place}&mt=8"


STORE_CANON = f"https://apps.apple.com/app/id{APP_ID}" if APP_ID else None


# ---------------------------------------------------------------- images
_dims = {}


def dims(rel):
    if rel not in _dims:
        p = os.path.join(SITE, rel.replace(BASE, "", 1))
        if rel.endswith(".svg"):
            m = re.search(r'width="(\d+)" height="(\d+)"', open(p).read(400))
            _dims[rel] = (int(m.group(1)), int(m.group(2)))
        else:
            with Image.open(p) as im:
                _dims[rel] = im.size
    return _dims[rel]


def shot_src(key, lang, w=720):
    rel = f"{A}img/shots/{lang}/{key}-{w}.webp"  # this language's screenshot when taken, English otherwise
    return rel if os.path.exists(os.path.join(SITE, rel.replace(BASE, "", 1))) else f"{A}img/shots/en/{key}-{w}.webp"


def shot_img(key, lang, alt, lazy=True, sizes="(max-width: 700px) 70vw, 300px"):
    s, b = shot_src(key, lang, 360), shot_src(key, lang, 720)
    w, h = dims(b)
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="{b}" srcset="{s} 360w, {b} 720w" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}"{load}>'


def phone(key, lang, alt, cls="", lazy=True):
    return f'<div class="phone {cls}"><div class="screen">{shot_img(key, lang, alt, lazy)}</div></div>'


def sp(name, alt="", size=64, cls="", lazy=True):
    load = ' loading="lazy" decoding="async"' if lazy else ""
    c = f' class="px {cls}"' if cls else ' class="px"'
    return f'<img{c} src="{A}img/sp/{name}.webp" width="{size}" height="{size}" alt="{e(alt)}"{load}>'


def ic_src(name):
    svg = os.path.join(SITE, "assets", "img", "ic", name + ".svg")
    return f"{A}img/ic/{name}.svg" if os.path.exists(svg) else f"{A}img/ic/{name}.webp"


def ic(name, size=32, alt="", cls=""):
    c = f' class="px {cls}"' if cls else ' class="px"'
    return f'<img{c} src="{ic_src(name)}" width="{size}" height="{size}" alt="{e(alt)}" loading="lazy" decoding="async">'


def motif(name, h=32, cls=""):
    w0, h0 = dims(f"{A}img/px/{name}.svg")
    c = f' class="px {cls}"' if cls else ' class="px"'
    return f'<img{c} src="{A}img/px/{name}.svg" width="{round(w0 * h / h0)}" height="{h}" alt="" loading="lazy" decoding="async">'


APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.37 12.76c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.77-3.32-1.8-1.41-.14-2.76.84-3.47.84-.72 0-1.82-.82-3-.8-1.54.02-2.96.9-3.76 2.27-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 1.23-.02 2.01-1.12 2.76-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.65zM14.1 6.02c.63-.77 1.06-1.83.94-2.89-.91.04-2.01.61-2.66 1.37-.58.67-1.09 1.75-.96 2.79 1.02.08 2.05-.52 2.68-1.27z"/></svg>')


def store_badge(lang, place, cls="store"):
    t = C[lang]["badge"]
    soon = "" if APP_ID else f' data-soon="{e(SOON[lang])}"'
    return (f'<a class="{cls}" href="{e(store(lang, place))}" aria-label="{e(t["aria"])}"{soon}>{APPLE}'
            f'<span>{e(t["top"])}<b>{e(t["big"])}</b></span></a>')


def tier(lang, t):
    return f'<span class="tag {t}">{e(C[lang][t])}</span>'


# ---------------------------------------------------------------- page frame
def head(lang, page, title, desc, og, og_alt, ld, og_type="website"):
    t = C[lang]
    canon = url(page, lang, True)
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(page, l, True)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{url(page, "en", True)}">'
    locs = "".join(f'<meta property="og:locale:alternate" content="{LOCALE[l]}">' for l in LANGS if l != lang)
    banner = f'\n<meta name="apple-itunes-app" content="app-id={APP_ID}">' if APP_ID else ""
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
<meta name="theme-color" content="#3e8c3a" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#2d6b2a" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">{banner}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="PETO">
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
<link rel="apple-touch-icon" href="{A}apple-touch-icon.png">
<link rel="preload" href="{A}fonts/pixelify-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{A}fonts/peto-pixel.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A}peto.css?v={VER['css']}">
<link rel="alternate" type="text/plain" href="{BASE}llms.txt" title="{e(t['llms_title'])}">
<script>document.documentElement.className="js";try{{var s=localStorage.getItem("peto-accent");if(s)document.documentElement.dataset.accent=s;if(localStorage.getItem("peto-font")==="clean")document.documentElement.dataset.font="clean"}}catch(_){{}}</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":"))}</script>
</head>"""


TABS = [("home", "tab_home"), ("about", "heart"), ("guides", "star"), ("faq", "bell"), ("support", "settings")]


def header(lang, page):
    t = C[lang]
    cur = "guides" if page in GUIDE_IDS else page
    nav = "".join(f'<a href="{url(p, lang)}"{" aria-current=page" if cur == p else ""}>{e(t["nav"][p])}</a>' for p, _ in TABS[1:])
    langs = "".join(f'<a href="{url(page, l)}" hreflang="{l}" lang="{l}"{" aria-current=true" if l == lang else ""} title="{e(C[l]["lang_name"])}">{l.upper()}</a>' for l in LANGS)
    tabs = "".join(f'<a href="{url(p, lang)}"{" aria-current=page" if cur == p else ""}>{ic(icon, 28)}<span>{e(t["nav"][p])}</span></a>' for p, icon in TABS)
    return f"""<body data-page="{e(page)}">
<a class="skip" href="#main">{e(t['skip'])}</a>
<header class="appbar"><div class="wrap">
<a class="brand" href="{url('home', lang)}" aria-label="{e(t['home_label'])}"><img src="{A}img/app-icon-256.webp" width="40" height="40" alt=""><span class="pp">PETO</span></a>
<nav class="topnav" aria-label="PETO">{nav}</nav>
<div class="langs" role="group" aria-label="{e(t['language'])}">{langs}</div>
<a class="btn sm gold get" href="{e(store(lang, 'nav'))}"{'' if APP_ID else f' data-soon="{e(SOON[lang])}"'}>{e(t['get'])}</a>
</div></header>
<nav class="tabbar" aria-label="PETO">{tabs}</nav>
<main id="main">"""


def footer(lang, page, extra_js=""):
    t, f = C[lang], C[lang]["foot"]
    gl = "".join(f'<li><a href="{url(g["id"], lang)}">{e(g[lang]["h1"] if len(g[lang]["h1"]) < 64 else g[lang]["title"])}</a></li>' for g in GUIDES[:5])
    parade = "".join(sp(f"pet_{s}_{SPRITES[s][i][0]}", cls=f"walker w{n}", size=48) for n, (s, i) in enumerate(
        [("dog", 0), ("cat", 1), ("rabbit", 0), ("dog", 6), ("hedgehog", 0), ("cat", 3)]))
    swatches = "".join(f'<button type="button" class="sw sw-{k}" data-accent="{k}" title="{e(n)}" aria-label="{e(f["theme"])}: {e(n)}"></button>'
                       for k, n, _ in t["home"]["themes"])
    hint = "".join(f'<a data-lang="{l}" lang="{l}" href="{url(page, l)}" hidden>{e(HINT[l])} →</a>' for l in LANGS if l != lang)
    return f"""</main>
<div class="kilim" aria-hidden="true"></div>
<div class="street" aria-hidden="true"><div class="skyline"></div><div class="parade">{parade}</div><div class="grass"></div></div>
<footer class="foot"><div class="wrap">
<div class="cols">
<div><a class="brand" href="{url('home', lang)}"><img src="{A}img/app-icon-256.webp" width="48" height="48" alt="" loading="lazy"><span class="pp">PETO</span></a><p>{e(f['tagline'])}</p>{store_badge(lang, 'footer')}</div>
<div><h2 class="h4">{e(f['app'])}</h2><ul><li><a href="{url('home', lang)}">{e(t['nav']['home'])}</a></li><li><a href="{url('about', lang)}">{e(t['nav']['about'])}</a></li><li><a href="{url('demo', lang)}">{e(f['demo'])}</a></li><li><a href="{url('faq', lang)}">{e(t['nav']['faq'])}</a></li></ul></div>
<div><h2 class="h4">{e(f['learn'])}</h2><ul>{gl}<li><a href="{url('guides', lang)}">{e(f['all_guides'])}</a></li></ul></div>
<div><h2 class="h4">{e(f['help'])}</h2><ul><li><a href="{url('support', lang)}">{e(t['nav']['support'])}</a></li><li><a href="{url('privacy', lang)}">{e(f['privacy'])}</a></li><li><a href="{url('terms', lang)}">{e(f['terms'])}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{BASE}llms.txt">llms.txt</a></li></ul></div>
</div>
<div class="foot-bar"><div class="swatches" role="group" aria-label="{e(f['theme'])}"><span>{e(f['theme'])}</span>{swatches}</div>
<small>{motif('nazar', 18)} {e(f['made'])} © 2026 {AUTHOR}. {e(f['apple'])}</small></div>
</div></footer>
<div class="lang-hint" role="region" aria-label="{e(t['language'])}">{hint}<button type="button" aria-label="{e(t['close'])}">×</button></div>
<div class="toast" role="status" aria-live="polite"></div>
<script src="{A}peto.js?v={VER['js']}" defer></script>{extra_js}
</body>
</html>
"""


def write(page, lang, body):
    path = os.path.join(SITE, PATHS[page][lang], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def sign(text, tag="span", cls=""):
    return f'<{tag} class="sign {cls}"><i></i>{e(text)}<i></i></{tag}>'


def section_head(kicker, h2, lead=None, extra=""):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="section-head reveal">{sign(kicker)}<h2>{e(h2)}</h2>{lead_html}{extra}</div>'


# ---------------------------------------------------------------- structured data
PERSON = {"@type": "Person", "@id": ORIGIN + "/#person", "name": AUTHOR, "alternateName": "Gul Eda Aydemir",
          "jobTitle": "Independent iOS developer", "url": ORIGIN + "/about/", "email": "mailto:" + EMAIL}


def app_ld(lang):
    t, h = C[lang], C[lang]["home"]
    ld = {"@type": ["MobileApplication", "SoftwareApplication"], "@id": ORIGIN + BASE + "#app", "name": "PETO",
          "alternateName": t["store_name"], "description": h["description"], "url": url("home", lang, True),
          "image": ORIGIN + A + "icon-512.png", "applicationCategory": "LifestyleApplication",
          "applicationSubCategory": "Pet care", "operatingSystem": "iOS 17, iPadOS 17, macOS 14, watchOS 10 or later",
          "availableOnDevice": ["iPhone", "iPad", "Mac", "Apple Watch"], "inLanguage": APP_LANGS,
          "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
          "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "category": "Free to download, optional in-app purchases"},
          "featureList": h["ld_features"], "keywords": h["ld_keywords"],
          "screenshot": [ORIGIN + shot_src(k, lang) for k in ("home", "pet", "routine", "calendar", "stats", "health")]}
    if STORE_CANON:
        ld["installUrl"] = ld["downloadUrl"] = STORE_CANON
        ld["sameAs"] = [STORE_CANON]
    return ld


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def crumbs_html(items):
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(f'<a href="{u.replace(ORIGIN, "")}">{e(n)}</a>' for n, u in items[:-1]) + "</nav>"


def faq_ld(pairs, lang):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(links(a, lang))}} for q, a in pairs]}


def links(s, lang):
    def link(m):
        if m.group(1) not in PATHS and m.group(1) != "demo":
            if os.environ.get("PETO_DRAFT"):
                print(f"draft: {m.group(1)!r} not written yet, linking the guides index")
                return url("guides", lang)
            raise SystemExit(f"unknown link target {m.group(1)!r}")
        return url(m.group(1), lang)
    return LINK.sub(link, s)


def faq_html(pairs, lang):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><div><p>{links(a, lang)}</p></div></details>" for q, a in pairs) + "</div>"


def cta_box(lang, place):
    t = C[lang]["cta_box"]
    return (f'<aside class="cta-box panel"><img class="icon" src="{A}img/app-icon-256.webp" width="96" height="96" alt="" loading="lazy">'
            f'<div><h3>{e(t["h"])}</h3><p>{e(t["p"])}</p>{store_badge(lang, place)}</div></aside>')


def page_hero(items, kicker, h1, lead, extra=""):
    return (f'<section class="page-hero"><div class="wrap">{crumbs_html(items)}{sign(kicker)}<h1>{e(h1)}</h1>'
            f'<p class="lead">{lead}</p>{extra}</div></section>')


# ---------------------------------------------------------------- home
def home(lang):
    t, h = C[lang], C[lang]["home"]
    ld = {"@context": "https://schema.org", "@graph": [
        PERSON, {"@type": "WebSite", "@id": ORIGIN + BASE + "#site", "name": "PETO", "url": ORIGIN + BASE, "inLanguage": LANGS, "publisher": {"@id": PERSON["@id"]}},
        {"@type": "WebPage", "@id": url("home", lang, True) + "#page", "url": url("home", lang, True), "name": h["title"], "description": h["description"], "inLanguage": lang,
         "isPartOf": {"@id": ORIGIN + BASE + "#site"}, "about": {"@id": ORIGIN + BASE + "#app"}, "primaryImageOfPage": ORIGIN + A + f"og/home-{lang}.jpg"},
        app_ld(lang), faq_ld(h["faq"], lang)]}
    out = [head(lang, "home", h["title"], h["description"], A + f"og/home-{lang}.jpg", h["og_alt"], ld), header(lang, "home")]

    slides = "".join(f'<div class="slide">{shot_img(k, lang, h["phone_alt"] if i == 0 else "", lazy=i > 0, sizes="(max-width: 900px) 62vw, 300px")}</div>'
                     for i, k in enumerate(("home", "pet", "calendar", "stats")))
    badges = "".join(f"<li>{e(b)}</li>" for b in h["badges"])
    soon = "" if APP_ID else f' data-soon="{e(SOON[lang])}"'
    parade = "".join(sp(n, size=56, cls=f"hero-walker h{i}", lazy=False) for i, n in enumerate(
        ("pet_dog_golden", "pet_cat_gray", "pet_rabbit_gray", "pet_dog_corgi", "pet_hamster_golden")))
    out.append(f"""
<section class="title-screen" id="top">
<div class="clouds" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="wrap hero-grid">
<div class="hero-copy">
<div class="logo-row"><img class="logo-icon" src="{A}img/app-icon-256.webp" width="112" height="112" alt="" fetchpriority="high"><h1 class="logo"><span class="pp">PETO</span><span class="sr"> — {e(h['eyebrow'])}</span></h1></div>
<p class="eyebrow pp">{e(h['eyebrow'])}</p>
<p class="lead">{e(h['lead'])}</p>
<nav class="start-menu" aria-label="{e(h['press_start'])}">
<a class="menu-item" href="{e(store(lang, 'hero'))}"{soon}>{APPLE}<span>{e(h['menu_store'])}</span></a>
<a class="menu-item" href="#demo">{ic('ball', 24)}<span>{e(h['menu_demo'])}</span></a>
<a class="menu-item" href="{url('guides', lang)}">{ic('star', 24)}<span>{e(h['menu_guides'])}</span></a>
</nav>
<p class="press-start pp" aria-hidden="true">{e(h['press_start'])}</p>
<ul class="badges">{badges}</ul>
</div>
<div class="hero-art">
<div class="hearts" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
<div class="phone hero-phone"><div class="screen slides">{slides}</div></div>
{sp('pet_dog_golden', 'Buddy', 96, 'buddy bob', lazy=False)}{sp('pet_cat_gray', 'Milo', 80, 'milo bob', lazy=False)}{sp('pet_rabbit_gray', 'Poppy', 80, 'poppy bob', lazy=False)}
<p class="tagline pp">{e(h['tagline'])} <span aria-hidden="true">♥</span></p>
</div>
</div>
<div class="ground" aria-hidden="true">{parade}</div>
</section>
<div class="marquee" aria-hidden="true"><div class="track">{''.join(f'<span>{e(p)}</span>' for p in h['marquee'] * 2)}</div></div>
""")

    steps = "".join(f'<div class="step panel reveal">{phone(k, lang, s_t, "sm")}<h3>{e(s_t)}</h3><p>{e(s_p)}</p></div>' for k, s_t, s_p in h["steps"])
    out.append(f"""
<section class="section" id="how"><div class="wrap">
{section_head(h['how_kicker'], h['how_h2'], e(h['how_lead']))}
<div class="steps">{steps}</div>
</div></section>
""")

    demo_strings = dict(t["demo"], storeUrl=store(lang, "demo"), soon="" if APP_ID else SOON[lang], sp=A + "img/sp/", ic=A + "img/ic/",
                        names={"dog": t["home"]["species"][0][1], "cat": t["home"]["species"][1][1], "rabbit": t["home"]["species"][2][1]})
    out.append(f"""
<section class="section band-grass" id="play"><div class="wrap">
{section_head(h['demo_kicker'], h['demo_h2'], e(h['demo_lead']))}
<div class="demo-box"><div class="demo" id="demo" role="application" aria-label="{e(h['demo_aria'])}"><noscript><p>{e(h['demo_note'])}</p></noscript></div>
<p class="demo-note">{e(h['demo_note'])}</p></div>
</div></section>
<div class="kilim" aria-hidden="true"></div>
""")

    slots = "".join(f'<button type="button" class="slot {tr}" data-item="{i}" aria-pressed="{"true" if i == 0 else "false"}" aria-controls="inv-text">{ic(icon, 40)}<span class="slot-name">{e(name)}</span>{tier(lang, tr)}</button>'
                    for i, (icon, name, tr, _) in enumerate(h["items"]))
    texts = "".join(f'<div class="item-text" data-item="{i}"{"" if i == 0 else " hidden"}><h3>{ic(icon, 28)}{e(name)} {tier(lang, tr)}</h3><p>{e(txt)}</p></div>'
                    for i, (icon, name, tr, txt) in enumerate(h["items"]))
    out.append(f"""
<section class="section" id="features"><div class="wrap">
{section_head(h['inv_kicker'], h['inv_h2'], e(h['inv_lead']))}
<div class="inventory reveal"><div class="slots" role="group" aria-label="{e(h['inv_kicker'])}">{slots}</div>
<div class="dialog" id="inv-text" aria-live="polite">{texts}<span class="more" aria-hidden="true">▼</span></div></div>
</div></section>
""")

    shots = "".join(f'<figure>{phone(k, lang, cap, "sm")}<figcaption>{e(cap)}</figcaption></figure>' for k, cap in h["shots"])
    out.append(f"""
<section class="section band-wood" id="screens"><div class="wrap">
{section_head(h['shots_kicker'], h['shots_h2'], e(h['shots_lead']))}
<div class="shots" tabindex="0" role="region" aria-label="{e(h['shots_h2'])}">{shots}</div>
</div></section>
""")

    species = "".join(f'<button type="button" class="sp-btn" data-species="{k}" aria-pressed="{"true" if i == 0 else "false"}">{sp(f"pet_{k}_{SPRITES[k][0][0]}", "", 48)}<span>{e(n)}</span></button>'
                      for i, (k, n) in enumerate(h["species"]))
    picker = {"sp": A + "img/sp/", "cat": SPRITES, "names": dict(h["species"]), "free": h["picker_free"], "premium": h["picker_premium"]}
    out.append(f"""
<section class="section" id="pets"><div class="wrap">
{section_head(h['pets_kicker'], h['pets_h2'], e(h['pets_lead']))}
<div class="picker panel reveal" data-picker='{e(json.dumps(picker, ensure_ascii=False))}'>
<div class="stage"><button type="button" class="arrow" data-step="-1" aria-label="{e(h['picker_prev'])}">◀</button>
<div class="big">{sp('pet_dog_golden', h['species'][0][1], 160, 'pick', lazy=False)}<p class="pick-name pp">{e(h['species'][0][1])} · Golden</p><p class="pick-tier">{tier(lang, 'free')}</p></div>
<button type="button" class="arrow" data-step="1" aria-label="{e(h['picker_next'])}">▶</button></div>
<div class="variants" role="group" aria-label="{e(h['picker_variant'])}"></div>
<div class="species" role="group" aria-label="{e(h['picker_species'])}">{species}</div>
</div>
</div></section>
<div class="kilim" aria-hidden="true"></div>
""")

    lines = "".join(f'<div class="line" data-line="{i}"{"" if i == 0 else " hidden"}>{sp(img, name, 72, "portrait")}<div><b class="who pp">{e(name)}</b><p>{e(txt)}</p></div></div>'
                    for i, (img, name, txt) in enumerate(h["why_lines"]))
    out.append(f"""
<section class="section band-cini" id="why"><div class="wrap narrow">
{section_head(h['why_kicker'], h['why_h2'])}
<div class="rpg panel reveal" data-rpg>{lines}<button type="button" class="next" aria-label="▼">▼</button></div>
<p class="center"><a class="btn" href="{url('about', lang)}">{ic('paw', 24)}{e(h['why_link'])}</a></p>
</div></section>
""")

    fl = "".join(f"<li>{e(x)}</li>" for x in h["free_list"])
    pl = "".join(f"<li>{e(x)}</li>" for x in h["premium_list"])
    plans = "".join(f'<div class="plan panel{" best" if i == 1 else ""}">{ic(icon, 44)}<h3 class="pp">{e(n)}</h3><p>{e(note)}</p></div>' for i, (icon, n, note) in enumerate(h["plans"]))
    out.append(f"""
<section class="section band-wood" id="shop"><div class="wrap">
{section_head(h['shop_kicker'], h['shop_h2'], e(h['shop_lead']))}
<div class="shop">
<div class="panel shelf reveal"><h3>{ic('paw', 32)}{e(h['free_h'])} {tier(lang, 'free')}</h3><ul class="ticks">{fl}</ul></div>
<div class="panel shelf premium reveal"><img class="hero-img" src="{A}img/premium-hero.webp" width="{dims(A + 'img/premium-hero.webp')[0]}" height="{dims(A + 'img/premium-hero.webp')[1]}" alt="PETO Premium" loading="lazy"><h3>{ic('crown', 32)}{e(h['premium_h'])} {tier(lang, 'premium')}</h3><ul class="ticks star">{pl}</ul></div>
</div>
<div class="plans">{plans}</div>
<p class="shop-note">{e(h['shop_note'])}</p>
</div></section>
""")

    prom = "".join(f'<div class="promise-card panel reveal">{motif(m, 56)}<h3>{e(ti)}</h3><p>{e(tx)}</p></div>' for m, ti, tx in h["promise"])
    out.append(f"""
<section class="section" id="promise"><div class="wrap">
<div class="section-head reveal">{motif('tulip', 40)}<h2>{e(h['promise_h2'])}</h2><p class="lead">{e(h['promise_lead'])}</p></div>
<div class="promises">{prom}</div>
</div></section>
""")

    themes = "".join(f'<button type="button" class="theme-btn sw-{k}" data-accent="{k}"><i></i><span>{e(n)}</span>{tier(lang, "premium") if p else tier(lang, "free")}</button>' for k, n, p in h["themes"])
    icons = "".join(f'<figure><img src="{A}img/appicons/{k}.webp" width="96" height="96" alt="{e(n)}" loading="lazy"><figcaption>{e(n)}</figcaption></figure>' for k, n in h["icons"])
    out.append(f"""
<section class="section band-grass" id="look"><div class="wrap">
{section_head(h['look_kicker'], h['look_h2'], e(h['look_lead']))}
<div class="themes reveal" role="group" aria-label="{e(t['foot']['theme'])}">{themes}</div>
<div class="appicons reveal">{icons}</div>
</div></section>
<div class="kilim" aria-hidden="true"></div>
""")

    out.append(f"""
<section class="section" id="guides"><div class="wrap">
{section_head(h['guides_kicker'], h['guides_h2'], e(h['guides_lead']))}
<div class="gcards">{''.join(guide_card(g, lang) for g in GUIDES[:6])}</div>
<p class="center"><a class="btn blue" href="{url('guides', lang)}">{ic('star', 24)}{e(h['guides_all'])}</a></p>
</div></section>
<section class="section tight"><div class="wrap narrow">
<div class="section-head reveal"><h2>{e(h['faq_h2'])}</h2></div>
{faq_html(h['faq'], lang)}
<p class="center"><a href="{url('faq', lang)}">{e(h['faq_all'])} →</a></p>
</div></section>
<section class="section final" id="get"><div class="wrap center">
<div class="final-pets" aria-hidden="true">{sp('pet_dog_golden', size=72)}{sp('pet_cat_gray', size=72)}{sp('pet_rabbit_gray', size=72)}{sp('pet_bird_blue', size=72)}{sp('pet_fish_goldfish', size=72)}</div>
<h2 class="pp">{e(h['final_h2'])}</h2><p class="lead">{e(h['final_p'])}</p>
{store_badge(lang, 'final', 'store big pulse')}
</div></section>
""")
    out.append(footer(lang, "home", f'\n<script type="application/json" id="demo-strings">{json.dumps(demo_strings, ensure_ascii=False)}</script>\n<script src="{A}demo.js?v={VER["demo"]}" defer></script>'))
    write("home", lang, "".join(out))


def guide_card(g, lang):
    gl = g[lang]
    sprites = "".join(sp(s, "", 40) for s in g["sprites"][:2])
    return (f'<a class="gcard panel reveal" data-cat="{g["category"]}" href="{url(g["id"], lang)}">'
            f'<div class="gc-top">{ic(g["icon"], 40)}<span class="cat">{e(C[lang]["cats"][g["category"]])}</span><span class="gc-pets">{sprites}</span></div>'
            f'<h3>{e(gl["h1"])}</h3><p>{e(gl["description"])}</p><span class="go pp">▶ {e(C[lang]["article"]["read"].format(n=read_minutes(gl)))}</span></a>')


def read_minutes(gl):
    return max(3, round(len(strip(gl["body"]).split()) / 220))


# ---------------------------------------------------------------- about
def about(lang):
    t, a = C[lang], C[lang]["about"]
    items = [(t["nav"]["home"], url("home", lang, True)), (a["h1"], url("about", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, app_ld(lang),
          {"@type": "AboutPage", "name": a["h1"], "headline": a["title"], "description": a["description"], "inLanguage": lang,
           "url": url("about", lang, True), "about": {"@id": ORIGIN + BASE + "#app"}, "author": {"@id": PERSON["@id"]},
           "image": ORIGIN + A + f"og/about-{lang}.jpg", "dateModified": TODAY}, crumbs_ld(items)]}
    out = [head(lang, "about", a["title"], a["description"], A + f"og/about-{lang}.jpg", a["h1"], ld), header(lang, "about")]
    speakers = ["pet_dog_golden", "pet_cat_gray", "pet_rabbit_gray", "pet_hamster_golden", "pet_bird_blue", "pet_turtle_redEared", "pet_cat_orange", "pet_dog_black"]
    secs = "".join(f'<section class="story panel reveal">{sp(speakers[i % len(speakers)], "", 64, "portrait")}<div><h2>{e(hh)}</h2>{links(b, lang)}</div></section>'
                   for i, (hh, b) in enumerate(a["sections"]))
    pr = "".join(f'<div class="principle panel">{ic(icon, 36)}<h3>{e(n)}</h3><p>{e(x)}</p></div>'
                 for icon, (n, x) in zip(("heart", "paw", "bell", "crown"), a["principles"]))
    extra = f'<div class="about-pets" aria-hidden="true">{sp("pet_dog_golden", size=72)}{motif("cay", 48)}{sp("pet_cat_gray", size=72)}{motif("nazar", 40)}{sp("pet_rabbit_gray", size=72)}</div>'
    out.append(f"""
{page_hero(items, a['kicker'], a['h1'], e(a['lead']), extra)}
<div class="wrap narrow">{secs}
<h2 class="center principles-h">{e(a['principles_h'])}</h2><div class="principles">{pr}</div>
{cta_box(lang, 'about')}</div>
""")
    out.append(footer(lang, "about"))
    write("about", lang, "".join(out))


# ---------------------------------------------------------------- guides
SHOT = re.compile(r"\[\[shot:([a-z_]+)\|(.*?)\]\]")
ENGLISH_NOTE = re.compile(r"\s*\((?:İngilizce(?: ekran(?: görüntüsü)?)?|ekran İngilizce|(?:pantalla|captura)(?: de pantalla)? en inglés|en inglés)\)", re.I)
TIP = re.compile(r"\[\[tip\|(.*?)\]\]", re.S)
CHECK = re.compile(r"\[\[checklist\|(.*?)\]\]", re.S)
TIP_PETS = ["pet_dog_golden", "pet_cat_orange", "pet_rabbit_lop", "pet_hamster_golden", "pet_bird_cockatiel"]


def render_body(body, lang, gid="x"):
    n = {"tip": 0, "check": 0}

    def shot(m):
        cap = m.group(2)
        if lang != "en" and f"/shots/{lang}/" in shot_src(m.group(1), lang):  # a native screenshot exists: drop "(screen in English)"
            cap = ENGLISH_NOTE.sub("", cap)
        return f'<figure class="shot">{phone(m.group(1), lang, strip(cap), "sm")}<figcaption>{cap}</figcaption></figure>'

    def tip(m):
        pet = TIP_PETS[(n["tip"] + len(gid)) % len(TIP_PETS)]
        n["tip"] += 1
        return f'<div class="tip">{sp(pet, "", 72)}<div class="bubble"><b class="t pp">{e(C[lang]["article"]["tip"])}</b><p>{m.group(1)}</p></div></div>'

    def check(m):
        n["check"] += 1
        items = [x.strip() for x in m.group(1).split(";;") if x.strip()]
        lis = "".join(f'<li><label><input type="checkbox" data-key="{gid}-{n["check"]}-{i}"><span>{e(x)}</span></label></li>' for i, x in enumerate(items))
        return f'<div class="checklist panel"><p class="cl-h">{ic("paw", 24)}{e(C[lang]["article"]["checklist"])}</p><ul>{lis}</ul></div>'

    body = SHOT.sub(shot, body)
    body = TIP.sub(tip, body)
    body = CHECK.sub(check, body)
    body = body.replace("[[cta]]", cta_box(lang, "guide"))
    body = links(body, lang)
    body = re.sub(r"<p>\s*(<figure|<div class=\"(?:tip|checklist)|<aside)", r"\1", body)
    body = re.sub(r"(</figure>|</aside>|</ul></div>|</p></div></div>)\s*</p>", r"\1", body)
    body = re.sub(r"<h2>(.*?)</h2>", lambda m: f'<h2 id="{slugify(m.group(1))}">{m.group(1)}</h2>', body)
    return body


def slugify(s):
    s = strip(s).lower()
    for a, b in (("ç", "c"), ("ğ", "g"), ("ı", "i"), ("ö", "o"), ("ş", "s"), ("ü", "u"), ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def aside(lang, current):
    t = C[lang]["article"]
    more = "".join(f'<li><a href="{url(g["id"], lang)}">{ic(g["icon"], 24)}<span>{e(g[lang]["h1"])}</span></a></li>' for g in GUIDES if g["id"] != current)
    return (f'<aside class="aside"><div class="panel"><h2 class="h4">{e(t["more"])}</h2><ul class="more">{more}</ul></div>'
            f'<div class="panel center">{sp("pet_dog_golden", "", 96, "bob")}<h2 class="h4">{e(t["demo_h"])}</h2><p>{e(t["demo_p"])}</p><a class="btn sm" href="{url("demo", lang)}">{e(t["demo_btn"])}</a></div></aside>')


def guide_page(g, lang):
    t, a, gl = C[lang], C[lang]["article"], g[lang]
    items = [(t["nav"]["home"], url("home", lang, True)), (t["nav"]["guides"], url("guides", lang, True)), (gl["h1"], url(g["id"], lang, True))]
    words = len(strip(gl["body"]).split())
    upd = g.get("updated", TODAY)
    art = {"@type": "Article", "headline": gl["h1"], "alternativeHeadline": gl["title"], "description": gl["description"], "inLanguage": lang,
           "image": ORIGIN + A + f"og/{g['id']}-{lang}.jpg", "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
           "datePublished": upd, "dateModified": upd, "mainEntityOfPage": url(g["id"], lang, True),
           "wordCount": words, "about": [gl["kicker"], {"@id": ORIGIN + BASE + "#app"}], "abstract": gl["answer"]}
    if gl["sources"]:
        art["citation"] = [{"@type": "CreativeWork", "name": n, "url": u} for n, u in gl["sources"]]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, art, faq_ld(gl["faq"], lang), crumbs_ld(items)]}
    out = [head(lang, g["id"], gl["title"], gl["description"], A + f"og/{g['id']}-{lang}.jpg", gl["h1"], ld, "article"), header(lang, g["id"])]
    take = "".join(f"<li>{e(x)}</li>" for x in gl["takeaways"])
    body = render_body(gl["body"], lang, g["id"])
    toc = "".join(f'<li><a href="#{i}">{hh}</a></li>' for i, hh in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body))
    src = ""
    if gl["sources"]:
        src = f'<h2 id="sources">{e(a["sources"])}</h2><ol class="sources">' + "".join(f'<li>{e(n)} <a href="{e(u)}" rel="noopener">{e(u)}</a></li>' for n, u in gl["sources"]) + "</ol>"
    pets = "".join(sp(s, "", 64, "bob") for s in g["sprites"][:3])
    out.append(f"""
<section class="page-hero guide-hero"><div class="wrap hero2">
<div>{crumbs_html(items)}{sign(gl['kicker'])}<h1>{e(gl['h1'])}</h1>
<p class="meta">{e(a['by'])} <a href="{url('about', lang)}">{AUTHOR}</a> · {e(a['updated'])} <time datetime="{upd}">{date_text(upd, lang)}</time> · {e(a['read'].format(n=read_minutes(gl)))}</p>
<div class="hero-pets" aria-hidden="true">{pets}</div></div>
{phone(g['shot'], lang, gl['h1'], 'sm tilt', lazy=False)}
</div></section>
<div class="wrap"><div class="article"><article class="prose">
<div class="reading" role="group" aria-label="{e(a['font'])}"><span>{e(a['font'])}</span><button type="button" data-font="pixel">{e(a['font_pixel'])}</button><button type="button" data-font="clean">{e(a['font_clean'])}</button></div>
<div class="answer panel"><span class="lbl pp">{e(a['answer'])}</span><p>{e(gl['answer'])}</p></div>
<h2 id="key-points">{e(a['takeaways'])}</h2><ul class="takeaways">{take}</ul>
<nav class="toc panel" aria-label="{e(a['toc'])}"><b>{e(a['toc'])}</b><ol>{toc}</ol></nav>
{body}
<h2 id="faq">{e(a['faq'])}</h2>{faq_html([(q, e(x)) for q, x in gl['faq']], lang)}
{src}
</article>
{aside(lang, g['id'])}
</div></div>
""")
    out.append(footer(lang, g["id"]))
    write(g["id"], lang, "".join(out))


def date_text(iso, lang):
    y, m, d = map(int, iso.split("-"))
    months = C[lang]["months"]
    return {"en": f"{months[m - 1]} {d}, {y}", "tr": f"{d} {months[m - 1]} {y}", "es": f"{d} de {months[m - 1]} de {y}"}[lang]


def guides_index(lang):
    t, gp = C[lang], C[lang]["guides_page"]
    items = [(t["nav"]["home"], url("home", lang, True)), (gp["h1"], url("guides", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON,
          {"@type": "CollectionPage", "name": gp["h1"], "description": gp["description"], "url": url("guides", lang, True), "inLanguage": lang,
           "hasPart": [{"@type": "Article", "headline": g[lang]["h1"], "url": url(g["id"], lang, True)} for g in GUIDES]},
          crumbs_ld(items)]}
    out = [head(lang, "guides", gp["title"], gp["description"], A + f"og/guides-{lang}.jpg", gp["h1"], ld), header(lang, "guides")]
    cats = [c for c in t["cats"] if any(g["category"] == c for g in GUIDES)]
    filt = "".join(f'<button type="button" data-cat="{k}" aria-pressed="{"true" if k == "all" else "false"}">{e(v)}</button>'
                   for k, v in [("all", gp["all"])] + [(c, t["cats"][c]) for c in cats])
    out.append(f"""
{page_hero(items, gp['kicker'], gp['h1'], e(gp['lead']))}
<section class="section tight"><div class="wrap">
<div class="filters" role="group" aria-label="{e(gp['filter'])}">{filt}</div>
<div class="gcards">{''.join(guide_card(g, lang) for g in GUIDES)}</div>
</div></section>
""")
    out.append(footer(lang, "guides"))
    write("guides", lang, "".join(out))


# ---------------------------------------------------------------- faq, support, privacy, terms
def faq_page(lang):
    t, f = C[lang], C[lang]["faq"]
    items = [(t["nav"]["home"], url("home", lang, True)), (f["h1"], url("faq", lang, True))]
    pairs = [p for _, ps in f["groups"] for p in ps]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, faq_ld(pairs, lang), crumbs_ld(items)]}
    out = [head(lang, "faq", f["title"], f["description"], A + f"og/faq-{lang}.jpg", f["h1"], ld), header(lang, "faq")]
    icons = ["paw", "bell", "heart", "leash", "crown", "nazar"]
    groups = "".join(f'<h2 class="faq-group">{motif("nazar", 26) if icons[i % 6] == "nazar" else ic(icons[i % 6], 30)}{e(gt)}</h2>{faq_html(ps, lang)}' for i, (gt, ps) in enumerate(f["groups"]))
    out.append(f"""
{page_hero(items, f['kicker'], f['h1'], links(f['lead'], lang))}
<section class="section tight"><div class="wrap narrow">{groups}
<div class="spacer"></div>{cta_box(lang, 'faq')}</div></section>
""")
    out.append(footer(lang, "faq"))
    write("faq", lang, "".join(out))


def support_page(lang):
    t, s = C[lang], C[lang]["support"]
    items = [(t["nav"]["home"], url("home", lang, True)), (s["h1"], url("support", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON,
          {"@type": "ContactPage", "name": s["h1"], "description": s["description"], "url": url("support", lang, True), "inLanguage": lang,
           "mainEntity": {"@type": "ContactPoint", "contactType": "customer support", "email": EMAIL, "availableLanguage": ["Turkish", "English", "Spanish"]}},
          faq_ld(s["quick"], lang), crumbs_ld(items)]}
    mail = f"mailto:{EMAIL}?subject={s['mail_subject'].replace(' ', '%20')}"
    out = [head(lang, "support", s["title"], s["description"], A + f"og/support-{lang}.jpg", s["h1"], ld), header(lang, "support")]
    checklist = "".join(f"<li>{e(x)}</li>" for x in s["include"])
    quick_id = "quick-start" if "quick-start" in PATHS else "guides"
    out.append(f"""
{page_hero(items, s['kicker'], s['h1'], e(s['lead']))}
<section class="section tight"><div class="wrap">
<div class="support-grid">
<div class="panel mailbox">{sp('pet_bird_blue', '', 80, 'bob')}<h2>{e(s['contact_h'])}</h2><p>{e(s['contact_p'])}</p><p><a class="btn" href="{e(mail)}">{ic('heart', 24)}{e(s['mail_btn'])}</a></p><p class="muted">{EMAIL}</p></div>
<div class="panel"><h2>{e(s['include_h'])}</h2><ul class="ticks">{checklist}</ul></div>
</div>
<div class="narrow"><h2 class="faq-group">{ic('settings', 30)}{e(s['quick_h'])}</h2>{faq_html(s['quick'], lang)}
<h2 class="faq-group">{ic('star', 30)}{e(s['more_h'])}</h2>
<p>{s['more_p'].format(faq=url('faq', lang), guide=url(quick_id, lang), privacy=url('privacy', lang))}</p></div>
</div></section>
""")
    out.append(footer(lang, "support"))
    write("support", lang, "".join(out))


def legal_page(lang, key):
    t, p = C[lang], C[lang][key]
    items = [(t["nav"]["home"], url("home", lang, True)), (p["h1"], url(key, lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "WebPage", "name": p["h1"], "description": p["description"], "url": url(key, lang, True),
          "inLanguage": lang, "dateModified": TODAY, "about": {"@id": ORIGIN + BASE + "#app"}}, crumbs_ld(items)]}
    out = [head(lang, key, p["title"], p["description"], A + f"og/{key}-{lang}.jpg", p["h1"], ld), header(lang, key)]
    secs = "".join(f"<h2>{e(h)}</h2>{links(b, lang)}" for h, b in p["sections"])
    badges = "<ul class=\"badges\">" + "".join(f"<li>{e(b)}</li>" for b in p["badges"]) + "</ul>" if "badges" in p else ""
    out.append(f"""
{page_hero(items, p['kicker'], p['h1'], e(p['lead']), f'<p class="meta">{e(p["effective"])} <time datetime="{TODAY}">{date_text(TODAY, lang)}</time></p>')}
<div class="wrap narrow"><div class="legal panel prose">{badges}{secs}</div></div>
""")
    out.append(footer(lang, key))
    write(key, lang, "".join(out))


# ---------------------------------------------------------------- social cards (1200x630)
FONT_UI = os.path.join(SRC, "fonts", "PixelifySans.ttf")
FONT_PX = os.path.join(SRC, "fonts", "peto-pixel.ttf")


def og_card(name, title, kicker, shot_key, lang, sprites):
    path = os.path.join(SITE, "assets", "og", f"{name}.jpg")
    sig = hashlib.sha1(json.dumps([title, kicker, shot_key, lang, sprites, 3]).encode()).hexdigest()[:10]
    stamp = os.path.join(SRC, ".og-cache", f"{name}.sig")  # build cache, kept out of the published assets
    os.makedirs(os.path.dirname(stamp), exist_ok=True)
    if os.path.exists(path) and os.path.exists(stamp) and open(stamp).read() == sig:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), "#F5DF93")
    d = ImageDraw.Draw(im)
    for y in range(8, H, 24):
        for x in range(8 + (12 if (y // 24) % 2 else 0), W, 24):
            d.rectangle([x, y, x + 3, y + 3], fill="#F0D57F")
    d.rectangle([0, 0, W, 86], fill="#3E8C3A")
    d.rectangle([0, 86, W, 94], fill="#4A2E12")
    icon = Image.open(os.path.join(SITE, "assets", "img", "app-icon-256.webp")).convert("RGB").resize((62, 62), Image.LANCZOS)
    im.paste(icon, (40, 12))
    px = ImageFont.truetype(FONT_PX, 50)
    d.text((118, 18), "PETO", font=px, fill="#4A2E12")
    d.text((114, 14), "PETO", font=px, fill="#FFF8E6")
    # kilim strip at the bottom
    y0 = H - 36
    cols = ["#4A2E12", "#D9372B", "#E39A2E", "#1F4F9C", "#FDF6DF"]
    for x in range(0, W, 12):
        d.rectangle([x, y0, x + 11, H], fill=cols[(x // 12) % 2 + 1])
        d.rectangle([x + 3, y0 + 12, x + 8, y0 + 23], fill=cols[3 + (x // 12) % 2])
    d.rectangle([0, y0 - 6, W, y0], fill="#4A2E12")
    # phone with the screenshot
    shot = Image.open(os.path.join(SITE, shot_src(shot_key, lang).replace(BASE, "", 1))).convert("RGB")
    sh = 468
    sw = round(shot.width * sh / shot.height)
    shot = shot.resize((sw, sh), Image.LANCZOS)
    px0, py0 = W - sw - 70, 112
    d.rectangle([px0 - 14 + 8, py0 - 14 + 8, px0 + sw + 14 + 8, py0 + sh + 14 + 8], fill="#C9A84C")
    d.rectangle([px0 - 14, py0 - 14, px0 + sw + 14, py0 + sh + 14], fill="#2B1D0E")
    im.paste(shot.crop((0, 0, sw, sh)), (px0, py0))
    # kicker sign
    f_k = ImageFont.truetype(FONT_PX, 26)
    kw = d.textlength(kicker.upper(), font=f_k)
    d.rectangle([60, 126, 60 + kw + 40, 172], fill="#5C3A18")
    d.rectangle([64, 130, 56 + kw + 40, 168], fill="#9C6632")
    d.text((80, 136), kicker.upper(), font=f_k, fill="#FFF8E6")
    # title, wrapped
    maxw = px0 - 120
    size = 64
    while True:
        f_t = ImageFont.truetype(FONT_UI, size)
        words, lines, cur = title.split(), [], ""
        for w_ in words:
            test = (cur + " " + w_).strip()
            if d.textlength(test, font=f_t) <= maxw:
                cur = test
            else:
                lines.append(cur); cur = w_
        lines.append(cur)
        if len(lines) * size * 1.18 <= 300 or size <= 36:
            break
        size -= 4
    y = 196
    for line in lines:
        d.text((63, y + 3), line, font=f_t, fill="#E2CFA3")
        d.text((60, y), line, font=f_t, fill="#2B1D0E")
        y += round(size * 1.18)
    # pets
    x = 60
    for s in sprites[:3]:
        spi = Image.open(os.path.join(SITE, "assets", "img", "sp", s + ".webp")).convert("RGBA").resize((96, 96), Image.NEAREST)
        im.paste(spi, (x, H - 36 - 6 - 96), spi)
        x += 108
    im.save(path, quality=88, optimize=True, progressive=True)
    open(stamp, "w").write(sig)


def og_all():
    for lang in LANGS:
        t = C[lang]
        og_card(f"home-{lang}", t["home"]["title"].split("—")[-1].strip(), t["home"]["eyebrow"], "home", lang, ["pet_dog_golden", "pet_cat_gray", "pet_rabbit_gray"])
        og_card(f"about-{lang}", t["about"]["h1"], t["about"]["kicker"], "pet", lang, ["pet_dog_golden", "pet_cat_orange"])
        og_card(f"guides-{lang}", t["guides_page"]["h1"], t["guides_page"]["kicker"], "routine", lang, ["pet_dog_corgi", "pet_cat_tuxedo", "pet_rabbit_lop"])
        og_card(f"faq-{lang}", t["faq"]["h1"], t["faq"]["kicker"], "settings", lang, ["pet_hamster_golden", "pet_bird_blue"])
        og_card(f"support-{lang}", t["support"]["h1"], t["support"]["kicker"], "settings", lang, ["pet_bird_blue", "pet_dog_golden"])
        og_card(f"privacy-{lang}", t["privacy"]["h1"], t["privacy"]["kicker"], "home", lang, ["pet_cat_gray"])
        og_card(f"terms-{lang}", t["terms"]["h1"], t["terms"]["kicker"], "home", lang, ["pet_turtle_redEared"])
        for g in GUIDES:
            og_card(f"{g['id']}-{lang}", g[lang]["h1"], g[lang]["kicker"], g["shot"], lang, g["sprites"])


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
    """Very small HTML -> Markdown for llms-full.txt."""
    s = re.sub(r"\[\[shot:[a-z_]+\|(.*?)\]\]", r"(Screenshot: \1)", s)
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
    s = html.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def llms():
    facts = open(os.path.join(SRC, "FACTS.md"), encoding="utf-8").read()
    facts = re.sub(r"\s*<!--.*?-->", "", facts[facts.index("\n## "):], flags=re.S).strip().replace("## ", "### ")  # public facts only, no writer notes
    intro = ("> PETO is a retro pixel-game pet-care routine app for iPhone, iPad and Apple Watch by independent developer Gül Eda Aydemir. "
             "It reminds you about feeding, walks, playtime, cuddles, medication and vet visits (with Fed ✓ / Snooze / Skip actions on the notification), "
             "logs care with one tap, keeps a health record with vaccine booster reminders and a weight chart, tracks a cat's litter box, water and toilet "
             "habits, schedules aquarium cleaning every N days, can play your own pet's bark or meow as the reminder sound, offers a gentle memorial mode "
             "when a pet dies, dresses pets in seasonal pixel outfits, makes a pet-sitter care card and a yearly PETO Wrapped, tracks dog walks on Apple "
             "Watch, and (Premium) shares one household over iCloud so families see who fed the pet. 13 species, 104 pixel avatars. Built for iPhone, iPad "
             "and Mac. Free to download; optional Premium monthly, yearly or lifetime (one purchase covers iPhone, iPad and Mac). No ads, no account, no "
             "tracking; pet data stays on the device; anonymous usage statistics can be turned off in Settings. App in 13 languages (including English, "
             "Turkish and Spanish); website in English, Turkish and Spanish.")
    store_line = f"- App Store: {STORE_CANON}" if STORE_CANON else "- App Store: coming soon (the link will be added here)"
    lines = ["# PETO — Retro Pet Care Routine & Reminder App (iPhone, iPad, Apple Watch)", "", intro, "",
             store_line, f"- Website (EN): {url('home', 'en', True)}", f"- Türkçe: {url('home', 'tr', True)}",
             f"- Español: {url('home', 'es', True)}", f"- Full text of the guides: {ORIGIN}{BASE}llms-full.txt", f"- Developer contact: {EMAIL}", "",
             "## Pages", ""]
    for page, label in (("home", "Launch page"), ("about", "Why we made PETO"), ("guides", "Guides"), ("faq", "FAQ"), ("support", "Support"), ("privacy", "Privacy policy"), ("terms", "Terms of use")):
        lines.append(f"- {label}: " + " | ".join(f"[{l.upper()}]({url(page, l, True)})" for l in LANGS))
    lines += ["", "## Guides (with short answers)", ""]
    for g in GUIDES:
        lines += [f"### {g['en']['h1']}", " | ".join(f"[{l.upper()}]({url(g['id'], l, True)})" for l in LANGS), "", g["en"]["answer"], ""]
    lines += ["## Frequently asked", ""]
    for _, ps in C["en"]["faq"]["groups"]:
        for q, a in ps:
            lines.append(f"- **{q}** {strip(links(a, 'en'))}")
    lines += ["", "## Facts about the app", "", facts, ""]
    open(os.path.join(SITE, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))

    full = ["# PETO guides — full text (English)", "", intro, ""]
    for g in GUIDES:
        gl = g["en"]
        full += [f"# {gl['h1']}", "", f"URL: {url(g['id'], 'en', True)}", "", f"**Quick answer:** {gl['answer']}", "",
                 "Key points:", *[f"- {x}" for x in gl["takeaways"]], "", md(links(gl["body"], "en")), "", "## Questions people ask", ""]
        full += [f"**{q}** {a}\n" for q, a in gl["faq"]]
        if gl["sources"]:
            full += ["Sources:", *[f"- {n} {u}" for n, u in gl["sources"]]]
        full += ["", "---", ""]
    open(os.path.join(SITE, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(full))


VER = {}


def static_files():
    for name, key in (("peto.css", "css"), ("peto.js", "js"), ("demo.js", "demo")):
        src = os.path.join(SRC, "static", name)
        data = open(src, "rb").read()
        VER[key] = hashlib.sha1(data).hexdigest()[:8]
        shutil.copyfile(src, os.path.join(SITE, "assets", name))


def check():
    def cmp(a, b, p):
        if isinstance(a, dict):
            if set(a) != set(b):
                raise SystemExit(f"content keys differ at {p}: {sorted(set(a) ^ set(b))}")
            for k in a:
                cmp(a[k], b[k], f"{p}.{k}")
        elif isinstance(a, (list, tuple)):
            if len(a) != len(b):
                raise SystemExit(f"content length differs at {p}: {len(a)} vs {len(b)}")
            for i, (x, y) in enumerate(zip(a, b)):
                cmp(x, y, f"{p}[{i}]")
    for l in LANGS[1:]:
        cmp(C["en"], C[l], l)
    for g in GUIDES:
        for l in LANGS:
            gl = g[l]
            for key in ("slug", "title", "description", "h1", "kicker", "answer", "takeaways", "body", "faq", "sources"):
                if key not in gl:
                    raise SystemExit(f"guide {g['id']} {l} lacks {key}")
            if gl["body"].count("[[cta]]") != 1:
                print(f"note: {g['id']} {l} has {gl['body'].count('[[cta]]')} [[cta]] tokens")
            if len(gl["title"]) > 60:
                print(f"note: {g['id']} {l} title is {len(gl['title'])} chars")
            for k in SHOT.findall(gl["body"]):
                if not os.path.exists(os.path.join(SITE, shot_src(k[0], l).replace(BASE, "", 1))):
                    raise SystemExit(f"guide {g['id']} {l}: unknown screenshot {k[0]!r}")
        for s in g["sprites"]:
            if not os.path.exists(os.path.join(SITE, "assets", "img", "sp", s + ".webp")):
                raise SystemExit(f"guide {g['id']}: unknown sprite {s!r}")
        if not os.path.exists(os.path.join(SITE, ic_src(g["icon"]).replace(BASE, "", 1))):
            raise SystemExit(f"guide {g['id']}: unknown icon {g['icon']!r}")
    if not APP_ID:
        print("WARNING: APP_ID is empty; store buttons say 'coming soon'. Set it in build.py before launch.")


if __name__ == "__main__":
    check()
    static_files()
    for lang in LANGS:
        home(lang); about(lang); guides_index(lang); faq_page(lang); support_page(lang)
        legal_page(lang, "privacy"); legal_page(lang, "terms")
        for g in GUIDES:
            guide_page(g, lang)
    og_all()
    sitemap()
    llms()
    print(f"built {len(PATHS) * len(LANGS)} pages ({len(GUIDES)} guides x {len(LANGS)} languages)")
