---
publish: false
date: 2026-08-05
updated: 2026-08-07
tags: [research, deep-dive, NBIS, CRWV, neoclouds, vera-rubin, ROIC, customer-advances, cash-flow]
sector: Neoclouds & GPU-as-a-Service
ticker: NBIS
source: vault synthesis — supersedes the held-rate framing in the 2026-08-04 Rubin ROIC note; corrected model per its Addendum 5 error audit
source_type: deep-dive
additional_sources:
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231x20f.htm
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d4.htm
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d5.htm
  - https://www.sec.gov/Archives/edgar/data/1513845/000110465926064092/nbis-20260331xex99d2.htm
  - https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm
  - https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm
merged_from:
  - "[[_Archive/Backups/Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive (pre-merge 2026-08-07)]]"
  - "[[_Archive/Backups/Research/2026-08-07 - NBIS CRWV - Customer Advances and Fleet ROIC - deep-dive (merged 2026-08-07)]]"
propagated_to: [NBIS, CRWV]
pending_propagation: [NBIS, CRWV]
---

# NBIS + CRWV — Rubin Fleet Economics: Rate-Multiple Sensitivity Model

## Thesis Delta

1. **Rubin operating economics still reduce primarily to the cash-equivalent rate achieved over current Blackwell contracts (~$6/GPU-hour), given Rubin's ~3× performance.** Lifetime EBIT per GPU on $183K invested at a seven-year life remains **1.5× → $175K · 2.0× → $282K · 2.5× → $389K · 3.0× → $496K**; the 15%-hurdle equivalent is $192K.
2. **The rational operating-price corridor remains 1.8×–3.0×, but customer advances create a separate funding overlay.** The five-year take-or-pay wrapper protects the initial rate and is worth ~$160K/GPU versus merchant pricing at 2.0×; collecting part of that wrapper early lowers external capital and raises project NPV without changing gross fleet ROIC at a given cash-equivalent price.
3. **NBIS's original Microsoft agreement provides for ~$6.96B of upfront payments, or 40% of $17.39B TCV, versus CRWV's disclosed 15–25% weighted-average prepayment across active contracts.** The advantage is contract-specific: two January 2026 Microsoft add-on tranches carry no upfront payment, while Meta and Rubin order-level terms remain undisclosed.
4. **A 40% advance is worth ~8.3% of TCV in present-value terms at an 8% discount rate over five years—not 40%.** It can turn a marginal $9/hour contract into roughly $9.75/hour on a monthly-billed equivalent basis, but it cannot make $6/hour equivalent to the ~$9.50 absolute operating hurdle.
5. **Rubin year-one EBIT remains positive across the sampled 1.5×–3.0× axis, but the company cash-flow path now separates sharply from fleet EBIT.** Q1 2026 NBIS received $3.20B through deferred revenue against $2.47B cash capex; reported FCF of −$0.22B becomes approximately −$3.41B before that cohort-financing inflow.
6. **The prior “NBIS interest ~nil” and “prepayments scale with Meta/MSFT” assumptions are retired as reported-earnings base cases.** The model now uses a cash-economic fleet convention—nominal cash service price with customer-financing revenue accretion and matching interest excluded symmetrically—and treats prepayment rate, milestone timing and implicit borrowing cost as separate sensitivities.

## Summary

This note integrates the corrected Rubin operating model with the customer-financing and cash-flow layer. Rubin's physical economics remain governed by rate, coverage, capex, utilization, cash cost and useful life. The 1.8×–3.0× rational corridor and the contract-versus-merchant gap are unchanged. Customer advances change who funds the asset and when cash arrives: the customer pays part of future service fees before delivery, the operator records deferred revenue, and future monthly cash billing falls as the advance is consumed.

That distinction prevents two opposite errors. Subtracting the advance from physical capex makes net-capital ROIC appear exceptional or undefined even though the operator still owes service, SLA and potential refund performance. Ignoring it understates the project-financing advantage and equity IRR. At an 8% discount rate, 15%/25%/40% upfront payments add approximately 3.1%/5.2%/8.3% to contract present value versus fully monthly billing. NBIS therefore has a material funding advantage on the original Microsoft cohort, but not proof of superior pricing or a durable 40% funding rate for Rubin. CRWV's advances remain material while its larger DDTL, OEM, lease and debt stack leaves more fleet economics exposed to cash interest and refinancing.

## Framework / Mental Model

**The pricing corridor.** Three lines locate Rubin's rational price:

| Line | Multiple | $/GPU-hr | Meaning |
|---|---:|---:|---|
| ROIC hurdle (15%) | ~1.6× | ~$9.50 | Below this, Rubin destroys value vs the hurdle |
| **Deployment floor** (slot test) | **~1.8×** | **~$10.60** | Revenue per watt matches current Blackwell — below this, sweating old fleets beats installing Rubin |
| **Performance-parity ceiling** | **~3.0×** | **~$18.00** | Customer's cost per unit of compute is flat vs Blackwell — above this, customers get no hardware gain |

Corridor = 1.8× to 3.0× → ROIC 19–39%. The hurdle sits *below* the deployment floor: rational deployment implies hurdle-clearing returns. The sampled axis (1.5×/2.0×/2.5×/3.0×) brackets the corridor: **2.0×, 2.5× and 3.0× sit inside it** (3.0× at the parity ceiling); 1.5× is the below-floor bear bound. Market anchors for calibration: 2× ($12/hr, ~$26/W-yr) ≈ IREN–Microsoft GB300 per-GPU rate; 3× (~$39/W-yr) ≈ IREN per-watt tier; 4× (~$52/W-yr) sits above the xAI–Google retail deal (~$46/W-yr) and means customers pay more per unit of performance than on Blackwell — sustained only in extreme scarcity.

**Customer-financing overlay.** An advance is future service consideration collected early, not incremental TCV or a permanent capex grant. For a five-year monthly-billed contract, 40% upfront lifts present value by ~8.3% at an 8% discount rate. The operator may keep that benefit through lower external funding, or surrender it through lower $/GPU-hour, fixed-rate duration, priority rights, service credits or refund protection. Gross fleet ROIC uses full physical capex and cash-equivalent service revenue; project IRR separately includes advance timing and reduced future collections.

Mental-model checks:

- **[[Mental Models/Generalist - Overview|G-7]]:** deferred-revenue inflows sit in CFO while functioning as customer project financing; significant-financing accretion can raise reported revenue and interest together.
- **[[Mental Models/Generalist - Overview|G-8]]:** access to customer funding can determine which cohort gets built before software differentiation matters.
- **[[Mental Models/Generalist - Overview|G-10]]:** netting the advance against invested capital can mechanically inflate ROIC without changing GPU productivity.
- **[[Mental Models/Generalist - Overview|G-12]]:** advances reduce conventional leverage but replace it with execution-contingent service and refund obligations.
- **[[Mental Models/Lens - Value Layer Monopoly|Value Layer Monopoly lens]]:** a large advance may signal scarce-capacity control or hyperscaler bargaining power. The discriminator is cash-equivalent price after payment-timing adjustment.

Agreement across these lenses triggers disconfirmation rather than commitment: an order-level Rubin disclosure containing both $/GPU-hour and prepayment timing is the single clean test.

## Evidence

### Assumptions (corrected model)

| Input | Value |
|---|---|
| Blackwell contract base rate | **$6.00/GPU-hr — a blended contract-vintage assumption, not spot.** The market is bifurcated: full-stack dedicated ~$11–12 (IREN–MSFT ~$95K/GPU-yr; xAI $11.6) > merchant list avg ~$6.17 > **NBIS/CRWV implied wholesale ~$3.35–5.70** (NBIS-MSFT deal math; CRWV blended realized) > reserved low $3.35. $6 was calibrated to reproduce reported 2026 revenue — mildly generous vs NBIS's own wholesale. **Anchor caveat:** the grids' rows are absolute ($9–18/hr), but the corridor bounds scale with the true anchor while the hurdle (~$9.50 absolute) does not — below a ~$5.40 anchor the slot floor drops under the hurdle and "rational deployment ⇒ hurdle-clearing" breaks (a $8.00–9.50 deploy-but-under-earn zone opens). NBIS's implied wholesale straddles that threshold → its true realized Blackwell rate is the decisive disclosure |
| Rubin capex | $183K/GPU all-in = $126K racks + $57K shell/power |
| Depreciation | **Non-linear descending-then-flat, everywhere** (no metric uses straight-line): racks yr1 30% · yr2 22% · yr3 14% · flat 34%/(N−3) yrs 4–N · shell 20-yr SL |
| Lives (N) | 5 / 7 / 9 / 11 yrs — sets the flat-tail rate, the re-rent window, and the scrap date. **Carried fully in Grids 1 & 2; Grids 3–4 shown at N=7 with the exact life-adjustment table under Grid 3** (Rubin's 2027–29 contribution is life-invariant: ages 1–3 share identical 30/22/14 weights at every N) |
| Billed hours | 8,410/yr (96% — take-or-pay pays on availability) |
| Revenue curve | Contract rate yrs 1–5 → re-rent at 55%, −7%/yr, yrs 6–N |
| Cash costs | Rubin 30% of revenue · CRWV current fleet 42% · NBIS current fleet 52% |
| Current fleets | CRWV: 130K Hopper ($4/hr) + 120K Blackwell ($6/hr) · NBIS: 40K Hopper + 200K Blackwell (140K lands 2027) |
| Rubin cohorts (from 2027) | CRWV 120K (=BW base) / 150K / 180K · NBIS 200K / 250K / 300K |
| **Cohort definition** | Unit counts are the **cumulative Rubin-generation fleet**, deployed on **Blackwell-matched cadence**: NBIS 70K (2027) + 130K (2028), CRWV 40K (2027) + 80K (2028) at base; tranches scale proportionally at +25%/+50%. **All grids are calendar-year** |
| Customer-advance overlay | NBIS 0% / 20% / 40% of TCV · CRWV 15% / 20% / 25%; separate 6% / 8% / 10% discount-rate and receipt-timing sensitivities. These are funding variables, not reductions to $183K physical capex |
| Earnings convention | Fleet grids use nominal cash service price and exclude both customer-financing GAAP revenue accretion and its matching interest expense. Company-reported bridges must add both, or neither |
| **Two sensitivity axes — do not conflate** | **Rate multiple** (1.5× / 2.0× / 2.5× / 3.0× of $6/hr; Grids 1, 3, 4) vs **unit scale** (fleet size base / +25% / +50% of BW units; scale line, Grid 5). Capex depends only on units; per-GPU ROIC only on rate; EBIT/EV on both |

### Pricing by asset age — the graduation-profile check

The model's age profile (shown at 2.0× = $12 contract): **years 1–5 flat at contract rate** (take-or-pay), then **graduation onto the empirical aging curve at roll** — 55% of contract at year 6, −7%/yr after ($6.60 → $4.59 by year 11). The step and slope are calibrated to the observed record: H100 re-signing at ~50–65% of contract-vintage rates (2026), A100 plateau decay ~−7%/yr (2023–26).

**Why not full Ampere/Hopper graduation from year 1:** the observed generational decay is the *spot/merchant* curve; take-or-pay transfers that decay to the customer for the term (IREN–MSFT flat ~$95K/GPU-yr × 5yrs; Google–SpaceX flat $920M/mo; the NBIS/CRWV backlogs). The counterfactual quantifies what the contract wrapper is worth — a merchant fleet priced on the empirical graduation composite (100/65/50/45/42/40/37/34/32/30/28% of launch rate) at 2.0×:

| Lifetime EBIT per GPU at 2.0×, $K | N=7 | N=11 |
|---|---:|---:|
| Contracted (Grid 1 below) | 282 | 392 |
| **Merchant (graduation from yr 1)** | **122** | **198** |
| 15%-hurdle equivalent | 192 | 302 |

**The merchant fleet fails the hurdle at every life; the contracted fleet clears it from 2.0× up. The contract wrapper is worth ~$160–194K/GPU at 2.0×** — the entire difference between a hurdle-clearing and value-destroying Rubin deployment, which is why backlog term/coverage is the most valuable disclosure in this sector. Sensitivities: a stricter 45% re-rent step (graduation-consistent low end) trims lifetime EBIT ~5% (N=7: 282→269; N=11: 392→356) — conclusions unchanged; any **uncontracted** capacity rides the merchant curve from day 1 — the model assumes 100% coverage, so disclosed contract-coverage % is the swing variable.

**Observed falloff — spot today vs original contract vintage (Aug 2026), vs the model:**

| Gen (age) | Launch contract vintage | Spot today | Retention | Model at same age |
|---|---:|---|---|---|
| Ampere (~6y) | ~$3.00–3.50 | $1.09–1.35 open · $2.00–3.50 hyperscaler channel | **35–40% open · 60–100% channel** | 55% (re-rent step) ≈ **the blend** |
| Hopper (~3.5y) | ~$4.50–5.50 | $2.35–3.46 (+40% contract rebound Oct-25→Mar-26) | **50–65%** | 100% (in contract; spot marks the customer) |
| Blackwell (~1–1.5y) | ~$6.00 | $3.35–6.17 | **55–100%** | 100% (in contract) |

Validation: Hopper spot at age 3.5 (~55–60% of contract vintage) forward-implies a roll at age 5–6 near ~50–55% — independently reproducing the model's 55% step. Plateau decay: observed A100 −5%/yr (2023–26) vs modeled −7%/yr (slightly conservative). Anchoring on launch *spot peaks* instead (H100 $8, A100 $4) shows −64–70% falloffs — but no contracted operator booked those peaks. **Cycle caveat: the entire observed record is shortage-vintage** — in a normalized market (2028–29 digestion) the age-6 step could land at the open-market 35–40% rather than the 55% blend, and that is exactly when the CRWV (then NBIS) rolls occur; the re-rent step is the model's most cycle-dependent input.

### Grid 1 — Rubin standalone lifetime EBIT per GPU ($K, on $183K invested; rate multiple × life)

| Multiple ($/hr) | N=5 | N=7 | N=9 | N=11 |
|---|---:|---:|---:|---:|
| 1.5× ($9.00) | 125 | 175 | 218 | 255 |
| 2.0× ($12.00) | 213 | 282 | 341 | 392 |
| 2.5× ($15.00) | 301 | 389 | 465 | 529 |
| 3.0× ($18.00, parity) | 390 | 496 | 588 | 666 |
| *15%-hurdle equivalent (0.15 × N × $183K)* | *137* | *192* | *247* | *302* |

**Read:** Total lifetime EBIT per GPU rises with both rate and life. The rate multiple is the steep axis (each 0.5× step adds ~$90–110K at N=7); life is the shallow one (re-rent tail years at 55% of contract, −7%/yr). Against the hurdle row: **1.5× fails at every life; 2.0×+ clears at every life** — at 2.0×/N=7 a GPU earns **$282K on $183K invested (1.54× capex as EBIT)**, scaling to 2.14× at N=11. Figures are pre-tax (post-tax ≈ ×0.79; hurdle-clearing multiple then ~1.9×, coincident with the ~1.8× deployment floor).

### Cost-completeness audit (what the ROIC does and does not charge)

| Layer | Treatment | Check |
|---|---|---|
| Capex — GPUs, racks, HBM/storage, networking, power infra, liquid cooling, civil | In the $183K/GPU (Foxconn $47B/GW is facility-all-in) | Non-rack slice $57K/GPU ≈ $14.6/W ✓ matches industry DC benchmark $10–15M/MW |
| Electricity | Inside the 30%-of-revenue cash charge | Bottom-up: 30.7 MWh/GPU-yr → $3.1–5.4K vs charge headroom — covered 2–4× over |
| Non-power DC opex (staff, maintenance, water, security, transit) | Inside the 30% | ~$0.7/W ≈ $2.7K/GPU-yr ✓ |
| Component replacement (optics/transceivers, fans, HBM failures, spares) | Inside the 30% — **not a named line** | ~1.5% capex/yr ≈ $2.7K ✓ fits; erosion risk concentrates in the N=9–11 columns |
| Marginal SG&A | Residual of the 30% (~$12–37K/GPU-yr rising with rate) | Conservative: true DC costs scale with watts, the charge scales with revenue → model *overstates* costs at high multiples (~$35K/GPU-yr at 3.0× vs ~$10K bottom-up) |
| Financing | Fleet EBIT excludes conventional interest and customer-advance accretion; company pretax bridges add the relevant financing stack separately | Customer advances may carry implicit interest even without a cash coupon; conventional debt remains the +25/+50% swing |
| Construction WIP | Excluded → company ROIC prints below fleet ROIC | Flagged, Grid 5 |
| Terminal shell value | Excluded (conservative) | Shell outlives GPUs; re-rackable |
| Taxes | Excluded from headline grid | Post-tax line above |

### Customer advances — pricing, funding and ROIC overlay

#### Mechanics and disclosed structures

| Stage | Accounting treatment | Economic treatment |
|---|---|---|
| Contract signed | No revenue until service performance | Customer reserves capacity, normally under take-or-pay terms |
| Advance invoiced/received | Cash and deferred revenue increase | Customer supplies working/project capital |
| Build and acceptance | PP&E/WIP and capex increase; service revenue waits for availability | Operator bears procurement, construction and delivery risk |
| Service delivered | Deferred revenue is released into revenue | Prepaid fees reduce later monthly cash collections |
| Delay/SLA failure/termination | Credits, liability reclassification or refund may apply | Advance becomes an operationally senior claim on liquidity |

| | NBIS | CRWV |
|---|---|---|
| Disclosed prepayment | Original Microsoft: ~$6.958B of ~$17.393B TCV = **40%** | Weighted average across active contracts: **15–25% of TCV** |
| Breadth | Microsoft base contract only; two Jan-2026 add-on tranches have **no upfront**; Meta/Rubin terms undisclosed | Portfolio-wide historical range; future Rubin terms can differ |
| 2026-03-31 balance | Deferred revenue **$4.778B** | Deferred revenue **$7.5B**; $1.3B reclassified to customer liabilities during Q1 |
| Funding stack | Advances + converts/equity + emerging asset-backed debt | Advances + DDTL/OEM/lease/debt; some customer deposits enter restricted waterfalls |
| Principal risk | Milestone timing, acceptance, refund and concentrated customer obligation | Debt service/refinancing plus committed delivery and customer concentration |

Primary filings: [NBIS 2025 20-F](https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231x20f.htm) · [Microsoft SOW](https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d4.htm) · [Microsoft Jan-2026 addendum](https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d5.htm) · [NBIS Q1 statements](https://www.sec.gov/Archives/edgar/data/1513845/000110465926064092/nbis-20260331xex99d2.htm) · [CRWV 2025 10-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm) · [CRWV Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm).

#### Pricing value of early cash

For a five-year contract with monthly billing, $q$ paid at inception and annual discount rate $r$:

$$
PV_{prepay}=q\cdot TCV+(1-q)\cdot TCV\cdot A(r,60)
$$

At 8%, the 60-month annuity factor as a share of nominal TCV is approximately 0.827:

| Upfront share of TCV | PV uplift vs fully monthly billing | Economically neutral headline-price discount |
|---:|---:|---:|
| 15% | 3.1% | 3.0% |
| 25% | 5.2% | 5.0% |
| 40% | 8.3% | 7.7% |

A $9/hour contract with 40% upfront is equivalent to approximately $9.75/hour paid monthly; $6/hour becomes ~$6.50, still far below the ~$9.50 absolute operating hurdle. The advance can move a marginal deal across a capital hurdle but cannot rescue deeply sub-economic pricing. Milestone rather than day-one receipt lowers the benefit; expensive or unavailable alternative funding raises it.

#### Rubin 2.0× bridge

At $12/hour, each Rubin GPU earns $100.9K annual revenue and $504.6K five-year nominal TCV against $183K all-in capex. Cash costs remain 30%; seven-year average pre-tax gross fleet ROIC remains approximately $282K ÷ 7 ÷ $183K = **22%**.

| Illustrative funding structure | Advance/GPU | Face-value capex coverage | Operator funding at inception | Incremental five-year project NPV at 8% |
|---|---:|---:|---:|---:|
| No advance | $0 | 0% | $183.0K | $0 |
| CRWV-like 15% | $75.7K | 41% | $107.3K | +$13.1K |
| CRWV-like 25% | $126.2K | 69% | $56.9K | +$21.8K |
| NBIS Microsoft-like 40% | $201.8K | 110% | **$18.8K initial surplus** | +$34.8K |

The table transplants historical prepayment percentages into an illustrative Rubin cohort, assumes advance and capex at inception, and excludes tax, financing fees and terminal/re-rent value. It is not evidence of either company's Rubin payment terms. Face-value coverage measures funding; the NPV column measures incremental value. Subtracting the full advance from capex makes equity ROIC meaningless once the advance exceeds capex, even though full service obligations remain.

#### Measurement and GAAP bridge

| Metric | Correct treatment | Error to avoid |
|---|---|---|
| Gross fleet ROIC | NOPAT on cash-equivalent service revenue ÷ full operating asset base | Subtracting the entire advance from physical capex |
| Project IRR/NPV | Include advance timing, reduced future collections, capex timing and refund risk | Treating the advance as extra TCV |
| Reported EBIT | Bridge significant-financing revenue accretion explicitly | Reading financing gross-up as operating pricing power |
| Pretax income | Include the matching customer-financing interest expense | Grossing up revenue while assuming zero interest |
| FCF | Separate FCF before deferred-revenue changes from advance-funded FCF | Capitalizing net new advances as a recurring perpetuity |
| EV | Do not treat advance-funded cash as excess without the service/refund obligation | Netting cash while ignoring deferred revenue |

Both companies evaluate payment/service gaps longer than one year for a significant financing component. NBIS records early-customer-funding accretion as revenue plus interest expense; CRWV states that interest expense includes revenue agreements with significant financing components. Use one of two internally consistent conventions: **cash-economic** (nominal cash consideration; no accretion or matching interest) or **GAAP** (grossed-up revenue plus matching interest). The fleet grids use the former.

#### Cash-flow profile and the advance treadmill

| Q1 2026, $B | NBIS | CRWV |
|---|---:|---:|
| Deferred-revenue cash-flow contribution | **+3.198** | +0.575 |
| Operating cash flow | 2.258 | 2.984 |
| Cash capex | (2.473) | (7.695) |
| Reported FCF | **(0.215)** | (4.711) |
| FCF excluding deferred-revenue contribution | **(3.413)** | (5.286) |

The ex-advance line is a normalization, not a claim that the cash is unusable. During rapid bookings growth, new advances can exceed old deferred-revenue run-off and make CFO appear structurally strong. When bookings flatten, the inflow stops while prepaid service delivery, opex and debt service continue. Terminal FCF therefore sets net new customer advances to zero unless the valuation also assumes perpetual capacity growth and replacement capex.

### Grid 2 — Current fleets standalone, EBIT $B (no Rubin)

**CRWV**

| Life | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|---:|
| N=5 | 3.41 | 3.79 | 4.30 | 2.34 | 2.34 | 0.00 |
| N=7 | 3.41 | 4.14 | 4.65 | 3.85 | 3.75 | 1.29 |
| N=9 | 3.41 | 4.26 | 4.76 | 4.14 | 4.05 | 2.38 |
| N=11 | 3.41 | 4.32 | 4.82 | 4.29 | 4.19 | 2.52 |

**NBIS**

| Life | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|---:|
| N=5 | 0.80 | 2.22 | 3.02 | 3.52 | 2.88 | 2.02 |
| N=7 | 0.80 | 2.22 | 3.13 | 3.89 | 4.00 | 3.32 |
| N=9 | 0.80 | 2.22 | 3.16 | 4.02 | 4.34 | 3.66 |
| N=11 | 0.80 | 2.22 | 3.18 | 4.08 | 4.50 | 3.82 |

**Read:** Both fleets are earnings machines through 2030 at any life ≥7. The life assumption matters only in the out-years: at N=5 CRWV's fleet revenue reaches zero in 2031; at N=9–11 it still earns ~$2.4–3.8B. CRWV's ~$2.1B interest consumes roughly half its standalone fleet EBIT.

### Grid 3 — Combined revenue and EBIT $B by rate multiple (N=7, base units, calendar years)

*Multiple = Rubin rental price vs today's $6/hr Blackwell contract: 1.5× = $9 · 2.0× = $12 · 2.5× = $15 · 3.0× = $18 (performance-parity) per GPU-hr.*

**CRWV (Rubin 40K in 2027 + 80K in 2028; pretax = EBIT − $3.9B interest)**

| Multiple | 2027 | 2028 | 2029 |
|---|---|---|---|
| 1.5× | rev 13.5 · EBIT 4.6 · pretax **+0.7** | 19.5 · 6.5 · +2.6 | 17.5 · 6.9 · +3.0 |
| 2.0× | rev 14.5 · EBIT 5.3 · pretax +1.4 | 22.5 · 8.7 · +4.8 | 20.6 · 9.1 · +5.2 |
| 2.5× | rev 15.5 · EBIT 6.0 · pretax +2.1 | 25.6 · 10.8 · +6.9 | 23.6 · 11.2 · +7.3 |
| 3.0× | rev 16.5 · EBIT 6.8 · pretax +2.9 | 28.6 · 12.9 · +9.0 | 26.6 · 13.3 · +9.4 |

**NBIS (Rubin 70K in 2027 + 130K in 2028; cash-economic convention—customer-financing accretion and matching interest excluded symmetrically)**

| Multiple | 2027 | 2028 | 2029 |
|---|---|---|---|
| 1.5× | rev 16.7 · EBIT **+3.1** | 26.6 · +6.3 | 26.6 · +9.1 |
| 2.0× | rev 18.5 · **+4.3** | 31.6 · +9.8 | 31.6 · +12.6 |
| 2.5× | rev 20.3 · **+5.6** | 36.7 · +13.4 | 36.7 · +16.1 |
| 3.0× | rev 22.0 · +6.8 | 41.7 · +16.9 | 41.7 · +19.7 |

**Read:** Every scenario is EBIT-positive from year one and ramps as tranche 2 lands. 2028 is the rate-reveal year: NBIS cash-economic revenue prints ≈ $27B / $32B / $37B / $42B across the four worlds. Reported GAAP revenue can run above these cells when customer-advance financing accretion is material, with the offset below EBIT as interest expense; compare pretax cash economics rather than EBIT alone. 2027 remains transitional.

**Life adjustment (exact, additive — converts any cell above to any life).** Rubin's 2027–29 contribution is life-invariant (ages 1–3, identical weights at every N); the only N-dependence is the current fleet, i.e. Grid 2's rows. Add these deltas to any Grid 3 EBIT cell:

| EBIT delta vs N=7, $B | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| CRWV N=5 | −0.35 | −0.35 | **−1.51** (Hopper scrapped rather than re-rented) |
| CRWV N=9 / N=11 | +0.12 / +0.18 | +0.11 / +0.17 | +0.29 / +0.44 |
| NBIS N=5 | 0.00 | −0.11 | −0.37 |
| NBIS N=9 / N=11 | 0.00 | +0.03 / +0.05 | +0.13 / +0.19 |

The one material cell is **CRWV 2029 at N=5**: at the 2.0× rate its EBIT spans 7.6 (N=5) → 9.1 (N=7) → 9.5 (N=11), i.e. EV/EBIT 8.9× → 7.5× → 7.1×. NBIS is nearly life-invariant through 2029 (young fleet); its life exposure sits in Grid 2's 2030–31 columns and Grid 1's Rubin tail.

### Scale sensitivity (2.5× rate, 2028 EBIT $B, Rubin units base / +25% / +50%, calendar basis)

| | Base | +25% | +50% |
|---|---:|---:|---:|
| CRWV EBIT (pretax) | 10.8 (+6.9) | 12.3 (+8.0) | 13.8 (+9.0) |
| NBIS EBIT | 13.4 | 15.9 | 18.5 |

**Read:** At corridor pricing, scale is monotonically accretive — more Rubin is better at any deployment size. (Below the ~1.6× hurdle, scale amplifies value destruction instead; the multiple, not the unit count, is the decision variable.) *Single-vintage convention retired 2026-08-05 — all grids are calendar-basis on Blackwell-matched cadence.*

### Grid 4 — EV/EBITDA and EV/EBIT by rate multiple (today's EV ÷ modeled earnings)

*Rows are the same rate multiples as Grid 3 (Rubin rental vs $6/hr Blackwell: 1.5×=$9 · 2.0×=$12 · 2.5×=$15 · 3.0×=$18/GPU-hr).* EV inputs (2026-08-04 prices, per [[Research/2026-08-04 - NBIS vs CRWV - Competitive Comparison]]): NBIS $46.0B conventional (stake-adjusted $39.6B → all NBIS multiples ~14% lower) · CRWV $67.9B.

**NBIS — EV $46B (EBITDA steps up as tranche 2 lands in 2028; no re-rents before 2030)**

| Multiple | EV/EBITDA 2027 | 2028–29 | EV/EBIT 2027 | 2028 | 2029 |
|---|---:|---:|---:|---:|---:|
| 1.5× | 5.0× | 2.9× | 14.9× | 7.3× | 5.1× |
| 2.0× | 4.4× | **2.3×** | 10.7× | **4.7×** | 3.7× |
| 2.5× | 3.9× | 2.0× | 8.3× | 3.4× | 2.9× |
| 3.0× | 3.6× | 1.7× | 6.8× | 2.7× | 2.3× |

**CRWV — EV $67.9B (Hopper re-rents 2029, so EBITDA dips that year)**

| Multiple | EV/EBITDA 2027 / 28 / 29 | EV/EBIT 2027 | 2028 | 2029 |
|---|---:|---:|---:|---:|
| 1.5× | 8.3× / 5.5× / 6.0× | 14.7× | 10.4× | 9.8× |
| 2.0× | 7.7× / **4.7×** / 5.1× | 12.7× | **7.8×** | 7.5× |
| 2.5× | 7.1× / 4.1× / 4.4× | 11.2× | 6.3× | 6.1× |
| 3.0× | 6.6× / 3.6× / 3.9× | 10.1× | 5.3× | 5.1× |

**Read:** Across the corridor (2.0–3.0×), today's EV prices at **2.3×–1.7× 2028 EBITDA for NBIS** and **4.7×–3.6× for CRWV** — versus NBIS's current optical ~14× EV/FY26-revenue; even the below-hurdle 1.5× world is only 2.9× / 5.5×. 2027 multiples are transition-year optics (tranche 1 only). The market is pricing disbelief in at least one of three things: **scale** (the cohorts don't deploy on cadence), **rate** (contracts embed a sub-corridor multiple), or **duration** (post-2029 re-rent cliff / hyperscaler in-housing truncates the annuity). Naming which disbelief is mispriced is the trade.

**Caveats:** EV is static (today's) — CRWV's base Rubin build adds ~$22B of debt (pro-forma EV ~$90B: multiply CRWV rows by ~1.3×). NBIS customer advances reduce conventional borrowing but do not create free excess cash: the ~$4.8B deferred-revenue balance carries service/refund obligations and can contain a significant financing component. Do not net advance-funded cash from EV while ignoring the liability. All years are calendar (Blackwell-matched deployment cadence).

### Grid 5 — Deployment feasibility: capital, funding, and power behind each scenario

**Capex implied by the model ($B):**

| Cohort | NBIS | CRWV | Spend window |
|---|---:|---:|---|
| Hopper (installed) | 1.7 | 5.5 | 2023–25 (sunk) |
| Blackwell | 4.2 + 9.8 build | 8.4 | 2025–26 — inside FY26 guides |
| Rubin **unit-scale** base / +25% / +50% (NBIS 200/250/300K · CRWV 120/150/180K GPUs, cumulative) | 36.6 / 45.8 / 54.9 | 22.0 / 27.4 / 32.9 | H2-26 → 2028 (tranches: NBIS 70K+130K · CRWV 40K+80K) |
| **Implied FY27 capex** | **~$22–26B / ~$28–32B / ~$33–38B** (remainder into FY28) | inside $31–35B cadence / +$5.5B / +$11B spread over two years | FY27 is **unguided** for NBIS |

**Funding check — the model does NOT assume all cash into GPUs; it assumes the funding stack keeps scaling:**

| | NBIS | CRWV |
|---|---|---|
| Base case | FY26 ≈ guide ($20–25B ✓); FY27 ≈ $27B ≈ flat vs FY26. Original Microsoft prepayment materially funds its cohort, but future Microsoft add-ons disclose 0% upfront and Meta/Rubin terms are unknown; use 0%/20%/40% prepayment sensitivities plus cash, converts, ABL/ATM and optional ClickHouse monetization | Base Rubin fits inside the existing $31–35B capex cadence and DDTL machinery; 15–25% historical customer prepayments supplement rather than replace the debt stack |
| +25% units | Needs ~$36B FY27 → ~$9B incremental external funding → **~$0.6B/yr interest drag** if ABL-funded at 7% (grids assume ~nil NBIS interest — trim accordingly) | +$5.5B — comfortably inside DDTL capacity |
| +50% units | Needs ~$45B FY27 → ~$18B incremental → **~$1.3B/yr interest**; approaching the dilution-or-leverage territory of thesis Insight #2 | +$11B — stretches but plausible via DDTL 5.0+ |

**Power and land — land is not the constraint; energization cadence is:**

| Active power implied (model watts) | Base | +25% | +50% | vs disclosed |
|---|---:|---:|---:|---|
| NBIS YE2027 → YE2028 | 0.78 → **1.28 GW** | 0.85 → 1.48 GW | 0.91 → 1.67 GW | 3.5→4GW contracted (>75% owned); 800MW–1GW connected YE26 target; Vineland/Finland/UK/Israel/Missouri pipeline; **PA gigawatt site first power end-2027** |
| CRWV YE2027 → YE2028 | 0.63 → 0.94 GW | 0.67 → 1.06 GW | 0.71 → 1.17 GW | >1GW active already; 3.5GW contracted — comfortable at every scale |

**Read:** On calendar cadence the 2027 energization tension dissolves — YE27 needs (0.78–0.91GW) sit inside the YE26-connected envelope, and YE28 targets (1.28–1.67GW) map onto the 2027–28 pipeline including Pennsylvania ramping through 2028. Funding remains the +25%/+50% binding constraint, but the company contrast is now conditional rather than categorical: CRWV is power-rich and debt-heavy; NBIS has a proven customer-funding advantage on the original Microsoft cohort but remains exposed to zero-prepay future tranches.

**Four model concessions:** (1) future NBIS prepayment rate is undisclosed and no longer assumed to scale automatically; (2) customer advances can contain implicit financing interest even without cash coupon—fleet grids exclude both GAAP accretion and matching interest; (3) invested capital counts only revenue-producing cohorts, while construction WIP depresses company ROIC during the build; and (4) advance-driven CFO is a cohort funding flow whose run-off must be included when growth slows.

## Contradiction Check

- **What breaks the corridor logic:** take-or-pay contracts signed *below* the deployment floor after adjusting for payment timing. A 40% advance lifts five-year contract PV by only ~8% at an 8% discount rate, so it cannot rescue a deeply low cash rate.
- **What breaks the funding case:** extrapolating the original Microsoft 40% advance to Rubin, Meta or later Microsoft cohorts. The January 2026 add-ons already disclose zero upfront payment; future order-level terms are the funding falsifier.
- **What reveals the rate early:** cash-equivalent revenue per active watt, any disclosed dedicated Rubin contract rate, and guidance slopes after separating significant-financing revenue accretion from service revenue.
- **What reveals the funding economics:** prepayment percentage, milestone dates, implicit borrowing rate, refund/termination rights and whether advance-funded cash is restricted. Advance size without those terms cannot establish pricing power.
- **EBITDA remains an incomplete discriminator:** it excludes the depreciation that determines gross fleet ROIC, while customer-financing accretion can raise revenue/EBIT and the matching charge appears below EBIT.
- **Cash-flow bull falsifier:** Rubin contracts disclose sub-$9.50 cash-equivalent pricing or NBIS must fund future cohorts with little advance and conventional leverage. **Bear falsifier:** order-level contracts show corridor pricing plus ≥20–40% upfront funding without a larger price giveback or broad refund optionality.
- **Prior-note reconciliation:** the 2026-08-04 held-rate ROIC (~0–9%) remains a below-floor stress case. This merged note adds the financing layer without changing the physical-capex, depreciation or contract-versus-merchant derivation.

## Related Research

- [[_Archive/Backups/Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive (pre-merge 2026-08-07)]] · [[_Archive/Backups/Research/2026-08-07 - NBIS CRWV - Customer Advances and Fleet ROIC - deep-dive (merged 2026-08-07)]] — immutable pre-merge source records.
- [[Theses/NBIS - Nebius Group]] · [[Theses/CRWV - CoreWeave]]
- [[Research/2026-08-04 - NBIS - Rubin Generation ROIC - deep-dive]] — derivation history: base model, historical launch-pricing test, $/watt scrap-and-slot model, error audit
- [[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]] — the One Chart cost-floor / value-ceiling framework
- "The Economics of a Neocloud" (5 Jul 26, _Inbox pending /ingest) — payback consensus source; its xAI/IREN/wholesale rate anchors calibrate the multiples
- [[Sectors/Neoclouds & GPU-as-a-Service]] · [[Macro & Technology/Sustainability of AI Capex]]
