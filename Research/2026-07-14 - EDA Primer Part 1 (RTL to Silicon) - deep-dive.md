---
publish: false
date: 2026-07-14
tags: [research, semiconductors, EDA, SNPS, CDNS]
sector: EDA & Chip Design Software
source: 'https://substack.com/home/post/p-190867437'
source_type: deep-dive
---

# EDA Primer Part 1: From RTL to Silicon (SemiAnalysis)

## Thesis Delta

Consensus prices the EDA vendors as a mid-single-digit "semiconductor software" category tethered to industry R&D; this primer shows the RTL-to-silicon path is a 13-leg relay in which EDA is the *only* non-substitutable connective tissue, and the binding constraint on AI silicon is migrating from lithography physics to design-and-verification **labor**. Verification alone consumes up to 70% of project effort, chip complexity compounds ~50%/yr against ~20%/yr design-productivity gains, and one-third of the US semiconductor workforce is over 55. The non-consensus inversion: the "engineer shortage" that reads as a throughput bear signal for fabless and foundry names is a structural forcing function that *pulls* automation into precisely the highest-margin corners of the toolchain (emulation hardware, simulators, formal, synthesis) — the toolchain owners monetise the bottleneck that constrains everyone above them. Investable names implicated but entirely uncovered in this vault: **Synopsys, Cadence, Siemens EDA**. This is Part 1 of 3 (technical flow); the business/market case is [[Research/2026-07-14 - EDA Market Primer Part 2 (Big-3 Dynamics) - deep-dive]].

## Summary

This is SemiAnalysis's technical primer (Gerald Wong, May 2026) tracing the full chip-design flow from RTL code to packaged, volume silicon. Its argument is structural, not a stock call: modern chips are built through a 13-stage waterfall — planning, architecture, RTL design, RTL verification, RTL freeze, parallel firmware/software, physical design, signoff, tapeout, fabrication, post-silicon validation, system integration, production — and every stage where human intent is translated toward manufacturable geometry runs on EDA software, "without which no chip designed after the mid-1980s would exist." The load-bearing claim for investors is that each stage is served by one to three dominant tools, and those tools are almost always from Synopsys, Cadence, or Siemens EDA. The flow is not a linear handoff but a mesh of feedback loops (architecture bugs force RTL changes; timing failures in physical design send engineers back to re-optimise), which is *why* EDA exists — no human team can track the dependency graph by hand.

The historical arc explains why the business model looks the way it does, and why the moat is structural rather than a matter of current product lead. Chip layout began as hand-cut Rubylith film under X-Acto knives (the process through the Intel 8080); Calma's Graphic Design System (1971) and GDS II (1978) digitised it — and remarkably GDSII remains the dominant mask-data interchange format nearly five decades later, alongside its successor OASIS. The industry proper was born in 1981 with Daisy, Mentor and Valid ("DMV"), which brought computer-aided engineering to the front end on dedicated workstations. But the decisive breakthrough was Synopsys's Design Compiler (1987), the first commercial logic-synthesis tool: by abstracting away manual gate placement it "unlocked a multi-million-fold increase in design complexity" that produced today's multi-billion-transistor SoCs. Synopsys (founded 1986, Aart de Geus, ex-GE research), Cadence (1988, the SDA+ECAD merger) and Mentor (acquired by Siemens 2017 for $4.5B, rebranded Siemens EDA 2021) are the survivors. The lesson for the moat: EDA's value was created the moment human gate-placement became economically impossible — "manual design stopped being possible at 65nm" — and it has compounded at every node since, because each new process node adds design rules and verification corners faster than human productivity can absorb them.

The primer's central mechanism is a "design bottleneck" formed by a trifecta: exploding complexity (the AMD MI455X packs 320 billion transistors across 12 logic dies on 2nm/3nm with hybrid bonding, HBM4 and 224G SerDes), compressed timelines (validation cycles crushed from years to months, where "even a 3 month delay means billions"), and a shrinking talent base (EE graduates dwindling while a third of the workforce nears retirement). Verification is the fulcrum of that bottleneck: now up to 70% of total project effort, with verification engineers the fastest-growing job category and the design-engineer-to-verification-engineer ratio chronically worse than the 1:4 ideal (some houses run 2:1 the wrong way). Respins are the tail risk that justifies verification spend — a single advanced mask set costs tens of millions, A0 silicon "rarely goes into production," and every stepping adds months to the schedule.

The most investable structural insight is *where* pricing power concentrates in the flow. The standard-cell library plus Process Design Kit (PDK) is "the foundry's main commercial interface with chip designers"; porting a design to a new foundry means migrating the cell library first, which "triggers the most re-work across the entire tool flow." PDK access is a rigid four-tier NDA system (Tier 1 anchor/JDA customers like Apple, NVIDIA and AMD get access 3+ years pre-production and can bankroll process features; EDA and IP vendors are Tier 2). And the sequential dependency itself is the lock-in: changing one tool re-runs everything downstream. The primer closes on the AI angle it will develop in Part 3 — Design Space Exploration is "easily verifiable with assignable reward functions for PPA," making it an ideal reinforcement-learning target already attacked by Synopsys DSO.ai and internal fabless efforts — plus foundry-side EDA (Synopsys Sentaurus/Mystic/QuantumATK) that designs the *next* process node in software before silicon exists.

On methodology, the primer is a compact reference for *why* verification resists automation and *where* the compute goes. RTL verification splits into two complementary paths: constrained-random simulation structured in UVM (sequencer → driver → monitor → scoreboard), which generates millions of randomised inputs within legal constraints to surface corner cases that directed tests miss, and formal verification (JasperGold, VC Formal) that uses SAT solvers and model checkers to *prove* SystemVerilog-Assertion properties exhaustively but hits capacity limits on wide datapaths. Completion is gated by coverage — code coverage (line/branch/toggle/FSM) and functional coverage (covergroups) — where "90% of test cases complete quickly" but the last 10% of coverage closure "takes serious effort, sometimes requiring weeks." Physical design is then a multi-loop optimisation (floorplanning → power planning → placement → routing → clock-tree synthesis → DFT), each pass re-running timing optimisation via buffer insertion, gate resizing, intentional useful-skew, logic remapping and hold-fixing. Signoff proves manufacturability across every PVT corner (DRC/LVS/ERC/STA/power). The candid "ugly reality" section admits the sacred RTL Freeze is in practice "just to tell DE to stop adding new features" — RTL ships to physical design still partially broken, with re-programmable software registers deliberately inserted so problematic features can be bypassed to hit hard deadlines, at a hidden PPA cost. That gap between the idealised waterfall and the overlapping reality is itself the demand for "Shift Left" tooling the incumbents sell.

## Framework / Mental Model — The 13-Stage Waterfall and its Tool-by-Stage Lock-in Map

The reusable framework is a stage → function → dominant-tool → vendor map. Its analytical value is that switching any single tool forces re-qualification of every downstream stage, so market share at each stage is defended not by per-tool merit alone but by the cost of re-running the chain. Apply it to any "can a challenger displace vendor X?" question by asking which downstream stages a switch would invalidate.

| # | Stage | Core function | Dominant tool(s) | Vendor |
|---|---|---|---|---|
| 1 | Planning | Set PPACt targets (perf/power/area/cost/time-to-market) | (internal / DSE) | — |
| 2 | Architecture | Block diagrams, NoC bandwidth, Design Space Exploration | DSO.ai (AI DSE) | Synopsys |
| 3 | RTL Design | Write SystemVerilog; lint | VC SpyGlass (lint) | Synopsys |
| 4 | RTL Verification | Constrained-random sim (UVM) + formal proof | VCS / Xcelium / Questa (sim); JasperGold / VC Formal (formal) | SNPS / CDNS / Siemens |
| 5 | RTL Freeze | Coverage closure; lock netlist; ECO gate | (coverage tools) | — |
| 6 | FW/SW (parallel) | Pre-silicon emulation at ~50MHz, 1000× SW sim | ZeBu (23B gates) / Palladium (48B gates) | SNPS / CDNS |
| 7 | Physical Design | Synthesis → place → route → CTS → DFT | Design Compiler / Fusion Compiler / Genus (synth); IC Compiler II / Innovus (P&R) | SNPS / CDNS |
| — | Equivalence check | Prove RTL ≡ gate netlist at every transform | Formality / Conformal LEC | SNPS / CDNS |
| 8 | Signoff | DRC / LVS / ERC / STA / power | IC Validator / Pegasus / Calibre (PV); PrimeTime / Tempus (STA); RedHawk-SC / Voltus (power) | SNPS / CDNS / **Siemens (Calibre)** |
| 9 | Tapeout | Export GDSII/OASIS; OPC mask synthesis | (mask/OPC) | — |
| 10 | Fabrication & packaging | 8–12 wk wafers; chiplets, CoWoS, 3D stack | — | (foundry) |
| 11 | Post-silicon validation | ATE test, probe cards, ATPG vectors, burn-in | TestMAX / Avalon (FA); Teradyne/Advantest ATE | Synopsys / ATE OEMs |
| 12 | System integration | Reference boards, SLT, driver/BIOS qual | (RVP) | — |
| 13 | Production | Yield ramp, binning, CIP with foundry | — | — |

Sub-frameworks the primer establishes:

- **PDK version milestones** — the foundry's process encoded for EDA tools, maturing 0.1/0.3 (TCAD-only, JDA anchors, ~2yr pre-production) → 0.5 (first real-silicon test data, real design begins) → 0.9 (full PVT-corner characterisation) → 1.0 (production-ready). Intel 18A walked this exact ladder: PDK 0.3 (Sep 2022) → 0.5 (Mar 2023) → 0.9 (Sep 2023) → 1.0 (Jul 2024) → Panther Lake launch (Jan 2026).
- **PDK access tiers** — Tier 1 anchor/JDA (Apple, NVIDIA, AMD; 3+ yrs early, shape design rules); Tier 2 EDA/IP partners (SNPS/CDNS/Siemens/Arm; months of lead time to qualify libraries); Tier 3 standard customers (rules as-is); Tier 4 academic (subsets, years late). Even Tier 1 never sees the physical recipe — the PDK is the abstraction layer that makes the fabless model possible.
- **Standard-cell library as the commercial interface** — advanced nodes (TSMC N2) hold tens of thousands of cells, multiple Vt options (TSMC 6 vs Intel 18A's 4, of which Intel used 3 — a concrete PPA-competitiveness gap 18AP is said to fix), and mixed cell-height schemes (FinFlex/NanoFlex) that make DTCO near-mandatory.
- **Steppings / respin economics** — Major stepping (A0→B0): full DE→DV→PV re-run, new coverage closure, full mask-set update. Minor (A0→A1): metal-layer-only change, circuit-edited via Focused Ion Beam. This is the cost function verification spend is bought to avoid.
- **DTCO / STCO** — Design-Technology Co-Optimisation chains Sentaurus TCAD → Mystic (PDK) → SiliconSmart/HSPICE → IC Compiler II/StarRC/PrimeTime into a feedback loop; custom cell libraries push PPA ~15% over standard (Apple/NVIDIA/AMD run dedicated foundry teams for this). STCO extends it to chiplet/package co-design (Intel Ponte Vecchio: 47 dies, 5 nodes, EMIB + Foveros).

### Verification methodology (why the bottleneck resists automation)

UVM (Universal Verification Methodology, Accellera-standardised 2011; before it every team rolled its own testbench) defines four reusable components: **Sequencer** (generates transaction sequences — where test scenarios are defined), **Driver** (converts abstract transactions into pin-level signal wiggles), **Monitor** (passively observes interfaces and reconstructs transactions), **Scoreboard** (compares a reference model's expected outputs against the design's actual outputs; any mismatch is a bug). This drives **constrained-random verification**: rather than hand-write directed tests, engineers define legal address ranges, packet formats and protocol rules, and the tool randomly generates millions of input combinations within those bounds — more effective at fault detection than directed testing, at high compute cost. **Formal verification** (JasperGold/Cadence, VC Formal/Synopsys) is the complement: SAT/model-checking engines prove a property holds for all inputs and state sequences (or emit a counterexample), excelling at protocol compliance, control-logic correctness and security properties, but limited by scalability on datapath-heavy wide-bus designs. FV proves critical properties exhaustively on targeted blocks; simulation covers the full chip at statistical confidence. Completion is measured by coverage → coverage closure → RTL Freeze; post-freeze changes require an Engineering Change Order (ECO) plus equivalence checking.

### Physical design optimisation loop (Stage 7)

Standard-cell physics: seven basic gates (INV, NAND, AND, OR, NOR, XOR, XNOR) → complex cells (AOI, OAI, registers, muxes, D-flip-flops, full adders) → special-purpose cells (IO pad, tap, filler, decap, tie-high/low, power/clock-gate, level shifters) plus SRAM macro compilers. Each gate ships in multiple drive strengths and up to 6 threshold-voltage (Vt) options — higher drive / lower Vt switch faster but leak more. **Process corners** the tools must close across: TT (nominal), FF (both transistor types fast), SS (both slow), FS/SF (skewed NMOS vs PMOS), voltage ±10% around nominal (e.g. 0.75V), temperature 0–105°C consumer / −40–125°C automotive; the design must meet timing at the slow corner and stay within power at the leaky corner. **Metal interconnect** stack: M0/M1 in-cell (thin, high-resistance) → M3–M5 block-level → thick top metals for the power-distribution network and global clock; layer count runs 10 (low-cost mobile SoC) to 19 (high-performance AI processor); backside power delivery (Intel 18A) segregates power and signal lines, cutting parasitics. The PnR flow — floorplanning (macros, IO pins) → power planning (PDN mesh, multi-voltage domains, power gating, minimise IR drop) → placement (global optimises wirelength/congestion, detailed legalises to grid rows) → routing → clock-tree synthesis (minimise skew) → DFT (scan chains, MBIST, ATPG) — iterates timing optimisation after every major step.

### PDK contents & signoff mechanics (Stage 8)

The PDK encodes the foundry process in standard file formats: **LEF** (physical cell geometry — pins, blockages, boundary), **LIB/Liberty** (timing arcs, power tables, noise data — one per PVT corner), **SPICE** models (analog transistor behavior — Vt, leakage, capacitance), **P-cells** (parameterised analog cells), parasitic-extraction decks (RC-max/RC-min), and the **DRM** (Design Rule Manual — thousands of geometric rules, >1,000 pages at advanced nodes). Signoff clears DRC + LVS + ERC (via IC Validator/Pegasus/**Calibre**), STA (PrimeTime/Tempus, using MCMM multi-corner-multi-mode across PVT + DVFS curves), and power signoff (IR-drop + electromigration via RedHawk-SC/Voltus). ECO flows split into functional ECO (repurpose pre-placed spare cells; only a lowest-metal mask change) vs timing ECO (resize/remap cells; may force a full mask-set change) — the mechanic that makes late bug-fixes cheap or catastrophic.

### The overlapping-waterfall reality & the second (foundry) market

The idealised waterfall overlaps heavily in practice: DV is still writing tests while physical design proceeds on partially-broken RTL; the ideal DE:DV ratio is 1:4 but no company achieves it (some run 2:1 the wrong way, forcing design engineers to self-verify). Licensed IP is a **black box** — NVIDIA×MediaTek GB10 and ARM cores expose only interfaces (AMBA CHI), so verification engineers cannot isolate whether an upstream timing conflict is a design fault or a testbench error, a problem compressed cycles worsen. Google's Jeff Dean disclosed that TPUs pay a small area penalty to embed structures *predicted* to become useful over a chip's 5-year life (Google won't say how often the prediction pays off or how many dormant circuits remain) — a concrete illustration of the hardware-software prediction gap that motivates re-programmable design. Separately, EDA runs a *second* market inside the foundry: **Sentaurus** TCAD (Process engine simulates fabrication steps → 3D device; Device engine simulates I-V/leakage/breakdown), **Mystic** extracting compact BSIM-CMG SPICE models to seed PDK 0.1, and **QuantumATK** doing atomic-scale DFT/NEGF materials modelling (work-function metallisation, Vt tuning) — Synopsys tools designing the transistor before any silicon exists.

## Evidence

Structural bottleneck metrics:

| Metric | Value | Source attribution |
|---|---|---|
| Chip-complexity growth | ~50%/yr | Siemens |
| Design-productivity growth | ~20%/yr | Siemens |
| Verification share of project effort | up to 70% | SemiAnalysis |
| US semi workforce over 55 | one-third | SemiAnalysis |
| Ideal DE:DV ratio (rarely achieved) | 1:4 | SemiAnalysis |
| Custom RTL in a modern SoC | only ~20–30% (rest licensed/reused IP) | SemiAnalysis |
| Full-regression compute per run | thousands of CPU core-hours | SemiAnalysis |
| Single chip's data footprint | multiple petabytes | SemiAnalysis |

Reference-design complexity (the demand driver): AMD MI455X = 320B transistors, 12 logic dies, 2nm+3nm, hybrid bonding, HBM4, 224G SerDes.

Emulation platform arms race (Stage 6):

| Platform | Vendor | Capacity | Note |
|---|---|---|---|
| ZeBu-200 | Synopsys | up to 23B gates | 2× runtime vs predecessor; Xilinx Versal VP1902 FPGAs |
| Palladium Z3 | Cadence | up to 48B gates | 1.5× vs Z2; custom Cadence emulation processor, liquid-cooled |
| Protium X3 | Cadence | — | FPGA prototyping |

Simulator ubiquity order (Stage 4): VCS (Synopsys, market leader) > Xcelium (Cadence) > Questa (Siemens). Most large houses license ≥2. Formal: JasperGold (Cadence) and VC Formal (Synopsys).

Physical-verification signoff triopoly (Stage 8), each foundry-entrenched: IC Validator (Synopsys), Pegasus (Cadence), **Calibre (Siemens)**. STA: PrimeTime (Synopsys), Tempus (Cadence). Power: RedHawk-SC (Synopsys), Voltus (Cadence).

Compute mix in the design loop: FPGAs for emulation/prototyping; **high-per-core server CPUs** for the branchy, dependency-heavy RTL/netlist/PV simulation that dominates verification. AWS runs ~1 million Graviton cores internally to design future Graviton/Trainium/Nitro — a live datapoint that leading-edge chip design is itself a large, recurring CPU-demand engine.

Fab/respin economics: advanced mask set = tens of millions; A0 rarely reaches production; wafer fab 8–12 weeks (compressible via priced "Hot Lots"); HTOL burn-in 72–168h (up to 1000h for aero/auto).

Coverage taxonomy (the RTL Freeze gate):

| Type | Metric | Question answered |
|---|---|---|
| Code | Line / Branch / Toggle / FSM | Has every line executed, branch taken, signal toggled, state visited? |
| Functional | Covergroups | Did we test the scenarios we care about (e.g. concurrent same-address writes, FIFO-full + interrupt)? |

Standard-cell / PDK depth at advanced nodes:

| Item | Datapoint |
|---|---|
| Cells in a TSMC N2 library | tens of thousands |
| Vt options | 6 (TSMC) vs 4 (Intel 18A, used 3) |
| DRM length | >1,000 pages at advanced nodes |
| Metal layers | 10 (mobile SoC) → 19 (HPC AI) |
| Cell-height schemes | TSMC N3 FinFlex, N2 NanoFlex (mixed heights) |
| Apple library mix | 3-2 FinFlex (high-perf CPU) + 2-1 FinFlex (dense/low-power) |

IP-integration economics: only ~20–30% of a modern SoC's RTL is custom; the rest is licensed/reused IP (Arm cores/GPU; Synopsys DesignWare USB/PCIe/DDR controllers; Broadcom high-speed IO). Licensing a PCIe Gen6 controller costs "a fraction" of a dedicated in-house I/O + verification team and ships pre-verified against the PCI-SIG spec — the make-vs-buy that seeds the EDA vendors' $3B+ IP business (developed in Part 2).

Open-source reference points (the capability floor): SkyWater SKY130 (Google-funded, 130nm, Apache-2.0, full RTL-to-GDSII), OpenROAD (P&R), OpenLane (flow orchestration) — usable for education and 130nm tape-outs, ~20-year-old process, and Google has since pulled MPW-shuttle funding. This bounds how far open-source substitutes reach vs the leading edge.

Design economics & the productivity gap (why the bottleneck monetises upward): the primer's core quantitative claim is a scissors — chip complexity compounding ~50%/yr against design-productivity gains of ~20%/yr — which means every new generation demands *exponentially* more engineering effort, compute, and automation per unit of silicon. That gap is the demand curve for EDA. It shows up three ways. First in *headcount*: verification engineers are the fastest-growing role in chip development and "the industry still cannot hire them fast enough," while a third of the US workforce nears retirement and EE enrolment lags (even Apple's New Silicon Initiative "barely moves the needle"). Second in *compute*: a full regression can burn thousands of CPU core-hours per run, on-prem verification farms are "usually insufficient," and teams burst to AWS/Azure before tapeout — the reason CPUs (high per-core performance for branchy, dependency-heavy simulation) dominate the design stack while FPGAs handle emulation/prototyping. Third in *capital-at-risk*: after "hundreds of millions of dollars on a new SoC design, there is no guarantee the chip will work," A0 "rarely goes into production," and each advanced mask respin costs tens of millions plus months of schedule. The ROI of verification and emulation spend is therefore insurance against a far larger loss — the structural reason the highest-margin EDA products (emulation hardware, simulators, formal) grow into the bottleneck rather than being competed away by it. The AMD MI455X (320B transistors, 12 dies, 2nm/3nm, hybrid bonding, HBM4, 224G SerDes) is the concrete embodiment: "designing something at this scale is not a matter of hiring more engineers or buying more verification servers — it tests a company's tooling, methodology, and human-capital organisation."

Post-silicon validation and test (Stages 11–13) is where EDA re-enters after fabrication and where a distinct equipment ecosystem sits. Automatic Test Equipment (ATE) from Teradyne and Advantest applies the thousands of test vectors that ATPG tools generated during design; JTAG interfaces provide debug access to errata; large breakout Probe Cards isolate each package pin for oscilloscope-level signal-integrity checks. Synopsys spans this with its TestMAX family (ATPG, yield diagnosis, DFT, test-program management) and Avalon failure-analysis (mapping a defect back to the schematic gate/wire). Reliability qualification runs HTOL burn-in (72–168h, up to 1,000h for aero/auto per JEDEC JESD47) to weed out infant-mortality parts on the Bathtub Curve. Speed-binning and yield-harvesting then convert manufacturing variability into a product mix — Intel's i5/i7/i9 tiers, and NVIDIA GPUs "almost never have all SMs enabled due to yield harvesting." The takeaway for the toolchain thesis: EDA's touchpoints bracket the entire lifecycle (design → signoff → test-pattern generation → failure analysis → yield learning that feeds the next PDK), not just the front-end design window — which is why the design-start / tape-out volume at leading-edge fabs is a better leading indicator of EDA revenue than seat counts.

## Contradiction Check

Foundational primer — its investment signal *supports* an (uncovered) EDA long and reinforces existing semi convictions rather than challenging any:

- **Reinforces [[Industry - Semiconductors]] #2(iii)** — the note already names the "EDA triopoly" as a design-lock-in / software-dependency qualification-gate monopoly; this primer supplies the *mechanism* (sequential-dependency lock-in: switching one stage's tool re-runs every downstream stage; standard-cell-library migration triggers whole-flow rework). Held as hypothesis to test, not verdict.
- **[[Theses/TSM - Taiwan Semiconductor]] §Industry Context / moat** — supports the ecosystem-lock-in thesis: the PDK + standard-cell library is "the foundry's main commercial interface," co-developed with SNPS/CDNS ~24 months pre-production; foundry↔EDA is a mutually reinforcing moat, not two separate ones. Bears on TSM's durability, not its price.
- **[[Theses/INTC - Intel]] §Bear Case / Industry Context** — concrete design-competitiveness datapoints: Intel 18A shipped with only 4 Vt options (used 3) vs TSMC's 6, hurting pareto-optimal PPA (18AP said to fix); the 18A PDK ladder (0.3 Sep-2022 → 1.0 Jul-2024 → Panther Lake Jan-2026) times Intel's external-foundry readiness. Marginally negative on 18A external-customer competitiveness; watch in Part 2's Intel-Foundry-EDA-mention data.
- **[[Theses/AMD - Advanced Micro Devices]] / [[Theses/NVDA - Nvidia]] §Bull/Industry Context** — MI455X (320B transistors, 12 dies, STCO-dependent) and NVIDIA yield-harvesting binning illustrate the design-complexity → EDA-intensity link; weak-support for the design-velocity moat, primary signal flows to the EDA vendors.
- **Honest low-signal note**: Part 1 confirms priors (EDA is entrenched, verification is the bottleneck) and challenges no existing conviction. Its unique contribution is locating the verification/engineer-shortage forcing function; the actionable delta lands in Part 2.

Mental-model triggers fired (for `/sync` to merge into the relevant `## Mental Models` sections, as hypotheses to test):
- Value Layer Monopoly · *locate-the-layer / interface-standard control* — EDA occupies the foundry-certified chip-design toolchain layer; sequential-dependency + cell-library migration is the switching-cost mechanism.
- Industry-Semi #2(iii) · *design lock-in via software dependency* — EDA triopoly; primer supplies the flow-level mechanism.
- Automation & AI-Readiness §6 semi overlay · *design/EDA/verification is data-rich and automatable* — DSE as an RL target (assignable PPA reward functions); design-productivity gap forces AI-tool adoption owned by incumbents.

## Source Excerpts

- "**Verification**, the process of proving a design does exactly what it should before committing it to silicon, now consumes up to 70% of total project effort."
- "The semiconductor industry's ability to keep building more powerful chips depends not on physics or lithography alone, but on **EDA** software… Without EDA, no chip designed after the mid-1980s would exist."
- "The standard cell library is the foundry's main commercial interface with chip designers… When a fabless company 'ports' a design to a new foundry, migrating the standard cell library is the first and most impactful step, and the one that triggers the most re-work across the entire tool flow."
- "AWS deploys 1 million Graviton cores internally to run EDA tools to design future Graviton, Trainium and Nitro chips."
- "Going forward, this step has increasingly been accelerated with AI, as the task is easily verifiable with assignable reward functions for PPA in a multi-dimensional input space."
- On the productivity scissors that is the whole demand curve: "While chip complexity grows at roughly 50% per year… design productivity improves only about 20% each year. This design productivity gap means every new generation of silicon demands exponentially more engineering effort, more compute, and more sophisticated automation."
- On why verification is the underrated fulcrum: "Designing a chip is easy. Knowing your design works with all possible scenarios is hard."
