/* ==========================================================================
   ATHA — Site runtime
   Injects header/footer, mounts brand visuals, resolves paths, and exposes
   shared helpers (fetchJSON, reveal) for later content-driven pages.
   Loaded with: <script src="<root>assets/js/atha.js" defer></script>
   ========================================================================== */
(function () {
  'use strict';

  /* ----------------------------------------------------------------------
     Configuration — the single place site structure is declared.
     Adding a new section here updates the header and footer everywhere.
     ---------------------------------------------------------------------- */
  var CONFIG = {
    brand: 'ATHA',
    tagline: 'ATHA means now. Breathe now.',
    author: 'Gül Eda Aydemir',
    email: 'guledaaydemir@gmail.com',
    developerSite: 'https://guledaaydemir.github.io/',
    appStoreURL: 'https://apps.apple.com/app/atha',
    campaign: '?utm_source=atha-web&utm_medium=referral',
    nav: [
      { label: 'Features',    href: 'features/' },
      { label: 'Guides',      href: 'guides/' },
      { label: 'Meditations', href: 'meditations/' },
      { label: 'Support',     href: 'support.html' }
    ],
    footer: [
      { label: 'Home',        href: 'index.html' },
      { label: 'Features',    href: 'features/' },
      { label: 'Guides',      href: 'guides/' },
      { label: 'Meditations', href: 'meditations/' },
      { label: 'Screenshots', href: 'press/' },
      { label: 'Other apps',  href: 'apps/' },
      { label: 'Support',     href: 'support.html' },
      { label: 'Privacy',     href: 'privacypolicy.html' }
    ]
  };

  /* ----------------------------------------------------------------------
     Path resolution — derived from this script's own URL so every page
     works identically at site root and inside guides/ or meditations/.
     ---------------------------------------------------------------------- */
  function resolveRoot() {
    var el = document.currentScript;
    if (!el) {
      var all = document.getElementsByTagName('script');
      for (var i = all.length - 1; i >= 0; i--) {
        if (/assets\/js\/atha\.js/.test(all[i].src)) { el = all[i]; break; }
      }
    }
    if (!el || !el.src) { return './'; }
    return el.src.replace(/assets\/js\/atha\.js.*$/, '');
  }

  var ROOT = resolveRoot();

  function url(path) {
    if (!path) { return ROOT; }
    if (/^(https?:)?\/\//.test(path) || path.charAt(0) === '#' || /^mailto:/.test(path)) { return path; }
    return ROOT + path.replace(/^\//, '');
  }

  // Appends campaign parameters to any outbound URL without breaking an
  // existing query string or fragment.
  function campaignURL(base, source, medium) {
    if (!base || /^(mailto:|#)/.test(base)) { return base; }
    var hash = '';
    var hashAt = base.indexOf('#');
    if (hashAt !== -1) { hash = base.slice(hashAt); base = base.slice(0, hashAt); }
    var join = base.indexOf('?') === -1 ? '?' : '&';
    var params = 'utm_source=atha-web&utm_medium=' + encodeURIComponent(medium || 'referral');
    if (source) { params += '&utm_campaign=' + encodeURIComponent(source); }
    return base + join + params + hash;
  }

  function storeURL(campaignSource) {
    return campaignURL(CONFIG.appStoreURL, campaignSource, 'referral');
  }

  /* ----------------------------------------------------------------------
     Active section detection
     ---------------------------------------------------------------------- */
  function currentPath() {
    var p = window.location.pathname.replace(/\/index\.html$/, '/');
    return p.charAt(p.length - 1) === '/' ? p : p;
  }

  function isActive(href) {
    if (/^https?:/.test(href)) { return false; }
    var here = currentPath();
    if (href === 'index.html') { return /\/$|\/index\.html$/.test(here) && !/\/(guides|meditations|features|press|apps)\//.test(here); }
    var section = href.replace(/\/$/, '');
    if (href.slice(-1) === '/') { return here.indexOf('/' + section + '/') !== -1; }
    return here.indexOf(href) !== -1;
  }

  /* ----------------------------------------------------------------------
     Brand visuals
     ---------------------------------------------------------------------- */
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

  /* ----------------------------------------------------------------------
     Header
     ---------------------------------------------------------------------- */
  function navMarkup(docType) {
    if (docType) {
      return '<span class="atha-doc-type">' + docType + '</span>';
    }
    var links = CONFIG.nav.map(function (item) {
      return '<a class="atha-nav__link" href="' + url(item.href) + '"' +
             (isActive(item.href) ? ' aria-current="page"' : '') + '>' + item.label + '</a>';
    }).join('');
    return '<button class="atha-nav__toggle" type="button" aria-expanded="false" aria-controls="atha-nav" aria-label="Menu">☰</button>' +
           '<nav class="atha-nav" id="atha-nav" aria-label="Primary">' + links +
           '<a class="atha-btn atha-btn--primary" data-atha-store="nav" href="' + storeURL('nav') + '">Get ATHA</a></nav>';
  }

  function mountHeader() {
    var host = document.querySelector('[data-atha-header]');
    if (!host) { return; }
    var docType = host.getAttribute('data-atha-header');
    host.outerHTML =
      '<a class="atha-skip" href="#atha-main">Skip to content</a>' +
      '<header class="atha-header"><div class="atha-container atha-header__inner">' +
      '<a class="atha-logo" href="' + url('index.html') + '" aria-label="ATHA home">' + CONFIG.brand + '</a>' +
      navMarkup(docType && docType !== 'true' ? docType : null) +
      '</div></header>';

    var toggle = document.querySelector('.atha-nav__toggle');
    var nav = document.getElementById('atha-nav');
    if (toggle && nav) {
      toggle.addEventListener('click', function () {
        var open = nav.classList.toggle('is-open');
        toggle.setAttribute('aria-expanded', String(open));
        toggle.textContent = open ? '✕' : '☰';
      });
      nav.addEventListener('click', function (e) {
        if (e.target.tagName === 'A' && nav.classList.contains('is-open')) {
          nav.classList.remove('is-open');
          toggle.setAttribute('aria-expanded', 'false');
          toggle.textContent = '☰';
        }
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && nav.classList.contains('is-open')) { toggle.click(); }
      });
    }
  }

  /* ----------------------------------------------------------------------
     Footer
     ---------------------------------------------------------------------- */
  function mountFooter() {
    var host = document.querySelector('[data-atha-footer]');
    if (!host) { return; }
    var links = CONFIG.footer.map(function (item) {
      return '<a href="' + url(item.href) + '"' +
             (item.external ? ' rel="noopener"' : '') + '>' + item.label + '</a>';
    }).join('');
    host.outerHTML =
      '<footer class="atha-footer"><div class="atha-container atha-footer__inner">' +
      '<div><span>© ' + new Date().getFullYear() + ' ' + CONFIG.brand + ' · ' + CONFIG.author + '</span>' +
      '<div class="atha-footer__tagline">' + CONFIG.tagline + '</div></div>' +
      '<div class="atha-footer__links">' + links + '</div>' +
      '</div></footer>';
  }

  /* ----------------------------------------------------------------------
     Static crawl path — real anchors present in the DOM for every page,
     so the site remains fully traversable when the content renderer does
     not run. Visually hidden; never a duplicate of the visible footer nav
     for assistive tech, which reads the footer links instead.
     ---------------------------------------------------------------------- */
  function mountCrawlPath() {
    if (document.getElementById('atha-crawl')) { return; }
    var links = CONFIG.footer.concat([
      { label: 'Developer portfolio', href: CONFIG.developerSite, external: true }
    ]).map(function (item) {
      return '<a href="' + url(item.href) + '"' + (item.external ? ' rel="noopener"' : '') + '>' + item.label + '</a>';
    }).join(' ');

    var nav = document.createElement('nav');
    nav.id = 'atha-crawl';
    nav.className = 'atha-visually-hidden';
    nav.setAttribute('aria-hidden', 'true');
    nav.innerHTML = links;
    document.body.appendChild(nav);
  }

  /* ----------------------------------------------------------------------
     Store links declared in page markup
     ---------------------------------------------------------------------- */
  function bindStoreLinks(scope) {
    var nodes = (scope || document).querySelectorAll('[data-atha-store]');
    for (var i = 0; i < nodes.length; i++) {
      var source = nodes[i].getAttribute('data-atha-store') || 'site';
      nodes[i].setAttribute('href', storeURL(source));
      nodes[i].setAttribute('rel', 'noopener');
    }
  }

  /* ----------------------------------------------------------------------
     Outbound click signal — a hook other analytics can listen to. No data
     leaves the page here; it only dispatches a DOM event.
     ---------------------------------------------------------------------- */
  function bindOutboundTracking() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest ? e.target.closest('a[href]') : null;
      if (!link) { return; }
      var href = link.getAttribute('href') || '';
      if (!/^https?:/.test(href)) { return; }
      if (href.indexOf(window.location.host) !== -1) { return; }

      var kind = link.hasAttribute('data-atha-store') ? 'appstore'
               : /guledaaydemir\.github\.io/.test(href) ? 'developer'
               : 'external';

      document.dispatchEvent(new CustomEvent('atha:outbound', {
        detail: {
          kind: kind,
          source: link.getAttribute('data-atha-store') || link.getAttribute('data-atha-outbound') || '',
          href: href,
          path: window.location.pathname
        }
      }));
    }, true);
  }

  /* ----------------------------------------------------------------------
     Reveal on scroll — no-op under Reduce Motion or without IO support
     ---------------------------------------------------------------------- */
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

  /* ----------------------------------------------------------------------
     JSON helper — used from Phase 2 onward by content manifests
     ---------------------------------------------------------------------- */
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

  /* ----------------------------------------------------------------------
     Shared DOM helpers
     ---------------------------------------------------------------------- */
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

  /* ----------------------------------------------------------------------
     Public API
     ---------------------------------------------------------------------- */
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

  /* ----------------------------------------------------------------------
     Boot
     ---------------------------------------------------------------------- */
  function init() {
    mountAurora();
    mountHeader();
    mountFooter();
    bindStoreLinks(document);
    bindOutboundTracking();
    mountCrawlPath();
    reveal(document);
    document.documentElement.setAttribute('data-atha-ready', 'true');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();