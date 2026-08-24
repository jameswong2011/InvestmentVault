---
title: 'Marvell Part 3: What Has Been Proven, and What Is Still Open'
url: 'https://damnang2.substack.com/p/marvell-part-3-what-has-been-proven'
sender: damnang2@substack.com
date: 2026-08-21
publication: Damnang
gmail_id: 1a024340bc1fa85f
---

# Marvell Part 3: What Has Been Proven, and What Is Still Open

*Damnang subscriber email, 2026-08-21T12:01:08Z (20:01 SGT). Gmail thread/message `1a024340bc1fa85f`. Canonical URL: https://damnang2.substack.com/p/marvell-part-3-what-has-been-proven. PLAIN_TEXT is the full article. Public Substack HTML is paywalled after §3; checkpoint scorecard, revenue-build chart, and proven/upside heatmap recovered from public figure images (`t1_en.png`, `f1.png`, `f7.png`). Gmail PLAIN_TEXT has no body under heading "8. What to watch in the August 27 print" (variables are named in Executive Summary point 6). Author scenario EPS table referenced in §6 as "the EPS figures above" was not present as text in Gmail PLAIN_TEXT; only the base implied price of $239 vs spot $251 is in prose. Do not invent the missing EPS rows.*

Updating the Part 2 checkpoints and the remaining FY28 upside ahead of the August 27 print.

## Executive Summary

1. Four of the five Part 2 checkpoints have passed. The FY27 Interconnect growth guide was raised to above 70%, and the Q2 revenue guide came in at $2.70B, above the $2.55B hurdle set in Part 2.
2. Interconnect is the core of FY27 incremental revenue. Company outlook is roughly $11.5B of FY27 revenue, Data Center growth of about 50%, and Interconnect growth above 70%. On the author's segment bridge, more than half of the FY27 Data Center increase comes from Interconnect.
3. Optical is the most de-risked business, and Memory is the least modeled. 1.6T, DCI, TIA and driver, and scale-up optics all have improving revenue visibility. CXL pooling and Photonic Fabric still contribute little to the P&L and are only partly reflected in valuation.
4. Bilateral programs are confirmed across all three pairs: NVIDIA and Marvell, NVIDIA and SK hynix, and Marvell and SK hynix. NVIDIA and Marvell cover custom XPU, scale-up networking, and silicon photonics. NVIDIA and SK hynix cover next-generation AI memory. Marvell and SK hynix co-developed the CMM-Ax CXL-PNM product. No three-party integrated program has been confirmed. The evidence that memory and data movement are becoming important within the same system roadmap has nonetheless strengthened.
5. The modeling unit for Custom Silicon is closer to system content than to sockets. The Google agreement spans inference accelerators, storage controllers, NICs, memory interface controllers, and near-memory compute. Within NVIDIA NVLink Fusion, Marvell likewise supplies custom XPU and scale-up networking together.
6. Valuation at $251 requires further estimate revisions. Simply delivering the company's FY28 revenue guide of $16.5B implies a base case price of $239. The variables on August 27 are FY27 Interconnect growth and the Q3 guide. FY28 segment estimates are the variable at the October 6 Investor Day.

I have been analyzing Marvell closely since the beginning of this year and have shared a positive view across several articles.

To start with the conclusion, I remain very positive on Marvell.

This piece looks in detail at how far the five checkpoints from Part 2 have been validated, which parts can still remain as upside for the stock, and where the valuation stands. For readers who want a fuller picture of the company itself, the earlier articles below are the place to start.

## Disclaimer

This note is a personal research piece written for information and industry analysis. It is not a recommendation to buy or sell any security. The author may hold positions in the securities discussed and may transact in them in the future. Revenue estimates, valuation, scenarios, and architecture interpretations that are not attributed to company guidance or public disclosure are the author's judgment and may differ from actual outcomes. The system architecture read-through connecting NVIDIA, SK hynix, and Marvell does not imply any disclosed three-party co-development agreement.

## 1. Part 2 checkpoints: four of five passed

Part 2 laid out five checkpoints for the May 27 print. Four have passed and one is partly confirmed. The largest change is that the Interconnect earnings contribution arrived faster than expected.

**Part 2 checkpoint scorecard** (figure `t1_en.png`; Gmail PLAIN_TEXT dropped the table):

| Part 2 checkpoint | Hurdle at the time | What was confirmed | Verdict |
|---|---|---|---|
| Interconnect growth | Positive if raised from 50% into the 60s | FY27 growth guide raised to above 70% | Cleared by a wide margin |
| Q2 revenue guide | $2.55B or higher | $2.70B midpoint | Passed |
| Data Center dollars and mix | Whether Interconnect outpaces Custom | Q1 DC revenue $1.833B, up 27% year over year. Interconnect leads the FY27 DC growth of about 50% | Passed |
| Bookings tone | Record pace maintained | Management described bookings as "exceptional AI-related bookings" | Passed |
| Custom HBM and advanced packaging | Whether the terms first appear in IR language | The exact keywords have not appeared. Instead, the Google memory-interface and near-memory scope and the NVIDIA silicon photonics collaboration were added | Partly confirmed |

### Part 2 update

The upside case at the time centered on next-generation Custom Silicon ASP. In practice the FY27 earnings revision came from Interconnect first. The larger Custom growth contribution remains ahead in FY28.

## 2. FY27 = Interconnect, FY28 = Custom

Marvell FY26 revenue was $8.195B.

The current company outlook is roughly $11.5B for FY27 and roughly $16.5B for FY28. Incremental revenue is about $3.3B in FY27 and a further $5.0B in FY28.

The FY27 Data Center growth guide is about 50% and the Interconnect guide is above 70%. The Q1 investor presentation put Custom growth above 20% in FY27 and above 2x in FY28. FY27 earnings leverage sits with Interconnect, while the FY28 growth mix shifts toward Custom.

**Revenue build and where the growth comes from** (figure `f1.png`; "Totals are company outlook. Segment splits are author estimates."):

| | FY26 actual | FY27 outlook | FY28 outlook |
|---|---|---|---|
| Interconnect | $2.4B | $4.1B (+$1.7B) | $6.0B (+$1.9B) |
| Custom silicon | $1.5B | $1.8B (+$0.3B) | $3.8B (+$2.0B) |
| Everything else | $4.3B | $5.6B | $6.7B |
| **Total** | **$8.2B** | **$11.5B** | **$16.5B** |

**How proven each business is, and how much upside is left** (figure `f7.png`; author 0–5 scores; bars scaled within each column):

| Business | Keywords | Proven today | FY27–28 earnings | Upside left |
|---|---|---|---|---|
| Optical / Interconnect | 1.6T, TIA/driver, DCI | 5.0 | 5.0 | 4.0 |
| Custom Silicon | XPU, XPU-attach, Google TPU | 4.0 | 3.5 | 5.0 |
| Switching | 51.2T, 102.4T T100 | 3.5 | 3.5 | 4.0 |
| Memory Infrastructure | CXL, Structera, Photonic Fabric | 3.0 | 2.0 | 5.0 |

## 3. Optical, Interconnect and Switching: the most de-risked FY27 driver

Optical and Interconnect currently offer the highest revenue visibility. The Q1 investor presentation described 800G demand as holding up strongly and 1.6T as ramping quickly. The 1.6T transition raises DSP and analog front-end complexity and narrows the set of qualified suppliers.

TIA and driver were guided to exceed $1B of annualized revenue within the next few quarters. DCI modules were described as having line of sight to $1B of annualized revenue during FY28. The FY28 revenue outlook for scale-up optics was doubled from the prior $150M.

Revenue exposure is broadening from PAM4 DSP into analog front end, DCI, and scale-up optics. The structure is one of capturing content across multiple link lengths and topologies within the same hyperscaler rather than riding a single transceiver cycle.

### Switching and T100

Switching moves along the same axis as Optical and Interconnect.

The Q1 investor presentation put FY27 scale-out switch revenue above $600M and FY28 at about $1B. At that size it is no longer an immaterial option.

Teralynx T100 offers 102.4Tbps, a 512-port radix, typical power below 1,000W, and BGA, co-packaged copper, and co-packaged optics options. Radix is the number of ports a single switch can connect directly. The commercial risk is validation and production ramp.

Higher radix and a flatter fabric reduce network tiers and optical link counts, which is a partial headwind to optical unit demand. Marvell, on the other hand, can supply switch silicon and CPO together, so company-level content can expand.

The accurate lens is system-level wallet share within the same customer rather than TAM by product line.

## 4. Memory Infrastructure: low current revenue, high optionality

Memory Infrastructure carries more architecture optionality than current revenue.

CXL separates compute from memory so that capacity can be pooled and expanded. KV cache, the stored context a language model reuses during inference, grows quickly as context length and the number of agentic workload steps increase.

Marvell's memory portfolio is focused on expanding that capacity outside local HBM.

Two developments covered in earlier articles point the same way. NVIDIA's HBM4 despec request and the CPO papers published by SK hynix both point toward extending capacity beyond local HBM, which is the concept behind Marvell's memory portfolio.

### NVIDIA $2B investment: system-level read-through

Marvell and SK hynix are already at the stage of direct collaboration.

On August 5, the two companies disclosed the co-development of CMM-Ax, a CXL-PNM solution that combines the CXL near-memory acceleration of Marvell Structera A with SK hynix memory.

CMM-Ax integrates the Structera A PNM engine, SK hynix memory, and the SK hynix software stack. Structera A provides 16 Arm Neoverse V2 cores and up to 200GB/s of bandwidth. The two companies presented the validation results together at FMS 2026.

There are three confirmed bilateral links.

- NVIDIA and Marvell on NVLink Fusion and silicon photonics.
- NVIDIA and SK hynix on next-generation AI memory.
- Marvell and SK hynix on CXL-PNM.

No three-party integrated program has been confirmed. There is also no evidence that SK hynix or NVIDIA has adopted Marvell Photonic Fabric.

CMM-Ax is a Structera A collaboration and is separate from Photonic Fabric, and it is currently at the validation stage with no disclosed production customer.

However, the possibility that Photonic Fabric connects back to SK hynix is worth flagging.

The pod-level shared memory tier that Photonic Fabric creates still has to be filled with DRAM. What Marvell supplies is the fabric and the controller, not the memory itself. Marvell already lists SK hynix, Samsung, and Micron as memory qualification partners on the Structera line, and it co-developed CMM-Ax with SK hynix. A relationship that already works at the memory interface layer has room to extend into the memory tier as it commercializes.

This is an inference with no disclosed basis. The point of confirmation is when the first Photonic Fabric customer and memory partner are disclosed.

## 5. Custom Silicon: Google expands content beyond the accelerator socket

The Google 8-K filed on August 19 broadened Custom Silicon content. The commercial agreement was signed on July 29 and spans AI inference accelerators, storage controllers, network interface controllers, memory interface controllers, and near-memory compute. It is not a single accelerator socket agreement.

Alongside the agreement, Marvell issued Google a warrant. It is the right to buy up to 58.97M Marvell shares at $206.58 each, roughly 6.7% of the share count before issuance.

The right is not granted all at once.

Only 1.36M shares vest with the passage of time over the first year. The rest opens up only as Google actually buys Marvell custom silicon. One two-hundred-fortieth vests for every $500M of purchases, running from FY27 Q3 through FY33. For the whole warrant to vest, Google would have to buy a cumulative $120B over seven years.

That $120B is neither a backlog nor a minimum purchase commitment.

It is the ceiling on the incentive, and the actual purchasing is entirely at Google's discretion.

There are two implications.

First, Marvell put close to 7% of its equity on the table to lock in this customer relationship. A single-generation design services engagement would not justify that price.

Second, from Google's side, the more volume it directs to Marvell, the more its own stake is worth. The purchase incentive sits in the equity structure rather than in the contract terms.

For Marvell shareholders the structure delivers a cost and a signal at the same time.

The cost is dilution.

Dilution only occurs to the extent Google actually buys, so the scenarios where dilution grows are the same scenarios where revenue grows.

The signal is duration. A structure that runs through FY33 indicates that neither side treats this as a single-generation program.

### NVIDIA provides a second system-content data point

In March, NVIDIA invested $2B in Marvell and included Marvell in the NVLink Fusion ecosystem. Marvell supplies custom XPUs and NVLink Fusion compatible scale-up networking, and co-develops silicon photonics with NVIDIA. Custom Silicon, Networking, and Optics overlap within the same system architecture.

Company guidance puts Custom revenue growth above 20% in FY27 and above 2x in FY28. The Google commercial agreement and the NVIDIA ecosystem improve FY28 visibility. The earnings variable is production timing and revenue cadence rather than the contract headline.

## 6. Valuation: base case below spot; upside requires revisions

At the August 20 close the stock was $251 and market capitalization was about $220B. The company's FY28 revenue guide of $16.5B already assumes a high growth rate. Delivering that number alone is not enough to justify the current price.

EPS and implied price are author estimates. They embed assumptions for revenue, operating leverage, tax, and diluted share count, and they represent scenario sensitivity rather than a price target. The Google warrant is not reflected in the EPS figures above, because most of it vests against qualifying revenue and it permits both cash exercise and net exercise.

The base-case implied price of $239 sits below the spot price of $251. The market is already pricing Marvell above current guidance.

My own view is that there is ample room for this to move toward the bull case.

The near-term catalysts are the August 27 earnings report and the October 6 Investor Day.

## 8. What to watch in the August 27 print

*(Gmail PLAIN_TEXT heading only — no body under this heading. Executive Summary point 6 names the variables: August 27 = FY27 Interconnect growth and the Q3 guide; October 6 Investor Day = FY28 segment estimates.)*

## Sources & Notes

- Marvell Q1 FY27 Financial Results, May 27, 2026
- Marvell Q1 FY27 Financial & Business Results Presentation, May 27, 2026
- Marvell AI Memory Infrastructure Portfolio, Aug. 4, 2026
- Marvell and SK hynix, Accelerating AI Infrastructure with Marvell Structera A and SK hynix CXL Memory: Enabling Efficient Near-Memory Processing, Aug. 5, 2026
- Marvell Structera CXL Memory Pooling, Mar. 17, 2026
- Marvell Teralynx T100, June 1, 2026
- Marvell Form 8-K, Google Commercial Agreement and Warrant, Aug. 19, 2026
- NVIDIA and Marvell NVLink Fusion Partnership, Mar. 31, 2026
- SK hynix, Next-Generation Memory Architecture at FMS 2026, Aug. 7, 2026
- SK hynix HBF and Tiered Memory at FMS 2026, Aug. 4, 2026
- NVIDIA and SK hynix Multi-year Memory Partnership, June 7, 2026
- NVIDIA and SK Group Expanded AI Factory and Memory Partnership, July 24, 2026
- SK hynix, Five things you need to know about SK hynix and the future of AI memory, June 23, 2026
- NVIDIA and Lumentum Strategic Optics Partnership and $2B Investment, Mar. 2, 2026
- NVIDIA and Coherent Strategic Optics Partnership and $2B Investment, Mar. 2, 2026
- Market data: MRVL $251, market capitalization approximately $220B as of Aug. 20, 2026 market close. Business estimates not explicitly attributed to company guidance are author estimates.
