# HANE guide files

One guide = one Python file in this folder, `<guide-id>.py`, holding a single dict `GUIDE`.
`../build.py` turns every file into three pages:

- EN `/HANE/guides/<en slug>/`
- TR `/HANE/tr/rehber/<tr slug>/`
- ES `/HANE/es/guias/<es slug>/`

Never hand-edit the generated HTML; edit the guide file and run `python3 HANE/_src/build.py`.

```python
GUIDE = {
    "id": "micro-breaks",            # file name without .py; used by {{link:...}} tokens
    "order": 1,                      # position on the guides index (1 = first)
    "category": "productivity",      # productivity | culture | game
    "hero": "intro_serve",           # image key (see list below) shown at the top
    "updated": "2026-11-16",
    "en": {
        "slug": "can-a-game-break-make-you-more-productive",   # ascii, lowercase, hyphens
        "title": "…",          # <title> and social title, <= 60 characters, keyword first
        "description": "…",    # meta description, 140-160 characters, plain text
        "h1": "…",             # the visible headline (may be longer than the title)
        "kicker": "…",         # 2-4 words over the h1, e.g. "Productivity"
        "answer": "…",         # 2-3 plain sentences that answer the page's main question directly.
                               # Shown first in a box; written so an AI assistant can quote it as is.
        "takeaways": ["…"],    # 3-5 short key points (plain text)
        "body": """<h2>…</h2><p>…</p>""",   # HTML, see rules below
        "faq": [("question?", "answer"), …],  # 3-5 pairs, plain text answers (become FAQPage schema)
        "sources": [("Author A, Author B (2022). Title. Journal 17(3).", "https://doi.org/…"), …],  # may be []
    },
    "tr": { … same keys … },
    "es": { … same keys … },
}
```

## Body HTML

Allowed tags: `h2 h3 p ul ol li strong em a blockquote table thead tbody tr th td`.
No inline styles, classes, scripts or images as tags. Start with an `h2` (the page has its own h1).

Tokens the build replaces:

| Token | Becomes |
| --- | --- |
| `[[fig:KEY\|caption]]` | a framed illustration with a caption (own paragraph line) |
| `[[shot:KEY\|caption]]` | a real game screenshot in a phone frame with a caption |
| `[[tip\|text]]` | a parchment "Usta's tip" callout (text may contain `<strong>`, `<em>`, `<a>`) |
| `[[cta]]` | the App Store download box (use once, near the end) |
| `{{link:ID}}` | URL of that page in the same language. ID = a guide id, or `home`, `story`, `faq`, `support`, `privacy`, `guides`, `demo` |

Example: `<p>Read <a href="{{link:kiraathane}}">what a kıraathane is</a>.</p>`

## Image keys

Illustrations (painted, from the game): `welcome` (usta and çırak greeting with open arms), `dream`
(çırak daydreaming of a red car), `market` (market stall), `opening` (tea-house door with red ribbon),
`quarrel` (two regulars arguing over a game), `cat` (cat on a table), `inspection` (zabıta officer with the
usta), `intro_goal` (çırak carrying a tray of tea through a full, happy room, coins flying),
`intro_order` (regular ordering, tea bubble), `intro_serve` (usta hands çırak a tray of tea),
`intro_bill` (çırak wiping a table), `intro_games` (regulars playing okey, çırak brings a tavla board),
`intro_incidents` (two regulars arguing, a ginger cat walking in, rain at the window, çırak startled),
`map` (map of Türkiye).

Screenshots (real game screens, localized): `room` (the tea house floor), `cat` (Tekir came in: choices),
`map` (branches on the map), `quarrel` (quarrel choices), `ribbon` (opening ribbon), `ribbon_cut`, `dream`
(Çırağın Hayali page: kumbara road to the car), `staff` (Kadro: çırak level, usta, waiters), `welcome`
(title screen), `upgrades` (Geliştir screen), `games` (table games screen).

## Writing rules

- Each language is written natively for its readers, not translated word for word. Same facts, same
  structure (same h2 sections, same faq count) in all three.
- Turkish words stay Turkish in every language (çırak, usta, kıraathane, kumbara, çaydanlık, tavşan kanı,
  okey, tavla, 52'lik, zabıta), explained once in EN/ES.
- Game facts must match the fact sheet given to you; never invent features, prices, numbers or reviews.
- Research claims: cite only sources you have confirmed exist (author, year, venue, DOI/URL). No invented
  statistics. Hedge where the evidence is mixed. No medical or personalised financial advice.
- Answer-first: the `answer` field and the first paragraph answer the question in the title.
- 1,000-1,600 words of body per language. Short paragraphs, descriptive h2s phrased like real searches.
