"""Shared config so RAG and OKF differ only in how knowledge reaches the prompt."""
import json
import re
import time
from pathlib import Path

from langchain_ollama import ChatOllama

ROOT = Path(__file__).parent
CORPUS = ROOT / "data/docs/ey_supply_chain_notes.txt"
BUNDLE_DIR = ROOT / "data/okf_bundle"
QUESTIONS = ROOT / "data/questions.json"
RESULTS_DIR = ROOT / "results"

GEN_MODEL = "llama3.1:8b"
JUDGE_MODEL = "gemma4:26b"
EMBED_MODEL = "nomic-embed-text"
NUM_CTX = 8192

ANSWER_PROMPT = """Answer the question using ONLY the context below. Be concise (1-4 sentences).
If the context does not contain the answer, reply exactly: The notes do not cover this.

Context:
{context}

Question: {question}
Answer:"""


def llm(model: str = GEN_MODEL) -> ChatOllama:
    # Ollama's default num_ctx silently truncates long prompts, so set it explicitly.
    # reasoning=False stops thinking-capable models (the gemma4 judge) from spending
    # minutes on hidden chain-of-thought before each structured reply.
    return ChatOllama(model=model, temperature=0, num_ctx=NUM_CTX, reasoning=False)


def load_questions() -> list[dict]:
    return json.loads(QUESTIONS.read_text())


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    meta = dict(line.split(": ", 1) for line in m.group(1).splitlines())
    return meta, m.group(2)


def answer(question: str, contexts: list[str]) -> dict:
    """Shared generation step; returns answer plus latency and token usage."""
    prompt = ANSWER_PROMPT.format(context="\n\n---\n\n".join(contexts) or "(none)", question=question)
    t0 = time.time()
    msg = llm().invoke(prompt)
    usage = msg.usage_metadata or {}
    return {"response": msg.content.strip(), "gen_seconds": time.time() - t0,
            "input_tokens": usage.get("input_tokens", 0), "output_tokens": usage.get("output_tokens", 0)}


def save(name: str, rows: list[dict]) -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    (RESULTS_DIR / f"{name}_results.json").write_text(json.dumps(rows, indent=2))
