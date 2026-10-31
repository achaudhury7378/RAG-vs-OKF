"""Grouped bar chart of ragas scores by question type, for the LinkedIn post."""
import matplotlib.pyplot as plt
import pandas as pd

from common import RESULTS_DIR

df = pd.concat([pd.read_csv(RESULTS_DIR / f"{n}_scores.csv") for n in ("rag", "okf")])
metrics = [c for c in df.columns if c in {
    "faithfulness", "answer_relevancy", "llm_context_precision_with_reference",
    "context_recall", "factual_correctness(mode=f1)"}]
labels = {"faithfulness": "Faithfulness", "answer_relevancy": "Answer relevancy",
          "llm_context_precision_with_reference": "Context precision",
          "context_recall": "Context recall", "factual_correctness(mode=f1)": "Factual correctness"}

groups = ["overall", "single", "multi_hop", "unanswerable"]
fig, axes = plt.subplots(1, len(groups), figsize=(16, 4), sharey=True)
for ax, g in zip(axes, groups):
    sub = df if g == "overall" else df[df["type"] == g]
    means = sub.groupby("pipeline")[metrics].mean().loc[["rag", "okf"]]
    means.T.rename(index=labels).plot.bar(ax=ax, color=["#6b7280", "#2563eb"], legend=False, width=0.75)
    ax.set_title(g.replace("_", "-"))
    ax.set_ylim(0, 1)
    ax.tick_params(axis="x", rotation=60)
axes[0].set_ylabel("ragas score")
axes[-1].legend(["RAG", "OKF"], loc="lower right")
fig.suptitle("RAG vs OKF on EY supply chain notes (llama3.1:8b generator, gemma4:26b judge)")
fig.tight_layout()
fig.savefig(RESULTS_DIR / "rag_vs_okf.png", dpi=160)

ops = df.groupby("pipeline")[["units_read", "retrieval_seconds", "gen_seconds", "input_tokens"]].mean().round(2)
print(ops.to_string())
summary = df.groupby(["pipeline", "type"])[metrics].mean().round(3)
summary.to_csv(RESULTS_DIR / "summary_by_type.csv")
print(summary.to_string())
