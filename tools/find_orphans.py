"""Find store fields that no page renders.

A control panel that offers fields which do nothing is worse than one that
offers fewer: the editor changes something, publishes, and sees no effect.

Method: build, then look for each leaf's text in the generated HTML. A value
that appears nowhere is almost certainly unreferenced. Short values are
skipped — a 3-character string matching somewhere proves nothing either way —
and so are image slugs, which reach the page as filenames rather than text.
"""
import html as H
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_LEN = 12


def leaves(v, p=""):
    if isinstance(v, dict):
        for k, x in v.items():
            yield from leaves(x, f"{p}.{k}" if p else k)
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from leaves(x, f"{p}[{i}]")
    elif isinstance(v, str):
        yield p, v


def main():
    subprocess.run([sys.executable, "build.py"], cwd=ROOT, check=True,
                   capture_output=True)
    blob = []
    for d, _, fs in os.walk(ROOT):
        if any(part in d for part in (".git", "tools", "assets")):
            continue
        for f in fs:
            if f.endswith(".html"):
                blob.append(open(os.path.join(d, f), encoding="utf-8").read())
    pages = "\n".join(blob)

    store = json.load(open(os.path.join(ROOT, "data", "site.json"), encoding="utf-8"))
    manifest = json.load(open(os.path.join(ROOT, "assets", "img", "manifest.json"),
                              encoding="utf-8"))
    store.pop("_note", None)

    orphans = []
    checked = 0
    for path, val in leaves(store):
        if len(val) < MIN_LEN or val in manifest:
            continue
        checked += 1
        if val in pages or H.escape(val) in pages:
            continue
        # Templates wrap some values, so also try the text without markup.
        bare = re.sub(r"<[^>]+>", "", val)
        if bare and (bare in pages or H.escape(bare) in pages):
            continue
        orphans.append((path, val))

    print(f"checked {checked} values of {MIN_LEN}+ characters")
    print(f"not found in any page: {len(orphans)}\n")
    for path, val in orphans:
        print(f"  {path}")
        print(f"      {val[:88]}{'…' if len(val) > 88 else ''}")

    if "--write" in sys.argv:
        out = os.path.join(ROOT, "data", "unused.json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump({
                "_note": "Paths whose text appears on no generated page. The "
                         "dashboard marks these so nobody edits a field that "
                         "cannot show. Some are conditional rather than dead "
                         "(the DRAFT placeholders only render when build.py's "
                         "DRAFT is True), so treat this as a prompt to check, "
                         "not a delete list. Regenerate with "
                         "`python3 tools/find_orphans.py --write`.",
                "paths": [p for p, _ in orphans],
            }, f, ensure_ascii=False, indent=1)
        print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
