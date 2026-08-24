---
publish: false
date: 2026-08-18
tags: [research, Compute, Foundries, Memory, Packaging, NVDA, TSM, BESI, 000660, SNDK]
sector: Compute & AI Compute Accelerators
ticker: NVDA
source: 'https://bepresearch.substack.com/p/the-tax-dodge-qualcomms-133-tbs-isnt'
source_type: news
propagated_to: [NVDA, TSM, BESI, 000660, SNDK]

---

# The Tax Dodge: Qualcomm's 133 TB/s Isn't What You Think — BEP Research

## Thesis Delta

Consensus still prices two trades as one: [[Theses/TSM - Taiwan Semiconductor]] Insight #1 treats the large-interposer / CoWoS scarcity premium as a $10B+ separable annuity (sold-out, +20% NVDA pre-book, 130K wpm 2027 target) and [[Theses/000660 - SK Hynix]] prices SK Hynix as an HBM-share/process story whose mix-shift risk is Samsung catching Rubin, not a customer routing around the cube. This 18 August 2026 BEP Research free note (Rick Xie + Ben Pouladian; second in the memory series after *The Bandwidth Tax*) implies the opposite map. Qualcomm HBC is a named architecture that stacks the accelerator *under* DRAM, connected by TSVs, and claims the silicon interposer is no longer needed — 133 TB/s, 6× bandwidth/W vs HBM, 200× capacity/W vs SRAM, 4–8× decode perf/W, AI250 2027 — but Rick's engineering read is that those headline numbers are unproven and the base case is a niche decode/offload tier. What BEP is actually underwriting is narrower: the packaging premium is currently priced as though nobody is trying to route around it, and that is no longer true. Consensus assumes/prices CoWoS + HBM packaging scarcity as one durable tax; this source implies the tax migrates (large interposer → DRAM-to-logic hybrid bonding / SoIC / Foveros / [[Theses/BESI - BE Semiconductor Industries]]–EVG–SUSS tools) rather than disappearing, and that the memory oligopoly is *neutral-to-bullish* on the mix-shift. Qualcomm does not need to catch [[Theses/NVDA - Nvidia]] for the detour to reprice the toll road. Conviction-trigger touches (flag only — do not change conviction/status): [[Theses/TSM - Taiwan Semiconductor]] → LOW if "a named production-scale CoWoS-alternative win" is **evidence-touched, not fired** (dir=LOW, watch): HBC is a named interposer-skip architecture, but first silicon is 2027, assembly flow and foundry are undisclosed, BEP is explicitly *not* underwriting HBC working, and the piece itself says CoWoS is sold out regardless. HIGH-reaffirm (FY26 >40% USD + Q3 GM ≥66% + Jan-2027 capex ≥$70B) and CLOSE (blockade / NVDA+AAPL >50% / GM <52%) are not in this piece. [[Theses/000660 - SK Hynix]] HIGH/LOW/CLOSE are Rubin-allocation / Samsung-share / CXMT / Namics handles — HBC mix-shift and the HBF teaser do not fire them. [[Theses/NVDA - Nvidia]], [[Theses/BESI - BE Semiconductor Industries]], and [[Theses/SNDK - SanDisk]] have no registered Conviction Triggers. Live-book conviction/status unchanged: NVDA high/active, TSM high/active, BESI medium/active, 000660 medium/active, SNDK medium/active.

## Summary

BEP Research published this free, citable note on 18 August 2026 (Gmail `1a01501051b76b61`, 21:05 Asia/Shanghai), co-authored with Rui "Rick" Xie. Six weeks after *The Bandwidth Tax* (9 July 2026) argued that the real cost of HBM is levied on the *system* around the stack — interposer, base die, packaging, cooling — Qualcomm's 24 June 2026 Investor Day put a commercial roadmap behind an architecture built to reduce dependence on the conventional HBM interposer. The stock-moving number was not 133 TB/s. It was FY29 non-handset revenue nearly doubled from $22B to $40B, with data center the major driver. The market is processing that through a MediaTek-style re-rating template (handset doghouse → data-center multiple); Citrini's July "All Along the AI Watchtower" called the hardware "taking detours around the HBM toll booth." High Bandwidth Compute takes the AI accelerator out of the SoC and places it directly beneath a DRAM stack, connected vertically by TSVs, so bandwidth flows up through die area rather than out through the edges. Qualcomm says multiple HBC stacks can be deployed with standard packaging and no HBM silicon interposer. AI200 racks ship this year *without* HBC; HBC debuts on AI250 in 2027, then AI300 and a server CPU in 2028. The company has never identified HBC's DRAM as LPDDR — coverage, including BEP's first draft, assumed it. Claimed Investor Day numbers, all Qualcomm's own: 6× bandwidth per watt of HBM; 200× capacity per watt of SRAM; 4–8× better decode performance per watt and on TCO; 133 TB/s. Tony Pialis frames the result as SRAM-like performance with stacked-memory density, built from mobile-chip constraints (low power, small area, no exotic packaging).

Rick's verification refuses the headlines. 133 TB/s is *effective* memory bandwidth: internal bandwidth consumed by local HBC computation while the main accelerator keeps orchestration-heavy work — workload bandwidth inside HBC, not raw bandwidth exposed to the host. No defensible sustained number can be reconstructed from LPDDR5X or LPDDR6 pin rates; Qualcomm has disclosed neither protocol nor interface width, channel structure, or stack configuration. The 6× figure is an internal estimate against competing published specs, *card-level*; the 200× SRAM comparison is *rack-level* — different boundaries, never a common benchmark. The HBM baseline will also move before AI250 samples: Micron specifies >2.8 TB/s for HBM4 and Samsung up to 3.6 TB/s for HBM4E. Classification is load-bearing: HBC is near-memory compute, not processing-in-memory. A separate logic die under DRAM bonded onto logic is Patterson's hierarchy point from BEP's January *The Hierarchy Rewrites* ("better suited for LLM inference than PIM because shards can be 1,000× larger"), which makes software the central test. Qualcomm has not detailed operator coverage, compiler partitioning, or fallback. Value exists only when locally eliminated traffic exceeds coordination cost. The dodge is partial by construction: it may delete the large silicon interposer, but it still needs direct DRAM-to-logic bonding and 3D integration — packaging complexity relocates into the vertical stack. Decisive evidence is sustained end-to-end tokens per joule under disclosed workload and thermal conditions. Until bandwidth boundary, methodology, and measured system results are published, the architecture is credible and the headline numbers are not.

Prior PIM attempts produced benchmarks without platforms: Samsung HBM-PIM (~2.5× system performance, >60% lower energy); SK Hynix still demonstrating AiMX on H100s with vLLM in 2025; UPMEM shipped programmable DRAM and a real software stack. None reached a named hyperscale deployment. Ownership and software, not viability, killed them. HBC fixes part of ownership — one vendor designs memory-side compute, accelerator, runtime, and rack, unlike SK Hynix bolting AiMX onto someone else's H100 — but CUDA is not a compiler. It is a decade of libraries, profilers, and deployment tooling that customers have already built models, reliability processes, and hiring around; ROCm is a thinner version that has taken AMD years. An incremental bandwidth or energy advantage does not clear the migration bar, and HBC still splits every real model across two compute domains. The variable that matters is the fraction of the token path that stays inside HBC after partitioning. Heat is the architectural exposure: active logic in 3D proximity to temperature-sensitive DRAM, which is the separation the interposer was providing. Eckert et al. used an 85°C DRAM threshold, refresh doubling per additional 10°C, and found allowable logic power ~8.5 W passive to ~55 W active. Those numbers do not predict HBC; they establish that cooling and stack orientation set a ceiling, and Qualcomm has disclosed no logic power, no DRAM junction temperature, and no sustained performance after thermal steady state. Rick's base case: HBC becomes a specialized decode or offload tier inside selected Qualcomm systems while GPU and HBM platforms keep the broader inference market.

That base case is survivable for BEP's *trade*, because the trade does not depend on Qualcomm winning. It depends on Qualcomm not being alone. Groq V3 uses on-chip SRAM on what appears to be a standard packaging process — no CoWoS, no HBM (BEP, *The Fourth Piece Ships*, March). Positron got there with commodity LPDDR. Three is a pattern; Qualcomm is the largest and best-funded instance. NVIDIA Feynman (2028) routes around SRAM physics with 3D-stacked SRAM using AMD X3D-style hybrid bonding; memory vendors route around TCB with hybrid bonding. Four weeks after Investor Day, Vera supplied the LPDDR datapoint coverage had been assuming for HBC: 88 custom cores with SOCAMM2 LPDDR5X at up to 1.2 TB/s per socket, 256 GB–1.5 TB per socket, field-replaceable, multi-vendor sourcing, 384 TB of LPDDR5X in one rack at maximum. Vera is *not* a dodge — it is a CPU, and Rubin GPUs beside it still run HBM4. What it establishes is that the largest accelerator vendor has qualified datacenter LPDDR as a real memory tier at rack scale. The open question is whether that capacity becomes addressable KV cache. The Bandwidth Tax rule: you route around a wall and you pay for the route. Hybrid bonding pays in packaging complexity, stacked SRAM in bonding yield, both bills due at the same suppliers. The question is not whether the tax disappears — BEP's thesis says it never does — but where it gets collected instead.

If HBC works, it is bearish the large-interposer premium (CoWoS capacity and the 30%+ HBM4 manufacturing premium from the parent piece) and neutral-to-bullish the memory oligopoly (Micron, Samsung, SK Hynix sell whatever high-density DRAM sits in the stack). Sanjay's confirmation that non-HBM margins are currently higher than HBM margins is the mix-shift tell: the same vendors sell the dodge with one hand and the tax with the other. Qualcomm has not identified the memory technology, named a DRAM supplier, or said who performs final logic-and-memory integration, so the mix-shift is a scenario with a supplier list missing. Even skipping large interposers and some CoWoS, HBC still consumes wafer thinning, bonding, known-good-die, and advanced test. Pressure falls on the scarcity premium attached to large interposers and conventional accelerator-to-HBM integration, not on packaging as an activity. Destination named in January's *The Hierarchy Rewrites*: TSMC SoIC, Intel Foveros, and hybrid-bonding equipment (Besi, EVG, SUSS) — plausible beneficiaries, not confirmed, because Qualcomm has disclosed neither assembly flow nor suppliers. If the architectures chasing HBC scale, value moves from interposer area toward bonding tools, stack yield, thermal integration, and test. CoWoS is sold out regardless and 2027 is a long way out; toll roads get repriced on the first credible detour, not the last car through. On Qualcomm itself: MediaTek re-rated from under 20× NTM once TPU exposure pulled it out of the handset bucket. Credibility gap is Centriq 2017 walkaway. Current validation stack: Alphawave SerDes, two hyperscaler custom-silicon programs contributing in FY27, multi-generation Meta CPU with production 2H28, pending Modular acquisition for software. Data-center is >$15B *of* the $40B, not additive: $10B automotive, >$14B IoT, >$15B data center. TD Cowen's unconfirmed read is that the target counts only existing customers. Named customers and measured system performance are the evidence; the guidance is the option.

Three break cases: (1) graveyard wins — all numbers Qualcomm's own, zero third-party benchmarks, first silicon 2027, high internal bandwidth that never becomes end-to-end inference because operator coverage, partitioning, fallback, and thermal throttling eat the local gain; (2) the stack outruns the dodge — HBM improving per stack/watt/delivered TB/s and sold out through the window in which HBC must prove itself, plus larger caches, lower-precision weights, speculative decoding, and KV-cache optimization shrinking near-memory value before AI250; the dodge only pays if the tax keeps rising; (3) HBC works and incumbents still collect — high-density DRAM from the same oligopoly, overlap with constrained stacking/test, bonding/yield/test/cooling/validation absorbing everything saved by deleting the interposer. A reader can accept the entire piece and still conclude the only durable longs are the memory vendors and foundries they already own. Mind-change by end-2027 requires *both*: Qualcomm discloses how effective bandwidth is calculated (raw DRAM vs locally consumed vs visible to the accelerator) *and* independent testing confirms at least half the claimed decode perf/watt advantage against contemporary HBM systems under matched quality/latency/thermal, with at least one named hyperscaler or frontier lab in production. Either missing, and BEP writes that the tax held. Closing rule: stop asking whether Qualcomm catches NVIDIA; stay long the constraint until the detour is proven cheaper. Paid follow-up will name the collection-point migration. The next free installment applies the same treatment to [[Theses/SNDK - SanDisk]] High Bandwidth Flash: NAND stacked and interfaced like HBM, OCP/sampling story, endurance not solved; the honest question is which AI bytes belong on NAND (read-mostly weights plausible; KV cache is a write stream with endurance, placement, and reload costs slide decks do not price). Hot Chips next week for field notes.

## Framework / Mental Model

**Name:** Bandwidth Tax / tax dodge — collection-point migration. Corollary of BEP's 9 July parent piece: the money made *around* each HBM stack grows faster than the money made *inside* it; when the tax gets high enough, someone builds a machine that owes less of it. The tax never disappears. It moves.

**Engineering axis (what HBC is, and is not):**

| Classification | Mechanism | What is proven | What is not |
|---|---|---|---|
| Near-memory compute (HBC as disclosed) | Separate logic die under DRAM, bonded onto logic; data-bound ops local; host keeps orchestration | Architecture description at Investor Day / OnQ July 2026 | Protocol, width, channel, stack, DRAM type, supplier, assembler |
| Processing-in-memory (not HBC) | Compute inside the DRAM array (HBM-PIM, AiMX, UPMEM) | Decade of benchmarks; Samsung ~2.5× / >60% energy; AiMX on H100+vLLM 2025 | Named hyperscale *platform* |
| Interposer HBM (the tax) | Accelerator sideways to HBM cubes across a large silicon interposer (CoWoS-S/L) | Sold-out CoWoS; 30%+ HBM4 manufacturing premium (parent piece) | Whether the premium survives a credible detour |

**Collection-point axis (where the tax is collected if the dodge works):**

| Seat today | Attacked by | Destination if HBC-class architectures scale | Confirmed? |
|---|---|---|---|
| Large silicon interposer / CoWoS scarcity premium | Tiled accelerator-memory stacks, "standard packaging," no HBM interposer | Bonding tools, stack yield, thermal integration, advanced test | No — Qualcomm has not named flow or suppliers |
| HBM manufacturing premium (stack, base die, TCB/MR-MUF) | Mix-shift into high-density non-HBM DRAM inside the vertical stack | Same DRAM oligopoly (MU / Samsung / SK Hynix); possibly higher non-HBM margins | Scenario only — DRAM type unnamed |
| CUDA / software tax | Split token path across HBC + host | Stays with the platform that owns libraries, profilers, hiring | Rick: migration bar not cleared |

**How applied.** Classify every "HBM alternative" headline on both axes before drawing beneficiaries. Engineering tells you whether the claim is a reconstructable pin-rate (it is not, for 133 TB/s) or an internal-workload number, and whether software/thermal ceilings bind. Collection-point tells you that bearish-interposer is not bearish-DRAM and not bearish-packaging-as-activity. Methodology constraints BEP states: (1) do not reconstruct sustained bandwidth from LPDDR pin rates the architecture does not disclose; (2) do not quote 6× and 200× as one benchmark (card vs rack); (3) Vera is a CPU LPDDR qualification, not a dodge; Rubin still runs HBM4; (4) Besi/EVG/SUSS/SoIC/Foveros are plausible, not confirmed; (5) mind-change needs *both* bandwidth-boundary disclosure *and* independent ≥½ decode-perf/W vs contemporary HBM by end-2027.

**Rule the framework produces.** Stay long the constraint until a detour is cheaper. Toll roads reprice on the first credible detour, not the last car. Do not short memory because packaging is detoured; do not treat CoWoS sold-out as proof the premium is perpetual.

## Evidence

All figures below are single-sourced to this BEP Research essay (Gmail-full, 2026-08-18) unless a nested primary is named. [web: bepresearch.substack.com]

### Qualcomm announcement / guidance

| Item | Figure | Tag |
|---|---|---|
| Publication | BEP Research; Rick Xie + Ben Pouladian; 2026-08-18; free memory-series #2 | [1×: BEP] |
| Parent piece | *The Bandwidth Tax*, 2026-07-09 | [1×: BEP] |
| Investor Day | 2026-06-24 | [1×: QCOM IR via BEP] |
| FY29 non-handset revenue | $22B → $40B; data center the major driver | [1×: QCOM IR via BEP] |
| FY29 segment bridge | $10B automotive; >$14B IoT; >$15B data center *within* the $40B | [1×: QCOM PR 2026-06-24 via BEP] |
| Citrini framing | "taking detours around the HBM toll booth"; 2026-07-19 | [1×: Citrini via BEP] |
| Architecture | Accelerator under DRAM stack; TSV vertical; bandwidth through die area not edges; no HBM silicon interposer; standard packaging for multiple stacks | [1×: QCOM IR via BEP] |
| Roadmap | AI200 this year, no HBC; HBC debuts AI250 2027; AI300 + server CPU 2028 | [1×: QCOM IR via BEP] |
| DRAM type | never identified as LPDDR (coverage assumed it, including BEP first draft) | [1×: BEP] |
| Supplier / assembler | unnamed | [1×: BEP] |
| Headline claims | 6× BW/W vs HBM; 200× capacity/W vs SRAM; 4–8× decode perf/W and TCO; 133 TB/s | [1×: QCOM IR via BEP] |
| 133 TB/s definition | *effective* / internal workload bandwidth consumed inside HBC, not raw BW to the main accelerator | [1×: QCOM / BEP] |
| 6× boundary | internal estimate vs competing published specs; card-level | [1×: QCOM / BEP] |
| 200× boundary | rack-level SRAM comparison | [1×: QCOM / BEP] |
| Pin-rate reconstruction | failed; protocol / width / channels / stack undisclosed | [1×: BEP] |
| HBM baselines that will move | Micron HBM4 >2.8 TB/s; Samsung HBM4E up to 3.6 TB/s | [1×: vendor specs via BEP] |
| Classification | near-memory compute, not PIM | [1×: BEP] |
| Patterson quote (Jan) | "better suited for LLM inference than PIM because shards can be 1,000× larger" | [1×: BEP *Hierarchy Rewrites*] |
| Software disclosure | no operator coverage, compiler partitioning, or fallback | [1×: BEP] |
| Dodge residual | still needs DRAM-to-logic bonding + 3D integration | [1×: BEP] |

### Prior PIM / thermal / CUDA

| Item | Figure | Tag |
|---|---|---|
| Samsung HBM-PIM | ~2.5× system performance; >60% lower energy | [1×: Samsung via BEP] |
| SK Hynix AiMX | still demoing on H100s with vLLM in 2025; no named hyperscale deployment | [1×: SK Hynix AI Infra Summit 2025 via BEP] |
| UPMEM | programmable DRAM + real software stack; no named hyperscale deployment | [1×: UPMEM via BEP] |
| Eckert et al. thermal | 85°C DRAM threshold; refresh doubles per +10°C; ~8.5 W passive / ~55 W active allowable logic | [1×: Eckert et al. via BEP] |
| QCOM thermal disclosure | no logic power, DRAM Tj, or sustained post-steady-state performance | [1×: BEP] |
| Rick base case | specialized decode/offload tier; GPU+HBM keep broader inference | [1×: BEP] |
| CUDA vs ROCm | CUDA = decade of libraries/profilers/tooling/hiring; ROCm thinner, years for AMD | [1×: BEP] |
| Binding variable | fraction of token path that stays inside HBC after partitioning | [1×: BEP] |

### Pattern of detours / Vera / collection points

| Item | Figure | Tag |
|---|---|---|
| Groq V3 | on-chip SRAM; appears standard packaging; no CoWoS; no HBM | [1×: BEP *Fourth Piece Ships*, March] |
| Positron | commodity LPDDR, earlier | [1×: BEP] |
| Pattern claim | three accelerator teams routing around HBM/interposer; Qualcomm largest/best-funded | [1×: BEP] |
| Feynman (2028) | 3D-stacked SRAM, AMD X3D-style hybrid bonding | [1×: BEP *Memory Wars*] |
| Vera | 88 custom cores; SOCAMM2 LPDDR5X; up to 1.2 TB/s per socket; 256 GB–1.5 TB per socket; field-replaceable; multi-vendor; 384 TB/rack max | [1×: BEP *NVIDIA Vera*] |
| Vera vs dodge | CPU, not a dodge; Rubin GPUs still HBM4; datacenter LPDDR is a named product line | [1×: BEP] |
| Open question | whether Vera LPDDR becomes addressable KV cache | [1×: BEP] |
| HBM4 manufacturing premium | 30%+ (parent piece) | [1×: BEP *Bandwidth Tax* / TrendForce via BEP] |
| Non-HBM vs HBM margins | "Sanjay confirmed that non-HBM margins are currently higher than HBM margins" | [1×: BEP *Micron Just Proved the Memory Thesis*] |
| Hybrid-bonding candidates | TSMC SoIC; Intel Foveros; Besi, EVG, SUSS | [1×: BEP *Hierarchy Rewrites*, January] |
| Confirmation status | plausible not confirmed; no assembly flow or suppliers named | [1×: BEP] |
| CoWoS | sold out regardless; 2027 far out | [1×: BEP] |
| QCOM re-rate comp | MediaTek started year <20× NTM; TPU exposure | [1×: BEP] |
| QCOM credibility | Centriq 2017 shipped then walked away | [1×: BEP] |
| Validation stack | Alphawave SerDes; two HS custom programs FY27; Meta CPU multi-gen, production 2H28; pending Modular | [1×: BEP] |
| TD Cowen | target counts only existing customers (QCOM not confirmed) | [1×: TD Cowen via BEP] |
| Mind-change | both of: bandwidth-boundary disclosure + independent ≥½ decode perf/W vs contemporary HBM, named HS/lab in production, by end-2027 | [1×: BEP] |
| Author disclosure | long NVDA, NOW, LITE, CRDO, TSEM, ALAB, WOLF, SMCI, BE, NBIS, ORCL 2027 LEAPS; no QCOM | [1×: BEP] |

### HBF teaser (next installment)

| Item | Figure | Tag |
|---|---|---|
| SNDK HBF | NAND stacked and interfaced like HBM; pitched as memory not storage; Investor Day last week | [1×: BEP] |
| Status | concept → standards and sampling | [1×: BEP] |
| Endurance | not solved | [1×: BEP] |
| Honest question | which AI bytes belong on NAND, not whether flash can deliver more BW | [1×: BEP] |
| Weights | read-mostly; plausible | [1×: BEP] |
| KV cache | far larger demand pool; write stream; endurance, placement, reload costs unpriced in slide decks | [1×: BEP] |
| Third installment | DRAM series (1–2) → flash | [1×: BEP] |
| Hot Chips | memory track next week; field notes to follow | [1×: BEP] |

### What to watch (author's checklist)

| Watch | Why | Tag |
|---|---|---|
| AI200 named-customer rack deployments this year | HBC is not in this product | [1×: BEP] |
| HBC silicon with *sustained* not aggregate BW; first third-party benchmark | headline-number test | [1×: BEP] |
| DRAM supplier disclosures; MU / Samsung / SK Hynix DC quals | mix-shift tell | [1×: BEP] |
| Meta C1000 2H28; either HS custom program named in FY27 | QCOM data-center evidence vs guidance-as-option | [1×: BEP] |
| NVDA / AMD LPDDR tiers or near-memory configs | whether the tier stops being one company's bet | [1×: BEP] |
| CoWoS pricing at the margin in 2027; HB tool orders at Besi, EVG, SUSS | collection-point offset | [1×: BEP] |

## Contradiction Check

**Supports** [[Theses/NVDA - Nvidia]] §Key Non-consensus Insights (CUDA is general-purpose; integration-cost 100–1000×; "CUDA is not a compiler") and §Bear / Outstanding Question on Groq LPX: BEP's PIM graveyard and HBC software test are the same wall the vault already uses to keep QCOM/AMD/ASIC displacement from auto-firing. Vera SOCAMM2 (1.2 TB/s, 256 GB–1.5 TB, 384 TB/rack, multi-vendor) corroborates the thesis's already-logged Vera/SOCAMM value-chain point ([[Research/2026-06-03 - AI Value Capture and GPU Rental Economics - deep-dive]], [[Research/2026-06-02 - Datacenter CPU Landscape 2026 - deep-dive]]) and the 12 August Kyber LPDDR-can-exceed-HBM log; BEP is explicit that Vera is *not* an HBM dodge and Rubin still runs HBM4. Groq V3 "no CoWoS, no HBM" restates the SRAM-inference segmentation already in NVDA Outstanding Questions / Bear. Feynman 3D-stacked SRAM via X3D-style hybrid bonding is consistent with the annual-cadence / SoIC-adjacent packaging stack, not a CUDA break. **Does not write** a Conviction Triggers section NVDA still lacks (gap flagged 2026-07-09 / 2026-04-23 stress). **Does not change** NVDA conviction high / status active.

**Challenges, does not break** [[Theses/TSM - Taiwan Semiconductor]] Insight #1 (CoWoS as $10B+ separable annuity) and the LOW trigger's named-observable "production-scale CoWoS-alternative win." HBC is the first *named commercial roadmap* in the live book that claims to tile accelerator-memory stacks without a large silicon interposer — that is the detour Insight #1's scarcity premium is not modeled as facing. Offset inside the same source: CoWoS sold out regardless, 2027 is far, Qualcomm has not named TSMC vs anyone, SoIC is listed as a *beneficiary* of the migration (Insight #3 A16/Feynman and SoIC-X hybrid bonding are the destination, not the victim), and BEP's own mind-change bar has not been met. This is a watch on the packaging-premium *multiple*, not a 2026 volume print. Insight #4 COUPE / #5 N2 pricing untouched. **Trigger touch:** TSM → LOW if "a named production-scale CoWoS-alternative win (e.g., Google TPU v9 volume on Intel EMIB-T)" — evidence-touched, dir=LOW, **not fired** (not production-scale, not a win, foundry unnamed). HIGH-reaffirm and CLOSE not in this piece. **Does not change** TSM conviction high / status active.

**Supports** [[Theses/BESI - BE Semiconductor Industries]] Insight #1 (BESI is a 3D-integration monopoly miscategorized as an HBM timing play) and the logic/SoIC installed-base argument: BEP names Besi / EVG / SUSS plus TSMC SoIC as the collection point if DRAM-to-logic bonding scales. This is the same "plausible not confirmed" caveat the vault already uses for HBF TCB orders. No HBC tool order is announced. BESI has no registered Conviction Triggers. **Does not change** BESI conviction medium / status active.

**Supports, does not fire** [[Theses/000660 - SK Hynix]] Insight #1/#2 share-erosion and MR-MUF-as-process-not-architecture: a mix-shift *away* from HBM packaging into high-density DRAM is framed as oligopoly-neutral-to-bullish (same three vendors; non-HBM margins currently higher). AiMX-on-H100 is filed as the PIM graveyard, which is consistent with HBF remaining the unpriced call (Insight #3) rather than in-memory compute. The HBF teaser (endurance unsolved; KV cache is a write stream) is a *qualifier* on Insight #3 / Q4 (hyperscaler production 2027 vs slip), not a Rubin-allocation datapoint. HIGH (≥60% Rubin + HBM4E sole-source + Kinex 16-Hi + Namics ≥2028), LOW (Samsung >35% Rubin *and* HBM −10% YoY), CLOSE (CXMT HBM + Samsung HB yield 70% at 16-Hi mid-2027) are not touched. **Does not change** 000660 conviction medium / status active.

**Qualifies** [[Theses/SNDK - SanDisk]] Insight #1 (HBF as TAM-creation / OCP-standard call) in the same direction the thesis's own Industry Context already moved: BEP will apply the Qualcomm treatment to HBF; endurance is not solved; the honest question is which AI bytes belong on NAND; weights plausible, KV-cache write-stream costs unpriced. That is corroboration of the vault's endurance–density–cost trilemma and NVIDIA-swing-factor caution, not a new kill. SNDK has no registered Conviction Triggers. **Does not change** SNDK conviction medium / status active.

**Related prior vault notes (do not treat as this source):** [[Research/2026-07-26 - QCOM NVDA MU PhotonCap Three Memory Wall Routes - deep-dive]] (three memory-wall routes; different author); [[Research/2026-08-16 - SNDK MU 000660 - PhotonCap HBF vs Optics - deep-dive]] (HBF beside/above/beyond); [[Research/2026-08-12 - TSM BESI AMAT - TSMC CoWoS 5.5x Reticle 99pct Yield - news]] (CoWoS near-balance, the other side of the sold-out claim). Honest read: high-signal for the *collection-point* map (interposer premium vs DRAM oligopoly vs hybrid-bonding tools vs CUDA wall); low-signal for any 2026 earnings print. QCOM is not a live-book name. Paid BEP follow-up will name entries; this free note does not.

## Source Excerpts

> "Rick's verification and my framing point in different directions, so let me be exact about what we are underwriting. Not HBC working: Rick's read, below, is that the headline numbers are unproven and the base case is a niche. We are underwriting something narrower and more actionable: the packaging premium is currently priced as though nobody is trying to route around it, and that is no longer true."

> "Qualcomm describes 133 TB/s as effective memory bandwidth, and explains that HBC makes internal memory bandwidth available to local computation while the main accelerator keeps the orchestration-heavy work. Read it as workload bandwidth consumed inside HBC, not raw bandwidth exposed to the main accelerator."

> "No defensible sustained number can be reconstructed from LPDDR5X or LPDDR6 pin rates, which is the first thing we tried and the first thing that failed."

> "HBC is near-memory compute, not processing-in-memory."

> "CUDA is not a compiler. It is a decade of optimized libraries, profilers, and deployment tooling that customers have already built their models, their reliability processes, and their hiring around."

> "Rick's base case: HBC becomes a specialized decode or offload tier inside selected Qualcomm systems while GPU and HBM platforms keep the broader inference market."

> "The Groq V3 uses on-chip SRAM on what appears to be a standard packaging process. No CoWoS interposer. No HBM stacks."

> "Vera pairs 88 custom cores with SOCAMM2 LPDDR5X at up to 1.2 TB/s per socket, 256 GB to 1.5 TB per socket, field-replaceable, multi-vendor sourcing explicitly enabled. … At maximum configuration that is 384 TB of LPDDR5X in one rack. Vera is not itself a dodge … It is a CPU, and the Rubin GPUs beside it still run HBM4."

> "HBC is bearish the large-interposer premium and neutral-to-bullish the memory oligopoly. Those are not the same trade, and the market is pricing them as one."

> "Sanjay confirmed that non-HBM margins are currently higher than HBM margins."

> "The Hierarchy Rewrites put the candidates for exactly this direction on the page in January: TSMC SoIC, Intel Foveros, and the hybrid-bonding equipment suppliers, Besi, EVG and SUSS. Direct DRAM-to-logic bonding is their process, not CoWoS's, which makes them plausible beneficiaries rather than confirmed ones, since Qualcomm has disclosed neither its assembly flow nor its suppliers."

> "Two conditions, by end-2027. Qualcomm discloses how effective bandwidth is calculated, in enough detail to separate raw DRAM bandwidth from locally consumed traffic from bandwidth visible to the accelerator. And independent testing confirms at least half the claimed decode perf/watt advantage against contemporary HBM systems under matched model quality, latency, and thermal conditions, with at least one named hyperscaler or frontier lab in production. Both, and the packaging-premium leg activates."

> "NAND endurance is not solved, so the honest question is not whether flash can deliver more bandwidth. It is which AI bytes actually belong on NAND. Model weights are read-mostly and plausible. KV cache could be the far larger demand pool, but it is a write stream, and the write stream carries endurance, placement, and reload costs the slide decks do not price."

> "The tax may move. Qualcomm still has to prove the detour is cheaper, and until it does, stay long the constraint."
