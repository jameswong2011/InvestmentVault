---
publish: false
date: 2026-08-24
tags: [research, email-backfill, JasonsChips]
source: 'https://www.jasonschips.ai/p/hot-chips-day-1-precious-memories'
source_type: web-clip
sender: jasonschips@substack.com
gmail_id: 1a031bfdcfbb7dc3
publication: Jason's Chips
---

# Hot Chips Day 1 - Precious Memories

### HBM Basics, Processing In Memory (Samsung), HBM Packaging (SK hynix), 3D DRAM (d-Matrix), High Bandwidth Flash (OXMIQ, PRAXMATI)

Jason's Chips · 24 August 2026 · https://www.jasonschips.ai/p/hot-chips-day-1-precious-memories

Hot Chips is a 3-day conference with a bunch of presenters and each day has its own distinct theme. Day 1 (today) is memory.

Very first thing you'll hear about is how bad the memory shortage is. It's like 70% of a rack at this point and clearly the elephant in the room.

Not exactly the most bullish thing for DRAM makers if everyone at a giant industry conference is dedicating their career to reducing the price of your product.

For me and my conference coverage the idea is that I am not gonna immediately take a side and opine on whether or not something will work or will not work. I am investor not PhD. But what I will do is try to make these things as easy as humanly possible to understand via unfiltered brain dump.

Also, a funny theme to notice is that every company that presents just shills their own stuff. Like Samsung is gonna shill HBM-based die and processing in memory because guess who is the only memory maker with their own leading-edge foundry supply? SK hynix shills HBM because, well, they are SK hynix.

#### Contents

1. HBM Basics
2. Processing In Memory (Samsung)
3. HBM Packaging (SK hynix)
4. 3D DRAM (d-Matrix)
5. High Bandwidth Flash (OXMIQ, PRAXMATI)

The entire newsletter is free.

## HBM Basics

Most of you know this but I always think it's worth going over the fundamentals. High bandwidth memory has high bandwidth because it's very parallel.

Therefore die needs to be bigger in order to allow this parallelism which contributes (but is not all of) to why HBM eats 3x die area vs DDR.

This conference (Hot Chips) was named after the main problem with HBM, which is that the chips get really hot.

The problem is pretty intuitive actually. The cooling is on top not the bottom but the base die processor which creates the heat is all the way at the bottom therefore chip gets very hot. Reliability degrades at high heat.

### Slide: HBM Architecture — high parallelism through multiple independent channels

Each DRAM die contains multiple independent channels. 2 pseudo-channels per channel share a Command/Address bus but have independent data buses. Bank scaling: HBM3E 128 banks/die; HBM4 256 banks/die. Example stack: 12-high DRAM on a base die with a central TSV spine.

### Slide: System Level Memory Bandwidth — HBM3E vs DDR5

| Feature | HBM3E | DDR5 |
|---|---|---|
| Core BW @ 8Gbps | 256 GB/s (256 IO * 8 Gbps) | 8 GB/s (8 IO * 8 Gbps) |
| Banks | 128 | 32 |

Combined overhead from design architecture, advanced packaging, and manufacturing complexity results in ~3X more silicon being consumed for delivering HBM3E capacity relative to DDR5. HBM3E die is larger (128 banks, central TSV PHY) vs DDR5 (32 banks, central Periphery & IO). Bandwidth/watt vs sequentiality: DDR5 stays low (CPU workload); HBM rises sharply for AI workloads (60-100% sequential).

### Slide: Thermal Challenges — thermal innovations essential to enable continued bandwidth and capacity scaling

Heat contributors: high-speed D2D interconnect; advanced functionality in base die; increasing DRAM die activity; increasing stack height. Cooling/mitigation: liquid cooling; hybrid bonding. Cross-section: cooling on top of the stack, heat source at the base die, thermal gradient hottest at bottom / coolest at top. Side mold around DRAM dice with TSV and solder between layers.

### Slide: HBM generation table

| Spec | HBM1 | HBM2 | HBM2E | HBM3 | HBM3E | HBM4 |
|---|---|---|---|---|---|---|
| Timeline | 2014 | 2018 | 2020 | 2022 | 2024 | 2026 |
| # Channels | 8 | 8 | 8 | 16 | 16 | 32 |
| # Pseudo-Channels (PC) | - | 16 | 16 | 32 | 32 | 64 |
| PC Width (bits) | 128 | 64 | 64 | 32 | 32 | 32 |
| Burst Length | 2 | 4 | 4 | 8 | 8 | 8 |
| Prefetch (bits) | 256 | 256 | 256 | 256 | 256 | 256 |
| Data I/O's | 1024 | 1024 | 1024 | 1024 | 1024 | 2048 |
| Nominal Data Rate (Gbps) | 1 | 2.4 | 3.6 | 6.4 | 8 | 11 |
| Nominal Bandwidth (GB/s) | 128 | 307 | 460 | 819 | 1024 | 2800 |
| DRAM Density (Gb) | 2 | 8 | 16 | 16 | 24 | 24 |
| DRAM Stack Height | 4 | 4/8 | 4/8 | 8/12 | 8+ | 8+ |
| Cube Capacity (GB) | 1GB | 4/8GB | 8/16GB | 16/24GB | 24GB+ | 24GB+ |

## Processing In Memory (Samsung)

This is fascinating. General idea is that if you can do some computation on the base die, you have to send less data from HBM to logic die. Think about if you're doing a complex math problem, instead of sending the entire starting problem back and forth between the memory and the processor, if the memory can get you to an intermediate solution already, you would only need to send that intermediate solution over to the processor. There is much less I/O.

It is necessary because compute is scaling faster than HBM memory bandwidth. And decode (attention/FFN) is memory bandwidth bound so this is the exact thing you don't want.

By reducing data transferred you also help the power requirement and therefore the thermals.

HBM base die currently is only a passive router, so arguably we can make it work harder. It only handles the communication channel to the compute die (the PHY) and test functions for the DRAM stack.

In the future base die can do a lot more stuff like the memory controller (moved off the xPU, freeing that area for compute), RAS sensors and self-test, connecting external memory directly through the base die, and eventually processing elements that do compute in the base die itself.

This also makes HBM a much more customized and less commoditized product.

This is obviously great for Samsung who has their own advanced logic foundry and doesn't have to beg TSMC for allocation (like hynix and Micron) and also happens to make HBM. Also leading edge logic base die reduces power.

They can do this by reducing HBM PHY (portion of chip dedicated to the physical I/O interface that talks to the GPU) region. On advanced logic, the PHY shrinks to a small D2D interface. That frees up the rest of the die.

The challenge again is thermal hotspots due to higher power density.

And they actually have a pretty smart solution for this. PHY is hot. PHY is also on the side. So why not extract heat from side instead of top?

Next is zHBM. This is a common 2030+ type hype technology. Requires hybrid bonding and rocket science.

For ultimate bandwidth hack, just stack HBM on top of the XPU.

Can also reduce power significantly. Which is necessary to save thermals. Would also be 4 hi instead of 8 hi also in order to save thermals. So thermal issue might actually not be as big of issue.

### Slide: Processing In/Near Memory

- Use the base die in HBM
- Custom memory chips for higher performance
- Analog Neural Nets (ANN) for the low end
- Software support is currently weak (this is a gating factor)
- Could ease memory wall issues

### Slide: Memory wall — memory technology has become a key factor limiting AI system performance

Normalized performance 2017-2027 (log): TFLOPS grow 3x every 2 years (TPU v3, A100, TPU v4, H100, MI300X, B100, TPU v5, B200, R200). HBM BW grows <2x every 2 years (HBM2E, HBM3, HBM3E, HBM4). Architectural evolution: 2.5D attached memory → 2.5D advanced memory → Processing in Memory (PIM).

### Slide: Roofline — memory bound vs compute bound

Memory-bound region: processors wait for more data. Increasing memory bandwidth steepens the diagonal. Compute-bound region: data arrives fast enough; plateau is maximum ops (varies by GPU).

### Slide: Phase #2 — Processing Elements Offloading

Concept and benefit: offloads partial xPU SoC computation to Processing Elements (PEs) in the B-die. Reduces D2D bandwidth requirements, lowering power and thermal overhead.

### Slide: Toward Custom HBM: Concept and Motivation

Exploring value-added features for the logic B-die. Standard HBM (sHBM) B-die is limited to basic data and test path functions. Key idea: leverage advanced logic processes to build SoC-like B-dies. Custom HBM (cHBM): customize the B-die logic while still sharing standard C-die stacks. sHBM B-die floorplan: HBM PHY / TSV Area / Test. cHBM B-die floorplan: custom logic in the former PHY and Test regions, TSV Area retained.

### Slide: HBM and xPU SoC process roadmap

| Year | 2016 | 2019 | 2021 | 2023 | 2026 | 2027 |
|---|---|---|---|---|---|---|
| Generation | HBM2 | HBM2E | HBM3 | HBM3E | HBM4 | HBM4E |
| HBM C-die (DRAM) | 2*nm | 1*nm | 1*nm | 1*nm | 1*nm | 1*nm |
| HBM B-die | 2*nm (DRAM) | 1*nm (DRAM) | 1*nm (DRAM) | 1*nm (DRAM) | 4nm (Logic) | 4nm (Logic) |
| xPU SoC (Logic) | 16n/12nm | 8n/4nm | 4nm | 4nm | 3nm | <3nm |

HBM4 is the generation where the B-die leaves DRAM process for 4nm logic.

### Slide: PHY footprint scaling across HBM generations

Conventional trend HBM2 to sHBM4: PHY footprint and channel length expand to achieve higher BW. Inflection: advanced logic for custom HBM (cHBM) from HBM4 reduces PHY and D2D areas.

| Generation | Die type | MPGA | PHY area | CH depth |
|---|---|---|---|---|
| HBM2 | Standard | 11.87mm x 7.75mm | 6mm x 1.2mm | 3.5mm |
| HBM3 | Standard | 10.75mm x 10.75mm | 8mm x 3mm | 4.5mm |
| sHBM4 | Standard | 11mm x 12.8mm | 8mm x 4mm | 5.5mm |
| cHBM4 | Custom | (not listed) | 8.5mm x 1.5mm (D2D) | 2mm |
| sHBM5 | Standard | 10.7mm x 16.3mm | 9.5mm x 1.7mm | 2mm |
| cHBM5 | Custom | 10.7mm x 16.3mm | ? (D2D) | ? |

PHY area based on bump map. Benefit of PHY shrinkage: shorter channel length improves energy efficiency (lower pJ/b). Challenge: higher power density creates thermal hotspots in the smaller PHY regions.

### Slide: Phase #1 Thermal Challenge and Solution — HPB (Heat Path Block)

Built on Samsung cHBM4 design experience. Dramatically reduces peak temperature by >35% with >50% PHY coverage ratio.

| Product | I/O speed | Power density | Thermal |
|---|---|---|---|
| sHBM4E | 14 Gbps | 0.5 W/mm2 | stable |
| sHBM5 | >28 Gbps | >2.0 W/mm2 | needs HPB to reach stability |

HPB is a vertical heat path beside the core-die stack (side extraction, not top-only). sHBM5 without HPB: intense PHY hotspot. With HPB coverage target >50%: hotspot reduced.

### Slide: Vertical integration and zHBM

Industry trend: AI memory architecture is rapidly moving toward tightly coupled solutions. Challenge (AGI and inference): maximizing bandwidth (TPS) within strict power limits. Ultimate solution (zHBM): true 3D vertical integration of the xPU and C-die stack, eliminating the 2.5D interposer. sHBM/cHBM: xPU and HBM side-by-side on an interposer; data path down into interposer then up into the stack. zHBM: xPU at the bottom, interlayer die, C-die stack on top; vertical data path; no 2.5D interposer.

### Slide: Power reduction — primary advantage is a dramatic decrease in I/O power

I/O optimization removes SERDES (data align / DQ I/O) to eliminate unnecessary power overhead. Power efficiency: zHBM ~70% power reduction vs HBM5. System-level: 1x GPU + 4x HBM4E vs 1x GPU + 4x zHBM. DRAM BW: 230% increase for zHBM vs HBM4E. DRAM power: 100W saving vs HBM4E. GPU power: 8.3% increase (power saved on DRAM reallocated to GPU within the same envelope). Author note: zHBM would also be 4-hi instead of 8-hi to save thermals.

## Packaging (SK hynix)

I still remember the days when MR-MUF was part of hynix moat thesis. SK hynix actually uses TC-NCF in HBM4 now.

I don't think there was anything too new about this presentation. This is the stuff that they've been doing since 2023 and doing a good job at.

### Slide: HBM PACKAGE TECHNOLOGIES (SK hynix)

| Feature | TC+NCF | MR+MUF |
|---|---|---|
| Bonding | Thermo-compression with Non-Conductive Film | Mass reflow + molded underfill |
| Inter-layer material | NCF | MUF |
| Productivity | Low (each die bonded individually) | High (whole stack at once) |
| Thermal | High thermal resistivity (worse) | Low thermal resistivity (better) |
| Warpage | Less sensitive to thin-die warpage | Sensitive to chip warpage; narrow gap-fill challenges |
| Encapsulation | EMC | MUF |

### Slide: HBM PROCESS FLOW, SK HYNIX

Wafer (Base/Core) → WT (Wafer Test) → WLP and KGSD (Known Good Stacked Die) wafer → KGSD wafer test → Singulation and 6D inspection → HBM cube release.

FAB: (1) Silicon etch (2) TSV Cu fill (3) TSV Cu CMP (4) BEOL metallization. Bumping/stocking: (5) Front-side bump (6) Wafer solder reflow (7) Temporary carrier bonding (8) TSV exposure and back-side passivation (9) Passivation CMP and TSV Cu exposure (10) Back-side bump (11) Carrier debonding and thin-wafer mount on tape (12) Chip stacking and PKG assembly with overmold = KGSD wafer. Then KGSD test, singulation and 6D inspection, HBM cube (slide shows HBM3E cube), SiP assembly and SiP test (OSAT), customer system (fabless).

### Slide: SK HYNIX'S HBM PACKAGE, KEY TECHNOLOGIES (source: IEDM 2018)

1. Via (TSV) formation: Si via etch, liner/barrier metal deposition, high-AR Cu filling. Concerns: KOZ, IMD integrity, Cu contamination.
2. Wafer thinning: temporary bonding/debonding, thinning/via reveal. Concerns: TTV control, adhesive residue, throughput, backside passivation.
3. Micro-bump formation: electroplating. Concerns: process uniformity, yield, mechanical and thermal reliability.
4. Chip stack / underfill: post gap-fill using mass-reflow molded underfill (MUF). Concerns: thin-die handling, warpage, voids and adhesive failure, joint reliability.

## 3D DRAM (d-Matrix)

This presentation was objectively great. Very easy to follow and understand. Here goes my explanation.

SRAM is very fast but too big and expensive.

High Bandwidth Memory isn't high bandwidth enough (but has great capacity).

d-Matrix solution is stacking compute on memory which they call 3D DRAM. High bandwidth because no beachfront limitation and high capacity because it's still DRAM.

Most of inference time is spent on decode which is memory bandwidth bound.

Pitch is 3D DRAM = speedy inference that doesn't bankrupt you.

This is actually really compelling. It's not even funny. It's like everyone's breaking their neck trying these esoteric solutions, and these guys are literally saying to just stack logic on DRAM. It's too simple: no multiple layers (it's just one layer), no hybrid bonding. Just. Stack. The. Damn. Logic. On. DRAM.

### Slide: SRAM: Bandwidth Advantage

Why SRAM is fast: 6T cell with direct bit-line access; on-die (no interposer or package crossing); sub-ns access latency.

Corsair SRAM Accelerator specs (card pair): bandwidth 300 TB/s; capacity 4 GB; latency ~1 ns; I/O energy ~0.5 pJ/bit.

Why SRAM cannot scale: 6T cell is 10x larger than a DRAM 1T1C cell; bitcell size frozen at ~0.021 um2 across TSMC N5, N3E, and N2 (TSMC IEDM/ISSCC); leakage tens of watts at GB scale; practical limit ~4 GB per card pair; 100x the cost of DRAM. Footer: SRAM is the fastest memory in silicon. Example use case: draft model in frontier-LLM speculative decoding.

### Slide: HBM: The Bandwidth Issue

HBM provides high capacity: 1T1C cell, high array density; 8-16 core dies per stack; 8 stacks per package.

HBM BW is challenging to scale to SRAM-like numbers: pin speed and IO width (per HBM base die) have improved slowly; number of stacks is beachfront limited; dedicating the entire die beachfront to HBM forces harder packaging (interposer size, warpage). Practical limit with HBM4 (Vera Rubin, MI 455): ~20 TB/s.

HBM-4 architecture: substrate, interposer, HBM stack (base die + PHY + 4-16 DRAM dies, 2048 wires) beside accelerator die (PHY, 20+ mm width). Topologies: (a) 1x4 = 8 HBM edges (2 per die x 4); (b) 2x2 edge only = 4 HBM edges; (c) 2x2 + interstitial = 6 HBM edges.

### Slide: Why 3D-DRAM?

| Architecture | Capacity | Bandwidth | Power |
|---|---|---|---|
| SRAM (on-die, compute + SRAM per tile) | Low | High | Low |
| HBM (2D package + beachfront) | High | Low | High |
| 3D DRAM (stacked compute-on-memory, vertical IO) | Medium | High | Low-Medium |

Energy ladder:

| Memories and interconnect | Energy / bit |
|---|---|
| SRAM (on-die) | ~50 fJ |
| On-chip wire | ~35 fJ/mm |
| 3D vertical IO | 0.3-0.4 pJ |
| Interposer trace | ~500 fJ/mm |
| 2.5D HBM4 (system) | 2.5 pJ + 3 pJ (on chip) |

3D IO lands ~10x below HBM energy. Yield: 3D DRAM uses a larger die with fewer layers (≤4 layers) vs HBM (12-16 layers). Performance: SRAM-class bandwidth at ~1/10th the energy of HBM (short 3D vertical IO, no sideways data movement, no PHY, no beachfront limit).

### Slide: Majority of wall-clock inference time is spent in decode

Raptor 72-card system. Decode (memory-bound) is the critical part of overall inference runtime.

GLM 5.2 (MLA + DSA): 4K prefill / 128 decode → decode ~81%; 4K / 1K decode → ~97%; 1M prefill / 4K decode → prefill ~76% (outlier); multi-turn 8K/1M context with 64 or 512 decode → decode 90-99%.

Kimi K3 (KDA + NoPE-MLA): 4K / 128 → decode ~71%; 4K / 1K → ~95%; 1M / 4K → prefill ~86%; multi-turn decode 83-99%.

### Slide: HBM4 vs 3D-DRAM (d-Matrix)

Top die: TSMC N4 logic. Bottom die: 3D DRAM. Integration: 36 um face-to-face stacking. Proven low cost, high volume, high yield process.

| Parameter | HBM4 | 3D-DRAM |
|---|---|---|
| Topology | 2.5D (beside) | F2F (below) |
| I/O energy | 2-3 pJ/bit | 0.37 pJ/bit |
| BW / card | 18 TB/s | 100+ TB/s |
| Capacity | 192 GB | 32 GB |

3D-DRAM vs HBM4: 5.6x higher BW / card; 5-8x lower energy / bit; 7x denser I/O.

## High Bandwidth Flash (OXMIQ, PRAXMATI)

HBF is 8-16x the capacity of HBM.

But $/GB isn't true TCO. What people actually care about is $/token. So you have to consider the tradeoff of bandwidth/latency which is 25x worse.

Memory bandwidth is important when you have high batch size (high throughput) and high interactivity (speedy inference). They are the opposite sides of the same tradeoff, so it is when you are pushing the Pareto frontier.

This graph is awful but maybe someone will find it helpful.

When you are trying to push that Pareto frontier you are memory bandwidth constrained and HBF will have tons of unused capacity.

HBF only useful for low batch size thus low bandwidth demand scenarios when you can use fewer GPUs and HBF stacks to serve the same tokens. So you can fill up the entire HBF.

Think about a small personal local or private enterprise workload. Smol box not big rack.

Another interesting use case is expert parallelism where in the FFN stage you put multiple experts on separate GPUs.

HBF thrives here because you cut down the amount of communication that is needed because more of the experts that are in the same place.

For HBF I was bullish going in but now am slightly less bullish and have more realism. If you haven't seen Sandisk Investor Day they PUMPED. But it's SanDisk. No, HBF does not have the same bandwidth as HBM. There is, in fact, a trade-off. But think about how mature the HBM ecosystem is and how much R&D has been poured into that, versus HBF. The fact that there are a few niche use cases today is kind of bullish because that means, as the software matures, as the systems get figured out, and as the actual design of the chip gets perfected, the HBM to HBF trade-off will start to go in HBF's favor.

But if anything interesting does come up there NAND won't even moon it will Mars. Think about it. HBM is like a 9x trade ratio because first you need SLC and not TLC and second you need to stack them like HBM.

### Slide: The (beta, alpha) memory landscape — labeled decades

X-axis (beta): cost per capacity ($/GB, relative to HBF = 1, log). Y-axis (alpha): bandwidth per GB (1/s, log).

| Technology | beta (~$/GB vs HBF) | alpha (~BW per GB) |
|---|---|---|
| NAND SSD | ~0.15x | ~0.001 |
| HBF-G1 | 1x | ~1.5 |
| HBF-G2 ("our focus") | 1x | ~3 |
| HBF-G3 | 1x | ~7 |
| LPDDR5X | ~3x | ~5 |
| HBM3E | ~10-15x | ~50 |
| HBM4 | ~10-15x | ~80 |
| HBM4E | ~10-15x | ~100 |
| SRAM-only (Cerebras, Groq) | ~300x | ~500,000 |

Callout: HBM is 25x vs HBF-G2 (~13x vs G3) on bandwidth per GB. Note: IMC / PIM / d-Matrix-style compute-in-memory escapes this plane — moves results, not bytes.

### Slide: Model personality — MoE vs Dense (HBF in AI Compute, Hot Chips 2026, OXMIQ)

Kimi-K2 (MoE) vs Llama-3.1-70B (dense) on B200 NVL72 (OxSOL). Log-log: throughput (tok/s) and interactivity (tok/s/user) vs batch size B per replica. Memory-bound region (BW drives T and I) at small B; compute-bound at large B; dense transition ~B=300.

Decode per step: b = [1 - (1 - k/N)^B] W + W0 + B · K. Interactivity I = BW / b (tok/s/user). Throughput T = B · I (tok/s). N = total experts; k = active experts per token; B = batch size; W = routed-expert weights; W0 = fixed weights (shared experts + dense); K = KV cache bytes per token.

Takeaway: MoE opens a small-B capacity sub-phase — model held in full, low bandwidth is fine. Ref: OxSOL simulations (OXMIQ); FineMoE (arXiv 2502.05370).

### Slide: EP x HBF — capacity buys back the comm (OPPORTUNITY)

Expert Parallelism: 8 GPUs, experts sharded, all-to-all every layer. HBF capacity: 2 nodes, experts local in HBF, little/no all-to-all. Cheap HBF capacity → fewer EP shards → less all-to-all comm.
