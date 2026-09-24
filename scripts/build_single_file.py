"""Stitch the whole manual into one giant Markdown file: great for printing,
reading offline, or handing to an AI as context.

    python scripts/build_single_file.py            # writes MANUAL.md
    python scripts/build_single_file.py out.md     # custom output path
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sync_manual import MANUAL, chapters, title_of  # noqa: E402

REPO = "https://github.com/Axmann8/claude_cloud_trial_credits/blob/main"


def main(out: Path) -> None:
    parts = chapters()
    toc, body = ["# AI for Advanced Beginners: The Massive Manual", "", "## Table of Contents", ""], []
    for label, files in parts:
        toc.append(f"- **{label}**")
        body += ["", f"# Part {label}", ""]
        for f in files:
            title = title_of(f)
            toc.append(f"  - {title}")
            text = f.read_text(encoding="utf-8")
            # links between files don't survive concatenation, so point them at GitHub
            rel_dir = f.parent.relative_to(MANUAL.parent).as_posix()
            text = re.sub(
                r"\]\((?!https?://|#)([^)\s]+)\)",
                lambda m: f"]({REPO}/{rel_dir}/{m.group(1)})",
                text,
            )
            body += ["", "---", "", text.replace("\n# ", "\n## ", 0)]
    out.write_text("\n".join(toc + body) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("MANUAL.md"))
