#!/usr/bin/env python3
"""Builds the HANE website (EN / TR / ES) as static HTML for GitHub Pages.

    python3 -I HANE/_src/assets.py     # first, when the game's art changed (images, videos, social cards)
    python3 -I HANE/_src/build.py      # pages, sitemap.xml, llms.txt, css/js

Copy lives in _src/content/{en,tr,es}.py, guides in _src/guides/*.py (see guides/FORMAT.md), game facts in
_src/FACTS.md. Never hand-edit the generated HTML.
"""
import glob, hashlib, html, json, os, re, runpy, shutil

from PIL import Image

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(SRC)
ORIGIN = "https://guledaaydemir.github.io"
BASE = "/HANE/"
A = BASE + "assets/"
APP_ID = "6835573103"   # the App Store id given for HANE; every store link is built from this one value
PT = "128720446"        # provider token used on the other app sites
EMAIL = "solostaseraofficial@gmail.com"
AUTHOR = "Gül Eda Aydemir"
TODAY = "2026-11-16"
LANGS = ["en", "tr", "es"]
LOCALE = {"en": "en_US", "tr": "tr_TR", "es": "es_ES"}

PATHS = {
    "home": {"en": "", "tr": "tr/", "es": "es/"},
    "story": {"en": "story/", "tr": "tr/hikaye/", "es": "es/historia/"},
    "guides": {"en": "guides/", "tr": "tr/rehber/", "es": "es/guias/"},
    "faq": {"en": "faq/", "tr": "tr/sss/", "es": "es/preguntas-frecuentes/"},
    "support": {"en": "support/", "tr": "tr/destek/", "es": "es/soporte/"},
    "privacy": {"en": "privacy/", "tr": "tr/gizlilik/", "es": "es/privacidad/"},
}
GUIDE_DIR = {"en": "guides/", "tr": "tr/rehber/", "es": "es/guias/"}
HINT = {"en": "This site is also in English", "tr": "Bu site Türkçe de var", "es": "Esta web también está en español"}

C = {l: runpy.run_path(os.path.join(SRC, "content", l + ".py"))["T"] for l in LANGS}
GUIDES = sorted((runpy.run_path(p)["GUIDE"] for p in glob.glob(os.path.join(SRC, "guides", "*.py"))), key=lambda g: g["order"])
for g in GUIDES:
    PATHS[g["id"]] = {l: GUIDE_DIR[l] + g[l]["slug"] + "/" for l in LANGS}

e = lambda s: html.escape(str(s), quote=True)
LINK = re.compile(r"\{\{link:([a-z0-9-]+)\}\}")


def url(page, lang, absolute=False):
    if page == "demo":
        return url("home", lang, absolute) + "#demo"
    u = BASE + PATHS[page][lang]
    return ORIGIN + u if absolute else u


def store(lang, place):
    return f"https://apps.apple.com/app/apple-store/id{APP_ID}?pt={PT}&ct=web-hane-{lang}-{place}&mt=8"


STORE_CANON = f"https://apps.apple.com/app/id{APP_ID}"


# ---------------------------------------------------------------- images
_dims = {}


def dims(rel):
    if rel not in _dims:
        with Image.open(os.path.join(SITE, rel.replace(BASE, "", 1))) as im:
            _dims[rel] = im.size
    return _dims[rel]


def ill(key, alt, sizes="(max-width: 700px) 92vw, 600px", lazy=True, cls=""):
    small, big = f"{A}img/ill/{key}-480.webp", f"{A}img/ill/{key}-960.webp"
    w, h = dims(big)
    sw = dims(small)[0]
    srcset = f"{small} {sw}w, {big} {w}w" if sw != w else big + f" {w}w"
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{big}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}"{load}>'


def shot_src(key, lang, w=720):
    d = "tr" if lang == "tr" else "en"
    rel = f"{A}img/shots/{d}/{key}-{w}.webp"
    return rel if os.path.exists(os.path.join(SITE, rel.replace(BASE, "", 1))) else f"{A}img/shots/en/{key}-{w}.webp"


def shot(key, lang, alt, cls="phone sm"):
    s, b = shot_src(key, lang, 360), shot_src(key, lang, 720)
    w, h = dims(b)
    return (f'<div class="{cls}"><img src="{b}" srcset="{s} 360w, {b} 720w" sizes="220px" width="{w}" height="{h}" '
            f'alt="{e(alt)}" loading="lazy" decoding="async"></div>')


def sp(name, alt="", h=None, cls="", lazy=True):
    src = f"{A}img/sp/{name}.webp"
    w0, h0 = dims(src)
    if h:
        w0, h0 = round(w0 * h / h0), h
    c = f' class="{cls}"' if cls else ""
    load = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img{c} src="{src}" width="{w0}" height="{h0}" alt="{e(alt)}"{load}>'


TULIP = ('<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3c2.6 3.4 6.6 4.6 6.6 11a6.6 6.6 0 0 1-13.2 0C9.4 7.6 13.4 6.4 16 3z" fill="currentColor"/>'
         '<path d="M16 9c-2 2-3 4-3 7 0 2 1.3 3.6 3 4.2 1.7-.6 3-2.2 3-4.2 0-3-1-5-3-7z" fill="#8e1b1b" opacity=".55"/>'
         '<path d="M16 21v9M16 26c-3-1-5-3-6-6M16 26c3-1 5-3 6-6" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg>')
NAZAR = ('<svg class="nazar" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="#1f4f9c"/><circle cx="12" cy="12" r="7.5" fill="#fff"/>'
         '<circle cx="12" cy="12" r="5" fill="#5fa1e0"/><circle cx="12" cy="12" r="2.6" fill="#111"/></svg>')
APPLE = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.37 12.76c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.77-3.32-1.8-1.41-.14-2.76.84-3.47.84-.72 0-1.82-.82-3-.8-1.54.02-2.96.9-3.76 2.27-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 1.23-.02 2.01-1.12 2.76-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.65zM14.1 6.02c.63-.77 1.06-1.83.94-2.89-.91.04-2.01.61-2.66 1.37-.58.67-1.09 1.75-.96 2.79 1.02.08 2.05-.52 2.68-1.27z"/></svg>')


def store_badge(lang, place, cls="store"):
    t = C[lang]["badge"]
    return (f'<a class="{cls}" href="{e(store(lang, place))}" aria-label="{e(t["aria"])}">{APPLE}'
            f'<span>{e(t["top"])}<b>{e(t["big"])}</b></span></a>')


def tulip_rule():
    return f'<div class="tulip-rule">{TULIP}</div>'


# ---------------------------------------------------------------- page frame
def head(lang, page, title, desc, og, og_alt, ld, og_type="website"):
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
<meta name="theme-color" content="#2a140b">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="HANE">
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Playfair+Display:wght@700;800;900&display=swap">
<link rel="stylesheet" href="{A}hane.css?v={VER['css']}">
<link rel="alternate" type="text/plain" href="{BASE}llms.txt" title="{e(t['llms_title'])}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":"))}</script>
</head>"""


def header(lang, page):
    t = C[lang]
    nav = "".join(f'<a href="{url(p, lang)}"{" aria-current=page" if page == p or (p == "guides" and page in GUIDE_IDS) else ""}>{e(t["nav"][p])}</a>'
                  for p in ("story", "guides", "faq", "support"))
    langs = "".join(f'<a href="{url(page, l)}" hreflang="{l}" lang="{l}"{" aria-current=true" if l == lang else ""} title="{e(C[l]["lang_name"])}">{l.upper()}</a>' for l in LANGS)
    return f"""<body>
<a class="skip" href="#main">{e(t['skip'])}</a>
<header class="nav"><div class="wrap">
<a class="brand" href="{url('home', lang)}" aria-label="{e(t['home_label'])}"><img src="{A}img/logo-360.webp" width="360" height="{dims(A + 'img/logo-360.webp')[1]}" alt="HANE"></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">{e(t['menu'])}</button>
<nav class="nav-links" id="nav-links" aria-label="HANE">{nav}
<div class="langs" role="group" aria-label="{e(t['language'])}">{langs}</div>
<a class="btn sm" href="{e(store(lang, 'nav'))}">{e(t['get'])}</a>
</nav></div></header>
<main id="main">"""


def footer(lang, page, extra_js=""):
    t, f = C[lang], C[lang]["foot"]
    gl = "".join(f'<li><a href="{url(g["id"], lang)}">{e(g[lang]["h1"] if len(g[lang]["h1"]) < 60 else g[lang]["title"])}</a></li>' for g in GUIDES[:5])
    street = f"""<div class="street" aria-hidden="true">
{sp('lamp', cls='p lamp1')}{sp('plane_tree', cls='p tree1')}{sp('simit_cart', cls='p simit')}{sp('cat_tekir', cls='p cat')}{sp('cypress', cls='p cyp')}{sp('bench', cls='p bench')}{sp('lamp', cls='p lamp2')}{sp('plane_tree', cls='p tree2')}{sp('fountain', cls='p fount')}
{sp('minibus', cls='v v1')}{sp('taxi', cls='v v2')}{sp('car_red', cls='v v3')}
</div>"""
    hint = "".join(f'<a data-lang="{l}" lang="{l}" href="{url(page, l)}" hidden>{e(HINT[l])} →</a>' for l in LANGS if l != lang)
    return f"""</main>
{street}
<footer class="foot"><div class="wrap">
<div class="cols">
<div><img class="logo" src="{A}img/logo-360.webp" width="360" height="{dims(A + 'img/logo-360.webp')[1]}" alt="HANE" loading="lazy"><p>{e(f['tagline'])}</p>{store_badge(lang, 'footer')}</div>
<div><h4>{e(f['game'])}</h4><ul><li><a href="{url('home', lang)}">{e(t['nav']['home'])}</a></li><li><a href="{url('story', lang)}">{e(t['nav']['story'])}</a></li><li><a href="{url('demo', lang)}">{e(f['demo'])}</a></li><li><a href="{url('faq', lang)}">{e(t['nav']['faq'])}</a></li></ul></div>
<div><h4>{e(f['learn'])}</h4><ul>{gl}<li><a href="{url('guides', lang)}">{e(f['all_guides'])}</a></li></ul></div>
<div><h4>{e(f['help'])}</h4><ul><li><a href="{url('support', lang)}">{e(t['nav']['support'])}</a></li><li><a href="{url('privacy', lang)}">{e(f['privacy'])}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{BASE}llms.txt">llms.txt</a></li></ul></div>
</div>
<small>{NAZAR}{e(f['made'])} © 2026 {AUTHOR}. {e(f['apple'])}</small>
</div></footer>
<div class="lang-hint" role="region" aria-label="{e(t['language'])}">{hint}<button type="button" aria-label="{e(t['close'])}">×</button></div>
<script src="{A}hane.js?v={VER['js']}" defer></script>{extra_js}
</body>
</html>
"""


def write(page, lang, body):
    path = os.path.join(SITE, PATHS[page][lang], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


# ---------------------------------------------------------------- structured data
PERSON = {"@type": "Person", "@id": ORIGIN + "/#person", "name": AUTHOR, "alternateName": "Gul Eda Aydemir",
          "jobTitle": "Independent iOS developer", "url": ORIGIN + "/about/", "email": "mailto:" + EMAIL}


def game_ld(lang):
    t = C[lang]
    return {"@type": ["VideoGame", "MobileApplication"], "@id": ORIGIN + BASE + "#game", "name": "HANE",
            "alternateName": t["store_name"], "description": t["home"]["description"], "url": url("home", lang, True),
            "image": ORIGIN + A + "icon-512.png", "applicationCategory": "GameApplication",
            "applicationSubCategory": "Simulation", "genre": t["ld_genres"], "operatingSystem": "iOS",
            "gamePlatform": ["iPhone", "iPad"], "playMode": "SinglePlayer", "inLanguage": ["tr", "en"],
            "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
            "installUrl": STORE_CANON, "downloadUrl": STORE_CANON,
            "screenshot": [ORIGIN + shot_src(k, lang) for k in ("room", "cat", "map", "dream", "ribbon")],
            "character": [{"@type": "Person", "name": n, "description": d} for n, d in t["ld_characters"]],
            "gameLocation": [{"@type": "Place", "name": n} for n in t["ld_places"]],
            "keywords": t["ld_keywords"]}


def crumbs_ld(lang, items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def crumbs_html(items):
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(f'<a href="{u.replace(ORIGIN, "")}">{e(n)}</a>' for n, u in items[:-1]) + "</nav>"


def faq_ld(pairs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in pairs]}


def links(s, lang):
    def link(m):
        if m.group(1) not in PATHS and m.group(1) != "demo":
            if os.environ.get("HANE_DRAFT"):  # preview while a guide is still being written
                print(f"draft: {m.group(1)!r} not written yet, linking the guides index")
                return url("guides", lang)
            raise SystemExit(f"unknown link target {m.group(1)!r}")
        return url(m.group(1), lang)
    return LINK.sub(link, s)


def faq_html(pairs, lang):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><div><p>{links(a, lang)}</p></div></details>" for q, a in pairs) + "</div>"


def cta_box(lang, place):
    t = C[lang]["cta_box"]
    return (f'<aside class="cta-box"><img class="icon" src="{A}img/app-icon-256.webp" width="256" height="256" alt="" loading="lazy">'
            f'<div><h3>{e(t["h"])}</h3><p>{e(t["p"])}</p>{store_badge(lang, place)}</div></aside>')


# ---------------------------------------------------------------- home
def home(lang):
    t, h = C[lang], C[lang]["home"]
    ld = {"@context": "https://schema.org", "@graph": [
        PERSON, {"@type": "WebSite", "@id": ORIGIN + BASE + "#site", "name": "HANE", "url": ORIGIN + BASE, "inLanguage": LANGS, "publisher": {"@id": PERSON["@id"]}},
        {"@type": "WebPage", "@id": url("home", lang, True) + "#page", "url": url("home", lang, True), "name": h["title"], "description": h["description"], "inLanguage": lang,
         "isPartOf": {"@id": ORIGIN + BASE + "#site"}, "about": {"@id": ORIGIN + BASE + "#game"}, "primaryImageOfPage": ORIGIN + A + f"og/home-{lang}.jpg"},
        game_ld(lang),
        {"@type": "VideoObject", "name": h["video_name"], "description": h["video_desc"], "thumbnailUrl": ORIGIN + A + f"video/hane-{lang}-poster.jpg",
         "contentUrl": ORIGIN + A + f"video/hane-{lang}.mp4", "uploadDate": TODAY, "duration": "PT29S", "inLanguage": lang},
        faq_ld(h["faq"])]}
    out = [head(lang, "home", h["title"], h["description"], A + f"og/home-{lang}.jpg", h["og_alt"], ld), header(lang, "home")]

    badges = "".join(f"<li>{e(b)}</li>" for b in h["badges"])
    out.append(f"""
<section class="hero"><div class="wrap">
<div class="hero-copy">
<span class="eyebrow">{e(h['eyebrow'])}</span>
<h1>{h['h1']}</h1>
<p class="lead">{e(h['lead'])}</p>
<div class="hero-ctas">{store_badge(lang, 'hero')}<a class="btn brass" href="#demo">{sp('tea_strong', h=28)}{e(h['try_demo'])}</a></div>
<ul class="badges">{badges}</ul>
</div>
<div class="hero-art">
<div class="door">
<svg class="lantern l" viewBox="0 0 60 120" aria-hidden="true"><path d="M30 0v22" stroke="#c9963a" stroke-width="2"/><path d="M22 22h16l4 8H18z" fill="#c9963a"/><path d="M18 30h24l6 30-18 34-18-34z" fill="#c23a2a"/><path d="M30 30v64M18 30l12 64M42 30l-12 64M12 60h36" stroke="#f2cf73" stroke-width="1.5" opacity=".8"/><circle cx="30" cy="60" r="9" fill="#ffd27a" opacity=".85"/><path d="M26 94h8l-4 12z" fill="#c9963a"/></svg>
<svg class="lantern r" viewBox="0 0 60 120" aria-hidden="true"><path d="M30 0v22" stroke="#c9963a" stroke-width="2"/><path d="M22 22h16l4 8H18z" fill="#c9963a"/><path d="M18 30h24l6 30-18 34-18-34z" fill="#1f6f8f"/><path d="M30 30v64M18 30l12 64M42 30l-12 64M12 60h36" stroke="#f2cf73" stroke-width="1.5" opacity=".8"/><circle cx="30" cy="60" r="9" fill="#ffd27a" opacity=".85"/><path d="M26 94h8l-4 12z" fill="#c9963a"/></svg>
<div class="door-in">
{ill('opening', h['door_alt'], sizes='(max-width: 900px) 86vw, 440px', lazy=False)}
{ill('welcome', h['welcome_alt'], sizes='(max-width: 900px) 86vw, 440px', cls='after')}
<img class="sign" src="{A}img/logo-720.webp" width="720" height="{dims(A + 'img/logo-720.webp')[1]}" alt="" fetchpriority="high">
<div class="cut-ribbon" aria-hidden="true"><i></i><i></i>{sp('ribbon_bow', cls='bow', lazy=False)}</div>
<div class="confetti" aria-hidden="true"></div>
<div class="cut-zone" aria-hidden="true"></div>
</div>
<div class="steam-glass" aria-hidden="true"><svg class="steam" viewBox="0 0 60 80"><path d="M20 76c-8-12 8-18 0-30s6-18 0-30"/><path d="M32 76c-8-12 8-18 0-30s6-18 0-30"/><path d="M44 76c-8-12 8-18 0-30s6-18 0-30"/></svg>{sp('tea_strong', lazy=False)}</div>
</div>
<div class="cut-ui"><button class="btn red" type="button" data-cut>{sp('i_scissors', h=26, lazy=False)}{e(h['cut_btn'])}</button><span class="cut-hint">{e(h['cut_hint'])}</span><div class="cut-done" role="status">{e(h['cut_done'])}</div></div>
</div>
</div></section>
<div class="marquee" aria-hidden="true"><div class="track">{''.join(f'<span>{e(p)}</span>' for p in h['marquee'] * 2)}</div></div>
""")

    steps = "".join(f'<div class="card step reveal">{ill(img, s_t, sizes="(max-width: 640px) 90vw, 260px")}<h3>{e(s_t)}</h3><p>{e(s_p)}</p></div>'
                    for img, s_t, s_p in h["steps"])
    facts = "".join(f'<span class="fact">{sp(icon, h=34)}{e(txt)}</span>' for icon, txt in h["facts"])
    out.append(f"""
<section class="section" id="how"><div class="wrap">
<div class="section-head reveal"><span class="ribbon">{e(h['how_kicker'])}</span><h2>{e(h['how_h2'])}</h2><p class="lead">{e(h['how_lead'])}</p></div>
<div class="grid g4 steps">{steps}</div>
<div class="facts">{facts}</div>
</div></section>
""")

    demo_strings = dict(h["demo_s"], storeUrl=store(lang, "demo"), wage=15, car=10000)
    out.append(f"""
<section class="section band-wood" id="play"><div class="wrap">
<div class="section-head reveal"><span class="ribbon">{e(h['demo_kicker'])}</span><h2>{e(h['demo_h2'])}</h2><p class="lead">{e(h['demo_lead'])}</p></div>
<div class="demo-box"><div class="demo" id="demo" role="application" aria-label="{e(h['demo_aria'])}"></div>
<p class="demo-note muted">{e(h['demo_note'])}</p></div>
</div></section>
""")

    shots = "".join(f'<figure>{shot(k, lang, cap)}<figcaption>{e(cap)}</figcaption></figure>' for k, cap in h["shots"])
    out.append(f"""
<section class="section band-red" id="screens"><div class="wrap">
<div class="section-head reveal"><span class="ribbon">{e(h['show_kicker'])}</span><h2>{e(h['show_h2'])}</h2><p class="lead">{e(h['show_lead'])}</p></div>
<div class="show">
<div><div class="phone"><video data-autoplay muted loop playsinline preload="none" poster="{A}video/hane-{lang}-poster.jpg" width="432" height="936" aria-label="{e(h['video_name'])}"><source src="{A}video/hane-{lang}.mp4" type="video/mp4"></video></div>
<div class="vid-ctl"><button class="btn sm brass" type="button" onclick="var v=this.closest('.show').querySelector('video');v.muted=!v.muted;v.play();this.textContent=v.muted?{json.dumps(h['sound_on'])}:{json.dumps(h['sound_off'])}">{e(h['sound_on'])}</button></div></div>
<div class="shots" tabindex="0" aria-label="{e(h['show_h2'])}">{shots}</div>
</div>
</div></section>
<div class="kilim-band" aria-hidden="true"></div>
""")

    flags = "".join(f'<span class="flag" data-at="{p / 100}">{p}%</span>' for p in (1, 5, 10, 25, 50, 75))
    stats = "".join(f'<span class="fact">{sp(icon, h=34)}{e(txt)}</span>' for icon, txt in h["dream_stats"])
    paras = "".join(f"<p>{links(p, lang)}</p>" for p in h["dream_p"])
    out.append(f"""
<section class="section" id="dream"><div class="wrap dream">
<div class="reveal"><div class="dream-art">{ill('dream', h['dream_alt'], sizes='(max-width: 900px) 92vw, 560px')}</div>
<div class="road" data-road="0.42" aria-hidden="true">{sp('i_kumbara', cls='kum')}{flags}{sp('cirak_walk_a', cls='walker')}{sp('dream_car', cls='car')}</div>
<p class="muted center" style="font-size:14px">{e(h['road_caption'])}</p></div>
<div class="reveal"><span class="ribbon">{e(h['dream_kicker'])}</span><h2>{e(h['dream_h2'])}</h2>{paras}
<div class="dream-stats">{stats}</div>
<p style="margin-top:22px"><a class="btn red" href="{url('story', lang)}">{e(h['dream_link'])}</a></p></div>
</div></section>
""")

    chars = "".join(f'<div class="card char reveal"><div class="pic">{sp(img, alt=name)}</div><span class="role">{e(role)}</span><h3>{e(name)}</h3><p>{e(txt)}</p></div>'
                    for img, role, name, txt in h["chars"])
    cats = "".join(f'<figure>{sp("cat_" + k, alt=n)}<figcaption>{e(n)}</figcaption></figure>' for k, n in
                   (("mirmir", "Mırmır"), ("pamuk", "Pamuk"), ("aslan", "Aslan"), ("tekir", "Tekir"), ("karagoz", "Karagöz")))
    out.append(f"""
<section class="section band-wood" id="characters"><div class="wrap">
<div class="section-head reveal"><span class="ribbon">{e(h['chars_kicker'])}</span><h2>{e(h['chars_h2'])}</h2><p class="lead">{e(h['chars_lead'])}</p></div>
<div class="chars">{chars}</div>
<h3 class="center" style="margin-top:46px">{e(h['cats_h'])}</h3><p class="center muted">{e(h['cats_p'])}</p>
<div class="cats">{cats}</div>
</div></section>
""")

    pins = ""
    for key, name, usta, cost, x, y in BRANCHES(lang):
        side = {"besiktas": " l", "bursa": " l", "kadikoy": " r", "eskisehir": " r"}.get(key, "")
        pins += f'<span class="pin{" start" if not cost else ""}{side}" style="left:{x * 100:.1f}%;top:{y * 100:.1f}%"><b>{e(name)}</b><i></i></span>'
    rows = "".join(f'<li><strong>{e(name)}</strong><em>{e(cost or h["map_start"])}</em><span>{e(usta)}</span></li>' for key, name, usta, cost, x, y in BRANCHES(lang))
    out.append(f"""
<section class="section band-sky" id="map"><div class="wrap">
<div class="section-head reveal"><span class="ribbon">{e(h['map_kicker'])}</span><h2>{e(h['map_h2'])}</h2><p class="lead">{e(h['map_lead'])}</p></div>
<div class="mapwrap"><div class="map">{ill('map', h['map_alt'], sizes='(max-width: 900px) 92vw, 640px')}{pins}</div>
<div><ul class="branches">{rows}</ul><p class="muted" style="font-size:14.5px;margin-top:14px">{e(h['map_note'])}</p></div></div>
</div></section>
""")

    items = "".join(f'<li>{sp(img, h=44)}<span>{e(n)}</span><b>{price} {e(t["coin"])}</b></li>' for img, n, price in h["menu"])
    out.append(f"""
<section class="section band-wood"><div class="wrap">
<div class="section-head reveal"><span class="ribbon">{e(h['menu_kicker'])}</span><h2>{e(h['menu_h2'])}</h2><p class="lead">{e(h['menu_lead'])}</p></div>
<div class="menu-board reveal"><h3>{e(h['menu_board'])}</h3><ul>{items}</ul><p>{e(h['menu_note'])}</p></div>
</div></section>
""")

    prom = "".join(f'<div class="card reveal">{sp(img, h=64)}<h3>{e(ti)}</h3><p>{e(tx)}</p></div>' for img, ti, tx in h["promise"])
    out.append(f"""
<section class="section promise"><div class="wrap">
<div class="section-head reveal">{tulip_rule()}<h2>{e(h['promise_h2'])}</h2><p class="lead">{e(h['promise_lead'])}</p></div>
<div class="grid g4">{prom}</div>
</div></section>
<div class="kilim-band" aria-hidden="true"></div>
""")

    out.append(f"""
<section class="section"><div class="wrap">
<div class="section-head reveal"><span class="ribbon">{e(h['guides_kicker'])}</span><h2>{e(h['guides_h2'])}</h2><p class="lead">{e(h['guides_lead'])}</p></div>
<div class="gcards">{''.join(guide_card(g, lang) for g in GUIDES[:6])}</div>
<p class="center" style="margin-top:30px"><a class="btn blue" href="{url('guides', lang)}">{e(h['guides_all'])}</a></p>
</div></section>
<section class="section tight"><div class="wrap">
<div class="section-head reveal"><h2>{e(h['faq_h2'])}</h2></div>
{faq_html(h['faq'], lang)}
<p class="center" style="margin-top:26px"><a href="{url('faq', lang)}">{e(h['faq_all'])} →</a></p>
</div></section>
<section class="section band-red"><div class="wrap center">
{tulip_rule()}<h2>{e(h['final_h2'])}</h2><p class="lead" style="max-width:640px;margin:0 auto 26px">{e(h['final_p'])}</p>
{store_badge(lang, 'final', 'store pulse')}
</div></section>
""")
    out.append(footer(lang, "home", f'\n<script type="application/json" id="demo-strings">{json.dumps(demo_strings, ensure_ascii=False)}</script>\n<script src="{A}demo.js?v={VER["demo"]}" defer></script>'))
    write("home", lang, "".join(out))


def BRANCHES(lang):
    mx = lambda lon: 0.03 + ((lon - 26) / 18.8 * 0.95)
    my = lambda lat: 0.175 + ((42.1 - lat) / 6.1 * 0.62)
    names = C[lang]["cities"]
    coin, star = C[lang]["coin"], "★"
    rows = [("uskudar", "Hasan", 0, 0, 0.207, 0.258), ("kadikoy", "Rıza", 300, 1, 0.2, 0.318), ("besiktas", "Cemal", 2500, 3, 0.155, 0.262),
            ("bursa", "İsmail", 9000, 6, mx(29.06), my(40.19)), ("izmir", "Nuri", 18000, 9, mx(27.14), my(38.42)),
            ("ankara", "Kemal", 30000, 12, mx(32.85), my(39.93)), ("eskisehir", "Salih", 45000, 15, mx(30.52), my(39.78)),
            ("trabzon", "Temel", 65000, 18, mx(39.72), my(40.85))]
    sep = "." if lang in ("tr", "es") else ","
    return [(k, names[k], f"{u} Usta", f"{format(c, ',').replace(',', sep)} {coin} · {star}{s}" if c else "", x, y) for k, u, c, s, x, y in rows]


def guide_card(g, lang):
    t = C[lang]
    gl = g[lang]
    return (f'<div><a class="card gcard reveal" data-cat="{g["category"]}" href="{url(g["id"], lang)}">{ill(g["hero"], "", sizes="(max-width: 640px) 92vw, 360px")}'
            f'<div class="in"><span class="cat">{e(t["guides_page"]["cats"][g["category"]])}</span><h3>{e(gl["h1"])}</h3><p>{e(gl["description"])}</p></div></a></div>')


# ---------------------------------------------------------------- story
def story(lang):
    t, s = C[lang], C[lang]["story"]
    items = [(t["nav"]["home"], url("home", lang, True)), (s["h1"], url("story", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, game_ld(lang),
          {"@type": "Article", "headline": s["h1"], "description": s["description"], "inLanguage": lang, "image": ORIGIN + A + "og/dream.jpg",
           "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]}, "datePublished": TODAY, "dateModified": TODAY,
           "mainEntityOfPage": url("story", lang, True), "about": {"@id": ORIGIN + BASE + "#game"}},
          crumbs_ld(lang, items)]}
    out = [head(lang, "story", s["title"], s["description"], A + "og/dream.jpg", s["og_alt"], ld, "article"), header(lang, "story")]
    out.append(f"""
<section class="page-hero"><div class="wrap">{crumbs_html(items)}<span class="kicker">{e(s['kicker'])}</span><h1>{e(s['h1'])}</h1><p class="lead">{e(s['lead'])}</p></div></section>
<div class="wrap"><div class="article"><article class="prose">
{render_body(s['body'], lang)}
<h2 id="kumbara">{e(s['calc_h2'])}</h2>
<p>{links(s['calc_p'], lang)}</p>
<div class="card calc" data-calc data-wage="15" data-car="10000" data-share="0.5">
<label for="tips">{e(s['calc_tips'])}</label>
<input id="tips" type="range" min="0" max="200" step="5" value="40">
<p>{s['calc_result']}</p>
<label for="days">{e(s['calc_days'])}: <span data-dayout></span></label>
<input id="days" data-dayslider type="range" min="0" max="400" step="1" value="60">
<div class="road" aria-hidden="true">{sp('i_kumbara', cls='kum')}{''.join(f'<span class="flag" data-at="{p / 100}">{p}%</span>' for p in (1, 5, 10, 25, 50, 75))}{sp('cirak_walk_a', cls='walker')}{sp('dream_car', cls='car')}</div>
<p class="center"><strong data-saved></strong></p>
<p class="muted" style="font-size:14px;margin:0">{e(s['calc_note'])}</p>
</div>
{render_body(s['body2'], lang)}
{cta_box(lang, 'story')}
</article>
{aside(lang, None)}
</div></div>
""")
    out.append(footer(lang, "story"))
    write("story", lang, "".join(out))


def aside(lang, current):
    t = C[lang]["article"]
    more = "".join(f'<li><a href="{url(g["id"], lang)}">{e(g[lang]["h1"])}</a></li>' for g in GUIDES if g["id"] != current)
    return (f'<aside class="aside"><div class="card"><h3>{e(t["more"])}</h3><ul>{more}</ul></div>'
            f'<div class="card center">{sp("cirak_carry", h=120)}<h3>{e(t["demo_h"])}</h3><p>{e(t["demo_p"])}</p><a class="btn sm" href="{url("demo", lang)}">{e(t["demo_btn"])}</a></div></aside>')


# ---------------------------------------------------------------- guides
FIG = re.compile(r"\[\[(fig|shot):([a-z_]+)\|(.*?)\]\]")
TIP = re.compile(r"\[\[tip\|(.*?)\]\]", re.S)


def render_body(body, lang):
    def fig(m):
        kind, key, cap = m.group(1), m.group(2), m.group(3)
        if kind == "fig":
            return f'<figure class="ill">{ill(key, cap, sizes="(max-width: 760px) 92vw, 740px")}<figcaption>{cap}</figcaption></figure>'
        return f'<figure class="shot">{shot(key, lang, re.sub("<[^>]+>", "", cap), "phone")}<figcaption>{cap}</figcaption></figure>'
    body = FIG.sub(fig, body)
    body = TIP.sub(lambda m: f'<div class="tip">{sp("usta", h=90)}<div><b class="t">{e(C[lang]["article"]["tip"])}</b><p>{m.group(1)}</p></div></div>', body)
    body = body.replace("[[cta]]", cta_box(lang, "guide"))
    body = links(body, lang)
    body = re.sub(r"<p>\s*(<figure|<div class=\"tip|<aside)", r"\1", body)
    body = re.sub(r"(</figure>|</aside>|</div></div>)\s*</p>", r"\1", body)
    return body


def guide_page(g, lang):
    t, a, gl = C[lang], C[lang]["article"], g[lang]
    items = [(t["nav"]["home"], url("home", lang, True)), (t["nav"]["guides"], url("guides", lang, True)), (gl["h1"], url(g["id"], lang, True))]
    words = len(re.sub("<[^>]+>", " ", gl["body"]).split())
    minutes = max(3, round(words / 220))
    ld = {"@context": "https://schema.org", "@graph": [PERSON,
          {"@type": "Article", "headline": gl["h1"], "alternativeHeadline": gl["title"], "description": gl["description"], "inLanguage": lang,
           "image": ORIGIN + A + f"og/{g['hero']}.jpg", "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
           "datePublished": g.get("updated", TODAY), "dateModified": g.get("updated", TODAY), "mainEntityOfPage": url(g["id"], lang, True),
           "wordCount": words, "about": gl["kicker"], "abstract": gl["answer"],
           "citation": [{"@type": "CreativeWork", "name": n, "url": u} for n, u in gl["sources"]] or None},
          faq_ld(gl["faq"]), crumbs_ld(lang, items)]}
    if not gl["sources"]:
        del ld["@graph"][1]["citation"]
    out = [head(lang, g["id"], gl["title"], gl["description"], A + f"og/{g['hero']}.jpg", gl["h1"], ld, "article"), header(lang, g["id"])]
    take = "".join(f"<li>{e(x)}</li>" for x in gl["takeaways"])
    src = ""
    if gl["sources"]:
        src = f'<h2>{e(a["sources"])}</h2><ol class="sources">' + "".join(f'<li>{e(n)} <a href="{e(u)}" rel="noopener">{e(u)}</a></li>' for n, u in gl["sources"]) + "</ol>"
    out.append(f"""
<section class="page-hero"><div class="wrap">{crumbs_html(items)}<span class="kicker">{e(gl['kicker'])}</span><h1>{e(gl['h1'])}</h1>
<p class="meta">{e(a['by'])} {AUTHOR} · {e(a['updated'])} <time datetime="{g.get('updated', TODAY)}">{date_text(g.get('updated', TODAY), lang)}</time> · {e(a['read'].format(n=minutes))}</p></div></section>
<div class="wrap"><div class="article"><article class="prose">
<div class="answer"><span class="lbl">{e(a['answer'])}</span><p>{e(gl['answer'])}</p></div>
<figure class="ill">{ill(g['hero'], gl['h1'], sizes='(max-width: 760px) 92vw, 740px', lazy=False)}</figure>
<h2>{e(a['takeaways'])}</h2><ul class="takeaways">{take}</ul>
{render_body(gl['body'], lang)}
<h2>{e(a['faq'])}</h2>{faq_html([(q, e(x)) for q, x in gl['faq']], lang)}
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
          crumbs_ld(lang, items)]}
    out = [head(lang, "guides", gp["title"], gp["description"], A + "og/intro_serve.jpg", gp["h1"], ld), header(lang, "guides")]
    filt = "".join(f'<button type="button" data-cat="{k}" aria-pressed="{"true" if k == "all" else "false"}">{e(v)}</button>'
                   for k, v in [("all", gp["all"])] + list(gp["cats"].items()))
    out.append(f"""
<section class="page-hero"><div class="wrap">{crumbs_html(items)}<span class="kicker">{e(gp['kicker'])}</span><h1>{e(gp['h1'])}</h1><p class="lead">{e(gp['lead'])}</p></div></section>
<section class="section"><div class="wrap">
<div class="filters" role="group" aria-label="{e(gp['filter'])}">{filt}</div>
<div class="gcards">{''.join(guide_card(g, lang) for g in GUIDES)}</div>
</div></section>
""")
    out.append(footer(lang, "guides"))
    write("guides", lang, "".join(out))


# ---------------------------------------------------------------- faq, support, privacy
def faq_page(lang):
    t, f = C[lang], C[lang]["faq"]
    items = [(t["nav"]["home"], url("home", lang, True)), (f["h1"], url("faq", lang, True))]
    pairs = [p for _, ps in f["groups"] for p in ps]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, faq_ld(pairs), crumbs_ld(lang, items)]}
    out = [head(lang, "faq", f["title"], f["description"], A + "og/intro_goal.jpg", f["h1"], ld), header(lang, "faq")]
    groups = "".join(f'<h2 class="faq-group">{e(gt)}</h2>{faq_html(ps, lang)}' for gt, ps in f["groups"])
    out.append(f"""
<section class="page-hero"><div class="wrap">{crumbs_html(items)}<span class="kicker">{e(f['kicker'])}</span><h1>{e(f['h1'])}</h1><p class="lead">{links(f['lead'], lang)}</p></div></section>
<section class="section tight"><div class="wrap">{groups}
<div style="max-width:840px;margin:40px auto 0">{cta_box(lang, 'faq')}</div></div></section>
""")
    out.append(footer(lang, "faq"))
    write("faq", lang, "".join(out))


def support_page(lang):
    t, s = C[lang], C[lang]["support"]
    items = [(t["nav"]["home"], url("home", lang, True)), (s["h1"], url("support", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON,
          {"@type": "ContactPage", "name": s["h1"], "description": s["description"], "url": url("support", lang, True), "inLanguage": lang,
           "mainEntity": {"@type": "ContactPoint", "contactType": "customer support", "email": EMAIL, "availableLanguage": ["Turkish", "English", "Spanish"]}},
          faq_ld(s["quick"]), crumbs_ld(lang, items)]}
    subject = s["mail_subject"]
    mail = f"mailto:{EMAIL}?subject={subject.replace(' ', '%20')}"
    out = [head(lang, "support", s["title"], s["description"], A + "og/intro_order.jpg", s["h1"], ld), header(lang, "support")]
    checklist = "".join(f"<li>{e(x)}</li>" for x in s["include"])
    out.append(f"""
<section class="page-hero"><div class="wrap">{crumbs_html(items)}<span class="kicker">{e(s['kicker'])}</span><h1>{e(s['h1'])}</h1><p class="lead">{e(s['lead'])}</p></div></section>
<section class="section tight"><div class="wrap">
<div class="grid g2" style="max-width:980px;margin:0 auto">
<div class="card"><h2 style="font-size:26px">{e(s['contact_h'])}</h2><p>{e(s['contact_p'])}</p><p><a class="btn" href="{e(mail)}">{sp('i_handshake', h=28)}{e(s['mail_btn'])}</a></p><p class="muted" style="font-size:15px">{EMAIL}</p></div>
<div class="card"><h2 style="font-size:26px">{e(s['include_h'])}</h2><ul>{checklist}</ul></div>
</div>
<h2 class="faq-group">{e(s['quick_h'])}</h2>{faq_html(s['quick'], lang)}
<h2 class="faq-group">{e(s['more_h'])}</h2>
<div class="faq" style="gap:8px"><p>{s['more_p'].format(faq=url('faq', lang), guide=url('beginners-guide', lang) if 'beginners-guide' in PATHS else url('guides', lang), privacy=url('privacy', lang))}</p></div>
</div></section>
""")
    out.append(footer(lang, "support"))
    write("support", lang, "".join(out))


def privacy_page(lang):
    t, p = C[lang], C[lang]["privacy"]
    items = [(t["nav"]["home"], url("home", lang, True)), (p["h1"], url("privacy", lang, True))]
    ld = {"@context": "https://schema.org", "@graph": [PERSON, {"@type": "WebPage", "name": p["h1"], "description": p["description"], "url": url("privacy", lang, True),
          "inLanguage": lang, "dateModified": TODAY}, crumbs_ld(lang, items)]}
    out = [head(lang, "privacy", p["title"], p["description"], A + "og/welcome.jpg", p["h1"], ld), header(lang, "privacy")]
    secs = "".join(f"<h2>{e(h)}</h2>{links(b, lang)}" for h, b in p["sections"])
    badges = "".join(f"<li>{e(b)}</li>" for b in p["badges"])
    out.append(f"""
<section class="page-hero"><div class="wrap">{crumbs_html(items)}<span class="kicker">{e(p['kicker'])}</span><h1>{e(p['h1'])}</h1><p class="lead">{e(p['lead'])}</p>
<p class="meta">{e(p['effective'])} <time datetime="{TODAY}">{date_text(TODAY, lang)}</time></p></div></section>
<div class="wrap"><div class="legal prose light"><ul class="badges">{badges}</ul>{secs}</div></div>
""")
    out.append(footer(lang, "privacy"))
    write("privacy", lang, "".join(out))


# ---------------------------------------------------------------- sitemap, llms.txt, static files
def sitemap():
    rows = []
    for page in PATHS:
        for l in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{url(page, x, True)}"/>' for x in LANGS)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url(page, "en", True)}"/>'
            prio = "1.0" if page == "home" else "0.8" if page in GUIDE_IDS or page == "story" else "0.6"
            rows.append(f"<url><loc>{url(page, l, True)}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority>{alts}</url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8").write(xml)


def llms():
    facts = open(os.path.join(SRC, "FACTS.md"), encoding="utf-8").read().split("\n", 2)[2].strip()
    lines = [f"# HANE — Turkish Tea House Tycoon (iPhone & iPad game)", "",
             "> HANE is an offline tea-house management game for iPhone and iPad by independent developer Gül Eda Aydemir. "
             "You play the çırak (apprentice) of a traditional Istanbul kıraathane: take orders, call them out to the usta, carry tea on a hanging tray, "
             "see the neighbourhood cats out, calm quarrels and open eight tea houses across Türkiye, while the çırak saves his wage and tips for a dream car. "
             "No ads, no in-app purchases, no account, no data collected. Game text in Turkish and English.", "",
             f"- App Store: {STORE_CANON}", f"- Website (EN): {url('home', 'en', True)}", f"- Türkçe: {url('home', 'tr', True)}",
             f"- Español: {url('home', 'es', True)}", f"- Developer contact: {EMAIL}", "",
             "## Pages", ""]
    for page, label in (("home", "Launch page"), ("story", "The çırak's dream (story)"), ("guides", "Guides"), ("faq", "FAQ"), ("support", "Support"), ("privacy", "Privacy policy")):
        lines.append(f"- {label}: " + " | ".join(f"[{l.upper()}]({url(page, l, True)})" for l in LANGS))
    lines += ["", "## Guides (with short answers)", ""]
    for g in GUIDES:
        lines.append(f"### {g['en']['h1']}")
        lines.append(" | ".join(f"[{l.upper()}]({url(g['id'], l, True)})" for l in LANGS))
        lines.append("")
        lines.append(g["en"]["answer"])
        lines.append("")
    lines += ["## Frequently asked", ""]
    for _, ps in C["en"]["faq"]["groups"]:
        for q, a in ps:
            lines.append(f"- **{q}** {re.sub('<[^>]+>', '', a)}")
    lines += ["", "## Facts about the game", "", facts, ""]
    open(os.path.join(SITE, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))


VER = {}


def static_files():
    for name, key in (("hane.css", "css"), ("hane.js", "js"), ("demo.js", "demo")):
        src = os.path.join(SRC, "static", name)
        data = open(src, "rb").read()
        VER[key] = hashlib.sha1(data).hexdigest()[:8]
        shutil.copyfile(src, os.path.join(SITE, "assets", name))


def check():
    base = set(C["en"])
    for l in LANGS[1:]:
        missing = base ^ set(C[l])
        if missing:
            raise SystemExit(f"content keys differ in {l}: {sorted(missing)}")
        for k in C["en"]:
            if isinstance(C["en"][k], dict) and set(C["en"][k]) != set(C[l][k]):
                raise SystemExit(f"content keys differ in {l}.{k}: {sorted(set(C['en'][k]) ^ set(C[l][k]))}")
    for g in GUIDES:
        for l in LANGS:
            gl = g[l]
            for key in ("slug", "title", "description", "h1", "kicker", "answer", "takeaways", "body", "faq", "sources"):
                if key not in gl:
                    raise SystemExit(f"guide {g['id']} {l} lacks {key}")
            if len(gl["title"]) > 60:
                print(f"note: {g['id']} {l} title is {len(gl['title'])} chars")


GUIDE_IDS = {g["id"] for g in GUIDES}

if __name__ == "__main__":
    check()
    static_files()
    for lang in LANGS:
        home(lang); story(lang); guides_index(lang); faq_page(lang); support_page(lang); privacy_page(lang)
        for g in GUIDES:
            guide_page(g, lang)
    sitemap()
    llms()
    print(f"built {len(PATHS) * len(LANGS)} pages ({len(GUIDES)} guides x {len(LANGS)} languages)")
