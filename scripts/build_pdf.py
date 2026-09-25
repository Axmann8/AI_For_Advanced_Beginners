"""Turn the whole manual into a beautifully formatted, printable PDF book.

    mkdocs build                                  # the PDF is made from the rendered site
    python scripts/build_pdf.py                   # writes MANUAL.pdf (US Letter)
    python scripts/build_pdf.py --paper a4 --out MANUAL-A4.pdf

One-time setup:

    pip install -r requirements-pdf.txt
    python -m playwright install chromium         # plus an emoji font, e.g. fonts-noto-color-emoji

How it works: every rendered page of the site is cleaned up for paper (ELI5 boxes and quiz answers
opened, tabs unrolled, links turned into jumps inside the book), then stitched into one HTML book with a
cover, a legend, contents, part dividers and a back cover. Chromium prints it, and PyMuPDF finishes it:
page numbers, running headers and bookmarks. Page references ("p. 42") are filled in by printing again
until every number is right.
"""

from __future__ import annotations

import argparse
import datetime
import html
import os
import re
import sys
import tempfile
import time
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin, urlsplit

import pymupdf
from bs4 import BeautifulSoup, Comment, Tag
from pygments.formatters import HtmlFormatter

sys.path.insert(0, str(Path(__file__).parent))
from sync_manual import PARTS, ROOT, pages_in  # noqa: E402

SITE_URL = "https://axmann8.github.io/claude_cloud_trial_credits/"
REPO_URL = "https://github.com/Axmann8/claude_cloud_trial_credits"
TITLE = "AI for Advanced Beginners"
PAPER = {"letter": ("8.5in", "11in"), "a4": ("210mm", "297mm")}
CACHE = ROOT / ".cache" / "pdf"
CSS_FILE = Path(__file__).parent / "pdf" / "book.css"
# Static (non-variable) font files, so Chromium embeds real TrueType fonts instead of bulky outlines
FONTSOURCE = "https://cdn.jsdelivr.net/npm/@fontsource/{family}@5/files/{family}-{subset}-{weight}-{style}.woff2"
FONTS = {
    "Inter": ("inter", [(w, "normal") for w in (400, 500, 600, 700, 800)] + [(400, "italic"), (700, "italic")]),
    "JetBrains Mono": ("jetbrains-mono", [(400, "normal"), (600, "normal")]),
}
SUBSETS = {
    "latin": "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, "
    "U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD",
    "latin-ext": "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+1D00-1DBF, "
    "U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF",
}
MERMAID_JS = "https://cdn.jsdelivr.net/npm/mermaid@11.17.2/dist/mermaid.min.js"
BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)
REF_OPEN, REF_CLOSE = "", ""  # placeholder brackets for page numbers
EMOJI_RE = re.compile(
    "[\U0001f000-\U0001faff←-⇿⌀-⏿①-➿⤀-⥿⬀-⯿️‍⃣]+"
)
PART_OF_BOOK = {"start-here": "Start Here", "appendices": "Appendices"}


# ----------------------------------------------------------------------------- model
@dataclass
class Doc:
    """One page of the website, as it appears in the book."""

    key: str  # site path, e.g. "part-2-mcp-and-connectors/07-mcp-explained/"
    kind: str  # "welcome" | "part" | "chapter"
    folder: str
    anchor: str  # id of this page's top in the book
    short: str = ""  # running-header title, e.g. "07 · MCP Explained"
    title: str = ""  # full title text
    num: str = ""  # "07", "A" or an emoji
    body: str = ""  # cleaned HTML
    extras: dict = field(default_factory=dict)


def ref(anchor_id: str) -> str:
    return f"{REF_OPEN}{anchor_id}{REF_CLOSE}"


def plain(s: str) -> str:
    """Title text without emoji, for running headers and bookmarks-safe strings."""
    return re.sub(r"\s+", " ", EMOJI_RE.sub("", s)).strip(" ·:")


def split_title(title: str) -> tuple[str, str]:
    """'07 · MCP Explained' -> ('07', 'MCP Explained'); 'Appendix A · Glossary' -> ('A', 'Glossary');
    '🧭 How to Use This Manual' -> ('🧭', 'How to Use This Manual')."""
    if m := re.match(r"^(\d{2}) · (.+)$", title):
        return m[1], m[2]
    if m := re.match(r"^Appendix ([A-Z]) · (.+)$", title):
        return m[1], m[2]
    if (m := re.match(r"^(\S+)\s+(.+)$", title)) and not re.search(r"\w", m[1]):
        return m[1], m[2]
    return "", title


# ----------------------------------------------------------------------------- assets
def fetch(url: str, dest: Path, ua: str | None = None) -> Path:
    if not dest.exists():
        req = urllib.request.Request(url, headers={"User-Agent": ua or BROWSER_UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            dest.write_bytes(r.read())
    return dest


def prepare_assets() -> None:
    """Download fonts and Mermaid once, so Chromium can print fully offline."""
    CACHE.mkdir(parents=True, exist_ok=True)
    fetch(MERMAID_JS, CACHE / "mermaid.min.js")
    faces = []
    for family, (slug, variants) in FONTS.items():
        for weight, style in variants:
            for subset, ranges in SUBSETS.items():
                name = f"{slug}-{subset}-{weight}-{style}.woff2"
                fetch(FONTSOURCE.format(family=slug, subset=subset, weight=weight, style=style), CACHE / name)
                faces.append(
                    f"@font-face {{ font-family: '{family}'; font-style: {style}; font-weight: {weight}; "
                    f"font-display: block; src: url({name}) format('woff2'); unicode-range: {ranges}; }}"
                )
    (CACHE / "fonts.css").write_text("\n".join(faces) + "\n", encoding="utf-8")


# ----------------------------------------------------------------------------- cleaning
def rename(tag: Tag, name: str, cls: str | None = None) -> None:
    tag.name = name
    if cls:
        tag["class"] = [cls]


def article_of(path: Path) -> BeautifulSoup:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    art = soup.find("article")
    if art is None:
        raise SystemExit(f"No <article> in {path}; is the site built?")
    return art


def title_of(art: Tag) -> str:
    h1 = art.find("h1")
    return re.sub(r"\s+", " ", h1.get_text(" ", strip=True).replace("¶", "")).strip() if h1 else ""


def clean(art: Tag, doc: Doc) -> None:
    """Strip the web-only bits and turn interactive widgets into print-friendly blocks."""
    soup = BeautifulSoup("", "lxml")
    for c in art.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for sel in ["a.headerlink", ".chapter-done", ".progress-tracker", "script", "button", "input",
                ".chapter-toc__title span", ".eli5-toggle"]:
        for el in art.select(sel):
            el.decompose()
    for a in art.select("a.next-chapter"):
        (a.parent if a.parent and a.parent.name == "p" else a).decompose()
    # a trailing rule left behind by the removed "mark as done" block
    while (last := art.find_all(recursive=False)[-1:]) and last[0].name == "hr":
        last[0].decompose()
    for ab in art.find_all("abbr"):
        ab.unwrap()
    for a in art.select('pre a[href^="#__codelineno"]'):
        a.decompose()
    for sp in art.select("pre span[id^='__span']"):
        del sp["id"]

    # <details> and admonitions -> .box (everything open on paper)
    for d in art.find_all("details"):
        classes = [c for c in d.get("class", []) if c != "emoji-title"] or ["note"]
        summary = d.find("summary", recursive=False)
        title = soup.new_tag("p", attrs={"class": "box-title"})
        if summary:
            title.extend(list(summary.contents))
            summary.decompose()
        d.name = "div"
        d.attrs = {"class": ["box", *classes]}
        if "quiz" in classes:
            answer = soup.new_tag("div", attrs={"class": "answer"})
            answer.extend(list(d.contents))
            d.append(answer)
        d.insert(0, title)
    for ad in art.select("div.admonition"):
        classes = [c for c in ad.get("class", []) if c not in ("admonition", "emoji-title")] or ["note"]
        ad["class"] = ["box", *classes]
        for t in ad.select(":scope > p.admonition-title"):
            t["class"] = ["box-title"]
    for box in art.select(".box"):
        if len(box.get_text()) > 1600:
            box["class"] = [*box["class"], "long"]

    # tabs -> one labelled block per tab
    for ts in art.select("div.tabbed-set"):
        labels = ts.select(".tabbed-labels > label")
        blocks = ts.select(".tabbed-content > .tabbed-block")
        wrap = soup.new_tag("div", attrs={"class": "tabs"})
        for lab, blk in zip(labels, blocks):
            tab = soup.new_tag("div", attrs={"class": "tab"})
            p = soup.new_tag("p", attrs={"class": "tab-label"})
            p.extend(list(lab.contents))
            tab.append(p)
            tab.extend(list(blk.contents))
            if len(tab.get_text()) > 1800 or tab.select(".long"):
                tab["class"] = ["tab", "long"]
            wrap.append(tab)
        ts.replace_with(wrap)

    # task lists -> printable tick boxes
    for lab in art.select("label.task-list-control"):
        lab.replace_with(soup.new_tag("span", attrs={"class": "checkbox"}))

    # mermaid source -> rendered in the browser before printing
    for pre in art.select("pre.mermaid"):
        div = soup.new_tag("div", attrs={"class": "diagram"})
        src = soup.new_tag("script", attrs={"type": "text/plain", "class": "mermaid-src"})
        src.string = pre.get_text()
        div.append(src)
        pre.replace_with(div)

    # long code blocks may break across pages
    for hl in art.select("div.highlight"):
        if hl.get_text().count("\n") > 38:
            hl["class"] = [*hl["class"], "long"]
            for pre in hl.select("pre"):
                pre["class"] = [*pre.get("class", []), "long"]

    # headings: the page title becomes the opener; everything else shifts to fit the book outline
    shift = {"chapter": 1, "welcome": 0, "part": 0}[doc.kind]
    names = {"h2": "sec", "h3": "sub", "h4": "subsub", "h5": "subsub", "h6": "subsub"}
    for h in art.find_all(re.compile(r"^h[2-6]$")):
        level = min(int(h.name[1]) + shift, 6)
        h["class"] = [names[h.name]]
        h.name = f"h{level}"
    h1 = art.find("h1")
    if h1:
        h1.decompose()


def prefix_ids(art: Tag, anchor: str) -> None:
    for el in art.find_all(id=True):
        el["id"] = f"{anchor}-{el['id']}"


# ----------------------------------------------------------------------------- building docs
def site_path(folder: str, stem: str | None) -> str:
    return f"{folder}/" if stem is None else f"{folder}/{stem}/"


def load_docs(site: Path) -> list[Doc]:
    docs: list[Doc] = [Doc("", "welcome", "", "pg0")]
    for folder in PARTS:
        docs.append(Doc(site_path(folder, None), "part", folder, f"pg{len(docs)}"))
        for page in pages_in(folder):
            d = Doc(site_path(folder, page.path.stem), "chapter", folder, f"pg{len(docs)}")
            d.short = page.nav_title
            docs.append(d)
    return docs


def link_rewriter(docs: list[Doc]):
    by_key = {d.key: d for d in docs}

    def rewrite(art: Tag, doc: Doc, ids: set[str], heads: set[str]) -> None:
        base = "http://book/" + doc.key
        for a in art.find_all("a", href=True):
            href = a["href"]
            if href.startswith(("mailto:", "tel:")):
                continue
            url = urlsplit(urljoin(base, href))
            if url.netloc != "book":
                continue
            key = url.path.lstrip("/")
            if key.endswith("index.html"):
                key = key[: -len("index.html")]
            target = by_key.get(key)
            if target is None:
                a["href"] = urljoin(SITE_URL, key) + (f"#{url.fragment}" if url.fragment else "")
                continue
            dest = target.anchor
            if url.fragment and f"{target.anchor}-{url.fragment}" in ids:
                dest = f"{target.anchor}-{url.fragment}"
            a["href"] = f"#{dest}"
            if dest not in heads:
                continue  # page numbers are only known for headings
            if a.find_parent("nav", class_="chapter-toc"):
                a.append(BeautifulSoup(f'<span class="pg">{ref(dest)}</span>', "lxml").span)
            else:
                a.insert_after(BeautifulSoup(f'<span class="pref">p.&#8239;{ref(dest)}</span>', "lxml").span)

    return rewrite


def build_docs(site: Path) -> list[Doc]:
    docs = load_docs(site)
    arts: list[Tag] = []
    for doc in docs:
        art = article_of(site / doc.key / "index.html")
        doc.title = title_of(art)
        doc.num, _ = split_title(doc.title)
        if doc.kind == "welcome":
            hero = art.select_one(".hero")
            lead = next((p for p in hero.find_all("p") if not p.find(class_="md-button")
                         and "hero-kicker" not in str(p)), None)
            doc.extras["stats"] = [
                (s.strong.get_text(strip=True), s.span.get_text(strip=True)) for s in hero.select(".stat")
            ]
            if lead:
                hero.insert_before(lead)
            hero.decompose()
            # "The eleven parts" duplicates the contents pages
            for h in art.find_all("h2"):
                if "eleven parts" in h.get_text().lower():
                    grid = h.find_next_sibling("div")
                    if grid is not None and "grid" in grid.get("class", []):
                        grid.decompose()
                    h.decompose()
        if doc.kind == "part":
            label, emoji = PARTS[doc.folder]
            doc.num, doc.short = emoji, label
            first = art.find("h1")
            lead = first.find_next_sibling() if first else None
            doc.extras["lead"] = str(lead) if lead is not None and lead.name == "p" else ""
            if doc.extras["lead"]:
                lead.decompose()
            eli5 = art.select_one("details.eli5")
            doc.extras["eli5"] = eli5.p.decode_contents() if eli5 and eli5.p else ""
            if eli5:
                eli5.decompose()
            # the chapter list lives on the divider, so drop the card grid (and its heading)
            for grid in art.select("div.grid.cards"):
                h = grid.find_previous_sibling("h2")
                if h is not None and h.find_next_sibling("div") is grid:
                    h.decompose()
                grid.decompose()
        clean(art, doc)
        prefix_ids(art, doc.anchor)
        arts.append(art)
    ids = {el["id"] for art in arts for el in art.find_all(id=True)} | {d.anchor for d in docs}
    heads = {h["id"] for art in arts for h in art.find_all(re.compile(r"^h[1-6]$"), id=True)}
    heads |= {d.anchor for d in docs}
    rewrite = link_rewriter(docs)
    for doc, art in zip(docs, arts):
        for lead in ("lead", "eli5"):
            if doc.extras.get(lead):
                frag = BeautifulSoup(f"<div>{doc.extras[lead]}</div>", "lxml").div
                for ab in frag.find_all("abbr"):
                    ab.unwrap()
                rewrite(frag, doc, ids, heads)
                doc.extras[lead] = frag.decode_contents()
        rewrite(art, doc, ids, heads)
        doc.body = art.decode_contents()
    return docs


# ----------------------------------------------------------------------------- book HTML
def opener(num: str, kicker: str, title: str, tag: str, anchor: str, bookmark: str) -> str:
    emoji = bool(num) and not re.search(r"\w", num)
    num_html = f'<div class="opener-num{" emoji" if emoji else ""}" aria-hidden="true">{html.escape(num)}</div>' if num else ""
    return (
        f'<header class="opener">{num_html}<div class="opener-text">'
        f'<div class="opener-kicker">{html.escape(kicker)}</div>'
        f'<{tag} class="chapter-title" id="{anchor}" data-bm="{html.escape(bookmark)}">{html.escape(title)}</{tag}>'
        f"</div></header>"
    )


def cover(stats: list[tuple[str, str]], edition: str) -> str:
    pills = "".join(f'<span class="stat"><strong>{html.escape(n)}</strong>{html.escape(l)}</span>' for n, l in stats)
    return f"""
<section class="full cover"><div class="inner">
  <div class="kicker">The Massive Manual · Printable Edition</div>
  <div class="rocket">🚀</div>
  <div class="title">AI for <em>Advanced</em><br>Beginners</div>
  <p class="subtitle">You know what an LLM is. You know how to prompt. <strong style="color:#fff">This is everything
  that comes next:</strong> connecting AI to your apps, automating your life, building your own tools and agents,
  running models at home, making art and music, and using it all in real life, with an 🧸 ELI5 for everything.</p>
  <div class="stats">{pills}</div>
  <div class="foot"><div><strong>{html.escape(edition)}</strong>Free and open, forever.</div>
  <div style="text-align:right">{SITE_URL.removeprefix("https://").rstrip("/")}</div></div>
</div></section>"""


def legend() -> str:
    boxes = [
        ("eli5", "🧸 ELI5", "The idea explained like you're five. Every chapter and every section has one. "
                            "Short on time? Read only these and you'll still get the big picture."),
        ("tryit", "🎮 Try this", "A hands-on challenge to do right now. Ten minutes of doing beats an hour of reading."),
        ("quiz", "❓ Check yourself", "Quick questions at the end of each chapter. The answer sits right under each one, "
                                     "so cover it with your hand first! 🙈"),
        ("tip", "💡 Tip", "Shortcuts, power moves and the little tricks that make things click."),
        ("note", "📌 Note", "Useful context: why something works the way it does."),
        ("warning", "⚠️ Watch out", "Things that can cost you money, data or trust. Read these twice."),
        ("funfact", "🎉 Fun fact", "Delightful detours. Totally optional, totally worth it."),
        ("takeaway", "✅ Checklists", "Tick the boxes with a pen. Appendix J collects the best ones for your fridge."),
    ]
    grid = "".join(
        f'<div class="box {c}"><p class="box-title">{t}</p><p>{html.escape(d)}</p></div>' for c, t, d in boxes
    )
    return f"""
<section class="doc front">
{opener("📖", "Before we begin", "How to Read This Book", "h1", "legend", "How to Read This Book")}
<p style="font-size:11pt">This is the whole manual in one printable book: <strong>88 chapters in eleven parts</strong>, the Start Here
guides, and ten appendices full of cheat sheets, prompts and checklists. You don't have to read it front to back. Skim the
contents, pick the part that makes you curious, and dive in. Every path is a good one. 💜</p>
<h2 class="sec">🧭 Finding your way</h2>
<ul>
<li><strong>Page references.</strong> When the text points somewhere else in the book, a small page number follows the link,
like this: <a href="#legend">How to Read This Book</a><span class="pref">p.&#8239;{ref("legend")}</span>.</li>
<li><strong>Every chapter starts the same way:</strong> a reading-time chip, a one-paragraph ELI5 of the whole chapter, and an
<em>In this chapter</em> map with page numbers.</li>
<li><strong>Reading on screen?</strong> Every link, contents entry and chapter map is clickable, and the bookmarks panel lists
every part, chapter and section.</li>
<li><strong>Want the code?</strong> The starter kits live on GitHub at <a href="{REPO_URL}">{REPO_URL.removeprefix("https://")}</a>,
and the searchable online edition (always up to date) is at <a href="{SITE_URL}">{SITE_URL.removeprefix("https://").rstrip("/")}</a>.</li>
</ul>
<h2 class="sec">🎨 The boxes you'll meet</h2>
<div class="legend-grid">{grid}</div>
</section>"""


def contents(docs: list[Doc]) -> str:
    out = [
        '<section class="doc front contents">',
        opener("🗂️", "Everything in this book", "Contents", "h1", "contents", "Contents"),
    ]
    welcome = docs[0]
    out.append(
        f'<div class="toc-part"><a class="toc-row part" href="#{welcome.anchor}"><span class="name"><span class="emoji">👋</span>'
        f'Welcome</span><span class="leader"></span><span class="pg">{ref(welcome.anchor)}</span></a></div>'
    )
    part = None
    for d in docs[1:]:
        if d.kind == "part":
            if part is not None:
                out.append("</div>")
            label, emoji = PARTS[d.folder]
            out.append(
                f'<div class="toc-part"><a class="toc-row part" href="#{d.anchor}"><span class="name"><span class="emoji">{emoji}</span>'
                f'{html.escape(label)}</span><span class="leader"></span><span class="pg">{ref(d.anchor)}</span></a>'
            )
            part = d
            continue
        num, rest = split_title(d.title)
        num_html = html.escape(num) if re.search(r"\w", num) else ""
        name = html.escape(rest if num_html else d.title)
        out.append(
            f'<a class="toc-row chapter" href="#{d.anchor}"><span class="num">{num_html}</span>'
            f'<span class="name">{name}</span><span class="leader"></span><span class="pg">{ref(d.anchor)}</span></a>'
        )
    out.append("</div></section>")
    return "\n".join(out)


def divider(part: Doc, chapters: list[Doc]) -> str:
    label, emoji = PARTS[part.folder]
    kicker, _, name = label.partition(" · ")
    if not name:
        kicker, name = {"start-here": "Before you begin", "appendices": "The reference shelf"}.get(part.folder, ""), label
    rows = []
    for d in chapters:
        num, _ = split_title(d.title)
        short = d.short
        if re.search(r"\w", num):
            short = re.sub(rf"^(Appendix )?{re.escape(num)} · ", "", short)
        else:
            num = ""
        rows.append(
            f'<a class="toc-row chapter" href="#{d.anchor}"><span class="num">{html.escape(num)}</span>'
            f'<span class="name">{html.escape(plain(short) or short)}</span><span class="leader"></span>'
            f'<span class="pg">{ref(d.anchor)}</span></a>'
        )
    eli5 = part.extras.get("eli5")
    eli5_html = f'<div class="eli5-card"><p><span class="label">🧸 ELI5:</span>{eli5}</p></div>' if eli5 else ""
    return f"""
<section class="full divider"><div class="inner">
  <div class="part-kicker">{html.escape(kicker)}</div>
  <div class="part-emoji">{emoji}</div>
  <h1 class="part-title" id="{part.anchor}" data-bm="{html.escape(emoji + " " + label)}">{html.escape(name)}</h1>
  {f'<div class="lead">{part.extras["lead"]}</div>' if part.extras.get("lead") else ""}
  {eli5_html}
  <div class="chapter-list"><div class="list-title">{"In this part" if part.folder.startswith("part-") else "Inside"}</div>{"".join(rows)}</div>
</div></section>"""


def backcover() -> str:
    return f"""
<section class="full backcover"><div class="inner">
  <div class="big">Now go build<br>something fun ✨</div>
  <p>This book is the printable edition of a free, open manual. The online edition is searchable and always up to
  date, and every starter kit lives on GitHub:</p>
  <p><a href="{SITE_URL}">{SITE_URL.removeprefix("https://").rstrip("/")}</a><br>
  <a href="{REPO_URL}">{REPO_URL.removeprefix("https://")}</a></p>
  <p style="margin-top:0.4in">Made with ❤️ and Claude Code.</p>
</div></section>"""


def book_html(docs: list[Doc], paper: str, edition: str) -> str:
    w, h = PAPER[paper]
    pyg = HtmlFormatter(style="friendly").get_style_defs(".highlight")
    parts: list[str] = [cover(docs[0].extras.get("stats", []), edition), legend(), contents(docs)]
    welcome = docs[0]
    parts.append(
        f'<section class="doc">{opener("👋", "Before we begin", "Welcome to the Massive Manual", "h1", welcome.anchor, "Welcome")}'
        f"{welcome.body}</section>"
    )
    i = 1
    while i < len(docs):
        part = docs[i]
        chapters = []
        j = i + 1
        while j < len(docs) and docs[j].kind == "chapter":
            chapters.append(docs[j])
            j += 1
        parts.append(divider(part, chapters))
        if BeautifulSoup(part.body, "lxml").get_text(strip=True):
            parts.append(f'<section class="doc part-intro">{part.body}</section>')
        label = PARTS[part.folder][0]
        for d in chapters:
            num, rest = split_title(d.title)
            kicker = PART_OF_BOOK.get(d.folder, label)
            if d.folder == "appendices" and num:
                kicker = f"Appendix {num}"
            parts.append(
                f'<section class="doc chapter">{opener(num, kicker, rest if num else d.title, "h2", d.anchor, d.title)}'
                f"{d.body}</section>"
            )
        i = j
    parts.append(backcover())
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{TITLE}</title>
<link rel="stylesheet" href="fonts.css">
<style>{pyg}</style>
<link rel="stylesheet" href="book.css">
<style>@page {{ size: {w} {h}; }} :root {{ --page-w: {w}; --page-h: {h}; }}
.highlight, .highlight pre {{ background: #faf9fe; }}</style>
</head><body>
{"".join(parts)}
<script src="mermaid.min.js"></script>
<script>
(async () => {{
  const errors = [];
  try {{
    await document.fonts.ready;
    const font = 'Inter, "Noto Color Emoji", sans-serif';
    mermaid.initialize({{
      startOnLoad: false, theme: 'base', securityLevel: 'loose', fontFamily: font,
      flowchart: {{ htmlLabels: true, curve: 'basis', padding: 12 }},
      themeVariables: {{
        fontFamily: font, fontSize: '14px',
        primaryColor: '#ede9fe', primaryBorderColor: '#7c3aed', primaryTextColor: '#1f1b2e',
        secondaryColor: '#fef3c7', secondaryBorderColor: '#f59e0b', secondaryTextColor: '#1f1b2e',
        tertiaryColor: '#ecfdf5', tertiaryBorderColor: '#10b981', tertiaryTextColor: '#1f1b2e',
        lineColor: '#6d28d9', textColor: '#1f1b2e', clusterBkg: '#faf9fe', clusterBorder: '#c4b5fd',
        edgeLabelBackground: '#ffffff', noteBkgColor: '#fef3c7', noteBorderColor: '#f59e0b',
        actorBkg: '#ede9fe', actorBorder: '#7c3aed', signalColor: '#4c1d95', signalTextColor: '#1f1b2e',
        quadrant1Fill: '#ede9fe', quadrant2Fill: '#fef3c7', quadrant3Fill: '#ecfdf5', quadrant4Fill: '#fdf2f8',
        quadrantPointFill: '#6d28d9', quadrantTitleFill: '#1f1b2e'
      }}
    }});
    let n = 0;
    for (const box of document.querySelectorAll('.diagram')) {{
      const src = box.querySelector('.mermaid-src').textContent;
      const id = 'mmd' + (n++);
      try {{
        const {{ svg }} = await mermaid.render(id, src);
        box.insertAdjacentHTML('beforeend', svg);
      }} catch (e) {{
        errors.push(id + ': ' + String(e).slice(0, 200));
        document.getElementById('d' + id)?.remove();
        const pre = document.createElement('pre');
        pre.textContent = src;
        box.replaceWith(pre);
      }}
    }}
  }} catch (e) {{ errors.push(String(e)); }}
  window.__errors = errors;
  window.__ready = true;
}})();
</script>
</body></html>"""


# ----------------------------------------------------------------------------- printing
def headings(page_html: str) -> list[tuple[int, str, str]]:
    """(level, id, bookmark title) for every heading, in document order."""
    out = []
    for m in re.finditer(r"<h([1-6])\b([^>]*)>(.*?)</h\1>", page_html, re.S):
        attrs = m[2]
        hid = re.search(r'\bid="([^"]*)"', attrs)
        bm = re.search(r'\bdata-bm="([^"]*)"', attrs)
        text = html.unescape(bm[1]) if bm else html.unescape(re.sub(r"<[^>]+>", "", m[3]))
        out.append((int(m[1]), hid[1] if hid else "", re.sub(r"\s+", " ", text).strip()))
    return out


def fill(page_html: str, pages: dict[str, int], placeholder: str) -> str:
    return re.sub(
        f"{REF_OPEN}(.*?){REF_CLOSE}", lambda m: str(pages.get(m[1], placeholder)), page_html
    )


def print_pdf(browser, page_html: str, out: Path) -> None:
    html_path = CACHE / "book.html"
    html_path.write_text(page_html, encoding="utf-8")
    (CACHE / "book.css").write_text(CSS_FILE.read_text(encoding="utf-8"), encoding="utf-8")
    page = browser.new_page()
    t0 = time.time()
    page.goto(html_path.as_uri(), wait_until="load", timeout=0)
    page.wait_for_function("window.__ready === true", timeout=300_000, polling=500)
    errors = page.evaluate("window.__errors")
    if errors:
        print(f"  ⚠️  {len(errors)} diagram(s) fell back to code:", *errors, sep="\n     ")
    t1 = time.time()
    page.pdf(path=str(out), prefer_css_page_size=True, print_background=True, outline=True, tagged=True)
    page.close()
    print(f"  laid out in {t1 - t0:.0f}s, printed in {time.time() - t1:.0f}s", flush=True)


def page_map(pdf: Path, heads: list[tuple[int, str, str]]) -> dict[str, int]:
    with pymupdf.open(pdf) as doc:
        toc = doc.get_toc(simple=True)
    if len(toc) != len(heads):
        raise SystemExit(f"Outline has {len(toc)} entries but the book has {len(heads)} headings")
    return {hid: pg for (_, hid, _), (_, _, pg) in zip(heads, toc) if hid}


# ----------------------------------------------------------------------------- finishing
def finish(pdf: Path, out: Path, docs: list[Doc], heads, pages: dict[str, int], edition: str) -> int:
    doc = pymupdf.open(pdf)
    n = doc.page_count

    # bookmarks: parts > chapters > sections
    toc, last = [], 0
    for level, hid, title in heads:
        if level > 3 or not hid or hid not in pages:
            continue
        level = min(level, last + 1)
        toc.append([level, title, pages[hid]])
        last = level
    doc.set_toc(toc)

    # running headers and page numbers
    regular, bold = pymupdf.Font("figo"), pymupdf.Font("figbo")
    bare = {1, n}  # cover and back cover
    openers = set()
    markers: list[tuple[int, str, str]] = []  # (first page, left header, right header)
    front = {"legend": "How to Read This Book", "contents": "Contents"}
    for hid, title in front.items():
        openers.add(pages[hid])
        markers.append((pages[hid], TITLE, title))
    for d in docs:
        start = pages[d.anchor]
        if d.kind == "welcome":
            openers.add(start)
            markers.append((start, TITLE, "Welcome"))
        elif d.kind == "part":
            bare.add(start)
            markers.append((start, plain(PARTS[d.folder][0]), "Overview"))
        else:
            openers.add(start)
            markers.append((start, plain(PARTS[d.folder][0]), plain(d.short)))
    markers.sort()

    ink, muted, violet = (0.12, 0.11, 0.18), (0.48, 0.46, 0.56), (0.49, 0.23, 0.93)
    for i, page in enumerate(doc, start=1):
        if i in bare:
            continue
        if not page.is_wrapped:
            page.wrap_contents()  # Chromium leaves a scaled matrix active; isolate it before drawing
        r = page.rect
        mx = 0.8 * 72
        even = i % 2 == 0
        tw = pymupdf.TextWriter(r)
        num = str(i)
        size = 8.5
        y_foot = r.height - 0.48 * 72
        x = mx if even else r.width - mx - bold.text_length(num, size)
        tw.append((x, y_foot), num, font=bold, fontsize=size)
        brand = TITLE
        bx = r.width - mx - regular.text_length(brand, 7) if even else mx
        tw.append((bx, y_foot), brand, font=regular, fontsize=7)
        tw.write_text(page, color=muted)
        page.draw_circle((x - 6 if not even else x + bold.text_length(num, size) + 6, y_foot - 2.8), 1.6,
                         color=None, fill=violet)
        if i in openers:
            continue
        current = [m for m in markers if m[0] <= i]
        if not current:
            continue
        _, left, right = current[-1]
        text = left if even else right
        if not text:
            continue
        maxw = r.width - 2 * mx
        while regular.text_length(text, 7.6) > maxw and len(text) > 4:
            text = text[:-2].rstrip() + "…"
        hw = pymupdf.TextWriter(r)
        y_head = 0.55 * 72
        hx = mx if even else r.width - mx - regular.text_length(text, 7.6)
        hw.append((hx, y_head), text, font=regular, fontsize=7.6)
        hw.write_text(page, color=ink if not even else muted)
        page.draw_line((mx, y_head + 6), (r.width - mx, y_head + 6), color=(0.9, 0.88, 0.96), width=0.6)

    doc.set_metadata({
        "title": f"{TITLE}: The Massive Manual",
        "author": "AI for Advanced Beginners",
        "subject": "A friendly, hands-on manual for everything after \"what is an LLM?\"",
        "keywords": "AI, MCP, connectors, automation, n8n, Zapier, Notion, agents, Claude Code, local AI, ELI5",
        "creator": f"scripts/build_pdf.py · {edition}",
        "producer": "Chromium + PyMuPDF",
    })
    doc.set_pagemode("UseOutlines")
    doc.save(out, garbage=1, deflate=True, use_objstms=1)  # object streams: small file, fast save
    doc.close()
    return n


# ----------------------------------------------------------------------------- main
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", type=Path, default=ROOT / "site", help="built site folder (default: site/)")
    ap.add_argument("--out", type=Path, default=ROOT / "MANUAL.pdf")
    ap.add_argument("--paper", choices=PAPER, default="letter")
    ap.add_argument("--max-passes", type=int, default=4)
    args = ap.parse_args()

    if not (args.site / "index.html").exists():
        raise SystemExit(f"{args.site} has no built site. Run `mkdocs build` first.")
    t0 = time.time()
    prepare_assets()
    edition = f"{datetime.date.today():%B %Y} edition"
    docs = build_docs(args.site)
    template = book_html(docs, args.paper, edition)
    heads = headings(template)
    print(f"📚 {len(docs)} pages stitched · {len(heads)} headings · {len(template) // 1024} KB of HTML")

    from playwright.sync_api import sync_playwright

    pages: dict[str, int] = {}
    with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
        browser = p.chromium.launch(executable_path=os.environ.get("PDF_CHROMIUM") or None)
        draft = Path(tmp) / "draft.pdf"
        for n in range(1, args.max_passes + 1):
            print(f"🖨️  Pass {n}: printing…", flush=True)
            print_pdf(browser, fill(template, pages, "000"), draft)
            new = page_map(draft, heads)
            if new == pages:
                break
            pages = new
        else:
            print("  ⚠️  page numbers still moving after the last pass; a few references may be off by one")
        browser.close()
        total = finish(draft, args.out, docs, heads, pages, edition)
    size = args.out.stat().st_size / 1_048_576
    print(f"✅ Wrote {args.out} · {total} pages · {size:.1f} MB · {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
