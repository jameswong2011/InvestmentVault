---
publish: false
date: 2026-06-06
tags: [research, meta, surface-scan]
status: active
source: vault synthesis
source_type: synthesis
scope: sector:Semiconductors
propagated_to: []
---

# Semiconductor Surface Scan — Mental-Model-Aligned Opportunity Discovery (2026-06-06)

Scope: semiconductor investment opportunities consistent with [[Mental Models/Industry - Semiconductors]]. The mental model locates alpha at five points: **#1 emerging bottlenecks driving asymmetric pricing-power shifts**, **#2 qualification-gate monopolies hidden behind share data**, **#14 reclassification triggers that flip the multiple**, **L1 DRAM de-cyclicalization**, **L2 WFE re-rating as structurally non-cyclical**. This scan ranks the vault's *uncovered* value-chain nodes against those lenses, not the 28 semi positions already held.

## Headline: the vault owns the equipment and substrate layers; it does not own the consumables, materials, or design-tool layers — and that is where the next binding constraint sits

Per [[Research/2026-06-05 - AI Silicon Shortage - N3 and Memory Constraint - deep-dive]] (SemiAnalysis, dated yesterday), the binding constraint migrated **CoWoS → datacenter power → front-end silicon (N3 logic + HBM/DRAM)**, with power now modeled *in excess* of compute. The vault has propagated this to 8 theses and 8 sectors at the foundry/memory/equipment layer. It has **not** built positions one layer upstream — silicon wafers, photoresist/EMC/specialty gases, and EDA — even though the mental model's #2 names "EDA triopoly" and "qualification-gate monopolies" explicitly, and the N3 shortage mechanically tightens every upstream consumable. Three of these nodes have raw material already sitting in the vault (two EDA primers in `_Inbox/`; `_hot.md` Open Question #74 flags upstream MLCC materials).

## Portfolio Blind Spots — uncovered nodes the vault's own theses imply are load-bearing

| Uncovered node | Implied by (vault evidence) | Mental-model lens | Coverage today |
|---|---|---|---|
| **EDA tools** (Synopsys / Cadence / Siemens EDA) | Mental model #2 names "EDA triopoly"; every fabless thesis (NVDA, AMD, AVGO, MRVL) depends on it; 2 unprocessed primers in `_Inbox/` | #2 qualification-gate monopoly + #16 geopolitical bifurcation | **Zero** thesis; 2 primers queued |
| **Leading-edge silicon wafers** (Shin-Etsu, SUMCO) | N3 deep-dive names front-end wafer THE binding constraint; appears only as passing mention in 5 theses | #1 bottleneck + #2 qual-gate + #17 inelastic supply | **Zero** thesis |
| **HBM/advanced-packaging materials** (Resonac/Showa Denko, Namics EMC, Mitsubishi Gas BT resin) | SK Hynix thesis: Namics EMC exclusivity is a *named moat dependency*; ABF sector note calls MGC BT resin a "second monopoly within the substrate stack" | #2 qual-gate monopoly | **Zero** thesis (mentioned inside others) |
| **ABF substrate manufacturers** (Ibiden, Unimicron) | Full draft sector note [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] with 10-name watchlist; "second-most-constrained capacity bottleneck after CoWoS" | #1 bottleneck + #14 (cyclical→AI-infrastructure reclassification) | Sector note exists; **zero** committed thesis |
| **Electronic specialty gases** (Linde, Air Liquide, Air Products) | Named in foundry/WFE Risk sections as unmonitored dependency; 100% consumable, qualification-gated | #2 qual-gate (consumable annuity) | **Zero** thesis |
| **Photomask / pellicle / blank mask** (Hoya, Toppan, Shin-Etsu) | EUV pellicle is a single-vendor chokepoint; appears nowhere | #2 qual-gate monopoly | **Zero** thesis |

The pattern: **the vault is long the picks-and-shovels (WFE primes, BESI, test) but flat the picks-and-shovels of the picks-and-shovels** — the consumables and design tools that gate the equipment layer itself. Under the mental model, these consumable/qualification-gate layers are *more* durable than the equipment they feed (no cyclical capex timing; revenue is per-wafer-shipped, not per-tool-sold).

## Supply-Chain Mapping — hidden correlations in what is already held

- **Taiwan-tail single-event risk is portfolio-wide, not position-wide.** TSM (foundry), Unimicron exposure (via TSM thesis), and the entire WFE basket's largest single customer all sit in the same ~100-mile window. The foundry sector note already frames this as "thesis risk for every foundry-exposed long, not a position risk." A silicon-wafer or EDA position would be a *diversifying* semi exposure: Shin-Etsu/SUMCO wafer fabs are in Japan; EDA is US-domiciled IP with no fab. Both reduce the book's geographic concentration while staying inside the mental model.
- **The book is triple-counting the HBM trade.** SK Hynix (HBM maker) + BESI (hybrid-bonding tools) + AEHR (HBM burn-in) + FORM (HBM probe, monitoring) + Ajinomoto/TOTO (packaging substrates) are all the *same* underlying bet. A single HBM4-allocation disappointment (the SK Hynix kill trigger: Samsung >35% of Rubin in Q3/Q4 2026) would simultaneously pressure five positions. The materials layer (Resonac EMC, MGC BT) is correlated too — but the EDA and wafer nodes are NOT, making them the cleanest diversifiers.
- **WFE basket is one rate-of-change away from synchronized de-rate.** Per mental model #19, equipment orders lead utilization by 6+ months and can push out together. The vault's UPSIZE recommendation on the WFE basket (LRCX/AMAT/KLA/ASMI/BESI → ~28-32% combined) concentrates the book into a single book-to-bill signal. Silicon wafers are a *consumption* exposure (utilization × wafers-shipped), structurally lagging-stable rather than order-cyclical — a better expression of L2's "structurally rising floor" thesis than the tool-makers themselves.

## Contrarian Signal Detection — where the framework most diverges from consensus

1. **Silicon wafers are priced as a commodity; they are a supply-disciplined oligopoly choosing margin over volume.** Shin-Etsu + SUMCO = >50% of 300mm capacity, top-5 = 72.6%. Both are *deliberately shelving greenfield expansion* despite AI-grade tightness (SUMCO cancelled its Saga greenfield, is exiting Miyazaki 200mm by late 2026 to free 300mm AI-grade capacity). This is the *exact* mental-model #1 + #17 setup: inelastic supply response because an oligopoly chooses to exercise pricing power and let demand fall rather than expand. Consensus models wafers as low-margin commodity; the framework reads structural pricing power at the front-end binding constraint. **Widest framework-vs-consensus gap in the uncovered set.**

2. **EDA is a software-margin qualification-gate monopoly trading as a GDP-sensitive cyclical.** Synopsys + Cadence + Siemens EDA = 70% global / ~80% China. Switching cost is total (a chip taped out on one flow cannot re-spin on another without full re-verification — the same design lock-in the mental model #2 cites for CUDA). The May 2025 BIS China ban (China = 10-16% of Synopsys revenue; 12% Cadence) → June 2025 partial reversal created a *live decoupling cycle*: consensus oscillates with trade headlines while the structural fact (every N3/N2 tape-out worldwide flows through 2-3 tools) is unchanged. Per mental model #16, the China-domestic EDA push (Empyrean, etc.) is a *parallel market*, not Western share loss — so the Western triopoly's effective moat on the AI-relevant leading edge is *wider* than aggregate China-inclusive share suggests.

3. **ABF substrate makers are the cyclical→structural reclassification (#14) the vault has researched but not acted on.** The draft sector note already does the work: substrate body sizes grew 2.5-3× since 2020, yield drops geometrically with area, "the market is still mispricing as PC/server cyclicality." Ibiden trades on PC-cycle sentiment while its AI-substrate franchise compounds underneath. This is the *identical* re-rating that played out at Ajinomoto 2021-2023 (cited in the vault's own TOTO thesis as the analog) — but the vault owns the *film* monopolist (Ajinomoto) and not the *substrate* franchise where the body-size-driven ASP step-up actually accrues.

## Implied-but-unwritten theses (tickers circling the vault without commitment)

- **EDA** — 2 primers in `_Inbox/` (`EDA Market Primer`, `The EDA Primer From RTL to Silicon`), named in mental model #2, referenced across 7 semi theses. The vault has been circling this for at least one ingest cycle without committing. **Highest-readiness gap.**
- **Upstream MLCC materials (Sakai 4078 / Toray / Disco 6146)** — `_hot.md` Open Question #74 explicitly flags the decision; the 2026-06-05 MLCC upstream deep-dive argues the most acute AI-MLCC pricing power sits one layer above Murata (which is held). Decision deferred on illiquidity / "investability paradox."
- **Silicon wafers (Shin-Etsu 4063 / SUMCO 3436)** — referenced in 5 theses as a dependency; never a thesis despite being the named binding constraint.

## Opportunity Generation — ranked by conviction impact

### 1. EDA triopoly thesis (Synopsys / Cadence / Siemens EDA) — HIGH impact
- **Topic**: Build a thesis cluster on the EDA triopoly as a #2 qualification-gate monopoly with #16 geopolitical-bifurcation optionality. Lead with the design-lock-in mechanism (tape-out flow switching cost = CUDA-grade), the AI-design-complexity tailwind (every chiplet/3D-IC/backside-power design multiplies verification compute and tool seats), and the China-decoupling cycle as a *recurring mispricing* rather than a structural impairment.
- **Why now**: 2 primers already deposited in `_Inbox/`; the N3 design-complexity inflection (chiplet + backside power + High-NA DTCO) is the structural EDA-intensity driver; the May-2025→June-2025 BIS ban-then-reversal makes the China-headline mispricing live and tradeable.
- **Vault connection**: [[Mental Models/Industry - Semiconductors]] #2/#16; builds adjacency to every fabless thesis ([[Theses/NVDA - Nvidia]], [[Theses/AMD - Advanced Micro Devices]], [[Theses/AVGO - Broadcom]], [[Theses/MRVL - Marvell Technology]]); diversifies the book's Taiwan-tail concentration (US-domiciled IP, no fab).
- **Expected impact**: High — could establish a new high-conviction qualification-gate position class the book entirely lacks. Likely 2-3 new theses (SNPS, CDNS).
- **Suggested approach**: `/ingest` the two `_Inbox/` primers → `/thesis SNPS` and `/thesis CDNS` → `/compare SNPS vs CDNS` for the duopoly split → create `Sectors/Electronic Design Automation` MOC.

### 2. Leading-edge silicon-wafer thesis (Shin-Etsu / SUMCO) — HIGH impact
- **Topic**: Thesis on the 300mm AI-grade wafer duopoly as the #1 binding-constraint bottleneck with #17 inelastic-supply dynamics. Core claim: the two suppliers' *deliberate* refusal to expand greenfield capacity into AI-driven tightness is the mental-model signature of an oligopoly exercising pricing power — mispriced as commodity cyclicality.
- **Why now**: yesterday's N3 deep-dive names front-end wafer THE binding constraint (>100% effective N3 utilization H2 2026, ~2-yr cleanroom ceiling); SUMCO cancelled Saga greenfield + exiting Miyazaki 200mm by late 2026 — concrete supply-discipline datapoints; >50% combined 300mm share.
- **Vault connection**: [[Research/2026-06-05 - AI Silicon Shortage - N3 and Memory Constraint - deep-dive]]; [[Sectors/Semiconductor Foundries]] (wafer is the input TSM is cleanroom-constrained on); mental model #1/#2/#17. Diversifies geography (Japan fabs) vs Taiwan-concentrated book.
- **Expected impact**: High — directly expresses the current binding constraint with a supply-disciplined-oligopoly structure the WFE basket does not replicate (consumption vs order-cyclical exposure).
- **Suggested approach**: web-research Shin-Etsu (4063) + SUMCO (3436) 300mm AI-grade mix, capex discipline, contract-vs-spot pricing structure → `/thesis 4063` (cleaner — diversified chemicals conglomerate with the wafer crown jewel, lower cyclicality) and/or `/thesis 3436` (pure-play, higher beta to the trade).

### 3. ABF substrate franchise thesis (Ibiden / Unimicron) — MEDIUM-HIGH impact
- **Topic**: Promote the existing draft sector note into committed theses. Lead with the #14 cyclical→AI-infrastructure reclassification: substrate body-size growth (50×50mm → 120×180mm) compounding faster than yield-learning curves = structural pricing power mispriced as PC cyclicality (the Ajinomoto 2021-2023 re-rating analog the vault already cites).
- **Why now**: CoWoS scaling 35K→130K wpm 2024-2027 drives ~3.7× carrier-substrate revenue; substrate is "second-most-constrained bottleneck after CoWoS" per the vault's own note; the cycle-bottom multiple (PC reset 2023-2024) still embedded gives an asymmetric entry.
- **Vault connection**: [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] (full draft watchlist already built); [[Theses/2802 - Ajinomoto]] (vault owns the film monopolist, not the substrate franchise); [[Theses/TSM - Taiwan Semiconductor]] (Unimicron is TSM's CoWoS carrier supplier).
- **Expected impact**: Medium-high — converts existing research into positions; but Unimicron adds Taiwan concentration (Ibiden is the cleaner Japan-domiciled expression).
- **Suggested approach**: `/thesis 4062` (Ibiden — #1 ABF substrate, Japan, Intel + AI-accelerator mix) as the lead; consider Mitsubishi Gas Chemical (4182) as the BT-resin #2-monopoly within the stack.

### 4. HBM/packaging materials monopoly thesis (Resonac / Mitsubishi Gas Chemical) — MEDIUM impact
- **Topic**: The named moat *dependencies* inside existing theses are themselves investable qualification-gate monopolies. SK Hynix's Namics EMC exclusivity and MGC's ~70-80% BT-resin share are #2 monopolies the vault references but does not own.
- **Why now**: HBM4→HBM4E→HBM5 stack-height escalation tightens every interface material (EMC, underfill, mold compound); these are single-source or near-single-source qualification gates with no cyclical capex.
- **Vault connection**: [[Theses/000660 - SK Hynix]] (Namics EMC named as moat dependency); [[Sectors/DRAM & HBM Memory]] §Yield Deltas (materials drive the 30-pt yield gap); [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] (MGC BT resin).
- **Expected impact**: Medium — high-quality monopolies but small-cap/illiquid; resolves the same "investability paradox" as Open Question #74's upstream-MLCC decision.
- **Suggested approach**: scope Resonac (4004) and MGC (4182) revenue exposure to AI-grade EMC/BT vs commodity; decide alongside the #74 Sakai/Toray/Disco upstream-materials decision as a single "upstream qualification-gate materials" initiative.

### 5. Resolve the deferred upstream-MLCC-materials decision (Open Question #74) — MEDIUM impact
- **Topic**: Already-flagged decision on Sakai (4078, BaTiO₃ pure-play), Toray (3402, release film), Disco (6146, >80% MLCC singulation + AI-semis). The 2026-06-05 deep-dive argues the most acute AI-MLCC pricing power is one layer above the held Murata position.
- **Why now**: the analysis is done; the decision is open in `_hot.md`. Disco (6146) is the standout — >80% share of precision dicing/grinding singulation is a qualification-gate monopoly spanning *both* MLCC and AI-semiconductor singulation, broader than the pure-MLCC names.
- **Vault connection**: [[Theses/6981 - Murata Manufacturing]]; [[Sectors/MLCC & Power Semiconductors]]; [[Research/2026-06-05 - AI-Grade MLCC Upstream Pricing Power - deep-dive]].
- **Expected impact**: Medium — Disco specifically may warrant high conviction (#2 monopoly + dual AI-semis/MLCC exposure); the pure-MLCC-materials names face the investability paradox.
- **Suggested approach**: `/thesis 6146` (Disco) as the highest-quality of the three; pass or watchlist the pure BaTiO₃/film names on liquidity.

## Cross-cutting observations

- **Attention allocation note**: the May-24 rebalancing synthesis (UPSIZE WFE basket + compounders, CUT memory) is propagated to 19 theses but **not actioned** (`/status` not run per ticker). The single highest-leverage *existing-book* action is executing that rebalance, independent of any new thesis above. The new theses are additive diversification; the rebalance is risk reduction the vault has already concluded it needs.
- **Decay alert**: no active semi thesis is stale (>30d untouched) — the semi book is the most actively maintained in the vault. The gaps are net-new nodes, not neglected positions.
- **Framework coherence**: all five opportunities sit squarely inside the mental model. None requires a macro/valuation call the vault's posture rejects; each is a qualitative qualification-gate / bottleneck / reclassification insight the framework is explicitly built to surface.

## Related
- [[Mental Models/Industry - Semiconductors]]
- [[Research/2026-06-05 - AI Silicon Shortage - N3 and Memory Constraint - deep-dive]]
- [[Research/2026-05-24 - Semiconductor Portfolio Rebalancing - synthesis]]
- [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]]
- [[Sectors/Semiconductor Foundries]] · [[Sectors/DRAM & HBM Memory]] · [[Sectors/Semiconductor Capital Equipment]]
- [[Theses/000660 - SK Hynix]] · [[Theses/TSM - Taiwan Semiconductor]] · [[Theses/2802 - Ajinomoto]] · [[Theses/6981 - Murata Manufacturing]]
