---
publish: false
date: 2026-08-27
tags: [research, DRAM, HBM, MU, 000660, BESI, TSM, Hot-Chips]
sector: DRAM & HBM Memory
ticker: MU
source: 'https://www.viksnewsletter.com/p/hot-chips-2026-tuning-into-memory'
source_type: deep-dive
propagated_to: [MU, 000660, TSM, BESI]
---

# Hot Chips 2026: Tuning into Memory Vibes

## Thesis Delta

Consensus still prices [[Theses/000660 - SK Hynix]]'s near-term HBM edge as an **MR-MUF process/materials moat** that survives through HBM4E 16-Hi (JEDEC height cushion; Namics EMC), and prices [[Theses/MU - Micron Technology]]'s HBM4 story as **qualification ≠ first-wave attach** (list ≠ boards; TSMC base-die on HBM4E CY27) with stack-height despec read as either cycle cliff or volume unlock. Viks' Hot Chips 2026 free note (conference notes on Micron / Samsung / SK Hynix talks) implies a different competitive axis: **custom base die on leading-edge logic nodes is the durable differentiator even if stack heights stay at 8-/12-Hi**, Samsung already has in-house 4nm logic for the base die (1c DRAM + 4nm logic) while MU/SKH partner out, and **MR-MUF's thermal "secret sauce" collapses once the industry moves to hybrid bonding** — leaving execution, not process chemistry, as the tie-breaker. Flag only (no conviction/status change): touches 000660 Insight #2 (MR-MUF process vs architectural hybrid-bonding) and Outstanding Q2; touches MU Outstanding Q on 8-Hi / base-die roadmap silence; does **not** fire 000660 → HIGH/LOW/CLOSE or MU → HIGH/LOW/CLOSE (no Rubin allocation %, no Namics renewal, no CXMT HBM qual, no board meter).

## Summary

Viks (Viks Newsletter / SemiExponent) attended Hot Chips for the first time and frames it as a small, single-track conference where the big-three memory talks functioned as heavily technical keynotes. This free post is explicitly an **initial note capture** — Micron, then Samsung, then SK Hynix — with roadmap implications deferred. The author's ranking is clear: Micron's talk was the least impressive (memory-wall / roofline / stacking bandwidth already known to an AI audience); Samsung's custom-base-die roadmap was the highlight (live-tweeted); SK Hynix's talk centers on MR-MUF vs hybrid bonding and thermal comparison tables that put Micron alone without an external heat-removal block.

The load-bearing argument in the Final Thought is that **custom base die on logic nodes is decoupled from stack-height ambition**. Even if production environments never need 12-/16-/20-Hi (and the note cites despec pressure from 12-Hi → 8-Hi, possibly 4-Hi for some SKUs, because HBM wafers consume 3–4× more wafers per bit and memory already exceeds half of rack cost), a logic-node base die still enables higher Gbps/pin, smaller/more efficient D2D PHY, controller offload onto the HBM stack, on-base-die SRAM repair scratchpad, RAS/telemetry/test, memory-extension controllers, and optional near-memory compute. Samsung alone among the three has that logic node in-house; Micron and SK Hynix must partner. The author calls Micron's HBM4 use of DRAM nodes for the logic/base die a "silent dig" target of Samsung's 1c+4nm slide.

SK Hynix content confirms the vault's existing MR-MUF → hybrid-bonding transition framing: MR-MUF works for 16-Hi at **775 µm** overall height (JEDEC revised to allow it), with lower thermal resistance vs TCB / better mid-stack heat removal — but **once hybrid bonding arrives (and if 20-Hi is still needed), everyone's hybrid-bonded HBM looks the same** and competition collapses to execution. Thermal-management comparison on the SKH slide: Samsung **Heat Path Block (HPB)**, SK Hynix **Integrated Cooling Engine (ICE)**, Micron **"improve circuit design"** only — either MU is behind next-gen cooling or MU has concluded stack height / lane rate will never require external cooling blocks. An Intel **EMIB** customer note on SKH's slide is a secondary packaging-path data point.

## Framework / Mental Model

**Samsung three-phase custom-base-die roadmap** (Hot Chips; Viks paraphrase). Re-applicable whenever scoring IDM vertical integration on HBM base die vs foundry-partnered peers.

| Phase | Name | Mechanism | What it unlocks | Caveat in source |
|---|---|---|---|---|
| 1 | Low hanging fruit | Logic-node base die shrinks HBM PHY (D2D to XPU); memory-controller offload from XPU → base die; on-die SRAM as failed-DRAM-cell scratchpad | More XPU compute area; more base-die area for advanced functions; repair without discarding stacks; higher pin rate (HBM5 path) | Smaller PHY → higher thermal density → needs **integrated Heat Path Block (HPB)** at HBM5; Samsung rejects UCIe for D2D (larger, worse energy/bit vs custom PHY) |
| 2 | RAS, Test, Extension, Processing | Smaller transistors free area for RAS, test, HBM health telemetry; optional second-stack / DRAM extension controller; optional matrix compression/encoding compute on base die | Telemetry matters because HBM is **#2 root cause of training-run interruptions** (after GPU fault; software #3, networking #4); latency/efficiency if compute never leaves the base die | "Nice accelerator" block diagrams are easy; **real performance benefits are questionable** |
| 3 | Going vertical | Stack custom base die + HBM **on top of** the logic/XPU die | Shorter compute↔memory distance → power efficiency + bandwidth via more parallel paths across chip area (not just beachfront) | Hard; proves roadmap optionality more than near-term SKU |

**Companion contrast (SK Hynix talk):** MR-MUF thermal/warpage edge vs TCB is real through 16-Hi @ 775 µm; **hybrid bonding erases that edge**. Competitive axis after HB = execution. Cooling-block presence (HPB / ICE vs MU circuit-design-only) is a separate tell on whether a vendor expects high stack / high lane-rate thermals.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Source type / access | Free full post (author: "This is a free post") | [1×: Viks Newsletter] |
| Conference | Hot Chips 2026; first attendance by author; single-track | [1×: Viks] |
| Coverage set | Micron, Samsung, SK Hynix memory talks | [1×: Viks] |
| HBM as training-run interrupt cause | **#2** root cause after GPU fault; software #3, networking #4 | [1×: Viks citing prior study] |
| Micron talk absences called out | No 16-Hi/20-Hi scaling / hybrid-bonding roadmap; **no custom base die**; no cooling solutions for faster lane rates | [1×: Viks] |
| Industry stack-height rumor context | Downgrades / despec; 12-Hi → 8-Hi, possibly **4-Hi** for some SKUs | [1×: Viks] |
| HBM wafer intensity | HBM uses **3–4×** more wafers per bit vs commodity | [1×: Viks] |
| Rack cost share (memory) | Memory alone **> half** overall rack cost | [1×: Viks] |
| Samsung HBM5 illustrative capacity | **60 GB** | [1×: Viks / Samsung chart] |
| Samsung HBM5 illustrative bandwidth | **6 TB/s** | [1×: Viks / Samsung chart] |
| Implied HBM5 pin rate (author calc) | 6 TB/s ÷ **2,048** lanes → **~23.5 Gbps/pin** | [est.: Viks] |
| Current SOTA pin rate (author) | **16 Gbps** | [1×: Viks] |
| Implied HBM5 stack (author) | 60 GB ÷ **3 GB/die** → **20-Hi** | [est.: Viks] |
| Samsung HBM4E pin rate (confirmed in talk) | **16 Gbps/pin** | [1×: Viks / Samsung] |
| Samsung DRAM node (stated) | **1c** for memory | [1×: Viks / Samsung] |
| Samsung logic/base-die node (stated) | **4nm** | [1×: Viks / Samsung] |
| Micron HBM4 base-die dig | Used **DRAM nodes for logic die** in HBM4 (Samsung contrast) | [1×: Viks] |
| Samsung D2D link choice | Custom PHY preferred over **UCIe** (size + energy/bit) | [1×: Viks / Samsung] |
| Samsung HBM5 thermal add-on | Integrated **Heat Path Block (HPB)** for D2D PHY region | [1×: Viks / Samsung] |
| Phase-1 controller move | Memory controller offload XPU → custom base die | [1×: Viks / Samsung] |
| Phase-1 SRAM role | SRAM scratchpad substitutes for failed DRAM cells via controller remap | [1×: Viks / Samsung] |
| Phase-2 extras | RAS, test, HBM telemetry; extension controller (second HBM or DRAM); optional on-base-die compute (e.g. matrix compression/encoding) | [1×: Viks / Samsung] |
| SKH bonding process | **MR-MUF** (Mass-Reflow Mold-UnderFill) vs TCB | [1×: Viks / SK Hynix] |
| SKH 16-Hi MR-MUF height claim | Works for **16-Hi** at **775 µm** overall stack height; JEDEC revised to support | [1×: Viks / SK Hynix] |
| Hybrid-bonding implication (author) | MR-MUF advantage **ends**; all hybrid-bonded HBM "falls to the same level"; competition → **execution** | [1×: Viks] |
| Thermal resistance claim | MR-MUF lower thermal resistance vs TCB; better mid-stack heat removal | [1×: Viks / SK Hynix] |
| Cooling comparison (SKH slide) | Samsung **HPB**; SK Hynix **ICE** (Integrated Cooling Engine); Micron **circuit-design only** (no external heat-removal block) | [1×: Viks / SK Hynix] |
| SKH packaging customer note | Some customers use SKH memory with **Intel EMIB** | [1×: Viks / SK Hynix] |
| Partner dependency (author) | Samsung in-house logic; Micron & SK Hynix **need a partner** for logic-node base die | [1×: Viks] |
| Prior vault: Rubin Ultra 8-Hi despec | Aligns with despec / lower-stack narrative in this note | [[Research/2026-08-11 - MU NVDA Rubin Ultra 8-Hi HBM Despec - deep-dive]] |
| Prior vault: MR-MUF→HB equipment | Aligns with JEDEC 775 µm + hybrid-bonding erasure of MR-MUF edge | [[Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive]] |
| Prior vault: Samsung 2nm base-die option | Directionally consistent with Samsung logic-node base-die advantage (4nm now; 2nm HBM5 path in other coverage) | [[Research/2026-08-15 - 000660 TSM NVDA - Samsung 2nm HBM Base Die - news]] |

## Contradiction Check

- **Supports [[Theses/000660 - SK Hynix]] Insight #2** (MR-MUF is a process moat, not an architectural one; hybrid bonding collapses differentiation): Viks states the MR-MUF advantage "is no more" under hybrid bonding and competition becomes execution. Reinforces Outstanding Q2's hybrid-bonding / HBM5 question and the BESI Kinex insurance framing without adding a new allocation print. **Does not challenge** the kill trigger (Samsung >35% of first two Rubin shipping quarters) — no Rubin share data here.
- **Supports [[Theses/MU - Micron Technology]] "list ≠ boards" / catch-up hygiene posture**: Micron talk omitted custom base die, high-stack/HB roadmap, and external cooling — while Samsung showcased 1c+4nm base die and HPB, and SKH showed ICE. Consistent with MU as third-source / later architectural follower (TSMC base-die on HBM4E CY27 in thesis), not a new reason to promote conviction. **Does not fire** MU → HIGH (needs board meter ≥10% + LTA cap-off + TrendForce prints) or → CLOSE.
- **Challenges a soft consensus that stack-height roadmap = the only HBM competitive axis**: Final Thought argues custom base die remains important **even at lower stack heights** — complementary to [[Research/2026-08-11 - MU NVDA Rubin Ultra 8-Hi HBM Despec - deep-dive]] (despec as volume unlock) rather than contradictory: lower stacks can coexist with logic-node base-die competition on pin rate, PHY, RAS, and controller offload.
- **Samsung**: no dedicated thesis file; evidence is relevant to [[Sectors/DRAM & HBM Memory]] competitive table and to 000660's Samsung U-shape / dual-source narrative. Weak-match equipment fanout: [[Theses/BESI - BE Semiconductor Industries]] (hybrid bonding), [[Theses/TSM - Taiwan Semiconductor]] (MU/SKH base-die partner), [[Theses/INTC - Intel]] (EMIB mention only).
- Honest low-signal caveat: conference-note initial capture; charts not reproduced numerically beyond the author's pin-rate/stack arithmetic; no ASPs, yields, or Rubin allocation percentages — confirms roadmap framing more than near-term earnings.

## Source Excerpts

> "HBM5 with a capacity of 60GB and 6 TB/s bandwidth would be nice. Let's calculate some numbers here. 6 TB/s with 2,048 lanes would mean 23.5 Gbps per pin. We are currently at 16 Gbps state-of-the-art... For 60 GB capacity with 3 GB per die, that would put the stack height at 20 high."

> "Samsung is using 1c node for memory and 4nm node for logic. It results in a significant power reduction in the base die. The slide below is a silent dig at Micron who used DRAM nodes for logic die in HBM4."

> "In fact, they have no problem in boldly claiming that MRMUF method works well for 16-high HBM, but that it would require 775 microns of overall stack height. The JEDEC spec was actually revised to support the larger height, so it does add up."

> "When hybrid bonding is used, the \"secret sauce\" of SK Hynix with MRMUF is no more, and everybody's hybrid bonded HBM falls to the same level. If it comes down to this, it comes down to execution."

> "Samsung has Heat Block Path (HPB), and SK Hynix has Integrated Cooling Enging (ICE). Micron is just going to \"improve circuit design\" to get there."

> "Even if stack heights do not go to 12, 16, or 20 in production environments, the use of custom base die on leading edge logic nodes is going to become important... Samsung has the advantage in this playing field due to the availability of in-house advanced logic processes."

> "Of note was the fact that HBM is the 2nd most important root cause of training-run interruptions, apart from the GPU being faulty itself. Software and networking were #3 and #4, respectively."
