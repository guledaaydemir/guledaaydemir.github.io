/* ============================================================
   DUMP — Motion & Interaction Engine
   assets/motion.js
   Vanilla JS, no dependencies. Loaded with `defer` on every page.
   Every module is opt-in: it runs only if its markup hook exists,
   so the same file is safe on index, faq, support, legal and 404.
   Public namespace: window.DUMP  (extended by basics.js in Phase 3)
   ============================================================ */
(function () {
  'use strict';

  /* ---------- 0. Namespace & shared config ---------- */
  var DUMP = window.DUMP = window.DUMP || {};

  DUMP.config = {
    appStoreId: '6798248086',
    appStoreURL: 'https://apps.apple.com/app/id6798248086',
    instagram: 'https://instagram.com/solo.stasera',
    email: 'solostaseraofficial@gmail.com',
    headerOffset: 84,
    /* Phase 11 fills these; harmless when empty. */
    utm: { source: '', medium: '', campaign: '' }
  };

  var reduce = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  DUMP.reduce = reduce;

  /* ---------- 1. Micro helpers ---------- */
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }
  function on(el, ev, fn, opt) { if (el) el.addEventListener(ev, fn, opt || false); }
  function clamp(v, a, b) { return v < a ? a : (v > b ? b : v); }

  /* rAF-throttled scroll/resize listener */
  var frameJobs = [], ticking = false;
  function onFrame(fn) { frameJobs.push(fn); fn(); }
  function requestFrame() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      for (var i = 0; i < frameJobs.length; i++) frameJobs[i]();
      ticking = false;
    });
  }
  on(window, 'scroll', requestFrame, { passive: true });
  on(window, 'resize', requestFrame, { passive: true });

  /* Single shared IntersectionObserver factory */
  function observe(els, fn, options) {
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { fn(el, true); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          fn(e.target, false);
          if (!options || options.once !== false) io.unobserve(e.target);
        }
      });
    }, {
      threshold: (options && options.threshold) || 0.16,
      rootMargin: (options && options.rootMargin) || '0px 0px -8% 0px'
    });
    els.forEach(function (el) { io.observe(el); });
    return io;
  }
  DUMP.observe = observe;
  DUMP.$ = $; DUMP.$$ = $$;

  /* ---------- 2. Reveal on scroll ---------- */
  function initReveal() {
    var els = $$('.rv');
    if (!els.length) return;
    if (reduce) { els.forEach(function (el) { el.classList.add('in'); }); return; }
    /* Anything already inside the first viewport shows immediately —
       a hero that fades in after load reads as a broken page. */
    els.forEach(function (el) {
      if (el.getBoundingClientRect().top < window.innerHeight * 0.85) el.classList.add('in');
    });
    observe(els.filter(function (el) { return !el.classList.contains('in'); }),
      function (el) { el.classList.add('in'); });
  }

  /* ---------- 3. Header state + scroll progress ---------- */
  function initHeader() {
    var header = $('header.site');
    if (!header) return;
    var bar = $('.scrollbar');
    onFrame(function () {
      var y = window.pageYOffset || document.documentElement.scrollTop;
      header.classList.toggle('scrolled', y > 12);
      if (bar) {
        var h = document.documentElement.scrollHeight - window.innerHeight;
        bar.style.width = (h > 0 ? clamp(y / h, 0, 1) * 100 : 0) + '%';
      }
    });
  }

  /* ---------- 4. Mobile drawer ---------- */
  function initDrawer() {
    var btn = $('.navtoggle'), drawer = $('.navdrawer');
    if (!btn || !drawer) return;
    function set(open) {
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      drawer.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    }
    on(btn, 'click', function () {
      set(btn.getAttribute('aria-expanded') !== 'true');
    });
    /* Any drawer link closes it, including same-page anchors. */
    $$('a', drawer).forEach(function (a) { on(a, 'click', function () { set(false); }); });
    on(document, 'keydown', function (e) { if (e.key === 'Escape') set(false); });
    on(window, 'resize', function () { if (window.innerWidth > 860) set(false); });
  }

  /* ---------- 5. Anchor scroll with header offset ---------- */
  function initAnchors() {
    on(document, 'click', function (e) {
      var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
      if (!a) return;
      var id = a.getAttribute('href');
      if (!id || id === '#' || id.length < 2) return;
      var target = document.getElementById(id.slice(1));
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.pageYOffset - DUMP.config.headerOffset;
      window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
      history.replaceState(null, '', id);
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    });
  }

  /* ---------- 6. Scrollspy ---------- */
  function initSpy() {
    var links = $$('.navlinks a.lk[href^="#"]');
    if (!links.length) return;
    var map = links.map(function (a) {
      return { a: a, el: document.getElementById(a.getAttribute('href').slice(1)) };
    }).filter(function (m) { return m.el; });
    if (!map.length) return;
    onFrame(function () {
      var y = window.pageYOffset + DUMP.config.headerOffset + 40, current = null;
      map.forEach(function (m) { if (m.el.offsetTop <= y) current = m; });
      map.forEach(function (m) { m.a.classList.toggle('active', m === current); });
    });
  }

  /* ---------- 7. Count-up stats ---------- */
  function initCounters() {
    var els = $$('[data-count]');
    if (!els.length) return;
    observe(els, function (el) {
      var target = parseFloat(el.getAttribute('data-count')) || 0;
      var dec = (el.getAttribute('data-dec') | 0);
      var prefix = el.getAttribute('data-prefix') || '';
      var suffix = el.getAttribute('data-suffix') || '';
      if (reduce) { el.textContent = prefix + target.toFixed(dec) + suffix; return; }
      var dur = 1400, t0 = performance.now();
      (function step(t) {
        var p = clamp((t - t0) / dur, 0, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = prefix + (target * eased).toFixed(dec) + suffix;
        if (p < 1) requestAnimationFrame(step);
      })(t0);
    });
  }

  /* ---------- 8. Magnetic buttons ---------- */
  function initMagnet() {
    if (reduce || !window.matchMedia('(hover:hover)').matches) return;
    $$('.magnet').forEach(function (el) {
      on(el, 'mousemove', function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) * 0.22;
        var y = (e.clientY - r.top - r.height / 2) * 0.32;
        el.style.transform = 'translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px)';
      });
      on(el, 'mouseleave', function () { el.style.transform = ''; });
    });
  }

  /* ---------- 9. Accordion ---------- */
  function initAccordion() {
    var items = $$('.acc-item');
    if (!items.length) return;

    function close(item) {
      item.classList.remove('open');
      var q = $('.acc-q', item), a = $('.acc-a', item);
      if (q) q.setAttribute('aria-expanded', 'false');
      if (a) a.style.maxHeight = '';
    }
    function open(item) {
      item.classList.add('open');
      var q = $('.acc-q', item), a = $('.acc-a', item);
      if (q) q.setAttribute('aria-expanded', 'true');
      if (a) a.style.maxHeight = a.scrollHeight + 'px';
    }
    DUMP.openAccordion = open;

    items.forEach(function (item, i) {
      var q = $('.acc-q', item), a = $('.acc-a', item);
      if (!q || !a) return;
      var id = item.id || ('q-' + (i + 1));
      item.id = id;
      a.id = id + '-a';
      q.setAttribute('aria-expanded', 'false');
      q.setAttribute('aria-controls', a.id);
      on(q, 'click', function () {
        var isOpen = item.classList.contains('open');
        /* One panel at a time inside a group keeps the page from
           jumping metres down on a long FAQ. */
        var group = item.closest('.acc');
        if (group && !group.hasAttribute('data-multi')) {
          $$('.acc-item.open', group).forEach(close);
        }
        isOpen ? close(item) : open(item);
      });
    });

    /* Reflow open panels when the text rewraps. */
    on(window, 'resize', function () {
      $$('.acc-item.open .acc-a').forEach(function (a) { a.style.maxHeight = a.scrollHeight + 'px'; });
    });

    /* Deep link: /faq.html#q-quality opens and scrolls to that answer. */
    if (location.hash.length > 1) {
      var target = document.getElementById(location.hash.slice(1));
      if (target && target.classList.contains('acc-item')) {
        open(target);
        setTimeout(function () {
          window.scrollTo({
            top: target.getBoundingClientRect().top + window.pageYOffset - DUMP.config.headerOffset,
            behavior: 'auto'
          });
        }, 60);
      }
    }
  }

  /* ---------- 10. Category filter (FAQ / support) ---------- */
  function initFilter() {
    var chips = $$('[data-filter]');
    if (!chips.length) return;
    chips.forEach(function (chip) {
      on(chip, 'click', function () {
        var key = chip.getAttribute('data-filter');
        chips.forEach(function (c) {
          var isOn = c === chip;
          c.classList.toggle('on', isOn);
          c.setAttribute('aria-pressed', isOn ? 'true' : 'false');
        });
        $$('[data-cat]').forEach(function (item) {
          var show = key === 'all' || item.getAttribute('data-cat') === key;
          item.style.display = show ? '' : 'none';
        });
      });
    });
  }

  /* ---------- 11. Marquee ---------- */
  function initMarquee() {
    $$('.marquee-track').forEach(function (track) {
      if (reduce) { track.style.animation = 'none'; return; }
      /* Duplicated once so the -50% keyframe loops with no visible seam. */
      track.innerHTML += track.innerHTML;
    });
  }

  /* ---------- 12. Screenshot gallery ---------- */
  function initShots() {
    /* A missing PNG must not leave a broken-image icon: the styled
       placeholder underneath stays visible until the file exists. */
    $$('.shot .fr img').forEach(function (img) {
      function fail() { img.style.display = 'none'; }
      on(img, 'error', fail);
      if (img.complete && img.naturalWidth === 0) fail();
      else img.addEventListener('load', function () {
        var ph = img.parentNode.querySelector('.ph');
        if (ph) ph.style.display = 'none';
      });
    });

    /* Drag-to-scroll on pointer devices; native swipe untouched on touch. */
    $$('.shots').forEach(function (rail) {
      var down = false, startX = 0, startL = 0;
      on(rail, 'pointerdown', function (e) {
        if (e.pointerType === 'touch') return;
        down = true; startX = e.clientX; startL = rail.scrollLeft;
        rail.style.cursor = 'grabbing';
      });
      on(window, 'pointerup', function () { down = false; rail.style.cursor = ''; });
      on(rail, 'pointermove', function (e) {
        if (!down) return;
        e.preventDefault();
        rail.scrollLeft = startL - (e.clientX - startX);
      });
    });
  }

  /* ---------- 13. Sticky mobile download bar ---------- */
  function initStickyBar() {
    var bar = $('.stickybar');
    if (!bar) return;
    /* Appears only once the hero CTA has left the screen, so it never
       competes with the primary button. */
    var anchor = $('#top') || $('.hero') || document.body;
    onFrame(function () {
      var past = (window.pageYOffset || 0) > (anchor.offsetHeight || 400) * 0.7;
      var atEnd = (window.innerHeight + window.pageYOffset) >
        (document.documentElement.scrollHeight - 220);
      bar.classList.toggle('show', past && !atEnd);
    });
  }

  /* ---------- 14. Store links, UTM & outbound safety ---------- */
  function initLinks() {
    $$('a[href*="apps.apple.com"]').forEach(function (a) {
      /* Apple attributes installs by campaign token. Each link declares its
         own placement via data-ct, so App Store Connect shows which section
         of the site actually converts. */
      var ct = a.getAttribute('data-ct') || 'web-' + (document.body.dataset.page || 'home');
      if (a.href.indexOf('ct=') < 0) {
        a.href += (a.href.indexOf('?') > -1 ? '&' : '?') + 'ct=' + encodeURIComponent(ct);
      }
      a.setAttribute('rel', 'noopener');
      a.setAttribute('target', '_blank');
      on(a, 'click', function () { DUMP.track('app_store_click', { href: a.href }); });
    });
    $$('a[target="_blank"]').forEach(function (a) {
      if (!a.getAttribute('rel')) a.setAttribute('rel', 'noopener noreferrer');
    });
  }

  /* ---------- 15. Copy to clipboard ---------- */
  function initCopy() {
    $$('[data-copy]').forEach(function (el) {
      on(el, 'click', function (e) {
        e.preventDefault();
        var text = el.getAttribute('data-copy') || el.textContent.trim();
        var done = function () {
          var old = el.getAttribute('data-label') || el.textContent;
          el.setAttribute('data-label', old);
          el.textContent = 'Copied';
          setTimeout(function () { el.textContent = old; }, 1800);
        };
        if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () { });
        else {
          var ta = document.createElement('textarea');
          ta.value = text; document.body.appendChild(ta); ta.select();
          try { document.execCommand('copy'); done(); } catch (err) { }
          document.body.removeChild(ta);
        }
      });
    });
  }

  /* ---------- 16. Year stamp ---------- */
  function initYear() {
    $$('[data-year], #yr').forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  /* ---------- 17. Analytics hook (Phase 11 binds a provider) ---------- */
  DUMP.track = function (event, payload) {
    if (typeof window.gtag === 'function') window.gtag('event', event, payload || {});
    if (window.DUMP_DEBUG) console.log('[track]', event, payload || {});
  };

  /* ---------- 18. Boot ---------- */
  function boot() {
    initHeader();
    initDrawer();
    initAnchors();
    initSpy();
    initReveal();
    initCounters();
    initMagnet();
    initAccordion();
    initFilter();
    initMarquee();
    initShots();
    initStickyBar();
    initLinks();
    initCopy();
    initYear();
    document.documentElement.classList.add('js-ready');
    requestFrame();
  }

  if (document.readyState === 'loading') on(document, 'DOMContentLoaded', boot);
  else boot();
})();
