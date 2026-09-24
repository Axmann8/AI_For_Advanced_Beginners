"""
Pocket Toolkit: a tiny, friendly MCP server to learn the ropes.

It gives your AI assistant four new abilities:
  - roll_dice          roll any dice using tabletop notation ("2d6+3")
  - random_fortune     a fortune-cookie message for motivation
  - save_note          write a quick note to a local JSON file
  - list_notes         read your notes back (optionally filtered)

Plus one resource (notes://all) and one prompt template (daily_standup).

Written for the MCP Python SDK v2 (`pip install "mcp[cli]"`).
On the older v1 SDK, change the import to:
    from mcp.server.fastmcp import FastMCP as MCPServer
"""

from __future__ import annotations

import json
import random
import re
from datetime import datetime
from pathlib import Path

from mcp.server.mcpserver import MCPServer

mcp = MCPServer(
    "pocket-toolkit",
    instructions=(
        "A playful helper toolkit: dice rolling, fortunes, and a tiny local "
        "notes store. Use save_note when the user asks you to remember something."
    ),
)

NOTES_FILE = Path(__file__).parent / "notes.json"

FORTUNES = [
    "The bug you're hunting is in the file you haven't opened yet.",
    "A small automation today saves a hundred clicks tomorrow.",
    "You are one config file away from something awesome.",
    "Curiosity is your best debugger.",
    "Ship the weird little project. The weird ones teach the most.",
    "Your future self is already thanking you for writing that README.",
    "Great things are built one tool call at a time.",
]

DICE_PATTERN = re.compile(r"^\s*(\d*)d(\d+)\s*([+-]\s*\d+)?\s*$", re.IGNORECASE)


def _load_notes() -> list[dict]:
    if not NOTES_FILE.exists():
        return []
    return json.loads(NOTES_FILE.read_text(encoding="utf-8"))


@mcp.tool()
def roll_dice(notation: str = "1d20") -> str:
    """Roll dice using tabletop notation, e.g. '1d20', '4d6', '2d8+3'."""
    match = DICE_PATTERN.match(notation)
    if not match:
        return f"Couldn't parse '{notation}'. Try something like '2d6+1'."
    count = int(match.group(1) or 1)
    sides = int(match.group(2))
    modifier = int((match.group(3) or "0").replace(" ", ""))
    if not (1 <= count <= 100 and 2 <= sides <= 1000):
        return "Keep it between 1-100 dice with 2-1000 sides, adventurer."
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + modifier
    mod_text = f" {'+' if modifier >= 0 else '-'} {abs(modifier)}" if modifier else ""
    return f"🎲 {notation}: {rolls}{mod_text} = **{total}**"


@mcp.tool()
def random_fortune() -> str:
    """Return a random fortune-cookie message. Great for morale."""
    return f"🥠 {random.choice(FORTUNES)}"


@mcp.tool()
def save_note(text: str, tag: str = "general") -> str:
    """Save a short note to the local notes file, with an optional tag."""
    notes = _load_notes()
    notes.append(
        {"text": text, "tag": tag, "created": datetime.now().isoformat(timespec="seconds")}
    )
    NOTES_FILE.write_text(json.dumps(notes, indent=2), encoding="utf-8")
    return f"📝 Saved note #{len(notes)} with tag '{tag}'."


@mcp.tool()
def list_notes(tag: str | None = None) -> str:
    """List saved notes. Pass a tag to filter, or leave empty for all notes."""
    notes = _load_notes()
    if tag:
        notes = [n for n in notes if n["tag"] == tag]
    if not notes:
        return "No notes yet. Ask me to save one!"
    return "\n".join(f"- [{n['tag']}] {n['text']} ({n['created']})" for n in notes)


@mcp.resource("notes://all")
def all_notes() -> str:
    """All saved notes as raw JSON, which the client can attach as context."""
    return json.dumps(_load_notes(), indent=2)


@mcp.prompt()
def daily_standup(focus: str = "my projects") -> str:
    """A reusable prompt template: turn your notes into a standup update."""
    return (
        f"Read my notes with list_notes, then write a short, upbeat standup "
        f"update about {focus}: what I did, what I'm doing next, and any blockers."
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
