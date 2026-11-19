# MULA guide files

One guide = one Python file in this folder, `<guide-id>.py`, holding a single dict `GUIDE`.
`../build.py` turns every file into three pages:

- EN `/MULA/guides/<en slug>/`
- TR `/MULA/tr/rehber/<tr slug>/`
- ES `/MULA/es/guias/<es slug>/`

Never hand-edit the generated HTML; edit the guide file and run `python3 -I MULA/_src/build.py`.
Read `../FACTS.md` first: it is the only source of truth about the app.

```python
GUIDE = {
    "id": "when-to-water",          # = file name without .py; used by {{link:...}} tokens
    "order": 2,                     # position on the guides index (1 = first)
    "category": "care",             # app | care | seasons | light
    "shot": "soil",                 # screenshot key shown beside the headline (see list below)
    "art": "monstera",              # plant artwork for the guide card and social card (see list below)
    "updated": "2026-11-18",
    "en": {
        "slug": "how-often-to-water-houseplants",  # ascii, lowercase, hyphens, no language prefix
        "title": "…",          # <title> and social title, <= 60 characters, main keyword first
        "description": "…",    # meta description, 140-160 characters, plain text
        "h1": "…",             # the visible headline (may be longer than the title)
        "kicker": "…",         # 2-4 words over the h1, e.g. "Watering"
        "answer": "…",         # 2-3 plain sentences that answer the page's main question directly.
                               # Shown first in a box; written so an AI assistant can quote it as is.
        "takeaways": ["…"],    # 3-5 short key points (plain text)
        "body": """<h2>…</h2><p>…</p>""",   # HTML, see rules below
        "faq": [("question?", "answer"), …],  # 3-5 pairs, plain-text answers (become FAQPage schema)
        "sources": [("Publisher (year). Title.", "https://…"), …],  # may be []
    },
    "tr": { … same keys … },
    "es": { … same keys … },
}
```

Use Python string literals carefully: triple-quoted strings for `body`; use typographic apostrophes (’) or
double quotes inside single-line strings so nothing breaks. The file must import with
`python3 -I -c "import runpy; runpy.run_path('<file>')"` without errors.

## Body HTML

Allowed tags: `h2 h3 p ul ol li strong em a blockquote table thead tbody tr th td`.
No inline styles, classes, scripts or `<img>`. Start with an `h2` (the page has its own h1).
Put every token below on its own line, outside `<p>`.

| Token | Becomes |
| --- | --- |
| `[[shot:KEY\|caption]]` | a real MULA screenshot in a phone frame, with a caption (avoid image names with words ad blockers filter, such as "identify", "track", "ad") |
| `[[art:KEY\|caption]]` | a MULA plant poster (photo above, cut-paper portrait below), with a caption |
| `[[tip\|text]]` | a "MULA tip" note on paper with a small sprout (text may contain `<strong>`, `<em>`, `<a>`) |
| `[[checklist\|item one;;item two;;item three]]` | a checklist readers can tick (3-12 items, plain text) |
| `[[cta]]` | the App Store download box (use exactly once, near the end) |
| `{{link:ID}}` | URL of that page in the same language. ID = a guide id, or `home`, `about`, `faq`, `support`, `privacy`, `guides`, `demo` |

Example: `<p>Set it up in the <a href="{{link:quick-start}}">quick-start guide</a>.</p>`

Guide ids that exist: `quick-start`, `when-to-water`, `overwatering-signs`, `seasonal-care`, `light-guide`,
`vacation-care`, `frost-heat-balcony`, `widgets-watch-siri`, `choose-app`. Link to 2-4 of the others where it
helps the reader.

## Screenshot keys (real screens, English app UI, sample garden Momo, Tsubaki, Nori, Ajisai, Ran, Mame)

- `today` — Today: monstera hero, "Today · Autumn", "Care for Your Plants", Emergency Care card "Momo has
  waited 7 days for water.", Upcoming Tasks: Watering Momo (7 days late), Mame (3 days late), Nori (today).
- `soil` — the soil check sheet: "How does Momo's soil feel?" with Dry · I watered it / A little moist / Wet.
- `garden` — My Garden: the six plants as cards with their pictures.
- `plant` — a plant page (Momo, Monstera deliciosa): photo hero, where it lives, light, this season's plan.
- `seasons` — Seasonal care editor: spring/summer/autumn/winter, water every N days, feed every N days,
  temperature range, "Follow the seasons automatically".
- `addplant` — Add a plant: name, species search, where it lives (Indoor/Balcony/Outdoor), light.
- `whatplant` — "Not sure what it is?" result: "Looks like: Orchid".
- `lightmeter` — the light meter: "About 2,400 lux · an estimate", Bright, indirect, plants that would like it.
- `weather` — Today with a weather alert line "Cold Night Ahead" for the balcony plants.
- `vacation` — Vacation Mode: dates, "Who is helping?", "Share the care sheet".
- `settings` — Settings: reminders (Remind me at, Quiet hours, Sound), appearance, etc.
- `premium` — MULA Premium screen: "A little more room to grow." Annual with 1-week free trial, Lifetime.
- `widgets` — MULA widgets (small, medium with Dry/Moist/Wet, large, Lock Screen).
- `watch` — the Apple Watch app listing plants that need care.
- `poster` — a plant poster: photo above, paper portrait below.

## Art keys (for `art` and `[[art:…]]`)

`camellia`, `monstera`, `ficus`, `hydrangea`, `orchid`, `pilea` — each a vertical poster: a real-looking
photo of the plant above and MULA's cut-paper geometric portrait of it below.

## Writing rules

- Each language is written natively for its readers, not translated word for word. Same facts, same
  structure (same h2 sections, same faq count) in all three. Spanish: neutral Spanish, "tú". Turkish:
  natural, warm, "sen" form, correct Turkish characters (ç ğ ı İ ö ş ü).
- The app's interface is in **English** only. In EN, quote the English labels in bold or quotes (e.g.
  **Today**, "A little moist"). In TR and ES, keep the English label exactly as it appears in the app, in
  quotes, and add a short translation in parentheses the first time, e.g. TR: “Dry · I watered it” (Kuru ·
  suladım), ES: “A little moist” (un poco húmeda). Never pretend the app shows Turkish or Spanish text.
- Product facts must match `../FACTS.md`; never invent features, prices, trial lengths other than the
  1-week trial, numbers, reviews or awards. Be clear about Free vs Premium where it matters. Never call the
  app "the best"; let the facts speak.
- Plant-care claims: practical, general and hedged ("most", "usually", "check the label"). No pesticide or
  chemical dosing advice. Cite only sources you have opened and confirmed (publisher, title, URL) — prefer
  RHS (rhs.org.uk), university extension services (e.g. University of Minnesota Extension, NC State
  Extension, UF/IFAS, Clemson HGIC, Penn State Extension, Missouri Botanical Garden), ASPCA for pet-toxic
  plants, Apple Support for iPhone features. No invented statistics. `sources` may be empty when the guide
  is purely about using the app.
- Answer-first: the `answer` field and the first paragraph answer the question in the title. Write for
  people asking a search engine or an AI assistant (e.g. "how often should I water my monstera",
  "app that reminds me to water plants", "how to keep plants alive on vacation").
- 900-1,300 words of body per language. Short paragraphs, descriptive h2s phrased like real searches,
  at least one `[[shot:…]]`, one `[[tip|…]]`, optionally one `[[art:…]]` and one `[[checklist|…]]`, and
  `[[cta]]` once.
- Tone: calm, warm, unhurried, a little poetic but always practical — like the app. No exclamation marks,
  no guilt ("you killed your plant"), no hype.
