#!/usr/bin/env python3
"""Builds the SHOOTS site from the page sources in tools/pages/.

Each source is an HTML fragment that starts with a JSON front-matter comment:

    <!--meta
    { "lang": "en", "path": "guides/my-guide/", "type": "article", "title": "...", ... }
    -->
    <p>Body HTML…</p>

`python3 SHOOTS/tools/build.py` writes every page to SHOOTS/<path>index.html, renders the
OG images (needs Pillow and macOS's SF fonts) and rewrites SHOOTS/sitemap.xml.
Shortcodes in bodies: {{shot:name|caption}}, {{pair:a,b|caption}}, {{watch:name|caption}},
{{store:01-hero|caption}}, {{appcard:dump|soloswipe|shoots}}, {{cta}}, {{faq}}, {{posts:guides|journal|all}}.
"""
import glob, html, json, math, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # …/SHOOTS
SRC = os.path.join(ROOT, "tools", "pages")
BASE = "/SHOOTS/"
SITE = "https://guledaaydemir.github.io"
APP_ID = "6825732746"
EMAIL = "solostaseraofficial@gmail.com"
TODAY = "2026-10-22"
STAR = "M69.92 51.74 L106.62 77.62 L60.72 59.00 L82.33 94.50 L51.95 63.86 L29.29 94.41 L41.82 58.78 L1.44 75.82 L32.07 51.57 L-0.41 30.65 L39.12 41.19 L25.09 10.14 L50.17 40.00 L79.49 10.87 L60.65 42.54 L107.68 33.46Z"
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.36 12.9c.02-2.2 1.8-3.26 1.88-3.31-1.03-1.5-2.62-1.71-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 2.18-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.74 2.21 1.1-.04 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.08 2.65-2.14.84-1.23 1.18-2.42 1.2-2.48-.03-.01-2.3-.88-2.32-3.5zM14.2 6.3c.6-.74 1.01-1.76.9-2.78-.87.04-1.93.58-2.56 1.31-.56.65-1.05 1.69-.92 2.68.97.08 1.96-.49 2.58-1.21z"/></svg>'

LAZY = ' loading="lazy"'
CUR_PAGE = ' aria-current="page"'
CUR_TRUE = ' aria-current="true"'

def star_svg(cls="st"):
    return f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true"><path d="{STAR}"/></svg>'

def store_url(lang):
    return f"https://apps.apple.com/{'' if lang == 'en' else lang + '/'}app/id{APP_ID}"

# ---------------------------------------------------------------- chrome strings
T = {
 "en": {
  "locale": "en_US", "home": "", "features": "features/", "guides": "guides/", "support": "support/", "about": "about/",
  "privacy": "privacy/", "terms": "terms/", "journal": "journal/",
  "nav": ["Home", "Features", "Guides", "FAQ & Support", "About"], "download": "Download",
  "menu": "Menu", "skip": "Skip to content", "dl_small": "Download on the", "dl_aria": "Download SHOOTS on the App Store",
  "qr_cap": "<b>On a computer?</b>Scan with your iPhone camera", "qr_alt": "QR code that opens SHOOTS on the App Store",
  "foot_about": "SHOOTS is a hands-free self timer camera for iPhone and Apple Watch, made by independent developer Gül Eda Aydemir. No account, no ads, no tracking.",
  "foot_app": "The app", "foot_legal": "Legal & help", "foot_more": "The photo trio", "foot_else": "Elsewhere",
  "f_features": "Features", "f_guides": "Guides", "f_journal": "Journal", "f_support": "FAQ & Support", "f_about": "About",
  "f_privacy": "Privacy policy", "f_terms": "Terms of use", "f_contact": "Email support", "f_all": "All apps by Gül Eda",
  "f_dump": "Turn shoots into photo dumps", "f_swipe": "Swipe away the rest", "f_store": "App Store", "f_insta": "Instagram @solo.stasera",
  "f_bottom": "© 2026 Gül Eda Aydemir. App Store and Apple Watch are trademarks of Apple Inc. Facts on this site checked against the app on 22 October 2026.",
  "crumb_home": "SHOOTS", "guides_t": "Guides", "journal_t": "Journal", "by": "By", "min": "min read", "updated": "Updated",
  "desk": "the SHOOTS Journal", "edited": "edited by Gül Eda Aydemir",
  "author_box": "<b>Gül Eda Aydemir</b> is the independent iOS developer behind SHOOTS, DUMP and Solo.Swipe. She designs, builds and answers support for every app herself. Say hi at <a href=\"mailto:{e}\">{e}</a>.",
  "sig_small": "Founder, SHOOTS",
  "cta_t": "Your solo photographer", "cta_p": "Prop up your iPhone, step into frame and let SHOOTS run the whole photoshoot.",
  "more_t": "Keep reading", "read": "Read",
  "app_go": "See the app", "app_dump": "Turn a shoot into a share-ready photo dump, carousel or collage in under a minute.",
  "app_swipe": "Swipe through your camera roll to delete what you don't need and sort the rest into albums.",
  "app_shoots": "The hands-free self timer camera: prop it up, step in, pose. SHOOTS fires the whole photoshoot.",
  "lang_name": "English", "date_fmt": lambda d: date.fromisoformat(d).strftime("%-d %B %Y"),
 },
 "tr": {
  "locale": "tr_TR", "home": "tr/", "features": "tr/ozellikler/", "guides": "tr/rehber/", "support": "tr/destek/", "about": "tr/hakkinda/",
  "privacy": "tr/gizlilik/", "terms": "terms/", "journal": "tr/rehber/",
  "nav": ["Ana sayfa", "Özellikler", "Rehberler", "SSS & Destek", "Hakkında"], "download": "İndir",
  "menu": "Menü", "skip": "İçeriğe geç", "dl_small": "Hemen indir:", "dl_aria": "SHOOTS'u App Store'dan indir",
  "qr_cap": "<b>Bilgisayarda mısın?</b>iPhone kameranla tara", "qr_alt": "SHOOTS'u App Store'da açan QR kod",
  "foot_about": "SHOOTS, iPhone ve Apple Watch için eller serbest bir zamanlayıcılı kamera. Bağımsız geliştirici Gül Eda Aydemir tarafından yapıldı. Hesap yok, reklam yok, takip yok.",
  "foot_app": "Uygulama", "foot_legal": "Yasal & yardım", "foot_more": "Fotoğraf üçlüsü", "foot_else": "Diğer",
  "f_features": "Özellikler", "f_guides": "Rehberler", "f_journal": "Rehberler", "f_support": "SSS & Destek", "f_about": "Hakkında",
  "f_privacy": "Gizlilik politikası", "f_terms": "Kullanım koşulları (EN)", "f_contact": "E-posta desteği", "f_all": "Gül Eda'nın tüm uygulamaları",
  "f_dump": "Çekimlerini photo dump'a çevir", "f_swipe": "Gerisini kaydırarak sil", "f_store": "App Store", "f_insta": "Instagram @solo.stasera",
  "f_bottom": "© 2026 Gül Eda Aydemir. App Store ve Apple Watch, Apple Inc.'in ticari markalarıdır. Bu sitedeki bilgiler 22 Ekim 2026'da uygulamayla karşılaştırıldı.",
  "crumb_home": "SHOOTS", "guides_t": "Rehberler", "journal_t": "Rehberler", "by": "Yazan:", "min": "dk okuma", "updated": "Güncellendi",
  "desk": "SHOOTS Journal", "edited": "editör: Gül Eda Aydemir",
  "author_box": "<b>Gül Eda Aydemir</b>, SHOOTS, DUMP ve Solo.Swipe'ın arkasındaki bağımsız iOS geliştiricisi. Her uygulamayı kendisi tasarlıyor, geliştiriyor ve destek e-postalarını kendisi yanıtlıyor: <a href=\"mailto:{e}\">{e}</a>",
  "sig_small": "SHOOTS kurucusu",
  "cta_t": "Kendi fotoğrafçın", "cta_p": "iPhone'unu bir yere yasla, kadraja gir, poz ver. Çekimin tamamını SHOOTS yapsın.",
  "more_t": "Okumaya devam et", "read": "Oku",
  "app_go": "İncele", "app_dump": "Çekimlerinden bir dakikadan kısa sürede paylaşmaya hazır photo dump, kaydırmalı post ya da kolaj yap.",
  "app_swipe": "Galerini kaydırarak gez: gereksizleri sil, kalanları albümlere ayır.",
  "app_shoots": "Eller serbest zamanlayıcılı kamera: telefonu yasla, kadraja gir, poz ver. Çekimi SHOOTS yapar.",
  "lang_name": "Türkçe", "date_fmt": lambda d: "{} {} {}".format(int(d[8:]), ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"][int(d[5:7]) - 1], d[:4]),
 },
 "es": {
  "locale": "es_ES", "home": "es/", "features": "es/funciones/", "guides": "es/guias/", "support": "es/soporte/", "about": "es/acerca/",
  "privacy": "es/privacidad/", "terms": "terms/", "journal": "es/guias/",
  "nav": ["Inicio", "Funciones", "Guías", "FAQ y soporte", "Acerca de"], "download": "Descargar",
  "menu": "Menú", "skip": "Saltar al contenido", "dl_small": "Descárgalo en el", "dl_aria": "Descarga SHOOTS en el App Store",
  "qr_cap": "<b>¿No estás en tu iPhone?</b>Escanéalo con la cámara del iPhone", "qr_alt": "Código QR que abre SHOOTS en el App Store",
  "foot_about": "SHOOTS es una cámara con temporizador manos libres para iPhone y Apple Watch, creada por la desarrolladora independiente Gül Eda Aydemir. Sin cuenta, sin anuncios, sin rastreo.",
  "foot_app": "La app", "foot_legal": "Legal y ayuda", "foot_more": "El trío de fotos", "foot_else": "En otros sitios",
  "f_features": "Funciones", "f_guides": "Guías", "f_journal": "Guías", "f_support": "FAQ y soporte", "f_about": "Acerca de",
  "f_privacy": "Política de privacidad", "f_terms": "Términos de uso (EN)", "f_contact": "Soporte por email", "f_all": "Todas las apps de Gül Eda",
  "f_dump": "Convierte sesiones en photo dumps", "f_swipe": "Desliza y borra el resto", "f_store": "App Store", "f_insta": "Instagram @solo.stasera",
  "f_bottom": "© 2026 Gül Eda Aydemir. App Store y Apple Watch son marcas de Apple Inc. Datos comprobados con la app el 22 de octubre de 2026.",
  "crumb_home": "SHOOTS", "guides_t": "Guías", "journal_t": "Guías", "by": "Por", "min": "min de lectura", "updated": "Actualizado",
  "desk": "el SHOOTS Journal", "edited": "editado por Gül Eda Aydemir",
  "author_box": "<b>Gül Eda Aydemir</b> es la desarrolladora independiente de iOS detrás de SHOOTS, DUMP y Solo.Swipe. Diseña y programa cada app, y responde ella misma los mensajes de soporte. Escríbele a <a href=\"mailto:{e}\">{e}</a>.",
  "sig_small": "Fundadora de SHOOTS",
  "cta_t": "Tu fotógrafo personal", "cta_p": "Apoya el iPhone, entra en el encuadre y posa. SHOOTS hace la sesión entera por ti.",
  "more_t": "Sigue leyendo", "read": "Leer",
  "app_go": "Ver app", "app_dump": "Convierte una sesión en un photo dump, carrusel o collage listo para publicar en menos de un minuto.",
  "app_swipe": "Desliza por tu carrete para borrar lo que no necesitas y ordenar el resto en álbumes.",
  "app_shoots": "La cámara con temporizador manos libres: apóyala, entra en el encuadre y posa. SHOOTS dispara la sesión entera.",
  "lang_name": "Español", "date_fmt": lambda d: "{} de {} de {}".format(int(d[8:]), ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"][int(d[5:7]) - 1], d[:4]),
 },
}
OTHER_APPS = {
 "dump": {"name": "DUMP", "url": "/DUMP/", "icon": "/DUMP/appicon-128.webp", "store": "https://apps.apple.com/app/id6798248086"},
 "soloswipe": {"name": "Solo.Swipe", "url": "/solo.swipe/", "icon": "/solo.swipe/appicon-128.webp", "store": "https://apps.apple.com/app/id6761368690"},
 "shoots": {"name": "SHOOTS", "url": BASE, "icon": BASE + "appicon-128.webp", "store": None},
}

def url(lang, key):
    return BASE + T[lang][key]

# ---------------------------------------------------------------- sources
def load_pages():
    pages = []
    for f in sorted(glob.glob(os.path.join(SRC, "**", "*.html"), recursive=True)):
        raw = open(f, encoding="utf-8").read()
        m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->\s*", raw, re.S)
        if not m:
            sys.exit(f"missing front matter: {f}")
        try:
            meta = json.loads(m.group(1))
        except json.JSONDecodeError as e:
            sys.exit(f"bad JSON in {f}: {e}")
        meta["body"] = raw[m.end():]
        meta["src"] = f
        meta.setdefault("type", "page")
        meta.setdefault("date", TODAY)
        meta.setdefault("updated", meta["date"])
        meta.setdefault("h1", meta.get("title"))
        meta.setdefault("og_title", meta.get("h1"))
        meta["url"] = BASE + meta["path"]
        pages.append(meta)
    return pages

# ---------------------------------------------------------------- snippets
def appstore(lang, ct="", cls=""):
    t = T[lang]
    return (f'<a class="appstore {cls}" href="{store_url(lang)}" aria-label="{t["dl_aria"]}" data-ct="{ct}">{APPLE}'
            f'<span class="t"><small>{t["dl_small"]}</small><b>App Store</b></span></a>')

def qr(lang, cls="desk"):
    t = T[lang]
    return (f'<div class="qr {cls}"><div class="code"><img src="{BASE}assets/img/qr/appstore-qr-{lang}.svg" width="78" height="78" alt="{t["qr_alt"]}" loading="lazy"></div>'
            f'<p class="cap">{t["qr_cap"]}</p></div>')

def device(name, alt, cls="", lazy=True, w=600):
    return (f'<div class="device {cls}"><img src="{BASE}assets/img/shots/{name}-600.webp" srcset="{BASE}assets/img/shots/{name}-600.webp 600w, {BASE}assets/img/shots/{name}-1206.webp 1206w" '
            f'sizes="(max-width: 640px) 72vw, 300px" width="600" height="1305" alt="{html.escape(alt, quote=True)}"{LAZY if lazy else ""} decoding="async"></div>')

def ipad(name, alt):
    return (f'<div class="tablet"><img src="{BASE}assets/img/ipad/{name}-700.webp" srcset="{BASE}assets/img/ipad/{name}-700.webp 700w, {BASE}assets/img/ipad/{name}-1400.webp 1400w" '
            f'sizes="(max-width: 640px) 88vw, 460px" width="700" height="933" alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async"></div>')

def watch(name, alt):
    return f'<div class="watch"><img src="{BASE}assets/img/watch/{name}-416.webp" width="416" height="496" alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async"></div>'

def store_img(name, alt):
    return (f'<img src="{BASE}assets/img/store/{name}-600.webp" srcset="{BASE}assets/img/store/{name}-600.webp 600w, {BASE}assets/img/store/{name}-1206.webp 1206w" '
            f'sizes="(max-width: 640px) 70vw, 300px" width="600" height="1304" alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async">')

def appcard(lang, key):
    a, t = OTHER_APPS[key], T[lang]
    desc = {"dump": t["app_dump"], "soloswipe": t["app_swipe"], "shoots": t["app_shoots"]}[key]
    href = a["url"] if key != "shoots" else url(lang, "home")
    tr_suffix = "tr/" if lang == "tr" and key != "shoots" else ""
    return (f'<a class="appcard" href="{href}{tr_suffix}"><img src="{a["icon"]}" width="64" height="64" alt="" loading="lazy">'
            f'<div><b>{a["name"]}</b><span>{desc}</span></div><span class="go">{t["app_go"]} ↗</span></a>')

def cta(lang):
    t = T[lang]
    return (f'<div class="dl-box"><div><b class="t">{t["cta_t"]}</b><p>{t["cta_p"]}</p>{appstore(lang, "article")}</div>{qr(lang, "")}</div>')

def faq_html(items):
    out = ['<div class="faq">']
    for it in items:
        if "group" in it:
            out.append(f'<h3 class="grp">{it["group"]}</h3>')
            continue
        out.append(f'<details><summary>{it["q"]}</summary><div class="a">{it["a"]}</div></details>')
    out.append('</div>')
    return "\n".join(out)

def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()

def post_card(p, feature=False):
    lang = p["lang"]
    t = T[lang]
    by = "Gül Eda, xoxo" if p.get("author") == "gul" else ("SHOOTS Journal" if p.get("section") == "journal" else "Gül Eda Aydemir")
    slug = og_slug(p)
    return (f'<a class="post{" feature" if feature else ""} rv" href="{p["url"]}"><div class="ph"><img src="{BASE}assets/img/og/{slug}-600.webp" width="600" height="315" alt="" loading="lazy" decoding="async"></div>'
            f'<div class="tx"><span class="k">{p.get("kicker", "")}</span><h3>{p["h1"]}</h3><p>{p.get("dek", p["description"])}</p>'
            f'<span class="by">{by} · {p.get("mins", 5)} {t["min"]}</span></div></a>')

def render_posts(lang, which, pages, exclude=None, limit=None):
    items = [p for p in pages if p["lang"] == lang and p["type"] == "article" and p is not exclude and (which == "all" or p.get("section") == which)]
    items.sort(key=lambda p: (p.get("order", 50), p["h1"]))
    if limit:
        items = items[:limit]
    return '<div class="posts">' + "".join(post_card(p) for p in items) + '</div>'

def shortcodes(body, lang, page, pages):
    def rep(m):
        kind, arg = m.group(1), (m.group(2) or "")
        if kind == "shot":
            name, _, cap = arg.partition("|")
            return f'<figure class="shot">{device(name.strip(), cap or name)}<figcaption>{cap}</figcaption></figure>'
        if kind == "pair":
            names, _, cap = arg.partition("|")
            a, b = [n.strip() for n in names.split(",")]
            return f'<figure class="pair">{device(a, cap)}{device(b, cap)}<figcaption>{cap}</figcaption></figure>'
        if kind == "ipad":
            name, _, cap = arg.partition("|")
            return f'<figure class="shot">{ipad(name.strip(), cap)}<figcaption>{cap}</figcaption></figure>'
        if kind == "watch":
            name, _, cap = arg.partition("|")
            return f'<figure class="shot">{watch(name.strip(), cap)}<figcaption>{cap}</figcaption></figure>'
        if kind == "store":
            name, _, cap = arg.partition("|")
            return f'<figure class="shot"><div class="device sm">{store_img(name.strip(), cap)}</div><figcaption>{cap}</figcaption></figure>'
        if kind == "storeimg":
            name, _, cap = arg.partition("|")
            return store_img(name.strip(), cap)
        if kind == "appcard":
            return appcard(lang, arg.strip())
        if kind == "cta":
            return cta(lang)
        if kind == "appstore":
            return appstore(lang, arg.strip())
        if kind == "qr":
            return qr(lang, arg.strip() or "desk")
        if kind == "faq":
            return faq_html(page.get("faq", []))
        if kind == "posts":
            which, _, lim = arg.partition("|")
            return render_posts(lang, which.strip(), pages, limit=int(lim) if lim else None)
        if kind == "star":
            return star_svg(arg.strip() or "st")
        if kind == "url":
            return url(lang, arg.strip())
        if kind == "store_url":
            return store_url(lang)
        return m.group(0)
    return re.sub(r"\{\{(\w+)(?::([^}]*))?\}\}", rep, body)

# ---------------------------------------------------------------- head / chrome
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:ital,wght@0,500;0,600;0,700;1,600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">')

def alternates(page, by_path):
    alts = {page["lang"]: page["path"]}
    for l, p in (page.get("alt") or {}).items():
        alts[l] = p
    return alts

def asset_v(name):
    import hashlib
    return hashlib.md5(open(os.path.join(ROOT, "assets", name), "rb").read()).hexdigest()[:8]

def person():
    return {"@type": "Person", "@id": SITE + "/#person", "name": "Gül Eda Aydemir", "alternateName": "Gul Eda Aydemir",
            "jobTitle": "Independent iOS developer", "url": SITE + "/about/", "email": EMAIL,
            "sameAs": ["https://apps.apple.com/us/developer/gul-eda-aydemir/id1889159460", "https://instagram.com/solo.stasera"]}

def app_schema():
    return {
     "@type": "MobileApplication", "@id": SITE + BASE + "#app", "name": "SHOOTS: Self Timer Camera",
     "alternateName": ["SHOOTS", "SHOOTS self timer camera", "SHOOTS interval camera"],
     "description": "Hands-free self timer and interval camera for iPhone with an Apple Watch remote. Set a start delay, an interval (from 0.5 seconds to 1 hour, or burst) and how many photos, then pose while SHOOTS takes the whole photoshoot. No account, no ads, no tracking; photos stay on the device.",
     "url": SITE + BASE, "applicationCategory": "PhotographyApplication", "applicationSubCategory": "Photo & Video",
     "operatingSystem": "iOS 18.6 or later; iPadOS 18.6 or later; watchOS 10.6 or later (Apple Watch app)",
     "softwareVersion": "1.0", "inLanguage": "en", "image": SITE + BASE + "appicon.png",
     "downloadUrl": store_url("en"), "installUrl": store_url("en"),
     "screenshot": [SITE + BASE + "assets/img/store/0%d-%s-1206.webp" % (i, n) for i, n in [(1, "hero"), (2, "watch"), (3, "countdown"), (5, "intervals")]],
     "isAccessibleForFree": True,
     "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "url": store_url("en")},
     "featureList": [
       "Hands-free photoshoots: start delay up to 60 seconds, interval from 0.5 seconds to 1 hour, 5 to 1,000 photos or Forever",
       "Burst intervals of about 42, 100 and 200 milliseconds (SHOOTS+)",
       "Apple Watch remote: start, stop, zoom with the Digital Crown, flip cameras, change mode and flash",
       "Apple Watch live viewfinder (SHOOTS+)",
       "48MP and Apple ProRAW (DNG) on supported iPhones (SHOOTS+); HEIF or JPEG",
       "Aspect ratios 3:4, 2:3, 9:16, 4:3, 3:2, 16:9 and Square; rule-of-thirds grid and level guide",
       "Video, Photo + Video, Live, Portrait and Cinematic modes (SHOOTS+); timed 4K or HD clips at 24, 30 or 60 fps",
       "Countdown beeps, five shutter sounds including Paparazzi, and a voice that announces the shoot and compliments you (compliments: SHOOTS+)",
       "Built-in gallery with one album per shoot, favorites, drag to select, save to Photos, 30-day Trash",
       "No account, no ads, no analytics, no tracking"],
     "author": {"@id": SITE + "/#person"}, "publisher": {"@id": SITE + "/#person"},
     "sameAs": ["https://apps.apple.com/app/id" + APP_ID]}

def head(page, pages, by_path):
    lang = page["lang"]
    t = T[lang]
    canon = SITE + page["url"]
    alts = alternates(page, by_path)
    alt_links = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE + BASE + p}">' for l, p in sorted(alts.items()))
    if "en" in alts:
        alt_links += f'<link rel="alternate" hreflang="x-default" href="{SITE + BASE + alts["en"]}">'
    og = SITE + BASE + "assets/img/og/" + og_slug(page) + ".jpg"
    title = html.escape(page["title"])
    desc = html.escape(page["description"], quote=True)
    og_alt = html.escape(page.get("og_alt", page["og_title"] + " — SHOOTS"), quote=True)
    locales = "".join(f'<meta property="og:locale:alternate" content="{T[l]["locale"]}">' for l in alts if l != lang)
    graph = [
      {"@type": "WebSite", "@id": SITE + BASE + "#website", "name": "SHOOTS", "url": SITE + BASE, "inLanguage": ["en", "tr", "es"], "publisher": {"@id": SITE + "/#person"}},
      person(),
    ]
    crumbs = [{"name": "SHOOTS", "url": SITE + url(lang, "home")}]
    if page["type"] == "article":
        sec = "journal" if page.get("section") == "journal" and lang == "en" else "guides"
        crumbs.append({"name": t["journal_t"] if sec == "journal" else t["guides_t"], "url": SITE + url(lang, sec)})
    if page["path"] != T[lang]["home"]:
        crumbs.append({"name": page.get("crumb", page["h1"]), "url": canon})
    webpage = {"@type": "WebPage", "@id": canon + "#webpage", "url": canon, "name": page["title"], "description": page["description"],
               "inLanguage": lang, "isPartOf": {"@id": SITE + BASE + "#website"}, "about": {"@id": SITE + BASE + "#app"},
               "primaryImageOfPage": og, "dateModified": page["updated"],
               "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c["name"], "item": c["url"]} for i, c in enumerate(crumbs)]}}
    if page.get("pagetype"):
        webpage["@type"] = page["pagetype"]
    graph.append(webpage)
    if page["type"] in ("home",) or page.get("app_schema"):
        graph.append(app_schema())
    if page["type"] == "article":
        graph.append({"@type": "BlogPosting" if page.get("section") == "journal" else "Article", "@id": canon + "#article",
                      "headline": page["h1"], "description": page["description"], "image": og, "inLanguage": lang,
                      "datePublished": page["date"], "dateModified": page["updated"], "mainEntityOfPage": {"@id": canon + "#webpage"},
                      "author": {"@id": SITE + "/#person"}, "publisher": {"@id": SITE + "/#person"},
                      "about": {"@id": SITE + BASE + "#app"}, "wordCount": page.get("words", 0)})
    if page.get("faq"):
        graph.append({"@type": "FAQPage", "@id": canon + "#faq", "inLanguage": lang, "mainEntity": [
            {"@type": "Question", "name": strip_tags(q["q"]), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(q["a"])}}
            for q in page["faq"] if "q" in q]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    preload = page.get("preload", "")
    kind = "article" if page["type"] == "article" else "website"
    art_meta = ""
    if page["type"] == "article":
        art_meta = (f'<meta property="article:published_time" content="{page["date"]}"><meta property="article:modified_time" content="{page["updated"]}">'
                    f'<meta property="article:author" content="Gül Eda Aydemir">')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Gül Eda Aydemir">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<link rel="canonical" href="{canon}">
{alt_links}
<link rel="icon" type="image/png" sizes="32x32" href="{BASE}favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="{BASE}appicon-180.png">
<meta name="theme-color" content="#0b0b0a">
<meta property="og:type" content="{kind}">
<meta property="og:site_name" content="SHOOTS">
<meta property="og:title" content="{html.escape(page['og_title'], quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{t['locale']}">{locales}
<meta property="og:image" content="{og}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">{art_meta}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(page['og_title'], quote=True)}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og}">
<script type="application/ld+json">
{ld}
</script>
<script>document.documentElement.classList.add('js');setTimeout(function(){{var d=document.documentElement;if(!d.classList.contains('js-ready'))d.classList.remove('js')}},3000)</script>
{FONTS}
{preload}<link rel="stylesheet" href="{BASE}assets/shoots.css?v={asset_v('shoots.css')}">
<script src="{BASE}assets/shoots.js?v={asset_v('shoots.js')}" defer></script>
</head>
"""

INK_FILTER = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><filter id="ink" x="-5%" y="-5%" width="110%" height="110%">'
              '<feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="7" result="n"/>'
              '<feDisplacementMap in="SourceGraphic" in2="n" scale="1.8" xChannelSelector="R" yChannelSelector="G"/></filter></svg>')

def header(page, by_path):
    lang = page["lang"]
    t = T[lang]
    keys = ["home", "features", "guides", "support", "about"]
    cur = page.get("nav")
    links = "".join(f'<a class="lk" href="{url(lang, k)}"{CUR_PAGE if cur == k else ""}>{n}</a>' for k, n in zip(keys, t["nav"]))
    alts = alternates(page, by_path)
    langs = []
    for l in ("en", "tr", "es"):
        href = BASE + alts[l] if l in alts else url(l, "home")
        langs.append(f'<a href="{href}" hreflang="{l}" lang="{l}" title="{T[l]["lang_name"]}"{CUR_TRUE if l == lang else ""}>{l.upper()}</a>')
    drawer = "".join(f'<a class="dl" href="{url(lang, k)}">{n}</a>' for k, n in zip(keys, t["nav"]))
    return f"""<body data-page="{page.get('nav', page['type'])}">
{INK_FILTER}
<a class="skip" href="#main">{t['skip']}</a>
<header class="site-head">
 <div class="wrap bar">
  <a class="brand" href="{url(lang, 'home')}" aria-label="SHOOTS"><img src="{BASE}appicon-128.webp" width="32" height="32" alt=""><span class="wm" aria-hidden="true"></span></a>
  <nav class="nav" aria-label="Primary">
   {links}
   <div class="langs" role="group" aria-label="Language">{''.join(langs)}</div>
   <a class="btn sm" href="{store_url(lang)}" data-ct="nav">{star_svg()}{t['download']}</a>
   <button class="menu-btn" type="button" aria-expanded="false" aria-controls="drawer" aria-label="{t['menu']}"><span></span></button>
  </nav>
 </div>
 <nav class="drawer" id="drawer" aria-label="{t['menu']}">{drawer}<a class="btn" href="{store_url(lang)}" data-ct="drawer">{star_svg()}{t['download']}</a></nav>
</header>
"""

def footer(page):
    lang = page["lang"]
    t = T[lang]
    tr = "tr/" if lang == "tr" else ""
    return f"""<footer class="site-foot">
 <div class="wrap">
  <span class="wm big" aria-hidden="true"></span>
  <div class="foot-grid">
   <div class="about"><p>{t['foot_about']}</p>{appstore(lang, 'footer')}</div>
   <div><h2>{t['foot_app']}</h2><ul>
    <li><a href="{url(lang, 'features')}">{t['f_features']}</a></li>
    <li><a href="{url(lang, 'guides')}">{t['f_guides']}</a></li>
    {f'<li><a href="{url(lang, "journal")}">{t["f_journal"]}</a></li>' if lang == 'en' else ''}
    <li><a href="{url(lang, 'support')}">{t['f_support']}</a></li>
    <li><a href="{url(lang, 'about')}">{t['f_about']}</a></li></ul></div>
   <div><h2>{t['foot_legal']}</h2><ul>
    <li><a href="{url(lang, 'privacy')}">{t['f_privacy']}</a></li>
    <li><a href="{BASE}terms/">{t['f_terms']}</a></li>
    <li><a href="mailto:{EMAIL}">{t['f_contact']}</a></li></ul></div>
   <div class="apps"><h2>{t['foot_more']}</h2><ul>
    <li><a href="/DUMP/{tr}"><img src="/DUMP/appicon-128.webp" width="26" height="26" alt="" loading="lazy">DUMP · {t['f_dump']}</a></li>
    <li><a href="/solo.swipe/{tr}"><img src="/solo.swipe/appicon-128.webp" width="26" height="26" alt="" loading="lazy">Solo.Swipe · {t['f_swipe']}</a></li>
    <li><a href="/{tr}">{t['f_all']}</a></li></ul></div>
   <div><h2>{t['foot_else']}</h2><ul>
    <li><a href="{store_url(lang)}">{t['f_store']}</a></li>
    <li><a href="https://instagram.com/solo.stasera">{t['f_insta']}</a></li>
    <li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
  </div>
  <div class="foot-bottom"><span>{t['f_bottom']}</span><span class="stamp" data-today>'26 10 22</span></div>
 </div>
</footer>
</body>
</html>
"""

# ---------------------------------------------------------------- article wrapper
def words_of(body):
    return len(strip_tags(body).split())

def article(page, pages, body):
    lang = page["lang"]
    t = T[lang]
    journal = page.get("section") == "journal"
    sec = "journal" if journal and lang == "en" else "guides"
    sec_name = t["journal_t"] if sec == "journal" else t["guides_t"]
    if page.get("author") == "gul":
        by = f'<img src="{BASE}appicon-128.webp" alt="" width="38" height="38"><span>{t["by"]} <b>Gül Eda</b>, xoxo</span>'
    elif journal:
        by = f'<img src="{BASE}appicon-128.webp" alt="" width="38" height="38"><span>{t["by"]} <b>{t["desk"]}</b> · {t["edited"]}</span>'
    else:
        by = f'<img src="{BASE}appicon-128.webp" alt="" width="38" height="38"><span>{t["by"]} <b>Gül Eda Aydemir</b></span>'
    d = t["date_fmt"](page["date"])
    cover = ""
    if page.get("cover"):
        c = page["cover"]
        cover = f'<figure class="cover rv">{device(c, page.get("cover_alt", page["h1"]), lazy=False)}<figcaption class="center">{page.get("cover_cap", "")}</figcaption></figure>'
    sign = ""
    if page.get("author") == "gul":
        sign = f'<div class="signoff"><span class="sig">xoxo, Gül Eda</span><small>{t["sig_small"]}</small></div>'
    related = [p for p in pages if p["lang"] == lang and p["type"] == "article" and p is not page]
    related.sort(key=lambda p: (0 if p.get("section") == page.get("section") else 1, p.get("order", 50)))
    related_html = "".join(post_card(p) for p in related[:3])
    return f"""<main id="main" class="article{' journal' if journal else ''}">
 <div class="wrap narrow">
  <header class="article-head">
   <ol class="crumbs"><li><a href="{url(lang, 'home')}">SHOOTS</a></li><li><a href="{url(lang, sec)}">{sec_name}</a></li></ol>
   <p class="kicker">{page.get('kicker', '')}</p>
   <h1>{page['h1']}</h1>
   {f'<p class="dek">{page["dek"]}</p>' if page.get('dek') else ''}
   <div class="byline">{by}<i class="dot"></i><time datetime="{page['date']}">{d}</time><i class="dot"></i><span>{page['mins']} {t['min']}</span></div>
  </header>
  {cover}
  <div class="prose">
{body}
  </div>
  {sign}
  <div class="author-box"><img src="{BASE}appicon-128.webp" alt="" width="56" height="56" loading="lazy"><p>{t['author_box'].format(e=EMAIL)}</p></div>
  <div style="margin-top:34px">{cta(lang)}</div>
 </div>
 <section class="sec tight related"><div class="wrap"><h2 class="poster h2" style="font-size:clamp(34px,4.6vw,56px);margin-bottom:30px">{t['more_t']}</h2><div class="posts">{related_html}</div></div></section>
</main>
"""

# ---------------------------------------------------------------- OG images
def og_slug(page):
    p = page["path"].strip("/") or "home"
    return p.replace("/", "-")

def og_images(pages, force=False):
    try:
        from PIL import Image, ImageDraw, ImageFont, ImageFilter
    except ImportError:
        print("Pillow missing: OG images skipped")
        return
    outdir = os.path.join(ROOT, "assets", "img", "og")
    os.makedirs(outdir, exist_ok=True)
    logo = Image.open(os.path.join(ROOT, "assets", "img", "logo", "logo-ink.webp")).split()[-1]
    grain = Image.open(os.path.join(ROOT, "assets", "img", "grain.png")).convert("L")
    SF = "/System/Library/Fonts/SFNS.ttf"
    MONO = "/System/Library/Fonts/SFNSMono.ttf"

    def font(size, width=40, weight=1000):
        f = ImageFont.truetype(SF, size)
        try:
            f.set_variation_by_axes([width, 96, 400, weight])
        except Exception:
            pass
        return f

    def tile_grain(img, strength, mode):
        g = Image.new("L", img.size)
        for x in range(0, img.size[0], grain.size[0]):
            for y in range(0, img.size[1], grain.size[1]):
                g.paste(grain, (x, y))
        rgb = Image.merge("RGB", (g, g, g))
        from PIL import ImageChops
        blend = ImageChops.screen(img, rgb) if mode == "screen" else ImageChops.multiply(img, rgb)
        return Image.blend(img, blend, strength)

    def brackets(d, color, inset=30, arm=34, w=3):
        W, H = 1200, 630
        for (x, y, dx, dy) in [(inset, inset, 1, 1), (W - inset, inset, -1, 1), (inset, H - inset, 1, -1), (W - inset, H - inset, -1, -1)]:
            d.line([(x, y), (x + dx * arm, y)], fill=color, width=w)
            d.line([(x, y), (x, y + dy * arm)], fill=color, width=w)

    def wrap_lines(d, text, f, maxw):
        words, lines, cur = text.split(), [], ""
        for w in words:
            cand = (cur + " " + w).strip()
            if d.textlength(cand, font=f) <= maxw or not cur:
                cur = cand
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    YEL, INK, EMB = (253, 253, 3), (10, 9, 5), (255, 133, 26)

    def up(text, lang):
        # Turkish capitals keep the dot: i → İ (str.upper() would give I).
        return text.replace("i", "İ").upper() if lang == "tr" else text.upper()

    cache_f = os.path.join(ROOT, "tools", "og-cache.json")
    cache = json.load(open(cache_f, encoding="utf-8")) if os.path.exists(cache_f) else {}
    for page in pages:
        slug = og_slug(page)
        jpg = os.path.join(outdir, slug + ".jpg")
        sig = json.dumps([page.get("og_title"), page.get("og_line"), page.get("kicker"), page.get("cover"), page["type"], page.get("og_style")], ensure_ascii=False)
        if not force and os.path.exists(jpg) and cache.get(slug) == sig:
            continue
        paper = page["type"] != "article" or page.get("og_style") == "paper"
        img = Image.new("RGB", (1200, 630), YEL if paper else (11, 11, 10))
        d = ImageDraw.Draw(img)
        fg = INK if paper else YEL
        mono = ImageFont.truetype(MONO, 22)
        if paper and page["type"] != "article":
            # The money shot: the logo printed on flash-yellow paper.
            lw = 760
            lh = round(lw * logo.size[1] / logo.size[0])
            m = logo.resize((lw, lh), Image.LANCZOS)
            img.paste(INK, ((1200 - lw) // 2, 120), m)
            line = up(page.get("og_line", page["og_title"]), page["lang"])
            f = ImageFont.truetype(MONO, 26)
            tw = d.textlength(line, font=f)
            if tw > 1040:
                f = ImageFont.truetype(MONO, int(26 * 1040 / tw))
                tw = d.textlength(line, font=f)
            d.text(((1200 - tw) / 2, 120 + lh + 44), line, font=f, fill=INK)
            brackets(d, INK)
            d.text((62, 52), "ISO 1600", font=mono, fill=INK)
            d.text((1200 - 62 - d.textlength("[36]", font=mono), 52), "[36]", font=mono, fill=INK)
            d.text((62, 630 - 78), "1/250  F2.8", font=mono, fill=INK)
            st = ImageFont.truetype("/System/Library/Fonts/SFNSMonoItalic.ttf", 26)
            d.text((1200 - 62 - d.textlength("'26 10 22", font=st), 630 - 82), "'26 10 22", font=st, fill=INK)
            img = tile_grain(img, 0.08, "multiply")
        else:
            # A poster headline on black film, with the cover screen on a phone.
            has_cover = bool(page.get("cover"))
            textw = 700 if has_cover else 1040
            title = up(page["og_title"], page["lang"])
            size = 104
            while size > 50:
                f = font(size)
                lines = wrap_lines(d, title, f, textw)
                if len(lines) * size * 0.98 <= 296:
                    break
                size -= 4
            kick = up(page.get("kicker") or "SHOOTS JOURNAL", page["lang"])
            d.text((80, 92), "● " + kick, font=mono, fill=(245, 245, 239))
            y = 140
            for ln in lines:
                d.text((78, y), ln, font=f, fill=fg)
                y += int(size * 0.98)
            lw = 150
            lh = round(lw * logo.size[1] / logo.size[0])
            img.paste(YEL, (80, 630 - 58 - lh), logo.resize((lw, lh), Image.LANCZOS))
            st = ImageFont.truetype("/System/Library/Fonts/SFNSMonoItalic.ttf", 24)
            if has_cover:
                shot = Image.open(os.path.join(ROOT, "assets", "img", "shots", page["cover"] + "-600.webp")).convert("RGB")
                sw = 270
                sh = round(shot.size[1] * sw / shot.size[0])
                shot = shot.resize((sw, sh), Image.LANCZOS)
                frame = Image.new("RGBA", (sw + 20, sh + 20), (0, 0, 0, 0))
                fd = ImageDraw.Draw(frame)
                fd.rounded_rectangle([0, 0, sw + 19, sh + 19], radius=44, fill=(5, 5, 5, 255), outline=(50, 50, 45, 255), width=2)
                mask = Image.new("L", (sw, sh), 0)
                ImageDraw.Draw(mask).rounded_rectangle([0, 0, sw - 1, sh - 1], radius=36, fill=255)
                frame.paste(shot, (10, 10), mask)
                frame = frame.rotate(-6, resample=Image.BICUBIC, expand=True)
                img.paste(frame, (830, 40), frame)
                # a paparazzi flash on the corner of the phone
                glow = Image.new("L", (1200, 630), 0)
                gd = ImageDraw.Draw(glow)
                cx, cy = 840, 92
                gd.ellipse([cx - 70, cy - 70, cx + 70, cy + 70], fill=255)
                glow = glow.filter(ImageFilter.GaussianBlur(34))
                img.paste((255, 255, 255), (0, 0), glow)
                OUTL = [(8, .2), (29, .63), (43, .14), (57, .55), (85, .14), (118, .49), (136, .12), (155, .55), (178, .18), (204, .54), (222, .14), (241, .47), (274, .1), (310, .49), (328, .13), (347, .6)]
                d2 = ImageDraw.Draw(img)
                d2.polygon([(cx + math.cos(math.radians(a - 3)) * r * 56, cy + math.sin(math.radians(a - 3)) * r * 56) for a, r in OUTL], fill=(255, 255, 255))
                d2.line([(cx - 160, cy), (cx + 160, cy)], fill=(255, 255, 255), width=2)
            d = ImageDraw.Draw(img)
            brackets(d, (245, 245, 239))
            sx = 80 + 150 + 28 if has_cover else 1200 - 70 - d.textlength("'26 10 22", font=st)
            d.text((sx, 630 - 82), "'26 10 22", font=st, fill=EMB)
            img = tile_grain(img, 0.06, "screen")
        img.save(jpg, "JPEG", quality=82, optimize=True, progressive=True)
        img.resize((600, 315), Image.LANCZOS).save(os.path.join(outdir, slug + "-600.webp"), "WEBP", quality=80, method=6)
        cache[slug] = sig
    json.dump(cache, open(cache_f, "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)

# ---------------------------------------------------------------- sitemap
def sitemap(pages):
    rows = []
    for p in sorted(pages, key=lambda p: (p["lang"] != "en", p["path"])):
        alts = alternates(p, None)
        links = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE + BASE + q}"/>' for l, q in sorted(alts.items())) if len(alts) > 1 else ""
        if len(alts) > 1 and "en" in alts:
            links += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE + BASE + alts["en"]}"/>'
        rows.append(f"  <url>\n    <loc>{SITE + p['url']}</loc>\n    <lastmod>{p['updated']}</lastmod>{links}\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<!-- SHOOTS pages in English, Turkish and Spanish. Generated by SHOOTS/tools/build.py. -->\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)

# ---------------------------------------------------------------- llms.txt
def llms(pages):
    head_f = os.path.join(ROOT, "tools", "llms-head.md")
    if not os.path.exists(head_f):
        return
    out = [open(head_f, encoding="utf-8").read().rstrip(), ""]
    groups = [("English guides", "en", "guides"), ("English journal", "en", "journal"), ("Türkçe rehberler (Turkish)", "tr", None), ("Guías en español (Spanish)", "es", None)]
    for title, lang, sec in groups:
        items = [p for p in pages if p["lang"] == lang and p["type"] == "article" and (sec is None or p.get("section") == sec)]
        if not items:
            continue
        items.sort(key=lambda p: (p.get("order", 50), p["h1"]))
        out.append(f"## {title}\n")
        for p in items:
            by = " (by Gül Eda Aydemir, personal post)" if p.get("author") == "gul" else ""
            out.append(f"- [{p['h1']}]({SITE + p['url']}): {p['description']}{by}")
        out.append("")
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")

# ---------------------------------------------------------------- main
def main():
    pages = load_pages()
    by_path = {p["path"]: p for p in pages}
    # hreflang must be two-way and complete: every translation of a page links to every other.
    clusters = {}
    for p in pages:
        for l, q in (p.get("alt") or {}).items():
            if q not in by_path:
                sys.exit(f"{p['src']}: alt {l} → {q} has no page")
            other = by_path[q]
            a_root = clusters.get(p["path"], {p["path"]})
            b_root = clusters.get(other["path"], {other["path"]})
            merged = a_root | b_root
            for member in merged:
                clusters[member] = merged
    for path, members in clusters.items():
        page = by_path[path]
        page["alt"] = {by_path[m]["lang"]: m for m in members if m != path}
    for p in pages:
        if p["type"] == "article":
            p["words"] = words_of(p["body"])
            p["mins"] = max(2, round(p["words"] / 230))
    og_images(pages, force="--force-og" in sys.argv)
    for p in pages:
        body = shortcodes(p["body"], p["lang"], p, pages)
        main_html = article(p, pages, body) if p["type"] == "article" else body
        out = head(p, pages, by_path) + header(p, by_path) + main_html + footer(p)
        dest = os.path.join(ROOT, p["path"], "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(out)
    sitemap(pages)
    llms(pages)
    print(f"built {len(pages)} pages")

if __name__ == "__main__":
    main()
