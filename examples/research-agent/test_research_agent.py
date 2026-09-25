"""Offline tests (no API key, no internet):   python test_research_agent.py"""

import tempfile
from pathlib import Path
from types import SimpleNamespace as NS

from research_agent import research, save_report, slugify


def block(**kw):
    return NS(**kw)


class FakeClient:
    """Plays back scripted responses, so we can test the agent loop without the API."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.messages = self

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self.responses.pop(0)


def test_slugify_and_save():
    assert slugify("Heat Pumps: Do They Work in -20°C?") == "heat-pumps-do-they-work-in-20-c"
    assert slugify("!!!") == "report"
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(save_report("My Report", "Body text", Path(tmp)))
        assert path.exists() and path.read_text().startswith("# My Report")
        assert path.parent == Path(tmp).resolve()


def test_full_loop_with_pause_and_save():
    report = "# Cold-climate heat pumps\n\n**TL;DR**\n- They work [1]\n\n## Sources\n[1] Example (https://example.com)"
    responses = [
        # 1) Claude searches (server-side), and the long turn gets paused
        NS(stop_reason="pause_turn", content=[
            block(type="text", text="Let me look into this."),
            block(type="server_tool_use", name="web_search", input={"query": "cold climate heat pump efficiency"}),
        ]),
        # 2) Claude calls our local tool to save the report
        NS(stop_reason="tool_use", content=[
            block(type="tool_use", id="toolu_1", name="save_report",
                  input={"title": "Cold-climate heat pumps", "markdown": report}),
        ]),
    ]
    client = FakeClient(responses)
    logs = []
    with tempfile.TemporaryDirectory() as tmp:
        path = research("Do heat pumps work in the cold?", "quick", client=client, reports_dir=Path(tmp), log=logs.append)
        assert path and Path(path).read_text().startswith("# Cold-climate heat pumps")
    assert len(client.calls) == 2, "pause_turn should trigger exactly one continuation"
    search_tool = next(t for t in client.calls[0]["tools"] if t.get("name") == "web_search")
    assert search_tool["max_uses"] == 4, "quick depth should cap searches"
    assert any("🔎 web_search" in line for line in logs)


def test_agent_that_never_saves():
    client = FakeClient([NS(stop_reason="end_turn", content=[block(type="text", text="Here you go.")])])
    assert research("anything", client=client, log=lambda *_: None) is None


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"✅ {name}")
    print("🎉 All research-agent tests passed.")
