/* ==========================================================================
   ATHA — in-browser breathing pacer
   Progressive enhancement over a static block: without JavaScript the CSS
   orb keeps breathing and the page still lists the exact timings.
   Runs entirely in the browser. No storage, no network, no tracking.

   Markup: <div class="atha-pacer" data-atha-pacer data-length="60">
             ... .atha-pacer__orb, [data-pacer-phase], [data-pacer-count],
             buttons with data-pattern="4,4,4,4", [data-pacer-toggle],
             select[data-pacer-length], input[data-pacer-sound],
             [data-pacer-controls] (hidden until ready)
   ========================================================================== */
(function () {
  'use strict';

  // Copy follows the page language (<html lang="tr"> gets Turkish).
  var TR = document.documentElement.lang === 'tr';
  var L = TR ? {
    labels: ['Nefes al', 'Tut', 'Nefes ver', 'Boş tut'], words: ['al', 'tut', 'ver', 'boş tut'],
    ready: 'Hazır', left: ' kaldı', done: 'Bitti',
    start: 'Başlat', stop: 'Durdur',
    paused: 'Duraklatıldı', hidden: 'Sayfa arka plana geçince duraklatıldı.'
  } : {
    labels: ['Breathe in', 'Hold', 'Breathe out', 'Hold'], words: ['in', 'hold', 'out', 'hold'],
    ready: 'Ready', perBreath: ' s a breath', left: ' left', done: 'Done',
    breath: ' breath', breaths: ' breaths', inWord: ' in ', start: 'Start', stop: 'Stop',
    paused: 'Paused', hidden: 'Paused while the page was hidden.'
  };
  var LABELS = L.labels;
  var SCALE = [1.16, 1.16, 0.8, 0.8];
  var TONES = [528, 0, 396, 0];

  function reducedMotion() {
    return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  }

  function parsePattern(text) {
    var parts = String(text || '').split(',');
    var out = [];
    for (var i = 0; i < 4; i++) {
      var n = parseFloat(parts[i]);
      out.push(isFinite(n) && n > 0 ? n : 0);
    }
    return out;
  }

  function fmt(seconds) {
    seconds = Math.max(0, Math.ceil(seconds));
    var m = Math.floor(seconds / 60);
    var s = seconds % 60;
    return m + ':' + (s < 10 ? '0' : '') + s;
  }

  function Pacer(root) {
    this.root = root;
    this.orb = root.querySelector('.atha-pacer__orb');
    this.phaseEl = root.querySelector('[data-pacer-phase]');
    this.countEl = root.querySelector('[data-pacer-count]');
    this.toggleBtn = root.querySelector('[data-pacer-toggle]');
    this.lengthSel = root.querySelector('[data-pacer-length]');
    this.soundBox = root.querySelector('[data-pacer-sound]');
    this.chips = Array.prototype.slice.call(root.querySelectorAll('[data-pattern]'));
    this.controls = root.querySelector('[data-pacer-controls]');
    this.timer = null;
    this.audio = null;
    this.running = false;

    var pressed = root.querySelector('[data-pattern][aria-pressed="true"]') || this.chips[0];
    this.pattern = parsePattern(pressed ? pressed.getAttribute('data-pattern') : '4,4,4,4');

    var self = this;
    this.chips.forEach(function (chip) {
      chip.addEventListener('click', function () { self.choose(chip); });
    });
    if (this.toggleBtn) {
      this.toggleBtn.addEventListener('click', function () {
        if (self.running) { self.stop(true); } else { self.start(); }
      });
    }
    if (this.lengthSel) {
      this.lengthSel.addEventListener('change', function () { if (self.running) { self.start(); } });
    }
    if (this.soundBox) {
      this.soundBox.addEventListener('change', function () { if (self.soundBox.checked) { self.tone(1); } });
    }
    document.addEventListener('visibilitychange', function () {
      if (document.hidden && self.running) { self.stop(false, L.hidden); }
    });

    if (this.controls) { this.controls.hidden = false; }
    root.classList.add('is-ready');
    this.idle();
  }

  Pacer.prototype.cycle = function () {
    return this.pattern[0] + this.pattern[1] + this.pattern[2] + this.pattern[3];
  };

  Pacer.prototype.idle = function () {
    this.setOrb(0.8, 0.6);
    this.phaseEl.textContent = L.ready;
    var words = L.words;
    var parts = [];
    for (var i = 0; i < 4; i++) {
      if (this.pattern[i] > 0) { parts.push(TR ? this.pattern[i] + ' ' + words[i] : words[i] + ' ' + this.pattern[i]); }
    }
    this.countEl.textContent = parts.join(' \u00b7 ') + (TR ? ' (bir nefes ' + this.cycle() + ' sn)' : ' (' + this.cycle() + L.perBreath + ')');
  };

  Pacer.prototype.choose = function (chip) {
    this.chips.forEach(function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
    this.pattern = parsePattern(chip.getAttribute('data-pattern'));
    if (this.running) { this.start(); } else { this.idle(); }
  };

  Pacer.prototype.setOrb = function (scale, seconds) {
    if (!this.orb || reducedMotion()) { return; }
    this.orb.style.transitionDuration = Math.max(0.2, seconds) + 's';
    this.orb.style.transform = 'scale(' + scale + ')';
  };

  Pacer.prototype.tone = function (freq) {
    if (!freq || !this.soundBox || !this.soundBox.checked) { return; }
    try {
      if (!this.audio) {
        var Ctx = window.AudioContext || window.webkitAudioContext;
        if (!Ctx) { return; }
        this.audio = new Ctx();
      }
      var ctx = this.audio;
      if (ctx.state === 'suspended') { ctx.resume(); }
      var osc = ctx.createOscillator();
      var gain = ctx.createGain();
      var t = ctx.currentTime;
      osc.type = 'sine';
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(0.0001, t);
      gain.gain.exponentialRampToValueAtTime(0.08, t + 0.06);
      gain.gain.exponentialRampToValueAtTime(0.0001, t + 0.9);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(t);
      osc.stop(t + 1);
    } catch (e) { /* sound is optional */ }
  };

  Pacer.prototype.start = function () {
    this.stop(false);
    var cycle = this.cycle();
    if (cycle <= 0) { return; }
    var wanted = this.lengthSel ? parseInt(this.lengthSel.value, 10) : parseInt(this.root.getAttribute('data-length') || '60', 10);
    // Always finish on a complete breath.
    this.total = Math.max(1, Math.round(wanted / cycle)) * cycle;
    this.cycles = Math.round(this.total / cycle);
    this.t0 = Date.now();
    this.lastPhase = -1;
    this.lastCycle = -1;
    this.running = true;
    if (this.toggleBtn) { this.toggleBtn.textContent = L.stop; this.toggleBtn.setAttribute('aria-pressed', 'true'); }
    // Create the audio context inside the click, so iOS Safari allows it.
    if (this.soundBox && this.soundBox.checked) { this.tone(1); }
    var self = this;
    this.tick();
    this.timer = window.setInterval(function () { self.tick(); }, 200);
  };

  Pacer.prototype.tick = function () {
    var elapsed = (Date.now() - this.t0) / 1000;
    if (elapsed >= this.total) { this.finish(); return; }
    var cycle = this.cycle();
    var inCycle = elapsed % cycle;
    var cycleIndex = Math.floor(elapsed / cycle);
    var acc = 0;
    var phase = 0;
    for (var i = 0; i < 4; i++) {
      if (this.pattern[i] <= 0) { continue; }
      if (inCycle < acc + this.pattern[i]) { phase = i; break; }
      acc += this.pattern[i];
    }
    var phaseLeft = acc + this.pattern[phase] - inCycle;
    if (phase !== this.lastPhase || cycleIndex !== this.lastCycle) {
      this.lastPhase = phase;
      this.lastCycle = cycleIndex;
      this.phaseEl.textContent = LABELS[phase];
      this.setOrb(SCALE[phase], this.pattern[phase]);
      this.tone(TONES[phase]);
    }
    this.countEl.textContent = Math.ceil(phaseLeft) + '  \u00b7  ' + fmt(this.total - elapsed) + L.left;
  };

  Pacer.prototype.finish = function () {
    var n = this.cycles;
    this.stop(false);
    this.phaseEl.textContent = L.done;
    this.countEl.textContent = TR
      ? fmt(this.total) + ' içinde ' + n + ' nefes'
      : n + (n === 1 ? L.breath : L.breaths) + L.inWord + fmt(this.total);
    this.setOrb(0.8, 1.2);
  };

  Pacer.prototype.stop = function (reset, message) {
    if (this.timer) { window.clearInterval(this.timer); this.timer = null; }
    var wasRunning = this.running;
    this.running = false;
    if (this.toggleBtn) { this.toggleBtn.textContent = L.start; this.toggleBtn.setAttribute('aria-pressed', 'false'); }
    if (reset) { this.idle(); }
    if (message && wasRunning) { this.phaseEl.textContent = L.paused; this.countEl.textContent = message; this.setOrb(0.8, 0.6); }
  };

  function init() {
    var nodes = document.querySelectorAll('[data-atha-pacer]');
    for (var i = 0; i < nodes.length; i++) {
      try { new Pacer(nodes[i]); } catch (e) { /* static fallback stays */ }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
