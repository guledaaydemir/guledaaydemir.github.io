/* MULA website — small, dependency-free. Motion follows the app: flowIn cascades, a focus-pull launch, a wave that flattens. */
(function () {
  "use strict";
  var doc = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (_) {} },
    del: function (k) { try { localStorage.removeItem(k); } catch (_) {} }
  };
  var data = (function () { var n = $("#mula-data"); try { return n ? JSON.parse(n.textContent) : null; } catch (_) { return null; } })();

  /* ---------------------------------------------------------- launch intro (home) */
  var heroVideo = $(".launch-video");
  function startVideo() {
    if (!heroVideo || reduce) return;
    heroVideo.currentTime = 0;
    var p = heroVideo.play();
    if (p && p.catch) p.catch(function () {});
  }
  function runLaunch(first) {
    var l = $(".launch");
    if (!l) return;
    var fresh = l.cloneNode(true);           // restarts every CSS animation
    l.parentNode.replaceChild(fresh, l);
    l = fresh;
    doc.classList.add("intro");
    var done = false;
    function finish() {
      if (done) return;
      done = true;
      l.classList.add("out");
      setTimeout(function () { doc.classList.remove("intro"); l.classList.remove("out"); startVideo(); wakeHero(); }, 900);
    }
    var t = setTimeout(finish, 3700);
    l.addEventListener("click", function () { clearTimeout(t); finish(); });
    document.addEventListener("keydown", function k(ev) { if (ev.key === "Escape" || ev.key === "Enter" || ev.key === " ") { clearTimeout(t); finish(); document.removeEventListener("keydown", k); } });
    try { sessionStorage.setItem("mula-intro", "1"); } catch (_) {}
  }
  if (doc.classList.contains("intro")) runLaunch(true); else startVideo();
  var replay = $(".replay");
  if (replay) replay.addEventListener("click", function () { if (reduce) { startVideo(); return; } window.scrollTo({ top: 0 }); runLaunch(false); });

  /* ---------------------------------------------------------- season eyebrow, hero wave + parallax */
  var season = $(".hero .season");
  function seasonIndex(d) { var m = d.getMonth(); return m >= 2 && m <= 4 ? 0 : m >= 5 && m <= 7 ? 1 : m >= 8 && m <= 10 ? 2 : 3; }
  if (season) { try { season.textContent = JSON.parse(season.getAttribute("data-seasons"))[seasonIndex(new Date())]; } catch (_) {} }
  var sheetWave = $(".sheet-wave"), photo = $(".hero-photo"), topbar = $(".topbar");
  function wakeHero() {}
  var ticking = false;
  function onScroll() {
    var y = window.scrollY || 0;
    if (topbar) topbar.classList.toggle("scrolled", y > 10);
    if (!reduce) {
      if (sheetWave) sheetWave.style.setProperty("--flat", Math.max(0.12, 1 - y / 520).toFixed(3));
      if (photo && y < 1200) photo.style.setProperty("--py", (y * 0.28).toFixed(1) + "px");
    }
    ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* ---------------------------------------------------------- reveal (flowIn) + emblems that build themselves */
  var waits = $$(".roots-art .emblem, .about-emblem .emblem");
  waits.forEach(function (em) { if (!reduce) em.classList.add("wait"); });
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        if (el.classList.contains("emblem")) { el.classList.remove("wait"); el.classList.add("play"); }
        else el.classList.add("in");
        io.unobserve(el);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
    waits.forEach(function (el) { io.observe(el); });
    if (heroVideo) {
      new IntersectionObserver(function (es) {
        es.forEach(function (en) { if (doc.classList.contains("intro")) return; if (en.isIntersecting) { var p = heroVideo.play(); if (p && p.catch) p.catch(function () {}); } else heroVideo.pause(); });
      }, { threshold: 0.2 }).observe(heroVideo);
    }
  } else {
    $$(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------------------------------------------------------- faces: photograph <-> paper portrait */
  var faces = $$(".face"), touched = false;
  faces.forEach(function (f) {
    f.addEventListener("click", function () { touched = true; f.setAttribute("aria-pressed", f.getAttribute("aria-pressed") === "true" ? "false" : "true"); });
  });
  if (faces.length && !reduce) {
    var fi = 0;
    setInterval(function () {
      if (touched || document.hidden) return;
      var r = faces[0].getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) return;
      var f = faces[fi % faces.length];
      f.setAttribute("aria-pressed", "true");
      setTimeout(function () { if (!touched) f.setAttribute("aria-pressed", "false"); }, 2600);
      fi++;
    }, 1700);
  }

  /* ---------------------------------------------------------- the soil check */
  var soil = $(".soil-demo");
  if (soil && data) {
    var res = $(".result", soil), cbtn = $(".cbtn", soil), clabel = $(".clabel", soil);
    var autumnN = data.soil.n[2];
    var currentN = data.soil.n[seasonIndex(new Date())] || autumnN;
    $$(".opt", soil).forEach(function (o) {
      o.addEventListener("click", function () {
        var a = o.getAttribute("data-a");
        $$(".opt", soil).forEach(function (x) { x.setAttribute("aria-pressed", x === o ? "true" : "false"); });
        soil.setAttribute("data-state", a);
        soil.classList.remove("poke"); void soil.offsetWidth; soil.classList.add("poke");
        res.classList.add("swap");
        setTimeout(function () {
          res.textContent = data.soil.res[a].replace("{n}", autumnN);
          clabel.textContent = data.soil.btn[a];
          res.classList.remove("swap");
          cbtn.classList.remove("done"); void cbtn.offsetWidth;
          if (a !== "unsure") cbtn.classList.add("done");
        }, 260);
      });
    });
    void currentN;
  }

  /* ---------------------------------------------------------- seasons */
  var sd = $(".season-demo");
  if (sd && data) {
    var L = data.labels, cur = { p: 0, s: seasonIndex(new Date()) };
    var wheel = $(".wheel", sd), art = $(".wheel-art", sd);
    function fmt(s, o) { return s.replace(/\{(\w+)\}/g, function (_, k) { return o[k]; }); }
    function render(changedPlant) {
      var p = data.plants[cur.p], s = cur.s;
      $$(".chip", sd).forEach(function (c, i) { c.setAttribute("aria-pressed", i === cur.p ? "true" : "false"); });
      $$(".stab", sd).forEach(function (c, i) { c.setAttribute("aria-pressed", i === s ? "true" : "false"); });
      wheel.setAttribute("data-s", s);
      wheel.style.setProperty("--rot", (-45 - s * 90) + "deg");
      if (changedPlant || !art.firstChild) {
        var img = new Image();
        img.src = (document.querySelector('.face .back img[src*="/' + p.id + '-geo"]') || {}).src || "";
        img.alt = "";
        art.innerHTML = ""; art.appendChild(img);
      }
      $(".p-name", sd).textContent = p.nick;
      $(".p-latin", sd).textContent = p.latin;
      var tip = $(".tipline", sd);
      tip.textContent = p.tips[s];
      $(".v-water", sd).textContent = fmt(L.seasons_water_v, { n: p.water[s] });
      $(".v-feed", sd).textContent = p.feed[s] > 0 ? fmt(L.seasons_feed_v, { n: p.feed[s] }) : L.seasons_rest;
      $(".v-light", sd).textContent = p.light;
      $(".v-place", sd).textContent = p.place;
      $(".v-temp", sd).textContent = fmt(L.seasons_temp_v, { a: p.min, b: p.max });
      $$(".tipline, .rows small, .rows b", sd).forEach(function (n) { n.classList.remove("flip"); void n.offsetWidth; n.classList.add("flip"); });
    }
    $$(".chip", sd).forEach(function (c, i) { c.addEventListener("click", function () { cur.p = i; render(true); }); });
    $$(".stab", sd).forEach(function (c, i) { c.addEventListener("click", function () { cur.s = i; render(false); }); });
    render(true);
  }

  /* ---------------------------------------------------------- real screens: edge recede + buttons */
  var sc = $(".screens");
  if (sc) {
    var items = $$(".scr", sc);
    function flow() {
      var mid = window.innerWidth / 2;
      items.forEach(function (it) {
        var r = it.getBoundingClientRect(), d = Math.min(1, Math.abs(r.left + r.width / 2 - mid) / (window.innerWidth * 0.6));
        it.style.setProperty("--s", (1 - d * 0.1).toFixed(3));
        it.style.setProperty("--o", (1 - d * 0.35).toFixed(3));
      });
    }
    if (!reduce) { sc.addEventListener("scroll", function () { requestAnimationFrame(flow); }, { passive: true }); window.addEventListener("resize", flow); flow(); }
    var step = function (dir) { var w = items[0] ? items[0].getBoundingClientRect().width + 28 : 280; sc.scrollBy({ left: dir * w, behavior: reduce ? "auto" : "smooth" }); };
    var pv = $(".scr-nav .prev"), nx = $(".scr-nav .next");
    if (pv) pv.addEventListener("click", function () { step(-1); });
    if (nx) nx.addEventListener("click", function () { step(1); });
  }

  /* ---------------------------------------------------------- light */
  var ld = $(".light-demo");
  if (ld && data) {
    var range = $(".lux", ld), win = $(".window", ld), nameEl = $(".l-name", ld), valEl = $(".l-val", ld), fits = $(".fits", ld);
    var nf = new Intl.NumberFormat(data.lang === "en" ? "en-US" : data.lang);
    var last = "";
    function lux(v) { return 50 * Math.pow(60000 / 50, v / 1000); }
    function upd() {
      var v = +range.value, l = lux(v), k = l < 800 ? "low" : l <= 10000 ? "bright" : "direct";
      var shown = l < 1000 ? Math.round(l / 10) * 10 : l < 10000 ? Math.round(l / 100) * 100 : Math.round(l / 1000) * 1000;
      win.style.setProperty("--L", (v / 1000).toFixed(3));
      nameEl.textContent = data.light[k];
      valEl.textContent = data.labels.light_value.replace("{lux}", nf.format(shown));
      range.setAttribute("aria-valuetext", data.light[k] + " · " + valEl.textContent);
      $$(".scale span", ld).forEach(function (s) { s.classList.toggle("on", s.getAttribute("data-k") === k); });
      if (k !== last) {
        last = k;
        fits.innerHTML = "";
        data.all.filter(function (s) { return s.light === k; }).forEach(function (s, i) {
          var li = document.createElement("li"); li.textContent = s.common; li.title = s.latin; li.style.setProperty("--i", i); fits.appendChild(li);
        });
      }
    }
    range.addEventListener("input", upd);
    upd();
  }

  /* ---------------------------------------------------------- Siri phrases */
  var ph = $$(".siri .phrases li");
  if (ph.length) {
    var pi = 0; ph[0].classList.add("on");
    if (!reduce) setInterval(function () { ph[pi].classList.remove("on"); pi = (pi + 1) % ph.length; ph[pi].classList.add("on"); }, 2800);
  }

  /* ---------------------------------------------------------- guides filter */
  var filters = $$(".filters .chip");
  filters.forEach(function (c) {
    c.addEventListener("click", function () {
      var cat = c.getAttribute("data-cat");
      filters.forEach(function (x) { var on = x === c; x.classList.toggle("on", on); x.setAttribute("aria-pressed", on ? "true" : "false"); });
      $$(".g-grid.all .g-card").forEach(function (g) { g.hidden = !(cat === "all" || g.getAttribute("data-cat") === cat); });
    });
  });

  /* ---------------------------------------------------------- checklists remember their ticks */
  $$(".checklist input[data-key]").forEach(function (cb) {
    var k = "mula-cl-" + cb.getAttribute("data-key");
    if (store.get(k) === "1") cb.checked = true;
    cb.addEventListener("change", function () { if (cb.checked) store.set(k, "1"); else store.del(k); });
  });

  /* ---------------------------------------------------------- paper mood (Light Paper / Dark Forest) */
  var mood = $(".mood");
  if (mood) mood.addEventListener("click", function () {
    var dark = doc.dataset.theme ? doc.dataset.theme === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    var next = dark ? "light" : "dark";
    doc.dataset.theme = next;
    store.set("mula-theme", next);
  });

  /* ---------------------------------------------------------- the tab bar's disc slides from the last page */
  var tb = $(".tabbar");
  if (tb && !reduce) {
    var now = parseInt(getComputedStyle(tb).getPropertyValue("--i"), 10), prev = null;
    try { prev = sessionStorage.getItem("mula-tab"); sessionStorage.setItem("mula-tab", String(now)); } catch (_) {}
    if (prev !== null && +prev !== now && now >= 0 && +prev >= 0) {
      var disc = $(".disc", tb);
      disc.style.transition = "none";
      tb.style.setProperty("--i", prev);
      void disc.offsetWidth;
      disc.style.transition = "";
      requestAnimationFrame(function () { tb.style.setProperty("--i", now); });
    }
  }

  /* ---------------------------------------------------------- "this site is also in …" */
  var hint = $(".lang-hint");
  if (hint && !store.get("mula-hint-closed")) {
    var want = (navigator.language || "").slice(0, 2).toLowerCase();
    var a = $('a[data-lang="' + want + '"]', hint);
    if (a && want !== doc.lang) {
      a.hidden = false;
      setTimeout(function () { hint.classList.add("show"); }, 4500);
    }
    $("button", hint).addEventListener("click", function () { hint.classList.remove("show"); store.set("mula-hint-closed", "1"); });
  }
})();
