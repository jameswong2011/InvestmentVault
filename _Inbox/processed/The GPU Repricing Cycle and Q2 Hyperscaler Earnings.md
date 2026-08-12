---
date: 2026-08-06
tags: [research, email-backfill, PhotonCap]
source: 'https://photoncap.net/p/the-gpu-repricing-cycle-and-q2-hyperscaler'
source_type: web-clip
sender: photoncap@substack.com
---

# The GPU Repricing Cycle and Q2 Hyperscaler Earnings

### Abstract

It is already early August, but to look back and think about AI infrastructure investment and the outlook going forward, I went through the hyperscaler earnings from the last week of July, pulled together commentary from various outlets and X, and prepared my own opinion and analysis alongside it. Alphabet, Microsoft, Amazon, and Meta earnings were all packed into the last week of July. I started writing this piece after seeing the Google Cloud +82% number, and as I wrote, it seems half of the piece turned into checking the underearning story Gavin Baker raised first, that is, the observation that GPU spot rental prices are more than 2x contracted prices, against this quarter’s results. The other half is redrawing and checking the cloud capex hardware map I drew in May with data one quarter later. To note just the direction up front, I see this quarter as the early stage where the supply shortage starts getting reflected in prices, and I suspect the place where that money stays longest is the two layers hyperscalers cannot insource.

### Contents

- Backlog at $514B, but the Stock Fell

- When the Lease Runs Out: Baker’s Underearning Thesis

- The Four Hyperscalers’ Results: The Numbers

- The Boundary Public Materials Can Show

- Primary Evidence of Repricing: Usage Above Commitments and Backlog Quality

- The Meta Compute Variable

- May Map Update: Allocation Tilting Toward L3 and L4

- As Efficiency Improves, the Bill Grows

- Conclusion, and the Conditions Under Which I’m Wrong

## 1. Backlog at $514B, but the Stock Fell

In Alphabet’s July 22 earnings, Google Cloud revenue was $24.77B, up +82% year over year [1]. The prior quarter’s growth rate was +63%, so it got even steeper in a single quarter. A company this large accelerating its revenue growth struck me as worth paying attention to. The backlog, contracted but not yet recognized as revenue, stands at $514B, up more than $50B in one quarter [1]. And yet the stock reacted to the earnings release by falling. The company raised capex guidance again, and quarterly free cash flow flipped negative [1].

To borrow the news framing, the books and the stock went in opposite directions.

This combination is the key question of this earnings season. Record demand is piling up on the books, while the market looks first at “the cash being burned to serve that demand.” Which of the two is the right lens?

So the points I want to discuss in this piece come down to two. One is whether the underearning thesis, that hyperscalers are currently selling compute below market rates, is supported by actual earnings data. The other is, if so, which hardware layer the growing cash flow and capex flow into.

## 2. When the Lease Runs Out: Baker’s Underearning Thesis

The starting point of this piece is the argument Gavin Baker of Atreides Management laid out in a recent X post and in his Invest Like the Best interview back in May [2][3][4]. The problem statement is his, and in this piece I put my own thinking alongside it and check that argument against this quarter’s primary data.

> “TL;DR Spot pricing for renting GPU compute materially above contracted rates implies hyperscalers are underearning while operating cash flow acceleration is an underestimated source of funds for AI capex.”…“As contracts roll-off, hyperscale growth rates are going to continue to accelerate as their installed bases of compute reprice higher.”…“Hyperscalers are underearning and anyone who signed a contract for GPU compute in 2024 and 2025 is overearning. Operating cash flow will be enough to fund capex but as contracts reprice and cloud growth continues to accelerate then spreads likely come in as well.”The market may be overreacting to widening hyperscaler credit spreads.If spot GPU rental prices are at least twice contracted rates, hyperscalers are likely underearning relative to the current value of their installed compute. As older contracts roll off and reprice higher, cloud revenue and operating cash flow could accelerate faster than consensus expects, allowing a much larger portion of future AI capex to be funded internally rather than through debt.• Customers that locked in GPU compute during 2024 and 2025 are currently overearning• Contract repricing could reaccelerate hyperscaler growth and operating cash flow• The real constraint may be power and data-center execution, not access to creditThe more important question may not be whether hyperscalers can finance AI infrastructure, but how quickly they can energize the GPUs and convert that capacity into revenue.

The argument goes like this. The price of renting GPU compute on the spot market, that is, on demand without a contract, is at least 2x the long-term contracted price [2]. Since most hyperscaler revenue comes from long-term contracts signed some time ago, they are effectively selling compute for less than half of what they could charge at today’s rates. Baker calls this underearning, meaning earning less than they could.

Think of a rent-stabilized apartment and the structure clicks. During the lease term, no matter how much market rent rises, what the landlord collects is fixed. If market rent doubles, the landlord gets upset, but there is nothing they can do until the lease ends. Instead, when renewal time comes, the accumulated rise in market rates gets reflected all at once. Or the landlord is expected to raise the price. Baker’s claim is that hyperscalers are now landlords sitting on rent-stabilized leases, and the renewal cycle has slowly started to come around.

Contracted rate vs spot rate repricing concept

So his conclusion follows from there. As existing contracts expire and renew at new prices, the hyperscalers’ entire installed base reprices upward, and growth does not just hold, it accelerates. In fact, multiple private companies are reportedly planning to pay more than 2x per GPU after their contracts expire [2]. He modeled combined hyperscaler operating cash flow growth accelerating from 31% in Q1 to 50% in Q2 [2], and this figure is not a measurement but a calculation mixing his estimates with reported results. Of course, I have not been able to recalculate this model, but I looked for a way to verify the direction and checked whether that direction actually holds. I figured we could just look at whether traces of repricing actually showed up in this quarter’s results.

## 3. The Four Hyperscalers’ Results: The Numbers

I summarized everything below based on company announcements.

Alphabet (7/22): Total revenue $119.8B, +24%. Google Cloud $24.77B, +82%, beating consensus by more than $2B. Cloud operating income was $8.8B, about three times a year ago. Backlog $514B, with just over half expected to be recognized as revenue within 24 months [1].

Microsoft (7/29): FY26 Q4 revenue $90B, +18%. Azure +43%, with Azure annual revenue crossing $100B for the first time on a fiscal-year basis (+41%). Commercial RPO $678B [5]. Quarterly capex including finance leases was $41B, +69%, and FY2027 capex guidance was reportedly set at $255~260B [6].

Amazon (7/30): Total revenue $200.6B, +20%. AWS $42.2B, +37%, the fastest growth in 18 quarters, with a 39.4% operating margin. The AI business and the in-house chip business each run above $25B annualized [7]. The 2026 capex outlook was raised from about $200B to about $220B [8].

Meta (7/29): Revenue $60.8B, +28%, beating consensus, with an EPS miss. Full-year capex guidance is $130-145B, narrowed from the prior $125-145B by raising the lower end [9]. The lower end is how they showed they have no intention of cutting. AI infrastructure spend was around $31B in this quarter alone, and free cash flow pressure was the theme of the earnings call [10].

Put the four announcements side by side, and cloud revenue growth is accelerating at all three clouds while all four companies raised capex. Two of them saw their stocks slide on cash flow concerns. (In my view, that makes no sense.) You can read this as a picture where the sellers’ growth is speeding up while the buyers’ spending speeds up at the same time. In a market with surplus supply, I doubt these two would show up together.

That ran long, so to sort it out a bit: the premise of Baker’s thesis, that demand exceeds supply and contracted prices lag market rates, and the shape of the four companies’ numbers this quarter show no contradiction anywhere.

Up to this point, this is an extension of what I wrote on May 11 in The Real Beneficiaries of Azure +40%, AWS +28%, GCP +63%: The Hardware Supply Chain Map Behind $580B in Cloud Capex. That piece drew the map of $580B in combined capex flowing into four hardware layers, and one quarter later, every one of those premise numbers has been revised upward.

## 4. The Boundary Public Materials Can Show

This is as far as public earnings releases and Baker’s public claims can take us. But to use this in investment decisions, there is more that needs checking.

First, whether there is evidence inside the results that repricing has already started rather than being something still to come. As it happens, two candidate pieces of evidence surfaced this quarter. One came out of Google’s earnings call, and the other is the difference in composition across the three companies’ backlogs. The backlogs of $514B, $638B, and $678B are all huge numbers that look like the same unit, but open them up and the contracts inside are different in character.

RPO paragraphs from the Oracle FY26 Q4 release

The other question is where the benefit of that repricing prints larger, in hyperscaler stocks themselves or in some hardware layer. There is a hint in the Oracle paragraphs captured above. The portion where customers prepaid for GPUs or bought and supplied them directly amounts to $75B [11], which means compute buyers have started taking on hardware procurement themselves. Why this paragraph matters is unpacked behind the paywall together with backlog quality.

Share this with anyone who needs to see the world through a different wavelength.

Share

## 5. Primary Evidence of Repricing: Usage Above Commitments and Backlog Quality

Starting with the first evidence candidate. A figure reportedly came out of this quarter’s results showing Google Cloud customers are spending about 50% more than their contracted commitments [12]. This is actually interesting. A commitment is the amount a customer promises as “we will spend at least this much.” Actually using 1.5x that floor is a direct signal that customers turned out to need more compute than they expected when they signed. Going back to the lease analogy, the tenant is paying extra to use more rooms, and once renewal negotiations start, this usage data will become the basis for the price increase as is.

Normally, you would sign a contract as conservatively as possible. You cannot pin down your usage in advance, and all of it can come back to you, the buyer, as losses. But 50% is a big number. In other words, couldn’t this be read as these buyers, too, having largely failed to predict their own demand?

The second piece of evidence shows up when you put the three backlogs side by side.

Google’s $514B, the company disclosed, has just over half expected to be recognized within 24 months [1]. It is a backlog with its conversion speed stated as an exact number. Microsoft’s $678B is total commercial RPO, so contracts beyond Azure are mixed in [5], and Oracle’s $638B, as the +363% growth rate itself tells you, is a number created by a handful of recent large AI contracts [11]. And $75B of it is the portion customers prepaid for hardware or supplied directly [11].

This $75B is the hint I flagged earlier. Compute is so scarce that buyers have gone as far as “I will bring the GPUs, just give me the space and power.” You would have to call this a contract structure that only appears in a market where pricing power has shifted substantially to the seller. More than the size of the backlog numbers, I see this change in composition as the stronger evidence for the underearning thesis.

The same thread shows up in Google’s transcript as well. CFO Anat Ashkenazi said on this call that they are still in a supply-constrained environment, and disclosed that while the vast majority of the $514B backlog is GCP agreements, TPU system sales are also reflected in it [13]. That means hardware sales mixing into cloud service backlogs is not just an Oracle thing.

Pulling this together in my own way, a signal that demand exceeds contracts (usage above commitments) and a signal that procurement burden has shifted to the customer (hardware prepayment) showed up in the same quarter, so I would judge repricing to be less of a preview and more of something already in progress.

But I will write down the limitations with the same weight. The starting figure, “spot at 2x the contracted rate,” is Baker’s observation. That judgment could of course be wrong. And for renewals to actually print in the P&L, expiring contract volume needs time to cycle through. This quarter’s numbers are early-stage evidence, not confirmation of the cycle.

## 6. The Meta Compute Variable

Meta is worth covering here. On July 1, Bloomberg reported that Meta is preparing a cloud business [14]. It would sell surplus AI compute externally, and the company is reportedly weighing two approaches: selling access to its own models, or selling raw GPU capacity. On the day of the report, Meta’s stock jumped while CoreWeave and Nebius each fell around 12% [15]. The hit to small neoclouds is obviously predictable.

There is a view that reads this report as a supply increase signal. If Meta sells compute, supply in the market grows and prices get pressured. But I want to read it a bit differently. I read it the other way. A company burning $130~145B a year considering external sales of even part of that infrastructure means there is an internal judgment that compute rental margins currently look comparable to reinvesting in its own ads business. It is the same pattern as SpaceX Started Renting Out Compute. The Rig Demand Is Now Written Into the Contract., which I covered in late June. It is less about renting out surplus resources and more about the spreading judgment that compute makes money, and I am holding this reading at the level of observation rather than conviction. (Of course, I want to lay down up front that I could be wrong.)

To add one piece of background here, hyperscalers themselves are also major customers of the neoclouds. Microsoft has struck commitments of around $60B combined with CoreWeave, Nebius, and Nscale, and by one tally Meta has stacked up contracts in the $35B range with CoreWeave and up to $27B with Nebius [16]. Meta buying this much on one side while preparing to sell on the other is itself a scene that shows how desperate capacity procurement is.

The neoclouds slid throughout July as the Meta Compute report overlapped with debt concerns. CoreWeave has Q1 revenue in the $2B range and a backlog around $100B, but total debt in the $50B range with quarterly interest expense climbing to the $500M range, and the stock is down about 40% from its high [17]. Nebius has $40B in contracted GPU revenue stacked up and reports earnings on August 12 [18].

Taking only what this piece needs, I read Meta’s entry consideration as a signal leaning toward compute prices holding for now.

## 7. May Map Update: Allocation Tilting Toward L3 and L4

Now to the second question, that is, where this money goes.

In the May piece I split capex into four layers. L1 compute (GPU), L2 custom ASIC, L3 memory, and L4 networking and optical. And I wrote that the layers that cannot be insourced are the real bottleneck. Google is partially insourcing L1 with TPU and Amazon with Trainium, but all three buy L3 and L4 from outside. One quarter later, that tilt has become clearer in the data.

Start with L3 memory. AI server DRAM costs roughly doubled in Q1 2026 alone, with forecasts of a fourfold increase for the full year [19]. Since 1GB of HBM consumes three to four times the wafer capacity of commodity DRAM, the more capacity shifts to HBM, the more the rest of memory dries up [19]. In other words, memory price increases are self-evident. Memory’s share of hyperscaler datacenter investment is around 30% this year, with 36% forecast next year [19]. That means one of every three capex dollars goes to memory, and new supply reportedly does not arrive until 2029 or later [19]. In The Cut Was Not HBM: The SOCAMM Selloff and the Optical Memory Fabric, written in June, I covered the path from memory bottleneck to optical fabric, and the supply shortage that piece assumed has now been confirmed in price data this quarter.

There is one thing to be careful about. Memory stocks sold off hard during SK hynix’s earnings week in late July. The peak debate on the price cycle has begun. I separate volume-based demand, that is, the memory share of hyperscaler capex, from the stock price cycle.

L4 optical interconnect is this account’s home turf, so I will go a bit deeper. The point where the repricing thesis meets optics is scale-across. As single-campus power hits its limits, training splits across multiple datacenters, and DCI (Data Center Interconnect, the optical transport network between datacenters) becomes part of compute performance itself. In July, One Layer Below SemiAnalysis’s Meta Map: Scale-Across Is Coherent, Not CPO laid out this structure from a coherent optics perspective.

This quarter, that demand printed in market data. Interest in ZR+ modules for long-haul DCI has jumped around 10x in a year, and the IPoDWDM systems market that uses them grew about 40% last year with a forecast in the $4B range by 2030 [20]. The more AI datacenters get connected to each other, the more this layer’s demand grows as a function of the distance and bandwidth between clusters rather than the number of clusters. Its absolute dollar amount within hyperscaler capex is smaller than L3, but it is the layer whose growth direction is tied directly to the structural shift toward campus distribution.

Capex to 4-layer allocation concept, post Q2 2026

Bringing it down to the stock level, it looks like this. In L3, the pure US-listed exposure is Micron ($MU), and going a bit further there is also Korea-listed SK hynix ($SKHY). The commodity DRAM shortage, the flip side of HBM capacity conversion, points the same way. The L4 DCI axis has Marvell ($MRVL) in coherent DSP, Ciena ($CIEN) in systems, and Coherent ($COHR) and Lumentum ($LITE) in optical components as the basic lineup. I judged that market caps and valuation comparisons for these names are best looked at in mid-August after earnings season ends and prices settle, so I am not pinning numbers in this piece. A comparison table built on July’s whipsaw prices goes stale within a week.

## 8. As Efficiency Improves, the Bill Grows

One objection to the repricing thesis remains. If models keep getting lighter, will compute demand hold?

This cycle’s data points the other way. Per-token inference prices fell around 1,000x over three years, while enterprise AI spending more than tripled last year [21]. Tokens routed through OpenRouter grew from around 5 trillion per week to the 30-trillion range in just over a year, and a single agentic request consumes fifteen times the tokens of a regular one [22]. The cheaper the unit price, the more things become worth doing, so total spending grows, a pattern that has repeated since the steam engine era. In July, Kimi K3’s Active Set Is 50B-Class. Its Weights Are 2.8T. covered the structure in which lightweighting does not reduce total demand, and this quarter’s usage-above-commitment figure is close to physical evidence of it.

And AI is not the whole of compute demand either. To add one paragraph as someone who works in semiconductors and engineering, buying large compute in the cloud was routine long before AI. Pre-tapeout EDA verification for a foundry run or device TCAD simulation are jobs that occupy a cluster whole for days at a time. A high-performance PC is not essential for semiconductor devices, design, or layout, but when you analyze and simulate those semiconductors, high-performance server computing power is essential. I know this better than anyone.

The cloud HPC market itself is under $9 billion a year, small next to AWS’s annual revenue [23], but the character of this demand is what matters. It is demand that keeps coming regardless of the economy or the AI cycle, as long as chips get designed, drugs get made, and airframes get analyzed. The list of reasons to buy compute keeps getting longer, and that is the floor of my answer to the question of whether the clouds keep making money.

## 9. Conclusion, and the Conditions Under Which I’m Wrong

Conclusion. I read this quarter as early-stage confirmation of the underearning thesis. Usage above commitments, customers prepaying for hardware, and all four companies raising capex at once all point the same way, and I have yet to find primary data that contradicts Baker’s frame that the renewal cycle, rolling from stabilized leases onto market rents, has begun. And I think the hardware-side benefit stays longest in L3 memory and L4 optical interconnect, the layers that cannot be insourced.

The prior-call review also goes here. The cross-layer gate in the May 11 piece was “check for capex guidance changes and 2027 guidance disclosure in hyperscaler Q2 earnings,” and the Alternative Case at the time was written as “further raises as the compute shortage deepens.” The results: Amazon raised from $200B to $220B [8], Microsoft put out FY27 at $255~260B [6], Meta raised its lower end [9], and Alphabet raised [1]. All four raised, so the Alternative Case became reality, and the call was confirmed beyond holding, toward the upside. The L3 pricing power call from that piece also holds on DRAM price data [19]. The part where I wrote ANET supply chain constraint resolution as the re-rating condition for L4, however, I could not verify in this piece, and I will come back to it next earnings.

If next quarter’s results show the usage-above-commitment rate rolling over or backlog growth stalling, then what we saw was order pull-forward, not repricing. If cloud gross margins do not rise even as renewal volume starts cycling through, it means the spot premium is not transferring into contracted prices, and the core of the thesis breaks. And if the GPU depreciation schedule debate turns into an accounting change, the cloud operating margins we see now have to be recalculated from scratch.

There are a few dates I am watching closely.

Nebius earnings on August 12 will give the first look at the direction of contract pricing on the neocloud side [18]. Micron’s late-September earnings are the gate for the L3 allocation thesis, and in the four companies’ Q3 results in late October I will recheck the usage-above-commitment rate and the backlog increments. As for the seven-neocloud comparison, I would like to continue that in a separate piece after seeing Nebius’s results, if the opportunity comes.

## Acknowledgment

The problem statement of this piece, the hyperscaler underearning thesis starting from the gap between GPU spot prices and contracted prices, was first laid out by Gavin Baker of Atreides Management in his X post and Invest Like the Best interview [2][3][4]. What this piece adds is the verification of that thesis against Q2 primary data (usage above commitments, backlog composition, capex guidance), and the connection to the four-layer hardware map. No paid-media data was used, and cited figures were verified directly against company announcements and public reporting.

## References & Sources

[1] “Alphabet Q2 FY 2026: Google Cloud Leads Growth Amid Rising AI Investment”

[2] “Gavin Baker on X: spot pricing for GPU compute”

[3] “15 Key Takeaways From Gavin Baker’s Invest Like the Best 2026 Interview”

[4] “Gavin Baker: Watts and Wafers, Invest Like the Best EP.473”

[5] “Microsoft FY26 Q4 Press Release”

[6] “Azure Crosses $100 Billion for the First Time as Microsoft Q4 Beats Revenue and Earnings Estimates”

[7] “Amazon Q2 2026 earnings report”

[8] “AWS earnings Q2 2026”

[9] “Meta Reports Second Quarter 2026 Results”

[10] “Meta Q2 Beats Revenue While Legal Charges and AI Spending Destroy Free Cash Flow”

[11] “Oracle Announces Record Q4 and FY 2026 Results Driven by Cloud Infrastructure & Cloud Applications”

[12] “Google Cloud customers spending 50% above commitments as AI demand drives record quarter”

[13] “Earnings call transcript: Alphabet beats Q2 2026 estimates, shares fall on capex surge”

[14] “Meta Is Planning a Cloud Business to Sell AI Computing Power”

[15] “Meta pops 9% as company makes cloud push to sell excess AI compute power capacity”

[16] “Neoclouds Challenge the Hyperscalers in Big Bets on AI Infrastructure”

[17] “Down 40%, CoreWeave Is Being Left Behind By the Market”

[18] “Nebius Locks In Aug. 12 Earnings Date After Vera Rubin Rack Goes Live in Finland”

[19] “Why the memory chip crunch is greater than expected, and may not ease until 2029”

[20] “Cloud and Data Center Interconnect (DCI) creates a new coherent optics wave”

[21] “The Inference Cost Paradox: Why Your AI Bill Goes Up as Models Get Cheaper”

[22] “Jevons Paradox: Why Every AI Optimization Makes the Hardware Shortage Worse”

[23] “Top 25 Companies in Global Cloud High Performance Computing Market”

This article is an independent technical analysis published by PhotonCap, based on an engineering perspective. All content is derived from publicly available information and is intended solely for educational and informational purposes. In other words, nothing in this material should be construed as a recommendation to buy, sell, or hold any specific securities. Please note this carefully.

The author may hold positions in the securities mentioned herein and reserves the right to trade such securities at any time without prior notice. Readers should conduct their own thorough review and research before making any investment decisions.

Share
