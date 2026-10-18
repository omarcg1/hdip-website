# HDIP website

A rebuild of the Health Development Information and Policy Institute site, following
**"HDIP Website — Site Structure for Approval" (29 Sep 2026)**.

Bilingual: English at the root, Arabic (RTL) under `/ar/`. 29 pages per language, covering 2022–2025.

## Run it

```bash
python3 -m http.server 4610 --directory .
```

## Structure

| Template | Pages |
| --- | --- |
| Home | `index.html` — 9 sections per the approved structure |
| About | `about.html` — who we are, vision, mission, 15 objectives, what we do |
| Programme areas | `work.html` + `area-{health,education,women,youth,research}.html` |
| Projects | `projects.html` + `project-{right-to-education,women-able,women-leaders,youth-leadership}.html` |
| Annual report | `reports.html` + `report-2022.html` … `report-2025.html` |
| News article | `news.html` + `news-*.html` (8 articles) |
| Contact | `contact.html` |
| Credits | `credits.html` — photography, document sources, outstanding gaps |

- `content.py` — organisation, areas, projects, 2024 report; `SOURCES`
- `content_years.py` — 2022 / 2023 / 2025 reports, project phases, libraries, `GAPS_REMAINING`
- `build.py` — templates and rendering
- `assets/css/style.css` — design system, components and RTL rules
- `assets/js/main.js` — nav, scroll reveals, counters

Rebuild after editing content or CSS:

```bash
python3 build.py
```

Pages embed `style.css?v=<md5>`, so a rebuild busts the browser cache.

## Content provenance

Every figure and paragraph comes from the 2024 documents HDIP supplied. Nothing is
invented. `content.py` records the source file for each, and `credits.html` renders
both the source list and the list of content still outstanding.

Programme photography is HDIP's own, extracted from the supplied `.docx` files. One
contextual Ramallah photograph from Wikimedia Commons is credited on `credits.html`.

## Data-quality note on 2023

The 2023 source document carries a note from its own translator saying the Arabic
original has number-formatting errors and the statistical tables should be verified
before publication. They are indeed inconsistent: the narrative and the statistical
annex disagree (23 vs 35 awareness sessions, 21 vs 43 school courses), and in two
cases the male and female sub-totals do not sum to the stated total. Only the overall
totals reconcile, so only those are published. The caveat is shown on the page.

## What is still outstanding

Rendered on the site as visible "content needed" blocks, and listed on `credits.html`:

- **Team & Board** — names, roles, photographs
- **Donors and partners** — no list or logos; only Friedrich-Ebert-Stiftung and Olof
  Palme International Center are identifiable, from banners in the 2024 photographs
- **Annual report PDFs** — none supplied, so report pages have no download
- **Contact details** — carried over from the earlier published site, unverified
- **Photography for 2022, 2023 and 2025** — only the 2024 batch included images
- **Per-phase donors** — which donor funded which project in which year
- **Online donations** — no decision recorded

## Design

The design was passed through the `impeccable` skill twice: a polish pass, then a
full `critique` (two isolated assessments — design review, and detector + browser
evidence — synthesised). Changes made: kicker/eyebrow labels removed throughout (the
heading carries its own weight), decorative 01/02/03 section numbers dropped while
genuinely sequential numbering was kept, contrast tokens corrected to pass 4.5:1,
an 11px floor applied to functional text, heading outline repaired so no level is
skipped, browser surfaces themed (selection, caret, scrollbars, focus ring,
tabular numerals), and `width` animation replaced with `transform` to stop layout
thrash. Retained against the detector's advice: the cream/brown palette, Fraunces
and Inter, and the single italic word in the hero — all committed brief decisions.


### What the critique changed

The detector's own findings turned out to be ~95% false positives: it composites
declared colour pairs without resolving paint order, photo layers or element
geometry, so it flagged white-on-ember text that does not exist while missing ten
genuine WCAG failures. Those ten were found by measuring real composited pixels:

- `.footer__bottom` 3.60:1 → **7.90:1** (it carries the email and phone)
- `.site-footer .brand__tag` 3.93:1 → **7.16:1**
- `.pillar__n` 1.60:1 → **4.20:1**
- breadcrumb trail and separator over photo heroes (3.9:1 / 2.5:1) and on light
  heroes (1.59:1) — both lightened
- form fields were the only controls with **no focus ring** (`outline: none` beat
  `:focus-visible` on specificity) — now ringed
- the focus ring itself failed on dark surfaces (1.92:1 on maroon) — dark contexts
  get a light ring
- tap targets: nav toggle 42×42 → 44×44, year tabs 40.7 → 47 tall, brand 36 → 44

**The RTL overlay bug is the one worth knowing about.** `.page-hero--media::after`
used `linear-gradient(100deg, …)` — a *physical* angle. In English the heading sits
on the 0.90-alpha end; in Arabic, which starts on the right, it sat on the
0.44-alpha end, dropping breadcrumb contrast from 5.39:1 to 2.38:1. Every
physically-angled wash is now mirrored under `[dir="rtl"]`.

### What the design review changed

- **All 18 photographs are now used** (11 were referenced zero times). No image
  heads more than two pages; it was four.
- **The closures map ships as the one untinted artefact** (`.media--true`, which
  existed in the CSS and had never been used) beside new copy on access —
  the most HDIP-specific object on the site.
- **Every page now ends on a call**, not a drop into the footer. `.cta` was used on
  1 page of 29; it is now on 27 (contact and credits excepted by design).
- **The contact form no longer destroys the message.** It warned *after*
  `form.reset()` had already wiped the field; the warning is now above the form and
  the text is preserved.
- **Internal "content needed" boxes no longer ship.** About closed by telling the
  public that HDIP had missed a deliverable. They are behind `DRAFT` in `build.py`
  (set it `True` while working); the full gap list stays on `credits.html`, and the
  2023 figures caveat — which is genuinely public-facing — is now an inline note.
- **Arabic pages no longer download Fraunces and Inter** only to override both to
  Almarai, and Arabic now has a real display/text contrast built from weight
  (800 headings against a 300 lead) rather than reading uniformly flat.
- Year switches became real tablists: `role="tab"`, `aria-selected`, roving
  tabindex and arrow-key navigation (mirrored for RTL). The data table is
  keyboard-reachable with `tabindex="0"` and an accessible name.
