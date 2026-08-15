---
publish: false
date: 2026-08-13
tags: [research, semiconductors, CXMT, 000660, MU]
sector: DRAM & HBM Memory
ticker: 000660
source: 'https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram'
source_type: deep-dive
propagated_to: [000660, MU, SNDK, 285A]
---

## Thesis Delta

Consensus prices CXMT as the structural short on DRAM — the fourth entrant whose cheap Chinese bits flood the market and crater triopoly pricing. This source inverts the near-term read: CXMT this cycle is a price-taker at 5-10% below incumbent ASP, capacity-bound by fab-construction lead times from irrational expansion, and riding the shortage rather than breaking it — so the DRAM-glut fear the market attaches to CXMT is misdated, and the repricing bears not on 2026-2027 pricing discipline (which CXMT *reinforces*) but on two deferred vectors: a walled parallel Chinese memory market that permanently removes China's DRAM+HBM demand bucket from [[Theses/000660 - SK Hynix]] and [[Theses/MU - Micron Technology]], and the commodity-glut mechanism that fires only when the cycle turns and CXMT's ~17%-of-global-capacity walled bits have nowhere to export. Held as hypotheses to test, not verdicts: **Semis #16** — CXMT is a parallel Chinese-domestic market with non-contestable share, to be modeled as a permanent wall removing a demand bucket, not future Western competition; **Semis L1** — the fourth entrant is gaining scale (17% capacity by 2028) yet discipline holds, so L1's break-trigger is the cycle turn, not CXMT's headcount of wafers; **Semis #1** — China's worsening HBM constraint is pricing power the incumbents cannot bank because export controls already wall them out; **Generalist G-4** — Hefei's decade of return-agnostic state capital funding a RMB36.65B accumulated deficit is textbook frenzy-phase over-build of parallel infrastructure.

## Summary

CXMT is the fourth-largest DRAM maker globally and, per SemiAnalysis's Memory Model reconciled against the STAR Market IPO prospectus, is set to become one of China's largest semiconductor listings in decades. The mechanism the source lays out is not a cost-disruption story — it is a *scale-plus-cycle* story funded by patient state capital. CXMT reached ~$8.6B FY25 revenue (+156% YoY) and its first-ever positive net income ($1B), then printed $7.3B in 1Q26 alone (~700% YoY, ~70% operating margin). The source is explicit that this earnings explosion is "driven more by the cycle itself than company's technology or market positioning": 1Q26 bit shipments rose only 11% while ASP rose ~57%, following +63% and +68% QoQ ASP gains in 3Q25 and 4Q25. CXMT is a cycle-levered price-taker, not a share-taker — its bit-share model moves from 9% (2025) to only 12% (2027).

The central non-consensus claim is that Chinese memory is *not* structurally cheaper in this cycle and will *not* flood pricing. CXMT's 1Q26 DRAM ASP sits only 5-10% below Samsung/SK Hynix/Micron, and the gap widens over 2026 not because of inherent price differences but because incumbents carry a richer server-DRAM/HBM mix (server + HBM projected >50% of the DRAM end-market by end-2027, at higher $/GB). On a cost-per-bit basis CXMT's DDR5 remains >30% more expensive than the three leaders — its ~38% FY25 gross margin (vs Samsung 39.4%, Micron 39.8%, SK Hynix 60.4%) is a pricing artifact of the shortage, not a competitiveness signal. The near-term supply-disruption fear from a Chinese entrant is, in the author's framing, "overplayed at least for the next two years": even loading CXMT's wafer adds into the model at high-90s% utilization, DRAM stays undersupplied high-single-digits in 2026 widening to low-to-mid teens in 2027. This is the same structural-deficit picture as [[Research/2026-05-31 - DRAM HBM Memory Supercycle - deep-dive]], now with the fourth supplier's adds explicitly netted in.

On capacity, CXMT is scaling faster than the "contained laggard" framing assumes: ~265 kwspm end-2025 → ~350 kwspm end-2026 (modestly below Micron's ~385 kwspm, i.e. near the third-largest DRAM maker by wafer capacity) → 420 kwspm possible by year-end 2026 → 500 kwspm by end-2028, taking ~17% of global DRAM capacity. But HBM is where the wall is thickest and the source is most bearish on CXMT: only ~5 kwspm of ~265 kwspm was HBM at end-2025 (≈99% of revenue is DDR/LPDDR), rising to ~30 kwspm (2026) and ~55 kwspm (2027). CXMT is still struggling to stabilize HBM3 8-hi — modeled front-end / back-end yields of ~35% / ~70% imply ~25% overall — with 12-hi materially worse. It may skip HBM3 for HBM3E 8-hi/12-hi; a Huawei-CXMT *custom, non-JEDEC* HBM path is floated as the way to close the bandwidth gap. Adoption is confined to Huawei, Cambricon, and select domestic AI startups, and even those buyers prefer smuggled/stockpiled foreign HBM3/HBM3E when they can get it. The strategic logic is that allocating scarce DRAM wafers to low-yield HBM is *economically irrational right now* — commodity DRAM carries higher margin AND >3x the bits per wafer — so CXMT rationally starves HBM; government pressure for AI self-sufficiency is modeled as the only force that overrides this, pushing HBM wafer capacity to 55 kwspm (2027) and 100 kwspm (2028), lifting CXMT's share of *global HBM wafer supply* from 1% (2025) to 12% (2028).

The claim scope is deliberately bounded to a bifurcated market (Semis #16). CXMT's presence "remains largely concentrated in China"; export controls wall it in two directions at once — China cannot buy foreign HBM (Dec-2024 FDPR) and CXMT cannot buy EUV (blocked since 2019) or advanced WFE (Oct-2022 sub-18nm-half-pitch controls capturing G4/G5). The result is a self-sufficiency flywheel: CXMT's ramp is the demand catalyst for domestic WFE (NAURA, AMEC, Piotech, ACM, Hwatsing) and a structurally HBM-constrained China that worsens over the next 18 months absent a domestic breakthrough or a controls change. The IPO itself funds *core DRAM* — RMB29.5B (~$4.1B) of proceeds, 69.5% to wafer lines / DRAM tech upgrades and 30.5% to forward DRAM research, with **no dedicated HBM project and no mention of HBM in the use-of-proceeds** — confirming the commodity-first, HBM-starved posture. Alibaba Cloud sits on the cap table (~4%) as anchor customer and endorser, and CXMT is negotiating 3+ year DRAM LTAs with domestic CSPs (Alibaba, ByteDance, Tencent), guaranteeing walled domestic volume the Korean incumbents never had in their home markets. For the vault's DRAM names in [[Sectors/DRAM & HBM Memory]], the source is bullish on near-term pricing durability and bearish on the *terminal* structure of the addressable market.

## Evidence

**Financials & cycle-mix (reported / modeled):**

| Metric | CXMT | Notes |
|---|---|---|
| FY23 revenue | ~$1.2B | GM −113% [web: semianalysis] |
| FY24 revenue | ~$3.3B | GM −4.7% [web: semianalysis] |
| FY25 revenue | ~$8.6B (+156% YoY) | First positive NI ($1B); GM 37.8% [web: semianalysis] |
| 1Q26 revenue | $7.3B (~+700% YoY) | ~70% operating margin; ≈FY25 full-year in one quarter [web: semianalysis] |
| 1H26 revenue (guided) | >$16B (~7x YoY) | Per IPO filing [web: semianalysis] |
| FY26 revenue (est.) | >$50B | ~6x YoY; >2x every year since 2023 [est. web: semianalysis] |
| 1Q26 bit shipments | +11% QoQ | Volume nearly flat [web: semianalysis] |
| 1Q26 ASP | +57% QoQ | After +63% (3Q25), +68% (4Q25) — earnings are ASP-driven [web: semianalysis] |

**Peer scale — CY25 DRAM revenue & 1Q26 margin:**

| Player | CY25 DRAM revenue | FY25 GM | 1Q26 Op margin |
|---|---|---|---|
| Samsung | ~$72.3B | 39.4% | 81% |
| SK Hynix | ~$52.1B | 60.4% (HBM mix) | 73% |
| Micron | ~$37.2B | 39.8% | 84% |
| CXMT | ~$8.6B | 37.8% | 70% |

[web: semianalysis]. CXMT DDR5 cost-per-bit runs >30% above the three leaders; 1Q26 CXMT DRAM ASP only 5-10% below incumbents [web: semianalysis]. Total DRAM market sized at ~$1T in 2027 [est.].

**Capacity (kwspm) & wafer adds:**

| Player | ~End-2025 | ~End-2026 | Wafer adds 2026 / 2027 / 2028 |
|---|---|---|---|
| Samsung | — | ~720 | 15k / 50k / 110k |
| SK Hynix | — | ~595 | 60k / 60k / 90k |
| Micron | — | ~385 | 30k / 90k / 115k |
| CXMT | ~265 | ~350 (→420 possible) | 85k / 70k / 80k |

[web: semianalysis est.]. CXMT to reach ~500 kwspm end-2028 = ~17% of global DRAM capacity (up from ~13% in 2025 by capacity; bit-share 9%→12% by 2027; source also cites an 11%→17% supply-share framing for 2025→2028). Shanghai site alone could exceed 400 kwspm at full ramp. Despite these adds, DRAM modeled undersupplied high-single-digit % (2026) → low-to-mid teens (2027) at high-90s% utilization [est.].

**HBM allocation & yield (the wall):**

| Item | 2025 | 2026 | 2027 | 2028 |
|---|---|---|---|---|
| CXMT HBM wafer capacity (kwspm) | ~5 | ~30 | ~55 | ~100 |
| CXMT share of global HBM wafer supply | 1% | — | — | 12% |

[web: semianalysis est.]. HBM3 8-hi modeled yields: front-end ~35%, back-end ~70%, overall ~25%; 12-hi materially worse [est.]. ≈99% of CY25 revenue = DDR/LPDDR [web: semianalysis]. Front-end G4 (1z-equivalent) DRAM is the bulk of 2026 output but still below the 85-90% mature-yield standard for 1z; G5 (1a-equivalent) targeted without EUV (Micron-style) but with rising cost/yield penalty. Possible roadmap: skip HBM3 → HBM3E 8-hi/12-hi for the '27 accelerator window. Huawei+CXMT custom non-JEDEC HBM floated to close bandwidth gap. Rubin Ultra uses 12-hi HBM4E (not 16-hi) partly because 16-hi's higher wafer intensity cuts effective DRAM bit supply — a supply-constraint tell that applies to all suppliers, not just CXMT.

**IPO structure & ownership:**

| Item | Value | Notes |
|---|---|---|
| Venue | STAR Market (Shanghai) | CSRC registration filed 27 May 2026; filing accepted Dec 2025 [web: semianalysis] |
| Proceeds deployed | RMB29.5B (~$4.1B) | 69.5% wafer lines / DRAM tech; 30.5% forward DRAM R&D [web: semianalysis] |
| HBM in use-of-proceeds | **None** | No dedicated HBM project; prospectus does not mention HBM [web: semianalysis] |
| Dilution / implied px | 10-15% of post-IPO shares | RMB4.41 (10%) or RMB2.78 (15%) vs RMB2.63 (Jun-2025 round) [web: semianalysis] |
| Implied valuation (low end) | ~RMB197B (~$27B) | ≈1.8x annualized 1H26 parent earnings — author calls it "too cheap" [est.] |
| FY25 consolidated NI | RMB7.14B | Only RMB1.87B attributable to parent (74% minority interest) [web: semianalysis] |
| Consolidation gap | ~4x overstatement | Holds 30.68% / 31.72% economics of Changxin Xinqiao / Jidian Beijing but 73.01% / 75.32% votes [web: semianalysis] |
| State vehicles post-listing | >30% | National IC Fund Phase II + Hefei + Anhui; largest holder Qinghui Jidian 21.67% [web: semianalysis] |
| Anchor customer on cap table | Alibaba Cloud ~4% | Endorser + anchor; GigaDevice (Zhu's fabless house) 1.8% [web: semianalysis] |
| Accumulated deficit (pre-2025) | ~RMB36.65B | ~decade of losses before first 2025 profit; Hefei funded ~80% of "506" phase 1 (RMB14.4B of 18B) [web: semianalysis] |

**Bifurcation / export-control stack (Semis #16):**

- EUV blocked to China since 2019 → CXMT patterns via DUV immersion + SADP/SAQP (more masks, longer cycle time, higher cost/bit; structural scaling ceiling absent domestic advanced litho or 3D DRAM) [web: semianalysis].
- Oct-2022 BIS: WFE for DRAM ≤18nm half-pitch controlled — captures G4 (~1z) and G5 (~1a) [web: semianalysis].
- Dec-2024: HBM export restriction to China + FDPR + 24 equipment types + 140 entities (NAURA, ACM, Piotech) [web: semianalysis].
- CXMT presence "remains largely concentrated in China"; DDR5/LPDDR5 appearing in domestic and foreign consumer brands (smartphones, wearables, PC OEMs in qualification) — the wall leaks *outward* on commodity, stays solid *inward* on HBM [web: semianalysis].
- CXMT DDR5 mix risen to >30% (from low-20s%); negotiating 3+ year DRAM LTAs with Alibaba/ByteDance/Tencent [web: semianalysis].
- Foundation: ~7,000 Qimonda patents (via Polaris/WiLAN, ~€30M, 2015; licensed to CXMT 2019), ~2.8TB technical docs, 46nm→10nm-class BWL cell; Kuesters (ex-Qimonda) + Ping Er-xuan (ex-Micron/SanDisk/AMAT) as tacit-knowledge carriers [web: semianalysis].

## Contradiction Check

**Bears on [[Theses/000660 - SK Hynix]] and [[Theses/MU - Micron Technology]] — both in [[Sectors/DRAM & HBM Memory]]. Net effect: supports near-term pricing conviction on both, updates the CXMT capacity numbers upward, and confirms (does not challenge) the HBM-insulation-on-Western-demand pillar.**

**SK Hynix — Key Non-consensus Insight #4 ("CXMT is the right bear case, but the wrong timing bear case"):** The thesis cites CXMT at "70K → 200K → 300K WSPM" reaching ~15% global DRAM share, "three nodes behind (1gamma vs 1c)," "no HBM product at all," HBM insulated through 2028. This source **materially updates the capacity figure upward and largely confirms the timing/HBM logic**:
- *Capacity understated in the thesis.* The source has CXMT already at ~265 kwspm (end-2025) → ~350 kwspm (end-2026), near Micron's ~385 kwspm and the third-largest DRAM maker by wafer capacity — well past the "300K WSPM" the thesis modeled as the end-state, and reaching ~500 kwspm / ~17% of global capacity by 2028. Insight #4's "commodity-DRAM commoditization by 2028-2029" mechanism is directionally right but the scale is arriving faster; the CXMT capacity numbers in the thesis are stale-low and should be refreshed.
- *HBM logic confirmed.* ~25% HBM3 8-hi overall yield, ~5 kwspm HBM at end-2025, HBM-starved-by-design (commodity is higher-margin + 3x bits/wafer) — this **supports** the thesis's "HBM insulated through 2028 by the node gap." Insight #4's claim that "the bear that matters is Samsung capturing Rubin in 2026, not CXMT in 2029" survives intact.

**SK Hynix — Outstanding Question Q3 ("Does CXMT produce a credible HBM2e or HBM3 by 2028, and at what yield?"):** The source is the partial answer the question asks for: CXMT is *attempting* HBM3 8-hi (may skip to HBM3E), ~25% overall yield, 55 kwspm HBM capacity by 2027 / 100 kwspm by 2028, 12% of *global HBM wafer supply* by 2028 — but all China-directed (Huawei/Cambricon) via a **custom non-JEDEC** path, not a JEDEC Western-hyperscaler product. Q3's "EUV would be the giveaway" tell is confirmed absent (no EUV, no HBM in IPO proceeds). This **resolves Q3 toward "credible domestic HBM volume by 2028, but walled to China"** — consistent with the thesis's own Mental Models note (2026-07-10) that the "CXMT insulation claim is dead: HBM3 samples at Huawei."

**SK Hynix — Conviction Trigger CLOSE ("CXMT produces a qualified HBM2e or HBM3 product *at a hyperscaler* by end-2028 AND Samsung HBM5 hybrid-bonding yield crosses 70% at 16-Hi by mid-2027"):** Tension worth flagging. Read *literally*, the source's HBM trajectory (100 kwspm, 12% of global HBM wafer supply, Alibaba/Huawei adoption) could satisfy the "at a hyperscaler by end-2028" leg — but on a *Chinese* hyperscaler that SK Hynix is already export-controlled out of serving. The economic intent of the CLOSE trigger (CXMT taking SK Hynix's addressable HBM demand) is **not** met, because that China HBM bucket is already walled away from SK Hynix (Semis #16). The trigger's wording under-specifies "Western hyperscaler"; the source argues the damage is muted regardless. Does not challenge conviction; sharpens the trigger's definition.

**MU — Key Non-consensus Insight #3 / Industry Context / Bear Case #4 (CXMT ~7% global DRAM revenue, commodity negotiation-chip dilution, "not a 2026 HBM event"):** **Strongly supported and slightly refined.** MU's "~7% global DRAM revenue" is close to the source's implied ~5% revenue share ($8.6B of ~$170B), while the source's *bit* share is higher (9%→12%) because CXMT sells cheaper commodity bits — a useful denominator distinction (revenue vs bit vs capacity) for the MU note. The source confirms the mechanism (DDR5 mix >30%, foreign consumer-brand qualifications, domestic CSP LTAs = fourth name in the OEM pool, per [[Research/2026-08-11 - MU CXMT Apple DRAM Repricing Fourth Supplier - deep-dive]]) but **tempers the timing**: CXMT this cycle is *not* undercutting (5-10% below, parity-ish, capacity-bound), so MU Bear Case #4's "loses the negotiation chip that made the residual expensive" is a *forward/structural* risk, not a 2026 crater. This **supports MU's low conviction on the structural axis while removing the near-term flood fear** its Bear Case leans on.

**MU — Conviction Trigger CLOSE ("CXMT ships qualified HBM to a Western hyperscaler"):** **Not firing per this source.** CXMT HBM is China-only (Huawei/Cambricon, custom non-JEDEC). This MU CLOSE leg stays dormant; the source removes one of the three OR-gated CLOSE conditions from near-term play.

**MU — Insight #3 "L1 is a hypothesis; the falsifier is 2018 destock" / Bear Case #1 (destock):** The source is a live test of **Semis L1**. L1 says triopoly discipline "breaks when a fourth entrant (CXMT) gains scale." The source shows scale arriving (17% capacity by 2028) *while discipline holds* — CXMT prices at parity, is capacity-bound from irrational expansion, and the shortage absorbs its adds. So L1's break-trigger is **not** CXMT's wafer count; it is the cycle turn, when CXMT's walled commodity capacity has nowhere to export and becomes the marginal price-setter — the same reverse-scaling reversal (3x→4x bits/wafer) that [[Research/2026-05-31 - DRAM HBM Memory Supercycle - deep-dive]] flags as the glut amplifier and that [[Macro & Technology/DRAM Memory Cycle - Duration, Peak Timing and Second-Order Effects]] dates. This **supports** MU's "2018-destock-is-the-falsifier" framing and adds a specific second-order actor (CXMT's parallel walled supply) to the glut mechanism.

**NAND read-through (out-of-scope but noted):** CXMT is DRAM-pure — no NAND, no HBF seat. China's NAND champion is YMTC, which sits in the competitive frame of [[Sectors/NAND Memory & Storage]] alongside [[Theses/SNDK - SanDisk]] and [[Theses/285A - Kioxia]]. The same Semis #16 bifurcation logic (walled parallel Chinese supply, non-contestable domestic share) applies to YMTC vs the NAND incumbents, but this source does not advance NAND-specific evidence beyond naming YMTC as part of the domestic WFE-demand flywheel.

**G-4 (Perez) hypothesis to test:** Hefei's state-venture capital — RMB36.65B accumulated deficit absorbed over ~a decade, ~80% of "506" phase-1 funding, never sold down — is return-agnostic financial capital funding parallel infrastructure in the AI frenzy. The IPO-in-the-supercycle is the frenzy-phase liquidity event. If G-4 holds, the parallel capacity laid down now becomes the cheap substrate for China's domestic-AI deployment golden age, and the "toll" is a commodity-DRAM overhang whenever the cycle turns — structurally deflationary for the *residual global* commodity market the incumbents still serve. Recorded as a lens, not a verdict.

## Source Excerpts

- "Company's bit shipments increased by only 11% in 1Q26, while ASPs rose by roughly 57%… what really drove up company's earnings is really the explosive ASP growth rather than significant market share gains."
- "CXMT's DRAM ASP challenges the common misconception that Chinese memory is structurally cheaper and will flood the market… we believe it is somewhat inaccurate in this cycle."
- "By the end of 2025, we believe only ~5 kwspm of CXMT's ~265 kwspm of capacity is allocated to HBM… roughly 99% of revenue consists of DDR and LPDDR products in 2025."
- "We model CXMT's HBM3 8-hi's front-end and back-end yields at roughly 35% and 70%, respectively, implying an overall yield of only around 25%."
- "The prospectus discloses no dedicated HBM project and does not mention HBM… no disclosed funding commitment to a near-term HBM expansion."
- "We estimate CXMT's HBM wafer capacity will reach 55kwspm and 100kwspm in 2027 and 2028… increase the company's share of global HBM wafer supply from 1% in 2025 to 12% in 2028."
- "Huawei and CXMT will have custom HBM that is not based on the slow JEDEC standards and phys, so it will be able to close the bandwidth disadvantage."
- "We believe China's HBM constraint will only worsen over the next 18 months unless there is a major technology improvement in domestic HBM or a change in export control rules."
- "CXMT is currently negotiating 3+ year DRAM LTAs with domestic CSPs, as these customers seek to secure as much server DRAM supply as possible beyond volumes available from foreign suppliers."
- "Only RMB1.87B was attributable to parent shareholders, with 74% attributable to minority interests… the consolidated figure overstates what public shareholders will actually receive by roughly four times."
