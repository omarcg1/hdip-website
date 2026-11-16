"""One-time extraction: the Python content modules -> data/site.json.

Run once to seed the store from whatever the modules currently hold. It copies
values verbatim; it never rewrites, reformats or "improves" any text. After the
switch the JSON is the source of truth and this script is only history.

Tuples become JSON arrays. Nothing in build.py depends on tuple-ness — every
use unpacks or indexes, which works the same on a list — and the byte-compare
in tools/verify_migration.py is what actually proves that.
"""
import importlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def public_names(mod):
    out = {}
    for k in dir(mod):
        if k.startswith("_"):
            continue
        v = getattr(mod, k)
        if callable(v) or type(v).__name__ == "module":
            continue
        out[k] = v
    return out


def main():
    import content, content_years
    store = {
        "_note": "Edited through the dashboard (tools/dashboard.py). "
                 "Seeded verbatim from the original content modules.",
        "content": public_names(content),
        "years": public_names(content_years),
    }
    out = os.path.join(ROOT, "data", "site.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=1, sort_keys=False)
    n = sum(1 for _ in json.dumps(store, ensure_ascii=False))
    print(f"wrote {out}  ({n//1024} KB, "
          f"{len(store['content'])} + {len(store['years'])} top-level keys)")


if __name__ == "__main__":
    main()
