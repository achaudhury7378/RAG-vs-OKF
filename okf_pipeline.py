"""OKF: the model reads index.md, asks for concept files, follows links, then answers."""
import re
import time

from common import BUNDLE_DIR, answer, llm, load_questions, save

MAX_ROUNDS, MAX_FILES = 3, 5

PICK_PROMPT = """You can read files from a knowledge bundle. Here is its index:

{index}

Question: {question}

Reply with ONLY lines of the form `READ: <filename>` (at most 3) for the files needed to answer.
If no file is relevant, reply `NONE`."""

FOLLOW_PROMPT = """Question: {question}

Files read so far:
{files}

Files can link to other files with Markdown links. Do you need to read more files to answer?
Reply with ONLY lines `READ: <filename>` for additional files, or `DONE` if you have enough."""

READ_RE = re.compile(r"READ:\s*`?([\w\-./]+\.md)`?")


def navigate(question: str, index: str) -> tuple[list[str], int]:
    """Return (filenames read, number of navigation LLM calls)."""
    read: list[str] = []
    prompt = PICK_PROMPT.format(index=index, question=question)
    for round_no in range(MAX_ROUNDS):
        reply = llm().invoke(prompt).content
        wanted = [f for f in READ_RE.findall(reply) if (BUNDLE_DIR / f).exists() and f not in read]
        if not wanted:
            return read, round_no + 1
        read += wanted[: MAX_FILES - len(read)]
        if len(read) >= MAX_FILES:
            return read, round_no + 1
        files = "\n\n".join(f"## {f}\n{(BUNDLE_DIR / f).read_text()}" for f in read)
        prompt = FOLLOW_PROMPT.format(question=question, files=files)
    return read, MAX_ROUNDS


def main() -> None:
    index = (BUNDLE_DIR / "index.md").read_text()
    rows = []
    for q in load_questions():
        t0 = time.time()
        files, nav_calls = navigate(q["question"], index)
        navigation_seconds = time.time() - t0
        contexts = [(BUNDLE_DIR / f).read_text() for f in files]
        out = answer(q["question"], contexts)
        rows.append({**q, "retrieved_contexts": contexts, "files_read": files, "nav_calls": nav_calls,
                     "retrieval_seconds": navigation_seconds, "units_read": len(files), **out})
        print(f"[okf] {q['id']} read={files} -> {out['response'][:80]!r}")
    save("okf", rows)


if __name__ == "__main__":
    main()
