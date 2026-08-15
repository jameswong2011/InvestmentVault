---
publish: false
date: 2026-06-27
tags: [research, deep-dive, 2383, 3110, copper-clad-laminate, glass-cloth]
sector: Copper-Clad Laminate & PCB Materials
ticker: [2383, 3110]
source: Web research 2026-06-27 (TrendForce glass-fiber-cloth shortage + T-glass deep-dive; Digitimes Doosan/EMC-Rubin Nov-2025 & Asahi-Kasei Apr-2026; queenems M9 CCL guide; GlobalTechResearch/yzyz NEZ-vs-Q-Glass; TSPA Semiconductor; cloudnews; hilelectronic; openpr); see Source Excerpts
source_type: deep-dive
propagated_to: [2383, 3110]
---

# M9 Quartz vs Low-Dk Glass — Asahi-Cohort Quartz Taking the Early M9 Majority: Impact on EMC & Nittobo

## Thesis Delta

- **[[Theses/3110 - Nitto Boseki]] — confirms and sharpens the →LOW trigger; damage is real but bounded.** M9 ("Low Dk3") is a *quartz* tier, and Nittobo's ~90% share is in T-glass (substrate, Low CTE) + NER-glass (Low Dk2, M8-class) — **not quartz**. Per TrendForce, the "Low Dk3 (Q-glass)" cohort — **Asahi Kasei, Shin-Etsu (SQX), Glotech, Feilihua, Taishan Fiberglass, Hong Ho** — is "collectively capturing the majority share in the early stages" of M9. Nittobo's answer (NEZ) is an evolved *glass fiber* (Dk ~4.0), structurally a half-step behind quartz (Dk ~3.7, Df ~0.0005, CTE ~0.5 ppm/°C). So the ~90% is **node-bound**, and the qualification-gate moat does not extend to a chemistry Nittobo does not lead → reinforces **reassess toward LOW**. Bound: M9 is the smallest/newest slice (switch-tray/backplane); quartz's ~2× cost + harder processing keep glass fiber in the larger M8/M8.5 + substrate volume, where Nittobo's allocation moat holds through 2027. Net read: monopoly multiple on an oligopoly franchise, not a franchise gone.
- **[[Theses/2383 - Elite Material]] — refines "material-agnostic laminator" toward ambiguous-to-negative.** Quartz at M9 (1) **erodes EMC's Insight-#3 allocation moat** (the quartz cohort adds qualified suppliers who can feed EMC's rivals), (2) gives a **supply-diversification offset** (less hostage to Nittobo's 40–55% hikes), and (3) — **the negative the vault missed** — a material-class change **resets CCL qualification, and EMC is not clearly ahead at M9.** Per Digitimes (Nov 2025), **Doosan (DS-7409 M9Q) is the early M9-quartz volume leader and "poised to secure exclusive Nvidia Rubin CCL supply as EMC failed a GB300 test"**; EMC is pushing **EM-896K3** to close the gap, Shengyi developing equivalents → conviction net-negative at the leading edge; EM-896K3 Rubin qualification is the swing.

## Summary

The M9 grade (NVIDIA internal spec **Df ≤0.0007, Dk <3.0 at 10 GHz**, mass production **2H 2026**, mandated for the **78-layer Rubin Ultra orthogonal backplane** and 1.6T switch/backplane trays) is the first node where the glass-cloth *reinforcement changes material class* — from low-Dk **borosilicate glass fiber** (M7/M8) to **quartz "Q-glass" (~99.9% silica)**. This matters because Nittobo's near-monopoly is a *glass-chemistry* gate (drawing/weaving/spreading low-Dk borosilicate yarn); quartz sidesteps that gate with a different material, which is exactly why a new cohort — not Nittobo — leads the early M9 reinforcement supply.

The impact is **highly asymmetric**. For Nittobo it is existential to the *leading-edge* franchise: quartz taking the early M9 majority is the single falsifying datapoint the [[Research/2026-06-26 - 3110 - Stress Test]] flagged, and it confirms the ~90% statistic is current-node-bound. But the damage is bounded — M9 is the newest, smallest slice (the larger M8/M8.5 compute-tray and the T-glass substrate franchises are not displaced), and quartz's ~2× cost and harder processing preserve glass fiber in cost-sensitive layers. For EMC the event is a *moat-modifier with ambiguous-to-negative sign*: it erodes the scarce-glass allocation moat that entrenched EMC (Insight #3) while diversifying its supply — but, more sharply than the vault assumed, the node transition **resets CCL qualification at the same moment**, and EMC's leading-edge M9 incumbency is contested (Doosan early lead; an EMC GB300 stumble reported Nov-2025). EMC's halogen-free *resin* IP does not automatically transfer to *quartz-lamination* mastery (quartz's hardness drives drill-bit wear and residual-fiber protrusion in vias, a copper-plating yield problem).

The cross-thesis synthesis (value-layer-monopoly lens): the M9/quartz transition is adverse for **both halves of the toll road at once**. Upstream the rent **disperses** (a ≥6-supplier quartz field replaces a clean glass monopoly); downstream the CCL leadership **reshuffles** (Doosan up, EMC contested). The node the bull case prices for more content-per-board (true — M9 CCL runs ~15–20× FR-4) is simultaneously **less monopolistic at the layer that mattered** — the toll booth relocates from Nittobo's loom to a contested quartz field, and neither incumbent automatically collects it.

## Evidence

- **M9 = NVIDIA internal spec**: Df ≤0.0007, Dk <3.0 at 10 GHz; mass production 2H 2026; mandated on the 78-layer Rubin Ultra orthogonal backplane + 1.6T switch/backplane trays. Rubin compute trays run M6/M8.5 (Goldman channel check, Sept 2025); reports (Jan 2026) put CPX boards at M8, CX9 interconnect at M7, midplanes at M8 — i.e., **M9 is concentrated at switch/backplane, not the whole platform**.
- **Grade taxonomy (TrendForce)**: Low Dk1 (NE-glass) — Asahi Kasei, Taiwan Glass, Fulltech, Taishan, Hong Ho; **Low Dk2 (NER-glass) — Nittobo ~60–70%**; **Low Dk3 (Q-glass/quartz) — Asahi Kasei, Shin-Etsu, Glotech, Feilihua, Taishan, Hong Ho "collectively capturing the majority share in the early stages"**; **T-glass (Low CTE) — Nittobo ~90%** (alts Taiwan Glass, Fulltech, Hong Ho).
- **Spec gap**: Q-glass ~99.9% silica, Dk ~3.7 @10GHz, Df ~0.0005 (intrinsic quartz → ~0.0002 but post-processing lands ~0.0005), CTE ~0.5 ppm/°C. Nittobo NEZ (glass fiber): Dk ~4.0 @10GHz. NE-glass Df baseline ~0.001 (quartz ~half).
- **Cost / supply**: Q-glass ~$50/m vs NEZ ~$25–30/m (1.7–2×). M9 CCL ~15–20× FR-4 (M8 ~10–15×, M7 ~6–9×, M6 ~3–5×). M8/M9 Q-glass lead times 20+ weeks, allocation-only. Fewer than five M9 CCL producers globally.
- **Processing penalty**: pure quartz is harder than glass fiber → accelerated drill-bit wear, residual fiber protrusion in drilled holes affecting copper plating; demands advanced drill coatings + tighter tool-life management.
- **CCL-maker leadership at M9 (Digitimes Nov-2025; queenems)**: **Doosan DS-7409 M9Q = early volume leader, "poised to secure exclusive Nvidia Rubin CCL supply as EMC failed a GB300 test."** EMC pushing EM-896K3; Shengyi (S-series) in testing. "Most legacy manufacturers remain stuck in prototype testing."
- **Asahi Kasei (Digitimes Apr-2026)**: entering AI-chip fiberglass/quartz to challenge Nittobo's 90%; NEG (Nippon Electric Glass) also referenced; "no official, detailed announcement comparable to Nittobo's" (cloudnews) — capacity/ramp figures not yet public.
- **Nittobo defense**: >¥50B 2026–27 to triple T-glass (Japan + Taiwan), relief mid-2027 at earliest + ~6mo yield ramp; next-gen T-glass slated 2028 (reported targets incl. NVIDIA, Apple). Price hikes +20% (Aug-25), +20–30% (Apr-26).
- **Next node**: M10 (448G) in qualification; Feynman 2027+; NVIDIA + Wus testing M10 with HVLP5 foil + Q-glass (Ming-Chi Kuo, 13 Mar 2026) — quartz extends *up* the ladder, not a one-node blip.

## Framework / Mental Model

**The grade-taxonomy correction** is the analytical unlock: "M-grade" is not one ladder with one supplier. Map each tier to its reinforcement *material class* and the supplier set changes:

| Tier | Reinforcement | Lead supplier(s) | Nittobo position |
|---|---|---|---|
| M7 / M8 / M8.5 | low-Dk **glass fiber** (NE/NER) | **Nittobo ~60–70% NER** | franchise |
| **M9 ("Low Dk3")** | **quartz "Q-glass"** | **Asahi-led cohort (≥6)** | NEZ = a follower glass-fiber option |
| substrate core | **T-glass** (Low CTE) | **Nittobo ~90%** | franchise (separate contest) |

**Value Layer Monopoly read (hypothesis to test):** Nittobo passes the layer-location test for glass-*chemistry* but fails the durability test at the *material-class boundary* — §2 "falling switching costs / commoditizing layer" fires because quartz is a substitute that routes around the gate, and the replacement layer (quartz) is **fragmented, not monopolized** (≥6 suppliers), so the rent disperses rather than transferring. The toll booth relocates and thins. EMC remains a §2 **layer-renter** in either world (it rents glass *or* quartz), and the node reset removes the temporary allocation-scarcity advantage that made the rent feel like a moat. **Industry-Semis #8** (architecture transition remaps the bottleneck) is the mechanism; **#2/#13** say leadership at a remapped node is node-bound, not structural — which is why both names' leading-edge positions are contestable here.

## Contradiction Check

Genuine source conflicts — held open, not resolved by assertion:

1. **"Quartz cohort takes the early M9 majority" (TrendForce, NEZ-vs-Q-Glass) vs "M9 glass supplied at production scale almost exclusively by Nittobo" (one queenems read).** Most likely reconciliation: the latter conflates Nittobo's *overall* low-Dk dominance with quartz specifically; the grade-segmented TrendForce taxonomy is more precise (quartz ≠ Nittobo's franchise). But if "almost exclusively Nittobo" proves right for M9 *volume* (vs design-win optics), the Nittobo →LOW thesis weakens and the bear case is wrong on this leg. **Resolver:** actual 2026–27 M9 reinforcement volume split by supplier.
2. **EMC bullish (Goldman channel check, Sept-2025: "EMC benefits most" on Rubin) vs EMC adverse (Digitimes, Nov-2025: "EMC failed GB300 test," Doosan poised for exclusive Rubin CCL).** Both are channel checks two months apart; the contradiction is itself the signal that the M9/Rubin socket is **live and unsettled**, not a settled loss. **Resolver:** EMC EM-896K3 qualification status on Rubin switch trays; whether Doosan exclusivity is confirmed or splits.
3. **Q-glass Dk cited as ~3.0 (queenems) vs ~3.7 (NEZ-vs-Q-Glass).** Likely intrinsic-quartz vs finished-cloth/post-processing difference; immaterial to the directional read (quartz < NEZ either way).
4. **Premise calibration**: the user framed "Asahi quartz taking the early M9 majority" as given. Evidence supports it *as a quartz-cohort* phenomenon (Asahi the most prominent, not sole); it is an *early-stage* read pre-mass-production (2H 2026), so it is a leading indicator, not a closed result.

**Strongest counter to the bear synthesis:** quartz's ~2× cost + harder drilling/plating yield could cap it at the switch-tray/backplane niche, leaving the larger M8/M8.5 glass-fiber volume — and Nittobo's allocation moat — intact through 2027; quartz then is a small top-slice, not a franchise breaker. That keeps the node contest real but *smaller than the multiple implies in either direction*.

## Source Excerpts

- TrendForce — *Glass Fiber Cloth: The Underlying Material Shortage in AI Infrastructure* (grade taxonomy, shares, ¥50B Nittobo capex): https://insights.trendforce.com/p/glass-fiber-cloth-shortage
- TrendForce — *Nittobo Reportedly Plans 2028 Next-Gen T-Glass* (NVIDIA/Apple targets): https://www.trendforce.com/news/2026/02/04/news-nittobo-reportedly-plans-2028-next-gen-t-glass-customers-may-include-nvidia-apple-and-others/
- Digitimes — *Doosan poised to secure exclusive Nvidia Rubin CCL supply as EMC fails GB300 test* (Nov 21, 2025, paywalled — headline + snippet): https://www.digitimes.com/news/a20251121PD242/doosan-ccl-nvidia-emc-rubin.html
- Digitimes — *Asahi Kasei enters AI chip fiberglass market to challenge Nittobo's dominance* (Apr 2, 2026, paywalled — headline + snippet): https://www.digitimes.com/news/a20260402PD227/asahi-kasei-ai-chip-fiberglass-cloth-materials-expansion-nittobo.html
- queenems — *M9 CCL Guide: NVIDIA AI Server PCB Standards* (NVIDIA spec, Doosan/Shengyi/EMC, Rubin tray split): https://www.queenems.com/blog/m9-ccl-guide-nvidia-ai-server-pcb-standards/
- GlobalTechResearch / yzyz — *NEZ vs. Q Glass – Who Will be the Next Electronic Fiber Glass Winner?* (Dk/Df, $/m, processing): https://globaltechresearch.substack.com/p/nez-vs-q-glass-who-will-be-the-next
- cloudnews — *Asahi Kasei Breaks Through a Key Bottleneck for AI Chips*: https://cloudnews.tech/asahi-kasei-breaks-through-a-key-bottleneck-for-ai-chips/
- TSPA Semiconductor — *From Glass Fiber to CCL* (paywalled): https://tspasemiconductor.substack.com/p/from-glass-fiber-to-ccl-the-material
- hilelectronic — *PCB Material Shortages / Raw Material Costs 2026*: https://hilelectronic.com/pcb-material-shortages/
- openpr — *M9 Copper Clad Laminates Latest Market Analysis Report 2026*: https://www.openpr.com/news/4296577/m9-copper-clad-laminates-latest-market-analysis-report-2026
