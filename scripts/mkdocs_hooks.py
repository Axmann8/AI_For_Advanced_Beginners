"""MkDocs hook: links that leave the docs folder (e.g. ../../examples/...) get
rewritten to GitHub URLs, so the same Markdown works on GitHub *and* on the site."""

import posixpath
import re

REPO = "https://github.com/Axmann8/claude_cloud_trial_credits"
LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")


def on_page_markdown(markdown, page, config, files):
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
