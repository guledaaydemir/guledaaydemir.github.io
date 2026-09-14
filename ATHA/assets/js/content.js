/* ==========================================================================
   ATHA — Content renderer
   Renders manifest-driven collections into any page. Pages declare what they
   want in markup; no page contains content data.

   Declarative:
     <div data-atha-collection="guides"
          data-layout="grid"      grid | list | compact | feature
          data-limit="6"
          data-category="sleep"
          data-featured="true"
          data-filters="true"
          data-search="true"
          data-exclude="cant-sleep-at-night"
          data-empty-title="Guides are on the way"></div>

   Programmatic:
     ATHA.content.render({ source: 'guides', target: el, limit: 3 });
   ========================================================================== */
(function () {
  'use strict';

  var A = window.ATHA;
  if (!A) {
    if (window.console) { console.error('ATHA: atha.js must load before content.js'); }
    return;
  }

  var esc = A.escapeHTML;

  var MANIFESTS = {
    guides:      'content/guides.json',
    meditations: 'content/meditations.json',
    features:    'content/features.json',
    apps:        'content/apps.json',
    screenshots: 'content/screenshots.json'
  };

  /* ----------------------------------------------------------------------
     Normalisation — every consumer sees the same shape regardless of what
     an individual manifest happens to omit.
     ---------------------------------------------------------------------- */
  function normalize(raw, name) {
    var manifest = raw && typeof raw === 'object' ? raw : {};
    var basePath = manifest.basePath == null ? (name + '/') : manifest.basePath;
    var items = Array.isArray(manifest.items) ? manifest.items : [];

    return {
      collection: manifest.collection || name,
      basePath: basePath,
      title: manifest.title || '',
      description: manifest.description || '',
      fallbackHref: manifest.fallbackHref || '',
      categories: Array.isArray(manifest.categories) ? manifest.categories : [],
      items: items.map(function (item, index) {
        return {
          slug: item.slug || ('item-' + index),
          title: item.title || '',
          summary: item.summary || '',
          category: item.category || '',
          tags: Array.isArray(item.tags) ? item.tags : [],
          intent: item.intent || '',
          icon: item.icon || '',
          image: item.image || '',
          alt: item.alt || item.title || '',
          tier: item.tier || '',
          pattern: item.pattern && typeof item.pattern === 'object' ? item.pattern : null,
          visual: item.visual || '',
          readMinutes: typeof item.readMinutes === 'number' ? item.readMinutes : null,
          updated: item.updated || '',
          featured: item.featured === true,
          external: item.external === true,
          href: item.href || '',
          order: typeof item.order === 'number' ? item.order : 9999,
          status: item.status || 'published',
          _base: basePath,
          _fallback: manifest.fallbackHref || ''
        };
      })
    };
  }

  var cache = {};

  function load(name) {
    var path = MANIFESTS[name] || name;
    if (cache[path]) { return cache[path]; }
    cache[path] = A.fetchJSON(path).then(function (raw) { return normalize(raw, name); });
    return cache[path];
  }

  /* ----------------------------------------------------------------------
     Item helpers
     ---------------------------------------------------------------------- */
  // Image path resolves against the collection's basePath, e.g. assets/img/screens/
  function itemImage(item) {
    if (!item.image) { return ''; }
    if (/^https?:/.test(item.image)) { return item.image; }
    return A.url(item._base + item.image);
  }

  function itemHref(item) {
    // An explicit href always wins, so an App Store URL can be dropped into
    // the manifest later without touching any page.
    if (item.href) {
      var direct = /^https?:/.test(item.href) ? item.href : A.url(item.href);
      return item.external && A.campaignURL ? A.campaignURL(direct, 'atha-web-' + item.slug) : direct;
    }
    if (item.external) {
      var fallback = item._fallback || A.config.developerSite;
      return A.campaignURL ? A.campaignURL(fallback, 'atha-web-' + item.slug) : fallback;
    }
    return A.url(item._base + item.slug + '.html');
  }

  function isLinkable(item) {
    return item.status !== 'draft' || item.external || !!item.href;
  }

  function categoryLabel(collection, id) {
    for (var i = 0; i < collection.categories.length; i++) {
      if (collection.categories[i].id === id) { return collection.categories[i].label; }
    }
    return id;
  }

  // Human-readable cycle, e.g. "4 · 7 · 8" — omits zero phases.
  function patternLine(pattern) {
    if (!pattern) { return ''; }
    var order = ['inhale', 'holdIn', 'exhale', 'holdOut'];
    var parts = [];
    for (var i = 0; i < order.length; i++) {
      var value = pattern[order[i]];
      if (typeof value === 'number' && value > 0) { parts.push(value); }
    }
    return parts.join(' · ');
  }

  function metaLine(collection, item) {
    var parts = [];
    if (item.category) { parts.push(categoryLabel(collection, item.category)); }
    if (item.pattern) { parts.push(patternLine(item.pattern)); }
    if (item.readMinutes) { parts.push(item.readMinutes + ' min read'); }
    if (item.tier === 'premium') { parts.push('Premium'); }
    return parts.join(' · ');
  }

  function matchesSearch(item, term) {
    if (!term) { return true; }
    var haystack = [item.title, item.summary, item.intent, item.tags.join(' ')].join(' ').toLowerCase();
    return haystack.indexOf(term.toLowerCase()) !== -1;
  }

  /* ----------------------------------------------------------------------
     Query
     ---------------------------------------------------------------------- */
  function query(collection, options) {
    var opts = options || {};
    var exclude = opts.exclude
      ? (Array.isArray(opts.exclude) ? opts.exclude : String(opts.exclude).split(','))
      : [];

    var result = collection.items.filter(function (item) {
      if (item.status === 'hidden') { return false; }
      if (!opts.includeDrafts && item.status === 'draft' && !isLinkable(item)) { return false; }
      if (opts.category && opts.category !== 'all' && item.category !== opts.category) { return false; }
      if (opts.tag && item.tags.indexOf(opts.tag) === -1) { return false; }
      if (opts.featured && !item.featured) { return false; }
      if (opts.tier && opts.tier !== 'all' && item.tier !== opts.tier) { return false; }
      if (exclude.indexOf(item.slug) !== -1) { return false; }
      if (!matchesSearch(item, opts.search)) { return false; }
      return true;
    });

    result.sort(function (a, b) {
      if (a.order !== b.order) { return a.order - b.order; }
      if (a.updated && b.updated && a.updated !== b.updated) { return a.updated < b.updated ? 1 : -1; }
      return a.title.localeCompare(b.title);
    });

    if (opts.limit > 0) { result = result.slice(0, opts.limit); }
    return result;
  }

  /* ----------------------------------------------------------------------
     Templates
     ---------------------------------------------------------------------- */
  function badgeHTML(item) {
    if (item.tier === 'premium') { return '<span class="atha-badge">Premium</span>'; }
    if (item.status === 'draft') { return '<span class="atha-badge atha-badge--accent">Coming soon</span>'; }
    return '';
  }

  function gridHTML(collection, item) {
    var linkable = isLinkable(item);
    var tag = linkable ? 'a' : 'div';
    var attrs = linkable
      ? ' href="' + esc(itemHref(item)) + '"' + (item.external ? ' rel="noopener"' : '')
      : ' aria-disabled="true"';

    return '<' + tag + ' class="atha-card atha-reveal' + (linkable ? '' : ' is-inert') + '"' + attrs + '>' +
      (item.icon ? '<span class="atha-card__icon" aria-hidden="true">' + esc(item.icon) + '</span>' : '') +
      '<p class="atha-card__title">' + esc(item.title) + '</p>' +
      (item.summary ? '<p class="atha-card__text">' + esc(item.summary) + '</p>' : '') +
      (metaLine(collection, item) || badgeHTML(item)
        ? '<div class="atha-card__foot">' +
            (metaLine(collection, item) ? '<span class="atha-card__meta">' + esc(metaLine(collection, item)) + '</span>' : '') +
            badgeHTML(item) +
          '</div>'
        : '') +
      '</' + tag + '>';
  }

  function listHTML(collection, item) {
    var linkable = isLinkable(item);
    var tag = linkable ? 'a' : 'div';
    var attrs = linkable
      ? ' href="' + esc(itemHref(item)) + '"' + (item.external ? ' rel="noopener"' : '')
      : ' aria-disabled="true"';

    return '<' + tag + ' class="atha-listitem atha-reveal' + (linkable ? '' : ' is-inert') + '"' + attrs + '>' +
      '<div class="atha-listitem__body">' +
        '<p class="atha-listitem__title">' + esc(item.title) + '</p>' +
        (item.summary ? '<p class="atha-listitem__text">' + esc(item.summary) + '</p>' : '') +
      '</div>' +
      '<div class="atha-listitem__aside">' +
        (metaLine(collection, item) ? '<span class="atha-card__meta">' + esc(metaLine(collection, item)) + '</span>' : '') +
        badgeHTML(item) +
      '</div>' +
      '</' + tag + '>';
  }

  function compactHTML(collection, item) {
    var linkable = isLinkable(item);
    if (!linkable) { return '<span class="atha-chip is-inert">' + esc(item.title) + '</span>'; }
    return '<a class="atha-chip" href="' + esc(itemHref(item)) + '"' +
           (item.external ? ' rel="noopener"' : '') + '>' + esc(item.title) + '</a>';
  }

  function featureHTML(collection, item) {
    return '<div class="atha-card atha-card--feature atha-reveal">' +
      (item.icon ? '<span class="atha-card__icon" aria-hidden="true">' + esc(item.icon) + '</span>' : '') +
      '<p class="atha-card__title">' + esc(item.title) + ' ' + badgeHTML(item) + '</p>' +
      (item.summary ? '<p class="atha-card__text">' + esc(item.summary) + '</p>' : '') +
      (item.href || item.external
        ? '<a class="atha-card__link" href="' + esc(itemHref(item)) + '"' +
          (item.external ? ' rel="noopener"' : '') + '>Learn more</a>'
        : '') +
      '</div>';
  }

  // Screenshot tile — image is the content, so a missing file removes the tile
  // rather than leaving a broken frame on a marketing surface.
  function shotHTML(collection, item) {
    var src = itemImage(item);
    if (!src) { return ''; }
    return '<figure class="atha-shot atha-reveal" data-atha-shot="' + esc(item.slug) + '">' +
      '<button class="atha-shot__trigger" type="button" ' +
        'data-atha-lightbox="' + esc(src) + '" ' +
        'data-caption="' + esc(item.title) + '">' +
        '<img src="' + esc(src) + '" alt="' + esc(item.alt || item.title) + '" ' +
          'loading="lazy" decoding="async" width="390" height="844" ' +
          'onerror="this.closest(\'[data-atha-shot]\').remove()" />' +
      '</button>' +
      '<figcaption class="atha-shot__caption">' +
        '<strong>' + esc(item.title) + '</strong>' +
        (item.summary ? '<span>' + esc(item.summary) + '</span>' : '') +
      '</figcaption>' +
      '</figure>';
  }

  var LAYOUTS = {
    grid:    { render: gridHTML,    wrap: 'atha-grid atha-grid--3' },
    list:    { render: listHTML,    wrap: 'atha-list' },
    compact: { render: compactHTML, wrap: 'atha-chiprow' },
    feature: { render: featureHTML, wrap: 'atha-grid atha-grid--2' },
    shots:   { render: shotHTML,    wrap: 'atha-shots' }
  };

  /* ----------------------------------------------------------------------
     Filter + search controls
     ---------------------------------------------------------------------- */
  function controlsHTML(collection, state, showFilters, showSearch) {
    if (!showFilters && !showSearch) { return ''; }
    var html = '<div class="atha-controls">';

    if (showSearch) {
      html += '<label class="atha-search">' +
        '<span class="atha-visually-hidden">Search ' + esc(collection.title || collection.collection) + '</span>' +
        '<input class="atha-search__input" type="search" placeholder="Search…" value="' + esc(state.search || '') + '" />' +
        '</label>';
    }

    if (showFilters && collection.categories.length) {
      html += '<div class="atha-chiprow" role="group" aria-label="Filter by category">';
      html += '<button type="button" class="atha-chip' + (!state.category || state.category === 'all' ? ' is-active' : '') +
              '" data-category="all" aria-pressed="' + (!state.category || state.category === 'all') + '">All</button>';
      collection.categories.forEach(function (cat) {
        var active = state.category === cat.id;
        html += '<button type="button" class="atha-chip' + (active ? ' is-active' : '') +
                '" data-category="' + esc(cat.id) + '" aria-pressed="' + active + '">' + esc(cat.label) + '</button>';
      });
      html += '</div>';
    }

    return html + '</div>';
  }

  /* ----------------------------------------------------------------------
     Render
     ---------------------------------------------------------------------- */
  function readOptions(el) {
    function bool(name) { return el.getAttribute(name) === 'true'; }
    var limit = parseInt(el.getAttribute('data-limit'), 10);
    return {
      source:      el.getAttribute('data-atha-collection'),
      layout:      el.getAttribute('data-layout') || 'grid',
      limit:       isNaN(limit) ? 0 : limit,
      category:    el.getAttribute('data-category') || '',
      tier:        el.getAttribute('data-tier') || '',
      tag:         el.getAttribute('data-tag') || '',
      exclude:     el.getAttribute('data-exclude') || '',
      featured:    bool('data-featured'),
      filters:     bool('data-filters'),
      search:      bool('data-search'),
      includeDrafts: bool('data-include-drafts'),
      emptyTitle:  el.getAttribute('data-empty-title') || 'Nothing here yet',
      emptyText:   el.getAttribute('data-empty-text') || 'New content is being written. Check back soon.',
      hideWhenEmpty: bool('data-hide-when-empty'),
      target:      el
    };
  }

  function render(options) {
    var opts = options || {};
    var target = opts.target;
    if (!target) { return Promise.resolve(); }

    var layout = LAYOUTS[opts.layout] || LAYOUTS.grid;
    var state = { category: opts.category || 'all', search: '' };

    A.renderLoading(target, opts.limit > 0 ? Math.min(opts.limit, 3) : 3);

    return load(opts.source).then(function (collection) {
      function paint() {
        var items = query(collection, {
          category: state.category,
          tier: opts.tier,
          tag: opts.tag,
          featured: opts.featured,
          exclude: opts.exclude,
          search: state.search,
          limit: opts.limit,
          includeDrafts: opts.includeDrafts
        });

         // Sections marked hide-when-empty disappear entirely (with their wrapper)
        // rather than showing an empty state on a marketing surface.
        if (!items.length && opts.hideWhenEmpty) {
          var region = target.closest ? target.closest('[data-atha-region]') : null;
          (region || target).hidden = true;
          target.removeAttribute('aria-busy');
          return;
        }
        if (opts.hideWhenEmpty) {
          var shown = target.closest ? target.closest('[data-atha-region]') : null;
          (shown || target).hidden = false;
        }

        var body = items.length
          ? '<div class="' + layout.wrap + '">' + items.map(function (item) {
              return layout.render(collection, item);
            }).join('') + '</div>'
          : '<div class="atha-state" role="status">' +
              '<p class="atha-state__title">' + esc(opts.emptyTitle) + '</p>' +
              '<p class="atha-state__text">' + esc(opts.emptyText) + '</p></div>';

        target.innerHTML = controlsHTML(collection, state, opts.filters, opts.search) + body;
        target.removeAttribute('aria-busy');
        bindControls();
        if (A.gallery) { A.gallery.bind(target); }
        A.reveal(target);
      }

      function bindControls() {
        var chips = target.querySelectorAll('.atha-chip[data-category]');
        for (var i = 0; i < chips.length; i++) {
          chips[i].addEventListener('click', function () {
            state.category = this.getAttribute('data-category');
            paint();
          });
        }

        var input = target.querySelector('.atha-search__input');
        if (input) {
          var timer = null;
          input.addEventListener('input', function () {
            var value = this.value;
            clearTimeout(timer);
            timer = setTimeout(function () {
              state.search = value;
              paint();
              var again = target.querySelector('.atha-search__input');
              if (again) { again.focus(); again.setSelectionRange(value.length, value.length); }
            }, 180);
          });
        }
      }

      paint();
      return collection;
    }).catch(function (err) {
      if (window.console) { console.error(err); }
      A.renderState(
        target,
        'error',
        'Content could not be loaded',
        'Please refresh the page. If this keeps happening, contact ' + A.config.email + '.'
      );
      target.removeAttribute('aria-busy');
    });
  }

  /* ----------------------------------------------------------------------
     Auto-mount
     ---------------------------------------------------------------------- */
  function mountAll(scope) {
    var nodes = (scope || document).querySelectorAll('[data-atha-collection]:not([data-atha-mounted])');
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].setAttribute('data-atha-mounted', 'true');
      render(readOptions(nodes[i]));
    }
  }

  A.content = {
    load: load,
    query: query,
    render: render,
    mountAll: mountAll,
    itemHref: itemHref,
    itemImage: itemImage,
    patternLine: patternLine,
    manifests: MANIFESTS
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { mountAll(document); });
  } else {
    mountAll(document);
  }
})();