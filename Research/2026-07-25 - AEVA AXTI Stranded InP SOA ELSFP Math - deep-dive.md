---
publish: false
date: 2026-07-25
updated: 2026-08-14
tags: [research, Semiconductors, LITE, AXTI, AEVA, Optics]
sector: Custom Silicon & Networking Semiconductors
ticker: AXTI
propagated_to: [LITE]
source: 'https://irrationalanalysis.substack.com/p/stranded-indium-phosphide'
source_type: deep-dive
---

# Stranded Indium Phosphide — SOA ELSFP Math

## Thesis Delta
Consensus prices leftover LiDAR InP capacity as stranded/dead and treats CPO/NPO ELS as a [[Theses/LITE - Lumentum]] / Coherent / Broadcom UHP-DFB allocation problem that other end-markets can relieve the way DRAM annexes consumer bits → this follow-up's public XLSX ("InP Model Lidar Shitco Edition") says a 1×100 mW seed + 4×650 mW SOA + PLC-split 8-fiber ELSFP still hits 22 dBm/fiber at ~17% laser-vendor residual GM vs ~51% for 8×250 mW discrete DFB, so the "dead" LiDAR SOA inventory is a sellable shortage valve, not a write-off. [Semis #1] InP is already ~80% AI with zero consumer spillover (IA: ignore the point estimates, keep the annex logic); [G-10] author still owns LITE / AXTI / AAOI, not AEVA or [[Theses/SIVE - Sivers Semiconductors]] — the kludge is an existence proof, not a preferred equity.

## Summary
Follow-up to [[Research/2026-07-19 - LITE COHR AEVA Practical SOA for CPO NPO - deep-dive]]. IA restates SOA as "a DFB without gratings" and immediately qualifies it: pre-amp section, taper, "weird optical beam shape." High-power SOA is a LiDAR-house skill, not a datacom-house skill. The load-bearing industry claim is an unnamed contact's DRAM-vs-InP annex analogy: ~25% of DRAM already goes to AI so consumer can be raided; ~80% of InP already goes to AI and InP has no consumer use-case to annex. IA tells the reader to discard the percentages and keep the mechanism — InP tightness cannot be solved by shooting smartphones.

Design objective for a single-λ 1310 nm ELSFP aimed at NPO/CPO: 22 dBm coupled into each of eight output fibers. Two mock-ups. **Normal way:** eight 250 mW-class DFBs, each L–I–L into an 8-fiber FAU; post-isolator ~23.5–24 dBm, FAU output 22–22.5 dBm. **LiDAR way:** one 100 mW DFB (20 dBm) seeds PLC #1 (1×4 split: 18.5 dBm in / 11.5 dBm out), four 650 mW SOAs boost 10 dBm → 28 dBm, L–I–L after each SOA, PLC #2 (4×1:2) takes 26.5 dBm down to 22 dBm into the same 8-fiber FAU. Device-level, the 650 mW SOA wins InP-area efficiency (464 mW/mm² vs ~408 for 250 mW CW and 400 for 100 mW CW). That ranking is incomplete: a discrete SOA still needs a CW seed, and coupling/isolator losses after the SOA's beam shape erase the area win at product level.

Product-level ELSFP model (consign devices to a TFC/Fabrinet/Accelink-class CM at 12% GM; hyperscaler ASP $300/module): 8× DFB BOM $124.8 / CM cost $131.4 / residual laser-vendor GM ~51%; SOA path BOM $188.3 / CM cost $221.5 / residual ~17%. IA's punchline is that a dead LiDAR franchise would take the 17% path at volume. Playbook: Lumentum, Coherent, Broadcom, Sumitomo, Furukawa, AAOI "do not know how to make this niche device." Two viable high-quality NPO/CPO SOAs — unnamed private IDM, plus AEVA with Sivers as InP fab (Aeva public claims independently checked for the COGS/InP rows). Anon mail 2026-07-22 is the Sivers–Aeva pointer (early-2024 call mention; ECOC 2025 DFB+SOA deck; LiDAR volume-ramp PR, possibly Daimler). IA still hates Sivers' 8/16-λ monolithic DWDM array ("garbage," "horrific" yield, Ayar "fleeing") and the Ayar/AMD fan story: Lumentum cut everyone except Nvidia; Ayar did not remove Lumentum from the site — Lumentum removed Ayar. Matt Sysak screenshot (Ayar laser VP → Lumentum CTO) is the "go ask" pointer. Split verdict: Sivers earns more revenue and GM dollars off Aeva SOA than it ever did off Ayar; AEVA is a more interesting buy than Sivers; AXTI is more interesting than both. Book: LITE, AXTI, AAOI only.

## Framework / Mental Model
**InP Model — LiDAR Shitco Edition** (IA, public XLSX). Two stacked sheets, not a scorecard.

| Layer | Question | Axes |
|---|---|---|
| `inp_device` | photons per mm² of 4" InP and die COGS | die geometry, dice/wafer, fab yield, package yield, $2k wafer / $4k process / $500 pkg (Rx column is the 6" exception), guessed ASP, optical power per InP area |
| `ELSFP_COGS_MODEL` | can the die win survive a 22 dBm × 8-fiber module | BOM (DFB, lens, isolator, active align, TEC, SOA), yield penalty, 12% CM take, $300 hyperscaler ASP, residual GM to the laser owner |

Methodology: rank devices on InP-area efficiency first, then force the winner through an 8-fiber ELSFP with explicit seed-laser + coupling tax. Device sheet assumes external sale; ELSFP sheet assumes the laser owner consigns dice into the CM and keeps the residual after the CM's 12%. Outputs (51% vs 17%, 464 vs 408 mW/mm²) sit in Evidence. Companion physics (FWM, discrete vs monolithic MOPA, alignment count) lives in the 2026-07-19 primer, not this workbook.

## Evidence

**Device sheet (`inp_device`, 4" InP except Coherent lite Rx on 6")** [1×: IA XLSX]

| Product | Area mm² | Dice/wafer | Fab yld % | Pkg yld % | Sellable | COGS $/die | ASP $ (guess) | GM % | mW per mm² |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100 mW CW | 0.25 | 25,888 | 50 | 50 | 6,472 | 1.0 | 3.5 | 71 | 400 |
| 250 mW CW | 0.6125 | 10,103 | 50 | 50 | 2,526 | 2.6 | 10 | 74 | 408 |
| 650 mW SOA | 1.4 | 4,551 | 35 | 40 | 637 | 10.2 | 20 | 49 | 464 |
| 400 mW CW, competent (0.5–1 MHz) | 1.5 | 4,308 | 50 | 50 | 1,077 | 6.0 | 40 | 85 | 267 |
| 400 mW CW, loser (0.5–1 MHz) | 2.5 | 2,526 | 30 | 50 | 379 | 17.2 | 40 | 57 | 160 |
| 200G EML | 0.375 | 17,200 | 30 | 50 | 2,580 | 2.5 | 10 | 75 | — |
| Coherent lite Rx (6") | 10 | 1,513 | 20 | 80 | 242 | 49.6 | 100 | 50 | — |

Wafer $2,000 / process $4,000 / pkg $500 on every 4" column; Rx uses wafer $6,000 / process $5,000 / pkg $1,000. [est.: IA XLSX]

**ELSFP optical path (mock-up, 22 dBm × 8 fibers, 1310 nm)** [1×: IA figure]

| Node | LiDAR / SOA path | Normal / 8× DFB path |
|---|---|---|
| Source | 1× 100 mW DFB = 20 dBm | 8× 250 mW DFB ≈ 24 dBm |
| After first L–I–L | 18.5 dBm into PLC #1 (1×4) | 23.5–24 dBm into FAU |
| After split / SOA | 11.5 dBm out of PLC; 10 dBm into each 650 mW SOA; 28 dBm SOA out | — |
| After second L–I–L / PLC #2 | 26.5 dBm into 4×1:2; 22 dBm at 8-fiber FAU | 22–22.5 dBm at 8-fiber FAU |
| Passives | 18 lenses, 5 isolators, 19 active aligns, 5 TECs, 4 SOAs | 16 lenses, 8 isolators, 16 active aligns, 4 TECs, 0 SOA |

**ELSFP COGS (consign to CM, 12% CM GM, $300 hyperscaler ASP)** [est.: IA XLSX]

| Line | Normal (8× DFB) | LiDAR (1 DFB + 4 SOA) | Note |
|---|---:|---:|---|
| # DFB / $ | 8 × 2.6 | 1 × 3.5 | 250 mW COGS vs 100 mW ASP; DFB vendor books device GM here |
| # Lens / $ | 16 × 1.5 | 18 × 2.0 | SOA path needs custom lenses for beam shape |
| # Isolator / $ | 8 × 2 | 5 × 2 | Isolator $ flat |
| # Active align / $ | 16 × 1.5 | 19 × 2.0 | tighter SOA tolerances |
| # TEC / $ | 4 × 10 | 5 × 12 | "2 DFB per TEC possible" on the discrete path |
| # SOA / $ | 0 | 4 × 10.2 | LiDAR house books device GM here |
| BOM $ | 124.8 | 188.3 | |
| Yield penalty | 95% | 85% | |
| CM final $ | 131.4 | 221.5 | BOM / penalty |
| ASP to CM $ | 147.2 | 248.1 | CM +12% |
| Hyperscaler ASP $ | 300 | 300 | same selling price |
| Laser-owner residual GM | 51% | 17% | ($300 − ASP-to-CM) / $300 |

**Industry / positioning claims** [1×: IA]

| Claim | Detail | Tag |
|---|---|---|
| DRAM vs InP annex | ~25% of DRAM already AI (can raid consumer); ~80% of InP already AI; InP has zero consumer use-case | [1×: unnamed contact via IA]; IA: ignore the % |
| High-power SOA makers | "only a very small number of LiDAR" houses; two viable for NPO/CPO: unnamed private IDM + AEVA | [1×: IA] |
| AEVA fab | Sivers InP partner; Aeva public claims independently verified for the model | [1×: IA]; anon 2026-07-22 |
| Usual-suspect gap | Lumentum, Coherent, Broadcom, Sumitomo, Furukawa, AAOI do not make this niche | [1×: IA] |
| Ayar / LITE | Lumentum cut everyone except Nvidia; Ayar left LITE on the site; LITE removed Ayar | [1×: IA] |
| Sivers DWDM array | 8/16-λ monolithic InP; "garbage"; yield "horrific"; Ayar fleeing | [1×: IA] |
| Sivers P&L mix | more $ and GM$ off Aeva SOA than off Ayar | [1×: IA] |
| Author book | LITE, AXTI, AAOI; not AEVA, not Sivers | [1×: IA] |
| Preference order | AEVA > Sivers; AXTI > both | [1×: IA] |

## Contradiction Check
**Supports [[Theses/LITE - Lumentum]] §Summary (sold-out InP / "arms dealer") and §Bull Case InP-substrate prepay chain.** [Semis #1] the annex-failure claim is the mechanism behind "InP world is apocalyptic": there is no consumer pool to steal. [Semis #8] NPO/CPO 22 dBm × 8-fiber ELSFP is the architecture that remaps the bottleneck from 200G EML onto UHP CW plus, as a second-best, SOA-boosted mid-power. Author book (LITE first) is consistent with the arms-dealer hierarchy.

**Challenges LITE §Bear Case (CPO migrates value to a "relatively standardized and commoditized" CW DFB/ELS layer) and §Risk #3 (CW lower-ASP, volume must offset).** On this workbook a 250 mW CW is 74% device GM and a "competent" 400 mW narrow-linewidth part is 85% — the opposite of a commodity print. The 51% ELSFP residual on the discrete-DFB path is the module-level echo of that device rent. [Semis #2] the qualification gate here is *not* SOA; usual suspects skipped the niche because they were busy in "real markets." SOA is the overflow valve, not the moat. Single falsifier for the LITE read: Broadcom / Lumentum / Coherent ship UHP DFB in enough volume that 17% SOA ELSFPs stop clearing. Secondary falsifier: a competent 400 mW vendor (the 85% GM column) floods, collapsing the "sold out" assumption that makes 17% still sellable.

**Supports [[Theses/IQE - IQE]] §Key Non-consensus Insight (global InP supply gap / SiPh still needs III-V light) and §Summary structural-InP-demand leg.** Every column that matters in `inp_device` is 4" InP area; the SOA path *increases* InP intensity at module level (four 1.4 mm² SOAs + a seed vs eight 0.61 mm² DFBs) even as it saves discrete-UHP die. The source never names IQE. It prefers AXTI as the substrate expression of the same shortage. Neutral-to-supportive on epi demand; silent on the dead M&A special-situation.

**Mixed / net-negative for [[Theses/SIVE - Sivers Semiconductors]] §Summary overflow thesis and §Key Non-consensus Insight #1 (listed ELS overflow / Ayar–POET–CPO book).** IA's one constructive Sivers sentence is the Aeva SOA P&L (more $ and GM$ than Ayar). The same post retires the Ayar/AMD DWDM-array story that the overflow narrative still leans on, and ranks Sivers below AEVA and below AXTI. [G-3] this is a mix shift, not a compounder re-rate. Touches SIVE §Conviction Trigger → CLOSE (d) (Aeva ramp delay past 2029): that trigger is now the *only* IA-endorsed cash path in this note — if Aeva slips, the "mildly bullish" clause dies and the DWDM-array hate is what remains. Also pressures SIVE §Business Model SOA line: the 49% device GM / 17% module residual is the economic ceiling IA will grant a LiDAR-origin SOA, versus LITE's 51% discrete-DFB residual.

**No AXTI thesis in the vault.** Author ranks AXTI above AEVA and Sivers as the cleanest way to own the InP shortage; that preference is untested against a dedicated AXTI note.

**[G-10] / [G-13] outside view.** Reference class for LiDAR-to-datacom pivots is hostile; IA applies that class to "the vast majority" of LiDAR names and carves out two exceptions (private IDM + AEVA). Cross-model agreement that InP is the bottleneck ([Semis #1], [G-4] frenzy overbuild of AI optics, LITE/IQE theses) is the cue to hunt the bear: UHP DFB ramps at LITE/AVGO/COHR, or SOA coupling/reliability failing in the field, both kill the 17% path without touching EML rent. [Semis #17] the usual-suspect "they will just make SOA" supply response is the assumption this post is written against.

## Source Excerpts
> "Only 25% of the worlds DRAM goes to AI. Can just take more from consumer. 80% of InP already going to AI." … "Ignore the absolute percentages he said. The core argument is true. InP has ZERO use-case for consumer markets."

> "As you can see, a 650 mW SOA has better InP area efficiency (more photons per unit area of InP) but this basic model at a device level misses two critical attributes. 1. You still need a CW laser to seed the discrete SOA. 2. Coupling losses from many lenses and isolators hurt a lot."

> "Normal way gets 51% gross margin while the LiDAR shitco way gets only 17%."

> "There are only two that have viable, high-quality SOA appropriate for NPO/CPO market. One is privately held IDM … The other is AEVA who manufactures with Seivers as the InP fab partner."

> "Lumentum cut everyone except Nvidia off. Ayar did not remove Lumentum from their website. Lumentum removed Ayar."

> "Seivers will may way more money (in revenue $ and gross margin $) off Aeva than they ever did off Ayar Labs." … "Aeva more interesting buy than Seivers and AXTI more interesting that both of them." … "I only own Lumentum, AXTI, and AAOI."
