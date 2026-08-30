---
date: 2026-08-29
tags:
  - essay
  - investment-case
  - laniakea-partners
  - neoclouds
  - artificial-intelligence
  - datacenters
  - NBIS
  - Nscale
status: draft
audience: intermediate
source_note:
  - "[[Research/2026-08-29 - NBIS - Rubin Hour 5GW Funding and Hyperscaler EBIT per GW - synthesis]]"
  - "[[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]"
  - "[[Research/2026-08-27 - NVDA NBIS - Nscale 45B Vera Rubin Anthropic - news]]"
  - "[[Research/2026-08-25 - NBIS - ClickHouse and Avride Private Stakes - synthesis]]"
  - "[[Theses/NBIS - Nebius Group]]"
  - "[[Sectors/Neoclouds & GPU-as-a-Service]]"
  - "[[Macro & Technology/AI Datacenter Financing Mechanism Design]]"
  - "[[Mental Models/Generalist - Overview]]"
  - "[[Mental Models/Lens - Value Layer Monopoly]]"
source: internal synthesis
---

# Nebius: Valuation and end game financial model

The four contracts above $1 billion that Nebius signed in the second quarter price the next vintage of capacity at $20–25 million of annual contract value per megawatt, on one-to-three-year terms and 50–60% prepaid, which at Rubin density is $9–11 per GPU-hour and is the band we take as the going-forward book. That sits above Nscale's six-year Anthropic contract at Monarch, the print the tape has been reading as the Rubin clearing price, which back-solves to about $7.30 an hour, and well above the roughly $3.35 an hour the live Microsoft book still bills, so three prices are in circulation for a GPU-hour and the question for the 2027–31 build is which of them it earns. This is against present prevailing rates of $7/GPU/Hr for Blackwell generation chips in spot markets, equivalent to at least $15/GPU/Hr for the Rubin generation.

## The upcoming vintage

The live book is still the Microsoft wholesale vintage, roughly 100,000 GPUs billing about $3.35 an hour, some $12 million a megawatt against the $20–25 million now being signed, which is a high origination return on the ~$70,000 Blackwell that was actually spent, a failing return on Blackwell at replacement cost, and not the price of the next hall. The four second-quarter contracts, signed against late-2026 capacity and hitting the profit and loss in 2027, are disclosed per megawatt-year rather than per hour, and the conversion rests on an assumed density: Rubin at 3.9 kilowatts, about 257,000 GPUs to the gigawatt, gives $8.90–11.10 at 8,760 hours, GB300 at roughly twice the GPU count per megawatt gives $5–7.50, and no Nebius contract has yet named a Rubin cash rate. We take $10 as the working point inside the Rubin-equivalent of the signed band and run the build from $8 to $12 so the reader can see where cash and the multiple break.

Nscale–Anthropic is the print the tape has been trying to use as the Rubin clearing price, and it is a different object: $45 billion over six years against some 460 megawatts of Vera Rubin at Monarch works out to about $16.3 million per megawatt-year, or about $7.30 an hour if the 460 megawatts is IT load, on a campus Microsoft and Google had both walked away from, with Anthropic filling that hole as the binding offtake and the largest line in a $51 billion backlog ahead of a September IPO, so the contract buys execution and prospectus insurance as much as it buys tokens. The discount reads as the price of a new entrant's execution risk and of the lower return it will tolerate while it builds initial scale, the usual shape of a lighthouse contract, and we therefore do not expect Nscale's rate to be the clearing price for a book with a strong execution record.

## EBIT, cash and dilution at $8 to $12

The 2026 plan is guided at 800 megawatts to a gigawatt of active power, Pennsylvania's first power is end-2027, and the company's own cadence is '>1GW/yr from 2027', so we hold the 2026 book as a persistent ~$2 billion EBIT / ~$4 billion cash-EBITDA line and add one gigawatt a year from 2027, each new gigawatt billed at the average of its start- and end-of-year state (2027 bills 1.5 gigawatts on the way to two at year-end), reaching five energised gigawatts at the end of 2030. Prefunding follows the second-quarter new-deal claim at 50% of capex, $23.5 billion a gigawatt, amortised over five years as deferred revenue; hall cash opex is 30% of revenue; and the 2026 book's 50% cash-EBITDA margin already carries about $1.6 billion of unallocated corporate cost, the gap to a 70% hall margin on $8 billion of ARR, from which incremental corporate cost grows $0.25 billion a year, under 3% of ARR by 2031.

Group EBIT is the $2 billion 2026-book line plus the Rubin stack as those halls age, less incremental corporate cost. 

| $/GPU-hr | 2027 EBIT $bn | 2028 | 2029 | 2030 | 2031 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $8 | 2.8 | 6.0 | 11.7 | 19.7 | 27.4 |
| $9 | 3.6 | 8.4 | 15.7 | 25.2 | 33.7 |
| $10 | 4.4 | 10.7 | 19.6 | 30.7 | 40.0 |
| $11 | 5.2 | 13.1 | 23.6 | 36.2 | 46.3 |
| $12 | 6.0 | 15.4 | 27.5 | 41.7 | 52.6 |

Prefunding steps down from 50% on the first new gigawatt to 30%, 20% and 10% on the next three, and the hole each year is filled with primary equity at a share price compounding 25% from the $209 close. Organic cash is cash EBITDA of the live book less amortisation of advances already collected less incremental corporate cost; net build is the next $47 billion sticker less that year's new advance; and dilution is the August notes' 18.1 million shares converting plus that year's primary, cumulative over 272 million shares.

| Year | Avg GW billed | EBIT $bn | Organic cash $bn | Prefund | Net build $bn | FCF $bn | Equity $bn | Price | Shares m | Cum FD m | Cum dilution |
| ---: | ------------: | -------: | ---------------: | ------: | ------------: | ------: | ---------: | ----: | -------: | -------: | -----------: |
| 2027 |           1.5 |      4.4 |              9.3 |     50% |          23.5 |   −14.2 |        6.2 |  $261 |       24 |      380 |          15% |
| 2028 |           2.5 |     10.7 |             21.0 |     30% |          32.9 |   −11.9 |       11.9 |  $327 |       36 |      416 |          29% |
| 2029 |           3.5 |     19.6 |             34.2 |     20% |          37.6 |    −3.4 |        3.4 |  $408 |        8 |      425 |          32% |
| 2030 |           4.5 |     30.7 |             48.3 |     10% |          42.3 |    +6.0 |          0 |  $510 |        0 |      425 |          32% |
| 2031 |           5.0 |     40.0 |             55.4 |       — |             0 |   +55.4 |          0 |  $638 |        0 |      425 |          32% |

Across the $8–12 band the prepay path and price curve are held constant. Enterprise value today is about $62 billion on an if-converted basis at the $209 close, 356 million shares including the August notes, and each year's EV/EBIT is that $62 billion over the year's EBIT, scaled up by one plus the cumulative dilution to that year.

| $/GPU-hr | Incremental equity $bn | Dilution if converts convert | FD shares m | EV today $bn | 2027 EV/EBIT | 2028 | 2029 | 2030 | 2031 |
| -------: | ---------------------: | ---------------------------: | ----------: | -----------: | -----------: | ---: | ---: | ---: | ---: |
|       $8 |                     41 |                          50% |         474 |           62 |          26× |  14× | 7.7× | 4.7× | 3.4× |
|       $9 |                     29 |                          39% |         445 |           62 |          20× | 9.8× | 5.5× | 3.4× | 2.6× |
|      $10 |                     22 |                          32% |         425 |           62 |          16× | 7.4× | 4.2× | 2.7× | 2.0× |
|      $11 |                     15 |                          25% |         406 |           62 |          14× | 5.9× | 3.3× | 2.1× | 1.7× |
|      $12 |                     12 |                          21% |         396 |           62 |          12× | 4.9× | 2.7× | 1.8× | 1.4× |

## Consensus carries no operating profit before 2029

The published estimates never reach the bottom of our range: aggregated at the same $209 close, the street has Nebius EBIT-negative through 2027 and topping out at $5.7 billion in 2030, with even the highest estimate under $9 billion, against $20 billion on our $8 floor and $31 billion at $10.

| Consensus FY | Revenue avg $bn (low / high) | EBIT low $bn | EBIT avg | EBIT high | Ours at $10 |
| -----------: | ---------------------------: | -----------: | -------: | --------: | ----------: |
|         2026 |           3.35 (3.31 / 3.38) |        −0.72 |    −0.48 |     −0.32 |         n/a |
|         2027 |         11.92 (8.12 / 17.19) |        −1.22 |    −0.75 |     −0.39 |         4.4 |
|         2028 |        22.15 (16.25 / 30.54) |        +0.16 |    +0.24 |     +0.34 |        10.7 |
|         2029 |        40.90 (30.00 / 56.39) |        +1.64 |    +2.49 |     +3.71 |        19.6 |
|         2030 |        57.94 (42.50 / 79.88) |        +3.76 |    +5.75 |     +8.57 |        30.7 |

## EBIT per gigawatt against the hyperscalers

A $10 Rubin gigawatt earns $6–9 billion a year, against between $7.5 and $10.7 billion of cloud operating income per gigawatt of total operating-IT load at Google, Microsoft and Amazon on their first-quarter 2026 loads of 4.7 to 6.2 gigawatts, and about $12–13 billion each once first-party load is stripped out of the denominator.

The discount is wholesale pricing and mix rather than worse silicon: Nebius sells take-or-pay GPU-hours to a handful of labs and hyperscalers, while AWS, Azure and Google Cloud sell a depreciated blend of reserved IaaS, enterprise agreements, Workspace-class SaaS and a GPU-hall slice, on twenty years of already-written-off shells and with the traditional CPU workloads (search, productivity, e-commerce, media) that still fill a minority of the halls and a majority of the historical depreciation base. A new Foxconn-sticker AI gigawatt inside Amazon would print Nebius's year one, $5.3 billion at $10, rather than Amazon's $12 billion external-adjusted blend, and the gap that remains after that restatement is the software and services layer sitting on top of the metal, the thing Nebius does not yet bill at scale and the thing the Yandex inheritance (managed services, an inference platform, MLOps) exists to become.

That gap should close on two clocks that are already running. Incremental IT load across the industry is almost fully AI: the watts being added in 2026–28 are accelerator halls rather than the next generation of search or Exchange, so the hyperscaler's mix is being rewritten from the margin toward the thing Nebius already sells, and the traditional-workload ballast that supports today's $12–13 billion of operating income per external gigawatt is a shrinking share of the live fleet. At the same time Nebius is not confined to renting bare metal: the software stack it built rather than bought is the one credible exception to the sector's 'no operator has differentiated technology' rule, and as that stack is sold as managed compute, storage and networking rather than as a GPU-hour, the wholesale discount to Azure and GCP is the thing being closed rather than a permanent feature of the layer. The convergence claim is narrower than 'a neocloud becomes a hyperscaler by stacking Rubin' and it is not year-one arithmetic: a fleet whose incremental watts are AI, billed with a services layer on top, should not trade at a permanent discount to the external-adjusted cloud gigawatt once the 2026 book has been depreciated through and the 2027–29 halls are the company. The 2028–29 multiples at $10 in the table above, dilution included, are the market's refusal to underwrite that convergence, and the Q3 active-power print decides whether the 2026 gigawatt exists to converge from.

We expect hyperscaler operating income per gigawatt to trend lower as the fleet's incremental watt becomes an AI hall sold against neocloud wholesale rather than a reserved CPU instance on a written-off shell, and as the large labs and the more sophisticated enterprises stop paying a hyperscaler to re-rent capacity the hyperscaler itself is buying from CoreWeave, IREN and Nebius. There is no durable reason for a customer to rent from a hyperscaler who is renting from a neocloud; the double mark-up survives only while the neocloud cannot offer identity, storage, networking and a managed inference and training platform on the same metal, and that bare hour is the current CoreWeave and IREN product, not the product Nebius inherited. As that stack is sold as IaaS and PaaS rather than as a GPU-hour, and as the name acquires the compliance and procurement credibility that today still routes traditional Azure and GCP customers through a hyperscaler logo, Nebius's EBIT per gigawatt should rise from the wholesale band toward the restated hyperscaler figure, and the two lines meet because the hyperscaler's mix is being rewritten from the margin at the same time as Nebius climbs the stack. Other neoclouds can add a control plane, but they cannot, on any near-term clock, recreate the Yandex-origin managed services, MLOps and inference platform already running on this fleet, which is what makes the disintermediation a Nebius claim rather than a sector-wide one.

## Implied valuation if Nebius emerges as a new hyperscaler

The implied sum of the parts on the commercial cloud today, taking second-quarter annualised operating income at 25× EV/EBIT, in line with the parents' own current multiples, and dividing by the external share of first-quarter 2026 operating-IT load, clusters around $300 billion per energised gigawatt.

| | Ann. cloud OI $bn | External GW | Implied cloud EV at 25× $bn | EV / GW $bn |
|---|---:|---:|---:|---:|
| AWS | 66 | 5.7 | 1,660 | 290 |
| Azure | 54 | 4.4 | 1,350 | 310 |
| Google Cloud | 35 | 2.8 | 880 | 310 |

If Nebius at five energised gigawatts is worth half of that cluster, $150 billion a gigawatt, the implied enterprise value is about $750 billion, which on 425 million fully diluted shares is about $1,770 a share, some 8.5 times the $209 close.

## Competitors fail the ROIC hurdle and are underfunded

Venture markets currently run a lower hurdle than public equity, and they are using that gap to fund a long tail of neoclouds, the cohort Palo Alto Networks chief executive Nikesh Arora had in mind when he said that within two years you will 'be able to buy a neocloud for less than they raise at today', because equity to fund capex only works in a euphoric market. He reserves 'neoscaler' for the names that reach scale, Nebius among them: the venture-backed incrementals compete with Nebius today for power, land and GPU allocation, and they compete on price because an execution-risk and supplier-relationship discount is already visible in prints such as Nscale–Anthropic at $7.30 against the $9–11 Rubin-equivalent of Nebius's signed book, so their ROIC on the same GPU capex is structurally lower than the incumbent's and they will have to tap public equity once the venture cheque is spent. Nebius is not exempt, since even the $10 path is still a $22 billion raise and 32% dilution once the August notes convert; what it has against the tail is a live book, a supplier line and a stack that can be taken to a public market as a going concern rather than as a construction story. Either the public market re-rates the class as a whole, in which case the competitors get funded and Nebius investors are paid the same re-rate on a name that already has the sites, or it does not, in which case the start-ups cannot develop the next campus once venture is tapped out.
