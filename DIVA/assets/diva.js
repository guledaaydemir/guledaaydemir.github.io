/* DIVA website interactions. No trackers, no cookies. */
(() => {
  const root = document.documentElement;
  root.classList.remove("no-js");
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch { /* private mode */ } },
  };

  /* ---- mobile menu ---- */
  const menuBtn = $(".menu-btn"), links = $(".nav-links");
  if (menuBtn && links) {
    menuBtn.addEventListener("click", () => {
      const open = links.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open);
    });
    links.addEventListener("click", e => { if (e.target.closest("a")) { links.classList.remove("open"); menuBtn.setAttribute("aria-expanded", "false"); } });
  }

  /* ---- reveal on scroll ---- */
  const io = "IntersectionObserver" in window && !reduce
    ? new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -8% 0px", threshold: .12 })
    : null;
  $$(".reveal").forEach(el => io ? io.observe(el) : el.classList.add("in"));

  /* ---- sparkles ---- */
  if (!reduce) {
    $$(".sparkles").forEach(box => {
      const n = +box.dataset.n || 14;
      for (let i = 0; i < n; i++) {
        const s = document.createElement("i");
        s.className = "spark";
        s.style.cssText = `left:${Math.random() * 100}%;top:${Math.random() * 100}%;--s:${8 + Math.random() * 16}px;--t:${2.2 + Math.random() * 3}s;--dl:${-Math.random() * 5}s`;
        box.appendChild(s);
      }
    });
  }

  /* ---- Y2K cursor sparkle trail ---- */
  if (!reduce && matchMedia("(pointer: fine)").matches) {
    const colors = ["#fff", "#ffc7e5", "#ff1493", "#dfc7a1"];
    let last = 0;
    addEventListener("pointermove", e => {
      const now = performance.now();
      if (now - last < 45) return;
      last = now;
      const t = document.createElement("i");
      t.className = "trail";
      t.style.cssText = `left:${e.clientX}px;top:${e.clientY}px;--c:${colors[(Math.random() * colors.length) | 0]};transform:scale(${.5 + Math.random()})`;
      document.body.appendChild(t);
      setTimeout(() => t.remove(), 900);
    }, { passive: true });
  }

  /* ---- flip phone texts ---- */
  const phone = $(".phone");
  if (phone) {
    const msgs = $$(".phone-msg", phone), typing = $(".phone-typing", phone);
    let i = 0;
    const next = () => {
      if (i >= msgs.length) { if (typing) typing.hidden = true; return; }
      msgs[i++].classList.add("on");
      setTimeout(next, reduce ? 0 : 1300);
    };
    setTimeout(next, reduce ? 0 : 900);
  }

  /* ---- weekday highlight (Mon = 0) ---- */
  const dow = (new Date().getDay() + 6) % 7;
  $$(".week").forEach(w => { const d = w.children[dow]; if (d) d.classList.add("today"); });

  /* ---- CD shelf era filter ---- */
  const filter = $(".era-filter");
  if (filter) {
    filter.addEventListener("click", e => {
      const b = e.target.closest("button"); if (!b) return;
      $$("button", filter).forEach(x => x.setAttribute("aria-pressed", x === b));
      const era = b.dataset.era;
      $$(".shelf .cd").forEach(cd => { cd.hidden = era !== "all" && cd.dataset.era !== era; });
      $(".shelf").scrollTo({ left: 0, behavior: reduce ? "auto" : "smooth" });
    });
  }

  /* ---- Pink Aura: the app's soundscape, rebuilt in Web Audio ---- */
  let ctx, aura;
  function startAura() {
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return;
    if (!ctx) {
      ctx = new AC();
      const master = ctx.createGain(); master.gain.value = 0; master.connect(ctx.destination);
      const merger = ctx.createChannelMerger(2); merger.connect(master);
      const freqs = [110, 164.81, 220, 277.18, 329.63], amps = [.2, .14, .12, .08, .06], rates = [.05, .071, .043, .093, .061];
      freqs.forEach((f, k) => [0, 1].forEach(ch => {
        const o = ctx.createOscillator(); o.frequency.value = f + (ch ? .35 : 0);
        const g = ctx.createGain(); g.gain.value = amps[k] * .55;
        const l = ctx.createOscillator(); l.frequency.value = rates[k];
        const lg = ctx.createGain(); lg.gain.value = amps[k] * .45;
        l.connect(lg).connect(g.gain); o.connect(g).connect(merger, 0, ch);
        o.start(); l.start();
      }));
      const len = ctx.sampleRate * 4, buf = ctx.createBuffer(2, len, ctx.sampleRate);
      for (let c = 0; c < 2; c++) { // pink-ish noise (Paul Kellet)
        const d = buf.getChannelData(c); let b0 = 0, b1 = 0, b2 = 0;
        for (let i = 0; i < len; i++) { const w = Math.random() * 2 - 1; b0 = .99765 * b0 + w * .099046; b1 = .963 * b1 + w * .2965164; b2 = .57 * b2 + w * 1.0526913; d[i] = (b0 + b1 + b2 + w * .1848) * .05; }
      }
      const n = ctx.createBufferSource(); n.buffer = buf; n.loop = true;
      const lp = ctx.createBiquadFilter(); lp.type = "lowpass"; lp.frequency.value = 1200;
      const ng = ctx.createGain(); ng.gain.value = .24;
      n.connect(lp).connect(ng).connect(master); n.start();
      aura = master;
    }
    ctx.resume();
    aura.gain.cancelScheduledValues(ctx.currentTime);
    aura.gain.setTargetAtTime(.2, ctx.currentTime, .6);
  }
  function stopAura() { if (aura) aura.gain.setTargetAtTime(0, ctx.currentTime, .35); }

  /* ---- demo player ---- */
  const player = $(".player");
  const demoData = $("#demo-data");
  if (player && demoData) {
    const D = JSON.parse(demoData.textContent);
    const audio = new Audio(); audio.preload = "none";
    const disc = $(".disc", player), discImg = $(".disc img", player);
    const lyrics = $(".lyrics", player), bar = $(".bar i", player);
    const title = $(".now strong", player), sub = $(".now .who", player);
    const auraToggle = $("#aura", player);
    let cd = D.first, voice = D.voices[0].id, playing = false;

    const key = () => `${cd}/${voice}/${D.audioLang}`;
    function render() {
      const c = D.cds[cd];
      discImg.src = c.cover; discImg.alt = c.title;
      title.textContent = c.title;
      sub.textContent = D.voices.find(v => v.id === voice).name;
      lyrics.innerHTML = c.lines.map((l, i) => `<li>${l}${c.tr && c.tr[i] ? `<small>${c.tr[i]}</small>` : ""}</li>`).join("");
      bar.style.width = "0";
    }
    function load(autoplay) {
      const m = D.timings[key()];
      audio.src = D.base + m.src;
      render();
      if (autoplay) play();
    }
    function play() {
      if (!audio.src) load(false);
      audio.play().then(() => {
        playing = true; player.classList.add("playing"); disc.classList.remove("paused");
        if (auraToggle.checked) startAura();
      }).catch(() => {});
    }
    function pause() { audio.pause(); }
    audio.addEventListener("pause", () => { playing = false; player.classList.remove("playing"); disc.classList.add("paused"); stopAura(); });
    audio.addEventListener("ended", () => { $$("li", lyrics).forEach(li => { li.classList.remove("on"); li.classList.add("done"); }); bar.style.width = "100%"; });
    audio.addEventListener("timeupdate", () => {
      const m = D.timings[key()]; if (!m) return;
      const t = audio.currentTime;
      bar.style.width = `${Math.min(100, (t / m.d) * 100)}%`;
      $$("li", lyrics).forEach((li, i) => {
        const [a, b] = m.t[i];
        li.classList.toggle("on", t >= a - .15 && t < b + .6);
        li.classList.toggle("done", t >= b + .6);
      });
    });
    $(".play", player).addEventListener("click", () => (playing ? pause() : play()));
    auraToggle.addEventListener("change", () => { if (playing) auraToggle.checked ? startAura() : stopAura(); });
    $$("[data-cd]", player).forEach(b => b.addEventListener("click", () => {
      $$("[data-cd]", player).forEach(x => x.setAttribute("aria-pressed", x === b));
      cd = b.dataset.cd; const was = playing; audio.pause(); load(was);
    }));
    $$("[data-voice]", player).forEach(b => b.addEventListener("click", () => {
      $$("[data-voice]", player).forEach(x => x.setAttribute("aria-pressed", x === b));
      voice = b.dataset.voice; const was = playing; audio.pause(); load(was);
    }));
    disc.classList.add("paused");
    render();
  }

  /* ---- pull your diva card ---- */
  const pull = $(".pull"), cardData = $("#card-data");
  if (pull && cardData) {
    const C = JSON.parse(cardData.textContent);
    const flip = $(".flip", pull), line = $(".face .line", pull), from = $(".face .from b", pull), again = $(".again", pull);
    let era = Object.keys(C)[0], lastIdx = -1;
    const deal = () => {
      const list = C[era];
      let i; do { i = (Math.random() * list.length) | 0; } while (list.length > 1 && i === lastIdx);
      lastIdx = i; line.textContent = `“${list[i][0]}”`; from.textContent = list[i][1];
    };
    const go = () => {
      if (flip.classList.contains("flipped")) {
        flip.classList.remove("flipped");
        setTimeout(() => { deal(); flip.classList.add("flipped"); }, reduce ? 0 : 520);
      } else { deal(); flip.classList.add("flipped"); }
      if (again) again.hidden = false;
    };
    flip.addEventListener("click", go);
    if (again) again.addEventListener("click", go);
    $$(".pull .chip").forEach(b => b.addEventListener("click", () => {
      $$(".pull .chip").forEach(x => x.setAttribute("aria-pressed", x === b));
      era = b.dataset.era; lastIdx = -1; go();
    }));
  }

  /* ---- "this page is also in your language" ---- */
  const hints = $("#lang-hints");
  if (hints && !store.get("diva-lang-hint")) {
    const H = JSON.parse(hints.textContent);
    const want = (navigator.languages || [navigator.language]).map(l => (l || "").slice(0, 2).toLowerCase());
    const here = root.lang;
    const pref = want.find(l => H[l]);
    if (pref && pref !== here && want[0] === pref) {
      const h = H[pref], bar = document.createElement("div");
      bar.className = "lang-hint"; bar.lang = pref; bar.setAttribute("role", "region");
      bar.innerHTML = `<span>${h.text}</span><a class="btn sm" href="${h.href}">${h.go}</a><button type="button">${h.close}</button>`;
      document.body.appendChild(bar);
      requestAnimationFrame(() => setTimeout(() => bar.classList.add("show"), 1200));
      $("button", bar).addEventListener("click", () => { bar.classList.remove("show"); store.set("diva-lang-hint", "1"); });
      $("a", bar).addEventListener("click", () => store.set("diva-lang-hint", "1"));
    }
  }
})();
