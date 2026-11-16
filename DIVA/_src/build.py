#!/usr/bin/env python3
"""Builds the DIVA website (EN / TR / ES) as static HTML for GitHub Pages.

    python3 DIVA/_src/build.py            # pages, sitemap.xml, llms.txt
    python3 DIVA/_src/build.py --og       # also regenerate social images (needs ImageMagick)

Copy lives in _src/content/{en,tr,es}.py; app text (CD titles, lines, ritual themes) comes from
_src/data/app.json, produced by extract.py from the app repo. Never hand-edit the generated HTML.
"""
import datetime, html, importlib.util, json, os, re, subprocess, sys

SRC = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(SRC)
ORIGIN = "https://guledaaydemir.github.io"
BASE = "/DIVA/"
A = BASE + "assets/"
APP_ID = "6834858888"
APP_STORE = f"https://apps.apple.com/app/id{APP_ID}"
EMAIL = "solostaseraofficial@gmail.com"
INSTAGRAM = "https://instagram.com/solo.stasera"
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
TODAY = "2026-11-14"
LANGS = ["en", "tr", "es"]
VER = "1"

WORDS = {  # tiny builder-only strings
    "months_en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "months_tr": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
    "months_es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
    "en": {"all": "All", "sticker": "Free ✦ iPhone", "play": "Play or pause the demo", "guides_n": "guides"},
    "tr": {"all": "Tümü", "sticker": "Ücretsiz ✦ iPhone", "play": "Demoyu oynat ya da duraklat", "guides_n": "rehber"},
    "es": {"all": "Todos", "sticker": "Gratis ✦ iPhone", "play": "Reproducir o pausar la demo", "guides_n": "guías"},
}
SITE_PRIVACY = {
    "en": ("11. This website", "This website has no cookies, analytics or ads. It is hosted on GitHub Pages, which may log basic technical data such as IP addresses for security. Fonts load from Google Fonts. The demo audio plays straight from this site, and nothing you do on these pages is sent anywhere."),
    "tr": ("11. Bu web sitesi", "Bu sitede çerez, analiz aracı ya da reklam yok. Site GitHub Pages üzerinde barınıyor; GitHub güvenlik için IP adresi gibi temel teknik verileri kaydedebilir. Yazı tipleri Google Fonts'tan yükleniyor. Demo sesleri doğrudan bu siteden çalıyor ve bu sayfalarda yaptığın hiçbir şey bir yere gönderilmiyor."),
    "es": ("11. Esta web", "Esta web no usa cookies, analíticas ni anuncios. Está alojada en GitHub Pages, que puede registrar datos técnicos básicos como direcciones IP por seguridad. Las fuentes se cargan desde Google Fonts. El audio de la demo se reproduce desde esta misma web y nada de lo que haces en estas páginas se envía a ningún sitio."),
}
VOICE_NAMES = {"velvet_whisper": "Velvet Whisper", "pink_muse": "Pink Muse", "runway_confidence": "Runway", "after_dark": "After Dark"}
AURAS = [("Pink Aura", True), ("Ocean at 2AM", True), ("Hotel Rain", False), ("Dreamy Static", False), ("Silk Noise", False),
         ("Celestial Drift", False), ("111 Tone", False), ("432 Tone", False), ("528 Tone", False), ("639 Tone", False),
         ("777 Tone", False), ("888 Tone", False), ("963 Tone", False)]
SHOT_ORDER = ["discover", "detail", "player", "mycds", "night", "board", "dream", "create", "wishlist"]
SHOTS = {  # real app screenshots (iPhone 17 Pro, After Dark theme); EN/ES pages show the English app
    "discover": {"en": "Discover: tonight's CD, picked for you", "tr": "Keşfet: bu gecenin CD'si seni bekliyor", "es": "Discover: el CD de esta noche, elegido para ti"},
    "detail": {"en": "Pick 10, 20 or 60 minutes, a voice and an aura", "tr": "10, 20 ya da 60 dakika; sesini ve auranı seç", "es": "Elige 10, 20 o 60 minutos, una voz y un aura"},
    "player": {"en": "Now playing, with the affirmation on screen", "tr": "Şimdi çalıyor; olumlama ekranda", "es": "Reproduciendo, con la afirmación en pantalla"},
    "mycds": {"en": "Daily rituals and your favourite CDs", "tr": "Günlük ritüeller ve favori CD'lerin", "es": "Rituales diarios y tus CDs favoritos"},
    "night": {"en": "The Bedtime ritual in the dim night player", "tr": "Loş gece oynatıcısında uyku öncesi ritüel", "es": "El ritual de noche en el reproductor nocturno"},
    "board": {"en": "Your dreams as a vision board", "tr": "Hayallerin, hayal panosu olarak", "es": "Tus sueños como vision board"},
    "dream": {"en": "Each dream with its affirmation, progress and CD", "tr": "Her hayal; olumlaması, ilerlemesi ve CD'siyle", "es": "Cada sueño con su afirmación, su progreso y su CD"},
    "create": {"en": "Create Your Own: a CD of lines that sound like you", "tr": "Kendi CD'ni Yarat: sana benzeyen olumlamalar", "es": "Create Your Own: un CD con frases que suenan a ti"},
    "wishlist": {"en": "Your Manifest List at a glance", "tr": "Manifest Listen bir bakışta", "es": "Tu Manifest List de un vistazo"},
}
INSIDE = {
    "en": ("Inside the app", "Real screens. Zero filter.", "Straight from the iPhone app in the After Dark theme. What you see is what you get, babe. Swipe through."),
    "tr": ("Uygulamanın içi", "Gerçek ekranlar. Sıfır filtre.", "Doğrudan iPhone uygulamasından, After Dark temasıyla. Ne görüyorsan o, aşkım. Kaydırarak gez."),
    "es": ("Dentro de la app", "Pantallas reales. Cero filtros.", "Directo de la app para iPhone, con el tema After Dark. Lo que ves es lo que hay, reina. En un iPhone en español, la app se ve en inglés."),
}
GUIDE_SHOTS = {"manifest": ["detail", "player"], "sleep": ["night", "mycds"], "morning": ["mycds"], "money": ["detail"],
               "lucky": ["discover"], "vision": ["board", "dream"], "confidence": ["player"], "love": ["mycds"],
               "write": ["create"], "app": ["discover", "player", "night"]}


def shot_src(lang, name, w):
    return f"{A}shots/{'tr' if lang == 'tr' else 'en'}-{name}-{w}.webp"


def phone_shot(lang, name, eager=False):
    cap = SHOTS[name][lang]
    load = "" if eager else ' loading="lazy" decoding="async"'
    return (f'<figure class="phone-shot"><div class="frame"><img src="{shot_src(lang, name, 600)}" '
            f'srcset="{shot_src(lang, name, 600)} 600w, {shot_src(lang, name, 1000)} 1000w" sizes="(max-width: 600px) 62vw, 250px" '
            f'width="600" height="1304" alt="{esc("DIVA app: " + cap if lang == "en" else "DIVA: " + cap)}"{load}><span class="island" aria-hidden="true"></span></div>'
            f'<figcaption>{esc(cap)}</figcaption></figure>')


DEMO_CDS = ["that_girl_energy", "rich_girl_frequency", "beauty_sleep_for_divas"]
HERO_CD = "that_girl_energy"


def nice_date(lang, iso):
    y, mo, d = (int(x) for x in iso.split("-"))
    name = WORDS["months_" + lang][mo - 1]
    return {"en": f"{name} {d}, {y}", "tr": f"{d} {name} {y}", "es": f"{d} de {name} de {y}"}[lang]


def load_lang(code):
    path = os.path.join(SRC, "content", f"{code}.py")
    spec = importlib.util.spec_from_file_location(code, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


APP = json.load(open(os.path.join(SRC, "data/app.json")))
PICKS = json.load(open(os.path.join(SRC, "data/card_picks.json")))
TIMINGS = json.load(open(os.path.join(SITE, "assets/audio/demo.json")))
CDS = {c["id"]: c for c in APP["cds"]}
def _complete(code):
    try:
        m = load_lang(code)
    except Exception as e:  # a translation still being written
        print(f"skipping {code}: {e}")
        return None
    need = ("PATHS", "UI", "HOME", "FAQ", "GUIDES", "SUPPORT", "PRIVACY")
    if not all(hasattr(m, k) for k in need) or len(m.GUIDES) != 10:
        print(f"skipping {code}: incomplete")
        return None
    return m


ONLY = next((a.split("=", 1)[1].split(",") for a in sys.argv if a.startswith("--langs=")), LANGS)
L = {c: m for c in LANGS if c in ONLY and os.path.exists(os.path.join(SRC, "content", f"{c}.py")) and (m := _complete(c))}
LIVE = [c for c in LANGS if c in L]


def esc(s):
    return html.escape(str(s), quote=True)


def absu(path):
    return ORIGIN + path


def store(lang, where):
    return f"https://apps.apple.com/app/apple-store/id{APP_ID}?pt=128720446&ct=web-diva-{lang}-{where}&mt=8"


def jdump(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def write(path, text):
    full = os.path.join(SITE, path.removeprefix(BASE))
    if full.endswith("/"):
        full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


# ---------- app text per language ----------
def text_lang(lang):
    return "tr" if lang == "tr" else "en"


def cd_title(lang, cid):
    return CDS[cid][text_lang(lang)]["title"]


def cd_sub(lang, cid):
    m = L[lang]
    if getattr(m, "CD_TEXT", {}).get(cid, {}).get("subtitle"):
        return m.CD_TEXT[cid]["subtitle"]
    return CDS[cid][text_lang(lang)]["subtitle"]


def cd_summary(lang, cid):
    m = L[lang]
    if getattr(m, "CD_TEXT", {}).get(cid, {}).get("summary"):
        return m.CD_TEXT[cid]["summary"]
    return CDS[cid][text_lang(lang)]["summary"]


def cat_title(lang, cat):
    m = L[lang]
    if getattr(m, "CATEGORIES", {}).get(cat):
        return m.CATEGORIES[cat]
    c = next(x for x in APP["categories"] if x["id"] == cat)
    return c["title"][text_lang(lang)]


def ritual_days(lang, kind):
    m = L[lang]
    if getattr(m, "RITUAL_THEMES", {}).get(kind):
        return m.RITUAL_THEMES[kind]
    return APP["rituals"][kind][text_lang(lang)]["days"]


def card_line(lang, cid, i):
    m = L[lang]
    if lang == "es":
        return m.CARD_LINES.get(f"{cid}:{i}") or APP["lines"][cid]["en"][i]
    return APP["lines"][cid][text_lang(lang)][i]


def cover(cid):
    return A + "covers/" + CDS[cid]["cover"].replace("cover_", "").replace("_", "-") + ".webp"


# ---------- urls ----------
def page_url(lang, key):
    return L[lang].PATHS[key]


def guide_url(lang, gid):
    g = next(x for x in L[lang].GUIDES if x["id"] == gid)
    return L[lang].PATHS["guides"] + g["slug"] + "/"


def alternates(key, gid=None):
    out = {}
    for lang in LIVE:
        out[lang] = guide_url(lang, gid) if gid else page_url(lang, key)
    return out


# ---------- images ----------
def photo(slug, alt, cls="", eager=False, sizes="(max-width: 860px) 92vw, 600px"):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    if os.path.exists(os.path.join(SITE, f"assets/img/{slug}-1200.webp")):
        return (f'<img class="{cls}" src="{A}img/{slug}-1200.webp" srcset="{A}img/{slug}-640.webp 640w, {A}img/{slug}-1200.webp 1200w" '
                f'sizes="{sizes}" width="1200" height="1200" alt="{esc(alt)}" {load}>')
    return f'<img class="{cls}" src="{A}img/{slug}.webp" width="800" height="1340" alt="{esc(alt)}" {load}>'


def photo_url(slug):
    p = f"assets/img/{slug}-1200.webp"
    return absu(BASE + p) if os.path.exists(os.path.join(SITE, p)) else absu(f"{A}img/{slug}.webp")


# ---------- shared fragments ----------
APPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.37 12.76c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.77-3.32-1.8-1.41-.14-2.76.84-3.47.84-.72 0-1.82-.82-3-.8-1.54.02-2.96.9-3.76 2.28-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 1.23-.02 2.01-1.12 2.76-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.65zM14.1 6.02c.63-.77 1.06-1.83.94-2.89-.91.04-2.01.6-2.66 1.37-.58.67-1.09 1.76-.95 2.8 1.01.08 2.04-.51 2.67-1.28z"/></svg>'
PLAY_SVG = '<svg class="i-play" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4.5v15a1 1 0 0 0 1.5.86l12.5-7.5a1 1 0 0 0 0-1.72L8.5 3.64A1 1 0 0 0 7 4.5z"/></svg><svg class="i-pause" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="5.5" y="4" width="4.5" height="16" rx="1.4"/><rect x="14" y="4" width="4.5" height="16" rx="1.4"/></svg>'


def store_btn(lang, where):
    u = L[lang].UI
    return (f'<a class="store" href="{esc(store(lang, where))}" aria-label="{esc(u["appstore_aria"])}">{APPLE_SVG}'
            f'<span><small>{esc(u["appstore_small"])}</small><strong>{esc(u["appstore_big"])}</strong></span></a>')


def qr(lang):
    u = L[lang].UI
    return f'<div class="qr"><img src="{A}appstore-qr.svg" width="88" height="88" alt="" loading="lazy"><span>{esc(u["qr_caption"])}</span></div>'


def cd_card(lang, cid, where="cd", tag="a"):
    c = CDS[cid]
    u = L[lang].UI
    badge = f'<span class="tag pro">{u["pro"]}</span>' if c["pro"] else f'<span class="tag">{u["free"]}</span>'
    return (f'<a class="cd" href="{esc(store(lang, where))}" data-era="{c["category"]}">'
            f'<div class="case">{badge}<div class="cover"><img src="{cover(cid)}" width="480" height="480" alt="{esc(cd_title(lang, cid))}" loading="lazy"></div>'
            f'<div class="disc" aria-hidden="true"><img src="{cover(cid)}" alt="" loading="lazy"></div></div>'
            f'<div class="era-label">{esc(cat_title(lang, c["category"]))}</div>'
            f'<h3>{esc(cd_title(lang, cid))}</h3><p>{esc(cd_sub(lang, cid))}</p></a>')


def cta_box(lang, where):
    u = L[lang].UI
    return (f'<aside class="cta-box reveal"><div class="disc" aria-hidden="true"><img src="{cover(HERO_CD)}" alt="" loading="lazy"></div>'
            f'<div><h3>{esc(u["cta_title"])}</h3><p>{esc(u["cta_body"])}</p>{store_btn(lang, where)}</div></aside>')


def resolve(lang, text, where="guide"):
    m = L[lang]
    for k in ("home", "guides", "faq", "support", "privacy"):
        text = text.replace("{{" + k + "}}", m.PATHS[k])
    text = text.replace("{{appstore}}", esc(store(lang, where)))
    text = re.sub(r"\{\{guide:([a-z_]+)\}\}", lambda mm: guide_url(lang, mm.group(1)), text)
    text = re.sub(r"\[\[img:([a-z0-9-]+)\|([^\]]+)\]\]",
                  lambda mm: f'<figure class="reveal">{photo(mm.group(1), mm.group(2), sizes="(max-width: 1020px) 92vw, 760px")}</figure>', text)
    text = re.sub(r"\[\[cd:([a-z_]+)\]\]",
                  lambda mm: (f'<a class="inline-cd" href="{esc(store(lang, where))}"><img src="{cover(mm.group(1))}" alt="" width="76" height="76" loading="lazy">'
                              f'<span><strong>{esc(cd_title(lang, mm.group(1)))}</strong><span>{esc(cd_sub(lang, mm.group(1)))}</span></span></a>'), text)
    text = text.replace("[[cta]]", cta_box(lang, where))
    return text


def langs_switch(lang, alts):
    out = []
    for code in LIVE:
        cur = ' aria-current="true"' if code == lang else ""
        out.append(f'<a href="{alts[code]}" hreflang="{code}" lang="{code}"{cur} title="{esc(L[code].NAME)}">{code.upper()}</a>')
    return f'<div class="langs" role="group" aria-label="{esc(L[lang].UI["lang_label"])}">{"".join(out)}</div>'


def nav(lang, current, alts):
    u, p = L[lang].UI, L[lang].PATHS

    def item(key, label):
        cur = ' aria-current="page"' if current == key else ""
        return f'<a href="{p[key]}"{cur}>{esc(label)}</a>'
    return f'''<header class="nav"><div class="wrap">
<a class="brand" href="{p["home"]}" aria-label="DIVA"><img src="{A}logo-460.png" width="460" height="213" alt="DIVA"></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">{esc(u["menu"])}</button>
<nav class="nav-links" id="nav-links" aria-label="DIVA">
{item("guides", u["nav_guides"])}{item("faq", u["nav_faq"])}{item("support", u["nav_support"])}
{langs_switch(lang, alts)}
<a class="btn sm" href="{esc(store(lang, "nav"))}">{esc(u["nav_cta"])}</a>
</nav></div></header>'''


def footer(lang, alts):
    u, p = L[lang].UI, L[lang].PATHS
    langs = "".join(f'<li><a href="{alts[c]}" hreflang="{c}" lang="{c}">{esc(L[c].NAME)}</a></li>' for c in LIVE)
    return f'''<footer class="footer"><div class="wrap">
<div class="cols">
<div><img class="flogo" src="{A}logo-460.png" width="460" height="213" alt="DIVA" loading="lazy"><p>{esc(u["footer_tagline"])}</p>{store_btn(lang, "footer")}</div>
<div><h4>{esc(u["footer_app"])}</h4><ul><li><a href="{p["home"]}">DIVA</a></li><li><a href="{p["guides"]}">{esc(u["nav_guides"])}</a></li><li><a href="{p["faq"]}">{esc(u["nav_faq"])}</a></li><li><a href="{APP_STORE}">App Store</a></li></ul></div>
<div><h4>{esc(u["footer_help"])}</h4><ul><li><a href="{p["support"]}">{esc(u["nav_support"])}</a></li><li><a href="{p["privacy"]}">{esc(u["nav_privacy"])}</a></li><li><a href="{EULA}">{esc(u["footer_terms"])}</a></li><li><a href="mailto:{EMAIL}">{esc(u["footer_contact"])}</a></li><li><a href="{INSTAGRAM}">Instagram</a></li></ul></div>
<div><h4>{esc(u["lang_label"])}</h4><ul>{langs}</ul></div>
</div>
<div class="fine"><span>{esc(u["footer_disclaimer"])}</span><span>{esc(u["footer_rights"])}</span></div>
</div></footer>'''


# ---------- structured data ----------
PERSON = {"@type": "Person", "@id": ORIGIN + "/#person", "name": "Gül Eda Aydemir", "alternateName": "Gul Eda Aydemir",
          "jobTitle": "Independent iOS developer", "url": ORIGIN + "/about/", "email": "mailto:" + EMAIL,
          "sameAs": ["https://apps.apple.com/us/developer/gul-eda-aydemir/id1889159460", INSTAGRAM]}


def app_ld(lang):
    en = L["en"]
    return {
        "@type": "MobileApplication", "@id": absu(BASE) + "#app", "name": "DIVA",
        "alternateName": ["DIVA: Affirmations & Manifest", "DIVA: Olumlamalar & Manifest", "DIVA Affirmations", "DIVA affirmation app"],
        "description": ("DIVA is an affirmation and manifestation app for iPhone where every theme is an affirmation CD. "
                        "Users pick a CD (for example That Girl Energy, Rich Girl Frequency or Beauty Sleep for Divas), choose one of four AI voices "
                        "and a soundscape, and listen to first-person affirmations for 10, 20 or 60 minutes. It includes Morning and Bedtime affirmation "
                        "meditations with a theme for each weekday, Make Your Own CD, and a Wishlist with a vision board. No account, no ads, no tracking."),
        "url": absu(BASE), "sameAs": [APP_STORE], "installUrl": APP_STORE, "downloadUrl": APP_STORE,
        "applicationCategory": "LifestyleApplication", "applicationSubCategory": "Affirmations & manifestation",
        "operatingSystem": "iOS 17.0 or later", "availableOnDevice": "iPhone", "inLanguage": ["en", "tr"],
        "image": absu(A + "icon-512.png"), "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
        "screenshot": [{"@type": "ImageObject", "url": absu(shot_src("en", n, 1000)), "width": 1000, "height": 2174, "caption": SHOTS[n]["en"]} for n in SHOT_ORDER],
        "isAccessibleForFree": True,
        "featureList": [
            "20 affirmation CDs across 12 themes (confidence, beauty, dream life, money, love, self-worth, career, dream home, gratitude, morning, sleep, calm)",
            "10, 20 and 60 minute sessions", "Morning and Bedtime affirmation meditations with a theme for every weekday",
            "Four AI voices: Velvet Whisper, Pink Muse, Runway, After Dark (narration in English; interface in English and Turkish)",
            "Soundscapes including Pink Aura, Ocean at 2AM, Hotel Rain and 432/528/963 Hz tones",
            "Make Your Own CD", "Wishlist with progress tracking, milestones and a photo vision board",
            "Sleep timer, background playback, lock screen controls, works offline",
            "No account, no ads, no tracking; data stays on the iPhone"],
        "offers": [
            {"@type": "Offer", "name": "DIVA (free)", "price": "0", "priceCurrency": "USD", "category": "free"},
            {"@type": "Offer", "name": "DIVA PRO Monthly", "price": "5.99", "priceCurrency": "USD", "category": "subscription"},
            {"@type": "Offer", "name": "DIVA PRO Yearly", "price": "29.99", "priceCurrency": "USD", "category": "subscription"},
            {"@type": "Offer", "name": "DIVA PRO Lifetime", "price": "69.99", "priceCurrency": "USD", "category": "one-time purchase"}],
    }


def website_ld(lang):
    return {"@type": "WebSite", "@id": absu(BASE) + "#website", "url": absu(BASE), "name": "DIVA",
            "inLanguage": LIVE, "publisher": {"@id": PERSON["@id"]}, "about": {"@id": absu(BASE) + "#app"}}


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": absu(u)} for i, (n, u) in enumerate(items)]}


def faq_ld(pairs, url):
    return {"@type": "FAQPage", "@id": absu(url) + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a).strip()}} for q, a in pairs]}


def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


# ---------- page shell ----------
FONTS = "https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=DM+Sans:opsz,wght@9..40,400..700&family=Great+Vibes&family=VT323&display=swap"


def shell(lang, *, title, desc, url, alts, body, current="", og_image, og_alt, og_type="website", ld=(), extra=""):
    m = L[lang]
    hreflang = "".join(f'<link rel="alternate" hreflang="{c}" href="{absu(alts[c])}">' for c in LIVE)
    hreflang += f'<link rel="alternate" hreflang="x-default" href="{absu(alts.get("en", url))}">'
    og_alt_loc = "".join(f'<meta property="og:locale:alternate" content="{L[c].OG_LOCALE}">' for c in LIVE if c != lang)
    graph = {"@context": "https://schema.org", "@graph": [PERSON, website_ld(lang), *ld]}
    hints = {c: {"text": L[c].UI["lang_hint"], "go": L[c].UI["lang_hint_go"], "close": L[c].UI["lang_hint_close"], "href": alts[c]} for c in LIVE}
    return f'''<!DOCTYPE html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{absu(url)}">
{hreflang}
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Gül Eda Aydemir">
<meta name="theme-color" content="#170b16">
<meta name="color-scheme" content="dark">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="DIVA">
<meta property="og:locale" content="{m.OG_LOCALE}">{og_alt_loc}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{absu(url)}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" type="image/png" sizes="32x32" href="{A}favicon-32.png">
<link rel="apple-touch-icon" href="{A}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{A}diva.css?v={VER}">
<link rel="alternate" type="text/plain" href="{BASE}llms.txt" title="DIVA facts for AI assistants">
{extra}<script type="application/ld+json">{jdump(graph)}</script>
</head>
<body>
<a class="skip" href="#main">{esc(m.UI["skip"])}</a>
{nav(lang, current, alts)}
<main id="main">
{body}
</main>
{footer(lang, alts)}
<script type="application/json" id="lang-hints">{jdump(hints)}</script>
<script src="{A}diva.js?v={VER}" defer></script>
</body>
</html>
'''


def og(lang, name):
    return absu(f"{A}og/{name}-{lang}.jpg")


# ---------- home ----------
def home(lang):
    m = L[lang]
    h, u, w = m.HOME, m.UI, WORDS[lang]
    alts = alternates("home")
    url = m.PATHS["home"]
    order = ["that_girl_energy", "rich_girl_frequency", "love_looks_good_on_me", "born_to_be_iconic", "the_life_i_ordered",
             "pretty_girls_dont_chase", "princess_treatment", "everything_works_out", "beauty_sleep_for_divas", "wake_up_icon",
             "thank_you_universe", "whisper_to_your_future_self", "dream_body_dream_energy", "million_dollar_energy", "first_class_only",
             "penthouse_state_of_mind", "ceo_after_hours", "im_the_prize", "perfect_inner_circle", "soft_girl_reset"]
    cats = []
    for cid in order:
        if CDS[cid]["category"] not in cats:
            cats.append(CDS[cid]["category"])
    marquee = "".join(f"<span>{esc(cd_title(lang, c))}</span>" for c in order[:10])
    chips = f'<button class="chip" type="button" data-era="all" aria-pressed="true">{esc(w["all"])}</button>' + "".join(
        f'<button class="chip" type="button" data-era="{c}" aria-pressed="false">{esc(cat_title(lang, c))}</button>' for c in cats)
    shelf = "".join(cd_card(lang, c, "shelf") for c in order)

    # demo
    alang = "en"  # narration is English only for now (Turkish voices paused); TR/ES show translations
    demo = {"first": DEMO_CDS[0], "audioLang": alang, "base": A + "audio/", "timings": {},
            "voices": [{"id": v, "name": VOICE_NAMES[v]} for v in VOICE_NAMES], "cds": {}}
    for cid in DEMO_CDS:
        lines = APP["demo"][cid][alang]
        entry = {"title": cd_title(lang, cid), "cover": cover(cid), "lines": [esc(x) for x in lines]}
        if lang == "es" and getattr(m, "DEMO_TRANSLATION", {}).get(cid):
            entry["tr"] = [esc(x) for x in m.DEMO_TRANSLATION[cid]]
        elif lang == "tr":
            entry["tr"] = [esc(x) for x in APP["demo"][cid]["tr"]]
        demo["cds"][cid] = entry
        for v in VOICE_NAMES:
            demo["timings"][f"{cid}/{v}/{alang}"] = TIMINGS[f"{cid}/{v}/{alang}"]
    first = demo["cds"][DEMO_CDS[0]]
    pre_lyrics = "".join(f"<li>{l}{('<small>' + first['tr'][i] + '</small>') if first.get('tr') else ''}</li>" for i, l in enumerate(first["lines"]))
    cd_btns = "".join(f'<button type="button" data-cd="{c}" aria-pressed="{"true" if i == 0 else "false"}"><img src="{cover(c)}" alt="" width="34" height="34">{esc(cd_title(lang, c))}</button>' for i, c in enumerate(DEMO_CDS))
    v_btns = "".join(f'<button type="button" data-voice="{v}" aria-pressed="{"true" if i == 0 else "false"}">{n}<small>{esc(h["voices"][v][0])}</small></button>' for i, (v, n) in enumerate(VOICE_NAMES.items()))
    lang_note = f'<p class="note">{esc(h["demo_lang_note"])}</p>' if h.get("demo_lang_note") else ""

    # rituals
    def week(kind):
        days = ritual_days(lang, kind)
        return '<div class="week">' + "".join(f"<div><b>{esc(h['weekdays'][i])}</b>{esc(days[i])}</div>" for i in range(7)) + "</div>"

    # wishlist board
    board = ""
    for i, (title, pct, img) in enumerate(h["wish_dreams"]):
        stamp = f'<span class="stamp">{esc(h["wish_achieved"])}</span>' if pct >= 100 else ""
        board += (f'<figure class="polaroid">{photo(img, title, sizes="(max-width: 860px) 44vw, 260px")}{stamp}'
                  f'<figcaption class="sr">{esc(title)}</figcaption><div class="dream-title">{esc(title)}</div><div class="progress" role="img" aria-label="{pct}%"><i style="--p:{pct}%"></i></div></figure>')

    # card pull
    card = {}
    for era, picks in PICKS.items():
        card[era] = [[card_line(lang, c, i), cd_title(lang, c)] for c, i in picks]
    card_chips = "".join(f'<button class="chip" type="button" data-era="{e}" aria-pressed="{"true" if i == 0 else "false"}">{esc(cat_title(lang, e))}</button>' for i, e in enumerate(PICKS))

    voices = "".join(f'''<article class="voice reveal" style="--d:{i * .08}s"><div class="wave" aria-hidden="true">{"".join(f'<i style="--i:{k}"></i>' for k in range(9))}</div>
<h3>{n}</h3><div class="desc">{esc(h["voices"][v][0])}</div><p>{esc(h["voices"][v][1])}</p></article>''' for i, (v, n) in enumerate(VOICE_NAMES.items()))
    auras = "".join(f'<span class="aura{" free" if free else ""}">{n}</span>' for n, free in AURAS)
    free_items = "".join(f"<li>{esc(x)}</li>" for x in h["free_items"])
    pro_items = "".join(f"<li>{esc(x)}</li>" for x in h["pro_items"])
    plans = "".join(f"<span>{esc(a)}<b>{esc(b)}</b></span>" for a, b in h["plans"])

    posts = "".join(post_card(lang, g, i) for i, g in enumerate(m.GUIDES[:3]))
    faqs = [it for grp in m.FAQ for it in grp["items"]][:6]
    faq_html = "".join(f'<details class="qa"><summary>{esc(q["q"])}</summary><div class="ans">{resolve(lang, q["a"], "faq")}</div></details>' for q in faqs)
    msgs = "".join(f'<p class="phone-msg">{esc(x)}</p>' for x in h["phone_msgs"])
    wish_pts = "".join(f"<li>{esc(x)}</li>" for x in h["wish_points"])
    badges = "".join(f"<li>{esc(b)}</li>" for b in h["hero_badges"])

    body = f'''
<section class="hero">
<div class="sparkles" data-n="22" aria-hidden="true"></div>
<div class="wrap">
<div class="hero-copy">
<span class="eyebrow">{esc(h["hero_eyebrow"])}</span>
<div class="hero-logo shine" style="--logo:url({A}logo.webp)"><img src="{A}logo.webp" width="920" height="425" alt="DIVA" fetchpriority="high"></div>
<span class="script">{esc(h["hero_script"])}</span>
<h1><span class="chrome-text">{esc(h["hero_h1"])}</span></h1>
<p class="lead">{esc(h["hero_lead"])}</p>
<div class="hero-ctas">{store_btn(lang, "hero")}<a class="btn ghost" href="#demo">▶ {esc(h["hero_cta2"])}</a></div>
<ul class="badges">{badges}</ul>
</div>
<div class="stage" aria-hidden="true">
<figure class="polaroid p1"><span class="tape"></span>{photo("pink-closet", "", sizes="260px", eager=True)}<figcaption>{esc(cat_title(lang, "dream_life"))}</figcaption></figure>
<figure class="polaroid p2"><span class="tape"></span>{photo("poolside-muse", "", sizes="260px")}<figcaption>{esc(cat_title(lang, "confidence"))}</figcaption></figure>
<div class="disc-wrap"><div class="disc"><img src="{cover(HERO_CD)}" alt="" width="480" height="480"></div></div>
<div class="phone"><div class="phone-screen"><div class="phone-top"><span>▂▄▆ DIVA</span><span>{esc(h["phone_time"])}</span></div>
<div class="phone-from">{esc(h["phone_from"])}</div>{msgs}<span class="phone-typing"><i></i><i></i><i></i></span></div><div class="phone-keys">{"<i></i>" * 9}</div></div>
<div class="sticker">{esc(w["sticker"])}</div>
</div>
</div>
</section>

<div class="marquee" aria-hidden="true"><div class="track">{marquee}{marquee}</div></div>

<section class="section tight" id="inside">
<div class="wrap">
<div class="section-head reveal"><span class="kicker">{esc(INSIDE[lang][0])}</span><h2>{esc(INSIDE[lang][1])}</h2><p class="lead">{esc(INSIDE[lang][2])}</p></div>
<div class="shots">{"".join(phone_shot(lang, n) for n in SHOT_ORDER)}</div>
</div>
</section>

<section class="section" id="cds">
<div class="wrap">
<div class="section-head reveal"><span class="kicker">{esc(h["eras_kicker"])}</span><h2>{esc(h["eras_h2"])}</h2><p class="lead">{esc(h["eras_lead"])}</p></div>
<div class="era-filter reveal" role="group" aria-label="{esc(h["eras_kicker"])}">{chips}</div>
<div class="shelf">{shelf}</div>
<p class="note">✦ {esc(h["eras_note"])}</p>
</div>
</section>

<section class="section" id="demo">
<div class="wrap">
<div class="section-head center reveal"><span class="kicker">{esc(h["demo_kicker"])}</span><h2>{esc(h["demo_h2"])}</h2><p class="lead">{esc(h["demo_lead"])}</p></div>
<div class="player reveal">
<div class="sparkles" data-n="12" aria-hidden="true"></div>
<div><div class="disc paused"><img src="{first["cover"]}" alt="{esc(first["title"])}" width="480" height="480"></div></div>
<div class="player-side">
<div><div class="label">{esc(h["demo_pick"])}</div><div class="pick">{cd_btns}</div></div>
<div><div class="label">{esc(h["demo_voice"])}</div><div class="pick voices">{v_btns}</div></div>
<div class="transport"><button class="play" type="button" aria-label="{esc(w["play"])}">{PLAY_SVG}</button>
<div class="now"><span class="label">{esc(h["demo_now"])}</span><strong>{esc(first["title"])}</strong><span class="who">Velvet Whisper</span><div class="bar"><i></i></div></div></div>
<label class="toggle"><input type="checkbox" id="aura" checked> {esc(h["demo_aura"])}</label>
<ol class="lyrics">{pre_lyrics}</ol>
{lang_note}<p class="note">{esc(h["demo_note"])}</p>
</div>
</div>
<script type="application/json" id="demo-data">{jdump(demo)}</script>
</div>
</section>

<section class="section" id="rituals">
<div class="wrap">
<div class="section-head reveal"><span class="kicker">{esc(h["rituals_kicker"])}</span><h2>{esc(h["rituals_h2"])}</h2><p class="lead">{esc(h["rituals_lead"])}</p></div>
<div class="rituals">
<article class="ritual reveal">{photo("backdrop-sunset", "")}<span class="script">☀</span><h3>{esc(h["morning_title"])}</h3><p>{esc(h["morning_body"])}</p>{week("morning")}</article>
<article class="ritual reveal" style="--d:.12s">{photo("backdrop-palms", "")}<span class="script">☾</span><h3>{esc(h["night_title"])}</h3><p>{esc(h["night_body"])}</p>{week("night")}</article>
</div>
<p class="note" style="margin-top:20px">✦ {esc(h["rituals_note"])}</p>
</div>
</section>

<section class="section" id="wishlist">
<div class="wrap split">
<div class="reveal"><span class="kicker">{esc(h["wish_kicker"])}</span><h2>{esc(h["wish_h2"])}</h2><p class="lead">{esc(h["wish_lead"])}</p><ul class="ticks">{wish_pts}</ul></div>
<div class="duo reveal">{phone_shot(lang, "board")}{phone_shot(lang, "dream")}</div>
</div>
</section>

<section class="section" id="sign">
<div class="wrap pull">
<div class="reveal"><span class="kicker">{esc(h["card_kicker"])}</span><h2>{esc(h["card_h2"])}</h2><p class="lead">{esc(h["card_lead"])}</p>
<div class="era-filter" role="group" aria-label="{esc(h["card_kicker"])}">{card_chips}</div>
<button class="btn again" type="button" hidden>✦ {esc(h["card_again"])}</button></div>
<div class="reveal"><button class="flip" type="button" aria-label="{esc(h["card_button"])}"><span class="flip-in">
<span class="face back"><img src="{A}logo.webp" alt="" width="920" height="425"><span>{esc(h["card_button"])}</span></span>
<span class="face front" aria-live="polite"><span class="line">{esc(h["card_back"])}</span><span class="from">{esc(h["card_from"])}<b></b></span></span>
</span></button></div>
</div>
<script type="application/json" id="card-data">{jdump(card)}</script>
</section>

<section class="section" id="voices">
<div class="wrap">
<div class="section-head center reveal"><span class="kicker">{esc(h["voices_kicker"])}</span><h2>{esc(h["voices_h2"])}</h2><p class="lead">{esc(h["voices_lead"])}</p></div>
<div class="grid4">{voices}</div>
<div class="section-head center reveal" style="margin:clamp(56px,8vw,96px) 0 0"><span class="kicker">{esc(h["auras_kicker"])}</span><h2>{esc(h["auras_h2"])}</h2><p class="lead">{esc(h["auras_lead"])}</p><div class="auras">{auras}</div></div>
</div>
</section>

<section class="section tight" id="privacy">
<div class="wrap"><div class="band reveal"><div class="sparkles" data-n="16" aria-hidden="true"></div>
<span class="kicker">{esc(h["priv_kicker"])}</span><h2 class="chrome-text">{esc(h["priv_h2"])}</h2><p>{esc(h["priv_body"])}</p>
<a class="btn ghost" href="{m.PATHS["privacy"]}">{esc(h["priv_link"])}</a></div></div>
</section>

<section class="section" id="pricing">
<div class="wrap">
<div class="section-head center reveal"><span class="kicker">{esc(h["price_kicker"])}</span><h2>{esc(h["price_h2"])}</h2></div>
<div class="prices">
<article class="price reveal"><h3>{esc(h["free_title"])}</h3><div class="amount">{esc(h["free_price"])}</div><ul class="ticks">{free_items}</ul>{store_btn(lang, "pricing-free")}</article>
<article class="price pro reveal" style="--d:.12s"><span class="crown" aria-hidden="true">👑</span><h3 class="chrome-text">{esc(h["pro_title"])}</h3><div class="amount">{esc(h["pro_price"])}</div><ul class="ticks">{pro_items}</ul><div class="plans">{plans}</div></article>
</div>
<p class="note center" style="margin-top:20px">{esc(h["price_note"])}</p>
</div>
</section>

<section class="section" id="letter">
<div class="wrap">
<article class="letter reveal"><span class="tape"></span><span class="tape r"></span>
<span class="kicker" style="color:#b0005f">{esc(h["letter_kicker"])}</span><h2>{esc(h["letter_h2"])}</h2>
{resolve(lang, h["letter_body"], "letter")}
<p class="sign">{esc(h["letter_sign"])}</p>
<img class="lips" src="{A}img/art-lips-star.webp" alt="" width="92" height="154" loading="lazy">
</article>
</div>
</section>

<section class="section" id="diaries">
<div class="wrap">
<div class="section-head reveal"><span class="kicker">{esc(h["diaries_kicker"])}</span><h2>{esc(h["diaries_h2"])}</h2><p class="lead">{esc(h["diaries_lead"])}</p></div>
<div class="posts">{posts}</div>
<p style="margin-top:28px"><a class="btn ghost" href="{m.PATHS["guides"]}">{esc(h["diaries_all"])} →</a></p>
</div>
</section>

<section class="section" id="faq">
<div class="wrap">
<div class="section-head center reveal"><span class="kicker">{esc(h["faq_kicker"])}</span><h2>{esc(h["faq_h2"])}</h2></div>
<div class="faq">{faq_html}</div>
<p class="center" style="margin-top:26px"><a class="btn ghost" href="{m.PATHS["faq"]}">{esc(h["faq_all"])} →</a></p>
</div>
</section>

<section class="section final">
<div class="sparkles" data-n="20" aria-hidden="true"></div>
<div class="wrap reveal">
<span class="script" style="transform-origin:center">{esc(h["final_script"])}</span>
<h2>{esc(h["final_h2"])}</h2><p class="lead">{esc(h["final_body"])}</p>
<div class="store-row">{store_btn(lang, "final")}{qr(lang)}</div>
</div>
</section>
'''
    page_ld = {"@type": "WebPage", "@id": absu(url) + "#webpage", "url": absu(url), "name": h["title"], "description": h["description"],
               "inLanguage": lang, "isPartOf": {"@id": absu(BASE) + "#website"}, "about": {"@id": absu(BASE) + "#app"},
               "primaryImageOfPage": {"@type": "ImageObject", "url": og(lang, "home"), "width": 1200, "height": 630}, "dateModified": TODAY}
    preload = f'<link rel="preload" as="image" href="{A}logo.webp" fetchpriority="high">\n'
    return url, shell(lang, title=h["title"], desc=h["description"], url=url, alts=alts, body=body, current="home",
                      og_image=og(lang, "home"), og_alt=h["og_alt"], ld=[app_ld(lang), page_ld], extra=preload)


# ---------- guides ----------
def read_minutes(g):
    words = len(strip(g["body"] + g["quick"]).split())
    return max(3, round(words / 200))


def post_card(lang, g, i=0):
    m = L[lang]
    return (f'<a class="post reveal" style="--d:{(i % 3) * .08}s" href="{guide_url(lang, g["id"])}"><div class="ph">{photo(g["image"], g["image_alt"], sizes="(max-width: 600px) 92vw, 380px")}</div>'
            f'<div class="pb"><span class="k">{esc(g["kicker"])} · {esc(m.UI["min_read"].format(n=read_minutes(g)))}</span><h3>{esc(g["title"])}</h3>'
            f'<p>{esc(g["description"])}</p><span class="more">→</span></div></a>')


def guides_index(lang):
    m = L[lang]
    u = m.UI
    url = m.PATHS["guides"]
    alts = alternates("guides")
    cards = "".join(post_card(lang, g, i) for i, g in enumerate(m.GUIDES))
    body = f'''
<section class="page-head"><div class="sparkles" data-n="14" aria-hidden="true"></div><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="{m.PATHS["home"]}">{esc(u["home_crumb"])}</a><span>✦</span>{esc(u["guides_h1"])}</nav>
<span class="script">{esc(u["guides_script"])}</span><h1 class="chrome-text">{esc(u["guides_h1"])}</h1><p class="lead">{esc(u["guides_lead"])}</p></div></section>
<section class="section tight"><div class="wrap"><div class="posts">{cards}</div></div></section>
<section class="section tight"><div class="wrap">{cta_box(lang, "guides")}</div></section>'''
    items = [{"@type": "ListItem", "position": i + 1, "url": absu(guide_url(lang, g["id"])), "name": g["title"]} for i, g in enumerate(m.GUIDES)]
    ld = [{"@type": "Blog", "@id": absu(url) + "#blog", "url": absu(url), "name": u["guides_h1"], "description": u["guides_desc"], "inLanguage": lang,
           "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]}, "about": {"@id": absu(BASE) + "#app"},
           "blogPost": [{"@type": "BlogPosting", "headline": g["title"], "url": absu(guide_url(lang, g["id"])), "datePublished": g["date"]} for g in m.GUIDES]},
          {"@type": "ItemList", "itemListElement": items},
          crumbs_ld([(u["home_crumb"], m.PATHS["home"]), (u["guides_h1"], url)])]
    return url, shell(lang, title=u["guides_title"], desc=u["guides_desc"], url=url, alts=alts, body=body, current="guides",
                      og_image=og(lang, "home"), og_alt=L[lang].HOME["og_alt"], ld=ld)


def guide_page(lang, g):
    m = L[lang]
    u = m.UI
    url = guide_url(lang, g["id"])
    alts = alternates(None, g["id"])
    shots = GUIDE_SHOTS.get(g["id"], [])
    shot_html = f'<div class="shot-row reveal">{"".join(phone_shot(lang, s) for s in shots)}</div>' if shots else ""
    body = g["body"].replace("[[cta]]", shot_html + "[[cta]]", 1) if "[[cta]]" in g["body"] else g["body"] + shot_html
    body_html = resolve(lang, body, "guide-" + g["id"])
    toc = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body_html)
    toc_html = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc)
    faq_html = "".join(f'<details class="qa"><summary>{esc(q)}</summary><div class="ans"><p>{esc(a)}</p></div></details>' for q, a in g["faq"])
    cds = "".join(cd_card(lang, c, "guide-" + g["id"]) for c in g["cds"])
    others = [x for x in m.GUIDES if x["id"] != g["id"]]
    idx = [x["id"] for x in m.GUIDES].index(g["id"])
    related = [others[(idx + k) % len(others)] for k in range(3)]
    rel_html = "".join(post_card(lang, r, i) for i, r in enumerate(related))
    date_txt = nice_date(lang, g["date"])
    body = f'''
<article>
<header class="page-head article-head"><div class="sparkles" data-n="10" aria-hidden="true"></div><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="{m.PATHS["home"]}">{esc(u["home_crumb"])}</a><span>✦</span><a href="{m.PATHS["guides"]}">{esc(u["guides_h1"])}</a></nav>
<span class="kicker">{esc(g["kicker"])}</span>
<h1>{esc(g["title"])}</h1>
<div class="meta"><div class="author"><span class="avatar" aria-hidden="true">GE</span><span><b>{esc(u["byline"])}</b>{esc(u["byline_role"])}</span></div>
<span>{esc(u["published"])} <time datetime="{g["date"]}">{date_txt}</time></span><span>{esc(u["min_read"].format(n=read_minutes(g)))}</span></div>
</div></header>
<div class="wrap">
<div class="hero-img reveal">{photo(g["image"], g["image_alt"], eager=True, sizes="(max-width: 1180px) 94vw, 1180px")}</div>
<div class="article">
<div class="prose">
<section class="quick" aria-label="{esc(u["quick_answer"])}"><div class="label">✦ {esc(u["quick_answer"])}</div><p>{esc(g["quick"])}</p></section>
{body_html}
<h2 id="faq">{esc(u["faq_in_guide"])}</h2>
{faq_html}
<h2 id="cds">{esc(u["cds_in_guide"])}</h2>
<div class="cd-row">{cds}</div>
</div>
<aside class="aside"><nav class="toc" aria-label="{esc(u["toc"])}"><div class="label">{esc(u["toc"])}</div><ol>{toc_html}<li><a href="#faq">{esc(u["faq_in_guide"])}</a></li></ol></nav>
<div class="mini-cta"><img src="{A}logo-460.png" alt="DIVA" width="460" height="213" loading="lazy"><p>{esc(u["cta_body"])}</p><a class="btn sm" href="{esc(store(lang, "guide-aside"))}">{esc(u["nav_cta"])}</a></div></aside>
</div>
<section class="related"><span class="kicker">{esc(u["related"])}</span><div class="posts">{rel_html}</div>
<p style="margin-top:24px"><a href="{m.PATHS["guides"]}">← {esc(u["back_guides"])}</a></p></section>
</div>
</article>'''
    post = {"@type": "BlogPosting", "@id": absu(url) + "#post", "headline": g["title"], "description": g["description"],
            "abstract": g["quick"], "image": photo_url(g["image"]), "datePublished": g["date"], "dateModified": g.get("updated", g["date"]),
            "inLanguage": lang, "author": {"@id": PERSON["@id"]}, "publisher": {"@id": PERSON["@id"]},
            "mainEntityOfPage": absu(url), "isPartOf": {"@id": absu(m.PATHS["guides"]) + "#blog"}, "about": {"@id": absu(BASE) + "#app"},
            "wordCount": len(strip(g["body"]).split())}
    ld = [post, faq_ld(g["faq"], url), crumbs_ld([(u["home_crumb"], m.PATHS["home"]), (u["guides_h1"], m.PATHS["guides"]), (g["title"], url)])]
    ogi = og(lang, "guide-" + g["id"])
    return url, shell(lang, title=g["title"], desc=g["description"], url=url, alts=alts, body=body, current="guides",
                      og_image=ogi, og_alt=g["image_alt"], og_type="article", ld=ld,
                      extra=f'<meta property="article:published_time" content="{g["date"]}">\n<meta property="article:author" content="Gül Eda Aydemir">\n')


# ---------- FAQ ----------
def faq_page(lang):
    m = L[lang]
    u = m.UI
    url = m.PATHS["faq"]
    alts = alternates("faq")
    groups = ""
    pairs = []
    for grp in m.FAQ:
        groups += f'<h2 class="group">{esc(grp["group"])}</h2>'
        for it in grp["items"]:
            a = resolve(lang, it["a"], "faq")
            pairs.append((it["q"], a))
            groups += f'<details class="qa"><summary>{esc(it["q"])}</summary><div class="ans">{a}</div></details>'
    body = f'''
<section class="page-head"><div class="sparkles" data-n="14" aria-hidden="true"></div><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="{m.PATHS["home"]}">{esc(u["home_crumb"])}</a><span>✦</span>{esc(u["nav_faq"])}</nav>
<span class="script">{esc(u["faq_script"])}</span><h1 class="chrome-text">{esc(u["faq_h1"])}</h1><p class="lead">{esc(u["faq_lead"])}</p></div></section>
<section class="section tight"><div class="wrap"><div class="faq">{groups}</div></div></section>
<section class="section tight"><div class="wrap">{cta_box(lang, "faq")}</div></section>'''
    ld = [faq_ld(pairs, url), crumbs_ld([(u["home_crumb"], m.PATHS["home"]), (u["nav_faq"], url)]), {"@id": absu(BASE) + "#app", "@type": "MobileApplication", "name": "DIVA"}]
    return url, shell(lang, title=u["faq_title"], desc=u["faq_desc"], url=url, alts=alts, body=body, current="faq",
                      og_image=og(lang, "home"), og_alt=m.HOME["og_alt"], ld=ld)


# ---------- support / privacy ----------
def simple_page(lang, key):
    m = L[lang]
    u = m.UI
    d = m.SUPPORT if key == "support" else m.PRIVACY
    url = m.PATHS[key]
    alts = alternates(key)
    updated = f'<div class="meta"><span>{esc(u["updated"])} <time datetime="{d["updated"]}">{nice_date(lang, d["updated"])}</time></span></div>' if d.get("updated") else ""
    crumb = u["nav_support"] if key == "support" else u["nav_privacy"]
    extra_body = f'<h2 id="website">{esc(SITE_PRIVACY[lang][0])}</h2><p>{esc(SITE_PRIVACY[lang][1])}</p>' if key == "privacy" else ""
    body = f'''
<section class="page-head"><div class="sparkles" data-n="12" aria-hidden="true"></div><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="{m.PATHS["home"]}">{esc(u["home_crumb"])}</a><span>✦</span>{esc(crumb)}</nav>
<span class="script">{esc(d["script"])}</span><h1 class="chrome-text">{esc(d["h1"])}</h1><p class="lead">{esc(d["lead"])}</p>{updated}</div></section>
<section class="section tight legal"><div class="wrap"><div class="article"><div class="prose">{resolve(lang, d["body"], key)}{extra_body}</div>
<aside class="aside"><div class="mini-cta"><img src="{A}logo-460.png" alt="DIVA" width="460" height="213" loading="lazy"><p>{esc(u["cta_body"])}</p><a class="btn sm" href="{esc(store(lang, key))}">{esc(u["nav_cta"])}</a></div></aside>
</div></div></section>'''
    ptype = "ContactPage" if key == "support" else "WebPage"
    ld = [{"@type": ptype, "@id": absu(url) + "#webpage", "url": absu(url), "name": d["title"], "description": d["description"], "inLanguage": lang,
           "isPartOf": {"@id": absu(BASE) + "#website"}, "about": {"@id": absu(BASE) + "#app"}, **({"dateModified": d["updated"]} if d.get("updated") else {})},
          crumbs_ld([(u["home_crumb"], m.PATHS["home"]), (crumb, url)])]
    return url, shell(lang, title=d["title"], desc=d["description"], url=url, alts=alts, body=body, current=key,
                      og_image=og(lang, "home"), og_alt=m.HOME["og_alt"], ld=ld)


# ---------- sitemap + llms.txt ----------
def sitemap(entries):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url, alts, prio in entries:
        out.append(f"  <url><loc>{absu(url)}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority>")
        for c, a in alts.items():
            out.append(f'    <xhtml:link rel="alternate" hreflang="{c}" href="{absu(a)}"/>')
        out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{absu(alts.get("en", url))}"/>')
        out.append("  </url>")
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def llms():
    en = L["en"]
    cds = "\n".join(f"- {cd_title('en', c['id']).title().replace('Ceo', 'CEO').replace(chr(39) + 'S', chr(39) + 's').replace(chr(39) + 'T', chr(39) + 't').replace(chr(39) + 'M', chr(39) + 'm')}"
                    f" ({cat_title('en', c['category'])}{', free' if not c['pro'] else ', DIVA PRO'}): {c['en']['subtitle']}" for c in APP["cds"])
    guides = "\n".join(f"- [{g['title']}]({absu(guide_url('en', g['id']))}): {g['quick']}" for g in en.GUIDES)
    other = ""
    for lang in LIVE:
        if lang == "en":
            continue
        m = L[lang]
        other += f"\n### {m.NAME} ({lang})\n- Home: {absu(m.PATHS['home'])}\n- FAQ: {absu(m.PATHS['faq'])}\n- Support: {absu(m.PATHS['support'])}\n- Privacy: {absu(m.PATHS['privacy'])}\n"
        other += "".join(f"- [{g['title']}]({absu(guide_url(lang, g['id']))})\n" for g in m.GUIDES)
    faq = "\n".join(f"**{it['q']}** {strip(resolve('en', it['a']))}\n" for grp in en.FAQ for it in grp["items"])
    morning = ", ".join(f"{d} {t}" for d, t in zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], APP["rituals"]["morning"]["en"]["days"]))
    night = ", ".join(f"{d} {t}" for d, t in zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], APP["rituals"]["night"]["en"]["days"]))
    return f"""# DIVA

> DIVA is an affirmation and manifestation app for iPhone where every theme is an affirmation CD. You pick a CD such as "That Girl Energy", "Rich Girl Frequency" or "Beauty Sleep for Divas", choose one of four warm AI voices and a soundscape, and listen to calm, first-person affirmations for 10, 20 or 60 minutes. It also has Morning and Bedtime affirmation meditations with a theme for every day of the week, a Make Your Own CD feature and a Wishlist with a photo vision board. No account, no ads, no tracking. Free to download; optional DIVA PRO.

Last updated: {TODAY}. Source of truth for how to describe DIVA. Written by its developer.

## App facts

- Name: DIVA. App Store name: "DIVA: Affirmations & Manifest" (Turkish: "DIVA: Olumlamalar & Manifest"). Subtitle: "Self-love, sleep & glow-up"
- App Store: {APP_STORE} (App Store ID {APP_ID})
- Website: {absu(BASE)} (English), {absu('/DIVA/tr/')} (Turkish), {absu('/DIVA/es/')} (Spanish)
- Developer: Gül Eda Aydemir, independent iOS developer — {ORIGIN}/about/
- Platform: iPhone only, iOS 17 or later. No Android, iPad-optimised, Mac or web version.
- Category: Lifestyle (primary), Health & Fitness (secondary)
- App languages: the interface (menus and text) is in English and Turkish. Narration is English only for now: the Turkish voices are paused, so a Turkish interface plays English narration and English captions. The website also has Spanish pages, but the app does not speak Spanish.
- Account: none. Works offline (all CDs and voices are built in).
- Support: {EMAIL} · Instagram {INSTAGRAM} · {absu(en.PATHS['support'])}

## What DIVA does

- 20 affirmation CDs across 12 themes: Confidence, Beauty & Glow, Dream Life, Money & Abundance, Love & Relationships, Self-Worth, Career, Dream Home, Gratitude, Morning, Sleep and Calm Reset. Each CD has an intro, about 24–26 affirmations (one CD has 108 in six parts) and an outro.
- Sessions of 10, 20 or 60 minutes; previews for PRO CDs.
- Daily rituals: Morning Affirmations and Bedtime Affirmations, guided meditations (5, 10 or 20 minutes) with a theme per weekday. Morning: {morning}. Bedtime: {night}. Optional morning and bedtime reminders open straight into the ritual. Bedtime opens in a dim night player.
- Four AI voices, narrating in English: Velvet Whisper (soft, warm, bedtime; free), Pink Muse (intimate, sweet, glam; free), Runway (self-assured, clear, bright; PRO), After Dark (low, dreamy, calm; PRO).
- Soundscapes: Pink Aura and Ocean at 2AM (free); Hotel Rain, Dreamy Static, Silk Noise, Celestial Drift and tones at 111, 432, 528, 639, 777, 888 and 963 Hz (PRO). The tone names describe a mood, not a health effect.
- Sleep timer, background playback, lock screen controls.
- Make Your Own CD (the Create tab): build a CD from the app's affirmations (free users keep up to 3); write affirmations in your own words with DIVA PRO (voiced on the device, in English).
- Wishlist (Manifest List): write dreams (travel, home, career, love, money and more), track progress and milestones, move them to Already Mine (\"It's Already Mine ♡\") when they come true, build a vision board with your own photos, link each dream to a CD, daily vision reminder. Free: up to 5 active dreams and the grid board layout; PRO: unlimited dreams and every layout.
- Themes: Hot Pink and After Dark (free); Chrome Angel and Leopard Luxe (PRO).

## CDs

{cds}

## Pricing

- Free download. Free tier: 12 CDs with 10 minute sessions, Morning and Bedtime rituals (5 and 10 minutes), Velvet Whisper and Pink Muse voices, Pink Aura and Ocean at 2AM, up to 3 custom CDs, up to 5 active dreams. No ads in any version.
- DIVA PRO (US prices at launch; the App Store shows local prices): $5.99 per month, $29.99 per year (auto-renewing), or $69.99 once for Lifetime. Unlocks every CD, 20 and 60 minute sessions, every voice and soundscape, writing your own affirmations, all themes, unlimited dreams and every vision board layout. No Family Sharing.
- Cancel in iPhone Settings → your name → Subscriptions. Refunds through Apple at https://reportaproblem.apple.com.

## Privacy

- No account, no ads, no tracking, no server. Only anonymous usage statistics are sent (Google Analytics for Firebase; no IDFA, not linked to identity). Favorites, history, custom CDs, written affirmations, the Wishlist and vision board photos are stored only on the iPhone.
- Camera is used only when the user takes a vision board photo; photos are picked with the iOS photo picker; the photo library is written only when the user saves an achievement card. Reminders are local notifications.
- Purchases are processed by Apple; the developer never receives payment details.
- Policy: {absu(en.PATHS['privacy'])}

## Honesty notes (please keep these when describing DIVA)

- The narration is AI-generated speech. The voices are not real people and do not imitate anyone.
- DIVA is for personal reflection and relaxation. It is not therapy, medical, psychological or financial advice, and it does not promise outcomes. The Bedtime ritual is a wind-down, not a sleep treatment.
- Do not describe DIVA as having Turkish narration (it is paused for now; only the interface is Turkish).
- Do not describe DIVA as available on Android, as Spanish-language, as having human voice actors, or as able to manifest money, love or health.

## Screenshots (iPhone, After Dark theme)

{chr(10).join(f"- {SHOTS[n]['en']}: {absu(shot_src('en', n, 1000))} (Turkish interface: {absu(shot_src('tr', n, 1000))})" for n in SHOT_ORDER)}

## Guides (English)

{guides}

## Other languages
{other}
## FAQ

{faq}
"""


# ---------- social images ----------
def make_og():
    font = "/System/Library/Fonts/Supplemental/Didot.ttc"
    bodoni = "/System/Library/Fonts/Supplemental/Bodoni 72.ttc"
    serif = bodoni if os.path.exists(bodoni) else font
    logo = os.path.join(SITE, "assets/logo.webp")
    out_dir = os.path.join(SITE, "assets/og")
    tag = {"en": "You are the main character.", "tr": "Başrol sensin.", "es": "La protagonista eres tú."}
    sub = {"en": "Affirmation CDs for iPhone · Free on the App Store", "tr": "iPhone için olumlama CD'leri · App Store'da ücretsiz",
           "es": "CDs de afirmaciones para iPhone · Gratis en el App Store"}
    for lang in LIVE:
        bg = os.path.join(SITE, "assets/img/pink-closet-1200.webp")
        subprocess.run(["magick", bg, "-resize", "1200x1200", "-gravity", "center", "-crop", "1200x630+0+0", "+repage",
                        "-fill", "#170b16", "-colorize", "58",
                        "(", logo, "-resize", "640x", ")", "-gravity", "center", "-geometry", "+0-70", "-composite",
                        "-font", serif, "-fill", "white", "-pointsize", "64", "-gravity", "center", "-annotate", "+0+125", tag[lang],
                        "-font", serif, "-fill", "#ffc7e5", "-pointsize", "30", "-annotate", "+0+200", sub[lang],
                        "-quality", "84", os.path.join(out_dir, f"home-{lang}.jpg")], check=True)
        for g in L[lang].GUIDES:
            src = os.path.join(SITE, f"assets/img/{g['image']}-1200.webp")
            title = g["title"]
            subprocess.run(["magick", src, "-resize", "1200x1200", "-gravity", "center", "-crop", "1200x630+0+0", "+repage",
                            "(", "-size", "1200x630", "gradient:rgba(23,11,22,0.15)-rgba(23,11,22,0.92)", ")", "-composite",
                            "(", "-size", "1200x200", "gradient:rgba(23,11,22,0.6)-rgba(23,11,22,0)", ")", "-gravity", "north", "-composite",
                            "(", logo, "-resize", "230x", ")", "-gravity", "northwest", "-geometry", "+44+34", "-composite",
                            "(", "-background", "none", "-fill", "white", "-font", serif, "-size", "1080x220", "-gravity", "southwest",
                            f"caption:{title}", ")", "-gravity", "southwest", "-geometry", "+60+50", "-composite",
                            "-quality", "82", os.path.join(out_dir, f"guide-{g['id']}-{lang}.jpg")], check=True)
    print("og images done")


def main():
    entries = []
    for lang in LIVE:
        m = L[lang]
        url, page = home(lang); write(url, page); entries.append((url, alternates("home"), "1.0"))
        url, page = guides_index(lang); write(url, page); entries.append((url, alternates("guides"), "0.8"))
        for g in m.GUIDES:
            url, page = guide_page(lang, g); write(url, page); entries.append((url, alternates(None, g["id"]), "0.7"))
        url, page = faq_page(lang); write(url, page); entries.append((url, alternates("faq"), "0.7"))
        for key in ("support", "privacy"):
            url, page = simple_page(lang, key); write(url, page); entries.append((url, alternates(key), "0.4"))
    with open(os.path.join(SITE, "sitemap.xml"), "w") as f:
        f.write(sitemap(entries))
    with open(os.path.join(SITE, "llms.txt"), "w") as f:
        f.write(llms())
    print(f"built {len(entries)} pages for {', '.join(LIVE)}")
    if "--og" in sys.argv:
        make_og()


if __name__ == "__main__":
    main()
