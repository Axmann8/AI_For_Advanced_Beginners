"""Fail if any relative Markdown link in the repo points at a file that doesn't exist."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "site"}

broken = 0
for md in ROOT.rglob("*.md"):
    if SKIP_DIRS & set(md.relative_to(ROOT).parts):
        continue
    for link in LINK.findall(md.read_text(encoding="utf-8")):
        if link.startswith(("http://", "https://", "#", "mailto:", "<")):
            continue
        target = (md.parent / link.split("#")[0]).resolve()
        if not target.exists():
            print(f"BROKEN  {md.relative_to(ROOT)} -> {link}")
            broken += 1

print(f"{broken} broken link(s)")
sys.exit(1 if broken else 0)
