/* HANE web demo: one short shift as the çırak, drawn with the game's own sprites.
   Built by _src/build.py from _src/static/demo.js — edit here, then rebuild.
   Rules follow the game (simplified): take the order at the table, call it out at the counter, the usta
   brews only what was called out, lift the glasses onto the tray (2 at a time), put each down at the table
   that ordered it, collect the bill (the çırak wipes the table while he is there), see the cat out. */
(function () {
  "use strict";
  var el = document.getElementById("demo"); if (!el) return;
  var S = JSON.parse(document.getElementById("demo-strings").textContent);
  var SP = "/HANE/assets/img/sp/";
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var ITEMS = {
    tea_strong: { price: 10, brew: 2.0 }, tea_light: { price: 10, brew: 2.0 },
    turkish_coffee: { price: 25, brew: 3.2 }, oralet_orange: { price: 16, brew: 2.4 }
  };
  var ORDER_POOL = ["tea_strong", "tea_strong", "tea_light", "tea_light", "turkish_coffee", "oralet_orange"];
  var CATS = [["mirmir", "Mırmır"], ["pamuk", "Pamuk"], ["aslan", "Aslan"], ["tekir", "Tekir"], ["karagoz", "Karagöz"]];
  var DAY = 90, TRAY = 2, WAIT_ORDER = 32, WAIT_TEA = 50;

  var W = 0, H = 0, k = 1, raf = 0, last = 0, running = false;
  var st;

  function $(tag, cls, parent) { var e = document.createElement(tag); if (cls) e.className = cls; if (parent) parent.appendChild(e); return e; }
  function img(name, parent, cls) { var i = $("img", cls, parent); i.src = SP + name + ".webp"; i.alt = ""; i.draggable = false; return i; }
  function fmt(s, o) { return s.replace(/\{(\w+)\}/g, function (_, n) { return o[n] !== undefined ? o[n] : ""; }); }
  function rnd(a, b) { return a + Math.random() * (b - a); }

  // ---------- scene ----------
  $("div", "wall", el); $("div", "rug", el);
  var layer = $("div", "", el); layer.style.cssText = "position:absolute;inset:0";
  function ent(name, x, y, w) {
    var e = $("div", "ent", layer); e._img = img(name, e); e._x = x; e._y = y; e._w = w; place(e); return e;
  }
  function place(e) {
    e.style.left = (e._x * W) + "px"; e.style.top = (e._y * H) + "px";
    e.style.width = (e._w * k) + "px"; e.style.zIndex = Math.round(e._y * 100);
  }
  var door = ent("door", 0.86, 0.235, 92);
  var plant = ent("plant", 0.96, 0.33, 56);
  ent("plant", 0.04, 0.95, 60);
  var usta = ent("usta", 0.13, 0.30, 70);
  var counter = ent("counter", 0.19, 0.37, 140);
  var readyRow = $("div", "ent", layer); readyRow.style.display = "flex"; readyRow.style.gap = "2px";
  readyRow._x = 0.19; readyRow._y = 0.255; readyRow._w = 120; place(readyRow); readyRow.style.zIndex = 99;
  var counterBubble = null;

  var TABLES = [{ x: 0.42, y: 0.60, guest: "guest_1_sit" }, { x: 0.74, y: 0.50, guest: "guest_3_sit" }, { x: 0.68, y: 0.86, guest: "guest_5_sit" }];
  TABLES.forEach(function (t, i) {
    t.id = i;
    t.guestEl = ent(t.guest, t.x - 0.005, t.y - 0.05, 64); t.guestEl.style.opacity = 0;
    t.el = ent("table", t.x, t.y, 96);
    t.cup = $("div", "ent", layer); t.cup._x = t.x; t.cup._y = t.y - 0.075; t.cup._w = 30; place(t.cup); t.cup.style.zIndex = Math.round(t.y * 100) + 1;
    t.btn = spot(t.x, t.y - 0.06, 120, fmt(S.table, { n: i + 1 }), function () { goTo(t.x - 0.09, t.y + 0.015, { table: t }); });
  });
  var cirak = ent("cirak", 0.30, 0.47, 58); cirak.classList.add("actor");
  var counterBtn = spot(0.19, 0.30, 150, S.counter, function () { goTo(0.26, 0.42, { counter: true }); });

  function spot(x, y, size, label, fn) {
    var b = $("button", "spot", el); b.type = "button"; b.setAttribute("aria-label", label);
    b._x = x; b._y = y; b._s = size; b.style.zIndex = 800;
    b.addEventListener("click", function (e) { e.stopPropagation(); if (running) fn(); });
    return b;
  }
  function placeSpot(b) { b.style.left = b._x * W + "px"; b.style.top = b._y * H + "px"; b.style.width = b.style.height = b._s * k + "px"; }

  // HUD
  var hud = $("div", "hud", el);
  var coinsChip = $("span", "chip", hud); img("coins", coinsChip); var coinsTxt = $("b", "", coinsChip);
  var servedChip = $("span", "chip", hud); img("i_happy", servedChip); var servedTxt = $("b", "", servedChip);
  var trayChip = $("span", "chip", hud); img("i_tray", trayChip); var trayBox = $("span", "tray", trayChip);
  var padChip = $("span", "chip", hud); img("i_megaphone", padChip); var padBox = $("span", "tray", padChip);
  var timeChip = $("span", "chip time", hud); var timeTxt = $("b", "", timeChip);
  trayChip.title = S.tray; padChip.title = S.notepad;
  var toastEl = $("div", "toast", el); toastEl.setAttribute("role", "status"); toastEl.setAttribute("aria-live", "polite");
  var toastT = 0;
  function toast(msg) { toastEl.textContent = msg; toastEl.classList.add("on"); toastT = 2.6; }
  function pop(x, y, txt) { var p = $("div", "pop", el); p.textContent = txt; p.style.left = x * W + "px"; p.style.top = y * H + "px"; setTimeout(function () { p.remove(); }, 1300); }
  function fx(name, x, y) { var f = img(name, el, "fx"); f.style.left = x * W + "px"; f.style.top = y * H + "px"; f.style.width = 56 * k + "px"; setTimeout(function () { f.remove(); }, 1150); }

  function bubble(host, icons, bar) {
    clearBubble(host);
    var b = $("div", "bubble", host); host._bubble = b;
    icons.forEach(function (n) { img(n, b); });
    if (bar) { var r = $("span", "bar", b); b._bar = $("b", "", r); }
    return b;
  }
  function clearBubble(host) { if (host._bubble) { host._bubble.remove(); host._bubble = null; } }

  // ---------- overlay ----------
  var ov = $("div", "overlay", el);
  function showOverlay(html, primary, secondary) {
    ov.innerHTML = ""; ov.hidden = false;
    var c = $("div", "card", ov); c.innerHTML = html;
    var row = $("div", "", c); row.style.cssText = "display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:12px";
    var b = $("button", "btn", row); b.type = "button"; b.textContent = primary; b.addEventListener("click", start);
    if (secondary) { var a = $("a", "btn red", row); a.href = secondary.href; a.textContent = secondary.label; }
    b.focus({ preventScroll: true });
  }
  showOverlay("<h3>" + S.title + "</h3><p>" + S.intro + "</p><ul><li>" + S.how.join("</li><li>") + "</li></ul>", S.start);

  // ---------- state ----------
  function start() {
    if (st && st.catEl) { st.catEl.remove(); if (st.catBtn) st.catBtn.remove(); }
    usta._img.src = SP + "usta.webp";
    st = { t: 0, coins: 0, tips: 0, served: 0, lost: 0, tray: [], pad: [], ready: [], brewing: 0, brewQueue: [],
      target: null, action: null, busy: 0, walkT: 0, cat: null, nextCat: 24, catsOut: 0 };
    TABLES.forEach(function (t, i) { setEmpty(t, i === 2 ? 3 : 0.4 + i * 0.8); });
    cirak._x = 0.30; cirak._y = 0.47; cirak._img.src = SP + "cirak.webp"; place(cirak);
    readyRow.innerHTML = ""; clearBubble(counter); clearBubble(cirak);
    ov.hidden = true; running = true; last = performance.now(); hudUpdate();
    toast(S.firstHint);
    cancelAnimationFrame(raf); raf = requestAnimationFrame(loop);
  }
  function setEmpty(t, delay) {
    t.state = "empty"; t.timer = delay; t.order = null; t.guestEl.style.opacity = 0; t.cup.innerHTML = ""; clearBubble(t.el);
  }
  function seat(t) {
    var g = ["guest_1_sit", "guest_2_sit", "guest_3_sit", "guest_4_sit", "guest_5_sit", "guest_6_sit"][Math.floor(Math.random() * 6)];
    t.guestEl._img.src = SP + g + ".webp"; t.guestEl.style.opacity = 1; t.guestEl.style.transition = "opacity .5s";
    t.state = "want"; t.wait = WAIT_ORDER; t.waitMax = WAIT_ORDER;
    bubble(t.el, ["i_exclamation"], true);
  }

  // ---------- movement ----------
  el.addEventListener("click", function (e) {
    if (!running || e.target.closest("button,a,.overlay")) return;
    var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / W, y = (e.clientY - r.top) / H;
    var near = null, best = 0.12;
    TABLES.forEach(function (t) { var dd = Math.hypot(x - t.x, (y - t.y) * H / W); if (dd < best) { best = dd; near = t; } });
    if (near) return near.btn.click();
    if (Math.hypot(x - 0.19, (y - 0.33) * H / W) < 0.12) return counterBtn.click();
    if (st.cat && Math.hypot(x - st.cat.x, (y - st.cat.y) * H / W) < 0.1) return st.catBtn.click();
    goTo(Math.min(0.95, Math.max(0.05, x)), Math.min(0.97, Math.max(0.36, y)), null);
  });
  function goTo(x, y, action) { if (st.busy > 0) return; st.target = { x: x, y: y }; st.action = action; }

  function loop(now) {
    var dt = Math.min(0.05, (now - last) / 1000); last = now;
    if (running) tick(dt);
    if (running) raf = requestAnimationFrame(loop);
  }
  document.addEventListener("visibilitychange", function () { last = performance.now(); });

  function tick(dt) {
    st.t += dt;
    if (toastT > 0 && (toastT -= dt) <= 0) toastEl.classList.remove("on");
    // walking
    if (st.busy > 0) { st.busy -= dt; if (st.busy <= 0) cirakPose(); }
    else if (st.target) {
      var dx = (st.target.x - cirak._x) * W, dy = (st.target.y - cirak._y) * H, dist = Math.hypot(dx, dy), sp = 300 * k * dt;
      if (dist <= sp) { cirak._x = st.target.x; cirak._y = st.target.y; st.target = null; cirakPose(); arrive(); }
      else {
        cirak._x += dx / dist * sp / W; cirak._y += dy / dist * sp / H;
        if (Math.abs(dx) > 2) cirak.classList.toggle("flip", dx < 0);
        st.walkT += dt; var f = Math.floor(st.walkT / 0.16) % 2 ? "b" : "a";
        cirak._img.src = SP + (st.tray.length ? "cirak_carry_walk_" : "cirak_walk_") + f + ".webp";
      }
      place(cirak);
    }
    // tables
    TABLES.forEach(function (t) {
      if (t.state === "empty") { if ((t.timer -= dt) <= 0 && st.t < DAY - 8) seat(t); }
      else if (t.state === "want" || t.state === "ordered") {
        t.wait -= dt; var b = t.el._bubble;
        if (b && b._bar) { b._bar.style.width = Math.max(0, t.wait / t.waitMax * 100) + "%"; b.classList.toggle("warn", t.wait < t.waitMax * 0.3); }
        if (t.wait <= 0) {
          st.lost++; bubble(t.el, ["i_angry"]); toast(S.leftAngry);
          st.pad = st.pad.filter(function (o) { return o.table !== t; });
          st.ready = st.ready.filter(function (o) { return o.table !== t; });
          st.tray = st.tray.filter(function (o) { return o.table !== t; });
          renderReady(); hudUpdate();
          t.state = "leaving"; t.timer = 1.2;
        }
      } else if (t.state === "leaving") { if ((t.timer -= dt) <= 0) setEmpty(t, rnd(2, 4)); }
      else if (t.state === "drinking") { if ((t.timer -= dt) <= 0) { t.state = "bill"; bubble(t.el, ["coins"]); } }
    });
    // the usta brews what was called out
    if (st.brewQueue.length) {
      st.brewing -= dt;
      if (st.brewing <= 0) {
        var o = st.brewQueue.shift(); st.ready.push(o); renderReady();
        st.brewing = st.brewQueue.length ? ITEMS[st.brewQueue[0].item].brew : 0;
        if (!st.brewQueue.length) { usta._img.src = SP + "usta.webp"; clearBubble(counter); }
      }
    }
    if (!st.target && st.busy <= 0 && atCounter() && st.ready.length && st.tray.length < TRAY) lift();
    // the cat
    if (!st.cat && st.t > st.nextCat && st.t < DAY - 10) catIn();
    if (st.cat) catTick(dt);
    // clock
    var left = Math.max(0, Math.ceil(DAY - st.t));
    timeTxt.textContent = Math.floor(left / 60) + ":" + ("0" + left % 60).slice(-2);
    if (st.t >= DAY) end();
  }

  function atCounter() { return Math.hypot((cirak._x - 0.26) * W, (cirak._y - 0.42) * H) < 30 * k; }
  function cirakPose(name) { cirak._img.src = SP + (name || (st.tray.length ? "cirak_carry" : "cirak")) + ".webp"; }
  function work(sec) { st.busy = sec; cirakPose("cirak_work"); }

  function arrive() {
    var a = st.action; st.action = null; if (!a) return;
    if (a.counter) {
      if (st.pad.length) {
        var items = st.pad.map(function (o) { return o.item; });
        bubble(counter, ["i_megaphone"].concat(items.slice(0, 4)));
        if (!st.brewQueue.length) st.brewing = ITEMS[st.pad[0].item].brew;
        st.brewQueue = st.brewQueue.concat(st.pad); st.pad = [];
        usta._img.src = SP + "usta_work.webp";
        toast(S.calledOut); hudUpdate();
      } else if (!st.ready.length && !st.brewQueue.length) toast(st.tray.length ? S.trayGo : S.nothingToCall);
      else if (st.tray.length >= TRAY && st.ready.length) toast(S.trayFull);
      return;
    }
    if (a.cat) return seeCatOut();
    var t = a.table;
    if (t.state === "want") {
      t.order = ORDER_POOL[Math.floor(Math.random() * ORDER_POOL.length)];
      st.pad.push({ table: t, item: t.order });
      t.state = "ordered"; t.wait = WAIT_TEA; t.waitMax = WAIT_TEA;
      bubble(t.el, [t.order], true); work(0.5);
      toast(fmt(S.orderTaken, { item: S.items[t.order] })); hudUpdate();
    } else if (t.state === "ordered") {
      var idx = -1;
      st.tray.forEach(function (o, i) { if (idx < 0 && o.table === t) idx = i; });
      if (idx < 0) { toast(st.pad.some(function (o) { return o.table === t; }) ? S.notCalled : S.notOnTray); return; }
      st.tray.splice(idx, 1);
      t.state = "drinking"; t.timer = rnd(3, 4.5); clearBubble(t.el);
      t.cup.innerHTML = ""; img(t.order, t.cup);
      st.served++; pop(t.x, t.y - 0.16, "♥"); toast(S.served); hudUpdate(); cirakPose();
    } else if (t.state === "bill") {
      var tip = Math.floor(rnd(0, 4)), price = ITEMS[t.order].price;
      st.coins += price + tip; st.tips += tip;
      pop(t.x, t.y - 0.14, "+" + (price + tip)); fx("coins", t.x, t.y - 0.08);
      t.guestEl.style.opacity = 0; clearBubble(t.el); t.cup.innerHTML = ""; img("empty_tea", t.cup);
      work(1.1); fx("bubbles", t.x, t.y - 0.03);
      setTimeout(function () { if (!running) return; t.cup.innerHTML = ""; fx("sparkles", t.x, t.y - 0.03); setEmpty(t, rnd(1.5, 3.5)); }, 1100);
      toast(tip ? fmt(S.paidTip, { n: price, tip: tip }) : fmt(S.paid, { n: price })); hudUpdate();
    } else if (t.state === "drinking") toast(S.stillDrinking);
    else if (t.state === "empty") toast(S.emptyTable);
  }

  function lift() {
    while (st.ready.length && st.tray.length < TRAY) st.tray.push(st.ready.shift());
    renderReady(); hudUpdate(); cirakPose(); toast(S.lifted);
  }
  function renderReady() {
    readyRow.innerHTML = ""; st.ready.forEach(function (o) { var i = img(o.item, readyRow); i.style.width = 26 * k + "px"; });
  }
  function hudUpdate() {
    coinsTxt.textContent = st.coins + " " + S.coin;
    servedTxt.textContent = st.served;
    trayBox.innerHTML = ""; for (var i = 0; i < TRAY; i++) { if (st.tray[i]) img(st.tray[i].item, trayBox); else $("span", "slot", trayBox); }
    padBox.innerHTML = ""; if (!st.pad.length) padBox.textContent = "–"; st.pad.slice(0, 4).forEach(function (o) { img(o.item, padBox); });
  }

  // ---------- the cat ----------
  function catIn() {
    var c = CATS[Math.floor(Math.random() * CATS.length)], t = TABLES[Math.floor(Math.random() * TABLES.length)];
    st.cat = { key: c[0], name: c[1], x: 0.86, y: 0.25, tx: t.x + 0.07, ty: t.y + 0.02, t: 0, table: t, out: false };
    st.catEl = ent("cat_" + c[0], 0.86, 0.25, 46);
    bubble(st.catEl, ["i_paw"]);
    st.catBtn = spot(0.5, 0.5, 70, fmt(S.catLabel, { cat: c[1] }), function () { goTo(st.cat.x - 0.06, st.cat.y, { cat: true }); });
    placeSpot(st.catBtn);
    toast(fmt(S.catIn, { cat: c[1] }));
  }
  function catTick(dt) {
    var c = st.cat; c.t += dt;
    var tx = c.out ? 0.86 : c.tx, ty = c.out ? 0.25 : c.ty;
    var dx = (tx - c.x) * W, dy = (ty - c.y) * H, dist = Math.hypot(dx, dy), sp = (c.out ? 260 : 120) * k * dt;
    if (dist > sp) { c.x += dx / dist * sp / W; c.y += dy / dist * sp / H; st.catEl.classList.toggle("flip", dx < 0); st.catEl.classList.add("actor"); }
    else if (c.out) { st.catEl.remove(); st.catBtn.remove(); st.cat = null; st.nextCat = st.t + 30; return; }
    else if (!c.sat) { c.sat = true; st.catEl._img.src = SP + "cat_" + c.key + "_sitting.webp"; }
    st.catEl._x = c.x; st.catEl._y = c.y; place(st.catEl);
    st.catBtn._x = c.x; st.catBtn._y = c.y - 0.05; placeSpot(st.catBtn);
    if (!c.out && c.t > 14) {
      var t = c.table;
      if (t.state === "drinking") { t.cup.innerHTML = ""; img("empty_tea", t.cup); }
      toast(fmt(S.catKnock, { cat: c.name })); c.out = true; c.sat = false; st.catEl._img.src = SP + "cat_" + c.key + ".webp"; clearBubble(st.catEl);
    }
  }
  function seeCatOut() {
    if (!st.cat || st.cat.out) return;
    st.cat.out = true; st.cat.sat = false; st.catsOut++;
    st.catEl._img.src = SP + "cat_" + st.cat.key + ".webp"; clearBubble(st.catEl);
    work(0.6); toast(fmt(S.catOut, { cat: st.cat.name }));
  }

  // ---------- end of the day ----------
  function end() {
    running = false; cancelAnimationFrame(raf);
    var kum = S.wage + Math.floor(st.tips / 2);
    showOverlay("<h3>" + S.dayOver + "</h3><p>" + fmt(S.summary, { served: st.served, coins: st.coins, tips: st.tips, lost: st.lost }) +
      "</p><p><strong>" + fmt(S.kumbara, { wage: S.wage, half: Math.floor(st.tips / 2), total: kum, left: (S.car - kum).toLocaleString(document.documentElement.lang) }) + "</strong></p>",
      S.again, { href: S.storeUrl, label: S.get });
  }

  // ---------- sizing ----------
  function resize() {
    var r = el.getBoundingClientRect(); W = r.width; H = r.height; k = Math.max(0.62, Math.min(1.1, W / 860));
    layer.querySelectorAll(".ent").forEach(place);
    el.querySelectorAll(".spot").forEach(placeSpot);
    readyRow.querySelectorAll("img").forEach(function (i) { i.style.width = 26 * k + "px"; });
  }
  window.addEventListener("resize", resize); resize();
  if (reduce) el.classList.add("still");
})();
