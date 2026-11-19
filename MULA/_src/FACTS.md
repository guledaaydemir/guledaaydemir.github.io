# MULA fact sheet (source of truth for site copy, guides and llms.txt)

Checked against the app's Swift code, README and in-app copy on 2026-11-18 (version 1.0).
Privacy/analytics and iCloud facts updated 2026-11-19 (Firebase Analytics, iCloud backup, sync and sharing, iPad and Mac).
App Store name "MULA: Plant Care", App Store id 6836519863. Do not state anything about MULA that is not here.

## The app

- **MULA** is a calm plant and flower care app for **iPhone** (iOS 17 or later) and **iPad** (iPadOS 17
  or later), that also runs on **Macs with Apple silicon** (as the iPad app, "Designed for iPad"), with an
  **Apple Watch** app (watchOS 10 or later, paired with an iPhone), Home Screen and Lock Screen **widgets**,
  and **Siri & Shortcuts**. A single universal App Store app (Premium carries over via "Restore purchases"); with "Sync with iCloud"
  every device signed in to the same Apple Account shows the same garden. On iPad and Mac the app shows a
  centred, phone-width column (no separate large-screen layout). The light meter uses the back camera, so
  it works on iPhone and iPad but not on a Mac. No Android or web version.
  <!-- Keep the iPhone the main framing (titles, screenshots); mention iPad and Mac where devices come up. -->
  Made by **Gül Eda Aydemir**, an independent iOS developer. Contact:
  solostaseraofficial@gmail.com · Instagram @solo.stasera.
- Look and feel: **calm, Japanese-inspired, paper-textured**. Cut-paper geometric illustrations, warm washi
  paper grain, serif headings (Cormorant Garamond, Lora) and Jost. Two paper moods: **Light Paper** ("Warm
  washi") and **Dark Forest** ("Deep felt green"); "Match the system" or "Evening calm" (Dark Forest from
  19:00). Optional **paper texture** and **Quiet motion** switches. Soft **garden music** (a minimal
  birdsong track) can play while MULA is open (on by default, volume slider, silent in silent mode, mixes
  with other audio).
- Three tabs only: **Today**, **Garden**, **Settings**.
- **No ads, ever. No account. No tracking.** "Your garden stays on your device." MULA has no server of
  its own. The garden is **backed up and synced through the person's own iCloud** (free, on by default;
  sharing a garden is Premium). It sends **anonymous usage statistics** to Google Analytics for Firebase (no advertising ID, no
  ad personalisation, never plant names, notes, captions or photos; can be turned off in Settings › Your
  garden › "Share anonymous usage"), and the optional Weather alerts ask Apple Weather (WeatherKit) for a
  forecast, see Privacy below.
  <!-- Never say MULA has "no analytics", "no analytics SDK" or that weather is its only network request. -->
- The app's interface is currently in **English**. (This website is in English, Turkish and Spanish.)
  <!-- Never claim the app itself is in Turkish or Spanish. -->
- **Free to download.** The free version keeps up to **10 plants** and **5 photos per plant**, with all
  reminders, soil checks, seasonal plans (viewing), the temperature check, small and Lock Screen widgets,
  the Apple Watch list and Siri.
- **MULA Premium**: **Annual** (with a **1-week free trial**, renews yearly until cancelled in Apple ID
  subscriptions) or **Lifetime** ("Pay once. Yours forever."). Premium adds: unlimited plants and
  portraits; editing the seasonal care plan of every plant; the full photo journal and posters; Vacation
  mode and care sheets; the light meter; weather alerts (frost and heat); answer buttons on the medium and
  large widgets and on Apple Watch; inviting others to a shared garden. "Restore purchases" in Settings. Purchases are handled by Apple.
  <!-- Do not state prices (they differ by country and are shown in the App Store), a release date,
  ratings, download counts or awards. -->

## The name and the idea (for the About page)

- MULA comes from **Mūlādhāra**, the root chakra in Sanskrit: *mūla* means root, *ādhāra* means support.
  It is the first of the seven, the one associated with feeling grounded, safe and steady.
- "A plant shows its leaves, but it lives through its roots. That is why MULA never orders a watering. It
  asks you to touch the soil first, and lets the answer decide."
- "Looking after something living is grounding for us too. MULA is made to feel like paper and quiet
  mornings: no ads, no noise, only the next small thing your garden needs."
- Launch screen: a cut-paper emblem (sun, hills, a soil bowl with roots, a sprout with four leaves, a small
  orbit) that pieces itself together, then "MULA" and the tagline **"Care · Grow · Bloom"**.
- Why it exists (maker's story; phrase as the maker's view): most plant apps tell you to water on a fixed
  day, which is exactly how many houseplants get overwatered; they are also often loud, full of ads or
  need an account. MULA asks instead of orders, follows the seasons, and stays quiet.

## Today (tab 1)

- A hero photo with the headline **"Care for Your Plants"** and an eyebrow with the season, e.g.
  "Today · Autumn". The paper sheet slides over the picture as you scroll.
- Status headlines such as "Everyone is cared for." / "One plant needs a little attention."
- **Emergency Care** card when a check is very late, e.g. "Momo has waited 7 days for water." The threshold
  is **"Emergency care after"** in Settings (default 7 days, adjustable): one extra nudge when a check is
  very late.
- **Upcoming Tasks**: Watering, Feeding and Seasonal check rows, e.g. "Watering · Momo · Monstera
  deliciosa · 7 days late". "View All" lists everything ("Needs you" / "Coming up").

## The soil check (the core idea): "A soil check, never an order"

- When a plant's interval is up, MULA asks **"How does Momo's soil feel?"** (in-app sheet, eyebrow
  "Watering · Momo") with these answers:
  - **"Dry"** ("Time for a drink") → button **"I watered Momo"**: the watering is logged and the next check
    is planned from today.
  - **"A little moist"** ("Check again in 2 days") → nothing is logged; MULA asks again **in two days**.
  - **"Wet"** ("Skip this round") → nothing is logged; this round is skipped (next check after a full interval).
  - **"Not sure"** ("Show me how to check") → shows: "Push a finger 3 cm into the soil. If it comes out clean
    and dry, it is time to water. If soil sticks to it, wait."
  - **"Remind me later"** postpones the question.
  - On notifications the same answers are buttons: **"Dry · I watered it"**, **"A little moist"**, **"Wet"**.
- A watering is only recorded when you say the soil was dry. The same rule is used on Today, in
  notifications, in widgets, on Apple Watch and with Siri ("Soil check for Momo in MULA").
- **Feeding**: "A little nourishment for Momo?" with **"Fed today"** or **"Later"**; shows "Last fed …".
  Fertilizer is optional. Feeding pauses in a plant's resting season and restarts on the first day of the
  next season that has feeding.

## Seasonal care plans

- Every plant has a **four-season plan** (spring, summer, autumn, winter): water every N days, feed every N
  days (or "Resting" — "Less water and no feeding while it rests."), and a short tip for the season.
- **"Follow the seasons automatically"**: reminders shift when the season changes. **Southern hemisphere**
  switch in Settings ("Seasons are reversed").
- Each plant also has a temperature range ("Happy between 15 and 30°C").
- Viewing the plan is free; editing season numbers is Premium. New plants get "A gentle starting plan"
  ("Every number can be changed later in Seasonal care.").
- The built-in plans are starting points, not botanical rules. <!-- In guides, say the defaults are
  starting points you can change; don't quote them as authoritative care advice. -->

## Plants and species

- 20 species in the catalog: Monstera deliciosa (Swiss cheese plant), Camellia japonica (Japanese
  camellia), Ficus elastica (Rubber plant), Hydrangea macrophylla (Bigleaf hydrangea), Phalaenopsis (Moth
  orchid), Pilea peperomioides (Chinese money plant), Dracaena trifasciata (Snake plant), Spathiphyllum
  (Peace lily), Epipremnum aureum (Pothos), Lavandula angustifolia (Lavender), Aloe vera, Rosa (Rose),
  Tulipa (Tulip), Cactaceae (Cactus), Nephrolepis exaltata (Boston fern), Hedera helix (English ivy),
  Begonia, Euphorbia pulcherrima (Poinsettia), Salvia rosmarinus (Rosemary), Dypsis lutescens (Areca palm).
  Any other plant can be added with a **"General care plan"**.
- Adding a plant: name (nickname), species (optional), **where it lives** (Indoor / Balcony / Outdoor) and
  **light** (Low light / Bright, indirect / Direct sun). Free version: up to 10 plants.
- Sample garden used in screenshots: **Momo** (Monstera deliciosa), **Tsubaki** (Camellia japonica),
  **Nori** (Ficus elastica), **Ajisai** (Hydrangea macrophylla), **Ran** (Phalaenopsis orchid),
  **Mame** (Pilea peperomioides).
- **"Not sure what it is?"** Take or pick a photo and MULA takes a look with Apple's **on-device** image
  classifier. It recognises plant **kinds**, not exact species (about 20 kinds such as orchid, rose, tulip,
  cactus, fern, ivy, begonia, poinsettia, rosemary, palm). "Looks like: Orchid" / "Might be: …". When it is
  not confident it says so and you pick the species yourself. The photo never leaves the phone.

## Garden, photo journal and posters (tab 2)

- **My Garden**: every plant as a card with its picture; "Needs care" marks.
- Plant page: a photo hero, "This season" plan, Care history (a calendar where days with a photo show the
  photo), **Journal**: "Little changes are worth keeping." Each photo becomes a moment; MULA pairs photos
  with a quiet **paper portrait** (geometric cut-paper illustration) and can show a **Poster** (photo above,
  portrait below, with the plant's name and number). Free: 5 photos per plant; Premium: full journal and
  posters.

## Reminders and notifications

- Local notifications from the iPhone (no server). "Only when a plant needs you. Never at night, never more
  than once a day for the same plant."
- Settings → **Reminders & quiet hours** ("Gentle, and only when needed."): switches for **Watering** ("A soil
  check, never an order"), **Fertilizing** ("Only in the growing season"), **Temperature** ("A seasonal check
  for balcony and outdoor plants"), **Weather alerts** (Premium), **Emergency care** ("One extra nudge when a
  check is very late").
- **Remind me at** (a time of day, default 9:00), **Quiet hours** (default 22:00–08:00), **Sound**: Kalimba (default),
  Wind chime, Water droplet, Singing bowl or the iPhone default sound (the calm sounds are MULA's own).
- Notification buttons: soil check → **Dry · I watered it / A little moist / Wet**; feeding → **Fed today /
  Later**. Answering works without opening the app. Tapping opens that plant. (A reminder that combines
  three or more plants has no buttons.)

## Temperature, frost and heat

- **Free**: a seasonal check for balcony and outdoor plants in the cold and hot months.
- **Weather alerts (Premium)**: Settings → Reminders → Weather alerts. Uses the forecast from **Apple
  Weather** (WeatherKit) for the next 3 days and compares lows and highs with each balcony/outdoor plant's
  temperature range. Cold night → alert the evening before at 18:00; hot day → alert that morning at 08:00
  (moved out of quiet hours). Today shows a line like "Cold Night Ahead · 2°C tonight" with only the
  affected plants. Location: approximate, asked once, rounded to about 1 km and stored on the device; only
  that rounded point is sent to Apple Weather. Works during Vacation mode. The Apple Weather mark and
  "Data sources" link are shown wherever the forecast is.

## Light meter (Premium)

- Opened from the sun icon in Garden or "Measure" next to the light choice when adding a plant.
- Uses the **back camera's exposure** to estimate light in **lux** ("About 2,400 lux · an estimate"). No
  photo is taken or saved. Under ~800 lux = low light; ~800–10,000 = bright, indirect; above = direct sun.
  These are rough estimates, not a lab instrument. Shows "Plants that would like it here" and "Your plants
  in this spot".

## Vacation mode and care sheets (Premium)

- Settings → **Vacation Mode** ("Going away?"): pick **Leaving** and **Back home** dates and one of three
  options: **"Pause reminders"** ("Nothing is marked as done. You review on return."), **"Someone is
  helping"** ("Share a care sheet with names and notes." — then "Who is helping?" name field and **"Share
  the care sheet"**), or **"Keep reminders"** ("I'll check from afar."). It warns e.g. "3 plants are due a
  soil check before you leave." Button: **"Start away mode"**. The care sheet is plain text for the helper,
  plant by plant: e.g. "Check the soil every N days; water only if the top is dry."
- "Pause reminders" and "Someone is helping" both hold reminders back; only "Keep reminders" keeps them on.
- Today shows "Away mode · back 24 Nov". Vacation mode never marks a task as done. Coming home (when reminders
  were held back): "Welcome home to your garden. Nothing was marked as done for you. Let's see how everyone
  is." with a "Log what they needed" step ("Water, feed or nothing at all"), and reminders resume.

## Widgets

- **Small** (free): the next plant; tap opens its soil check.
- **Lock Screen** circular, rectangular and inline (free): how many plants are waiting and the first name.
- **Medium**: plant and question; the **Dry / Moist / Wet** buttons are Premium (free shows "Answer here
  with Premium").
- **Large**: today's four tasks and upcoming checks; buttons on each row are Premium.

## Apple Watch

- The watch app lists the plants that need you (free). Answering **Dry / Moist / Wet** or **Fed / Later**
  from the wrist is Premium. If the iPhone is not nearby, the answer waits and is applied when it is.
- Watch-face complications: number of plants waiting and the first plant's name.

## Siri & Shortcuts (free, no setup)

- "I watered Momo in MULA" / "Log watering in MULA" — logs a watering and says the next check day.
- "What needs care in MULA" — reads today's soil checks and feedings.
- "Soil check for Momo in MULA" — asks how the soil feels; only "dry" logs a watering.
- "I fed Momo in MULA" — logs a feeding. Siri recognises the plant's nickname, species or common name.
  Phrases are English.

## Other

- **Grow further** in Settings links to the developer's other apps: Solo.Shots (make a timelapse of your
  plant), Solora, and more apps by the developer.
- Onboarding: "Make room for a little more green. MULA keeps every plant's name, face and rhythm in one
  quiet place." / "Every plant has its rhythm." (water, feed, warmth) / "Keep the little moments." Then
  "Would you like a gentle reminder?" (notification permission) and "Begin my garden".

## Privacy (what is true in the code)

- Plants, care history, photos and settings are stored **on the iPhone** in an App Group container shared
  with MULA's own widgets and its Apple Watch app. No MULA account and no MULA server: the developer cannot
  see the garden. Copies in iCloud (below) live in the person's own iCloud, handled by Apple.
- **iCloud backup** (Settings › "iCloud backup", free, on by default, needs iCloud Drive): plants, care
  history, photos and settings are backed up to MULA's private space in the person's iCloud ("only you can
  see it"), automatically "after changes and once a day, when you leave MULA", or with "Back up now". The
  backup before the last one is kept as a spare ("The backup before this one"). On a new iPhone, or after
  MULA was deleted, MULA offers to restore it before the intro ("Welcome back"); restoring replaces the
  garden on that device. An empty garden is never backed up automatically and never overwrites another
  device's backup. Premium is not in the backup; it comes back with "Restore purchases".
- **Sync with iCloud** (Settings › "Sync & sharing", free, on by default, needs an Apple Account): "One
  garden, every device." Every device signed in to the same Apple Account shows the same plants, care
  history and photos, through Apple's CloudKit in the person's private iCloud database. A plant deleted on
  one device goes to Recently deleted on the others. Turned off: "This garden lives only on this device.
  Backups still work."
- **Share this garden** (Settings › "Sync & sharing" › "Garden together", **Premium** for the person who
  invites; joining is free): "Invite a partner or flatmate." Uses Apple's iCloud sharing; both see the same
  plants, and when one waters, the other's reminder goes away. The person who joins brings their plants into
  the shared garden; whoever leaves (or if the owner stops sharing) keeps a copy of every plant. People in a
  shared garden see each other's names as shown by iCloud.
- **Recently deleted**: a removed plant waits 30 days with its photos and history and can be put back.
- **Export & print**: a printable care journal (PDF) and the whole garden as one `.mulagarden` file, shared
  only where the person sends it.
- No ads, no tracking, no data sold. Deleting the app removes its data from the device; iCloud backup and
  sync copies stay in the person's iCloud until they delete them (iOS Settings › Apple Account › iCloud ›
  storage).
  <!-- Never say "no cloud sync", "no cloud copy" or that the garden lives on one iPhone only. -->
- **Anonymous usage analytics** (added 2026-11-19): MULA sends anonymous usage statistics to **Google
  Analytics for Firebase** (Google's service; `FirebaseAnalyticsCore`, iPhone app only). What is sent: which
  screens are opened; care answers and actions (kind, where they were answered: app, notification, widget,
  Apple Watch, Siri); the plant's catalogue species, placement and light; counts and buckets (number of
  plants, photos, care records); on/off settings; feature use (light meter, vacation, backup, export…);
  steps around MULA Premium (offer shown, what led to it, plan chosen, purchase started, completed or
  cancelled, free trial, Premium ending, refunded or restored).
  Firebase also collects automatically: device model, iOS and app version, language, a random
  app-installation identifier and an approximate region/country from the IP address.
- **Never sent**: plant names, notes, photo captions, a helper's name, photos or any other text the person
  types; a custom species name is sent only as "custom". No advertising identifier (IDFA), no App Tracking
  Transparency prompt, ad personalisation off (consent mode ad_* denied), no tracking across other
  companies' apps or websites. Not linked to the person's name, email or Apple Account. Nothing is sold.
- Opt-out: **Settings › Your garden › "Share anonymous usage"** ("Helps improve MULA. Never names, notes or
  photos."). Turning it off stops collection and clears the analytics data on the device. Google's
  <https://firebase.google.com/support/privacy> applies; data is kept for a limited time. The App Store
  privacy label: Device ID, Product Interaction, Purchase History, used for analytics, not linked to the
  user, not used for tracking.
- Permissions MULA may ask for: **notifications** (reminders); **camera** (plant photos and the light meter;
  light readings are never saved); **photo library** via the system picker (to add a plant photo);
  **approximate location while using** (only for Weather alerts, Premium).
- Weather alerts send only a rounded (~1 km) location to Apple Weather (WeatherKit), Apple's privacy policy
  applies there. Purchases go through Apple (StoreKit); the developer does not see payment details.
- Photo identification and the light meter run fully on the device.
- **Not professional horticultural advice**: plans are starting points; MULA cannot diagnose pests or
  diseases.
