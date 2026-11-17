#!/usr/bin/env python3
"""HDIP control panel.

Edits data/site.json — every piece of copy, every figure, every photo
assignment and the slideshow order — then regenerates the static site.

The site stays static: this runs locally (or behind your own auth), you edit,
you press Publish, and build.py rewrites the 58 pages. Nothing dynamic is
exposed to the public site.

    python3 tools/dashboard.py          # http://127.0.0.1:4610

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
PORT = int(os.environ.get("HDIP_PORT", "4610"))
HOST = os.environ.get("HDIP_HOST", "127.0.0.1")

# The panel is mounted inside the site's own origin, so one address serves
# both: / is the site, /admin is the control panel. When the site is deployed
# as static files, /admin is simply not among them and cannot ship by accident.
PREFIX = "/admin"
AUTH_FILE = os.path.join(ROOT, "data", "admin.local.json")

# ---------------------------------------------------------------------------
# One screen per part of the site, not one per variable.
# An editor thinks "I am editing the Reports page", not "I am editing
# years.REPORTS and content.REPORT_2024 and years.YEARS" — so each section
# below is a single page holding everything that part of the site needs.
# ---------------------------------------------------------------------------
SECTIONS = [
    ("home", "Home page", "index.html — top to bottom", [
        ("content.HOME", "Section headings, leads and hero copy"),
        ("years.HERO_SLIDES", "Hero slideshow — which photos, in what order"),
        ("years.IMPACT", "Four years of results — the figures per year"),
        ("content.GOVERNORATES", "Governorate names (English)"),
        ("content.GOVERNORATES_AR", "Governorate names (Arabic)"),
    ]),
    ("about", "About", "about.html", [
        ("content.ABOUT", "Vision, mission, objectives"),
        ("years.ABOUT_EXTRA", "Areas, approach, donor principles"),
    ]),
    ("work", "Our work", "work.html and the five programme area pages", [
        ("content.AREAS", "The areas — name, purpose, activities, photo"),
    ]),
    ("projects", "Projects", "projects.html and a page per project", [
        ("content.PROJECTS", "Name, tagline, objectives, components, figures"),
        ("years.PHASES", "Results by year, per project"),
    ]),
    ("news", "Articles & news", "news.html and a page per article", [
        ("content.NEWS", "Articles (2024)"),
        ("years.NEWS_2025", "Articles (2025)"),
    ]),
    ("reports", "Reports", "reports.html and a page per annual report", [
        ("years.REPORTS", "Annual reports"),
        ("content.REPORT_2024", "The 2024 annual report"),
        ("years.LIBRARIES", "Libraries narrative (2022)"),
        ("years.YEARS", "Which years exist, newest first"),
        ("content.IMPACT_2024", "2024 headline figures"),
    ]),
    ("contact", "Contact", "contact.html", [
        ("content.CONTACT", "Address, email, phone, lead text"),
        ("content.CONTACT_FIELDS", "Enquiry routes"),
    ]),
    ("credits", "Photography & credits", "credits.html", [
        ("years.CONTEXT_PHOTOS", "Captions and alt text for contextual photos"),
        ("years.HERO_PHOTOS", "Which photo heads each page"),
        ("content.SOURCES", "Source documents"),
        ("years.SOURCES_EXTRA", "Source documents (other years)"),
        ("content.GAPS", "Content still needed"),
        ("years.GAPS_REMAINING", "Content still needed (other years)"),
    ]),
    ("site", "Site-wide", "Navigation, buttons and labels — every page", [
        ("content.UI", "Button and label text"),
        ("content.NAV", "Main navigation"),
        ("years.ENDINGS", "Closing call-to-action per page type"),
        ("years.SLIDESHOW_UI", "Slideshow control labels"),
        ("years.CLOSURES_NOTE", "Closures note"),
    ]),
]
SECTION = {sid: (name, where, items) for sid, name, where, items in SECTIONS}
LABELS = {k: (lbl, name)
          for _, name, _, items in SECTIONS for k, lbl in items}
SECTION_OF = {k: sid for sid, _, _, items in SECTIONS for k, _ in items}


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
    return f"{PREFIX}/img/{slug}-{w}.{ext}"


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

# ---------------------------------------------------------------------------
# Adding and removing list items
# Articles are the obvious case, but projects, areas and the year lists are
# the same shape. A new item is cloned from an existing one so every key the
# templates read is present — a missing key is a build failure, not a blank.
# ---------------------------------------------------------------------------
# Lists an editor may add to or delete from, and what one item is called.
LISTS = {
    "content.NEWS": "article",
    "years.NEWS_2025": "article",
    "content.PROJECTS": "project",
    "content.AREAS": "programme area",
}


def blank_like(value):
    """Same shape, emptied. Keeps keys so templates never hit a KeyError."""
    if isinstance(value, dict):
        return {k: blank_like(v) for k, v in value.items()}
    if isinstance(value, list):
        return [blank_like(v) for v in value]
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return 0
    if value is None:
        return None
    return ""


def slug_exists(slug):
    data = store.load()
    for key in LISTS:
        for item in get_at(data, parse_path(key)):
            if isinstance(item, dict) and item.get("slug") == slug:
                return True
    return False


def slugify(text):
    """A slug is a filename and a URL — keep it to what both can carry."""
    out = re.sub(r"[^a-z0-9]+", "-", str(text).strip().lower()).strip("-")
    return out


def unique_slug(base="new-article"):
    base = slugify(base) or "new-item"
    slug, n = base, 2
    while slug_exists(slug):
        slug, n = f"{base}-{n}", n + 1
    return slug


ICON_NAMES = None


def icon_names():
    """The icons build.py can actually draw.

    An unknown name is not an error there — icon() falls back to "doc" — so a
    free-text field would silently draw the wrong glyph. Read from the source
    rather than copied, so the picker cannot drift from the set.
    """
    global ICON_NAMES
    if ICON_NAMES is None:
        with open(os.path.join(ROOT, "build.py"), encoding="utf-8") as f:
            m = re.search(r"^ICONS = \{(.*?)^\}", f.read(), re.S | re.M)
        ICON_NAMES = re.findall(r'"([a-z-]+)":\s*_i', m.group(1)) if m else []
    return ICON_NAMES


# Fields whose value has to be one of a known set, or the generated page
# would link somewhere that does not exist.
def choices_for(path, value):
    leaf = path.rsplit(".", 1)[-1]
    data = store.load()
    if leaf == "area":
        return [("", "— none —")] + [(a["slug"], a["en"]["name"])
                                     for a in data["content"]["AREAS"]]
    if leaf == "project":
        return [("", "— none —")] + [(p["slug"], p["en"]["name"])
                                     for p in data["content"]["PROJECTS"]]
    if leaf == "icon":
        return [(n, n) for n in icon_names()]
    if leaf == "status":
        # Indexed straight into UI by the templates, so it cannot be free text.
        return [(k, data["content"]["UI"]["en"].get(k, k))
                for k in ("ongoing", "completed")]
    return None


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


NICE = {
    "recs": "Recommendations", "recs_title": "Recommendations heading",
    "me": "Monitoring and evaluation", "me_title": "Monitoring heading",
    "glance": "At a glance", "table": "Data table",
    "table_head": "Data table — column headings",
    "what": "What we do", "what_title": "“What we do” heading",
    "who": "Who we are", "who_title": "“Who we are” heading",
    "ui": "Labels", "pwd": "People with disabilities",
    "num": "Figure", "tag": "Label", "lead": "Lead paragraph",
    "alt": "Alt text (for screen readers)",
}

# Dicts keyed by the slug of something named elsewhere. Showing the name is
# the difference between "Youth-leadership" and "Young Leadership in
# Universities" on a collapsed row.
SLUG_KEYED = {"years.PHASES": "content.PROJECTS"}


def pretty(key):
    k = str(key)
    if k.lower() in NICE:
        return NICE[k.lower()]
    k = k.replace("_", " ").strip()
    return k[:1].upper() + k[1:]


def key_label(path, key):
    src = SLUG_KEYED.get(path)
    if src:
        for item in get_at(store.load(), parse_path(src)):
            if isinstance(item, dict) and item.get("slug") == key:
                return item.get("en", {}).get("name") or pretty(key)
    return pretty(key)


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

    # Values that must be one of a known set — a free-text area or project
    # would generate a link to a page that does not exist.
    choices = choices_for(path, value)
    if choices is not None:
        opts = "".join(
            f'<option value="{esc(v)}"{" selected" if v == (value or "") else ""}>'
            f'{esc(t)}</option>' for v, t in choices)
        return (f'<div class="f f--s">{lab}'
                f'<select id="{lid}" name="{lid}">{opts}</select></div>')

    text = "" if value is None else str(value)
    if len(text) > 85 or "\n" in text:
        # Shallow by default: a textarea tall enough for every paragraph makes
        # a screen unreadable, and it drags to any height.
        rows = min(9, max(2, text.count("\n") + len(text) // 95 + 1))
        return (f'<div class="f f--t">{lab}'
                f'<textarea id="{lid}" name="{lid}" rows="{rows}">{esc(text)}</textarea></div>')
    return (f'<div class="f f--s">{lab}'
            f'<input id="{lid}" name="{lid}" type="text" value="{esc(text)}"></div>')


# A record with this many fields inside it is worth collapsing: a screen then
# opens as a list of what is on it, not a wall of inputs. The fields are still
# in the form while collapsed, so Save writes them either way.
FOLD_MIN = 10
TITLE_KEYS = ("title", "name", "headline", "year")


def record_name(value):
    """The English title of a record, for its collapsed summary line."""
    if not isinstance(value, dict):
        return ""
    en = value.get("en") if isinstance(value.get("en"), dict) else value
    for k in TITLE_KEYS:
        v = en.get(k) if isinstance(en, dict) else None
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


def record_chips(value):
    """The short structural fields, shown without opening the record."""
    if not isinstance(value, dict):
        return []
    out = []
    for k in ("slug", "status", "area", "years", "date"):
        v = value.get(k)
        if isinstance(v, str) and v.strip():
            out.append(v.strip())
    return out


def record_thumb(value):
    if isinstance(value, dict) and is_image(value.get("photo")):
        return thumb(value["photo"])
    return ""


def fold(title, inner, chips=(), meta="", image="", fid=""):
    img = (f'<img class="fold__img" src="{esc(image)}" alt="" loading="lazy">'
           if image else "")
    cs = "".join(f'<span class="fold__c">{esc(c)}</span>' for c in chips if c)
    return (f'<details class="fold" data-fold="{esc(fid)}">'
            f'<summary>{img}<span class="fold__t">{esc(title)}</span>{cs}'
            f'<span class="fold__n">{esc(meta)}</span></summary>'
            f'<div class="fold__b">{inner}</div></details>')


def fields_box(inner):
    """Short inputs flow side by side; prose and sub-groups take the width."""
    return f'<div class="fields">{inner}</div>'


def is_leaf(v):
    return not isinstance(v, (dict, list))


def render(path, value, label=None, depth=0):
    """Recursive editor. The data's own shape decides the controls."""
    if isinstance(value, dict):
        # A bilingual pair is the commonest shape — show the languages side by
        # side. A record that carries its own fields as well (a project has a
        # slug, an area, a photo) shows those first and the two languages
        # beneath, rather than burying one language under the other.
        langs = ""
        if {"en", "ar"} <= set(value):
            cols = "".join(
                f'<div class="lang" dir="{"rtl" if lg == "ar" else "ltr"}">'
                f'<h4>{LANG_NAME[lg]}</h4>{render(f"{path}.{lg}", value[lg], None, depth + 1)}'
                f'</div>' for lg in ("en", "ar"))
            langs = f'<div class="langs">{cols}</div>'
        if set(value) == {"en", "ar"}:
            inner = langs
        else:
            parts = []
            for k, v in value.items():
                if k in ("en", "ar") and langs:
                    continue
                sub = f"{path}.{k}"
                n = count_fields(v)
                name = key_label(path, k)
                # A list is a repeated structure with its own heading, so it
                # folds sooner than a dict of labelled fields does.
                if isinstance(v, (dict, list)) and n >= (6 if isinstance(v, list)
                                                         else FOLD_MIN):
                    extra = record_name(v)
                    chips = [extra] if extra and extra != name else []
                    parts.append(fold(name,
                                      render(sub, v, None, depth + 1),
                                      chips=chips, meta=f"{n} fields",
                                      image=record_thumb(v), fid=sub))
                else:
                    parts.append(render(sub, v, name, depth + 1))
            inner = fields_box("".join(parts)) + langs
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

        head = f'<h3>{esc(label)}</h3>' if label else ""

        # Bullet lists and table rows are not records: one line each, no card.
        if all(is_leaf(v) for v in value):
            items = "".join(
                f'<li><span class="n">{i + 1}</span>'
                f'{field(f"{path}[{i}]", v, None)}</li>'
                for i, v in enumerate(value))
            return (f'<div class="grp grp--list">{head}'
                    f'<ol class="flat">{items}</ol></div>')
        if all(isinstance(v, list) and all(is_leaf(x) for x in v) for v in value):
            items = ""
            for i, v in enumerate(value):
                cells = "".join(field(f"{path}[{i}][{j}]", x, None)
                                for j, x in enumerate(v))
                items += (f'<li><span class="n">{i + 1}</span>'
                          f'<div class="cells" style="--n:{len(v)}">{cells}</div></li>')
            return (f'<div class="grp grp--list">{head}'
                    f'<ol class="flat flat--grid">{items}</ol></div>')

        noun = LISTS.get(path)

        def controls(i, item):
            if not noun:
                return ""
            name = record_name(item) or (item.get("slug", "")
                                         if isinstance(item, dict) else "")
            # A button can only submit its own name and value, and a section
            # may hold more than one list, so the value carries both which
            # list and which row.
            return (f'<p class="delrow"><button class="btn btn--del" type="submit" '
                    f'formaction="{{PREFIX}}/delitem" formmethod="post" '
                    f'formnovalidate name="item" value="{esc(path)}|{i}" '
                    f'data-confirm="Delete the {esc(noun)} &quot;{esc(name)}&quot;? '
                    f'This cannot be undone.">Delete this {esc(noun)}</button></p>')

        # One record per row, collapsed — opening one is how you edit it. A
        # list of small records stays open: a fold would hide less than it
        # costs to open.
        foldable = max(count_fields(v) for v in value) >= FOLD_MIN
        items = ""
        for i, v in enumerate(value):
            body = render(f"{path}[{i}]", v, None, depth + 1) + controls(i, v)
            if not foldable:
                items += (f'<li class="rec"><span class="n">{i + 1}</span>'
                          f'<div class="recb">{body}</div></li>')
                continue
            items += ("<li>" + fold(f"{i + 1}. " + (record_name(v) or "Untitled"),
                                    body, chips=record_chips(v),
                                    meta=f"{count_fields(v)} fields",
                                    image=record_thumb(v),
                                    fid=f"{path}[{i}]") + "</li>")
        add = ""
        if noun:
            add = (f'<p class="addrow"><button class="btn btn--add" type="submit" '
                   f'formaction="{{PREFIX}}/additem" formmethod="post" formnovalidate '
                   f'name="listkey" value="{esc(path)}">'
                   f'Add {esc(noun)}</button>'
                   f'<span class="hint">Saves what is on screen first, then adds '
                   f'a blank {esc(noun)} at the end.</span></p>')
        return (f'<div class="grp grp--list">{head}'
                f'<ol class="recs">{items}</ol>{add}</div>')

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
input[type=text],input[type=password],textarea,select{width:100%;padding:9px 11px;border:1px solid var(--line);
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
.scards{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:16px}
.scard{display:block;background:var(--card);border:1px solid var(--line);border-radius:var(--r);
padding:18px 20px;text-decoration:none;color:inherit;transition:border-color .15s,box-shadow .15s}
.scard:hover{border-color:var(--brand);box-shadow:0 6px 22px -14px rgba(14,35,68,.45)}
.scard__head{display:flex;align-items:baseline;gap:10px}
.scard h2{font-size:1.02rem;margin:0}
.scard .count{margin-inline-start:auto;color:var(--mute);font-size:.76rem;white-space:nowrap}
.scard .where{color:var(--mute);font-size:.84rem;margin:3px 0 12px}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{font-size:.72rem;color:var(--soft);background:var(--bg);border:1px solid var(--line);
border-radius:999px;padding:2px 9px}
.jump{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}
.jump a{font-size:.8rem;text-decoration:none;color:var(--soft);background:var(--card);
border:1px solid var(--line);border-radius:999px;padding:5px 12px}
.jump a:hover{border-color:var(--brand);color:var(--brand)}
.block{background:var(--card);border:1px solid var(--line);border-radius:var(--r);
padding:6px 22px 20px;margin:0 0 18px;scroll-margin-top:72px}
.block__head{display:flex;align-items:baseline;gap:10px;border-bottom:1px solid var(--line);
padding:14px 0 12px;margin:0 0 14px}
.block__head h2{font-size:1rem;margin:0}
.block__head code{margin-inline-start:auto;font-size:.72rem;color:var(--mute)}
form.edit{background:none;border:0;padding:0}
.addbox{background:var(--card);border:1px dashed var(--line);border-radius:var(--r);
padding:16px 20px;margin:0 0 18px}
.addbox b{font-size:.94rem}
.addbox .hint{margin:4px 0 10px}
.addbox__row{display:flex;gap:10px;align-items:center}
.addbox__row input{max-width:150px}
.btn--add{border-color:var(--brand);color:var(--brand)}
.btn--add:hover{background:#F5F8FD}
.btn--del{border-color:#F0C9C2;color:#9B2C1C;margin-top:10px;font-size:.82rem;padding:6px 13px}
.btn--del:hover{background:#FDF0EE;border-color:#D88B7C}
.addrow{display:flex;align-items:center;gap:12px;margin:16px 0 0}
.addrow .hint{margin:0}
.btn--quiet{color:var(--mute)}
.btn--quiet:hover{color:var(--ink)}
.login{max-width:380px;margin:12vh auto 0;background:var(--card);border:1px solid var(--line);
border-radius:var(--r);padding:28px 26px}
.login h1{font-size:1.25rem;margin:0 0 4px}
.login .sub{margin:0 0 22px;font-size:.9rem}
.login .btn{width:100%;justify-content:center;margin-top:6px}
.login input{padding:10px 12px}
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

/* --- compact layout -------------------------------------------------------
   Records are collapsed (details/summary) and short inputs flow side by side,
   so a screen opens as a list of what is on it rather than a wall of fields.
   The inputs exist in the form whether a record is open or shut, so Save and
   Publish are unaffected by what happens to be expanded. */
.block{padding:4px 18px 16px;margin:0 0 14px}
.block__head{padding:13px 0 11px;margin:0 0 13px}
section.grp{padding:14px 0 2px;margin-top:6px}
.grp h3{margin:0 0 7px}
.langs{gap:14px}
.lang h4{margin:0 0 6px}
.f{margin:0}
.f label{margin:0 0 3px;font-size:.78rem}
.fields{display:grid;grid-template-columns:repeat(auto-fill,minmax(196px,1fr));
gap:9px 12px;align-items:start}
.fields>.f--t,.fields>.grp,.fields>.fold,.fields>.langs,
.fields>section{grid-column:1/-1}
.fields>.f--img{grid-column:span 2}
@media(max-width:700px){.fields>.f--img{grid-column:1/-1}}
.fields input[type=text],.fields select,.fields textarea,
.flat input[type=text],.flat select,.flat textarea{padding:7px 10px;border-radius:7px}
.fold{border:1px solid var(--line);border-radius:10px;background:#FCFDFE}
.fold>summary{display:flex;align-items:center;gap:9px;padding:9px 12px;cursor:pointer;
list-style:none;font-size:.9rem}
.fold>summary::-webkit-details-marker{display:none}
.fold>summary::before{content:"▸";color:var(--mute);font-size:.75rem;flex:none;width:9px}
.fold[open]>summary::before{content:"▾"}
.fold>summary:hover{background:#F4F7FC}
.fold[open]>summary{background:#F4F7FC;border-bottom:1px solid var(--line);
border-radius:9px 9px 0 0}
.fold__t{font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.fold__c{font-size:.71rem;color:var(--soft);background:var(--bg);border:1px solid var(--line);
border-radius:999px;padding:1px 8px;white-space:nowrap;flex:none}
.fold__n{margin-inline-start:auto;color:var(--mute);font-size:.73rem;white-space:nowrap;
flex:none;direction:ltr;unicode-bidi:isolate}
.fold__img{width:42px;height:29px;object-fit:cover;border-radius:5px;flex:none;
border:1px solid var(--line);background:#fff}
.fold__b{padding:12px 14px 14px}
.fold .fold{background:#fff}
.fold--hit{border-color:var(--brand);box-shadow:0 0 0 3px rgba(14,73,163,.12)}
ol.recs{list-style:none;margin:0;padding:0;display:grid;gap:8px}
ol.flat{list-style:none;margin:0;padding:0;display:grid;gap:7px}
ol.flat>li{display:grid;grid-template-columns:19px 1fr;gap:8px;align-items:start;
border:0;padding:0;background:none}
ol.flat>li .n{color:var(--mute);font-size:.73rem;font-weight:700;padding-top:9px}
.cells{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:8px}
@media(max-width:820px){.cells{grid-template-columns:1fr}}
.delrow{margin:14px 0 0}
.btn--del{margin-top:0}
ol.recs>li.rec{display:grid;grid-template-columns:19px 1fr;gap:9px;
border:1px solid var(--line);border-radius:9px;padding:10px 12px;background:#FCFDFE}
ol.recs>li.rec .n{color:var(--mute);font-size:.73rem;font-weight:700;padding-top:3px}
.tools{display:flex;gap:8px;align-items:center;margin:0 0 14px}
.tools .hint{margin:0}
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

// Deleting removes a page from the site, so it asks first. The dirty-state
// warning is suppressed for Add and Delete, which save the form themselves.
document.querySelectorAll('[data-confirm]').forEach(b=>{
  b.addEventListener('click',e=>{
    if(!confirm(b.dataset.confirm)){e.preventDefault();return;}
    dirty=false;
  });
});
document.querySelectorAll('.btn--add').forEach(b=>{
  b.addEventListener('click',()=>{dirty=false;});
});

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

// Records are collapsed by default, so give a way to see everything at once,
// and open the one just added (or linked to) rather than leaving the editor
// hunting for it at the bottom of the list.
function allFolds(){return [...document.querySelectorAll('details.fold')];}
const expandBtn=document.querySelector('[data-expand]');
if(expandBtn){
  expandBtn.addEventListener('click',()=>{
    const open=allFolds().some(d=>!d.open);
    allFolds().forEach(d=>{d.open=open;});
    expandBtn.textContent=open?'Collapse all':'Expand all';
  });
}
(function openRequested(){
  const want=new URLSearchParams(location.search).get('open')||
             decodeURIComponent(location.hash.slice(1));
  if(!want)return;
  const el=document.querySelector('details.fold[data-fold="'+
    want.replace(/"/g,'\\"')+'"]');
  if(!el)return;
  let p=el;
  while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement;}
  el.classList.add('fold--hit');
  el.scrollIntoView({block:'center'});
  const first=el.querySelector('input,textarea,select');
  if(first)first.focus({preventScroll:true});
})();
"""


def page(title, body, flash=None, bar=None, chrome=True):
    thumbs = json.dumps({s: thumb(s) for s in manifest()})
    note = ""
    if flash:
        kind, msg = flash
        note = f'<div class="flash flash--{kind}">{esc(msg)}</div>'
    barhtml = f'<div class="bar"><div class="in">{bar}</div></div>' if bar else ""
    head = ("""<header class="top"><div class="in">
  <a class="brand" href="{PREFIX}">hdip control panel</a>
  <nav>
    <a class="btn" href="{PREFIX}">Content</a>
    <a class="btn" href="{PREFIX}/images">Photos</a>
    <a class="btn" href="/" target="_blank" rel="noopener">View site</a>
    <form method="post" action="{PREFIX}/logout" style="display:contents">
      <button class="btn btn--quiet" type="submit">Sign out</button>
    </form>
  </nav>
</div></header>""" if chrome else "")
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<title>{esc(title)} — HDIP control panel</title><style>{CSS}</style></head>
<body>
{head}
<main class="wrap">{note}{body}</main>
{barhtml}
<script>window.__thumbs={thumbs};</script>
<script>{JS}</script>
</body></html>"""
    # Views are built from a mix of f-strings and plain strings, so resolve the
    # mount point once on the finished document rather than per literal — a
    # missed f prefix would otherwise ship "{PREFIX}" into an href.
    return doc.replace("{PREFIX}", PREFIX)


def count_fields(value):
    if isinstance(value, dict):
        return sum(count_fields(v) for v in value.values())
    if isinstance(value, list):
        return sum(count_fields(v) for v in value)
    return 1


def view_index(flash=None):
    data = store.load()
    cards = []
    for sid, name, where, items in SECTIONS:
        n = sum(count_fields(get_at(data, parse_path(k))) for k, _ in items)
        bits = "".join(f'<span class="chip">{esc(lbl)}</span>' for _, lbl in items)
        cards.append(
            f'<a class="scard" href="{PREFIX}/s/{sid}">'
            f'<div class="scard__head"><h2>{esc(name)}</h2>'
            f'<span class="count">{n} fields</span></div>'
            f'<p class="where">{esc(where)}</p>'
            f'<div class="chips">{bits}</div></a>')
    body = ("<h1>Content</h1>"
            '<p class="sub">One screen per part of the site. Edit, save, then '
            'publish to rewrite the pages.</p>'
            f'<div class="scards">{"".join(cards)}</div>')
    bar = ('<form method="post" action="{PREFIX}/publish" style="display:contents">'
           '<button class="btn btn--p" type="submit">Publish to the site</button></form>'
           '<span class="state">Publishing rebuilds all 58 pages</span>')
    return page("Content", body, flash, bar)


def view_section(sid, flash=None):
    if sid not in SECTION:
        return None
    name, where, items = SECTION[sid]
    data = store.load()

    # Reports are keyed by year rather than listed, so adding one means four
    # coordinated entries; it gets its own control rather than a generic Add.
    extra = ""
    if sid == "reports":
        extra = ('<div class="addbox">'
                 '<b>Add an annual report</b>'
                 '<p class="hint">Creates the report text, adds the year to the '
                 'switch, and sets up its figures and hero photo.</p>'
                 '<div class="addbox__row">'
                 '<input type="text" name="year" placeholder="2026" '
                 'pattern="(19|20)[0-9]{2}" required form="addreport">'
                 '<button class="btn" type="submit" form="addreport">Add report</button>'
                 '</div></div>'
                 f'<form id="addreport" method="post" '
                 f'action="{PREFIX}/addreport" hidden>'
                 f'<input type="hidden" name="sid" value="{esc(sid)}"></form>')

    blocks = []
    for k, lbl in items:
        value = get_at(data, parse_path(k))
        blocks.append(
            f'<section class="block" id="{esc(k.split(".")[1].lower())}">'
            f'<div class="block__head"><h2>{esc(lbl)}</h2>'
            f'<code>{esc(k)}</code></div>'
            f'<input type="hidden" name="__key" value="{esc(k)}">'
            f'{render(k, value, None)}</section>')

    jump = "".join(
        f'<a href="#{esc(k.split(".")[1].lower())}">{esc(lbl)}</a>'
        for k, lbl in items) if len(items) > 1 else ""

    body = (f'<p class="sub" style="margin:0 0 4px">'
            f'<a href="{PREFIX}">← All sections</a></p>'
            f'<h1>{esc(name)}</h1>'
            f'<p class="sub">{esc(where)}</p>'
            + (f'<nav class="jump">{jump}</nav>' if jump else "")
            + '<div class="tools">'
              '<button class="btn" type="button" data-expand>Expand all</button>'
              '<span class="hint">Records are collapsed — open one to edit it. '
              'Saving writes every field on the screen, open or not.</span>'
              '</div>'
            + extra
            + f'<form class="edit" method="post" action="{PREFIX}/save">'
            f'<input type="hidden" name="__sid" value="{esc(sid)}">'
            f'{"".join(blocks)}</form>')
    bar = ('<button class="btn btn--p" '
           'onclick="document.querySelector(\'form.edit\').requestSubmit();return false;">'
           'Save</button>'
           '<a class="btn" href="{PREFIX}">Cancel</a>'
           '<span class="state">Saved changes go live when you publish</span>')
    return page(name, body, flash, bar)


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
            '<form class="up" method="post" action="{PREFIX}/upload" enctype="multipart/form-data">'
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



# ---------------------------------------------------------------------------
# Structural changes
# Adding or removing an item touches the shape of the store, not just text,
# so each one is tried against a real build and rolled back if the build
# fails. The panel should never be able to leave the site unbuildable.
# ---------------------------------------------------------------------------
def apply_structural(change):
    """Run `change(data)`, keep it only if the site still builds."""
    before = store.load()
    data = json.loads(json.dumps(before))
    try:
        note = change(data)
    except ValueError as e:
        return ("err", str(e))
    store.save(data)
    r = subprocess.run([sys.executable, "build.py"], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        store.save(before)
        subprocess.run([sys.executable, "build.py"], cwd=ROOT, capture_output=True)
        detail = (r.stderr or r.stdout).strip().splitlines()[-1:] or [""]
        return ("err", "Change rolled back — the site would not build.\n"
                       + detail[0])
    return ("ok", note)


def add_list_item(key):
    noun = LISTS[key]

    def change(data):
        lst = get_at(data, parse_path(key))
        if not lst:
            raise ValueError("Nothing to copy the shape from.")
        item = blank_like(lst[0])
        if isinstance(item, dict):
            # Blank the prose, but inherit the fields the templates resolve
            # against something else. build.py looks an area up with an
            # unguarded next() and indexes UI by status, so an empty one is a
            # failed build rather than an empty page.
            for structural in ("area", "status", "photo", "icon"):
                if structural in item and lst[0].get(structural):
                    item[structural] = lst[0][structural]
            if "slug" in item:
                item["slug"] = unique_slug(f"new-{noun}")
            for lg in ("en", "ar"):
                block = item.get(lg)
                if not isinstance(block, dict):
                    continue
                for titleish in ("title", "name"):
                    if titleish in block:
                        block[titleish] = f"Untitled {noun}"
        lst.append(item)
        return f"Added a blank {noun}. Fill it in, then publish."

    kind, msg = apply_structural(change)
    anchor = ""
    if kind == "ok":
        lst = get_at(store.load(), parse_path(key))
        anchor = f"{key}[{len(lst) - 1}]"
    return kind, msg, anchor


def delete_list_item(key, idx):
    noun = LISTS[key]

    def change(data):
        lst = get_at(data, parse_path(key))
        if not 0 <= idx < len(lst):
            raise ValueError("That item no longer exists.")
        if len(lst) <= 1:
            raise ValueError(f"The last {noun} cannot be deleted — "
                             "the templates need at least one to copy from.")
        gone = lst.pop(idx)
        name = record_name(gone) or (gone.get("slug", "")
                                     if isinstance(gone, dict) else "")
        return f"Deleted the {noun} “{name}”. Publish to remove its page."
    return apply_structural(change)


def add_report(year):
    """A report year is four coordinated entries, not one.

    REPORTS holds the text, YEARS drives the index and the year switch,
    IMPACT the figures behind that switch, and HERO_PHOTOS the picture at the
    top — which build.py reads directly, so a missing one is a KeyError and a
    failed build rather than a blank page.
    """
    if not re.fullmatch(r"(19|20)\d{2}", year or ""):
        return ("err", "Use a four-digit year, for example 2026.")

    def change(data):
        years, reports = data["years"], data["years"]["REPORTS"]
        if year in reports or year in years["YEARS"]:
            raise ValueError(f"{year} already exists.")
        template = reports[sorted(reports)[-1]]
        new = blank_like(template)
        for lg in ("en", "ar"):
            if isinstance(new.get(lg), dict):
                new[lg]["year"] = year
                new[lg]["title"] = (f"Annual Report {year}" if lg == "en"
                                    else f"التقرير السنوي {year}")
        reports[year] = new
        years["YEARS"] = sorted(set(years["YEARS"]) | {year}, reverse=True)
        years["IMPACT"][year] = blank_like(
            years["IMPACT"][sorted(years["IMPACT"])[-1]])
        photos = years["HERO_PHOTOS"]
        photos[f"report-{year}"] = photos.get(
            f"report-{sorted(reports)[-1]}", sorted(manifest())[0])
        return (f"Added Annual Report {year} — report text, the year switch, "
                "its figures and a hero photo. Fill it in, then publish.")
    return apply_structural(change)



def save_fields(form):
    """Write every submitted field that lies inside a known content key.

    A section page posts several keys at once, so the guard is per field:
    a path is written only if it sits under one of the keys this panel owns.
    """
    data = store.load()
    roots = [(k, parse_path(k)) for k in LABELS]
    count = 0
    for path, vals in form.items():
        if path.startswith("__"):
            continue
        parts = parse_path(path)
        if not any(parts[:len(r)] == r for _, r in roots):
            continue
        value = vals[0]
        # build.py writes a page per slug, named after it, so a typed slug is
        # normalised rather than trusted: "New Project" would otherwise
        # generate "project-New Project.html" and link to it with a space.
        if parts[-1] == "slug" and isinstance(value, str) and value.strip():
            value = slugify(value) or value.strip()
        try:
            set_at(data, parts, value)
            count += 1
        except (KeyError, IndexError, TypeError):
            continue
    store.save(data)
    return count


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



# ---------------------------------------------------------------------------
# Access control
# The panel writes files and runs builds, so it is never open — not even on
# localhost. Credentials live in data/admin.local.json, which is gitignored:
# only a PBKDF2 hash is stored, never the password itself.
# ---------------------------------------------------------------------------
import base64
import hashlib
import hmac
import http.cookies
import secrets
import time

PBKDF2_ROUNDS = 240_000


def hash_password(password, salt=None):
    salt = salt or secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                             salt.encode("ascii"), PBKDF2_ROUNDS)
    return {"salt": salt, "hash": dk.hex(), "rounds": PBKDF2_ROUNDS}


NOTE = ("Credentials for the control panel at /admin. Gitignored — never "
        "commit this file. To change the password, type a new one into "
        "\"password\" and restart: the hash is re-derived from it on startup. "
        "Delete the file and restart to be issued a fresh random one.")


def write_credentials(rec):
    os.makedirs(os.path.dirname(AUTH_FILE), exist_ok=True)
    tmp = AUTH_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=1)
    os.replace(tmp, AUTH_FILE)
    os.chmod(AUTH_FILE, 0o600)


def ensure_credentials():
    """Load credentials, creating them on first run.

    Editing "password" in the file is the supported way to change it: the
    hash is re-derived whenever the two disagree. Checking the hash while
    ignoring an edited password would lock the owner out of their own panel
    with no visible reason, which is a worse failure than any it prevents.

    The password is never echoed into the server log — logs get pasted into
    chats and issues.
    """
    if os.path.isfile(AUTH_FILE):
        with open(AUTH_FILE, encoding="utf-8") as f:
            rec = json.load(f)
        plain = rec.get("password")
        if plain:
            dk = hashlib.pbkdf2_hmac("sha256", plain.encode("utf-8"),
                                     rec["salt"].encode("ascii"),
                                     rec.get("rounds", PBKDF2_ROUNDS))
            if not hmac.compare_digest(dk.hex(), rec.get("hash", "")):
                rec.update(hash_password(plain))
                rec["_note"] = NOTE
                write_credentials(rec)
                print("  Password changed in data/admin.local.json — hash updated.")
        return rec

    user = os.environ.get("HDIP_ADMIN_USER", "hdip")
    password = os.environ.get("HDIP_ADMIN_PASSWORD") or secrets.token_urlsafe(18)
    rec = {"_note": NOTE, "user": user, "password": password,
           **hash_password(password)}
    write_credentials(rec)
    print(f"\n  Control panel credentials written to {AUTH_FILE}")
    print("  (open that file for the password; it is not printed here)\n")
    return rec


def set_password_interactively():
    """`--set-password`: prompt without echo, store the hash only."""
    import getpass
    rec = ensure_credentials()
    user = input(f"user [{rec['user']}]: ").strip() or rec["user"]
    first = getpass.getpass("new password: ")
    if len(first) < 10:
        print("  Too short — use at least 10 characters.")
        return 1
    if first != getpass.getpass("repeat: "):
        print("  They did not match; nothing changed.")
        return 1
    new = {"_note": NOTE, "user": user, **hash_password(first)}
    write_credentials(new)
    print(f"  Updated {AUTH_FILE} — hash only, the password is not stored.")
    return 0


CREDS = None
_CREDS_MTIME = None


def current_credentials():
    """Re-read the credentials file whenever it changes on disk.

    Loading once at startup meant editing the password appeared to do nothing
    until the server was restarted — with no error to explain it. Re-reading
    on change costs a stat per request, which is nothing beside the PBKDF2
    round that follows.
    """
    global CREDS, _CREDS_MTIME
    try:
        mtime = os.path.getmtime(AUTH_FILE)
    except OSError:
        return CREDS
    if mtime != _CREDS_MTIME:
        CREDS = ensure_credentials()
        _CREDS_MTIME = os.path.getmtime(AUTH_FILE)
    return CREDS


def verify_password(user, password):
    """Constant-time check against the stored PBKDF2 hash."""
    creds = current_credentials()
    if not creds:
        return False
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                             creds["salt"].encode("ascii"),
                             creds.get("rounds", PBKDF2_ROUNDS))
    return (hmac.compare_digest(user, creds["user"])
            and hmac.compare_digest(dk.hex(), creds["hash"]))


# ---------------------------------------------------------------------------
# Sessions
# HTTP Basic has no logout: the browser replays the password on every request
# and there is no standard way to make it stop. A cookie session gives a real
# sign-out, and means the password crosses the wire once rather than with
# every image on the photos screen.
#
# Sessions live in memory only, so restarting the server signs everyone out.
# ---------------------------------------------------------------------------
SESSION_COOKIE = "hdip_session"
SESSION_HOURS = 12
SESSIONS = {}


def new_session(user):
    token = secrets.token_urlsafe(32)
    SESSIONS[token] = {"user": user, "expires": time.time() + SESSION_HOURS * 3600}
    return token


def session_user(cookie_header):
    """The signed-in user for this request, or None."""
    if not cookie_header:
        return None
    jar = http.cookies.SimpleCookie()
    try:
        jar.load(cookie_header)
    except http.cookies.CookieError:
        return None
    morsel = jar.get(SESSION_COOKIE)
    if not morsel:
        return None
    rec = SESSIONS.get(morsel.value)
    if not rec:
        return None
    if rec["expires"] < time.time():
        SESSIONS.pop(morsel.value, None)
        return None
    return rec["user"]


def drop_session(cookie_header):
    if not cookie_header:
        return
    jar = http.cookies.SimpleCookie()
    try:
        jar.load(cookie_header)
    except http.cookies.CookieError:
        return
    morsel = jar.get(SESSION_COOKIE)
    if morsel:
        SESSIONS.pop(morsel.value, None)


def view_login(message=None, nexturl=None):
    note = (f'<div class="flash flash--err">{esc(message)}</div>' if message else "")
    body = (
        '<div class="login">'
        f'{note}'
        '<h1>Sign in</h1>'
        '<p class="sub">The control panel for the HDIP website.</p>'
        f'<form method="post" action="{PREFIX}/login">'
        f'<input type="hidden" name="next" value="{esc(nexturl or PREFIX)}">'
        '<div class="f"><label for="u">User</label>'
        '<input id="u" name="user" type="text" autocomplete="username" autofocus required></div>'
        '<div class="f"><label for="p">Password</label>'
        '<input id="p" name="password" type="password" autocomplete="current-password" required></div>'
        '<button class="btn btn--p" type="submit">Sign in</button>'
        '</form></div>')
    return page("Sign in", body, chrome=False)


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

    def redirect(self, to, cookie=None):
        self.send_response(303)
        self.send_header("Location", to)
        if cookie:
            self.send_header("Set-Cookie", cookie)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def session_cookie(self, token, clear=False):
        """HttpOnly so script cannot read it; Strict so it is not sent
        cross-site; Secure only over HTTPS, since a Secure cookie on plain
        HTTP is simply dropped and sign-in would fail with no explanation."""
        bits = [f"{SESSION_COOKIE}={'' if clear else token}",
                f"Path={PREFIX}", "HttpOnly", "SameSite=Strict"]
        if clear:
            bits.append("Max-Age=0")
        else:
            bits.append(f"Max-Age={SESSION_HOURS * 3600}")
        if self.headers.get("X-Forwarded-Proto") == "https":
            bits.append("Secure")
        return "; ".join(bits)

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
    # -- access ----------------------------------------------------------
    def guard(self, full_path):
        """Every /admin request needs a session. Returns True to continue."""
        if session_user(self.headers.get("Cookie")):
            return True
        if self.command == "GET":
            self.send_html(view_login(nexturl=full_path), 401)
        else:
            self.redirect(f"{PREFIX}/login")
        return False

    def admin_path(self, u):
        """`/admin/edit` -> `/edit`; None when the request is not for the panel."""
        if u.path == PREFIX:
            return "/"
        if u.path.startswith(PREFIX + "/"):
            return u.path[len(PREFIX):]
        return None

    def serve_site(self, u):
        """The built static site, so one address serves site and panel."""
        rel = urllib.parse.unquote(u.path).lstrip("/") or "index.html"
        path = os.path.normpath(os.path.join(ROOT, rel))
        # Never serve outside the project, and never serve the panel's own
        # files, the store, or the credentials.
        if not path.startswith(ROOT + os.sep) and path != ROOT:
            self.send_error(403)
            return
        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
        blocked = (os.path.join(ROOT, "data"), os.path.join(ROOT, "tools"),
                   os.path.join(ROOT, ".git"))
        if any(path.startswith(b + os.sep) for b in blocked):
            self.send_error(404)
            return
        ext = path.rsplit(".", 1)[-1].lower()
        ctype = {"html": "text/html; charset=utf-8", "css": "text/css; charset=utf-8",
                 "js": "text/javascript; charset=utf-8", "json": "application/json",
                 "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
                 "webp": "image/webp", "svg": "image/svg+xml",
                 "ico": "image/x-icon"}.get(ext, "application/octet-stream")
        self.serve_file(path, ctype)

    # -- routes ----------------------------------------------------------
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        p = self.admin_path(u)
        if p is None:
            self.serve_site(u)
            return
        if p == "/login":
            if session_user(self.headers.get("Cookie")):
                self.redirect(PREFIX)
            else:
                self.send_html(view_login())
            return
        if not self.guard(self.path):
            return

        q = urllib.parse.parse_qs(u.query)
        flash = None
        if "ok" in q:
            flash = ("ok", q["ok"][0])
        elif "err" in q:
            flash = ("err", q["err"][0])

        if p == "/":
            self.send_html(view_index(flash))
        elif p.startswith("/s/"):
            v = view_section(p[3:], flash)
            if v:
                self.send_html(v)
            else:
                self.send_error(404, "No such section")
        elif p == "/edit":
            # Old per-key links still work; send them to the section.
            sid = SECTION_OF.get(q.get("k", [""])[0])
            self.redirect(f"{PREFIX}/s/{sid}" if sid else PREFIX)
        elif p == "/images":
            self.send_html(view_images(flash))
        elif p.startswith("/img/"):
            name = os.path.basename(urllib.parse.unquote(p[5:]))
            ext = name.rsplit(".", 1)[-1].lower()
            ctype = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
                     "webp": "image/webp", "svg": "image/svg+xml"}.get(
                         ext, "application/octet-stream")
            self.serve_file(os.path.join(IMG_DIR, name), ctype)
        else:
            self.send_error(404)

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        p = self.admin_path(u)
        if p is None:
            self.send_error(404)
            return

        if p == "/login":
            length = int(self.headers.get("Content-Length", "0"))
            form = urllib.parse.parse_qs(self.rfile.read(length).decode("utf-8"))
            user = form.get("user", [""])[0]
            password = form.get("password", [""])[0]
            nexturl = form.get("next", [PREFIX])[0]
            # Only ever bounce back inside the panel.
            if not nexturl.startswith(PREFIX):
                nexturl = PREFIX
            if verify_password(user, password):
                self.redirect(nexturl,
                              self.session_cookie(new_session(user)))
            else:
                self.send_html(view_login("That user and password did not match.",
                                          nexturl), 401)
            return

        if p in ("/additem", "/delitem", "/addreport"):
            length = int(self.headers.get("Content-Length", "0"))
            form = urllib.parse.parse_qs(
                self.rfile.read(length).decode("utf-8"), keep_blank_values=True)
            sid = form.get("__sid", form.get("sid", [""]))[0]
            if sid not in SECTION:
                self.send_error(400, "Unknown section")
                return
            if not session_user(self.headers.get("Cookie")):
                self.redirect(f"{PREFIX}/login")
                return
            # Keep what is on screen before changing the shape, so edits in
            # progress are not lost by pressing Add.
            if p != "/addreport":
                save_fields(form)

            anchor = ""
            if p == "/addreport":
                kind, msg = add_report(form.get("year", [""])[0].strip())
            else:
                if p == "/additem":
                    key = form.get("listkey", [""])[0]
                    if key not in LISTS:
                        self.send_error(400, "Not an editable list")
                        return
                    kind, msg, anchor = add_list_item(key)
                else:
                    key, _, raw = form.get("item", [""])[0].rpartition("|")
                    if key not in LISTS:
                        self.send_error(400, "Not an editable list")
                        return
                    try:
                        idx = int(raw)
                    except ValueError:
                        idx = -1
                    kind, msg = delete_list_item(key, idx)
            to = f"{PREFIX}/s/{sid}?{kind}=" + urllib.parse.quote(msg)
            if anchor:
                to += "&open=" + urllib.parse.quote(anchor)
            self.redirect(to)
            return

        if p == "/logout":
            drop_session(self.headers.get("Cookie"))
            self.redirect(f"{PREFIX}/login",
                          self.session_cookie(None, clear=True))
            return

        if not self.guard(self.path):
            return
        u = urllib.parse.urlparse(p)

        if u.path == "/publish":
            kind, msg = publish()
            self.redirect(f"{PREFIX}?{kind}={urllib.parse.quote(msg)}")
            return

        if u.path == "/upload":
            fields = parse_multipart(self.headers, self.rfile)
            slug = str(fields.get("slug", "")).strip().lower()
            item = fields.get("file")
            if not re.fullmatch(r"[a-z0-9-]+", slug or ""):
                self.redirect(f"{PREFIX}/images?err=" + urllib.parse.quote(
                    "Use lower-case letters, numbers and hyphens for the short name."))
                return
            if not isinstance(item, tuple) or not item[1]:
                self.redirect(f"{PREFIX}/images?err=" + urllib.parse.quote("No file received."))
                return
            err = add_image(slug, item[1], item[0] or "")
            if err:
                self.redirect(f"{PREFIX}/images?err=" + urllib.parse.quote(err))
            else:
                self.redirect(f"{PREFIX}/images?ok=" + urllib.parse.quote(
                    f"Added “{slug}”. Pick it on a content screen, then publish."))
            return

        if u.path == "/save":
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8")
            form = urllib.parse.parse_qs(body, keep_blank_values=True)
            sid = form.get("__sid", [""])[0]
            if sid not in SECTION:
                self.send_error(400, "Unknown section")
                return
            count = save_fields(form)
            self.redirect(f"{PREFIX}/s/{sid}&ok=".replace("&ok=", "?ok=")
                          + urllib.parse.quote(
                              f"Saved {count} fields. Publish to put them live."))
            return

        self.send_error(404)


def main():
    global CREDS
    if "--set-password" in sys.argv:
        return set_password_interactively()
    CREDS = ensure_credentials()

    if HOST not in ("127.0.0.1", "localhost", "::1"):
        print("\n  WARNING: binding to", HOST, "exposes /admin beyond this machine.")
        print("  The sign-in form posts the password in clear text, so put")
        print("  TLS in front of it before doing that on a real network.\n")

    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"  site   http://{HOST}:{PORT}/")
    print(f"  panel  http://{HOST}:{PORT}{PREFIX}")
    print(f"  store  data/site.json")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    sys.exit(main() or 0)
