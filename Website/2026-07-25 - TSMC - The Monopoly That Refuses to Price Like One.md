---
date: 2026-07-25
tags: [essay, investment-case, laniakea-partners, semiconductors, foundry, TSM]
status: draft
audience: intermediate
source_note:
  - "[[Theses/TSM - Taiwan Semiconductor]]"
  - "[[Thesis Breakdowns/2026-07-25 - TSMC]]"
  - "[[Website/2026-07-22 - How Laniakea Partners Invests]]"
  - "[[Sectors/Semiconductor Foundries]]"
  - "[[Mental Models/Industry - Semiconductors]]"
  - "[[Mental Models/Lens - Value Layer Monopoly]]"
source: internal synthesis
---

# TSMC: The Monopoly That Refuses to Price Like One

**The case for TSMC is not that it dominates leading-edge chipmaking—the market has known that for years. It is that the dominance is running deliberately below its own capacity on price, that a yield lead measured in tens of points converts into margin no competitor can bid away, and that a share price at roughly the index multiple hands the next decade of AI demand to the buyer for free.**

On July 16, 2026, TSMC reported the strongest quarter in semiconductor history: $40.2 billion of revenue, up 34% in US dollars, a 67.7% gross margin—a record, up more than nine points in a year—full-year growth guidance raised to above 40%, and capital spending raised to $60–64 billion. The stock fell 5% on the print and now sits 11% below its high, near 23 times this year's earnings.

The market's logic follows the industry's base rate. Record margins, sold-out capacity, aggressive customer forecasts and record capital spending have clustered near every semiconductor top for fifty years. On that template, 2026 is the peak of a shortage, the new factories are the coming glut, and today's margins are a scarcity rent about to be competed away.

Three observations challenge the template. TSMC's margins are produced by a yield gap that new capacity cannot close, because competitors cannot yet manufacture the product economically at any price. Its pricing beneath a visible shortage is restraint, not weakness—an unexercised option the company spends in measured doses. And the demand curve underneath it points toward a roughly five-fold expansion over the next decade, while the multiple assumes growth effectively ends here.

This is the configuration Laniakea Partners looks for: a business the market fully recognises, still valued through the mechanics of a cycle it may no longer belong to.

## Yield is the product, and failed chips have no salvage value

A foundry does not really sell wafers; it sells working chips. Every leading-edge wafer absorbs the same cost whether its chips function or not—the same EUV exposures, the same hundreds of process steps, the same months of cycle time. A failed die cannot be reworked, discounted or resold. It is scrapped. At a given wafer price, yield—the share of chips that work—does not influence the margin at the edges. Yield *is* the margin.

That is what makes TSMC's lead over Intel, Samsung and the Chinese foundries an absolute advantage rather than a relative one. Every percentage point of yield above a competitor is a full point of saleable output at zero incremental cost, and every point below is fully-paid-for silicon in the scrap bin. The current gap is not a percentage point. At 2nm-class production, TSMC's N2 runs near 90% yield at maturity while Samsung's SF2 is estimated at 55–60%—below the 65–70% threshold at which a leading-edge line recovers its capital at all.

| | TSMC N2 | Samsung SF2 |
|---|---|---|
| Wafer price | ~$30,000 | ~$20,000 (a 33% discount) |
| Yield | ~90% at maturity | 55–60% |
| Working chips from a 100-die wafer | ~90 | 55–60 |
| Effective cost per working chip | ~$333 | ~$348–364 |
| Resulting economics | 67.7% gross margin | reported segment losses |

Samsung's discount is an illusion. The customer pays per working chip, and at current yields Samsung is the more expensive foundry at two-thirds the price. TSMC's premium is therefore not a cost its customers bear—it is TSMC's share of a yield surplus that only TSMC creates. This is why undercutting cannot buy back share, and why the profit spread across the industry—TSMC at a 67.7% gross margin, SMIC at 20.1%, Samsung Foundry and Intel Foundry in losses—is simply the yield table restated in accounting form.

The rest of the field confirms the pattern. Intel's process recovery is real: 18A products entered high-volume production in early 2026 with backside power delivery ahead of TSMC. But its foundry booked $293 million of external revenue against a $2.1 billion quarterly operating loss, and most of the external growth came from an accounting change, not a new customer. Technology roadmaps are converging; merchant proof—a major outside designer in sustained, repeat high-volume production—has not. SMIC's best independently confirmed process remains 7nm-class, built on older DUV tools whose extra patterning steps impose the exact cost-and-yield penalty this framework predicts, with reported yields on advanced parts as low as 15–46%.

The gap also compounds. Yield is learning, learning scales with wafers processed, and TSMC runs roughly 92% of the world's leading-edge output—an order of magnitude more production learning than everyone else combined, accumulated across 12,682 products for 534 customers in 2025 alone. Yield knowledge is tacit: defect provenance, recipe tuning, operator craft. It cannot be hired, licensed or reverse-engineered from a teardown, which is why fifteen years of node labels claiming parity have not produced economic parity.

## Pricing restraint is unexpressed pricing power

The shortage is not subtle. TSMC's N3 node runs above 100% effective utilization in the second half of 2026, with AI taking roughly 60% of its output this year and an estimated 86% next. N2 sold out at launch. Nvidia pre-booked more than half of 2026 CoWoS advanced-packaging capacity at a 20% price increase, and C.C. Wei told investors in July that packaging capacity is "so tight that now it's limiting my customers' growth." Cleanrooms take about two years to build, so no supply response can arrive faster.

Against that backdrop, TSMC raised prices 3–10% across nodes—its fourth consecutive annual single-digit increase—and deferred part of the 2026 increase into early 2027. In memory, comparable scarcity produced triple-digit price moves. Jensen Huang, the largest customer, has said publicly that TSMC should charge more. A monopoly supplier being told by its own customer to raise prices is direct evidence of a gap between list price and market-clearing price. That gap is unexpressed pricing power, and it surfaces as rationing: when price does not clear a market, allocation does. TSMC currently decides which of its customers is allowed to grow.

Wei explained the restraint himself: customers must remain successful, TSMC will not impose "sudden four- or five-fold increases," and margins need only fund expansion. This is lifetime-value pricing. Extracting the full scarcity rent today would drain the customer profits that fund the next generation of designs—TSMC's future orders—would subsidise second sources into existence (Samsung is discounting 2nm by a third precisely to buy re-qualification trials; Intel has US industrial policy behind it), and would invite the political ceiling that every essential-layer monopoly eventually meets. Restraint maximises the duration of the rent rather than this cycle's share of it, and part of the compensation is taken in kind: multi-year commitments, prepayments, early roadmap access and allocation obedience instead of headline price.

The proof that this is choice rather than ceiling is the margin itself. TSMC prints a 67.7% gross margin *while under-charging*, absorbing three to four points of N2 ramp dilution and rising overseas-fab costs. The reserve gets spent in controlled doses at each node transition—N2 at ~$30,000 a wafer, packaging at +20% for guaranteed allocation. What the market prices as a cyclical margin peak is closer to a margin policy, with the un-charged spread held back as the shock absorber for exactly the downturn the bears forecast. A company that has not exercised its pricing power retains it for when it matters.

## A five-fold demand curve priced for zero growth

A five-fold expansion of AI compute demand over ten years—roughly 17% a year—is the conservative reading of the current evidence, not the aggressive one. Hyperscalers will spend an estimated $400–450 billion on capex in 2026 and management says its multi-year AI outlook has strengthened. High-performance computing is now 66% of TSMC revenue, up from 41% in early 2023. Demand is broadening, not narrowing: GPUs, the custom accelerators of every major cloud, server CPUs, networking silicon and optical interconnect have all converged on the same two or three TSMC processes, with no second source at economic yield. And each time compute gets cheaper, total consumption has grown—falling cost per token keeps unlocking workloads that were previously uneconomic to automate, the same dynamic that has expanded every general-purpose technology since the steam engine.

TSMC also captures more of each AI dollar over time. Wafer, advanced packaging, testing, HBM base dies and, from 2027, co-packaged optics stack toward roughly 40% of an Nvidia system's silicon bill of materials, against 15–18% in a typical foundry relationship. A five-fold demand curve therefore translates to at least a five-fold TSMC AI revenue opportunity.

Now the price. At the time of writing the ADR trades near $407, about 23 times an estimated $17.50 of 2026 earnings—roughly the index multiple, and a discount to every monopoly analogue (ASML near 35 times, Visa near 28). An index multiple on a business growing above 40% with 68% gross margins and a 46% return on equity is an explicit forecast: *these earnings do not compound.* The market's own behaviour states it plainly. Earnings that internal work modelled two years ago as a 2028 bull case (~$16–17 per share) are landing in 2026—two years early—and the market's response was an 11% de-rate against rising estimates. Growth arrived ahead of schedule and was assigned a negative price, the arithmetic of a market treating incremental AI earnings as borrowed from the future rather than added to it.

That sets a remarkably low hurdle. If growth truly stops, the buyer owns the most profitable manufacturer on earth at the market multiple, with a dividend just raised by a third. If the five-fold path is even directionally right and TSMC holds its share and content, earnings compound in the mid-teens for a decade and the shareholder return approximates that compounding at an unchanged multiple. Zero growth is priced; everything above zero is free.

## Two readings of the same company

| The capex-cyclical read (in the price) | The toll-road read |
|---|---|
| Record margins mark the top of a shortage | Margins are the yield spread over competitors, which is structural |
| Pricing rode scarcity up and will ride it down | Pricing never rode scarcity up—the scarcity rent is largely unspent |
| Record capex signals the coming glut | Capacity is pre-sold: N2 sold out, >50% of 2026 packaging pre-booked, customers publicly supply-constrained |
| New supply restores competition | Rivals cannot make the product at economic yield; qualification adds years after they can |
| 2026 is peak earnings, to be faded | 2026 is the first year structural AI demand met deliberately restrained pricing |

## What would prove the bull case wrong

The margin test is the cleanest. Two consecutive quarters below a 63% gross margin—after separating the disclosed N2 and overseas-fab dilution—while announced price increases are in effect would mean pricing is failing rather than investing, and the restraint story collapses into an erosion story.

The competitive falsifier is merchant proof, not roadmap parity: a named external customer's leading-edge product in sustained high-volume production at Intel or Samsung, or a production-scale win for a CoWoS packaging alternative (Google's TPU evaluating Intel's EMIB is the live watch item). Announcements and internal chips do not count; repeat qualified volume does.

The demand falsifier is the second derivative of hyperscaler capex. If AI spending decelerates before the new capacity fills—TSMC's HPC revenue growing below 10% in any 2027 quarter would be the marker—the record capex becomes the overhang the bears already price. Related: if software efficiency starts shrinking total silicon consumed rather than expanding workloads, the five-fold curve bends. The observable is aggregate leading-edge wafer consumption, not any single model's requirements.

Taiwan stands apart from all of these—a binary, not a data series. More than 95% of leading-edge capacity remains physically in Taiwan through 2028, and internal scenario work puts invasion or blockade at 85–95% permanent impairment, far beyond the discount embedded in the multiple. The $265 billion US buildout thickens deterrence by making TSMC's survival an American balance-sheet interest, but Arizona at 5–8% of capacity through 2030 is resilience, not duplication. Part of the "zero-growth multiple" is Taiwan rent. Owning TSMC is underwriting deterrence, and the position should be sized by that fact rather than pretending the discount is inefficiency.

## The cheapest monopoly in the AI stack

The market is not blind to TSMC's position; it is unwilling to pay for its duration. It sees record margins and prices a peak. It sees single-digit price increases amid a shortage and reads a ceiling where the mechanism says reserve. It sees a demand curve pointing five-fold higher and offers the index multiple. The bullish reading requires no heroics: the yield gap keeps scrappage on competitors' books, pricing power stays banked rather than spent, and AI demand needs to arrive at only a fraction of forecast for zero-growth expectations to break. TSMC does not need to start charging monopoly prices. It only needs to remain the one factory that can make what everyone must buy—and let the price it declines to charge stand as the measure of how much power is still in reserve.
