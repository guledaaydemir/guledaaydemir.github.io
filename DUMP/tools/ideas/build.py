#!/usr/bin/env python3
"""Builds DUMP's ideas pages from one JSON content file per page.

    python3 DUMP/tools/ideas/build.py              # pages, indexes, sitemap + llms blocks, share images
    python3 DUMP/tools/ideas/build.py --force-og   # also re-render every share image
    python3 DUMP/tools/ideas/build.py --check      # validate the content files, write nothing

Content:  DUMP/tools/ideas/pages/<lang>/<slug>.json  (one file per page, see README.md)
Settings: DUMP/tools/ideas/config.json  (App Store provider token, Custom Product Page ids)
Writes:   DUMP/<slug>/index.html and DUMP/tr/<slug>/index.html, the ideas indexes
          (DUMP/ideas/, DUMP/tr/fikirler/), an og.jpg next to each page, and the generated
          blocks in DUMP/sitemap.xml and DUMP/llms.txt. Hand edits to those outputs get overwritten.
Share images are rendered by headless Google Chrome from the site's own fonts and colours,
then saved as JPEG with Pillow. No other dependencies.
"""
import glob, hashlib, html, json, os, re, shutil, subprocess, sys, tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))                   # …/DUMP/tools/ideas
DUMP = os.path.dirname(os.path.dirname(TOOLS))                       # …/DUMP
SITE = "https://guledaaydemir.github.io"
APP_ID = "6798248086"
EMAIL = "solostaseraofficial@gmail.com"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
MAX_TITLE, MAX_DESC = 60, 155
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.36 12.9c.02-2.2 1.8-3.26 1.88-3.31-1.03-1.5-2.62-1.71-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 2.18-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.74 2.21 1.1-.04 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.08 2.65-2.14.84-1.23 1.18-2.42 1.2-2.48-.03-.01-2.3-.88-2.32-3.5zM14.2 6.3c.6-.74 1.01-1.76.9-2.78-.87.04-1.93.58-2.56 1.31-.56.65-1.05 1.69-.92 2.68.97.08 1.96-.49 2.58-1.21z"/></svg>'
INSTAGRAM = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zm0 3.68A6.16 6.16 0 1 0 18.16 12 6.16 6.16 0 0 0 12 5.84zm0 10.16A4 4 0 1 1 16 12a4 4 0 0 1-4 4zm6.4-10.4a1.44 1.44 0 1 0 1.44 1.44A1.44 1.44 0 0 0 18.4 5.6z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4.24-8 4.76-8-4.76V6l8 4.76L20 6z"/></svg>'
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">')

# Cloudflare Web Analytics (cookieless visit counts; disclosed in the privacy policies)
CF_BEACON = '<!-- Cloudflare Web Analytics --><script type=\'module\' src=\'https://static.cloudflareinsights.com/beacon.min.js\' data-cf-beacon=\'{"token": "0d4a3a7a679a46d1b1ff35a88bd52782"}\'></script><!-- End Cloudflare Web Analytics -->'

e = html.escape

# ---------------------------------------------------------------- chrome strings
# Everything a page needs that is not content: navigation, footer, CTA wording, labels.
T = {
    "en": {
        "locale": "en_US", "home": "/DUMP/", "ideas": "/DUMP/ideas/", "skip": "Skip to content",
        "brand_aria": "DUMP home", "nav_aria": "Primary", "menu_aria": "Menu", "open_menu": "Open menu",
        "lang_aria": "Language / Dil",
        "nav": [("Home", "/DUMP/"), ("Features", "/DUMP/#features"), ("Guides", "/DUMP/guides/"),
                ("FAQ", "/DUMP/faq.html"), ("Support", "/DUMP/support.html")],
        "drawer": [("Home", "/DUMP/"), ("Features", "/DUMP/#features"), ("How it works", "/DUMP/#how"),
                   ("Free vs Premium", "/DUMP/#premium"), ("Guides", "/DUMP/guides/"), ("FAQ", "/DUMP/faq.html"),
                   ("Support", "/DUMP/support.html"), ("More apps by Gül Eda", "/")],
        "download": "Download", "download_long": "Download on the App Store",
        "crumb_ideas": "Ideas", "byline": "By", "byline_role": "indie iOS developer", "updated": "Updated",
        "min_read": "min read", "jump": "On this page", "faq_h": "Frequently asked questions",
        "more_h": "More ideas", "more_dump": 'Want the how-to as well? Browse the <a href="/DUMP/guides/">DUMP guides</a> or see <a href="/DUMP/">what DUMP does</a>.',
        "copy": "Copy", "copied": "Copied", "copy_sr": "caption",
        "cta_h": "Turn your camera roll into a photo dump in under a minute",
        "cta_p": "DUMP picks your sharpest, most varied shots, lays them out as a carousel and saves the slides to Photos in posting order. Free on iPhone and iPad.",
        "cta_aria": "Get DUMP on the App Store", "badge_small": "Download on the", "badge_aria": "Download DUMP on the App Store",
        "qr_alt": "QR code that opens DUMP on the App Store", "qr_b": "On a computer?", "qr_t": "Scan with your iPhone camera",
        "cta_tiny": "Free · iPhone &amp; iPad · iOS 18.6+ · No account · Works offline",
        "sticky_aria": "Download DUMP", "sticky_m": "Free · iPhone &amp; iPad · No account",
        "more_apps": "More apps by Gül Eda",
        "apps": [("/solo.swipe/", "Solo.Swipe", "Swipe to clean your camera roll in 5-minute daily sessions"),
                 ("/solo.shots/", "Solo.Shots", "Progress photos that line up, turned into a timelapse"),
                 ("/solora/", "Solora", "Role-based life planner: pick today's Big 3, keep habits going"),
                 ("/ATHA/", "ATHA", "Breathing exercises for sleep, stress and focus — calm in one tap")],
        "tagline": "Pick it. Make it. <b>DUMP</b> it.", "tagline2": "The photo dump app that picks your best shots, on your iPhone.",
        "ig_aria": "@solo.stasera on Instagram", "mail_aria": "Email DUMP support", "store_aria": "DUMP on the App Store",
        "foot": [("DUMP", [("Features", "/DUMP/#features"), ("How it works", "/DUMP/#how"), ("Free vs Premium", "/DUMP/#premium"),
                           ("What's new", "/DUMP/#whats-new"), ("Guides", "/DUMP/guides/"), ("Ideas", "/DUMP/ideas/")]),
                 ("Help", [("FAQ", "/DUMP/faq.html"), ("Support", "/DUMP/support.html"), ("Email the developer", "mailto:" + EMAIL),
                           ("Rate on the App Store", "https://apps.apple.com/app/id6798248086?action=write-review")]),
                 ("About", [("About the developer", "/about/"), ("Privacy Policy", "/DUMP/privacypolicy.html"),
                            ("Terms of Use", "/DUMP/terms.html"), ("All apps by Gül Eda", "/")])],
        "index": {
            "slug": "ideas", "crumb": "Ideas", "eyebrow": "Ideas",
            "title": "Photo Dump Ideas, Captions & Carousel Layouts | DUMP",
            "description": "Free photo dump ideas to copy and use: 100 captions, 40 dump ideas with slide order tips and seamless Instagram carousel layouts.",
            "h1": 'Ideas for your next <span class="g">photo dump.</span>',
            "lead": "Captions you can copy in one tap, what to put in each kind of dump, and carousel layouts to try. Everything here is original and free to use. Written by Gül Eda Aydemir, who makes DUMP.",
            "count": "{n} idea pages", "cards_h": "Pick a starting point", "guides_h": "Looking for step-by-step help?",
            "guides_p": 'The <a href="/DUMP/guides/">DUMP guides</a> cover picking photos, posting order, carousel sizes and photo quality, each with sources.',
            "og": {"kicker": "Photo dump ideas", "title": "Ideas for your next", "accent": "photo dump", "sub": "Captions, dump ideas and carousel layouts", "art": "index"},
        },
    },
    "tr": {
        "locale": "tr_TR", "home": "/DUMP/tr/", "ideas": "/DUMP/tr/fikirler/", "skip": "İçeriğe geç",
        "brand_aria": "DUMP ana sayfa", "nav_aria": "Ana menü", "menu_aria": "Menü", "open_menu": "Menüyü aç",
        "lang_aria": "Dil / Language",
        "nav": [("Ana sayfa", "/DUMP/tr/"), ("Özellikler", "/DUMP/tr/#ozellikler"), ("Rehberler", "/DUMP/tr/#rehberler"),
                ("SSS", "/DUMP/tr/#sss"), ("Destek", "/DUMP/support.html")],
        "drawer": [("Ana sayfa", "/DUMP/tr/"), ("Özellikler", "/DUMP/tr/#ozellikler"), ("Nasıl çalışır?", "/DUMP/tr/#nasil"),
                   ("Ücretsiz ve Premium", "/DUMP/tr/#premium"), ("Rehberler", "/DUMP/tr/#rehberler"), ("SSS", "/DUMP/tr/#sss"),
                   ("Destek (İngilizce)", "/DUMP/support.html"), ("Gül Eda'nın diğer uygulamaları", "/")],
        "download": "İndir", "download_long": "App Store'dan indir",
        "crumb_ideas": "Fikirler", "byline": "Yazan:", "byline_role": "bağımsız iOS geliştiricisi", "updated": "Güncellendi",
        "min_read": "dk okuma", "jump": "Bu sayfada", "faq_h": "Sık sorulan sorular",
        "more_h": "Daha fazla fikir", "more_dump": 'Adım adım anlatım mı lazım? <a href="/DUMP/tr/#rehberler">Türkçe rehberlere</a> göz at ya da <a href="/DUMP/tr/">DUMP\'ın neler yaptığını</a> gör.',
        "copy": "Kopyala", "copied": "Kopyalandı", "copy_sr": "açıklama",
        "cta_h": "Galerini bir dakikadan kısa sürede photo dump'a dönüştür",
        "cta_p": "DUMP en net ve en çeşitli karelerini seçer, kaydırmalı post olarak dizer ve slaytları paylaşım sırasıyla Fotoğraflar'a kaydeder. iPhone ve iPad'de ücretsiz.",
        "cta_aria": "DUMP'ı App Store'dan indir", "badge_small": "Ücretsiz indir", "badge_aria": "DUMP'ı App Store'dan indir",
        "qr_alt": "DUMP'ı App Store'da açan QR kod", "qr_b": "Bilgisayarda mısın?", "qr_t": "iPhone kameranla tara",
        "cta_tiny": "Ücretsiz · iPhone ve iPad · iOS 18.6+ · Hesap yok · İnternetsiz çalışır · Uygulama Türkçe",
        "sticky_aria": "DUMP'ı indir", "sticky_m": "Ücretsiz · iPhone ve iPad · Hesap yok",
        "more_apps": "Gül Eda'nın diğer uygulamaları",
        "apps": [("/solo.swipe/tr/", "Solo.Swipe", "Galerini günde 5 dakikalık kaydırma seanslarıyla temizle"),
                 ("/solo.shots/tr/", "Solo.Shots", "Üst üste oturan ilerleme fotoğrafları, sonunda bir timelapse"),
                 ("/solora/tr/", "Solora", "Rollerine göre yaşam planlayıcı: günün 3 önceliğini seç, alışkanlıkları sürdür"),
                 ("/ATHA/tr/", "ATHA", "Uyku, stres ve odak için nefes egzersizleri: tek dokunuşla sakinlik")],
        "tagline": "Seç. Yap. <b>DUMP</b>'la.", "tagline2": "En iyi karelerini iPhone'unda seçen photo dump uygulaması.",
        "ig_aria": "Instagram'da @solo.stasera", "mail_aria": "DUMP desteğine e-posta gönder", "store_aria": "App Store'da DUMP",
        "foot": [("DUMP", [("Özellikler", "/DUMP/tr/#ozellikler"), ("Nasıl çalışır?", "/DUMP/tr/#nasil"),
                           ("Ücretsiz ve Premium", "/DUMP/tr/#premium"), ("Türkçe rehberler", "/DUMP/tr/#rehberler"),
                           ("Fikirler", "/DUMP/tr/fikirler/"), ("Tüm rehberler (İngilizce)", "/DUMP/guides/")]),
                 ("Yardım", [("Sık sorulan sorular", "/DUMP/tr/#sss"), ("Destek (İngilizce)", "/DUMP/support.html"),
                             ("Geliştiriciye e-posta (Türkçe yazabilirsin)", "mailto:" + EMAIL),
                             ("App Store'da değerlendir", "https://apps.apple.com/tr/app/id6798248086?action=write-review")]),
                 ("Hakkında", [("Geliştirici hakkında (İngilizce)", "/about/"), ("Gizlilik Politikası (İngilizce)", "/DUMP/privacypolicy.html"),
                               ("Kullanım Koşulları (İngilizce)", "/DUMP/terms.html"), ("Tüm uygulamalar", "/")])],
        "index": {
            "slug": "fikirler", "crumb": "Fikirler", "eyebrow": "Fikirler",
            "title": "Photo Dump Fikirleri, Caption ve Carousel Önerileri",
            "description": "Ücretsiz photo dump fikirleri: tek dokunuşla kopyalanan 100 caption, slayt sırası ipuçlarıyla 40 dump fikri ve kesintisiz carousel düzenleri.",
            "h1": 'Bir sonraki <span class="g">photo dump\'ın</span> için fikirler.',
            "lead": "Tek dokunuşla kopyalayabileceğin açıklamalar, her dump türüne ne koyacağın ve deneyebileceğin carousel düzenleri. Hepsi özgün ve ücretsiz. DUMP'ı yapan Gül Eda Aydemir yazdı.",
            "count": "{n} fikir sayfası", "cards_h": "Nereden başlamak istersin?", "guides_h": "Adım adım anlatım mı arıyorsun?",
            "guides_p": '<a href="/DUMP/tr/#rehberler">Türkçe rehberler</a> fotoğraf seçmeyi, kaydırmalı post paylaşmayı ve birleşik postu anlatıyor; <a href="/DUMP/guides/" hreflang="en">İngilizce rehberler</a> boyutları ve kaliteyi de kapsıyor.',
            "og": {"kicker": "Photo dump fikirleri", "title": "Bir sonraki", "accent": "photo dump'ın için", "sub": "Caption, dump fikirleri ve carousel düzenleri", "art": "index"},
        },
    },
}

# ---------------------------------------------------------------- helpers
def path_of(lang, slug):
    return f"/DUMP/{slug}/" if lang == "en" else f"/DUMP/{lang}/{slug}/"

def abs_url(path):
    return SITE + path

def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()

def unfilled(value):
    """Placeholders are written in capitals (PROVIDER_TOKEN, PPID_CAROUSEL): treat them as empty."""
    return not value or re.fullmatch(r"[A-Z_]+", value) is not None

def store_link(cfg, campaign, product_page):
    """The App Store campaign link from the user's spec. pt and ppid are added once config.json has them."""
    q = []
    if not unfilled(cfg.get("provider_token")):
        q.append("pt=" + cfg["provider_token"])
    q.append("ct=" + campaign)
    q.append("mt=8")
    ppid = (cfg.get("product_pages") or {}).get(product_page or "")
    if product_page and not unfilled(ppid):
        q.append("ppid=" + ppid)
    return f"https://apps.apple.com/app/apple-store/id{APP_ID}?" + "&amp;".join(q)

def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=1) + "\n</script>"

def fmt_date(iso, lang):
    y, m, d = iso.split("-")
    months = {"en": "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec",
              "tr": "Ocak Şubat Mart Nisan Mayıs Haziran Temmuz Ağustos Eylül Ekim Kasım Aralık"}[lang].split()
    return f"{int(d)} {months[int(m) - 1]} {y}"

# ---------------------------------------------------------------- carousel layout strips
# Tiny CSS diagrams for layout ideas: n portrait panels with dashed seams, plus shapes placed in %.
# Each preset returns a list of (class, left, top, width, height, extra-style).
def _tiles(n, panels, top=28, h=44, w=None, cls="ph"):
    pw = 100 / n
    w = w or pw * 0.62
    return [(cls + ("" if i % 2 == 0 else " b"), pw * p + (pw - w) / 2, top, w, h, "") for i, p in enumerate(panels)]

def _seam_tiles(n, top=26, h=46):
    pw = 100 / n
    w = pw * 0.56
    return [("ph" + ("" if i % 2 else " b"), pw * (i + 1) - w / 2, top + (6 if i % 2 else 0), w, h, f"transform:rotate({-4 if i % 2 else 3}deg)") for i in range(n - 1)]

STRIPS = {
    "horizon": lambda n: [("sky", 0, 0, 100, 100, ""), ("sea", 0, 64, 100, 36, ""), ("sun", 100 / n * 1.5 - 7, 40, 14, 0, "")],
    "reveal": lambda n: [("sky dusk", 0, 0, 100, 100, ""), ("blob", 100 / n * 0.62, 22, 100 / n * 0.9, 62, "")],
    "line": lambda n: [("sky", 0, 0, 100, 100, ""), ("sea", 0, 64, 100, 36, ""), ("ln", 0, 63, 100, 0, ""), ("dt", 100 - 100 / n * 0.5, 63, 0, 0, "")],
    "fade": lambda n: [("sky fade", 0, 0, 100, 100, "")],
    "scrapbook": lambda n: [("paper", 0, 0, 100, 100, "")] + _tiles(n, range(n), top=14, h=38) + _seam_tiles(n, top=48, h=40),
    "film": lambda n: [("band", 0, 24, 100, 52, "")] + [("ph" + (" b" if i % 2 else ""), 2 + i * (96 / (2 * n)), 32, 96 / (2 * n) - 2, 36, "") for i in range(2 * n)],
    "banner": lambda n: [("paper dark", 0, 0, 100, 100, ""), ("tx", 100 / n * 0.25, 30, 100 / n * 1.5, 12, ""), ("tx", 100 / n * 0.25, 48, 100 / n * 1.0, 8, "")] + _tiles(n, range(2, n)),
    "colors": lambda n: [("sky hues", 0, 0, 100, 100, "")] + _tiles(n, range(n), top=24, h=52),
    "timeline": lambda n: [("paper dark", 0, 0, 100, 100, ""), ("ln", 3, 50, 94, 0, "")] + [("dt", 100 / n * (i + 0.5), 50, 0, 0, "") for i in range(n)]
              + [("ph" + (" b" if i % 2 else ""), 100 / n * (i + 0.5) - 100 / n * 0.3, 12 if i % 2 == 0 else 58, 100 / n * 0.6, 30, "") for i in range(n)],
    "opener": lambda n: [("sky", 0, 0, 300 / n, 100, ""), ("sea", 0, 64, 300 / n, 36, ""), ("sun", 100 / n * 1.5 - 5, 40, 10, 0, "")] + _tiles(n, range(3, n)),
    "closer": lambda n: _tiles(n, range(0, n - 2)) + [("sky", 100 - 200 / n, 0, 200 / n, 100, ""), ("sea", 100 - 200 / n, 64, 200 / n, 36, ""), ("sun", 100 - 100 / n - 5, 40, 10, 0, "")],
    "middle": lambda n: _tiles(n, [0, 1, n - 1]) + [("sky", 200 / n, 0, 100 - 300 / n, 100, ""), ("sea", 200 / n, 64, 100 - 300 / n, 36, ""), ("sun", 50 - 5, 40, 10, 0, "")],
    "beforeafter": lambda n: [("sky grey", 0, 0, 50, 100, ""), ("sky", 50, 0, 50, 100, ""), ("sea grey", 0, 64, 50, 36, ""), ("sea", 50, 64, 50, 36, "")],
    "zoom": lambda n: [("sky", 0, 0, 300 / n, 100, ""), ("sea", 0, 64, 300 / n, 36, ""), ("sun", 100 / n * 1.5 - 5, 40, 10, 0, ""),
                       ("ph sunny", 100 / n * 3.12, 14, 100 / n * 0.76, 72, ""), ("ph sea", 100 / n * 4.12, 14, 100 / n * 0.76, 72, "")],
    "route": lambda n: [("paper map", 0, 0, 100, 100, "")] + [("dt", x, y, 0, 0, "") for x, y in
                        [(6, 70), (14, 62), (22, 56), (30, 50), (38, 46), (46, 44), (54, 46), (62, 50), (70, 52), (78, 48), (86, 40), (94, 32)][::1]]
                       + [("pin", 100 / n * (i + 0.5), [62, 44, 50, 40][i % 4] - 22, 0, 0, "") for i in range(n)],
}

def strip_html(preset, n):
    parts = []
    for cls, x, y, w, h, extra in STRIPS[preset](n):
        style = f"left:{x:.2f}%;top:{y:.2f}%"
        if w: style += f";width:{w:.2f}%"
        if h: style += f";height:{h:.2f}%"
        if extra: style += ";" + extra
        parts.append(f'<b class="{cls}" style="{style}"></b>')
    seams = "".join(f'<i style="left:{100 * k / n:.3f}%"></i>' for k in range(1, n))
    return f'<div class="strip" style="--n:{n}" aria-hidden="true">{"".join(parts)}{seams}</div>'

# ---------------------------------------------------------------- content loading
def load_pages():
    pages = []
    for f in sorted(glob.glob(os.path.join(TOOLS, "pages", "*", "*.json"))):
        with open(f, encoding="utf-8") as fh:
            p = json.load(fh)
        p["lang"] = os.path.basename(os.path.dirname(f))
        p["src"] = os.path.relpath(f, os.path.dirname(DUMP))
        if p["lang"] not in T:
            sys.exit(f"{p['src']}: no chrome strings for language '{p['lang']}' (add it to T in build.py)")
        p["path"] = path_of(p["lang"], p["slug"])
        pages.append(p)
    return pages

def validate(pages):
    problems, warnings = [], []
    seen = {}
    for p in pages:
        src = p["src"]
        for k in ("key", "slug", "title", "description", "h1", "campaign", "keyword", "published", "updated", "card", "og", "intro", "sections", "faq"):
            if k not in p:
                problems.append(f"{src}: missing \"{k}\"")
        if problems:
            continue
        if len(p["title"]) > MAX_TITLE:
            problems.append(f"{src}: title is {len(p['title'])} characters (max {MAX_TITLE})")
        if len(p["description"]) > MAX_DESC:
            problems.append(f"{src}: description is {len(p['description'])} characters (max {MAX_DESC})")
        if not re.fullmatch(r"[a-z0-9-]+", p["slug"]):
            problems.append(f"{src}: slug must be lowercase letters, digits and hyphens")
        if len(p["campaign"]) > 30:
            problems.append(f"{src}: campaign tag is longer than App Store Connect's 30 characters")
        if not 4 <= len(p["faq"]) <= 6:
            warnings.append(f"{src}: {len(p['faq'])} FAQ questions (4-5 recommended)")
        if (p["lang"], p["slug"]) in seen:
            problems.append(f"{src}: slug already used by {seen[(p['lang'], p['slug'])]}")
        seen[(p["lang"], p["slug"])] = src
        ids = [s["id"] for s in p["sections"]]
        if len(ids) != len(set(ids)):
            problems.append(f"{src}: section ids must be unique")
        if p.get("mid_cta_after") and p["mid_cta_after"] not in ids:
            problems.append(f"{src}: mid_cta_after '{p['mid_cta_after']}' is not a section id")
    by_key = {}
    for p in pages:
        by_key.setdefault(p.get("key"), []).append(p["lang"])
    for key, langs in by_key.items():
        if len(langs) != len(set(langs)):
            problems.append(f"key '{key}' is used twice in one language")
    return problems, warnings

# ---------------------------------------------------------------- page parts
def header(lang, alt_path, cfg_link):
    t = T[lang]
    nav = "\n".join(f'      <a class="lk" href="{h}">{e(l)}</a>' for l, h in t["nav"])
    drawer = "\n".join(f'    <a href="{h}">{e(l)}</a>' for l, h in t["drawer"])
    here = alt_path[lang]
    langsw = "".join(
        f'<a href="{alt_path[l]}" hreflang="{l}" lang="{l}" title="{"English" if l == "en" else "Türkçe"}"{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>'
        for l in ("en", "tr") if l in alt_path)
    langsw_html = f'\n      <div class="langsw" role="group" aria-label="{t["lang_aria"]}">{langsw}</div>' if len(alt_path) > 1 else ""
    return f"""<a class="skip" href="#main">{t['skip']}</a>

<header class="site">
  <div class="nav">
    <a class="brand" href="{t['home']}" aria-label="{e(t['brand_aria'])}">
      <img src="/DUMP/appicon-128.webp" alt="" width="32" height="32">
      <span class="wordmark">DUMP</span>
    </a>
    <nav class="navlinks" aria-label="{e(t['nav_aria'])}">
{nav}
      <a class="btn btn-grad magnet" href="{cfg_link}">{t['download']}</a>{langsw_html}
      <button class="navtoggle" aria-expanded="false" aria-label="{e(t['open_menu'])}" aria-controls="drawer"><span></span></button>
    </nav>
  </div>
  <span class="scrollbar" aria-hidden="true"></span>
  <nav class="navdrawer" id="drawer" aria-label="{e(t['menu_aria'])}">
{drawer}
    <a class="btn btn-grad" href="{cfg_link}">{e(t['download_long'])}</a>
  </nav>
</header>"""

def footer(lang, link):
    t = T[lang]
    # motion.js tags every App Store link without ct= using data-ct, so the review link gets its own tag
    review_ct = f' data-ct="{"" if lang == "en" else lang + "-"}footer-review"'
    apps = "\n".join(f"""        <a class="app-card" href="{h}">
          <img src="{h.split('/tr/')[0].rstrip('/') + '/'}appicon-128.webp" alt="" width="44" height="44" loading="lazy" decoding="async">
          <span><b>{n}</b><small>{e(d)}</small></span>
        </a>""" for h, n, d in t["apps"])
    cols = "\n".join("      <div>\n        <h2 class=\"fh\">" + e(h) + "</h2>\n" + "\n".join(
        f'        <a href="{u}"{review_ct if "write-review" in u else ""}>{e(l)}</a>' for l, u in links) + "\n      </div>" for h, links in t["foot"])
    return f"""<footer class="site">
  <div class="wrap">
    <section class="more-apps" aria-labelledby="more-apps-h">
      <h2 class="fh" id="more-apps-h">{e(t['more_apps'])}</h2>
      <div class="more-apps-grid">
{apps}
      </div>
    </section>
    <div class="foot-grid">
      <div>
        <a class="brand" href="{t['home']}" aria-label="{e(t['brand_aria'])}">
          <img src="/DUMP/appicon-128.webp" alt="" width="32" height="32" loading="lazy">
          <span class="wordmark">DUMP</span>
        </a>
        <p class="tagline" style="margin-top:12px">{t['tagline']}</p>
        <p class="tagline" style="margin-top:6px">{e(t['tagline2'])}</p>
        <div class="social">
          <a href="https://instagram.com/solo.stasera" target="_blank" rel="noopener noreferrer" aria-label="{e(t['ig_aria'])}">{INSTAGRAM}</a>
          <a href="mailto:{EMAIL}" aria-label="{e(t['mail_aria'])}">{MAIL}</a>
          <a href="{link}" aria-label="{e(t['store_aria'])}">{APPLE}</a>
        </div>
      </div>
{cols}
    </div>
    <div class="foot-bottom">
      <span>© <span id="yr">2026</span> Gül Eda Aydemir · DUMP: Carousel &amp; Collage</span>
      <span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://instagram.com/solo.stasera" target="_blank" rel="noopener noreferrer">@solo.stasera</a></span>
    </div>
  </div>
</footer>

<div class="stickybar" role="complementary" aria-label="{e(t['sticky_aria'])}">
  <img src="/DUMP/appicon-128.webp" alt="" width="40" height="40" loading="lazy">
  <div class="m"><b>DUMP</b><span>{t['sticky_m']}</span></div>
  <a class="btn btn-grad" href="{link}">{t['download']}</a>
</div>"""

def badge(lang, link, magnet=False):
    t = T[lang]
    return (f'<a class="appstore{" magnet" if magnet else ""}" href="{link}" aria-label="{e(t["badge_aria"])}">\n  {APPLE}\n'
            f'  <span class="t"><small>{e(t["badge_small"])}</small><b>App Store</b></span>\n</a>')

def cta_card(lang, link, text):
    t = T[lang]
    return f"""<aside class="try-card" aria-label="{e(t['cta_aria'])}">
  <img src="/DUMP/appicon-128.webp" alt="" width="52" height="52" loading="lazy">
  <div class="tx"><b>{e(t['cta_h'])}</b><p>{text}</p></div>
  {badge(lang, link)}
</aside>"""

def cta_end(lang, link, text):
    t = T[lang]
    return f"""<div class="guide-cta">
  <h2>{e(t['cta_h'])}</h2>
  <p>{text}</p>
  <div class="cta-row">
    {badge(lang, link, magnet=True)}
    <div class="qr">
  <img loading="lazy" src="/DUMP/assets/appstore-qr.svg" width="76" height="76" alt="{e(t['qr_alt'])}">
  <span><b>{e(t['qr_b'])}</b>{e(t['qr_t'])}</span>
</div>
  </div>
  <p class="tiny" style="margin-top:14px;margin-bottom:0">{t['cta_tiny']}</p>
</div>"""

def faq_html(lang, faq):
    t = T[lang]
    items = []
    for i, q in enumerate(faq):
        items.append(f"""  <details id="faq-{i + 1}"{' open' if i == 0 else ''}>
    <summary><h3>{e(q['q'])}</h3><span class="pm" aria-hidden="true">+</span></summary>
    <div class="a"><p>{q['a']}</p></div>
  </details>""")
    return f'<h2 id="faq">{e(t["faq_h"])}</h2>\n<div class="faq-list">\n' + "\n".join(items) + "\n</div>"

def page_card(p, cls="guide-card"):
    c = p["card"]
    cv = p.get("cover")
    if cv:
        s = cv["slug"]
        return f"""<a class="post-card" href="{p['path']}">
  <span class="cover"><img src="/DUMP/assets/covers/{s}-600.webp" srcset="/DUMP/assets/covers/{s}-600.webp 600w, /DUMP/assets/covers/{s}-1200.webp 1200w" sizes="(max-width:640px) calc(100vw - 52px), (max-width:980px) 45vw, 360px" width="600" height="315" loading="lazy" decoding="async" alt="{e(cv['alt'])}"></span>
  <span class="pc"><span class="tag">{e(c['tag'])}</span><h3>{e(c['title'])}</h3><p>{e(c['text'])}</p></span>
</a>"""
    return f"""<a class="{cls}" href="{p['path']}">
  <span class="tag">{e(c['tag'])}</span>
  <h3>{e(c['title'])}</h3>
  <p>{e(c['text'])}</p>
</a>"""

# ---------------------------------------------------------------- sections
def section_html(p, s, counter):
    """One H2 section. Captions and ideas are numbered across the whole page."""
    lang = p["lang"]
    t = T[lang]
    out = [f'<h2 id="{s["id"]}">{e(s["h2"])}</h2>']
    if s.get("lead"):
        out.append(f'<p class="lead-answer">{s["lead"]}</p>')
    if s.get("html"):
        out.append(s["html"])
    if s.get("captions"):
        rows = []
        for c in s["captions"]:
            counter["n"] += 1
            text, note, clang = (c, None, None) if isinstance(c, str) else (c["text"], c.get("note"), c.get("lang"))
            lang_attr = f' lang="{clang}"' if clang else ""
            note_html = f'<small>{e(note)}</small>' if note else ""
            rows.append(f'  <li><span class="n">{counter["n"]}</span><span class="t"><span class="c"{lang_attr}>{e(text)}</span>{note_html}</span>'
                        f'<button class="cap-copy" type="button" hidden data-done="{e(t["copied"])}"><span class="l">{e(t["copy"])}</span>'
                        f'<span class="sr-only"> {e(t["copy_sr"])}: {e(text)}</span></button></li>')
        out.append('<ul class="caps">\n' + "\n".join(rows) + "\n</ul>")
    if s.get("ideas"):
        start = counter["n"] + 1
        rows = []
        for it in s["ideas"]:
            counter["n"] += 1
            rows.append(f'  <li><strong>{e(it["title"])}</strong> — {it["text"]}</li>')
        out.append(f'<ol start="{start}">\n' + "\n".join(rows) + "\n</ol>")
    if s.get("layouts"):
        rows = []
        for it in s["layouts"]:
            counter["n"] += 1
            rows.append(f'  <li>{strip_html(it["strip"], it.get("panels", 3))}<div><strong><span class="n">{counter["n"]}</span>{e(it["title"])}</strong>'
                        f'<p>{it["text"]}</p></div></li>')
        out.append('<ul class="lays">\n' + "\n".join(rows) + "\n</ul>")
    if s.get("steps"):
        out.append('<ol class="steps-num">\n' + "\n".join(f'  <li><b>{e(st["title"])}</b>{st["text"]}</li>' for st in s["steps"]) + "\n</ol>")
    if s.get("after"):
        out.append(s["after"])
    return "\n\n".join(out)

def word_count(p):
    parts = list(p["intro"]) + [q["q"] + " " + q["a"] for q in p["faq"]]
    for s in p["sections"]:
        parts += [s["h2"], s.get("lead", ""), s.get("html", ""), s.get("after", "")]
        parts += [c if isinstance(c, str) else c["text"] for c in s.get("captions", [])]
        parts += [it["title"] + " " + it["text"] for it in s.get("ideas", []) + s.get("layouts", []) + s.get("steps", [])]
    return len(strip_tags(" ".join(parts)).split())

# ---------------------------------------------------------------- head
def head(lang, *, title, desc, path, alt_path, og_path, og_alt, og_type, extra_ld, published, updated, scripts=""):
    t = T[lang]
    url = abs_url(path)
    alts = ""
    if len(alt_path) > 1:
        alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{abs_url(alt_path[l])}">' for l in ("en", "tr") if l in alt_path)
        alts += f'\n<link rel="alternate" hreflang="x-default" href="{abs_url(alt_path.get("en", path))}">'
    other_locale = "".join(f'\n<meta property="og:locale:alternate" content="{T[l]["locale"]}">' for l in alt_path if l != lang)
    article = ""
    if og_type == "article":
        article = (f'\n<meta property="article:published_time" content="{published}">'
                   f'\n<meta property="article:modified_time" content="{updated}">'
                   f'\n<meta property="article:author" content="{SITE}/about/">')
    og_img = abs_url(og_path)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<!-- Generated by DUMP/tools/ideas/build.py. Edit the content file and rebuild; changes made here get overwritten. -->

<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="Gül Eda Aydemir">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<link rel="canonical" href="{url}">
{alts}
<link rel="icon" type="image/png" sizes="32x32" href="/DUMP/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/DUMP/appicon-180.png">
<link rel="manifest" href="/DUMP/site.webmanifest">
<meta name="theme-color" content="#0D0D0D">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="DUMP">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{t['locale']}">{other_locale}
<meta property="og:image" content="{og_img}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(og_alt)}">{article}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{og_img}">
<meta name="twitter:image:alt" content="{e(og_alt)}">

{extra_ld}

<script>document.documentElement.classList.add('js');setTimeout(function(){{var d=document.documentElement;if(!d.classList.contains('js-ready'))d.classList.remove('js')}},3000)</script>
{FONTS}
<link rel="stylesheet" href="/DUMP/assets/dump.css">
<script src="/DUMP/assets/motion.js" defer></script>{scripts}
</head>"""

def author_ld():
    return {"@type": "Person", "@id": f"{SITE}/#person", "name": "Gül Eda Aydemir", "url": f"{SITE}/about/"}

def app_ld():
    return {"@type": "MobileApplication", "@id": f"{SITE}/DUMP/#app", "name": "DUMP: Carousel & Collage",
            "operatingSystem": "iOS 18.6 or later; iPadOS 18.6 or later", "applicationCategory": "MultimediaApplication",
            "url": f"{SITE}/DUMP/", "downloadUrl": f"https://apps.apple.com/app/id{APP_ID}",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}

def breadcrumb_ld(lang, trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(u)} for i, (n, u) in enumerate(trail)]}

# ---------------------------------------------------------------- pages
def cover_html(p):
    """Optional blog header image from tools/covers (DUMP/assets/covers/<slug>-1200.webp)."""
    cv = p.get("cover")
    if not cv:
        return ""
    s = cv["slug"]
    return (f'\n    <figure class="guide-cover"><img src="/DUMP/assets/covers/{s}-1200.webp" srcset="/DUMP/assets/covers/{s}-600.webp 600w, '
            f'/DUMP/assets/covers/{s}-1200.webp 1200w" sizes="(max-width:860px) calc(100vw - 52px), 768px" width="1200" height="630" '
            f'fetchpriority="high" decoding="async" alt="{e(cv["alt"])}"></figure>')

def render_page(p, siblings, alt_path, cfg):
    lang, t = p["lang"], T[p["lang"]]
    link = store_link(cfg, p["campaign"], p.get("product_page"))
    url = abs_url(p["path"])
    og_path = p["path"] + "og.jpg"
    words = word_count(p)
    minutes = max(1, round(words / 220))
    index = t["index"]
    trail = [("DUMP", t["home"]), (index["crumb"], t["ideas"]), (p["crumb"], p["path"])]

    article = {"@context": "https://schema.org", "@type": "Article", "@id": url + "#article",
               "headline": strip_tags(p["h1"]), "description": p["description"], "url": url, "mainEntityOfPage": url,
               "inLanguage": lang, "datePublished": p["published"], "dateModified": p["updated"],
               "image": [abs_url(og_path)], "wordCount": words, "author": author_ld(),
               "publisher": {"@type": "Person", "@id": f"{SITE}/#person", "name": "Gül Eda Aydemir"},
               "isPartOf": {"@type": "WebSite", "name": "DUMP", "url": f"{SITE}/DUMP/"},
               "about": [{"@type": "Thing", "name": p["keyword"]}], "mentions": app_ld()}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "@id": url + "#faq", "url": url, "mainEntity": [
        {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": strip_tags(q["a"])}} for q in p["faq"]]}
    ld = "\n".join(jsonld(x) for x in (article, breadcrumb_ld(lang, trail), faq))
    has_caps = any(s.get("captions") for s in p["sections"])
    scripts = '\n<script src="/DUMP/assets/ideas.js" defer></script>' if has_caps else ""

    secs = p["sections"]
    mid_after = p.get("mid_cta_after") or secs[max(0, len(secs) // 2 - 1)]["id"]
    cta_text = p.get("cta_text") or t["cta_p"]
    counter = {"n": 0}
    body = []
    for s in secs:
        body.append(section_html(p, s, counter))
        if s["id"] == mid_after:
            body.append(cta_card(lang, link, cta_text))
    jump = "\n".join(f'  <a class="chip" href="#{s["id"]}">{e(s.get("short") or s["h2"])}</a>' for s in secs)
    related = [page_card(x) for x in siblings] + [page_card({"path": x["href"], "card": x}) for x in p.get("related", [])]
    status_live = '\n<p class="sr-only" id="copy-status" role="status" aria-live="polite"></p>' if has_caps else ""

    return head(lang, title=p["title"], desc=p["description"], path=p["path"], alt_path=alt_path, og_path=og_path,
                og_alt=p["og"].get("alt") or strip_tags(p["h1"]), og_type="article", extra_ld=ld,
                published=p["published"], updated=p["updated"], scripts=scripts) + f"""
<body data-page="ideas">

{header(lang, alt_path, link)}

<main id="main">

<article>
<header class="guide-hero section-sm" id="top">
  <div class="wrap wrap-doc">
    <p class="crumb"><a href="{t['home']}">DUMP</a> / <a href="{t['ideas']}">{e(index['crumb'])}</a> / {e(p['crumb'])}</p>
    <span class="eyebrow">{e(p['eyebrow'])}</span>
    <h1 class="h1" style="font-size:clamp(30px,5vw,50px);max-width:22ch">{p['h1']}</h1>
    <p class="guide-meta">
      <span>{minutes} {t['min_read']}</span><span>·</span><span>{e(p['card']['tag'])}</span>
    </p>
    <p class="byline">{t['byline']} <a href="/about/">Gül Eda Aydemir</a>, {t['byline_role']} · {t['updated']} <time datetime="{p['updated']}">{fmt_date(p['updated'], lang)}</time></p>{cover_html(p)}
  </div>
</header>

<div class="doc">
  <div class="wrap wrap-doc guide-body">
{chr(10).join('<p>' + x + '</p>' for x in p['intro'])}

{cta_card(lang, link, cta_text)}

<nav class="jump" aria-label="{e(t['jump'])}">
{jump}
</nav>

{chr(10).join(chr(10) + b + chr(10) for b in body)}

{faq_html(lang, p['faq'])}

{cta_end(lang, link, cta_text)}

<h2 id="more">{e(t['more_h'])}</h2>
<div class="related">
{chr(10).join(related)}
</div>
<p class="more-note">{t['more_dump']}</p>{status_live}
  </div>
</div>
</article>

</main>

{footer(lang, link)}
{CF_BEACON}
</body>
</html>
"""

def render_index(lang, pages, alt_path, cfg):
    t = T[lang]
    ix = t["index"]
    path = t["ideas"]
    url = abs_url(path)
    link = store_link(cfg, "web-ideas-index" + ("" if lang == "en" else "-" + lang), "photo_dump")
    og_path = path + "og.jpg"
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "@id": url + "#page", "name": strip_tags(ix["h1"]),
            "description": ix["description"], "url": url, "inLanguage": lang, "isPartOf": {"@type": "WebSite", "name": "DUMP", "url": f"{SITE}/DUMP/"},
            "author": author_ld(), "mainEntity": {"@type": "ItemList", "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": abs_url(p["path"]), "name": p["card"]["title"]} for i, p in enumerate(pages)]}}
    ld = "\n".join(jsonld(x) for x in (coll, breadcrumb_ld(lang, [("DUMP", t["home"]), (ix["crumb"], path)])))
    updated = max(p["updated"] for p in pages)
    cards = "\n".join(page_card(p, "guide-card rv") for p in pages)
    return head(lang, title=ix["title"], desc=ix["description"], path=path, alt_path=alt_path, og_path=og_path,
                og_alt=strip_tags(ix["h1"]), og_type="website", extra_ld=ld, published=updated, updated=updated) + f"""
<body data-page="ideas-index">

{header(lang, alt_path, link)}

<main id="main">

<section class="guide-hero section-sm" id="top">
  <div class="wrap">
    <p class="crumb"><a href="{t['home']}">DUMP</a> / {e(ix['crumb'])}</p>
    <span class="eyebrow">{e(ix['eyebrow'])}</span>
    <h1 class="h1" style="font-size:clamp(32px,5.4vw,54px)">{ix['h1']}</h1>
    <p class="lead">{e(ix['lead'])}</p>
    <p class="tiny" style="margin-top:14px">{ix['count'].format(n=len(pages))} · {t['updated']} <time datetime="{updated}">{fmt_date(updated, lang)}</time></p>
  </div>
</section>

<section class="section-sm" aria-labelledby="ideas-cards" style="padding-top:28px;padding-bottom:28px">
  <div class="wrap">
    <h2 class="h3" id="ideas-cards" style="margin-bottom:18px">{e(ix['cards_h'])}</h2>
    <div class="post-grid">
{cards}
    </div>
  </div>
</section>

<section class="section-sm" style="padding-top:12px">
  <div class="wrap wrap-doc guide-body">
{cta_end(lang, link, t['cta_p'])}
<h2 id="guides">{e(ix['guides_h'])}</h2>
<p>{ix['guides_p']}</p>
  </div>
</section>

</main>

{footer(lang, link)}
{CF_BEACON}
</body>
</html>
"""

# ---------------------------------------------------------------- share images
OG_CSS = """
*{box-sizing:border-box;margin:0}
html,body{width:1200px;height:630px;overflow:hidden;background:#0D0D0D;color:#F5F5F5;font-family:Inter,sans-serif}
body{position:relative}
body::before{content:"";position:absolute;inset:0;background:
 radial-gradient(58% 60% at 88% -10%,rgba(199,153,250,.34),transparent 70%),
 radial-gradient(46% 50% at 0% 0%,rgba(255,55,95,.20),transparent 70%),
 radial-gradient(50% 50% at 60% 115%,rgba(10,132,255,.16),transparent 72%)}
.l{position:absolute;left:72px;top:64px;bottom:60px;width:600px;display:flex;flex-direction:column}
.brand{display:flex;align-items:center;gap:14px;font-family:"Space Grotesk";font-weight:700;font-size:30px;letter-spacing:-.5px}
.brand img{width:52px;height:52px;border-radius:13px;box-shadow:0 0 26px rgba(199,153,250,.5)}
.k{margin-top:auto;font-family:"Space Mono";font-size:19px;letter-spacing:4px;text-transform:uppercase;color:#C799FA}
h1{font-family:"Space Grotesk";font-weight:700;font-size:74px;line-height:1.02;letter-spacing:-2px;margin-top:16px}
.g{background:linear-gradient(120deg,#C799FA,#FF375F);-webkit-background-clip:text;background-clip:text;color:transparent}
.s{margin-top:18px;font-size:24px;color:#B5B5B5}
.u{margin-top:auto;font-family:"Space Mono";font-size:16px;color:#6B6B6B;letter-spacing:.5px}
.r{position:absolute;right:56px;top:0;bottom:0;width:440px;display:flex;align-items:center;justify-content:center}
.cap{display:flex;align-items:center;gap:14px;background:#1A1A1A;border:1px solid #2E2E2E;border-radius:16px;padding:16px 16px 16px 22px;width:420px;margin:9px 0;box-shadow:0 14px 40px rgba(0,0,0,.5)}
.cap span{flex:1;font-size:21px;color:#F5F5F5}
.cap b{font-size:15px;font-weight:600;border:1px solid #383838;border-radius:99px;padding:8px 14px;color:#D2D2D2}
.cap b.on{background:linear-gradient(120deg,#C799FA,#FF375F);color:#12030A;border-color:transparent}
.caps .cap:nth-child(2){transform:translateX(-26px)}
.fan{position:relative;width:420px;height:420px}
.sl{position:absolute;top:50px;width:236px;height:295px;border-radius:22px;border:3px solid #F5F5F5;box-shadow:0 20px 50px rgba(0,0,0,.55);
 display:flex;align-items:flex-end;padding:18px;font-family:"Space Mono";font-size:18px;color:rgba(255,255,255,.85)}
.strip3{position:relative;display:flex;width:450px;height:188px;border-radius:14px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.55);
 background:linear-gradient(180deg,#2B1B4A 0%,#C799FA 52%,#FF375F 100%)}
.strip3 .sea{position:absolute;left:0;right:0;bottom:0;height:34%;background:linear-gradient(180deg,rgba(10,132,255,.55),#120C1E)}
.strip3 .sun{position:absolute;left:186px;top:58px;width:78px;height:78px;border-radius:50%;background:#FFD27A;box-shadow:0 0 50px rgba(255,210,122,.7)}
.strip3 i{position:absolute;top:0;bottom:0;border-left:3px dashed rgba(255,255,255,.75)}
.under{display:flex;gap:10px;margin-top:22px}
.under b{width:144px;height:180px;border-radius:12px;border:2px solid #383838}
.pfan{position:relative;flex:none;width:480px;height:540px}
.pfan .p{position:absolute;border-radius:18px;border:3px solid #F5F5F5;background:#1A1A1A center/cover no-repeat;box-shadow:0 22px 50px rgba(0,0,0,.6)}
.pfan .p.front{box-shadow:0 0 0 1px rgba(255,55,95,.4),0 0 44px rgba(255,55,95,.45),0 26px 60px rgba(0,0,0,.65)}
.pfan .cap{position:absolute;width:auto;margin:0;padding:12px 12px 12px 18px;border-radius:14px;background:rgba(26,26,26,.94)}
.pfan .cap span{font-size:20px;white-space:nowrap}
.pfan .cap b{font-size:14px;padding:7px 13px}
"""

def og_photo_fan(og):
    """Three of the user's own photos as a fanned dump, with two caption pills. Paths are relative to tools/ideas/."""
    files = [os.path.join(TOOLS, f) for f in og["photos"][:3]]
    for f in files:
        if not os.path.exists(f):
            sys.exit(f"share image photo not found: {os.path.relpath(f, DUMP)}")
    # The photos' bytes go into the page as a comment, so replacing a photo re-renders the image.
    stamp = "".join(hashlib.sha1(open(f, "rb").read()).hexdigest()[:12] for f in files)
    url = lambda i: "file://" + files[i]
    caps = og.get("samples", [])
    return f"""<div class="pfan"><!-- {stamp} -->
<div class="p" style="left:0;top:78px;width:200px;height:250px;transform:rotate(-8deg);background-image:url('{url(1)}')"></div>
<div class="p" style="right:-12px;top:64px;width:200px;height:250px;transform:rotate(7deg);background-image:url('{url(2)}')"></div>
<div class="p front" style="left:110px;top:96px;width:260px;height:325px;transform:rotate(-1.5deg);background-image:url('{url(0)}')"></div>
<div class="cap" style="left:14px;top:14px"><span>{e(caps[1])}</span><b>{e(og['copy'])}</b></div>
<div class="cap" style="right:20px;top:404px"><span>{e(caps[0])}</span><b class="on">{e(og['copied'])}</b></div>
</div>"""

def og_art(art, og):
    if art == "captions" and og.get("photos"):
        return og_photo_fan(og)
    if art == "captions":
        rows = og.get("samples", [])[:3]
        return '<div class="caps">' + "".join(
            f'<div class="cap"><span>{e(r)}</span><b class="{"on" if i == 1 else ""}">{e(og["copied"] if i == 1 else og["copy"])}</b></div>'
            for i, r in enumerate(rows)) + "</div>"
    if art == "carousel":
        return ('<div><div class="strip3"><div class="sea"></div><div class="sun"></div><i style="left:150px"></i><i style="left:300px"></i></div>'
                '<div class="under"><b style="background:linear-gradient(180deg,#2B1B4A,#C799FA 60%,#FF375F)"></b>'
                '<b style="background:linear-gradient(180deg,#3A245F,#D98AD8 60%,#FF375F)"></b><b style="background:linear-gradient(180deg,#2B1B4A,#C799FA 60%,#FF6A5F)"></b></div></div>')
    colours = ["linear-gradient(150deg,#FF9F0A,#FF375F)", "linear-gradient(150deg,#0A84FF,#C799FA)",
               "linear-gradient(150deg,#30D158,#0A84FF)", "linear-gradient(150deg,#C799FA,#FF375F)"]
    labels = og.get("labels", ["01", "02", "03", "04"])
    slides = "".join(f'<div class="sl" style="left:{40 + i * 46}px;transform:rotate({-12 + i * 8}deg);background:{c}">{e(labels[i])}</div>'
                     for i, c in enumerate(colours))
    return f'<div class="fan">{slides}</div>'

def og_page_html(og, lang):
    icon = "file://" + os.path.join(DUMP, "appicon.png")
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{FONTS}<style>{OG_CSS}</style></head><body>
<div class="l">
  <div class="brand"><img src="{icon}" alt="">DUMP</div>
  <div class="k">{e(og['kicker'])}</div>
  <h1>{e(og['title'])} <span class="g">{e(og['accent'])}</span></h1>
  <div class="s">{e(og['sub'])}</div>
  <div class="u">guledaaydemir.github.io/DUMP</div>
</div>
<div class="r">{og_art(og.get('art', 'ideas'), og)}</div>
</body></html>"""

def render_og(jobs, force):
    """jobs: [(og dict, lang, output path)]. Skips images whose inputs did not change."""
    cache_file = os.path.join(TOOLS, "og-cache.json")
    cache = json.load(open(cache_file)) if os.path.exists(cache_file) else {}
    todo = []
    for og, lang, out in jobs:
        doc = og_page_html(og, lang)
        digest = hashlib.sha1(doc.encode()).hexdigest()
        rel = os.path.relpath(out, DUMP)
        if force or cache.get(rel) != digest or not os.path.exists(out):
            todo.append((doc, out, rel, digest))
    if not todo:
        return 0
    if not os.path.exists(CHROME):
        print(f"! Google Chrome not found at {CHROME}: {len(todo)} share image(s) not rendered")
        return 0
    from PIL import Image
    tmp = tempfile.mkdtemp(prefix="dump-og-")
    try:
        for doc, out, rel, digest in todo:
            src, png = os.path.join(tmp, "og.html"), os.path.join(tmp, "og.png")
            with open(src, "w", encoding="utf-8") as fh:
                fh.write(doc)
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                            "--allow-file-access-from-files", f"--user-data-dir={os.path.join(tmp, 'profile')}",
                            "--window-size=1200,630", "--virtual-time-budget=8000", f"--screenshot={png}", "file://" + src],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
            img = Image.open(png).convert("RGB")
            if img.size != (1200, 630):
                img = img.crop((0, 0, 1200, 630))
            os.makedirs(os.path.dirname(out), exist_ok=True)
            img.save(out, "JPEG", quality=86, optimize=True, progressive=True)
            cache[rel] = digest
            print(f"  og  {rel}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    with open(cache_file, "w") as fh:
        json.dump(dict(sorted(cache.items())), fh, indent=1)
        fh.write("\n")
    return len(todo)

# ---------------------------------------------------------------- sitemap and llms.txt blocks
def replace_block(file, start, end, block, anchor, lead=""):
    """Swap the text between two marker lines; insert it before `anchor` the first time."""
    with open(file, encoding="utf-8") as fh:
        text = fh.read()
    new = f"{start}\n{block}\n{end}"
    if start in text:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), lambda m: new, text, flags=re.S)
    else:
        i = text.rindex(anchor) if anchor else len(text)
        text = text[:i] + lead + new + "\n" + text[i:]
    with open(file, "w", encoding="utf-8") as fh:
        fh.write(text)

def sitemap_block(groups):
    out = []
    for g in groups:
        for lang, (path, updated, og_title) in sorted(g.items()):
            alts = ""
            if len(g) > 1:
                alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(g[l][0])}"/>' for l in sorted(g))
                alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(g.get("en", g[lang])[0])}"/>'
            out.append(f"""  <url>
    <loc>{abs_url(path)}</loc>
    <lastmod>{updated}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>{alts}
    <image:image><image:loc>{abs_url(path)}og.jpg</image:loc><image:title>{e(og_title, quote=False)}</image:title></image:image>
  </url>""")
    return "\n".join(out)

def llms_block(pages):
    lines = ["## Ideas pages (free captions and ideas to copy; generated from DUMP/tools/ideas/)",
             f"- [Ideas index]({abs_url(T['en']['ideas'])}): every ideas page in one list. Turkish: {abs_url(T['tr']['ideas'])}"]
    for p in sorted((p for p in pages if p["lang"] == "en"), key=lambda p: p.get("order", 99)):
        tr = next((q for q in pages if q["key"] == p["key"] and q["lang"] == "tr"), None)
        lines.append(f"- [{p['card']['title']}]({abs_url(p['path'])}): {p['description']}"
                     + (f" Turkish version: {abs_url(tr['path'])}" if tr else ""))
    return "\n".join(lines)

# ---------------------------------------------------------------- main
def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"  page {os.path.relpath(path, DUMP)}")

def main():
    args = set(sys.argv[1:])
    with open(os.path.join(TOOLS, "config.json"), encoding="utf-8") as fh:
        cfg = json.load(fh)
    pages = load_pages()
    problems, warnings = validate(pages)
    for w in warnings:
        print("! " + w)
    if problems:
        sys.exit("Content problems:\n  " + "\n  ".join(problems))
    if "--check" in args:
        print(f"{len(pages)} content files OK")
        return

    by_key = {}
    for p in pages:
        by_key.setdefault(p["key"], {})[p["lang"]] = p
    og_jobs, groups = [], []
    for p in pages:
        alt_path = {l: q["path"] for l, q in by_key[p["key"]].items()}
        siblings = sorted((q for q in pages if q["lang"] == p["lang"] and q is not p), key=lambda q: q.get("order", 99))
        write(os.path.join(DUMP, p["path"][len("/DUMP/"):], "index.html"), render_page(p, siblings, alt_path, cfg))
        og = dict(p["og"], copy=T[p["lang"]]["copy"], copied=T[p["lang"]]["copied"])
        og_jobs.append((og, p["lang"], os.path.join(DUMP, p["path"][len("/DUMP/"):], "og.jpg")))
    for key, variants in by_key.items():
        groups.append({l: (q["path"], q["updated"], strip_tags(q["h1"])) for l, q in variants.items()})

    langs = sorted({p["lang"] for p in pages})
    index_paths = {l: T[l]["ideas"] for l in langs}
    for lang in langs:
        mine = sorted((p for p in pages if p["lang"] == lang), key=lambda p: p.get("order", 99))
        write(os.path.join(DUMP, T[lang]["ideas"][len("/DUMP/"):], "index.html"), render_index(lang, mine, index_paths, cfg))
        og_jobs.append((T[lang]["index"]["og"], lang, os.path.join(DUMP, T[lang]["ideas"][len("/DUMP/"):], "og.jpg")))
    groups.insert(0, {l: (T[l]["ideas"], max(p["updated"] for p in pages if p["lang"] == l), strip_tags(T[l]["index"]["h1"])) for l in langs})

    replace_block(os.path.join(DUMP, "sitemap.xml"), "  <!-- ideas:start (generated by DUMP/tools/ideas/build.py) -->",
                  "  <!-- ideas:end -->", sitemap_block(groups), "</urlset>")
    replace_block(os.path.join(DUMP, "llms.txt"), "<!-- ideas:start (generated by DUMP/tools/ideas/build.py) -->",
                  "<!-- ideas:end -->", llms_block(pages), "\n## Legal", lead="\n")
    print("  sitemap.xml and llms.txt blocks updated")
    n = render_og(og_jobs, "--force-og" in args)
    print(f"{len(pages)} pages + {len(langs)} indexes built, {n} share image(s) rendered")

    missing = []
    if unfilled(cfg.get("provider_token")):
        missing.append("provider_token")
    used = {p.get("product_page") for p in pages if p.get("product_page")}
    missing += [f"product_pages.{k}" for k in sorted(used) if unfilled((cfg.get("product_pages") or {}).get(k))]
    if missing:
        print("! Still placeholders in config.json (left out of the App Store links): " + ", ".join(missing))

if __name__ == "__main__":
    main()
