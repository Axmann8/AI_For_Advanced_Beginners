"""MkDocs hooks: one set of Markdown files that looks great on GitHub *and* on the website.

Authors write plain, GitHub-friendly Markdown. At build time these hooks upgrade it:

  Source (renders fine on GitHub)                    →  Website
  ------------------------------------------------------------------------------------------
  <details class="eli5" [open]><summary>…</summary>   →  collapsible styled box (??? eli5)
  > [!TIP] + **🎮 Try this**                          →  styled admonition (type from emoji)
  > ⏱️ 20 min · 🎯 Level · 🧰 Needs                  →  "chips" row under the title
  <!-- in-this-chapter -->                            →  clickable section cards (from the real TOC)
  **Next:** [Title →](file.md)                        →  big "Next up" button + ✅ done button
  [Text](file.md "button") / "button-primary"        →  site buttons
  links leaving manual/ (../../examples/…)            →  GitHub URLs
  acronyms from the glossary (MCP, RAG, …)            →  hover tooltips with an ELI5 definition
"""

import html
import posixpath
import re
from pathlib import Path

REPO = "https://github.com/Axmann8/claude_cloud_trial_credits"
ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "manual" / "appendices" / "a-glossary.md"

# --------------------------------------------------------------------------- helpers ---
FENCE = re.compile(r"^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$", re.M | re.S)
PLACEHOLDER = "\x00CODE{}\x00"


def _stash_code(text: str) -> tuple[str, list[str]]:
    """Swap fenced code blocks for placeholders so no transform touches code."""
    blocks: list[str] = []

    def keep(match: re.Match) -> str:
        blocks.append(match.group(0))
        return PLACEHOLDER.format(len(blocks) - 1)

    return FENCE.sub(keep, text), blocks


def _restore_code(text: str, blocks: list[str]) -> str:
    def put_back(match: re.Match) -> str:
        indent, idx = match.group(1), int(match.group(2))
        # a block may have been indented (e.g. moved inside a collapsible box)
        return "\n".join(indent + line if line else line for line in blocks[idx].split("\n"))

    return re.sub(r"^([ \t]*)\x00CODE(\d+)\x00", put_back, text, flags=re.M)


def _indent(body: str) -> str:
    return "\n".join(("    " + line) if line.strip() else "" for line in body.split("\n"))


def _q(title: str) -> str:
    return title.replace('"', "“")


# ------------------------------------------------ GitHub alerts → Material admonitions ---
ALERT = re.compile(r"^> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\][ \t]*\n((?:>.*(?:\n|$))*)", re.M)
ALERT_TYPES = {"NOTE": "note", "TIP": "tip", "IMPORTANT": "info", "WARNING": "warning", "CAUTION": "danger"}
EMOJI_TYPES = {
    "🎮": "tryit", "🧸": "eli5", "🤿": "deepdive", "🤯": "funfact", "🎯": "takeaway",
    "⚠": "warning", "🔐": "danger", "🛡": "danger", "💡": "tip", "📌": "note",
    "🧪": "example", "✅": "success", "❓": "quiz", "🚧": "pitfall", "🧭": "note",
}


def _type_for(title: str, default: str) -> str:
    for emoji, kind in EMOJI_TYPES.items():
        if title.startswith(emoji):
            return kind
    return default


def _alert(match: re.Match) -> str:
    kind = ALERT_TYPES[match.group(1)]
    lines = [re.sub(r"^> ?", "", line) for line in match.group(2).rstrip("\n").split("\n")]
    title = ""
    if lines and (bold := re.fullmatch(r"\*\*(.+)\*\*", lines[0].strip())):
        lines.pop(0)
        title = bold.group(1).strip()
        kind = _type_for(title, kind)
    extra = " emoji-title" if title and not title[0].isalnum() else ""
    head = f"!!! {kind}{extra}" + (f' "{_q(title)}"' if title else "")
    return f"{head}\n\n{_indent(chr(10).join(lines).strip(chr(10)))}\n"


# ----------------------------------------------------- <details> → pymdownx.details ---
DETAILS = re.compile(
    r'^<details class="([\w-]+)"( open)?>[ \t]*\n<summary>(.*?)</summary>[ \t]*\n(.*?)\n</details>[ \t]*$',
    re.M | re.S,
)


def _details(match: re.Match) -> str:
    kind, is_open, title, body = match.groups()
    title = re.sub(r"<[^>]+>", "", title).strip()
    marker = "???+" if is_open else "???"
    extra = " emoji-title" if title and not title[0].isalnum() else ""
    return f'{marker} {kind}{extra} "{_q(title)}"\n\n{_indent(body.strip(chr(10)))}\n'


# ------------------------------------------------------------------- meta chips ---
META = re.compile(r"^(# .+)\n+> (⏱.+)$", re.M)


def _meta(match: re.Match) -> str:
    chips = [c.strip().replace("**", "") for c in match.group(2).split(" · ") if c.strip()]
    spans = "".join(f'<span class="chip">{html.escape(c)}</span>' for c in chips)
    return f'{match.group(1)}\n\n<div class="chapter-meta">{spans}</div>\n'


# ------------------------------------------------------------ Next → big button ---
NEXT = re.compile(r"^\*\*Next:\*\* \[(.+?)\]\((.+?)\)[ \t]*$", re.M)
END = re.compile(r"^\*\*You made it to the end! 🎉\*\* \[(.+?)\]\((.+?)\)[ \t]*$", re.M)
BUTTON = re.compile(r'\[([^\]]+)\]\(([^)\s]+) "(button(?:-primary)?)"\)')
LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")

# ------------------------------------------------------------- glossary tooltips ---
_ABBR_CACHE: list[str] | None = None


def _abbreviations() -> list[str]:
    """Acronym rows of the glossary become site-wide hover tooltips (ELI5 column)."""
    global _ABBR_CACHE
    if _ABBR_CACHE is None:
        _ABBR_CACHE = []
        if GLOSSARY.exists():
            for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) < 2 or not (m := re.fullmatch(r"\*\*(.+?)\*\*", cells[0])):
                    continue
                term = m.group(1).strip()
                acronym = re.fullmatch(r"[A-Za-z0-9./+-]{2,8}", term) and sum(ch.isupper() for ch in term) >= 2
                if not acronym:
                    continue
                tip = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cells[-1])  # drop links
                tip = re.sub(r"[*`_]", "", tip).replace("🧸", "").strip()
                if tip:
                    _ABBR_CACHE.append(f"*[{term}]: {tip}")
    return _ABBR_CACHE


# ------------------------------------------------------------------------ hooks ---
def on_page_markdown(markdown, page, config, files):
    text, blocks = _stash_code(markdown)

    text = META.sub(_meta, text, count=1)
    text = DETAILS.sub(_details, text)
    text = ALERT.sub(_alert, text)
    text = BUTTON.sub(
        lambda m: f"[{m.group(1)}]({m.group(2)}){{ .md-button"
        + (" .md-button--primary" if m.group(3).endswith("primary") else "")
        + " }",
        text,
    )
    done = "<!-- chapter-done -->\n\n" if re.match(r"part-\d+-[^/]+/\d{2,3}-", page.file.src_uri) else ""
    text = NEXT.sub(
        lambda m: f'{done}[<span class="next-label">Next up</span> {m.group(1)}]({m.group(2)})'
        "{ .md-button .md-button--primary .next-chapter }",
        text,
    )
    text = END.sub(
        lambda m: f'{done}[<span class="next-label">You made it to the end! 🎉</span> {m.group(1)}]({m.group(2)})'
        "{ .md-button .md-button--primary .next-chapter }",
        text,
    )

    page_dir = posixpath.dirname(page.file.src_uri)

    def rewrite(match):
        target, _, frag = match.group(1).partition("#")
        resolved = posixpath.normpath(posixpath.join("manual", page_dir, target))
        if resolved.startswith("manual/"):
            return match.group(0)  # stays inside the docs: MkDocs handles it
        kind = "blob" if posixpath.splitext(resolved)[1] else "tree"
        return f"]({REPO}/{kind}/main/{resolved}" + (f"#{frag}" if frag else "") + ")"

    text = LINK.sub(rewrite, text)
    text = _restore_code(text, blocks)

    if page.file.src_uri != "appendices/a-glossary.md":
        text += "\n\n" + "\n".join(_abbreviations()) + "\n"
    return text


def on_page_content(html_out, page, config, files):
    if "<!-- in-this-chapter -->" in html_out:
        items = []
        for top in page.toc:
            items.extend(top.children if top.level == 1 else [top])
        cards = "".join(
            f'<li><a href="{item.url}"><span class="n">{i}</span><span>{item.title}</span></a></li>'
            for i, item in enumerate(items, 1)
        )
        nav = (
            '<nav class="chapter-toc" aria-label="In this chapter">'
            '<p class="chapter-toc__title">🗺️ In this chapter <span>· tap a card to jump straight there</span></p>'
            f"<ol>{cards}</ol></nav>"
        )
        html_out = html_out.replace("<!-- in-this-chapter -->", nav, 1)
    if "<!-- chapter-done -->" in html_out:
        done = (
            f'<div class="chapter-done" data-chapter="{html.escape(page.url)}">'
            '<button type="button" class="chapter-done__btn">✅ Mark this chapter as done</button>'
            '<p class="chapter-done__hint">Progress is saved in this browser only, so no account needed. · '
            f'<a href="{"../" * page.url.count("/")}download/">📄 Prefer paper? Get the PDF book</a></p></div>'
        )
        html_out = html_out.replace("<!-- chapter-done -->", done, 1)
    return html_out
