---
snapshot_of: "[[Website/2026-08-22 - Neoclouds - The Property Developers of Compute]]"
snapshot_date: 2026-08-26
snapshot_trigger: manual-edit
snapshot_batch: manual-edit-2026-08-26-125856
date: 2026-08-22
tags:
  - essay
  - investment-case
  - laniakea-partners
  - neoclouds
  - artificial-intelligence
  - datacenters
  - NBIS
status: draft
audience: intermediate
source_note:
  - "[[Theses/NBIS - Nebius Group]]"
  - "[[Sectors/Neoclouds & GPU-as-a-Service]]"
  - "[[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]"
  - "[[Research/2026-08-13 - NBIS CRWV - Economics of a Neocloud Unit Model - deep-dive]]"
  - "[[Research/2026-08-13 - NBIS NVDA - Nebius Q2 5GW Power Target - news]]"
  - "[[Mental Models/Generalist - Overview]]"
  - "[[Mental Models/Lens - Value Layer Monopoly]]"
source: internal synthesis
---

# Nebius: The emergence of new cloud giants

**Google pays SpaceX roughly $920 million a month for capacity on the xAI Colossus 2 campus, a rate that returns the entire cost of the datacenter in under a year.** The arithmetic is short: $920 million across roughly 110,000 GB200-class GPUs works out to about $11.60 per GPU-hour, and dropped onto a 100MW build costing near $5 billion, the gross cash comes back before the first anniversary. That deal was struck in a famine, at a price even its promoters concede was generous; normalise the rate toward $6 and the payback stretches to about two years. Even two years would rank among the fastest capital recoveries heavy infrastructure has ever printed. Businesses that recover their capital that fast either own extraordinary technology or sit inside an extraordinary shortage, and the neoclouds, on any honest reading, own no technology at all. CoreWeave, Nebius, Lambda, Crusoe and Nscale all run the same Nvidia reference architecture, the same InfiniBand or Spectrum-X fabric, the same liquid-cooled racks. The market resolves this contradiction by treating the returns as a temporary spike on a commodity business and refusing to capitalise them, which is why Nebius, the fastest-growing infrastructure franchise in public markets, can be bought today for roughly five to six times the operating earnings its contracted book produces in 2028–29.

We think the market has the business model wrong, and that the right comparison sits in one of the oldest industries there is. A neocloud is a property development firm. Once the category is correct, both the returns and the multiple start to make sense, and the question becomes whether the conditions that produce the returns are a cycle or a state.

## Coordination is the product

A property developer also owns no technology. Its inputs all belong to other people: land from owners who must be optioned years ahead, money from capital markets that must be raised against presales, permission from planners and local government, tolerance from the community that will live beside the site, tenants who must sign before the foundations are poured, and contractors and labour who must arrive in the right order at the right price. The finished building is almost incidental; any competent builder can pour the concrete. What the developer actually sells is the elimination of sequencing failure across a dozen counterparties who do not answer to each other, and its margin is the spread between the cost of assembling those pieces without a hiccup and the value of the stabilised, tenanted asset. The firms that do this repeatedly, across cities and planning regimes, compound a reputation that becomes its own source of terms: banks lend cheaper against their presales, landowners option to them first, anchor tenants sign with them because the building will actually open.

The datacenter developer is the special case of this model in which two of the inputs are rationed rather than priced. Grid connections in tier-1 markets now carry 24–48 month queues, so a power contract secured in 2023 is an asset no amount of 2026 money can replicate. And the equipment that fills the shell is allocated by a single vendor, Nvidia, whose decision about who receives GPUs functions as the industry's planning permission. Preferential access to power and to compute equipment is thus the essence of the neocloud's alpha; everything else in the stack can be bought.

| Development function | Property developer | Neocloud |
|---|---|---|
| Land bank | Plots optioned ahead of planning | Contracted power pipeline (Nebius: ~4.5GW at Q2 2026, >75% owned, 5GW year-end target) |
| Planning permission | Zoning, permits, community consent | Interconnect queue (24–48 months), permitting, behind-the-meter generation |
| Presales | Off-plan deposits fund construction | Customer prepayments (~70% of Nebius Q2 deals prepaid, covering 50–60% of associated capex) |
| Anchor tenant | Department store signed before the mall is built | Microsoft ~$17.4–19.4B (~$7B prepaid); Meta $27B on take-or-pay terms |
| Construction finance | Bank debt drawn against presales | GPU-collateralised term loans (CoreWeave, SOFR+450) or contract-secured facilities (Nebius, $775M at SOFR+2.50) |
| Scarce input | Prime land | Nvidia allocation; energised megawatts |

The table understates one asymmetry. A residential developer's presale deposit is a fraction of the unit price; a neocloud's anchor customers now pay half the construction cost up front, before a rack is installed, on contracts running to 2031. When the tenant funds the building, the developer's own capital works twice as hard, which is where the return numbers below come from.

## Low barriers to entry, high barriers to repetition

The commodity critique of the neoclouds is true as far as it goes. Anyone can buy GPUs and rack them; hundreds of small operators do, and the sub-scale end of the market (spot aggregators renting H100s by the hour) behaves exactly like the commodity it is. What the critique misses is that nothing about racking one cluster scales into delivering forty. The business at contract scale is the continuous, simultaneous coordination of land acquisition, grid applications, substation construction, prefabricated shell capacity, transformer and switchgear queues, GPU allocation timing, ODM production slots, network fabric delivery, commissioning crews, and customer acceptance testing, repeated across sites, geographies and regulatory environments that share none of their bottlenecks. A missed transformer delivery in Pennsylvania does not delay a Finnish hall, but a missed Nvidia allocation window delays both, and a contract written against either slips its revenue start date while the prepayment clock runs.

That coordination efficacy is measurable in exactly one place: the efficiency of capital. Time-to-energisation is the whole profit and loss statement when capacity is presold on take-or-pay terms (the customer pays whether or not it uses the hours), because every quarter between capital deployed and megawatts billing is pure return erosion. The operators who compress that interval earn a structurally higher return on identical hardware, and the advantage compounds: higher realised returns let the stronger developer outbid less experienced rivals for the scarce inputs, and the providers of those inputs, the landowners, the utilities, the labour market for commissioning engineers, and above all Nvidia, prefer the counterparty whose projects finish. In a scarcity environment the preference hardens into exclusion. A hyperscaler signing a $10 billion take-or-pay contract will not hand it to a second-rate developer to save two dollars an hour, because execution failure by any component actor in the chain (the vault's supply-chain work found the choke can sit as low as ODM working capital and the concentration of the Taiwanese bank group financing it) produces delayed energisation, delayed revenue, and, for a levered counterparty, bankruptcy. Scarcity does to development what yield-sensitivity does to semiconductor supply chains: it converts the qualification into the moat.

Nvidia's equity programme should be read in this light. The $100 million CoreWeave investment in 2023 with most-favoured-nation GPU access, the $2 billion each into CoreWeave, Nebius and Nscale since, and the ~$40 billion portfolio overall are the industry's completion track record made explicit: operators Nvidia backs are credentialed to bid for hyperscaler-scale contracts, and operators it does not back cannot acquire enough silicon to try. Capital, the input assumed to gate entry, is the abundant one: $5–10 billion project facilities are available to any operator with creditworthy offtake. The gate is the pair of rationed inputs, which flow toward demonstrated coordinators, a list that at gigawatt scale currently carries about five names.

## An industry created by a missing ingredient

The obvious objection is that the world's best datacenter developers already exist and are called hyperscalers. It is correct. Microsoft, Google and Amazon have built more datacenter capacity than everyone else combined, at a lower cost of capital and with two decades of site-development experience; supplier disclosures show neoclouds paying an urgency premium of roughly 38–42% gross margin on power and cooling equipment against a ~35% hyperscaler blend, which is what being the less experienced, more desperate buyer costs. On every traditional axis of the development trade, the CSPs win.

They are missing one ingredient. From late 2022, when ChatGPT created a GPU shortage the hyperscalers could not absorb, Nvidia began allocating silicon directly to non-hyperscaler operators, deliberately, to fragment the cloud layer, broaden its own customer base, and cap the bargaining power of the three buyers who would otherwise corner it. The policy has been remarkably consistent: allocation priority and equity for the neoclouds, public praise for their speed, and a growing roster of them (five majors and a sovereign tail) bidding against each other and against the CSPs for the same chips. The result is an industry-scale arbitrage: the most competent developers of datacenters have empty halls they cannot fill on allocation terms they would like, while a set of five-year-old firms hold the silicon and learn the development trade with hyperscaler money. Microsoft's $60 billion-plus of neocloud commitments and Meta's $27 billion Nebius contract are what it looks like when the incumbent rents from the entrant.

As long as that allocation policy holds, the neoclouds occupy a protected wedge with an unusual property: the wedge trains them to become what they bill. Nebius is the clearest case, because its Yandex inheritance means it ships the software layer (managed services, an inference platform, MLOps tooling) that CoreWeave had to buy for $1.7 billion and the rest lack entirely; a firm renting GPU-hours to Microsoft while operating its own full cloud stack is a CSP in gestation, growing on its future competitors' capex. The wedge is rented, and we return to that in the risk ledger below. But rented positions can be long ones: the supplier's incentive to keep its largest customers from consolidating the cloud layer does not expire with this GPU generation, and every year it persists, the developers' coordination franchise and customer relationships compound into something the policy no longer has to protect.

## What the development math earns

The unit economics, on our fleet model of the Rubin generation (all-in cost ~$183,000 per GPU, ~$47 billion per gigawatt, seven-year life, contracted take-or-pay; operating costs charged at a flat 30% of revenue, which runs two to four times the bottom-up cost stack of electricity, maintenance and component replacement, so every cash figure below is conservative):

| Cash rate ($/GPU-hr) | Cash EBITDA per GPU per year | Gross payback | Payback on Nebius's ~60% funded share | Lifetime EBIT | Pre-tax ROIC |
|---:|---:|---:|---:|---:|---:|
| $9 | $55K | 3.3 yrs | 2.0 yrs | $175K | 13.7% |
| $12 | $74K | 2.5 yrs | 1.5 yrs | $282K | 22% |
| $15 | $92K | 2.0 yrs | 1.2 yrs | $389K | 30% |
| $18 | $110K | 1.7 yrs | 1.0 yr | $496K | 39% |

What the table says:

- **Payback of two and a half years; lifetime ROIC of 22%.** At $12 an hour the fleet returns roughly 40% of its cost in cash each year, and after the machine's full cost is charged over the seven-year life, the average accounting return on the original investment is 22%.
- **Nebius's own money does better than the headline.** Customers prepay half the cost of the build on most new deals, so Nebius deploys roughly 60 cents of each capex dollar. Its own capital comes back in about eighteen months to two years, and the return on that capital runs about 1.6 times the table.
- **The conservative case still clears the bar.** Even at $9, the bottom of the contracted range, the fleet earns an 18.4% IRR against a 15% infrastructure hurdle; returns fall below the hurdle only under roughly $8.20. Nebius's four new contracts from Q2 2026 price at the equivalent of $9–11 per GPU-hour: famine froth removed, still above the bar, prepayments on top.
- **The asset lives longer than the accounting.** The shell, substation and power contract are decades-long infrastructure, and the silicon keeps earning past its write-off: A100 GPUs bought in 2020 still rent for $1–2 per hour six years later. The xAI Colossus deal is the famine extreme of the same model, sub-one-year payback, when a desperate buyer meets the only developer with slots.

The contract is the other half of the story. The identical fleet run without one, selling by the hour at open-market rates, earns 9–10% and misses the hurdle, because merchant GPU pricing decays every time Nvidia launches a faster generation. A five-year take-or-pay agreement freezes the launch rate through the richest years of the asset's life and hands that repricing risk to the customer; that single clause is worth roughly $160K per GPU, more than the fleet's entire margin over the hurdle. And launch-rate paper is only offered to developers with a completion record, credentialed Nvidia allocation and a bankable balance sheet, which is why identical hardware earns commodity returns in unproven hands and franchise returns in proven ones.

What a Rubin hour should cost against a Blackwell hour is the final consistency check, because the rates in the table are only aggressive if the customer is overpaying. Rubin ships roughly 1.6 times the BF16 training throughput and about three times the FP8 inference throughput of the $6 Blackwell hour it competes with, on a rack costing roughly twice as much, so generational fair value against Blackwell spans $9.60 on pure training arithmetic to $18 on pure inference arithmetic:

| $/GPU-hr | What the price marks |
|---:|---|
| ~$8.20 | 15% IRR on a newly built Rubin watt; the deployment floor |
| $9.60 | Customer indifference vs $6 Blackwell on BF16 training throughput |
| ~$10.60 | Revenue-per-watt parity with a $6 Blackwell fleet |
| $12 | The contracted anchor: 22% ROIC, 2.5-year gross payback |
| ~$13.75 | Rate at which replacing a live $6 Blackwell slot with Rubin pays |
| $18 | Customer indifference vs $6 Blackwell on FP8 inference throughput |

A $12 contract sits in the sharing zone of that ladder: the operator clears its hurdle with room to spare while an inference-weighted customer cuts its cost per token by up to a third against renting Blackwell, before counting the wall-clock value of finishing the same job on fewer, faster GPUs. The generational surplus is split rather than extracted, which is the strongest argument that rates near twice the prior generation are an equilibrium price and not a famine artefact: every generation that widens tokens per dollar re-arms the ceiling under which the next contract is written. On pure BF16 arithmetic $12 does exceed the $9.60 parity point, so the paper being signed prices inference throughput and guaranteed availability rather than spot-training parity; in a rationed market the cheap Blackwell alternative is sold out, and the realistic counterfactual to a Rubin contract is unserved demand.

## The multiple the market will not pay

Set those returns against the price. On our modelled calendar earnings for Nebius's disclosed fleet and pipeline (Blackwell base plus the contracted Rubin tranches, seven-year life), today's ~$64 billion enterprise value pays:

| Cash rate ($/GPU-hr) | 2027 EV/EBIT | 2028 EV/EBIT | 2029 EV/EBIT |
|---:|---:|---:|---:|
| $9 | ~21× | ~10× | ~7× |
| $12 | ~15× | ~6.5× | ~5× |
| $15 | ~11.5× | ~4.7× | ~4× |
| $18 | ~9.5× | ~3.8× | ~3.2× |

At a $12 cash rate the market is charging roughly five to six and a half times 2028–29 operating earnings for the business described above, nearer four at $15, and roughly three times EBITDA. (The optics say otherwise, ~120x trailing sales, which is why the headline multiple debate never resolves; the spread between 120x backward and 5x forward is simply the build itself.) A multiple that low on earnings that near prices a disbelief: that the rate collapses at renewal, that the megawatts never energise, or that the asset dies young. Identifying which disbelief is wrong is the entire trade.

Our argument is that if none of them is right, the gap is the widest re-rating available in large-cap markets. A two-to-two-and-a-half-year payback at the contracted band is a 40–50% annual cash yield on total capital; the accounting return prints lower because the machine, unlike a building, consumes itself: full depreciation over seven years costs roughly fourteen points of yield a year, and the final two years re-rent below the contracted rate, which averages the life to the 22–30% pre-tax ROIC of the fleet table. Infrastructure with that return profile, secular demand, and a deployment roadmap of more than a gigawatt a year into a 5GW owned power bank (with management guiding above that from 2027) is the pairing every capital-allocation framework hunts, a high return on incremental capital multiplied by a long runway of places to deploy it, and on any standard infrastructure capitalisation that pairing supports an operating multiple of 25–40 times. The re-rating does not require the famine to persist; it requires only that current neocloud economics, take-or-pay contracts at roughly twice the prior generation's cash rate, prove to be the stable equilibrium rather than the spike, and that GPU useful life holds at the seven-to-eight years the resale and re-rental record now supports. 

## What would prove us wrong

The property frame cuts both ways, and we hold the sector's full risk ledger in view; developers earn their most spectacular spreads in the two years before a glut, and levered developers do not survive gluts. The specific falsifiers:

- **The re-rent step.** Our model assumes fleets re-sign at ~55% of the initial rate when first contracts roll, calibrated to H100 re-signs and the A100 plateau. Every datapoint in that record is shortage-vintage. A normalised 2028–29 market landing the step at 35–40% erases the initial-contract advantage, and the first aging-Hopper re-rental prints will say which world we are in.
- **The cash rate.** Below roughly $8.20 per Rubin GPU-hour the fleet destroys value against a 15% hurdle. Nebius's implied wholesale on its older Microsoft paper sits materially below its new-contract pricing; the decisive disclosure is a Rubin cash rate with a coverage percentage attached, and until an operator publishes one, backlog headlines are not evidence.
- **Asset life.** Each assumed year of useful life is worth about $0.78 per hour of rental equivalent. A world that scraps GPUs at five years re-prices every row of every table above. The observed evidence runs the other way, but the evidence is six years old at most.
- **The missing ingredient returns.** The wedge exists at Nvidia's pleasure. Allocation normalising toward the CSPs would remove the reason this industry exists, and hyperscaler silicon (MAIA, MTIA, Trainium, TPU) attacks the same dependency from the demand side on a 2027–2030 timeline; Nebius's two anchor tenants are also the two most motivated in-housers.
- **Counterparty concentration.** Three capex programmes, Microsoft, Meta and OpenAI, underwrite the majority of disclosed neocloud backlog. Every prior infrastructure cycle has featured a 25–30% capex cut by an anchor buyer; interest at 20–25% of revenue has historically marked where levered builders break, and CoreWeave already prints 25.8%. The prepay-funded developer survives that world; the DDTL-funded one may not, and we would rather own the developer the customers fund than the one the leverage funds.
- **The build itself.** Nebius guided active power from ~170MW at the end of 2025 to 800MW–1GW by the end of 2026 and disclosed no active-megawatt figure at all in Q2. A greater-than-fourfold energisation in twelve months has almost no precedent; the November print, and whether it shows at least ~600MW, is the single highest-information datapoint in the sector this year.

## The synthesis

The neocloud complex will be described as a commodity right up until the moment the survivors are described as the next hyperscalers, and the difference between those two descriptions is nothing more than the compounding of coordination advantages the commodity framing cannot see. The market is pricing the neoclouds on the memory of past developer busts (at ~30% short interest), but Nebius has zero leverage today, and the returns we cited are unlevered rather than typical developers holdco leveraged returns.

The market is essentially pricing the neocloud industry as if current pricing will collapse as AI demand is unable to catchup to supply of compute and a glut of unpowered GPUs will sit in cold datacenters in a few years time. This sentiment persists in the midst of sky high valuations and on a concurrent semiconductor shortage, that is likely to last into 2029/30 and potentially still be tight beyond that. 

There is a structural failure in consistency in valuations for the neocloud industry relative to even conservative assessment of AI adoption. We hold Nebius as our highest weight position on a 3 year view.
