---
date: 2026-04-23
tags: [sector, moc, DRAM, HBM, memory]
status: active
sector: DRAM & HBM Memory
snapshot_of: "[[Sectors/DRAM & HBM Memory]]"
snapshot_date: 2026-04-24
snapshot_trigger: sync
snapshot_batch: sync-2026-04-24-101646
---

# DRAM & HBM Memory

## Active Theses
- [[Theses/000660 - SK Hynix]] — HBM triopoly leader, 57% Q1 2026 share, 72% Q1 op margin (memory-industry record), conviction medium pending Samsung Rubin allocation H2 2026 and BESI Kinex hybrid-bonding qual

> **Map of Content** — DRAM is the volatile-memory layer of every compute system; HBM is the AI-specific premium variant priced at 3-5x commodity DRAM. The two sub-segments now share a single physical wafer pool, a single packaging bottleneck (TSMC CoWoS), and a single demand curve (AI accelerator units × HBM-content-per-GPU). The triopoly (SK Hynix / Samsung / Micron) controls ~94% of global DRAM revenue and 100% of merchant HBM. CXMT plus Huawei's in-house HiBL form a sanctioned, technologically-decoupled Chinese sub-market. The defining 2026-2030 question is whether HBM stays a triopoly or fragments into a quadripoly with CXMT as the marginal supplier — and whether the Korean MR-MUF lead survives the hybrid-bonding transition at HBM5.

## Key Industry Questions

- **HBM4 Vera Rubin allocation split** *(status: 70/30 SK Hynix/Samsung confirmed for initial ramp; Micron excluded)*: UBS projects SK Hynix ~70% of Nvidia Rubin HBM4, Samsung ~30%, Micron locked out of the first Rubin SKU per TrendForce/KED Global. Samsung passed Nvidia's HBM4 qualification in Q1 2026 with above-spec pin speeds (11.7 Gbps standard, pushed to 13 Gbps at Nvidia's request), securing official supply and ending the HBM3E qualification miss that defined 2024-2025. The binding question is whether Samsung's 30% allocation expands toward 35-40% in H2 2026 as 1c DRAM yield (currently ~50% pilot) crosses Samsung's internal 70% threshold, which would track Gemini's "Incumbent Erosion" path (SK Hynix 62%→45% by 2030) ahead of consensus. See [[Theses/000660 - SK Hynix]] §Key Non-consensus Insights #1 and [[Research/2025-11-27 - Semis - Gemini HBM4 Market Canvas]].

- **Hybrid bonding inflection at HBM5/HBM4E** *(status: industry consensus is HBM5 = hybrid bonding; SK Hynix MR-MUF cushion expires at 20-Hi)*: Samsung committed to hybrid bonding from HBM4 generation; SK Hynix targets HBM4E-into-HBM5 transition (BESI Kinex pilot line live, qualification expected H2 2026). At 20-Hi stack height (HBM5 baseline, ~2028-2029), MR-MUF underfill physics breaks down — copper-to-copper direct bonding becomes the only path to acceptable thermals. SK Hynix's March 2026 BESI Kinex order is the market's tell that even the MR-MUF leader is buying insurance. If Samsung's hybrid bonding crosses 70% yield at 16-Hi by Q4 2026, the 2024-2026 packaging hierarchy inverts at HBM5. See [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]].

- **CXMT HBM3 production timing and yield** *(status: timeline slipping, mass production unlikely in 2026)*: CXMT targeting end-2026 HBM3 mass production using G4 16-nm node and MR-MUF packaging (explicitly copying SK Hynix process). Initial yields tracking ~50%; HBM3 still in testing with no mass-production orders booked per Digitimes (April 2026). Shanghai HBM packaging facility coming online late 2026 at 30K WSPM initial capacity. CXMT total wafer capacity targeted at 300K WSPM by end-2026 with 60K WSPM allocated to HBM (20% of total). $4.2B Shanghai STAR Market IPO planned Q1 2026 to fund expansion. The genuine threat is 2028-2029 commodity-DRAM commoditization (compresses SK Hynix's $40B commodity-DRAM segment from 30-35% gross margin to 15-20%); HBM remains insulated through at least 2028 by 1c-node gap and absent Chinese hybrid-bonding ecosystem. See [[Theses/000660 - SK Hynix]] §Key Non-consensus Insights #4.

- **Commodity DRAM pricing trajectory in 2026** *(status: TrendForce projects 55-60% QoQ Q1 2026, server allocation crowding all-DRAM-categories higher)*: Server DRAM and HBM demand crowding out client DRAM (PC, mobile, consumer) production allocation. DDR5 64GB RDIMM expected to double YoY by late 2026; tier-1 hyperscalers receiving only 40-60% of requested allocation. DDR5 profitability projected to surpass HBM3e starting Q1 2026 — first time commodity DRAM out-margins HBM in the AI era — because HBM3e enters supplier-competition phase as Samsung and Micron ramp 12-Hi capacity while DDR5 stays in single-supplier-allocation mode for 64GB/128GB modules. The HBM premium over server DDR5 narrows from 4-5x to 1-2x by end-2026. See [[Theses/000660 - SK Hynix]] §Q5 oversupply scenario.

- **HBF (High-Bandwidth Flash) hyperscaler adoption timing** *(status: SK Hynix + SanDisk + Samsung OCP standardization in flight; first GPU integration likely late 2027/early 2028 post-Rubin)*: Nvidia Rubin (H2 2026) does not natively support HBF; first GPU-side integration is post-Rubin generation. SanDisk pilot line accelerated 6 months to H2 2026 (Japan); SK Hynix H3 architecture simulation (8x HBM3E + 8x HBF + B200 GPU) shows 2.69x perf/watt, 18.8x batch size expansion, 32→2 GPU reduction. If HBF captures 10% of HBM TAM by 2030, that creates ~$10B incremental NAND-die-priced revenue at 50%+ gross margin — split largely between SK Hynix and SanDisk per OCP standardization participation. See [[Sectors/NAND Memory & Storage]] for HBF technology stack.

---

## Industry History

### Genesis (1966-1980): The American Era

DRAM was invented at IBM (Robert Dennard, 1966). Intel's 1024-bit 1103 launched the commodity-DRAM market in 1970 at 1¢/bit — the price point that displaced magnetic core memory and made silicon main memory economical. **Mostek**, founded 1969 by ex-TI engineers, invented address multiplexing with the MK4096 (1973), which fit a 4Kb DRAM into a 16-pin DIP. By the late 1970s Mostek held 85% global DRAM share. Intel, TI, and Mostek collectively dominated through the 64Kb generation.

### Japanese Conquest (1980-1991): Loss of US Leadership

Japanese conglomerates (Hitachi, NEC, Toshiba, Mitsubishi, Fujitsu) entered aggressively at the 64Kb node with manufacturing-scale strategies. Intel exited DRAM in 1985 under Andy Grove ("we don't have a memory company") — the most consequential strategic exit in semiconductor history. By 1986 most US DRAM producers (including Mostek, acquired by United Technologies then Thomson SA) had withdrawn. Japanese share peaked at >75% of global DRAM in 1988. The US Semiconductor Trade Agreement (1986) imposed price floors, ironically benefiting Korean entrants by establishing a global pricing cushion.

### Korean Ascent (1983-2002): Samsung's Industrial Industrial Triumph

**Samsung Semiconductor** (founded 1978, transferred Sharp/Micron technology in 1983) shipped Korea's first 64Kb DRAM in 1984. Samsung's countercyclical investment doctrine — building capacity into downcycles to bankrupt weaker competitors — defined the next two decades. Samsung passed every Japanese leader through the 1990s on the strength of the chaebol balance sheet absorbing two consecutive industry losses (1996, 2001) that Japanese keiretsus could not. By 2000, Samsung held the #1 DRAM position globally, a rank it would hold for 24 of the next 25 years.

**Hyundai Electronics** (1983) acquired LG Semicon (1998, Asian Financial Crisis-driven Korean government merger) for $2.1B, then renamed itself **Hynix** in 2001. Hynix nearly went bankrupt twice (2002 Korean creditor restructuring, 2009 down-cycle) before SK Group acquired control in 2011 and renamed it SK Hynix.

### The Cartel Era and Forced Consolidation (1998-2013)

The DOJ DRAM price-fixing investigation (2002-2007) established a $731M settlement — the second-largest criminal antitrust fine in US history at the time — with guilty pleas from Samsung ($300M), Hynix ($185M), Infineon ($160M), and Micron (cooperation). Five vendors plus Elpida pleaded to a 1998-2002 cartel. The settlement **did not break the oligopoly**; it disciplined it. Within a decade, four of those five vendors (Infineon, Elpida, Qimonda, Promos) exited, leaving Samsung, SK Hynix, and Micron — the modern triopoly.

| Year | Event | Structural Impact |
|---|---|---|
| 1999 | NEC + Hitachi DRAM operations merge → Elpida | Japanese consolidation begins |
| 2006 | DRAM cartel investigation pleas settle | $731M fines; oligopoly disciplined, not broken |
| 2008-09 | Qimonda (formerly Infineon DRAM) bankruptcy with $3B accumulated losses | German DRAM exit; Samsung/Hynix absorb share |
| 2011 | SK Group acquires Hynix (renamed SK Hynix) | Korean #2 stabilizes financially |
| 2012 | Elpida bankruptcy ($5.5B liabilities — largest Japan corporate failure since JAL) | Japanese DRAM exits as standalone industry |
| 2013 | Micron acquires Elpida for ¥200B (¥60B cash + ¥140B installment) — effectively a free acquisition | Micron jumps to #3 globally; modern triopoly forms |
| 2017-18 | Samsung peak DRAM cycle — operating margin >50% on commodity DRAM | Wealth concentration; $84B Samsung Electronics annual op profit |
| 2018-19 | DRAM downcycle — prices fall 50%+; all three post YoY revenue declines | Capex discipline mantra emerges |
| 2019 | Japan-Korea trade dispute — Japan restricts fluorinated polyimide, photoresist, hydrogen fluoride exports to Korea | Korea sources 87.9% HF from Japan pre-dispute; Korean memory makers diversified to Belgian/US/Taiwanese suppliers within 18 months |
| 2021 | SK Hynix acquires Intel NAND/SSD for $9B (Phase 1: $6.61B) → Solidigm | SK Group becomes #2 NAND; QLC enterprise leadership |
| 2022 | YMTC (Chinese NAND) added to US Entity List | Bifurcates NAND equipment market; signals Chinese memory containment posture |
| 2023-24 | NAND/DRAM trough — Samsung memory division posts losses | Forced 20-30% wafer-start cuts set up 2025-2027 supply deficit |

### The HBM Era (2013-Present): Architecture as Pricing Power

HBM was conceptualized at AMD/SK Hynix (joint development 2008-2013); first JEDEC standard (HBM1, JESD235) ratified October 2013. AMD's Fiji GPU (Fury X, 2015) was the first commercial HBM product. HBM remained a niche through HBM2/HBM2E (2016-2020), used primarily in HPC accelerators and select Nvidia data-center products (Tesla V100, A100). The category was effectively dormant — sub-$3B annual revenue — until ChatGPT (November 2022) created the first AI-accelerator demand wave.

| Year | HBM Generation | Defining Event | SK Hynix Share |
|---|---|---|---|
| 2013 | HBM1 ratified | Joint AMD-SK Hynix specification | >90% (sole supplier) |
| 2016 | HBM2 | Nvidia Tesla P100 first volume HBM customer | ~70% |
| 2020 | HBM2E | A100 ramp; Samsung enters | ~50% |
| 2022 | HBM3 | H100 launch; SK Hynix wins sole-source | ~50%, growing |
| 2024 | HBM3E | H200/B200 ramp; Samsung HBM3E qualification miss at Nvidia | **62%** (peak share) |
| 2025-2026 | HBM3E 12-Hi + HBM4 12-Hi | Samsung HBM4 qualification at Nvidia ("best scores"); Rubin SKU allocation 70/30 SK Hynix/Samsung | **57%** (Q1 2026) |
| 2027-2028 | HBM4E 16-Hi | Hybrid bonding adoption inflection; Micron HBM4E custom base die | Forecast 48-52% |
| 2029-2030 | HBM5 20-Hi (4096-bit IO, 4 TB/s, 80 GB/stack) | Samsung leap-frog if hybrid bonding leads | Forecast 40-45% |

**The defining structural feature of DRAM history is asymmetric capital intensity rewarding the deepest pocket through downcycles.** From >12 producers in the 1980s to 3 in 2025. Each downcycle (1996, 2001, 2008, 2018, 2023) killed one or more competitors. The current cycle is the first where structural demand-side change (AI accelerator volume) plus capacity-allocation prioritization (HBM diversion crowds out commodity DRAM at 3:1 wafer penalty) extends the upcycle beyond historical 18-24 month patterns. Macquarie expects this cycle to extend through 2027 — vs the 6-12 months prior cycles ran.

---

## Competitive Dynamics

### Market Position Snapshot (Q1 2026)

| Vendor | DRAM Revenue Share | HBM Revenue Share | HBM4 Rubin Allocation | DRAM Capex 2026 | Strategic Position |
|---|---|---|---|---|---|
| **SK Hynix** | ~36% (overtook Samsung Q1 2025; ceded back Q4 2025) | **57%** (Q1 2026; down from 62% Q2 2025) | **~70%** initial Rubin | $13B-$29B (range; lower-end memory-focused) | Incumbent with MR-MUF process moat through HBM4/4E; hybrid-bonding insurance via BESI Kinex |
| **Samsung** | ~33% (Q4 2025 reclaim) | ~30% (rising from 17% trough Q2 2025) | ~30% Rubin | $20B+ (+11% YoY; 50% HBM capacity expansion) | Leap-frog hybrid-bonding bet; turnkey foundry+memory+AVP integration; 1c DRAM yield rising from 50% pilot toward 70% target |
| **Micron** | ~21% | ~13-25% (varies by source — 25% per Q3 2025 SK Hynix analyses; 11-13% per Counterpoint) | **0% Rubin initial** (excluded — significant) | $13.5B (+23% YoY) | Sole-source LPDDR5X for Nvidia GB300; HBM3E 12-Hi ramping; HBM4 redesign reportedly delayed parts to 2027 |
| **CXMT** (China) | ~5-6% (Q4 2025 estimate; 9-10% by 2026E) | **0% global** (HBM3 mass production targeted end-2026, slipping to H2 2026, ~50% yield) | — | $4.2B IPO + state subsidy ($142B PRC fund) | Domestic-only; 1gamma node = 3 nodes behind leaders; G4 16-nm HBM3 platform; Huawei lead customer |

**SK Hynix dethroned Samsung in DRAM revenue for the first time in Q1 2025** (36% vs 34%) — the first time since SK Hynix's 1983 Hyundai-Electronics founding. Samsung reclaimed #1 in Q4 2025 on commodity-DRAM allocation and DDR5 pricing strength. The seesaw reflects which segment is the cycle leader: when HBM is the marginal-margin product (2024-Q3 2025), SK Hynix wins; when conventional DDR5 commands premium pricing (Q4 2025-2026), Samsung's scale dominates.

### Packaging-Technology Hierarchy (the Competitive Axis)

Three vendor philosophies define the 2026-2030 share trajectory:

| Vendor | Current Packaging | HBM3E/HBM4 (12-Hi/16-Hi) | HBM4E (16-Hi/20-Hi) | HBM5 (20-Hi/24-Hi) | Strategic Bet |
|---|---|---|---|---|---|
| **SK Hynix** | MR-MUF (Mass Reflow Molded Underfill) — liquid epoxy fills gaps; thermal-conductivity advantage | MR-MUF extended to 16-Hi; yield stability | Advanced MR-MUF + parallel hybrid-bonding development (BESI Kinex pilot) | Hybrid bonding (Cu-Cu direct, no microbumps) | Process incumbent moat through HBM4/4E; insurance for HBM5 transition |
| **Samsung** | TC-NCF (Thermal Compression Non-Conductive Film) → Hybrid Bonding | Hybrid bonding on HBM4 if yields hit thresholds; TC-NCF backup | Hybrid bonding standard | Hybrid bonding 20-Hi | Leap-frog technology to retake leadership at HBM5; hybrid bonding decision targeted May-June 2026 per BESI |
| **Micron** | TC-NCF pragmatic | TC-NCF HBM4 12-Hi | TC-NCF + selective hybrid bonding | Hybrid bonding HBM5 | Power-efficiency leadership (1-beta then 1-gamma node); custom base die TSMC 3nm for HBM4E |
| **CXMT** | MR-MUF (copying SK Hynix) | HBM3 only (G4 16-nm DRAM); ~50% yield | Speculative | Speculative | Domestic-only; YMTC hybrid-bonding patent pool potential domestic shortcut |

**Hybrid bonding is the "great filter" for HBM5.** At 20-Hi stack heights, MR-MUF underfill physics break down — gap-fill voids and warpage exceed acceptable thresholds. Samsung's hybrid-bonding gamble (BESI Kinex tool + AMAT Kinex platform, ~$10.7M per system) is timed to hit yield maturity 12-24 months ahead of SK Hynix. If Samsung clears 70% hybrid-bonding yield at 16-Hi by Q4 2026, the 2024-2026 share trajectory inverts at HBM5. SK Hynix's March 2026 BESI Kinex order = explicit acknowledgment that MR-MUF is a temporary cushion, not a permanent advantage.

### Logic Base Die — Foundry Lock-in

HBM4 introduces foundry-fabricated logic base dies (replacing the legacy memory-process buffer dies). This adds vendor lock-in dynamics absent from prior generations:

| Vendor | HBM4 Base Die Process | HBM4E Base Die Plan | Foundry Partnership |
|---|---|---|---|
| **SK Hynix** | TSMC 12FFC+/N5 | **TSMC 3nm (reported, March 2026)** | TSMC strategic alliance — synchronizes HBM with Nvidia/AMD GPU process |
| **Samsung** | Samsung 4nm internal | Samsung 2nm (first time, January 2026 report) — may also offer custom designs to OpenAI ASIC | Internal "One Samsung" turnkey (memory + foundry + AVP) |
| **Micron** | TSMC partner ecosystem | TSMC custom base dies for HBM4E | TSMC custom logic for hyperscaler-specific designs |

**Vendor lock-in is the asymmetric pricing-power lever.** In HBM3 era, hyperscalers could swap SK Hynix → Samsung HBM with limited revalidation. In HBM4 era, a hyperscaler's custom base die (e.g., OpenAI Titan ASIC choosing Samsung 2nm) cannot easily port to TSMC. This makes 2026 share losses/gains "stickier" — SK Hynix's HBM4 Rubin allocation becomes structural for the Rubin/Rubin Ultra/Feynman roadmap (H2 2026 → 2028); Samsung's 30% Rubin allocation is similarly defended for the same lifecycle. **Custom HBM (HBM4 + ASIC base die) is forecast at ~33% of total HBM market in 2026, growing 82% YoY.**

### Pricing Power Trajectory

| Segment | Q3 2025 | Q1 2026 | H2 2026E | 2027E | 2028E |
|---|---|---|---|---|---|
| HBM3E 8-Hi ASP | Stable peak | Down ~5% YoY (supplier competition) | Down 10-15% (Goldman scenario) | Down 15-20% | Phase out |
| HBM4 12-Hi ASP | n/a | Premium $30+/GB | Stable on Rubin allocation | Down 10% as 16-Hi premium emerges | Stable on volume |
| HBM4E 16-Hi ASP | n/a | n/a | Sample pricing | **Premium 1.5-2x HBM4 12-Hi** | Volume |
| Server DDR5 (64GB RDIMM) | +30-40% QoQ | **+55-60% QoQ** (TrendForce) | **Doubles YoY** by late 2026 | Stable peak | Soften |
| Server DDR5 (128GB RDIMM) | Allocation-only | 40-60% of hyperscaler ask filled | Continued shortage | Eases late 2027 | Normalize |
| LPDDR5X (mobile/data center) | +20-25% QoQ | +25-30% QoQ | Premium pricing on Nvidia GB300 sole-source (Micron) | Stable | — |
| 1Tb DDR5 die (spot) | $4.80 | $10.70 (+123%) | Continued tightening | Peak | Soften |

**The 2026 inversion: DDR5 profitability surpasses HBM3e for the first time since 2024.** TrendForce projects this in Q1 2026 because (1) HBM3e becomes a three-supplier-competitive product as Micron and Samsung 12-Hi capacity comes online, while (2) DDR5 64GB/128GB modules remain effectively sole-supplier-allocated due to fab-space crowding-out by HBM. The HBM premium over server DDR5 narrows from 4-5x (peak 2024) to 1-2x by end-2026. This is the first cycle where HBM is the de-rating product and conventional DRAM is the re-rating product — counterintuitive to consensus framing.

### The 3:1 Wafer Penalty (Structural Supply Constraint)

To produce one HBM-grade wafer, vendors sacrifice three wafers of standard DDR5 capacity: HBM requires extensive TSV (Through-Silicon Via) formation, 1c DRAM die (premium-process), longer cycle times, and larger die area for the 2048-bit interface. As HBM share of DRAM revenue rises from 18% (2024) → 33% (2025) → 50%+ (2030E per Yole), commodity-DRAM bit supply growth structurally lags demand growth. **AI is forecast to consume 20% of global DRAM wafer capacity in 2026.**

---

## Product-Level Analysis

### HBM Generational Roadmap (JEDEC + Vendor-Specific)

| Generation | Years | Interface Width | Per-Pin Speed | Per-Stack Bandwidth | Stack Heights | Capacity per Stack | Key Architectural Change |
|---|---|---|---|---|---|---|---|
| HBM1 | 2015-2016 | 1024-bit | 1 Gbps | 128 GB/s | 4-Hi | 1 GB | First TSV-stacked DRAM |
| HBM2 | 2016-2020 | 1024-bit | 2-2.4 Gbps | 256-307 GB/s | 4/8-Hi | 2-8 GB | Volume HPC adoption |
| HBM2E | 2020-2022 | 1024-bit | 3.2-3.6 Gbps | 410-461 GB/s | 8-Hi | 8-16 GB | Nvidia A100 era |
| HBM3 | 2022-2024 | 1024-bit | 6.4 Gbps | 819 GB/s | 8/12-Hi | 16-24 GB | Nvidia H100/H200 era; SK Hynix sole-source |
| **HBM3E** | 2024-2026 | 1024-bit | 8-9.6 Gbps | 1.0-1.2 TB/s | 8/12-Hi | 24-36 GB | B200/Rubin compatibility; Samsung qualification miss |
| **HBM4** | 2026-2028 | **2048-bit** (doubled) | 8-13 Gbps | **2.0-2.8 TB/s** | 12/16-Hi | 36-64 GB | Foundry-class logic base die; Samsung HBM4 11.7-13 Gbps to Nvidia |
| HBM4E | 2027-2029 | 2048-bit | 11+ Gbps | 2.5-3.2 TB/s | 16-Hi | 48-72 GB | Hybrid-bonding inflection; custom base dies for ASIC |
| HBM5 | 2028-2031 | 4096-bit (doubled) | 8 Gbps | **4 TB/s** | 16-20-Hi | 80 GB | Hybrid bonding mandatory; ~100W per stack; immersion cooling |
| HBM6 | 2032+ | 4096-bit | 16 Gbps | **8 TB/s** | 20-Hi | 96-120 GB | Multi-tower interposer; on-die network switch |

### Vendor HBM Product Specifications (Q1 2026)

| Product | Vendor | Stack | Bandwidth | Capacity | Customer | Status |
|---|---|---|---|---|---|---|
| HBM3E 12-Hi | SK Hynix | 12-Hi | 1.2 TB/s | 36 GB | Nvidia B200, B300 | Volume; ~80% yield |
| HBM3E 12-Hi | Micron | 12-Hi | 1.2 TB/s | 36 GB | Nvidia GB200/300; AMD MI350 | Volume; mid-2025 ramp |
| HBM3E 12-Hi | Samsung | 12-Hi | 1.0 TB/s | 36 GB | AMD MI350 (qualified); Nvidia (HBM3E qualification miss) | Volume to AMD |
| HBM4 12-Hi | SK Hynix | 12-Hi | 2.0 TB/s | 36 GB | Nvidia Vera Rubin (~70% allocation) | Mass production Q1 2026 |
| HBM4 12-Hi | Samsung | 12-Hi | 2.0-2.6 TB/s (11.7-13 Gbps) | 36 GB | Nvidia Vera Rubin (~30% allocation), AMD MI400 | Mass production Q1 2026 |
| HBM4 12-Hi | Micron | 12-Hi | 2.0+ TB/s | 36 GB | AMD MI400; Nvidia (excluded from initial Rubin) | Volume 2026; redesign reportedly slipped 2027 |
| HBM4E 16-Hi | All three | 16-Hi | 2.5-3.2 TB/s | 48 GB | Vera Rubin Ultra (H2 2027); Nvidia Feynman (2028) | Sampling H2 2026 |
| **HiBL 1.0** | Huawei (in-house) | 12-Hi (estimate) | 1.6 TB/s | 128 GB | Ascend 950PR (Q1 2026) | Production; SMIC N+3 process |
| **HiZQ 2.0** | Huawei (in-house) | 16-Hi (estimate) | 4 TB/s | 144 GB | Ascend 950DT (Q4 2026) | Sampling |

### Conventional DRAM Product Hierarchy (April 2026)

| Product Class | Vendor Strength | Process Node | Use Case | Pricing Trajectory |
|---|---|---|---|---|
| DDR5 server RDIMM (64GB/128GB) | Samsung scale leader; SK Hynix 1c-node leader | 1b/1c (Samsung 1c yield ~50% pilot, 70% target end-2026) | Hyperscaler general-purpose servers | **2x YoY by late 2026**; tier-1 hyperscalers receiving 40-60% of ask |
| DDR5 client UDIMM | Samsung volume leader | 1a/1b | PC, workstation | +40-50% Q1 2026 QoQ |
| DDR4 (legacy) | Samsung exits; Micron exits; CXMT, Nanya, Winbond expanding | Mature | Industrial, telecom, embedded | Spot prices doubled 2025; allocation tight through 2027 |
| LPDDR5X (mobile + data center) | **Micron sole-supplier to Nvidia GB300** | 1b | Smartphones, Nvidia data-center superchips | Premium (Nvidia GB200/GB300 LPDDR doubled with rack volume) |
| GDDR7 graphics DRAM | SK Hynix leader; Samsung, Micron parity | 1b | Nvidia GeForce, AMD Radeon, AI training secondary tier | Premium; AI demand consumption rising |

### The "Bit Crossover" Year 2026

By end-2026, HBM bit shipments cross 50% of DRAM bit shipments at SK Hynix and ~40% at Samsung. HBM is now the dominant bit-volume product as well as the dominant revenue product at SK Hynix. Within the AI server market, HBM + LPDDR5X + DDR5 RDIMM combined consume ~35% of all DRAM wafer capacity globally — a category that did not meaningfully exist 4 years ago.

---

## Acquisitions and New Entrants

### Major M&A History (DRAM Sub-Sector)

| Year | Acquirer | Target | Price | Strategic Rationale | Outcome |
|---|---|---|---|---|---|
| 1998 | Hyundai Electronics | LG Semicon | $2.1B | Korean government-forced post-Asian-crisis consolidation | Created Hynix; later renamed SK Hynix |
| 1998 | Micron | Texas Instruments memory | ~$1B | US DRAM consolidation around Micron | Cemented Micron as #3 globally |
| 1999 | NEC + Hitachi (JV) | DRAM operations merged | n/a | Japanese consolidation against Korean cost advantage | Created Elpida — Japan's last DRAM hope |
| 2009 | (none) | Qimonda bankruptcy | $3B accumulated losses | Failed to compete; German government $500M support insufficient | Capacity absorbed by Samsung/SK Hynix |
| 2011 | SK Group | Hynix (35% stake) | KRW 3.4T | Korean-conglomerate ownership stabilizes #2 player | SK Hynix renamed; financial discipline |
| 2013 | Micron | Elpida | ¥200B (¥60B cash) | Japanese DRAM exit; absorption of remaining Tier-2 | Modern triopoly forms; Micron #3 cemented |
| 2021 | SK Hynix | Intel NAND/SSD (→ Solidigm) | $9B (Phase 1 $6.61B) | NAND vertical integration; QLC enterprise leadership | SK Group #2 NAND; Solidigm 51% QLC share by 2025 |
| 2025 | SK Hynix | Solidigm Phase 2 | $1.9B remaining | Final IP + R&D + workforce transfer (March 2025) | Full Solidigm consolidation |
| 2025 | (Carve-out) | Samsung HBM division reform | n/a | "AI-innovation oriented approach" — $73.2B 2026 capex | HBM4 mass-production focus |
| 2026 | (Planned IPO) | CXMT Shanghai STAR | $4.2B raise (29.5B yuan) | Domestic-funded HBM expansion under sanctions | 2nd-largest STAR Market IPO since 2019 |
| 2026 | (Rumored) | Solidigm IPO carve-out | Target $15-25B valuation | Crystallize hidden NAND value inside SK Hynix consolidated cap | Targeted post-Kioxia float re-pricing window |

### New Entrants and Disruptors

**CXMT (ChangXin Memory Technologies) — DRAM disruptor:**
- Founded 2016 with Hefei municipal + state-level subsidy backing (~$24B+ cumulative subsidies estimated)
- Achieved 1ynm DDR4 production 2020; 1z (~17nm) DDR4 by 2022; 1alpha (~14nm) by 2024; G4 (16nm) for HBM3 by 2026
- ~3 nodes behind SK Hynix's 1c (~10nm-class) leading-edge
- Total wafer capacity targeted at 300K WSPM by end-2026 (vs SK Hynix ~620K target, Samsung ~750K)
- HBM3 mass production targeted end-2026; ~50% yield in initial samples; explicitly copying SK Hynix MR-MUF process
- $4.2B Shanghai STAR Market IPO planned Q1 2026; second-largest since STAR launch
- Customer base: Huawei (lead), Cambricon, Biren, Moore Threads (Chinese AI accelerator designers)
- US export-control posture: hard line on HBM as "choke point" per January 2026 framework update; CXMT cannot access leading-edge ASML EUV (no scanners imported); confined to DUV multi-patterning at trailing-edge

**Huawei in-house HBM (HiBL/HiZQ) — vertically-integrated entrant:**
- HiBL 1.0: 128 GB capacity, 1.4-1.6 TB/s bandwidth, paired with Ascend 950PR (Q1 2026 production; SMIC N+3 process)
- HiZQ 2.0: 144 GB capacity, 4 TB/s bandwidth, paired with Ascend 950DT (Q4 2026)
- Marketed as "more cost-effective than HBM3E/HBM4E" — lower-spec but vertically integrated cost structure
- Dies fabricated by SMIC; packaging by Tongfu Microelectronics (CoWoS-equivalent domestic packaging)
- 2026 die volume target: ~1.6M dies for the Ascend 950 family
- ByteDance committed $5.6B for Ascend 950PR; ~750K-unit shipment target FY2026
- Strategic implication: removes the SK Hynix/Samsung HBM chokepoint for the Chinese AI compute stack — the most consequential supply-chain decoupling event in memory since the 1990s

**YMTC (Yangtze Memory Technologies) — NAND vendor with hybrid-bonding patent pool:**
- Primarily NAND (see [[Sectors/NAND Memory & Storage]])
- Wafer-to-wafer hybrid-bonding patent portfolio reportedly larger than SK Hynix and Samsung combined
- Strategic convergence with CXMT plausible: YMTC hybrid-bonding IP applied to CXMT DRAM stacking could enable "Hybrid HBM" pathway bypassing restricted Western packaging tools
- Samsung licensed YMTC's hybrid-bonding patents for V10 NAND (March 2026) — first time Samsung NAND depended on external IP and an Entity-List-restricted vendor

### Why No US/EU/Japan Re-entry

The DRAM industry has not seen a meaningful new entrant in 30+ years (CXMT excepted, and only with state subsidy). Three structural barriers:

1. **Capital intensity**: A modern DRAM fab requires $20-30B with 5-7 year payback under best-case pricing
2. **Process knowledge**: 1c DRAM EUV process mastery requires 8-15 years of cumulative engineering — Samsung's 50% pilot yield reflects this learning curve even with $73B 2026 capex available
3. **Customer qualification**: Hyperscalers and Nvidia require 12-18 month qualification cycles with sustained reliability data — a barrier YMTC and CXMT face in international markets, and that protects the triopoly globally

**The CXMT IPO + Huawei HiBL combination is the first credible new-entrant ecosystem in 30 years.** Whether it remains a sanctioned domestic-only ecosystem (base case through 2028) or merges into the global supply chain (low-probability scenario) is the binary question for the long-term DRAM market structure.

---

## Macro Shifts

### 1. AI Accelerator Unit Growth Binds HBM Demand (Current — Structural)

HBM demand is now mechanically tied to AI accelerator unit shipments × HBM-content-per-GPU. Both are accelerating:

| Driver | 2024 | 2026E | 2030E | Compounding Factor |
|---|---|---|---|---|
| Total HBM revenue | $17B | $42-62B | $90-101B | Yole CAGR 33% |
| HBM as % of DRAM revenue | 18% | 33% | 50%+ | Inversion of historical commodity-DRAM dominance |
| HBM content per Nvidia GPU | 80GB (H100) | 192GB (B200) → 288GB (Rubin) | **1TB (Rubin Ultra HBM4E)** | 12.5x in 6 years |
| HBM content per AMD GPU | 192GB (MI300X) | 288GB (MI350) → 432GB (MI400) | 600GB+ (MI500) | 3.1x in 5 years |
| AI capex (hyperscaler) | $256B | $602B (Microsoft, Google, Meta, Amazon, Oracle) | $1T+ | 4x in 6 years |

**The supply side is structurally constrained through 2027.** All three vendors' 2026 HBM capacity is sold out; 2027 allocations are being negotiated; M15X (SK Hynix) and Samsung P4/P5 expansions don't deliver incremental supply at scale until late 2026/2027. 2028 is the earliest year supply may catch demand under base-case AI capex trajectories.

### 2. CoWoS Packaging as the True AI Bottleneck (Current — Structural)

HBM dies are useless without TSMC CoWoS (Chip-on-Wafer-on-Substrate) integration with the GPU/ASIC. CoWoS capacity is the binding constraint, not HBM dies:

| Year | TSMC CoWoS Capacity | Status | Limiter for AI Compute |
|---|---|---|---|
| 2024 | 35K-40K WSPM | Baseline | Nvidia pre-booked 60-65% |
| 2025 | 75K-80K WSPM | +100% YoY | Sold out |
| 2026E | 100K-130K WSPM | +60-80% YoY (TSMC quadrupling) | Tight; CoWoS-L sold out, OSAT partners (ASE CoWoP) stepping in |
| 2027E | ~150K+ WSPM | Continued expansion | Potential equilibrium |

Nvidia pre-booked 60-65% of TSMC's 2026 CoWoS output; AMD secured ~11% for MI400. **Without CoWoS, HBM dies sit on shelves.** This makes TSMC the upstream constraint for HBM revenue realization, capturing 30-40% gross margin on every CoWoS wafer that contains HBM.

### 3. ASML EUV Equipment as Upstream Equipment Dependency (Current — Locked-in)

1c DRAM (10nm-class) requires extensive EUV layers. SK Hynix placed a $7.9B ASML order in 2025 to enable 1c capacity expansion (160-190K WSPM by end-2026, 800% expansion). ASML installed the **first commercial High-NA EUV system at SK Hynix's Icheon DRAM fab in September 2025** — ahead of any logic foundry. 1c uses at least 5 EUV layers (vs 3 in 1b). ASML captures ~8% of SK Hynix's DRAM capex as pure equipment margin. Samsung and Micron similarly committed to 1c EUV ramps.

**ASML is the equipment-layer monopolist** — see [[Theses/ASML]] (if exists) and [[Sectors/Semiconductor Capital Equipment]]. No 1c DRAM scaling without ASML. No HBM4/HBM4E without 1c DRAM. Equipment-layer pricing power passes through to HBM cost structure.

### 4. The 3:1 Wafer Penalty — Structural Cross-Cannibalization (Current — Worsening)

To produce one wafer of HBM-grade DRAM, vendors sacrifice three wafers of standard DDR5. As HBM shifts from 18% (2024) → 33% (2025) → 50%+ (2030E) of DRAM revenue, the bit-shipment penalty cascades:

- 2026: HBM consumes ~20% of global DRAM wafer capacity but generates 33% of revenue
- Server DDR5 RDIMM (64GB/128GB) experiences allocation rationing — hyperscalers receiving only 40-60% of ask
- Client DRAM (PC, mobile) prices doubled YoY by late 2026 as suppliers prioritize server allocation
- Smartphone OEMs (Samsung, Apple supply chain) downgrading specs to manage memory cost

The 3:1 penalty is the mechanism by which the AI memory cycle generates pricing power across the entire DRAM stack, not just HBM. **DDR5 profitability surpasses HBM3e in Q1 2026** for the first time since 2024 — a counter-intuitive inversion that consensus has not internalized.

### 5. Geopolitical Bifurcation (Structural — Accelerating 2026)

The DRAM/HBM market is bifurcating along US-aligned vs PRC-aligned supply chains:

| Pool | Vendors | Equipment Access | Customer Base | HBM Capability |
|---|---|---|---|---|
| US-aligned (95%+ of merchant supply) | SK Hynix, Samsung, Micron | ASML EUV, AMAT, LRCX, TEL, KLA full access | Nvidia, AMD, Broadcom, AWS, Google, Meta, Microsoft + global enterprise | HBM3E, HBM4 production; HBM5 development |
| PRC-domestic | CXMT, Huawei (HiBL) | DUV multi-patterning + domestic AMEC, Naura, Maxwell tools; export-controlled from EUV | Huawei Ascend, Cambricon, Biren, Alibaba, Tencent, ByteDance, domestic enterprise | HBM3 only (CXMT 2026); HiBL/HiZQ vertically integrated for Ascend |

The US Department of Commerce updated its export-control framework in January 2026, maintaining HBM as a "choke point" technology with case-by-case review for some chips. The bifurcation is now de facto permanent through at least 2028 absent major policy change.

**The Korean memory dependency on Japanese chemical inputs (fluorinated polyimide, photoresist, hydrogen fluoride) was largely diversified post-2019 trade dispute** — Korea sourced 87.9% of HF from Japan pre-dispute, dropped that to ~30% by 2022 via Belgian/US/Taiwan substitution. This historical episode informs how supply-chain dependencies get re-priced rapidly under geopolitical stress; the reverse case (US dependency on Korean HBM) does not have an equivalent fast-substitute.

### 6. The Taiwan Tail (Binary Structural Risk)

SK Hynix and Samsung HBM dies → Taiwan TSMC CoWoS integration → Nvidia/AMD silicon → global AI compute. A China-Taiwan kinetic event invalidates 60-80% of HBM end-market demand for 12-24 months until non-Taiwan CoWoS-class capacity can be rebuilt. SK Hynix and Samsung have **no public disclosed hedge** to this concentration. See [[Macro/AI Bubble Risk and Semiconductor Valuations]] §2026-04-19 update — TSMC stress-test rated permanent impairment at -85-92% under invasion; HBM revenue collapses synchronously with TSMC output collapse.

### 7. HBF (High-Bandwidth Flash) — New Memory Tier Creation (Emerging 2027-2030)

HBF — co-developed by SanDisk + SK Hynix + Samsung — creates a third memory tier between HBM ($8-10/GB, ~2 TB/s) and SSD ($0.10-0.20/GB, GB/s scale): NAND-die-priced (~$1/GB), 1.6-3.2 TB/s bandwidth, 512GB-1.5TB capacity per stack. SK Hynix H3 architecture simulation: HBF replacing portion of HBM in inference workload delivers 2.69x perf/watt, 18.8x batch size, 32→2 GPU reduction. OCP standardization workstream in flight (target H2 2026). First Nvidia GPU integration likely late 2027/early 2028 (post-Rubin). If HBF captures 10% of HBM TAM by 2030 ≈ $10B incremental revenue at 50%+ gross margin shared across SK Hynix + SanDisk + Samsung. See [[Sectors/NAND Memory & Storage]] §HBF.

### 8. Algorithmic Compression Risk (Bear-Case Optionality)

TurboQuant (Google, March 2026): 6x KV-cache compression, zero accuracy loss. DeepSeek MLA: 93.3% KV-cache reduction. Both compress *dynamic* memory (KV cache) but not *static* (model weights). Per Jevons Paradox + 2026 supply reality:
- Initial market reaction: SK Hynix -6.23% intraday, Samsung -4.71% (March 24-25, 2026)
- Analyst consensus pushback: efficiency expands AI deployments; total memory demand rises despite per-token efficiency
- Long-term unresolved: if compression algorithms continue to compound (e.g., 2-bit weight quantization at <1% accuracy loss), HBM demand inflection point shifts forward by 12-24 months
- Contrarian bear: TurboQuant-class compression deployed at scale could compress 2027-2028 HBM demand growth from forecast +30-40% YoY toward +10-15% YoY — invalidating the AI memory supercycle

See [[Research/2026-03-27 - TurboQuant Impact on Memory Demand]] and [[Research/2026-01-15 - AI Compute and Memory Demands - HBM Shortage]].

---

## Investor Heuristics

### What Is Priced In (Consensus)

1. **HBM supercycle through 2026-2027.** Sell-side targets average KRW 1.43M for SK Hynix (Mirae 1.37M, Samsung Securities + IBK 1.8M, high-end 2.5M). Bank of America designates SK Hynix as memory industry "Top Pick" for 2026 supercycle. Macquarie expects cycle to extend through 2027 vs prior 6-12 month cycles.

2. **SK Hynix maintains HBM leadership.** Goldman Sachs: ">50% HBM share through 2026." UBS: 70% Rubin HBM4 allocation. The consensus view treats Q1 2026 57% share as the trough, with SK Hynix re-extending lead via HBM4E sole-source into late 2027.

3. **Samsung HBM4 recovery validated.** Morgan Stanley projects Samsung 2026 EPS +150% YoY on HBM4 + DRAM combined. The 30% Rubin allocation is treated as the baseline, not the upper bound.

4. **2026 DRAM market growth +51% YoY.** Bank of America "supercycle similar to 1990s boom." Nomura forecasts memory market +98% YoY to $445B in 2026.

5. **CXMT as a 2027-2028 risk factor.** Most sell-side models include CXMT as a future bear-case scenario, not an active 2026 concern.

### What Is Not Priced In (Non-Consensus)

**1. Incumbent Erosion path: SK Hynix 62% → 45% by 2030 is a structural regression, not a cyclical dip.** Sell-side extrapolates current 57% forward as if MR-MUF, 1c yield (~80%), and Nvidia cycle familiarity constitute a durable moat. Gemini's HBM4 Market Canvas projects Samsung "U-Shape Recovery" (24% → 33% by 2030) and Micron "Steady Climb" (15% → 21% by 2030) erode SK Hynix from 58% → 45% within five years. **Once Samsung's 1c yield crosses 70%, Nvidia's posture shifts from "SK Hynix preferred" to "dual-source at parity pricing"** — which compresses SK Hynix's blended HBM gross margin from current 60%+ toward 40-45%. Single most important non-consensus call. See [[Theses/000660 - SK Hynix]] §Non-consensus #1.

**2. The packaging hierarchy inverts at HBM5.** MR-MUF is a process moat, not an architectural one. At 20-Hi (HBM5, 2028-2029), MR-MUF physics break down — hybrid bonding becomes mandatory. SK Hynix's March 2026 BESI Kinex order = explicit acknowledgment that the company is buying insurance, not extending dominance. Samsung's hybrid-bonding lead at 2-3 years could leap-frog SK Hynix at HBM5. The market reads MR-MUF as a permanent advantage rather than a temporary cushion. See [[Theses/000660 - SK Hynix]] §Non-consensus #2.

**3. CXMT is the wrong-timing bear case.** Consensus bears treat CXMT 2027-2028 ramp as the threat. Reality: CXMT is 3 nodes behind on DRAM and has no HBM product through end-2026 with 50% yield. The genuine threat is **commodity-DRAM commoditization 2028-2029** — which compresses SK Hynix's $40B commodity-DRAM segment from 30-35% gross margin to 15-20%. HBM (60%+ gross margin, the earnings engine) is insulated through at least 2028 by 1c-node gap. The bear case that matters in 2026 is Samsung Rubin allocation expansion, not CXMT. Consensus conflates these and mis-prices the nearer threat.

**4. The DDR5/HBM profitability inversion.** Q1 2026: DDR5 profitability surpasses HBM3e for the first time in two years (TrendForce). Server DDR5 64GB RDIMM doubles YoY by late 2026 while HBM3e ASPs decline 5-15% on three-supplier competition. Samsung's commodity-DRAM scale becomes the cyclical winner, not the cyclical laggard. Sell-side models the inverse — assigning premium multiples to HBM-pure exposure when the cyclical leader is moving toward Samsung's commodity strength.

**5. HBF as a $5-10B unpriced TAM option.** Sell-side assigns zero value to HBF in SK Hynix, SanDisk, Samsung valuations because it is pre-revenue. OCP standardization (target H2 2026) + SanDisk pilot acceleration + Samsung patent activity + SK Hynix H3 simulation data = five de-risking signals the market reads as "speculative optionality." HBF is structurally different from Optane: NAND-based scalability (most-scalable memory tech in existence), multi-vendor OCP standard (not Intel-proprietary), concrete $/inference savings (32→2 GPU reduction). If HBF captures 10% of HBM TAM by 2030 = $10B+ revenue at 50%+ gross margin — currently unmodeled.

**6. The Solidigm carve-out re-rating is unpriced.** SK Hynix paid $9B for Solidigm in 2021. At 51% QLC market share + $3.34B Q3 2025 quarterly run-rate, Solidigm standalone valuation = $15-25B. A 2027 IPO crystallizes $6-15B of hidden value and resets parent multiple by separating 15% EBITDA-margin NAND from 80% EBITDA-margin DRAM/HBM. Sell-side blended 8x EV/EBITDA on SK Hynix; sum-of-parts (DRAM/HBM 12x + Solidigm 8x) argues 10-11x — a 20-30% re-rating independent of HBM share trajectory.

**7. Custom HBM (foundry-fabricated base dies) creates vendor lock-in that makes share losses sticky in either direction.** A hyperscaler's HBM4 base die fabricated at Samsung 2nm cannot port to TSMC for SK Hynix HBM4 — and vice versa. This makes 2026 HBM4 share allocation structural for 3+ year GPU/ASIC roadmaps. Counter to the consensus framing of "Nvidia/AMD will dual-source on price every cycle," the HBM4 allocations are now sticky. SK Hynix's 70% Rubin lock-in is durable through 2028; Samsung's 30% is similarly defended. **Custom HBM share grows 82% YoY in 2026, reaching ~33% of total HBM market** — the unpriced lock-in is the single largest counter to the Incumbent Erosion thesis.

**8. The Huawei HiBL + CXMT bifurcation is more consequential than consensus models.** China's vertical-integration of in-house HBM + domestic GPU + domestic packaging removes the SK Hynix/Samsung chokepoint for the China AI compute stack. ByteDance's $5.6B Ascend 950PR commitment is the first major hyperscaler-class order outside the SK Hynix/Samsung HBM ecosystem in 10+ years. The China-domestic pool may reach 15-20% of global HBM bit demand by 2028, cleaving global HBM into two non-interchangeable markets. Implication: SK Hynix/Samsung lose the China HBM TAM permanently; Western HBM pricing power retains for the addressable ~80% of global TAM.

**9. The TurboQuant/algorithmic-compression risk is currently mispriced as bullish.** Consensus: Jevons Paradox absorbs efficiency gains, total HBM demand rises. Counter: if compression algorithms compound (TurboQuant 2-bit weights, MLA, KV-cache offload to HBF/CXL), 2027-2028 HBM demand growth could decelerate from +30-40% YoY to +10-15%. The market absorbed the March 24, 2026 TurboQuant shock (-6.23% SK Hynix) within a week and re-anchored on Jevons; a follow-on breakthrough has unmodeled tail risk for the supercycle thesis.

**10. The Korean equity multiple rerating is the cleanest path to 2x upside in SK Hynix.** Korean equity discount runs 30-40% to global peers on persistent governance + Korean political risk. SK Hynix at 5-8x P/E on 2026 realized earnings vs Micron at 11-14x P/E on equivalent earnings = the largest single-stock discount in global semiconductor markets. Multiple expansion (not earnings revision) is the asymmetric driver — consensus prices the multiple as fixed, but a Korean equity re-rating cycle (precedent: 2016-2017) could deliver 50-80% upside independent of share trajectory.

---

## Memory Tier Architecture (2026-2030)

```
    ┌──────────────────────────────────────────────────────────┐
    │              AI INFERENCE / TRAINING SERVER              │
    │                                                          │
    │  ┌────────────┐  ┌───────────────┐  ┌────────────────┐  │
    │  │  GPU/ASIC  │──│  HBM (Hot)    │──│  HBF (2027+)   │  │
    │  │ Compute    │  │  36-144GB     │  │  Warm / Weights │  │
    │  │ Tensor/    │  │  $8-10/GB     │  │  512GB-1.5TB    │  │
    │  │ Matrix     │  │  2-4 TB/s     │  │  ~$1/GB         │  │
    │  │            │  │  HBM3E/HBM4   │  │  1.6-3.2 TB/s   │  │
    │  └────────────┘  └───────────────┘  └────────────────┘  │
    │       │                                                  │
    │       └─────┐                                            │
    │             ▼                                            │
    │  ┌──────────────────┐                                    │
    │  │ DDR5 RDIMM 64-128GB │  ← Server CPU + auxiliary       │
    │  │ ~$0.50/GB         │     memory pool                   │
    │  │ 64-100 GB/s/channel │                                 │
    │  └──────────────────┘                                    │
    │             │                                            │
    │             ▼                                            │
    │  ┌──────────────────────────────────────────────────────┐ │
    │  │     Enterprise SSD (Cold Storage)                     │ │
    │  │     61-245TB per drive                                │ │
    │  │     $0.10-0.20/GB                                     │ │
    │  │     14-28 GB/s sequential                             │ │
    │  └──────────────────────────────────────────────────────┘ │
    └──────────────────────────────────────────────────────────┘
```

The DRAM/HBM sector owns the top two tiers (HBM + DDR5), with the future HBF tier emerging from NAND vendors with HBM packaging IP (SK Hynix + SanDisk + Samsung). Pricing power, gross margin, and capital intensity all decline monotonically down the stack. Within the AI server, the top-tier (HBM) consumes 25-40% of total system memory cost despite representing <5% of total bit volume — the inversion that defines AI-era memory economics.

---

## Watchlist

- **Samsung Electronics (005930.KS)** — DRAM #1 (Q4 2025 reclaim); HBM #2 with 30% Rubin allocation; 2026 capex $73B (foundry + memory + AVP). 1c DRAM yield trajectory (50% pilot → 70% target end-2026) is the central operational catalyst. Hybrid-bonding decision May-June 2026 per BESI. **No vault thesis yet** — consider opening if Samsung HBM4 ramp delivers >35% Rubin allocation in H2 2026 (Bear case for SK Hynix; Bull case for Samsung).
- **Micron Technology (MU)** — DRAM #3 (~21%); HBM ~13-25% (varies by source); excluded from initial Rubin allocation per VideoCardz/TweakTown but Samsung/Micron mass-production confirmed for Vera Rubin per other sources (conflicting reporting). FY2026 op margin 74.9% non-GAAP; LPDDR5X sole-supplier to Nvidia GB300; Q2 FY2026 revenue $23.86B (+196% YoY). $13.5B 2026 capex (+23% YoY). **No vault thesis yet** — consider opening as the second-derivative HBM exposure with cleaner US public-market access than SK Hynix (KRX-listed).
- **CXMT (private, planned 2026 STAR Market IPO)** — $4.2B raise; HBM3 mass production targeted end-2026; 300K WSPM total wafer capacity. Pre-IPO valuation $42B (Cryptopolitan). Monitor IPO timing, HBM3 yield disclosures (50% pilot), Huawei Ascend allocation.
- **Huawei (private)** — HiBL 1.0 + HiZQ 2.0 in-house HBM; Ascend 950PR (Q1 2026) + 950DT (Q4 2026); 1.6M die volume FY2026 target. The single largest competitive risk to global HBM pricing power outside the triopoly.
- **BESI (BESI.AS)** — Hybrid-bonding tool monopolist (~67% D2W hybrid-bonding share). Joint Kinex platform with AMAT. SK Hynix March 2026 Kinex order is the leading indicator for HBM5 hybrid-bonding adoption timing. See [[Theses/BESI - BE Semiconductor Industries]].
- **ASML (ASML)** — EUV scanner monopolist; First commercial High-NA EUV at SK Hynix Icheon (Sept 2025); $7.9B SK Hynix order (2025). Equipment-layer pricing power passes through to HBM cost structure.

---

## Related Research

- [[Research/2025-11-01 - DRAM HBM Competitive Dynamics]] — Q4 2025 DRAM revenue +29.4% sequential; conventional DRAM contract prices +45-50% QoQ; SK Hynix 2025 op profit ₩47.2T ($31.59B); Samsung 110T won 2026 capex; Samsung HBM 250K WSPM target by end-2026
- [[Research/2025-11-27 - HBM4 Breakthroughs and Yields]] — JEDEC HBM4 (JESD238) ratified April 2025; vendor-by-vendor yield benchmarks (SK Hynix 1c ~80%, Samsung 1c ~50% pilot); HBM4 2030 revenue scenario $93B at SK Hynix 40% share
- [[Research/2025-11-27 - Semis - Gemini HBM4 Market Canvas]] — Vera Rubin HBM4 architecture deep-dive; 2030 share trajectory SK Hynix 45% / Samsung 33% / Micron 21% / Others 1%; vendor-lock-in second-order effect
- [[Research/2026-01-15 - AI Compute and Memory Demands - HBM Shortage]] — Memory bandwidth grew 17x while FLOPS grew 80x (2012-2022); HBM provided 77% of SK Hynix Q2 2025 revenue; Engram architecture redirects demand to DRAM
- [[Research/2026-01-17 - Semis - Gemini AI Compute HBM Canvas]] — DeepSeek MLA architecture; HBM4 "bit crossover" 2026; 3:1 wafer penalty for HBM vs DDR5
- [[Research/2026-03-27 - TurboQuant Impact on Memory Demand]] — March 24 2026 selloff mechanics (SK Hynix -6.23%); Jevons Paradox analyst pushback; structural HBM supply shortage through 2027
- [[Research/2026-04-23 - NVDA - Investment Brief]] — NVDA's HBM consumption profile; Rubin/Rubin Ultra/Feynman roadmap; Taiwan tail risk

## Related Sectors and Macro

- [[Sectors/NAND Memory & Storage]] — Sister memory sub-sector; HBF tier emerging from NAND vendors; Solidigm IPO catalyst inside SK Hynix
- [[Sectors/GPU & AI Compute Accelerators]] — HBM downstream demand source; Nvidia 60-65% CoWoS pre-booking; HBM content per GPU trajectory
- [[Sectors/Semiconductor Capital Equipment]] — ASML EUV monopoly upstream of HBM; BESI hybrid bonding; HBM4 packaging equipment intensity
- [[Macro/AI Bubble Risk and Semiconductor Valuations]] — $650B AI revenue requirement for 2030; Taiwan kinetic tail risk; hyperscaler capex digestion-phase scenarios

## Log

### 2026-04-23
- Sector note created by /thesis 000660 — first thesis in this sector. Scaffold-only; analytical content to be added via /deepen or /surface. DRAM/HBM sector split from prior NAND-inclusive memory coverage; now symmetric with [[Sectors/NAND Memory & Storage]].
- **Full population from vault synthesis + deep web research.** Replaced placeholder content across all 8 sections (Active Theses, Key industry questions, Industry history, Competitive dynamics, Product level analysis, Acquisitions and new entrants, Macro shifts, Investor heuristics). Sources: SK Hynix Q1 2026 earnings (record 72% op margin, 57% HBM share), TrendForce/UBS/BofA/Goldman/Morgan Stanley/Macquarie consensus aggregation, vault research notes (5 HBM-specific deep dives), web research (CXMT IPO + HBM3 timeline slip, Samsung HBM4 Nvidia qualification + 30% Rubin allocation, Micron Rubin exclusion, BESI Kinex hybrid-bonding qualification timing, TSMC CoWoS quadrupling to 130K WSPM, Huawei HiBL/HiZQ in-house HBM). Status changed draft → active. Key non-consensus calls: (1) Incumbent Erosion (62%→45%) is structural, not cyclical; (2) MR-MUF lead inverts at HBM5; (3) CXMT is wrong-timing bear case (commodity DRAM 2028-2029, not HBM); (4) DDR5 profitability surpasses HBM3e Q1 2026; (5) HBF $5-10B option unpriced; (6) custom HBM vendor lock-in makes 2026 share allocations sticky for 3+ year roadmaps; (7) Korean equity discount = clean multiple-expansion path. Reminder to run `/graph last` after this edit per CLAUDE.md metadata-ownership rule.
