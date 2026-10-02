"""Tiny stand-in for the Anthropic Messages API, so screenshots show realistic AI output without an API key.
Responses are picked by keywords in the prompt (sample data for documentation screenshots)."""
import json, sys, time
from http.server import BaseHTTPRequestHandler, HTTPServer

RESPONSES = [
    ("summarize this note", "Your landlord needs a reply by tonight on whether Thursday at 10am works for the boiler repair.\n\nUrgent: Yes"),
    ("triage", json.dumps({"title": "Renew car insurance before the 20th", "type": "Task", "priority": "High",
                           "summary": "Car insurance renews on the 20th. Check whether bundling it with home insurance is cheaper.",
                           "next_step": "Ask the current insurer for a bundled car + home quote"}, indent=2)),
    ("urgent", json.dumps({"summary": "The landlord is asking for access on Thursday at 10am to fix the boiler and needs a reply today.",
                           "urgent": True}, indent=2)),
    ("plan", json.dumps({"plan": "Compare three dentists near you, check what your insurance covers, then book the earliest slot before the 20th.",
                         "subtasks": ["Check insurance coverage for check-ups", "Shortlist three nearby dentists", "Call and book a slot before the 20th"]}, indent=2)),
    ("briefing", "Good morning! You have 3 things due today. Start with the insurance renewal (due at noon), then book the dentist. The team update can wait until after lunch."),
]
DEFAULT = "Here's a one-line summary: the message asks you to confirm Thursday's 10am meeting."

def pick(body):
    text = json.dumps(body).lower()
    if "summarize this note" in text and "insurance" in text:
        return "Renew your car insurance before the 20th and compare the price of bundling it with home insurance.\n\nUrgent: No"
    for key, resp in RESPONSES:
        if key in text:
            return resp
    return DEFAULT

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        if "models" in self.path:
            data = {"data": [{"id": m, "type": "model", "display_name": n, "created_at": "2026-01-01T00:00:00Z"}
                             for m, n in [("claude-sonnet-5-5", "Claude Sonnet 5.5"), ("claude-haiku-4-5", "Claude Haiku 4.5")]],
                    "has_more": False, "first_id": "claude-sonnet-5-5", "last_id": "claude-haiku-4-5"}
            return self._json(data)
        self._json({"ok": True})
    def do_POST(self):
        n = int(self.headers.get("content-length", 0))
        body = json.loads(self.rfile.read(n) or b"{}")
        text = pick(body)
        model = body.get("model", "claude-sonnet-5-5")
        msg = {"id": "msg_sample", "type": "message", "role": "assistant", "model": model,
               "content": [{"type": "text", "text": text}], "stop_reason": "end_turn", "stop_sequence": None,
               "usage": {"input_tokens": 120, "output_tokens": 60}}
        if not body.get("stream"):
            return self._json(msg)
        self.send_response(200); self.send_header("content-type", "text/event-stream"); self.end_headers()
        def ev(name, data):
            self.wfile.write(f"event: {name}\ndata: {json.dumps(data)}\n\n".encode()); self.wfile.flush()
        start = dict(msg, content=[], stop_reason=None); ev("message_start", {"type": "message_start", "message": start})
        ev("content_block_start", {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}})
        for i in range(0, len(text), 40):
            ev("content_block_delta", {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": text[i:i+40]}})
        ev("content_block_stop", {"type": "content_block_stop", "index": 0})
        ev("message_delta", {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": None}, "usage": {"output_tokens": 60}})
        ev("message_stop", {"type": "message_stop"})
    def _json(self, d):
        b = json.dumps(d).encode(); self.send_response(200); self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(b))); self.end_headers(); self.wfile.write(b)

HTTPServer(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 8788), H).serve_forever()
