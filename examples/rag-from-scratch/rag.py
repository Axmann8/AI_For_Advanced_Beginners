"""
📚 RAG from Scratch: chat with a folder of notes, and see every step.

    chunk → vectorize → search → answer (with citations)

The retrieval half is pure Python (no API key, no downloads), using TF-IDF vectors and cosine
similarity. That's the classic ancestor of embeddings, and it shows exactly how "find the relevant
bits" works. The answer half sends the best chunks to Claude.

    python rag.py --search "how do I descale the coffee machine"     # retrieval only, no key needed
    python rag.py "how do I descale the coffee machine?"               # full RAG answer (needs ANTHROPIC_API_KEY)
    python rag.py --notes ~/Obsidian/MyVault "what did I learn about sleep?"
"""

import argparse
import math
import re
from collections import Counter
from pathlib import Path

MODEL = "claude-opus-5"
STOPWORDS = set("a an and are as at be by for from has have how i in is it its of on or the to was what when where which with you your do does did my me".split())


# ------------------------------------------------------------ 1. chunk ---
def chunk_notes(folder: Path) -> list[dict]:
    """Split each Markdown file into chunks at headings: small, meaningful passages."""
    chunks = []
    for path in sorted(folder.rglob("*.md")):
        for section in re.split(r"\n(?=#{1,3} )", path.read_text(encoding="utf-8")):
            text = section.strip()
            heading, _, body = text.partition("\n")
            if len(body.strip()) > 30:  # skip heading-only fragments
                heading = heading.lstrip("# ").strip()
                chunks.append({"source": f"{path.name} › {heading}", "text": text})
    return chunks


# -------------------------------------------------------- 2. vectorize ---
def tokenize(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-zà-ÿ0-9]+", text.lower()) if w not in STOPWORDS and len(w) > 1]


class Index:
    """A tiny TF-IDF vector index. Real systems swap this for neural embeddings + a vector DB."""

    def __init__(self, chunks: list[dict]):
        self.chunks = chunks
        docs = [Counter(tokenize(c["text"] + " " + c["source"])) for c in chunks]
        df = Counter(term for d in docs for term in d)
        self.idf = {t: math.log((1 + len(docs)) / (1 + n)) + 1 for t, n in df.items()}
        self.vectors = [self._vector(d) for d in docs]

    def _vector(self, counts: Counter) -> dict[str, float]:
        vec = {t: (1 + math.log(n)) * self.idf.get(t, 0.0) for t, n in counts.items()}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        return {t: v / norm for t, v in vec.items()}

    # ------------------------------------------------------- 3. search ---
    def search(self, query: str, k: int = 3) -> list[tuple[float, dict]]:
        q = self._vector(Counter(tokenize(query)))
        scored = [(sum(w * vec.get(t, 0.0) for t, w in q.items()), c) for vec, c in zip(self.vectors, self.chunks)]
        return [s for s in sorted(scored, key=lambda s: s[0], reverse=True)[:k] if s[0] > 0]


# ------------------------------------------------------------ 4. answer ---
def answer(question: str, hits: list[tuple[float, dict]]) -> str:
    import anthropic  # imported here so --search works without the SDK installed

    context = "\n\n".join(f"<source id=\"{i+1}\" name=\"{c['source']}\">\n{c['text']}\n</source>"
                          for i, (_, c) in enumerate(hits))
    response = anthropic.Anthropic().beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=("Answer using ONLY the provided sources. Cite them like [1]. If the sources don't "
                "contain the answer, say so warmly instead of guessing."),
        messages=[{"role": "user", "content": f"{context}\n\nQuestion: {question}"}],
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        return "🙅 The request was declined."
    return "".join(b.text for b in response.content if b.type == "text")


def main() -> None:
    parser = argparse.ArgumentParser(description="Chat with a folder of Markdown notes.")
    parser.add_argument("question", nargs="+")
    parser.add_argument("--notes", type=Path, default=Path(__file__).parent / "notes")
    parser.add_argument("--search", action="store_true", help="only show retrieved chunks (no API call)")
    parser.add_argument("-k", type=int, default=3, help="how many chunks to retrieve")
    args = parser.parse_args()
    question = " ".join(args.question)

    index = Index(chunk_notes(args.notes.expanduser()))
    hits = index.search(question, args.k)
    print(f"🔎 Top {len(hits)} of {len(index.chunks)} chunks for: {question!r}")
    for score, chunk in hits:
        print(f"   {score:.2f}  {chunk['source']}")
    if not hits:
        print("No relevant notes found. Try different words!")
    elif not args.search:
        print("\n💬", answer(question, hits))


if __name__ == "__main__":
    main()
