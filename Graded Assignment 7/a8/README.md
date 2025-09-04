# 2024 MRR Growth Analysis

**Author:** 23f2003577@ds.study.iitm.ac.in

This pull request analyzes the **Monthly Recurring Revenue (MRR) growth** for 2024 on a quarterly basis, benchmarks performance against an **industry target of 15%**, and provides an **actionable data story** with concrete recommendations.

## Dataset

| Quarter | MRR Growth (%) |
|--------:|----------------:|
| Q1 | 2.78 |
| Q2 | 4.60 |
| Q3 | 5.60 |
| Q4 | 11.94 |

**Average (2024): 6.23%**

> Source: Product analytics (synthetic example for this PR).

## Key Findings

1. **Upward trajectory but below target:** Growth accelerates through the year from **2.78% (Q1)** to **11.94% (Q4)**. However, the annual **average is 6.23%**, which is **41% of the industry target (15%)**.
2. **Material Q4 improvement:** Q4 shows a near **2× uplift** vs. Q3 (from 5.6% → 11.94%), suggesting that recent initiatives (pricing tests, demand capture) may be working.
3. **Sustained gap to benchmark:** Even with the Q4 improvement, the **shortfall to target is ~3.06 pts** in Q4 and **8.77 pts on average** in 2024.

## Business Implications

- The product is gaining traction but **lags competitive growth rates**, which may impact investor confidence and sales efficiency.
- **Retention and expansion** need attention: MRR growth depends on both **net new** and **net revenue retention (NRR)**. A sub-15% run rate suggests insufficient expansion or cross-sell.
- **Budgeting & targets:** FY25 targets should reflect **Q4 momentum** while acknowledging the **average-level headroom**.

## Recommendations to Reach the Target (15%)

1. **Solution: Expand into new market segments.**  
   - Prioritize 2–3 **adjacent ICPs** with strong willingness-to-pay and low switching costs.  
   - Launch **localized onboarding** and **vertical-specific templates** (e.g., healthcare, logistics).  
   - Create **segment-specific messaging** and pilots with success metrics (CAC payback < 12 months).

2. **Upsell playbook for existing accounts.**  
   - Package advanced features into **growth tiers**; roll out **usage-based nudges**.  
   - Introduce **annual prepay discounts** to pull revenue forward and improve MRR stability.

3. **Pricing & packaging experiments.**  
   - Test **bundles and add-ons** to lift ARPU.  
   - Run **geo-based price tests** where elasticity permits.

4. **Retention investments.**  
   - Improve activation with **guided product tours**; expand **success-led QBRs** for top cohorts.  
   - Proactive **churn risk scoring** with lifecycle interventions.

## Visualizations

- **`figures/mrr_trend.png`** — Trend line with target benchmark.  
- **`figures/mrr_vs_target.png`** — Quarterly bars with a target reference line.

## Reproducibility

```bash
python -m pip install -r requirements.txt
python analysis/analyze_mrr.py
```

## Files in this PR

```
data/mrr_quarterly_2024.csv
analysis/analyze_mrr.py
figures/mrr_trend.png
figures/mrr_vs_target.png
README.md
requirements.txt
```

## How this PR was produced

This analysis was authored with the assistance of **LLM code generation tools** and reviewed for correctness.

