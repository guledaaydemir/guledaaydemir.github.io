/* ============================================================
   DUMP — Learn Basics Engine
   assets/basics.js
   Scroll-driven, in-phone demos of what the app actually does.
   Requires: assets/dump.css, assets/motion.js. Load after motion.js.

   GEOMETRY RULE
   -------------
   Media is never sized with a percentage height. The phone screen is
   tall and narrow, so a percentage height turns a photo into a stick.
   Every tile sets a width and an `aspect-ratio`, so a photo stays
   photo-shaped at any screen size.

   MARKUP CONTRACT
   ---------------
   <section class="story">
     <div class="story-sticky">
       <div class="phone"><span class="phone-glow"></span>
         <div class="screen"><div class="screen-pad">
           <div class="scene-bar" id="basicsBar"></div>
           <div class="demo-host" id="basicsHost"></div>
           <div class="demo-cap"  id="basicsCap"></div>
         </div></div>
       </div>
     </div>
     <div class="story-steps">
       <article class="story-step" data-scene="0"> ... </article>   x6
     </div>
   </section>

   Standalone looping demo elsewhere:
   <div class="demo-scr" data-scene="3"><div class="demo-host"></div></div>
   ============================================================ */
(function () {
  'use strict';

  var DUMP = window.DUMP = window.DUMP || {};
  var reduce = DUMP.reduce === true;
  var $ = DUMP.$ || function (s, r) { return (r || document).querySelector(s); };
  var $$ = DUMP.$$ || function (s, r) {
    return Array.prototype.slice.call((r || document).querySelectorAll(s));
  };

  /* ---------- 0. Fake media ---------- */
  /* Deterministic gradients: the same seed always renders the same
     "photo", so a replayed scene never flickers into a new palette. */
  var SWATCH = [
    ['#C799FA', '#7A4FB0'], ['#FF375F', '#B31E3C'], ['#0A84FF', '#0A4E9E'],
    ['#FF9F0A', '#B36A00'], ['#30D158', '#1B7A36'], ['#F2E8DC', '#B8A88F'],
    ['#5E5CE6', '#332F9E'], ['#FF6482', '#A83552'], ['#64D2FF', '#2B7FA8'],
    ['#A2845E', '#6B5539'], ['#8E8E93', '#3A3A3C'], ['#FFD60A', '#B08D00']
  ];
  function swatch(i) { return SWATCH[Math.abs(i) % SWATCH.length]; }

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  /* A photo. `ratio` is width/height — 1.333 landscape, 0.8 portrait, 1 square. */
  function photo(seed, ratio, isVideo) {
    var t = el('div', 'tile flat');
    var c = swatch(seed);
    var ang = 120 + (seed % 5) * 24;
    t.style.aspectRatio = String(ratio || 1);
    t.innerHTML =
      '<i style="background:linear-gradient(' + ang + 'deg,' + c[0] + ',' + c[1] + ')"></i>' +
      (isVideo ? '<span class="vid">&#9654;</span>' : '');
    return t;
  }

  function box(styles) {
    var n = el('div');
    n.style.cssText = styles;
    return n;
  }

  function toolbar(icons, activeIndex) {
    var t = el('div', 'toolbar');
    icons.forEach(function (ic, i) {
      t.appendChild(el('div', 'ti' + (i === activeIndex ? ' on' : ''), ic));
    });
    return t;
  }

  function cursor(host, x, y) {
    var c = el('div', 'cursor');
    c.style.left = '0';
    c.style.top = '0';
    c.style.transform = 'translate(' + x + 'px,' + y + 'px)';
    c.style.opacity = '0';
    host.appendChild(c);
    return {
      to: function (nx, ny) {
        c.style.opacity = '1';
        c.style.transform = 'translate(' + nx + 'px,' + ny + 'px)';
      },
      tap: function () { c.classList.remove('tap'); void c.offsetWidth; c.classList.add('tap'); },
      hide: function () { c.style.opacity = '0'; }
    };
  }

  var EASE = 'cubic-bezier(.22,1,.36,1)';

  /* ============================================================
     1. SCENES
     Each builder returns { steps:[{t,fn}], period, label }.
     ============================================================ */

  /* Scene 0 — Intro: a camera roll too big to choose from becomes a dump. */
  function sIntro(host) {
    host.innerHTML = '';

    /* The camera roll: a real 4-column thumbnail grid. */
    var roll = box('position:absolute;inset:0;display:grid;grid-template-columns:repeat(4,1fr);' +
      'gap:4px;align-content:start;padding:4px;transition:opacity .5s ease,transform .6s ' + EASE);
    host.appendChild(roll);

    var tiles = [], N = 20, keep = [2, 6, 9, 13, 18];
    for (var i = 0; i < N; i++) {
      var t = photo(i, 1, i % 6 === 0);
      t.style.transition = 'opacity .5s ease,filter .5s ease,box-shadow .35s ease,transform .5s ' + EASE;
      roll.appendChild(t);
      tiles.push(t);
    }

    /* The finished dump: five real photos fanned into a stack. */
    var stack = box('position:absolute;inset:0;display:grid;place-items:center;opacity:0;' +
      'transition:opacity .5s ease');
    host.appendChild(stack);

    var deck = box('position:relative;width:74%');
    stack.appendChild(deck);

    var fan = [[-24, -7, .84], [-12, -3.5, .92], [0, 0, 1], [12, 3.5, .92], [24, 7, .84]];
    var cards = [];
    keep.forEach(function (k, n) {
      var c = photo(k, 0.8, k % 6 === 0);
      c.style.cssText += 'position:' + (n === 2 ? 'relative' : 'absolute') +
        ';top:0;left:0;width:100%;z-index:' + (10 - Math.abs(n - 2)) +
        ';border:3px solid rgba(255,255,255,.9);box-shadow:0 10px 26px rgba(0,0,0,.45);' +
        'transform:translate(0,0) rotate(0deg) scale(.7);opacity:0;' +
        'transition:transform .7s ' + EASE + ',opacity .5s ease';
      deck.appendChild(c);
      cards.push({ node: c, fan: fan[n] });
    });

    var mark = box('position:absolute;left:0;right:0;bottom:12%;text-align:center;z-index:20;' +
      'opacity:0;transform:translateY(10px);transition:opacity .5s ease,transform .5s ' + EASE);
    mark.innerHTML = '<b style="font-family:\'Space Grotesk\',sans-serif;font-size:22px;' +
      'font-weight:700;letter-spacing:-.5px">One dump. Ready to post.</b>';
    mark.style.fontSize = '0';
    host.appendChild(mark);

    return {
      label: 'Your camera roll',
      period: 6400,
      steps: [
        { t: 800, fn: function () {
          keep.forEach(function (k) { tiles[k].classList.add('pick'); });
        } },
        { t: 1700, fn: function () {
          tiles.forEach(function (t, i) { if (keep.indexOf(i) < 0) t.classList.add('drop'); });
        } },
        { t: 2600, fn: function () {
          roll.style.opacity = '0';
          roll.style.transform = 'scale(.94)';
          stack.style.opacity = '1';
          cards.forEach(function (c, n) {
            setTimeout(function () {
              c.node.style.opacity = '1';
              c.node.style.transform = 'translateX(' + c.fan[0] + '%) rotate(' + c.fan[1] +
                'deg) scale(' + c.fan[2] + ')';
            }, n * 90);
          });
        } },
        { t: 3900, fn: function () {
          mark.style.opacity = '1';
          mark.style.transform = 'none';
        } }
      ]
    };
  }

  /* Scene 1 — Random Dump: one tap builds a carousel, one tap reshuffles a slot. */
  function sRandom(host) {
    host.innerHTML = '';

    var stage = box('position:absolute;left:0;right:0;top:6%;display:grid;place-items:center');
    host.appendChild(stage);

    /* A swipeable deck: current slide large, neighbours peeking. */
    var deck = box('position:relative;width:64%');
    stage.appendChild(deck);

    var seeds = [3, 7, 11], slots = [];
    var pose = [
      { x: -74, s: 0.8, o: 0.45, z: 1 },
      { x: 0, s: 1, o: 1, z: 3 },
      { x: 74, s: 0.8, o: 0.45, z: 1 }
    ];
    seeds.forEach(function (s, i) {
      var wrap = box('position:' + (i === 1 ? 'relative' : 'absolute') + ';top:0;left:0;width:100%;' +
        'aspect-ratio:.8;border-radius:10px;overflow:hidden;z-index:' + pose[i].z + ';' +
        'border:2px solid rgba(255,255,255,.85);box-shadow:0 10px 24px rgba(0,0,0,.45);' +
        'opacity:0;transform:translateX(' + pose[i].x + '%) scale(' + (pose[i].s * 0.86) + ');' +
        'transition:opacity .45s ease,transform .55s ' + EASE);
      var p = photo(s, 0.8, i === 1);
      p.style.cssText += 'position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto';
      wrap.appendChild(p);
      deck.appendChild(wrap);
      slots.push({ wrap: wrap, tile: p, pose: pose[i] });
    });

    var dots = box('display:flex;gap:5px;justify-content:center;margin-top:16px');
    for (var d = 0; d < 5; d++) {
      dots.appendChild(box('width:5px;height:5px;border-radius:50%;background:' +
        (d === 1 ? '#C799FA' : 'rgba(255,255,255,.22)')));
    }
    stage.appendChild(dots);

    var btn = el('div', '', '&#8646;&nbsp; Shuffle');
    btn.style.cssText = 'position:absolute;left:50%;bottom:14%;transform:translateX(-50%);' +
      'padding:9px 20px;border-radius:999px;font-size:12px;font-weight:600;color:#12030A;' +
      'white-space:nowrap;background:linear-gradient(120deg,#C799FA,#FF375F);' +
      'transition:transform .2s ' + EASE;
    host.appendChild(btn);

    var cur = cursor(host, 70, 60);

    function swap(i, seed) {
      var s = slots[i];
      var next = photo(seed, 0.8, seed % 5 === 0);
      next.style.cssText += 'position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto;' +
        'opacity:0;transform:scale(1.12);transition:opacity .4s ease,transform .5s ' + EASE;
      s.wrap.appendChild(next);
      requestAnimationFrame(function () { next.style.opacity = '1'; next.style.transform = 'none'; });
      var old = s.tile;
      old.style.transition = 'opacity .35s ease';
      old.style.opacity = '0';
      setTimeout(function () { if (old.parentNode) old.parentNode.removeChild(old); }, 420);
      s.tile = next;
    }

    var steps = [];
    slots.forEach(function (s, i) {
      steps.push({ t: 260 + i * 140, fn: function () {
        s.wrap.style.opacity = String(s.pose.o);
        s.wrap.style.transform = 'translateX(' + s.pose.x + '%) scale(' + s.pose.s + ')';
      } });
    });
    steps.push({ t: 1500, fn: function () { cur.to(112, 300); } });
    steps.push({ t: 2000, fn: function () { cur.tap(); btn.style.transform = 'translateX(-50%) scale(.93)'; } });
    steps.push({ t: 2200, fn: function () {
      btn.style.transform = 'translateX(-50%) scale(1)';
      swap(1, 21); swap(2, 15);
    } });
    steps.push({ t: 3200, fn: function () { cur.tap(); swap(0, 26); swap(1, 33); } });
    steps.push({ t: 4100, fn: function () { cur.hide(); } });

    return { label: 'Random dump', period: 5400, steps: steps };
  }

  /* Scene 2 — Templates: pick a look, media pours into it. */
  function sTemplate(host) {
    host.innerHTML = '';

    var rail = box('position:absolute;left:5%;right:5%;top:3%;display:flex;gap:7px');
    host.appendChild(rail);

    var cards = [];
    [0, 1, 2].forEach(function (i) {
      var c = box('flex:1;aspect-ratio:.8;border-radius:9px;border:1px solid rgba(255,255,255,.10);' +
        'background:#212121;position:relative;overflow:hidden;padding:5px;display:grid;gap:3px;' +
        'transition:transform .4s ' + EASE + ',box-shadow .4s ease,border-color .4s ease;' +
        (i === 0 ? 'grid-template-columns:1fr' :
          i === 1 ? 'grid-template-columns:1fr;grid-template-rows:1fr 1fr' :
            'grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr'));
      var n = i === 0 ? 1 : i === 1 ? 2 : 4;
      for (var k = 0; k < n; k++) {
        var s = swatch(i * 3 + k);
        c.appendChild(box('border-radius:3px;opacity:.6;background:linear-gradient(140deg,' +
          s[0] + ',' + s[1] + ')'));
      }
      rail.appendChild(c);
      cards.push(c);
    });

    var stage = box('position:absolute;left:0;right:0;top:34%;display:grid;place-items:center');
    host.appendChild(stage);

    var page = box('width:74%;aspect-ratio:.8;border-radius:12px;background:#1A1A1A;' +
      'border:1px solid rgba(255,255,255,.08);display:grid;gap:5px;padding:7px;' +
      'grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;opacity:0;transform:scale(.92);' +
      'transition:opacity .5s ease,transform .5s ' + EASE);
    stage.appendChild(page);

    var cells = [];
    for (var k = 0; k < 4; k++) {
      var cell = box('border-radius:6px;background:rgba(255,255,255,.05);overflow:hidden;position:relative');
      page.appendChild(cell);
      cells.push(cell);
    }

    var cur = cursor(host, 40, 20);

    var steps = [
      { t: 500, fn: function () { cur.to(160, 40); } },
      { t: 1000, fn: function () {
        cur.tap();
        cards[2].style.transform = 'translateY(-5px)';
        cards[2].style.boxShadow = '0 0 0 2px #C799FA';
        cards[2].style.borderColor = 'transparent';
      } },
      { t: 1350, fn: function () { page.style.opacity = '1'; page.style.transform = 'none'; cur.hide(); } }
    ];
    [0, 1, 2, 3].forEach(function (i) {
      steps.push({ t: 1750 + i * 250, fn: function () {
        var t = photo(i + 4, 1, i === 1);
        t.style.cssText += 'position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto;' +
          'opacity:0;transform:scale(1.15);transition:opacity .4s ease,transform .5s ' + EASE;
        cells[i].appendChild(t);
        requestAnimationFrame(function () { t.style.opacity = '1'; t.style.transform = 'none'; });
      } });
    });

    return { label: 'Templates', period: 4800, steps: steps };
  }

  /* Scene 3 — Grid: photos snap into a layout, spacing dialled live. */
  function sGrid(host) {
    host.innerHTML = '';

    var stage = box('position:absolute;left:0;right:0;top:6%;display:grid;place-items:center');
    host.appendChild(stage);

    var page = box('width:78%;aspect-ratio:.8;border-radius:12px;background:#1A1A1A;' +
      'border:1px solid rgba(255,255,255,.08);display:grid;padding:6px;gap:2px;' +
      'grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr 1fr;' +
      'transition:gap .6s ' + EASE + ',padding .6s ' + EASE);
    stage.appendChild(page);

    var cells = [];
    for (var i = 0; i < 6; i++) {
      var c = box('position:relative;overflow:hidden;border-radius:2px;' +
        'background:rgba(255,255,255,.05);opacity:0;transform:scale(.8);' +
        'transition:opacity .4s ease,transform .45s cubic-bezier(.34,1.56,.64,1),border-radius .6s ease');
      var t = photo(i + 2, 1, i === 4);
      t.style.cssText += 'position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto';
      c.appendChild(t);
      page.appendChild(c);
      cells.push(c);
    }

    var slider = box('position:absolute;left:14%;right:14%;bottom:16%;height:4px;' +
      'border-radius:3px;background:rgba(255,255,255,.13)');
    var knob = box('position:absolute;top:-7px;left:calc(16% - 9px);width:18px;height:18px;' +
      'border-radius:50%;background:linear-gradient(120deg,#C799FA,#FF375F);' +
      'box-shadow:0 3px 10px rgba(0,0,0,.5);transition:left .7s ' + EASE);
    slider.appendChild(knob);
    host.appendChild(slider);

    var lbl = el('div', '', 'Spacing');
    lbl.style.cssText = 'position:absolute;left:0;right:0;bottom:8%;text-align:center;font-size:10px;' +
      'letter-spacing:2px;text-transform:uppercase;color:#6B6B6B;font-family:"Space Mono",monospace';
    host.appendChild(lbl);

    var steps = [];
    cells.forEach(function (c, i) {
      steps.push({ t: 240 + i * 110, fn: function () { c.style.opacity = '1'; c.style.transform = 'none'; } });
    });
    steps.push({ t: 1700, fn: function () {
      knob.style.left = 'calc(60% - 9px)';
      page.style.gap = '8px';
      page.style.padding = '11px';
      cells.forEach(function (c) { c.style.borderRadius = '7px'; });
    } });
    steps.push({ t: 3000, fn: function () {
      knob.style.left = 'calc(16% - 9px)';
      page.style.gap = '2px';
      page.style.padding = '6px';
      cells.forEach(function (c) { c.style.borderRadius = '2px'; });
    } });

    return { label: 'Grid layouts', period: 4600, steps: steps };
  }

  /* Scene 4 — Canvas: freeform page with stickers, text and frames. */
  function sCanvas(host) {
    host.innerHTML = '';

    var stage = box('position:absolute;left:0;right:0;top:4%;display:grid;place-items:center');
    host.appendChild(stage);

    var page = box('position:relative;width:80%;aspect-ratio:.8;border-radius:12px;overflow:hidden;' +
      'background:linear-gradient(160deg,#F2E8DC,#D9CCB8)');
    stage.appendChild(page);

    var a = photo(6, 1.333);
    a.style.cssText += 'position:absolute;left:6%;top:8%;width:60%;aspect-ratio:1.333;' +
      'border:3px solid #fff;box-shadow:0 6px 16px rgba(0,0,0,.28);transform:rotate(-5deg);' +
      'transition:border-width .4s ease';
    page.appendChild(a);

    var b = photo(9, 1.333, true);
    b.style.cssText += 'position:absolute;right:6%;top:44%;width:60%;aspect-ratio:1.333;' +
      'border:3px solid #fff;box-shadow:0 6px 16px rgba(0,0,0,.28);opacity:0;' +
      'transform:rotate(6deg) scale(.85);transition:opacity .45s ease,transform .6s ' +
      'cubic-bezier(.34,1.56,.64,1),border-width .4s ease';
    page.appendChild(b);

    var star = el('div', '', '&#10022;');
    star.style.cssText = 'position:absolute;right:10%;top:5%;font-size:20px;color:#FF375F;opacity:0;' +
      'transform:scale(.3) rotate(-40deg);transition:opacity .35s ease,transform .5s ' +
      'cubic-bezier(.34,1.56,.64,1)';
    page.appendChild(star);

    var text = el('div', '', 'summer, unfiltered');
    text.style.cssText = 'position:absolute;left:7%;bottom:5%;font-family:"Space Grotesk",sans-serif;' +
      'font-size:13px;font-weight:700;color:#1A1A1A;opacity:0;transform:translateY(8px);' +
      'transition:opacity .4s ease,transform .45s ' + EASE;
    page.appendChild(text);

    var bar = toolbar(['&#128444;', '&#10022;', 'T', '&#9638;', '&#11036;'], -1);
    bar.style.cssText += 'position:absolute;left:6%;right:6%;bottom:4%';
    host.appendChild(bar);

    var items = $$('.ti', bar);
    function pick(i) { items.forEach(function (n, k) { n.classList.toggle('on', k === i); }); }

    return {
      label: 'Canvas editor',
      period: 5800,
      steps: [
        { t: 500, fn: function () { pick(0); } },
        { t: 800, fn: function () { b.style.opacity = '1'; b.style.transform = 'rotate(6deg) scale(1)'; } },
        { t: 1700, fn: function () { pick(1); } },
        { t: 2000, fn: function () { star.style.opacity = '1'; star.style.transform = 'scale(1) rotate(0)'; } },
        { t: 2900, fn: function () { pick(2); } },
        { t: 3200, fn: function () { text.style.opacity = '1'; text.style.transform = 'none'; } },
        { t: 4100, fn: function () {
          pick(3);
          a.style.borderWidth = '7px';
          b.style.borderWidth = '7px';
        } },
        { t: 5100, fn: function () { pick(-1); } }
      ]
    };
  }

  /* Scene 5 — Export: full quality out, straight into a Photos album. */
  function sExport(host) {
    host.innerHTML = '';

    var arc = el('div', 'progress-arc', '<b>0%</b>');
    arc.style.cssText += 'position:absolute;left:0;right:0;top:24%;margin:0 auto;' +
      'transition:opacity .4s ease';
    host.appendChild(arc);

    var stage = box('position:absolute;left:0;right:0;top:20%;display:grid;place-items:center');
    host.appendChild(stage);

    var album = box('width:80%;padding:12px;border-radius:14px;background:#212121;' +
      'border:1px solid rgba(255,255,255,.08);opacity:0;transform:translateY(14px) scale(.94);' +
      'transition:opacity .45s ease,transform .5s cubic-bezier(.34,1.56,.64,1)');
    var thumbs = box('display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-bottom:10px');
    [4, 8, 12, 1, 6, 9].forEach(function (s) {
      var t = photo(s, 1);
      t.style.borderRadius = '5px';
      thumbs.appendChild(t);
    });
    album.appendChild(thumbs);
    album.appendChild(box('font-family:\'Space Grotesk\',sans-serif;font-size:13px;font-weight:600;' +
      'color:#F5F5F5')).textContent = 'July Dump';
    album.appendChild(box('font-size:11px;color:#9E9E9E')).textContent = '10 items · original quality';
    stage.appendChild(album);

    var badge = el('div', '', '&#10003;&nbsp; Saved to Photos');
    badge.style.cssText = 'position:absolute;left:0;right:0;bottom:16%;text-align:center;font-size:12px;' +
      'font-weight:600;color:#30D158;opacity:0;transform:translateY(8px);' +
      'transition:opacity .4s ease,transform .4s ease';
    host.appendChild(badge);

    var val = arc.querySelector('b');
    function setP(p) {
      arc.style.background = 'conic-gradient(#C799FA ' + p + '%,rgba(255,255,255,.09) 0)';
      val.textContent = p + '%';
    }
    setP(0);

    var steps = [];
    [12, 34, 58, 79, 100].forEach(function (p, i) {
      steps.push({ t: 400 + i * 380, fn: function () { setP(p); } });
    });
    steps.push({ t: 2500, fn: function () { arc.style.opacity = '0'; } });
    steps.push({ t: 2800, fn: function () { album.style.opacity = '1'; album.style.transform = 'none'; } });
    steps.push({ t: 3300, fn: function () { badge.style.opacity = '1'; badge.style.transform = 'none'; } });

    return { label: 'Export', period: 5400, steps: steps };
  }

  var SCENES = [sIntro, sRandom, sTemplate, sGrid, sCanvas, sExport];
  var LABELS = ['Camera roll', 'Random dump', 'Templates', 'Grid', 'Canvas', 'Export'];
  DUMP.scenes = SCENES;

  /* ============================================================
     2. RUNNERS
     ============================================================ */

  /* Reduced motion: render the scene's final frame, no loop. */
  function runStatic(host, builder) {
    var s = builder(host);
    s.steps.forEach(function (x) { x.fn(); });
    return s;
  }

  function makeLoop(host) {
    var timers = [], stopped = true, current = -1;
    function clear() { timers.forEach(clearTimeout); timers = []; }
    return {
      get index() { return current; },
      play: function (i, onLabel) {
        if (i === current && !stopped) return;
        clear();
        current = i;
        stopped = false;
        var builder = SCENES[i];
        if (!builder) return;
        if (onLabel) onLabel(LABELS[i]);
        if (reduce) { runStatic(host, builder); stopped = true; return; }
        (function go() {
          clear();
          var s = builder(host);
          s.steps.forEach(function (x) { timers.push(setTimeout(x.fn, x.t)); });
          timers.push(setTimeout(go, s.period));
        })();
      },
      stop: function () { clear(); stopped = true; }
    };
  }

  /* ---------- 3. Story rail ---------- */
  function initStory() {
    var host = $('#basicsHost');
    if (!host) return;
    var cap = $('#basicsCap');
    var bar = $('#basicsBar');
    var steps = $$('.story-step');
    if (!steps.length) return;

    if (bar) {
      bar.innerHTML = '';
      steps.forEach(function () { bar.appendChild(el('span', 'pill')); });
    }
    var pills = bar ? $$('.pill', bar) : [];
    var loop = makeLoop(host);

    function setLabel(text) { if (cap) cap.textContent = text; }

    function activate(i) {
      steps.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      pills.forEach(function (p, k) { p.classList.toggle('on', k === i); });
      loop.play(i, setLabel);
    }

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        var best = null;
        entries.forEach(function (e) {
          if (e.isIntersecting && (!best || e.intersectionRatio > best.intersectionRatio)) best = e;
        });
        if (!best) return;
        var i = steps.indexOf(best.target);
        if (i > -1) activate(i);
      }, { threshold: 0.55, rootMargin: '-20% 0px -30% 0px' });
      steps.forEach(function (s) { io.observe(s); });
    }

    /* Clicking a step jumps its demo — the rail doubles as navigation. */
    steps.forEach(function (s, i) {
      s.setAttribute('tabindex', '0');
      s.setAttribute('role', 'button');
      var go = function () { activate(i); if (DUMP.track) DUMP.track('basics_step', { step: i }); };
      s.addEventListener('click', go);
      s.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); }
      });
    });

    /* Pause off-screen: looping timers behind the fold burn battery. */
    if ('IntersectionObserver' in window && !reduce) {
      var section = host.closest('.story') || host;
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) activate(Math.max(loop.index, 0));
          else loop.stop();
        });
      }, { threshold: 0.02 }).observe(section);
    }

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) loop.stop();
      else activate(Math.max(loop.index, 0));
    });

    activate(0);
  }

  /* ---------- 4. Standalone demos ---------- */
  function initStandalone() {
    $$('.demo-scr').forEach(function (scr) {
      var host = $('.demo-host', scr);
      if (!host) return;
      var i = parseInt(scr.getAttribute('data-scene'), 10) || 0;
      var cap = $('.demo-cap', scr);
      if (cap) cap.textContent = LABELS[i];
      if (reduce) { runStatic(host, SCENES[i]); return; }
      var loop = makeLoop(host);
      if (!('IntersectionObserver' in window)) { loop.play(i); return; }
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { e.isIntersecting ? loop.play(i) : loop.stop(); });
      }, { threshold: 0.25 }).observe(scr);
    });
  }

  function boot() { initStory(); initStandalone(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
