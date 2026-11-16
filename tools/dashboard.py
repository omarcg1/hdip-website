#!/usr/bin/env python3
"""HDIP control panel.

Edits data/site.json — every piece of copy, every figure, every photo
assignment and the slideshow order — then regenerates the static site.

The site stays static: this runs locally (or behind your own auth), you edit,
you press Publish, and build.py rewrites the 58 pages. Nothing dynamic is
exposed to the public site.

    python3 tools/dashboard.py          # http://127.0.0.1:4620

Standard library only, matching the rest of the project — nothing to install.
"""
import html
import io
import json
import os
import re
import subprocess
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import store  # noqa: E402

IMG_DIR = os.path.join(ROOT, "assets", "img")
PORT = int(os.environ.get("HDIP_DASH_PORT", "4620"))

# ---------------------------------------------------------------------------
# How the 30 content keys map onto the pages an editor actually thinks about.
# Without this the panel is an alphabetical wall of variable names.
# ---------------------------------------------------------------------------
GROUPS = [
    ("Home page", "The home page, top to bottom", [
        ("content.HOME", "Section headings, leads and hero copy"),
        ("years.HERO_SLIDES", "Hero slideshow — which photos, in what order"),
        ("years.IMPACT", "Four years of results — the figures per year"),
        ("content.GOVERNORATES", "Governorate names (English)"),
        ("content.GOVERNORATES_AR", "Governorate names (Arabic)"),
    ]),
    ("About", "about.html", [
        ("content.ABOUT", "Vision, mission, objectives"),
        ("years.ABOUT_EXTRA", "Areas, approach, donor principles"),
    ]),
    ("Programme areas", "work.html and the five area pages", [
        ("content.AREAS", "The five areas — name, purpose, activities, photo"),
    ]),
    ("Projects", "projects.html and the four project pages", [
        ("content.PROJECTS", "Name, tagline, objectives, components, figures"),
        ("years.PHASES", "Results by year, per project"),
    ]),
    ("Reports", "reports.html and the four annual reports", [
        ("content.REPORT_2024", "The 2024 annual report"),
        ("years.REPORTS", "The 2022, 2023 and 2025 reports"),
        ("years.LIBRARIES", "Libraries narrative (2022)"),
        ("years.YEARS", "Which years exist, newest first"),
        ("content.IMPACT_2024", "2024 headline figures"),
    ]),
    ("News & stories", "news.html and the article pages", [
        ("content.NEWS", "Articles (2024)"),
        ("years.NEWS_2025", "Articles (2025)"),
    ]),
    ("Contact", "contact.html", [
        ("content.CONTACT", "Address, email, phone, lead text"),
        ("content.CONTACT_FIELDS", "Enquiry routes"),
    ]),
    ("Photography & credits", "credits.html", [
        ("years.CONTEXT_PHOTOS", "Captions and alt text for contextual photos"),
        ("years.HERO_PHOTOS", "Which photo heads each page"),
        ("content.SOURCES", "Source documents"),
        ("years.SOURCES_EXTRA", "Source documents (other years)"),
        ("content.GAPS", "Content still needed"),
        ("years.GAPS_REMAINING", "Content still needed (other years)"),
    ]),
    ("Site-wide", "Navigation, buttons, labels — every page", [
        ("content.UI", "Button and label text"),
        ("content.NAV", "Main navigation"),
        ("years.ENDINGS", "Closing call-to-action per page type"),
        ("years.SLIDESHOW_UI", "Slideshow control labels"),
        ("years.CLOSURES_NOTE", "Closures note"),
    ]),
]
LABELS = {k: (lbl, grp) for grp, _, items in GROUPS for k, lbl in items}


def manifest():
    with open(os.path.join(IMG_DIR, "manifest.json"), encoding="utf-8") as f:
        return json.load(f)


def is_image(value):
    return isinstance(value, str) and value in manifest()


def thumb(slug):
    m = manifest().get(slug)
    if not m:
        return ""
    w = m["widths"][0]
    ext = m.get("ext", "jpg")
    return f"/img/{slug}-{w}.{ext}"


def unused_paths():
    """Store paths that reach no page (tools/find_orphans.py --write).

    Marked in the panel rather than hidden: some are conditional rather than
    dead, and none of it is ours to delete. The point is only that nobody
    edits a field, publishes, and wonders why nothing changed.
    """
    p = os.path.join(ROOT, "data", "unused.json")
    if not os.path.isfile(p):
        return set()
    with open(p, encoding="utf-8") as f:
        return set(json.load(f).get("paths", []))


UNUSED = unused_paths()


def is_unused(path):
    """Orphans are recorded with the same full path the form fields use."""
    return path in UNUSED


# ---------------------------------------------------------------------------
# Addressing: a dotted/indexed path reaches any leaf, and is also the form
# field name, so saving is a straight walk rather than bespoke parsing.
# ---------------------------------------------------------------------------
TOKEN = re.compile(r"([^.\[\]]+)|\[(\d+)\]")


def parse_path(path):
    out = []
    for name, idx in TOKEN.findall(path):
        out.append(int(idx) if idx else name)
    return out


def get_at(obj, parts):
    for p in parts:
        obj = obj[p]
    return obj


def set_at(obj, parts, value):
    for p in parts[:-1]:
        obj = obj[p]
    last = parts[-1]
    old = obj[last]
    # Keep the leaf's type: a figure stored as a number must not become "12".
    if isinstance(old, bool):
        value = value in ("1", "true", "on", "True")
    elif isinstance(old, int) and not isinstance(old, bool):
        value = int(value) if str(value).strip() else 0
    elif isinstance(old, float):
        value = float(value) if str(value).strip() else 0.0
    elif old is None and value == "":
        value = None
    obj[last] = value


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def pretty(key):
    k = str(key).replace("_", " ").strip()
    return k[:1].upper() + k[1:]


LANG_NAME = {"en": "English", "ar": "العربية"}


def field(path, value, label=None):
    """One leaf. Image references get a picker; long text gets a textarea."""
    lid = esc(path)
    mark = ('<span class="dead" title="No page renders this field">not shown</span>'
            if is_unused(path) else "")
    lab = (f'<label for="{lid}">{esc(label or "")}{mark}</label>'
           if (label or mark) else "")
    if is_image(value):
        opts = "".join(
            f'<option value="{esc(s)}"{" selected" if s == value else ""}>{esc(s)}</option>'
            for s in sorted(manifest()))
        return (f'<div class="f f--img">{lab}'
                f'<div class="imgpick">'
                f'<img src="{thumb(value)}" alt="" loading="lazy">'
                f'<select id="{lid}" name="{lid}" data-img>{opts}</select>'
                f'</div></div>')
    text = "" if value is None else str(value)
    if len(text) > 85 or "\n" in text:
        rows = min(14, max(3, text.count("\n") + len(text) // 70 + 1))
        return (f'<div class="f">{lab}'
                f'<textarea id="{lid}" name="{lid}" rows="{rows}">{esc(text)}</textarea></div>')
    return (f'<div class="f">{lab}'
            f'<input id="{lid}" name="{lid}" type="text" value="{esc(text)}"></div>')


def render(path, value, label=None, depth=0):
    """Recursive editor. The data's own shape decides the controls."""
    if isinstance(value, dict):
        # A bilingual pair is the commonest shape — show the languages side by side.
        if set(value) == {"en", "ar"}:
            cols = "".join(
                f'<div class="lang" dir="{"rtl" if lg == "ar" else "ltr"}">'
                f'<h4>{LANG_NAME[lg]}</h4>{render(f"{path}.{lg}", value[lg], None, depth + 1)}'
                f'</div>' for lg in ("en", "ar"))
            inner = f'<div class="langs">{cols}</div>'
        else:
            inner = "".join(render(f"{path}.{k}", v, pretty(k), depth + 1)
                            for k, v in value.items())
        if label is None:
            return inner
        tag = "section" if depth < 2 else "div"
        return (f'<{tag} class="grp grp--{min(depth,3)}">'
                f'<h3>{esc(label)}</h3>{inner}</{tag}>')

    if isinstance(value, list):
        if not value:
            return f'<div class="f"><label>{esc(label or "")}</label><em>empty</em></div>'
        # A list of image slugs is the slideshow: order matters, so make it movable.
        if all(is_image(v) for v in value):
            items = "".join(
                f'<li draggable="true" data-row>'
                f'<span class="handle" title="Drag to reorder">⋮⋮</span>'
                f'{render(f"{path}[{i}]", v, None, depth + 1)}</li>'
                for i, v in enumerate(value))
            return (f'<div class="grp grp--list"><h3>{esc(label or "")}</h3>'
                    f'<ol class="slides" data-sortable>{items}</ol>'
                    f'<p class="hint">Drag to reorder. The order here is the order on the page.</p>'
                    f'</div>')
        items = "".join(
            f'<li><span class="n">{i + 1}</span>'
            f'<div class="row">{render(f"{path}[{i}]", v, None, depth + 1)}</div></li>'
            for i, v in enumerate(value))
        head = f'<h3>{esc(label)}</h3>' if label else ""
        return f'<div class="grp grp--list">{head}<ol class="rows">{items}</ol></div>'

    return field(path, value, label)


CSS = """
:root{--ink:#161A1F;--soft:#4A535E;--mute:#667080;--line:#E6E9ED;--bg:#F7F8FA;
--card:#fff;--brand:#0E49A3;--brand-dk:#0B3A82;--ok:#1C7A4A;--warn:#9A5B00;--r:12px}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--brand)}
header.top{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.92);
backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top .in{max-width:1180px;margin:0 auto;padding:12px 22px;display:flex;align-items:center;gap:16px}
.brand{font-weight:700;letter-spacing:-.02em;color:var(--brand);text-decoration:none;font-size:1.1rem}
.top nav{display:flex;gap:4px;margin-inline-start:auto;align-items:center}
.wrap{max-width:1180px;margin:0 auto;padding:26px 22px 90px}
.btn{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);
background:#fff;color:var(--ink);padding:8px 15px;border-radius:999px;cursor:pointer;
font:inherit;font-weight:600;font-size:.88rem;text-decoration:none}
.btn:hover{border-color:var(--mute)}
.btn--p{background:var(--brand);border-color:var(--brand);color:#fff}
.btn--p:hover{background:var(--brand-dk);border-color:var(--brand-dk)}
h1{font-size:1.6rem;letter-spacing:-.02em;margin:0 0 6px}
.sub{color:var(--mute);margin:0 0 26px}
.groups{display:grid;gap:18px}
.gcard{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:18px 20px}
.gcard h2{font-size:1rem;margin:0 0 2px}
.gcard p.where{color:var(--mute);font-size:.84rem;margin:0 0 14px}
.links{display:grid;gap:8px}
.links a{display:flex;justify-content:space-between;gap:14px;align-items:baseline;
padding:10px 13px;border:1px solid var(--line);border-radius:9px;text-decoration:none;color:inherit}
.links a:hover{border-color:var(--brand);background:#F5F8FD}
.links b{font-weight:600;font-size:.92rem}
.links span{color:var(--mute);font-size:.82rem;text-align:end}
form.edit{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:4px 22px 22px}
section.grp{border-top:1px solid var(--line);padding:18px 0 4px;margin-top:10px}
section.grp:first-of-type{border-top:0}
.grp--1,.grp--2,.grp--3{border:0;padding:10px 0 0;margin:0}
.grp h3{font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);
margin:0 0 10px;font-weight:700}
.grp--2 h3,.grp--3 h3{text-transform:none;letter-spacing:0;font-size:.9rem;color:var(--soft)}
.langs{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:860px){.langs{grid-template-columns:1fr}}
.lang h4{margin:0 0 8px;font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:var(--brand)}
.lang[dir=rtl] h4{letter-spacing:0;text-transform:none;font-size:.86rem}
.f{margin:0 0 12px}
.f label{display:block;font-size:.8rem;color:var(--soft);margin:0 0 4px;font-weight:600}
input[type=text],textarea,select{width:100%;padding:9px 11px;border:1px solid var(--line);
border-radius:8px;font:inherit;background:#fff;color:var(--ink)}
input:focus,textarea:focus,select:focus{outline:2px solid var(--brand);outline-offset:1px;border-color:transparent}
textarea{resize:vertical;line-height:1.5}
[dir=rtl] input,[dir=rtl] textarea{direction:rtl;text-align:right}
ol.rows,ol.slides{list-style:none;margin:0;padding:0;display:grid;gap:12px}
ol.rows>li{display:grid;grid-template-columns:28px 1fr;gap:12px;
border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:#FCFDFE}
ol.rows>li .n{color:var(--mute);font-size:.78rem;font-weight:700;padding-top:3px}
ol.slides>li{display:flex;align-items:center;gap:10px;border:1px solid var(--line);
border-radius:10px;padding:8px 10px;background:#FCFDFE}
ol.slides>li.drag{opacity:.4}
.handle{cursor:grab;color:var(--mute);user-select:none;font-size:1rem}
.imgpick{display:flex;align-items:center;gap:10px}
.imgpick img{width:62px;height:44px;object-fit:cover;border-radius:6px;border:1px solid var(--line);background:#fff;flex:none}
.f--img{flex:1;margin:0}
.hint{color:var(--mute);font-size:.8rem;margin:8px 0 0}
.dead{display:inline-block;margin-inline-start:8px;padding:1px 7px;border-radius:999px;
background:#FFF4E5;border:1px solid #F0D9B5;color:var(--warn);font-size:.68rem;
font-weight:700;letter-spacing:.02em;vertical-align:1px}
.bar{position:fixed;inset-inline:0;bottom:0;background:rgba(255,255,255,.95);
backdrop-filter:blur(8px);border-top:1px solid var(--line);padding:11px 22px;z-index:20}
.bar .in{max-width:1180px;margin:0 auto;display:flex;align-items:center;gap:12px}
.bar .state{color:var(--mute);font-size:.85rem;margin-inline-start:auto}
.flash{padding:11px 15px;border-radius:9px;margin:0 0 18px;font-size:.9rem;border:1px solid}
.flash--ok{background:#EAF7F0;border-color:#BFE3CF;color:var(--ok)}
.flash--err{background:#FDF0EE;border-color:#F3C9C2;color:#9B2C1C;white-space:pre-wrap;
font-family:ui-monospace,Menlo,monospace;font-size:.82rem}
.imgs{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:14px}
.imgs figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.imgs img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block;background:#EEF1F4}
.imgs figcaption{padding:8px 10px;font-size:.78rem}
.imgs code{font-size:.74rem;color:var(--mute);word-break:break-all}
.up{background:var(--card);border:1px dashed var(--line);border-radius:var(--r);
padding:18px 20px;margin:0 0 20px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
"""

JS = """
// Mark the form dirty so Publish can warn about unsaved edits.
let dirty=false;
const form=document.querySelector('form.edit');
if(form){
  form.addEventListener('input',()=>{dirty=true;setState('Unsaved changes');});
  window.addEventListener('beforeunload',e=>{if(dirty){e.preventDefault();e.returnValue='';}});
  form.addEventListener('submit',()=>{dirty=false;});
  // Swap the thumbnail when a different photo is picked.
  form.querySelectorAll('select[data-img]').forEach(s=>{
    s.addEventListener('change',()=>{
      const img=s.closest('.imgpick').querySelector('img');
      if(img) img.src=window.__thumbs[s.value]||'';
    });
  });
}
function setState(t){const el=document.querySelector('.bar .state');if(el)el.textContent=t;}

// Slideshow reordering. The inputs keep their own values; only the rows move,
// and the order is read off the DOM on submit.
document.querySelectorAll('[data-sortable]').forEach(list=>{
  let src=null;
  list.addEventListener('dragstart',e=>{
    src=e.target.closest('[data-row]');if(!src)return;
    src.classList.add('drag');e.dataTransfer.effectAllowed='move';
  });
  list.addEventListener('dragend',()=>{if(src)src.classList.remove('drag');src=null;renumber(list);});
  list.addEventListener('dragover',e=>{
    e.preventDefault();
    const over=e.target.closest('[data-row]');
    if(!over||over===src)return;
    const r=over.getBoundingClientRect();
    list.insertBefore(src,(e.clientY-r.top)/r.height>0.5?over.nextSibling:over);
  });
});
// After a move the field names must match the new positions, or the save
// would write the old order back.
function renumber(list){
  [...list.querySelectorAll('[data-row]')].forEach((li,i)=>{
    li.querySelectorAll('[name]').forEach(el=>{
      el.name=el.name.replace(/\\[\\d+\\]$/,'['+i+']');
      el.id=el.name;
    });
  });
  dirty=true;setState('Unsaved changes');
}
"""


def page(title, body, flash=None, bar=None):
    thumbs = json.dumps({s: thumb(s) for s in manifest()})
    note = ""
    if flash:
        kind, msg = flash
        note = f'<div class="flash flash--{kind}">{esc(msg)}</div>'
    barhtml = f'<div class="bar"><div class="in">{bar}</div></div>' if bar else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} — HDIP control panel</title><style>{CSS}</style></head>
<body>
<header class="top"><div class="in">
  <a class="brand" href="/">hdip control panel</a>
  <nav>
    <a class="btn" href="/">Content</a>
    <a class="btn" href="/images">Photos</a>
    <a class="btn" href="http://127.0.0.1:4610/" target="_blank" rel="noopener">View site</a>
  </nav>
</div></header>
<main class="wrap">{note}{body}</main>
{barhtml}
<script>window.__thumbs={thumbs};</script>
<script>{JS}</script>
</body></html>"""


def view_index(flash=None):
    cards = []
    for name, where, items in GROUPS:
        links = "".join(
            f'<a href="/edit?k={urllib.parse.quote(k)}">'
            f'<b>{esc(lbl)}</b><span>{esc(k.split(".")[1])}</span></a>'
            for k, lbl in items)
        cards.append(f'<div class="gcard"><h2>{esc(name)}</h2>'
                     f'<p class="where">{esc(where)}</p>'
                     f'<div class="links">{links}</div></div>')
    body = ("<h1>Content</h1>"
            "<p class=\"sub\">Every field on the site. Edit, save, then publish "
            "to rewrite the pages.</p>"
            f'<div class="groups">{"".join(cards)}</div>')
    bar = ('<form method="post" action="/publish" style="display:contents">'
           '<button class="btn btn--p" type="submit">Publish to the site</button></form>'
           '<span class="state">Publishing rebuilds all 58 pages</span>')
    return page("Content", body, flash, bar)


def view_edit(key, flash=None):
    if key not in LABELS:
        return None
    label, group = LABELS[key]
    data = store.load()
    value = get_at(data, parse_path(key))
    body = (f'<p class="sub" style="margin:0 0 4px"><a href="/">← Content</a> · {esc(group)}</p>'
            f'<h1>{esc(label)}</h1>'
            f'<p class="sub">{esc(key)}</p>'
            f'<form class="edit" method="post" action="/save">'
            f'<input type="hidden" name="__key" value="{esc(key)}">'
            f'{render(key, value, None)}'
            f'</form>')
    bar = ('<button class="btn btn--p" form="" '
           'onclick="document.querySelector(\'form.edit\').requestSubmit();return false;">'
           'Save</button>'
           '<a class="btn" href="/">Cancel</a>'
           '<span class="state">Saved changes go live when you publish</span>')
    return page(label, body, flash, bar)


def view_images(flash=None):
    m = manifest()
    figs = []
    for slug in sorted(m):
        e = m[slug]
        ext = e.get("ext", "jpg")
        figs.append(
            f'<figure><img src="{thumb(slug)}" alt="" loading="lazy">'
            f'<figcaption><b>{esc(slug)}</b><br>'
            f'<code>{esc("/".join(str(w) for w in e["widths"]))} · {esc(ext)}</code>'
            f'</figcaption></figure>')
    body = ("<h1>Photos</h1>"
            '<p class="sub">Every photo on the site. Uploading adds the sizes the '
            'pages need; pick a photo for a page from the content screens.</p>'
            '<form class="up" method="post" action="/upload" enctype="multipart/form-data">'
            '<input type="file" name="file" accept="image/*" required>'
            '<input type="text" name="slug" placeholder="short-name" required '
            'pattern="[a-z0-9-]+" title="lower-case letters, numbers and hyphens">'
            '<button class="btn btn--p" type="submit">Add photo</button>'
            '</form>'
            f'<div class="imgs">{"".join(figs)}</div>')
    return page("Photos", body, flash)


# ---------------------------------------------------------------------------
# Photo ingest: the pages use srcset, so an upload has to become the same
# tiers everything else has. Never upscales — a small source simply gets
# fewer tiers, which is what build.py's manifest-driven srcset expects.
# ---------------------------------------------------------------------------
TIERS = (320, 800, 1600, 2400)


def add_image(slug, raw, filename):
    try:
        from PIL import Image
    except ImportError:
        return ("Pillow is not installed, so photos cannot be resized here.\n"
                "Install it once with:  python3 -m pip install Pillow")
    im = Image.open(io.BytesIO(raw))
    keep_alpha = im.mode in ("RGBA", "LA") and im.getchannel("A").getextrema()[0] < 255
    im = im.convert("RGBA" if keep_alpha else "RGB")
    w, h = im.size
    widths = [t for t in TIERS if t <= w] or [w]
    ext = "webp" if keep_alpha else "jpg"
    for t in widths:
        out = im.resize((t, round(h * t / w)), Image.LANCZOS)
        p = os.path.join(IMG_DIR, f"{slug}-{t}.{ext}")
        if ext == "webp":
            out.save(p, "WEBP", quality=86, method=6)
        else:
            out.save(p, "JPEG", quality=86, optimize=True, progressive=True)
    m = manifest()
    entry = {"widths": widths, "w": widths[0],
             "h": round(h * widths[0] / w), "max": widths[-1]}
    if ext != "jpg":
        entry["ext"] = ext
    m[slug] = entry
    with open(os.path.join(IMG_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(m, f, indent=1, sort_keys=True)
    return None


def publish():
    r = subprocess.run([sys.executable, "build.py"], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        return ("err", (r.stderr or r.stdout).strip()[-1800:])
    n = len([f for f in os.listdir(ROOT) if f.endswith(".html")])
    n += len([f for f in os.listdir(os.path.join(ROOT, "ar")) if f.endswith(".html")])
    return ("ok", f"Published. {n} pages rewritten.")



def parse_multipart(headers, rfile):
    """Minimal multipart/form-data reader.

    cgi.FieldStorage was removed in Python 3.13 and email is the documented
    replacement. Returns {name: value}, where a file part's value is
    (filename, bytes) and every other part is a string.
    """
    import email.parser
    import email.policy

    length = int(headers.get("Content-Length", "0"))
    raw = (b"Content-Type: " + headers["Content-Type"].encode("utf-8")
           + b"\r\nMIME-Version: 1.0\r\n\r\n" + rfile.read(length))
    msg = email.parser.BytesParser(policy=email.policy.HTTP).parsebytes(raw)
    out = {}
    for part in msg.iter_parts():
        name = part.get_param("name", header="content-disposition")
        if not name:
            continue
        fname = part.get_filename()
        payload = part.get_payload(decode=True) or b""
        out[name] = (fname, payload) if fname else payload.decode("utf-8", "replace")
    return out


class Handler(BaseHTTPRequestHandler):
    server_version = "HDIPPanel/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))

    # -- helpers ---------------------------------------------------------
    def send_html(self, body, code=200):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def redirect(self, to):
        self.send_response(303)
        self.send_header("Location", to)
        self.end_headers()

    def serve_file(self, path, ctype):
        if not os.path.isfile(path):
            self.send_error(404)
            return
        with open(path, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    # -- routes ----------------------------------------------------------
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(u.query)
        flash = None
        if "ok" in q:
            flash = ("ok", q["ok"][0])
        elif "err" in q:
            flash = ("err", q["err"][0])

        if u.path == "/":
            self.send_html(view_index(flash))
        elif u.path == "/edit":
            v = view_edit(q.get("k", [""])[0], flash)
            if v:
                self.send_html(v)
            else:
                self.send_error(404, "No such content key")
        elif u.path == "/images":
            self.send_html(view_images(flash))
        elif u.path.startswith("/img/"):
            name = os.path.basename(urllib.parse.unquote(u.path[5:]))
            ext = name.rsplit(".", 1)[-1].lower()
            ctype = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
                     "webp": "image/webp", "svg": "image/svg+xml"}.get(
                         ext, "application/octet-stream")
            self.serve_file(os.path.join(IMG_DIR, name), ctype)
        else:
            self.send_error(404)

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)

        if u.path == "/publish":
            kind, msg = publish()
            self.redirect(f"/?{kind}={urllib.parse.quote(msg)}")
            return

        if u.path == "/upload":
            fields = parse_multipart(self.headers, self.rfile)
            slug = str(fields.get("slug", "")).strip().lower()
            item = fields.get("file")
            if not re.fullmatch(r"[a-z0-9-]+", slug or ""):
                self.redirect("/images?err=" + urllib.parse.quote(
                    "Use lower-case letters, numbers and hyphens for the short name."))
                return
            if not isinstance(item, tuple) or not item[1]:
                self.redirect("/images?err=" + urllib.parse.quote("No file received."))
                return
            err = add_image(slug, item[1], item[0] or "")
            if err:
                self.redirect("/images?err=" + urllib.parse.quote(err))
            else:
                self.redirect("/images?ok=" + urllib.parse.quote(
                    f"Added “{slug}”. Pick it on a content screen, then publish."))
            return

        if u.path == "/save":
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8")
            form = urllib.parse.parse_qs(body, keep_blank_values=True)
            key = form.pop("__key", [""])[0]
            if key not in LABELS:
                self.send_error(400, "Unknown content key")
                return
            data = store.load()
            allowed = parse_path(key)
            count = 0
            for path, vals in form.items():
                parts = parse_path(path)
                # Only ever write inside the section being edited.
                if parts[:len(allowed)] != allowed:
                    continue
                try:
                    set_at(data, parts, vals[0])
                    count += 1
                except (KeyError, IndexError, TypeError):
                    continue
            store.save(data)
            self.redirect(f"/edit?k={urllib.parse.quote(key)}&ok="
                          + urllib.parse.quote(
                              f"Saved {count} fields. Publish to put them live."))
            return

        self.send_error(404)


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"HDIP control panel  →  http://127.0.0.1:{PORT}")
    print(f"store: data/site.json")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
