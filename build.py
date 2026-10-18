#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HDIP static site generator — builds the structure approved in
"HDIP Website — Site Structure for Approval" (29 Sep 2026).

English at the root, Arabic (RTL) under /ar/. Run:  python3 build.py
All text lives in content.py; all figures come from HDIP's 2024 documents.
"""

import math
import hashlib
import json
import os

import content as C
import content_years as Y

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ("en", "ar")

# Internal "content needed" placeholders. They are a signal for us, not content
# for HDIP's readers — About should not close by reporting a missing deliverable.
# Set True to see the gaps inline while working; the full list always stays on
# credits.html either way.
DRAFT = False

HDIP_PHOTOS = {p["slug"]: p for p in
               json.load(open(os.path.join(ROOT, "assets/img/hdip-photos.json"), encoding="utf-8"))}
CC_PHOTOS = {c["slug"]: c for c in
             json.load(open(os.path.join(ROOT, "assets/img/credits.json"), encoding="utf-8"))}

# What actually exists on disk. Variants are never upscaled, so a small source
# simply has fewer tiers — srcset follows the manifest instead of assuming
# 320/800/1600 and pointing at files we deliberately did not fabricate.
MANIFEST = json.load(open(os.path.join(ROOT, "assets/img/manifest.json"), encoding="utf-8"))


def asset_hash(path):
    try:
        return hashlib.md5(open(os.path.join(ROOT, path), "rb").read()).hexdigest()[:8]
    except OSError:
        return "0"


CSS_V = None  # filled in main()

# All four annual reports in one place (2024 lives in content.py).
ALL_REPORTS = dict(Y.REPORTS)
ALL_REPORTS["2024"] = C.REPORT_2024
ALL_NEWS = C.NEWS + Y.NEWS_2025


# --------------------------------------------------------------------------
# Icons
# --------------------------------------------------------------------------
def _i(p):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + p + "</svg>")


ICONS = {
    "pulse": _i('<path d="M3 12h4l2.5-7 4 14L16 12h5"/>'),
    "book": _i('<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5Z"/>'
               '<path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5A2.5 2.5 0 0 1 4 20.5Z"/>'),
    "users": _i('<path d="M16 20v-1.5a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4V20"/><circle cx="9" cy="7" r="3.2"/>'
                '<path d="M22 20v-1.5a4 4 0 0 0-3-3.85"/><path d="M16.5 4.2a3.2 3.2 0 0 1 0 5.6"/>'),
    "vote": _i('<path d="M3 15.5 12 19l9-3.5"/><path d="M3 15.5 12 12l9 3.5"/>'
               '<path d="M7.5 10.5V4h9v6.5"/><path d="M10 7h4"/>'),
    "search": _i('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>'),
    "mail": _i('<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="m3 7 9 6 9-6"/>'),
    "phone": _i('<path d="M6 3h3l2 5-2.5 1.5a12 12 0 0 0 6 6L16 13l5 2v3a2 2 0 0 1-2.2 2A17 17 0 0 1 4 5.2 2 2 0 0 1 6 3Z"/>'),
    "pin": _i('<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/>'),
    "print": _i('<path d="M7 8V3h10v5"/><rect x="3" y="8" width="18" height="8" rx="2"/><path d="M7 14h10v7H7Z"/>'),
    "doc": _i('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/>'
              '<path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/>'),
    "globe": _i('<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18Z"/>'),
    "flag": _i('<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>'),
    "alert": _i('<circle cx="12" cy="12" r="9"/><path d="M12 8v5"/><path d="M12 16.5h.01"/>'),
    "heart": _i('<path d="M12 20s-7-4.4-7-9.2A4 4 0 0 1 12 8a4 4 0 0 1 7 2.8C19 15.6 12 20 12 20Z"/>'),
}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>')


def icon(n):
    return ICONS.get(n, ICONS["doc"])


# --------------------------------------------------------------------------
# Images
# --------------------------------------------------------------------------
# Artwork supplied for the build rather than photographed or licensed from a
# source. Kept separate from credits.json, which is specifically the record of
# photographers and their licences.
SUPPLIED_ART = {
    "annual-report-book": {
        "alt": "",                      # decorative; the link beside it names it
        "en": "Annual report cover mockup",
        "ar": "نموذج غلاف التقرير السنوي",
        "source": "Supplied by Dragon Media",
    },
    "founding-1989": {
        "alt": "",                      # decorative; the year is in the heading
        "en": "Founding-year illustration — numerals, olive branches and a "
              "cross-stitch motif",
        "ar": "رسم توضيحي لسنة التأسيس — أرقام وأغصان زيتون ونقش تطريز",
        "source": "Supplied by Dragon Media",
    },
}


def img(slug, lang, sizes="(max-width: 900px) 100vw, 50vw", eager=False, decorative=False):
    base = "../assets/img" if lang == "ar" else "assets/img"
    if slug in HDIP_PHOTOS:
        alt = HDIP_PHOTOS[slug]["alt"]
    elif slug in CC_PHOTOS:
        alt = Y.CONTEXT_PHOTOS.get(slug, {}).get("alt", "")
    else:
        # Commissioned artwork carries no photographic credit; it is recorded
        # in SUPPLIED_ART instead of being given a fake entry in credits.json.
        alt = SUPPLIED_ART.get(slug, {}).get("alt", "")
    load = "" if eager else ' loading="lazy"'
    if decorative:
        alt = ""
    entry = MANIFEST[slug]
    widths = entry["widths"]
    # Photographs are JPEG; anything that must keep its transparency declares
    # its own format, so it sits over whatever is behind it instead of
    # carrying a baked-in background.
    ext = entry.get("ext", "jpg")
    srcset = ", ".join(f"{base}/{slug}-{w}.{ext} {w}w" for w in widths)
    fallback = 800 if 800 in widths else widths[0]
    return (f'<img src="{base}/{slug}-{fallback}.{ext}" '
            f'srcset="{srcset}" '
            f'sizes="{sizes}" alt="{alt}" width="{entry["w"]}" height="{entry["h"]}"'
            f'{load} decoding="async">')


def caption(slug, lang):
    if slug in HDIP_PHOTOS:
        m = HDIP_PHOTOS[slug]
        return m["cap_ar"] if lang == "ar" else m["cap_en"]
    c = Y.CONTEXT_PHOTOS.get(slug)
    return (c["ar"] if lang == "ar" else c["en"]) if c else ""


def credit(slug, lang):
    if slug in HDIP_PHOTOS:
        return "© HDIP"
    c = CC_PHOTOS[slug]
    return f'<a href="{c["page"]}" target="_blank" rel="noopener">{c["artist"]}</a> · {c["license"]}'


def figure(slug, lang, ratio="3x2", sizes="(max-width: 900px) 100vw, 50vw", cap=True):
    f = f'<figure class="media media--{ratio}">{img(slug, lang, sizes)}'
    if cap:
        f += (f'<figcaption class="media__cap"><b>{caption(slug, lang)}</b>'
              f'<span class="credit">{credit(slug, lang)}</span></figcaption>')
    return f + "</figure>"


def plain(slug, lang, ratio="3x2", sizes="(max-width: 900px) 100vw, 33vw"):
    return f'<figure class="media media--{ratio}">{img(slug, lang, sizes)}</figure>'


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------
def brand(lang):
    u = C.UI[lang]
    home = "index.html"
    base = "../assets/img" if lang == "ar" else "assets/img"
    # Two renditions: blue for the light masthead, cream for the dark footer,
    # where the official blue only reaches 1.95:1.
    def mark(variant, cls):
        v = asset_hash(f"assets/img/{variant}-320.png")   # bust the cache on edits
        return (f'<img class="{cls}" src="{base}/{variant}-160.png?v={v}" '
                f'srcset="{base}/{variant}-160.png?v={v} 160w, {base}/{variant}-320.png?v={v} 320w, '
                f'{base}/{variant}-480.png?v={v} 480w" sizes="96px" '
                f'alt="{u["org_short"]}" width="1027" height="473" decoding="async">')
    return (f'<a class="brand" href="{home}" aria-label="{u["org"]}">'
            f'{mark("logo", "brand__logo")}'
            f'{mark("logo-light", "brand__logo brand__logo--light")}</a>')


def header(lang, current):
    u = C.UI[lang]
    links = "\n            ".join(
        f'<a class="nav__link" href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>'
        for h, t in C.NAV[lang])
    other = "ar/" if lang == "en" else "../"
    alt_page = current if current != "index.html" else ""
    lang_href = f"{other}{alt_page}" if lang == "en" else f"../{alt_page}"
    return f"""  <a class="skip-link" href="#main">{u['skip']}</a>
  <header class="site-header">
    <nav class="nav wrap" aria-label="Primary">
      {brand(lang)}
      <div class="nav__menu" id="nav-menu">
        <div class="nav__links">
            {links}
        </div>
        <div class="nav__actions">
          <a class="nav__lang" href="{lang_href}" lang="{'ar' if lang == 'en' else 'en'}">{u['lang_label']}</a>
          <a class="btn" href="contact.html">{u['contact']}</a>
        </div>
      </div>
      <div class="nav__actions">
        <a class="nav__lang" href="{lang_href}" lang="{'ar' if lang == 'en' else 'en'}">{u['lang_label']}</a>
        <a class="btn" href="contact.html">{u['contact']}</a>
      </div>
      <button class="nav__toggle" type="button" aria-expanded="false"
              aria-controls="nav-menu" aria-label="Menu"><span></span></button>
    </nav>
  </header>
"""


def footer(lang):
    u = C.UI[lang]
    areas = "".join(f'<li><a href="area-{a["slug"]}.html">{a[lang]["name"]}</a></li>' for a in C.AREAS)
    projects = "".join(f'<li><a href="project-{p["slug"]}.html">{p[lang]["name"]}</a></li>' for p in C.PROJECTS)
    more = {"en": [("about.html", "About HDIP"), ("reports.html", "Reports"),
                   ("news.html", "News & stories"),
                   ("contact.html", "Contact")],
            "ar": [("about.html", "عن البرنامج"), ("reports.html", "التقارير"),
                   ("news.html", "أخبار وقصص"),
                   ("contact.html", "اتصل بنا")]}[lang]
    more_li = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in more)
    h = {"en": ("Programme areas", "Projects", "More"), "ar": ("مجالات العمل", "المشاريع", "المزيد")}[lang]
    return f"""  <footer class="site-footer">
    <span class="stitchfield stitchfield--dots" aria-hidden="true"
          style="--px:8%;--py:26%;--pw:40%;--ph:62%;--stitch-op:.5"></span>
    <span class="stitchfield" aria-hidden="true"
          style="--px:92%;--py:70%;--pw:34%;--ph:56%;--stitch-op:.5"></span>
    <div class="wrap">
      <div class="footer__grid">
        <div>
          {brand(lang)}
          <p class="footer__about">{u['footer_about']}</p>
        </div>
        <div class="footer__col"><h3 class="footer__h">{h[0]}</h3><ul>{areas}</ul></div>
        <div class="footer__col"><h3 class="footer__h">{h[1]}</h3><ul>{projects}</ul></div>
        <div class="footer__col"><h3 class="footer__h">{h[2]}</h3><ul>{more_li}</ul></div>
      </div>
      <div class="footer__bottom">
        <div class="footer__row">
          <p>© <span data-year>2026</span> {u['org']} — {u['org_short'].upper()}</p>
          <p class="footer__by">{u['developed_by']}
            <a href="https://itsdragon.com" target="_blank" rel="noopener">Dragon Media</a></p>
        </div>
        <div class="footer__row">
          <p><a href="mailto:hdip@hdip.org">hdip@hdip.org</a> · <a href="tel:+97222985372">+972 2 298 5372</a></p>
        </div>
      </div>
    </div>
  </footer>
"""


def page(lang, filename, title, description, body, current=None, social=None):
    u = C.UI[lang]
    current = current or filename
    base = "../assets" if lang == "ar" else "assets"
    base_root = "../" if lang == "ar" else ""
    # Arabic overrides both Latin families to Almarai site-wide, so do not
    # download two families the RTL pages never paint.
    if lang == "ar":
        fonts = ("https://fonts.googleapis.com/css2?family=Almarai:wght@300;400;700;800"
                 "&family=IBM+Plex+Mono:wght@400;500&display=swap")
    else:
        fonts = ("https://fonts.googleapis.com/css2?family=Outfit:wght@300..800"
                 "&family=Inter:wght@400..700"
                 "&family=IBM+Plex+Mono:wght@400;500&display=swap")
    # Use the largest tier that actually exists — not every image has a 1600.
    if social:
        best = max(MANIFEST[social]["widths"])
        og = f'\n  <meta property="og:image" content="{base}/img/{social}-{best}.jpg">'
    else:
        og = ""
    out_dir = os.path.join(ROOT, "ar") if lang == "ar" else ROOT
    os.makedirs(out_dir, exist_ok=True)
    html = f"""<!doctype html>
<html lang="{u['code']}" dir="{u['dir']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — {u['org_short'].upper()}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#0E49A3">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">{og}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{fonts}" rel="stylesheet">
  <link rel="stylesheet" href="{base}/css/style.css?v={CSS_V}">
  <link rel="icon" href="{base_root}favicon.svg" type="image/svg+xml">
  <link rel="mask-icon" href="{base_root}favicon.svg" color="#0E49A3">
</head>
<body>
 <div class="canvas">
{header(lang, current)}
  <main id="main">
{body}
  </main>
{footer(lang)}
 </div>
  <script src="{base}/js/main.js?v={asset_hash('assets/js/main.js')}"></script>
</body>
</html>
"""
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)
    return ("ar/" if lang == "ar" else "") + filename


# --------------------------------------------------------------------------
# Blocks
# --------------------------------------------------------------------------
def page_hero(lang, crumb, title, lead, slug=None, crumb_href=None):
    u = C.UI[lang]
    trail = f'<a href="index.html">{u["home"]}</a><span>/</span>'
    if crumb_href:
        trail += f'<a href="{crumb_href}">{crumb[0]}</a><span>/</span>{crumb[1]}'
    else:
        trail += crumb
    if slug is None:
        return f"""    <section class="page-hero">
      <div class="wrap"><p class="crumbs">{trail}</p><h1>{title}</h1>
      <p class="lead measure">{lead}</p></div>
    </section>
"""
    return f"""    <section class="page-hero page-hero--media">
      <div class="page-hero__bg" aria-hidden="true">{img(slug, lang, "100vw", eager=True, decorative=True)}</div>
      <div class="wrap page-hero__content">
        <p class="crumbs">{trail}</p>
        <h1>{title}</h1>
        <p class="lead measure">{lead}</p>
      </div>
      <p class="page-hero__credit">{caption(slug, lang)} — {credit(slug, lang)}
        · <a href="credits.html">{C.UI[lang]['credits']}</a></p>
    </section>
"""


def needed(lang, title, note=None):
    u = C.UI[lang]
    return f"""        <div class="needed" data-reveal>
          <span class="needed__tag">{icon('alert')} {u['content_needed']}</span>
          <h3>{title}</h3>
          <p>{note or u['content_needed_note']}</p>
        </div>"""


def ending(lang, kind, href="contact.html"):
    """Every page closes on a call, not on the footer."""
    t, body, cta = Y.ENDINGS[lang][kind]
    return f"""    <section class="section--tight" style="padding-bottom:clamp(72px,10vw,132px)">
      <div class="wrap">
        <div class="cta" data-reveal>
          <h2 class="measure center">{t}</h2>
          <p class="lead measure center" style="color:rgba(240,247,243,.82)">{body}</p>
          <div class="hero__actions" style="justify-content:center">
            <a class="btn btn--light" href="{href}">{cta} {ARROW}</a>
          </div>
        </div>
      </div>
    </section>
"""


def stat_grid(items, lang):
    cells = "".join(
        f'<div class="stat"><span class="stat__num">{n}</span>'
        f'<span class="stat__label">{l}</span></div>' for n, l in items)
    return f'<div class="stats" data-reveal>{cells}</div>'


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
CROWD_FIELD = (
    '<svg class="crowd" viewBox="0 0 1200 520" preserveAspectRatio="xMidYMid slice" '
    'aria-hidden="true" focusable="false">'
    '<defs>'
    '<pattern id="crowd-tile" width="46" height="52" patternUnits="userSpaceOnUse">'
    '<g fill="currentColor">'
    '<circle cx="11" cy="13" r="4.6"/>'
    '<path d="M3.4 32c0-4.6 3.4-8.2 7.6-8.2s7.6 3.6 7.6 8.2v4H3.4z"/>'
    '<circle cx="34" cy="31" r="4.6"/>'
    '<path d="M26.4 50c0-4.6 3.4-8.2 7.6-8.2s7.6 3.6 7.6 8.2v2H26.4z"/>'
    '</g>'
    '</pattern>'
    '<radialGradient id="crowd-fade" cx="50%" cy="50%" r="62%">'
    '<stop offset="0%" stop-color="#fff" stop-opacity="0"/>'
    '<stop offset="52%" stop-color="#fff" stop-opacity="0.45"/>'
    '<stop offset="100%" stop-color="#fff" stop-opacity="1"/>'
    '</radialGradient>'
    '<mask id="crowd-mask">'
    '<rect width="1200" height="520" fill="url(#crowd-fade)"/>'
    '</mask>'
    '</defs>'
    '<rect width="1200" height="520" fill="url(#crowd-tile)" mask="url(#crowd-mask)"/>'
    '</svg>'
)


# A picture of each governorate. Every entry is a photograph actually taken in
# that governorate — the five sourced from Wikimedia Commons are openly
# licensed and recorded in credits.json with photographer and licence, which
# the credits page renders. These are documentary pictures of the places, not
# HDIP programme photography; swap any of them the moment HDIP supplies their
# own picture from that governorate.
#
# Two were chosen over more obvious results on purpose. Abu Dis searches turn
# up the separation barrier; Al-Quds University says more about why HDIP works
# there. Gaza searches turn up war damage; a city panorama states the presence
# without making an editorial claim HDIP has not made.
GOV_PHOTO = {
    "Hebron":     "olive-planting",     # olive planting at Beit Ummar, Hebron governorate
    "Bethlehem":  "bethlehem-city",     # Church of the Nativity
    "Abu Dis":    "abudis-aqu",         # Al-Quds University, which is in Abu Dis
    "Ramallah":   "ramallah-oldcity",
    "Jenin":      "jenin-city",
    "Tulkarm":    "tulkarm-downtown",
    "Nablus":     "olives-nablus",
    "Gaza":       "gaza-city",          # city panorama, 2007 — see the note in credits
}


def founding_mark(lang, h):
    """The founding year as the section's image.

    Supplied artwork, used as given. It is cropped only below the
    illustration, where the source carries a caption band baked into the
    pixels: those labels are English, so they would ship untranslated onto
    the Arabic pages, and flat pixels cannot be links. The timeline and the
    programme links below the figure carry that content live, translated and
    clickable. Restore the full frame by re-cropping to the source height.

    The figure itself is decorative and hidden from assistive technology —
    the founding year is already in the heading beside it.
    """
    u = C.UI[lang]
    areas = "".join(
        f'<li><a href="area-{a["slug"]}.html">{a[lang]["name"]}</a></li>'
        for a in C.AREAS)
    return (
        f'<div class="yearmark" data-reveal>'
        f'<div class="yearmark__art" aria-hidden="true">'
        f'{img("founding-1989", lang, "(max-width: 920px) 92vw, 46vw")}'
        f'</div>'
        f'<p class="yearline"><span>1989</span><span class="yearline__bar"></span>'
        f'<span>{u["today"]}</span></p>'
        f'<ul class="pillars">{areas}</ul>'
        f'</div>'
    )


def section_head(title, eyebrow=None, lead=None, aside=None):
    """The standard section opening: a small tracked label, then the heading.

    `eyebrow` is optional because not every section has a short label written
    for it; those render the rule and heading alone rather than being given an
    invented one.
    """
    top = (f'<p class="eyebrow"><span class="rule"></span>{eyebrow}</p>'
           if eyebrow else '<span class="rule"></span>')
    right = aside if aside is not None else (f'<p class="lead">{lead}</p>' if lead else '')
    return (f'<div class="section-head section-head--split">'
            f'<div>{top}<h2>{title}</h2></div>{right}</div>')


def report_book(lang, rep):
    """The latest annual report, as the supplied cover mockup.

    Decorative: the report itself is a page, linked beside this, so the figure
    is hidden from assistive technology and the link carries the meaning.
    """
    return (f'<div class="bookshot" aria-hidden="true" data-reveal>'
            f'{img("annual-report-book", lang, "(max-width: 920px) 76vw, 34vw")}'
            f'</div>')

def governorate_map(govs, lang):
    """HDIP at the centre, a ring of governorates around it.

    A true ring needs a roughly square area, which the two-column layout of
    this section provides; the earlier wide, short band did not, which is why
    it used a fan. Positions are percentages of the box, and the SVG uses a
    0-100 viewBox with preserveAspectRatio="none" so the two coordinate
    systems agree at every width; non-scaling-stroke keeps the lines an even
    weight despite the non-uniform scale.

    The names are real text in document order, so the section reads the same
    to a screen reader as a plain list would; the spokes are decorative and
    hidden from the accessibility tree. Below 760px the ring collapses to a
    wrapped row and the SVG is dropped.
    """
    n = len(govs)
    cx = cy = 50.0
    rx = ry = 35.5
    nodes, lines = [], []
    for i, (g, g_en) in enumerate(zip(govs, C.GOVERNORATES)):
        # Start at the top and go round, mirrored for RTL so the ring turns
        # with the language.
        a = -math.pi / 2 + (-1 if lang == "ar" else 1) * (2 * math.pi * i / n)
        x = cx + rx * math.cos(a)
        y = cy + ry * math.sin(a)
        geom = (f'x1="{cx}" y1="{cy}" x2="{x:.2f}" y2="{y:.2f}" pathLength="1" '
                f'vector-effect="non-scaling-stroke" style="--i:{i}"')
        lines.append(f'<line class="netmap__link" {geom}></line>'
                     f'<line class="netmap__pulse" {geom}></line>')

        slug = GOV_PHOTO.get(g_en)
        if slug:
            face = f'<span class="netmap__disc">{plain(slug, lang, "1x1", sizes="120px")}</span>'
        else:
            face = (f'<span class="netmap__disc netmap__disc--mark" aria-hidden="true">'
                    f'{icon("pin")}</span>')
        nodes.append(
            f'<li class="netmap__node" style="--x:{x:.2f}%;--y:{y:.2f}%;--i:{i}">'
            f'{face}<span class="netmap__name">{g}</span></li>'
        )
    return (
        f'<div class="netmap" data-netmap data-reveal>'
        f'<svg class="netmap__web" viewBox="0 0 100 100" preserveAspectRatio="none" '
        f'aria-hidden="true" focusable="false">{"".join(lines)}</svg>'
        f'<span class="netmap__hub" aria-hidden="true">'
        f'<img src="{"../" if lang == "ar" else ""}assets/img/logo-320.png'
        f'?v={asset_hash("assets/img/logo-320.png")}" alt="" '
        f'width="1027" height="473" decoding="async"></span>'
        f'<ul class="netmap__nodes">{"".join(nodes)}</ul>'
        f'</div>'
    )


def hero_slides(lang):
    """Slides + controls for the full-section hero stage. Slide one ships
    visible and the control row is revealed by script, so the hero survives
    with no JavaScript."""
    ui = Y.SLIDESHOW_UI[lang]
    total = len(Y.HERO_SLIDES)
    slides, dots = "", ""
    for i, slug in enumerate(Y.HERO_SLIDES):
        on = " is-on" if i == 0 else ""
        slides += f"""          <figure class="slide{on}" data-slide="{i}"{'' if i == 0 else ' aria-hidden="true"'}>
            {img(slug, lang, "100vw", eager=(i == 0))}
            <figcaption class="hero__credit"><b>{caption(slug, lang)}</b>
              <span class="credit">{credit(slug, lang)}</span></figcaption>
          </figure>
"""
        dots += (f'<button class="dot{on}" type="button" data-goto="{i}" '
                 f'aria-label="{ui["slide"].format(n=i + 1, total=total)}" '
                 f'aria-current="{str(i == 0).lower()}"></button>')
    controls = f"""      <div class="slideshow__ui" hidden>
        <button class="slideshow__toggle" type="button" data-toggle
                aria-label="{ui['pause']}" data-label-pause="{ui['pause']}"
                data-label-play="{ui['play']}">
          <span class="slideshow__bar"></span>
        </button>
        <div class="slideshow__dots" role="group" aria-label="{ui['choose']}">{dots}</div>
      </div>
      <div class="slideshow__nav">
        <button class="snav" type="button" data-prev aria-label="{ui['prev']}">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
               stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg>
        </button>
        <button class="snav" type="button" data-next aria-label="{ui['next']}">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
               stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>
        </button>
      </div>
"""
    return slides, controls, ui["label"]


def build_home(lang):
    u, h = C.UI[lang], C.HOME[lang]
    slides_html, controls_html, slides_label = hero_slides(lang)
    facts = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in h["who_facts"])
    tabs = "".join(
        f'<button class="yrtab{" is-on" if y == "2025" else ""}" type="button" role="tab" '
        f'id="yr-tab-{y}" aria-controls="yr-panel-{y}" '
        f'aria-selected="{str(y == "2025").lower()}" tabindex="{0 if y == "2025" else -1}" '
        f'data-year-tab="{y}">{y}</button>'
        for y in Y.YEARS)
    panels = "".join(
        f'<div class="yrpanel{" is-on" if y == "2025" else ""}" id="yr-panel-{y}" '
        f'role="tabpanel" aria-labelledby="yr-tab-{y}" data-year-panel="{y}">'
        + "".join(f'<div class="stat"><span class="stat__num" data-count>{i["num"]}</span>'
                  f'<span class="stat__label">{i["ar" if lang == "ar" else "en"]}</span></div>'
                  for i in Y.IMPACT[y]) + "</div>"
        for y in Y.YEARS)
    area_cards = "".join(f"""          <a class="card card--photo" href="area-{a['slug']}.html">
            <span class="card__icon">{icon(a['icon'])}</span>
            {plain(a['photo'], lang, "3x2")}
            <span class="card__body"><h3>{a[lang]['name']}</h3><p>{a[lang]['purpose']}</p>
            <span class="card__foot"><span class="link-arrow">{u['explore']}</span></span></span>
          </a>""" for a in C.AREAS)
    proj_cards = "".join(f"""          <a class="card card--photo" href="project-{p['slug']}.html">
            <span class="card__index">{p['years']}</span>
            {plain(p['photo'], lang, "3x2")}
            <span class="card__body"><h3>{p[lang]['name']}</h3><p>{p[lang]['tagline']}</p>
            <span class="card__foot"><span class="link-arrow">{u['explore']}</span></span></span>
          </a>""" for p in C.PROJECTS)
    govs = C.GOVERNORATES_AR if lang == "ar" else C.GOVERNORATES
    gov_map = governorate_map(govs, lang)
    news_items = "".join(f"""          <a class="news__item" href="news-{n['slug']}.html">
            <span class="news__date">{n[lang]['date']}</span>
            <span class="news__thumb">{img(n['photo'], lang, "140px")}</span>
            <span class="news__body"><h3>{n[lang]['title']}</h3><p>{n[lang]['summary']}</p></span>
            <span class="news__tag">{n[lang]['tag']}</span>
          </a>""" for n in ALL_NEWS[:3])
    rep = ALL_REPORTS['2025'][lang]

    return f"""    <section class="hero hero--full" data-slideshow
             aria-roledescription="carousel" aria-label="{slides_label}">
      <div class="hero__slides">
{slides_html}      </div>
      <div class="wrap hero__overlay">
        <p class="hero__badge"><b>{h['hero_badge']}</b> {u['org']}</p>
        <h1 class="hero__title">{h['hero_title']}</h1>
        <p class="lead measure">{h['hero_lead']}</p>
        <div class="hero__actions">
          <a class="btn btn--light" href="work.html">{C.NAV[lang][1][1]} {ARROW}</a>
          <a class="btn btn--outline" href="contact.html">{u['partner']}</a>
        </div>
      </div>
{controls_html}      <span class="hero__cue" aria-hidden="true"></span>
    </section>
    </section>

    <section class="section">
      <div class="wrap where where--who">
        <div class="where__intro">
          <p class="eyebrow"><span class="rule"></span>{h['who_eyebrow']}</p>
          <h2>{h['who_title']}</h2>
          <p class="lead">{h['who_short']}</p>
          <ul class="facts">{facts}</ul>
          <p style="margin-top:26px"><a class="link-arrow" href="about.html">{C.NAV[lang][0][1]}</a></p>
        </div>
        {founding_mark(lang, h)}
      </div>
    </section>

    <section class="section section--ink section--impact">
      <span class="stitchfield" aria-hidden="true"
            style="--px:86%;--py:14%;--pw:38%;--ph:50%"></span>
      <span class="stitchfield stitchfield--dots" aria-hidden="true"
            style="--px:12%;--py:90%;--pw:30%;--ph:42%;--stitch-op:.45"></span>
      <div class="wrap where where--impact">
        <div class="where__intro">
          <p class="eyebrow"><span class="rule"></span>{h['impact_eyebrow']}</p>
          <h2>{h['impact_title']}</h2>
          <p class="lead">{h['impact_lead']}</p>
          <p><a class="btn btn--outline" href="reports.html">{C.NAV[lang][3][1]} {ARROW}</a></p>
        </div>
        <div class="stitchnum" aria-hidden="true" data-reveal>
          <span class="stitchnum__fig">{len(Y.YEARS)}</span>
          <span class="stitchnum__label">{u['years_label']}</span>
        </div>
      </div>
      <div class="wrap">
        <div class="yrswitch" role="tablist" aria-label="{u['year_switch']}">{tabs}</div>
        <div class="yrpanels stats" data-reveal>{panels}</div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        {section_head(h['areas_title'], h['areas_eyebrow'], h['areas_lead'])}
        <div class="grid grid--3" data-stagger data-reveal>
{area_cards}
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap">
        {section_head(h['projects_title'], h['projects_eyebrow'], h['projects_lead'])}
        <div class="grid grid--4" data-stagger data-reveal>
{proj_cards}
        </div>
      </div>
    </section>

    <section class="band band--light">
      <div class="band__bg" aria-hidden="true">{CROWD_FIELD}</div>
      <div class="wrap where">
        <div class="where__intro">
          <p class="eyebrow"><span class="rule"></span>{h['where_eyebrow']}</p>
          <h2 class="figure-head">
            <span class="figure-head__num">{len(C.GOVERNORATES)}</span>
            <span class="figure-head__label">{u['governorates']}</span>
          </h2>
          <p class="lead">{h['where_lead']}</p>
          <p><a class="link-arrow" href="work.html">{u['explore']}</a></p>
        </div>
        {gov_map}
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        {section_head(h['news_title'], h['news_eyebrow'])}
        <div class="news" data-stagger data-reveal>
{news_items}
        </div>
        <p style="margin-top:30px"><a class="link-arrow" href="news.html">{u['all_news']}</a></p>
      </div>
    </section>

    <section class="section section--alt">
      <span class="stitchfield" aria-hidden="true"
            style="--px:94%;--py:52%;--pw:30%;--ph:60%"></span>
      <span class="stitchfield stitchfield--dots" aria-hidden="true"
            style="--px:3%;--py:100%;--pw:24%;--ph:34%"></span>
      <span class="stitchfield stitchfield--dots" aria-hidden="true"
            style="--px:74%;--py:4%;--pw:22%;--ph:34%;--stitch-op:.45"></span>
      <div class="wrap where where--reports">
        <div class="where__intro">
          <p class="eyebrow"><span class="rule"></span>{h['reports_eyebrow']}</p>
          <h2>{h['reports_title']}</h2>
          <p class="lead">{h['reports_lead']}</p>
          <div class="hero__actions">
            <a class="btn" href="report-2025.html">{rep['title']} {ARROW}</a>
            <a class="link-arrow" href="reports.html">{C.NAV[lang][3][1]}</a>
          </div>
        </div>
        {report_book(lang, rep)}
      </div>
    </section>

    <section class="section--tight" style="padding-bottom:clamp(72px,10vw,132px)">
      <div class="wrap">
        <div class="cta" data-reveal>
          <h2 class="measure center">{h['partner_title']}</h2>
          <p class="lead measure center" style="color:rgba(240,247,243,.8)">{h['partner_lead']}</p>
          <div class="hero__actions" style="justify-content:center">
            <a class="btn btn--light" href="contact.html">{u['contact']} {ARROW}</a>
          </div>
        </div>
      </div>
    </section>
"""


def build_about(lang):
    u, a = C.UI[lang], C.ABOUT[lang]
    who = "".join(f"<p>{p}</p>" for p in a["who"])
    objs = "".join(f'<li><span class="obj__n">{i:02d}</span><span>{o}</span></li>'
                   for i, o in enumerate(a["objectives"], 1))
    x = Y.ABOUT_EXTRA[lang]
    approach = "".join(f"<p>{p}</p>" for p in x["approach"])
    principles = "".join(f"<li>{p}</li>" for p in x["principles"])
    def _wd(t, d, slug):
        label = f'<a href="area-{slug}.html">{t}</a>' if slug else t
        return f"<li><b>{label}</b><span>{d}</span></li>"
    whatwedo = "".join(_wd(t, d, slug) for t, d, slug in x["whatwedo"])
    body = page_hero(lang, C.NAV[lang][0][1], a["title"], a["lead"], Y.HERO_PHOTOS["about"]) + f"""
    <section class="section" id="who">
      <div class="wrap split">
        <div class="prose"><h2>{a['who_title']}</h2>{who}</div>
        <div data-reveal>{figure('women-able-group', lang, "4x5", "(max-width: 900px) 100vw, 45vw")}</div>
      </div>
    </section>

    <section class="section section--alt" id="vision">
      <div class="wrap grid grid--2">
        <div class="card card--statement" data-reveal><h3>{a['vision_title']}</h3><p>{a['vision']}</p></div>
        <div class="card card--statement" data-reveal><h3>{a['mission_title']}</h3><p>{a['mission']}</p></div>
      </div>
    </section>

    <section class="section" id="objectives">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div><span class="rule"></span><h2>{a['objectives_title']}</h2></div>
          <p class="lead">{a['objectives_lead']}</p>
        </div>
        <ol class="objectives" data-reveal>{objs}</ol>
      </div>
    </section>

    <section class="section section--alt" id="what">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div><span class="rule"></span><h2>{x['whatwedo_title']}</h2></div>
          <p class="lead">{x['whatwedo_lead']}</p>
        </div>
        <ul class="deflist deflist--wide" data-reveal>{whatwedo}</ul>
      </div>
    </section>

    <section class="section" id="approach">
      <div class="wrap split">
        <div><h2>{x['approach_title']}</h2></div>
        <div class="prose">{approach}</div>
      </div>
    </section>

    <section class="section section--ink" id="partner">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div><span class="rule"></span><h2>{x['partner_title']}</h2></div>
          <p class="lead" style="color:rgba(244,237,228,.74)">{x['partner_lead']}</p>
        </div>
        <ol class="principles" data-reveal>{principles}</ol>
        <p class="lead measure" style="margin-top:38px;color:rgba(244,237,228,.74)">{x['partner_close']}</p>
        <p style="margin-top:26px"><a class="btn btn--light" href="contact.html">{u['contact']} {ARROW}</a></p>
      </div>
    </section>

{(f'''    <section class="section">
      <div class="wrap grid grid--3">
{needed(lang, a["team_title"])}
      </div>
    </section>
''') if DRAFT else ""}{ending(lang, "about")}"""
    return page(lang, "about.html", a["title"], a["lead"][:160], body, social=Y.HERO_PHOTOS["about"])


def build_work(lang):
    u = C.UI[lang]
    h = C.HOME[lang]
    cards = "".join(f"""          <a class="card card--photo" href="area-{a['slug']}.html">
            <span class="card__icon">{icon(a['icon'])}</span>
            {plain(a['photo'], lang, "3x2")}
            <span class="card__body"><h2>{a[lang]['name']}</h2><p>{a[lang]['purpose']}</p>
            <span class="card__foot"><span class="link-arrow">{u['explore']}</span></span></span>
          </a>""" for a in C.AREAS)
    body = page_hero(lang, C.NAV[lang][1][1], h["areas_title"], h["areas_lead"], Y.HERO_PHOTOS["work"]) + f"""
    <section class="section"><div class="wrap"><div class="grid grid--3">
{cards}
    </div></div></section>
{ending(lang, "area")}"""
    return page(lang, "work.html", h["areas_title"], h["areas_lead"][:160], body,
                current="work.html", social=Y.HERO_PHOTOS["work"])


def build_area(lang, a):
    u, d = C.UI[lang], a[lang]
    what = "".join(f'<li><b>{t}</b><span>{x}</span></li>' for t, x in d["what"])
    figs = "".join(f'<div class="stat"><span class="stat__num">{n}</span>'
                   f'<span class="stat__label">{l}</span></div>' for n, l in d["figures"])
    rel_p = [p for p in C.PROJECTS if p["area"] == a["slug"]]
    rel_n = [n for n in ALL_NEWS if n["area"] == a["slug"]][:3]
    proj_html = "".join(f"""          <a class="card card--photo" href="project-{p['slug']}.html">
            <span class="card__index">{p['years']}</span>{plain(p['photo'], lang, "3x2")}
            <span class="card__body"><h3>{p[lang]['name']}</h3><p>{p[lang]['tagline']}</p></span>
          </a>""" for p in rel_p)
    news_html = "".join(f"""          <a class="news__item" href="news-{n['slug']}.html">
            <span class="news__date">{n[lang]['date']}</span>
            <span class="news__thumb">{img(n['photo'], lang, "140px")}</span>
            <span class="news__body"><h3>{n[lang]['title']}</h3><p>{n[lang]['summary']}</p></span>
            <span class="news__tag">{n[lang]['tag']}</span></a>""" for n in rel_n)
    extra = ""
    if a["slug"] == "research":
        L = Y.LIBRARIES[lang]
        lib_fig = "".join(f'<div class="stat"><span class="stat__num">{n}</span>'
                          f'<span class="stat__label">{l}</span></div>' for n, l in L["figures"])
        lib_body = "".join(f"<p>{x}</p>" for x in L["body"])
        lib_fac = "".join(f"<li>{x}</li>" for x in L["facilities"])
        lib_srv = "".join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in L["services"])
        lib_wk = "".join(f"<li>{x}</li>" for x in L["workshops"])
        extra = f"""    <section class="section" id="libraries">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div><span class="rule"></span><h2>{L['title']} <span class="yr-tag">2022</span></h2></div>
          <p class="lead">{L['lead']}</p>
        </div>
        <div class="stats" data-reveal style="margin-bottom:clamp(36px,4vw,56px)">{lib_fig}</div>
        <div class="split">
          <div class="prose">{lib_body}
            <h3>{L['facilities_title']}</h3><ul class="checklist">{lib_fac}</ul>
          </div>
          <div>
            <h3>{L['services_title']}</h3>
            <ul class="deflist" data-reveal>{lib_srv}</ul>
          </div>
        </div>
        <h3 style="margin-top:clamp(40px,5vw,60px)">{L['workshops_title']}</h3>
        <ul class="checklist checklist--two" data-reveal>{lib_wk}</ul>
      </div>
    </section>
"""
    hero = Y.HERO_PHOTOS.get(f"area-{a['slug']}", a["photo"])
    body = page_hero(lang, (C.NAV[lang][1][1], d["name"]), d["name"], d["purpose"],
                     hero, crumb_href="work.html") + f"""
    <section class="section">
      <div class="wrap split">
        <div><h2>{d['what_title']}</h2>
          <p class="lead">{d['overview']}</p></div>
        <ul class="deflist" data-reveal>{what}</ul>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>2024</h2></div>
        <div class="stats" data-reveal>{figs}</div>
      </div>
    </section>
{extra}
""" + (f"""    <section class="section">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{C.NAV[lang][2][1]}</h2></div>
        <div class="grid grid--3">
{proj_html}
        </div>
      </div>
    </section>
""" if rel_p else "") + (f"""    <section class="section section--alt">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{C.HOME[lang]['news_title']}</h2></div>
        <div class="news">
{news_html}
        </div>
      </div>
    </section>
""" if rel_n else "") + ending(lang, "area")
    return page(lang, f"area-{a['slug']}.html", d["name"], d["purpose"][:160], body,
                current="work.html", social=hero)


def build_projects(lang):
    u, h = C.UI[lang], C.HOME[lang]
    cards = "".join(f"""          <a class="card card--photo" href="project-{p['slug']}.html">
            <span class="card__index">{p['years']}</span>{plain(p['photo'], lang, "3x2")}
            <span class="card__body"><h2>{p[lang]['name']}</h2><p>{p[lang]['tagline']}</p>
            <span class="card__foot"><span class="status status--{p['status']}">{u[p['status']]}</span></span>
            </span></a>""" for p in C.PROJECTS)
    body = page_hero(lang, C.NAV[lang][2][1], h["projects_title"], h["projects_lead"], Y.HERO_PHOTOS["projects"]) + f"""
    <section class="section"><div class="wrap"><div class="grid grid--2">
{cards}
    </div></div></section>
{ending(lang, "project")}"""
    return page(lang, "projects.html", h["projects_title"], h["projects_lead"][:160], body,
                current="projects.html", social=Y.HERO_PHOTOS["projects"])


def build_project(lang, p):
    u, d = C.UI[lang], p[lang]
    area = next(a for a in C.AREAS if a["slug"] == p["area"])
    glance = "".join(f'<li><b>{k}</b><span>{v}</span></li>' for k, v in d["glance"])
    objs = "".join(f"<li>{o}</li>" for o in d["objectives"])
    comps = "".join(f'<li><b>{t}</b><span>{x}</span></li>' for t, x in d["components"])
    res = "".join(f"<li>{r}</li>" for r in d["results"])
    table = ""
    if d.get("table"):
        head = "".join(f"<th>{c}</th>" for c in d["table_head"])
        rows = "".join("<tr>" + "".join(
            f'<td{" class=\"is-total\"" if r[0] in ("Total", "المجموع الكلي") else ""}>{c}</td>'
            for c in r) + "</tr>" for r in d["table"])
        table = f"""    <section class="section section--alt">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>2024</h2></div>
        <div class="table-wrap" data-reveal tabindex="0" role="region"
             aria-label="{d['name']} — {u['results']} 2024">
          <table class="data"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>
        </div>
      </div>
    </section>
"""
    partner_row = (f'<li><b>{u["partner_label"]}</b><span>{p["partner"]}</span></li>' if p["partner"] else "")
    # Results by year — the phase tabs in the approved project template
    phases_html = ""
    ph = dict(Y.PHASES.get(p["slug"], {}))
    head24 = {"en": "Results reported for 2024.", "ar": "النتائج كما وردت لعام 2024."}[lang]
    ph["2024"] = {lang: dict(headline=head24, notes=[], results=d["results"])}
    if ph:
        years = sorted(ph.keys(), reverse=True)
        tabs = "".join(
            f'<button class="yrtab{" is-on" if i == 0 else ""}" type="button" role="tab" '
            f'id="ph-tab-{yr}" aria-controls="ph-panel-{yr}" '
            f'aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}" '
            f'data-phase-tab="{yr}">{yr}</button>'
            for i, yr in enumerate(years))
        panes = ""
        for i, yr in enumerate(years):
            d2 = ph[yr][lang]
            notes = "".join(f"<p>{n}</p>" for n in d2["notes"])
            rs = "".join(f"<li>{r}</li>" for r in d2["results"])
            panes += (f'<div class="yrpanel{" is-on" if i == 0 else ""}" id="ph-panel-{yr}" '
                      f'role="tabpanel" aria-labelledby="ph-tab-{yr}" data-phase-panel="{yr}">'
                      f'<h3>{d2["headline"]}</h3><div class="prose">{notes}</div>'
                      f'<ul class="checklist">{rs}</ul></div>')
        phases_html = f"""    <section class="section section--alt">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div><span class="rule"></span><h2>{u['results']} · {' / '.join(years)}</h2></div>
          <div class="yrswitch" role="tablist" aria-label="{u['year_switch']}">{tabs}</div>
        </div>
        <div class="yrpanels">{panes}</div>
      </div>
    </section>
"""
    closures = ""
    if p["slug"] == "right-to-education":
        cn = Y.CLOSURES_NOTE[lang]
        closures = f"""    <section class="section">
      <div class="wrap split">
        <div>
          <h2>{cn['title']}</h2>
          <p class="lead">{cn['body']}</p>
        </div>
        <div data-reveal>
          <figure class="media media--true media--3x2">
            {img('closures-map', lang, "(max-width: 900px) 100vw, 50vw")}
            <figcaption class="media__cap"><b>{caption('closures-map', lang)}</b>
              <span class="credit">{credit('closures-map', lang)}</span></figcaption>
          </figure>
        </div>
      </div>
    </section>
"""
    gap = ""
    if DRAFT and p["slug"] == "women-able" and lang == "en":
        gap = f"""    <section class="section--tight"><div class="wrap">
{needed(lang, "English source text", "The 2024 phase on this page is translated from the Arabic document: the English half of the 2024 file contains Right to Education text instead of this project. The 2025 phase has its own English source.")}
    </div></section>
"""
    hero = Y.HERO_PHOTOS.get(f"project-{p['slug']}", p["photo"])
    body = page_hero(lang, (C.NAV[lang][2][1], d["name"]), d["name"], d["tagline"],
                     hero, crumb_href="projects.html") + f"""
    <section class="section">
      <div class="wrap split">
        <div>
          <h2>{u['at_a_glance']}</h2>
          <p class="lead">{d['about']}</p>
          <p style="margin-top:22px">
            <a class="link-arrow" href="area-{area['slug']}.html">{area[lang]['name']}</a></p>
        </div>
        <div class="hero__panel" data-reveal>
          <div class="panel__title"><h3>{u['at_a_glance']}</h3>
            <span class="status status--{p['status']}">{u[p['status']]} · {p['years']}</span></div>
          <ul class="info-list glance">{glance}{partner_row}</ul>
        </div>
      </div>
    </section>

{closures}
    <section class="section section--alt">
      <div class="wrap split">
        <div><h2>{u['objectives']}</h2></div>
        <ol class="numlist" data-reveal>{objs}</ol>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{u['activities']}</h2></div>
        <ul class="deflist deflist--wide" data-reveal>{comps}</ul>
        <div data-reveal style="margin-top:clamp(36px,4vw,56px)">{figure(p['photo'], lang, "16x9", "(max-width: 900px) 100vw, 70vw")}</div>
      </div>
    </section>
{table}
{phases_html}
{gap}
{ending(lang, "project")}"""
    return page(lang, f"project-{p['slug']}.html", d["name"], d["tagline"][:160], body,
                current="projects.html", social=hero)


def build_reports(lang):
    u = C.UI[lang]
    t = {"en": ("Annual reports", "Strategic directions, activities, outputs and recommendations, year by year."),
         "ar": ("التقارير السنوية", "التوجهات الاستراتيجية والأنشطة والمخرجات والتوصيات، عامًا بعد عام.")}[lang]
    cards = ""
    for yr in Y.YEARS:
        r = ALL_REPORTS[yr][lang]
        flag = ""
        if ALL_REPORTS[yr][lang].get("caveat"):
            flag = f'<span class="report-card__flag">{icon("alert")}</span>'
        cards += f"""          <a class="report-card" href="report-{yr}.html" data-reveal>
            {flag}<span class="report-card__year">{yr}</span>
            <h2>{r['title']}</h2><p>{r['lead']}</p>
            <span class="card__foot"><span class="link-arrow">{u['explore']}</span></span>
          </a>"""
    body = page_hero(lang, C.NAV[lang][3][1], t[0], t[1], Y.HERO_PHOTOS["reports"]) + f"""
    <section class="section"><div class="wrap">
      <div class="grid grid--4">
{cards}
      </div>
      <p class="form__note" style="margin-top:28px">{u['no_download']}</p>
    </div></section>
{ending(lang, "about")}"""
    return page(lang, "reports.html", t[0], t[1][:160], body, current="reports.html", social=Y.HERO_PHOTOS["reports"])


def build_report(lang, year):
    u, r = C.UI[lang], ALL_REPORTS[year][lang]
    summary = "".join(f"<p>{p}</p>" for p in r["summary"])
    pillars = "".join(f"""        <article class="pillar" data-reveal>
          <span class="pillar__n">{i:02d}</span>
          <div><h3>{t}</h3><p>{desc}</p>
          {('<ul class="checklist checklist--sm">' + "".join(f'<li>{o}</li>' for o in outs) + '</ul>') if outs else ''}</div>
        </article>""" for i, (t, desc, outs) in enumerate(r["pillars"], 1))
    outputs = "".join(f'<li><b>{t}</b><span>{x}</span></li>' for t, x in r["outputs"])
    recs = "".join(f'<li><b>{t}</b><span>{x}</span></li>' for t, x in r["recs"])
    impact = "".join(f'<div class="stat"><span class="stat__num">{i["num"]}</span>'
                     f'<span class="stat__label">{i["ar" if lang == "ar" else "en"]}</span></div>'
                     for i in Y.IMPACT[year])
    caveat = ""
    if r.get("caveat"):
        caveat = f"""    <section class="section--tight" style="padding-top:0"><div class="wrap">
        <p class="note note--warn" style="max-width:82ch">{icon('alert')}
          <span><b>{'About these figures. ' if lang == 'en' else 'حول هذه الأرقام. '}</b>{r['caveat']}</span></p>
    </div></section>
"""
    me = ""
    if r.get("me"):
        rows = "".join(f'<li><b>{t}</b><span>{x}</span></li>' for t, x in r["me"])
        me = f"""    <section class="section">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{r['me_title']}</h2></div>
        <ul class="deflist deflist--wide" data-reveal>{rows}</ul>
      </div>
    </section>
"""
    photo = Y.HERO_PHOTOS[f"report-{year}"]
    nav_years = "".join(
        f'<a class="yrtab{" is-on" if y == year else ""}" href="report-{y}.html">{y}</a>' for y in Y.YEARS)
    body = page_hero(lang, (C.NAV[lang][3][1], year), r["title"], r["lead"],
                     photo, crumb_href="reports.html") + f"""
    <section class="section--tight">
      <div class="wrap"><div class="yrswitch yrswitch--links">{nav_years}</div></div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="wrap split">
        <div class="prose"><h2>{r['summary_title']}</h2>{summary}</div>
        <div class="hero__panel" data-reveal>
          <div class="panel__title"><h3>{u['key_figures']}</h3><span>{year}</span></div>
          <ul class="info-list glance">{''.join(
              f'<li><b>{i["num"]}</b><span>{i["ar" if lang == "ar" else "en"]}</span></li>'
              for i in Y.IMPACT[year])}</ul>
          <p class="form__note" style="margin-top:18px">{u['no_download']}</p>
        </div>
      </div>
    </section>
{caveat}
    <section class="section section--alt">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{r['pillars_title']}</h2></div>
        <div class="pillars">
{pillars}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{r['outputs_title']}</h2></div>
        <ul class="deflist deflist--num" data-reveal>{outputs}</ul>
      </div>
    </section>
{me}
    <section class="section section--ink">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{r['recs_title']}</h2></div>
        <ul class="deflist deflist--num deflist--light" data-reveal>{recs}</ul>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{year}</h2></div>
        <div class="stats" data-reveal>{impact}</div>
      </div>
    </section>
{ending(lang, "report", "reports.html")}"""
    return page(lang, f"report-{year}.html", r["title"], r["lead"][:160], body,
                current="reports.html", social=photo)


def build_news_index(lang):
    u = C.UI[lang]
    t = {"en": ("News & stories", "Single activities and events drawn from HDIP's 2024 reporting."),
         "ar": ("أخبار وقصص", "أنشطة وفعاليات مفردة مستخلصة من تقارير البرنامج لعام 2024.")}[lang]
    items = "".join(f"""          <a class="news__item" href="news-{n['slug']}.html">
            <span class="news__date">{n[lang]['date']}</span>
            <span class="news__thumb">{img(n['photo'], lang, "140px")}</span>
            <span class="news__body"><h2>{n[lang]['title']}</h2><p>{n[lang]['summary']}</p></span>
            <span class="news__tag">{n[lang]['tag']}</span></a>""" for n in ALL_NEWS)
    body = page_hero(lang, C.NAV[lang][4][1], t[0], t[1], Y.HERO_PHOTOS["news"]) + f"""
    <section class="section"><div class="wrap"><div class="news">
{items}
    </div></div></section>
{ending(lang, "about")}"""
    return page(lang, "news.html", t[0], t[1][:160], body, current="news.html", social=Y.HERO_PHOTOS["news"])


def build_article(lang, n):
    u, d = C.UI[lang], n[lang]
    area = next(a for a in C.AREAS if a["slug"] == n["area"])
    body_html = "".join(f"<p>{p}</p>" for p in d["body"])
    others = [x for x in ALL_NEWS if x["slug"] != n["slug"]][:3]
    rel = "".join(f"""          <a class="news__item" href="news-{x['slug']}.html">
            <span class="news__date">{x[lang]['date']}</span>
            <span class="news__thumb">{img(x['photo'], lang, "140px")}</span>
            <span class="news__body"><h3>{x[lang]['title']}</h3></span>
            <span class="news__tag">{x[lang]['tag']}</span></a>""" for x in others)
    proj_link = ""
    if n["project"]:
        p = next(x for x in C.PROJECTS if x["slug"] == n["project"])
        proj_link = f'<a class="tag-link" href="project-{p["slug"]}.html">{p[lang]["name"]}</a>'
    body = f"""    <section class="page-hero page-hero--media">
      <div class="page-hero__bg">{img(n['photo'], lang, "100vw", eager=True)}</div>
      <div class="wrap page-hero__content">
        <p class="crumbs"><a href="index.html">{u['home']}</a><span>/</span>
          <a href="news.html">{C.NAV[lang][4][1]}</a><span>/</span>{d['date']}</p>
        <h1 class="article-title">{d['title']}</h1>
        <p class="tag-row"><a class="tag-link" href="area-{area['slug']}.html">{area[lang]['name']}</a>{proj_link}</p>
      </div>
      <p class="page-hero__credit">{caption(n['photo'], lang)} — {credit(n['photo'], lang)}</p>
    </section>

    <section class="section">
      <div class="wrap article">
        <p class="lead">{d['summary']}</p>
        <div class="prose">{body_html}</div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap">
        <div class="section-head"><span class="rule"></span><h2>{C.HOME[lang]['news_title']}</h2></div>
        <div class="news">
{rel}
        </div>
      </div>
    </section>
{ending(lang, "news", "news.html")}"""
    return page(lang, f"news-{n['slug']}.html", d["title"], d["summary"][:160], body,
                current="news.html", social=n["photo"])


def build_contact(lang):
    u, c = C.UI[lang], C.CONTACT[lang]
    rows = ""
    for ic, en_l, ar_l, en_v, ar_v, href in C.CONTACT_FIELDS:
        label = ar_l if lang == "ar" else en_l
        val = ar_v if lang == "ar" else en_v
        val = f'<a href="{href}">{val}</a>' if href else val
        rows += f'<li>{icon(ic)}<span><b>{label}</b>{val}</span></li>'
    partners = "".join(f'<li>{icon("flag")}<span><b>{a}</b>{b}</span></li>' for a, b in c["partners"])
    body = page_hero(lang, u["contact"], c["title"], c["lead"], Y.HERO_PHOTOS["contact"]) + f"""
    <section class="section">
      <div class="wrap contact-grid">
        <div>
          <h2>{u['org_short'].upper()}</h2>
          <ul class="info-list">{rows}</ul>
          <p class="note note--warn">{icon('alert')} {c['unverified']}</p>

          <h3 style="margin-top:46px">{c['partners_title']}</h3>
          <p>{c['partners_lead']}</p>
          <ul class="info-list">{partners}</ul>
        </div>
        <div>
          <div class="hero__panel">
            <div class="panel__title"><h3>{c['direct_title']}</h3><span>{u['partner']}</span></div>
            <p class="lead" style="font-size:1rem">{c['direct_lead']}</p>
            <div class="hero__actions" style="margin-top:26px">
              <a class="btn" href="mailto:hdip@hdip.org">{c['email_cta']} {ARROW}</a>
              <a class="btn btn--ghost" href="tel:+97222985372">{c['call_cta']}</a>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
    return page(lang, "contact.html", c["title"], c["lead"][:160], body,
                current="contact.html", social=Y.HERO_PHOTOS["contact"])


def build_credits(lang):
    u = C.UI[lang]
    t = {"en": ("Photography & credits",
                "Programme photographs supplied by HDIP, plus freely-licensed contextual images."),
         "ar": ("الصور والمصادر", "صور برامجية من البرنامج، إضافة إلى صور سياقية بترخيص حر.")}[lang]
    hdip_rows = "".join(f"""          <li>{plain(s, lang, "3x2", "112px")}
            <span><b>{caption(s, lang)}</b><span>{HDIP_PHOTOS[s]['source']}</span></span>
            <span class="lic-tag">© HDIP</span></li>""" for s in HDIP_PHOTOS)
    # Every freely-licensed photograph on the site, not a hand-kept subset:
    # CC BY and CC BY-SA both require attribution wherever the image is used,
    # so this list has to follow what is actually in credits.json.
    cc_rows = "".join(f"""          <li>{plain(s, lang, "3x2", "112px")}
            <span><b>{CC_PHOTOS[s]['title']}</b><span>{credit(s, lang)}</span></span>
            <span class="lic-tag">{CC_PHOTOS[s]['license']}</span></li>"""
                      for s in CC_PHOTOS if s in MANIFEST)
    srcs = "".join(f"<li><code>{k}</code> — {v}</li>"
                   for k, v in {**C.SOURCES, **Y.SOURCES_EXTRA}.items())
    gaps = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in Y.GAPS_REMAINING[lang])
    art_rows = "".join(f"""          <li>{plain(k, lang, "3x2", "112px")}
            <span><b>{v[lang]}</b><span>{v['source']}</span></span>
            <span class="lic-tag">{'Artwork' if lang == 'en' else 'رسم'}</span></li>"""
                       for k, v in SUPPLIED_ART.items() if k in MANIFEST)
    h = {"en": ("HDIP programme photography", "Contextual photography", "Document sources",
                "Content still needed", "Artwork"),
         "ar": ("صور برامج البرنامج", "صور سياقية", "المستندات المصدرية",
                "محتوى ما زال مطلوبًا", "الرسوم")}[lang]
    body = page_hero(lang, u["credits"], t[0], t[1], Y.HERO_PHOTOS["credits"]) + f"""
    <section class="section"><div class="wrap">
      <h2>{h[0]}</h2>
      <ul class="credits-list">{hdip_rows}</ul>
      <h2 style="margin-top:56px">{h[1]}</h2>
      <ul class="credits-list">{cc_rows}</ul>
      <h2 style="margin-top:56px">{h[4]}</h2>
      <ul class="credits-list">{art_rows}</ul>
      <h2 style="margin-top:56px">{h[2]}</h2>
      <ul class="srclist">{srcs}</ul>
      <h2 style="margin-top:56px">{h[3]}</h2>
      <ul class="deflist">{gaps}</ul>
    </div></section>
"""
    return page(lang, "credits.html", t[0], t[1][:160], body)


# --------------------------------------------------------------------------
def main():
    global CSS_V
    CSS_V = asset_hash("assets/css/style.css")
    written = []
    for lang in LANGS:
        u = C.UI[lang]
        written.append(page(lang, "index.html", u["org"],
                            C.HOME[lang]["hero_lead"][:170], build_home(lang),
                            current="index.html", social="conference-hall"))
        written.append(build_about(lang))
        written.append(build_work(lang))
        for a in C.AREAS:
            written.append(build_area(lang, a))
        written.append(build_projects(lang))
        for p in C.PROJECTS:
            written.append(build_project(lang, p))
        written.append(build_reports(lang))
        for yr in Y.YEARS:
            written.append(build_report(lang, yr))
        written.append(build_news_index(lang))
        for n in ALL_NEWS:
            written.append(build_article(lang, n))
        written.append(build_contact(lang))
        written.append(build_credits(lang))
    for w in written:
        print("wrote", w)
    print(f"\n{len(written)} pages ({len(written)//2} per language)")


if __name__ == "__main__":
    main()
