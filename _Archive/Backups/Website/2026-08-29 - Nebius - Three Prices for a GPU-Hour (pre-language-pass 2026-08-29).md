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

Nebius's second-quarter landmarks price the upcoming vintage at $20–25 million of annual contract value per megawatt, one-to-three years, 50–60% prepaid, which at Rubin density is $9–11 per GPU-hour and is the rate we take as the going-forward book. That is above Nscale's $45 billion, six-year Anthropic print at Monarch, which back-solves to about $7.30 if 460 megawatts is IT load at 3.9 kilowatts.

## The upcoming vintage

The live book is still the Microsoft wholesale vintage at about $3.35 per hour and about $12 million per megawatt on roughly 100,000 GPUs and $3.0 billion of annualised revenue, a high origination return on the ~$70,000 Blackwell that was actually spent and a failing return on replacement-cost Blackwell. It is not the price of the next hall. The four second-quarter contracts above $1 billion, signed against late-2026 capacity and hitting the profit and loss in 2027, are disclosed as $20–25 million per megawatt-year; converting that to an hour requires an assumed density, and Rubin at 3.9 kilowatts and about 257,000 GPUs per gigawatt is $8.90–11.10 at 8,760 hours, while GB300 at roughly twice the GPU count per megawatt is $5–7.50. There is still no named Rubin cash rate on a Nebius contract. We take $10 as the working point inside the Rubin-equivalent of the signed band, and we run the build from $8 to $12 so the reader can see where cash and the multiple break.

Nscale–Anthropic is the print the tape has been trying to use as the Rubin clearing price, and it is a different object. $45 billion over six years against ~460 megawatts of Vera Rubin at Monarch is about $16.3 million per megawatt-year and about $7.30 per hour on an IT-load reading. Anthropic filled the hole as the binding offtake and the largest line in Nscale's $51 billion backlog ahead of a September IPO, which is execution and prospectus insurance as much as tokens. Nscale's contract discount likely indicates a higher execution risk and lower ROIC tolerance for the company: lighthouse contracts generally price lower for a new entrant looking to build initial scale, and Microsoft and Google both walked from the same campus. Therefore we do not expect Nscale's pricing to be the market clearing rate for a strong execution pipeline book. 

## EBIT, cash and dilution at $8 to $12

The 2026 plan is guided at 800 megawatts to 1GW of active power. Pennsylvania's first power is end-2027, and the company's own cadence is '>1GW/yr from 2027'. We therefore hold the 2026 book as a persistent ~$2 billion EBIT / ~$4 billion cash-EBITDA line and add one gigawatt a year from 2027, billed at the average of start and end so 2027 is 1.5GW (YE 2GW), five energised gigawatts at YE2030.  Prefunding at the second-quarter new-deal claim is 50% of capex, $23.5 billion per gigawatt, amortised over five years as deferred revenue. Hall cash opex is 30% of revenue; the 2026 book's 50% cash-EBITDA margin already carries about $1.6 billion of unallocated corporate, the gap to a 70% hall margin on $8 billion of ARR, and incremental corporate grows $0.25 billion a year from that base, $1.25 billion in 2031, about 2.8% of 2031 ARR. 

Group EBIT is the $2 billion 2026-book line plus the Rubin stack as those halls age, less the incremental corporate:

| $/GPU-hr | 2027 EBIT $bn | 2028 | 2029 | 2030 | 2031 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $8 | 2.8 | 7.3 | 14.3 | 23.2 | 30.9 |
| $9 | 3.6 | 9.7 | 18.3 | 28.7 | 37.2 |
| $10 | 4.4 | 12.0 | 22.2 | 34.2 | 43.5 |
| $11 | 5.2 | 14.4 | 26.2 | 39.7 | 49.8 |
| $12 | 6.0 | 16.7 | 30.1 | 45.2 | 56.1 |

Prefund steps 50% / 30% / 20% / 10% on each new year of 1GW adds, and the hole each year is filled at a share price that compounds 25% from the $209 close ($261, $327, $408, $510). Organic cash is cash EBITDA of the live book less amortisation of advances already collected less incremental corporate; net build is the next $47 billion sticker less that year's new advance. Dilution is the August 18.1 million converting plus that year's primary, cumulative over 272 million.

| Year | Avg GW billed | EBIT $bn | Organic cash $bn | Prefund | Net build $bn | FCF $bn | Equity $bn | Price | Shares m | Cum FD m | Cum dilution |
| ---: | ------------: | -------: | ---------------: | ------: | ------------: | ------: | ---------: | ----: | -------: | -------: | -----------: |
| 2027 |           1.5 |      4.4 |              9.3 |     50% |          23.5 |   −14.2 |        6.2 |  $261 |       24 |      380 |          15% |
| 2028 |           2.5 |     12.0 |             21.0 |     30% |          32.9 |   −11.9 |       11.9 |  $327 |       36 |      416 |          29% |
| 2029 |           3.5 |     22.2 |             34.2 |     20% |          37.6 |    −3.4 |        3.4 |  $408 |        8 |      425 |          32% |
| 2030 |           4.5 |     34.2 |             48.3 |     10% |          42.3 |    +6.0 |          0 |  $510 |        0 |      425 |          32% |
| 2031 |           5.0 |     43.5 |             55.4 |       — |             0 |   +55.4 |          0 |  $638 |        0 |      425 |          32% |

Same prepay path and price curve across the $8–$12 band. EV today is if-converted at the $209 close, 356 million including the August notes, about $62 billion. Each year's EV/EBIT is ($62 billion / that year's EBIT) × (1 + cumulative dilution to that year).

| $/GPU-hr | Incremental equity $bn | Dilution if converts convert | FD shares m | EV today $bn | 2027 EV/EBIT | 2028 | 2029 | 2030 | 2031 |
| -------: | ---------------------: | ---------------------------: | ----------: | -----------: | -----------: | ---: | ---: | ---: | ---: |
|       $8 |                     41 |                          50% |         474 |           62 |          26× |  12× | 6.3× | 4.0× | 3.0× |
|       $9 |                     29 |                          39% |         445 |           62 |          20× | 8.4× | 4.7× | 3.0× | 2.3× |
|      $10 |                     22 |                          32% |         425 |           62 |          16× | 6.6× | 3.7× | 2.4× | 1.9× |
|      $11 |                     15 |                          25% |         406 |           62 |          14× | 5.4× | 2.9× | 1.9× | 1.6× |
|      $12 |                     12 |                          21% |         396 |           62 |          12× | 4.5× | 2.5× | 1.7× | 1.3× |

## Consensus carries no operating profit before 2029

The published estimates never reach the bottom of our range. Aggregated at the same $209 close, the street has Nebius EBIT-negative through 2027 and topping out at $5.7 billion in 2030 on a $3.8 to $8.6 billion band, against $23.2 billion on our $8 floor and $34.2 billion at $10.

| Consensus FY | Revenue avg $bn (low / high) | EBIT low $bn | EBIT avg | EBIT high | Ours at $10 |
| -----------: | ---------------------------: | -----------: | -------: | --------: | ----------: |
|         2026 |           3.35 (3.31 / 3.38) |        −0.72 |    −0.48 |     −0.32 |         n/a |
|         2027 |         11.92 (8.12 / 17.19) |        −1.22 |    −0.75 |     −0.39 |         4.4 |
|         2028 |        22.15 (16.25 / 30.54) |        +0.16 |    +0.24 |     +0.34 |        12.0 |
|         2029 |        40.90 (30.00 / 56.39) |        +1.64 |    +2.49 |     +3.71 |        22.2 |
|         2030 |        57.94 (42.50 / 79.88) |        +3.76 |    +5.75 |     +8.57 |        34.2 |

## EBIT per gigawatt against the hyperscalers

A $10 Rubin gigawatt earns $6-9 billion per annum, against Amazon, Microsoft and Google at about $10.7 / $9.9 / $7.5 billion of cloud operating income per *total* operating-IT gigawatt on the first-quarter 2026 loads of 6.2 / 5.4 / 4.7 gigawatts, and about $12 / $13 / $13 billion once first-party load is stripped out of the denominator.

The discount is wholesale pricing and mix, not worse silicon. Nebius sells take-or-pay GPU-hours to a handful of labs and hyperscalers; AWS, Azure and Google Cloud sell a depreciated blend of reserved IaaS, enterprise agreements, Workspace-class SaaS and a GPU-hall slice, and they have twenty years of already-written-off shells plus the traditional CPU workloads (search, productivity, e-commerce, media) that still fill a minority of the halls and a majority of the historical depreciation base. A new Foxconn-sticker AI gigawatt inside Amazon would print Nebius year one, $5.3 billion at $10, not Amazon's $12 billion external-adjusted blend. The gap that remains after that restatement is the software and services layer sitting on top of the metal, which is the thing Nebius does not yet bill at scale and the thing the Yandex inheritance (managed services, an inference platform, MLOps) exists to become.

That gap should close on two clocks that are already running. Incremental IT load across the industry is almost fully AI: the watts being added in 2026–28 are accelerator halls, not the next generation of search or Exchange, so the hyperscaler's mix is being rewritten from the margin toward the thing Nebius already sells, and the traditional-workload ballast that supports today's $12–13 billion of operating income per external gigawatt is a shrinking share of the live fleet. At the same time Nebius is not stuck as a bare-metal renter. The software stack it built rather than bought is the one credible exception to the sector's 'no operator has differentiated technology' rule, and as that stack is sold as managed compute, storage and networking rather than as a GPU-hour, the wholesale discount relative to Azure and GCP is the thing being closed, not a permanent feature of the layer. Convergence is not year-one arithmetic and it is not a claim that a neocloud becomes a hyperscaler by stacking Rubin; it is the claim that a fleet whose incremental watts are AI, billed with a services layer on top, should not trade as a permanent discount to the external-adjusted cloud gigawatt once the 2026 book has been depreciated through and the 2027–29 halls are the company. The 2028–29 multiple at $10, 6.6× then 3.7× after (1 + dilution), is the market's refusal to underwrite that convergence. The Q3 active-power print is whether the 2026 gigawatt exists to converge from.

We expect hyperscaler operating income per gigawatt to trend lower as the fleet's incremental watt is an AI hall sold against neocloud wholesale rather than a reserved CPU instance on a written-off shell, and as the large labs and the more sophisticated enterprises stop paying a hyperscaler to re-rent capacity the hyperscaler itself is buying from CoreWeave, IREN and Nebius. There is no durable reason for a customer to rent from a hyperscaler who is renting from a neocloud: the double mark-up survives only while the neocloud cannot offer identity, storage, networking and a managed inference and training platform on the same metal, which is the current CoreWeave and IREN product and is not the product Nebius inherited. As that stack is sold as IaaS and PaaS rather than as a GPU-hour, and as the name acquires the compliance and procurement credibility that today still routes traditional Azure and GCP customers through a hyperscaler logo, Nebius's EBIT per gigawatt should rise from the wholesale $5–9 billion band toward the restated hyperscaler $12–13 billion, and the two lines meet because the hyperscaler's mix is being rewritten from the margin at the same time as Nebius climbs the stack. Other neoclouds can add a control plane; they cannot, on any near-term clock, recreate the Yandex-origin managed services, MLOps and inference platform that is already running on this fleet, which is why the disintermediation is a Nebius claim and not a sector-wide one.

## Implied valuation if Nebius emerges as a new hyperscaler 

The implied sum of the parts on the commercial cloud today, taking second-quarter annualised operating income at 25× EV/EBIT, in line with the parents' own current multiples, and dividing by the external share of first-quarter 2026 operating-IT load, clusters around $300 billion per energised gigawatt.

| | Ann. cloud OI $bn | External GW | Implied cloud EV at 25× $bn | EV / GW $bn |
|---|---:|---:|---:|---:|
| AWS | 66 | 5.7 | 1,660 | 290 |
| Azure | 54 | 4.4 | 1,350 | 310 |
| Google Cloud | 35 | 2.8 | 880 | 310 |

If Nebius at five energised gigawatts is worth 50% of that cluster, the implied enterprise value is about $750 billion, $150 billion a gigawatt. On 425 million fully diluted that is about $1,770 a share, $1,560 of upside from the $209 close, 8.5 times.

## Competitors fail ROIC hurdle and are underfunded

Venture markets currently run a lower hurdle than public equity, and they are using that gap to fund a long tail of neoclouds, the cohort Palo Alto Networks chief executive Nikesh Arora said you will, in two years, 'be able to buy a neocloud for less than they raise at today', because equity to fund capex only works in a euphoric market. He reserves 'neoscaler' for the names that reach scale, Nebius among them: the venture-backed incrementals compete with Nebius today for power, land and GPU allocation, and they compete on price because an execution-risk and supplier-relationship discount is already visible in prints such as Nscale–Anthropic at $7.30 against the $9–11 Rubin-equivalent of Nebius's signed book, so their ROIC is structurally lower than the incumbent's on the same GPU capex. As such they will have to tap public equity once the venture cheque is spent. Nebius is not exempt: at $10 with 1.5GW billed in 2027 the stepped-prefund path is still a $22 billion raise, 32% dilution if the August notes convert. What it does have, against the tail, is a live book, a supplier line and a stack that can be taken to a public market as a going concern rather than as a construction story. Either the public market re-rates the class as a whole, in which case the competitors get funded and Nebius investors are paid the same re-rate on a name that already has the sites, or it does not, in which case the start-ups cannot develop the next campus once venture is tapped out.
