---
publish: false
date: 2026-08-24
tags: [research, semiconductors, DRAM, HBM, NAND, 000660, MU, SNDK, NVDA, TSM]
sector: DRAM & HBM Memory
ticker: 000660
source: 'https://www.jasonschips.ai/p/hot-chips-day-1-precious-memories'
source_type: deep-dive
title: 'Hot Chips Day 1 - Precious Memories'
publication: "Jason's Chips"
gmail_id: 1a031bfdcfbb7dc3
author: "Jason's Chips"
sender: jasonschips@substack.com
propagated_to: [000660, MU, SNDK, TSM, BESI, 285A]
---

# Hot Chips Day 1 - Precious Memories

## Thesis Delta

Consensus prices the 2026 memory shortage as a rent event for the DRAM triopoly ([[Theses/000660 - SK Hynix]] HBM scarcity through 2027; [[Theses/MU - Micron Technology]] queue; [[Sectors/DRAM & HBM Memory]] evergreen-reset pin) and prices [[Theses/SNDK - SanDisk]] HBF as near-HBM bandwidth at NAND cost (Investor Day "within 2.2% of HBM" / ~$1/GB). This 24 August 2026 Jason's Chips Hot Chips Day 1 note (free Substack; Gmail `1a031bfdcfbb7dc3`) implies the market has the *response function* wrong: memory is already ~70% of a rack, the conference itself is a career-scale effort to cut the price of DRAM, SK hynix is already shipping HBM4 on TC-NCF rather than the MR-MUF moat the tape still recites, Samsung is using the only IDM-owned leading-edge foundry to turn the HBM base die from a passive router into custom PIM / cHBM / zHBM, d-Matrix is offering SRAM-class bandwidth by stacking one logic die on DRAM without hybrid bonding, and HBF's real attach is low-batch and expert-parallelism (8-16x HBM capacity, 25x worse bandwidth/latency vs HBM-G2). Trigger touch: **no-touch** on 000660 → HIGH (Rubin ≥60% + HBM4E sole-source + Kinex 16-Hi + Namics ≥2028), → LOW (Samsung >35% first two Rubin quarters AND HBM ASP −10% YoY H1 2026), → CLOSE (CXMT qualified HBM + Samsung HBM5 hybrid-bond 70% at 16-Hi by mid-2027); **no-touch** on MU → HIGH / LOW / CLOSE (no Q3 board meter, no LTA-cap print, no destock/CXMT/GB300 dual-source). [[Theses/NVDA - Nvidia]] has no Conviction Triggers section (untested-no-trigger). [[Theses/SNDK - SanDisk]] has no Conviction Triggers section. Conviction/status unchanged.

## Summary

Jason's Chips' Day 1 Hot Chips dump (theme: memory) is an investor translation of five talks, not a verdict on which architecture wins. The opening is the shortage itself: HBM-class memory is already about 70% of a rack, and a room full of presenters is trying to make that line item cheaper. Parallelism is why HBM is high-bandwidth and why it eats ~3x silicon vs DDR5 for the same capacity (256 IO vs 8 IO at 8 Gbps; 128 vs 32 banks on HBM3E). The conference name is the thermal problem: cooling sits on top of the stack, the base-die PHY and D2D are the heat source at the bottom, reliability falls as the gradient steepens. Liquid cooling and hybrid bonding are the named mitigations; high-speed D2D, richer base-die function, higher DRAM activity and taller stacks are the named heat sources. Generation table in the slides: HBM4 (2026) is 32 channels / 64 pseudo-channels / 2048 I/Os / 11 Gbps / 2800 GB/s / 24 Gb die / 8+ hi / 24GB+ cube, vs HBM3E at 16 / 32 / 1024 / 8 Gbps / 1024 GB/s.

Samsung's PIM talk is the customisation story. Compute is scaling ~3x every two years (TPU v3 through R200) while HBM bandwidth is scaling <2x every two years (HBM2E through HBM4), and decode (attention/FFN) is the memory-bandwidth-bound phase that already eats most wall-clock inference time. Today's HBM base die is a passive router (PHY + DRAM-stack test). The roadmap moves the memory controller off the xPU, adds RAS/self-test, attaches external memory through the base die, then puts processing elements in the B-die so only intermediate results cross D2D. That makes HBM a custom, less-commoditised product. Samsung can do this without begging [[Theses/TSM - Taiwan Semiconductor]] for logic allocation, unlike SK hynix and Micron. HBM4 is the node where the B-die leaves DRAM process for 4nm logic (C-die stays 1*nm DRAM; xPU is 3nm / <3nm by 2027). On advanced logic the PHY shrinks from a large HBM PHY to a small D2D interface (cHBM4 PHY 8.5mm x 1.5mm, channel depth 2mm, vs sHBM4 8mm x 4mm / 5.5mm), which frees die area and cuts pJ/bit and also concentrates power density. Samsung's answer is a side Heat Path Block (HPB): >35% peak-temperature cut at >50% PHY coverage, aimed at sHBM5 jumping from 14 Gbps / 0.5 W/mm2 (sHBM4E) to >28 Gbps / >2.0 W/mm2. zHBM is labelled 2030+ hype: hybrid-bond the C-die stack onto the xPU, kill the 2.5D interposer, drop to 4-hi for thermals. Slide claims vs HBM4E: ~70% power vs HBM5, +230% DRAM BW, 100W DRAM-power save, 8.3% GPU-power reallocation after stripping SERDES. Software support for PIM is called the gating factor.

SK hynix's packaging talk is, in the author's words, nothing new and "the stuff that they've been doing since 2023." The load-bearing line for the vault is the aside: "I still remember the days when MR-MUF was part of hynix moat thesis. SK hynix actually uses TC-NCF in HBM4 now." The slides still teach both flows. TC+NCF: thermo-compression plus non-conductive film, less warpage-sensitive, low productivity, high thermal resistivity. MR+MUF: mass reflow plus molded underfill, high productivity, low thermal resistivity, warpage and narrow-gap-fill problems. Process flow is wafer-test → KGSD (known-good stacked die) → singulation / 6D inspection → cube → OSAT SiP → fabless customer; key process risks at TSV fill (KOZ, Cu contamination), wafer thinning (TTV), micro-bumps (uniformity/yield), and MUF gap-fill (voids, joint reliability). Source cited on the key-technologies slide: IEDM 2018.

d-Matrix's 3D DRAM talk is the author's favourite. SRAM is fast (6T, on-die, sub-ns; Corsair card-pair 300 TB/s, 4 GB, ~1 ns, ~0.5 pJ/bit) and cannot scale (10x a DRAM 1T1C cell, bitcell frozen ~0.021 um2 at TSMC N5/N3E/N2, leakage at GB scale, ~4 GB practical, ~100x DRAM cost). HBM has capacity (8-16 core dies, 8 stacks/package) and cannot scale bandwidth to SRAM-like numbers because pin speed and IO width move slowly and stack count is beachfront-limited; practical HBM4 ceiling named for Vera Rubin and MI 455 is ~20 TB/s. d-Matrix stacks one TSMC N4 logic die face-to-face (36 um) on 3D DRAM: no multi-layer HBM stack, no hybrid bonding, no beachfront. Slide vs HBM4: F2F-below vs 2.5D-beside, 0.37 vs 2-3 pJ/bit, 100+ vs 18 TB/s per card, 32 vs 192 GB. Claimed 5.6x BW/card, 5-8x lower energy/bit, 7x denser I/O. Energy ladder: SRAM ~50 fJ, 3D vertical IO 0.3-0.4 pJ, 2.5D HBM4 system 2.5 pJ + 3 pJ on-chip; 3D IO ~10x below HBM. Decode-time charts on a 72-card Raptor box (GLM 5.2, Kimi K3) show decode at 71-99% of wall-clock except the 1M-prefill outliers.

OXMIQ / PRAXMATI on High Bandwidth Flash is the HBF realism pass. Capacity is 8-16x HBM. The metric that matters is $/token, not $/GB, and the bandwidth/latency trade-off vs HBM is 25x worse (slide: 25x vs HBF-G2, ~13x vs G3 on bandwidth per GB). Pushing the Pareto of high batch (throughput) and high interactivity (tokens/user) is exactly when you are memory-bandwidth constrained, so HBF sits with unused capacity. Useful attach: low batch, small personal/private boxes, and expert parallelism where more experts live on fewer nodes and all-to-all collapses (8 GPUs sharded → 2 HBF-capacity nodes). (β, α) landscape puts HBF at 1x cost/GB vs NAND SSD ~0.15x, LPDDR5X ~3x, HBM ~10-15x, SRAM-only (Cerebras/Groq) ~300x. Author entered bullish on HBF after SanDisk Investor Day, leaves slightly less bullish: HBF is not HBM bandwidth, the HBM stack has absorbed far more R&D, and today's niche use-cases are the bull case only if software and silicon close the gap later. If the category works, NAND's bit-to-HBM-like-cube conversion is a ~9x trade (SLC not TLC, then HBM-style stacking).

## Framework / Mental Model

**Name:** three stacked typologies from Day 1 (sHBM/cHBM/zHBM; SRAM/HBM/3D-DRAM energy ladder; (β, α) HBF landscape). Not one named scoring scheme; three classification planes the source applies to the same memory-wall problem.

**Components.**

| Plane | Axes | How the source applies it |
|---|---|---|
| Custom HBM | sHBM (standard B-die: PHY + test) vs cHBM (SoC-like B-die on advanced logic, shared C-die stacks) vs zHBM (C-die stack on the xPU, no 2.5D interposer, 4-hi) | HBM4 B-die flips from DRAM process to 4nm logic. PHY shrink is the area/power win and the hotspot. HPB is side-extract heat. zHBM is 2030+ and hybrid-bond constrained. |
| Energy ladder | SRAM on-die vs 3D vertical IO vs 2.5D HBM4 system vs beachfront-limited HBM | SRAM wins latency and dies on area/cost/leakage. HBM wins capacity and dies on beachfront (~20 TB/s practical at HBM4 for Vera Rubin / MI 455). 3D DRAM is one F2F logic die on DRAM: SRAM-class BW, DRAM-class (medium) capacity, ~10x below HBM energy. |
| (β, α) landscape | β = $/GB relative to HBF=1; α = bandwidth per GB | NAND SSD cheapest/slowest; HBF-G2 the presenter's focus; HBM 10-15x cost and 25x α vs G2; SRAM-only ~300x cost. PIM/d-Matrix "escapes this plane" because they move results, not bytes. HBF attach is off the high-batch / high-interactivity Pareto (small-B MoE, local box, EP capacity). |

**Methodology.** Roofline first (is the workload memory-bound?). Then pick the plane: customise the B-die (Samsung), change the topology (d-Matrix), or buy capacity and give up α (HBF). Software support is the PIM gate; beachfront is the HBM gate; unused capacity at the Pareto frontier is the HBF gate.

## Evidence

All figures below are slide- or prose-transcribed from one free Substack conference note. Tag `[web: jasonschips.ai]` unless marked otherwise.

**Shortage and HBM basics**

| Item | Figure | Tag |
|---|---|---|
| Memory share of rack | ~70% | [web: jasonschips.ai] |
| HBM vs DDR silicon for same capacity | ~3x | [web: jasonschips.ai] |
| HBM3E core BW @ 8 Gbps | 256 GB/s (256 IO) vs DDR5 8 GB/s (8 IO) | [web: jasonschips.ai] |
| Banks | HBM3E 128/die; HBM4 256/die; DDR5 32 | [web: jasonschips.ai] |
| Pseudo-channels | 2 per channel (shared CA, independent data) | [web: jasonschips.ai] |
| HBM4 vs HBM3E | 32 vs 16 ch; 64 vs 32 PC; 2048 vs 1024 I/O; 11 vs 8 Gbps; 2800 vs 1024 GB/s | [web: jasonschips.ai] |
| Cube capacity | HBM3E/HBM4 24GB+ | [web: jasonschips.ai] |
| Thermal gradient | cooling on top; heat at base die | [web: jasonschips.ai] |
| Heat sources | high-speed D2D; advanced B-die function; DRAM activity; stack height | [web: jasonschips.ai] |
| Named mitigations | liquid cooling; hybrid bonding | [web: jasonschips.ai] |

**Samsung PIM / cHBM / zHBM**

| Item | Figure | Tag |
|---|---|---|
| Compute vs HBM BW scaling | TFLOPS 3x / 2yr; HBM BW <2x / 2yr | [web: jasonschips.ai] |
| Named compute points | TPU v3, A100, TPU v4, H100, MI300X, B100, TPU v5, B200, R200 | [web: jasonschips.ai] |
| Today's B-die | passive router: PHY + stack test | [web: jasonschips.ai] |
| Future B-die | memory controller off xPU; RAS/self-test; external memory attach; PEs in B-die | [web: jasonschips.ai] |
| Foundry split | Samsung in-house leading-edge logic; hynix and Micron "beg TSMC" | [web: jasonschips.ai] |
| B-die process flip | DRAM process through HBM3E; 4nm logic at HBM4/HBM4E | [web: jasonschips.ai] |
| xPU SoC node | 3nm (2026) / <3nm (2027) | [web: jasonschips.ai] |
| PHY footprint sHBM4 vs cHBM4 | 8mm x 4mm, CH 5.5mm vs 8.5mm x 1.5mm D2D, CH 2mm | [web: jasonschips.ai] |
| sHBM4E vs sHBM5 | 14 Gbps / 0.5 W/mm2 vs >28 Gbps / >2.0 W/mm2 | [web: jasonschips.ai] |
| HPB | >35% peak-temp cut at >50% PHY coverage | [web: jasonschips.ai] |
| zHBM dating | "common 2030+ type hype"; hybrid bonding | [web: jasonschips.ai] |
| zHBM vs HBM5 power | ~70% reduction | [web: jasonschips.ai] |
| zHBM vs HBM4E | +230% DRAM BW; 100W DRAM save; +8.3% GPU power reallocated | [web: jasonschips.ai] |
| zHBM stack | 4-hi (not 8-hi) for thermals | [web: jasonschips.ai] |
| PIM software | "currently weak"; "gating factor" | [web: jasonschips.ai] |

**SK hynix packaging**

| Item | Figure | Tag |
|---|---|---|
| HBM4 packaging (author) | TC-NCF, not MR-MUF | [web: jasonschips.ai] |
| TC+NCF vs MR+MUF | low vs high productivity; high vs low thermal resistivity; warpage-tolerant vs warpage-sensitive | [web: jasonschips.ai] |
| Flow | WT → KGSD wafer → KGSD test → singulation / 6D inspection → cube → OSAT SiP | [web: jasonschips.ai] |
| Key-tech slide source | IEDM 2018 | [web: jasonschips.ai] |
| Author's novelty read | nothing too new; process they have run since 2023 | [web: jasonschips.ai] |

**d-Matrix 3D DRAM**

| Item | Figure | Tag |
|---|---|---|
| Corsair SRAM card pair | 300 TB/s; 4 GB; ~1 ns; ~0.5 pJ/bit | [web: jasonschips.ai] |
| SRAM vs DRAM cell | 6T is 10x 1T1C; bitcell ~0.021 um2 frozen at N5/N3E/N2 | [web: jasonschips.ai] |
| SRAM cost / leak | ~100x DRAM; tens of watts at GB scale; ~4 GB practical | [web: jasonschips.ai] |
| HBM4 practical BW | ~20 TB/s (Vera Rubin, MI 455) | [web: jasonschips.ai] |
| HBM topology | 8-16 core dies/stack; 8 stacks/package; 2048 wires; 4-16 stacks; 20+ mm accelerator PHY | [web: jasonschips.ai] |
| 3D DRAM stack | TSMC N4 logic on 3D DRAM; 36 um F2F; one layer; no hybrid bonding | [web: jasonschips.ai] |
| HBM4 vs 3D-DRAM | 2.5D beside vs F2F below; 2-3 vs 0.37 pJ/bit; 18 vs 100+ TB/s/card; 192 vs 32 GB | [web: jasonschips.ai] |
| Multiples vs HBM4 | 5.6x BW/card; 5-8x lower energy/bit; 7x denser I/O | [web: jasonschips.ai] |
| Energy ladder | SRAM ~50 fJ; on-chip wire ~35 fJ/mm; 3D IO 0.3-0.4 pJ; interposer ~500 fJ/mm; 2.5D HBM4 2.5 pJ + 3 pJ | [web: jasonschips.ai] |
| 3D vs HBM layers | ≤4 vs 12-16 (yield argument) | [web: jasonschips.ai] |
| Decode share (Raptor 72-card) | GLM 5.2 81-97% typical, 90-99% multi-turn; Kimi K3 71-95% typical, 83-99% multi-turn; 1M-prefill outliers prefill-heavy | [web: jasonschips.ai] |

**HBF (OXMIQ / PRAXMATI)**

| Item | Figure | Tag |
|---|---|---|
| HBF vs HBM capacity | 8-16x | [web: jasonschips.ai] |
| BW/latency vs HBM | 25x worse (25x vs HBF-G2; ~13x vs G3 on α) | [web: jasonschips.ai] |
| True TCO metric | $/token, not $/GB | [web: jasonschips.ai] |
| Useful regime | low batch; personal/private box; expert parallelism | [web: jasonschips.ai] |
| EP cartoon | 8 GPUs all-to-all → 2 HBF-capacity nodes, little/no all-to-all | [web: jasonschips.ai] |
| β landscape | NAND SSD ~0.15x; HBF 1x; LPDDR5X ~3x; HBM ~10-15x; SRAM-only ~300x | [web: jasonschips.ai] |
| α landscape | NAND ~0.001; HBF-G1 ~1.5; G2 ~3; G3 ~7; LPDDR5X ~5; HBM3E ~50; HBM4 ~80; HBM4E ~100; SRAM ~500,000 | [web: jasonschips.ai] |
| MoE vs dense | Kimi-K2 vs Llama-3.1-70B on B200 NVL72 (OxSOL); dense knee ~B=300 | [web: jasonschips.ai] |
| Author stance | entered bullish (SanDisk Investor Day); left slightly less bullish, more realism | [web: jasonschips.ai] |
| NAND conversion if HBF works | ~9x trade (SLC not TLC, then HBM-style stack) | [web: jasonschips.ai] |

## Contradiction Check

Supports the shortage half of [[Theses/000660 - SK Hynix]] §Industry Context and [[Macro & Technology/DRAM Memory Cycle - Duration, Peak Timing and Second-Order Effects]] (memory already ~70% of a rack) and simultaneously challenges the rent-duration half: a Hot Chips day dedicated to cutting DRAM's price is the demand-side response [[Theses/MU - Micron Technology]] Insight #3 (L1 / 2018 destock analog) needs to keep on the table. Industry #1 (bottleneck identification) still fires on HBM; Industry #8 (architecture remaps the bottleneck) fires on three parallel remaps at once (custom B-die, 3D DRAM, HBF).

Challenges [[Theses/000660 - SK Hynix]] Insight #2 ("MR-MUF is a process moat") on a named observable the thesis still treats as current: the author states SK hynix uses **TC-NCF in HBM4 now**. That does not fire → LOW (Samsung Rubin share + ASP) or → CLOSE (hybrid-bond yield). It does re-weight Insight #2 toward "architecture wins" earlier than the 2028-29 hybrid-bond leap-frog window, and it rhymes with [[Research/2026-08-20 - 000660 NVDA MRVL - Damnang HBM Density Peak - deep-dive]] (8-Hi life extends; yield/supply/base-die function outweigh 12-Hi/16-Hi qualification). Samsung PIM/cHBM/HPB/zHBM is the same architectural axis as [[Research/2026-08-13 - 000660 MU - Samsung zHBM 3D Memory Vision FMS 2026 - news]] and [[Research/2026-08-15 - 000660 TSM NVDA - Samsung 2nm HBM Base Die - news]]: foundry-owned logic B-die is the IDM advantage. zHBM remains 2030+ projection (hybrid bonding, 4-hi, SERDES-off); it does not mint 2026 Rubin cubes.

For [[Theses/MU - Micron Technology]] the foundry line is direct: custom B-die / PIM is "great for Samsung" because hynix and Micron "beg TSMC for allocation." That is process-hygiene for a LOW-conviction non-holding (qualified third ≠ first-wave cubes), not a board-meter print. No IR 8-Hi HBM4 SKU is still the MU Ultra tell; this note's zHBM 4-hi and d-Matrix 32 GB are not MU SKUs.

Challenges [[Theses/SNDK - SanDisk]] Insight #1 and Q1 (HBF as TAM-creation, "within 2.2% of HBM") more than it kills it. The OXMIQ/PRAXMATI plane says HBF is 8-16x capacity and 25x worse on bandwidth/latency, useful off the high-batch Pareto (small box, small-B MoE, EP capacity), not as an HBM substitute in a dense rack. That is closer to the thesis's own 18 August mix-HBF sleeve and the "Google not NVIDIA" attach than to Investor Day HBF-only. Author leaving "slightly less bullish" after SanDisk's pumped day is a sentiment mark, not a 2027 sample-yield print. Q4 (HBF 2027 vs slip to 2028+) is untouched. The 9x SLC+stack trade is a NAND-bit bull case *if* the category works, shared with [[Theses/285A - Kioxia]] via Flash Ventures, not a 2026 earnings line. [[Sectors/NAND Memory & Storage]] HBF question stays "probability increasing, sample window slipped."

[[Theses/NVDA - Nvidia]] is the customer of every talk (Vera Rubin ~20 TB/s HBM4 ceiling; R200 on the TFLOPS curve; B200 NVL72 in the MoE slide). Beachfront-limited HBM and decode-bound inference support the system-budget shift already in the 8-Hi / NVL576 research, and they do not create a trigger to test. [[Theses/TSM - Taiwan Semiconductor]] is the logic landlord for everyone who is not Samsung (HBM4 B-die 4nm; d-Matrix N4 top die). [[Theses/BESI - BE Semiconductor Industries]] is the hybrid-bond tool implied by zHBM and by the thermal-mitigation snowflake; this note does not print a Kinex 16-Hi qual. [[Theses/AMD - Advanced Micro Devices]] is named once (MI 455 ~20 TB/s HBM4 practical). [[Theses/CBRS - Cerebras Systems]] sits on the SRAM-only ~300x corner of the (β, α) plot with Groq.

Net: architecture-not-yield is the through-line. Shortage is confirmed. MR-MUF-as-current-HBM4-moat is contradicted by the author's TC-NCF line. HBF-as-HBM-equivalent is contradicted by the 25x α gap. Nothing here is a conviction or status change.

## Source Excerpts

> "It's like 70% of a rack at this point and clearly the elephant in the room. Not exactly the most bullish thing for DRAM makers if everyone at giant industry conference is dedicating their career to reducing price of your product."

> "Samsung is gonna shill HBM-based die and processing in memory because guess who is the only memory maker with their own leading-edge foundry supply? ... This is obviously great for Samsung who has their own advanced logic foundry and doesn't have to beg TSMC for allocation (like hynix and Micron)."

> "I still remember the days when MR-MUF was part of hynix moat thesis. SK hynix actually uses TC-NCF in HBM4 now."

> "It's too simple: no multiple layers (it's just one layer), no hybrid bonding. Just. Stack. The. Damn. Logic. On. DRAM."

> "HBF is 8-16x the capacity of HBM. But $/GB isn't true TCO. What people actually care about is $/token. So you have to consider the tradeoff of bandwidth/latency which is 25x worse."

> "For HBF I was bullish going in but now am slightly less bullish and have more realism. ... No, HBF does not have the same bandwidth as HBM. There is, in fact, a trade-off."

> "HBM is like a 9x trade ratio because first you need SLC and not TLC and second you need to stack them like HBM."
