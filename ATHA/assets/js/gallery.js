/* ==========================================================================
   ATHA — Screenshot lightbox
   Binds any [data-atha-lightbox] trigger. Works with screenshots rendered by
   content.js and with hand-written markup on the press page.
   ========================================================================== */
(function () {
  'use strict';

  var A = window.ATHA;
  if (!A) { return; }

  var overlay = null;
  var items = [];
  var index = 0;
  var lastFocused = null;

  function build() {
    if (overlay) { return overlay; }
    overlay = document.createElement('div');
    overlay.className = 'atha-lightbox';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Screenshot viewer');
    overlay.hidden = true;
    overlay.innerHTML =
      '<button class="atha-lightbox__close" type="button" aria-label="Close">✕</button>' +
      '<button class="atha-lightbox__nav atha-lightbox__nav--prev" type="button" aria-label="Previous screenshot">‹</button>' +
      '<button class="atha-lightbox__nav atha-lightbox__nav--next" type="button" aria-label="Next screenshot">›</button>' +
      '<figure class="atha-lightbox__figure">' +
        '<img alt="" />' +
        '<figcaption class="atha-lightbox__caption"></figcaption>' +
      '</figure>';
    document.body.appendChild(overlay);

    overlay.querySelector('.atha-lightbox__close').addEventListener('click', close);
    overlay.querySelector('.atha-lightbox__nav--prev').addEventListener('click', function () { step(-1); });
    overlay.querySelector('.atha-lightbox__nav--next').addEventListener('click', function () { step(1); });
    overlay.addEventListener('click', function (e) { if (e.target === overlay) { close(); } });

    document.addEventListener('keydown', function (e) {
      if (overlay.hidden) { return; }
      if (e.key === 'Escape') { close(); }
      else if (e.key === 'ArrowLeft') { step(-1); }
      else if (e.key === 'ArrowRight') { step(1); }
      else if (e.key === 'Tab') { trapFocus(e); }
    });

    return overlay;
  }

  function trapFocus(e) {
    var focusables = overlay.querySelectorAll('button');
    if (!focusables.length) { return; }
    var first = focusables[0];
    var last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  function paint() {
    var item = items[index];
    if (!item) { return; }
    var img = overlay.querySelector('img');
    img.setAttribute('src', item.src);
    img.setAttribute('alt', item.alt || item.caption || '');
    overlay.querySelector('.atha-lightbox__caption').textContent =
      item.caption + (items.length > 1 ? ' · ' + (index + 1) + ' / ' + items.length : '');

    var multiple = items.length > 1;
    overlay.querySelector('.atha-lightbox__nav--prev').hidden = !multiple;
    overlay.querySelector('.atha-lightbox__nav--next').hidden = !multiple;
  }

  function step(delta) {
    if (!items.length) { return; }
    index = (index + delta + items.length) % items.length;
    paint();
  }

  function open(group, startIndex) {
    build();
    items = group;
    index = startIndex;
    lastFocused = document.activeElement;
    paint();
    overlay.hidden = false;
    document.body.classList.add('atha-lightbox-open');
    overlay.querySelector('.atha-lightbox__close').focus();
  }

  function close() {
    if (!overlay || overlay.hidden) { return; }
    overlay.hidden = true;
    document.body.classList.remove('atha-lightbox-open');
    if (lastFocused && lastFocused.focus) { lastFocused.focus(); }
  }

  /* Collect all triggers inside one scope so arrow keys walk that gallery. */
  function bind(scope) {
    var root = scope || document;
    var triggers = root.querySelectorAll('[data-atha-lightbox]:not([data-atha-bound])');
    if (!triggers.length) { return; }

    var group = [];
    for (var i = 0; i < triggers.length; i++) {
      var trigger = triggers[i];
      var img = trigger.querySelector('img');
      group.push({
        src: trigger.getAttribute('data-atha-lightbox'),
        caption: trigger.getAttribute('data-caption') || '',
        alt: img ? img.getAttribute('alt') : ''
      });
    }

    for (var j = 0; j < triggers.length; j++) {
      (function (position) {
        triggers[position].setAttribute('data-atha-bound', 'true');
        triggers[position].addEventListener('click', function () { open(group, position); });
      })(j);
    }
  }

  A.gallery = { bind: bind, open: open, close: close };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { bind(document); });
  } else {
    bind(document);
  }
})();