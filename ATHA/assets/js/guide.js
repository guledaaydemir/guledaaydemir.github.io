/* ==========================================================================
   ATHA — Guide runtime
   Builds the table of contents from the article's own h2 headings.
   Byline, dates and related guides are static HTML in each guide.
   ========================================================================== */
(function () {
  'use strict';

  function slugify(text) {
    return String(text).toLowerCase()
      .replace(/[^\w\s-]/g, '')
      .trim()
      .replace(/\s+/g, '-')
      .slice(0, 60);
  }

  function escapeHTML(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

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
      links.push('<li><a href="#' + id + '">' + escapeHTML(h.textContent) + '</a></li>');
    }

    toc.hidden = false;
    toc.innerHTML =
      '<p class="atha-toc__label">On this page</p>' +
      '<nav aria-label="Table of contents"><ol>' + links.join('') + '</ol></nav>';
  }

  function init() {
    var article = document.querySelector('[data-atha-guide]');
    if (article) { buildTOC(article); }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
