---
publish: false
date: 2026-08-04
tags: [research, Semiconductors, MPWR, Power]
sector: MLCC & Power Semiconductors
ticker: MPWR
propagated_to: [6981, VICR]
source: 'https://damnang2.substack.com/p/the-power-delivery-bottleneck-in'
source_type: deep-dive
updated: 2026-08-14
---

# The Power Delivery Bottleneck in AI Data Centers

## Thesis Delta

Consensus prices "AI power" as campus megawatts — turbines, interconnect queues, rack UPS — and prices [[Theses/VICR - Vicor Corporation]] as if a clean vertical-power-delivery (VPD) win is already in the multiple (~17× sales on the August 3 market cap versus company FY revenue guidance) [1×: Damnang]. This source splits the word: grid and permitting are a utility problem; the binding chip-level constraint is kiloamp I²R loss plus load-step sag at >1 kW / <1 V, so the equity map is MPWR (volume lateral / hybrid content while today's board layout holds 2–3 years), Vicor (VPD density + patents, gated by a second fab), and [[Theses/6981 - Murata Manufacturing]] / Samsung Electro-Mechanics (high-spec MLCC oligopoly as a price-and-availability cycle, not a layout bet) — [G-3] mean-reversion vs trend, Semis #1/#8/#13, VLM last-millimeter layer.

## Summary

Damnang's claim is that every AI-infrastructure conversation uses "power" for two problems that do not share an equity map. A GPU sits at roughly a kilowatt, a rack is already hundreds of kilowatts and heading toward a megawatt, and a campus is measured in gigawatts — several AI campuses due in 2026, OpenAI's Stargate already past its original 10 GW-by-2029 commitment after adding more than 3 GW in the ninety days to April 2026, Meta talking tens of gigawatts this decade [1×: Damnang]. Getting that electricity onto the campus is transmission, substations, and multi-year US interconnection queues: [[Theses/VRT - Vertiv Holdings]]'s layer. This article is the second problem: delivering watts to a die that will not accept them at high voltage. Claim scope is explicit — 800VDC rack distribution is deferred to a sequel; figures are public-source snapshots that may have moved; the piece is not a buy/sell recommendation.

The mechanism is school-physics applied at current densities a house never sees. Power is voltage times current, so a modern data-center GPU at more than 1,000 W and under 1 V forces thousands of amps (a typical home service is ~200 A). Resistive loss scales with the square of current: double the flow, quadruple the heat; triple it, nine times. Voltage at the die cannot be raised, so the only lever is a shorter, thicker path. The second failure mode is transient: when compute load steps, a converter sitting a board-trace away cannot refill the rail in time, voltage sags, and the GPU throttles to avoid a glitch. Leave either unsolved and campus megawatts become heat before they become FLOPS — paper GPU specs do not land. Two fixes follow. Skip the traditional 48 V → ~12 V → <1 V cascade and convert 48 V straight to the point of load; move the converter from the chip's edge (lateral power delivery, LPD) to the underside of the board directly beneath the die (VPD), shrinking the kiloamp run. Put local capacitance next to the die — industry estimates put hundreds of thousands of MLCCs in a single NVL72-class cabinet — so the spike is drawn from a tank a millimeter away rather than from a converter centimeters away.

On converters, MPWR and Vicor both ship LPD and VPD; the weight of the franchise differs. MPWR is a volume power-semiconductor house: cheap at scale, designed into most of what ships today, earning on unit count and rising amps-per-stage rather than on a layout flip. Vicor sells modules (converter + coil + capacitor in one package), leads on current-per-area-and-thickness, and has wrapped VPD plus the internal circuit architecture in patents — design around them or pay a licence; Q2 guidance rose on both higher product revenue and a newly signed licence [1×: Damnang / Vicor]. Consensus, which the author shares for the next two to three years, is that LPD stays dominant because higher-current single converters lift performance without a board-and-package redesign, and because VPD still stacks converter heat under the GPU. What actually ships is a hybrid: most stages around the chip, some underneath — the path Vicor management described on its earnings call. On that clock, MPWR is the steadier cash-flow: enterprise-data revenue ~2.6× year-ago in Q2 and the segment growth-guide floor lifted from 85% to 130%, so rising chip power alone can carry results inside the current generation even if VPD slips [1×: Damnang / MPWR]. The residual risk is generational socket reset, not layout. Vicor is the opposite security: existing module revenue does not explain the price; the multiple is the bet that as multi-die + HBM packages eat the perimeter, both modules and patents re-rate. Large OEMs and some hyperscalers are asking for modules ≤3 mm; Vicor's second-generation part hits the required current density at ~1.5 mm and is described as the only company that can do both today. That part is already in wafer-scale systems (industry assumption: [[Theses/CBRS - Cerebras Systems]]), and management named TPUs, GPUs, and wafer-scale engines together as second-generation targets. The near-term bind is manufacturing: fab 1 is near capacity, so a record backlog is not converting until fab 2 is confirmed and lines come up. At ~17× sales the licence mix already fattens the multiple versus a typical power-IC comp; what is not in the number is the size and timing of fab 2 — groundbreaking is the point the author says the math gets redone [1×: Damnang]. [G-13] isolates one operating variable: VPD timing, not "does AI use power."

MLCC is a different exercise. High-capacitance, high-reliability parts for AI servers are an oligopoly centered on Murata and Samsung Electro-Mechanics. Capacitors sort by distance from the die: large polymer/tantalum on the board for slow changes, MLCCs around the chip for the middle band, thinner/faster silicon capacitors under or inside the package. MLCCs dominate by count and by value. Whichever converter layout wins, more chip power means more capacitors, so the converter question (who takes the socket) does not apply. The trade is price and supply: enter while prices are rising, exit before the phase turns — closer to owning a cyclical component than waiting on a technology transition ([G-3], Semis #3/#7/#13). Right now the constraint is availability, not list price. Murata capacitor revenue +16.5% quarter-on-quarter with backlog at ¥617.8 billion; channel checks put some high-spec lead times at 30 weeks [1×: Damnang]. Customers are locking volume via long-term supply agreements rather than pushing price down; SEMCO has closed agreements with about ten counterparties including major hyperscalers and semiconductor firms. Only a handful of suppliers can build the top of the range — parts above 100 µF or rated to 125 °C — so leverage sits on the supply side (Semis #2 qualification-gate). Timing of P&L flow-through differs: Murata raised first, is already seeing it, and lifted full-year data-center revenue outlook to ¥370.6 billion, ~+110% year-on-year; SEMCO raised 30% from August shipments, so the print starts in Q3. SEMCO has also signed AI-server MLCC contracts centered on 2027 delivery (~₩750 billion among those disclosed) plus a ₩1.5 trillion silicon-capacitor agreement announced in May, and is one of the few firms commercializing MLCCs, silicon capacitors, and package substrates together (VLM platform-envelopment test). The cycle-end question is when new lines at both firms start running into a consumer recovery at the same time — the 2022 template for handing price increases back.

## Framework / Mental Model

Damnang titles the map **AI Datacenter Power Investment Map: From 765 kV to 0.65 V** and then applies four nested typologies.

| Layer | Components | How the source uses it |
|---|---|---|
| Three-scale power | GPU ~1 kW; rack hundreds of kW → ~1 MW; campus GW | Separates "gigawatt campus" talk from the chip that actually burns the watt |
| Two bundled "power" problems | (1) plant → campus (grid, lines, substations, interconnection years); (2) rack → die without I²R / sag | Assigns (1) to utilities / power-equipment names and (2) to this article's four-name set |
| Two delivery failure modes + two fixes | Resistive loss ∝ I²; load-step voltage sag. Fix A: shorten/thicken the kiloamp path (48 V→PoL; LPD vs VPD). Fix B: local capacitance | Physics first, tickers second |
| Converter layout typology | LPD (edge of chip); VPD (under board); hybrid (most stages lateral, some vertical) | Consensus + author: LPD-centered hybrid holds 2–3 years; VPD heat-stacking still open |
| Capacitor-by-distance | Polymer/tantalum (board, slow); MLCC (around chip); silicon cap (under/in package, fastest) | MLCC is the volume/value bucket; silicon cap is the innermost complement |
| Two investment exercises | Converter layer = guess which layout wins and who takes the socket. MLCC layer = price and supply; demand is treated as settled | Same AI rack, opposite security type: layout-option vs cycle |

Methodology: start at the die voltage, compute current from P = V × I, then ask which listed company captures the next increment of current, local capacitance, or patent rent. 800VDC is named and then excluded — the map is incomplete on purpose.

## Evidence

All figures are Damnang's citations of public filings, earnings calls, or channel checks as of the August 2026 piece. None independently audited here.

| Item | Figure | Tag |
|---|---|---|
| GPU power / accepted voltage | >1,000 W / <1 V → thousands of amps | [1×: Damnang] |
| Home service current (comparison) | ~200 A | [1×: Damnang] |
| I²R scaling | 2× current → 4× loss; 3× current → 9× loss | [1×: Damnang] |
| Traditional rack cascade | 48 V → ~12 V on board → <1 V near chip | [1×: Damnang] |
| NVL72-class MLCC count | Hundreds of thousands per cabinet | [1×: Damnang] |
| OpenAI Stargate | 10 GW by 2029 committed; already passed by Apr 2026; >3 GW added in prior 90 days | [1×: Damnang] |
| Meta campus language | Tens of GW this decade | [1×: Damnang] |
| GW scale analogy | ~1 million US homes | [1×: Damnang] |
| MPWR enterprise-data revenue | ~2.6× YoY (Q2) | [1×: Damnang / MPWR] |
| MPWR enterprise-data growth-guide floor | 85% → 130% | [1×: Damnang / MPWR] |
| Author LPD/hybrid horizon | 2–3 years LPD-centered hybrid | [1×: Damnang] |
| Vicor Q2 guide | Raised on product revenue + new licence | [1×: Damnang / Vicor] |
| OEM / hyperscaler height ask | Modules ≤3 mm | [1×: Damnang / Vicor call] |
| Vicor 2nd-gen module | Required current density at ~1.5 mm; described as only vendor that can | [1×: Damnang / Vicor call] |
| 2nd-gen named targets | TPUs, GPUs, wafer-scale engines | [1×: Damnang / Vicor] |
| Wafer-scale customer (industry assumption) | Cerebras | [1×: Damnang] |
| Vicor valuation snapshot | ~17× sales (Aug 3 mkt cap / company FY revenue guide); licence mix fattens vs product comps | [1×: Damnang] |
| Vicor capacity bind | Fab 1 near capacity; record backlog waits on fab 2 site + lines; groundbreaking redoes the math | [1×: Damnang] |
| High-spec MLCC structure | Oligopoly: Murata + Samsung Electro-Mechanics | [1×: Damnang] |
| Top-of-range parts | >100 µF or 125 °C — handful of suppliers | [1×: Damnang] |
| Murata capacitor revenue | +16.5% QoQ | [1×: Damnang] |
| Murata capacitor backlog | ¥617.8B | [1×: Damnang] |
| High-spec MLCC lead times | Up to 30 weeks (channel checks, some SKUs) | [1×: Damnang] |
| Murata FY data-center outlook | ¥370.6B, ~+110% YoY | [1×: Damnang / Murata] |
| SEMCO LTA book | ~10 counterparties incl. major hyperscalers and semi firms | [1×: Damnang] |
| SEMCO price hike | +30% from August shipments; P&L from Q3 | [1×: Damnang] |
| SEMCO AI-server MLCC contracts | Centered on 2027 delivery; ~₩750B among those disclosed | [1×: Damnang] |
| SEMCO silicon-capacitor agreement | ₩1.5T, announced May | [1×: Damnang] |
| SEMCO bundle | MLCCs + silicon capacitors + package substrates | [1×: Damnang] |
| Cycle-end template | New lines + consumer recovery together; 2022 giveback | [1×: Damnang] |
| Explicitly out of scope | 800VDC to the rack | [1×: Damnang] |

No MPWR thesis exists in `/Theses`; do not invent one. Converter-layer claims attach to [[Theses/VICR - Vicor Corporation]]; passives to [[Theses/6981 - Murata Manufacturing]]; the current sink to [[Theses/NVDA - Nvidia]]; campus/grid to [[Theses/VRT - Vertiv Holdings]]; the named wafer-scale socket to [[Theses/CBRS - Cerebras Systems]].

## Contradiction Check

**[[Theses/VICR - Vicor Corporation]] §Summary and §Key Non-consensus Insights #1 (architectural necessity) vs this source's 2–3 year LPD-centered hybrid.** The thesis states VPD is "structurally required" to feed 2,000 A+ Rubin/Rubin Ultra currents and that "the architectural reality has flipped" after the H100 lateral displacement. Damnang's consensus-plus-author view is the opposite clock: LPD stays dominant because higher-current converters postpone a board redesign, VPD still co-locates converter heat with the GPU, and what ships is hybrid — Vicor management said the same on the call. That cuts the socket-necessity leg and lines up with the thesis's own July mental-model update that architectural-necessity is weakening and the live bet is the IP toll. Semis #8 (architecture remaps the bottleneck) fires as a *timing* hypothesis, not as "VPD has already won."

**[[Theses/VICR - Vicor Corporation]] §Conviction Triggers → HIGH (Rubin NVL144 VPD content + FY27 licensing >$300M cumulative + Q4 2026 product-only GM >50%) and → CLOSE (MPS ships a clean-sheet vertical matching density).** Source does not confirm a NVIDIA reference-design socket. It places second-generation VPD in wafer-scale first (Cerebras assumed), then names TPU/GPU/WSE as a customer-count path from one to two to three. That is closer to the thesis Mental Models line that the lead VPD customer has migrated to [[Theses/CBRS - Cerebras Systems]] than to HIGH-trigger NVIDIA content. On CLOSE, the source's 1.5 mm / required-density "only company today" claim is the live test of whether the architectural moat is buyable — hold as hypothesis, not a verdict (VLM interface/standard-control + Semis #2). **Valuation / capacity:** ~17× sales on an August 3 print is [G-13] expectations infrastructure — the price embeds a layout shift plus licence mix; fab-2 groundbreaking is the author's isolated operating variable. That sits next to, and is not automatically the same object as, the thesis's Andover Fab One expansion already lifted to ~$1.5B nameplate with a second 3Di line in 2026 — two capacity stories that a later `$sync` has to reconcile rather than merge.

**[[Theses/6981 - Murata Manufacturing]] §Summary / Insight #1 (440k MLCCs per GB200 NVL72; AI volume swamps smartphone) and §Conviction Triggers.** "Hundreds of thousands" in an NVL72-class cabinet is the same order of magnitude, less precise — supports the structural-count direction, does not verify the thesis's 5,000+ per-accelerator HIGH-trigger print. Backlog ¥617.8B, +16.5% QoQ capacitor revenue, 30-week high-spec leads, and Murata's ¥370.6B / ~+110% data-center outlook support the availability-constraint / units-up-prices-up phase (Semis #1, #7). The author's explicit instruction — treat MLCC as a cyclical component, exit before capacity plus consumer recovery rhymes with 2022 — is the thesis's own → LOW trigger (small-case ASP down >5% YoY two quarters, leads <10 weeks, GM <28%) written in English. [G-3] and Semis #13 fire adversarially: do not narrate a late-up-cycle shortage as a compounder. SEMCO's ₩1.5T silicon-cap agreement (May) plus ~₩750B 2027-delivery AI MLCC and the MLCC+cap+substrate bundle corroborate the thesis Outstanding Question that SEMCO, not Murata, is commercializing the innermost silicon-cap socket (VLM: owning the chemistry ≠ owning the AI application layer).

**[[Theses/NVDA - Nvidia]] §Summary (Rubin as the current sink; paper FLOPS as the priced object).** Source does not touch CUDA, Omniverse, or ASIC share. It does say a GPU that cannot be fed at <1 V without sag will throttle — so PDN physics is a performance limiter *on Nvidia's own parts*, complementary to the compute-layer thesis rather than a challenge to it. NVL72 cabinet MLCC counts and kiloamp rails are the Semis #8 rack-scale remap (NVL72 → higher current → power-delivery + passives) sitting under every Rubin unit.

**[[Theses/VRT - Vertiv Holdings]] §Summary and §Non-consensus Insight #5 (grid interconnect as the real chokepoint).** Source agrees that plant-to-campus is a years-long utility/permitting problem and then refuses to let that problem stand in for board-level delivery. Owning Vertiv (or "owning utilities") is not the whole power trade. It does not test VRT's liquid-cooling physics moat, OCP authorship, or book-to-bill; those live one layer above the 48 V → 0.65 V run.

**[[Theses/CBRS - Cerebras Systems]] §Summary / Semis #10.** Industry assumption that wafer-scale VPD is already in use because there is no perimeter for converters is an adjacency, not a Cerebras revenue confirmation. It supports Vicor's named concentration migration; it does not clear CBRS HIGH triggers (OpenAI recognition, UAE mix, cloud GM).

No MPWR thesis to contradict. If one is opened, the source's question is content-per-accelerator while LPD/hybrid holds versus socket loss at the next GPU turn — not "does VPD obsolete MPS in 2026." Cross-model agreement (bottleneck + qualification-gate + infrastructure-layer VLM) is the READING PROTOCOL cue to hunt the bear: VPD arrives faster than the 2–3 year hybrid clock (hurts MPWR content, helps Vicor product); MLCC capacity plus consumer recovery reprints 2022 (hurts 6981); GPU current density stalls (hurts all four names).

## Source Excerpts

> "A modern data center GPU pulls more than a thousand watts, while the voltage it actually accepts is under one volt. Pushing all that power through at rock bottom pressure sends the current into the thousands of amps."

> "My own view is that an LPD-centered hybrid holds for the next two to three years."

> "Enterprise data revenue came in around 2.6 times the year ago level, and management lifted the low end of its full year growth expectation for the segment from 85% to 130%."

> "Large OEMs and some hyperscalers are asking for modules 3 mm or shorter. Vicor's second generation part delivers the required current density at about 1.5 mm, half that, and it's understood to be the only company that can do it today."

> "Set the August 3 market cap against the company's own revenue guidance for the year and you get roughly 17 times sales."

> "Murata's capacitor revenue rose 16.5% quarter on quarter while its backlog built to 617.8 billion yen… Channel checks suggest lead times on some high spec parts have stretched to as long as 30 weeks."

> "Samsung Electro-Mechanics raised 30% from August shipments… It has signed a run of AI server MLCC contracts centered on 2027 delivery, roughly 750 billion won among those disclosed, plus a 1.5 trillion won silicon capacitor agreement announced in May."

> "In 2022 that's exactly where the price increases were handed back."
