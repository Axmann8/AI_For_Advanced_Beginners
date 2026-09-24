"""
🤖 Build Your Own Agent: the agent loop, demystified.

About 100 lines that show *exactly* what every AI agent does under the hood:

    goal → model thinks → calls a tool → gets the result → thinks again → … → final answer

Tools this agent has (all local and harmless):
    calculator   evaluate a math expression safely
    list_files   see what's in ./workspace
    read_file    read a file from ./workspace
    now          get the current date and time

Run it:
    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=sk-ant-...      # or `ant auth login`
    python agent.py "How much will the party shopping list cost in total, and what's still left on my to-do list?"
"""

import ast
import operator
import sys
from datetime import datetime
from pathlib import Path

import anthropic

MODEL = "claude-opus-5"
WORKSPACE = Path(__file__).parent / "workspace"
MAX_TURNS = 10  # safety valve: agents should always have a stopping point

# ---------------------------------------------------------------- tools ---
# 1) Tell the model what tools exist. Names + descriptions are its "manual".
TOOLS = [
    {
        "name": "calculator",
        "description": "Evaluate an arithmetic expression like '3*4.5 + 2*5.25'. Use for any math.",
        "input_schema": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"],
        },
    },
    {
        "name": "list_files",
        "description": "List the files available in the workspace folder.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "read_file",
        "description": "Read a text file from the workspace folder by name, e.g. 'todo.md'.",
        "input_schema": {
            "type": "object",
            "properties": {"name": {"type": "string"}},
            "required": ["name"],
        },
    },
    {
        "name": "now",
        "description": "Get the current local date and time.",
        "input_schema": {"type": "object", "properties": {}},
    },
]

# 2) Implement them. The model never runs these: *your code* does.
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
       ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg}


def safe_eval(node):
    """Evaluate +, -, *, /, ** on numbers only (no eval() of arbitrary code!)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](safe_eval(node.operand))
    raise ValueError("Only numbers and + - * / ** are allowed")


def run_tool(name: str, args: dict) -> str:
    if name == "calculator":
        return str(round(safe_eval(ast.parse(args["expression"], mode="eval").body), 4))
    if name == "list_files":
        return "\n".join(sorted(p.name for p in WORKSPACE.iterdir() if p.is_file()))
    if name == "read_file":
        path = (WORKSPACE / args["name"]).resolve()
        if WORKSPACE.resolve() not in path.parents:  # no escaping the sandbox folder
            raise ValueError("That file is outside the workspace")
        return path.read_text(encoding="utf-8")
    if name == "now":
        return datetime.now().strftime("%A %Y-%m-%d %H:%M")
    raise ValueError(f"Unknown tool: {name}")


# ----------------------------------------------------------- the loop ---
def run_agent(goal: str) -> str:
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": goal}]

    for turn in range(1, MAX_TURNS + 1):
        # 3) Ask the model what to do next, given everything so far.
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=16000,
            system="You are a cheerful, precise assistant. Use tools instead of guessing.",
            tools=TOOLS,
            messages=messages,
            # If a request is ever declined by a safety classifier, let the API retry it on a fallback model.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )

        if response.stop_reason == "refusal":
            return "🙅 The request was declined."

        # 4) Remember what the model said (including its tool requests).
        messages.append({"role": "assistant", "content": response.content})

        tool_calls = [b for b in response.content if b.type == "tool_use"]
        if not tool_calls:  # no tools requested → the model is done!
            return "".join(b.text for b in response.content if b.type == "text")

        # 5) Run each requested tool and hand back ALL results in one message.
        results = []
        for call in tool_calls:
            try:
                output, is_error = run_tool(call.name, call.input), False
            except Exception as exc:  # tell the model what went wrong so it can adapt
                output, is_error = f"Error: {exc}", True
            print(f"  🔧 turn {turn}: {call.name}({call.input}) → {output[:70]!r}")
            results.append({"type": "tool_result", "tool_use_id": call.id,
                            "content": output, "is_error": is_error})
        messages.append({"role": "user", "content": results})

    return "⏱️ Stopped after reaching the turn limit."


if __name__ == "__main__":
    goal = " ".join(sys.argv[1:]) or (
        "How much will the party shopping list cost in total, "
        "and what's still left on my to-do list?"
    )
    print(f"🎯 Goal: {goal}\n")
    print(f"\n✅ {run_agent(goal)}")
