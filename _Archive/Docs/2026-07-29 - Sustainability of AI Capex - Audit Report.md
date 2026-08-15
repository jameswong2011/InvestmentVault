---
publish: false
title: Sustainability of AI Capex — Audit Report
date: 2026-07-29
tags: [audit, ai-capex, archive]
status: closed
source: "[[Website/2026-07-29 - Sustainability of AI Capex]]"
reviewed_version: "2026-07-29 15:00:22 +07"
---

# Sustainability of AI Capex — Audit Report

**Verdict: hold publication.** The central distinction—AI investment can remain financeable after its economic returns become unattractive—is strong. The document does not yet prove its two load-bearing conclusions:

1. Aggregate AI returns are currently **5–7% versus an 8–10% hurdle rate**.
2. Financing can sustain the stated **$6.5–7.2T 2027–30 race path**.

Several calculations, accounting classifications, and causal leaps undermine those claims.

Reviewed: [[Website/2026-07-29 - Sustainability of AI Capex]] saved at **2026-07-29 15:00:22 +07**.

## 1. Numerical and accounting errors

| Severity | Issue | Finding |
|---|---|---|
| **Critical** | **The 5–7% “return” is not ROIC** | $100–120B revenue × 50–60% gross margin produces **$50–72B gross profit**, not operating profit. The denominator is gross cumulative capex rather than average invested capital, while the numerator excludes allocated operating costs, taxes, working capital and losses at AI labs. Comparing this pre-tax proxy with a conventional post-tax WACC is invalid. The defensible conclusion is: **disclosed monetization does not yet demonstrate returns above the hurdle rate**. |
| **Critical** | **Range arithmetic is selectively paired** | $50B ÷ $1.2T = **4.2%**; $70B ÷ $1.0T = **7.0%**. Matched low/low and high/high cases give approximately **5.0–5.8%**, not 5–7%. |
| **Critical** | **“Already invested” includes future 2026 spending** | The $1.0–1.2T denominator incorporates full-year 2026 plans. On July 29, that money has neither all been spent nor all entered service. Current annualized earnings are therefore being divided by a forecast year-end asset cohort. |
| **Critical** | **The $850–900B capex denominator is unreconciled** | Core-five estimates of $785–830B plus CoreWeave’s $31–35B already yield roughly **$816–865B**, before Chinese and sovereign projects. The document does not show the offsetting deductions for non-AI logistics, offices, Kuiper, leases, fiscal-calendar mismatches or duplicated supplier/customer spending. |
| **Critical** | **Funding stack does not fund the race path** | The 2027–30 annual path totals **$6.5–7.2T**. The funding rows total **$5.6–7.0T**. The low case is approximately **$0.9T short**; the high race case is $0.2T above maximum funding. Including 2031 produces **$8.5–9.4T**, but the funding table ends in 2030. |
| **Critical** | **Funding sources are partly double-counted** | “Retained operating cash flow” includes customer prepayments, while prepayment-backed financing is counted again elsewhere. Oracle’s FY2026 operating cash flow included **$4.6B of customer prepayments with a significant financing component**, so the categories are not independent. Retained OCF also cannot all be allocated to AI after maintenance and non-AI investment. [Oracle FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm) |
| **High** | **Consumer subscription formula is wrong** | 2.5B × 6% × $12 × 12 = **$21.6B**; 3B × 8% × $15 × 12 = **$43.2B**. The implied range is $22–43B, not $35–55B. Tools, APIs and advertising require separate, non-overlapping rows. |
| **High** | **WTP is actually WTA** | The $124.50 mean and $11.40 median measure compensation users require to give up AI for a month—**willingness to accept**, not willingness to pay. It cannot directly support subscription pricing. [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/publication/what-is-generative-ai-worth/) |
| **High** | **Depreciation revenue bridge is misstated** | Moving from $110–120B to $260–300B requires a $140–190B uplift. At a 50% contribution margin, that means **$280–380B** of incremental revenue, not $300–360B. “Operating margin” would usually include depreciation, creating a risk of double counting. |
| **High** | **Power ceiling does not follow from the capacity figures** | 76GW to 134GW adds 58GW. Over four years that is about 14.5GW annually; at $45–55B/GW, the implied annual construction ceiling is approximately **$650–800B**, not $1.5–2T. Reaching $1.5–2T requires a global capacity input of roughly 27–44GW annually. The section combines a US capacity forecast with a global spending conclusion. Epoch AI’s reference estimate is approximately **$38B for a typical 1GW AI data centre**, which also needs reconciling. [Epoch AI cost breakdown](https://epoch.ai/data-insights/ai-datacenter-cost-breakdown) |
| **High** | **Big Four leverage usage is inconsistent** | Current gross leverage of 0.6× divided by a 2.0–2.5× ceiling means **24–30% of capacity is drawn**, not 10–20%. A 10–20% result requires net debt near 0–0.3× and must be labelled accordingly. |
| **Medium** | **Tranches do not reconcile** | A–D sum to 90–105%. C plus D equals 35–45%, yet the subsequent text calls only 30–35% fragile, leaving 5–15 percentage points unexplained. The taxonomy also mixes workload economics with funding source. |
| **Medium** | **GDP comparison mixes geographies** | The $850–900B “ecosystem” includes Chinese and sovereign spending but is divided by US GDP. A global numerator needs world GDP; a US GDP comparison needs US-only capex. |

## 2. Factual and temporal inconsistencies

- **Meta did not announce that buybacks were “suspended.”** It made no Q1 2026 repurchases, but retained $25.03B of authorization. “Paused during Q1” is supportable; “suspended” implies a formal policy action. [Meta Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm)
- The hyperscaler capex/OCF crossover is described as a fact, while Epoch AI says capex was **“on track”** to overtake operating cash flow around Q3 2026. It remains a forecast. [Epoch AI](https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow)
- Alphabet’s Q2 2026 capex is compared with FY2025 Cloud operating income. Q2 2026 Cloud operating income was $8.814B for the quarter, so selectively updating capex while leaving the earnings proxy stale biases the return comparison downward. [Alphabet Q2 2026 release](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf)
- The productivity section uses METR’s early-2025 −19% result without equal treatment of its later update. METR says subsequent raw estimates suggest speedups but suffer selection bias; it also warns against generalising the original 16-developer study to other tasks. [Original METR study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [February 2026 update](https://metr.org/blog/2026-02-24-uplift-update/)

## 3. Logical fallacies and qualitative inconsistencies

| Type | Problem |
|---|---|
| **Non sequitur** | Power-law outcomes do not establish that the capital-weighted expected return exceeds WACC. Winner magnitude, probability, loser losses and financing costs are all missing. |
| **Internal contradiction** | Part One says losers can earn deeply negative returns; Part Two says over-investing risks “only mediocre returns.” Both cannot describe the same downside. |
| **False necessity** | Under-investment does not “almost guarantee exclusion.” Firms can rent capacity, partner, adopt custom silicon, wait for price declines, acquire distressed assets or specialise above the infrastructure layer. |
| **Composition fallacy** | Pooling Big Four cash flows, neocloud debt, lab commitments and sovereign budgets into one “complex” treats capital as transferable across entities that are not cross-guaranteed. |
| **Cash-flow/value conflation** | Cash-funded spending reduces insolvency risk; it does not make negative-NPV investment sustainable. Shareholder pressure can stop internally financed capex before credit capacity is reached. |
| **Selection bias** | The historical reference class contains failed booms selected with hindsight, without successful investment cycles or a defined sampling methodology. The claimed two-year clock is asserted rather than estimated. |
| **Median-to-total inference** | The article describes AI usage as power-law distributed, then uses median enterprise adoption as the binding aggregate-demand variable. A small number of very large users could dominate token and revenue demand. |
| **Circular scenario construction** | Base and bull converge in the low-$2T range because similar terminal growth is assumed. “Same destination” is therefore an input, not an analytical result. |
| **Unsupported expectations claim** | The conclusion says markets are misclassifying semiconductor cyclicality, but contains no reverse DCF, consensus expectations or company-specific valuation bridge. |
| **Overgeneralisation** | Qualification gates protect share and pricing; they do not eliminate demand cyclicality. “Trough earnings no longer behave cyclically at all” goes beyond the evidence and conflicts with the uncertainty retained in [[Website/2026-07-27 - Pricing the End of the Semiconductor Cycle]]. |

## 4. Material gaps

1. **Auditable capex ledger:** company, geography, calendarisation, cash versus leases, AI allocation and overlap eliminations.
2. **Cohort return model:** placed-in-service date, utilisation, revenue per accelerator-hour, power cost, useful life, residual value and lifetime NPV.
3. **Entity-specific financing:** debt maturities, covenants, fixed obligations, contract termination rights and credit-spread sensitivity.
4. **De-circularised demand ledger:** identify where cloud revenue, lab revenue, internal savings, advertising uplift and non-AI workloads overlap.
5. **A genuine bear scenario:** demand stall, recession, efficiency shock, export controls, regulation or credit event, with probabilities.
6. **Observable falsifiers:** current utilisation and “median workflow depth” thresholds are largely undisclosed. Each test needs a source, measurement definition and reporting frequency.
7. **Market-pricing bridge:** show what adoption, margins and terminal capex are embedded in each relevant equity.
8. **Source-level citations:** the website article relies on a source-note link but gives readers no provenance for its load-bearing estimates.

## Recommended repair order

1. **Rebuild the capex/return model** on matched periods and entity-level NOPAT versus average invested capital.
2. **Balance the funding ledger** and remove prepayment/OCF double counting.
3. **Correct the consumer, depreciation, leverage and power calculations.**
4. **Add a probability-weighted bear/base/bull matrix.**
5. **Rewrite the final semiconductor claim as a falsifiable hypothesis**, not a concluded structural reclassification.
6. **Add citations beside every central figure and historical analogy.**

The strongest publishable conclusion today is narrower: **AI infrastructure spending can remain financeable after disclosed monetisation ceases to justify the incremental capital, but the timing and magnitude of that divergence have not yet been quantified reliably.**
