---
publish: false
date: 2026-05-24
tags: [research, synthesis, portfolio, semiconductors, rebalancing]
status: active
sector: Multiple (Semiconductors)
source: Vault synthesis — Live Portfolio FMP refresh 2026-05-23 16:50 + [[Mental Models/Industry - Semiconductors]] + 19 per-position thesis notes (TSM, NVDA, 000660 SK Hynix, SNDK, AMD, LITE, AVGO, MRVL, LRCX, AMAT, KLA, ASMI, BESI, 6981 Murata, VICR, AEHR, SIVE, AIXA, IQE) + 2026-05-22 portfolio-wide manual alignment + 2026-05-24 1w retrospective synthesis
---

# Semiconductor Portfolio Rebalancing — 2026-05-24

## Thesis Delta

Portfolio is the **inverse of the barbell the mental models prescribe**. ~40–50% NAV concentrated in two memory positions ([[Theses/000660 - SK Hynix|SK Hynix]] Full 25%+, [[Theses/SNDK - SanDisk|SanDisk]] High 10–25%) — one a semi-cyclical compounder per L1 trading at peak cycle, one a textbook true cyclical up 3,866% in 12 months on guided 65–67% gross margins unprecedented in NAND history. Five highest-quality structural compounders ([[Theses/TSM - Taiwan Semiconductor|TSM]], [[Theses/NVDA - Nvidia|NVDA]], [[Theses/BESI - BE Semiconductor Industries|BESI]], [[Theses/KLA - KLA Corporation|KLAC]], [[Theses/AMAT - Applied Materials|AMAT]]) sit Medium-to-Low. Eight loss-making or single-digit-ROIC names are up 300–1,682% on momentum.

**Recommended rotation**: memory ~40–50% → ~12–15%; WFE basket ~10% → ~28–32%; structural compounders ~15% → ~33–37%; exit MRVL, trim aggressively (VICR/Murata/AIXA/IQE/Sivers/AAOI/AEHR collectively ~4–6% vs current ~14%). Position count compresses 20 → 19 with significant weight rotation. Aggregate semi NAV unchanged ~90%.

## Summary

Three independent vault signals confirm the portfolio is mis-sized for its cycle position:

1. **Mental model #7 cycle reading**: DRAM +171.8% YoY, NAND contract +55–60% QoQ Q1 2026, HBM 2026 sold out — late up-cycle / shortage phase. Mean-reversion pressure on true cyclicals (commodity NAND/DRAM) is the dominant near-term risk.
2. **Cohort 1Y returns**: median ~+250%, top quintile +900%+. The momentum extension that bid up loss-making names (AAOI +915%, AEHR +973%, LITE +1,149%, Sivers +1,682%, SNDK +3,866%) has decoupled their multiples from per-position quality. Mental model #18 (cycle confused with structural) is at maximum risk.
3. **2026-05-24 1w retrospective signal**: SK Hynix shows the largest narrative-price gap in the portfolio — stress test flagged 5🔴 / 5🟡 / 0🟢 ("low conviction with optionality") while the stock sits near ATH; NVDA shows the largest "unreactive-good" gap — Q1 FY27 monster beat ($82B vs $78B guide, GM recovery 74.9%, $80B buyback) drew flat reaction. The two largest gaps in the book sit at the two memory + GPU compounder pillars and both argue for the rotation: cut SK Hynix, add NVDA.

The compounder cohort in this book is **underweighted relative to its structural quality**. TSM (textbook #13 compounder; ROIC 32%, EV/EBIT NTM 22.5x) sits Medium. NVDA (CUDA + Omniverse OpenUSD moat, ROIC 60% — highest in book) sits Medium and has trailed peers materially (+64% 1Y vs cohort median +250%). KLAC (process control monopoly, ROIC 73% — highest in WFE, 17yr dividend, $7B buyback) sits Low. The WFE basket (LRCX/AMAT/KLAC/ASMI/BESI) is uniformly Low despite four of five having ROIC NTM ≥30% and the #12 structurally-rising-floor thesis validated by hyperscaler 2026 capex ~$750B per CreditSights.

The rebalancing rotates from "concentrated memory cyclicals at peak + dispersed momentum tail" to **"concentrated structural compounders + smaller memory cycle position + tight convex tail"**. Memory cyclical exposure compresses from ~40–50% to ~12–15%; structural compounders (TSM + NVDA + AVGO + KLAC + LRCX + AMAT + BESI + ASMI) rise from ~25% to ~52–63%; cyclical challengers (AMD, LITE, Murata, VICR) trim to a combined ~7–10%; convex tail (AEHR, AIXA, IQE, Sivers, AAOI) compresses to ~3–4%; MRVL exits as the lowest-conviction custom-silicon challenger with negative ROIC NTM and Trainium 3 execution credibility gap.

## Framework / Mental Model

This synthesis applies the [[Mental Models/Industry - Semiconductors]] evergreen framework, weighted toward these models per position cluster:

| Model | Application | Positions Most Affected |
|---|---|---|
| **#1 Bottleneck pricing power** | Identify which positions hold a binding bottleneck in the current cycle (HBM, CoWoS, hybrid bonding, advanced packaging, 200G EML, VPD, WLBI, MOCVD) | TSM (CoWoS, A16), SK Hynix (HBM3E/4), BESI (hybrid bonding), LITE (200G EML), KLAC (defect inspection at 2nm), AIXA (6-inch InP MOCVD), VICR (Rubin >2,000A VPD), AEHR (WLBI >600W TDP) |
| **#2 Qualification-gate monopolies** | Distinguish capacity scarcity (cycle-bound) from qualification-gate pricing power (structural) | KLAC (75–80% patterned wafer share), BESI (67% D2W hybrid bonding), NVDA (CUDA), TSM (leading-edge logic, no-second), LITE (butt-joint regrowth 4-decade IP), ASMI (HKMG gate-stack chemistries) |
| **#6 Peak margins don't symmetrically mean-revert in qualification-gated segments** | Applies to WFE primes and qualification-gated segments — NOT to commodity memory | AMAT/LRCX/KLAC/ASMI keep margins; SNDK/SK Hynix commodity DRAM do not |
| **#7 Cycle-phase signal from units × price** | Current readings confirm shortage / late up-cycle phase | All memory positions (SK Hynix, SNDK), secondary impact on WFE/foundry capex orders |
| **#10 Anchor customer concentration is binary** | Single-anchor positions face existential, not "concentration risk" exposure | LITE (NVDA NVLink ~75% Rubin demand), AMD (OpenAI 6GW + Meta 6GW 12GW combined), AEHR (~88% Q3 FY26 single AI customer), MRVL (AWS Trainium loss = thesis dent), VICR (Rubin Ultra single architecture bet) |
| **#11 Memory triopoly discipline is rented (4–7 years)** | Pricing power rotates between Samsung / SK Hynix / Micron when discipline breaks or 4th entrant scales (CXMT) | SK Hynix (L1 partially overrides for HBM but not for commodity DRAM) |
| **#12 WFE primes have structurally rising floors** | Each cycle trough is higher than the last; #13 categorizes WFE as semi-cyclical compounders not true cyclicals | AMAT, LRCX, KLAC, ASMI, BESI |
| **#13 Compounder vs semi-cyclical vs true cyclical classification** | The most expensive call in this sector. Misclassification is the highest-cost error | SNDK (true cyclical), TSM/NVDA/AVGO/KLAC (compounders), AMD/LITE/MRVL (semi-cyclical challengers), AIXA/AEHR/Sivers/IQE/AAOI (cyclical or pre-chasm) |
| **#14 Reclassification triggers flip the multiple** | SK Hynix HBM monopoly = reclassification up; Samsung HBM4 Vera Rubin win = potential reclassification down; HBF success = SNDK reclassification up; Aether dry resist TOR = LRCX category-share gain | SK Hynix (binary on Q3/Q4 2026 Rubin allocation), SNDK (HBF option), LRCX (Aether second TOR), BESI (HBM5+ 24-Hi mandate path 2029–2030) |
| **#17 New entrants don't materialize at tight prices** | Multi-billion fab capex + 5–7yr lead times mean supply lags 18–30 months at every node | Supports compounder thesis (TSM, ASMI, BESI, KLAC); refutes "loss-makers will saturate cheaply" — but also disciplines AAOI/AIXA/IQE upside expectations |
| **#18 Conflating cycle and structural shifts** | The dominant error mode at current cycle position; both directions of error possible | Memory positions (cycle being read as structural), loss-makers (cycle/momentum being read as fundamentals) |
| **L1 (live anchor) DRAM less cyclical via HBM contracts** | Argues SK Hynix mid-cycle multiple expands 7–10x → 15–25x; supports a core memory position but not 25%+ exposure | SK Hynix (sizing tempered by Samsung HBM4 qualification risk per existing kill trigger) |

Generalist principles from the preamble that drove the rebalancing:
- **Mean reversion vs trend continuation**: misapplying mean reversion to compounders (selling NVDA) or trend continuation to cyclicals (chasing SNDK at memory cycle peaks) is the single most expensive equity-research mistake. SNDK +3,866% YoY in a textbook true cyclical (#13) is the largest current example of trend continuation being applied where mean reversion is the correct frame.
- **S-curve location**: pre-chasm = binary outcome distribution (Sivers, IQE, AAOI); mid-chasm = highest-edge zone for long-term capital (BESI hybrid bonding, AIXA InP MOCVD, LITE EML 200G); late mainstream = mean-reversion regime (Murata mature MLCC). The portfolio overweights pre-chasm via loss-makers while underweighting mid-chasm structural-compounder bets.
- **Power-law portfolio**: 2–3 names typically drive >70% of returns. Current 20-position dispersion with multiple loss-makers fights this.
- **Barbell construction**: 80–90% in resilient compounders + 10–20% in downside-bounded convex bets. Current book is closer to 30/30/40 (compounder/cyclical/speculative) — inverted.
- **Long-horizon edge**: quant + L/S have wrung out <6-month alpha. Long-horizon thesis-driven holdings (compounders) are where alpha persists in this sector specifically because cycle shocks compress short-term alpha for cyclicals.

## Evidence

### Cycle Position — Late Up-Cycle / Shortage Phase

| Signal | Reading | Per Mental Model #7 |
|---|---|---|
| DRAM prices YoY (late 2025) | +171.8% | "units up + prices up" = SHORTAGE |
| NAND contract prices Q1 2026 | +55–60% QoQ | SHORTAGE |
| HBM 2026 capacity | Sold out | #1 bottleneck binding |
| Portfolio 1Y returns | Median ~+250%, top quintile +900%+ | Mean-reversion pressure rising |
| Sell-side language | "Allocation" returning; "supercycle extension" framing dominant | #18 structural-extrapolation peak |
| Cross-thesis NVDA Q1 FY27 reaction | $82B revenue beat $78B guide → AH +1.37% then flat (Q&A skeptical-keyword density = 0) | Sell-side capitulation marker — peak optimism in consensus |

Second-derivative signal (prices firming with units falling, marking cycle bottom per #7) has **not** turned — we remain in the up-leg. The gap between current cycle phase and the inevitable phase change is closing. Positioning for the turn while the up-leg still runs is the correct disposition for a long-horizon thesis-driven book.

### Per-Thesis Mental Model Assessment

Every position evaluated against #13 classification, primary moat per #1/#2, anchor-customer profile per #10, key reclassification triggers per #14, and any thesis-specific stress-test findings from existing vault research:

#### Tier 1 — Structural Compounders (Anchor Positions)

**[[Theses/TSM - Taiwan Semiconductor|TSM]] — Taiwan Semiconductor Manufacturing Company**
- **#13 Classification**: Structural compounder (textbook). 92% advanced-node share, ~58.8% Q1 2026 GM, N2 at +20% premium to N3. The "no-second" foundry per the L2/EUV-monopoly analog.
- **#1/#2 Moat**: CoWoS as $10B+ separable annuity (capacity 35K→130K wpm 2024-2027); A16 backside-power-rail exclusivity to NVDA Feynman (2027); COUPE silicon photonics (AMD risk production Feb 2026, +$5-8B by 2029 unmodeled in consensus). New: HBM4 base-die foundry win at 2 of 3 HBM IDMs (SK Hynix 3nm + Micron HBM4 12-Hi redesign) — +4-6% incremental wafer revenue at HBM4 peak, additive to GPU + CoWoS.
- **#10 Anchor risk**: AAPL+NVDA ~40% — unprecedented for $1T+ manufacturer, but multi-anchor across customer base and diversifying via AI/sovereign demand
- **L4 Taiwan tail**: real but quantified via $165B US co-investment (Arizona + Trump $100B March 2025 pledge); existing thesis Stress Test (2026-04-19) rated 8/9 bull assumptions 🔴 under invasion/destruction scenario — invasion permanently impairs -85-95%, not -30%
- **Quant**: P/E NTM data error (showing 0.8); EV/EBIT NTM 22.5x; ROIC NTM +32.3%; Rev Gr CFY +36.6%; EPS Gr CFY +49.7%; 1Y +110% (cohort mid-tier)
- **Action: UPSIZE Medium (~5%) → 12–14%** — highest-quality structural compounder still fairly priced on quality-comp basis; Taiwan tail is unhedged but priced

**[[Theses/NVDA - Nvidia|NVDA]] — Nvidia Corporation**
- **#13 Classification**: Structural compounder via CUDA software lock-in. Q1 FY2027 print (2026-05-22): $82B revenue (+85% YoY) beat $78B guide by $4B; GM recovery 71.1%→74.9%; sovereign +80% YoY across 40 countries / $50T GDP; Vera CPU "$200B brand-new TAM"; $80B buyback + dividend 20x to $0.20.
- **#1/#2 Moat**: CUDA general-purpose vs ASIC application-specific (AI architecture shifted 4x in 3 years; ASIC respin required each shift, CUDA inherits via preserved ABI Pascal 2016 → Rubin 2026); 6M CUDA developers (vs 1.8M in 2020); 400+ CUDA-X libraries; Omniverse + OpenUSD as $600B industrial software TAM call option (Core Spec 1.0 Dec 2025 Linux Foundation; GTC 2026 Cadence/Dassault/PTC/Siemens/Synopsys formal coalition)
- **#10 Anchor risk**: Customer dispersed across 5 hyperscalers + 40 sovereign programs
- **Stress test (2026-04-23)**: 6/10 bull assumptions 🔴 (share erosion to ~75% on Bear trajectory, Taiwan tail 3x consensus, China $50B structural loss, Jevons-vs-efficiency contested, valuation prices flawless execution); 4/10 🟡, 0 🟢. Mitigants since stress test: Q1 FY27 monster beat + Hopper/A100 useful life extending 7-8yr (Dylan Patel) + 1T-parameter dense models = research-bucket 3x pre-train compute (Luo Fuli) partially counter the Jevons-vs-efficiency assumption.
- **Quant**: P/E NTM 45.9x; EV/EBIT NTM 50.8x; ROIC NTM **+60.3%** (highest in book); Rev Gr CFY -1.1% (consensus conservative post-Q1 FY27 raise); EPS Gr CFY -4.8% (same); 1Y +64% (cohort LAGGARD)
- **Retro 2026-05-24 signal**: Largest "unreactive-good" gap in portfolio (×2.0 weighting) — Q1 monster beat drew flat reaction; sell-side capitulation has fully priced the beat into consensus
- **Action: UPSIZE Medium (~5%) → 12–14%** — highest-ROIC compounder + cohort laggard + execution validated; relative-strength bottom is the entry point

**[[Theses/AVGO - Broadcom|AVGO]] — Broadcom**
- **#13 Classification**: Structural compounder (dual semis + software). VMware acquisition (Nov 2023, $69B) delivered largest software M&A margin expansion ever recorded: pre-acquisition 13–22% operating margin → 78% in 24 months; FY25 software revenue $27B (+26% YoY); software gross margin 93%.
- **#1/#2 Moat**: 80–90% merchant Ethernet switching silicon (Tomahawk 6 at 102.4 Tbps shipping March 2026, 6 months ahead of NVDA Spectrum-X1600); 5 XPU customers in volume production (Google, Meta, ByteDance, OpenAI, Anthropic); Anthropic-Google deal locks AVGO as Google's primary silicon partner through 2031
- **#10 Anchor risk**: Multi-anchor — softer than LITE/AMD binary risk
- **Forward visibility**: Hock Tan guiding ">$100B" AI revenue 2027; CEO compensation tied to $60–120B by 2028-2030
- **Quant**: P/E NTM 36.8x; EV/EBIT NTM 51.7x; ROIC NTM +26.2%; Rev Gr CFY +61.8%; EPS Gr CFY +129.5%; 1Y +81%
- **Action: UPSIZE Medium (~5%) → 7–9%** — second-best structural compounder in book (after TSM/NVDA); VMware decouples ~35–40% revenue from semis cyclicality

#### Tier 2 — Semi-cyclical Compounders (WFE Basket — Structurally Rising Floor per #12)

**[[Theses/KLA - KLA Corporation|KLAC]] — KLA Corporation**
- **#13 Classification**: Structural compounder. Growth algorithm = WFE × process-control intensity × share = 12–17% CAGR floor vs 9–11% WFE consensus. Process-control intensity rising 100-200bp per node (10% @ 28nm → 16-17% @ 2nm) and never reverses.
- **#2 Qualification gate**: 56–63% PC share overall; 75–80% patterned wafer; 80%+ reticle inspection; defect-library substrate is 25 years of cross-customer data — non-replicable. Service annuity $4B → $6B by 2030 (capex-cycle-insensitive).
- **Quality signal**: ROIC 73% (highest in WFE); 17 consecutive years dividend increases; $7B buyback Mar 2026 (~2.7% of cap); 62.32% GM, 43.11% operating margin. At 30-36x forward P/E vs quality comps Visa/Moody's/Roper at 30-40x with 30-50% ROIC, KLAC looks structurally cheap.
- **Risks**: ASML eScan e-beam metrology bundling at High-NA EUV (~$0.5-0.7B SAM at risk); equipment-maker integration of inline metrology (AMAT PVI, LRCX Equipment Intelligence). Both compress ~5-8% of FY30 revenue, absorbed by 4-vector growth algorithm.
- **Quant**: P/E NTM 51.0x; EV/EBIT NTM 48.5x; ROIC NTM +40.6%; Rev Gr CFY +11.2%; EPS Gr CFY +21.3%; 1Y +149%
- **Action: UPSIZE Low (~2%) → 7–8%** — arguably the highest-quality WFE compounder

**[[Theses/LRCX - Lam Research|LRCX]] — Lam Research**
- **#13 Classification**: Semi-cyclical compounder transitioning to logic+memory diversified. Q3 FY26 mix 59% Foundry/Logic / 34% Memory — structural inversion from historical 55-65% Memory weight.
- **#1/#2 Moat**: Four independent content-per-wafer expansion vectors that compound: ~80% etch share at sub-3nm GAA (Akara), dry resist Aether as production TOR at SK Hynix HBM4 (taking share from TEL ~90% liquid-track monopoly), Cryo 3.0 + ALTUS Halo Mo for 400-1000 layer NAND, +40% advanced packaging guide for CY26 (TSV etch Vantex 60% share + SABRE 3D copper plating 6,000+ cells)
- **Quant**: P/E NTM 53.8x; EV/EBIT NTM 52.8x; ROIC NTM **+50.6%** (highest in WFE); Rev Gr CFY +25.7%; EPS Gr CFY +36.2%; 1Y +276%
- **2028 Investor Day target**: $25-27B / 50% GM / 34-35% OM / $6-7 EPS — implies structural margin expansion, not cyclical mean reversion
- **Risk**: Aether stalls at one customer (SK Hynix); NAND restart slips; China revenue cliff at <30% guide
- **Action: UPSIZE Low (~2%) → 5–6%** — high-quality WFE compounder with Aether being a non-consensus structural-category-gain catalyst

**[[Theses/AMAT - Applied Materials|AMAT]] — Applied Materials**
- **#13 Classification**: Semi-cyclical compounder (#12 rising floor). Broadest WFE company touching 9 of 14 major wafer fab process steps.
- **#1 Moat**: PVD 85%, CMP 65%, implant 70%+, epitaxy #1 (vs ASMI #2). Four simultaneous architectural inflections: GAA + BSPDN + HBM/AP + ICAPS recovery. AGS service annuity ~$6.4B + 5%+ growth on 55K+ installed base.
- **Strategic optionality**: 9% BESI stake + Kinex co-development at Singapore COE (~$1B cost basis); EPIC Center customer-lock-in flywheel opening Spring 2026 ($4-5B Silicon Valley R&D campus with embedded TSMC/Intel/Samsung/Micron teams)
- **Risks**: ASML overtook AMAT as #1 WFE vendor 2024; ASMI structural ALD lead at 2nm could compress GAA category multiplier; AMEC/NAURA China substitution erodes ICAPS
- **Quant**: P/E NTM 35.5x (CHEAPEST WFE); EV/EBIT NTM 27.8x; ROIC NTM **+44.0%** (DOUBLED from 21.6 LTM — strong NTM signal); Rev Gr CFY +17.3%; EPS Gr CFY +39.8%; 1Y +174% (relative WFE laggard)
- **Action: UPSIZE Low (~2%) → 6–7%** — cheapest WFE prime with strongest ROIC NTM expansion; ROIC near-doubling is the empirical signal that the four-inflection thesis is materializing

**[[Theses/ASMI - ASM International|ASMI]] — ASM International**
- **#13 Classification**: Structural compounder (POR annuity reframe). Each node win locks ASMI into 5-7 years of consumables-like equipment revenue.
- **#2 Qualification gate**: ~55% single-wafer ALD share globally; HKMG gate-stack chemistries (HfO2, TiN, TiAl, La, capping layers) — chemistries Lam ALTUS Halo and AMAT Trillium have not productized at HVM scale. Each tool requires 12-24 months of customer qualification.
- **Two compounding engines**: ALD (today, $400M SAM expansion per node at 2nm doubling to $400M from $200M at 7nm) + Epi (CFET architecture post-GAA ~2030+ doubles epi intensity)
- **Hidden value**: ~25% ASMPT stake worth $1.0-1.2B off-balance-sheet; activist pressure for resolution; Axus CMP acquisition (Dec 2024) adds bundling optionality
- **Risks**: Lam ALTUS Halo Mo and AMAT Trillium attack adjacencies (Mo NAND wordlines, batch ALD spacers) — not core HKMG stack
- **Quant**: P/E NTM 41.2x; EV/EBIT NTM 32.8x (cheapest WFE compounder); ROIC NTM +29.7%; Rev Gr CFY +24.5% (HIGHEST WFE); EPS Gr CFY +47.9% (HIGHEST WFE); 1Y +92% (cohort LAGGARD)
- **Action: UPSIZE Low (~2%) → 4–5%** — high-quality structural compounder + relative-value laggard

**[[Theses/BESI - BE Semiconductor Industries|BESI]] — BE Semiconductor Industries**
- **#13 Classification**: Structural compounder (3D integration monopoly). 67% D2W hybrid bonding share, 150+ installed systems across 18 customers.
- **#1/#2 Moat**: Switching costs are front-end-grade (ISO 3 cleanrooms, sub-0.5nm surface roughness, queue times in minutes via Kinex). Competitors 2-3 years behind in production qualification. AMAT 9% stake + Kinex co-development = strategic infrastructure validation. Lam Research + AMAT takeover interest disclosed March 2026.
- **#14 Reclassification timing**: JEDEC HBM4 720→775→900µm relaxation pushed HBM-mandated hybrid bonding from HBM4 to HBM5+ 24-Hi (2029-2030) — delays HBM-driven inflection ~2 years. Logic-line bridge intact: TSMC SoIC + Intel Foveros Direct (Meteor Lake first high-volume hybrid-bonded client product) + SK Hynix Mar 2026 Kinex order for 2nm logic (dual-use HBM5).
- **Quant**: P/E NTM 68.9x (most expensive WFE); EV/EBIT NTM 64.4x; ROIC NTM +30.4%; Rev Gr CFY +57.4%; EPS Gr CFY +139.3%; 1Y +159%
- **Action: UPSIZE Low (~2%) → 4–5%** — hybrid bonding monopoly intact but 2026-2028 revenue ramp velocity revised down post JEDEC; HBM5+ 24-Hi architectural mandate path still locked

#### Tier 3 — Semi-cyclical Memory (Cycle-Trade)

**[[Theses/000660 - SK Hynix|SK Hynix]] — SK Hynix**
- **#13 Classification**: Semi-cyclical compounder per L1 (HBM contracted markets + winner-take-most). 57% HBM share, Q1 2026 op margin 72% (record in memory history), $37.9B Q1 revenue, $30B 2026 HBM revenue book.
- **#1 Moat**: HBM3E + HBM4 — but eroding. Samsung HBM4 passed Vera Rubin qualification with "best scores"; Vera Rubin initial allocation confirmed ~70/30/0 SK Hynix/Samsung/Micron (per [[Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive]]). Gemini Incumbent Erosion path: 62% → 57% → 52% → 48% → 45% (2024 → 2030).
- **#14 Kill trigger**: Samsung HBM4 captures >35% of Rubin allocation in first two shipping quarters (Q3-Q4 2026) — directly invalidates 57% share base. The single highest-information binary event in the book.
- **Stress test (2026-05-22)**: 5/10 assumptions 🔴 — materials moat (Namics EMC) in active renegotiation, HBM share already eroded 62→57% in 12mo; verdict "low conviction with optionality"
- **Hidden options**: HBF (High-Bandwidth Flash) co-invented with SanDisk — $5-10B TAM by 2030 unpriced; Solidigm 51% QLC share at $15-20B standalone vs paid $9B 2021 — potential 2027 IPO crystallizes $6-15B hidden value
- **Quant**: P/E NTM 6.9x (looks cheap on PEAK earnings); EV/EBIT NTM 21.6x; ROIC NTM +29.5%; Rev Gr CFY +232.6%; EPS Gr CFY +353.2%; 1Y **+870%**
- **Retro 2026-05-24 signal**: Largest narrative-price gap in book (×1.5 weighting on inverted-bear) — vault weakened (stress test) while price near ATH; kill trigger OR-gated on Samsung Rubin allocation in Q3 OR Q4 2026 earnings
- **Action: CUT Full 25%+ → 10–12%** — L1 thesis intact but sizing reflects cycle position + binary HBM4 allocation risk + materials-moat uncertainty; L1 will play out without 25%+ exposure to a binary outcome

**[[Theses/SNDK - SanDisk|SanDisk]] — SanDisk Corporation**
- **#13 Classification**: TRUE CYCLICAL with HBF call option. The textbook current example of misapplying trend continuation to a cyclical.
- **#18 Cycle-vs-structural confusion**: Q2 FY26 51.1% GM guided to 65-67% — unprecedented in NAND history; pre-acquisition peak was 42-43%. Mid-cycle GM on normalized NAND is 30-40%, mid-cycle P/E 8-12x.
- **#14 Reclassification option**: HBF (High-Bandwidth Flash) with SK Hynix + OCP standardization — pre-revenue option valued at $12B TAM by 2030; samples H2 2026, commercial 2027 aligned with NVIDIA Rubin.
- **#10 Anchor concentration**: 89% datacenter revenue from top 7 cloud providers; asymmetric negotiating leverage
- **Quant**: P/E NTM 22.9x (looks reasonable on PEAK margins); EV/EBIT NTM -163 (anomalous — data noise from cycle reversal); ROIC NTM -9.0% (turning negative as cycle peak compresses); Rev Gr CFY +166.8%; EPS Gr CFY **-671%**; 1Y **+3,866%** (single largest 1Y return in portfolio)
- **Action: CUT High (10-25%) → 2–3%** — single largest mispricing in book per #13/#18; cycle-trade discipline applies. Keep small HBF option exposure only. Use April 30 Q3 FY26 earnings ($4.4-4.8B / 65-67% GM guide) as sell window — that is the cycle high-water mark.

#### Tier 4 — Cyclical Challengers (Trim to Smaller Positions)

**[[Theses/AMD - Advanced Micro Devices|AMD]] — Advanced Micro Devices**
- **#13 Classification**: Semi-cyclical challenger (#2 in GPU duopoly). Sole merchant full-stack NVDA alternative — CPU (EPYC Venice 2nm) + GPU (MI400 series Helios rack Q3 2026 with 72 MI455X / 31TB HBM4 / 3 AI exaflops) + DPU (Pensando Pollara 400 UEC-ready) + FPGA (Xilinx).
- **#2 Moat (weak)**: NO CUDA equivalent. ROCm narrowing via framework-native PyTorch/vLLM/SGLang/Triton adoption but training parity remains open question. AMD's #2 position is structural via hyperscaler-imposed diversification, not technical merit.
- **Hyperscaler commitments**: OpenAI 6GW + Meta 6GW signed inside 5 months — 12GW total. OpenAI 10% warrant dilution (160M shares at $0.01 across deployment milestones through 2030).
- **Agentic-AI CPU positioning**: Venice Dense 5/5 action score per Vik Sekar Apr 2026 framework; 2.7x thread density vs Intel Diamond Rapids (post-SMT removal, 192c/192t vs Venice 256c/512t); Intel stranded until Coral Rapids ~2028+ (SMT restoration).
- **Risks**: NVDA Rubin GR200 ships H2 2026 with 10x lower inference cost vs Blackwell — Helios competes against Rubin, not against Blackwell; CoWoS allocation 11% vs NVDA 60-65% caps AI revenue ceiling; ROCm training parity unproven.
- **Quant**: P/E NTM 62.8x (most expensive multiple in book); EV/EBIT NTM **149.7x**; ROIC NTM +8.1% (LOW for the multiple); Rev Gr CFY +44.0%; EPS Gr CFY +178.8%; 1Y +323%
- **Retro 2026-05-24 signal**: Cleanest aligned-up confirmation in portfolio ($417→$462 in week, +10%) — Meta $60B AI infra deal + OpenAI 6GW + MI400/Helios merchant-GPU validation; "gap magnitude high with vault and price both pointing same direction"
- **Action: TRIM Medium (~5%) → 3–4%** — softer cut than first pass because structural second-source thesis is real and aligned-up signal confirms execution; but ROIC 8% on 62x P/E is uncomfortable, anchor concentration on OpenAI/Meta deals is binary

**[[Theses/LITE - Lumentum|LITE]] — Lumentum Holdings**
- **#13 Classification**: Semi-cyclical compounder (per #14 reclassified up via NVDA NVLink optics qual + arms-dealer pricing position)
- **#1/#2 Moat**: Sole volume supplier of 200G EML lasers (50-60% market share); butt-joint regrowth physics-gated 7-10 years for new entrant. Failure rates scale with **4th power of bandwidth** — 200G is 16x harder than 100G in yield terms.
- **Arms dealer position**: Wins regardless of which transceiver maker captures downstream share. Chinese transceiver giants (Innolight, Eoptolink — 70%+ module share) are structurally dependent on Lumentum's components.
- **#10 Anchor concentration**: NVDA $2B strategic investment with capacity lock-out (March 2026); NVDA explicit dual-supplier with Coherent. NVDA-LITE concentration is binary if Coherent qualifies at parity.
- **SiPh paradox**: Every silicon photonic transceiver requires external InP laser sources. CW laser TAM $22B by 2030 — captured even under CPO transition (lower-ASP CW vs higher-ASP EML).
- **Optical Circuit Switches**: $400M+ backlog, $100M/quarter target by end-2026, $2.5B 2029 TAM — data-rate-agnostic, structurally durable.
- **Quant**: P/E NTM 115.1x (most expensive); EV/EBIT NTM -3,618 (data noise from capacity expansion); ROIC NTM -0.7% (negative due to 8x capacity expansion); Rev Gr CFY +81.7%; EPS Gr CFY +2064.5%; 1Y **+1,149%** (second-highest in book)
- **Action: TRIM Medium (~5%) → 2–3%** — structural monopoly is real but 1,149% YoY + 115x P/E + negative ROIC NTM = pricing perfection; smaller cut than MRVL because moat is genuine, but reduce to manage anchor-binary + valuation risk

**[[Theses/6981 - Murata Manufacturing|Murata Manufacturing]]**
- **#13 Classification**: Semi-cyclical compounder (mature). Specialist whose share rises monotonically with technical difficulty across case size, application, and reliability tier.
- **#2 Moat**: 50% share at 008004 case size (vs 15% at 1206/0805 commodity); 50% EV-grade AEC-Q200 share; ~60% premium iPhone sockets. Four measurable edges: yield (>95% vs 70-85% Chinese), DPM (<0.1 vs 1-10), AEC-Q200 platform installed base (hundreds vs dozens), dielectric chemistry IP (40-year iteration). Chinese share gains entirely from commodity case sizes — the parts becoming a shrinking demand share.
- **AI server content scaling**: 440K MLCCs per GB200 NVL72 rack vs 1,300 per iPhone = 1 AI rack = 340 smartphones of content. 800VDC AI rack transition: 008004 count rises 2-3x.
- **EV exposure**: 50% global share of EV-grade MLCCs, 3-5x ICE content. Chinese EV premiumization is unpriced tailwind.
- **Risks**: Yageo/Walsin/Sunlord closing chemistry gap (7-10yr horizon); JPY appreciation risk to reported margins
- **Quant**: P/E NTM 59.5x; EV/EBIT NTM 37.3x; ROIC NTM +9.1% (LOW for multiple); Rev Gr CFY -1.2%; EPS Gr CFY -6.2% (negative on segment mix); 1Y +247%
- **Action: TRIM Low (~2%) → 1–2%** — structural-volume thesis is real but ROIC 9% + negative growth makes the rich multiple uncomfortable; modest position holds AI-server MLCC + EV premiumization optionality

**[[Theses/VICR - Vicor Corporation|Vicor Corporation]]**
- **#13 Classification**: Niche specialist with architectural moat. Sole US-domiciled, US-manufactured, founder-controlled high-density power module supplier.
- **#1 Architectural necessity**: NVDA Rubin >2,000A per processor — current density past threshold where lateral power delivery (MPS H100 product) physically works. Compal NVL8 demo on Vicor VPD at NVDA GTC March 2026.
- **#2 Six reinforcing moats**: ITC LEO converting share losses to ~90% GM royalties (Delta/Cyntec/Foxconn settled $45M in 2025, $300M pipeline through 2026); SAC+FPA topology IP (decades of refinement); ChiP+3Di fabrication (panel-level, no IDM analog); 2nd-gen VPD spec gap (3 A/mm² / 40× multiplication / 1.5mm); 5-7yr reverse-engineering clock; NVDA V100/A100 qualification history + Andover US manufacturing
- **Risks**: Founder Vinciarelli 78 with >25% stake — succession risk; FY26 guide "contingent on licensing agreements awaiting resolution in 2027"; MPS or Flex clean-sheet vertical product within 18-24 months
- **Quant**: P/E NTM 96.7x; EV/EBIT NTM 158.1x (extremely expensive); ROIC NTM +10.4%; Rev Gr CFY +39.8%; EPS Gr CFY +5.4% (low EPS leverage); 1Y **+543%**
- **Action: TRIM Low (~2%) → 1%** — architectural-necessity thesis at Rubin Ultra is real and ITC LEO licensing creates option-value asymmetry, but +543% YoY + 96x P/E + founder succession overhang requires smaller position; keep as convex bet on Rubin Ultra socket content disclosure

#### Tier 5 — Convex Bets (Small Positions Only)

**[[Theses/AEHR - Aehr Test Systems|AEHR]] — Aehr Test Systems**
- **#13 Classification**: Cyclical equipment / pre-chasm AI WLBI option
- **#1 Bottleneck**: Wafer-level burn-in (WLBI) structurally non-substitutable for AI accelerators >600W TDP. NVDA H100 700W; Blackwell B200 ~1000W; Rubin/Rubin Ultra 1200W+. Advantest/Teradyne (~80% ATE share combined) don't have WLBI — handler-based functional test cannot deliver simultaneous high-power, long-duration multi-DUT thermal stress. 4-7 year qualification gap.
- **Q3 FY26 inflection**: Revenue $10.3M (-43.7% YoY on SiC drain) but bookings $37.2M (5x QoQ, book-to-bill >3.5x), backlog $50.9M record. AI processors >35% of mix (was ~0% 2 years ago). Lead AI customer $14M Feb 2026 follow-on order = second order = platform validation.
- **Asymmetric kicker**: Silicon photonics WLBI design-in March 2026 ("global networking leader" — Marvell/AVGO/Cisco candidates). First hyperscale CPO/SiPh customer for wafer-level optical-electrical test. $20-40M incremental TAM by FY28 from this single customer.
- **Risk**: ~88% Q3 FY26 from one customer; identity (NVDA vs hyperscaler captive) determines volume scaling
- **Quant**: P/E NTM -709 (loss-making); EV/EBIT NTM 746; ROIC NTM +2.5% (TURNING positive); Rev Gr CFY -15.4%; EPS Gr CFY +3.1%; 1Y +973%
- **Action: HOLD Low (~2%) → 1–2%** — genuine convex bet with platform validation in motion; second AI customer disclosure is binary catalyst

**[[Theses/AIXA - Aixtron|Aixtron]]**
- **#13 Classification**: Structural compounder per Kerrisdale "ASML of compound semi deposition" framing. 90%+ share in 6-inch InP MOCVD (G10-AsP); 90%+ share in GaN power MOCVD.
- **#1 Mix shift**: Optoelectronics from 12% (2024) → 23% (2025) → 65% Q1 2026 order share — structural transition compressed into 4 quarters. FY26 €560M revenue guide.
- **Two demand legs**: InP photonics (LITE Greensboro 6-inch mid-2028, COHR four 6-inch lines ~2027, Nokia G10-AsP, SMART Photonics) + 800V data center power (NVDA Rubin 2027+, OCP Mt. Diablo Meta/Google parallel)
- **Implicit long LITE/COHR/NVDA at semis-cycle multiples**: AIXA at ~32x forward P/E vs LITE 48-60x and NVDA Omniverse-premium multiples; equipment supplier captures first-dollar capacity capex 18-24 months ahead of customer revenue
- **Kerrisdale Nov 2025 target**: €55/share at +296% upside (from €13.88); avg of two methodologies (33.5x small-cap median P/E × €1.90 2028E EPS + DCF at 11.1% WACC). Current ~€53.68 = roughly halfway to Kerrisdale target.
- **Risks**: Veeco 6-inch InP MOCVD ship by 2H 2027 (compresses monopoly window); NVDA 800V slips; Q1 2026 -38% EBIT operating deleverage continuing
- **Quant**: P/E NTM 75.1x; EV/EBIT NTM 48.0x; ROIC NTM +11.1%; Rev Gr CFY +2.2%; EPS Gr CFY -6.0% (operating leverage compressed at light Q1 revenue); 1Y +337%
- **Action: REVISED — HOLD Low (~2%) → 1–2%** — picks-and-shovels play on InP photonics buildout; structural mix shift is real but 1Y +337% has captured material upside; convex-bet sizing

**[[Theses/IQE - IQE|IQE]]**
- **#13 Classification**: Convex M&A special situation. UK Takeover Code formal offer period active since September 2025 (Lazard advising).
- **Stock dynamics**: 4.7p (Nov 2025) → ~52.5p (April 2026) = >1,000% rally. EV/Revenue 2.3x → 6.1x — at peer parity (Win Semi 6.7x, Coherent 6.9x). Stock exceeds analyst consensus ~40p.
- **Strategic position**: Only scaled independent Western multi-material III-V epitaxy supplier (UK + US + Taiwan). Taiwan operations being marketed for sale.
- **#10 Customer concentration**: Apple/Lumentum VCSEL supply chain is revenue anchor; Coherent's growing VCSEL capability is structural competitive threat (Apple awarded Coherent Face ID VCSEL contract).
- **Scale disadvantage**: Win Semi at 50%+ GaAs foundry share with 33% EBITDA margins vs IQE 2% margins — structural gap; standalone profitability unproven.
- **Quant**: P/E NTM -4,004 (loss-making); EV/EBIT NTM -19.9; ROIC NTM -15.0%; Rev Gr CFY +0.5%; EPS Gr CFY -71.1%; 1Y +318%
- **Action: TRIM Low (~2%) → 1%** — M&A optionality is real but post-rally the discount that justified the position has evaporated; convex-bet size only

**Applied Optoelectronics (AAOI)**
- No thesis in vault (confirmed via Glob 2026-05-24)
- Optical transceiver competitor to LITE; participates in 1.6T transition
- **Quant**: P/E NTM 175.7x; EV/EBIT NTM -44.9; ROIC NTM **-22.1%** (loss-making); Rev Gr CFY +128.3% (surging); EPS Gr CFY **-261%** (losing money); 1Y **+915%**
- **Action: TRIM Low (~2%) → 0.5–1%** — loss-making at peak revenue growth is textbook #17/#18 trap; without thesis support, convex-bet size only

**[[Theses/SIVE - Sivers Semiconductors|Sivers Semiconductors]]**
- **#13 Classification**: Pre-chasm option (conviction explicitly low in source thesis).
- Only listed pure-play on External Light Source (ELS) layer of CPO. 4-inch InP fab in Glasgow (vs LITE Greensboro 6-inch mid-2028, Coherent four 6-inch ~2027).
- Partnerships: POET / O-Net + Enablence / Jabil 1.6T LRO / Imec + ASM AMICRA / Ayar Labs / Aeva / Celestial AI (via POET) / ALL.SPACE — all pre-revenue at scale
- **Binary risks**: SEK 186.5M FY25 net loss against SEK 43.5M YE25 cash repaired by SEK 125M directed share issue + 10.85% coupon convertible; Voleon Capital 0.53%+ short on dilution math; Swedish Economic Crime Authority preliminary investigation into Nasdaq listing announcement leak; PCAOB restatement revealed deeper-than-disclosed losses
- **Quant**: P/E NTM -214.4 (loss-making); EV/EBIT NTM -78.8; ROIC NTM -18.2%; Rev Gr CFY +18.3%; EPS Gr CFY -50.7%; 1Y **+1,682%**
- **Action: TRIM Low (~2%) → 0.5%** — pure speculation on partnership conversion + Nasdaq listing catalyst; keep tiny convex bet

#### Tier 6 — Exit

**[[Theses/MRVL - Marvell Technology|MRVL]] — Marvell Technology**
- **#13 Classification**: Semi-cyclical challenger. Second-source structural position to AVGO in custom silicon (~13-15% share vs AVGO ~55-60%).
- **Negative signals**: Trainium 3 socket loss to Alchip on advanced-packaging execution gap is management-competence red flag — central thesis pillar dented. Google "talks" not signed (Broadcom locked Google TPU through-2031 three days before April 2026 Marvell-Google talks leaked). NVLink Fusion $2B Nvidia investment is containment, not pure partnership.
- **Real assets**: Celestial AI $3.25B Photonic Fabric (memory disaggregation, 16 Tbps Gen 1 / 64 Tbps Gen 2) — binary on 2027-2028 architectural validation; 80% long-reach DSP share (Inphi heritage) but LPO transition compressing DSP margins
- **AVGO comparison**: AVGO has 5 XPU customers with multi-year committed roadmaps, secured supply through 2028; MRVL has 18 cloud design wins but Trainium 3 loss signals execution credibility gap
- **Quant**: P/E NTM 69.0x; EV/EBIT NTM **-1,151** (negative); ROIC NTM **-0.8%** (negative); Rev Gr CFY -0.1% (declining); EPS Gr CFY -8.2%; 1Y +223%
- **Action: EXIT Low (~2%) → 0%** — AVGO provides higher-quality custom-silicon exposure with much better positioning; cleaner concentration

### Quality vs Cheapness Matrix — Updated for Per-Thesis Depth

Positioned by structural quality (vertical: per #13 + per-position moat depth) vs through-cycle valuation (horizontal):

| | Cheap vs through-cycle | Fair | Expensive vs through-cycle |
|---|---|---|---|
| **Anchor compounders (ROIC >25% + structural moat)** | — | **TSM**, **NVDA**, **AVGO**, **SK Hynix***, **ASMI** | **BESI**, **KLAC**, **LRCX** |
| **Semi-cyclical compounders (ROIC 10–25% + #12 rising floor)** | — | **AMAT** | **Murata** (mature) |
| **Semi-cyclical challengers (no structural moat or anchor-binary)** | — | — | **AMD**, **LITE**, **VICR** |
| **True cyclical / loss-makers / pre-chasm** | — | **AEHR** (convex turn), **AIXA** (mid-chasm) | **SNDK**, **MRVL**, **AAOI**, **Sivers**, **IQE** |

*SK Hynix appears cheap on LTM (6.9x); normalizes to "fair" on mid-cycle earnings under L1 framing — but cycle-trade discipline argues for cut regardless.

**No position is cheap on through-cycle valuation.** The book sits entirely in the fair-to-expensive corner. The expensive corner is materially overweighted; the compounder corner is underweighted relative to quality. The expensive bottom-right corner (true cyclical / loss-makers trading rich) is where the largest mispricings sit.

### Proposed Reweighting — Final

Weights are % of total semi NAV. Aggregate semi exposure unchanged ~90%.

| Ticker | Current | Proposed | Action | Rationale (Mental Model + Per-Thesis) |
|---|---|---|---|---|
| **TSM** | Medium (~5%) | **12–14%** | **UPSIZE** | #13 textbook compounder; A16/CoWoS/COUPE three lines + HBM4 base-die win adds 4-6% incremental wafer revenue |
| **NVDA** | Medium (~5%) | **12–14%** | **UPSIZE** | Highest-ROIC compounder; CUDA + Omniverse $600B option; Q1 FY27 monster beat + cohort laggard |
| **SK Hynix** | Full (25%+) | **10–12%** | **CUT 50–60%** | Semi-cyclical compounder per L1 but binary kill trigger on Q3/Q4 2026 Samsung Rubin allocation + stress test 5🔴 |
| **AVGO** | Medium (~5%) | **7–9%** | **UPSIZE** | 5 XPU customers + Anthropic-Google through 2031 + VMware (largest software M&A margin expansion ever) |
| **KLAC** | Low (~2%) | **7–8%** | **UPSIZE 3-4x** | Highest-quality WFE compounder; 73% ROIC + 17yr dividend + $7B buyback + service annuity $4B→$6B |
| **AMAT** | Low (~2%) | **6–7%** | **UPSIZE 3x** | Cheapest WFE prime; ROIC NTM doubled 21.6→44.0%; 4 architectural inflections + EPIC Center |
| **LRCX** | Low (~2%) | **5–6%** | **UPSIZE 2.5-3x** | Highest ROIC in WFE (50.6%); Aether dry resist taking TEL share; mix shift to logic+memory diversified |
| **BESI** | Low (~2%) | **4–5%** | **UPSIZE 2x** | Hybrid bonding monopoly intact; logic-line bridge + HBM5+ 24-Hi mandate; JEDEC relaxation delays HBM ramp 2yr |
| **ASMI** | Low (~2%) | **4–5%** | **UPSIZE 2x** | POR annuity reframe; relative-value laggard +92% 1Y vs WFE cohort; ALD + Epi two compounding engines |
| **AMD** | Medium (~5%) | **3–4%** | **TRIM 30-40%** | Sole merchant full-stack alternative; Helios + Venice Dense agentic CPU; but ROIC 8% on 62x P/E uncomfortable |
| **SNDK** | High (10-25%) | **2–3%** | **CUT 80–90%** | True cyclical at peak; 65-67% GM unprecedented in NAND history; HBF option only |
| **LITE** | Medium (~5%) | **2–3%** | **TRIM 50%** | Physics-gated monopoly real; arms-dealer position; but +1,149% YoY + 115x P/E + negative ROIC NTM |
| **AEHR** | Low (~2%) | **1–2%** | **HOLD** | Convex bet; WLBI non-substitutable >600W TDP; second AI customer disclosure binary catalyst |
| **AIXA** | Low (~2%) | **1–2%** | **HOLD** | ASML of compound semi deposition; Q1 2026 65% optoelectronics order share; Kerrisdale €55 target |
| **Murata** | Low (~2%) | **1–2%** | **TRIM** | 800VDC AI-rack MLCC scaling 2-3x; 50% EV MLCC share; but ROIC 9% rich vs multiple |
| **VICR** | Low (~2%) | **1%** | **TRIM** | Rubin >2,000A architectural necessity + ITC LEO 90% GM royalties; but founder/valuation/+543% YoY |
| **IQE** | Low (~2%) | **1%** | **TRIM** | M&A optionality; >1,000% rally has captured the discount; convex-bet size only |
| **AAOI** | Low (~2%) | **0.5–1%** | **TRIM 70%** | No thesis support; -22% ROIC NTM + +915% YoY = textbook #17/#18 trap |
| **Sivers** | Low (~2%) | **0.5%** | **TRIM 75%** | Pre-chasm + binary Nasdaq listing + Economic Crime probe; +1,682% YoY pure speculation |
| **MRVL** | Low (~2%) | **0%** | **EXIT** | Negative ROIC NTM; Trainium 3 loss execution credibility gap; AVGO is higher-quality exposure |

### Aggregate Composition Shift

| Tier | Current Weight | Proposed | Direction |
|---|---|---|---|
| Memory (SK Hynix + SNDK) | ~40–50% | ~12–15% | **CUT MASSIVELY** |
| Structural compounders (TSM + NVDA + AVGO + KLAC + ASMI) | ~14–17% | **42–50%** | **UPSIZE 3x** |
| Semi-cyclical compounders WFE (LRCX + AMAT + BESI) | ~6% | **15–18%** | **UPSIZE 2.5-3x** |
| Cyclical challengers (AMD + LITE + Murata + VICR) | ~14% | ~7–10% | **TRIM 40-50%** |
| Convex bets (AEHR + AIXA + IQE + Sivers + AAOI) | ~10% | ~4–6% | **TRIM 50%+** |
| Exits (MRVL) | ~2% | 0% | **EXIT** |
| Position count | 20 | 19 | **Concentrate** |
| Compounder share of book (structural + semi-cyclical WFE) | ~20–23% | **57–68%** | **3x rotation** |

### Execution Priorities

1. **Sell SanDisk into cycle peak first.** Single largest mispricing per #13/#18. True cyclical up 3,866% on 22.9x peak-margin earnings. Use the April 30 2026 Q3 FY26 earnings print (guide $4.4–4.8B / 65–67% GM) as the sell window — that is the cycle high-water mark.
2. **Trim SK Hynix in two tranches.** Halve the position now to ~13%; further trim to 10-12% if Samsung captures >35% Vera Rubin HBM4 allocation in either Q3 or Q4 2026 earnings (the existing thesis kill trigger). L1 thesis intact at smaller exposure.
3. **Upsize TSM and NVDA aggressively.** Both are structural compounders (#13). TSM at EV/EBIT NTM 22.5x with 32% ROIC is the cheapest structural compounder. NVDA at +64% YoY is the cohort laggard with 60% ROIC; the relative-strength bottom + Q1 FY27 monster beat + retro 1w "unreactive-good" largest gap is the entry point.
4. **Upsize the WFE basket and rebalance within it.** AMAT and ASMI are the relative-value laggards (+174% and +92% 1Y vs WFE cohort +200%+). LRCX and KLAC are the highest-quality. Target 22–26% NAV across LRCX 5–6, AMAT 6–7, KLAC 7–8, ASMI 4–5, plus BESI 4–5.
5. **Upsize AVGO meaningfully.** VMware integration is empirically the largest software M&A margin expansion ever recorded. 5 XPU customers + Anthropic-Google through 2031. AI revenue $8.4B Q1 FY26 (+106%) tracking to $100B+ 2027.
6. **Exit MRVL entirely.** Negative ROIC NTM + Trainium 3 execution credibility gap. Reallocate to AVGO (higher-quality custom-silicon exposure) or KLAC/AMAT.
7. **Trim convex bets to tail allocation.** AEHR/AIXA/IQE/Sivers/AAOI combined to ≤4% of NAV (vs current ~10%). The barbell construction principle caps convex bets at 10–20%, and at current prices these have moved from convex zone into momentum territory.
8. **Reduce LITE meaningfully but retain core.** Lumentum's 200G EML butt-joint-regrowth moat is real (4th-power-of-bandwidth failure rate scaling is physics-gated). But 1,149% YoY + 115x P/E + NVDA-anchor binary at $2B capacity lock-out demands 50% cut.
9. **Trim AMD softer than first pass.** Sole merchant full-stack NVDA alternative with Helios rack-scale execution + Venice Dense agentic CPU + cleanest retro "aligned-up" signal. But ROIC 8% on 62x P/E + 10% OpenAI warrant dilution caps upsize. Target 3–4%.

### Trigger Watchlist

| Trigger | Signal | Impact on Rebalancing |
|---|---|---|
| Samsung Q3 2026 Vera Rubin HBM4 allocation | >35% Samsung share | Further cut SK Hynix; close cycle thesis |
| NAND contract pricing Q3/Q4 2026 | First QoQ decline | Sell remaining SNDK; cycle has turned per #7 |
| NVDA Feynman architecture reveal (GTC Oct 2026) | A16 exclusivity + COUPE photonics confirmed | Reinforces TSM + NVDA upsize |
| Intel 18A external customer wins (Q3/Q4 2026) | MSFT/AMD/MediaTek commits 2+ wins | Trim TSM modestly (Mental Model #14 reclassification risk) |
| HBF OCP standardization (Q3 2026) + first hyperscaler qual | Meta/Microsoft hyperscaler qualifies HBF | SNDK reclassification trigger; option crystallizes (only at this trigger do we re-add) |
| LRCX Aether second TOR customer (TSMC/Micron) | Confirmed by Q1 CY27 | LRCX reclassification up — consider additional upsize |
| BESI Kinex HBM5+ hybrid-bonding yield (H2 2026) | >70% at 16-Hi | Confirms BESI HBM5 path; modest BESI upsize |
| NVDA Rubin Ultra reference design (H2 2026) | Vicor VPD confirmed primary supplier | VICR reclassification — consider retain at 1-2% |
| AEHR Q4 FY26 earnings (Jun-Jul 2026) | Second AI customer disclosed >$5M | AEHR de-risk — retain 1-2% |
| Sivers Q1 2026 result + Swedish probe outcome (May 29) | Probe closes + listing confirmed | Sivers de-risk — retain 0.5%; otherwise exit |
| Taiwan kinetic escalation | Any binary event | Position-wide impact — own less, faster |

## Contradiction Check

What would invalidate this rebalancing or specific position calls:

1. **L1 thesis is more durable than my treatment of SK Hynix**. If HBM contract-market discipline holds AND Samsung HBM4 fails to capture meaningful Rubin allocation, the "cut SK Hynix 50-60%" call is too aggressive. **Counterweight**: even under bullish L1, the existing thesis kill trigger remains Samsung >35% Rubin allocation. Sizing at 10–12% allows the L1 thesis to play out without 25%+ exposure to a binary outcome. The 2026-05-24 retro identifies SK Hynix as the largest narrative-price gap with vault explicitly weakening while price near ATH — this is the position where the deltas are widest.

2. **AI capex cycle extends through 2028**, not peaks 2026. If hyperscaler capex grows another full leg (NVDA Q1 2027 guidance >+30%, TSMC capex raised to $50B+, Samsung HBM4 fails qualification), memory cycle keeps running and SNDK at 22.9x is correct rather than mean-reverting. **Counterweight**: SNDK is NAND-only pure-play; AI capex extension supports HBM (SK Hynix, BESI, TSM CoWoS) more than NAND. Proposed reweighting captures HBM/CoWoS extension via SK Hynix core position + BESI/TSM/KLAC/AMAT upsize while shedding pure-NAND beta where structural argument is weakest. NVDA Q1 FY27 actual print ($82B vs $78B guide, +85% YoY) is empirical AI capex extension validation supporting the rotation rather than weakening it.

3. **NVDA stress test concerns underweighted in upsize call**. The 2026-04-23 stress test rated 6/10 bull assumptions 🔴 — share erosion to ~75% on Bear trajectory, Taiwan tail 3x consensus, China $50B structural loss, Jevons-vs-efficiency contested. **Counterweight**: stress test concerns are real but partially counter-acted since: Q1 FY27 monster beat validates execution; Hopper/A100 useful life extending to 7-8 years (Dylan Patel) and 1T-parameter dense models as agent-era entry ticket (Luo Fuli) directly counter Jevons-vs-efficiency 🔴. NVDA at 60% ROIC + 45.9x P/E is fairly priced for the structural moat depth.

4. **AMD trim call is too aggressive given aligned-up retro signal**. The 2026-05-24 retro identifies AMD as cleanest aligned-up confirmation ($417→$462 +10% week) driven by Meta $60B AI infra deal + OpenAI 6GW + MI400/Helios validation. **Counterweight**: cleanest aligned-up signal supports retaining a meaningful position (3-4% vs 0%), not aggressive upsize. ROIC 8.1% on 62x P/E remains the binding constraint regardless of momentum confirmation.

5. **Mental model #13 misclassifies a position**. The most expensive error in this sector is classification. If AMD is actually re-rating toward a compounder via custom-silicon design wins, the trim destroys value. If MRVL's Celestial Photonic Fabric validates as the memory-disaggregation primitive, the exit destroys multi-bagger upside. **Counterweight**: AMD ROIC NTM 8.1% and MRVL ROIC NTM -0.8% are the empirical disconfirmation of compounder classification at the current cycle position. Compounders run ROIC >25%. The valuations (62.8x and 69x P/E NTM) already price the compounder outcome — asymmetry to the downside if classification fails to flip.

6. **VICR / Murata / AIXA exits are too aggressive given moat depth**. **Counterweight**: I revised these from EXIT to TRIM (1-2%) recognizing:
   - VICR: Rubin >2,000A architectural necessity + ITC LEO licensing optionality is real
   - Murata: 50% EV MLCC + 008004 monopoly + 800VDC AI-rack content scaling is real
   - AIXA: 90%+ 6-inch InP MOCVD share + Q1 2026 mix shift to 65% optoelectronics is real (Kerrisdale €55 target = +296% from publication)
   - Final calls hold modest positions for optionality rather than pure exit; 1-2% sizing reflects asymmetric upside with bounded downside

7. **Power-law concentration argument may be wrong for institutional memory of a single allocator**. Power-law portfolio returns from 30-stock benchmarks may not apply to a single concentrated book where idiosyncratic execution dominates. **Counterweight**: proposed structure is more concentrated (19 positions, but compounder share of book rising from ~20-23% to 57-68%); rebalancing implements the power-law thesis rather than diluting it.

8. **Loss-makers (Sivers, IQE, AAOI) are pre-chasm S-curve options that pay off binary**. Generalist principle in preamble warns pre-chasm is "binary outcome distribution, high failure risk" — but also that mid-chasm secured S-curves are highest-edge zone. **Counterweight**: proposed cuts retain 0.5-1% positions for option value; cuts are from 2% to 0.5-1%, not to 0%. Convex bets stay convex bets, but at sizes that reflect their pre-chasm risk profile.

9. **WFE upsize call (3x rotation to 28–32% NAV) is overly concentrated in one sub-sector**. **Counterweight**: WFE is structurally different from logic foundry (TSM) — semi-cyclical compounders with #12 rising floor, multi-customer (not anchor-binary), and structurally diversified across nodes (foundry + memory + AP). The five WFE names (LRCX/AMAT/KLAC/ASMI/BESI) have distinct moats (etch dominance / broadest WFE / process control / ALD POR / hybrid bonding) — they are not a single trade.

## Source Excerpts

Primary inputs (per-thesis reads completed 2026-05-24):
- [[Live Portfolio]] — refresh 2026-05-23 16:50, FMP wholesale tier, 28/28 tickers; valuation/growth/ROIC data per position in active table
- [[Mental Models/Industry - Semiconductors]] — evergreen models #1–#19 + live anchor L1 (DRAM structural reclassification via HBM contracted markets)

Per-thesis source notes:
- [[Theses/TSM - Taiwan Semiconductor]] — Q1 2026 58.8% GM, 92% advanced-node share, $165B Arizona, CoWoS $10B annuity, A16 NVDA exclusivity, COUPE photonics
- [[Theses/NVDA - Nvidia]] — Q1 FY27 monster beat ($82B vs $78B guide, 74.9% GM recovery, $80B buyback), CUDA general-purpose vs ASIC application-specific, Omniverse + OpenUSD $600B option, stress test 6/10 🔴 partially mitigated
- [[Theses/000660 - SK Hynix]] — Q1 2026 72% op margin record, Vera Rubin HBM4 ~70/30/0 split, Samsung "best scores" qualification, Gemini Incumbent Erosion 62→45%, HBF + Solidigm options, stress test 5/10 🔴
- [[Theses/SNDK - SanDisk]] — Q2 FY26 51.1% GM guided to 65-67%, +3,271% from spin-off, HBF SK Hynix partnership + OCP standardization, ~12% NAND share, 89% top-7 cloud concentration
- [[Theses/AMD - Advanced Micro Devices]] — Sole merchant full-stack NVDA alternative, OpenAI 6GW + Meta 6GW (12GW combined), 10% OpenAI warrant dilution, Helios rack Q3 2026, Venice Dense 2.7x thread density vs Intel
- [[Theses/LITE - Lumentum]] — 50-60% 200G EML share, butt-joint regrowth 4th-power-of-bandwidth failure scaling, NVDA $2B capacity lock-out, OCS $400M backlog, S&P 500 inclusion Nov 2025
- [[Theses/AVGO - Broadcom]] — VMware 13-22%→78% OpMargin (largest software M&A margin expansion ever), 5 XPU customers, Anthropic-Google through 2031, Tomahawk 6 (102.4 Tbps, 2 quarters ahead of NVDA Spectrum-X1600), $100B+ AI revenue 2027 target
- [[Theses/MRVL - Marvell Technology]] — Trainium 3 socket loss to Alchip, Google "talks" not signed, Celestial AI Photonic Fabric $3.25B pre-revenue, NVLink Fusion $2B Nvidia containment
- [[Theses/LRCX - Lam Research]] — Q3 FY26 mix 59% F/L / 34% Memory structural inversion, ~80% etch share GAA Akara, Aether dry resist SK Hynix TOR, 2028 IDay $25-27B / 50% GM target
- [[Theses/AMAT - Applied Materials]] — Broadest WFE (PVD 85%, CMP 65%, implant 70%+), 4 architectural inflections (GAA + BSPDN + HBM/AP + ICAPS), BESI 9% stake + Kinex, EPIC Center Spring 2026
- [[Theses/KLA - KLA Corporation]] — 56-63% PC share, growth algorithm WFE × intensity × share = 12-17% CAGR floor, $4B → $6B service annuity, 73% ROIC, 17yr dividend streak, $7B buyback
- [[Theses/ASMI - ASM International]] — ~55% single-wafer ALD share, POR annuity 5-7yr per node win, two engines ALD + Epi (CFET 2030+), ASMPT 25% stake $1.0-1.2B off-balance-sheet
- [[Theses/BESI - BE Semiconductor Industries]] — 67% D2W hybrid bonding share, AMAT 9% stake + Kinex, JEDEC HBM4 720→775→900µm relaxation delays HBM ramp 2yr, HBM5+ 24-Hi architectural mandate 2029-2030
- [[Theses/6981 - Murata Manufacturing]] — 50% EV MLCC share at 3-5x ICE content, 50% 008004 small-case share, 440K MLCCs per GB200 NVL72 rack, 800VDC AI-rack content scaling 2-3x
- [[Theses/VICR - Vicor Corporation]] — Rubin >2,000A architectural necessity for VPD, ITC LEO converting share losses to 90% GM royalties, 6 reinforcing moats, founder Vinciarelli 78yo
- [[Theses/AEHR - Aehr Test Systems]] — Q3 FY26 bookings $37.2M (5x QoQ, book-to-bill >3.5x), AI processors >35% of mix, SiPh design-in March 2026, 4-7yr qualification gap
- [[Theses/SIVE - Sivers Semiconductors]] — Only listed pure-play on ELS tier of CPO, 4-inch InP fab in Glasgow, partnerships pre-revenue, Swedish Economic Crime Authority preliminary investigation
- [[Theses/AIXA - Aixtron]] — Kerrisdale "ASML of compound semi deposition", 90%+ share in 6-inch InP MOCVD, Q1 2026 65% optoelectronics order share, Kerrisdale €55 target (+296% from publication)
- [[Theses/IQE - IQE]] — UK Takeover Code formal offer period since Sept 2025, stock 4.7p→52.5p (>1,000% rally), Taiwan operations for sale, Win Semi 50%+ share at 33% margins vs IQE 2%

Supporting sector context:
- [[Sectors/DRAM & HBM Memory]]
- [[Sectors/NAND Memory & Storage]]
- [[Sectors/Semiconductor Foundries]]
- [[Sectors/Semiconductor Capital Equipment]]
- [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]]
- [[Sectors/Optical Networking & Photonics]]
- [[Sectors/Compute & AI Compute Accelerators]]
- [[Sectors/Custom Silicon & Networking Semiconductors]]
- [[Sectors/MLCC & Power Semiconductors]]
- [[Sectors/Modular Power Conversion Components]]
- [[Sectors/Data Center Power & Cooling]]
- [[Sectors/Photonic Metrology]]

Cross-portfolio retrospective input:
- [[Research/2026-05-24 - Retrospective 1w - Synthesis]] — NVDA largest "unreactive-good" gap (×2.0), AMD cleanest aligned-up confirmation, SK Hynix largest narrative-price gap (×1.5 inverted-bear); rotation signals corroborated

## Log
- 2026-05-24: Created (initial version). Portfolio-level synthesis applying [[Mental Models/Industry - Semiconductors]] (#1, #2, #6, #7, #10, #11, #12, #13, #14, #17, #18, L1) against Live Portfolio valuation/growth/ROIC data refreshed 2026-05-23 16:50. Headline call: book is inverted barbell — memory cyclicals at peak overweighted; structural compounders underweighted. Recommended rotation: memory ~40-50% → ~12-15%; compounder share of book ~20-23% → 57-68%; exit Murata, VICR, MRVL, AIXA, IQE.
- 2026-05-24: Rewrote with per-thesis depth after user feedback that initial pass shortcut by classifying positions from general knowledge rather than reading actual thesis content (graph-primer anti-pattern per CLAUDE.md Rule 8). Read all 19 semi theses in vault (AAOI confirmed not to have thesis). Per-position revisions: AMD trim softened from 60% to 30-40% (sole merchant full-stack alternative + retro aligned-up signal); AVGO upsized further (VMware playbook empirically working at 78% OpMargin); KLAC upsized to 7-8% (highest-quality WFE compounder by ROIC + service annuity reframe); LITE trim reduced from 60% to 50% (physics-gated monopoly is real); Murata + VICR + AIXA revised from EXIT to TRIM (1-2% each — moat depth real even if multiples rich); MRVL confirmed EXIT (Trainium 3 execution gap + negative ROIC NTM). 2026-05-24 1w retrospective signals (NVDA unreactive-good largest gap, AMD aligned-up confirmation, SK Hynix narrative-price gap) corroborate rotation direction. Conviction tags in source thesis files ignored per user instruction; classification driven by Mental Model #13 + ROIC NTM as quality proxy + per-thesis moat analysis.
