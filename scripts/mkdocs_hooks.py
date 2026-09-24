"""MkDocs hooks that let one set of Markdown files look great on GitHub *and* on the website.

1. GitHub alerts (`> [!TIP]`) → Material admonitions (`!!! tip`).
2. Links that leave the docs folder (e.g. ../../examples/...) → GitHub URLs.
"""

import posixpath
import re

REPO = "https://github.com/Axmann8/claude_cloud_trial_credits"
LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")
ALERT = re.compile(r"^> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\n((?:>.*(?:\n|$))*)", re.M)
ALERT_TYPES = {"NOTE": "note", "TIP": "tip", "IMPORTANT": "info", "WARNING": "warning", "CAUTION": "danger"}


def _alert_to_admonition(match: re.Match) -> str:
    kind = ALERT_TYPES[match.group(1)]
    lines = [re.sub(r"^> ?", "", line) for line in match.group(2).rstrip("\n").split("\n")]
    title = ""
    if lines and re.fullmatch(r"\*\*(.+)\*\*", lines[0].strip()):
        title = f' "{lines.pop(0).strip()[2:-2]}"'
    body = "\n".join(f"    {line}" if line else "" for line in lines)
    return f"!!! {kind}{title}\n{body}\n"


def on_page_markdown(markdown, page, config, files):
    markdown = ALERT.sub(_alert_to_admonition, markdown)
    page_dir = posixpath.dirname(page.file.src_uri)

    def rewrite(match):
        target, _, frag = match.group(1).partition("#")
        resolved = posixpath.normpath(posixpath.join("manual", page_dir, target))
        if resolved.startswith("manual/"):
            return match.group(0)  # stays inside the docs: MkDocs handles it
        kind = "blob" if posixpath.splitext(resolved)[1] else "tree"
        url = f"{REPO}/{kind}/main/{resolved}" + (f"#{frag}" if frag else "")
        return f"]({url})"

    return LINK.sub(rewrite, markdown)
