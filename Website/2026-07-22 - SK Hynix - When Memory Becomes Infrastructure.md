---
publish: false
date: 2026-07-22
tags: [essay, investment-case, laniakea-partners, semiconductors, HBM, 000660]
status: draft
audience: intermediate
source_note:
  - "[[Theses/000660 - SK Hynix]]"
  - "[[Thesis Breakdowns/2026-07-19 - SK Hynix]]"
  - "[[Website/2026-07-22 - How Laniakea Partners Invests]]"
  - "[[Sectors/DRAM & HBM Memory]]"
  - "[[Mental Models/Industry - Semiconductors]]"
  - "[[Mental Models/Lens - Value Layer Monopoly]]"
source: internal synthesis
---

# SK hynix: When Memory Becomes Infrastructure

**The case for SK hynix is that the industry has changed enough for the next trough to be far more profitable than the last, and for a business still valued as a violent cyclical to earn a permanently higher valuation; the present memory shortage does not need to last forever.**

The market's concern is familiar: memory prices rise, manufacturers report peak margins, profits fund new factories, supply eventually overwhelms demand. Earnings then collapse toward the levels of the previous downcycle. That base rate has been correct for most of the industry's history.

Three forces now challenge it. DRAM has consolidated from dozens of producers to three global suppliers. HBM (high-bandwidth memory) is co-designed and qualified with customers rather than bought as an interchangeable chip in a spot market. AI is raising memory content while HBM production itself consumes disproportionate wafer capacity. Together, these changes support faster volume growth, greater supply discipline and a higher floor under margins.

This is the category change we look for at Laniakea Partners: the market can see the boom, but may still be valuing the business through the structure of the cycle that came before it.

## Memory has been consolidating for fifty years

Memory did not begin as an oligopoly. In the 1970s, Intel, Texas Instruments and Mostek led DRAM; Mostek alone once held roughly 85% of the market. Japanese conglomerates then attacked with superior manufacturing scale. By 1988, Hitachi, NEC, Toshiba, Mitsubishi and Fujitsu had taken more than three-quarters of global DRAM production.

Korean manufacturers displaced them through even more aggressive countercyclical investment. Samsung built during downturns, accepted losses that weaker competitors could not, and used the next process transition to take their customers. Hyundai Electronics followed a similar path, acquired LG Semicon after the Asian Financial Crisis and became Hynix.

The industry's later history is a sequence of exits rather than entries:

| Year | Event | Structural result |
|---|---|---|
| 1998 | Hyundai Electronics acquires LG Semicon | Korea consolidates around Samsung and the future Hynix |
| 1999 | NEC and Hitachi merge their DRAM operations | Elpida becomes Japan's final scaled DRAM challenger |
| 2009 | Qimonda fails after accumulating billions in losses | Europe effectively exits commodity DRAM |
| 2011 | SK Group acquires control of Hynix | The number-two Korean producer gains a durable balance sheet |
| 2012–2013 | Elpida fails and Micron acquires it | Japan exits standalone DRAM; the modern triopoly forms |

Each bust removed the producer least able to finance the next process node; the survivors absorbed its share, gained scale and raised the capital required to challenge them. A modern DRAM fab now costs tens of billions of dollars, takes years to build and still needs a decade of process knowledge before yields become competitive. Outside China's subsidised domestic ecosystem, no new global DRAM supplier has reached scale in more than thirty years.

That three companies control the market is half the point; the other half is that there is no longer an undercapitalised fourth player to bankrupt. Samsung once had a rational reason to flood the market: destroying Qimonda or Elpida created lasting share gains. Repeating that strategy against SK hynix or Micron would impose years of losses without reliably removing either competitor. Reducing the field from three to two would invite fierce customer and regulatory resistance.

## Three survivors can prioritise returns over share

Consolidation did not abolish the memory cycle; the triopoly existed during the 2018–2019 and 2022–2023 downturns. It did, however, change how quickly supply responded once economics deteriorated.

At the 2023 trough, Samsung, SK hynix and Micron all cut wafer starts by roughly 20–30%. Those decisions did not require explicit coordination: each company could see the same inventories, utilisation rates, competitor capacity and cash losses. With only three participants, aggregate supply is legible and the cost of irrational expansion is borne by the same firms that would suffer the price decline.

The old industry maximised bits and defended share; the emerging one increasingly optimises product mix and return on capital. A supplier can allocate a wafer to HBM, server DRAM or lower-value consumer memory according to customer commitments and margin. Multi-year agreements make those decisions less dependent on speculative spot orders. Public capacity plans make the likely supply response easier for every participant to model.

Samsung remains the main threat to this discipline: it has the balance sheet and strategic incentive to spend heavily when it wants to regain share. The bullish view does not assume permanent harmony; it assumes that a three-player industry needs less destructive capacity growth to meet structurally stronger demand.

## HBM changes memory from a commodity into a qualified component

Traditional DRAM is close to interchangeable: a PC or phone manufacturer can shift orders among qualified suppliers, negotiate against spot prices and carry inventory when it expects a shortage. Price and cost per bit dominate the decision.

High-bandwidth memory changes the relationship. HBM stacks multiple DRAM dies beside an AI accelerator and connects them through thousands of microscopic channels; the stack must move data at extreme speed while controlling heat, electrical noise, warpage and compounded defects. One weak layer can ruin the finished product.

SK hynix has worked on HBM since co-developing the first standard with AMD between 2008 and 2013. Its MR-MUF packaging method and accumulated yield knowledge helped it qualify successive generations with Nvidia while larger rivals struggled. That history matters because qualification is not a one-off laboratory test: supplier and customer debug the memory, packaging and accelerator as one system. Production then creates failure and yield data that improves the next generation.

This turns the customer relationship from purchasing into co-design. Early roadmap access guides the supplier's capital and process decisions, custom logic base dies make a memory product specific to a processor platform, and switching supplier can require system revalidation rather than a new purchase order. The anchor customer thus becomes a source of learning and lock-in, not just revenue concentration.

Contract structure follows the technical structure. AI customers increasingly reserve memory through multi-year supply agreements because missing HBM can delay an entire datacenter deployment. Reported agreements have moved toward firmer volume commitments and less price protection. Contracts cannot repeal supply and demand, but they replace part of the old spot-market cycle with planned capacity, committed volumes and shared roadmaps.

HBM is therefore not a permanent monopoly: Samsung and Micron can qualify, Nvidia wants multiple sources, and each architecture generation reopens part of the contest. Yet a three-supplier qualified market is structurally different from commodity memory sold by a dozen producers against daily spot prices.

## AI demand tightens both premium and conventional memory

The strongest bull mechanism is that HBM demand expands the market while constraining its supply. HBM uses larger dies, through-silicon vias, more demanding front-end processes and stacked yields; a wafer dedicated to HBM3E can produce roughly one-third of the usable bits of a conventional DRAM wafer; the penalty can widen further at HBM4.

Every wafer redirected to HBM therefore removes several wafers' worth of ordinary bit supply. Growth in the premium product tightens conventional server and consumer DRAM at the same time. This is the opposite of a normal technology transition, where better products usually increase effective supply and push prices down.

Demand is also shifting toward end markets with rising memory content. AI accelerators need more bandwidth and capacity with each platform generation, general-purpose servers require more DRAM to feed larger computing clusters, datacenter processors are adopting additional low-power memory, and inference creates demand for high-capacity enterprise storage. SK hynix participates through HBM, conventional DRAM and Solidigm's NAND products.

Software efficiency is the cleanest counterargument: better quantisation, caching or model architecture can reduce memory required per task. The demand thesis survives if lower inference cost expands the number of tasks faster than memory intensity falls. The observable is total memory shipped into AI systems, not memory required for one benchmark.

## Why the next trough can sit far above the last

The bullish reclassification rests on the interaction of consolidation, qualification and volume growth rather than any one factor alone.

| Old memory cycle | Emerging memory structure |
|---|---|
| Many suppliers fought for survival and share | Three scaled global suppliers can prioritise return on capital |
| PC and mobile demand drove large inventory swings | AI, servers and storage add faster structural volume growth |
| Products were selected mainly on price and cost per bit | HBM requires co-design, yield leadership and platform qualification |
| Spot pricing and short contracts transmitted every inventory swing | Multi-year commitments increase volume visibility and slow repricing |
| Process scaling increased bits per wafer and restored supply | HBM 'reverse scaling' removes conventional bit supply as it grows |
| Downcycles pushed laggards into losses or bankruptcy | The surviving firms can cut output before solvency becomes the constraint |

Peak margins will still fall: rival yields will improve, new fabs will arrive and customers will recover some negotiating leverage. The difference is the likely distance between peak and trough. A larger market growing through AI content, supplied by three disciplined producers and increasingly governed by qualification and contracts, should not need to revisit the loss-making economics that eliminated the previous generation of competitors.

That makes today's peak earnings more relevant than memory investors assume. They may represent an extreme version of a new earnings range rather than a temporary point disconnected from future earning power. If future trough profits remain close enough to the present peak, the stock should no longer be valued as though almost all current earnings will disappear.

## SK hynix is the highest-quality expression of the change

SK hynix combines the industry reset with company-specific execution. It holds the leading HBM position, has accumulated more than a decade of co-design and packaging experience, and has repeatedly converted process knowledge into qualified volume. Its high HBM mix gives it greater exposure to the part of memory becoming least commodity-like.

The company does not need to preserve peak market share for the thesis to work; a smaller share of a much larger HBM market can still produce rising volume, while qualification and yield can protect superior economics. The relevant test is whether SK hynix keeps preferred allocations and pricing as Samsung and Micron become credible alternatives.

Its broader portfolio adds useful optionality. Solidigm provides enterprise QLC storage for data-heavy AI systems. High-bandwidth flash, under development with SanDisk, could create a tier between expensive HBM and slower bulk storage. Neither is required to justify the core case, but both extend the runway if SK hynix evolves from a DRAM manufacturer into a full memory-architecture supplier.

## The valuation prices an earnings collapse

At the time of writing, SK hynix trades at roughly five times current-year earnings estimates, a multiple that expresses a forecast rather than neglect: the market expects peak earnings to collapse. Even a 50% decline in profit would turn five times peak earnings into roughly ten times trough earnings. The bullish case is that consolidation, structural volume growth, contracts and HBM mix make the decline smaller, leaving both higher normalised earnings and room for a permanently higher valuation regime.

## What would prove the bull case wrong

The thesis fails if the new structure behaves like the old one. The clearest warning would be capital spending rising faster than committed demand while memory prices weaken; Samsung choosing share over returns would reopen the historical capacity war.

A global fourth supplier would also damage the three-player floor. CXMT can become a major producer inside China; the larger risk is that it reaches leading-edge yields and competes across the global customer base rather than remaining part of a parallel domestic ecosystem.

SK hynix must also re-earn its process lead. Hybrid bonding or another packaging transition could reset the yield race. Multi-year contracts could prove easy to renegotiate once supply loosens. Nvidia could turn qualification into ordinary dual-source procurement. Any of these would narrow the gap between HBM and commodity economics.

The decisive evidence will arrive in the next downcycle. If pricing normalises but SK hynix's margins remain above prior-cycle peaks, the higher-floor thesis is confirmed; if new capacity returns the company to old trough economics, the apparent structural change was only an unusually powerful boom.

## Memory may be leaving its old category

Memory became one of technology's most cyclical industries because too many suppliers sold interchangeable products from factories they could not afford to idle. Fifty years of consolidation removed nearly all of those suppliers, and HBM then changed the product itself: manufacturing became more difficult, customers entered the design loop, supply moved toward long-term agreements, and the fastest-growing product began consuming rather than releasing effective capacity.

The market is fighting the last war: it sees record earnings and assumes the familiar collapse. The more bullish reading is that the next downturn begins from a different industry structure and ends at a much higher margin floor. SK hynix does not need the cycle to disappear; it needs only memory's future trough to resemble today's earnings more than yesterday's losses.
