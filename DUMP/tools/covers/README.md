# DUMP guide covers

Blog cover images for `/DUMP/guides/` and the ideas pages. Each cover puts a few photos from `photos/` on the left and
an iPhone on the right showing a recreated DUMP screen filled with the same photos. The screens copy the real app's
layout and English labels: Preview ("Original quality · Saved in this order", Save to Photos, Generate Caption), the
Swipe Carousel editor (Replace, Random, Fill, Reorder, Remove, Add), the grid canvas (Dump It, Background, Layers,
Ratio, Slides) and the Caption Generator (its six styles and real caption lines from the app).

```bash
python3 DUMP/tools/covers/build.py                       # render covers whose inputs changed
python3 DUMP/tools/covers/build.py --only travel-photo-dump
python3 DUMP/tools/covers/build.py --force               # re-render everything
```

Output in `DUMP/assets/covers/`: `<slug>.jpg` (1200×630 share image), `<slug>-1200.webp` and `<slug>-600.webp`.
Needs Google Chrome and Pillow.

## Add or change a cover

Edit `covers.json`: `slug`, `bg` (blurred background photo), `alt` (alt text), `art` and `screen`.

- `art.type`: `fan` (3 photos), `grid` (4 photos + optional `loose`), `pick` (6 `tiles`; mark one `["name", "blurry"]` or
  `["name", "duplicate"]`), `seamless` (4 photos over 3 slides, optional `paper` colour), `ratios` (1 photo at 4:5, 3:4, 1:1),
  `zoom` (1 photo + magnifier `focus`).
- `screen.type`: `preview` (`title`, `count`, `photo`), `editor` (`title`, `count`, `photo`, 6 `strip` photos),
  `grid` (4 `photos`), `caption` (`style`, `caption`, 3 `photos`). Caption text must be a real line from the app
  (`~/DUMP/DUMP/en.lproj/Localizable.strings`, keys `caption.*`).

Photos are named by content (`bali-temple-coconut`, `cafe-croissant-smile`, …). To add one, save a web-size copy
(about 900 px wide) into `photos/`.

Where covers are used:
- **Guides:** the `<figure class="guide-cover">` under the byline in each `DUMP/guides/*.html`, plus `og:image`,
  `twitter:image` and the Article image, all pointing at `assets/covers/<slug>.jpg`.
- **Guides index:** the cards on `DUMP/guides/index.html`.
- **Ideas pages:** a `"cover": {"slug", "alt"}` field in their content file (see `../ideas/README.md`).
