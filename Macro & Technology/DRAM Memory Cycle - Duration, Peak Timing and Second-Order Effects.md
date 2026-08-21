---
publish: true
date: 2026-07-09
tags: [macro, semiconductors, memory, catalyst, sector/semiconductors]
status: active
sector: semiconductors
source: Synthesis — TrendForce/IDC/SemiAnalysis web data (July 2026) + vault sector notes and research
---

# DRAM Memory Cycle — Duration, Peak Timing and Second-Order Effects

## The Call (opinion, falsifiable)

| Question | Base case (55%) | Partial structural reset (25%) | Peak already in (20%) |
|---|---|---|---|
| Commodity DRAM contract price peak | Q2–Q3 2027 | H2 2027, plateau not spike | Q4 2026 (demand destruction + CXMT bites early) |
| Memory equity peak | **Q4 2026 – Q1 2027**, ~2 quarters ahead of price peak | H2 2027 | **Mid-June 2026 highs were the top** |
| Peak level (SK Hynix / Micron) | ~$1.3–1.5T market caps each (+30–50% from July 2026), at 5–6x peak-forward EPS | $1.8–2.2T caps, multiple holds 10–12x | No new high; 40–60% drawdown from June highs by mid-2027 |
| Downcycle | Prices roll H2 2027, capitulation 2028–29 | Shallow correction, trough margins above prior peaks | Sharp 2027 downturn on hyperscaler capex digestion |

The blended view: this cycle has **2–4 quarters of equity upside left, not 8**, and the remaining return is the melt-up phase: the worst risk/reward segment of any memory cycle. The scenario weights deliberately track the sector note's Evergreen Reset probabilities (60/25/15 there) but shift 5pts toward "peak already in" because three tells have fired since April: the QoQ contract-price second derivative peaked in Q1 2026 (+90–95% → +58–63% in Q2), the late-June equity correction (SK Hynix −23%, MU from 11x to 7x forward in two weeks) shows the marginal buyer is already fighting about the top, and **SK Hynix's $29B Nasdaq listing this month is a textbook cycle-top tell**: mega equity issuance clusters at peak enthusiasm (base rate: secondary listings/IPOs of cyclicals near cycle highs; Kioxia's Dec 2024 IPO marked the NAND trough; issuance direction follows insider information asymmetry).

## Why the price cycle runs into 2027 but not beyond

**Demand.** DRAM deficit ~4.9%, HBM ~5.1%: widest since 2011 ([source](https://finance.biggo.com/news/Vta3FZ4B6tLPsnrZ5pOO)). 2026 supply bit growth only ~16% YoY vs 20–30% norms ([IDC via storageswiss](https://storageswiss.com/2026/05/06/memory-and-flash-prices-not-coming-down/)). HBM 2026 fully sold out, 2027 HBM contract prices negotiated "multiples higher" per [TrendForce](https://www.trendforce.com/presscenter/news/20260602-13074.html). The 3:1 HBM wafer penalty (see [[Sectors/DRAM & HBM Memory]]) means every HBM4 wafer removes ~3 commodity wafers: the shortage is a reallocation, not a demand spike alone.

**Supply: the consensus blind spot.** Sell-side extrapolates "shortage through 2027+" from big-three capex caution ([TrendForce Nov 2025](https://www.trendforce.com/presscenter/news/20251113-12780.html)), but the supply response is larger and earlier than the narrative admits:

| Capacity event | Bits land | Note |
|---|---|---|
| SK Hynix M15X | Mid-2027 ramp → bits Q4 2027 | 1b DRAM, plus M14/M16 1c conversions scaling 10k→70k wpm in 2026 |
| Samsung P5 Pyeongtaek | 2028 | Part of the joint ~$870B decade plan ([DCD](https://www.datacenterdynamics.com/en/news/samsung-and-sk-hynix-to-scale-up-memory-production-capacity-in-2026-to-meet-ai-demand/)) |
| Micron ID1 (Boise) | 2027+ | MU exited consumer memory Dec 2025 to concentrate on DC |
| **CXMT** | Continuous | ~350 kwspm by end-2026 (≈ Micron's ~385k), 420–600 kwspm range by end-2027, ~17% of global wafer capacity; HBM capacity 5k→30k→55k wpm 2025→2027 ([SemiAnalysis](https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram)) |

Per mental model #16, CXMT is a parallel market, but only for leading-edge/qualified product. In commodity DDR4/DDR5 and LPDDR, Chinese bits are fungible with Western bits at the margin (CXMT modules already shipping in Lenovo ThinkBooks, March 2026). CXMT doesn't need HBM qualification to end the commodity shortage; it needs wafers, and it is adding the equivalent of a fourth major by end-2027.

**Demand destruction is the underpriced accelerant.** Consumer is the balancing item: [IDC](https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/) is cutting 2026–27 smartphone/PC forecasts as OEMs cut specs or raise prices. Memoryflation also feeds the AI-monetization gap (per [[AI Bubble Risk and Semiconductor Valuations]]: DDR5 +638% YoY raises AI-server BoM, mechanically widening the $650B threshold). The cycle's demand side is eating itself at both ends: consumer bits priced out now, AI capex ROI pressure building for 2027 budget season.

**Duration arithmetic.** Contract prices inflected Q3–Q4 2025. A Q2–Q3 2027 price peak = a 7–8 quarter upswing, at the long end of the historical 6–9 quarter range (2016–18 ran ~9). Extending the price peak into 2028 requires believing both that CXMT + M15X + conversions add nothing to commodity balance and that hyperscaler capex accelerates a third consecutive year. That is a compound bet, not a base case.

## The equity peak — mechanics of the top

Memory equities peak **~2 quarters before the fundamental peak, every cycle**: MU topped May 2018 at 4–5x forward while earnings rose into Q4 2018, then fell 56%; the historical give-back is 40–60% within six months of the pricing peak ([UncoverAlpha](https://www.uncoveralpha.com/p/every-memory-cycle-ends-the-same), [Luminix](https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators)). Applied to a Q2–Q3 2027 price peak → equity top Q4 2026 – Q1 2027.

The multiple math caps the upside more than bulls model. SK Hynix (+186% YTD) and MU (+141% YTD) both crossed $1T caps ([Yahoo](https://finance.yahoo.com/markets/stocks/article/sk-hynix-joins-micron-in-1-trillion-club-as-ai-memory-chip-rally-accelerates-024514610.html)) and trade at 6–7x forward after the June correction. From here, forward EPS rises maybe 40–60% into mid-2027 estimates while the peak multiple historically compresses toward 4–6x as the market smells the top: the two forces largely cancel. That is how +30–50% (not +150%) becomes the ceiling even in the base case. The market pays peak multiples at the trough and trough multiples at the peak; at 6–7x forward we are already in trough-multiple territory, meaning **consensus already treats these earnings as peak**: the remaining upside is earnings drift, not re-rating.

The 25% scenario is the one that breaks this template: if the [[Sectors/DRAM & HBM Memory]] Evergreen Reset diagnostic confirms (two consecutive quarters of flat/rising HBM ASP while a vendor's share falls ≥5pp; first testable window **Q3–Q4 2026**), contracted HBM has genuinely converted the leaders into semi-cyclicals, mid-cycle multiples re-anchor at 12–15x, and the equity peak moves out to H2 2027 at ~2x current caps. Per Industry mental model L1 this is the user's own live theory, which is exactly why it must be tested adversarially, not assumed: the same L1 logic (winner-take-most, SK Hynix 70% Rubin share) is contradicted by the vault's own Incumbent Erosion model (SKH HBM share 62%→45% by 2030) and by the unactioned 2026-05-22 stress-test flag on [[Theses/000660 - SK Hynix]].

**This note sides with the 2026-05-24 rebalancing synthesis over the sector note's structural framing on position sizing, while agreeing with the sector note on cycle length.** The reconciliation the vault has been missing is that both can be right: the price cycle extends into 2027 (sector note correct) AND the equity risk/reward has already inverted (rebalancing correct), because equities lead. Staged reduction into Q4 2026 – Q1 2027 strength, cutting commodity-torque exposure first (SNDK at 65–67% guided GM is the textbook cyclical at peak) and HBM-qualified leader exposure last.

## Winners beyond the big three

| Name / group | Mechanism | Torque vs durability |
|---|---|---|
| **Nanya, Winbond, PSMC (Taiwan legacy DRAM)** | Big-three DDR4/DDR3 EOL abandonment → EOL parts on allocation, DDR2 contracts +55–60% in a quarter ([VideoCardz](https://videocardz.com/newz/ddr2-memory-is-still-sold-under-contracts-prices-expected-to-rise-55-to-60-this-quarter)) | Highest % torque in the complex; pure true cyclicals: trade, never own. Exit with the equity peak window |
| **Seagate, WDC (HDD)** | NAND price umbrella + nearline sold out through 2027; exabyte pricing power without memory capex risk | Semi-cyclical; cleaner risk/reward than NAND names at this stage |
| **Memory WFE: LRCX, TEL, AMAT, ASMI** | M15X + P5 + ID1 + CXMT tool orders = 2026–28 memory capex wave; DRAM etch/dep intensity rises with 4F2/vertical transitions | Per L2, floors rise each cycle, but orders peak before memory prices peak; [[Theses/LRCX - Lam Research]] and [[Theses/AMAT - Applied Materials]] are the right structure but wrong entry at cycle top |
| **HBM test/assembly chain: Advantest, Camtek/Onto, Besi/Hanmi/ASMPT** | Test intensity per HBM stack is multiples of commodity DRAM; HBM4E/HBM5 → hybrid bonding transition re-rates bonder vendors ([[Theses/BESI - BE Semiconductor Industries]]) | Most durable winner group: qualification-gated (#2), rides HBM units not DRAM price |
| **TSMC** | HBM4 base die migrates to foundry logic: the memory value chain now pays a per-stack toll to [[Theses/TSM - Taiwan Semiconductor]]; layer-monopoly fit under [[Lens - Value Layer Monopoly]] | Structural, cycle-agnostic; memory boom accretes to logic |
| **Materials: Ajinomoto ABF, Namics EMC, Simmtech, Soulbrain** | Substrate/underfill/precursor content per HBM stack; Namics MR-MUF exclusivity (expiry 2026–27 is the swing factor: see [[Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive]]) | [[Theses/2802 - Ajinomoto]] qualification-gate economics; least cyclical of the winners |
| **SRAM-first inference silicon (Cerebras, post-Groq NVDA)** | Memoryflation is a relative subsidy to architectures that dodge the HBM tax: every HBM price hike improves wafer-scale SRAM's comparative economics per token ([[Theses/CBRS - Cerebras Systems]]) | Second-order and partial (MemoryX still buys DDR5), but a genuine non-consensus lens on the CBRS thesis: the memory cycle is a tailwind to its cost position |
| **Chinese memory stack: CXMT ecosystem, NAURA** | Parallel market (#16): domestic HBM3 by end-2026 with domestic toolchain ([Tom's Hardware](https://www.tomshardware.com/pc-components/dram/chinese-semiconductor-industry-gears-up-for-domestic-hbm3-production-by-the-end-of-2026-cxmt-to-produce-chips-while-naura-maxwell-and-u-preseason-design-tools-for-assembly)) | Non-investable directly for this book but the decisive 2027 supply variable |

Already-played (do not chase): module/inventory holders (Kingston-type, Phison, distributors) made their cycle profit on the 2025 inventory revaluation; at this stage they hold expensive inventory into a future price peak: their next move is the write-down.

## Losers

| Group | Mechanism | Severity |
|---|---|---|
| **Low-end Android OEMs: Transsion, TCL, Realme, Honor, Xiaomi** | Memory is the largest BoM line in a sub-$200 phone; thin-margin models cannot absorb 60%+ LPDDR inflation → spec cuts reverse a decade of spec democratization ([IDC](https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/)) | Existential for Transsion-tier margins through 2027 |
| **Consumer PC OEMs (Acer, Asus consumer lines)** | Same squeeze; Lenovo partially hedged via inventory + CXMT sourcing | Margin compression, unit cuts |
| **Industrial / auto Tier-1s on legacy DDR4** | Big-three EOL + allocation on parts designed into 10-year product cycles; no requalification path before 2027 | Underappreciated: shows up as 2026–27 margin misses outside tech |
| **GPU AIBs, consoles, smart TV / set-top** | GDDR7/LPDDR cost inflation into fixed retail price points | Moderate |
| **The AI capex complex itself (second-order)** | Memoryflation widens the $650B monetization gap ([[AI Bubble Risk and Semiconductor Valuations]]); HBM at "multiples higher" 2027 pricing raises accelerator BoM → either NVDA margin pressure or hyperscaler ROI pressure: someone absorbs it | The bear-amplifier: the memory cycle's peak pricing is itself a catalyst for the AI capex digestion that ends the memory cycle. Reflexive loop, not independent risk |
| **[[Theses/PSTG - Pure Storage]] and enterprise storage buyers** | NAND cost pass-through lag compresses gross margin for 2–3 quarters per repricing | Manageable, timing risk only |

## Monitoring dashboard (falsifiable, dated)

| Signal | Window | Reading |
|---|---|---|
| Samsung Rubin HBM4 allocation >35% | Q3–Q4 2026 earnings | Fires the 000660 kill trigger AND the Evergreen Reset diagnostic simultaneously |
| HBM ASP flat/rising while a vendor loses ≥5pp share, 2 consecutive quarters | Q3 2026 – Q1 2027 | Confirms partial reset → shift to 25% scenario, extend equity peak to H2 2027 |
| QoQ DRAM contract increments fall to single digits | Any quarter | Begin staged exit regardless of narrative; the second derivative has led every top |
| 2027 HBM LTA pricing confirmed "multiples higher" | H2 2026 negotiations | Extends earnings visibility; supports base case over peak-already-in |
| Hyperscaler FY2027 capex guides | Jan–Feb 2027 | First deceleration = the cycle's demand-side kill switch |
| CXMT Shanghai Phase 1 ramp + HBM3 domestic qualification | End-2026 | Commodity balance turns 2 quarters after wafers start |
| SK Hynix Nasdaq listing completion and aftermarket | July–Aug 2026 | Distribution into the listing = the top tell confirming; strong absorption = melt-up phase intact |

## Mental Models applied (hypotheses, not verdicts)

- **#3/#7 (capital cycle, phase diagnostic)**: units up + prices up = shortage phase confirmed; the second derivative of contract prices already peaked Q1 2026. Hypothesis: the phase clock is later than the narrative clock.
- **#9 (inventory propagation)**: spot led contract up in 2025; watch spot for the reverse signal: spot softening while contracts still rise = 1–2 quarters to price peak.
- **#17 (supply lags 18–30 months)**: cuts both ways: capacity ordered in the 2025 panic lands 2027–28, on schedule for the historical bust timing.
- **#18 (cycle vs structural decomposition)**: the structural component (HBM contracted, qualification-gated, winner-take-most) is real and owned by SK Hynix/leaders; the cyclical component (commodity DRAM, NAND, legacy) is behaving exactly like every prior cycle. The error to avoid is letting the structural HBM story extend holding periods on the cyclical commodity exposure: that is "AI demand is forever at the 2025 peak" wearing new clothes.
- **L1 (DRAM less cyclical going forward)**: the user's live theory; the Evergreen Reset test Q3–Q4 2026 is its first falsification window. This note deliberately does not assume it.
- **Base rates (Generalist)**: every one of ~8 DRAM upcycles since 1995 ended with a 40–60% equity drawdown; the reference class says the burden of proof is on "this time is contracted," and the June 2026 correction shows the market will not pay for the structural story until the diagnostic confirms.
- **Perez (frenzy phase)**: memory capex is now part of the AI installation-phase over-build; the capacity laid down in this frenzy becomes 2028's cheap substrate: the winners of that phase are memory consumers, not producers.

## Related

[[Sectors/DRAM & HBM Memory]] · [[Sectors/NAND Memory & Storage]] · [[Theses/000660 - SK Hynix]] · [[Theses/SNDK - SanDisk]] · [[Theses/285A - Kioxia]] · [[Theses/CBRS - Cerebras Systems]] · [[Theses/TSM - Taiwan Semiconductor]] · [[Theses/BESI - BE Semiconductor Industries]] · [[Theses/LRCX - Lam Research]] · [[Theses/AMAT - Applied Materials]] · [[Theses/2802 - Ajinomoto]] · [[Theses/NVDA - Nvidia]] · [[Theses/PSTG - Pure Storage]] · [[AI Bubble Risk and Semiconductor Valuations]] · [[CXL Memory Disaggregation Framework]] · [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]] · [[Research/2026-05-31 - DRAM HBM Memory Supercycle - deep-dive]]

Coverage gap: no Micron thesis exists despite MU being load-bearing across every memory note; if the partial-reset scenario confirms, MU (0% Rubin allocation, pure commodity torque + US listing premium) is the highest-beta expression and needs its own note before it can be traded.

- [[Research/2026-08-14 - 000660 NVDA - SK hynix 720B AI Memory Buildout - news]]
- [[Research/2026-08-14 - 000660 SNDK 285A - YMTC NAND Third Place - news]]
- [[Research/2026-08-14 - SNDK - Asymmetrical Bets Investor Day Recap - deep-dive]]: NAND-side contracted book $93.9B / 80% floor-GM; does not retire the DRAM cycle-top call (NAND floors untested; DRAM still the tighter 2026–27 constraint)
## Log
- 2026-07-09: Note created. Call: commodity price peak Q2–Q3 2027, equity peak Q4 2026–Q1 2027 at ~$1.3–1.5T caps (55%), with 20% weight that mid-June 2026 was the top. Reconciles sector-note bull framing with unactioned 2026-05-24 rebalancing rec: both right — equities lead prices by ~2 quarters.

### 2026-08-14
- [[Research/2026-08-14 - 000660 NVDA - SK hynix 720B AI Memory Buildout - news]]: Chey $720B + ten LTAs + custom-HBM — scarcity can persist through 2027 *and* 2029 glut can be seeded by the same buildout.
- [[Research/2026-08-14 - 000660 SNDK 285A - YMTC NAND Third Place - news]]: YMTC 14% NAND units / CXMT 7% DRAM — China as complementary bits this cycle, substitute at destock.
### 2026-08-15
- [[Research/2026-08-14 - SNDK - Asymmetrical Bets Investor Day Recap - deep-dive]]: NAND NBM $93.9B / 80% floor-GM is a contracted-book claim on the *other* memory cycle — does not move the DRAM equity-peak call; floors untested and DRAM remains the tighter 2026–27 constraint.

### 2026-08-20
- Voice pass: de-LLM-speak on body prose (em-dashes, inversion closers, labelled insight, decorative colour). No analytical delta — conviction unchanged
