"""Offline tests for the agent's tools (no API key needed):  python test_tools.py"""

from agent import run_tool

assert run_tool("calculator", {"expression": "3*4.5 + 2*5.25"}) == "24.0"
assert "todo.md" in run_tool("list_files", {})
assert "birthday cake" in run_tool("read_file", {"name": "shopping.md"})
for bad in ({"expression": "__import__('os')"},):
    try:
        run_tool("calculator", bad)
        raise AssertionError("unsafe expression was evaluated")
    except ValueError:
        pass
try:
    run_tool("read_file", {"name": "../agent.py"})
    raise AssertionError("escaped the workspace")
except ValueError:
    pass
print("✅ all tool tests passed")
