/* PETO website: small progressive enhancements. Everything works without JavaScript; this adds the game feel. */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set: function (k, v) { try { if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (_) {} }
  };
  var $$ = function (sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); };

  // ---------------------------------------------------------------- toast ("coming soon" store links)
  var toastEl = document.querySelector(".toast"), toastTimer;
  function toast(text) {
    if (!toastEl) return;
    toastEl.textContent = text;
    toastEl.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }
  window.petoToast = toast;
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("[data-soon]");
    if (a && a.dataset.soon) { ev.preventDefault(); toast(a.dataset.soon); }
  });

  // ---------------------------------------------------------------- theme accent (Meadow, Sky, Honey, Berry, Blossom)
  function setAccent(k) {
    if (!k || k === "green") { delete root.dataset.accent; store.set("peto-accent", null); }
    else { root.dataset.accent = k; store.set("peto-accent", k); }
    var cur = root.dataset.accent || "green";
    $$("[data-accent]").forEach(function (b) { if (b !== root) b.setAttribute("aria-pressed", String(b.dataset.accent === cur)); });
  }
  $$("button[data-accent]").forEach(function (b) { b.addEventListener("click", function () { setAccent(b.dataset.accent); }); });
  setAccent(root.dataset.accent || "green");

  // ---------------------------------------------------------------- language hint
  var hint = document.querySelector(".lang-hint");
  if (hint && !store.get("peto-langhint")) {
    var here = root.lang, prefs = (navigator.languages || [navigator.language || ""]).map(function (l) { return String(l).slice(0, 2).toLowerCase(); });
    var want = null;
    for (var i = 0; i < prefs.length; i++) { if (prefs[i] === here) break; if (["en", "tr", "es"].indexOf(prefs[i]) > -1) { want = prefs[i]; break; } }
    var link = want && hint.querySelector('[data-lang="' + want + '"]');
    if (link) { link.hidden = false; hint.classList.add("show"); }
    hint.querySelector("button").addEventListener("click", function () { hint.classList.remove("show"); store.set("peto-langhint", "1"); });
  }

  // ---------------------------------------------------------------- typewriter
  function type(el, text) {
    if (reduce || !el) { if (el) el.textContent = text; return; }
    clearInterval(el._tw);
    var n = 0;
    el.textContent = "";
    el._tw = setInterval(function () {
      n += 2;
      el.textContent = text.slice(0, n);
      if (n >= text.length) clearInterval(el._tw);
    }, 18);
  }

  // ---------------------------------------------------------------- inventory
  var slots = $$(".slot");
  slots.forEach(function (s) {
    s.addEventListener("click", function () {
      slots.forEach(function (o) { o.setAttribute("aria-pressed", String(o === s)); });
      $$(".item-text").forEach(function (t) {
        var on = t.dataset.item === s.dataset.item;
        t.hidden = !on;
        if (on) { var p = t.querySelector("p"); p._full = p._full || p.textContent; type(p, p._full); }
      });
    });
  });

  // ---------------------------------------------------------------- RPG dialog (Why we made PETO)
  $$("[data-rpg]").forEach(function (box) {
    var lines = $$(".line", box), at = 0;
    function show(i) {
      lines.forEach(function (l, j) { l.hidden = j !== i; });
      var p = lines[i].querySelector("p"); p._full = p._full || p.textContent; type(p, p._full);
    }
    box.querySelector(".next").addEventListener("click", function () { at = (at + 1) % lines.length; show(at); });
    if ("IntersectionObserver" in window) {
      var seen = false;
      new IntersectionObserver(function (es, ob) { if (es[0].isIntersecting && !seen) { seen = true; show(0); ob.disconnect(); } }, { threshold: .5 }).observe(box);
    }
  });

  // ---------------------------------------------------------------- character select
  $$("[data-picker]").forEach(function (box) {
    var d = JSON.parse(box.dataset.picker), species = Object.keys(d.cat), si = 0, vi = 0;
    var big = box.querySelector(".pick"), name = box.querySelector(".pick-name"), tierEl = box.querySelector(".pick-tier"), vbox = box.querySelector(".variants");
    var spBtns = $$(".sp-btn", box);
    function render() {
      var sp = species[si], vs = d.cat[sp], v = vs[vi];
      big.src = d.sp + "pet_" + sp + "_" + v[0] + ".webp";
      big.alt = d.names[sp] + " · " + v[1];
      name.textContent = d.names[sp] + " · " + v[1];
      tierEl.innerHTML = '<span class="tag ' + (v[2] ? "premium" : "free") + '">' + (v[2] ? d.premium : d.free) + "</span>";
      vbox.innerHTML = "";
      vs.forEach(function (x, j) {
        var b = document.createElement("button");
        b.type = "button"; b.className = x[2] ? "locked" : ""; b.setAttribute("aria-pressed", String(j === vi));
        b.setAttribute("aria-label", d.names[sp] + " · " + x[1] + " (" + (x[2] ? d.premium : d.free) + ")");
        b.innerHTML = '<img class="px" src="' + d.sp + "pet_" + sp + "_" + x[0] + '.webp" width="44" height="44" alt="">';
        b.addEventListener("click", function () { vi = j; render(); });
        vbox.appendChild(b);
      });
      spBtns.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.species === sp)); });
    }
    spBtns.forEach(function (b) { b.addEventListener("click", function () { si = species.indexOf(b.dataset.species); vi = 0; render(); }); });
    $$(".arrow", box).forEach(function (a) {
      a.addEventListener("click", function () {
        vi += Number(a.dataset.step);
        if (vi > 7) { vi = 0; si = (si + 1) % species.length; }
        if (vi < 0) { si = (si - 1 + species.length) % species.length; vi = 7; }
        render();
      });
    });
    render();
  });

  // ---------------------------------------------------------------- guides filter
  var filters = $$(".filters button");
  filters.forEach(function (b) {
    b.addEventListener("click", function () {
      filters.forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
      $$(".gcards .gcard").forEach(function (c) { c.classList.toggle("hide", b.dataset.cat !== "all" && c.dataset.cat !== b.dataset.cat); });
    });
  });

  // ---------------------------------------------------------------- checklists (remembered in this browser only)
  $$(".checklist input[data-key]").forEach(function (c) {
    var k = "peto-check-" + root.lang + "-" + c.dataset.key;
    c.checked = store.get(k) === "1";
    c.addEventListener("change", function () { store.set(k, c.checked ? "1" : null); });
  });

  // ---------------------------------------------------------------- reading font
  var fontBtns = $$(".reading button");
  function setFont(f) {
    if (f === "clean") root.dataset.font = "clean"; else delete root.dataset.font;
    store.set("peto-font", f === "clean" ? "clean" : null);
    fontBtns.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.font === (root.dataset.font || "pixel"))); });
  }
  fontBtns.forEach(function (b) { b.addEventListener("click", function () { setFont(b.dataset.font); }); });
  if (fontBtns.length) setFont(root.dataset.font || "pixel");

  // ---------------------------------------------------------------- wide tables scroll on phones
  $$(".prose table").forEach(function (t) {
    if (t.parentNode.classList.contains("table-wrap")) return;
    var w = document.createElement("div"); w.className = "table-wrap"; t.parentNode.insertBefore(w, t); w.appendChild(t);
  });

  // ---------------------------------------------------------------- reveal on scroll
  var rev = $$(".reveal");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    rev.forEach(function (r) { io.observe(r); });
  } else {
    rev.forEach(function (r) { r.classList.add("in"); });
  }
})();
