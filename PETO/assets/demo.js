/* PETO web demo: a tiny, simplified PETO Home with a fast-forward clock, reminders with actions, one-tap logging,
   a log and weekly-style counters. Made-up times; the real app schedules local notifications on the iPhone. */
(function () {
  "use strict";
  var host = document.getElementById("demo"), data = document.getElementById("demo-strings");
  if (!host || !data) return;
  var S = JSON.parse(data.textContent);
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var TYPES = ["feed", "walk", "play", "cuddle"];
  var ICON = { feed: "bowl", walk: "leash", play: "ball", cuddle: "heart" };
  var PETS = [
    { id: "buddy", name: "Buddy", type: "dog", sprite: "pet_dog_golden", plan: { feed: [450, 1110], walk: [540, 1140], play: [1020], cuddle: [1200] } },
    { id: "milo", name: "Milo", type: "cat", sprite: "pet_cat_gray", plan: { feed: [480, 1170], play: [1080], cuddle: [1260] } },
    { id: "poppy", name: "Poppy", type: "rabbit", sprite: "pet_rabbit_gray", plan: { feed: [510, 1080], play: [960], cuddle: [1230] } }
  ];
  var st;
  function fresh() {
    st = { now: 420, sel: "buddy", tab: "home", done: {}, skipped: {}, log: [], notifs: [], snooze: [], fired: {} };
  }
  fresh();

  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var fmt = function (m) { m = ((m % 1440) + 1440) % 1440; var h = Math.floor(m / 60), mm = m % 60; return (h < 10 ? "0" : "") + h + ":" + (mm < 10 ? "0" : "") + mm; };
  var tpl = function (s, o) { return s.replace(/\{(\w+)\}/g, function (_, k) { return o[k]; }); };
  var key = function (pet, type, t) { return pet.id + ":" + type + ":" + t; };
  var pet = function (id) { return PETS.filter(function (p) { return p.id === id; })[0]; };

  // ---------------------------------------------------------------- status, like PetStatusResolver (schedule-derived)
  function status(p) {
    var best = { rank: 0, text: S.st_ok, cls: "ok" };
    TYPES.forEach(function (type) {
      (p.plan[type] || []).forEach(function (t) {
        var k = key(p, type, t), done = st.done[k], skip = st.skipped[k];
        var r = null;
        if (done && st.now - done < 120) r = { rank: 1, cls: "done", text: { feed: S.st_full, walk: S.st_walked, play: S.st_played, cuddle: S.st_loved }[type] };
        else if (!done && !skip && st.now >= t + 60) r = { rank: 4, cls: "late", text: { feed: S.st_hungry, walk: S.st_walk_late, play: S.st_play_now, cuddle: S.st_cuddle_now }[type] };
        else if (!done && !skip && st.now >= t) r = { rank: 3, cls: "now", text: { feed: S.st_meal_now, walk: S.st_walk_now, play: S.st_play_now, cuddle: S.st_cuddle_now }[type] };
        else if (!done && !skip && t - st.now <= 60 && t > st.now && (type === "feed" || type === "walk")) r = { rank: 2, cls: "soon", text: type === "feed" ? S.st_meal_soon : S.st_walk_soon };
        if (r && r.rank > best.rank) best = r;
      });
    });
    return best;
  }
  function next(p) {
    var n = null;
    TYPES.forEach(function (type) {
      (p.plan[type] || []).forEach(function (t) {
        var k = key(p, type, t);
        if (st.done[k] || st.skipped[k]) return;
        if (!n || t < n.t) n = { t: t, type: type };
      });
    });
    if (!n) return "";
    var d = n.t - st.now, when = d <= 0 ? S.due : d >= 60 ? tpl(S.in_h, { n: Math.round(d / 60) }) : tpl(S.in_m, { n: d });
    return '<img class="px" src="' + S.ic + ICON[n.type] + '.webp" width="16" height="16" alt=""> ' + esc(S.next) + ": " + esc(when);
  }

  // ---------------------------------------------------------------- actions
  function logCare(p, type, silent) {
    var due = (p.plan[type] || []).filter(function (t) { var k = key(p, type, t); return !st.done[k] && !st.skipped[k] && t <= st.now + 60; });
    var t = due.length ? due[0] : null;
    if (t !== null) st.done[key(p, type, t)] = st.now;
    st.notifs = st.notifs.filter(function (n) { return !(n.pet === p.id && n.type === type); });
    st.log.unshift({ time: st.now, pet: p.id, type: type });
    if (!silent) burst(p.id);
    render();
  }
  function advance(mins) {
    var from = st.now;
    st.now = Math.min(st.now + mins, 1439);
    PETS.forEach(function (p) {
      TYPES.forEach(function (type) {
        (p.plan[type] || []).forEach(function (t) {
          var k = key(p, type, t);
          if (t > from && t <= st.now && !st.done[k] && !st.fired[k]) { st.fired[k] = 1; st.notifs.unshift({ pet: p.id, type: type, t: t }); }
        });
      });
    });
    st.snooze = st.snooze.filter(function (s) {
      if (s.at <= st.now) { st.notifs.unshift({ pet: s.pet, type: s.type, t: s.t }); return false; }
      return true;
    });
    st.notifs = st.notifs.slice(0, 2);
    render();
  }
  function notifAction(i, act) {
    var n = st.notifs[i], p = pet(n.pet);
    st.notifs.splice(i, 1);
    if (act === "done") return logCare(p, n.type);
    if (act === "snooze") { st.snooze.push({ pet: n.pet, type: n.type, t: n.t, at: st.now + 15 }); window.petoToast && window.petoToast(S.toast_snooze); }
    if (act === "skip") { st.skipped[key(p, n.type, n.t)] = 1; window.petoToast && window.petoToast(S.toast_skip); }
    render();
  }

  // ---------------------------------------------------------------- view
  function petCard(p) {
    var s = status(p), on = p.id === st.sel;
    return '<button type="button" class="d-pet' + (on ? " on" : "") + '" data-pet="' + p.id + '" aria-pressed="' + on + '">' +
      '<span class="d-av"><img class="px" src="' + S.sp + p.sprite + '.webp" width="56" height="56" alt=""></span>' +
      '<span class="d-info"><b>' + esc(p.name) + '</b><small>' + esc(S.names[p.type]) + "</small>" +
      '<span class="d-st ' + s.cls + '">' + esc(s.text) + '</span><small class="d-next">' + next(p) + "</small></span>" +
      '<span class="d-bar ' + s.cls + '" aria-hidden="true"></span></button>';
  }
  function careButtons() {
    var p = pet(st.sel);
    return '<div class="d-care">' + TYPES.map(function (type) {
      var has = !!p.plan[type];
      return '<button type="button" class="d-btn ' + type + '" data-care="' + type + '"' + (has ? "" : " disabled") + '>' +
        '<img class="px" src="' + S.ic + ICON[type] + '.webp" width="30" height="30" alt=""><span>' + esc(S[type]) + "</span></button>";
    }).join("") + "</div>";
  }
  function homeView() {
    var need = PETS.filter(function (p) { return status(p).rank >= 3; }).length;
    var greet = need ? tpl(need === 1 ? S.greet_need : S.greet_need_pl, { n: need }) : S.greet_ok;
    return '<div class="d-greet' + (need ? " warn" : "") + '"><img class="px" src="' + S.ic + 'bell.webp" width="22" height="22" alt="">' + esc(greet) + "</div>" +
      '<div class="d-h pp">' + esc(S.my_pets) + "</div>" + PETS.map(petCard).join("") + careButtons();
  }
  function logView() {
    if (!st.log.length) return '<div class="d-h pp">' + esc(S.today) + '</div><p class="d-empty">' + esc(S.nothing) + "</p>";
    return '<div class="d-h pp">' + esc(S.today) + '</div><ul class="d-log">' + st.log.slice(0, 12).map(function (l) {
      return '<li><img class="px" src="' + S.ic + ICON[l.type] + '.webp" width="22" height="22" alt=""><time>' + fmt(l.time) + "</time><span>" +
        esc(S["done_" + l.type]) + " – " + esc(pet(l.pet).name) + '</span><i aria-hidden="true">✓</i></li>';
    }).join("") + "</ul>";
  }
  function statsView() {
    var c = { feed: 0, walk: 0, play: 0, cuddle: 0 };
    st.log.forEach(function (l) { c[l.type]++; });
    var tile = function (type, label) {
      return '<div class="d-tile ' + type + '"><img class="px" src="' + S.ic + ICON[type] + '.webp" width="34" height="34" alt=""><b>' + c[type] + "</b><span>" + esc(label) + "</span></div>";
    };
    return '<div class="d-h pp">' + esc(S.tab_stats) + '</div><div class="d-tiles">' + tile("feed", S.stats_meals) + tile("walk", S.stats_walks) + tile("play", S.stats_play) + tile("cuddle", S.stats_cuddles) + "</div>";
  }
  function notifs() {
    return '<div class="d-notifs" aria-live="polite">' + st.notifs.map(function (n, i) {
      var p = pet(n.pet);
      return '<div class="d-notif"><div class="d-n-top"><img class="px" src="' + S.sp + p.sprite + '.webp" width="28" height="28" alt=""><b>' + esc(S.notif_app) +
        "</b><small>" + esc(S.notif_now) + "</small></div><p>" + esc(tpl(S["notif_" + n.type], { pet: p.name })) + '</p><div class="d-n-act">' +
        '<button type="button" data-n="' + i + '" data-act="done">' + esc(S.act_done) + '</button><button type="button" data-n="' + i + '" data-act="snooze">' +
        esc(S.act_snooze) + '</button><button type="button" data-n="' + i + '" data-act="skip">' + esc(S.act_skip) + "</button></div></div>";
    }).join("") + "</div>";
  }
  function render() {
    var view = st.tab === "home" ? homeView() : st.tab === "log" ? logView() : statsView();
    var tabs = [["home", "tab_home", S.tab_home], ["log", "tab_calendar", S.tab_log], ["stats", "tab_stats", S.tab_stats]].map(function (t) {
      return '<button type="button" data-tab="' + t[0] + '"' + (st.tab === t[0] ? ' aria-current="page"' : "") + '><img class="px" src="' + S.ic + t[1] + '.webp" width="24" height="24" alt=""><span>' + esc(t[2]) + "</span></button>";
    }).join("");
    host.innerHTML =
      '<div class="d-wrap"><div class="phone d-phone"><div class="screen"><div class="d-app">' +
      '<div class="d-status"><b>' + fmt(st.now) + '</b><span aria-hidden="true">▂▄▆ ◼</span></div>' +
      '<div class="d-bar-top pp">PETO</div>' + notifs() + '<div class="d-body">' + view + "</div>" +
      '<nav class="d-tabs">' + tabs + "</nav></div></div></div>" +
      '<div class="d-side panel"><div class="d-clock"><span>' + esc(S.clock) + '</span><b class="pp">' + fmt(st.now) + "</b></div>" +
      '<button type="button" class="btn gold" data-ff>⏩ ' + esc(S.ff) + '</button><button type="button" class="btn white sm" data-reset>↺ ' + esc(S.reset) + "</button>" +
      '<p class="d-hint">' + esc(S.hint) + '</p><a class="btn sm" href="' + esc(S.storeUrl) + '"' + (S.soon ? ' data-soon="' + esc(S.soon) + '"' : "") + ">" + esc(S.get) + "</a></div></div>";
  }
  function burst(id) {
    if (reduce) return;
    var card = host.querySelector('[data-pet="' + id + '"] .d-av') || host.querySelector(".d-body");
    if (!card) return;
    for (var i = 0; i < 5; i++) {
      var h = document.createElement("i");
      h.className = "d-heart";
      h.style.left = (10 + Math.random() * 70) + "%";
      h.style.animationDelay = (i * 0.08) + "s";
      card.appendChild(h);
      setTimeout(function (el) { return function () { el.remove(); }; }(h), 1300);
    }
    var ph = host.querySelector(".d-phone");
    if (ph) { ph.classList.remove("shake"); void ph.offsetWidth; ph.classList.add("shake"); }
  }

  host.addEventListener("click", function (ev) {
    var b = ev.target.closest("button");
    if (!b || !host.contains(b)) return;
    if (b.dataset.pet) { st.sel = b.dataset.pet; render(); }
    else if (b.dataset.care) logCare(pet(st.sel), b.dataset.care);
    else if (b.dataset.tab) { st.tab = b.dataset.tab; render(); }
    else if (b.dataset.act) notifAction(Number(b.dataset.n), b.dataset.act);
    else if (b.hasAttribute("data-ff")) advance(60);
    else if (b.hasAttribute("data-reset")) { fresh(); render(); }
  });
  render();
})();
