"""Stitch the whole manual into one giant Markdown file: great for printing,
reading offline, or handing to an AI as context.

    python scripts/build_single_file.py            # writes MANUAL.md
    python scripts/build_single_file.py out.md     # custom output path
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sync_manual import MANUAL, PARTS, pages_in  # noqa: E402

REPO = "https://github.com/Axmann8/AI_For_Advanced_Beginners/blob/main"


def main(out: Path) -> None:
    toc = ["# The Massive AI Manual 🚀", "", "## Table of Contents", ""]
    body: list[str] = []
    for folder, (label, emoji) in PARTS.items():
        pages = pages_in(folder)
        if not pages:
            continue
        toc.append(f"- **{emoji} {label}**")
        body += ["", f"# {emoji} {label}", ""]
        for page in pages:
            toc.append(f"  - {page.h1}")
            text = page.text
            rel_dir = page.path.parent.relative_to(MANUAL.parent).as_posix()
            # links between files don't survive concatenation, so point them at GitHub
            text = re.sub(
                r"\]\((?!https?://|#)([^)\s]+)\)",
                lambda m: f"]({REPO}/{rel_dir}/{m.group(1)})",
                text,
            )
            text = re.sub(r"^# ", "## ", text, count=1, flags=re.M)
            body += ["", "---", "", text]
    out.write_text("\n".join(toc + body) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("MANUAL.md"))
