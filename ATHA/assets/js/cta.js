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

    var bar = document.createElement('div');
    bar.className = 'atha-stickycta';
    bar.setAttribute('role', 'complementary');
    bar.setAttribute('aria-label', 'Get ATHA');
    bar.innerHTML =
      '<div class="atha-stickycta__body">' +
        '<span class="atha-stickycta__title">ATHA means now.</span>' +
        '<span class="atha-stickycta__text">Free · No ads · No account</span>' +
      '</div>' +
      '<a class="atha-btn atha-btn--primary" data-atha-store="' + source + '">Get ATHA</a>' +
      '<button class="atha-stickycta__dismiss" type="button" aria-label="Dismiss">✕</button>';

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
    var closing = document.querySelector('.atha-ctaband:last-of-type');
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