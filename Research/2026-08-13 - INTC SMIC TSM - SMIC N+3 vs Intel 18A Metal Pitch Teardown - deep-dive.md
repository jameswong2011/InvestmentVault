---
publish: false
date: 2026-08-13
tags: [research, semiconductors, SMIC, INTC, TSM]
sector: Semiconductor Foundries
ticker: INTC
source: 'https://newsletter.semianalysis.com/p/steel-smic-n3-teardown'
source_type: deep-dive
propagated_to: [INTC, TSM]
---

# SMIC N+3 vs Intel 18A — Metal-Pitch Teardown (STEEL / Kirin 9030)

## Thesis Delta

SMIC N+3's 32.5 nm minimum metal pitch is genuinely ~10% tighter than the 36 nm M0 shipping in Intel 18A Panther Lake — a true headline that inverts the real ranking, because on normalized Bohr density SMIC N+3 (113.4 MTr/mm²) sits 38% behind Intel 18A's HD library (~184 MTr/mm² implied) and only matches TSMC's 2019-era N6, reached through SAQP multi-patterning and aggressive DTCO that SMIC pays for in mask count, overlay sensitivity, efficiency, yield and process control. Consensus reads a single cherry-picked M0 number as either "China has caught the leading edge" or "Intel 18A is uncompetitive"; the teardown shows the opposite on both counts — a walled Chinese-domestic node five-plus effective generations behind on performance-per-watt (no EUV, no backside power, prime core at 2021 Arm Cortex-X2 per-clock), and an Intel 18A whose loose 36 nm M0 is a deliberate PowerVia / backside-power design choice (18A *supports* 32 nm M0, tighter than SMIC), not a process deficit.

## Summary

The subject is Huawei's Kirin 9030 Pro SoC (~140 mm²) on SMIC N+3, the most advanced logic process in China and SMIC's third-generation 7 nm node, torn down and cross-sectioned against MediaTek's Helio G99 (~29 mm²) on TSMC N6 as a matched-class baseline — one node heavily export-controlled, the other built on the West's most advanced equipment. The headline finding is a real engineering achievement: SMIC N+3 reaches TSMC N6-class logic density (113.4 vs 107.7 MTr/mm²) without any EUV, edging slightly ahead of a mature node that itself uses EUV. The mechanism is the entire point. N6 hits ~40 nm lower-metal pitches with SADP-class double patterning throughout; SMIC pushes M0 to 32.5 nm — below what a single DUV spacer can resolve — forcing a cascaded second spacer step (SAQP), and holds M1/M2 at 38/40 nm on SADP. More masks, more overlay error, higher trench aspect ratios, tighter process margin, and higher cost per wafer buy a density number that N6 gets for less. Density parity is real; cost, maturity and PPA parity are not.

The density itself is a DTCO construction, not a lithography win. SMIC pulls every design-technology co-optimization booster available: fin depopulation to 2 fins per transistor (same as N6 HD), contact-over-active-gate (COAG — which N6 does *not* integrate), single diffusion break, a 3:2 M1-to-gate ratio for local routing flexibility, and a compressed 228 nm cell height (5% below N6's 240 nm, 9.5% below N+2's 252 nm) at a 57 nm contacted gate pitch identical to N6 HD. The cost of leaning entirely on DTCO shows in library breadth: the Kirin 9030 exposes only one standard-cell library (2 NMOS + 2 PMOS fins), where TSMC N6 ships both HD and HP (3+3) libraries that designers mix on timing-critical paths — a narrower design surface the teardown attributes to SMIC's smaller customer base and a constrained domestic EDA ecosystem. The 3:2 routing ratio is itself an outlier the leading edge has largely abandoned (TSMC and Intel both run 1:1 on their current nodes; only Samsung still uses 3:2 at SF4/SF3), trading patterning and layout complexity for density it cannot otherwise reach.

A metal-pitch headline proves density; it does not prove competitiveness, and the PPA gap is where the node's true position sits. M0 is a local intra-cell routing layer whose usefulness depends on the full interconnect stack — M1/M2 pitch, track count, via and line resistance, design rules, mask count, overlay control. On the axis that matters since Dennard scaling broke — performance and efficiency, not area — the Kirin 9030 Pro performs like a three-year-old Android flagship and trails current Apple, Qualcomm, MediaTek and Samsung parts, with a wider efficiency gap than performance gap. Huawei's prime core lands at roughly Arm Cortex-X2 per-clock (a 2021 design); Apple's 2020 M1 Firestorm is still 35% higher per clock and 57% faster in absolute integer at a similar 4.5 W, the Apple M5 P-core is 60% higher per clock and 2.7× faster, and Apple's *efficiency* core delivers 20% more integer performance drawing 1 W against Huawei's prime core at 4.5 W. N+3 matches N6, but N6 is several nodes old; Apple and Qualcomm build on N4/N3P, which sit on a better voltage-frequency curve and hand designers a larger transistor budget for wider cores, larger caches and lower operating voltage. The cores also failed to hold rated maximum frequencies, pointing to thermal, power or stability limits — the process-control tax showing up as clock ceilings.

The report is also a market-structure event: it is the first public output of STEEL (the SemiAnalysis Teardown Engineering & Evaluation Lab in Oregon, standing up over ~18 months), pitched explicitly at PE-owned TechInsights — under-invested in capex, being sold, and long unchallenged in reverse-engineering. The strategic read on China is deliberately two-sided. Export controls changed China's optimization problem rather than freezing it: without EUV, SMIC leans on DUV immersion, SAQP and DTCO while Huawei shifts the burden onto architecture and packaging. Huawei's τ (tau) scaling law — system-technology co-optimization reframed in the time domain — and its "LogicFolding" 3D-stacking roadmap are the answer to a planar-density ceiling, targeting prime-core frequency from 2.75 GHz today toward ~5 GHz by 2031 and package-footprint density that is explicitly not a like-for-like foundry comparison. Process learning is diffusing outward — SMIC is licensing N+2/N+3 to HLMC/Hua Hong at government direction, with Cambricon (a ByteDance supplier) and Alibaba's T-Head positioned to benefit — so sanctions aimed at one fab lose bite as the knowledge spreads to an ecosystem. The teardown's own conclusion: China is not closing the gap with Intel, Samsung and TSMC (no EUV, no backside power, higher process complexity, visible trade-offs), but it is advancing, and domestic silicon that is "good enough" for phones, inference, networking and security-sensitive workloads can matter strategically without matching the leading edge — a parallel market, not a Western competitor.

## Framework / Mental Model

The teardown operationalizes a repeatable methodology for judging process-node competitiveness that is worth extracting as a scoring scheme, because the entire investment error it guards against — reading one headline spec as node leadership — is the [[Industry - Semiconductors]] #2 failure mode (qualification-gate quality hidden behind a single optic, here metal pitch standing in for share data). The method has four axes that must be read together; any one in isolation misleads.

**1. Normalize density before comparing — the Bohr metric.** Compare nodes on a weighted average of NAND2 gate area (60%) and scan-flip-flop area (40%), a realistic mix of combinational and sequential logic, rather than on any single pitch. This is a pure process-level density comparison and is how SMIC N+3 (113.4 MTr/mm²) resolves to *slightly above* N6 (107.7) yet 38% *below* Intel 18A HD — a ranking the raw 32.5 nm M0 number hides. The metric has limits (it mismodels mixed-fin cells such as TSMC FinFLEX) but is the cleanest apples-to-apples density lens.

**2. Read pitch to infer patterning cost, not lithography wavelength.** A pitch below single-DUV-spacer resolution implies a cascaded second spacer (SAQP); an A/B-split pitch at ~38–40 nm implies SADP. From cross-sections the analyst can distinguish double vs quadruple patterning — the mask-count and overlay-cost axis — but *cannot* assign a specific layer to EUV. The discipline: a tighter pitch reached by SAQP where a rival uses SADP is a higher-cost, lower-margin route to the same density, not evidence of a better process. Patterning scheme is a cost signal masquerading as a capability signal.

**3. Separate the density upper bound from usable density and from PPA.** FEOL transistor density sets an upper bound; the interconnect stack (M1/M2 track count, via/line resistance, design rules, routing flexibility) sets how much of that density is usable at block and chip level; and PPA — power and performance, not area — sets competitiveness, because since Dennard scaling broke the voltage-frequency curve of the node (a function of node vintage) dominates. Area is the easiest thing to see in a die shot and the least decisive.

**4. Inventory the DTCO boosters and price their side-effects.** The levers a foundry pulls to buy density without EUV — fin depopulation (trades drive strength for area), COAG (drops cell height), single diffusion break (saves area, raises local-layout-effect sensitivity that must be modeled in the PDK), M1:gate ratio, track-count reduction — each carries a process-complexity or routing-flexibility cost. Counting the boosters a node needs to reach a density target is a direct read on how much margin it is spending to get there. SMIC N+3 needs the full stack of boosters plus SAQP to match a node (N6) that reaches the same density with fewer.

Applied as a hypothesis to test (per the [[Generalist - Overview]] reading protocol): the headline "SMIC 32.5 nm < Intel 36 nm" is exactly the kind of single high-salience spec that Semis #2 warns hides the real qualification gate — which is not pitch but yield and cost per good die, and PPA per watt. The framework's value is forcing the density-vs-cost-vs-yield-vs-power decomposition before any "who is ahead" verdict.

## Evidence

Provenance legend: `[1×: SemiAnalysis STEEL]` = first-party STEEL lab measurement from this teardown; `[est.]` = STEEL estimate/derivation or roadmap projection; `[web: semianalysis]` = comparative/context claim from the article narrative.

### Metal stack and patterning — SMIC N+3 vs TSMC N6 vs Intel 18A

| Layer | SMIC N+3 | TSMC N6 | Intel 18A | Patterning (N+3) |
|---|---|---|---|---|
| M0 (min metal pitch) | 32.5 nm `[1×: SemiAnalysis STEEL]` | ~40 nm `[1×: SemiAnalysis STEEL]` | 32 nm supported / 36 nm shipped in Panther Lake `[web: semianalysis]` | SAQP (below single-spacer resolution) `[1×: SemiAnalysis STEEL]` |
| M0 intra-cell line width | 21.5–24 nm (alternating) `[1×: SemiAnalysis STEEL]` | — | — | 4-population line-width loading `[1×: SemiAnalysis STEEL]` |
| M0 power-rail width (VDD/VSS) | 55 nm `[1×: SemiAnalysis STEEL]` | — | — | wide wire, low IR drop `[web: semianalysis]` |
| M1 | 38 nm `[1×: SemiAnalysis STEEL]` | ~57 nm `[est.]` (N+3 is 33% below N6) | 1:1 M1:gate `[web: semianalysis]` | SADP (A/B split) `[1×: SemiAnalysis STEEL]` |
| M2 | 40 nm `[1×: SemiAnalysis STEEL]` | 40 nm `[1×: SemiAnalysis STEEL]` | — | SADP; edge of double-patterning limit `[1×: SemiAnalysis STEEL]` |
| M3 | 44 nm `[1×: SemiAnalysis STEEL]` | 40 nm `[est.]` (N+3 10% larger) | — | — |
| M4–M6 | 80–82 nm `[1×: SemiAnalysis STEEL]` | — | — | semi-global `[1×: SemiAnalysis STEEL]` |
| M7–M10 | 128 nm `[1×: SemiAnalysis STEEL]` | — | — | semi-global `[1×: SemiAnalysis STEEL]` |
| M11 / M12 / M13 | 148 / 1920 / 4600 nm `[1×: SemiAnalysis STEEL]` | fewer routing layers (coarse ~850 nm by M9) `[1×: SemiAnalysis STEEL]` | — | top/global metals `[1×: SemiAnalysis STEEL]` |

Fin-patterning integration: a single CD mandrel litho pattern at 128 nm pitch undergoing SAQP produces a die-wide ~32 nm grid (128/4) supporting both logic and SRAM pitch sequencing `[1×: SemiAnalysis STEEL]`. Intel 18A carries the loosest M0 pitches among leading-edge nodes *because* PowerVia moves power routing to the backside, freeing the entire front-side stack for signal routing `[web: semianalysis]`.

### Transistor density and standard-cell architecture

| Metric | SMIC N+3 | TSMC N6 | SMIC N+2 | Intel 18A |
|---|---|---|---|---|
| Bohr transistor density | 113.4 MTr/mm² `[1×: SemiAnalysis STEEL]` | 107.7 MTr/mm² `[1×: SemiAnalysis STEEL]` | — | HD ~184 MTr/mm² `[est.]`; HP 163.6 MTr/mm² `[est.]` |
| Normalized density gap | −38% vs 18A HD `[est.]` | — | — | reference `[est.]` |
| Cell height | 228 nm `[1×: SemiAnalysis STEEL]` | 240 nm (HD) `[1×: SemiAnalysis STEEL]` | 252 nm `[1×: SemiAnalysis STEEL]` | — |
| Contacted gate pitch (CGP) | 57 nm `[1×: SemiAnalysis STEEL]` | 57 nm (HD) `[1×: SemiAnalysis STEEL]` | ~63 nm `[est.]` | — |
| Standard-cell libraries | 1 (2+2 fins only) `[1×: SemiAnalysis STEEL]` | 2 (HD 2+2, HP 3+3) `[web: semianalysis]` | — | HP-heavy `[web: semianalysis]` |
| M1-to-gate ratio | 3:2 `[1×: SemiAnalysis STEEL]` | 1:1 `[web: semianalysis]` | 3:2 `[1×: SemiAnalysis STEEL]` | 1:1 `[web: semianalysis]` |
| M2 track height | 5.7-track `[1×: SemiAnalysis STEEL]` | — | — | — |
| DTCO boosters | fin depopulation + COAG + SDB `[1×: SemiAnalysis STEEL]` | fin depopulation + SDB (no COAG) `[1×: SemiAnalysis STEEL]` | — | PowerVia backside power `[web: semianalysis]` |

### Fin profile (fin-cut cross-section)

| Metric | SMIC N+3 | TSMC N6 |
|---|---|---|
| Fin aspect ratio | ~9.5:1 `[1×: SemiAnalysis STEEL]` | ~7.8:1 `[1×: SemiAnalysis STEEL]` |
| Fin pitch | 30–32 nm `[1×: SemiAnalysis STEEL]` | 34 nm `[1×: SemiAnalysis STEEL]` |
| Top-rounding radius | ~2.0 nm `[1×: SemiAnalysis STEEL]` | ~2.8 nm `[1×: SemiAnalysis STEEL]` |
| Rounding-to-width ratio (lower better) | 0.37 `[1×: SemiAnalysis STEEL]` | 0.44 `[1×: SemiAnalysis STEEL]` |

Absolute single-digit-nanometer values are approximate (few cuts); the robust result is the relative gap — N+3 fins are taller, narrower and less rounded than N6 `[1×: SemiAnalysis STEEL]`.

### SRAM (Kirin 9030, measured + estimated)

| Cell / array | Value | Reference point |
|---|---|---|
| 8T HCC bitcell (measured) | 0.0463 µm² → 21.6 Mib/mm² peak `[1×: SemiAnalysis STEEL]` | dedicated read port, read-disturb removed `[web: semianalysis]` |
| 6T HCC (estimated) | 0.0337 µm² `[est.]` | ~12% larger than 6T HCC on Intel 3 / Intel 4 `[est.]` |
| 6T HDC (estimated) | 0.0260 µm² → 38.5 Mib/mm² peak `[est.]` | near Samsung 7LPP/5LPP, slightly below TSMC N7/N6 `[est.]` |
| SLC 128 KiB array | 25.5 Mib/mm² achieved (66% of peak) `[1×: SemiAnalysis STEEL]` | 18% shrink vs Kirin 9020 `[1×: SemiAnalysis STEEL]` |
| L3 64 KiB array | 23.8 Mib/mm² achieved (62% of peak) `[1×: SemiAnalysis STEEL]` | 0.0210 mm²; ~18–31% smaller than 9020 arrays `[1×: SemiAnalysis STEEL]` |
| Prime L2 32 KiB array | 17.6 Mib/mm² achieved (59% of peak) `[1×: SemiAnalysis STEEL]` | ~17% shrink vs 9020 `[1×: SemiAnalysis STEEL]` |

SRAM scaled ~19% N+2→N+3, close to the logic shrink, but N+2 bitcells were unusually large, so part of the gain is catch-up rather than true scaling `[web: semianalysis]`.

### Performance / efficiency gap (PPA — the competitiveness axis)

| Comparison | Result |
|---|---|
| Kirin 9030 Pro overall | ≈ three-year-old Android flagship; efficiency gap wider than performance gap `[web: semianalysis]` |
| Huawei prime core per-clock | ≈ Arm Cortex-X2 (a 2021 design) `[web: semianalysis]` |
| Apple M1 Firestorm (2020) vs prime | +35% per clock, +57% absolute integer at ~4.5 W `[1×: SemiAnalysis STEEL]` |
| Apple M5 P-core vs prime | +60% per clock, 2.7× faster `[1×: SemiAnalysis STEEL]` |
| Arm C1 Ultra vs prime | +45% per clock, 2× faster `[1×: SemiAnalysis STEEL]` |
| Apple efficiency core vs prime | +20% integer at 1 W vs Huawei prime at 4.5 W `[1×: SemiAnalysis STEEL]` |
| 9030 middle / tiny cores vs 9020 | +17% / +14% per-clock integer `[1×: SemiAnalysis STEEL]` |
| Tiny-core efficiency | +45% integer, +24% FP; middle-core integer efficiency −7% `[1×: SemiAnalysis STEEL]` |
| Maleoon 935 GPU vs 920 | +70% 3DMark WLE, +79% SNL; first Huawei GPU with HW ray tracing `[1×: SemiAnalysis STEEL]` |
| Maleoon 935 vs current flagships | Snapdragon 8 Elite Gen 5 / Dimensity 9500 ~2.4–2.6× faster WLE, ~3.2× SNL `[web: semianalysis]` |
| Rated-clock behavior | cores failed to hold max frequency (thermal/power/stability limits) `[1×: SemiAnalysis STEEL]` |
| Prime core clock | 2.5 → 2.75 GHz (+10%); core −7.6% (−21% ex-L2), L2 1→2 MiB `[1×: SemiAnalysis STEEL]` |

### Roadmap and 3D-stacking (τ scaling / LogicFolding)

| Node / step | Projection | Reference |
|---|---|---|
| N+4 (theoretical, planar) | cell height 198 nm, CGP 54 nm, 137.8 MTr/mm² `[est.]` | ≈ TSMC N5 / Samsung SF4 `[est.]` |
| N+5 (theoretical, backside contacts) | cell height 170 nm, CGP 53 nm, 163.6 MTr/mm² `[est.]` | ≈ Intel 18A HP library `[est.]` |
| CGP practical floor | ~48 nm even with EUV `[web: semianalysis]` | — |
| Huawei prime-core frequency | 2.75 GHz (2026) → ~5 GHz (2031 target) `[web: semianalysis]` | LogicFolding 3D stacking `[web: semianalysis]` |
| Huawei 3D density (per-package-footprint) | 114 → 215 (2030) → 295 MTr/mm² (2031) `[est.]` | NOT like-for-like (stacked active layers) `[web: semianalysis]` |
| AMD MI450X (N2/N3P) under same method | 460.2 MTr/mm² in 2026 `[est.]` | vs Huawei 295 in 2031 `[est.]` |

Each roadmap step is individually plausible but cumulatively harder than N+2→N+3 — likely longer, costlier, less process margin `[web: semianalysis]`. N+5 reaches 18A-HP density "through a much more expensive route," not cost-competitively `[web: semianalysis]`.

### Process-control tells and memory/packaging

- M0 trenches visibly more re-entrant (narrower at bottom) than M1/M2, with a bright barrier-rich foot at the etch-stop `[1×: SemiAnalysis STEEL]`.
- M0 integration deviation vs the big-three foundries: a blowout of the liner bottom at the alumina (AlOₓ) etch-stop layer `[1×: SemiAnalysis STEEL]`.
- TaN barrier appears oxidized; tungsten plugs on cobalt S/D contacts; eSiGe PMOS strain (industry standard since 45 nm; SMIC has run IBM-licensed 40/45 nm since ~2008) `[1×: SemiAnalysis STEEL]`.
- Cross-sections flag challenges in line-edge-roughness control, selective caps, and possibly doping modules; EUV is the obvious tooling gap `[web: semianalysis]`.
- Memory: Kirin 9030 Pro carries 12 GB Samsung LPDDR5X-9600 on Samsung 1a; 16 GB Pro Max ships with either CXMT (G4, ~0.3 Gib/mm² ≈ others' 1z) or Samsung DRAM `[1×: SemiAnalysis STEEL]`.
- Packaging: all-organic iPoP (integrated package-on-package) — ABF build-up over BT core, organic RDL interposer, no silicon interposer; CTE kept close to PCB, avoiding silicon-interposer cost the bandwidth does not need `[web: semianalysis]`.

## Contradiction Check

The teardown bears directly on two open theses; both readings anchor to specific sections.

**[[Theses/INTC - Intel]] — §Industry Context → "Yield trajectory and the structural second-source role," and the §Key Non-consensus Insights framing of 18A as a genuine leading-edge process.** The source corrects a specific potential misread without weakening the bear case. The naive inference — that Intel 18A's 36 nm shipping M0 makes it uncompetitive versus SMIC's 32.5 nm — is exactly backwards: 18A *supports* a 32 nm M0 (tighter than SMIC), ships 36 nm in Panther Lake only because of heavy HP-library use, and carries the loosest M0 among leading-edge nodes *by design* because PowerVia backside power delivery frees the front-side stack for signal routing. On the normalized axis, 18A HD is ~184 MTr/mm² against SMIC N+3's 114 (18A ~61% denser), and SMIC does not reach 18A-HP density (163.6) even in a *theoretical* N+5 that requires backside contacts at a much higher cost, dated implicitly to 2028+. So on raw process capability 18A leads SMIC by roughly five effective generations — a mild positive for the "18A is a real leading-edge node" leg, which the thesis already frames correctly (High-NA EUV deployed ahead of TSMC; 14A "parallel to TSMC A14"). Critically, this does *not* move conviction: the INTC bear case rests on 18A *yield-cost economics* (~65–75% entry yield, ~10 pts behind mature N2), the IDM 2.0 structural conflict, AMD server-share compounding (46.2% Q1 revenue), and a ~102–145x forward multiple — none of which a metal-pitch teardown touches. SMIC is not an Intel Foundry competitor: it is a walled Chinese-domestic parallel market ([[Industry - Semiconductors]] #16), so N+3 progress neither adds nor removes an IFS customer. Net: immaterial to conviction (stays low); useful as a guard against a bull mis-argument that "18A loose M0 = weak node."

**[[Theses/TSM - Taiwan Semiconductor]] — §Industry Context → Competitive landscape (the SMIC row: "7 nm via DUV multi-patterning, ~1% Chinese only, blocked from EUV, serves Huawei"), §Outstanding Questions #6 (Huawei Ascend + SMIC reducing TSMC China TAM), Insight #2 (silicon shield / structural concentration), and the ## Mental Models entry that "Western leading-edge concentration in TSM is structurally higher than aggregate share suggests."** N+3's density-parity-at-a-cost **strengthens** that structural-concentration view, and both legs of the evidence point the same way. Leg one: N+3 is *good enough* to self-supply China's domestic phone, inference, networking and security-sensitive tier — permanently walling off that demand bucket as the independent parallel market of Semis #16, accelerated by SMIC licensing N+2/N+3 to Hua Hong and by Cambricon/T-Head/ByteDance uptake (the exact China-TAM-erosion vector of Outstanding Q6, already in TSM's base case but now with a concrete diffusion mechanism). Leg two: N+3 is *not good enough* to contest the leading edge — a 2019 N6-equivalent with no EUV, no backside power, a prime core at 2021 Cortex-X2 per-clock, SRAM 6T HCC ~12% larger than Intel 3/4, and a DUV multi-patterning ceiling that makes N+4/N+5 cumulatively harder — so no credible Chinese second source emerges for the N3/N2/A16 demand that NVDA, Apple, AMD and the hyperscaler ASIC set route exclusively through TSMC. Both legs raise TSM's true monopoly over *contestable* (non-Chinese) leading-edge demand above what the ~92% share optically implies, because the ~1% "SMIC" slice is non-contestable parallel-market share, not leading-edge competition. This reinforces the durability-of-monopoly core of the high-conviction thesis rather than the near-term-priced-in debate. It does not fire any LOW/CLOSE trigger: SMIC is not a "credible leading-edge second source" in the sense the Intel-18A LOW trigger contemplates.

**[[Generalist - Overview]] [G-10] (base rates / outside view) — held as a hypothesis to test.** The "32.5 nm < 36 nm, China caught up" narrative is the canonical inside-view extrapolation from a single flattering datapoint; the reference-class read (DUV-only nodes run five-plus generations behind on PPA, hit a multi-patterning cost wall, and face cumulative N+4/N+5 difficulty) is the base rate the headline must beat and does not. The discipline the teardown itself enforces — normalize density, price the patterning, decompose PPA — is the outside-view correction applied at the engineering layer.

**[[Industry - Semiconductors]] #4 (tech-curve race) and #2 (qualification gate) — hypotheses.** #2: metal pitch is the cherry-picked optic; the real gate is yield and cost per good die and performance-per-watt, on all of which SMIC trails — the teardown is a physics-level instance of the "quality differentiation hidden behind a headline number" edge. #4: density parity does not imply cost/efficiency/yield parity, and the laggard pays in process control — visible here as re-entrant M0 trenches, a liner blowout at the etch-stop, an oxidized TaN barrier, cores that miss rated clocks, and LER/selective-cap/doping challenges. The open question #4 poses: whether SMIC's "aggressive tech upgrade without demand-calibrated economics" is the bankruptcy-risk end of the race (too aggressive, sub-scale margins) or a state-subsidized exception where normal capital-cycle economics are suspended — a distinction that determines whether SMIC ever becomes a cost-competitive threat or remains a strategically-necessary but structurally-uneconomic national champion. Cross-reference: [[Research/2026-04-19 - Huawei Ascend Roadmap - news]] and [[Sectors/Semiconductor Foundries]] for the Chinese-domestic-stack context.

## Source Excerpts

- "The headline is true, but an incomplete cherry picked metric. N+3 reaches the density of TSMC N6 through aggressive DUV multi-patterning and design-technology co-optimization (DTCO), but it pays for that in complexity, efficiency and process control."
- "SMIC N+3 uses a 32.5 nm local metal pitch. That is smaller than the 36 nm M0 pitch on Intel 18A in Panther Lake. However, this does not mean that SMIC has a better process than Intel 18A or TSMC N3P. M0 is a local intra-cell routing layer."
- "Intel 18A supports an M0 pitch of 32 nm, although Panther Lake has only shipped with a looser 36 nm pitch… Among leading-edge nodes, 18A has the loosest M0 pitches due to PowerVia. With power routing moving to the backside, congestion is reduced, and the entire front-side metal stack can be used for signal routing."
- "On a normalized Bohr-density basis, SMIC N+3 is ~114 MTr/mm², 38% less than Intel 18A's HD library."
- "N+3 matches TSMC N6, but N6 is several generations old. Apple and Qualcomm build on N4 and N3P, which are denser and sit on a better voltage-frequency curve, giving them a larger transistor budget and more performance per watt."
- "China is not closing the gap with Intel, Samsung and TSMC. The teardown shows the opposite in several places: no EUV, no backside power, higher process complexity, and visible trade-offs. But China is still advancing. If domestic chips become good enough for phones, inference, networking and security-sensitive workloads, they can matter strategically without matching TSMC at the leading edge."
- "SMIC is licensing its N+2 and N+3 processes to HLMC/Hua Hong at the government's direction rather than by choice… Sanctions aimed at SMIC alone become less effective once the manufacturing knowledge has spread to other fabs and design houses."
