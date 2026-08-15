---
publish: false
date: 2026-08-05
updated: 2026-08-13
tags: [research, deep-dive, NBIS, CRWV, neoclouds, vera-rubin, ROIC, customer-advances, cash-flow]
sector: Neoclouds & GPU-as-a-Service
ticker: NBIS
source: vault synthesis — supersedes the held-rate framing in the 2026-08-04 Rubin ROIC note; corrected model per its Addendum 5 error audit
source_type: deep-dive
revision: '2026-08-13 v3 — primer + asset-life sensitivity as a first-class axis'
additional_sources:
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231x20f.htm
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d4.htm
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d5.htm
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926064092/nbis-20260331xex99d2.htm
  - https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm
  - https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm
merged_from:
  - "[[_Archive/Backups/Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive (pre-rewrite 2026-08-13)]]"
  - "[[_Archive/Backups/Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive (pre-merge 2026-08-07)]]"
  - "[[_Archive/Backups/Research/2026-08-07 - NBIS CRWV - Customer Advances and Fleet ROIC - deep-dive (merged 2026-08-07)]]"
propagated_to: [NBIS, CRWV]
---

# NBIS + CRWV — Rubin Fleet Economics

## Primer — what this business is

A **neocloud** buys NVIDIA AI chips, plugs them into a building with power and cooling, and rents the chips by the hour to Microsoft, Meta, and AI labs. It is a landlord. NVIDIA owns the scarce chip. The grid owns the scarce watt. The neocloud owns the lease.

**Vera Rubin** is the next NVIDIA generation. One GPU, including the rack and its share of the building, costs **$183K** — about double the current Blackwell generation, mostly because memory got more expensive. The chip is roughly 3× faster on the main inference math (FP8), ~1.6× on older training math (BF16).

The customer usually signs a **five-year take-or-pay**: they pay whether they use the chip or not. After year 5 the chip is re-rented on the open market at a discount, then scrapped when it no longer earns its keep. That scrap date is **useful life** — 5, 7, 9, or 11 years in this model. Default in the company grids is 7.

Cash in a year ≈ hourly rent × 8,410 hours (96% of the year — the contract pays for the chip being available) × 70% (the other 30% is power, staff, parts). Subtract depreciation, get EBIT. The investment question is whether that stream, over the chip's life, beats a 15% cost of capital on the $183K.

[[Theses/NBIS - Nebius Group|NBIS]] (Nebius) and [[Theses/CRWV - CoreWeave|CRWV]] (CoreWeave) are the two public pure-plays. Same landlord model. NBIS is earlier in the build and funds more with customer prepayments. CRWV is larger, already live, and carries a big debt stack.

## Thesis Delta

1. **Three numbers set the return: the cash rent, how much of the fleet is locked in a five-year contract at that rent, and how many years the chip stays in service.** Not a multiple of $6. $6 is a label used to name rows. NBIS's own Microsoft math is closer to **$3.35/hour**.
2. **Useful life is not a rounding error at the $9 rent.** At $9, a 5-year life earns **13.7% IRR / −$5K NPV @ 15%** (fails). A 7-year life earns **18.4% / +$17K** (clears). The rent that exactly earns 15% IRR is **$9.27 (5yr) · $8.22 (7yr) · $7.65 (9yr) · $7.32 (11yr)**. At $12 the extra years are gravy (IRR 27% → 33%). The prior "life is the shallow axis" line was an accounting-ROIC artifact.
3. **$9.50 is a bookkeeping screen, not the value-destruction line.** It is "average EBIT over N years ÷ $183K = 15%." That double-charges capital (depreciation already took the principal back). Use IRR/NPV to decide if the GPU creates value.
4. **A customer prepayment is a loan against future rent, not free capex.** Microsoft's 40% on the original deal is **~$51K per GPU** (~28% of Rubin cost), not 110% of a hypothetical $12 contract. 40% upfront lifts the present value of a five-year contract by **~8%** at an 8% discount rate. It cannot turn a $6 cash rent into a $9 rent.
5. **2027–29 reported fleet EBIT barely moves with life** — those Rubin chips are 1–3 years old, still inside the contract. Life shows up from 2029 on CRWV, when old Hopper chips would be scrapped (5-year life) or still earning (7–11).

## Summary

Buy a $183K box. Collect a contracted hourly rent for five years. Then collect a smaller re-rent until you throw the box away. If the contracted rent is **$12**, the box clears 15% at every life from 5 to 11 years. If it is **$9**, you need the box to last past five years. If it is **$6**, no plausible life saves it (IRR 9% even at 11 years).

The contract is doing most of the work. The same $12 GPU rented on the open market from day one (prices falling the way every prior generation fell) earns about half as much EBIT and fails the 15% test at every life. So the live questions are: what cash rent is on the paper, what share of GPUs have paper, and whether that paper was signed before Rubin got twice as expensive.

## Framework / Mental Model

Three levers, in order of how much they move the answer:

| Lever | What it is | Why it matters |
|---|---|---|
| **Cash rent** | $/GPU-hour the customer actually pays | Steep axis. Each extra $3/hour at a 7-year life adds ~$107K of lifetime EBIT |
| **Coverage** | Share of GPUs on a 5-year take-or-pay vs open-market | At $12, coverage below ~44% fails the bookkeeping screen |
| **Useful life (N)** | Years until scrap after the 5-year contract | Decides $9. Irrelevant once rent is $12+. Hits the *company* P&L only when old chips would otherwise be scrapped |

Two ways people quote "15%":

| Test | What it asks | $9 / 7-year result |
|---|---|---|
| **IRR / NPV @ 15%** | Does the cash come back at 15%? | **Clears** (18.4%, +$17K) |
| **Gross-book screen** | Average EBIT ÷ original $183K = 15%? | **Fails** (13.7%). Needs $9.50 |

This note uses IRR to decide value. The screen is a conservative filter, not a destruction line.

Mental-model checks (hypotheses): **[G-7]** incremental dollar on Rubin is the variable; **[G-11] inverted** EBITDA hides depreciation, and the book screen then charges 15% on capital already depreciated; **[G-10]** holding launch prices for five years is outside the merchant history — only the contract puts it in the model; extra life past 5 years is a free option on a sunk rack, except at the $9 edge where the option is in-the-money vs 15%.

## Evidence

### One GPU — what "life" means in cash

| Years | What the GPU is doing | Rent as % of the contracted rate |
|---|---|---|
| 1–5 | Locked take-or-pay | 100% |
| 6 | First re-rent | 55% |
| 7 | Re-rent, decaying | 51% |
| 8 | | 48% |
| 9 | | 44% |
| 10 | | 41% |
| 11 | Last year if N=11 | 38% |
| After N | Scrapped | 0 |

A 5-year life never sees the re-rent tail. A 7-year life gets two cheaper years. An 11-year life gets six. The tail is real cash (the chip is already paid for) but smaller than the contract years.

### Rate × life — the table that matters

All figures: one Rubin GPU, $183K in, 100% five-year contract, 30% cash cost, no tax. **Bold** = clears 15% IRR.

**Unlevered IRR**

| Cash rent | 5 years | 7 years | 9 years | 11 years |
|---:|---:|---:|---:|---:|
| $6 | −1.2% | 4.5% | 7.6% | 9.4% |
| $9 | 13.7% | **18.4%** | **20.6%** | **21.7%** |
| $12 | **26.8%** | **30.7%** | **32.3%** | **33.1%** |
| $15 | **38.9%** | **42.2%** | **43.4%** | **43.9%** |
| $18 | **50.4%** | **53.1%** | **54.0%** | **54.4%** |

**NPV @ 15% ($K per GPU)**

| Cash rent | 5 years | 7 years | 9 years | 11 years |
|---:|---:|---:|---:|---:|
| $6 | −65 | −49 | −40 | −33 |
| $9 | **−5** | **+17** | +32 | +42 |
| $12 | +54 | +84 | +104 | +117 |
| $15 | +113 | +151 | +176 | +192 |
| $18 | +172 | +218 | +248 | +267 |

**Lifetime EBIT ($K)** — cash profit after depreciation, before tax. The $192K row at 7 years is the bookkeeping screen (0.15 × 7 × $183K).

| Cash rent | 5 years | 7 years | 9 years | 11 years |
|---:|---:|---:|---:|---:|
| $9 | 125 | 175 | 218 | 255 |
| $12 | 213 | 282 | 341 | 392 |
| $15 | 301 | 389 | 465 | 529 |
| $18 | 390 | 496 | 588 | 666 |
| *Screen (15% × N × $183K)* | *137* | *192* | *247* | *302* |

**Rent that exactly earns 15% IRR**

| Useful life | 5 years | 7 years | 9 years | 11 years |
|---|---:|---:|---:|---:|
| Cash rent | **$9.27** | **$8.22** | **$7.65** | **$7.32** |
| If leftover building value is credited at scrap | $8.20 | $7.59 | $7.28 | $7.10 |

Read:

- **$6 never works.** Even an 11-year life is a 9% IRR. This is "charge the same dollars per hour as today's Blackwell," which is the pessimistic held-rate case.
- **$9 is a life bet.** Fail at 5 years, clear at 7+. NVIDIA's annual product cadence (Blackwell → Rubin → Feynman) is the argument for a short life. Hopper chips still renting at year 7–8 is the argument for a long one. The model does not pick; it prices both.
- **$12 works at every life.** Extra years add cash (NPV +54 → +117) and barely lift IRR (27% → 33%) because most of the money is in years 1–5.
- **Accounting ROIC falls as life extends** (at $12: 23.3% → 19.5%) because it keeps charging 15% on the original $183K in years when the rack is mostly written off. That is why an earlier version of this note called life "shallow." IRR, the value test, rises.

### The contract vs the street

Same $12 GPU, no five-year lock — price follows the observed open-market fade (100% of launch in year 1, then 65 / 50 / 45 / 42 …):

| | 5 years | 7 years | 9 years | 11 years |
|---|---:|---:|---:|---:|
| Contracted lifetime EBIT | $213K | $282K | $341K | $392K |
| Open-market lifetime EBIT | $73K | $122K | $163K | $198K |
| Extra EBIT from the 5-year lock | $140K | $160K | $178K | $194K |

Open-market fails the bookkeeping screen at every life. The lock *is* the investment. Mix at $12 / 7 years: you need **~44% of GPUs contracted** to still print 15% average EBIT / $183K. Below that, merchant GPUs drag the fleet under.

The model assumes 100% contracted at the sampled rent. That is the bull case. Microsoft/Meta paper signed *before* Rubin doubled in cost may already cover some of these MW at $3–6. That is a vintage mix, not a "$12 row."

After year 5 the model re-rents at 55% of contract, then −7%/year. That 55% is a blend of today's 6-year-old chips (cheap on the open market, still expensive if a hyperscaler wants them). The whole history is a shortage period. If 2028–29 is a digestion, the step could be 35–40% — exactly when CRWV's old Hopper chips roll.

### What customers will pay

People quote rents as "2× Blackwell." Blackwell itself trades in a stack:

| Who is paying | $/hour | Notes |
|---|---:|---|
| Dedicated full-stack (IREN–Microsoft, xAI) | ~$11–12 | Retail / they own the power |
| Mid-market list | ~$6 | The model's *label* |
| NBIS / CRWV wholesale (deal math) | **~$3.35–5.70** | Microsoft-implied at the low end |

A customer will not pay more per unit of work than their alternative. If their alternative is a $6 Blackwell and Rubin is 3× faster, the ceiling is $18. If Rubin is only 1.6× faster (training), the ceiling is $9.60. If their alternative is a $3.35 wholesale Blackwell, the ceiling is $10 (inference) or $5.36 (training) — the band inverts.

Installing a new Rubin instead of *keeping* a working $6 Blackwell that is already paid for needs ~$13.75/hour, not $10.60. $10.60 only matches revenue per watt; it ignores that Rubin still has to pay for a new $183K box.

### Customer advances (who funds the box)

The customer sometimes pays part of the five-year rent on day one. The operator records cash and a promise to deliver service later. That is a loan against the lease, not a gift.

| | NBIS | CRWV |
|---|---|---|
| Disclosed prepay | Original Microsoft 40% of that deal (~$7.0B / $17.4B) | 15–25% across the book |
| Per GPU on the Microsoft deal | **~$51K** = 28% of Rubin capex | — |
| Later Microsoft add-ons | **0%** upfront | — |

Present-value lift vs paying monthly, 8% discount, five years: 15% upfront → +3%; 40% upfront → +8%. A $9 rent with 40% upfront is like $9.75 paid monthly. A $6 rent becomes $6.50 — still a bad GPU.

Do not take 40% of a made-up $12 contract ($202K) and call the GPU self-funded. That is a different deal than the one in the filing.

Q1 2026: NBIS reported FCF −$0.2B. Strip the $3.2B of new deferred-revenue cash and it is −$3.4B. CRWV −$4.7B reported / −$5.3B ex-advance. New customer checks can make operating cash look structural while the fleet is still being built. When bookings stop, the inflow stops and the service obligation remains.

### Company fleets (default: 7-year life)

Existing chips, no Rubin: CRWV 130K Hopper @ $4 + 120K Blackwell @ $6. NBIS 40K Hopper + 200K Blackwell (140K arrives 2027). Rubin arrives on the same calendar as Blackwell did: CRWV 40K in 2027 + 80K in 2028; NBIS 70K + 130K. 100% contracted at the sampled rent. CRWV pretax = EBIT − $3.9B interest.

**EBIT $B at a 7-year life**

| | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| CRWV @ $9 / $12 / $15 / $18 | 4.6 / 5.3 / 6.0 / 6.8 | 6.5 / 8.7 / 10.8 / 12.9 | 6.9 / 9.1 / 11.2 / 13.3 |
| NBIS @ $9 / $12 / $15 / $18 | 3.1 / 4.3 / 5.6 / 6.8 | 6.3 / 9.8 / 13.4 / 16.9 | 9.1 / 12.6 / 16.1 / 19.7 |

**What life does to those years.** Rubin chips in 2027–29 are 1–3 years old — still inside the five-year contract — so *their* EBIT does not change with N. Only the *old* fleet does:

| vs 7-year EBIT, $B | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| CRWV if chips last only 5 years | −0.35 | −0.35 | **−1.51** (Hopper thrown away, not re-rented) |
| CRWV if 9 / 11 years | +0.12 / +0.18 | +0.11 / +0.17 | +0.29 / +0.44 |
| NBIS if 5 years | 0 | −0.11 | −0.37 |
| NBIS if 9 / 11 years | 0 | +0.03 / +0.05 | +0.13 / +0.19 |

CRWV 2029 at $12 is $7.6B (5yr) / $9.1B (7yr) / $9.5B (11yr). NBIS is almost life-blind through 2029 because its fleet is young. Life for NBIS lives in 2030–31 and in the per-GPU tail above. Year-by-year current-fleet EBIT in [[#Appendix B — Fleet path detail]].

### What the stock is pricing

Today's enterprise value (2026-08-04) ÷ 2028 modeled earnings, 7-year life, 100% coverage, $12 rent: NBIS **2.3× EBITDA / 4.7× EBIT** on $46B EV. CRWV **4.7× / 7.8×** on $68B. Even $9 is 2.9× / 5.5×. That is today's EV over earnings that still require ~$37–46B of Rubin/Blackwell spend to exist. Read it as "the market does not believe scale, cash rent, or duration" — then name which. Full grid in [[#Appendix C — Multiples]].

### Can they fund and power it

Base Rubin: NBIS 200K GPUs / $37B. CRWV 120K / $22B. FY26 capex is inside both guides. FY27 is unguided for NBIS (~$22–26B). Microsoft's 40% funds *that* Microsoft cohort; later Microsoft add-ons are 0% upfront. CRWV's Rubin fits its $31–35B cadence and debt machine. Power: YE2028 needs 1.28 GW (NBIS) and 0.94 GW (CRWV), inside contracted pipelines. Detail in [[#Appendix D — Capex, funding, power]].

## Contradiction Check

Against [[Theses/NBIS - Nebius Group]] Insight #6, [[Theses/CRWV - CoreWeave]] Insight #6 / Q#8, and [[Sectors/Neoclouds & GPU-as-a-Service]] §Rubin fleet economics — those notes were rewritten 2026-08-13 to drop the 1.8×–3.0× corridor. This pass adds the life axis they still treat as secondary.

- **Supports:** a five-year take-or-pay at ~$12 with high coverage clears 15% at every life. Open-market from day one does not.
- **Adds:** $9 is a 5-year vs 7-year decision, not a blanket "clears" or "destroys." The 15% IRR rent moves $9.27 → $7.32 as life goes 5 → 11. Company 2027–29 EBIT is not the place to see that; the per-GPU tail and CRWV 2029 Hopper scrap are.
- **Breaks the operating case:** cash rent below the 15% IRR line for the life you actually believe (below $9.27 if you believe 5 years; below $8.22 if you believe 7), or coverage/vintage that puts the blend under the screen you are using.
- **Breaks the funding case:** treating Microsoft 40% as a 40% Rubin funding rate. January 2026 add-ons are already 0%.
- **Reveals life:** Hopper/Blackwell re-rent rates and any impairment language as those fleets hit year 5–6 (CRWV 2028–29, NBIS later). A 35–40% open-market step instead of 55% is the digestion print.
- **Prior notes:** [[Research/2026-08-04 - NBIS - Rubin Generation ROIC - deep-dive]] held-rate ($4.90–6) remains the below-IRR case at every life. [[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]] is the $11.6/hour retail-outlier unit model.

## Related Research

- [[_Archive/Backups/Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive (pre-rewrite 2026-08-13)]] — pre-rewrite record
- [[_Archive/Backups/Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive (pre-merge 2026-08-07)]] · [[_Archive/Backups/Research/2026-08-07 - NBIS CRWV - Customer Advances and Fleet ROIC - deep-dive (merged 2026-08-07)]]
- [[Theses/NBIS - Nebius Group]] · [[Theses/CRWV - CoreWeave]]
- [[Research/2026-08-04 - NBIS - Rubin Generation ROIC - deep-dive]]
- [[Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison]]
- [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]]
- [[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]]
- [[Sectors/Neoclouds & GPU-as-a-Service]] · [[Macro & Technology/Sustainability of AI Capex]]

---

## Appendix A — Accounting ROIC by life

Average EBIT ÷ original $183K. This is the screen, not IRR (IRR is in the body).

| Cash rent | 5 years | 7 years | 9 years | 11 years |
|---:|---:|---:|---:|---:|
| $9 | 13.6% | 13.7% | 13.2% | 12.6% |
| $12 | 23.3% | 22.0% | 20.7% | 19.5% |
| $15 | 32.9% | 30.4% | 28.2% | 26.3% |
| $18 | 42.6% | 38.7% | 35.7% | 33.1% |

It falls as life extends because the tail years are cheaper and the denominator never shrinks. Post-tax ≈ ×0.79 on EBIT.

---

## Appendix B — Fleet path detail

**Current fleets only, EBIT $B.** Includes NBIS's 140K Blackwell landing in 2027. No Rubin.

CRWV

| Life | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|---:|
| N=5 | 3.41 | 3.79 | 4.30 | 2.34 | 2.34 | 0.00 |
| N=7 | 3.41 | 4.14 | 4.65 | 3.85 | 3.75 | 1.29 |
| N=9 | 3.41 | 4.26 | 4.76 | 4.14 | 4.05 | 2.38 |
| N=11 | 3.41 | 4.32 | 4.82 | 4.29 | 4.19 | 2.52 |

NBIS

| Life | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|---:|
| N=5 | 0.80 | 2.22 | 3.02 | 3.52 | 2.88 | 2.02 |
| N=7 | 0.80 | 2.22 | 3.13 | 3.89 | 4.00 | 3.32 |
| N=9 | 0.80 | 2.22 | 3.16 | 4.02 | 4.34 | 3.66 |
| N=11 | 0.80 | 2.22 | 3.18 | 4.08 | 4.50 | 3.82 |

N=5 zeros CRWV in 2031 (Hopper scrapped 2029). CRWV standalone ~$2.1B interest consumes about half of pre-Rubin fleet EBIT.

**Scale at $15, 2028 EBIT $B** (Rubin units base / +25% / +50%).

| | Base | +25% | +50% |
|---|---:|---:|---:|
| CRWV EBIT | 10.8 | 12.3 | 13.8 |
| CRWV pretax | +6.9 | +8.0 | +9.0 |
| NBIS EBIT | 13.4 | 15.9 | 18.5 |

---

## Appendix C — Multiples

Today's EV ÷ modeled calendar earnings. 7-year life. Hopper re-rents hit CRWV EBITDA in 2029.

**NBIS EV $46B — EV/EBITDA**

| Rate | 2027 | 2028 | 2029 |
|---:|---:|---:|---:|
| $9 | 5.0× | 2.9× | 2.9× |
| $12 | 4.4× | **2.3×** | **2.3×** |
| $15 | 3.9× | 2.0× | 2.0× |
| $18 | 3.6× | 1.7× | 1.7× |

**NBIS — EV/EBIT**

| Rate | 2027 | 2028 | 2029 |
|---:|---:|---:|---:|
| $9 | 14.9× | 7.3× | 5.1× |
| $12 | 10.7× | **4.7×** | 3.7× |
| $15 | 8.3× | 3.4× | 2.9× |
| $18 | 6.8× | 2.7× | 2.3× |

**CRWV EV $67.9B — EV/EBITDA**

| Rate | 2027 | 2028 | 2029 |
|---:|---:|---:|---:|
| $9 | 8.3× | 5.5× | 6.0× |
| $12 | 7.7× | **4.7×** | 5.1× |
| $15 | 7.1× | 4.1× | 4.4× |
| $18 | 6.6× | 3.6× | 3.9× |

**CRWV — EV/EBIT**

| Rate | 2027 | 2028 | 2029 |
|---:|---:|---:|---:|
| $9 | 14.7× | 10.4× | 9.8× |
| $12 | 12.7× | **7.8×** | 7.5× |
| $15 | 11.2× | 6.3× | 6.1× |
| $18 | 10.1× | 5.3× | 5.1× |

---

## Appendix D — Capex, funding, power

| Cohort | NBIS | CRWV | Window |
|---|---:|---:|---|
| Hopper (sunk) | 1.7 | 5.5 | 2023–25 |
| Blackwell | 4.2 + 9.8 build | 8.4 | 2025–26, inside FY26 guides |
| Rubin base / +25% / +50% (200/250/300K · 120/150/180K) | 36.6 / 45.8 / 54.9 | 22.0 / 27.4 / 32.9 | H2-26 → 2028 (70+130 · 40+80) |
| Implied FY27 capex | ~$22–26B / ~$28–32B / ~$33–38B (rest FY28) | inside $31–35B / +$5.5B / +$11B over two years | FY27 unguided for NBIS |

| | NBIS | CRWV |
|---|---|---|
| Base | FY26 ≈ guide; FY27 ≈ $27B flat vs FY26. Microsoft 40% funds its cohort; use 0/20/40% prepay + cash/converts/ABL/ATM/optional ClickHouse | Base Rubin inside $31–35B + DDTL; 15–25% prepay supplements debt |
| +25% units | ~$36B FY27 → ~$9B extra → **~$0.6B/yr** interest at 7% ABL | +$5.5B, inside DDTL |
| +50% units | ~$45B FY27 → ~$18B extra → **~$1.3B/yr** | +$11B, DDTL 5.0+ |

| Active power (model W) | Base | +25% | +50% | vs disclosed |
|---|---:|---:|---:|---|
| NBIS YE27 → YE28 | 0.78 → **1.28 GW** | 0.85 → 1.48 | 0.91 → 1.67 | 3.5→4 GW contracted; 800 MW–1 GW connected YE26; PA GW site first power end-2027 |
| CRWV YE27 → YE28 | 0.63 → 0.94 GW | 0.67 → 1.06 | 0.71 → 1.17 | >1 GW active; 3.5 GW contracted |

---

## Appendix E — Assumptions, depreciation, costs

| Input | Value |
|---|---|
| Numeraire | $6.00/GPU-hr blended. Grids are absolute $9–18 |
| Rubin capex | $183K = $126K racks + $57K shell/power |
| Depreciation | Racks: yr1 30% · yr2 22% · yr3 14% · flat 34%/(N−3) yrs 4–N. Shell: 20-yr SL |
| Lives | 5 / 7 / 9 / 11 |
| Billed hours | 8,410/yr (96%) |
| Revenue | Contract yrs 1–5 → 55% step, −7%/yr, yrs 6–N |
| Cash costs | Rubin 30% of revenue · CRWV current 42% · NBIS current 52% |
| Current fleets | CRWV 130K H ($4) + 120K BW ($6) · NBIS 40K H + 200K BW |
| Rubin units | CRWV 120/150/180K · NBIS 200/250/300K |
| Earnings | Cash-economic: no financing accretion, no matching interest |

**Year-one EBIT is a convention.** At $9: +$12.3K with shell on 20-year SL; −$1.9K if year-1 charges 30% of all-in $183K.

**Merchant graduation** (% of launch rate): 100/65/50/45/42/40/37/34/32/30/28. Stricter 45% re-rent step: N=7 EBIT 282→269; N=11 392→356.

| Gen (age) | Launch contract | Spot now | Retention | Model at that age |
|---|---|---|---|---|
| Ampere (~6y) | ~$3.00–3.50 | $1.09–1.35 open · $2.00–3.50 channel | 35–40% open · 60–100% channel | 55% step ≈ the blend |
| Hopper (~3.5y) | ~$4.50–5.50 | $2.35–3.46 | 50–65% | 100% (in contract) |
| Blackwell (~1–1.5y) | ~$6.00 | $3.35–6.17 | 55–100% | 100% (in contract) |

**Cost completeness.** $57K shell ≈ $14.6/W. Electricity 30.7 MWh/GPU-yr → $3.1–5.4K, inside the 30% charge at $9–18. The 30% charge scales with revenue, so the model overstates cost at $18 and can understate it below ~$6. Terminal building value excluded (conservative). Taxes excluded from headline grids.

**Slot test.** Blackwell 2.2 kW, Rubin 3.9 kW, opex $1.49/W-yr, capex amortized 7-year SL. Replacement indifference vs live $6 Blackwell: **$13.75/hour**.

**Advance formula.** \(PV = q\cdot TCV + (1-q)\cdot TCV\cdot A(r,60)\). At 8%, \(A \approx 0.827\).

Primary filings: [NBIS 2025 20-F](https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231x20f.htm) · [Microsoft SOW](https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d4.htm) · [Microsoft Jan-2026 addendum](https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d5.htm) · [NBIS Q1](https://www.sec.gov/Archives/edgar/data/1513845/000110465926064092/nbis-20260331xex99d2.htm) · [CRWV 2025 10-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm) · [CRWV Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm).
