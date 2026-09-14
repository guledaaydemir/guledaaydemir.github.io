/* ==========================================================================
   ATHA — Guide runtime
   Builds the table of contents from the article's own headings, links the
   current guide to its manifest entry, and renders related guides.

   Page declares identity once:
     <article class="atha-article" data-atha-guide="slug" data-collection="guides">
   ========================================================================== */
(function () {
  'use strict';

  var A = window.ATHA;
  if (!A || !A.content) {
    if (window.console) { console.error('ATHA: guide.js requires atha.js and content.js'); }
    return;
  }

  function slugify(text) {
    return String(text).toLowerCase()
      .replace(/[^\w\s-]/g, '')
      .trim()
      .replace(/\s+/g, '-')
      .slice(0, 60);
  }

  /* ----------------------------------------------------------------------
     Table of contents — generated from h2 elements in the article body.
     Hidden automatically when the article is too short to need one.
     ---------------------------------------------------------------------- */
  function buildTOC(article) {
    var toc = article.querySelector('[data-atha-toc]');
    if (!toc) { return; }

    var body = article.querySelector('.atha-article__body');
    var headings = body ? body.querySelectorAll('h2') : [];
    var minimum = parseInt(toc.getAttribute('data-min') || '3', 10);

    if (headings.length < minimum) { toc.hidden = true; return; }

    var used = {};
    var links = [];

    for (var i = 0; i < headings.length; i++) {
      var h = headings[i];
      var id = h.id || slugify(h.textContent);
      if (used[id]) { id = id + '-' + i; }
      used[id] = true;
      h.id = id;
      links.push('<li><a href="#' + id + '">' + A.escapeHTML(h.textContent) + '</a></li>');
    }

    toc.hidden = false;
    toc.innerHTML =
      '<p class="atha-toc__label">On this page</p>' +
      '<nav aria-label="Table of contents"><ol>' + links.join('') + '</ol></nav>';
  }

  /* ----------------------------------------------------------------------
     Meta line — read time, category and updated date come from the manifest
     so a guide's metadata is never duplicated in two places.
     ---------------------------------------------------------------------- */
  function fillMeta(article, collection, entry) {
    var host = article.querySelector('[data-atha-meta]');
    if (!host || !entry) { return; }

    var parts = [];
    if (entry.category) {
      var label = entry.category;
      for (var i = 0; i < collection.categories.length; i++) {
        if (collection.categories[i].id === entry.category) { label = collection.categories[i].label; }
      }
      parts.push('<span>' + A.escapeHTML(label) + '</span>');
    }
    if (entry.pattern) {
      var cycle = A.content.patternLine(entry.pattern);
      if (cycle) { parts.push('<span>' + A.escapeHTML(cycle) + '</span>'); }
    }
    if (entry.visual) { parts.push('<span>' + A.escapeHTML(entry.visual) + ' visual</span>'); }
    if (entry.readMinutes) { parts.push('<span>' + entry.readMinutes + ' min read</span>'); }
    if (entry.updated) {
      parts.push('<span>Updated <time datetime="' + A.escapeHTML(entry.updated) + '">' +
                 A.escapeHTML(formatDate(entry.updated)) + '</time></span>');
    }
    host.innerHTML = parts.join('');
  }

  function formatDate(iso) {
    var d = new Date(iso + 'T00:00:00');
    if (isNaN(d.getTime())) { return iso; }
    return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
  }

  /* ----------------------------------------------------------------------
     Related guides — same category first, topped up from the collection.
     ---------------------------------------------------------------------- */
  function renderRelated(article, source, slug, entry) {
    var host = article.querySelector('[data-atha-related]');
    if (!host) { return; }

    var limit = parseInt(host.getAttribute('data-limit') || '3', 10);

    A.content.render({
      source: source,
      target: host,
      layout: 'list',
      limit: limit,
      category: entry && entry.category ? entry.category : '',
      exclude: slug,
      includeDrafts: false,
      hideWhenEmpty: true
    });
  }

  /* ----------------------------------------------------------------------
     Boot
     ---------------------------------------------------------------------- */
  function init() {
    var article = document.querySelector('[data-atha-guide]');
    if (!article) { return; }

    var slug = article.getAttribute('data-atha-guide');
    var source = article.getAttribute('data-collection') || 'guides';

    buildTOC(article);

    A.content.load(source).then(function (collection) {
      var entry = null;
      for (var i = 0; i < collection.items.length; i++) {
        if (collection.items[i].slug === slug) { entry = collection.items[i]; break; }
      }
      fillMeta(article, collection, entry);
      renderRelated(article, source, slug, entry);
    }).catch(function (err) {
      if (window.console) { console.warn('ATHA: guide metadata unavailable', err); }
      var host = article.querySelector('[data-atha-related]');
      if (host) { host.hidden = true; }
    });

    A.reveal(article);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();