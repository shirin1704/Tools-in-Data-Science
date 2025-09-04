import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------
# Data Generation
# ---------------------------
np.random.seed(42)

# Create synthetic customer spending data for 4 customer segments
segments = ["Budget", "Standard", "Premium", "VIP"]
data = []

for segment in segments:
    if segment == "Budget":
        spend = np.random.normal(loc=50, scale=15, size=200)
    elif segment == "Standard":
        spend = np.random.normal(loc=120, scale=30, size=200)
    elif segment == "Premium":
        spend = np.random.normal(loc=250, scale=50, size=200)
    else:  # VIP
        spend = np.random.normal(loc=500, scale=100, size=200)

    for s in spend:
        data.append({"Segment": segment, "Spending": max(s, 0)})  # spending cannot be negative

df = pd.DataFrame(data)

# ---------------------------
# Seaborn Styling
# ---------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ---------------------------
# Visualization
# ---------------------------
plt.figure(figsize=(8, 8))  # 512x512 with dpi=64
ax = sns.boxplot(
    data=df,
    x="Segment",
    y="Spending",
    palette="Set2",
    showfliers=True
)

# Titles and labels
ax.set_title("Customer Spending Distribution by Segment", fontsize=18, weight="bold")
ax.set_xlabel("Customer Segment", fontsize=14)
ax.set_ylabel("Monthly Spending (USD)", fontsize=14)

# Save chart
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
