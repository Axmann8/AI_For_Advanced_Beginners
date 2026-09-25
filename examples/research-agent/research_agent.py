"""
🔎 Research Agent: give it a question, get back a cited Markdown report.

How it works (the whole agent loop, visible):

    question → Claude plans → searches & reads the web (server-side tools)
             → calls save_report (our local tool) → report.md 🎉

Tools:
    web_search    run by Anthropic's servers: no search API key needed
    web_fetch     run by Anthropic's servers: reads full pages
    save_report   run by THIS script: writes the Markdown report into ./reports

Run it:
    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=sk-ant-...
    python research_agent.py "Which heat pumps work best in cold climates, and what do they cost to run?"
    python research_agent.py --depth quick "What's new in the Model Context Protocol this year?"

Server tool type names are versioned. If the API rejects them, check the docs for the current names.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import anthropic

MODEL = "claude-opus-5"
REPORTS_DIR = Path(__file__).parent / "reports"
MAX_TURNS = 12  # safety valve: every agent needs a stopping point

DEPTHS = {
    "quick": {"searches": 4, "words": "400–600"},
    "standard": {"searches": 8, "words": "800–1,200"},
    "deep": {"searches": 15, "words": "1,500–2,500"},
}

SYSTEM = """You are a meticulous, friendly research assistant.

Process:
1. Break the question into 3–5 sub-questions.
2. Search broadly, then read the most promising primary sources in full (official sites, papers, reputable outlets).
3. Cross-check important claims across at least two sources. Note disagreements honestly.
4. When you're done researching, call save_report exactly once with the finished report.

Report format (Markdown):
- A title, then a 3-bullet **TL;DR**.
- Sections that answer each sub-question, with inline citations like [1], [2].
- A "What's uncertain or debated" section.
- A "Sources" list: [n] Title (URL).
Never invent sources, numbers or quotes. If something couldn't be verified, say so.
Write for a smart, curious non-expert. Aim for {words} words."""


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return (slug[:60].rstrip("-") or "report")


def save_report(title: str, markdown: str, reports_dir: Path = REPORTS_DIR) -> str:
    """Write the report to reports/YYYY-MM-DD-<slug>.md and return the path. Never writes outside reports_dir."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = (reports_dir / f"{date.today().isoformat()}-{slugify(title)}.md").resolve()
    if reports_dir.resolve() not in path.parents:
        raise ValueError("Refusing to write outside the reports folder")
    if not markdown.lstrip().startswith("#"):
        markdown = f"# {title}\n\n{markdown}"
    path.write_text(markdown.rstrip() + "\n", encoding="utf-8")
    return str(path)


TOOLS = [
    {"type": "web_search_20260318", "name": "web_search", "max_uses": 8},
    {"type": "web_fetch_20260318", "name": "web_fetch", "max_uses": 8},
    {
        "name": "save_report",
        "description": "Save the finished research report as a Markdown file. Call this exactly once, at the end.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Short, descriptive report title"},
                "markdown": {"type": "string", "description": "The complete report in Markdown, including Sources"},
            },
            "required": ["title", "markdown"],
        },
    },
]


def research(question: str, depth: str = "standard", client=None, reports_dir: Path = REPORTS_DIR, log=print) -> str | None:
    """Run the agent loop. Returns the saved report path, or None if the agent never saved one."""
    client = client or anthropic.Anthropic()
    settings = DEPTHS[depth]
    tools = [dict(t) for t in TOOLS]
    for tool in tools:
        if tool.get("name") in ("web_search", "web_fetch"):
            tool["max_uses"] = settings["searches"]

    messages: list[dict] = [{"role": "user", "content": f"Research question: {question}"}]
    saved_path = None

    for turn in range(1, MAX_TURNS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=32000,
            system=SYSTEM.format(words=settings["words"]),
            tools=tools,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})

        for block in response.content:
            if block.type == "server_tool_use":
                query = block.input.get("query") or block.input.get("url") or ""
                log(f"  🔎 {block.name}: {query}")
            elif block.type == "text" and block.text.strip():
                log(f"  💭 {block.text.strip()[:120]}")

        if response.stop_reason == "pause_turn":
            # A long server-side tool turn was paused: send the conversation back so Claude can continue.
            continue

        tool_calls = [b for b in response.content if b.type == "tool_use"]
        if not tool_calls:
            break  # finished (or stopped) without more work to do

        results = []
        for call in tool_calls:
            if call.name == "save_report":
                try:
                    saved_path = save_report(call.input["title"], call.input["markdown"], reports_dir)
                    log(f"  💾 Saved report → {saved_path}")
                    results.append({"type": "tool_result", "tool_use_id": call.id, "content": f"Saved to {saved_path}"})
                except (KeyError, ValueError) as err:
                    results.append({"type": "tool_result", "tool_use_id": call.id, "content": str(err), "is_error": True})
            else:
                results.append({"type": "tool_result", "tool_use_id": call.id,
                                "content": f"Unknown tool {call.name}", "is_error": True})
        messages.append({"role": "user", "content": results})
        if saved_path:
            break
    else:
        log(f"  ⏹️ Stopped after {MAX_TURNS} turns (safety limit).")

    return saved_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Research any question and get a cited Markdown report.")
    parser.add_argument("question", help="What do you want researched?")
    parser.add_argument("--depth", choices=DEPTHS, default="standard")
    args = parser.parse_args()

    print(f"🧭 Researching ({args.depth}): {args.question}\n")
    path = research(args.question, args.depth)
    if path:
        print(f"\n🎉 Done! Open your report: {path}")
    else:
        print("\n😕 The agent finished without saving a report. Try again, or try --depth quick.")
        sys.exit(1)


if __name__ == "__main__":
    main()
