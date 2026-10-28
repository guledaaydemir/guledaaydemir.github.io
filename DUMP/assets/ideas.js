/* ============================================================
   DUMP — ideas pages
   assets/ideas.js
   One-tap copy for captions. Buttons ship hidden and only appear
   here, so a page without JS shows plain, selectable captions.
   Label text comes from the page (data-done), so it works in TR too.
   ============================================================ */
(function () {
  'use strict';
  var buttons = document.querySelectorAll('.cap-copy');
  if (!buttons.length) return;
  var status = document.getElementById('copy-status');

  function fallback(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (err) { }
    document.body.removeChild(ta);
    return ok ? Promise.resolve() : Promise.reject();
  }

  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).catch(function () { return fallback(text); });
    }
    return fallback(text);
  }

  Array.prototype.forEach.call(buttons, function (btn) {
    var label = btn.querySelector('.l');
    var idle = label.textContent;
    var done = btn.getAttribute('data-done') || 'Copied';
    var timer;
    btn.hidden = false;
    btn.addEventListener('click', function () {
      var text = btn.parentNode.querySelector('.c').textContent;
      copy(text).then(function () {
        label.textContent = done;
        btn.classList.add('done');
        if (status) status.textContent = done + ': ' + text;
        clearTimeout(timer);
        timer = setTimeout(function () {
          label.textContent = idle;
          btn.classList.remove('done');
        }, 1600);
      }, function () { });
    });
  });
})();
