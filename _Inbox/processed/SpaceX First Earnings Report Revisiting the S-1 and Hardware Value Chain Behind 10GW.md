---
date: 2026-08-10
tags: [research, email-backfill, PhotonCap]
source: 'https://photoncap.net/p/spacexs-first-earnings-report-revisiting'
source_type: web-clip
sender: photoncap@substack.com
---

# SpaceX First Earnings Report Revisiting the S-1 and Hardware Value Chain Behind 10GW

SpaceX, the name that ran so hot, has put out its first earnings since going public. Back in June I read the S-1 and wrote a piece breaking the company down layer by layer, and watching this release, I wanted to pull that piece back out and check it against what I had published. The first quarterly filing carries the judgments I had built on the IPO documents, and it is the first material that lets me check how well my thinking actually held up, so I thought it mattered. And if the 10GW compute outlook from this earnings call becomes real, I thought it also matters which side of data center investment we should be looking from. So this piece runs in two parts. The front half is the work of reviewing the judgments made at S-1 time against the first earnings, and in the back half I try to follow the feasibility of the 10GW outlook and the hardware layers that money will flow into. To note just the direction up front, I read this report less as a space company’s earnings and more as the first quarterly report of an AI infrastructure company, and I expect the benefit to arrive first not at SpaceX shareholders but at the ones receiving the parts orders, or the investors around them.

### Contents

- Quarterly Capex of $18.4B, With $15.8B Going to AI

- Revisiting the S-1, Part 1: Connectivity, the ARPU Decline Has Stopped

- Revisiting the S-1, Part 2: Space, Seven in Ten Launches Were Internal

- Revisiting the S-1, Part 3: The AI Segment and the 90-Day Termination Call

- Rereading the 90-Day Termination Clause: Weakness or Sales Condition

- Is 10GW Real: Power, Money, Skepticism

- The Hardware Bill: Power, Optics, and Scale-Across

- Conclusion, and What Would Prove Me Wrong

## 1. Quarterly Capex of $18.4B, With $15.8B Going to AI

SpaceX’s capex this quarter was $18.4B, and the AI segment’s share of it was a whopping $15.8B [1]. That works out to 86%, and is that a high number or a low one, what would the answer be? Yes, as you probably guessed, it is quite high. A company that builds rockets and satellites put nearly nine tenths of its quarterly investment into AI data centers.

The August 4 release was the first earnings since the red-hot June 12 listing. Revenue came in at $7.8B, up 92% year over year, net loss narrowed to $541M, about half the level of a year ago, and Adjusted EBITDA was $3.5B [1]. Even with revenue beating estimates by nearly $1B, the stock reportedly slid around 8% after hours [2]. The capex caught the eye before the surprise did. It is the same reaction pattern as the four hyperscaler earnings in late July.

Segment results table from the SpaceX Q2 2026 press release

And on the call, Musk named the destination of that capex. Past 2GW of compute by the end of 2026, and by the end of 2027, to a level closer to 10GW than to 5GW [3]. This from a company at 1.4GW nameplate today [1].

There are two things I want to do in this piece today. One is to review the layer-by-layer judgments built on the S-1 in June’s The Largest IPO in History, One Profitable Layer: Where SpaceX Exposure Really Sits, and the Traps against the first earnings. The other is which hardware layer gets the attention if that 10GW number becomes real, or which one we should be paying attention to.

## The Largest IPO in History, One Profitable Layer: Where SpaceX Exposure Really Sits, and the Traps

SpaceX, the largest IPO in history (ticker SPCX, targeting a June 12 Nasdaq debut at a $1.75T valuation), posted a loss in its most recent fiscal year. The analysis uses the S-1 as the primary source and starts from one observation: SpaceX’s extreme vertical integration makes the pool of “supplier beneficiaries” thinner than people assume. From there it splits the upside into four layers ranked by certainty. Two conclusions. The profit and the proof sit in Layer 1 (LEO connectivity, Connectivity revenue $11.4B, 61% of the company), and the AI revenue that anchors part of the $1.75T valuation comes from idle compute that rivals Anthropic ($1.25B/month) and Google ($920M/month) rent, with the Anthropic contract cancellable on 90 days’ notice and the Google contract carrying GPU delivery conditions plus a 90-day termination right after year-end 2026. So the liquid exposure is not direct supply to SpaceX. It sits in dual-use light source and DSP names ($COHR, $LITE, $MRVL), the OISL bottleneck ($RKLB, $CACI), and the AI infrastructure bottleneck (power, CPO, cooling, $NVDA).

## 2. Revisiting the S-1, Part 1: Connectivity, the ARPU Decline Has Stopped

In the June piece I classified Starlink as SpaceX’s only profitable engine, while also writing down as a risk the pricing pressure that had pushed ARPU from $99 to $81 on an annual basis, and down to $66 on a quarterly basis.

Layering the first earnings on top of that, it looks like this. Connectivity revenue was $4.3B, up 66% year over year, operating income $1.7B, up 79%, and subscribers doubled in a year to 12 million [1]. And ARPU held at $66, flat with the prior quarter [1]. There was reporting in May of an attempted price increase, and at least this quarter, the picture that came out was doubling subscribers while thankfully holding the unit price. There is also a side growing faster than consumer. Enterprise & Government revenue grew 108% year over year, and the filing also includes over $6B in multi-year US government contracts won through Starshield [1].

The result of a quick review is that I keep the judgment that the company still has its profitable engine. That said, the decline stopping and the price rising again are different stories. That it stopped at $66 is as far as this quarter’s facts go, and whether this price increase actually shows up in ARPU has to be checked precisely against next quarter’s numbers.

## 3. Revisiting the S-1, Part 2: Space, Seven in Ten Launches Were Internal

The S-1 contained the language that “to meet our orbital compute goals, we may prioritize our own payloads ahead of US government contracts or third-party customers” [4]. At the time I wrote, based on that language, that the upside for outside listed names in the launch layer was narrow. The first quarter’s numbers show that language in action. Of 38 launches in the quarter, 28 were internal, and of 485 metric tons put into orbit, nearly 400 tons were internal payloads [1]. More than seven in ten launches went to lifting its own satellites, that is, Starlink satellites.

Space revenue grew 29% year over year to $962M, yet the operating loss was $542M [1]. Starship R&D is booked at around $1.1B for the quarter. Flight 12 in May and Flight 13 in July hit their objectives back to back, and Flight 13 reportedly went as far as deploying 20 production V3 satellites [1], so the nature of this loss is closer to deployment speed than failure cost. There is nothing to change in the June judgment on the launch layer.

## 4. Revisiting the S-1, Part 3: The AI Segment and the 90-Day Termination Call

Now for the main part of this piece. In the June piece I attached a warning to the AI revenue line. The Anthropic contract at $1.25B a month and the Google contract at $920M a month sit at the center of the AI revenue story, but both can be ended on 90 days’ notice, so the headline contract sizes should not be taken at face value. That was the warning [4][5].

In the first earnings, AI revenue was $2.56B, 3.5x year over year. Of that, AI solutions & infrastructure was $2.19B, up more than 4x in a single quarter from $475M [1]. The Anthropic ramp was scheduled across May and June, so the timing lines up. Compute capacity stood at 1.4GW nameplate, up from 1.0GW the prior quarter [1].

But what caught my eye first in this filing was not the revenue number but a definition tucked into the back of the release. SpaceX announced the Cloud Services Agreements newly signed this quarter as $14.1B in contracted sales, and in Note 2 it spelled out how it counts that number. It does not count the full amount written into the contract, only the revenue from the period that cannot be cancelled [1]. Meaning that for a contract that can be ended on 90 days’ notice, even if three years of value is written on paper, only the non-cancellable first few months land in contracted sales. The $45B and $30B deal values the press quotes add up the entire contract term, while the number the company officially tallies counts only the locked-in piece. This is exactly the point I made in June. That as long as the 90-day clause is there, the headline totals should not be taken at face value. With this filing, the company effectively discounted the number that way itself.

Contracted sales definition language in Note 2 of the press release

Up to this point, you could say PhotonCap’s June call was more or less right. But there is a flipped half to this observation. That the 90-day clause may be, rather than a weakness, the very condition that makes this business sell so well. That is where we pick up below.

## 5. Rereading the 90-Day Termination Clause: Weakness or Sales Condition

Start with the speed at which contracts are stacking up. Cloud Services Agreements signed during the quarter came to $14.1B, and the CFO reportedly said another $6.7B was contracted within the first weeks of Q3, with that volume ramping from October [6]. A number tallied under the conservative definition, with cancellable portions stripped out, is growing at this speed. The Google volume also starts in October by contract [5], so the second-half AI revenue line has a queue of already-signed contracts waiting to ramp.

Why does it stack up this fast? I have come to see the 90-day termination clause as half of the answer. From the buyer’s side, a contract you can walk out of on 90 days’ notice puts no long-term debt-like commitment on the balance sheet. The weight of the signature is different from a 15-year take-or-pay data center contract. In a compute-short period, if there is a supplier handing over large-scale capacity within 3-5 months and the contract risk is capped at 90 days, the buyer’s approval threshold drops sharply. SemiAnalysis, on the basis of this structure, observes that SpaceX is selling compute above market at $30-50M per MW per year [7]. In the June piece I read this clause only as a weakness in revenue durability, and I missed the other face of it, a sales condition that creates velocity and pricing.

This setup is an extension of last week’s The GPU Repricing Cycle and Q2 Hyperscaler Earnings: Which Hardware Layer the Capex Flows To. To borrow that piece’s landlord analogy, the hyperscalers are landlords rolling old fixed-rate leases up to market, while SpaceX is a landlord that has only ever rented month to month. The shorter the contract term, the faster market rates flow through, and right now market rates sit above contract rates.

On profitability too, a positive number showed up for the first time. AI Segment Adjusted EBITDA came in at $1.1B, swinging from negative $609M the prior quarter [1]. That said, this number is hard to take at face value. It adds back $1.9B of depreciation, so the operating loss is still $1.3B [1], and the $15.8B of capex going in every quarter will come back as depreciation over the next several years. This is the stretch where equipment is bought up front and the cost is recognized later, so reading the EBITDA turn as proof of profitability is early. What I see as valid is the direction. That rental revenue has started to clear cash costs, and that this happened before the contract ramps even kicked in fully.

That ran long, so to pull the review together: the point that headlines should be discounted because of the 90-day clause was confirmed by the company’s own disclosure, and what this quarter newly confirmed is that the clause, instead of cutting revenue durability, is lifting revenue velocity and pricing. The durability warning itself stays. A structure where contracts stack up fast is also a structure where they can drain fast.

## 6. Is 10GW Real: Power, Money, Skepticism

One exchange on the call is the starting point of this section. Morgan Stanley’s Adam Jonas asked about line of sight on permitting, chips, and turbines, and Musk’s answer went like this. Close to 10GW of nameplate compute by the end of 2027, and at the power and cooling equipment level, a tentative target of 20GW, though in practice it will land near 15GW [3]. What stands out is that he split the power plant level number from the compute level number. Stack cooling and margin on top of IT load and power equipment always has to be larger than compute, so at least the number system is an engineer’s.

Even so, the market’s base expectation leans toward hard. The stock sliding despite an earnings beat is itself that temperature [2], and the reality on the power side is no small thing either. The deadline to fully remove the 69 unpermitted gas turbines running at the Colossus site has slipped to July 2027, and the 1.2GW permanent plant replacing them, a 41-turbine configuration, is reportedly under construction with Mississippi state permits [8]. A lawsuit from the NAACP and environmental groups is pending, and the Justice Department has sided with the company on national security grounds [8]. Even now, running 1.4GW, power is this noisy, and the target is to stand up seven times that within two years.

Satellite map of the Southaven area, Colossus and nearby candidate sites

In the June 30 piece I put up the gap between Musk’s 1GW claim and the roughly 350MW of cooling observed in satellite imagery as a monitoring point. This filing narrowed that gap some. With 1.4GW nameplate now a quarterly disclosure item, the company has at least started putting out a number that can be checked on a regular basis [1]. But nameplate is installed capacity, not operating capacity. The fact that the company deliberately picked this word is worth keeping in mind as is.

The case for feasibility has been laid out by SemiAnalysis. Nationwide site surveys, turbine volumes circulating in the secondary market, procurement that routes around the large power transformer backlog with Chinese power modules, that sort of thing [7], and the direction is one. Shortening procurement paths that take others five years, with money and speed. The APR Energy acquisition and the plan to buy $2B of turbines over three years sit on the same line [8].

What about the money? Cash and marketable securities stand at $100B. It raised $85.7B in the IPO and $25B in investment-grade bonds in late June, at a weighted average coupon of 5.855% [1]. A quarterly capex pace of $18.4B is a $70B-plus annual run rate, and if 10GW costs $50B per GW as SemiAnalysis roughly figures, the funding needed is several times that [7]. As a candidate to fill that gap, I look at the Nvidia exclusivity declaration on the call. Musk called Vera Rubin the best AI computer and said the company will use only Nvidia chips [3][9], and for a company that has evaluated TPU and AMD to nail down a single vendor, I think there is a good chance vendor financing negotiations sit in the background. (author estimate)

My judgment is this. The absolute 10GW quantity itself will probably slip. But the reason this company is burning big money is clear. Even counting only the cancellable portion, more than $20B of contracts stacked up in half a year, and the fact that buyers are lining up for compute as fast as it gets built is this quarter’s measurement. In a market where it is confirmed that whatever gets built gets sold, burning money on build speed is closer to arithmetic than to gambling.

## 7. The Hardware Bill: Power, Optics, and Scale-Across

So let’s follow, layer by layer, where that bill actually lands.

Power is the biggest axis. Taking Musk’s 15-20GW power plant level number as given, that means standing up the power equipment of 15 to 20 nuclear reactors within two years. New large gas turbines are backlogged years out at the major suppliers, so secondary market turbines, small and mid-size turbines and engines, onsite generation packages, and power modules sell first [7][8]. Demand in this layer does not end with SpaceX alone. The hyperscalers are in the same procurement race, so the turbine and generation equipment value chain is one of the clearest seller’s markets of this cycle.

Optics follows in proportion to GPU count. Pulling back out the conversion ladder from the June 30 piece, on a GB300 NVL72 basis, each GPU carries one 800G-class scale-out connection [10]. Taking 135kW per rack and rough-converting 10GW nameplate, GPUs land in the millions (author estimate), and leaf-level scale-out ports grow in the same order of magnitude. Add the spine and super-spine tiers and optical transceiver endpoints become a multiple of that. And of course the related switches will see demand as well. The detailed conversion is written up in SpaceX Started Renting Out Compute. The Rig Demand Is Now Written Into the Contract.

And the thing I am really watching these days is scale-across. Can a single site carry 10GW? I doubt it. Colossus 1 and 2, the Southaven plant, new-build shells, and the retrofit sites SemiAnalysis flags as candidates [7], this buildout is split across multiple campuses from the start. Once campuses split, the DCI linking them becomes part of compute performance. From the moment a training job crosses a site boundary, coherent optics and long-haul transmission gear matter as much as the network inside the cluster, and this structure is the same one I drew in July in One Layer Below SemiAnalysis’s Meta Map: Scale-Across Is Coherent, Not CPO around Meta’s multi-campus buildout. The picture drawn for Meta is repeating at SpaceX. Personally, these days, I am paying deep attention to scale-across.

Brought down to the ticker level, it goes like this.

- Coherent DSP and optical components: Marvell ($MRVL) is the DSP axis, Coherent ($COHR) and Lumentum ($LITE) the optical component axis. These three are the same lineup classified as dual-use crossover names in the June piece, and with scale-across attached, they gain one more exposure path.

- Long-haul transmission systems: Ciena ($CIEN) is the DCI systems axis. As campus dispersion progresses, this is the layer where demand grows as a function of distance and bandwidth between campuses rather than cluster count.

- Memory: millions of GPUs bring HBM along at the same scale. The L3 memory argument from last week’s piece applies to this layer as is, and the pure exposure is Micron ($MU). But this layer is a function of the whole cycle more than a SpaceX-specific benefit, so it should not be bought on a SpaceX frame but viewed on a capex cycle frame.

- Optical field validation and test: millions of ports mean millions of validation events at install and in operation. As covered in the June 30 piece, this layer’s beta tracks port count multiplied by operational complexity.

Ladder diagram converting 10GW nameplate into GPUs, scale-out ports, and DCI

One limitation is worth writing down. The conversions above are all rough figures based on GB300 NVL72 reference ratios, and nothing has been disclosed yet on the rack configuration and network ratios of the Vera Rubin generation SpaceX will actually deploy in 2027.

## 8. Conclusion, and What Would Prove Me Wrong

The read that SpaceX is less a space company than an AI company has spread across the market, and I think this earnings report supports that read. Of course, an AI company including the space data centers. The spending structure says so. 86% of quarterly investment went to AI, and revenue grew, but investment grew much faster. Follow the reason for burning this much money and it comes down to one thing. The judgment that AI compute demand stays large and the market gets larger, and the fact that whatever gets built gets sold, confirmed in the contracted sales. With even SpaceX now in on that judgment, I think what matters for an investor is mapping where this buildout’s value chain passes through.

However, if year-end compute falls short of the 2GW Musk named, the credibility of the 10GW call has to be recalculated first. If contracted sales growth stalls or the first termination case appears, section 5 of this piece, which reread the 90-day clause as a sales condition, will also need revising. And if AI revenue growth slows even in Q4, when the Google volume and new contracts ramp, the assumptions on pricing and demand have to be questioned.

By the dates, it looks like this. The Google volume and the $6.7B of new contracts start ramping in October [5][6], the Cursor acquisition targets a close within Q3 [1], and the Q3 earnings expected in early November are where the increments in nameplate GW and contracted sales get rechecked. The deadline for fully removing the unpermitted turbines is July 2027 [8]. Including the year-end 2GW checkpoint, this is a call studded with verdict dates.

Personally, the work of matching the judgments I wrote down while reading the S-1 in June against the first earnings was fun in itself. Next earnings season, I plan to dig into the power layer in a separate piece.

## Acknowledgment

The framing of the 10GW feasibility discussion and the power procurement observations (secondary turbine market, candidate sites, procurement workarounds) started from SemiAnalysis’s SpaceX 10GW analysis [7]. What this piece adds is a review grounded in primary data from the S-1 and the first quarterly release, and the conversion into the optics and scale-across layers. All cited figures were verified directly against company disclosures and public reporting.

## References & Sources

[1] SpaceX, “SpaceX Reports Second Quarter 2026 Results”

[2] CNBC, “SpaceX earnings takeaways: Soaring AI costs outweigh revenue beat in first report since IPO”

[3] Yahoo Finance, “Space Exploration Technologies (SPCX) Q2 FY2026 earnings call transcript”

[4] SpaceX (Space Exploration Technologies Corp.), “Form S-1 / S-1/A, File No. 333-296070”, SEC EDGAR, 2026-05-20.

[5] Reuters, “SpaceX signs cloud deal with Google”

[6] Yahoo Finance, “SpaceX Q2 2026 earnings: revenue beats, stock falls after hours”

[7] SemiAnalysis, “SpaceX 10GW in 2027: Why It’s Real, Will Drive $300B ARR for SpaceX, and Why Microsoft Will Be the Largest Offtaker”

[8] TechCrunch, “SpaceX won’t remove all of xAI’s unpermitted turbines for another year”

[9] Yahoo Finance, “Here’s Exactly What Elon Musk Said About Nvidia on the SpaceX Earnings Call”

[10] NVIDIA, “Network Logical Architecture, NVL72 AI Factory Enterprise Reference Architecture”

This article is an independent technical analysis published by PhotonCap, based on an engineering perspective. All content is derived from publicly available information and is intended solely for educational and informational purposes. In other words, nothing in this material should be construed as a recommendation to buy, sell, or hold any specific securities. Please note this carefully.

The author may hold positions in the securities mentioned herein and reserves the right to trade such securities at any time without prior notice. Readers should conduct their own thorough review and research before making any investment decisions.

Share this with anyone who needs to see the world through a different wavelength.

Share
