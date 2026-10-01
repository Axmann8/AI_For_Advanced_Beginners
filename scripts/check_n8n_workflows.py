"""Sanity-check every importable n8n workflow in examples/ (run in CI).

    python scripts/check_n8n_workflows.py

For each workflow JSON it checks that: node names are unique, every connection points at a node that exists, every
node has a type, version and position, and the workflow has at least one trigger.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRIGGER_HINTS = ("Trigger", "webhook", "mcpTrigger", "chatTrigger", "formTrigger")


def check(path: Path) -> list[str]:
    wf = json.loads(path.read_text(encoding="utf-8"))
    problems: list[str] = []
    nodes = wf.get("nodes", [])
    names = [n.get("name") for n in nodes]
    if len(names) != len(set(names)):
        problems.append("duplicate node names")
    for n in nodes:
        for key in ("name", "type", "typeVersion", "position", "parameters"):
            if key not in n:
                problems.append(f"node {n.get('name', '?')} is missing '{key}'")
    known = set(names)
    for src, kinds in wf.get("connections", {}).items():
        if src not in known:
            problems.append(f"connection from unknown node '{src}'")
        for outputs in kinds.values():
            for output in outputs:
                for target in output:
                    if target.get("node") not in known:
                        problems.append(f"'{src}' connects to unknown node '{target.get('node')}'")
    if not any(any(h.lower() in n.get("type", "").lower() for h in TRIGGER_HINTS) for n in nodes):
        problems.append("no trigger node")
    return problems


def main() -> int:
    files = sorted(p for p in (ROOT / "examples").rglob("*.json")
                   if "node_modules" not in p.parts and '"nodes"' in p.read_text(encoding="utf-8")[:4000])
    failed = 0
    for f in files:
        problems = check(f)
        rel = f.relative_to(ROOT)
        if problems:
            failed += 1
            print(f"❌ {rel}")
            for p in problems:
                print(f"   - {p}")
        else:
            print(f"✅ {rel}")
    print(f"{len(files)} workflow(s) checked, {failed} with problems")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
