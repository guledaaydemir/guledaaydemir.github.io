/* ==========================================================================
   ATHA — Sticky App Store CTA (mobile)
   Appears only after the reader has engaged, stays dismissible for the
   session, and never covers the page's own closing CTA.
   Opt out per page with: <body data-atha-stickycta="off">
   ========================================================================== */
(function () {
  'use strict';

  var A = window.ATHA;
  if (!A) { return; }

  var DISMISS_KEY = 'atha-stickycta-dismissed';
  var SHOW_AFTER = 0.28;   // fraction of page scrolled before appearing

  function dismissed() {
    try { return window.sessionStorage.getItem(DISMISS_KEY) === '1'; }
    catch (e) { return false; }
  }

  function remember() {
    try { window.sessionStorage.setItem(DISMISS_KEY, '1'); } catch (e) {}
  }

  function init() {
    if (document.body.getAttribute('data-atha-stickycta') === 'off') { return; }
    if (dismissed()) { return; }
    if (!window.matchMedia || !window.matchMedia('(max-width: 640px)').matches) { return; }

    var source = document.body.getAttribute('data-atha-cta-source') || 'sticky';
    // Turkish pages: Turkish copy and the Turkish App Store link.
    var tr = document.documentElement.lang === 'tr';
    var T = tr
      ? { label: 'ATHA\u2019yı indir', title: 'ATHA şimdi demek.', text: 'Ücretsiz · Hesap yok · Veriler Toplanmaz',
          cta: 'Ücretsiz indir', dismiss: 'Kapat', href: 'https://apps.apple.com/tr/app/id6807887691' }
      : { label: 'Get ATHA', title: 'ATHA means now.', text: 'Free · No account · Data Not Collected',
          cta: 'Get ATHA', dismiss: 'Dismiss', href: A.config.appStoreURL };

    var bar = document.createElement('div');
    bar.className = 'atha-stickycta';
    bar.setAttribute('role', 'complementary');
    bar.setAttribute('aria-label', T.label);
    bar.innerHTML =
      '<div class="atha-stickycta__body">' +
        '<span class="atha-stickycta__title">' + T.title + '</span>' +
        '<span class="atha-stickycta__text">' + T.text + '</span>' +
      '</div>' +
      '<a class="atha-btn atha-btn--primary" href="' + T.href + '" data-atha-store="' + source + '">' + T.cta + '</a>' +
      '<button class="atha-stickycta__dismiss" type="button" aria-label="' + T.dismiss + '">✕</button>';

    document.body.appendChild(bar);
    document.body.classList.add('atha-has-stickycta');
    A.bindStoreLinks(bar);

    bar.querySelector('.atha-stickycta__dismiss').addEventListener('click', function () {
      bar.classList.remove('is-visible');
      remember();
      window.setTimeout(function () {
        bar.remove();
        document.body.classList.remove('atha-has-stickycta');
      }, 400);
    });

    // Hide while the page's own closing CTA is on screen, so the two never
    // compete for the same tap.
    var bands = document.querySelectorAll('.atha-ctaband');
    var closing = bands.length ? bands[bands.length - 1] : null;
    var closingVisible = false;

    if (closing && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        closingVisible = entries[0].isIntersecting;
        update();
      }, { threshold: .2 }).observe(closing);
    }

    function update() {
      var doc = document.documentElement;
      var scrollable = doc.scrollHeight - window.innerHeight;
      var progress = scrollable > 0 ? window.pageYOffset / scrollable : 0;
      var shouldShow = progress > SHOW_AFTER && !closingVisible;
      bar.classList.toggle('is-visible', shouldShow);
    }

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) { return; }
      ticking = true;
      window.requestAnimationFrame(function () { update(); ticking = false; });
    }, { passive: true });

    update();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();