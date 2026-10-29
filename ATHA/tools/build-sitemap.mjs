/* ==========================================================================
   ATHA — sitemap generator
   Rewrites sitemap.xml from the static page list below plus every published
   item in content/guides.json (guides, practice pages, comparisons, audience
   pages; an item's "path" wins over guides/<slug>.html). Exact live case: /ATHA/.

   Turkish pages (/ATHA/tr/) are listed in TR_PAGES. Pages that exist in both
   languages carry <xhtml:link> alternates (en, tr, x-default -> en); keep PAIRS
   in step with the hreflang tags in the pages themselves.

   Run from the ATHA folder:  node tools/build-sitemap.mjs
   Draft guides are skipped. Bump a page's lastmod only when its content changes.
   ========================================================================== */
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const SITE = 'https://guledaaydemir.github.io/ATHA/';

// path -> last real content change (YYYY-MM-DD)
const STATIC_PAGES = [
  ['',                   '2026-10-29'],
  ['features/',          '2026-10-15'],
  ['meditations/',       '2026-10-15'],
  ['guides/',            '2026-10-28'],
  ['box-breathing-timer/', '2026-10-29'],
  ['support.html',       '2026-10-15'],
  ['about.html',         '2026-10-15'],
  ['press/',             '2026-10-15'],
  ['apps/',              '2026-10-15'],
  ['privacypolicy.html', '2026-10-15'],
  ['terms.html',         '2026-10-15']
];

// Turkish pages: path -> last real content change
const TR_PAGES = [
  ['tr/',                                '2026-10-29'],
  ['tr/rehber/',                         '2026-10-29'],
  ['tr/rehber/uyuyamiyorum.html',        '2026-10-15'],
  ['tr/rehber/4-7-8-nefes-teknigi.html', '2026-10-15'],
  ['tr/rehber/kutu-nefesi.html',         '2026-10-15'],
  ['tr/kutu-nefesi-zamanlayici/',        '2026-10-29']
];

// English path <-> Turkish path
const PAIRS = [
  ['',                                     'tr/'],
  ['guides/',                              'tr/rehber/'],
  ['guides/cant-sleep-at-night.html',      'tr/rehber/uyuyamiyorum.html'],
  ['guides/4-7-8-breathing-for-sleep.html', 'tr/rehber/4-7-8-nefes-teknigi.html'],
  ['practices/box-breathing.html',         'tr/rehber/kutu-nefesi.html'],
  ['box-breathing-timer/',                 'tr/kutu-nefesi-zamanlayici/']
];

function alternates(path) {
  const pair = PAIRS.find(([en, tr]) => en === path || tr === path);
  if (!pair) { return ''; }
  const [en, tr] = pair;
  return '\n    <xhtml:link rel="alternate" hreflang="en" href="' + SITE + en + '"/>' +
         '\n    <xhtml:link rel="alternate" hreflang="tr" href="' + SITE + tr + '"/>' +
         '\n    <xhtml:link rel="alternate" hreflang="x-default" href="' + SITE + en + '"/>\n  ';
}

const entry = (path, lastmod) => {
  const alt = alternates(path);
  return alt
    ? `  <url><loc>${SITE + path}</loc><lastmod>${lastmod}</lastmod>${alt}</url>`
    : `  <url><loc>${SITE + path}</loc><lastmod>${lastmod}</lastmod></url>`;
};

async function build() {
  const urls = STATIC_PAGES.map(([path, lastmod]) => entry(path, lastmod));
  const guides = JSON.parse(await readFile(join(ROOT, 'content/guides.json'), 'utf8'));
  let count = 0;
  for (const item of guides.items || []) {
    if (item.status !== 'published' || !item.slug) { continue; }
    const path = item.path || `guides/${item.slug}.html`;
    urls.splice(4 + count, 0, entry(path, item.updated));
    count++;
  }
  for (const [path, lastmod] of TR_PAGES) { urls.push(entry(path, lastmod)); }
  const xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<!--',
    '  ATHA sitemap. Regenerate with: node tools/build-sitemap.mjs (from the ATHA folder).',
    '  Every URL uses the exact live case: /ATHA/ (uppercase). English/Turkish pairs carry xhtml:link alternates.',
    '-->',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    urls.join('\n'),
    '</urlset>',
    ''
  ].join('\n');
  await writeFile(join(ROOT, 'sitemap.xml'), xml, 'utf8');
  console.log(`sitemap.xml written: ${urls.length} URLs (${count} guides and articles, ${TR_PAGES.length} Turkish pages)`);
}

build().catch((error) => { console.error(error); process.exit(1); });
