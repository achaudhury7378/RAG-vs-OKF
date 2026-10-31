# RAG vs OKF (Open Knowledge Format), scored with ragas

Same corpus, same generator, same prompt. Only the way knowledge reaches the prompt differs.

- **Corpus:** `data/docs/ey_supply_chain_notes.txt` (17-page interview notes PDF, text extracted with `extract_pdf.py`)
- **Generator:** `llama3.1:8b` (Ollama, temperature 0, `num_ctx=8192`)
- **Judge:** `gemma4:26b` (Ollama, thinking disabled)
- **Embeddings:** `nomic-embed-text`
- **Questions:** 24 in `data/questions.json` (8 single-fact, 12 multi-hop, 4 unanswerable)

## Pipelines
| | RAG (`rag_pipeline.py`) | OKF (`okf_pipeline.py`) |
|---|---|---|
| Knowledge | 800-char chunks in Chroma | `data/okf_bundle/`: 30 one-concept Markdown files with YAML frontmatter and cross-links, plus a generated `index.md` |
| Access | top-4 by embedding similarity | model reads `index.md`, replies `READ: file.md` (max 3 rounds, 5 files), can follow links, then answers |
| Context given to ragas | retrieved chunks | full text of the files read |

The final answer step (`common.answer`) is identical for both.

## Run
```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python extract_pdf.py            # PDF -> text
.venv/bin/python okf_index.py              # regenerate bundle index
.venv/bin/python rag_pipeline.py
.venv/bin/python okf_pipeline.py
.venv/bin/python evaluate.py rag           # ~25 min each with a local judge
.venv/bin/python evaluate.py okf
.venv/bin/python plot.py
```

## Caveats to state when you publish
- **Curation cost is not free.** The OKF bundle was hand-authored (by Claude, once, from the PDF text and then committed), while RAG consumed the raw extracted text, including flattened tables. That favours OKF; say so.
- 24 questions, one document, one domain. Treat gaps of a few points as noise.
- LLM-as-judge, local model, temperature 0. Check the NaN counts printed by `evaluate.py`.
- ragas `ResponseRelevancy` scores "The notes do not cover this." as non-committal (near 0) by design, so read the unanswerable group with faithfulness and factual correctness instead.
- OKF navigation with an 8B model uses a plain-text `READ:` protocol, not tool calling; it sometimes over-reads files.
