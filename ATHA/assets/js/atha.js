/* ==========================================================================
   ATHA — Site runtime
   The header, footer, lists and every App Store link are plain HTML in each
   page, so the site works without JavaScript and crawlers see everything.
   This script only adds enhancements: the phone menu toggle, the aurora
   background, reveal-on-scroll, and shared helpers for content.js.
   Loaded with: <script src="/ATHA/assets/js/atha.js" defer></script>
   ========================================================================== */
(function () {
  'use strict';

  var CONFIG = {
    brand: 'ATHA',
    tagline: 'ATHA means now. Breathe now.',
    author: 'Gül Eda Aydemir',
    email: 'solostaseraofficial@gmail.com',
    developerSite: 'https://guledaaydemir.github.io/',
    // Real App Store URL (id6807887691). Apple ignores utm_* parameters; use
    // App Store Connect campaign links (pt / ct) in the HTML if needed.
    appStoreURL: 'https://apps.apple.com/app/id6807887691'
  };

  /* Path resolution — derived from this script's own URL. */
  function resolveRoot() {
    var el = document.currentScript;
    if (!el) {
      var all = document.getElementsByTagName('script');
      for (var i = all.length - 1; i >= 0; i--) {
        if (/assets\/js\/atha\.js/.test(all[i].src)) { el = all[i]; break; }
      }
    }
    if (!el || !el.src) { return '/ATHA/'; }
    return el.src.replace(/assets\/js\/atha\.js.*$/, '');
  }

  var ROOT = resolveRoot();

  function url(path) {
    if (!path) { return ROOT; }
    if (/^(https?:)?\/\//.test(path) || path.charAt(0) === '#' || /^mailto:/.test(path)) { return path; }
    return ROOT + path.replace(/^\//, '');
  }

  // Kept for content.js. Outbound links are no longer decorated with UTM tags.
  function campaignURL(base) { return base; }
  function storeURL() { return CONFIG.appStoreURL; }

  /* Brand visuals */
  function mountAurora() {
    if (document.querySelector('.atha-aurora')) { return; }
    if (document.body.hasAttribute('data-atha-aurora-off')) { return; }
    var layer = document.createElement('div');
    layer.className = 'atha-aurora';
    layer.setAttribute('aria-hidden', 'true');
    layer.innerHTML =
      '<span class="atha-aurora__band atha-aurora__band--1"></span>' +
      '<span class="atha-aurora__band atha-aurora__band--2"></span>' +
      '<span class="atha-aurora__band atha-aurora__band--3"></span>' +
      '<span class="atha-aurora__veil"></span>';
    document.body.insertBefore(layer, document.body.firstChild);
  }

  /* Phone menu for the static header */
  function bindMenu() {
    var toggle = document.querySelector('.atha-nav__toggle');
    var nav = document.getElementById('atha-nav');
    if (!toggle || !nav) { return; }

    function set(open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      var tr = document.documentElement.lang === 'tr';
      toggle.setAttribute('aria-label', open ? (tr ? 'Menüyü kapat' : 'Close menu') : (tr ? 'Menüyü aç' : 'Open menu'));
      toggle.innerHTML = open ? '&#10005;' : '&#9776;';
    }

    toggle.addEventListener('click', function () { set(!nav.classList.contains('is-open')); });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && nav.classList.contains('is-open')) { set(false); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { set(false); toggle.focus(); }
    });
  }

  /* Any store link without an href (older markup) gets the real URL. */
  function bindStoreLinks(scope) {
    var nodes = (scope || document).querySelectorAll('[data-atha-store]');
    for (var i = 0; i < nodes.length; i++) {
      if (!nodes[i].getAttribute('href')) { nodes[i].setAttribute('href', CONFIG.appStoreURL); }
    }
  }

  /* Reveal on scroll — only for elements that opt in; no-op under Reduce Motion */
  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function reveal(scope) {
    var nodes = (scope || document).querySelectorAll('.atha-reveal:not(.is-visible)');
    if (!nodes.length) { return; }
    if (reducedMotion || !('IntersectionObserver' in window)) {
      for (var i = 0; i < nodes.length; i++) { nodes[i].classList.add('is-visible'); }
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, index) {
        if (!entry.isIntersecting) { return; }
        var delay = Math.min(index * 70, 280);
        setTimeout(function () { entry.target.classList.add('is-visible'); }, delay);
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    for (var j = 0; j < nodes.length; j++) { io.observe(nodes[j]); }
  }

  /* JSON + DOM helpers (used by content.js) */
  var jsonCache = {};

  function fetchJSON(path) {
    var target = url(path);
    if (jsonCache[target]) { return jsonCache[target]; }
    jsonCache[target] = fetch(target, { cache: 'no-cache' }).then(function (res) {
      if (!res.ok) { throw new Error('ATHA: failed to load ' + target + ' (' + res.status + ')'); }
      return res.json();
    }).catch(function (err) {
      delete jsonCache[target];
      throw err;
    });
    return jsonCache[target];
  }

  function escapeHTML(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function renderState(target, kind, title, text) {
    if (!target) { return; }
    target.innerHTML =
      '<div class="atha-state" role="status" data-state="' + kind + '">' +
      '<p class="atha-state__title">' + escapeHTML(title) + '</p>' +
      '<p class="atha-state__text">' + escapeHTML(text) + '</p></div>';
  }

  function renderLoading(target, count) {
    if (!target) { return; }
    var html = '';
    for (var i = 0; i < (count || 3); i++) { html += '<div class="atha-skeleton" aria-hidden="true"></div>'; }
    target.innerHTML = html;
    target.setAttribute('aria-busy', 'true');
  }

  window.ATHA = {
    config: CONFIG,
    root: ROOT,
    url: url,
    storeURL: storeURL,
    campaignURL: campaignURL,
    bindStoreLinks: bindStoreLinks,
    fetchJSON: fetchJSON,
    reveal: reveal,
    escapeHTML: escapeHTML,
    renderState: renderState,
    renderLoading: renderLoading,
    reducedMotion: reducedMotion
  };

  function init() {
    mountAurora();
    bindMenu();
    bindStoreLinks(document);
    reveal(document);
    document.documentElement.setAttribute('data-atha-ready', 'true');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
