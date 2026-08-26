---
date: 2026-08-26
tags:
  - essay
  - investment-case
  - laniakea-partners
  - artificial-intelligence
  - ai-compute
  - token-economics
  - neoclouds
  - datacenters
  - NBIS
status: draft
audience: intermediate
source_note:
  - "[[Macro & Technology/AI Supply-Demand Considerations to 2030]]"
  - "[[Research/2026-07-23 - Vera Rubin NVL72 vs GB200 Inference TCO - deep-dive]]"
  - "[[Research/2026-08-05 - NBIS CRWV - Rubin Fleet Economics - Rate Sensitivity Model - deep-dive]]"
  - "[[Macro & Technology/Sustainability of AI Capex]]"
  - "[[Website/2026-08-22 - Neoclouds - The Property Developers of Compute]]"
  - "[[Mental Models/Generalist - Overview]]"
source: internal synthesis
---

# The token factory: what a gigawatt makes, what it costs, and the hurdle demand has to clear

**A gigawatt of Rubin-class capacity, once its racks are powered, produces roughly ten quadrillion tokens a year in ordinary service and forty at the benchmark limit, about what the whole industry served in a month in mid-2026, and it costs about $6.5 million per megawatt a year to run once the building, the substation, the racks, the networking and the electricity are all charged against it.** Those two numbers, one physical and one financial, are the supply side of AI compute in full, and most of what is argued about the returns on the build can be settled by what they imply. The industry's capacity to make tokens compounds at about 3x a year through 2028; its cost of making them compounds at the rate megawatts are energised, about 40% a year; the gap between the two is an efficiency term that has run at 1.7–2.0x a year on a measured basis. Demand, in dollars, has only to grow at the slower of those two rates for the economics of the compute layer to stay where they are, and it is currently growing at a multiple of the faster one.

## What the factory makes

Token capacity is physical input multiplied by tokens per unit of input, and the physical input is the energised watt. Two gates sit on it. High-bandwidth memory gates what Nvidia can package, and all three memory vendors sold out 2026 and 2027 before either year began, with HBM4 contracts roughly doubling into 2027; power gates what operators can switch on, and that gate is the durable one, because the additions engine is bounded by delivered heavy equipment rather than by permitting: global gas-turbine manufacturing runs 60–70GW a year against 110GW of 2025 orders with slots sold through 2029–30, generator step-up transformers quote 128–144 weeks, and the grid-connected route is effectively closed in PJM while behind-the-meter builds in ERCOT compress land-to-energised to 18–30 months. Realisation runs 50–60% of schedule. Global energised AI capacity was about 19GW at the end of 2025, reaches about 30GW this year, and on the additions the two largest builders themselves guide to (a doubling of their fleets in two years) runs to roughly 60GW by the end of 2028 and 110GW by the end of 2030.

| Supply term | 2026 | 2027 | 2028 | Mechanism |
|---|---|---|---|---|
| Energised AI watts, global | +55–65% | +45–50% | +35–42% | US achievable +14–18 / +20–25 / +28–35 GW a year; Gulf and Asia add ~5 points |
| HBM installed stock | ~×1.6 | +~60% | +~55% | ~×2.5 end-2026 to end-2028; a young fleet, flow-dominated |
| Fleet-average efficiency | ×1.7–2.0 | ×1.7–2.0 | ×1.7–2.0 | new silicon ~2.5x the fleet average on the year's additions; software harvests 1.3–1.4x on the standing fleet |
| **Token capacity** | **~×3** | **~×2.9–3.2** | **~×2.7–3.2** | ×8–12 cumulative end-2026 to end-2028 |

The efficiency term is two-thirds of the growth and carries the widest gap between what vendors market and what independent benchmarks measure. Blackwell was sold as 30x Hopper and benchmarked at about 4x the throughput for 1.7x the power. Rubin's 'ten times lower cost per token' is a comparison against a year-old GB200 software stack at one interactivity point; against the July 2026 GB300 install the same data shows about 2x per megawatt at ordinary interactivity, 4x at 200 tokens a second per user and 5.4x at the 300-token frontier where GB300 can barely serve at all. The fleet-average construction is what matters for supply: the year's additions arrive at roughly 2.5x the fleet average and the standing fleet harvests another 1.3–1.4x from software maturation, which compounds to 1.7–2.0x a year. Chaining the per-generation and software headline numbers would give 7x a year and is the standard double-count. The source of the roughly 2x-per-generation gain is the precision ladder, FP16 to FP8 to FP4 to Rubin's 3.125-bit lookup format; below three or four bits accuracy fails, so after Feynman in 2028 the gain has to come from process node, memory bandwidth, SRAM-first decode and co-packaged optics, and we expect the fleet rate to fade toward 1.4–1.7x in 2029–30.

Put the two together and the factory's output runs from about 8 quadrillion tokens a month in mid-2026 to about 14 at the end of this year, about 100 at the end of 2028 and about 450 at the end of 2030, a ten-fold rise to 2028 and a forty- to fifty-fold rise to 2030. On calendar totals that is roughly 100 quadrillion tokens in 2026 and 4,000 quadrillion in 2030.

What one megawatt makes depends heavily on how fast each user wants their answer, and this 'interactivity tax' is the least understood number in the supply arithmetic. On SemiAnalysis's renormalisation of CoreWeave's Rubin data, a Rubin NVL72 megawatt serves 1.33 million tokens a second at 50 tokens per second per user, the batch end of the curve, and 96,000 at 300 tokens per second per user, the fast tier that latency-sensitive agents demand. That is 42 trillion tokens per megawatt-year at one end and 3 trillion at the other, a fourteen-fold spread on identical hardware. In ordinary service, after 60% utilisation and the penalty for frontier-scale models and long agentic context, a megawatt-year yields on the order of 10 trillion tokens; a gigawatt therefore adds about 10 quadrillion tokens a year, roughly the industry's monthly output in mid-2026.

| Rubin NVL72, per megawatt-year | Batch, 50 tok/s/user | Mid, 135 tok/s/user | Fast tier, 300 tok/s/user |
|---|---:|---:|---:|
| Tokens at full utilisation (benchmark) | 42 trillion | 28 trillion | 3.0 trillion |
| Cost per million output tokens, economic basis | $0.25 | $0.38 | $3.50 |
| Realised, after utilisation and model/context penalty | ~10 trillion at ~$1.05 | ~7 trillion at ~$1.60 | ~0.7 trillion at ~$15 |
| Frontier API revenue on the same megawatt | up to ~$100M a year | | open-weight serving sub-$30M |

## What a token costs to make

The cost side is a bill for a watt, and it has to be built at the rack rather than the accelerator, because the accelerator is a little over half of it. Per Rubin GPU the all-in figure is about $183,000: a rack share of about $118,000 (the GPU packages ~$55,000; HBM4 and LPDDR memory ~$36,000; the Vera CPUs, NVLink switch trays, network cards, compute trays, power shelves and in-rack cooling distribution ~$27,000), about $8,000 of scale-out networking and storage beyond the rack, and about $57,000 of shell, substation, switchgear, UPS and cooling plant. At 3.9 kilowatts of all-in utility power per GPU that is $47 per watt, which is the figure Foxconn quotes per gigawatt for a Rubin build ($47B) and, allowing for the 2026–27 memory surge, reconciles to Epoch's $38B for a GB200 build split 56% servers, 13% network and 30% facility.

Two things follow from the bill. Capex per watt is roughly flat across generations, because shell, power and cooling scale with watts and Nvidia prices each generation to hold system dollars per watt while performance per watt rises (GB300 at $37.4 per watt of marketed IT capex against Vera Rubin at $38.1 despite the jump in power per chip); memory is the one component breaking that into 2027, and the 2028 relief wave takes it back. And electricity, the input that dominates the public conversation, is a small line: at 8.76 kilowatt-hours per watt-year and about $90 a megawatt-hour it is 12% of the running cost, so a doubling of delivered power price adds about 10% to the cost of a token, six weeks of efficiency. Power matters as a gate on quantity, and the price signal of that gate is the GPU-hour, not the electricity bill.

| Per all-in utility watt, Rubin-class | Capex $/W | Life | Accounting $/W-yr | Economic $/W-yr |
|---|---:|---:|---:|---:|
| Accelerators and memory | ~25 | 7 yr | 3.6 | 6.0 |
| Other IT: CPUs, NVLink switches, scale-out network, storage | ~7 | 7 yr | 1.0 | 1.7 |
| Shell, substation, switchgear, UPS, cooling plant | ~15 | 25 yr | 0.6 | 1.65 |
| Electricity | | | 0.8 | 0.8 |
| Maintenance, staff, water, property tax, insurance | | | 0.5 | 0.5 |
| **Total** | **~47** | | **~6.5** | **~10.6** |

The two right-hand columns answer different questions. The accounting basis spreads the principal over the asset's life and is what reported gross margins use; the economic basis charges the principal plus the return the capital has to earn (15% over seven years on the IT, 10% over twenty-five on the shell) and is what decides whether the next fleet should be built. Per GPU that is $20,300 a year against $36,500, and the $16,000 gap is the profit the machine must earn every year to have been worth buying. A longer asset life moves the first number a great deal (a 5.5-year accelerator life gives $8.0 per watt-year) and the second one barely, because a longer life spreads the principal while the return on it keeps accruing.

Charging that bill against the fleet gives the industry's cost of making tokens through 2030. The line below is defined at the physical layer: depreciation of the fleet, amortisation of the shell and power plant, electricity and operating cost; it excludes the rental markup a lab pays a cloud (a transfer inside the industry) and the labs' own research spend.

| | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Installed AI capacity, year-average (GW) | 24 | 37 | 52 | 71 | 96 |
| of which serving inference (50% rising to 70%) | 12 | 20 | 31 | 46 | 67 |
| Token-serving cost, accounting ($B) | 75 | 133 | 203 | 291 | 417 |
| Whole-fleet cost, accounting ($B) | 149 | 241 | 338 | 447 | 595 |
| Whole-fleet cost, economic ($B) | 240 | 385 | 540 | 715 | 950 |
| Tokens served, calendar total (quadrillion) | 100 | 300 | 800 | 1,900 | 4,000 |
| Serving cost per million tokens, accounting | $0.75 | $0.44 | $0.25 | $0.15 | $0.10 |

The serving cost compounds at 53% a year and the whole fleet at 41%, against tokens rising forty-fold and the cost of a token falling seven-fold. The slope of the cost line is the watts line and nothing else; the level is the life assumption. That is the central fact of the supply side: the industry's cost of goods grows with the megawatts it energises, not with the tokens it serves, and the efficiency engine absorbs the difference.

## The hurdle demand has to clear

The compute layer's revenue is rent per watt multiplied by energised watts, and its cost per watt is flat. If compute expenditure across every payer grows at the rate watts energise, about 40% a year and four-fold by 2030, then rent per watt holds, every watt-owner's margin holds, and revenue and operating profit at each of them grow with the gigawatts they switch on. That is the hurdle, and it is worth stating plainly because it is so much lower than the token figures suggest: dollar demand for compute has to compound at about 40% a year, against tokens compounding at 3x, for the current economics of the industry to be consistent.

Who pays that rent is broader than the 'AI revenue' line the market watches. In 2026 the compute layer receives roughly $300–400B: $110–140B funded by end customers (cloud AI services plus the labs' inference compute cost), $50–100B from the hyperscalers' own franchises (ad ranking, search, recommendations, bundled copilots), $100–120B of training paid from raised equity, vendor finance and increasingly the labs' own gross profit, and $25–40B of open-weight, enterprise self-hosted and sovereign serving at the residual rent. Measured AI revenue of about $165B is well under half of it. Every energised watt has a payer, and against $240B of economic cost the layer as a whole earns about 1.4–1.7x its economic rate; a neocloud on new contracted Rubin paper at $9.60–12 per GPU-hour ($21–26M per megawatt-year) earns about 2x its $10.6M economic cost, with a 15% deployment floor at $17.6M, so today's rents carry a cushion of about 25% before the next fleet stops clearing its hurdle.

Set that against the price of the assets. Nebius grows its energised base from about 170MW at the end of 2025 to 800MW–1GW at the end of this year and adds more than a gigawatt a year from 2027 against 5GW of contracted power, so at a held rent its revenue and operating profit compound several times faster than the industry's 40%, and at a $12 cash rate the disclosed fleet (240K Blackwell plus 200K Rubin, about 1.3GW active by the end of 2028, with no further additions modelled) puts its enterprise value at about 6.5x 2028 and 5x 2029 operating earnings; each further gigawatt energised at that rate adds ~$18B of cash EBITDA and ~$8B of first-year operating profit rising to ~$15B by year four, so a gigawatt a year from 2027, if funded, takes the 2030 multiple toward 2–3x. A business whose profits compound at 40% a year on the industry line alone, before its own share gains, priced at five to six times earnings two years out, is a growth-adjusted multiple below 0.2x. The market is paying for a collapse in rent; the hurdle for rent merely to hold is 40% a year of dollar demand.

## Demand is running well above the hurdle

Every measure of demand we track is compounding at a multiple of that rate. In tokens: Google's surface-wide processing went from 9.7 trillion to 480 trillion to 3.2 quadrillion tokens a month across April 2024, May 2025 and May 2026; OpenAI went from 6 billion to 15 billion tokens a minute in five months; OpenRouter's agentic volumes rose 14x in six months; the aggregate runs 5–9x a year. In dollars: Anthropic's run-rate went from $9B to $44B in about a year at an inference gross margin above 70%, which means the labs' compute spend now scales with their revenue and funds training from gross profit rather than from the next equity round; the hyperscalers' 2026 capital plans total about $725B, up 77%; Nvidia's datacenter revenue grew 85%; AWS carries $496B of backlog. Rationing sits underneath all of these prints (rate limits, quota tiers, waitlists), so they understate demand at current prices rather than overstate it.

The penetration numbers say the curve is early. Agentic coding has reached 15–25% of roughly 35 million developers with about a tenth of those intense; enterprise workflow agents are scaling in 2–5% of business functions; autonomous background fleets are below 2%. An agentic seat consumes 50–100 times the tokens of a chat subscription, and it cannot queue: an agent blocked mid-task is a human waiting and the labour arbitrage breaks, so agentic demand leaves the rationing tier and enters the priority-priced one, concentrating on the frontier model where cross-elasticity to cheap substitutes collapses. The gate on enterprise depth is organisational rather than technical, which means adoption compounds for a decade rather than saturating in three years. Our own forecast for 2027 is token demand at 3.5–4.5x against supply at 3x: the overhang widens before it closes.

That is why the economic profile of the compute layer should improve, not deteriorate, for at least the next few years. Scarcity clears in a sequence (training reallocation, internal squeeze, queues, price discrimination, posted price last), so the blended price moves little while the marginal signals move a great deal: the fast-tier to batch spread runs about 4x today and heads toward 8–10x in a famine; the one-year H100 contract index is up 40% from its low; Rubin renewals are being written above launch rates. Each of those lands on the watt-owner as rent per watt rising on the merchant sliver and on every renewal, and the ceiling on that rent is what the customer's tokens are worth, up to $100M per megawatt-year at the frontier against $10.6M of cost, not parity with the previous GPU generation. Eighty to ninety per cent of capacity sits on fixed-price take-or-pay, so the surplus arrives slowly and lands with the labs first; for an operator adding a gigawatt a year, though, new signings and renewals are most of the book by 2028, which is exactly where the surplus lands second.

## What would prove us wrong

- **A token print annualising below 2.5x.** Tokens-per-task compression (Opus 4.5 delivering the same work with 76% fewer output tokens) outrunning penetration would put demand below the supply line even in a strong adoption world.
- **A financing break.** The four payers are correlated, all of them scaling with token revenue, so the hurdle is met only if end-customer AI revenue runs roughly five-fold to about $850B by 2030; a shortfall of a third takes new fleets below the deployment floor, and the first 25–30% capex cut by an anchor buyer is the trigger. Hyperscaler capex crossed above operating cash flow in the third quarter of 2026.
- **Independent Rubin prints at or above 3x per watt at fixed precision.** Supply would leak past the 3x line and the famine would end a year early; independent InferenceX numbers on a modern model are due this quarter.
- **Ageing-Hopper re-rents at 35–40% of launch rather than the 55% the record supports.** That is the digestion print, and it arrives before any change in the token numbers.
- **Nvidia lifting system dollars per watt on the Kyber generation.** The flat cost line breaks, and part of the famine leaks upstream to the silicon layer instead of staying with the watt-owner.

## The synthesis

The supply side of AI compute reduces to a factory whose output compounds at 3x a year and whose cost compounds at 40%, because the cost is a bill for watts and the output is watts multiplied by an efficiency engine. The compute layer earns about 1.4–1.7x its economic cost today, dollar demand has to grow at about 40% a year for that to hold, and every measure of demand is compounding at two to five times that rate while agentic penetration sits in the low single digits to low tens of per cent. The neoclouds are priced as though rent per watt will collapse into the largest shortage the industry has recorded. We think the next few years run the other way, and we hold Nebius as our highest-weight position on a three-year view.
