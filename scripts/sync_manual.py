"""Keep the whole manual in sync with its files. Run after adding or editing chapters:

    python scripts/sync_manual.py            # regenerate everything
    python scripts/sync_manual.py --check    # only lint, don't write (used in CI)

It regenerates:
  * the `nav:` block in mkdocs.yml (parts → chapters, with part landing pages)
  * every page's closing "**Next:**" link, in reading order
  * the "⏱️ N min read" chip from the real word count
  * chapter cards on each part landing page     (<!-- chapters:start/end -->)
  * part cards + stats on the home page          (<!-- parts / stats / progress -->)
  * the chapter table in README.md               (<!-- toc:start/end -->)
  * appendices/g-eli5-edition.md: the whole manual explained like you're five

And it lints: numbering, balanced <details>, the chapter-level ELI5, the section map marker, and an
ELI5 for every section ("ELI5 for everything" is a promise!).
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUAL = ROOT / "manual"

# folder → (nav label, emoji). Order here is the reading order.
PARTS: dict[str, tuple[str, str]] = {
    "start-here": ("Start Here", "🧭"),
    "part-1-ai-from-zero": ("Part I · AI from Zero", "🐣"),
    "part-2-ai-assistants-field-guide": ("Part II · The AI Assistants Field Guide", "🤖"),
    "part-3-foundations": ("Part III · Foundations", "🧠"),
    "part-4-mcp-and-connectors": ("Part IV · MCP & Connectors", "🔌"),
    "part-5-automation": ("Part V · Automation", "⚙️"),
    "part-6-ai-in-your-apps": ("Part VI · AI in Your Apps", "🏡"),
    "part-7-building-with-ai": ("Part VII · Building with AI", "🛠️"),
    "part-8-knowledge-and-memory": ("Part VIII · Knowledge & Memory", "📚"),
    "part-9-local-ai": ("Part IX · Local AI", "🏠"),
    "part-10-creative-ai": ("Part X · Creative AI", "🎨"),
    "part-11-ai-for-life-and-work": ("Part XI · AI for Life & Work", "🌱"),
    "part-12-mastery": ("Part XII · Mastery", "🏆"),
    "part-13-build-alongs": ("Part XIII · Build-Alongs", "🧱"),
    "appendices": ("Appendices", "📎"),
}
SECTION_EXEMPT = re.compile(r"(key takeaways|check yourself|quick quiz|try this|what's next|next steps)", re.I)
WORDS_PER_MINUTE = 220
ELI5_EDITION = MANUAL / "appendices" / "g-eli5-edition.md"


@dataclass
class Page:
    path: Path
    folder: str

    @property
    def text(self) -> str:
        return self.path.read_text(encoding="utf-8")

    @property
    def rel(self) -> str:
        return self.path.relative_to(MANUAL).as_posix()

    @property
    def is_chapter(self) -> bool:
        return self.folder.startswith("part-") and bool(re.match(r"\d{2,3}-", self.path.name))

    @property
    def h1(self) -> str:
        for line in self.text.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return self.path.stem

    @property
    def nav_title(self) -> str:
        """Short title for the nav: '07 · MCP Explained' (drops subtitle and trailing emoji).

        Build-alongs are titled '81 · Build-Along: Your Pocket AI Assistant…', so for those the part
        after the colon is the useful bit: '81 · Your Pocket AI Assistant…'.
        """
        head, _, rest = self.h1.partition(":")
        if head.strip().endswith("Build-Along") and rest.strip():
            number = head.split("·")[0].strip()
            head = f"{number} · {rest.strip()}"
        return re.sub(r"[^\w)&'!?.]+$", "", head.strip())


def pages_in(folder: str) -> list[Page]:
    d = MANUAL / folder
    if not d.is_dir():
        return []
    def order(p: Path) -> tuple[int, str]:
        m = re.match(r"(\d+)-", p.name)
        return (int(m[1]) if m else -1, p.name)

    files = sorted((p for p in d.glob("*.md") if p.name != "index.md"), key=order)
    return [Page(p, folder) for p in files]


def all_pages() -> list[Page]:
    return [p for folder in PARTS for p in pages_in(folder)]


def rel(target: Path, frm: Path) -> str:
    return os.path.relpath(target, frm.parent).replace(os.sep, "/")


def replace_block(text: str, name: str, content: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:start -->)(.*?)(<!-- {name}:end -->)", re.S)
    if not pattern.search(text):
        return text
    return pattern.sub(lambda m: f"{m.group(1)}\n{content}\n{m.group(3)}", text)


# ------------------------------------------------------------------ parsing helpers ---
DETAILS_OPEN_ELI5 = re.compile(r'<details class="eli5" open>\s*\n<summary>.*?</summary>\s*\n(.*?)\n</details>', re.S)


def strip_code(text: str) -> str:
    return re.sub(r"^([ \t]*)(`{3,}|~{3,}).*?^\1\2[ \t]*$", "", text, flags=re.M | re.S)


def word_count(text: str) -> int:
    body = re.sub(r"<[^>]+>", " ", strip_code(text))
    return len(re.findall(r"[A-Za-z0-9']+", body))


def meta_line(text: str) -> str:
    m = re.search(r"^> (⏱.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def lead(text: str) -> str:
    """First real paragraph after the H1/meta line, trimmed to one or two sentences."""
    body = text.split("\n", 1)[1] if "\n" in text else ""
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block.startswith((">", "<", "#", "|", "-", "*   ", "```", "!!!", "???")):
            continue
        plain = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", block)
        plain = re.sub(r"[*_`]", "", plain).replace("\n", " ")
        sentences = re.split(r"(?<=[.!?])\s+", plain)
        out = sentences[0]
        if len(out) < 90 and len(sentences) > 1:
            out += " " + sentences[1]
        return out.strip()
    return ""


def chapter_eli5(text: str) -> str:
    m = DETAILS_OPEN_ELI5.search(text)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------- anchor fixing ---
def _slugger():
    try:
        from pymdownx.slugs import slugify
        return slugify(case="lower")
    except Exception:  # pymdown-extensions not installed: skip anchor fixing
        return None


def heading_slugs(text: str, slug) -> set[str]:
    slugs = set()
    for m in re.finditer(r"^#{1,6} (.+)$", strip_code(text), re.M):
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", m.group(1))
        title = re.sub(r"[`*_]", "", title).strip()
        slugs.add(slug(title, "-"))
    return slugs


def fix_anchors(pages: list[Page]) -> int:
    """Make section links match real heading ids (e.g. emoji headings get a leading '-')."""
    slug = _slugger()
    if slug is None:
        return 0
    by_path = {p.path.resolve(): heading_slugs(p.text, slug) for p in pages}
    fixed = 0
    for p in pages:
        text = p.text

        def repair(m):
            nonlocal fixed
            target, frag = m.group(1), m.group(2)
            dest = (p.path.parent / target).resolve() if target else p.path.resolve()
            slugs = by_path.get(dest)
            if not slugs or frag in slugs:
                return m.group(0)
            norm = lambda s: re.sub(r"-+", "-", s).strip("-")
            for candidate in sorted(slugs):
                if norm(candidate) == norm(frag):
                    fixed += 1
                    return f"]({target}#{candidate})"
            return m.group(0)

        new = re.sub(r"\]\(((?:[^)#\s]+\.md)?)#([^)\s]+)\)", repair, text)
        if new != text:
            p.path.write_text(new, encoding="utf-8")
    return fixed


# ------------------------------------------------------------------------- lint ---
def lint(pages: list[Page]) -> list[str]:
    problems, seen_numbers = [], {}
    for p in pages:
        t = p.text
        if t.count("<details") != t.count("</details>"):
            problems.append(f"{p.rel}: unbalanced <details> tags")
        if p.is_chapter:
            num = p.path.name.split("-")[0]
            if not p.h1.startswith(f"{num} · "):
                problems.append(f"{p.rel}: H1 should start with '{num} · '")
            if num in seen_numbers:
                problems.append(f"{p.rel}: duplicate chapter number {num} (also {seen_numbers[num]})")
            seen_numbers[num] = p.rel
            if not meta_line(t):
                problems.append(f"{p.rel}: missing '> ⏱️ …' meta line under the title")
            if not chapter_eli5(t):
                problems.append(f"{p.rel}: missing the chapter-level <details class=\"eli5\" open> box")
            if "<!-- in-this-chapter -->" not in t:
                problems.append(f"{p.rel}: missing <!-- in-this-chapter --> marker")
    return problems


def eli5_coverage(pages: list[Page]) -> tuple[int, int, list[str]]:
    """Every H2 section of a chapter should open with an ELI5 box."""
    total = covered = 0
    missing = []
    for p in pages:
        if not p.is_chapter:
            continue
        sections = re.split(r"^## ", strip_code(p.text), flags=re.M)[1:]
        for sec in sections:
            heading = sec.splitlines()[0]
            if SECTION_EXEMPT.search(heading):
                continue
            total += 1
            head = sec[:600]
            if 'class="eli5"' in head:
                covered += 1
            else:
                missing.append(f"{p.rel} › {heading.strip()}")
    return covered, total, missing


# ------------------------------------------------------------------------ writers ---
def sync_reading_time(page: Page) -> None:
    t = page.text
    minutes = max(3, round(word_count(t) / WORDS_PER_MINUTE))
    new = re.sub(r"^> ⏱️ \d+ min read", f"> ⏱️ {minutes} min read", t, count=1, flags=re.M)
    if new != t:
        page.path.write_text(new, encoding="utf-8")


def sync_next_links(order: list[Page]) -> None:
    for i, p in enumerate(order):
        if i + 1 < len(order):
            nxt = order[i + 1]
            line = f"**Next:** [{nxt.nav_title} →]({rel(nxt.path, p.path)})"
        else:
            line = f"**You made it to the end! 🎉** [Back to the manual home ↩]({rel(MANUAL / 'index.md', p.path)})"
        lines = p.text.rstrip("\n").split("\n")
        if lines and lines[-1].startswith(("**Next:**", "**You made it")):
            lines[-1] = line
        else:
            lines += ["", "---", "", line]
        p.path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def sync_nav() -> None:
    lines = ["nav:", f"  - {yaml_str('🏠 Home')}: index.md"]
    if (MANUAL / "download.md").exists():
        lines.append(f"  - {yaml_str('📄 Download the PDF')}: download.md")
    for folder, (label, emoji) in PARTS.items():
        pages = pages_in(folder)
        if not pages:
            continue
        lines.append(f"  - {yaml_str(f'{emoji} {label}')}:")
        if (MANUAL / folder / "index.md").exists():
            lines.append(f"      - {folder}/index.md")
        for p in pages:
            lines.append(f"      - {yaml_str(p.nav_title)}: {p.rel}")
    cfg = ROOT / "mkdocs.yml"
    text = cfg.read_text(encoding="utf-8")
    block = "# NAV:START (generated by scripts/sync_manual.py; do not edit by hand)\n" + "\n".join(lines) + "\n# NAV:END"
    cfg.write_text(re.sub(r"# NAV:START.*?# NAV:END", lambda _: block, text, flags=re.S), encoding="utf-8")


def ensure_part_index(folder: str) -> Path:
    index = MANUAL / folder / "index.md"
    if not index.exists():
        label, emoji = PARTS[folder]
        index.write_text(f"# {emoji} {label}\n\n<!-- chapters:start -->\n<!-- chapters:end -->\n", encoding="utf-8")
    return index


def card(p: Page, frm: Path) -> str:
    meta = meta_line(p.text)
    chips = " · ".join(meta.split(" · ")[:2]) if meta else ""
    blurb = lead(p.text)
    out = [f"-   **[{p.h1}]({rel(p.path, frm)})**", "", "    ---", ""]
    if chips:
        out += [f'    <span class="card-meta">{chips}</span>', ""]
    if blurb:
        out += [f"    {blurb}", ""]
    return "\n".join(out)


def sync_part_indexes() -> None:
    for folder in PARTS:
        pages = pages_in(folder)
        if not pages or folder == "appendices" and not (MANUAL / folder / "index.md").exists():
            continue
        index = ensure_part_index(folder)
        cards = "\n".join(card(p, index) for p in pages)
        grid = f'<div class="grid cards clickable" markdown>\n\n{cards}\n</div>'
        index.write_text(replace_block(index.read_text(encoding="utf-8"), "chapters", grid), encoding="utf-8")


def part_blurb(folder: str) -> str:
    index = MANUAL / folder / "index.md"
    return lead(index.read_text(encoding="utf-8")) if index.exists() else ""


def sync_home(pages: list[Page], coverage: tuple[int, int]) -> None:
    home = MANUAL / "index.md"
    if not home.exists():
        return
    text = home.read_text(encoding="utf-8")
    chapters = [p for p in pages if p.is_chapter]
    corpus = "\n".join(p.text for p in pages)
    eli5s = corpus.count('<details class="eli5"')
    quizzes = corpus.count('<details class="quiz"')
    tries = corpus.count("**🎮 Try this")
    words = sum(word_count(p.text) for p in pages)
    kits = len([d for d in (ROOT / "examples").iterdir() if d.is_dir()])
    stats = [
        (len(chapters), "chapters"),
        (eli5s, "ELI5 explanations 🧸"),
        (quizzes, "quiz questions"),
        (tries, "try-this challenges"),
        (kits, "starter kits"),
        (f"{round(words / 1000)}k", "words of fun"),
    ]
    stat_html = '<div class="hero-stats">' + "".join(
        f'<div class="stat"><strong>{n}</strong><span>{label}</span></div>' for n, label in stats
    ) + "</div>"
    text = replace_block(text, "stats", stat_html)
    text = replace_block(
        text, "progress", f'<div class="progress-tracker" data-total="{len(chapters)}"></div>'
    )
    part_cards = []
    for folder, (label, emoji) in PARTS.items():
        pgs = pages_in(folder)
        if not pgs or folder == "start-here":
            continue
        target = MANUAL / folder / "index.md"
        if not target.exists():
            target = pgs[0].path
        count = sum(p.is_chapter for p in pgs) or len(pgs)
        noun = "chapters" if any(p.is_chapter for p in pgs) else "pages"
        part_cards += [
            f"-   **{emoji} [{label}]({rel(target, home)})**",
            "",
            "    ---",
            "",
            f'    <span class="card-meta">{count} {noun}</span>',
            "",
            f"    {part_blurb(folder)}",
            "",
        ]
    grid = '<div class="grid cards clickable" markdown>\n\n' + "\n".join(part_cards) + "\n</div>"
    text = replace_block(text, "parts", grid)
    home.write_text(text, encoding="utf-8")


def sync_readme() -> None:
    readme = ROOT / "README.md"
    rows = ["| Part | Chapters |", "|---|---|"]
    for folder, (label, emoji) in PARTS.items():
        pgs = pages_in(folder)
        if not pgs:
            continue
        links = " · ".join(f"[{p.nav_title}](manual/{p.rel})" for p in pgs)
        rows.append(f"| **{emoji} {label}** | {links} |")
    text = readme.read_text(encoding="utf-8")
    readme.write_text(replace_block(text, "toc", "\n".join(rows)), encoding="utf-8")


def sync_eli5_edition() -> None:
    out = [
        "# Appendix G · The ELI5 Edition 🧸",
        "",
        "> ⏱️ 30 min read · 🎯 Everyone, including actual five-year-olds · 🧰 Needs: nothing at all",
        "",
        "**The entire manual, explained like you're five.** Every chapter's big idea in a few friendly sentences. "
        "Read it top to bottom for the whole story, or use it to decide which chapter to dive into next.",
        "",
        "> [!NOTE]",
        "> **📌 This page writes itself**",
        "> It's generated automatically from the 🧸 box at the top of every chapter (`python scripts/sync_manual.py`),",
        "> so it always matches the latest version of the manual.",
        "",
    ]
    for folder, (label, emoji) in PARTS.items():
        chapters = [p for p in pages_in(folder) if p.is_chapter]
        if not chapters:
            continue
        out += [f"## {emoji} {label}", ""]
        for p in chapters:
            eli5 = chapter_eli5(p.text)
            if not eli5:
                continue
            out += [f"### [{p.h1}]({rel(p.path, ELI5_EDITION)})", "", eli5, ""]
    ELI5_EDITION.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    check_only = "--check" in sys.argv
    if not check_only:
        sync_eli5_edition()
    pages = all_pages()
    problems = lint(pages)
    covered, total, missing = eli5_coverage(pages)
    if not check_only:
        fixed = fix_anchors(pages)
        if fixed:
            print(f"🔗 fixed {fixed} section link(s)")
        for p in pages:
            if p.is_chapter:
                sync_reading_time(p)
        order = [p for p in pages]  # start-here → parts → appendices
        sync_next_links(order)
        sync_nav()
        sync_part_indexes()
        sync_home(pages, (covered, total))
        sync_readme()
    chapters = sum(p.is_chapter for p in pages)
    print(f"📚 {len(pages)} pages ({chapters} chapters) · 🧸 section ELI5 coverage {covered}/{total}")
    for m in missing[:25]:
        print(f"   ELI5 missing: {m}")
    if len(missing) > 25:
        print(f"   … and {len(missing) - 25} more")
    for prob in problems:
        print(f"❌ {prob}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
