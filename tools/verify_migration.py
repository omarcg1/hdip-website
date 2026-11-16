"""Byte-compare the generated site against a snapshot.

The whole point of the content migration was that it change nothing. This
rebuilds and compares every page's SHA-256 against a baseline taken before the
switch, so "identical" is a measurement, not a claim.

  python3 tools/verify_migration.py --snapshot   # before a change
  python3 tools/verify_migration.py              # after: compare
"""
import hashlib, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "/tmp/hdip-before/hashes.json"


def hashes():
    pages = [f for f in os.listdir(ROOT) if f.endswith(".html")]
    pages += ["ar/" + f for f in os.listdir(os.path.join(ROOT, "ar"))
              if f.endswith(".html")]
    return {p: hashlib.sha256(open(os.path.join(ROOT, p), "rb").read()).hexdigest()
            for p in sorted(pages)}


def main():
    if "--snapshot" in sys.argv:
        os.makedirs(os.path.dirname(BASE), exist_ok=True)
        json.dump(hashes(), open(BASE, "w"), indent=1)
        print(f"snapshot: {len(hashes())} pages")
        return 0

    subprocess.run([sys.executable, "build.py"], cwd=ROOT,
                   check=True, capture_output=True)
    before = json.load(open(BASE))
    after = hashes()

    missing = sorted(set(before) - set(after))
    added = sorted(set(after) - set(before))
    changed = sorted(p for p in set(before) & set(after) if before[p] != after[p])

    print(f"pages before {len(before)} | after {len(after)}")
    print(f"identical {len(set(before) & set(after)) - len(changed)}"
          f" | changed {len(changed)} | missing {len(missing)} | new {len(added)}")
    for label, items in (("changed", changed), ("missing", missing), ("new", added)):
        for p in items[:12]:
            print(f"  {label}: {p}")
    return 0 if not (changed or missing or added) else 1


if __name__ == "__main__":
    sys.exit(main())
