# analysis/analyze_mrr.py
# Author: 23f2003577@ds.study.iitm.ac.in
#
# Processes 2024 quarterly MRR growth, computes summary stats, and creates visualizations.
# Produces:
#   figures/mrr_trend.png
#   figures/mrr_vs_target.png
#
# Usage:
#   python analysis/analyze_mrr.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

TARGET = 15.0

def main():
    data_path = Path(__file__).resolve().parents[1] / "data" / "mrr_quarterly_2024.csv"
    fig_dir = Path(__file__).resolve().parents[1] / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path)
    df["quarter_order"] = df["quarter"].map({"Q1":1, "Q2":2, "Q3":3, "Q4":4})
    df = df.sort_values("quarter_order")

    avg = df["mrr_growth"].mean().round(2)

    # Print key stats to console
    print(f"Average MRR growth 2024: {avg}")
    print(f"Target: {TARGET}")
    print("Quarterly values:")
    print(df[["quarter", "mrr_growth"]].to_string(index=False))

    # Styling
    sns.set_style("whitegrid")
    sns.set_context("talk")

    # Figure 1: Trend line
    plt.figure(figsize=(10,6))
    ax = sns.lineplot(data=df, x="quarter", y="mrr_growth", marker="o")
    ax.axhline(TARGET, linestyle="--", linewidth=1.5, label=f"Target {TARGET}")
    for i, row in df.iterrows():
        ax.text(row["quarter"], row["mrr_growth"] + 0.3, f"{row['mrr_growth']}", ha="center", va="bottom", fontsize=12)
    ax.set_title("2024 Quarterly MRR Growth (%)")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("MRR Growth (%)")
    ax.legend()
    plt.tight_layout()
    plt.savefig(fig_dir / "mrr_trend.png", dpi=200)
    plt.close()

    # Figure 2: Bars vs target
    plt.figure(figsize=(10,6))
    ax = sns.barplot(data=df, x="quarter", y="mrr_growth", palette="Blues")
    ax.axhline(TARGET, linestyle="--", linewidth=1.5, color="red", label=f"Target {TARGET}")
    for p in ax.patches:
        ax.annotate(f"{p.get_height():.2f}", (p.get_x() + p.get_width()/2., p.get_height()),
                    ha="center", va="bottom", fontsize=12, xytext=(0, 5), textcoords="offset points")
    ax.set_title("MRR Growth vs. Target (2024)")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("MRR Growth (%)")
    ax.legend()
    plt.tight_layout()
    plt.savefig(fig_dir / "mrr_vs_target.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    main()
