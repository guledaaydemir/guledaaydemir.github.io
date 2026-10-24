/* SHOOTS website. The hero is a port of the app's LaunchView: a 00s red-carpet shoot of the
   wordmark. The AF hunts and locks, the paparazzi open fire and every flash catches one letter,
   then the money shot burns the frame into the logo: black ink on flash yellow, star punched
   through the O's. Every frame is a pure function of the time since it started. */
(function () {
  'use strict';
  var doc = document.documentElement;
  doc.classList.add('js', 'js-ready');
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var STAR = 'M69.92 51.74 L106.62 77.62 L60.72 59.00 L82.33 94.50 L51.95 63.86 L29.29 94.41 L41.82 58.78 L1.44 75.82 L32.07 51.57 L-0.41 30.65 L39.12 41.19 L25.09 10.14 L50.17 40.00 L79.49 10.87 L60.65 42.54 L107.68 33.46Z';
  function starSvg(cls) { return '<svg class="' + (cls || '') + '" viewBox="0 0 100 100" aria-hidden="true"><path d="' + STAR + '"/></svg>'; }

  // ---------- curves (LaunchView.Shoot) ----------
  function ramp(t, a, b) { return Math.min(Math.max((t - a) / (b - a), 0), 1); }
  function easeOut(x) { return 1 - Math.pow(1 - x, 3); }
  function burst(dt, decay) { if (dt < 0) return 0; var at = 0.02; return dt < at ? dt / at : Math.exp(-3 * (dt - at) / decay); }
  function spring(dt, w, z) {
    if (dt <= 0) return 0;
    var wd = w * Math.sqrt(1 - z * z), e = Math.exp(-z * w * dt);
    return 1 - e * (Math.cos(wd * dt) + z * w / wd * Math.sin(wd * dt));
  }

  // ---------- date stamp, the way 2003 point-and-shoots printed it: '26 10 22 ----------
  var now = new Date();
  var stampText = "'" + String(now.getFullYear()).slice(2) + ' ' + ('0' + (now.getMonth() + 1)).slice(-2) + ' ' + ('0' + now.getDate()).slice(-2);
  document.querySelectorAll('[data-today]').forEach(function (el) { el.textContent = stampText; });

  // ---------- hero ----------
  var hero = document.querySelector('[data-launch]');
  if (hero) launch(hero);

  function launch(hero) {
    var T = { focusLock: 0.45, refocus: 1.26, climax: 1.42, twinkle: 2.12, end: 2.85 };
    var flashes = [
      { time: 0.55, x: 0.14, y: 0.30, size: 1.00, spin: 12, letter: 0 },
      { time: 0.74, x: 0.88, y: 0.66, size: 0.85, spin: -20, letter: 4 },
      { time: 0.90, x: 0.20, y: 0.75, size: 0.90, spin: 30, letter: 2 },
      { time: 1.03, x: 0.85, y: 0.25, size: 1.05, spin: -8, letter: 5 },
      { time: 1.14, x: 0.07, y: 0.53, size: 0.80, spin: 18, letter: 1 },
      { time: 1.24, x: 0.94, y: 0.44, size: 0.95, spin: -28, letter: 3 },
      { time: 1.96, x: 0.12, y: 0.22, size: 0.65, spin: 5, letter: null },
      { time: 2.34, x: 0.90, y: 0.79, size: 0.55, spin: -15, letter: null }
    ];
    var tilt = [-7, 5, -4, 6, -6, 4], lift = [-0.06, 0.05, 0.08, -0.05, 0.07, -0.08];
    var word = hero.querySelector('.word');
    var letters = [].slice.call(hero.querySelectorAll('.word .L'));
    var print = hero.querySelector('.word .print');
    var fm = hero.querySelector('.word .fringe.m'), fc = hero.querySelector('.word .fringe.c');
    var star = hero.querySelector('.word .star'), starPath = star.querySelector('path.body'), ping = star.querySelector('.ping');
    var af = hero.querySelector('.word .af');
    var white = hero.querySelector('.whiteout');
    var counter = hero.querySelector('[data-frames]');
    var readouts = hero.querySelectorAll('.vf .ro');
    var tag = hero.querySelector('.tagline');
    var tagText = tag ? tag.getAttribute('data-text') : '';
    var stage = hero.querySelector('.stage');
    var glintBox = hero.querySelector('.glints');
    var glints = flashes.map(function (f) {
      var g = document.createElement('span');
      g.className = 'glint';
      g.style.left = (f.x * 100) + '%'; g.style.top = (f.y * 100) + '%';
      g.innerHTML = '<i class="spill"></i><i class="core"></i><i class="streak"></i>' + starSvg();
      glintBox.appendChild(g);
      return g;
    });
    var start = null, raf = 0, done = false;

    function sizeGlints() {
      var r = stage.getBoundingClientRect(), m = Math.min(r.width, r.height);
      glints.forEach(function (g, i) { g.style.setProperty('--s', (flashes[i].size * m).toFixed(1) + 'px'); });
    }
    sizeGlints();
    window.addEventListener('resize', sizeGlints, { passive: true });

    function render(t) {
      var printed = t >= T.climax, sc = t - T.climax;
      var capH = word.clientHeight * 0.95;
      hero.classList.toggle('printed', printed);
      // Letters: afterimages caught by the flashes, then the print takes over.
      var caught = 0;
      letters.forEach(function (el, i) {
        var f = flashes.filter(function (x) { return x.letter === i; })[0];
        if (printed || t < f.time) { el.style.opacity = 0; return; }
        caught++;
        var heat = burst(t - f.time, 0.45), bounce = 0;
        flashes.forEach(function (o) { if (o.letter !== null && o.time > f.time) bounce += burst(t - o.time, 0.22); });
        var hush = 1 - 0.8 * ramp(t, T.climax - 0.14, T.climax);
        var glow = Math.min(1, 0.26 + 0.74 * heat + 0.3 * bounce) * hush;
        el.style.background = 'rgb(255,255,' + Math.round(heat * 255) + ')';
        el.style.opacity = glow.toFixed(3);
        var settle = 1 - easeOut(ramp(t, f.time, f.time + 0.18));
        el.style.transform = 'translateY(' + (capH * lift[i] * settle).toFixed(2) + 'px) rotate(' + (tilt[i] * settle).toFixed(2) + 'deg) scale(' + (1 + 0.22 * settle).toFixed(3) + ')';
      });
      if (counter) counter.textContent = '[' + (36 - (printed ? 6 : caught)) + ']';
      readouts.forEach(function (r) { r.style.opacity = 1 - ramp(t, T.climax, T.climax + 0.15); });
      // The money shot: punch-in, shake and cheap-digicam colour fringing, dying away fast.
      print.style.opacity = printed ? 1 : 0;
      var impact = printed ? Math.exp(-sc * 9) : 0, fringe = printed ? Math.exp(-sc * 8) : 0;
      word.style.transform = impact > 0.002
        ? 'translate(' + (capH * 0.05 * impact * Math.sin(sc * 70)).toFixed(2) + 'px,' + (capH * 0.035 * impact * Math.cos(sc * 55)).toFixed(2) + 'px) scale(' + (1 + 0.08 * impact).toFixed(4) + ')'
        : '';
      var split = capH * 0.045 * fringe;
      fm.style.opacity = fc.style.opacity = fringe > 0.03 ? fringe.toFixed(3) : 0;
      fm.style.transform = 'translate(' + (-split).toFixed(2) + 'px,' + (split * 0.4).toFixed(2) + 'px)';
      fc.style.transform = 'translate(' + split.toFixed(2) + 'px,' + (-split * 0.4).toFixed(2) + 'px)';
      // The star bursts out white-hot, spins into place and cools to the paper's yellow.
      if (printed) {
        var grow = spring(sc, 17, 0.42), spin = -60 * (1 - spring(sc, 10, 0.8)), heat = burst(sc, 0.45);
        star.style.opacity = 1;
        star.style.transform = 'rotate(' + spin.toFixed(2) + 'deg) scale(' + Math.max(grow, 0.001).toFixed(4) + ')';
        starPath.style.fill = 'rgb(' + Math.round(253 + 2 * heat) + ',' + Math.round(253 + 2 * heat) + ',' + Math.round(3 + 252 * heat) + ')';
        star.style.filter = heat > 0.01 ? 'drop-shadow(0 0 ' + (capH * 0.1).toFixed(1) + 'px rgba(255,255,255,' + heat.toFixed(3) + '))' : '';
        var p = burst(t - T.twinkle, 0.3);
        ping.style.opacity = p > 0.004 ? p.toFixed(3) : 0;
        ping.style.transform = 'rotate(' + (25 + 80 * (1 - p)).toFixed(2) + 'deg) scale(' + (0.25 + 0.2 * p).toFixed(3) + ')';
      } else {
        star.style.opacity = 0;
      }
      white.style.opacity = burst(t - T.climax, 0.3).toFixed(3);
      // Paparazzi: speedlight envelope, anamorphic streak, spinning star.
      glints.forEach(function (g, i) {
        var f = flashes[i], a = burst(t - f.time, f.letter === null ? 0.24 : 0.16);
        if (a <= 0.004) { g.style.opacity = 0; return; }
        g.style.opacity = a.toFixed(3);
        g.firstChild.style.display = printed ? 'none' : '';
        var s = g.querySelector('svg');
        s.style.transform = 'translate(-50%,-50%) rotate(' + (f.spin + 50 * (1 - a)).toFixed(1) + 'deg) scale(' + (0.5 + 0.5 * a).toFixed(3) + ')';
      });
      // Autofocus: hunts, locks with two blinks, refocuses on the star, then the print.
      var lockedAt = t >= T.refocus ? T.refocus : T.focusLock;
      var vis = t < T.refocus ? ramp(t, 0.05, 0.15) * (1 - ramp(t, 0.6, 0.75)) : (printed ? 0 : 1);
      var hunting = t < lockedAt;
      var wob = t < T.refocus ? (hunting ? 0.3 * (1 - t / T.focusLock) + 0.04 * Math.sin(t * 45) : 0) : 0.25 * (1 - ramp(t, T.refocus, T.refocus + 0.05));
      var sl = t - lockedAt, blink = sl > 0 && sl < 0.24 && Math.floor(sl / 0.06) % 2 === 1;
      af.style.opacity = blink ? 0 : vis;
      af.style.color = hunting ? '#fff' : 'var(--yellow)';
      af.style.transform = 'scale(' + (1 + wob).toFixed(3) + ')';
      // The tagline types itself out like a date imprint, without reflowing.
      if (tag) {
        var n = Math.round(tagText.length * ramp(t, T.climax + 0.4, T.climax + 1.0));
        tag.innerHTML = '<span>' + esc(tagText.slice(0, n)) + '</span><span class="rest">' + esc(tagText.slice(n)) + '</span>';
      }
    }
    function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

    function frame(ts) {
      if (start === null) start = ts;
      var t = (ts - start) / 1000;
      render(Math.min(t, T.end));
      if (t >= T.end) { finish(); return; }
      raf = requestAnimationFrame(frame);
    }
    function finish() {
      if (done) return;
      done = true; cancelAnimationFrame(raf);
      render(T.end);
      hero.classList.add('settled');
      stragglers();
    }
    function play() {
      done = false; start = null;
      hero.classList.remove('settled');
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(frame);
    }
    hero.querySelector('.skipper').addEventListener('click', finish);
    stage.addEventListener('click', function () { if (!done) finish(); });
    var replay = hero.querySelector('.replay');
    if (replay) replay.addEventListener('click', function () { if (!calm) play(); });

    // ?frame=1.2 freezes the intro at that moment (for checking the choreography).
    var frozen = /[?&]frame=([\d.]+)/.exec(location.search);
    if (frozen) { render(Number(frozen[1])); hero.classList.remove('intro'); return; }
    if (calm) { render(T.end); hero.classList.add('settled'); hero.classList.remove('intro'); return; }
    // Start in the dark; a hidden tab waits until it's visible so nobody misses the shoot.
    render(0);
    hero.classList.remove('settled', 'intro');
    if (document.hidden) document.addEventListener('visibilitychange', function once() { if (!document.hidden) { document.removeEventListener('visibilitychange', once); setTimeout(play, 250); } });
    else setTimeout(play, 350);

    // After the shoot, the odd photographer keeps firing at the edges of the frame.
    var heroVisible = true;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { heroVisible = e[0].isIntersecting; }).observe(hero);
    var timer = 0;
    function stragglers() {
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (done && heroVisible && !document.hidden) {
          var r = stage.getBoundingClientRect(), left = Math.random() < 0.5;
          popAt(r.left + (left ? 0.04 + Math.random() * 0.12 : 0.84 + Math.random() * 0.12) * r.width, r.top + (0.15 + Math.random() * 0.7) * r.height, 0.7);
        }
        stragglers();
      }, 3800 + Math.random() * 4200);
    }
    word.addEventListener('pointerenter', function (e) { if (done) popAt(e.clientX, e.clientY, 0.6); });
  }

  // ---------- one paparazzi pop anywhere on screen ----------
  var lastPop = 0;
  function popAt(x, y, scale) {
    if (calm) return;
    var nowT = Date.now(); if (nowT - lastPop < 450) return; lastPop = nowT;
    var p = document.createElement('span');
    p.className = 'pop-flash';
    p.style.left = x + 'px'; p.style.top = y + 'px';
    p.style.scale = String(scale || 1);
    p.innerHTML = '<i class="core"></i><i class="streak"></i>' + starSvg();
    document.body.appendChild(p);
    setTimeout(function () { p.remove(); }, 700);
  }
  document.querySelectorAll('.appstore, .btn').forEach(function (b) {
    b.addEventListener('pointerenter', function () {
      var r = b.getBoundingClientRect(), side = Math.random() < 0.5;
      popAt(side ? r.left + 6 : r.right - 6, r.top + 4, 0.45);
    });
  });

  // ---------- menu ----------
  var mb = document.querySelector('.menu-btn'), drawer = document.getElementById('drawer');
  if (mb && drawer) {
    mb.addEventListener('click', function () {
      var open = mb.getAttribute('aria-expanded') !== 'true';
      mb.setAttribute('aria-expanded', String(open));
      drawer.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    drawer.addEventListener('click', function (e) { if (e.target.closest('a')) { mb.click(); } });
  }

  // ---------- reveal on scroll; screenshots get "taken" as they come in ----------
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        e.target.querySelectorAll('.device').forEach(function (d) { if (!d.querySelector('.snapflash')) { var s = document.createElement('i'); s.className = 'snapflash'; d.appendChild(s); } d.classList.add('snap'); });
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    document.querySelectorAll('.rv').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.rv').forEach(function (el) { el.classList.add('in'); });
  }

  // ---------- film strip ----------
  document.querySelectorAll('[data-strip]').forEach(function (wrap) {
    var strip = wrap.querySelector('.strip');
    wrap.querySelectorAll('[data-dir]').forEach(function (b) {
      b.addEventListener('click', function () {
        var f = strip.querySelector('.frame');
        strip.scrollBy({ left: (f ? f.getBoundingClientRect().width : 280) * Number(b.getAttribute('data-dir')) * 2, behavior: calm ? 'auto' : 'smooth' });
      });
    });
  });

  // ---------- interval chips (the Timer sheet) ----------
  document.querySelectorAll('[data-intervals]').forEach(function (box) {
    var out = box.querySelector('.readout');
    box.querySelectorAll('.chip').forEach(function (c) {
      c.addEventListener('click', function () {
        box.querySelectorAll('.chip').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
        c.setAttribute('aria-pressed', 'true');
        out.innerHTML = c.getAttribute('data-say');
      });
    });
  });

  // ---------- voices ----------
  var audio = null, playingBtn = null;
  function stopVoice() { if (audio) { audio.pause(); audio = null; } if (playingBtn) playingBtn.classList.remove('playing'); playingBtn = null; }
  document.querySelectorAll('.voice[data-src]').forEach(function (b) {
    b.addEventListener('click', function () {
      var same = playingBtn === b; stopVoice(); if (same) return;
      audio = new Audio(b.getAttribute('data-src')); playingBtn = b; b.classList.add('playing');
      audio.addEventListener('ended', stopVoice);
      audio.play().catch(stopVoice);
    });
  });

  // ---------- demo shoot ----------
  document.querySelectorAll('[data-demo]').forEach(function (box) {
    // The phone carries the data; the controls can live anywhere in the same section.
    var root = box.closest('section') || box;
    var dev = box.querySelector('.demo'), cd = dev.querySelector('.cd'), hud = dev.querySelector('.hud span'), fl = dev.querySelector('.fl');
    var bubble = dev.querySelector('.bubble'), doneEl = dev.querySelector('.done'), doneN = doneEl.querySelector('[data-n]');
    var btn = root.querySelector('.shutter .big'), soundBtn = root.querySelector('.sound-tg');
    if (!btn) return;
    var lines = JSON.parse(box.getAttribute('data-lines') || '[]');
    var opts = { delay: 3, interval: 1, count: 5 }, timers = [], running = false, sound = false;
    var sfx = {};
    function sfxPlay(name) { if (!sound) return; try { var a = sfx[name] || (sfx[name] = new Audio(box.getAttribute('data-sfx') + name + '.m4a')); a.currentTime = 0; a.play().catch(function () {}); } catch (e) {} }
    root.querySelectorAll('[data-opt]').forEach(function (c) {
      c.addEventListener('click', function () {
        if (running) return;
        var k = c.getAttribute('data-opt');
        root.querySelectorAll('[data-opt="' + k + '"]').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
        c.setAttribute('aria-pressed', 'true');
        opts[k] = Number(c.getAttribute('data-v'));
      });
    });
    if (soundBtn) soundBtn.addEventListener('click', function () { sound = soundBtn.getAttribute('aria-pressed') !== 'true'; soundBtn.setAttribute('aria-pressed', String(sound)); });
    function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
    function stop() {
      timers.forEach(clearTimeout); timers = []; running = false;
      dev.classList.remove('running'); btn.setAttribute('aria-pressed', 'false');
      bubble.classList.remove('show');
    }
    btn.addEventListener('click', function () {
      if (running) { stop(); return; }
      running = true; btn.setAttribute('aria-pressed', 'true'); doneEl.classList.remove('show');
      var t = 0, n = 0;
      for (var s = opts.delay; s >= 1; s--) (function (s, at) {
        later(function () { cd.textContent = s; cd.classList.remove('show'); void cd.offsetWidth; cd.classList.add('show'); sfxPlay(s === 1 ? 'countdown_final' : 'countdown_tick'); }, at);
      })(s, (opts.delay - s) * 1000);
      t = opts.delay * 1000;
      later(function () { cd.classList.remove('show'); dev.classList.add('running'); hud.textContent = '0 / ' + opts.count; }, t);
      for (var i = 1; i <= opts.count; i++) (function (i, at) {
        later(function () {
          n = i; hud.textContent = n + ' / ' + opts.count;
          if (!calm) { fl.classList.remove('pop'); void fl.offsetWidth; fl.classList.add('pop'); }
          sfxPlay('photo_beep');
          if (lines.length && (i === 2 || i === opts.count - 1 || (i > 2 && i % 4 === 0))) {
            bubble.textContent = '“' + lines[Math.floor(Math.random() * lines.length)] + '”';
            bubble.classList.add('show');
            later(function () { bubble.classList.remove('show'); }, 1500);
          }
        }, at);
      })(i, t + (i - 1) * opts.interval * 1000);
      later(function () {
        stop(); doneN.textContent = opts.count; doneEl.classList.add('show'); sfxPlay('shoot_complete');
        later(function () { doneEl.classList.remove('show'); }, 2600);
      }, t + (opts.count - 1) * opts.interval * 1000 + 700);
    });
  });
})();
