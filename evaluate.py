"""Score a pipeline's saved results with ragas, judged by a local model."""
import json
import sys
import warnings

import pandas as pd
from langchain_ollama import OllamaEmbeddings
from ragas import EvaluationDataset, evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import (Faithfulness, FactualCorrectness, LLMContextPrecisionWithReference,
                           LLMContextRecall, ResponseRelevancy)
from ragas.run_config import RunConfig

from common import EMBED_MODEL, JUDGE_MODEL, RESULTS_DIR, llm

warnings.filterwarnings("ignore")

name = sys.argv[1]
limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
rows = json.loads((RESULTS_DIR / f"{name}_results.json").read_text())[:limit]

dataset = EvaluationDataset.from_list([
    {"user_input": r["question"], "response": r["response"], "reference": r["reference"],
     # ragas rejects empty context lists; a placeholder keeps the row scoreable
     "retrieved_contexts": r["retrieved_contexts"] or ["(no context retrieved)"]}
    for r in rows
])

judge = LangchainLLMWrapper(llm(JUDGE_MODEL))
embeddings = LangchainEmbeddingsWrapper(OllamaEmbeddings(model=EMBED_MODEL))
result = evaluate(
    dataset,
    metrics=[Faithfulness(), ResponseRelevancy(), LLMContextPrecisionWithReference(),
             LLMContextRecall(), FactualCorrectness()],
    llm=judge, embeddings=embeddings,
    run_config=RunConfig(timeout=900, max_workers=2, max_retries=3),
)

scores = result.to_pandas()
metric_cols = [c for c in scores.columns if c not in dataset.features() and c not in
               {"user_input", "response", "reference", "retrieved_contexts"}]
df = pd.DataFrame(rows)[["id", "type", "units_read", "retrieval_seconds", "gen_seconds",
                         "input_tokens", "output_tokens"]]
df = pd.concat([df, scores[metric_cols].reset_index(drop=True)], axis=1)
df.insert(0, "pipeline", name)
df.to_csv(RESULTS_DIR / f"{name}_scores.csv", index=False)

print(df.groupby("type")[metric_cols].mean().round(3).to_string())
print("\noverall\n", df[metric_cols].mean().round(3).to_string())
print("\nNaN counts\n", df[metric_cols].isna().sum().to_string())
