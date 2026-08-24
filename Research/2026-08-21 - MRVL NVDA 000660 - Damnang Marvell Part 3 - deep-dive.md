---
date: 2026-08-21
tags: [research, custom-silicon, networking, optical-dsp, MRVL, NVDA, 000660]
sector: Custom Silicon & Networking Semiconductors
ticker: MRVL
source: 'https://damnang2.substack.com/p/marvell-part-3-what-has-been-proven'
source_type: deep-dive
title: 'Marvell Part 3: What Has Been Proven, and What Is Still Open'
publication: Damnang
gmail_id: 1a024340bc1fa85f
author: Damnang
sender: damnang2@substack.com
publish: false
propagated_to: [MRVL, NVDA, 000660, AVGO]
---

# Marvell Part 3: What Has Been Proven, and What Is Still Open — Damnang

## Thesis Delta

Consensus, at $251 / ~$220B [1×: Damnang], already prices Marvell *above* management's FY28 $16.5B guide — the vault's [[Theses/MRVL - Marvell Technology]] Summary and Key Metrics still sit on the Aug 14 close ($222.02, ~$194B, 55× FY27E / 36× FY28E) with consensus FY28 revenue $16.7B ≈ the $16.5B target, so "deliver the guide" is treated as the priced base. This 21 August 2026 Damnang subscriber piece (Gmail `1a024340bc1fa85f`) implies the market has the *mix and the unit of analysis* wrong, not the top-line: FY27 incremental dollars are Interconnect (guide raised above 70%, four of five Part 2 checkpoints passed), FY28 is Custom (above 2×), and Custom Silicon should be modeled as **system content** (Google 8-K spans inference accelerators + storage controllers + NICs + memory-interface + near-memory compute; NVIDIA NVLink Fusion attaches custom XPU and scale-up networking together) rather than as a single accelerator socket. Author base-case implied price of $239 [est.] sits *below* the $251 spot, so further estimate revisions — not mere guide delivery — are required; the August 27 variables are **FY27 Interconnect growth** and the **Q3 guide**, and the October 6 Investor Day variable is **FY28 segment estimates**. Trigger touch (flag-only, no `/status`): [[Theses/MRVL - Marvell Technology#Conviction Triggers]] **HIGH leg 1** (signed Google custom-silicon commercial agreement for MPU or inference TPU) is **evidence-touched / near-fired, not fired** — the Aug 19 8-K discloses a July 29 commercial agreement that is *broader* than the trigger's MPU/inference-TPU wording, but HIGH still requires all three conjuncts and legs 2 (AWS T3 ≥400K) and 3 (Celestial PO / end-2026 tape-out) are unmet. $120B is the warrant **vesting ceiling**, not a PO or minimum (prior 2026-08-21 vault read unchanged). HIGH leg 3 is evidence-touched the other way: Photonic Fabric still contributes little to the P&L, CMM-Ax is Structera A not PF, no disclosed production customer. LOW leg 2 (Google BRCM-exclusive close-out) is **inverted**. CLOSE leg 1 (FY28 custom below $3.6B implied) is **inverted** on the author's $3.8B FY28 Custom split [est.]. Conviction/status unchanged (MRVL medium, HELD Medium 3.5–10% in [[Live Portfolio]]). [[Theses/NVDA - Nvidia]] has no Conviction Triggers section (no triggers to test). [[Theses/000660 - SK Hynix]] HIGH/LOW/CLOSE (Rubin HBM share, Samsung, CXMT) are **no-touch**; CMM-Ax is a CXL-PNM co-dev, not an HBM-allocation datapoint.

## Summary

Damnang's Part 3 is a checkpoint-and-valuation update on Marvell ahead of the August 27 Q2 FY27 print, not a company primer. The author's stance stays "very positive," but the analytical claim is narrower: four of five Part 2 checkpoints for the May 27 print have passed, Interconnect — not next-generation Custom ASP — delivered the FY27 earnings revision, and Custom's larger growth contribution is still a FY28 event. Company outlook is FY26 $8.195B → FY27 ~$11.5B → FY28 ~$16.5B, incremental ~$3.3B then ~$5.0B. FY27 Data Center growth ~50% and Interconnect above 70%; Q1 IR put Custom above 20% in FY27 and above 2× in FY28. On the author's segment bridge, more than half of the FY27 Data Center increase comes from Interconnect.

Optical / Interconnect is the most de-risked FY27 driver. Q1 IR: 800G demand holding up, 1.6T ramping quickly; the 1.6T transition raises DSP and analog front-end complexity and narrows qualified suppliers. TIA and driver guided to exceed $1B annualized within the next few quarters; DCI modules have line of sight to $1B annualized during FY28; FY28 scale-up optics outlook doubled from the prior $150M. Exposure is broadening from PAM4 DSP into analog front end, DCI, and scale-up optics — content across multiple link lengths and topologies at the same hyperscaler, not a single transceiver cycle. Switching sits on the same axis: FY27 scale-out switch revenue above $600M and FY28 about $1B. Teralynx T100 is 102.4Tbps, 512-port radix, typical power below 1,000W, with BGA, co-packaged copper, and co-packaged optics options. Higher radix / flatter fabric is a partial headwind to optical *unit* demand; Marvell can supply switch silicon and CPO together, so company-level content can still expand. The named lens is **system-level wallet share within the same customer**, not TAM by product line.

Memory Infrastructure is the least modeled: more architecture optionality than current revenue. CXL pooling and Photonic Fabric still contribute little to the P&L and are only partly in the price. The portfolio is about expanding capacity *outside local HBM* as KV cache grows with context length and agentic steps. NVIDIA's HBM4 despec and SK hynix CPO papers are read as pointing the same way. Bilateral programs are confirmed on all three pairs — NVIDIA–Marvell (custom XPU, scale-up networking, silicon photonics / NVLink Fusion), NVIDIA–SK hynix (next-generation AI memory), Marvell–SK hynix (CMM-Ax CXL-PNM, Aug 5: Structera A PNM engine + SK hynix memory + SK hynix software; Structera A = 16 Arm Neoverse V2 cores, up to 200GB/s; validation results at FMS 2026) — but **no three-party integrated program** is confirmed, and there is no evidence SK hynix or NVIDIA has adopted Photonic Fabric. CMM-Ax is a Structera A collaboration, separate from PF, validation-stage, no disclosed production customer. A PF–SK hynix memory-tier extension is flagged as an inference with no disclosed basis; confirmation is first PF customer and memory partner.

Custom Silicon's modeling unit is system content, not sockets. The Google 8-K filed August 19 (agreement signed July 29) spans AI inference accelerators, storage controllers, NICs, memory interface controllers, and near-memory compute. The accompanying warrant is the right to buy up to 58.97M Marvell shares at $206.58, ~6.7% of the pre-issuance share count. Only 1.36M shares time-vest over the first year; the rest vests 1/240 per $500M of purchases from FY27 Q3 through FY33. Full vest implies a cumulative $120B over seven years — **neither backlog nor minimum**; it is the incentive ceiling, purchasing entirely at Google's discretion. Dilution and revenue grow together; duration through FY33 is the signal that neither side treats this as a single-generation program. NVIDIA's March $2B investment and NVLink Fusion seat is the second system-content data point: custom XPUs + Fusion-compatible scale-up networking + silicon photonics co-development, so Custom, Networking, and Optics overlap in one architecture. FY28 Custom visibility improved; the earnings variable is production timing and cadence, not the contract headline.

Valuation: Aug 20 close $251 / ~$220B. Delivering the FY28 $16.5B guide alone implies an author base-case price of $239 [est.], below spot — the market is already above current guidance. EPS/implied-price rows in the source were author estimates (revenue, operating leverage, tax, diluted share count; Google warrant not in those EPS figures because most vests against qualifying revenue and permits cash or net exercise); Gmail PLAIN_TEXT did not carry the scenario table numbers beyond the $239 base. The author still sees "ample room" toward a bull case. Near-term catalysts: **August 27 earnings** (variables: FY27 Interconnect growth and the Q3 guide) and **October 6 Investor Day** (variable: FY28 segment estimates).

## Framework / Mental Model

**Name:** FY27 = Interconnect, FY28 = Custom, scored on a three-axis "how proven / FY27–28 earnings / upside left" grid, with Custom modeled as **system content** rather than sockets, and Optical/Switching modeled as **system-level wallet share** rather than product-line TAM (Damnang Part 3).

**Components.**

| Axis | Definition | How the source applies it |
|---|---|---|
| Part 2 checkpoint scorecard | Five pre-registered May 27 hurdles with pass / partial / fail | Interconnect growth, Q2 guide, DC mix, bookings tone passed; Custom HBM / advanced-packaging IR language only partly confirmed |
| Mix timing | Which engine prints earnings *this* year vs *next* | FY27 leverage = Interconnect (>70%); FY28 mix shift = Custom (>2×). Part 2 upside had been Custom ASP; the revision arrived from Interconnect first |
| Proven / earnings / upside (0–5) | Separate "how de-risked today," "how much is in FY27–28 P&L," and "how much is still optional" | Optical 5.0 / 5.0 / 4.0; Custom 4.0 / 3.5 / 5.0; Switching 3.5 / 3.5 / 4.0; Memory 3.0 / 2.0 / 5.0 [est.] |
| System content vs sockets | Custom is a bundle of XPU + attach (NICs, storage, memory interface, near-memory), not one accelerator win | Google 8-K five-product span; NVIDIA NVLink Fusion = custom XPU + scale-up networking + SiPh |
| Wallet share vs product TAM | Capture content across link lengths and topologies at the same hyperscaler | PAM4 DSP + TIA/driver + DCI + scale-up optics + switch + CPO as one customer wallet; T100's higher radix is a unit headwind but a content tailwind if Marvell supplies both switch and CPO |
| Bilateral vs trilateral | Three pairwise collaborations ≠ one joint program | NVIDIA–MRVL, NVIDIA–000660, MRVL–000660 confirmed; no three-party integration; PF adoption by SK hynix/NVIDIA not evidenced |
| Warrant as ceiling, not PO | Vesting math is an incentive schedule | $120B = 240 × $500M; 1.36M time-vest; rest performance-vest FY27 Q3–FY33; purchasing at Google's discretion |
| Guide delivery vs revision | Spot vs the price that *just* delivers company FY28 revenue | $16.5B delivered → base $239 [est.] vs spot $251; Aug 27 prints Interconnect/Q3, Oct 6 reprints FY28 segments |

**Methodology.** Treat company outlook totals ($8.195B / ~$11.5B / ~$16.5B) as given; treat segment splits as author estimates. Score businesses on proven/earnings/upside separately so Memory can be high-optionality and low-P&L at once. Do not convert the Google warrant ceiling into backlog. Do not infer a three-party NVIDIA–SK hynix–Marvell program from three bilateral links. Confirmation for the PF–DRAM inference is first disclosed Photonic Fabric customer and memory partner.

## Evidence

All figures below are single-sourced to this Damnang 21 August 2026 subscriber essay (Gmail `1a024340bc1fa85f`, PLAIN_TEXT full) unless noted. Segment splits, proven/upside scores, and the $239 base implied price are author estimates. [1×: Damnang / damnang2.substack.com]

| Claim | Figure / statement | Tag |
|---|---|---|
| Publication | Damnang; 2026-08-21T12:01:08Z (20:01 SGT); Gmail `1a024340bc1fa85f`; URL `https://damnang2.substack.com/p/marvell-part-3-what-has-been-proven` | [1×: Damnang] |
| Stance | Author remains "very positive" on Marvell | [1×: Damnang] |
| Checkpoint score | Four of five Part 2 May 27 checkpoints passed; one partly confirmed | [1×: Damnang] |
| Interconnect growth hurdle | Positive if raised from 50% into the 60s → FY27 guide raised to **above 70%**; cleared by a wide margin | [1×: Damnang] |
| Q2 revenue-guide hurdle | $2.55B or higher → **$2.70B midpoint**; passed | [1×: Damnang] |
| DC dollars / mix hurdle | Whether Interconnect outpaces Custom → Q1 DC **$1.833B**, +27% YoY; Interconnect leads FY27 DC growth of about 50%; passed | [1×: Damnang] |
| Bookings tone hurdle | Record pace maintained → "exceptional AI-related bookings"; passed | [1×: Damnang] |
| Custom HBM / advanced packaging hurdle | Whether the terms first appear in IR language → exact keywords have not appeared; Google memory-interface / near-memory scope and NVIDIA silicon-photonics collaboration added instead; **partly confirmed** | [1×: Damnang] |
| FY26 revenue | **$8.195B** | [1×: Damnang] |
| FY27 company outlook | roughly **$11.5B** | [1×: Damnang] |
| FY28 company outlook | roughly **$16.5B** | [1×: Damnang] |
| Incremental revenue | about **$3.3B** in FY27 and a further **$5.0B** in FY28 | [1×: Damnang] |
| FY27 DC growth guide | about **50%** | [1×: Damnang] |
| FY27 Interconnect guide | **above 70%** | [1×: Damnang] |
| Custom growth (Q1 IR) | **above 20%** in FY27 and **above 2×** in FY28 | [1×: Damnang] |
| FY27 DC mix (author) | more than half of the FY27 Data Center *increase* comes from Interconnect | [1×: Damnang; est.] |
| Author segment split FY26 | Interconnect **$2.4B** / Custom **$1.5B** / else **$4.3B** / total **$8.2B** | [est.] |
| Author segment split FY27 | Interconnect **$4.1B** (+$1.7B) / Custom **$1.8B** (+$0.3B) / else **$5.6B** / total **$11.5B** | [est.] |
| Author segment split FY28 | Interconnect **$6.0B** (+$1.9B) / Custom **$3.8B** (+$2.0B) / else **$6.7B** / total **$16.5B** | [est.] |
| Optical proven / earnings / upside | **5.0 / 5.0 / 4.0** (1.6T, TIA/driver, DCI) | [est.] |
| Custom proven / earnings / upside | **4.0 / 3.5 / 5.0** (XPU, XPU-attach, Google TPU) | [est.] |
| Switching proven / earnings / upside | **3.5 / 3.5 / 4.0** (51.2T, 102.4T T100) | [est.] |
| Memory proven / earnings / upside | **3.0 / 2.0 / 5.0** (CXL, Structera, Photonic Fabric) | [est.] |
| 800G / 1.6T | 800G demand holding up strongly; 1.6T ramping quickly (Q1 IR) | [1×: Damnang] |
| TIA and driver | guided to exceed **$1B** annualized revenue within the next few quarters | [1×: Damnang] |
| DCI | line of sight to **$1B** annualized during FY28 | [1×: Damnang] |
| Scale-up optics | FY28 outlook **doubled** from the prior **$150M** | [1×: Damnang] |
| Scale-out switch | FY27 **above $600M**; FY28 about **$1B** (Q1 IR) | [1×: Damnang] |
| Teralynx T100 | **102.4Tbps**, **512-port** radix, typical power **below 1,000W**; BGA / co-packaged copper / CPO options | [1×: Damnang] |
| CMM-Ax | disclosed **Aug 5**; CXL-PNM = Structera A PNM + SK hynix memory + SK hynix software; validation at **FMS 2026**; no disclosed production customer | [1×: Damnang] |
| Structera A | **16** Arm Neoverse **V2** cores; up to **200GB/s** bandwidth | [1×: Damnang] |
| Three bilaterals | NVIDIA–Marvell (NVLink Fusion + SiPh); NVIDIA–SK hynix (next-gen AI memory); Marvell–SK hynix (CXL-PNM). **No** three-party integrated program. **No** evidence SK hynix or NVIDIA adopted Photonic Fabric | [1×: Damnang] |
| Google commercial agreement | signed **July 29**; 8-K filed **August 19**; spans inference accelerators, storage controllers, NICs, memory interface controllers, near-memory compute | [1×: Damnang] |
| Google warrant size / strike | up to **58.97M** shares at **$206.58**; roughly **6.7%** of share count before issuance | [1×: Damnang] |
| Time-vest | only **1.36M** shares vest with time over the first year | [1×: Damnang] |
| Performance-vest | **1/240** per **$500M** of purchases, FY27 Q3 through FY33 | [1×: Damnang] |
| Vesting ceiling | full vest ⇒ cumulative **$120B** over seven years; **not** backlog or minimum; purchasing at Google's discretion | [1×: Damnang] |
| NVIDIA investment | **$2B** (March); NVLink Fusion ecosystem; custom XPUs + Fusion-compatible scale-up networking + silicon photonics co-dev | [1×: Damnang] |
| Spot / cap | Aug 20 close **$251**; market cap about **$220B** | [1×: Damnang] |
| Base implied price | delivering FY28 **$16.5B** ⇒ **$239** | [est.] |
| Aug 27 variables | **FY27 Interconnect growth** and the **Q3 guide** | [1×: Damnang] |
| Oct 6 variable | **FY28 segment estimates** (Investor Day) | [1×: Damnang] |
| PLAIN_TEXT gap: §8 | Heading "8. What to watch in the August 27 print" has no body in Gmail PLAIN_TEXT. Variables are named in Executive Summary point 6: Aug 27 = FY27 Interconnect growth and the Q3 guide; Oct 6 Investor Day = FY28 segment estimates | [1×: Damnang; clipper note] |
| PLAIN_TEXT gap: EPS table | Author scenario EPS table referenced in §6 as "the EPS figures above" is **not** in Gmail PLAIN_TEXT. Only the base implied price of **$239** vs spot **$251** is in prose. Do not invent missing EPS rows. Google warrant is not in those (absent) EPS figures | [1×: Damnang] |
| Live Portfolio (vault, not this source) | MRVL **HELD** as row 9, Medium (3.5–10%), last table print $222.02; NVDA row 5 Medium (3.5–10%); 000660 row 1 Full (25%+). Upcoming MRVL earnings 2026-08-27, EPS est $0.93, rev est $2.7B | [Live Portfolio table; not JS] |

## Contradiction Check

Supports, sharpens, and in one place contradicts the live [[Theses/MRVL - Marvell Technology]] file. Named targets:

- **`## Outstanding Questions` #1 (Google signed contract vs talks) — toward resolution.** The Aug 19 8-K / July 29 commercial agreement is the formal-agreement disclosure the question asked for. Scope is broader than "MPU + additional inference TPU talks": inference accelerators, storage controllers, NICs, memory interface, near-memory compute. Does **not** by itself quantify share of Google's inference-silicon spend.
- **`## Conviction Triggers` → HIGH, conjunct 1 — evidence-touched / near-fired, not fired.** Trigger requires a disclosed commercial agreement for the MPU or inference TPU *and* AWS T3 ≥400K *and* Celestial PO / end-2026 tape-out, all within FY27. Leg 1 now has an 8-K commercial agreement that includes inference accelerators (and more). Legs 2 and 3 are not in this source. Prior 2026-08-21 vault read (Google 8-K is 1/3 HIGH, near-fired not fired; $120B is vesting ceiling not a PO; print 8/27) is **unchanged**. Flag-only; conviction stays medium.
- **`## Conviction Triggers` → HIGH, conjunct 3 (Celestial PO / end-2026 tape-out) — evidence-touched, not fired.** Source: CXL pooling and Photonic Fabric "still contribute little to the P&L"; no evidence SK hynix or NVIDIA adopted PF; CMM-Ax is Structera A, validation-stage, no production customer. This is the opposite of a PO/tape-out print.
- **`## Conviction Triggers` → LOW, conjunct 2 (Google signs BRCM-exclusive or BRCM+MediaTek-only, closing Marvell out) — inverted.** A five-category commercial agreement plus a ~6.7% warrant is not a close-out. Does not retire Insight #1's fourth-seat / Full-COT (Axion EDA) worry; it does retire the "still only talks" formulation of OQ #1.
- **`## Conviction Triggers` → CLOSE, conjunct 1 (FY28 custom path below $3.6B implied run-rate) — inverted on the author's split.** Q1 IR Custom above 2× in FY28; author FY28 Custom **$3.8B** [est.] is above the $3.6B CLOSE line. Not a company disclosure of a custom walk-back.
- **`## Key Non-consensus Insights` #1 (second-source is a procurement slot, ~60% GM ceiling, seats churn).** The warrant (~7% of equity, vest-through-FY33, 1/240 per $500M) is Damnang's argument that Google is *not* a single-generation design-services engagement. That supports duration of the *relationship*; it does not contradict the structural GM-ceiling or Full-COT in-sourcing vector. System-content framing (attach + near-memory + NICs) is consistent with thesis subsegments 1–2 (custom compute + attach) and with Bull Case driver 1, but the thesis still treats Google as a fourth seat behind Broadcom Sunfish and MediaTek Zebrafish.
- **`## Key Non-consensus Insights` #2 (Celestial is memory-disaggregation, not CPO) and Bull Case driver 3.** Source agrees PF is the high-optionality / low-P&L bucket (Memory 3.0 / 2.0 / 5.0) and explicitly separates CMM-Ax from PF. Does **not** add a PO, tape-out, or second named customer. The SK hynix–PF inference is labeled as having no disclosed basis.
- **`## Key Non-consensus Insights` #3 (NVIDIA $2B is UALink containment; Marvell is the contained party).** Source uses the same $2B / NVLink Fusion fact as a *system-content* data point (custom XPU + scale-up networking + SiPh overlap). That does not falsify containment; it is the author's bullish read of the same perimeter. Wikilink [[Theses/NVDA - Nvidia]] (no Conviction Triggers to test).
- **`## Business Model` row 6 (Teralynx / T100) and Industry Context CPO-vs-wallet-share.** T100 102.4T / 512-port / <1000W and FY27 >$600M / FY28 ~$1B switch guide match the thesis's "no longer two generations behind" update. The wallet-share-vs-TAM lens (higher radix cuts optical units; company content can still rise if Marvell sells switch + CPO) is additive, not contradictory. Competitive #2 slot vs [[Theses/AVGO - Broadcom]] Tomahawk remains the deployment-gap risk the thesis already carries.
- **`## Business Model` row 4 (DCI ~$1B FY28) and electro-optics TIA/driver.** Source's TIA/driver >$1B annualized "within the next few quarters" and DCI $1B FY28 and scale-up optics doubled from $150M are the IR-language quantification the thesis already sketched; Optical 5.0/5.0/4.0 is the author's claim that this engine is the de-risked FY27 print.
- **`## Catalysts` (Q2 FY27 earnings, Aug 27 2026).** Source **names the Aug 27 variables**: FY27 Interconnect growth and the Q3 guide. Adds **October 6 Investor Day** as the FY28 segment-estimate event (not previously on the thesis catalyst list). Print 8/27 unchanged as the live date.
- **`## Key Metrics` / Valuation / Risk #6 (guide is priced).** Thesis at $222.02 / 55× FY27E treated the $16.5B guide as the priced base. Damnang's $251 / ~$220B and base implied $239 [est.] **agrees in direction and is harsher**: even *delivering* $16.5B is not enough at spot; revisions are required. That is [G-13] expectations investing, not a conviction change.
- **[[Theses/000660 - SK Hynix]] CMM-Ax / FMS 2026.** Touches Business Model / memory-tier extension (CXL-PNM with Structera A) and the prior Damnang HBM-density-peak read. **No-touch** on 000660 HIGH (Rubin ≥60% + HBM4E sole-source + Kinex 16-Hi + Namics ≥2028), LOW (Samsung >35% Rubin AND HBM ASP −10% YoY), CLOSE (CXMT qualified HBM + Samsung HBM5 70%). CMM-Ax is not an HBM-allocation print.
- **[[Macro & Technology/CXL Memory Disaggregation Framework]].** Source treats CXL pooling as low-P&L optionality and KV-cache growth as the demand driver for capacity outside local HBM — consistent with the framework, and consistent with the thesis's July KV-cache-socket-capture caution (PF not evidenced at NVIDIA/SK hynix).

Honest low-signal remainder: this source **confirms** the Interconnect-first FY27 mix the May guide already printed, **formalises** Google (OQ #1), and **does not** move Celestial, Trainium 3/4, LPO blended GM, or UALink vs Fusion. A source that upgrades mix visibility and still leaves HIGH at 1/3 is useful into the print; it is not a conviction rewrite.

**Conviction-trigger scoreboard (flag-only, no `/status`, no conviction/status change).**

| Thesis | Trigger | Verdict | Why |
|---|---|---|---|
| [[Theses/MRVL - Marvell Technology#Conviction Triggers]] | → HIGH if (1) signed Google MPU / inference-TPU commercial agreement **and** (2) AWS T3 ≥400K **and** (3) Celestial PO or on-schedule end-2026 tape-out | **1/3 near-fired; HIGH not fired** | Leg 1 evidence-touched / near-fired (July 29 / Aug 19 8-K commercial agreement includes inference accelerators + near-memory compute). Leg 2 no-touch (no Trainium 3 allocation). Leg 3 evidence-touched the other way (PF little P&L, CMM-Ax ≠ PF, no production customer, no PO / tape-out) |
| same | → LOW if any two of: custom miss >10%; Google BRCM-exclusive close-out; OFC 2027 LPO >35% 1.6T short-reach share loss; Celestial tape-out slip past end-2026 | **no-fire; leg 2 inverted** | Google signed *with* Marvell. No custom-miss print, no OFC share, no public tape-out slip |
| same | → CLOSE if FY28 custom path below $3.6B implied; Celestial to FY30 / impairment; Trainium 4 exclusive Alchip; UALink ≥50% CY28 scale-up and XConn/ESUN fail | **no-fire; CLOSE 1 inverted on author split** | Q1 IR Custom >2× FY28; author FY28 Custom $3.8B [est.] is above the $3.6B line. No T4 / UALink / impairment print |
| [[Theses/NVDA - Nvidia]] | (none registered) | **no triggers to test** | Gap already flagged in the NVDA 2026-07-09 mental-models pass. $2B / NVLink Fusion / SiPh is a system-content restatement, not a CUDA or ASIC-share print. Conviction unchanged (high) |
| [[Theses/000660 - SK Hynix#Conviction Triggers]] | HIGH (Rubin ≥60% + HBM4E sole-source + Kinex 16-Hi + Namics ≥2028); LOW (Samsung >35% Rubin AND HBM ASP −10% YoY); CLOSE (CXMT qualified HBM + Samsung HBM5 70%) | **no-touch** | CMM-Ax is CXL-PNM (Structera A 16 V2 / 200GB/s, FMS 2026 validation). Not an HBM-allocation, Namics, CXMT, or Kinex print. Conviction unchanged (medium) |

**Live-book overlap** (markdown holdings table in [[Live Portfolio]], not the JS). In-article / load-bearing: [[Theses/MRVL - Marvell Technology]] (HELD, row 9, Medium 3.5–10%), [[Theses/NVDA - Nvidia]] (row 5, Medium 3.5–10%), [[Theses/000660 - SK Hynix]] (row 1, Full 25%+). Adjacent live names, colour only: [[Theses/AVGO - Broadcom]] (switch-CPO / custom-seat competitor; T100 vs Tomahawk deployment gap unchanged); [[Theses/TSM - Taiwan Semiconductor]] (implied foundry / packaging, no wpm or GM print). **No-touch** on PLTR, SPCX, NET, NBIS, SNDK, 285A, 6857, LRCX, AMAT. Do not change any conviction or status.

**Mental-model identifier** (ingest records; `/sync` writes thesis bodies): [[Generalist - Overview]] [G-13] expectations — $251 / ~$220B already above the $239 [est.] implied by delivering the $16.5B FY28 guide, so the priced variable is *revisions*, not guide delivery. [G-10] outside view — three consecutive >40% years off an $8.195B FY26 base remains a top-decile outlier the source does not re-underwrite. [[Industry - Semiconductors]] #8 architecture transition remaps the bottleneck — source's system-content unit (XPU + NIC + storage + memory interface + near-memory; NVLink Fusion XPU + scale-up + SiPh) and the three-bilateral / no-tripartite rule are the same data-movement migration as the 20 Aug density-peak note, now applied to Marvell's P&L mix. #13 classification — Interconnect is the owned-layer print for FY27; Custom remains the rented seat whose FY28 >2× is still cadence, not contract headline. [[Lens - Value Layer Monopoly]] — optics / TIA-driver / DCI is the owned layer (Optical 5.0 / 5.0 / 4.0); Custom is still a layer-renter buying duration with ~6.7% equity (warrant through FY33); Memory / PF remains residual optionality, not a layer win. Disconfirming check if models agree: an Aug 27 Interconnect-growth cut or a Q3 guide miss would break the FY27 Interconnect-first frame first; a company walk-back of FY28 Custom below the $3.6B CLOSE line would convert the author's $3.8B [est.] inversion into a CLOSE touch; a disclosed Photonic Fabric production customer (or NVIDIA / SK hynix PF adoption) would be the HIGH-3 fire this source explicitly says has not happened.

## Source Excerpts

> "Marvell FY26 revenue was $8.195B. The current company outlook is roughly $11.5B for FY27 and roughly $16.5B for FY28. Incremental revenue is about $3.3B in FY27 and a further $5.0B in FY28."

> "The FY27 Data Center growth guide is about 50% and the Interconnect guide is above 70%. The Q1 investor presentation put Custom growth above 20% in FY27 and above 2x in FY28."

> "Four of the five Part 2 checkpoints have passed. The FY27 Interconnect growth guide was raised to above 70%, and the Q2 revenue guide came in at $2.70B, above the $2.55B hurdle set in Part 2."

> "On the author's segment bridge, more than half of the FY27 Data Center increase comes from Interconnect."

> "TIA and driver were guided to exceed $1B of annualized revenue within the next few quarters. DCI modules were described as having line of sight to $1B of annualized revenue during FY28. The FY28 revenue outlook for scale-up optics was doubled from the prior $150M."

> "The Q1 investor presentation put FY27 scale-out switch revenue above $600M and FY28 at about $1B."

> "Teralynx T100 offers 102.4Tbps, a 512-port radix, typical power below 1,000W, and BGA, co-packaged copper, and co-packaged optics options."

> "The accurate lens is system-level wallet share within the same customer rather than TAM by product line."

> "No three-party integrated program has been confirmed. There is also no evidence that SK hynix or NVIDIA has adopted Marvell Photonic Fabric."

> "CMM-Ax integrates the Structera A PNM engine, SK hynix memory, and the SK hynix software stack. Structera A provides 16 Arm Neoverse V2 cores and up to 200GB/s of bandwidth."

> "The modeling unit for Custom Silicon is closer to system content than to sockets."

> "Alongside the agreement, Marvell issued Google a warrant. It is the right to buy up to 58.97M Marvell shares at $206.58 each, roughly 6.7% of the share count before issuance."

> "Only 1.36M shares vest with the passage of time over the first year. The rest opens up only as Google actually buys Marvell custom silicon. One two-hundred-fortieth vests for every $500M of purchases, running from FY27 Q3 through FY33. For the whole warrant to vest, Google would have to buy a cumulative $120B over seven years."

> "That $120B is neither a backlog nor a minimum purchase commitment. It is the ceiling on the incentive, and the actual purchasing is entirely at Google's discretion."

> "In March, NVIDIA invested $2B in Marvell and included Marvell in the NVLink Fusion ecosystem."

> "At the August 20 close the stock was $251 and market capitalization was about $220B. … The base-case implied price of $239 sits below the spot price of $251. The market is already pricing Marvell above current guidance."

> "The variables on August 27 are FY27 Interconnect growth and the Q3 guide. FY28 segment estimates are the variable at the October 6 Investor Day."

> "Company guidance puts Custom revenue growth above 20% in FY27 and above 2x in FY28."

> "The system architecture read-through connecting NVIDIA, SK hynix, and Marvell does not imply any disclosed three-party co-development agreement."

> "EPS and implied price are author estimates. They embed assumptions for revenue, operating leverage, tax, and diluted share count, and they represent scenario sensitivity rather than a price target. The Google warrant is not reflected in the EPS figures above, because most of it vests against qualifying revenue and it permits both cash exercise and net exercise."

> "This is an inference with no disclosed basis. The point of confirmation is when the first Photonic Fabric customer and memory partner are disclosed."

*(Gmail PLAIN_TEXT heading only, no body: "8. What to watch in the August 27 print". Do not invent the missing §8 bullets or the §6 EPS scenario rows.)*
