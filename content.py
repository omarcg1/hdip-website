"""Organisation content — loaded from the store, not written here.

Edit through the dashboard (`python3 tools/dashboard.py`), which writes
data/site.json. The original hand-written module is kept at
tools/legacy/content_original.py for reference.
"""
from store import section as _section

globals().update(_section("content"))
