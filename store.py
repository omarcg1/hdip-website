"""The content store.

All site copy, figures, photo assignments and slideshow order live in
data/site.json, which the dashboard writes. content.py and content_years.py
expose that JSON under the names the templates already use, so build.py is
unchanged: `import content as C` still gives C.HOME, C.PROJECTS and the rest.

Read fresh on each call rather than cached, so a build immediately after a
save in the dashboard sees the save.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(ROOT, "data", "site.json")


def load():
    with open(STORE, encoding="utf-8") as f:
        return json.load(f)


def save(store):
    """Write atomically — a half-written store would break every build."""
    tmp = STORE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=1)
    os.replace(tmp, STORE)


def section(name):
    return load()[name]
