---
name: inbox-triage
description: Triage the 00-Inbox folder of this second-brain vault. Use when the user says "triage my inbox", "sort my notes", "process my inbox" or "clean up the inbox".
---
# Inbox triage

1. List every note in `00-Inbox/` (skip `Welcome.md` unless asked).
2. For each note, decide:
   - **Project** (has a goal and finish line) → `01-Projects/`
   - **Area** (ongoing responsibility) → `02-Areas/`
   - **Resource** (reference or interest) → `03-Resources/`
   - **Archive** (done or no longer relevant) → `04-Archive/`
   - **Task** inside an existing project → append it to that project's "Next actions" instead of moving the note
3. Suggest 1–3 tags and up to 2 `[[wiki-links]]` to existing notes for each.
4. Show the plan as a table: note → destination → tags → links → reason. **Wait for the user's OK.**
5. After approval: move the notes, update front matter (`type`, `status`, `tags`), add links, and report what changed.

Never delete anything. Keep the user's original wording.
