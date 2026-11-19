# PETO guide files

One guide = one Python file in this folder, `<guide-id>.py` (hyphens allowed in the file name), holding a
single dict `GUIDE`. `../build.py` turns every file into three pages:

- EN `/PETO/guides/<en slug>/`
- TR `/PETO/tr/rehber/<tr slug>/`
- ES `/PETO/es/guias/<es slug>/`

Never hand-edit the generated HTML; edit the guide file and run `python3 -I PETO/_src/build.py`.
Read `../FACTS.md` first: it is the only source of truth about the app.

```python
GUIDE = {
    "id": "daily-routine",          # = file name without .py; used by {{link:...}} tokens
    "order": 2,                     # position on the guides index (1 = first)
    "category": "care",             # app | care | health | family
    "shot": "routine",              # screenshot key shown beside the headline (see list below)
    "sprites": ["pet_dog_golden", "pet_cat_gray"],   # 1-3 pixel pets for the hero and social card
    "icon": "bowl",                 # pixel icon for the guide card (see list below)
    "updated": "2026-11-17",
    "en": {
        "slug": "daily-pet-care-routine",   # ascii, lowercase, hyphens, no language prefix
        "title": "…",          # <title> and social title, <= 60 characters, main keyword first
        "description": "…",    # meta description, 140-160 characters, plain text
        "h1": "…",             # the visible headline (may be longer than the title)
        "kicker": "…",         # 2-4 words over the h1, e.g. "Daily care"
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

Use Python string literals carefully: triple-quoted strings for `body`, escape nothing else. The file must
import with `python3 -I -c "import runpy; runpy.run_path('<file>')"` without errors.

## Body HTML

Allowed tags: `h2 h3 p ul ol li strong em a blockquote table thead tbody tr th td`.
No inline styles, classes, scripts or `<img>`. Start with an `h2` (the page has its own h1).
Put every token below on its own line, outside `<p>`.

| Token | Becomes |
| --- | --- |
| `[[shot:KEY\|caption]]` | a real PETO screenshot in a pixel phone frame, with a caption |
| `[[tip\|text]]` | a "PETO tip" speech-bubble callout with a pixel pet (text may contain `<strong>`, `<em>`, `<a>`) |
| `[[checklist\|item one;;item two;;item three]]` | a pixel checkbox list readers can tick (3-12 items, plain text) |
| `[[cta]]` | the App Store download box (use exactly once, near the end) |
| `{{link:ID}}` | URL of that page in the same language. ID = a guide id, or `home`, `about`, `faq`, `support`, `privacy`, `guides`, `demo` |

Example: `<p>Set it up in the <a href="{{link:quick-start}}">quick-start guide</a>.</p>`

Guide ids that exist: `quick-start`, `daily-routine`, `family-sharing`, `health-record`, `sitter-card`,
`apple-watch-walks`, `choose-app`, and (new, 2026-11-18) `cat-litter-water`, `aquarium-cleaning`,
`pet-voice-reminders`, `memorial-mode`, `seasonal-outfits`. Link to 2-4 of the others where it helps the reader.

## Screenshot keys

Real screens from the app with the sample household Buddy (dog), Milo (cat), Poppy (rabbit).
Turkish versions exist for: `home`, `pet`, `routine`, `calendar`, `stats`, `settings`, `catcare`, `aquarium`,
`petvoice`, `outfits`, `memorial`, `memorialpage`, `languages` (the 13-language picker). Spanish versions exist for:
`home`, `pet`, `routine`, `calendar`, `stats`, `catcare`, `aquarium`. Missing ones show the English screen.
The app itself is in 13 languages, including Turkish and Spanish.

- `home` — Home: "1 pet needs attention", pet cards with status (Milo "Getting hungry", Buddy/Poppy
  "All good"), next feeding "in 8 h", Quick Actions row (feed, walk, play, cuddle, locked medication).
- `pet` — Buddy's page: avatar, "Dog · Golden Retriever · 3 years", status, FEED/WALK/PLAY/CUDDLE buttons,
  Care Plan with Feeding 7:30 AM · 6:30 PM, Walk 9:00 AM, Playtime 5:00 PM, Attention 8:00 PM (ON switches).
- `routine` — Routine editor for Buddy's Feeding: two times, Add time, Repeat (Every day / Weekdays /
  Custom), Remind me (At time / 10 min before / 30 min before), reminders switch, default portion.
- `log` — Buddy's Today's Log (Fed 7:30, Walk completed 28 min · Park, Played 18 min, Fed 6:35 PM,
  Attention 8:00 PM still open) plus Health record, Add Vet Appointment, History, Care card buttons.
- `logdetail` — Edit log for a feeding: date/time, amount + unit, food, appetite (Ate all / Ate some /
  Ate little / Skipped), note.
- `history` — History with filters (All, Feeding, Walk, Park, Playtime…) grouped by Today / Yesterday.
- `calendar` — Month calendar with coloured care dots, a vet cross on the 20th, pet filter, today's list.
- `stats` — Weekly insights: 12 meals completed, 3 walks, 2 park visits, 4 play sessions (49 min),
  scheduled meals logged 80 %, "Your 2026 Wrapped" banner.
- `settings` — Settings: Manage pets, Add pet, Family sharing, PETO Wrapped, care-reminder switches
  (medication shows a Premium badge), notification settings.
- `wrapped` — A Wrapped story card: "In 2026 you took 7 walks with Buddy · 4 park visits · 3 h 37 min walking".
- `health` — Health record for Buddy: Vet report (PDF), Vaccines (+ Add, "add vaccines and preventives to
  get booster reminders"), Weight (+ Add), Medication routine (Premium).

New screens (2026-11-18, English only unless noted):

- `catcare` — Milo's pet page with the cat-only "Litter & water" card (today's water and toilet numbers,
  7-day average, last litter clean).
- `aquarium` — Bubbles the fish: pet page with the "Aquarium" card (last clean, next date).
- `petvoice` — Settings → Notifications → "Reminders in my pet's voice" (record, Test, default sound).
- `memorial` — the memorial setup sheet (Poppy the rabbit in English, Buddy in Turkish): "We're so sorry. Poppy was deeply loved.",
  what happens (reminders stop quietly, logs/photos/health record kept, the page becomes a simple memorial,
  leave memorial mode any time), date, "A few words (optional)", "Create memorial" / "Not now".
- `memorialpage` — Buddy's "IN MEMORY" page: dates, "3 years of love", "Memories together" (7 walks
  together, 13 meals shared, 6 play sessions, favourite park), "Share memorial".
- `outfits` — the "OUTFITS" picker: a pet trying on the Bayram fez (Milo the cat in English, Buddy in Turkish —
  don't name the pet in captions), "Try them on for free", a Premium badge on each season and small locks; sections Halloween (witch hat, pumpkin
  cap), New Year (Santa hat, reindeer antlers, party hat), Bayram (fez, crescent tiara, tulip crown).
- `catcare` — Milo's "LITTER & WATER" card: LITTER / WATER / TOILET buttons, Today (pee 2, poop 1),
  7-day average (182 mL, pee 3), "Litter cleaned 17 hours ago", "A cat straining with little or no urine
  needs a vet right away."
- `aquarium` — Bubbles' "AQUARIUM" card: TANK button, "Cleaned 5 days ago · 25% water changed · Filter
  cleaned · Every 7 days · Next: Friday, Nov 20", "Change interval".
- `petvoice` — "PET VOICES": intro, "Reminders in my pet's voice" ON, a Record button and "Default
  sound" for Buddy, Milo and Poppy.

## Sprite and icon names

Sprites: `pet_<species>_<variant>`, e.g. `pet_dog_golden`, `pet_dog_black`, `pet_dog_corgi`,
`pet_dog_pug`, `pet_dog_husky`, `pet_cat_orange`, `pet_cat_gray`, `pet_cat_tuxedo`, `pet_cat_white`,
`pet_rabbit_gray`, `pet_rabbit_lop`, `pet_hamster_golden`, `pet_guineaPig_ginger`, `pet_bird_blue`,
`pet_bird_cockatiel`, `pet_fish_goldfish`, `pet_turtle_redEared`, `pet_lizard_leopardGecko`,
`pet_hedgehog_albino`, `pet_ferret_sable`.

Icons: `bowl leash ball heart medicine clinic bell star paw crown calendar calendarStar park palette
settings trends infinity`.

Outfit art (for `sprites`, use pet sprites only): outfits are drawn by the app; don't reference them as sprites.

## Writing rules

- Each language is written natively for its readers, not translated word for word. Same facts, same
  structure (same h2 sections, same faq count) in all three. Spanish: neutral Spanish, "tú". Turkish:
  natural, warm, "sen" form, correct Turkish characters (ç ğ ı İ ö ş ü).
- App UI words: in EN use the English labels in quotes or bold (e.g. **Care Plan**, "Remind me"). In TR
  use the app's Turkish labels where you know them (Ana Sayfa, Takvim, İstatistik, Ayarlar, Bakım Planı,
  Besle, Yürüyüş, Oyna, Sev, Rutin, Saatler, Tekrar, Her gün, Hafta içi, Özel, Bana hatırlat, Saatinde,
  10 dk önce, 30 dk önce, Rutini kaydet, Aile paylaşımı, Bakım hatırlatıcıları, İlaç, Haftalık Özet),
  otherwise describe the action. In ES use the app's Spanish (Spain, `es`) labels from
  /Users/guledaaydemir/PETO/SharedArt/Localizable.xcstrings (e.g. "Plan de cuidados", "Recuérdamelo").
- Product facts must match `../FACTS.md`; never invent features, prices, trial lengths, numbers, reviews
  or awards. Be clear about Free vs Premium where it matters. Never call the app "the best"; let the
  facts speak.
- Pet-care claims: practical, general and hedged. No medical or dosing advice; say "ask your vet" for
  health decisions. Cite only sources you have opened and confirmed (publisher, title, URL) — prefer
  WSAVA, AAHA, AVMA, RSPCA, PDSA, ASPCA, Cornell Feline Health Center, Apple Support. No invented
  statistics. `sources` may be empty when the guide is purely about using the app.
- Answer-first: the `answer` field and the first paragraph answer the question in the title. Write for
  people asking a search engine or an AI assistant (e.g. "app to remind me to feed my dog",
  "how to share pet care with family", "who fed the cat").
- 900-1,300 words of body per language. Short paragraphs, descriptive h2s phrased like real searches,
  at least one `[[shot:…]]`, one `[[tip|…]]`, optionally one `[[checklist|…]]`, and `[[cta]]` once.
