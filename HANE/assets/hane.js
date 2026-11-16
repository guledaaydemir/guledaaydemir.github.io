/* HANE website behaviour. Built by _src/build.py from _src/static/hane.js — edit here, then rebuild. */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  root.classList.remove("no-js");
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  // menu
  var mb = d.querySelector(".menu-btn"), links = d.getElementById("nav-links");
  if (mb && links) mb.addEventListener("click", function () {
    var open = links.classList.toggle("open"); mb.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // reveal on scroll (+ map pins, dream road)
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      if (e.target.dataset.road) moveRoad(e.target, parseFloat(e.target.dataset.road));
      io.unobserve(e.target);
    });
  }, { threshold: 0.18 }) : null;
  d.querySelectorAll(".reveal,.map,[data-road]").forEach(function (el) { io ? io.observe(el) : el.classList.add("in"); });

  // the çırak's road: share of the car saved -> place on the road (start stretched, like the game)
  function roadPos(share) { return 7 + 74 * Math.sqrt(Math.max(0, Math.min(1, share))); }
  function moveRoad(road, share) {
    var w = road.querySelector(".walker"); if (w) w.style.left = roadPos(share) + "%";
  }
  d.querySelectorAll(".road").forEach(function (road) {
    road.querySelectorAll(".flag").forEach(function (f) { f.style.left = roadPos(parseFloat(f.dataset.at)) + "%"; });
    var w = road.querySelector(".walker"); if (w) w.style.left = roadPos(0) + "%";
  });

  // kumbara calculator (story page)
  var calc = d.querySelector("[data-calc]");
  if (calc) {
    var tips = calc.querySelector("input"), out = calc.querySelector("[data-days]"), per = calc.querySelector("[data-per]");
    var road = calc.querySelector(".road"), wage = +calc.dataset.wage, car = +calc.dataset.car, share = +calc.dataset.share;
    var dayInput = calc.querySelector("[data-dayslider]"), dayOut = calc.querySelector("[data-dayout]"), saved = calc.querySelector("[data-saved]");
    var fmt = new Intl.NumberFormat(root.lang || "en");
    var update = function () {
      var p = wage + Math.floor(+tips.value * share);
      per.textContent = fmt.format(p);
      out.textContent = fmt.format(Math.ceil(car / p));
      var days = +dayInput.value, s = Math.min(car, days * p);
      dayOut.textContent = fmt.format(days);
      saved.textContent = fmt.format(s) + " / " + fmt.format(car);
      moveRoad(road, s / car);
    };
    tips.addEventListener("input", update); dayInput.addEventListener("input", update); update();
  }

  // ribbon cutting on the launch page
  var door = d.querySelector(".door");
  if (door) {
    var zone = door.querySelector(".cut-zone"), btn = d.querySelector("[data-cut]"), conf = door.querySelector(".confetti");
    var cut = function () {
      if (door.classList.contains("cut")) return;
      door.classList.add("cut"); store("hane-ribbon", "1");
      if (reduce || !conf) return;
      var colors = ["#e2483a", "#f2cf73", "#2aa3a3", "#ffffff", "#1f4f9c", "#77c452"];
      for (var i = 0; i < 70; i++) {
        var c = d.createElement("i"), a = Math.random() * Math.PI * 2, r = 120 + Math.random() * 260;
        c.style.background = colors[i % colors.length];
        c.style.setProperty("--x", Math.cos(a) * r + "px");
        c.style.setProperty("--y", Math.sin(a) * r * 0.8 + 140 + "px");
        c.style.setProperty("--r", (Math.random() * 720 - 360) + "deg");
        c.style.animationDelay = Math.random() * 0.25 + "s";
        conf.appendChild(c);
      }
      setTimeout(function () { conf.innerHTML = ""; }, 2600);
    };
    if (store("hane-ribbon") === "1") door.classList.add("cut");
    if (btn) btn.addEventListener("click", cut);
    if (zone) {
      var sx = null, sy = 0, ribbonY = function () { var r = door.getBoundingClientRect(); return r.top + r.height * 0.415; };
      zone.addEventListener("pointerdown", function (e) { sx = e.clientX; sy = e.clientY; });
      zone.addEventListener("pointermove", function (e) {
        if (sx === null) return;
        var y = ribbonY(), crossed = (sy - y) * (e.clientY - y) <= 0 || Math.abs(e.clientY - y) < 26;
        if (Math.abs(e.clientX - sx) > 50 && crossed) { cut(); sx = null; }
      });
      zone.addEventListener("pointerup", function (e) {
        if (sx !== null && Math.abs(e.clientX - sx) < 8 && Math.abs(e.clientY - ribbonY()) < 40) cut();
        sx = null;
      });
    }
  }

  // play the preview video only while visible
  d.querySelectorAll("video[data-autoplay]").forEach(function (v) {
    if (reduce || !("IntersectionObserver" in window)) return;
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause(); });
    }, { threshold: 0.4 }).observe(v);
  });

  // guide filters
  var fl = d.querySelector(".filters");
  if (fl) fl.addEventListener("click", function (e) {
    var b = e.target.closest("button"); if (!b) return;
    fl.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
    var c = b.dataset.cat;
    d.querySelectorAll(".gcard").forEach(function (g) { g.parentElement.hidden = c !== "all" && g.dataset.cat !== c; });
  });

  // suggest the reader's language once (no automatic redirect)
  var hint = d.querySelector(".lang-hint");
  if (hint && !store("hane-lang-hint")) {
    var want = (navigator.languages || [navigator.language || ""]).map(function (l) { return (l || "").slice(0, 2).toLowerCase(); });
    var pick = null;
    for (var i = 0; i < want.length && !pick; i++) if (want[i] !== root.lang && hint.querySelector('[data-lang="' + want[i] + '"]')) pick = want[i];
    if (pick && want[0] !== root.lang) {
      hint.querySelectorAll("[data-lang]").forEach(function (a) { a.hidden = a.dataset.lang !== pick; });
      hint.classList.add("on");
    }
    hint.addEventListener("click", function (e) {
      if (e.target.closest("button,a")) { store("hane-lang-hint", "1"); hint.classList.remove("on"); }
    });
  }
})();
