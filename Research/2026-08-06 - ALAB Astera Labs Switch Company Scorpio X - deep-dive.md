---
publish: false
date: 2026-08-06
tags: [research, Semiconductors, ALAB]
sector: Custom Silicon & Networking Semiconductors
ticker: ALAB
source: 'https://www.viksnewsletter.com/p/post-astera-labs-is-a-switch-company'
source_type: deep-dive
updated: 2026-08-14
---

# Astera Labs is a Switch Company in Connectivity Clothing

## Thesis Delta

Consensus still prices ALAB as a PCIe-retimer / connectivity analog — the vault's own [[Macro & Technology/CXL Memory Disaggregation Framework]] QLogic/Emulex HBA analog — → Vik's free half says score it as a [[Theses/AVGO - Broadcom]]-like scale-up switch company: Scorpio becomes the largest family in Q3 (one quarter ahead of the May guide), PCIe 6 already >50% of revenue, and dollar content/XPU steps from $50–$100 at IPO to multiple $1,000s, of which the 320-lane Scorpio X is $1,000 alone. No ALAB thesis exists; the question this raises is Semis #13/#14 reclassification (retimer stub → intra-rack switch compounder) versus a single-anchor Trainium-3 attach that fails to convert the other ten pre-prod quals ([G-3] mean-reversion vs trend, [G-13] which operating variable the price embeds, VLM intra-rack PCIe scale-up switch — WEAK FIT until quals print revenue).

## Summary

Vik's claim is a category flip, not a beat-and-raise recap. Astera built the franchise retiming intra-tray XPU–CPU–NIC links on Aries; the investable move is the step out of the tray into the rack via Scorpio, and the Q2 print is offered as the first quarter where that step shows up in the mix. Revenue printed $392.4M, +27% sequential and +104% year over year, against a May guide of $355–365M. PCIe 6 products — Scorpio switches plus Gen 6 Aries retimers — crossed 50% of revenue for the first time, up from roughly a third in Q1. Q3 guide is $540–560M, ~72% non-GAAP gross margin, $1.16–$1.21 non-GAAP EPS. Management now expects Scorpio to be the largest product family in Q3, one quarter earlier than the May call. The author's instruction is explicit: treat ALAB as a switch company along Broadcom lines going forward, as the 320-lane Scorpio X takes share not only at AWS Trainium but at neoclouds and add-in-card inference GPU vendors.

The content mechanism is the dollar-per-XPU step-function. Around IPO, Astera content sat at $50–$100 per XPU. On the Q2 call, COO Sanjay Gajendra said the business can contribute multiple $1,000s per XPU, with the 320-lane Scorpio X scale-up switch itself contributing $1,000 per XPU. SemiAnalysis's Trainium 3 deep-dive (reproduced, not independently audited here) puts Scorpio X attach at 0.25–0.28 per XPU depending on the switched-rack Trn3 SKU. At $1,000/XPU that maps to $32,000 of 320-lane Scorpio X in a 32-XPU Gen2 Trn3 rack delivered as eight switches, and $72,000 across twenty switches in the 72-XPU variant — an implied ASP of $3,600–$4,000 per Scorpio X. Vik prices that against [[Theses/AVGO - Broadcom]] Tomahawk 6: TH6 launched below $20,000 before volume discounts at 102.4 Tbps, ~$200/Tbps; Scorpio X is 20.48 Tbps (5× lower bandwidth) and at the same $/Tbps lands at ~$4,000. That is a pricing analog, not a product substitute — TH6 is scale-out Ethernet; Scorpio X is intra-rack PCIe scale-up. The Gen2 Trn3 PCB also carries lower-lane Scorpio-P SKUs (144×32-lane, 72×64-lane, or 36×128-lane) plus Aries retimers on top, which is how PCIe 6 can already be half of the P&L before CXL or optics contribute.

The buyer set is written wider than a single AWS socket. SambaNova- and d-Matrix-class add-in-card GPU vendors are named as Scorpio X demand, and that demand tightens if those vendors can buy [[Theses/NVDA - Nvidia]] NVLink Fusion interfaces to sit next to Nvidia silicon — a thread Vik flags as material for Trainium 4. Neoclouds are a third buyer class for scale-up switches. Gajendra disclosed ten customers in pre-production and qualification; conversion into revenue is left open. COSMOS is the software coupling that is supposed to keep the switch from becoming a merchant ASIC: early Aries growth used deep telemetry; the current stack adds Hypercast and in-network compute that offload multi-destination packet distribution and collective operations onto the fabric switch, raising GPU utilization inside the rack. CXL (Leo) is dated 2027 — one US-hyperscaler design win in Q2, controllers shipping to two US hyperscalers in 2027, volume not this year's print. Optics follow the same clock: NPO is a 2027 story, CPO later. The Inbox clip ends at the subscription break; Vik's remainder on where the company goes, what can fail, and what to watch is not in this source file.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Q2 revenue | $392.4M | [1×: ALAB / Vik] |
| Q2 vs May guide | $355–365M | [1×: Vik / ALAB May guide] |
| Q2 sequential / YoY | +27% / +104% | [1×: ALAB / Vik] |
| PCIe 6 share of revenue (Q2) | >50% first time | [1×: Vik] |
| PCIe 6 share of revenue (Q1) | ~1/3 | [1×: Vik] |
| PCIe 6 constituents | Scorpio switches + Gen 6 Aries retimers | [1×: Vik] |
| Q3 revenue guide | $540–560M | [1×: Vik / ALAB] |
| Implied Q3 sequential (midpoint) | ~+40% vs Q2 | [est.: $550M / $392.4M] |
| Q3 non-GAAP GM guide | ~72% | [1×: Vik / ALAB] |
| Q3 non-GAAP EPS guide | $1.16–$1.21 | [1×: Vik / ALAB] |
| Scorpio as largest family | Q3, one quarter ahead of May guide | [1×: Vik / ALAB] |
| IPO-era content / XPU | $50–$100 | [1×: Vik] |
| Target content / XPU | Multiple $1,000s | [1×: ALAB COO Gajendra / Vik] |
| Scorpio X content / XPU | $1,000 (320-lane scale-up) | [1×: Gajendra / Vik] |
| Scorpio X lanes / bandwidth | 320 lanes / 20.48 Tbps | [1×: Vik] |
| SemiAnalysis Trn3 Scorpio X attach | 0.25–0.28 / XPU (SKU-dependent) | [1×: SemiAnalysis via Vik] |
| 32-XPU Gen2 Trn3 Scorpio X content | $32,000 as 8 switches | [1×: Vik / SemiAnalysis] |
| 72-XPU Gen2 Trn3 Scorpio X content | $72,000 as 20 switches | [1×: Vik / SemiAnalysis] |
| Implied Scorpio X ASP | $3,600–$4,000 | [est.: Vik from $1,000/XPU ÷ attach] |
| TH6 launch price / bandwidth | <$20,000 / 102.4 Tbps (pre-discount) | [1×: Vik / Broadcom] |
| TH6 implied $/Tbps | ~$200/Tbps | [est.: Vik] |
| Scorpio X at TH6 $/Tbps | ~$4,000 | [est.: 20.48 × $200] |
| Scorpio-P on Gen2 Trn3 PCB | 144×32-lane, or 72×64-lane, or 36×128-lane | [1×: Vik] |
| Incremental content above Scorpio X | Scorpio-P + Aries retimers (not in $1,000) | [1×: Vik] |
| Named non-AWS Scorpio X interest | SambaNova, d-Matrix (AIC GPUs); neoclouds | [1×: Vik] |
| NVLink Fusion role | AIC GPUs + Nvidia attach; material for Trainium 4 | [1×: Vik] |
| Pre-prod / qualification customers | 10; conversion unstated | [1×: Gajendra / Vik] |
| COSMOS features beyond telemetry | Hypercast + in-network compute for collectives | [1×: Vik] |
| CXL product | Leo memory controllers | [1×: Vik] |
| CXL Q2 design win | 1 US hyperscaler | [1×: Gajendra / Vik] |
| CXL 2027 ship | Controllers to 2 US hyperscalers | [1×: Vik] |
| CXL / NPO volume clock | 2027; CPO later | [1×: Vik] |
| Clip completeness | Free half only; failure-mode / watch-item remainder absent | [1×: Inbox file] |

## Contradiction Check

No ALAB thesis file exists, so the source cannot confirm or break an ALAB conviction; it collides with three live theses plus the CXL framework. [[Theses/AVGO - Broadcom]] §Key Non-consensus Insights (Tomahawk as compute-agnostic Ethernet chokepoint, 80–90% merchant switching) is **not** share-theft: Scorpio X is intra-rack PCIe scale-up at 20.48 Tbps, not Tomahawk 6 scale-out Ethernet at 102.4 Tbps — the $200/Tbps compare is a pricing sanity check, not a TAM overlap. It does, however, test the unspoken "only Broadcom owns switching dollars in the AI rack" heuristic: if Gajendra's $1,000/XPU Scorpio X + Scorpio-P + Aries stack holds, a second switch P&L opens *below* Tomahawk. [[Theses/MRVL - Marvell Technology]] Insight #5 (Trainium 3 primary lost to Alchip; 500K packaged allocation unconfirmed) is **supported as an AWS-volume tell and challenged as a Marvell-content tell** — Vik's SemiAnalysis table is a Trn3 rack bill-of-materials with Astera scale-up silicon, not a Marvell custom-silicon recovery. Insight #3 / Outstanding Question 4 and Conviction Trigger → CLOSE #4 (NVLink Fusion vs UALink; Fusion as containment) is **sharpened**: Vik says Fusion interfaces become the reason AIC GPU vendors and Trainium 4 buy Scorpio, which is the same "pulled inside Nvidia's perimeter" mechanism the MRVL thesis already assigns to Marvell — ALAB is a second Fusion-adjacent merchant, not a UALink hedge. Insight #2 (Celestial as the rack-scale CXL.mem physical layer) is **untouched on photonics and dated later on CXL silicon**: Leo volume is 2027, matching the framework's 2027–2028 primitive, not pulling Celestial forward. [[Theses/NVDA - Nvidia]] §Summary (Trainium 30–40% better price-performance as ASIC share risk) plus the NVLink 6.0 lock-in in §Business Model are **split**: Trn3 Scorpio attach at 0.25–0.28/XPU is evidence the custom-ASIC rack still needs a merchant scale-up switch, which is *not* NVLink; Fusion-as-Trainium-4 enabler is the containment path that would recapture that layer. [[Macro & Technology/CXL Memory Disaggregation Framework]] Thesis Delta (ALAB = QLogic/Emulex retimer analog, validated-but-priced, Aug 4 Q2 as checkpoint) is the **direct hit** — this source moves the analog *up* one SAN layer, from HBA/retimer toward Brocade-style fabric switching, and the Q2 mix (PCIe 6 >50%, Scorpio largest family next quarter) is the checkpoint printing in the switch column, not the CXL column. Falsifiers the free half itself leaves open: the ten quals do not convert ([G-10] base-rate on design-win-to-revenue); Fusion-attached AIC/neocloud demand stays slideware; CXL slips past 2027; or the remainder (not in this clip) names a failure mode that reclassifies Scorpio as a one-customer Trainium SKU. Semis #2/#8/#10 are the live tests: qualification conversion, tray→rack architecture shift, and whether AWS remains a binary anchor.

## Source Excerpts

> "Astera Labs should be viewed as a switch company – along the lines of Broadcom – going forward, as their 320-lane Scorpio X switch gains larger adoption, notably even with neoclouds and inference GPU providers." [1×: Vik]

> "Around the time of IPO, the dollar content of Astera products per XPU was $50-$100. In the Q2 earnings call, COO Sanjay Gajendra said that he sees their business contributing multiple $1,000s per XPU with the 320-lane Scorpio-X scale-up switch itself contributing $1,000 per XPU." [1×: Vik / Gajendra]

> "At $1,000 of Scorpio X content per XPU, a 32-XPU Gen2 Trn3 rack carries $32,000 worth of 320-lane Scorpio X content, delivered as 8 scale-up switches. The 72-XPU variant Gen2 Trn3 rack carries $72,000 across 20 switches. All this points to an ASP of $3,600-$4,000 per Scorpio X switch." [1×: Vik / SemiAnalysis]

> "Broadcom priced Tomahawk 6 below $20,000 at launch, before volume discounts, for a total switch bandwidth of 102.4 Tbps. That works out to roughly $200/Tbps. Scorpio X has 5x lower switch bandwidth at 20.48 Tbps, and at $200/Tbps, that prices it right at $4,000." [1×: Vik]

> "Gajendra said that there are 10 customers getting into pre-production and qualification cycles. It remains to be seen how many will materialize into revenue in future quarters." [1×: Vik / Gajendra]
