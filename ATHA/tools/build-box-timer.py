#!/usr/bin/env python3
"""ATHA box breathing timer: builds every page the timer appears on.

Writes, from one template and one set of strings per language:
  box-breathing-timer/index.html          English tool page
  box-breathing-timer/embed.html          English iframe version (noindex)
  tr/kutu-nefesi-zamanlayici/index.html   Turkish tool page
  tr/kutu-nefesi-zamanlayici/embed.html   Turkish iframe version (noindex)
  index.html, tr/index.html               the "Try it now" section, between
                                          <!-- box-timer:home:start/end -->

The site header and footer of the tool pages are kept from the files already
on disk, so nav or footer edits made by hand survive a rebuild.
Behaviour lives in assets/js/box-timer.js, styles in atha.css section 27.

Run from the ATHA folder:  python3 tools/build-box-timer.py
Then, if a page date changed: node tools/build-sitemap.mjs
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://guledaaydemir.github.io'
# Bump these whenever atha.css or box-timer.js change, or browsers keep the old copy.
CSS = '/ATHA/assets/css/atha.css?v=5'
JS = '/ATHA/assets/js/box-timer.js?v=5'
UPDATED = '2026-10-29'
PUBLISHED = {'en': '2026-10-28', 'tr': '2026-10-29'}
BEACON = ("<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' "
          "data-cf-beacon='{\"token\": \"0d4a3a7a679a46d1b1ff35a88bd52782\"}'></script><!-- End Cloudflare Web Analytics -->")

# Rounded square, 280 x 280 with 36 px corners, starting halfway round the
# bottom-left corner and running clockwise: each side is exactly a quarter.
TRACK = ('M30.544 289.456A36 36 0 0 1 20 264V56A36 36 0 0 1 56 20H264A36 36 0 0 1 300 56'
         'V264A36 36 0 0 1 264 300H56A36 36 0 0 1 30.544 289.456Z')

PATTERNS = [('3,3,3,3', '3 s', '3 sn'), ('4,4,4,4', '4 s', '4 sn'), ('5,5,5,5', '5 s', '5 sn'),
            ('6,6,6,6', '6 s', '6 sn'), ('4,0,4,0', 'No holds', 'Tutuşsuz')]
LENGTHS = [('60', '1'), ('120', '2'), ('180', '3'), ('300', '5'), ('600', '10'), ('0', '∞')]

STORE_ICON = ('<svg class="atha-store__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3.5v10.5m0 0-4.2-4.2M12 14l4.2-4.2M5 16.5v3h14v-3" '
              'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

T = {
  'en': dict(
    lang='en', locale='en_US', alt_locale='tr_TR',
    url=SITE + '/ATHA/box-breathing-timer/', path='box-breathing-timer/',
    embed_url=SITE + '/ATHA/box-breathing-timer/embed.html',
    store='https://apps.apple.com/app/id6807887691', store_small='Download on the', store_aria='Download ATHA on the App Store',
    home=SITE + '/ATHA/', home_path='/ATHA/', hub_path='/ATHA/meditations/', hub_name='Breathing techniques',
    guide_path='/ATHA/practices/box-breathing.html',
    og_image=SITE + '/ATHA/assets/img/og/og-box-breathing.jpg',
    title='Box Breathing Timer Online: Free 4-4-4-4 Exercise | ATHA',
    description='Free online box breathing timer. Follow the animated square: breathe in 4, hold 4, out 4, hold 4. Pick 3 to 6 seconds and 1 to 10 minutes. No download, no sign-up.',
    og_title='Box breathing timer: free, online, 4-4-4-4',
    og_description='Follow the animated square: in 4, hold 4, out 4, hold 4. A free breathing exercise timer that runs in your browser.',
    og_alt='Box breathing: in 4, hold 4, out 4, hold 4. A free timer by ATHA',
    crumb='Box breathing timer',
    badge='Free · online · no download',
    h1='Box breathing timer',
    sub='Breathe in 4, hold 4, breathe out 4, hold 4. Press Start and follow the square. It’s free and runs right here in your browser.',
    aria='Box breathing timer',
    phase0='Box breathing · 4-4-4-4', status0='In 4 · hold 4 · out 4 · hold 4',
    sides=['In', 'Hold', 'Out', 'Hold'], sec='s',
    start='Start', reset='Reset', full='Full screen',
    per_side='Seconds per side', minutes='Minutes', no_limit='No limit', tones='Soft tones', vibration='Vibration',
    done_title='Do this in one tap with the app.',
    done_text='<span data-bt-done-count>8 boxes</span> done. ATHA’s Box Breathing traces the same square and taps every corner on iPhone and Apple Watch.',
    nojs='Seconds per side: 4 in · 4 hold · 4 out · 4 hold. The square breathes at that pace; turn on JavaScript for the countdown and settings.',
    note='<span class="atha-boxtimer__kbd">Space starts and pauses · </span>Runs in your browser, nothing is saved',
    credit='<a href="{url}" target="_blank" rel="noopener">Box breathing timer</a> by <a href="{home}" target="_blank" rel="noopener">ATHA</a> · nothing is saved',
    embed_title='Box breathing timer by ATHA', embed_desc='Embeddable 4-4-4-4 box breathing timer by ATHA.',
    cta_source='box-timer', home_source='home-try',
  ),
  'tr': dict(
    lang='tr', locale='tr_TR', alt_locale='en_US',
    url=SITE + '/ATHA/tr/kutu-nefesi-zamanlayici/', path='tr/kutu-nefesi-zamanlayici/',
    embed_url=SITE + '/ATHA/tr/kutu-nefesi-zamanlayici/embed.html',
    store='https://apps.apple.com/tr/app/id6807887691', store_small='Ücretsiz indir', store_aria='ATHA’yı App Store’dan ücretsiz indir',
    home=SITE + '/ATHA/tr/', home_path='/ATHA/tr/', hub_path='/ATHA/tr/rehber/', hub_name='Rehberler',
    guide_path='/ATHA/tr/rehber/kutu-nefesi.html',
    og_image=SITE + '/ATHA/assets/img/og/og-tr-kutu-nefesi.jpg',
    title='Kutu Nefesi Zamanlayıcı Online: Ücretsiz 4-4-4-4 Egzersiz | ATHA',
    description='Ücretsiz online kutu nefesi zamanlayıcı. Hareketli kareyi takip et: 4 al, 4 tut, 4 ver, 4 boş tut. 3-6 saniye ve 1-10 dakika seç. İndirme yok, üyelik yok.',
    og_title='Kutu nefesi zamanlayıcı: ücretsiz, online, 4-4-4-4',
    og_description='Hareketli kareyi takip et: 4 al, 4 tut, 4 ver, 4 boş tut. Tarayıcında çalışan ücretsiz nefes egzersizi zamanlayıcısı.',
    og_alt='Kutu nefesi: 4 saniye al, 4 tut, 4 ver, 4 boş tut. ATHA’dan ücretsiz zamanlayıcı',
    crumb='Kutu nefesi zamanlayıcı',
    badge='Ücretsiz · online · indirme yok',
    h1='Kutu nefesi zamanlayıcı',
    sub='4 saniye al, 4 tut, 4 ver, 4 boş tut. Başlat’a bas ve kareyi takip et. Ücretsiz, doğrudan tarayıcında çalışır.',
    aria='Kutu nefesi zamanlayıcı',
    phase0='Kutu nefesi · 4-4-4-4', status0='4 al · 4 tut · 4 ver · 4 boş tut',
    sides=['Al', 'Tut', 'Ver', 'Boş tut'], sec='sn',
    start='Başlat', reset='Sıfırla', full='Tam ekran',
    per_side='Kenar başına saniye', minutes='Dakika', no_limit='Süresiz', tones='Yumuşak sesler', vibration='Titreşim',
    done_title='Bunu uygulamada tek dokunuşla yap.',
    done_text='<span data-bt-done-count>8 kutu</span> tamam. ATHA’nın Kutu Nefesi aynı kareyi çizer ve iPhone ile Apple Watch’ta her köşede titreşir.',
    nojs='Kenar süreleri: 4 sn al · 4 sn tut · 4 sn ver · 4 sn boş tut. Kare bu ritimle nefes alır; geri sayım ve ayarlar için JavaScript’i aç.',
    note='<span class="atha-boxtimer__kbd">Boşluk tuşu başlatır ve duraklatır · </span>Tarayıcında çalışır, hiçbir şey kaydedilmez',
    credit='<a href="{url}" target="_blank" rel="noopener">Kutu nefesi zamanlayıcı</a>, <a href="{home}" target="_blank" rel="noopener">ATHA</a> · hiçbir şey kaydedilmez',
    embed_title='Kutu nefesi zamanlayıcı, ATHA', embed_desc='ATHA’nın sitene ekleyebileceğin 4-4-4-4 kutu nefesi zamanlayıcısı.',
    cta_source='kutu-zamanlayici-tr', home_source='home-tr-try',
  ),
}


def esc(text):
    """Escape for HTML text; keeps markup we put in on purpose out of here."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def store_badge(t, source, extra=''):
    return (f'<a class="atha-store" href="{t["store"]}" data-atha-store="{source}" aria-label="{t["store_aria"]}"{extra}>{STORE_ICON}'
            f'<span class="atha-store__text"><span class="atha-store__small">{t["store_small"]}</span><span class="atha-store__big">App Store</span></span></a>')


def qr(t, big=False, title=None, text=None):
    en = t['lang'] == 'en'
    alt = 'QR code that opens ATHA on the App Store' if en else 'ATHA’yı App Store’da açan QR kod'
    title = title or ('On a computer?' if en else 'Bilgisayardan mı bakıyorsun?')
    text = text or ('Scan with your iPhone camera to open the App Store.' if en else 'iPhone kameranla tara, App Store’da açılsın.')
    size = 104 if big else 76
    cls = 'atha-qr atha-qr--lg' if big else 'atha-qr'
    return (f'<div class="{cls}"><img src="/ATHA/assets/img/qr-appstore-atha.svg" width="{size}" height="{size}" alt="{alt}" loading="lazy" decoding="async" />'
            f'<p><strong>{title}</strong>{text}</p></div>')


def timer(t, variant):
    """The card. variant: page | embed | home."""
    attrs = 'data-box-timer'
    if variant != 'page':
        attrs += ' data-no-url'
    if variant == 'embed':
        attrs += f' data-share-url="{t["url"]}"'
    tag = 'section' if variant == 'page' else 'div'
    role = '' if variant == 'page' else ' role="region"'
    done_extra = ' target="_blank" rel="noopener"' if variant == 'embed' else ''
    source = {'page': t['cta_source'] + '-done', 'embed': t['cta_source'] + '-embed-done', 'home': t['home_source'] + '-done'}[variant]

    segs = '\n'.join(
        f'            <li class="atha-boxtimer__seg" style="flex-grow:4"><span class="atha-boxtimer__segbar"><span class="atha-boxtimer__segfill"></span></span>'
        f'<span class="atha-boxtimer__seglabel">{esc(side)} <span class="atha-boxtimer__segsec">4 {t["sec"]}</span></span></li>'
        for side in t['sides'])
    pats = ''.join(
        f'<label class="atha-seg__opt{" atha-seg__opt--wide" if value == "4,0,4,0" else ""}"><input type="radio" name="bt-pattern" value="{value}"'
        f'{" checked" if value == "4,4,4,4" else ""} /><span>{en if t["lang"] == "en" else tr}</span></label>'
        for value, en, tr in PATTERNS)
    lens = ''.join(
        f'<label class="atha-seg__opt"><input type="radio" name="bt-length" value="{value}"{" checked" if value == "120" else ""} />'
        + (f'<span aria-hidden="true">{label}</span><span class="atha-visually-hidden">{t["no_limit"]}</span>' if value == '0' else f'<span>{label}</span>')
        + '</label>'
        for value, label in LENGTHS)
    foot = (f'<p class="atha-embed__credit">{t["credit"].format(url=t["url"], home=t["home"])}</p>' if variant == 'embed'
            else f'<p class="atha-boxtimer__note">{t["note"]}</p>')

    return f'''<{tag} class="atha-boxtimer" {attrs}{role} aria-label="{t["aria"]}">
    <button type="button" class="atha-boxtimer__iconbtn" data-bt-focus aria-pressed="false" aria-label="{t["full"]}" title="{t["full"]}"><svg class="is-enter" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><svg class="is-exit" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
    <div class="atha-boxtimer__layout">
      <div class="atha-boxtimer__stage">
        <svg class="atha-boxtimer__svg" viewBox="0 0 320 320" aria-hidden="true" focusable="false">
          <defs>
            <linearGradient id="atha-bt-stroke" x1="0" y1="1" x2="1" y2="0">
              <stop offset="0" stop-color="#ffc09b" />
              <stop offset=".5" stop-color="#e994d6" />
              <stop offset="1" stop-color="#a48aff" />
            </linearGradient>
            <linearGradient id="atha-bt-fill" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stop-color="#7c5cff" />
              <stop offset=".55" stop-color="#c56fd0" />
              <stop offset="1" stop-color="#f08e7f" />
            </linearGradient>
            <linearGradient id="atha-bt-sheen" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#fff" stop-opacity=".26" />
              <stop offset=".5" stop-color="#fff" stop-opacity="0" />
            </linearGradient>
            <filter id="atha-bt-blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22" /></filter>
          </defs>
          <g class="atha-boxtimer__orb" data-bt-orb>
            <rect class="atha-boxtimer__orb-glow" x="60" y="60" width="200" height="200" rx="56" />
            <rect class="atha-boxtimer__orb-body" x="60" y="60" width="200" height="200" rx="56" />
            <rect class="atha-boxtimer__orb-sheen" x="60" y="60" width="200" height="200" rx="56" />
            <rect class="atha-boxtimer__orb-edge" x="60.5" y="60.5" width="199" height="199" rx="55.5" />
          </g>
          <path class="atha-boxtimer__track" data-bt-track d="{TRACK}" />
          <path class="atha-boxtimer__progress" data-bt-progress d="{TRACK}" pathLength="100" stroke-dasharray="0 100" />
          <circle class="atha-boxtimer__dot" data-bt-dot cx="30.54" cy="289.46" r="6" />
        </svg>
        <button type="button" class="atha-boxtimer__stagebtn" data-bt-stage tabindex="-1" aria-hidden="true"></button>
        <div class="atha-boxtimer__center" aria-hidden="true">
          <p class="atha-boxtimer__count" data-bt-count></p>
          <svg class="atha-boxtimer__glyph atha-boxtimer__glyph--play" viewBox="0 0 24 24" focusable="false"><path d="M8 5.6v12.8a1 1 0 0 0 1.53.85l10.1-6.4a1 1 0 0 0 0-1.7L9.53 4.75A1 1 0 0 0 8 5.6z" fill="currentColor" /></svg>
          <svg class="atha-boxtimer__glyph atha-boxtimer__glyph--check" viewBox="0 0 24 24" focusable="false"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" /></svg>
        </div>
      </div>
      <div class="atha-boxtimer__panel">
        <div>
          <p class="atha-boxtimer__phase" data-bt-phase aria-live="polite">{t["phase0"]}</p>
          <p class="atha-boxtimer__status" data-bt-status>{t["status0"]}</p>
        </div>
        <ol class="atha-boxtimer__timeline" data-bt-timeline aria-hidden="true">
{segs}
        </ol>
        <div class="atha-boxtimer__controls" data-bt-controls hidden>
          <div class="atha-boxtimer__actions">
            <button type="button" class="atha-btbtn atha-btbtn--secondary" data-bt-reset hidden>{t["reset"]}</button>
            <button type="button" class="atha-btbtn atha-btbtn--primary" data-bt-toggle aria-pressed="false">{t["start"]}</button>
          </div>
          <div class="atha-boxtimer__done" data-bt-done role="status" hidden>
            <img src="/ATHA/appicon-128.webp" width="56" height="56" alt="" loading="lazy" decoding="async" />
            <div>
              <p class="atha-boxtimer__done-title">{t["done_title"]}</p>
              <p class="atha-boxtimer__done-text">{t["done_text"]}</p>
            </div>
            {store_badge(t, source, done_extra)}
          </div>
          <div class="atha-boxtimer__settings">
            <div class="atha-boxtimer__row atha-boxtimer__row--stack">
              <span class="atha-boxtimer__rowlabel" aria-hidden="true">{t["per_side"]}</span>
              <fieldset class="atha-seg" data-bt-patterns><legend>{t["per_side"]}</legend><span class="atha-seg__thumb" aria-hidden="true"></span>{pats}</fieldset>
            </div>
            <div class="atha-boxtimer__row atha-boxtimer__row--stack">
              <span class="atha-boxtimer__rowlabel" aria-hidden="true">{t["minutes"]}</span>
              <fieldset class="atha-seg" data-bt-lengths><legend>{t["minutes"]}</legend><span class="atha-seg__thumb" aria-hidden="true"></span>{lens}</fieldset>
            </div>
            <label class="atha-boxtimer__row"><span>{t["tones"]}</span><input type="checkbox" role="switch" class="atha-switch" data-bt-sound /></label>
            <label class="atha-boxtimer__row" data-bt-vibrate-row hidden><span>{t["vibration"]}</span><input type="checkbox" role="switch" class="atha-switch" data-bt-vibrate /></label>
          </div>
        </div>
        <p class="atha-boxtimer__nojs">{t["nojs"]}</p>
        {foot}
      </div>
    </div>
  </{tag}>'''


def mini_square(side):
    """A 40 x 40 square icon with one side lit (0 left, 1 top, 2 right, 3 bottom)."""
    lit = ['M6 30V10', 'M10 6H30', 'M34 10V30', 'M30 34H10'][side]
    return (f'<svg viewBox="0 0 40 40" aria-hidden="true" focusable="false"><rect class="bs-frame" x="6" y="6" width="28" height="28" rx="7" />'
            f'<path class="bs-side" d="{lit}" /></svg>')


# ---------------------------------------------------------------------------
# Page copy (body sections and FAQ) per language
# ---------------------------------------------------------------------------

COPY = {
  'en': dict(
    what_h='What is box breathing?',
    what_p='Box breathing, also called <strong>square breathing</strong> or <strong>4-4-4-4 breathing</strong>, is a slow breathing exercise with four equal steps: breathe in for 4 seconds, hold for 4, breathe out for 4 and hold for 4. One round is a 16-second &#8220;box&#8221;. People use it to feel calm but alert: before a meeting, an exam or a difficult conversation.',
    steps=[('Breathe in', '4 seconds, through your nose. The dot climbs the left side.'),
           ('Hold', '4 seconds, shoulders soft. The dot crosses the top.'),
           ('Breathe out', '4 seconds, slow and even. The dot runs down the right side.'),
           ('Hold', '4 seconds, empty and still. The dot comes home along the bottom.')],
    how_h='How to use this online box breathing timer',
    how=[('Pick seconds per side', '4 is the classic. Choose 3 if 4 feels long, 5 or 6 once it feels easy, or <em>No holds</em> if holding your breath makes you uneasy.'),
         ('Pick the minutes', '2 minutes is a good start. The timer rounds to whole boxes, so it never stops halfway through a side.'),
         ('Press Start, then breathe out fully', 'You get three seconds to empty your lungs before the first box begins.'),
         ('Follow the square', 'Breathe in as the inner square grows, hold while it waits, breathe out as it shrinks. The number counts down each side.')],
    how_after='Want to close your eyes? Turn on <em>Soft tones</em>: each side has its own pitch. The full-screen button in the corner hides everything but the square.',
    long_h='How long should you do box breathing?',
    long_p='Three or four boxes, about a minute, while you learn. After that, 2 to 5 minutes is plenty.',
    table=('Box sizes and how long they take', ['Seconds per side', 'One box', 'Boxes in 2 min', 'Breaths a minute'],
           [['3-3-3-3', '12 s', '10', '5'], ['4-4-4-4', '16 s', '8 (2:08)', '3.75'], ['5-5-5-5', '20 s', '6', '3'],
            ['6-6-6-6', '24 s', '5', '2.5'], ['4-4, no holds', '8 s', '15', '7.5']]),
    guide='New to it? Read <a href="/ATHA/practices/box-breathing.html">how to do box breathing, step by step</a>: when it beats a long exhale and who should skip the holds.',
    app_label='Box breathing app for iPhone &amp; Apple Watch',
    app_title='Do this in one tap with the app.',
    app_p='The web timer needs you to watch the screen. ATHA, a free box breathing app, doesn&#8217;t: it taps every corner of the box with a gentle haptic, so you can close your eyes, lock your phone in your pocket or follow it on your wrist.',
    app_list=['Haptic taps for every phase, on iPhone and Apple Watch', 'Eyes-closed view that dims the screen', 'Free, nothing locked, no account, Data Not Collected'],
    app_shot_alt='ATHA Box Breathing session on iPhone: a rounded square, the word Inhale and a timeline of four 4-second phases',
    share_h='Share it or put it on your site',
    share_p='Your settings live in the address bar, so a link opens the timer exactly as you set it, for example 5 seconds a side for 3 minutes.',
    share_copy='Copy link to these settings', share_btn='Share',
    embed_p='Teachers, coaches, clinics and bloggers are welcome to embed the timer. Paste this where you want it to appear:',
    embed_label='Embed code for the box breathing timer', embed_copy='Copy embed code',
    embed_link_text='Box breathing timer', embed_by=' by ATHA', iframe_title='Box breathing timer',
    faq_h='Common questions',
    faq=[('Is this box breathing timer free?', 'Yes. There&#8217;s no sign-up and nothing to install. The timer runs in your browser, and your sessions are not saved or sent anywhere.'),
         ('Is box breathing the same as square breathing?', 'Yes. Box breathing, square breathing, 4-4-4-4 breathing and tactical breathing usually mean the same equal four-part pattern: in, hold, out, hold.'),
         ('What count should I use for box breathing?', 'Start with 4 seconds a side. If that feels long, use 3; if it feels easy, try 5 or 6. Keep the four sides equal and never strain. If the holds make you uncomfortable, use the no-hold version.'),
         ('How long should I do box breathing?', 'Three or four boxes, about a minute at 4-4-4-4, while you learn, as <a href="https://health.clevelandclinic.org/box-breathing-benefits" rel="noopener">Cleveland Clinic</a> suggests. After that, 2 to 5 minutes is plenty. The timer always ends on a complete box.'),
         ('Can I use the timer with my eyes closed?', 'Turn on <em>Soft tones</em>: each side of the box has its own pitch, so you can follow it without looking. On Android phones you can also turn on <em>Vibration</em>. For haptic taps on an iPhone or your wrist, use the free ATHA app.'),
         ('Does the timer keep running if my phone locks?', 'While a session runs, the timer asks the browser to keep the screen on. If you switch apps or the tab is hidden, it pauses, and <em>Resume</em> carries on where you left off.'),
         ('Is there a box breathing app?', 'Yes. ATHA is a free box breathing app for iPhone, iPad and Apple Watch. It guides the same 4-4-4-4 box with haptic taps, keeps going on your wrist and has no account, ads or in-app purchases.'),
         ('Can I put this box breathing timer on my website?', 'Yes. Copy the <a href="#share">embed code</a> above and paste it into your site. It&#8217;s free for blogs, classrooms, clinics and newsletters.')],
    disclaimer='This timer is a breathing aid, not a medical device, and this page is not medical advice. Stop if you feel dizzy or unwell, never practise breath holds in water, and talk to a doctor before doing breath holds if you have a heart or lung condition or are pregnant.',
    related_h='Keep reading',
    related=[('/ATHA/practices/box-breathing.html', 'Box breathing: how to do it, step by step', 'The exact method, how long to keep going, when it beats a long exhale, and who should skip the holds.', 'Technique &middot; 6 min'),
             ('/ATHA/guides/calm-nerves-before-presentation.html', 'How to calm nerves before a presentation', 'A 10-minute countdown for talks, interviews and big meetings: box breathing at T-10, one long exhale at T-0.', 'Calm &middot; 6 min'),
             ('/ATHA/meditations/', 'Ten breathing techniques, with exact timings', 'Box, 4-7-8, coherence, extended exhale and more: what each one is for and how long to do it.', 'Techniques')],
    cta_h='Do this in one tap with the app.',
    cta_p='Box Breathing in ATHA taps every corner, on your iPhone or your wrist, so you never have to watch a screen. Free, with nothing locked.',
    home_kicker='Try it now', home_h='Try box breathing right now.',
    home_p='No download for this one. Press Start and follow the square: in up the left side, hold across the top, out down the right, hold along the bottom.',
    home_more='Open the full-screen timer &rarr;',
    home_end_p='ATHA&#8217;s Box Breathing traces the same square and taps every corner on iPhone and Apple Watch, so you can close your eyes. Free, nothing locked, no account.',
    home_qr_title='Scan to download', home_qr_text='Point your iPhone camera here to open ATHA on the App Store.',
  ),
  'tr': dict(
    what_h='Kutu nefesi nedir?',
    what_p='Kutu nefesi, <strong>kare nefes</strong> ya da <strong>4-4-4-4 nefes</strong> olarak da bilinir: dört eşit adımlı yavaş bir nefes egzersizidir. 4 saniye nefes al, 4 tut, 4 ver ve 4 boş tut. Bir tur 16 saniyelik bir &#8220;kutu&#8221;dur. Sakin ama uyanık hissetmek için kullanılır: toplantıdan, sınavdan ya da zor bir konuşmadan önce.',
    steps=[('Nefes al', '4 saniye, burnundan. Nokta sol kenardan yukarı çıkar.'),
           ('Tut', '4 saniye, omuzlar gevşek. Nokta üst kenarı geçer.'),
           ('Nefes ver', '4 saniye, yavaş ve düzgün. Nokta sağ kenardan iner.'),
           ('Boş tut', '4 saniye, boş ve sakin. Nokta alt kenardan başa döner.')],
    how_h='Bu online kutu nefesi zamanlayıcı nasıl kullanılır?',
    how=[('Kenar başına saniyeyi seç', 'Klasik olan 4. Uzun geliyorsa 3, kolaylaşınca 5 ya da 6; nefes tutmak seni geriyorsa <em>Tutuşsuz</em>.'),
         ('Dakikayı seç', '2 dakika iyi bir başlangıç. Zamanlayıcı süreyi tam kutulara yuvarlar, bir kenarın ortasında kesilmez.'),
         ('Başlat&#8217;a bas, nefesini tamamen ver', 'İlk kutu başlamadan önce ciğerlerini boşaltmak için üç saniyen var.'),
         ('Kareyi takip et', 'İçteki kare büyürken nefes al, beklerken tut, küçülürken ver. Sayı her kenarı geri sayar.')],
    how_after='Gözlerini kapatmak mı istiyorsun? <em>Yumuşak sesler</em>&#8217;i aç: her kenarın kendi tonu var. Köşedeki tam ekran düğmesi kare dışındaki her şeyi gizler.',
    long_h='Kutu nefesi ne kadar yapılmalı?',
    long_p='Öğrenirken üç dört kutu, yaklaşık bir dakika. Sonrasında 2 ile 5 dakika fazlasıyla yeterli.',
    table=('Kutu boyları ve süreleri', ['Kenar başına saniye', 'Bir kutu', '2 dk&#8217;da kutu', 'Dakikada nefes'],
           [['3-3-3-3', '12 sn', '10', '5'], ['4-4-4-4', '16 sn', '8 (2:08)', '3,75'], ['5-5-5-5', '20 sn', '6', '3'],
            ['6-6-6-6', '24 sn', '5', '2,5'], ['4-4, tutuşsuz', '8 sn', '15', '7,5']]),
    guide='Yeni mi başlıyorsun? <a href="/ATHA/tr/rehber/kutu-nefesi.html">Kutu nefesi adım adım nasıl yapılır</a>: kaç tur yapılır, sınav öncesi nasıl kullanılır, kimler tutuşları atlamalı.',
    app_label='iPhone ve Apple Watch için kutu nefesi uygulaması',
    app_title='Bunu uygulamada tek dokunuşla yap.',
    app_p='Web zamanlayıcısında ekrana bakman gerekir. Ücretsiz kutu nefesi uygulaması ATHA&#8217;da gerekmez: kutunun her köşesinde hafifçe titreşir; gözlerini kapatabilir, telefonu cebinde tutabilir ya da bileğinden takip edebilirsin.',
    app_list=['iPhone ve Apple Watch&#8217;ta her aşamada titreşim', 'Ekranı karartan Gözler kapalı görünümü', 'Ücretsiz, kilitli bir şey yok, hesap yok, Veriler Toplanmaz'],
    app_shot_alt='iPhone&#8217;da ATHA Kutu Nefesi seansı (İngilizce arayüz): yuvarlatılmış bir kare, Inhale yazısı ve dört 4 saniyelik aşama',
    share_h='Paylaş ya da kendi sitene ekle',
    share_p='Ayarların adres çubuğunda durur; böylece bir bağlantı zamanlayıcıyı tam senin ayarladığın gibi açar, örneğin 3 dakika boyunca kenar başına 5 saniye.',
    share_copy='Bu ayarların bağlantısını kopyala', share_btn='Paylaş',
    embed_p='Öğretmenler, koçlar, klinikler ve blog yazarları zamanlayıcıyı sitelerine ekleyebilir. Görünmesini istediğin yere şunu yapıştır:',
    embed_label='Kutu nefesi zamanlayıcı için yerleştirme kodu', embed_copy='Yerleştirme kodunu kopyala',
    embed_link_text='Kutu nefesi zamanlayıcı', embed_by=', ATHA', iframe_title='Kutu nefesi zamanlayıcı',
    faq_h='Sık sorulan sorular',
    faq=[('Bu kutu nefesi zamanlayıcı ücretsiz mi?', 'Evet. Üyelik yok, kurulacak bir şey yok. Zamanlayıcı tarayıcında çalışır; seansların hiçbir yere kaydedilmez ya da gönderilmez.'),
         ('Kutu nefesi ile kare nefes aynı şey mi?', 'Evet. Kutu nefesi, kare nefes ve 4-4-4-4 nefes genellikle aynı dört eşit adımlı kalıbı anlatır: al, tut, ver, tut.'),
         ('Kutu nefesinde kaç saniye kullanmalıyım?', 'Kenar başına 4 saniyeyle başla. Uzun geliyorsa 3, kolay geliyorsa 5 ya da 6 dene. Dört kenarı eşit tut ve zorlama. Tutuşlar seni geriyorsa tutuşsuz sürümü kullan.'),
         ('Kutu nefesi ne kadar sürmeli?', 'Öğrenirken üç dört kutu yeter; 4-4-4-4 ile yaklaşık bir dakika. <a href="https://health.clevelandclinic.org/box-breathing-benefits" rel="noopener" hreflang="en">Cleveland Clinic</a> de böyle öneriyor. Sonrasında 2 ile 5 dakika fazlasıyla yeterli. Zamanlayıcı her zaman tam bir kutuyla biter.'),
         ('Zamanlayıcıyı gözlerim kapalıyken kullanabilir miyim?', '<em>Yumuşak sesler</em>&#8217;i aç: kutunun her kenarının kendi tonu var, bakmadan takip edebilirsin. Android telefonlarda <em>Titreşim</em>&#8217;i de açabilirsin. iPhone&#8217;da ya da bileğinde titreşimle takip etmek için ücretsiz ATHA uygulamasını kullan.'),
         ('Telefon kilitlenirse zamanlayıcı çalışmaya devam eder mi?', 'Seans sürerken zamanlayıcı tarayıcıdan ekranı açık tutmasını ister. Başka bir uygulamaya geçersen ya da sekme gizlenirse duraklar; <em>Devam et</em> ile kaldığın yerden sürer.'),
         ('Kutu nefesi uygulaması var mı?', 'Evet. ATHA; iPhone, iPad ve Apple Watch için ücretsiz bir kutu nefesi uygulaması. Aynı 4-4-4-4 kutuyu titreşimle yönlendirir, bileğinde de devam eder; hesap, reklam ya da uygulama içi satın alma yok.'),
         ('Bu zamanlayıcıyı kendi siteme ekleyebilir miyim?', 'Evet. Yukarıdaki <a href="#share">yerleştirme kodunu</a> kopyala ve sitene yapıştır. Bloglar, sınıflar, klinikler ve bültenler için ücretsiz.')],
    disclaimer='Bu zamanlayıcı bir nefes yardımcısıdır; tıbbi bir cihaz değildir ve bu sayfa tıbbi tavsiye değildir. Başın dönerse ya da kendini kötü hissedersen dur, nefes tutma alıştırmalarını asla suda yapma; kalp ya da akciğer rahatsızlığın varsa veya hamileysen nefes tutmadan önce bir hekime danış.',
    related_h='Okumaya devam et',
    related=[('/ATHA/tr/rehber/kutu-nefesi.html', 'Kutu nefesi nasıl yapılır? (4-4-4-4)', '4 al, 4 tut, 4 ver, 4 boş tut. Kaç tur yapılır, sınav ve sunum öncesi nasıl kullanılır, kimler tutuşları atlamalı.', 'Teknik &middot; 7 dk'),
             ('/ATHA/tr/rehber/4-7-8-nefes-teknigi.html', '4-7-8 nefes tekniği nasıl yapılır?', '4 al, 7 tut, 8 ver. Bir tur 19 saniye; 4 turla başla. Tur hesabı, baş dönmesine yol açan hatalar ve ücretsiz zamanlayıcı.', 'Uyku &middot; 6 dk'),
             ('/ATHA/tr/rehber/uyuyamiyorum.html', 'Uyuyamıyorum, ne yapmalıyım?', 'Saate bakma, telefonu bırak: 4 saniye al, 6&#8211;8 saniye ver. 20 dakika kuralı, gece uyanmaları ve ne zaman hekime gitmeli.', 'Uyku &middot; 7 dk')],
    cta_h='Bunu uygulamada tek dokunuşla yap.',
    cta_p='ATHA&#8217;daki Kutu Nefesi her köşede titreşir, iPhone&#8217;unda ya da bileğinde; ekrana bakman gerekmez. Ücretsiz, hiçbir şey kilitli değil.',
    home_kicker='Hemen dene', home_h='Kutu nefesini şimdi dene.',
    home_p='Bunun için indirme yok. Başlat&#8217;a bas ve kareyi takip et: sol kenardan yukarı al, üstte tut, sağdan aşağı ver, altta boş tut.',
    home_more='Tam ekran zamanlayıcıyı aç &rarr;',
    home_end_p='ATHA&#8217;nın Kutu Nefesi aynı kareyi çizer ve iPhone ile Apple Watch&#8217;ta her köşede titreşir; gözlerini kapatabilirsin. Ücretsiz, kilitli bir şey yok, hesap yok.',
    home_qr_title='Tara ve indir', home_qr_text='iPhone kameranı buraya tut, ATHA App Store&#8217;da açılsın.',
  ),
}


def strip_tags(html):
    text = re.sub(r'<[^>]+>', '', html)
    return (text.replace('&#8217;', '’').replace('&#8220;', '“').replace('&#8221;', '”')
                .replace('&amp;', '&').replace('&middot;', '·').replace('&rarr;', '→'))


def json_ld(lang):
    t, c = T[lang], COPY[lang]
    other = T['tr' if lang == 'en' else 'en']
    en = lang == 'en'
    person = {
        '@type': 'Person', '@id': SITE + '/#person', 'name': 'Gül Eda Aydemir', 'alternateName': 'Gul Eda Aydemir',
        'jobTitle': 'Independent iOS developer' if en else 'Bağımsız iOS geliştirici',
        'url': SITE + '/about/', 'email': 'mailto:solostaseraofficial@gmail.com',
        'sameAs': ['https://apps.apple.com/us/developer/gul-eda-aydemir/id1889159460', 'https://instagram.com/solo.stasera'],
    }
    graph = [
        {
            '@type': 'WebApplication', '@id': t['url'] + '#tool',
            'name': 'Box Breathing Timer' if en else 'Kutu Nefesi Zamanlayıcı',
            'alternateName': (['Online box breathing timer', 'Square breathing timer', '4-4-4-4 breathing timer', 'Box breathing exercise online']
                              if en else ['Online kutu nefesi zamanlayıcı', 'Kare nefes zamanlayıcı', '4-4-4-4 nefes zamanlayıcı']),
            'description': strip_tags(t['description']),
            'url': t['url'], 'applicationCategory': 'HealthApplication',
            'operatingSystem': 'Any (runs in a web browser)' if en else 'Hepsi (web tarayıcısında çalışır)',
            'browserRequirements': 'Requires JavaScript' if en else 'JavaScript gerekir',
            'isAccessibleForFree': True, 'inLanguage': lang,
            'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD' if en else 'TRY'},
            'featureList': (['Animated square: one lap is one box', '3, 4, 5 or 6 seconds per side, or no holds',
                             '1, 2, 3, 5 or 10 minutes, or no time limit', 'Optional soft tones for each side',
                             'Full screen and keyboard control (Space starts and pauses)', 'Nothing saved or sent']
                            if en else ['Hareketli kare: bir tur bir kutu', 'Kenar başına 3, 4, 5 ya da 6 saniye veya tutuşsuz',
                                        '1, 2, 3, 5 ya da 10 dakika veya süresiz', 'Her kenar için isteğe bağlı yumuşak sesler',
                                        'Tam ekran ve klavye kontrolü (boşluk tuşu başlatır ve duraklatır)', 'Hiçbir şey kaydedilmez ya da gönderilmez']),
            'workTranslation' if en else 'translationOfWork': {'@id': other['url'] + '#tool'},
            'author': {'@id': SITE + '/#person'}, 'publisher': {'@id': SITE + '/#person'},
            'isPartOf': {'@id': SITE + '/ATHA/#website'}, 'mentions': {'@id': SITE + '/ATHA/#app'},
            'datePublished': PUBLISHED[lang], 'dateModified': UPDATED,
        },
        {
            '@type': 'WebPage', '@id': t['url'] + '#webpage', 'url': t['url'], 'name': t['title'],
            'isPartOf': {'@id': SITE + '/ATHA/#website'}, 'mainEntity': {'@id': t['url'] + '#tool'}, 'inLanguage': lang,
            'breadcrumb': {'@id': t['url'] + '#breadcrumb'},
            'primaryImageOfPage': {'@type': 'ImageObject', 'url': t['og_image'], 'width': 1200, 'height': 630},
        },
        {
            '@type': 'BreadcrumbList', '@id': t['url'] + '#breadcrumb',
            'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'ATHA', 'item': t['home']},
                {'@type': 'ListItem', 'position': 2, 'name': t['hub_name'], 'item': SITE + t['hub_path']},
                {'@type': 'ListItem', 'position': 3, 'name': t['crumb']},
            ],
        },
        {
            '@type': 'FAQPage', '@id': t['url'] + '#faq',
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in c['faq']],
        },
        person,
    ]
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=2)


def head(lang):
    t = T[lang]
    en_t, tr_t = T['en'], T['tr']
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{t["title"]}</title>
  <meta name="description" content="{t["description"]}" />
  <link rel="canonical" href="{t["url"]}" />
  <link rel="alternate" hreflang="en" href="{en_t["url"]}" />
  <link rel="alternate" hreflang="tr" href="{tr_t["url"]}" />
  <link rel="alternate" hreflang="x-default" href="{en_t["url"]}" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <meta name="theme-color" content="#070914" />
  <meta name="color-scheme" content="dark" />
  <meta name="author" content="Gül Eda Aydemir" />
  <meta name="apple-itunes-app" content="app-id=6807887691" />
  <link rel="icon" href="/ATHA/favicon-32.png" sizes="32x32" type="image/png" />
  <link rel="apple-touch-icon" href="/ATHA/appicon-180.png" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="ATHA" />
  <meta property="og:locale" content="{t["locale"]}" />
  <meta property="og:locale:alternate" content="{t["alt_locale"]}" />
  <meta property="og:title" content="{t["og_title"]}" />
  <meta property="og:description" content="{t["og_description"]}" />
  <meta property="og:url" content="{t["url"]}" />
  <meta property="og:image" content="{t["og_image"]}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="{t["og_alt"]}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{t["og_title"]}" />
  <meta name="twitter:description" content="{t["og_description"]}" />
  <meta name="twitter:image" content="{t["og_image"]}" />
  <meta name="twitter:image:alt" content="{t["og_alt"]}" />
  <link rel="stylesheet" href="{CSS}" />
  <script type="application/ld+json">
{json_ld(lang)}
  </script>
</head>'''


def block(src, start_pat, end_tag):
    i = src.index(start_pat)
    j = src.index(end_tag, i) + len(end_tag)
    return src[i:j]


def page(lang):
    t, c = T[lang], COPY[lang]
    out = ROOT / t['path'] / 'index.html'
    old = out.read_text(encoding='utf-8')
    header = block(old, '<header class="atha-header">', '</header>')
    footer = block(old, '<footer class="atha-footer">', '</footer>')
    en = lang == 'en'

    steps = '\n'.join(f'        <li>{mini_square(i)}<strong>{h}</strong>{p}</li>' for i, (h, p) in enumerate(c['steps']))
    how = '\n'.join(f'        <li><strong>{h}</strong>{p}</li>' for h, p in c['how'])
    cap, cols, rows = c['table']
    thead = ''.join(f'<th scope="col">{x}</th>' for x in cols)
    tbody = '\n'.join('            <tr>' + ''.join((f'<td class="atha-nowrap">{v}</td>' if k == 0 else f'<td>{v}</td>') for k, v in enumerate(r)) + '</tr>' for r in rows)
    faq = '\n'.join(f'''        <details>
          <summary>{q}</summary>
          <div class="atha-faq__answer"><p>{a}</p></div>
        </details>''' for q, a in c['faq'])
    related = '\n'.join(f'        <li><a class="atha-listitem" href="{href}"><div class="atha-listitem__body"><p class="atha-listitem__title">{title}</p>'
                        f'<p class="atha-listitem__text">{text}</p></div><div class="atha-listitem__aside"><span class="atha-card__meta">{meta}</span></div></a></li>'
                        for href, title, text, meta in c['related'])
    app_list = ''.join(f'<li>{x}</li>' for x in c['app_list'])
    embed_code = (f'&lt;iframe src="{t["embed_url"]}" title="{c["iframe_title"]}" width="100%" height="920" style="border:0;max-width:480px;border-radius:28px" loading="lazy"&gt;&lt;/iframe&gt;\n'
                  f'&lt;p&gt;&lt;a href="{t["url"]}"&gt;{c["embed_link_text"]}&lt;/a&gt;{c["embed_by"]}&lt;/p&gt;')
    shot = ('<figure class="atha-phone atha-phone--sm"><img src="/ATHA/assets/img/screens/session-box-600.webp" srcset="/ATHA/assets/img/screens/session-box-600.webp 600w, '
            '/ATHA/assets/img/screens/session-box-1206.webp 1206w" sizes="200px" width="600" height="1304" '
            f'alt="{c["app_shot_alt"]}" loading="lazy" decoding="async" /></figure>')
    skip = 'Skip to content' if en else 'İçeriğe geç'

    html = f'''{head(lang)}
<body data-atha-cta-source="{t["cta_source"]}-sticky">

<a class="atha-skip" href="#atha-main">{skip}</a>
{header}

<main id="atha-main" class="atha-main atha-main--tool atha-container">

  <ol class="atha-breadcrumb">
    <li><a href="{t["home_path"]}">ATHA</a></li>
    <li><a href="{t["hub_path"]}">{t["hub_name"]}</a></li>
    <li aria-current="page">{t["crumb"]}</li>
  </ol>

  <header class="atha-toolhero">
    <p class="atha-toolhero__badge">{t["badge"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="atha-toolhero__sub">{t["sub"]}</p>
  </header>

  {timer(t, "page")}

  <article class="atha-article" style="margin-top:var(--atha-s-8)">
    <div class="atha-article__body">

      <h2 id="what">{c["what_h"]}</h2>
      <p>{c["what_p"]}</p>
      <ol class="atha-boxsteps">
{steps}
      </ol>

      <h2 id="how">{c["how_h"]}</h2>
      <ol class="atha-steps">
{how}
      </ol>
      <p>{c["how_after"]}</p>

      <h2 id="how-long">{c["long_h"]}</h2>
      <p>{c["long_p"]}</p>
      <div class="atha-tablewrap">
        <table class="atha-pattern atha-pattern--fit">
          <caption>{cap}</caption>
          <thead>
            <tr>{thead}</tr>
          </thead>
          <tbody>
{tbody}
          </tbody>
        </table>
      </div>
      <p>{c["guide"]}</p>

      <section class="atha-appcard" aria-labelledby="app-title">
        <div>
          <img class="atha-appcard__icon" src="/ATHA/appicon-128.webp" width="64" height="64" alt="" loading="lazy" decoding="async" />
          <p class="atha-trycard__label">{c["app_label"]}</p>
          <h2 class="atha-appcard__title" id="app-title">{c["app_title"]}</h2>
          <p>{c["app_p"]}</p>
          <ul>{app_list}</ul>
          <div class="atha-getrow">{store_badge(t, t["cta_source"] + "-app")}{qr(t)}</div>
        </div>
        {shot}
      </section>

      <h2 id="share">{c["share_h"]}</h2>
      <p>{c["share_p"]}</p>
      <div class="atha-share">
        <button type="button" class="atha-btn atha-btn--ghost" data-bt-copy>{c["share_copy"]}</button>
        <button type="button" class="atha-btn atha-btn--ghost" data-bt-share hidden>{c["share_btn"]}</button>
        <span class="atha-share__status" data-bt-share-status role="status"></span>
      </div>
      <p>{c["embed_p"]}</p>
      <label class="atha-visually-hidden" for="atha-embed-code">{c["embed_label"]}</label>
      <textarea class="atha-embedcode" id="atha-embed-code" data-bt-embed-code readonly spellcheck="false">{embed_code}</textarea>
      <div class="atha-share"><button type="button" class="atha-btn atha-btn--ghost" data-bt-copy-embed>{c["embed_copy"]}</button></div>

      <h2 id="faq">{c["faq_h"]}</h2>
      <div class="atha-faq">
{faq}
      </div>

      <p class="atha-disclaimer">{c["disclaimer"]}</p>
    </div>

    <hr class="atha-aurora-rule" />

    <section aria-labelledby="atha-related-heading">
      <h2 id="atha-related-heading">{c["related_h"]}</h2>
      <ul class="atha-related">
{related}
      </ul>
    </section>

  </article>

  <section class="atha-panel atha-ctaband">
    <div class="atha-aura atha-aura--sm" style="margin:0 auto var(--atha-s-5)" aria-hidden="true"></div>
    <h2>{c["cta_h"]}</h2>
    <p>{c["cta_p"]}</p>
    <div class="atha-getrow atha-getrow--center">{store_badge(t, t["cta_source"] + "-footer")}{qr(t)}</div>
  </section>

</main>

{footer}

<script src="/ATHA/assets/js/atha.js" defer></script>
<script src="/ATHA/assets/js/cta.js" defer></script>
<script src="{JS}" defer></script>
{BEACON}
</body>
</html>
'''
    out.write_text(html, encoding='utf-8')
    return out


def embed(lang):
    t = T[lang]
    out = ROOT / t['path'] / 'embed.html'
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t["embed_title"]}</title>
  <meta name="description" content="{t["embed_desc"]}" />
  <link rel="canonical" href="{t["url"]}" />
  <meta name="robots" content="noindex, follow" />
  <meta name="color-scheme" content="dark" />
  <link rel="icon" href="/ATHA/favicon-32.png" sizes="32x32" type="image/png" />
  <link rel="stylesheet" href="{CSS}" />
</head>
<body class="atha-embed">
  {timer(t, "embed")}

<script src="{JS}" defer></script>
{BEACON}
</body>
</html>
'''
    out.write_text(html, encoding='utf-8')
    return out


def home_section(lang):
    t, c = T[lang], COPY[lang]
    tool_path = '/ATHA/' + t['path']
    return f'''  <!-- box-timer:home:start (generated by tools/build-box-timer.py) -->
  <section class="atha-section atha-tryhome" id="try-now" aria-labelledby="try-title">
    <div class="atha-tryhome__head">
      <p class="atha-kicker">{c["home_kicker"]}</p>
      <h2 id="try-title">{c["home_h"]}</h2>
      <p class="atha-lead">{c["home_p"]} <a href="{tool_path}">{c["home_more"]}</a></p>
    </div>
  {timer(t, "home")}
    <div class="atha-tryhome__end">
      <img class="atha-tryhome__end-icon" src="/ATHA/appicon-128.webp" width="64" height="64" alt="" loading="lazy" decoding="async" />
      <div class="atha-tryhome__end-copy">
        <p class="atha-tryhome__end-title">{c["cta_h"]}</p>
        <p>{c["home_end_p"]}</p>
      </div>
      <div class="atha-getrow">{store_badge(t, t["home_source"])}{qr(t, True, c["home_qr_title"], c["home_qr_text"])}</div>
    </div>
  </section>
  <!-- box-timer:home:end -->
'''


def home(lang):
    path = ROOT / ('index.html' if lang == 'en' else 'tr/index.html')
    src = path.read_text(encoding='utf-8')
    start, end = '  <!-- box-timer:home:start', '  <!-- box-timer:home:end -->\n'
    if start not in src:
        raise SystemExit(f'{path}: add the box-timer:home:start/end markers first')
    i = src.index(start)
    j = src.index(end) + len(end)
    src = src[:i] + home_section(lang) + src[j:]
    src = re.sub(r'/ATHA/assets/css/atha\.css\?v=\d+', CSS, src)
    if '/ATHA/assets/js/box-timer.js' in src:
        src = re.sub(r'/ATHA/assets/js/box-timer\.js(\?v=\d+)?', JS, src)
    else:
        src = src.replace('<script src="/ATHA/assets/js/cta.js" defer></script>\n',
                          f'<script src="/ATHA/assets/js/cta.js" defer></script>\n<script src="{JS}" defer></script>\n', 1)
    path.write_text(src, encoding='utf-8')
    return path


if __name__ == '__main__':
    for lang in ('en', 'tr'):
        for fn in (page, embed, home):
            print('wrote', fn(lang).relative_to(ROOT))
