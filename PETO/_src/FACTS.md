# PETO fact sheet (source of truth for site copy, guides and llms.txt)

Checked against the app's code, README, docs/ANALYTICS.md and in-app FAQ/Privacy screens on 2026-11-17,
updated 2026-11-18 (cat care, aquarium care, pet voices, memorial mode, seasonal outfits, living pet,
Mac, 13 app languages, anonymous analytics). App Store id 6836239120.
Do not state anything about PETO that is not here.

## The app

- **PETO** is a pet-care routine app for **iPhone and iPad** (iOS 17 or later), with an **Apple Watch** app
  (watchOS 10 or later). The same app is also built for **Mac** (macOS 14 or later, Mac Catalyst) with
  **Universal Purchase**: one Premium purchase or subscription unlocks it on iPhone, iPad and Mac. On Mac,
  Live Activities, the Screen Time nudge and alternate app icons are not available. <!-- Before stating that the
  Mac version is on the store, prefer "PETO is built for iPhone, iPad and Mac". --> Made by **Gül Eda Aydemir**, an independent iOS developer.
  Contact: solostaseraofficial@gmail.com.
- Style: a warm **retro pixel-game look**: pixel-art pet avatars, chunky pixel buttons, ON/OFF pixel
  switches, wooden signs, a game-style tab bar (Home, Calendar, Stats, Settings), the Pixelify Sans font.
- **No ads. No PETO account. No tracking across other apps or websites. PETO has no server of its own.**
  Pet data is saved on the device. (Optional Family sharing syncs through the user's own iCloud.)
- **Anonymous usage statistics** (Google Analytics for Firebase): counts which screens open, which
  features and care types are used, how many pets and routines (numbers and species only), app settings
  and whether Premium is active. Never pet names, notes, photos, phone numbers, vet/clinic names or health
  records. No advertising ID, nothing used for ads, no App Tracking Transparency prompt. Users can turn it
  off in **Settings → Data → "Share anonymous usage stats"**, which also clears on-device analytics data.
  <!-- NEVER write "no analytics" anywhere. -->
- The app's own text is in **13 languages**: English (US and UK), Turkish, Spanish (Spain and Mexico),
  Brazilian Portuguese, French, German, Italian, Japanese, Korean, Arabic (right-to-left) and Russian.
  Switch inside the app; it applies instantly. Siri phrases work in every app language. This website is in
  English, Turkish and Spanish.
- **Free to download.** Core reminders and logging are free. Optional **PETO Premium** is sold as
  **monthly**, **yearly** (auto-renewing until cancelled in Apple ID subscriptions) or **lifetime**
  (a one-time purchase that never renews). Purchases are handled by Apple; "Restore Purchases" in
  Settings → Premium. Premium keeps working offline once verified.
<!-- Do not state a price, a free-trial length, a release date, ratings, download counts or awards. -->

## Pets

- Multiple pets, each with its own routines, logs, appointments and health record.
- **13 species**: dog, cat, rabbit, guinea pig, hamster, ferret, hedgehog, bird, fish, turtle, lizard,
  snake, and "other" (e.g. rat, hermit crab, snail, sugar glider).
- Each species has **8 pixel avatar variants** (104 in total); the first 4 per species are free, the
  others are Premium.
- Onboarding suggests routines per species (suggestions only): dog → feeding, walk, playtime, attention;
  cat → feeding, playtime, attention; small mammals → feeding, playtime, attention; bird → feeding,
  attention; fish → feeding; turtle/lizard/snake → feeding, attention.
- Sample household used in screenshots: **Buddy** (dog, Golden Retriever, 3 years), **Milo** (cat,
  2 years), **Poppy** (rabbit, 1 year), **Bubbles** (fish).
- Suggested routines now also include **Aquarium** for fish (feeding + aquarium) and turtles (feeding,
  attention, aquarium).

## Care routines (one engine for every care type)

- Care types: **Feeding, Walk, Playtime, Attention (cuddles)** — free — and **Medication** — Premium.
  Plus, all free: **Litter**, **Water** and **Toilet** (cat care) and **Aquarium** (tank cleaning).
- A routine has one or more **times** per day (e.g. feeding 7:30 AM and 6:30 PM), a **repeat** rule
  (Every day / Weekdays / Custom days, or **every N days**, 2–60, counted from the day it was actually
  done, so a late log moves the next reminder too), a **"Remind me"** offset (At time / 10 min before / 30 min before),
  an ON/OFF switch for reminders of that routine, and an optional default portion (e.g. "1 cup").
- **One-tap logging**: big FEED / WALK / PLAY / CUDDLE buttons on the pet page and Quick Actions on
  Home. Logging is optional; reminders work without it.
- Optional log details: time, **amount and unit** (cup / g), **food**, **appetite** (Ate all / Ate some /
  Ate little / Skipped), a **note**; walks can record duration and a **park** visit; play records minutes.
- **History** per pet, filterable by Feeding / Walk / Park / Playtime / …; logs can be edited or deleted.
- **Friendly status labels**, derived only from the schedule and the logs, never medical: "All good",
  "Full", "Meal coming up", "Meal time", "Getting hungry", "Just walked", "Walk time soon", "Walk time!",
  "Needs a walk", "Happy & played", "Needs some play", "Feeling loved", "Wants cuddles", etc. Home sorts
  pets by who needs something next and shows a greeting like "1 pet needs attention".

## Reminders (the core feature)

- Local notifications scheduled by iOS from the user's routines (no server). A rolling schedule covers
  the next 3 days and is rebuilt when the app opens or data changes. Logging something cancels its
  reminder.
- Actions right on the notification: **"Fed ✓ / Walked ✓…"**, **"Snooze 15 min"**, **"Skip"**; tapping
  opens the quick log for that pet. Reminders are grouped per pet and show the pet's pixel sprite.
  Feeding, walk, medication and vet reminders are time-sensitive.
- **Smart nudges** (free, can be turned off): one gentle follow-up for unlogged essential care; a
  "Buddy misses you" nudge after N hours without play or cuddles (quiet hours respected); an evening recap.
- **Playtime Live Activity** (free): countdown to the next playtime and a play timer with a "Done ✓"
  button on the Lock Screen and in the Dynamic Island.
- **Screen Time nudge** (free, optional): after N minutes on apps the user picks (e.g. social media),
  "Buddy hasn't played with you in 6 h". Uses Apple's Screen Time (Family Controls); stays on device.
- Per-type switches in Settings → Care reminders (feeding, walk, playtime, attention, medication,
  vet appointment) and a master notifications switch.
- Routines follow the device's local clock; after travelling, open PETO once so reminders are rebuilt.

## Calendar and stats

- **Calendar**: a month grid with coloured dots per care type and a red cross for vet appointments;
  filter by pet; today's list with ticks for done items. **Vet appointments** (free) with reminders.
- **Stats / Weekly insights** (free): meals completed, walks completed, park visits, play sessions and
  minutes, and "scheduled meals logged" as a percentage bar; filter by pet. Only logged activity is
  counted ("unlogged is unknown, not missed").
- **Premium**: trends and week-over-week comparisons.

## Health record (free; vet PDF report is Premium)

- Per pet: **vaccines and preventives with booster reminders**, **weight log with a trend chart**,
  medication (the medication routine is Premium), vet visits.
- **Vet report (PDF)**: an A4 report to show or send to the vet — Premium.

## Family sharing (Premium to create; joining is free)

- One household shared over the users' **own iCloud** (Apple CloudKit sharing). Everyone sees who fed,
  walked or played, so there are no double meals. Notifications like "Eda fed Buddy 🐾 — already done,
  no need to do it again." Invitees join free by opening the invitation link on their iPhone.
- PETO cannot read this data; stop sharing or leave the household at any time.

## Cat care (free; cats only)

- **Litter cleaning reminders** (a normal routine), **water drunk** in ml, and a **toilet log**: pee, poop
  or both; urine amount (none / small / normal / large); stool (normal / soft / diarrhoea / hard); warning
  signs (straining, blood, outside the box, frequent trips, pain). The toilet log is log-only, not a routine.
- A cat-only **"Litter & water"** card on the pet page: today's numbers, a **7-day average**, when the
  litter was last cleaned, and gentle prompts: if warning signs were logged in the last 48 h it says "These
  can be signs of a urinary problem. Show this log to your vet."; with no pee logged for over 24 hours it
  says "If you haven't seen any in the box either, call your vet."; "A cat straining with little or no urine
  needs a vet right away." It links to the health record and vet report.
- The (Premium) vet PDF report includes a **14-day "Litter & water" table**.
- Why it matters <!-- (for guides, hedged, cite vets) -->: changes in litter-box habits, straining or blood in urine
  can signal urinary problems; a cat straining to pee with little or nothing coming out is an emergency.

## Aquarium care (free; fish and turtles)

- Tank cleaning as a routine on the owner's own interval (every N days). Log **% of water changed** and
  whether the **filter was cleaned**. An **"Aquarium" card** on the pet page shows the last clean and the
  next date ("Counted from the last clean: log it a day late and the next reminder moves too.").
- PETO does not give water-chemistry advice; the schedule is the owner's (ask the vet or aquarium shop).

## Pet voices (free)

- Settings → Notifications → **"Reminders in my pet's voice"**: record your pet's bark, meow or chirp
  (up to 8 seconds; silence trimmed and loudness evened out). That pet's reminders, follow-ups and nudges
  play its own voice as the notification sound. **"Test"** sends a real reminder in about 3 seconds
  ("Lock your phone to hear it like the real thing"). Delete it to go back to the default sound.
- Needs microphone access only while recording; the recording stays on the device.

## Memorial mode (free, never behind Premium)

- For when a pet passes away: Edit Pet → **Memorial mode** → "Create memorial". Every reminder, nudge, Live
  Activity and Apple Watch entry for that pet **stops quietly**; logs, photos and the health record are
  **all kept**. The pet page becomes a simple **memorial page**: dates, "years of love", "a few words" you
  write (e.g. "Forever our little sunshine"), **"Memories together"** drawn from the log (e.g. favourite
  park), and a **shareable memorial card**. The pet is drawn still. Reversible: leave memorial mode at any
  time and reminders resume. The app opens with "We're so sorry. [Name] was deeply loved."

## Seasonal pixel outfits (try on free; keeping one is Premium)

- Pixel headwear drawn on top of any of the 104 sprites. Seasons: **Halloween** (witch hat, pumpkin cap),
  **New Year / Yılbaşı** (Santa hat, reindeer antlers, party hat), **Bayram** (fez, crescent tiara,
  tulip crown). The live season is featured (Halloween Oct 1 – Nov 7, New Year Dec 1 – Jan 15, Bayram from a
  week before Ramazan and Kurban Bayramı, computed with the Umm al-Qura calendar). Released outfits stay
  wearable all year. Anyone can try outfits on; keeping one on a pet is Premium.

## The living pet (free)

- On Home and the pet page the pixel pet is "alive": **press and hold to pet it** — a dog wags, a cat or
  small furry pet purrs, birds and fish flutter, reptiles nuzzle — felt through haptics (and mirrored on
  Apple Watch). **At night it sleeps** in a nightcap under a moon; the first look each morning it **yawns
  awake** with a sun. Right after a walk is logged it wanders about on **muddy paws** for a while. Memorial
  pets are drawn still; Reduce Motion keeps the looks but stops the movement.
- **Fold fun**: on a foldable iPhone (iPhone Duo), iPad split view or when a Mac window is maximised, a big
  one-step size change plays a little animation (pixel covers swing open and the pets hop out with hearts;
  folding squashes the app and puffs out paw prints). Decorative only; Reduce Motion turns it off.

## Other features

- **Pet-sitter care card** (free): a one-page PDF or image with the pet's routines, times, notes and a
  phone number, to hand to a sitter, neighbour or family member.
- **PETO Wrapped** (free): a yearly set of 9:16 story cards (1080×1920) such as "Your 2026" and
  "In 2026 you took 7 walks with Buddy · 4 park visits · 3 h 37 min walking", to share (e.g. Instagram).
- **Photo → pixel avatar** (Premium to save): turns a photo of your pet into a pixel avatar fully on the
  device (subject lift, 14-colour palette, outline). The original photo is never uploaded.
- **Themes**: Meadow (green) and Sky (blue) are free; Honey, Berry and Blossom are Premium. Light and
  dark appearance.
- **Alternate app icons** (Premium): Classic, Night, Ocean, Sakura, Gold, Retro Green, Halloween.
- **History export** (Premium).
- **Siri & Shortcuts**: "I fed Buddy in PETO" (TR: "PETO Buddy beslendi"), "How is Buddy?", "Open Buddy";
  feed / walk / play / cuddle shortcuts. On iOS 18+ a "Log care" control for Control Center, the Lock
  Screen or the Action Button.
- **Apple Watch**: pets listed by urgency, one-tap Feed / Play / Cuddle / Meds with haptics; tapping Walk
  asks "Track walk" or "Quick log",
  **walk tracking** as a HealthKit walking workout (time, distance, steps, saved to Apple Health only if
  allowed; "Buddy keeps you fit!" summary; without Health access the walk is still timed and logged),
  watch-face **complications** for the most urgent pet. Reminders appear on the wrist with their buttons.
- Settings → **Reset all data**, or deleting the app, removes everything PETO stored on the device.

## Privacy (what the app's Privacy screen says)

- Stores pet profiles, routines, logs, health records, vet appointments and preferences **on the device**.
- Family sharing (optional) syncs through the user's own iCloud; PETO has no server and can't read it.
- Photo avatars are made on the device; walks are saved to Apple Health only if allowed.
- Permissions PETO may ask for: notifications; Photos (add only — to save avatars, care cards and
  Wrapped cards); **Microphone** (only to record a pet voice); Health on Apple Watch (read steps/distance
  during a walk, save walks); Screen Time (only if the user turns on the Screen Time nudge); iCloud (only
  for Family sharing).
- Anonymous usage statistics as described above (opt-out in Settings → Data). App Store privacy label:
  Device ID, Product Interaction and Purchase History, used for analytics, not linked to the user, no
  tracking.
- No PETO account, no ads, no tracking across apps or websites; pet data is never sold.
- **Not medical advice**: status labels come from the schedule. For health questions, see a vet.

## Why PETO exists (the maker's story, for the About page)

- Pet care at home is many small, repeating jobs that are easy to forget or to do twice when several
  people share them ("Did anyone feed the cat?"). Most apps for this felt like spreadsheets, wanted an
  account, or showed ads.
- PETO turns the routine into something calm and a little playful, like a cosy pixel game: you open it,
  see who needs what, tap once, done. Gentle reminders instead of guilt; no streak pressure.
- PETO speaks 13 languages including Turkish, and the website borrows from Turkish craft (kilim borders, İznik tile
  patterns, the nazar bead, tulips). In Türkiye, neighbourhoods often look after street cats and dogs
  together (food and water bowls on doorsteps); that "we care for them together" spirit fits PETO's idea
  of shared care. <!-- Do not claim where the developer lives or works. -->
