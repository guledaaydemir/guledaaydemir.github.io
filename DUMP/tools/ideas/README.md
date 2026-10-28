# DUMP ideas pages

The ideas section (`/DUMP/ideas/`, Turkish `/DUMP/tr/fikirler/`) is generated from one JSON file per page.
Never edit the generated `index.html` files: the next build overwrites them.

```
DUMP/tools/ideas/
  build.py          the generator (Python 3; Pillow + Google Chrome only for share images)
  config.json       App Store provider token and Custom Product Page ids, filled in once
  og-cache.json     which share images are up to date (managed by build.py)
  pages/en/*.json   English pages  → /DUMP/<slug>/
  pages/tr/*.json   Turkish pages  → /DUMP/tr/<slug>/
```

## Build

```bash
python3 DUMP/tools/ideas/build.py
```

One run writes every page, both ideas indexes, an `og.jpg` share image next to each page,
and the generated blocks in `DUMP/sitemap.xml` and `DUMP/llms.txt` (between the `ideas:start` / `ideas:end` comments).
Options: `--check` validates the content files without writing anything; `--force-og` re-renders every share image.

The build stops if a title is over 60 characters, a description over 155, a slug is reused, or a campaign tag is over
30 characters (App Store Connect's limit). It warns when a page has fewer than 4 or more than 6 FAQ questions.

## Add a new ideas page

1. Copy an existing file in `pages/en/` (for a list of copyable lines, start from `photo-dump-caption-ideas.json`;
   for a numbered list of ideas, `photo-dump-ideas.json`; for layout diagrams, `instagram-carousel-ideas.json`).
2. Give it a new `slug` (the URL), `key`, `title`, `description`, `campaign` and content.
3. For a Turkish version, add a file with the **same `key`** in `pages/tr/`. Pages that share a key get hreflang links,
   a language switch and the same sitemap entry. A page without a pair is fine too.
4. Run the build, check the page locally (see below), commit.

The new page appears on the ideas index, in the "More ideas" block of the other pages, in the sitemap and in llms.txt
automatically. To feature it on `/DUMP/guides/` as well, add a card there by hand.

### Fields

| Field | What it does |
|---|---|
| `key` | Pairs language versions. Same value in `en/` and `tr/`. |
| `order` | Position on the ideas index and in "More ideas". |
| `slug` | URL: `/DUMP/<slug>/` (or `/DUMP/tr/<slug>/`). Lowercase, digits, hyphens. |
| `keyword` | The main search phrase. Goes into the Article structured data. |
| `title` | `<title>`, Open Graph and Twitter title. Max 60 characters. |
| `description` | Meta description. Max 155 characters. |
| `h1` | The page heading. HTML allowed; wrap the highlighted words in `<span class="g">…</span>`. |
| `crumb`, `eyebrow` | Breadcrumb label and the small line above the heading. |
| `campaign` | `ct=` value for App Store Connect → Analytics → Campaigns (e.g. `web-captions`, `web-captions-tr`). |
| `product_page` | `photo_dump`, `carousel` or `null`. Picks the Custom Product Page id from `config.json`. |
| `published`, `updated` | ISO dates (`2026-10-28`). Bump `updated` when you change the content. |
| `card` | `tag`, `title`, `text` for the card on the ideas index and on other pages. |
| `og` | Share image text: `kicker`, `title`, `accent` (gradient part), `sub`, `alt`, and `art`: `captions` (shows the 3 lines in `samples`), `ideas` (fanned slides with 4 `labels`) or `carousel`. With `art: "captions"`, an optional `photos` list of three of your own photos in `og-photos/` shows them as a fanned dump instead. |
| `intro` | One or two short paragraphs (HTML). The first CTA box follows them. |
| `cta_text` | Optional. Replaces the sentence under the CTA heading on this page. |
| `mid_cta_after` | Section `id` after which the middle CTA box goes. Defaults to the middle section. |
| `sections` | The H2 sections, in order (see below). |
| `faq` | 4–5 `{ "q": …, "a": … }` pairs. Rendered at the bottom and as FAQPage structured data. |
| `related` | Optional extra cards for "More ideas": `{ "href", "tag", "title", "text" }`. |

Each section has an `id` (the anchor), `h2`, an optional `short` label for the jump chips at the top, an optional
`lead` (answer-first sentence) and **one or more** of:

- `captions`: lines with a Copy button. A line is a string, or `{ "text", "note", "lang" }` to add a small
  translation under it (`note` is not copied).
- `ideas`: `{ "title", "text" }` items, numbered across the page.
- `layouts`: `{ "strip", "panels", "title", "text" }` items with a slide diagram. `strip` is one of the presets in
  `STRIPS` in build.py: `horizon`, `reveal`, `line`, `fade`, `scrapbook`, `film`, `banner`, `colors`, `timeline`,
  `route`, `opener`, `closer`, `middle`, `beforeafter`, `zoom`.
- `steps`: `{ "title", "text" }` items as a numbered how-to.
- `html` (before the lists) and `after` (after them): free HTML for paragraphs, tables or bullet lists.

Every page automatically gets: one H1, the Smart App Banner, canonical and hreflang links, Open Graph and Twitter tags,
Article + BreadcrumbList + FAQPage JSON-LD, three CTA boxes (after the intro, in the middle, at the end) and links to the
other ideas pages, the ideas index and the DUMP home page.

Content rules: original writing only, and no invented numbers, user counts or reviews. Anything said about DUMP
must match the app (check `~/DUMP`).

## App Store campaign links (`config.json`)

Every App Store link on an ideas page is

```
https://apps.apple.com/app/apple-store/id6798248086?pt=PROVIDER_TOKEN&ct=CAMPAIGN&mt=8&ppid=PPID
```

with `ct` from the page's `campaign` and `ppid` from its `product_page`. Values still written in CAPITALS in
`config.json` count as not filled in and are left out of the links, so a page never ships a placeholder.
After filling them in, run the build again.

- **`provider_token`**: App Store Connect → Apps → DUMP → Analytics → Campaigns → "Generate a campaign link".
  The token is the `pt=` number in the link it shows. It's the same for all your apps.
- **`product_pages.photo_dump`** and **`product_pages.carousel`**: App Store Connect → Apps → DUMP →
  Distribution → Custom Product Pages → open the page → **Product Page ID** at the bottom of the page. It is *not* the
  id in the browser's address bar. Until the page is approved, the link opens your default product page.
  The captions and ideas pages use the Photo Dump page; the carousel page uses the Carousel page.

## Check locally

```bash
python3 -m http.server 8000
```

Run it from the repository root, then open http://localhost:8000/DUMP/ideas/. The pages use root-relative paths
(`/DUMP/…`), so opening the files directly from Finder won't load the styles.
