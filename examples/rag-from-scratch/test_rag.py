"""Offline retrieval tests (no API key needed):  python test_rag.py"""

from pathlib import Path

from rag import Index, chunk_notes

index = Index(chunk_notes(Path(__file__).parent / "notes"))
cases = {
    "how do I descale the coffee machine": "Descaling",
    "grinder jammed error": "Error codes",
    "basil cold nights": "Herbs",
    "lemon cake oven temperature": "lemon cake",
}
for question, expected in cases.items():
    top = index.search(question, k=1)[0][1]["source"]
    assert expected in top, f"{question!r} → {top}"
    print(f"✅ {question!r} → {top}")
