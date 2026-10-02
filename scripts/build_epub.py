"""Turn the whole manual into a Kindle-ready EPUB 3 ebook.

    mkdocs build                                  # the ebook is made from the rendered site
    python scripts/build_epub.py                  # writes MANUAL.epub

The EPUB works with Send to Kindle, Apple Books, Kobo and any EPUB reader, and Amazon KDP accepts it for publishing.
It reuses the PDF builder's cleanup (boxes opened, tabs unrolled, links turned into jumps inside the book), then:

  * splits the book into one XHTML file per page, with an HTML contents page and a nested navigation menu
  * renders every Mermaid diagram to a PNG image (Kindles can't run JavaScript)
  * swaps emoji for small Twemoji images, so they show in color on every reader
  * adds a cover (page 1 of MANUAL.pdf when available) and a colophon

Validate with the W3C checker:  java -jar epubcheck.jar MANUAL.epub
"""

from __future__ import annotations

import argparse
import datetime
import html
import io
import re
import sys
import urllib.error
import uuid
import zipfile
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import emoji as emoji_lib
from bs4 import BeautifulSoup, Tag
from pygments.formatters import HtmlFormatter

sys.path.insert(0, str(Path(__file__).parent))
from build_pdf import (  # noqa: E402
    CACHE,
    PART_OF_BOOK,
    PARTS,
    REPO_URL,
    ROOT,
    SITE_URL,
    TITLE,
    build_docs,
    fetch,
    plain,
    prepare_assets,
    split_title,
)

TWEMOJI = "https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/72x72/{}.png"
EMOJI_CACHE = ROOT / ".cache" / "twemoji"
BOOK_ID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, SITE_URL))
XHTML_HEAD = (
    '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
    '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">\n'
    '<head><meta charset="utf-8"/><title>{title}</title>'
    '<link rel="stylesheet" type="text/css" href="css/book.css"/></head>\n'
)

CSS = """
body { font-family: serif; line-height: 1.5; margin: 0 0.4em; }
h1, h2, h3, h4, h5 { font-family: sans-serif; line-height: 1.25; page-break-after: avoid; color: #3b1f8f; }
h1 { font-size: 1.7em; margin: 0.2em 0 0.6em; }
h2 { font-size: 1.35em; margin: 1.6em 0 0.5em; border-bottom: 1px solid #ddd6fe; padding-bottom: 0.15em; }
h3 { font-size: 1.15em; margin: 1.2em 0 0.4em; }
h4, h5 { font-size: 1em; margin: 1em 0 0.3em; }
p { margin: 0 0 0.7em; }
a { color: #6d28d9; text-decoration: none; }
img.emoji { height: 1em; width: 1em; vertical-align: -0.12em; margin: 0 0.05em; }
.kicker { font-family: sans-serif; font-size: 0.75em; letter-spacing: 0.12em; text-transform: uppercase;
  color: #7c3aed; margin: 1.5em 0 0.2em; font-weight: bold; }
.opener { margin-bottom: 1em; }
.chapter-meta { font-family: sans-serif; font-size: 0.8em; color: #555; margin: 0 0 1em; }
.chapter-meta .chip { display: inline; margin-right: 0.8em; }
.box { border-left: 4px solid #a78bfa; background: #f8f7ff; padding: 0.5em 0.8em; margin: 1em 0; }
.box-title { font-family: sans-serif; font-weight: bold; margin: 0 0 0.4em; }
.box.keypoints { border-left-color: #f59e0b; background: #fffbeb; }
.box.tryit, .box.tip, .box.success { border-left-color: #10b981; background: #f0fdf4; }
.box.warning, .box.pitfall { border-left-color: #f97316; background: #fff7ed; }
.box.danger { border-left-color: #ef4444; background: #fef2f2; }
.box.quiz { border-left-color: #8b5cf6; }
.box.deepdive, .box.note, .box.info { border-left-color: #3b82f6; background: #eff6ff; }
.box p:last-child { margin-bottom: 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.85em; }
th, td { border: 1px solid #ccc; padding: 0.3em 0.45em; vertical-align: top; text-align: left; }
th { background: #ede9fe; font-family: sans-serif; }
pre { font-family: monospace; font-size: 0.75em; white-space: pre-wrap; background: #f6f6f8;
  border: 1px solid #e5e5ea; padding: 0.5em; margin: 0.8em 0; }
code { font-family: monospace; font-size: 0.9em; }
blockquote { margin: 0.8em 1em; font-style: italic; color: #333; }
figure.diagram { margin: 1em 0; text-align: center; page-break-inside: avoid; }
figure.diagram img { max-width: 100%; }
figure.shot { margin: 1em 0; page-break-inside: avoid; }
figure.shot img { max-width: 100%; border: 1px solid #ccc; border-radius: 6px; }
figure.shot figcaption { font-size: 0.85em; color: #555; margin-top: 0.3em; }
.chapter-toc { border: 1px solid #ddd6fe; padding: 0.4em 0.8em; margin: 1em 0; }
.chapter-toc__title { font-family: sans-serif; font-weight: bold; margin: 0.2em 0 0.4em; }
.chapter-toc ol { margin: 0; padding-left: 1.4em; }
.chapter-toc .n { display: none; }
.tab-label { font-family: sans-serif; font-weight: bold; color: #6d28d9; margin-top: 0.8em; }
.checkbox:before { content: "\\2610\\00a0"; }
.titlepage { text-align: center; margin-top: 18%; }
.titlepage h1 { font-size: 2.2em; border: none; }
.subtitle { font-style: italic; color: #444; }
.toc-part { font-family: sans-serif; font-weight: bold; margin: 1.1em 0 0.3em; }
.toc-chapters { margin: 0 0 0.6em 0.8em; }
.toc-ch { margin: 0 0 0.25em; }
.cover { text-align: center; margin: 0; padding: 0; }
.cover img { max-width: 100%; max-height: 100%; }
"""


# ----------------------------------------------------------------------------- emoji
def twemoji_name(seq: str) -> str:
    cps = [f"{ord(c):x}" for c in seq]
    if "200d" not in cps:
        cps = [c for c in cps if c != "fe0f"]
    return "-".join(cps)


class EmojiImages:
    """Downloads Twemoji PNGs on demand and remembers which ones the book uses."""

    def __init__(self) -> None:
        EMOJI_CACHE.mkdir(parents=True, exist_ok=True)
        self.used: dict[str, Path] = {}
        self.missing: set[str] = set()

    def path_for(self, seq: str) -> str | None:
        names = [twemoji_name(seq), "-".join(f"{ord(c):x}" for c in seq)]
        for name in dict.fromkeys(names):
            if name in self.used:
                return name
            if name in self.missing:
                continue
            dest = EMOJI_CACHE / f"{name}.png"
            try:
                fetch(TWEMOJI.format(name), dest)
                self.used[name] = dest
                return name
            except (urllib.error.HTTPError, urllib.error.URLError):
                self.missing.add(name)
        return None

    def replace(self, root: Tag, soup: BeautifulSoup) -> None:
        for text in list(root.find_all(string=True)):
            if text.find_parent(["pre", "code", "script", "style", "title"]):
                continue
            found = emoji_lib.emoji_list(str(text))
            if not found:
                continue
            pieces, last = [], 0
            s = str(text)
            for item in found:
                pieces.append(s[last:item["match_start"]])
                name = self.path_for(item["emoji"])
                if name:
                    img = soup.new_tag("img", attrs={"class": "emoji", "src": f"images/emoji/{name}.png",
                                                     "alt": item["emoji"]})
                    pieces.append(img)
                else:
                    pieces.append(item["emoji"])
                last = item["match_end"]
            pieces.append(s[last:])
            for piece in pieces:
                if piece == "":
                    continue
                text.insert_before(piece)
            text.extract()


# ----------------------------------------------------------------------------- diagrams
def render_diagrams(sources: list[str], out_dir: Path) -> list[bytes]:
    """Render Mermaid sources to PNGs with the same Mermaid build the PDF uses."""
    from playwright.sync_api import sync_playwright

    images: list[bytes] = []
    if not sources:
        return images
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception:
            browser = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        page = browser.new_page(viewport={"width": 760, "height": 600}, device_scale_factor=2)
        page.set_content('<html><body style="margin:0;background:#fff"><div id="o" '
                         'style="display:inline-block;padding:8px;background:#fff"></div></body></html>')
        page.add_script_tag(path=str(CACHE / "mermaid.min.js"))
        page.evaluate("""() => mermaid.initialize({ startOnLoad: false, theme: 'base', fontFamily: 'sans-serif',
            flowchart: { useMaxWidth: false, htmlLabels: true },
            themeVariables: { primaryColor: '#ede9fe', primaryBorderColor: '#8b5cf6', primaryTextColor: '#1f1147',
                              lineColor: '#7c3aed', fontSize: '15px', clusterBkg: '#faf9ff', clusterBorder: '#c4b5fd' } })""")
        for i, src in enumerate(sources):
            page.evaluate("""async ([s, id]) => {
                const { svg } = await mermaid.render(id, s);
                const o = document.getElementById('o'); o.innerHTML = svg;
                const el = o.querySelector('svg'); el.style.maxWidth = '740px'; el.removeAttribute('height');
            }""", [src, f"d{i}"])
            images.append(page.locator("#o").screenshot(type="png"))
        browser.close()
    return images


# ----------------------------------------------------------------------------- book assembly
def xhtml(title: str, body: str, epub_type: str = "") -> str:
    attr = f' epub:type="{epub_type}"' if epub_type else ""
    return XHTML_HEAD.format(title=html.escape(title)) + f"<body{attr}>\n{body}\n</body>\n</html>\n"


def to_xml(fragment: BeautifulSoup | Tag) -> str:
    """bs4 serializes void tags as <br/> and quotes every attribute, which is valid XHTML."""
    return fragment.decode(formatter="minimal")


def fix_tree(root: Tag, kind: str) -> None:
    # headings: chapters get h1 from the opener, so sections become h2 again
    levels = {"sec": "h2", "sub": "h3", "subsub": "h4"}
    for h in root.find_all(re.compile(r"^h[1-6]$")):
        cls = (h.get("class") or [""])[0]
        if cls in levels:
            h.name = levels[cls]
    for el in root.select("span.pref, span.pg, svg, .md-button, iframe, video, audio"):
        el.decompose()
    for el in root.find_all(True):
        for attr in [a for a in el.attrs if a in ("markdown", "onclick", "target", "data-md-component")
                     or (a.startswith("data-") and a not in ("data-chapter",))]:
            del el[attr]
        if el.name == "a" and el.get("href", "").startswith("javascript:"):
            del el["href"]
    for table in root.find_all("table"):
        for attr in ("cellpadding", "cellspacing", "border"):
            if attr in table.attrs:
                del table[attr]


def build(site: Path, out: Path, cover_pdf: Path | None) -> None:
    prepare_assets()
    docs = build_docs(site)
    emojis = EmojiImages()

    # ---- parse every page body and work out which file each id lives in
    files: list[tuple[str, str]] = []  # (filename, xhtml)
    trees: dict[str, BeautifulSoup] = {}
    id_file: dict[str, str] = {}
    for doc in docs:
        tree = BeautifulSoup(f"<div>{doc.body}</div>", "lxml")
        trees[doc.anchor] = tree
        name = f"{doc.anchor}.xhtml"
        id_file[doc.anchor] = name
        for el in tree.find_all(id=True):
            id_file.setdefault(el["id"], name)

    # ---- diagrams
    diagram_srcs, diagram_divs = [], []
    for doc in docs:
        for div in trees[doc.anchor].select("div.diagram"):
            src = div.select_one("script.mermaid-src")
            if src is not None:
                diagram_srcs.append(src.get_text())
                diagram_divs.append(div)
    print(f"🧜 Rendering {len(diagram_srcs)} diagrams…")
    pngs = render_diagrams(diagram_srcs, out.parent)
    images: dict[str, bytes] = {}
    for i, (div, png) in enumerate(zip(diagram_divs, pngs)):
        name = f"images/diagram-{i + 1:03d}.png"
        images[name] = png
        soup = BeautifulSoup("", "lxml")
        fig = soup.new_tag("figure", attrs={"class": "diagram"})
        fig.append(soup.new_tag("img", attrs={"src": name, "alt": f"Diagram {i + 1}"}))
        div.replace_with(fig)

    # ---- page files
    toc_entries: list[tuple[int, str, str]] = []  # (level, title, href)
    by_part: dict[str, list] = {}
    for doc in docs:
        tree = trees[doc.anchor]
        root = tree.div
        name = id_file[doc.anchor]
        soup = BeautifulSoup("", "lxml")

        # links: in-book jumps → file#id
        for a in root.select("figure.shot > a"):  # screenshots link to themselves on the site
            a.unwrap()
        for a in root.find_all("a", href=True):
            href = a["href"]
            if href.startswith("#"):
                target = href[1:]
                dest = id_file.get(target)
                if dest is None:
                    del a["href"]
                else:
                    a["href"] = dest if target == dest[: -len(".xhtml")] else f"{dest}#{target}"
        # images from the site → copied into the book
        for img in root.find_all("img"):
            src = img.get("src", "")
            if not src or src.startswith("images/"):
                continue
            if src.startswith(("http://", "https://", "data:")):
                img.replace_with(img.get("alt", ""))
                continue
            path = (site / doc.key / unquote(urlsplit(src).path)).resolve()
            if not path.exists():
                img.replace_with(img.get("alt", ""))
                continue
            key = f"images/site/{path.name}"
            images[key] = path.read_bytes()
            img["src"] = key
            img.attrs = {k: v for k, v in img.attrs.items() if k in ("src", "alt", "class")}
            img["alt"] = img.get("alt", "")
        fix_tree(root, doc.kind)

        title_plain = plain(doc.title) or doc.title
        if doc.kind == "welcome":
            head = f'<h1 id="{doc.anchor}">Welcome</h1>'
            page_title, etype = "Welcome", "chapter"
            toc_entries.append((1, "👋 Welcome", name))
        elif doc.kind == "part":
            label, emoji_char = PARTS[doc.folder]
            kicker, _, pname = label.partition(" · ")
            if not pname:
                kicker, pname = {"start-here": "Before you begin", "appendices": "The reference shelf"}.get(
                    doc.folder, ""), label
            lead = doc.extras.get("lead", "")
            points = doc.extras.get("keypoints", "")
            chapters = [d for d in docs if d.kind == "chapter" and d.folder == doc.folder]
            items = "".join(f'<p class="toc-ch"><a href="{d.anchor}.xhtml">{html.escape(plain(d.short) or d.short)}</a></p>'
                            for d in chapters)
            head = (f'<p class="kicker">{html.escape(kicker)}</p>'
                    f'<h1 id="{doc.anchor}">{emoji_char} {html.escape(pname)}</h1>{lead}'
                    + (f'<div class="box keypoints"><p class="box-title">✅ Key points</p>{points}</div>' if points else "")
                    + (f'<h2>{"In this part" if doc.folder.startswith("part-") else "Inside"}</h2>'
                       f'<div class="toc-chapters">{items}</div>' if items else ""))
            page_title, etype = label, "part"
            toc_entries.append((1, f"{emoji_char} {label}", name))
            by_part[doc.folder] = [doc, chapters]
        else:
            num, rest = split_title(doc.title)
            kicker = PART_OF_BOOK.get(doc.folder, PARTS[doc.folder][0])
            if doc.folder == "appendices" and num:
                kicker = f"Appendix {num}"
            head = (f'<header class="opener"><p class="kicker">{html.escape(kicker)}</p>'
                    f'<h1 id="{doc.anchor}">{html.escape(doc.title)}</h1></header>')
            page_title, etype = title_plain, "chapter"
            toc_entries.append((2, doc.title, name))
            for h in root.find_all("h2", id=True):
                toc_entries.append((3, h.get_text(" ", strip=True), f"{name}#{h['id']}"))

        page = BeautifulSoup(f"<section>{head}</section>", "lxml").section
        page["epub:type"] = etype
        page.extend(list(root.contents))
        wrapper = BeautifulSoup("<div></div>", "lxml").div
        wrapper.append(page)
        emojis.replace(wrapper, soup)
        files.append((name, xhtml(page_title, to_xml(page))))

    # ---- front matter: title page and HTML contents
    stats = next((d.extras.get("stats", []) for d in docs if d.kind == "welcome"), [])
    edition = datetime.date.today().strftime("%B %Y")
    stat_line = " · ".join(f"{s} {label}" for s, label in stats[:4])
    title_html = (f'<section epub:type="titlepage" class="titlepage"><h1>🚀 {TITLE}</h1>'
                  '<p class="subtitle">From your very first chat to building your own agents: a friendly, '
                  'hands-on guide for everyone</p>'
                  f'<p>{html.escape(stat_line)}</p><p>{edition} edition</p>'
                  f'<p><a href="{SITE_URL}">{SITE_URL.removeprefix("https://").rstrip("/")}</a></p></section>')
    toc_body = ['<nav epub:type="toc" id="toc-page"><h1>Contents</h1>', '<p><a href="pg0.xhtml">👋 Welcome</a></p>']
    for folder, (part_doc, chapters) in by_part.items():
        label, emoji_char = PARTS[folder]
        toc_body.append(f'<p class="toc-part"><a href="{part_doc.anchor}.xhtml">{emoji_char} {html.escape(label)}</a></p>')
        if chapters:
            toc_body.append('<div class="toc-chapters">' + "".join(
                f'<p class="toc-ch"><a href="{d.anchor}.xhtml">{html.escape(plain(d.short) or d.short)}</a></p>'
                for d in chapters) + "</div>")
    toc_body.append("</nav>")
    colophon = (
        '<section epub:type="colophon"><h1>About this book</h1>'
        f"<p>{TITLE} is a free, open manual. The online edition is searchable and always up to date, and every "
        f'starter kit lives on GitHub:</p><p><a href="{SITE_URL}">{SITE_URL.removeprefix("https://").rstrip("/")}</a>'
        f'<br/><a href="{REPO_URL}">{REPO_URL.removeprefix("https://")}</a></p>'
        f"<p>This ebook edition was generated on {datetime.date.today().isoformat()}. Diagrams are rendered with "
        "Mermaid. Emoji graphics are from Twemoji, © Twitter, Inc and other contributors, licensed under "
        'CC-BY 4.0 (<a href="https://creativecommons.org/licenses/by/4.0/">creativecommons.org/licenses/by/4.0</a>).</p>'
        "<p>Made with ❤️ and Claude Code.</p></section>"
    )
    front = []
    for name, title, body, etype in [
        ("title.xhtml", TITLE, title_html, ""),
        ("contents.xhtml", "Contents", "\n".join(toc_body), ""),
        ("colophon.xhtml", "About this book", colophon, ""),
    ]:
        tree = BeautifulSoup(f"<div>{body}</div>", "lxml")
        emojis.replace(tree.div, tree)
        front.append((name, xhtml(title, "".join(to_xml(c) for c in tree.div.contents), etype)))

    # ---- cover
    cover_bytes = None
    if cover_pdf and cover_pdf.exists():
        import pymupdf

        with pymupdf.open(cover_pdf) as pdf:
            page = pdf[0]
            zoom = 1600 / page.rect.width
            cover_bytes = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom)).tobytes("jpg", jpg_quality=88)
    elif (site / "assets/pdf/cover.jpg").exists():
        cover_bytes = (site / "assets/pdf/cover.jpg").read_bytes()
    cover_page = ('<section epub:type="cover" class="cover"><img src="images/cover.jpg" alt="Cover of '
                  f'{TITLE}"/></section>') if cover_bytes else ""

    # ---- navigation documents
    entries = [(1, "Contents", "contents.xhtml")] + toc_entries + [(1, "About this book", "colophon.xhtml")]
    tree: list[dict] = []  # nested: {"text", "href", "kids"}
    path: list[tuple[int, list]] = [(0, tree)]
    ncx_points, play = [], 0
    for level, title, href in entries:
        text = html.escape(plain(title) or title)
        while path[-1][0] >= level:
            path.pop()
        node = {"text": text, "href": href, "kids": []}
        path[-1][1].append(node)
        path.append((level, node["kids"]))
        if level <= 2:
            play += 1
            ncx_points.append((level, text, href, play))

    def render(nodes: list[dict]) -> str:
        return "<ol>" + "".join(
            f'<li><a href="{n["href"]}">{n["text"]}</a>{render(n["kids"]) if n["kids"] else ""}</li>' for n in nodes
        ) + "</ol>"

    nav = ['<nav epub:type="toc" id="toc"><h1>Contents</h1>', render(tree), "</nav>"]
    nav.append('<nav epub:type="landmarks" hidden=""><ol>'
               + ('<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>' if cover_bytes else "")
               + '<li><a epub:type="toc" href="contents.xhtml">Contents</a></li>'
               '<li><a epub:type="bodymatter" href="pg0.xhtml">Start of content</a></li></ol></nav>')
    nav_xhtml = xhtml("Contents", "".join(nav))

    ncx = ['<?xml version="1.0" encoding="utf-8"?>\n<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
           f'<head><meta name="dtb:uid" content="{BOOK_ID}"/></head><docTitle><text>{TITLE}</text></docTitle><navMap>']
    open_part = False
    for level, text, href, n in ncx_points:
        if level == 1:
            if open_part:
                ncx.append("</navPoint>")
            ncx.append(f'<navPoint id="n{n}" playOrder="{n}"><navLabel><text>{text}</text></navLabel>'
                       f'<content src="{href}"/>')
            open_part = True
        else:
            ncx.append(f'<navPoint id="n{n}" playOrder="{n}"><navLabel><text>{text}</text></navLabel>'
                       f'<content src="{href}"/></navPoint>')
    if open_part:
        ncx.append("</navPoint>")
    ncx.append("</navMap></ncx>")

    # ---- manifest and spine
    css = CSS + HtmlFormatter(style="friendly").get_style_defs(".highlight")
    spine = (["cover.xhtml"] if cover_bytes else []) + ["title.xhtml", "contents.xhtml"] + \
        [n for n, _ in files] + ["colophon.xhtml"]
    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                '<item id="css" href="css/book.css" media-type="text/css"/>']
    if cover_bytes:
        manifest.append('<item id="cover-image" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
    for i, n in enumerate(spine):
        manifest.append(f'<item id="p{i}" href="{n}" media-type="application/xhtml+xml"/>')
    all_images = dict(images)
    for name, path in emojis.used.items():
        all_images[f"images/emoji/{name}.png"] = path.read_bytes()
    for i, n in enumerate(sorted(all_images)):
        mt = "image/png" if n.endswith(".png") else "image/jpeg" if n.endswith((".jpg", ".jpeg")) else \
            "image/svg+xml" if n.endswith(".svg") else "image/gif"
        manifest.append(f'<item id="img{i}" href="{n}" media-type="{mt}"/>')
    modified = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    opf = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en">'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
        f'<dc:identifier id="bookid">{BOOK_ID}</dc:identifier><dc:title>{TITLE}</dc:title>'
        '<dc:creator>The Massive AI Manual contributors</dc:creator><dc:language>en</dc:language>'
        f'<dc:date>{datetime.date.today().isoformat()}</dc:date>'
        '<dc:description>A free, friendly, hands-on manual for everyone, from your first AI chat to building your own '
        'agents: every major assistant, MCP, automation, n8n and Notion, local AI, creative AI and real life.</dc:description>'
        f'<meta property="dcterms:modified">{modified}</meta>'
        + ('<meta name="cover" content="cover-image"/>' if cover_bytes else "")
        + '</metadata><manifest>' + "".join(manifest) + '</manifest><spine toc="ncx">'
        + "".join(f'<itemref idref="p{i}"/>' for i in range(len(spine))) + "</spine></package>"
    )

    # ---- write the zip (mimetype first, uncompressed)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0" encoding="utf-8"?>\n<container version="1.0" '
                   'xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles>'
                   '<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
                   "</rootfiles></container>", compress_type=zipfile.ZIP_DEFLATED)
        put = lambda name, data: z.writestr(f"OEBPS/{name}", data, compress_type=zipfile.ZIP_DEFLATED)  # noqa: E731
        put("content.opf", opf)
        put("nav.xhtml", nav_xhtml)
        put("toc.ncx", "".join(ncx))
        put("css/book.css", css)
        if cover_bytes:
            put("images/cover.jpg", cover_bytes)
            put("cover.xhtml", xhtml(f"{TITLE}: cover", cover_page))
        for name, data in front + files:
            put(name, data)
        for name, data in all_images.items():
            put(name, data)
    size = out.stat().st_size / 1048576
    print(f"✅ Wrote {out} · {len(files)} pages · {len(images)} diagrams/images · {len(emojis.used)} emoji · "
          f"{size:.1f} MB" + (f" · emoji kept as text: {len(emojis.missing)}" if emojis.missing else ""))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", type=Path, default=ROOT / "site", help="built site folder (default: site/)")
    ap.add_argument("--out", type=Path, default=ROOT / "MANUAL.epub")
    ap.add_argument("--cover-pdf", type=Path, default=ROOT / "MANUAL.pdf",
                    help="use page 1 of this PDF as the cover (default: MANUAL.pdf, if it exists)")
    args = ap.parse_args()
    build(args.site, args.out, args.cover_pdf)


if __name__ == "__main__":
    main()
