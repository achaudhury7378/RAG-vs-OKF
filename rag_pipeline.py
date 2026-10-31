"""Baseline RAG: chunk -> embed -> top-k retrieve -> answer."""
import time

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from common import CORPUS, EMBED_MODEL, answer, load_questions, save

CHUNK_SIZE, CHUNK_OVERLAP, TOP_K = 800, 100, 4


def build_store() -> Chroma:
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_text(CORPUS.read_text())
    return Chroma.from_texts(chunks, OllamaEmbeddings(model=EMBED_MODEL), collection_name="rag")


def main() -> None:
    store = build_store()
    rows = []
    for q in load_questions():
        t0 = time.time()
        docs = store.similarity_search(q["question"], k=TOP_K)
        contexts = [d.page_content for d in docs]
        retrieval_seconds = time.time() - t0
        out = answer(q["question"], contexts)
        rows.append({**q, "retrieved_contexts": contexts, "retrieval_seconds": retrieval_seconds,
                     "units_read": len(contexts), **out})
        print(f"[rag] {q['id']}: {out['response'][:90]!r}")
    save("rag", rows)


if __name__ == "__main__":
    main()
