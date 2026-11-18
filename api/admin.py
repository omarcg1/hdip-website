"""The control panel, as a hosted function.

Vercel serves the built site from dist/ and routes only /admin here, so the
pages stay static and on the CDN — the panel is the one thing that needs to
run. `app` is the WSGI application; dashboard.py holds the panel itself and
does not care which front door it is answering.

The environment this expects:

    HDIP_GITHUB_REPO    owner/name of this repository
    HDIP_GITHUB_TOKEN   a token that may read and write it
    HDIP_ADMIN_USER     who signs in
    HDIP_ADMIN_HASH     salt$rounds$hash, from `--set-password --env`
    HDIP_SECRET         signs session cookies; any long random string
    HDIP_FUNCTION_PATH  /api/admin

Without the GitHub pair the panel writes to its own filesystem, which on a
serverless host means writing to something that is about to be discarded —
so backend.choose() refuses a half-configured environment rather than
accepting edits it cannot keep.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, ROOT)

import dashboard  # noqa: E402

app = dashboard.wsgi
