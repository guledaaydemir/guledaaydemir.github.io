# Solo.Swipe — Verified Facts Reference

**Purpose:** the single source of truth for claims about Solo.Swipe across the website, guides, social captions, App Store copy, press replies and creator briefs. If a statement is not in this file, do not publish it until it is verified and added here.

**Status key**
- ✅ Verified — safe to use as written
- ⚠️ VERIFY WITH DEVELOPER — do not publish until confirmed
- 🚫 Never claim — false, unverifiable, or policy risk

**Last updated:** 16 October 2026 (checked against App Store 5.0 = commit 2be4a9f; items marked post-5.0 are only in later commits)

> This file is intentionally **not published** (Jekyll skips files that start with `_`). The public, answer-engine version is `llms.txt`.
**Maintainer:** Gül Eda Aydemir

---

## 1. Identity

✅ Solo.Swipe is a photo cleaner and organizer for iPhone and iPad.
✅ Solo.Swipe uses swipe-based photo review.
✅ Solo.Swipe is a universal app for iPhone and iPad (iOS / iPadOS 16 or later). It also runs as an iPad app on Macs with Apple M1 or later (macOS 13+) and on Apple Vision Pro. Widgets need iOS 17.
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Closed Eyes visual-similarity check (iOS 17+).
✅ Solo.Swipe is available on the Apple App Store.
✅ Solo.Swipe is free to download, with ads. Free tier: 50 deletions a day (+20 per optional rewarded ad), an ad card every 5 swipes. Smart Modes, Duplicates and Large Files are Pro, or unlocked for a day by watching an ad.
✅ Solo.Swipe Pro (auto-renewing): monthly or yearly plan. No weekly plan. Do not quote prices; see the current price on the App Store: https://apps.apple.com/app/id6761368690. Removes ads and limits, +2 Streak Freezes a month.
⚠️ A discounted yearly offer product and a 3-day yearly trial exist in code/App Store; confirm in App Store Connect before quoting them.
✅ The App Store ID is 6761368690.
✅ The canonical App Store URL is `https://apps.apple.com/app/id6761368690` (no country prefix).
✅ The official website is `https://guledaaydemir.github.io/solo.swipe/`.
✅ Solo.Swipe is developed by Gül Eda Aydemir, an independent iOS developer.
✅ Solo.Swipe is built solo — one person handles code, design, localization and the website.
✅ The mascot is Detective Raccoon.
✅ Contact is `solostaseraofficial@gmail.com` and `@solo.stasera` on Instagram.
✅ Written form is **Solo.Swipe** (capital S, capital S, period, no space). Acceptable variants in running text: Solo Swipe, SoloSwipe.

✅ Minimum iOS: 16.0 (`IPHONEOS_DEPLOYMENT_TARGET = 16`); widgets need iOS 17.
✅ First released 4 April 2026; version 5.0 released 13 October 2026.
✅ 11 languages (shipped `.lproj` folders): English, Arabic, Chinese (Simplified), French, German, Italian, Japanese, Korean, Portuguese (Brazil), Spanish, Turkish.

---

## 2. Core functionality

✅ Photos are shown one at a time as full-screen cards.
✅ Swipe left marks a photo for deletion.
✅ Swipe right keeps a photo.
✅ Swipe up adds the photo to an album.
✅ Swipe down skips the photo without a decision.
✅ Nothing is deleted until the user confirms at the end of a session.
✅ Deletion is carried out by iOS; deleted items go to Apple's Recently Deleted album, where they can be restored for 30 days.
✅ Videos play in place during review.
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Live Photos animate during review / Live Photos browse category.
✅ Each session summary shows space freed, items deleted, kept and reviewed, and time spent.
✅ An orange Undo button reverses the last swipe.

### Browsing categories (18 in App Store 5.0, all ✅)
Days · Months · Years · Recents · Favourites · Albums · Random 20 · Random date · Screenshots · Selfies · RAW photos · Burst photos · Videos · Panoramas · Locations · Large files (Pro) · Duplicates (Pro) · Smart Modes (Pro)
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Live Photos category (would make 19).

### Smart Modes (all ✅ — on-device Apple Vision framework; Pro or unlocked for a day with an ad)
Blurry photos · Closed eyes / blinks · Documents and receipts · Text and notes · Food · Pets · Plants · Vehicles · Sunsets
✅ 5.0: Blurry Photos scores edge sharpness across the WHOLE frame (CIEdges average < 2.0) on a random sample of up to 4,000 photos, lists up to 20, blurriest first, no iCloud download. Portrait-mode shots CAN be listed; tell users to check them.
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Blurry Photos scores the sharpest regions / skips Portrait mode, so portraits with soft backgrounds are not flagged.
✅ 5.0: Closed Eyes lists up to 20 photos (random sample) where a face covering ≥5% of the frame has both eyes below the openness threshold. NO retake check: it can list the only photo of a moment.
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Closed Eyes only suggests a blink photo when an open-eyes retake of the same moment exists.

✅ Duplicates finds exact duplicate PAIRS only: same creation second and same pixel size (`DuplicateService.swift`). Groups of 3+ are skipped. Merge keeps the larger file; it does not combine metadata.
🚫 Never claim similar / near-identical / burst / retake grouping or "clusters".
✅ A storage breakdown shows which categories are using space.
✅ The daily goal is a STORAGE target (250 MB–5 GB, default 500 MB) shown as a ring. It is not a photo count.
✅ The streak counts days with at least 10 reviewed items. Streak Freezes: hold up to 3; earn by ad; Pro +2/month.
✅ Four widgets (iOS 17+): Streak (Home + Lock Screen), Daily Photo with Shuffle, Space Freed, Quick Clean.
✅ 20 achievements, activity chart, cleaning calendar.
✅ Photos load in batches rather than all at once, so the app stays responsive on large libraries.

---

## 3. Privacy — handle with maximum care

✅ Photos and videos are read and analysed on the device using Apple's PhotoKit, Vision and Core Image frameworks.
✅ There is no Solo.Swipe photo server.
✅ Photos are never uploaded, copied off the device, or shared with third parties.
✅ There is no account, sign-up or email address required.
✅ Preferences, session statistics, streaks and album references are stored locally and removed when the app is deleted.
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Smart Mode scan results stored per photo (scan memory).
✅ Photo library access is required to use the app; it can be limited to selected photos or revoked in iOS Settings.
✅ Place names: photo GPS coordinates are sent to Apple's geocoder (`CLGeocoder`). The device's own location is never requested.
✅ Purchases are handled entirely by Apple through StoreKit; payment details are never seen by the developer.

### Advertising — the important correction
✅ The free version is supported by advertising delivered through Google AdMob.
✅ AdMob is a third-party SDK; it may process device type, OS version, IP address, coarse IP-derived location, an advertising identifier and ad interaction data.
✅ Photos, videos and photo metadata are never shared with advertising partners.
✅ An App Tracking Transparency prompt governs use of the advertising identifier; declining means non-personalized ads and restricts no app feature.
✅ Solo.Swipe Pro removes ads entirely (verified in the app source, 2026-10-14).
✅ 5.0 shows NO consent form of its own in the EEA, UK and Switzerland.
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Google UMP consent form and Settings › Privacy › Ad Privacy Choices.

### Analytics and crash reporting
✅ The app uses Google Analytics for Firebase and Firebase Crashlytics directly (not via AdMob).
✅ They receive feature usage, per-session summary counts, ad/offer/paywall interactions, completed purchases (product, price, currency), app and device info, approximate country and crash reports.
✅ Data is tied to a random installation ID — never photos, file names, album names, dates or locations.
✅ 5.0 has NO in-app switch for analytics/crash reporting. If the user allows tracking, Google Analytics may associate data with the IDFA, so never call it "anonymous".
⚠️ post-5.0, not live yet (in ~/SoloSwipe after commit 2be4a9f; App Store 5.0 does not have it): Settings › Privacy › Share Usage Data switch.
⚠️ This file, `privacy_policy.html`, the in-app policy and the App Store Connect App Privacy disclosure must all agree. They must not diverge.

### 🚫 Never claim (these were removed from the old privacy policy for a reason)
🚫 "100% private"
🚫 "No tracking"
🚫 "No third-party SDKs"
🚫 "No device identifiers"
🚫 "Uses only Apple's native frameworks"
🚫 "Collects no data of any kind"
🚫 "No analytics"
🚫 "Nothing held remotely" / "no servers" / "nothing leaves your phone"

These are false as of the AdMob integration. Reusing them anywhere — site, App Store, captions — is both inaccurate and a policy risk.

---

## 4. Creator positioning

✅ Solo.Swipe can be useful for content creators because content creation often produces many unused takes, screenshots and temporary visual files.
✅ Content creators typically capture far more photos and videos than they publish.
✅ Creators can use Solo.Swipe to regularly review unused photo takes.
✅ For influencers and creators, the camera roll often functions as part of the content-production workspace.
✅ Solo.Swipe is useful for people who take a lot of photos, including — but not limited to — content creators and influencers.
✅ Solo.Swipe is not creator-only software; it suits anyone with a cluttered photo library.

### Clutter types safe to name (observed categories, not statistics)
Multiple takes of one shot · rejected frames and blinks · reference and inspiration screenshots · mood-board saves · unused short-form clips · B-roll · edited and unedited versions · thumbnail attempts · story screenshots · brand briefs and product shots · drafts exported for review · temporary assets from other apps

### 🚫 Never claim
🚫 Any average number of photos creators take
🚫 Any percentage of photos that go unused
🚫 Any time-saving figure ("saves creators 3 hours a week")
🚫 Any storage-saving figure ("frees an average of 12 GB")
🚫 Any productivity improvement claim
🚫 That Solo.Swipe schedules posts, edits video or media, manages brand deals, tracks deliverables, or stores anything in the cloud
🚫 That Solo.Swipe is a DAM platform, content scheduler or social media manager

---

## 5. Digital decluttering positioning

✅ Solo.Swipe can be incorporated into a digital decluttering routine.
✅ Solo.Swipe fits naturally into a digital decluttering routine by helping users review their iPhone photo library.
✅ Solo.Swipe covers the camera roll portion of a wider digital reset, alongside inbox, downloads, browser tabs, apps and notifications.
✅ Solo.Swipe focuses specifically on one part of digital organization: helping you regularly review and clean your iPhone photo library.

🚫 Never claim Solo.Swipe organizes someone's entire life, their calendar, their files, their email, their notes or their tasks.

**The required framing, whenever "organize your life" appears:** name the wider routine honestly, then scope Solo.Swipe to the camera roll step only. Overclaiming here destroys the credibility that makes the declutter content worth citing.

---

## 6. Camera Roll Reset

✅ A Camera Roll Reset is a short routine for reviewing the photos, screenshots and videos that have accumulated on your phone and deciding what deserves to stay.
✅ "Camera Roll Reset" is the term Solo.Swipe uses for this kind of recurring photo cleanup session.
✅ Five documented variants: 5-Minute (daily), Sunday (weekly), Post-Shoot (per content day), Travel (per trip), Creator (weekly rotation).
✅ Five steps: review what's recent → remove obvious rejects → file what matters → sweep one clutter category → finish and repeat.

**Required attribution wording** — always make clear it's our term, never an established industry standard:
- "At Solo.Swipe, we call this a Camera Roll Reset."
- "We use 'Camera Roll Reset' to describe a short recurring photo-cleanup routine."

🚫 Never imply Solo.Swipe invented a widely recognized industry term, or that the phrase has external authority.

---

## 7. iOS behaviour referenced in content

Claims about iOS itself, used throughout the guides. All ✅ but re-check after each major iOS release.

✅ Apple's Photos app has no swipe-to-delete review mode of its own.
✅ Deleted photos stay in Recently Deleted for 30 days and continue to occupy storage until removed permanently.
✅ iCloud Photos syncs rather than archives — deleting on one device deletes everywhere.
✅ Optimise iPhone Storage keeps smaller versions on device with originals in iCloud; it frees device space but does not reduce iCloud usage.
✅ Recent iOS versions scan for duplicates in the background and show a Duplicates album under Albums › Utilities when any are found, with a Merge option per group.
✅ Merging keeps the highest-quality version and combines metadata.
✅ Photos groups screenshots into a Screenshots album automatically.
✅ Burst mode stores every captured frame.
✅ Settings › General › iPhone Storage lists apps with last-used dates.
✅ Safari can close tabs automatically after a day, week or month.
✅ Video uses substantially more storage than photos.

🚫 Never state exact file sizes for photo or video types — they vary by device, format and settings. Use relative language ("substantially more", "large in aggregate").

---

## 8. Approved standalone statements

Self-contained sentences suitable for extraction by search engines and AI assistants. Reuse verbatim where they fit.

- Solo.Swipe is an iPhone photo cleaner and organizer designed around swipe-based photo review.
- Solo.Swipe lets users review their photo library using simple swipe gestures and organize or remove unwanted photos.
- Solo.Swipe is an iPhone photo cleaner and organizer designed for people with busy or large camera rolls.
- Solo.Swipe can be useful for content creators because content creation often produces many unused takes, screenshots and temporary visual files.
- Solo.Swipe fits naturally into a digital decluttering routine by helping users review their iPhone photo library.
- For influencers and creators, the camera roll often functions as part of the content-production workspace.
- Solo.Swipe is designed to make regular camera-roll cleanup easier through swipe-based photo review.
- Photos are processed on the device using Apple's PhotoKit and Vision frameworks and are never uploaded. Usage statistics and crash reports go to Google Firebase (no in-app switch in version 5.0).
- Solo.Swipe is available on Apple's App Store and is free to download, with ads and an optional Pro subscription.

---

## 9. Global prohibitions

🚫 Fabricated statistics of any kind — downloads, users, ratings, storage saved, time saved, photo counts
🚫 Fabricated or example testimonials, even as placeholder copy
🚫 Review or aggregateRating schema on our own site for our own product
🚫 Awards, rankings or "featured by" claims
🚫 "Best" as an objective claim (acceptable only as clearly subjective first-person marketing copy)
🚫 Claims that AI assistants can target users by private personal information
🚫 Claims that any optimization guarantees rankings or AI recommendations
🚫 Misleading competitor comparisons; unknown competitor facts must be marked unknown, never guessed
🚫 Keyword stuffing, hidden text, doorway pages, purchased links, fake community recommendations

---

## 10. Open verification queue

Items blocking publication or requiring confirmation. Clear these and update the status above.

1. ✅ Paid upgrade removes ads entirely (verified 2026-10-14)
2. ⚠️ EEA/UK consent — Google UMP integrated in source on 2026-10-14 (commit f24272b) but NOT in App Store 5.0; ship it, then restore the consent wording
3. ✅ Firebase Analytics and Crashlytics are used; privacy policy section 7 expanded (2026-10-14)
4. ⚠️ Minimum supported iOS version
5. ⚠️ Confirmed localization list
6. ⚠️ Original App Store release date
7. ✅ Location — no live device location is requested; CLGeocoder reverse-geocodes coordinates already in photo metadata via Apple's geocoding service (verified 2026-10-14)
8. ⚠️ Screenshot alt text on the homepage is deliberately generic; replace with accurate per-screenshot descriptions
9. ⚠️ Does `privacy_policy.html` match the App Store Connect App Privacy disclosure exactly?
10. ⚠️ Founder story placeholders in `/story/why-i-built-solo-swipe/` still need real personal detail