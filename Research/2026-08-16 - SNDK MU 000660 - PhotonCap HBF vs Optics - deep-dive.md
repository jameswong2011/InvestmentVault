---
publish: false
date: 2026-08-16
tags: [research, Memory, Optical-Networking-Photonics, SNDK, MU, 000660, 285A, BESI]
sector: Memory
ticker: SNDK
source: 'https://photoncap.net/p/beside-above-or-beyond-the-ai-memory'
source_type: deep-dive
propagated_to: [SNDK, MU, 000660, 285A, BESI, MRVL, AVGO, NVDA, LITE, COHR]
---

# Beside, Above, or Beyond: HBF vs Optics — PhotonCap

## Thesis Delta
Consensus still prices “stacking NAND” as one story and the optical interconnect as another: [[Theses/SNDK - SanDisk]] Insight #1 and [[Theses/000660 - SK Hynix]] Insight #3 treat High Bandwidth Flash as a 2027 OCP-spec call option (tape-out done, customer samples 2027, FY30 HBF revenue modeled at $0 at SNDK), [[Theses/MU - Micron Technology]] treats Micron as HBM4-plus-fast-SSD with “no HBF standard seat,” and the optics names ([[Theses/MRVL - Marvell Technology]] Photonic Fabric, [[Theses/AVGO - Broadcom]] CPO, [[Theses/NVDA - Nvidia]] scale-up, [[Theses/LITE - Lumentum]] / [[Theses/COHR - Coherent]] InP) are underwritten as switch/transceiver demand, not as the seat that receives the *increment* of AI capacity growth. This 16 August 2026 PhotonCap deep-dive implies the opposite map. “Stacking” is three processes (layer-count, wafer bonding, TSV/package stacking) and three placements (beside / above / beyond the processor). Only the third process changes the interface from serial PCIe to a parallel memory bus. Only the beyond seat — the same HBF stack moved across an optical link — sits behind a wall that time and technology can lower. Beachfront is geometry and heat is thermodynamics; energy-per-bit is on a CPO/LPO/NPO curve. First-generation HBF starts in the UCIe seat beside the processor; once capacity demand outruns package real estate, growth accumulates on optically connected flash, not on another on-package stack. Investment translation is hold the memory names *and* the optics names, not sell memory because optics “wins.” Micron is not in the HBF consortium and says HBF zero times on its careers site, but two Tokyo NVEG postings (April and July 2026, still up four months) hire for TSV interface circuits, HBM-like lane repair, and HBM3/3E/4 experience — circumstances of preparing the same physical structure outside the standard, not a product confirmation. Conviction-trigger touches: [[Theses/000660 - SK Hynix]] HIGH/LOW/CLOSE are Rubin/CXMT/Namics handles — HBF does not fire them; the H2 2026 OCP-spec catalyst in that thesis has now landed. [[Theses/MU - Micron Technology]] HIGH/LOW/CLOSE are the Q3 Rubin board meter, LTA-cap removal, destock prints, CXMT Western-HBM qual, and GB300 dual-source — job-posting structure does not touch them. [[Theses/SNDK - SanDisk]], [[Theses/285A - Kioxia]], and [[Theses/BESI - BE Semiconductor Industries]] have no registered Conviction Triggers. [[Theses/MRVL - Marvell Technology]] Celestial HIGH (disclosed PO or on-schedule end-2026 tape-out) is evidence-touched on the named “memory-over-optics” seat, not fired — PhotonCap restates company H2 FY2028 revenue contribution, not a PO.

## Summary
The week of 13 August 2026 put two facts on the same tape. At SanDisk’s Investor Day the HBF Consortium Milestones slide showed Meta joining after Google, ten days after the first OCP HBF specification (up to 512 GB, up to 3.0 TB/s, UCIe) was published. The same week Samsung unveiled zHBM — HBM stacked vertically on the accelerator, vendor-claimed 8× HBM5 performance and >10× density, still a concept model. SanDisk closed $1,528 on 13 August after +6% on the 12th (mid-$1,300s) and +14% on the 13th, more than 5× year-to-date; PhotonCap treats the NAND-cycle tape and the ~$90B contract backlog as the surface and “NAND leaving the storage box and climbing onto the memory bus” as the structural change. HBF is the transplant of HBM’s stacking formula onto NAND: much wider than SSD, much bigger than HBM. January PhotonCap still had conference slides; August has an OCP spec with three bandwidth grades (0.4–3.0 TB/s), a UCIe host, and two company schedules that the piece does not reconcile — the 3 August SanDisk/SK hynix IR still says samples in H2 2026 and inference devices in early 2027, while Investor Day says the first HBF die is taped out and customer samples are 2027. Consortium formation under OCP was February 2026 (Google and Tenstorrent at that time); August 2025 was the SanDisk–SK hynix standardization agreement. Two hyperscalers that design their own AI chips — Google and Meta — have now put their names on a NAND-based memory standard.

PhotonCap’s load-bearing claim is that investors who lump “stacking NAND” draw the beneficiary map wrong. Process and placement are different questions. Process: (1) layer stacking inside the die — Samsung V10 >400 layers, Kioxia/SanDisk BiCS10 332 layers, Micron G9 276 layers — is the cost game every NAND vendor plays; (2) wafer bonding (cell-array wafer + CMOS wafer) — Kioxia/SanDisk CBA, Samsung BV-NAND from V10 — still finishes as a die behind an SSD controller and PCIe; (3) HBF — completed NAND dies TSV-stacked 8-high or 16-high on a logic base die, wide parallel bus beside the processor, up to 512 GB/stack, 0.4–3.0 TB/s. Only (3) changes the interface from storage-serial to memory-parallel. Placement then splits the capacity block: beside = on-package HBF (wall: beachfront; HBF is designed to the same footprint and pin layout as HBM4, so one HBF seat is one HBM seat dropped — 512 GB of capacity versus ~2 TB/s and tens of GB); above = Samsung zHBM (wall: heat; memory sits between a ~1 kW accelerator and the cold plate; DRAM past ~85 °C doubles refresh while logic silicon holds to ~105 °C; AMD 3D V-Cache is the mass-production precedent and the limit case — one low-power SRAM die on a cool cache region, early gen even clocked down, then flipped under the cores); beyond = the same HBF stack in a remote unit across an optical link (wall: energy per bit from EO/OE conversion). Beyond is not a new memory. It is a different seat for the same stack, and optics is the means that makes the seat possible.

NAND’s microseconds are why the beyond seat is physically allowed. Read latency is tens of microseconds, ~1,000× DRAM’s nanoseconds. An optical signal travels 1 m in ~5 ns; moving an HBF stack 2 m across a rack, plus conversion, switches, and protocol, adds hundreds of nanoseconds — about one-hundredth of NAND access time. Move DRAM 2 m and access latency jumps several times. HBM cannot leave the processor’s side; HBF was allowed to leave from the start. The 3.0 TB/s HBF grade is a dozen-or-so-fiber WDM bundle at rack distance. First generation therefore starts in the UCIe seat the spec writes; the increment, once package seats run out, lands on optically connected flash appliances — the same direction as SK hynix H³ hybrid and PhotonCap’s earlier optical-memory-pooling pieces. On-package electrical will always beat distanced HBF-plus-optics on energy per bit. The destination is tiering, not a knockout: hot weights and KV cache on HBM plus a small on-package HBF allocation; warm data on rack-distance optical capacity. The claim is not “on-package loses.” The claim is “the increment accumulates on the optics side.” That is why the piece says hold memory companies and optics companies together, not sell memory.

Micron is the test of whether the third stacking is a two-company exclusive or an industry direction. It is not an HBF consortium member. FMS 2026 award was a 245 TB-class data-center SSD. CBO Sumit Sadana at the early-August Technology Leadership Forum stopped at “when DRAM is insufficient, KV cache spills over to the NAND side.” Public Micron stacks in the first and second meanings — cost. Careers-site search: “HBF” = 0 postings. Two Tokyo NVEG Principal Design Engineer postings (JR94304 posted 13 April 2026; JR106037 posted 21 July 2026) hire for “design and optimization of TSV interface circuits connecting memory die to logic die,” “TSV power integrity for highly parallel IO,” “energy-per-bit optimization in the context of 3D-stacked memory architectures,” “column redundancy and lane repair schemes compatible with HBM-like highly parallel bus architecture,” preferred HBM3/HBM3E/HBM4 interface experience. Tokyo is where Kioxia/WD-lineage NAND design talent sits; location-as-talent-pool is PhotonCap’s conjecture, not a company reason. A job posting is a development-organization primary, not a product-roadmap confirmation. The piece goes only as far as “circumstances of quietly preparing the same physical structure outside the standards consortium,” which recasts “HBF vs advanced NAND” as “TSV NAND inside the standard vs TSV NAND outside the standard.” Samsung’s same-week zNAND-O (V-NAND 4- and 8-layer stacked NAND for edge AI) was shown beside an NPU with a UCIe marking on the exhibit substrate — press release silent on interface; exhibit labeling is the source. Inside the standard or outside it, everyone is drawing NAND onto the memory bus.

The optics map is four layers, not one ticker. Package-boundary: UCIe does not discriminate electrical chiplets from optical chiplets, so an optical I/O chiplet in the same seat as the NAND stack has low design-transition friction (inference, not a fact of the standard; lasers, fiber attach, and thermal verification still attach). Names: [[Theses/MRVL - Marvell Technology]] Photonic Fabric (Celestial AI) — “memory over optics, out of the package,” first revenue contribution H2 FY2028 per company; unlisted Ayar Labs TeraPHY. Both pre-revenue / samples-and-design-wins. Scale-up fabric: optical switching and engines that tie GPUs to the capacity tier in and around the rack — [[Theses/AVGO - Broadcom]] CPO switch roadmap and the [[Theses/NVDA - Nvidia]] ecosystem’s optical scale-up. Asymmetry: this layer grows without HBF and grows more with HBF, because a capacity tier outside the package adds “memory access” to East-West traffic. Light source and components: [[Theses/COHR - Coherent]] and [[Theses/LITE - Lumentum]] — optical disaggregation of the capacity tier is an amplification of the existing SAM, not a new SAM. Counterargument PhotonCap rejects: on-package HBF reduces network travel and is therefore bad for optics. Inference no longer finishes inside one GPU; model and KV cache are sharded across nodes. “Pack it all inside the package” requires the data to fit; data size is growing the other way. Traffic really falls only if models stop growing — at which point the whole AI-infrastructure book is the rethink, not optics.

Stacking equipment is the placement-fight-insensitive volume layer. TSV stacking (thin, align, bond) is the HBM-verified chain: thermo-compression bonding suppliers ASMPT, Hanmi Semiconductor, Kulicke & Soffa, with [[Theses/BESI - BE Semiconductor Industries]] entered on production orders. An 8-high / 16-high HBF stack puts joins per stack in the same digit range as one HBM stack. Caveat that blocks a BESI order-catalyst read: SanDisk’s official wording is TSV and microbumps plus “proprietary stacking technology”; bonding method is not confirmed as TCB; production-process details (bonding, underfill, stack thickness) are undisclosed; no equipment company has announced an HBF-related order. Wafer-bonding maturity is split: Kioxia/SanDisk CBA is already in mass-produced product; Samsung BV-NAND is an announcement at the 400-layer range. W2W: EV Group (unlisted), SUSS MicroTec, Tokyo Electron. D2W hybrid bonding: BESI in the leading group. Micron’s WoW Bonding posting (JR97682, 24 May 2026) lists wafer bonding, Si grinding, and bevel-trimming integrated optimization — a preceding development signal, not an equipment order. Picking rule: stacking equipment is the volume side less sensitive to who wins the placement fight; optical links strengthen as the beyond placement grows.

Falsifiers the author will re-open the piece on: (1) CPO energy-per-bit stall — if next-generation optical-engine numbers stand still at OFC next March, “time is on optics’ side” collapses; (2) panel-level packaging widens the shoreline faster than expected, and beside lives longer; (3) first-generation on-package HBF absorbs most KV-cache demand, and the increment does not come outside. Checking dates: HBF sample shipment H2 2026 *and* customer samples 2027 (the piece keeps both), first inference devices early 2027, Micron late-December earnings for NAND-side new-product mentions, OFC next March, FMS next August. January 26 PhotonCap called HBF a “candidate trigger for expanding the optical interconnect ecosystem”; half a year later the OCP spec, UCIe, and Google/Meta membership are the direction check. Stock-level calls from that piece (POET named) are marked half a grade down — direction and tickers are different problems.

## Framework / Mental Model
**Name:** Beside / Above / Beyond — three paths and three walls, crossed with three meanings of “stacking.”

**Process axis (how the die is built):**

| Category | What is stacked | Purpose | Interface after the stack | Money flow |
|---|---|---|---|---|
| Layer stacking | NAND cells inside one die (V10 >400L; BiCS10 332L; G9 276L) | More bits / wafer; lower $/bit | Still SSD controller + serial PCIe | Cost game; every NAND vendor |
| Wafer bonding | Cell-array wafer + CMOS/periphery wafer (CBA; BV-NAND) | Density + faster I/O on one die | Still SSD controller + serial PCIe | Still cost; “how to make one die well” |
| TSV / package stacking (HBF) | Completed NAND dies, 8-Hi or 16-Hi, on a logic base die | Bandwidth; memory-bus seat | Parallel wide bus (UCIe); HBM-class pin/footprint | Interface change; “wider,” not “cheaper” |

zHBM is not a fourth process. It is a placement of HBM (not NAND) onto the processor. PhotonCap’s one-line sort: layer-count and bonding = stacking of cost; HBF = stacking of bandwidth; zHBM = stacking of position. The three hit different physical limits and must not be one word.

**Placement axis (where the finished capacity block sits relative to the processor):**

| Seat | Instance | What sits there | Wall | Wall type | Time’s side |
|---|---|---|---|---|---|
| Beside | On-package HBF, HBM4-footprint/pin compatible | 512 GB NAND stack taking an HBM seat (256 Gb/die × 16-Hi; gen-1 read up to 1.6 TB/s) | Beachfront / package edge already filled by HBM | Geometry (reticle, interposer). Zero-sum: one HBF seat = one HBM seat dropped | Does not move |
| Above | Samsung zHBM (concept): HBM on top of the accelerator | DRAM in the 1 kW heat path, between die and cold plate | Heat. Logic ~105 °C; DRAM refresh doubles past ~85 °C. 3D V-Cache is the limit case, not the template for 12-Hi DRAM on a 1 kW GPU | Thermodynamics. Bonding-interface thermal-resistance cuts (Samsung: <½) do not remove the placement | Does not move |
| Beyond | Same HBF stack in a remote unit across an optical link | Optically connected flash appliance at rack distance | Energy per bit (EO/OE). Electrical inside the package stays cheapest | Technology curve: DSP → LPO → NPO → CPO | Time and technology take this side |

**How applied.** Classify every “stacking NAND / stacking memory” headline on both axes before drawing beneficiaries. Process tells you whether money is still in bit-cost (layers, CBA/BV-NAND at [[Theses/285A - Kioxia]] / [[Theses/SNDK - SanDisk]] / Samsung / [[Theses/MU - Micron Technology]]) or has jumped to a memory-bus interface (HBF at SNDK + [[Theses/000660 - SK Hynix]], TSV-NAND-outside-the-standard at MU, zNAND-O at Samsung). Placement tells you which wall the design hits and therefore which second-order layer gets the increment: stacking equipment (TSV/TCB and W2W/D2W) is common to all three seats; optical I/O, scale-up fabric, and InP/engines strengthen only as beyond grows. Methodology constraint: a job posting is a development-organization primary, not a roadmap; vendor zHBM figures are concept-stage claims; UCIe-socket → optical-chiplet substitution is inference, not a fact of the standard; SanDisk “proprietary stacking technology” means HBF is not a confirmed TCB order for [[Theses/BESI - BE Semiconductor Industries]].

**NAND-distance arithmetic (the physical reason beyond is allowed).** Optical flight time ~5 ns/m. Two meters of rack + conversion/switch/protocol ≈ hundreds of nanoseconds. NAND read is tens of microseconds, so the added delay is ~1/100 of access time. DRAM moved the same distance multiplies latency. Fast tiers are distance-sensitive; slow tiers are not. HBM stays beside; HBF may leave. Bandwidth to leave is optics’ specialty (WDM, terabit-class per fiber; 3.0 TB/s ≈ a dozen-or-so-fiber bundle depending on WDM).

**Investment rule the framework produces.** Do not treat optics vs HBF as a binary. On-package electrical keeps winning energy/bit. Realistic end-state is tiering (HBM + small on-package HBF for hot; optical HBF for warm). The increment of capacity growth, once beachfront is full and zHBM heat does not cool, accumulates on the optical interconnect. Hold memory and optics. Sell-memory-because-optics-wins is the wrong reading of the same facts.

## Evidence

### Tape, consortium, spec

| Item | Figure | Tag |
|---|---|---|
| SNDK 12 Aug 2026 close | +6%; mid-$1,300s | [1×: PhotonCap / 24/7 Wall St.] |
| SNDK 13 Aug 2026 close (Investor Day) | +14%; $1,528 | [1×: PhotonCap / TIKR] |
| SNDK YTD into ID week | >5× | [1×: PhotonCap] |
| NBM / backlog (surface, not this piece’s subject) | ~$90B range | [1×: TIKR via PhotonCap] |
| SanDisk–SK hynix HBF standardization | August 2025 | [1×: PhotonCap / Sandisk IR] |
| OCP consortium formed | February 2026; Google + Tenstorrent | [1×: Sandisk IR / TrendForce via PhotonCap] |
| First OCP HBF spec | ~3 Aug 2026; up to 512 GB; 0.4–3.0 TB/s; UCIe | [1×: Sandisk IR 2026-08-03 / SK hynix FMS] |
| Consortium expansion | August 2026: Meta | [1×: Sandisk ID slide via PhotonCap] |
| Hyperscalers on a NAND memory standard | Google + Meta (own-chip designers) | [1×: PhotonCap] |
| First HBF die | taped out (design handed to foundry) | [1×: TIKR / ID via PhotonCap] |
| Sample schedule (Aug 3 IR — stale vs vault) | samples H2 2026; inference devices early 2027 | [1×: Sandisk IR 2026-08-03 via PhotonCap] |
| Sample schedule (Investor Day — live with vault) | customer samples 2027 | [1×: TIKR / ID via PhotonCap] |

### HBF product / process (third stacking)

| Item | Figure | Tag |
|---|---|---|
| Stack height | 8-high or 16-high | [1×: SK hynix / OCP via PhotonCap] |
| Capacity / stack | up to 512 GB | [1×: OCP spec via PhotonCap] |
| Bandwidth grades | 0.4 / … / 3.0 TB/s | [1×: OCP spec via PhotonCap] |
| Host interface | UCIe | [1×: OCP spec via PhotonCap] |
| Die / stack construction (fact sheet) | 256 Gb/die; 16-high → 512 GB; HBM4 footprint + pin compatible | [1×: Sandisk HBF fact sheet via PhotonCap] |
| Gen-1 read bandwidth (company target) | up to 1.6 TB/s | [1×: Sandisk HBF fact sheet via PhotonCap] |
| Stacking wording (official) | TSV + microbumps + “proprietary stacking technology” | [1×: Sandisk TAB IR via PhotonCap] |
| Bonding method | not confirmed as TCB; underfill / stack thickness undisclosed | [1×: PhotonCap] |
| Equipment HBF orders | none announced | [1×: PhotonCap] |

### Cost stacking (first and second meanings)

| Item | Figure | Tag |
|---|---|---|
| Samsung V10 layers | >400 | [1×: Samsung Newsroom via PhotonCap] |
| Kioxia / SanDisk BiCS10 | 332 layers; CBA; up to 60% QLC bit-density gain | [1×: Sandisk Newsroom 2026-08-04 via PhotonCap] |
| Micron G9 | 276 layers; 3.6 GB/s interface | [1×: Micron / TechPowerUp via PhotonCap] |
| Samsung bonding transition | BV-NAND from V10 | [1×: Samsung Newsroom via PhotonCap] |
| CBA status | already in mass-produced Kioxia/SanDisk product | [1×: PhotonCap] |

### Samsung placement / edge NAND

| Item | Figure | Tag |
|---|---|---|
| zHBM | HBM (not NAND) stacked on the accelerator; concept model, not a product or confirmed roadmap | [1×: Samsung FMS 2026 via PhotonCap] |
| zHBM vendor claims | 8× HBM5 performance; >10× density | [1×: Samsung Newsroom via PhotonCap] |
| zHBM thermal-resistance claim | reduced to <½ (bonding interfaces); placement heat path unchanged | [1×: Samsung via PhotonCap] |
| zNAND-O | V-NAND 4- and 8-layer stacked NAND for edge AI | [1×: Samsung Newsroom via PhotonCap] |
| zNAND-O exhibit | stack beside an NPU; UCIe marking on substrate (exhibit labeling, not PR body) | [1×: PhotonCap exhibit] |

### Micron public vs careers

| Item | Figure | Tag |
|---|---|---|
| HBF consortium membership | not a member | [1×: TrendForce via PhotonCap] |
| FMS 2026 award | 245 TB-class data-center SSD | [1×: TweakTown via PhotonCap] |
| Public NAND stance (Sadana, TLF) | KV cache spills to NAND when DRAM is insufficient; firepower on HBM4 + fast SSDs | [1×: Investing.com transcript via PhotonCap] |
| Careers keyword “HBF” | 0 postings | [1×: PhotonCap / Micron Workday] |
| Tokyo NVEG postings | JR94304 posted 2026-04-13; JR106037 posted 2026-07-21; live ~4 months | [1×: Micron Careers via PhotonCap] |
| NVEG first responsibility | “Design and optimization of TSV interface circuits connecting memory die to logic die” | [1×: Micron JR106037 / JR94304] |
| NVEG requirements | TSV power integrity for highly parallel IO; energy-per-bit in 3D-stacked memory; column redundancy / lane repair compatible with HBM-like parallel bus | [1×: Micron JR106037 / JR94304] |
| NVEG preferred | HBM3, HBM3E, HBM4 interface design | [1×: Micron JR106037] |
| WoW bonding posting | JR97682 posted 2026-05-24; wafer bonding + Si grinding + bevel trimming | [1×: Micron Careers via PhotonCap] |
| Author limit | posting ≠ product roadmap; not an assertion Micron is shipping an HBF rival | [1×: PhotonCap] |

### Physics of the three walls

| Item | Figure | Tag |
|---|---|---|
| Accelerator heat class (above) | ~1 kW; heat escapes almost entirely upward | [1×: PhotonCap] |
| Logic vs DRAM temperature | logic ~105 °C; DRAM refresh doubles past ~85 °C | [1×: PhotonCap] |
| 3D V-Cache precedent | one low-power SRAM on cool cache; early gen clocked down; gen-2 flipped cache under cores | [1×: PhotonCap] |
| NAND read latency | tens of microseconds; ~1,000× DRAM nanoseconds | [1×: PhotonCap] |
| Optical flight time | ~5 ns per meter | [1×: PhotonCap] |
| 2 m rack move + optics/switch/protocol | added delay hundreds of nanoseconds ≈ 1/100 of NAND access | [1×: PhotonCap] |
| HBF 3.0 TB/s at rack distance | bundle of ~a dozen fibers, WDM-dependent | [1×: PhotonCap] |
| Beside zero-sum | HBF seat = dropped HBM seat (~2 TB/s-class + tens of GB traded for 512 GB) | [1×: PhotonCap] |

### Optics and equipment names

| Item | Figure | Tag |
|---|---|---|
| Package-boundary optical I/O | MRVL Photonic Fabric (Celestial); Ayar Labs TeraPHY; both pre-mass-production | [1×: PhotonCap] |
| MRVL revenue contribution timing | first Photonic Fabric revenue H2 FY2028 (company) | [1×: Marvell 2026-02-02 via PhotonCap] |
| Scale-up fabric | AVGO CPO switch roadmap; NVIDIA optical scale-up; grows w/o HBF, more with HBF | [1×: PhotonCap] |
| Light source / engines | COHR, LITE — amplification of existing SAM | [1×: PhotonCap] |
| TCB / TSV attach names | ASMPT, Hanmi, K&S main; BESI entered on production orders | [1×: PhotonCap] |
| Joins per HBF stack | same digit range as one HBM stack at 8-Hi / 16-Hi | [1×: PhotonCap] |
| W2W bonding names | EV Group (unlisted), SUSS MicroTec; TEL entered | [1×: PhotonCap] |
| D2W hybrid bonding | BESI counted in leading group | [1×: PhotonCap] |
| HBF equipment orders | none announced | [1×: PhotonCap] |

### Author falsifiers / check dates

| Item | Figure | Tag |
|---|---|---|
| Falsifier 1 | CPO pJ/bit stall at next OFC | [1×: PhotonCap] |
| Falsifier 2 | panel-level packaging widens shoreline; beside lives longer | [1×: PhotonCap] |
| Falsifier 3 | gen-1 on-package HBF absorbs most KV-cache demand | [1×: PhotonCap] |
| Check dates | H2 2026 samples (Aug 3 IR) *and* 2027 customer samples (ID); early-2027 inference devices; MU late-Dec earnings; OFC next March; FMS next August | [1×: PhotonCap] |
| January call score | direction (HBF as optics-ecosystem trigger) roughly right; stock-level names (e.g. POET) half a grade down | [1×: PhotonCap] |

Live-portfolio context (not PhotonCap): [[Live Portfolio]] holds [[Theses/000660 - SK Hynix]] at Full (25%+), [[Theses/NVDA - Nvidia]] / [[Theses/AVGO - Broadcom]] / [[Theses/MRVL - Marvell Technology]] at Medium, [[Theses/SNDK - SanDisk]] / [[Theses/285A - Kioxia]] / [[Theses/BESI - BE Semiconductor Industries]] at Low. [[Theses/MU - Micron Technology]] is coverage-only (conviction low; weight 0; not in the table).

## Contradiction Check
**Supports** [[Theses/SNDK - SanDisk]] Insight #1 (HBF as TAM creation; SK hynix + OCP kills Betamax) and Outstanding Question #1 (commercial viability, NVIDIA/hyperscaler re-architecture) — Meta-on-the-slide plus a published OCP spec with UCIe and 0.4–3.0 TB/s grades is the strongest standardization print since the February consortium, and it does not put HBF on a 2026 revenue line. **Supports** the 2026-08-15 /sync already on that Outstanding Question (first die taped out; META joined with SKHY / GOOG; FY30 HBF still $0). **Challenges the stale H2 2026 sample language, and does not fully retire it.** PhotonCap cites the 3 August SanDisk IR — “samples in the second half of this year, inference devices in early 2027” — *and* the Investor Day line that customer samples are next year, then lists both as checking dates in the conclusion. Vault live timing, set by Ilkbahar at the 13 August ID and already written into Catalysts (“~~HBF sampling milestone (H2 2026)~~ → slipped: customer samples now **2027**”) and Insight #1 (“samples 2027 (slipped from H2 2026)”), is 2027 samples. The Aug 3 H2 2026 sample window is the stale clause. This source does not move samples back to 2026; it is sloppy about carrying both. Treat 2027 customer samples as live; treat H2 2026 sample shipment as the superseded IR sentence. **Does not retire** SNDK Bear “HBF execution risk,” Risk #1 (commercialization / NVIDIA adoption), or Risk #4 (Samsung competitive entry): zHBM and zNAND-O are exactly the Samsung-flank the thesis already named, and PhotonCap’s own maturity labels (concept; exhibit UCIe, not PR) keep them as direction, not a 2026 product. **Does not touch** SNDK’s unwritten Conviction Triggers (structural gap; suggested HIGH was NBM coverage >50% of FY27 bits — a different source). NVIDIA ICMS/GIDS route-around on the SNDK Mental Models HBF note is unchanged: PhotonCap’s beyond path is complementary (optical flash appliance) rather than a retract of NVIDIA’s own KV-cache-to-NAND.

**Supports** [[Theses/000660 - SK Hynix]] Insight #3 (unpriced HBF option; OCP workstream) and Bull pillar 3 (HBF monetization at OCP-standard deployment 2027+). The H2 2026 Catalyst “OCP HBF spec finalization” has landed — first spec published ~3 August. Outstanding Question Q4 (“hyperscaler production deployment by 2027, or slip to 2028+”) is not answered; Meta-on-the-consortium is the leading-indicator print Q4 asked for, not Meta qualification or H2 2027 production. **Does not fire** 000660 → HIGH (Rubin ≥60% + HBM4E sole-source + Kinex 16-Hi + Namics ≥2028), → LOW (Samsung >35% Rubin + HBM price −10%), or → CLOSE (CXMT qualified HBM + Samsung HB yield 70% at 16-Hi). Insight #3’s parenthetical that the workstream is “SK Hynix + SanDisk + Samsung” is looser than this source: PhotonCap does not put Samsung in the HBF consortium; Samsung’s week is zHBM / zNAND-O, outside or beside the standard. Tencent is in the vault’s Asymmetrical Bets consortium list and is absent here (Google, Tenstorrent, then Meta).

**Challenges the wording, not the triggers, of** [[Theses/MU - Micron Technology]]. Industry Context and Business Model say Micron “competes with SNDK and 285A on enterprise SSD, not on HBF” and “has no HBF standard seat.” Both remain factually true on membership and public stages. The Tokyo NVEG postings are the first primary the vault has that Micron’s NAND design org is hiring the third stacking (TSV die-to-logic, HBM-like parallel bus, HBM3–HBM4 preferred). That is a circumstance, not a SKU, and it does not put cubes on a Rubin board. **Does not touch** MU → HIGH (Q3 meter ≥10% **and** LTA-cap-off **and** two TrendForce prints), → LOW (meter ~70/30/0 **and** GM −400 bps with destock language), or → CLOSE (two DRAM −20% prints **or** CXMT Western-HBM **or** GB300 LPDDR5X dual-source). Do not promote MU on job descriptions.

**Supports** [[Theses/285A - Kioxia]] Insight #1 (CBA / density-per-layer, BiCS10 332L) only as the *cost* stacking — CBA is already in mass production; BiCS10 332L is the layer-count print. 285A is not named as an HBF consortium member. The Kioxia Mental Models line on an “HBF prototype (5TB, 64 GB/s)” is not in this source and is not corroborated here. **Does not touch** 285A’s unwritten Conviction Triggers. JV-tension Risk #7 (Stargate vs LC9) is untouched; this piece is about the memory bus, not enterprise SSD share.

**Supports, with a hard process caveat,** [[Theses/BESI - BE Semiconductor Industries]] Insight #5 (demand vectors beyond HBM — silicon photonics and 3D NAND) and the Mental Models logic/CPO leg: stacking equipment is the common volume layer across beside/above/beyond, D2W hybrid bonding is the BESI seat, and CPO/COUPE is the wall that time is lowering. **Does not create an HBF order catalyst.** PhotonCap is explicit: bonding method for HBF is not confirmed as TCB; SanDisk says “proprietary stacking technology”; no equipment company has announced an HBF-related order. TCB names in the piece are ASMPT, Hanmi, and K&S first, BESI as entered-on-production-orders. Treating HBF 8-Hi/16-Hi as a Kinex/TCB volume print would be a category error the source itself blocks. BESI has no registered Conviction Triggers.

**Touches** [[Theses/MRVL - Marvell Technology]] Insight on scale-up fabric / Celestial Photonic Fabric and the named HIGH observable (tier-1 Gen-1 PO or end-2026 tape-out) without firing it. PhotonCap places Photonic Fabric in the package-boundary “memory over optics, out of the package” seat and repeats the company H2 FY2028 revenue-contribution timing. That is the same layer the MRVL bull case needs if memory-pool disaggregation becomes the 2027–28 rack primitive. It is not a PO, not a second named customer, and not a tape-out confirmation. MRVL Bear “Celestial slips or gets confined” (NVLink + Ethernet-NAND + HBF capturing the KV-cache socket) is the exact counter the piece writes down and then rejects on fit-inside-the-package grounds — evidence-touched, not retired.

**Touches** [[Theses/NVDA - Nvidia]] only on the scale-up / CPO fabric, not on CUDA Insights. PhotonCap’s “pack it in the package and traffic dies” rejection is the same direction as the vault’s already-logged Bluefield-4 / ICMS / GIDS KV-cache-to-NAND path: working memory is leaving HBM, and NVIDIA will take a networking/DPU cut whether the NAND is HBF-on-package or flash-across-optics. No NVDA Conviction Triggers section to test. **Touches** [[Theses/AVGO - Broadcom]] CPO-switch optionality the same way — grows without HBF, more with HBF — without a registered AVGO trigger in the files read for this draft.

**Does not** change conviction or status on any name. **Does not** write to the vault.

Mental-model triggers for a later `/sync` (ingest identifies only): [[Mental Models/Industry - Semiconductors]] #1 bottleneck-moves — beachfront and heat do not move; energy/bit is the only wall on a curve, so the binding constraint migrates from package seats to optical pJ/bit. [[Mental Models/Lens - Value Layer Monopoly]] interface/standard control — UCIe as a socket that does not discriminate electrical vs optical chiplets is the layer-control claim. [[Mental Models/Generalist - Overview]] [G-3] mean-reversion vs trend — the increment-on-optics read is a trend-continuation on capacity demand (Jevons on compression/quantization) against a geometric package limit. [[Mental Models/Industry - Semiconductors]] #13 classification — HBF remains a TAM-creation option, not a 2026 earnings line; do not reclassify SNDK off the cycle on this piece.

## Source Excerpts
> “whichever direction the stacking competition gets settled, wouldn’t a considerable part of the growth go not to the memory companies but to the optical interconnect layer?”

> “a concrete spec document with 512GB capacity, three bandwidth grades from 0.4 to 3.0TB/s, and a UCIe interface is up on OCP, and it has come to the stage where the company states a schedule: samples in the second half of this year, inference devices in early 2027. At the Investor Day they went one step further, and it is said that the tape-out of the first HBF die … is complete and customer samples are next year.”

> “the layer-count competition and the bonding transition are the stacking of cost, HBF is the stacking of bandwidth, and zHBM is the stacking of position.”

> “Design and optimization of TSV interface circuits connecting memory die to logic die.”
> “Column redundancy and lane repair schemes compatible with HBM-like highly parallel bus architecture.”

> “HBF receiving one seat means one HBM stack drops out as it is. It is trading a seat that gave 2TB/s-class bandwidth and tens of GB of capacity for 512GB of capacity, so neither side can easily yield a seat. Since it is a fight over seats, it is zero-sum.”

> “An optical signal travels 1 meter in roughly 5 nanoseconds. Even if you move an HBF stack from beside the processor to 2 meters away across the rack, and add all of the optical conversion, switches, and protocol delays on top, the added portion ends at the level of hundreds of nanoseconds. In front of an access latency of tens of microseconds, it is at the level of one hundredth.”

> “My claim is not ‘on-package loses’ but ‘the increment accumulates on the optics side’ … If the former, you should sell the memory companies, but if the latter, it is a picture of holding the memory companies and the optics companies together.”

> “Sandisk’s official wording is TSV and microbumps plus ‘proprietary stacking technology,’ so the bonding method is not confirmed as TCB. … no equipment company has announced an HBF-related order.”

> “The checking dates are these. HBF sample shipment in the second half of this year and the customer samples said to be next year, the first inference devices said to be early 2027, NAND-side new product mentions at Micron’s earnings call in late December, and the spec updates of OFC next March and FMS next August.”
