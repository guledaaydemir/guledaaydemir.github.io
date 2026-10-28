#!/usr/bin/env python3
"""Renders the blog cover image for each DUMP guide and ideas page.

    python3 DUMP/tools/covers/build.py            # render covers whose inputs changed
    python3 DUMP/tools/covers/build.py --force    # re-render every cover
    python3 DUMP/tools/covers/build.py --only travel-photo-dump

Each cover is 1200x630: a few of the photos in tools/covers/photos/ laid out as a dump on the left, and an
iPhone on the right showing a recreation of a real DUMP screen (Preview, Swipe Carousel editor, grid canvas or
Caption Generator) filled with the same photos. Labels match the app's own English strings.
Covers are listed in covers.json. Output, per slug, in DUMP/assets/covers/:
  <slug>.jpg (1200x630, share image), <slug>-1200.webp and <slug>-600.webp (page and cards).
Rendered with headless Google Chrome; Pillow converts the results.
"""
import hashlib, html, json, os, shutil, subprocess, sys, tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
DUMP = os.path.dirname(os.path.dirname(TOOLS))
OUT = os.path.join(DUMP, "assets", "covers")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
e = html.escape

def photo(name):
    path = os.path.join(TOOLS, "photos", name + ".jpg")
    if not os.path.exists(path):
        sys.exit(f"photo not found: tools/covers/photos/{name}.jpg")
    return "file://" + path

def bg(name):
    return f"background-image:url('{photo(name)}')"

# ---------------------------------------------------------------- icons (24px, stroke)
def icon(name, size=18, sw=2, fill="none"):
    paths = {
        "back": '<path d="M15 5l-7 7 7 7"/>',
        "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
        "comment": '<path d="M20 12a8 8 0 0 1-11.6 7.1L4 20l1-4.2A8 8 0 1 1 20 12z"/>',
        "send": '<path d="M21 3L10 14"/><path d="M21 3l-7 18-4-7-7-4z"/>',
        "bookmark": '<path d="M6 3h12v18l-6-4-6 4z"/>',
        "more": '<circle cx="5" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="19" cy="12" r="1.3"/>',
        "save": '<rect x="4" y="5" width="16" height="15" rx="3"/><path d="M12 9v7M9 13l3 3 3-3"/>',
        "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
        "image": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-8 8"/>',
        "shuffle": '<path d="M3 7h4l10 10h4M17 7h4M3 17h4"/><path d="M19 5l2 2-2 2M19 15l2 2-2 2"/>',
        "fill": '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
        "reorder": '<path d="M7 4l-3 3 3 3M4 7h12M17 14l3 3-3 3M20 17H8"/>',
        "trash": '<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/>',
        "plus": '<path d="M12 5v14M5 12h14"/>',
        "undo": '<path d="M9 14L4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 0 12h-3"/>',
        "redo": '<path d="M15 14l5-5-5-5"/><path d="M20 9H10a6 6 0 0 0 0 12h3"/>',
        "share": '<path d="M12 3v12M8 7l4-4 4 4"/><path d="M6 11v9h12v-9"/>',
        "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
        "ratio": '<rect x="4" y="6" width="16" height="12" rx="2"/><path d="M8 10v4M12 10h4"/>',
        "slides": '<rect x="7" y="7" width="13" height="13" rx="2"/><path d="M4 16V5a1 1 0 0 1 1-1h11"/>',
        "x": '<path d="M6 6l12 12M18 6L6 18"/>',
        "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
        "plane": '<path d="M2 16l20-8-3 10-7-3-3 5-1-6z"/>',
        "cloud": '<path d="M7 18a4 4 0 0 1 0-8 6 6 0 0 1 11.3 2A3 3 0 0 1 18 18z"/>',
        "smile": '<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5a4.5 4.5 0 0 0 7 0"/><circle cx="9" cy="10" r=".8"/><circle cx="15" cy="10" r=".8"/>',
        "calendar": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
        "minus": '<path d="M6 12h12"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{paths[name]}</svg>')

STATUS = ('<div class="status"><b>09:41</b><span class="island"></span><span class="sig">'
          '<i></i><i></i><i></i><i></i><em class="wifi"></em><em class="batt"></em></span></div>')

# ---------------------------------------------------------------- app screens (402x874 logical points)
def screen_preview(s):
    n = s.get("count", 10)
    return f"""{STATUS}
<div class="top"><span class="round pink">{icon('back', 20, 2.6)}</span><div class="ttl"><b>Preview</b><small>1 / {n}</small></div><span class="round ghost"></span></div>
<div class="post">
  <div class="ph-head"><span class="avatar"></span><b>{e(s['title'])}</b><span class="dots">{icon('more', 20, 2)}</span></div>
  <div class="ph-img" style="{bg(s['photo'])}"><span class="count">1/{n}</span></div>
  <div class="pager">{''.join('<i class="on"></i>' if i == 0 else '<i></i>' for i in range(min(n, 9)))}</div>
  <div class="ph-icons">{icon('heart', 24, 1.8)}{icon('comment', 24, 1.8)}{icon('send', 24, 1.8)}<span class="sp"></span>{icon('bookmark', 24, 1.8)}</div>
</div>
<p class="note">{icon('check', 15, 2)} Original quality · Saved in this order</p>
<div class="btn pinkbtn">{icon('save', 20, 2)} Save to Photos</div>
<div class="btn darkbtn">Generate Caption</div>"""

def screen_editor(s):
    strip = "".join(f'<span class="th{" sel" if i == 0 else ""}" style="{bg(p)}"></span>' for i, p in enumerate(s["strip"][:6]))
    tools = [("image", "Replace"), ("shuffle", "Random"), ("fill", "Fill"), ("reorder", "Reorder"), ("trash", "Remove"), ("plus", "Add")]
    return f"""{STATUS}
<div class="top"><span class="round pink">{icon('back', 20, 2.6)}</span><div class="ttl left"><b>{e(s['title'])}</b><small>1 / {s.get('count', 10)}</small></div>
<span class="pill">{icon('more', 18, 2)}<b>Preview</b></span></div>
<div class="ed-img" style="{bg(s['photo'])}"></div>
<div class="strip">{strip}</div>
<div class="toolbar">{''.join(f'<span>{icon(i, 22, 1.9)}<small>{l}</small></span>' for i, l in tools)}</div>"""

def screen_grid(s):
    cells = "".join(f'<span style="{bg(p)}"></span>' for p in s["photos"][:4])
    return f"""{STATUS}
<div class="top icons"><span class="round pink">{icon('back', 20, 2.6)}</span><small class="pg">1/3</small>
{icon('undo', 20, 2)}{icon('redo', 20, 2)}<span class="round line">{icon('more', 18, 2)}</span><span class="sp"></span><span class="round pink">{icon('share', 19, 2.2)}</span></div>
<div class="canvas"><div class="grid4">{cells}</div><span class="addslide">{icon('plus', 18, 2.4)}</span></div>
<div class="dumpit">{icon('shuffle', 15, 2.2)} Dump It</div>
<div class="gbar"><span><i class="dotw"></i><small>Background</small></span><span>{icon('layers', 22, 1.9)}<small>Layers</small></span>
<span class="fab">{icon('plus', 26, 2.6)}</span><span>{icon('ratio', 22, 1.9)}<small>Ratio</small></span><span>{icon('slides', 22, 1.9)}<small>Slides</small></span></div>"""

def screen_caption(s):
    styles = [("cloud", "Soft Dump"), ("smile", "Funny Dump"), ("plane", "Travel Dump"), ("calendar", "Monthly Recap"),
              ("sparkle", "Influencer"), ("minus", "Minimal")]
    chips = "".join(f'<span class="chip{" on" if l == s["style"] else ""}">{icon(i, 15, 2)}{l}</span>' for i, l in styles)
    return f"""{STATUS}
<div class="top"><span class="round line">{icon('x', 18, 2.2)}</span><div class="ttl"><b>Caption Generator</b></div><span class="round ghost"></span></div>
<p class="label">CAPTION STYLE</p>
<div class="chips">{chips}</div>
<div class="capbox"><p>{e(s['caption'])}</p><small>Made in #DumpApp ✨</small>
<span class="mini">{icon('check', 13, 2)} DUMP tag added</span><span class="mini">Copy Caption</span></div>
<div class="btn pinkbtn low">{icon('sparkle', 18, 2)} Generate Another</div>
<div class="thumbs">{''.join(f'<span style="{bg(p)}"></span>' for p in s.get('photos', [])[:3])}</div>"""

SCREENS = {"preview": screen_preview, "editor": screen_editor, "grid": screen_grid, "caption": screen_caption}

# ---------------------------------------------------------------- left-hand art
def art_fan(a):
    p = a["photos"]
    return f"""<div class="fan">
<span class="card" style="left:20px;top:120px;width:250px;height:312px;transform:rotate(-10deg);{bg(p[1])}"></span>
<span class="card" style="left:330px;top:110px;width:250px;height:312px;transform:rotate(9deg);{bg(p[2])}"></span>
<span class="card front" style="left:150px;top:70px;width:300px;height:375px;transform:rotate(-2deg);{bg(p[0])}"></span></div>"""

def art_grid(a):
    cells = "".join(f'<span style="{bg(x)}"></span>' for x in a["photos"][:4])
    loose = a.get("loose")
    behind = f'<span class="card" style="left:330px;top:150px;width:240px;height:300px;transform:rotate(8deg);{bg(loose)}"></span>' if loose else ""
    return f'<div class="fan">{behind}<div class="page" style="left:70px;top:70px;transform:rotate(-3deg)"><div class="grid4">{cells}</div></div></div>'

def art_pick(a):
    tiles = []
    for t in a["tiles"][:6]:
        name, state = (t, "keep") if isinstance(t, str) else (t[0], t[1])
        badge = {"keep": f'<em class="ok">{icon("check", 22, 2.4)}</em>', "blurry": '<em class="tag">blurry</em>',
                 "duplicate": '<em class="tag">duplicate</em>'}[state]
        tiles.append(f'<span class="tile {state}"><i style="{bg(name)}"></i>{badge}</span>')
    return f'<div class="pick">{"".join(tiles)}</div>'

def art_seamless(a):
    p = a["photos"]
    return f"""<div class="seam" style="background:{a.get('paper', '#F2E3DC')}">
<span class="sp1" style="{bg(p[0])}"></span><span class="sp2" style="{bg(p[1])}"></span><span class="sp3" style="{bg(p[2])}"></span>
<span class="sp4" style="{bg(p[3])}"></span><i style="left:200px"></i><i style="left:400px"></i></div>"""

def art_ratios(a):
    p = a["photos"][0]
    frames = [("4:5", 196, 245), ("3:4", 186, 248), ("1:1", 196, 196)]
    return '<div class="ratios">' + "".join(
        f'<span class="rf"><i style="width:{w}px;height:{h}px;{bg(p)}"></i><b>{r}</b></span>' for r, w, h in frames) + "</div>"

def art_zoom(a):
    p = a["photos"][0]
    x, y = a.get("focus", ["50%", "35%"])
    return f"""<div class="fan"><span class="card front" style="left:90px;top:60px;width:330px;height:412px;transform:rotate(-2deg);{bg(p)}"></span>
<span class="lens" style="{bg(p)};background-size:900px auto;background-position:{x} {y}"></span></div>"""

ARTS = {"fan": art_fan, "grid": art_grid, "pick": art_pick, "seamless": art_seamless, "ratios": art_ratios, "zoom": art_zoom}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1200px;height:630px;overflow:hidden;background:#0D0D0D;font-family:system-ui,-apple-system,"SF Pro Text",sans-serif;color:#fff}
.bgph{position:absolute;inset:-60px;background-size:cover;background-position:center;filter:blur(34px) saturate(1.1) brightness(.42);transform:scale(1.1)}
.glow{position:absolute;inset:0;background:radial-gradient(60% 70% at 85% 10%,rgba(199,153,250,.30),transparent 70%),
 radial-gradient(50% 60% at 5% 100%,rgba(255,55,95,.22),transparent 70%),linear-gradient(90deg,rgba(13,13,13,.15),rgba(13,13,13,.55))}
.artbox{position:absolute;left:40px;top:0;width:660px;height:630px}
.fan{position:absolute;inset:0}
.card,.page,.tile,.rf i,.seam{box-shadow:0 26px 60px rgba(0,0,0,.55),0 4px 14px rgba(0,0,0,.35)}
.card{position:absolute;border-radius:20px;border:6px solid #F5F5F5;background-size:cover;background-position:center}
.card.front{box-shadow:0 0 0 1px rgba(255,55,95,.35),0 0 50px rgba(255,55,95,.35),0 30px 70px rgba(0,0,0,.65)}
.page{position:absolute;width:400px;height:500px;background:#F5F5F5;border-radius:18px;padding:12px}
.page .grid4{width:100%;height:100%}
.grid4{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:8px}
.grid4 span{background-size:cover;background-position:center;border-radius:6px}
.pick{position:absolute;left:30px;top:80px;display:grid;grid-template-columns:repeat(3,190px);gap:16px}
.tile{position:relative;width:190px;height:226px;border-radius:16px;overflow:hidden;border:4px solid #F5F5F5}
.tile i{position:absolute;inset:0;background-size:cover;background-position:center}
.tile.blurry i{filter:blur(5px);transform:scale(1.08)}
.tile.blurry,.tile.duplicate{opacity:.5;border-color:#555}
.tile .ok{position:absolute;right:10px;bottom:10px;width:38px;height:38px;border-radius:50%;background:#FF375F;display:grid;place-items:center;color:#fff}
.tile .tag{position:absolute;left:10px;bottom:10px;font-size:14px;font-weight:600;font-style:normal;background:rgba(0,0,0,.75);padding:5px 10px;border-radius:99px}
.seam{position:absolute;left:30px;top:150px;width:600px;height:330px;border-radius:14px;overflow:hidden}
.seam span{position:absolute;background-size:cover;background-position:center;border:5px solid #fff;box-shadow:0 10px 24px rgba(0,0,0,.3)}
.sp1{left:24px;top:40px;width:140px;height:175px;transform:rotate(-4deg)}
.sp2{left:132px;top:150px;width:136px;height:160px;transform:rotate(5deg)}
.sp3{left:300px;top:28px;width:200px;height:250px;transform:rotate(-2deg)}
.sp4{left:448px;top:120px;width:130px;height:170px;transform:rotate(6deg)}
.seam i{position:absolute;top:0;bottom:0;border-left:3px dashed rgba(13,13,13,.55)}
.ratios{position:absolute;left:20px;top:150px;display:flex;gap:22px;align-items:flex-end}
.rf{display:flex;flex-direction:column;align-items:center;gap:14px}
.rf i{display:block;background-size:cover;background-position:center 30%;border-radius:12px;border:5px solid #F5F5F5}
.rf b{font:700 22px ui-monospace,"SF Mono",monospace;color:#F5F5F5;background:rgba(0,0,0,.45);padding:4px 14px;border-radius:99px}
.lens{position:absolute;left:330px;top:300px;width:230px;height:230px;border-radius:50%;border:6px solid #F5F5F5;
 box-shadow:0 0 0 2px #FF375F,0 24px 60px rgba(0,0,0,.6)}
/* phone */
.phone{position:absolute;left:792px;top:34px;width:272px;height:586px;border-radius:50px;padding:9px;
 background:linear-gradient(160deg,#4a4a4a,#151515 40%,#2a2a2a);box-shadow:0 0 0 1.5px rgba(255,255,255,.08),0 40px 90px rgba(0,0,0,.7),0 0 70px rgba(199,153,250,.18)}
.scr{position:relative;width:254px;height:568px;border-radius:42px;overflow:hidden;background:#000}
.app{position:absolute;left:0;top:0;width:402px;height:874px;transform:scale(.6318);transform-origin:0 0;background:#000;color:#fff;font-size:15px}
.status{height:54px;display:flex;align-items:center;justify-content:space-between;padding:0 34px 0 40px}
.status b{font-size:17px;font-weight:600}
.island{position:absolute;left:138px;top:12px;width:126px;height:36px;border-radius:20px;background:#000;box-shadow:0 0 0 1px #111}
.sig{display:flex;align-items:flex-end;gap:2px}
.sig i{display:block;width:3.5px;background:#fff;border-radius:1px}.sig i:nth-child(1){height:5px}.sig i:nth-child(2){height:7px}.sig i:nth-child(3){height:9px}.sig i:nth-child(4){height:11px}
.wifi{display:block;width:16px;height:11px;margin-left:6px;border-radius:16px 16px 0 0;border:3px solid #fff;border-bottom:0}
.batt{display:block;width:25px;height:12px;margin-left:6px;border-radius:4px;border:1.5px solid #30D158;background:linear-gradient(90deg,#30D158 70%,transparent 70%)}
.top{display:flex;align-items:center;gap:12px;padding:8px 16px 12px}
.round{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;flex:none;background:#1C1C1E}
.round.pink{color:#FF375F}.round.ghost{background:none}.round.line{background:#1C1C1E;color:#fff}
.ttl{flex:1;text-align:center;line-height:1.2}.ttl.left{text-align:left}
.ttl b{display:block;font-size:17px;font-weight:600}.ttl small{font-size:12.5px;color:#8E8E93}
.pill{display:flex;align-items:center;gap:8px;background:#1C1C1E;border-radius:99px;padding:9px 14px;color:#fff}
.pill b{color:#FF375F;font-weight:600}
.post{margin:4px 16px 0;background:#1C1C1E;border-radius:22px;padding:12px 12px 14px}
.ph-head{display:flex;align-items:center;gap:10px;padding:2px 4px 12px}
.avatar{width:30px;height:30px;border-radius:50%;background:radial-gradient(circle at 50% 38%,#FF8FA6 0 26%,#FF375F 27%)}
.ph-head b{font-size:15px;font-weight:600}.dots{margin-left:auto;color:#aaa}
.ph-img{position:relative;width:100%;aspect-ratio:4/5;border-radius:6px;background-size:cover;background-position:center}
.count{position:absolute;right:12px;top:12px;font-size:12.5px;font-weight:600;background:rgba(0,0,0,.55);padding:4px 10px;border-radius:99px}
.pager{display:flex;justify-content:center;gap:5px;padding:10px 0 4px}.pager i{width:6px;height:6px;border-radius:50%;background:#555}.pager i.on{background:#FF375F}
.ph-icons{display:flex;gap:18px;padding:6px 6px 0;color:#fff}.ph-icons .sp{flex:1}
.note{display:flex;justify-content:center;align-items:center;gap:6px;font-size:13px;color:#C9C9CE;margin:16px 0 14px}.note svg{color:#FF375F}
.btn{margin:0 16px 12px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:10px;font-size:17px;font-weight:600}
.pinkbtn{background:#FF375F}.darkbtn{background:#1C1C1E}
.ed-img{margin:10px 16px 0;height:470px;border-radius:4px;background-size:cover;background-position:center}
.strip{display:flex;gap:10px;padding:22px 16px 14px;overflow:hidden}
.strip .th{flex:none;width:52px;height:64px;border-radius:9px;background-size:cover;background-position:center}
.strip .th.sel{box-shadow:0 0 0 3px #FF375F}
.toolbar{margin:6px 16px 0;background:#1C1C1E;border-radius:22px;display:flex;justify-content:space-around;padding:14px 4px}
.toolbar span,.gbar span{display:flex;flex-direction:column;align-items:center;gap:6px;color:#fff}
.toolbar small,.gbar small{font-size:11.5px}
.top.icons{gap:16px;color:#fff}.pg{font-size:14px;color:#ddd}.top .sp{flex:1}
.canvas{position:relative;margin:70px auto 0;width:300px;height:375px;background:#2a2a2a}
.canvas .grid4{position:absolute;inset:0;gap:3px}.canvas .grid4 span{border-radius:0}
.addslide{position:absolute;right:-50px;top:170px;width:36px;height:36px;border-radius:50%;background:#1C1C1E;display:grid;place-items:center}
.dumpit{position:absolute;right:20px;top:690px;background:#FF375F;border-radius:99px;padding:11px 18px;font-weight:600;display:flex;gap:8px;align-items:center}
.gbar{position:absolute;left:0;right:0;bottom:22px;display:flex;justify-content:space-around;align-items:center;padding:0 10px}
.dotw{display:block;width:22px;height:22px;border-radius:50%;background:#fff}
.fab{width:62px;height:62px;border-radius:50%;background:#FF375F;display:grid !important;place-items:center}
.label{font-size:12.5px;color:#8E8E93;letter-spacing:.4px;padding:22px 20px 10px}
.chips{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:0 16px}
.chip{display:flex;align-items:center;gap:8px;background:#1C1C1E;border-radius:14px;padding:14px 14px;font-size:14px;font-weight:500}
.chip svg{color:#FF375F}.chip.on{background:#FF375F}.chip.on svg{color:#fff}
.capbox{margin:22px 16px 0;background:#1C1C1E;border-radius:22px;padding:30px 20px 22px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:12px}
.capbox p{font-size:19px;font-weight:500;line-height:1.35;margin-bottom:22px}
.capbox small{font-size:12px;color:#8E8E93}
.mini{display:flex;align-items:center;gap:6px;font-size:13px;color:#FF375F;background:rgba(255,55,95,.15);padding:7px 14px;border-radius:99px}
.low{margin-top:26px}
.thumbs{display:flex;justify-content:center;gap:12px;margin-top:20px}
.thumbs span{width:96px;height:120px;border-radius:10px;background-size:cover;background-position:center;opacity:.9}
"""

def cover_html(c):
    art = ARTS[c["art"]["type"]](c["art"])
    scr = SCREENS[c["screen"]["type"]](c["screen"])
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body>
<div class="bgph" style="{bg(c['bg'])}"></div><div class="glow"></div>
<div class="artbox">{art}</div>
<div class="phone"><div class="scr"><div class="app">{scr}</div></div></div>
</body></html>"""

def render(items, force):
    from PIL import Image
    os.makedirs(OUT, exist_ok=True)
    cache_file = os.path.join(TOOLS, "cache.json")
    cache = json.load(open(cache_file)) if os.path.exists(cache_file) else {}
    tmp = tempfile.mkdtemp(prefix="dump-covers-")
    done = 0
    try:
        for c in items:
            doc = cover_html(c)
            stamp = doc + "".join(hashlib.sha1(open(p[7:], "rb").read()).hexdigest()
                                  for p in sorted(set(x.split("'")[1] for x in doc.split("url(")[1:])))
            digest = hashlib.sha1(stamp.encode()).hexdigest()
            jpg = os.path.join(OUT, c["slug"] + ".jpg")
            if not force and cache.get(c["slug"]) == digest and os.path.exists(jpg):
                continue
            src, png = os.path.join(tmp, "c.html"), os.path.join(tmp, "c.png")
            open(src, "w", encoding="utf-8").write(doc)
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                            "--allow-file-access-from-files", f"--user-data-dir={os.path.join(tmp, 'profile')}",
                            "--window-size=1200,630", "--virtual-time-budget=6000", f"--screenshot={png}", "file://" + src],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
            img = Image.open(png).convert("RGB").crop((0, 0, 1200, 630))
            img.save(jpg, "JPEG", quality=84, optimize=True, progressive=True)
            img.save(os.path.join(OUT, c["slug"] + "-1200.webp"), "WEBP", quality=80, method=6)
            img.resize((600, 315), Image.LANCZOS).save(os.path.join(OUT, c["slug"] + "-600.webp"), "WEBP", quality=80, method=6)
            cache[c["slug"]] = digest
            done += 1
            print("  cover", c["slug"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    json.dump(dict(sorted(cache.items())), open(cache_file, "w"), indent=1)
    return done

def main():
    args = sys.argv[1:]
    items = json.load(open(os.path.join(TOOLS, "covers.json"), encoding="utf-8"))["covers"]
    if "--only" in args:
        want = set(args[args.index("--only") + 1].split(","))
        items = [c for c in items if c["slug"] in want]
    n = render(items, "--force" in args or "--only" in args)
    print(f"{n} cover(s) rendered into DUMP/assets/covers/")

if __name__ == "__main__":
    main()
