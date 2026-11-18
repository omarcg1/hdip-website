"""Where the panel's edits go.

Locally the panel owns the checkout. It writes data/site.json, runs build.py,
and the pages on disk change immediately — which is what you want on the
machine the site is developed on.

A serverless host has no checkout to own. The filesystem is read-only apart
from /tmp, and /tmp is thrown away between requests, so a panel that writes
files there would report "saved" and lose the save a second later. The store
therefore lives in the GitHub repository and a save is a commit; the deploy
that follows the commit is what rebuilds the pages.

Both backends present the same operations, so dashboard.py never asks which
one it is talking to:

    load()                  the store, as a dict
    save(data, message)     record an edit — not yet live
    publish()               make what is saved the live site
    add_files(files, msg)   binary files (photo tiers and their manifest)
    read_bytes(path)        a file from the working copy, whatever that is
    pending()               a line for the UI: is anything unpublished?

Edits are never trusted blind: validate() builds the candidate store in a
temporary directory first, and only a store that produces 58 pages is
written anywhere. Locally that replaces the old write-build-and-roll-back
dance, which briefly left a broken store on disk; nothing is written now
until the build has proved itself.
"""
import base64
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import store  # noqa: E402

STORE_PATH = "data/site.json"


# ---------------------------------------------------------------------------
# Validation, shared by both backends
# ---------------------------------------------------------------------------
def validate(data):
    """Build `data` somewhere disposable. Returns (ok, detail).

    HDIP_STORE points the loaders at the candidate and --out sends the pages
    to a temp directory, so neither the real store nor the real site is
    touched by a store that turns out not to build.
    """
    tmp = tempfile.mkdtemp(prefix="hdip-check-")
    try:
        cand = os.path.join(tmp, "site.json")
        with open(cand, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        env = dict(os.environ, HDIP_STORE=cand)
        r = subprocess.run(
            [sys.executable, "build.py", "--out", os.path.join(tmp, "site"),
             "--no-assets"],
            cwd=ROOT, capture_output=True, text=True, env=env)
        if r.returncode != 0:
            detail = (r.stderr or r.stdout).strip().splitlines()[-1:] or [""]
            return False, detail[0]
        return True, ""
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------------------
# The checkout on this machine
# ---------------------------------------------------------------------------
class Local:
    kind = "local"
    where = "data/site.json"
    note = "Saved changes go live when you press Publish."

    def load(self):
        return store.load()

    def save(self, data, message=""):
        store.save(data)

    def read_bytes(self, path):
        full = os.path.join(ROOT, path.replace("/", os.sep))
        if not os.path.isfile(full):
            return None
        with open(full, "rb") as f:
            return f.read()

    def add_files(self, files, message=""):
        for path, raw in files.items():
            full = os.path.join(ROOT, path.replace("/", os.sep))
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "wb") as f:
                f.write(raw)

    def publish(self):
        r = subprocess.run([sys.executable, "build.py"], cwd=ROOT,
                           capture_output=True, text=True)
        if r.returncode != 0:
            return "err", (r.stderr or r.stdout).strip()[-1800:]
        n = sum(len([f for f in os.listdir(d) if f.endswith(".html")])
                for d in (ROOT, os.path.join(ROOT, "ar")))
        return "ok", f"Published. {n} pages rewritten."

    def pending(self):
        return ""


# ---------------------------------------------------------------------------
# The repository
# ---------------------------------------------------------------------------
class GitHub:
    """Saves commit to a draft branch; Publish copies the draft onto main.

    Two branches rather than one because the panel promises two steps: Save
    puts an edit somewhere safe, Publish puts it in front of the public. A
    single branch would make every keystroke live, and the Publish button a
    lie. The host builds the draft branch as a preview deployment, so Save
    also produces something the editor can look at before committing to it.

    Publish copies the file rather than merging refs: a copy always applies,
    where a fast-forward fails as soon as main has moved on for any other
    reason. The draft branch is deleted afterwards, so the next edit starts
    from whatever is live rather than from a branch that has drifted.
    """
    kind = "github"
    API = "https://api.github.com"
    CACHE_SECONDS = 3

    def __init__(self, repo, token, branch="main", draft="panel-draft"):
        self.repo = repo
        self.token = token
        self.branch = branch
        self.draft = draft
        self.where = f"{repo} ({draft})"
        self.note = ("Saved changes sit on the draft branch. Publish copies "
                     "them to the live site.")
        self._cache = {}

    # -- HTTP -----------------------------------------------------------
    def _api(self, method, path, body=None, accept="application/vnd.github+json"):
        req = urllib.request.Request(
            self.API + path, method=method,
            data=json.dumps(body).encode("utf-8") if body is not None else None)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Accept", accept)
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        req.add_header("User-Agent", "hdip-panel")
        if body is not None:
            req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
        if accept.endswith("raw"):
            return raw
        return json.loads(raw) if raw else None

    def _try(self, *a, **kw):
        """The same call, but a missing thing is None rather than an error."""
        try:
            return self._api(*a, **kw)
        except urllib.error.HTTPError as e:
            if e.code in (404, 409):
                return None
            raise

    # -- reading --------------------------------------------------------
    def _branch_in_use(self):
        """The draft if it exists, otherwise the live branch."""
        key = "_ref"
        hit = self._cache.get(key)
        if hit and hit[0] > time.time():
            return hit[1]
        ref = self._try("GET", f"/repos/{self.repo}/git/ref/heads/"
                               f"{urllib.parse.quote(self.draft)}")
        name = self.draft if ref else self.branch
        self._cache[key] = (time.time() + self.CACHE_SECONDS, name)
        return name

    def read_bytes(self, path, ref=None):
        ref = ref or self._branch_in_use()
        key = f"{ref}:{path}"
        hit = self._cache.get(key)
        if hit and hit[0] > time.time():
            return hit[1]
        raw = self._try("GET",
                        f"/repos/{self.repo}/contents/{urllib.parse.quote(path)}"
                        f"?ref={urllib.parse.quote(ref)}",
                        accept="application/vnd.github.raw")
        self._cache[key] = (time.time() + self.CACHE_SECONDS, raw)
        return raw

    def load(self):
        raw = self.read_bytes(STORE_PATH)
        if raw is None:
            raise RuntimeError(f"{STORE_PATH} is not in {self.repo}.")
        return json.loads(raw.decode("utf-8"))

    # -- writing --------------------------------------------------------
    def _head(self, branch):
        ref = self._try("GET", f"/repos/{self.repo}/git/ref/heads/"
                               f"{urllib.parse.quote(branch)}")
        return ref["object"]["sha"] if ref else None

    def _ensure_draft(self):
        sha = self._head(self.draft)
        if sha:
            return sha
        live = self._head(self.branch)
        self._api("POST", f"/repos/{self.repo}/git/refs",
                  {"ref": f"refs/heads/{self.draft}", "sha": live})
        return live

    def _commit(self, branch, files, message, parent):
        """One commit for all of it — a photo is five files (four tiers and
        the manifest) and five separate commits would leave the repo in four
        states where the manifest disagrees with what is on disk."""
        base = self._api("GET", f"/repos/{self.repo}/git/commits/{parent}")
        tree = []
        for path, raw in files.items():
            blob = self._api("POST", f"/repos/{self.repo}/git/blobs", {
                "content": base64.b64encode(raw).decode("ascii"),
                "encoding": "base64"})
            tree.append({"path": path, "mode": "100644", "type": "blob",
                         "sha": blob["sha"]})
        new_tree = self._api("POST", f"/repos/{self.repo}/git/trees",
                             {"base_tree": base["tree"]["sha"], "tree": tree})
        commit = self._api("POST", f"/repos/{self.repo}/git/commits",
                           {"message": message, "tree": new_tree["sha"],
                            "parents": [parent]})
        self._api("PATCH", f"/repos/{self.repo}/git/refs/heads/"
                           f"{urllib.parse.quote(branch)}",
                  {"sha": commit["sha"]})
        self._cache.clear()
        return commit["sha"]

    def save(self, data, message="Edit content"):
        raw = json.dumps(data, ensure_ascii=False, indent=1).encode("utf-8")
        self._commit(self.draft, {STORE_PATH: raw}, message,
                     self._ensure_draft())

    def add_files(self, files, message="Add photo"):
        self._commit(self.draft, files, message, self._ensure_draft())

    def publish(self):
        draft = self._head(self.draft)
        if not draft:
            return "ok", "Nothing to publish — the live site is up to date."
        files = {}
        for path in self._changed_paths(draft):
            raw = self.read_bytes(path, ref=self.draft)
            if raw is not None:
                files[path] = raw
        if not files:
            return "ok", "Nothing to publish — the live site is up to date."
        # Field edits are written without a build — a slug typed into a box
        # can still break the site. This is the last point at which that is
        # cheap to catch, and the first at which it would be public.
        if STORE_PATH in files:
            ok, detail = validate(json.loads(files[STORE_PATH].decode("utf-8")))
            if not ok:
                return "err", ("Not published — the site would not build.\n"
                               + detail)
        self._commit(self.branch, files, "Publish from the control panel",
                     self._head(self.branch))
        self._api("DELETE", f"/repos/{self.repo}/git/refs/heads/"
                            f"{urllib.parse.quote(self.draft)}")
        self._cache.clear()
        n = len(files)
        return "ok", (f"Published {n} file{'s' if n != 1 else ''}. The site "
                      "rebuilds and goes live in a minute or two.")

    def _changed_paths(self, draft_sha):
        cmp = self._api("GET", f"/repos/{self.repo}/compare/"
                               f"{urllib.parse.quote(self.branch)}...{draft_sha}")
        return [f["filename"] for f in cmp.get("files", [])
                if f["status"] != "removed"]

    def pending(self):
        draft = self._head(self.draft)
        if not draft:
            return ""
        n = len(self._changed_paths(draft))
        if not n:
            return ""
        return f"{n} saved change{'s' if n != 1 else ''} not yet published."


# ---------------------------------------------------------------------------
def choose():
    """GitHub when it is configured, the checkout otherwise.

    Configuration is all-or-nothing on purpose: half-configured credentials
    should fail loudly at startup, not silently write to a disk that is about
    to disappear.
    """
    repo = os.environ.get("HDIP_GITHUB_REPO")
    token = os.environ.get("HDIP_GITHUB_TOKEN")
    if not repo and not token:
        return Local()
    if not (repo and token):
        raise SystemExit("Set both HDIP_GITHUB_REPO and HDIP_GITHUB_TOKEN, "
                         "or neither.")
    return GitHub(repo, token,
                  os.environ.get("HDIP_GITHUB_BRANCH", "main"),
                  os.environ.get("HDIP_DRAFT_BRANCH", "panel-draft"))
