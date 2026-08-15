---
publish: false
date: 2026-08-02
tags: [research, email-backfill, PhotonCap]
source: 'https://photoncap.net/p/axt-and-lumentums-prepayment-deal'
source_type: web-clip
sender: photoncap@substack.com
---

# AXT and Lumentums Prepayment Deal The InP Substrate LTA Chain

People often discuss where the bottlenecks lie. Whether it’s the GPU, memory, or optics. As AI agents gained prominence, the importance of the CPU came to the fore, followed by concerns regarding power supply and land availability. There was also a time when Indium Phosphide (InP) substrates attracted significant attention.

A prime example is AXT, a company that saw tremendous growth this year, with its stock price climbing to around $120. Although the price has recently dropped significantly driven by the Leopold liquidation event and concerns over China-related risks I would like to take a closer look at this stock.

### TL;DR

- On July 29, AXT announced a long-term InP substrate supply agreement with Lumentum. A $43.5M deposit lands in cash within a month, another payment of the same size is scheduled for 2028, and capacity is reserved through the end of 2031.

- Lumentum is a company running no fewer than five InP fabs. That means it needs a lot of InP substrates, and this time it decided to buy them prepaid.

- The same week, Lumentum’s CEO said in a public forum that the InP shortage will get worse than what we see in memory. The words and the money came out in the same week.

- To note just the direction up front, I read this contract as evidence of the InP substrate shortage in the optics market, and at the same time I see it as the start button on the cycle clock. The checkpoint dates to monitor, and the reasoning behind them, are laid out one by one later in the piece.

### Contents

- July 29

- The Structure of the $87M Deposit

- Who Actually Makes the Substrate

- The LTA Chain

- Deposit Economics and the Expansion Race

- The 1060nm Detour

- Up and Down the Chain: Layer by Layer

- Conclusion and the Dates to Check

## 1. July 29

On July 29, AXT (NASDAQ: AXTI) announced a long-term supply agreement with Lumentum (NASDAQ: LITE) [1]. It covers InP substrates, that is, the indium phosphide wafers that light-emitting laser chips are built on, supplying them through the end of 2031 and reserving a minimum annual capacity for Lumentum. In return, Lumentum pays a $43.5M deposit in cash within 30 business days of signing, and will put in the same amount once more sometime during 2028 [1]. $87M in total.

There was one more statement that came out the same week. Lumentum CEO Michael Hurlston reportedly said on a summit stage in Paris that the InP shortage will become even worse than what the memory side is seeing [2][3]. A number came with it: the gap between demand and supply has widened beyond what was said on the last earnings call, to over 30% [2][3].

Thank you for sharing, Molly O’Shea..

And by coincidence, on the very same day, we (Aurelion Research and PhotonCap) published a piece summarizing a conversation with Lumentum’s VP of Investor Relations. That content is available for free in A Conversation with Lumentum, and I’ll be bringing its testimony back throughout this article.

## A Conversation with Lumentum

Disclaimer: This article is a joint publication. The management meeting and investment analysis were prepared by Aurelion Research, and the technical comments by PhotonCap. All content is based on publicly available information and the authors’ notes, and is provided for educational and informational purposes only. Nothing herein constitutes investment …

The CEO’s words and the company’s money came out in the same week. That is the starting point of this article and the reason I sat down to analyze it.

## 2. The Structure of the $87M Deposit

Before we get into the contract, it would be good to quickly go over what InP is. Silicon, the protagonist of the semiconductors we know well, CMOS, CPU, GPU, Memory, is hopeless at turning electricity into light. It carries electricity just fine, but its crystal structure leaks the energy away as heat instead of light when it tries to emit.

InP is the opposite: it is a material that converts electricity directly into light, and above all it is practically the only base wafer on which you can stack, defect-free, the lasers and receiver devices for the wavelengths with the lowest loss in optical fiber (1310nm, 1550nm). That is why every optical link in a data center starts on this wafer. As for why neither silicon nor GaAs can take its place, we covered it at length, starting from the material physics, in March’s AXT Inc. (AXTI) Deep Dive: The Hidden Bottleneck in AI Optical Interconnects, so if you need the background, feel free to start with that piece. (The first half is written to be understandable without an engineering degree.)

Now, the contract itself. It is a definitive agreement disclosed via 8-K, meaning a binding contract, not a letter of intent [1]. The two deposits are applied as credits against future shipment payments, so in effect Lumentum is depositing money in advance for the wafers it will buy [1].

It is a contract where the money moves before the goods.

As you well know, there is no reason to do this in a loose supply market. Putting money down first to hold your place, like paying upfront to lock in a purchase, is an action you take exactly when the goods are scarce, or when you believe they will stay scarce. And indeed, Lumentum’s stock slipped after the announcement, and an article ran with a headline calling it a costly supply deal [4]. To be honest, access to that article was blocked and I could not verify the full text, so I am citing it only at the headline level.

That leaves a natural question. Why did a company running five InP fabs have to buy substrates from outside, and prepaid at that?

## 3. Who Actually Makes the Substrate

Owning fabs and making substrates are different businesses. There is the stage where indium metal, a byproduct of zinc smelting, is grown into single-crystal ingots and sliced thin into substrate wafers; there is epitaxy (the process of depositing crystal layers on the substrate, epi from here on), which stacks the light-emitting layers on that wafer; and then comes the fab, which processes it into laser chips. What Lumentum owns five of is only the last stage. In other words, it has no wafers of its own.

And the substrate companies in the earlier stage are few in the entire world. Japan’s Sumitomo Electric, US-listed AXT, and Japan’s JX Advanced Metals are known to hold most of the world’s supply (we analyzed this down to the supply chain in AXT Inc. (AXTI) Deep Dive: The Hidden Bottleneck in AI Optical Interconnects) [5].

There is a good reason why there are so few substrate manufacturers: InP (indium phosphide) single crystals are notoriously difficult to grow. Because the phosphorus (P) component tends to vaporize and escape near the melting point, high pressure must be maintained throughout the growth process to prevent its loss. Furthermore, the finished crystals are more brittle than silicon. That’s why, while silicon wafers transitioned to 12-inch sizes long ago, InP wafers are still primarily produced in 2- to 4-inch formats, with mass production of 6-inch products only just beginning. The know-how required to produce usable wafers is embedded in decades of accumulated process data, making this a sector that new entrants cannot easily penetrate simply by injecting capital.

The significance of this in the current market cycle is straightforward: there is a long lead time between the announcement of production capacity expansion and the actual shipment of products. Not only does it take time to set up the crystal growth furnaces, but additional time is required to achieve a yield of wafers that meet commercial quality standards. Consequently, these structural characteristics make this stage of the process a frequent source of bottlenecks when demand surges.

Even Coherent, said to be the most deeply vertically integrated among optical players, buys its substrates outside under multi-year contracts and starts from epi in its own fabs [6]. So buying substrates is, in itself, business as usual, and the signal is in how they are being bought. A deposit instead of a purchase order, a six-year reservation instead of spot.

InP value chain layers, from indium metal to laser chip, with the substrate stage highlighted

But here an enormous variable called China comes into the picture. AXT’s production sits in its Beijing subsidiary Tongmei, and since indium-related items are on China’s export control list, every shipment needs a permit. In fact, within the past year there is a track record of one quarter getting crushed by permit delays and then recovering sharply once the permits came through [7].

On top of that, the company has said that data-center-driven InP demand is growing fast inside China as well [7]. With Chinese companies occupying the top ranks of the global optical module market, the same substrates end up contested between Chinese domestic demand and export volumes. China’s optical module market, as those who know it will know, is quite large. We covered it in a free article called Chinese Optical Modules Own 7 of the Top 10 Seats. The fact that the supply line Lumentum just locked in sits inside China’s permit regime is both a condition and a risk of this contract.

In the conversation introduced earlier, Lumentum IR said EML capacity at the two fabs in Japan grew eight-fold in two and a half years. And yet it still falls more than 30% short [2], so isn’t the bottleneck not the speed of making chips, but the substrate in front of it??

## 4. The LTA Chain

The picture gets bigger if you look at this contract not as a single box but as a supply chain. Early this year, NVIDIA invested $2B in Lumentum in the form of convertible preferred stock, attaching a multi-year purchase commitment [8]. One layer down, Lumentum put an $87M deposit on AXT and reserved capacity through 2031 [1], and AXT in turn raised funds for substrate expansion through an equity offering in the $600M range [2]. The money that started on the side buying optical modules has come down a full three links, through contract after contract, all the way to substrate expansion.

Because each layer’s seller is the next layer’s buyer, every company puts a deposit on the layer below and receives a deposit from the layer above. When the shortage is real, this chain is rational for everyone.

But as you may have noticed, the problem is that the moment the shortage ends, the chain works in reverse too. That story comes after the paywall.

The LTA chain, three contract links from NVIDIA to Lumentum to AXT with deposit and reservation terms

In fact, the existence of this contract was not news. On the May earnings call, Lumentum said it had already secured long-term agreements for substrate, and even explained that the structure included deposits and take-or-pay (you pay even if you don’t take the volume). Only the counterparty was undisclosed. We covered that passage at the time in The 8 Companies Behind Lumentum’s $808M Quarter and put counterparty disclosure on the monitoring list, and this 8-K is the answer sheet. The name was AXT, and the deposit structure was exactly as foreshadowed.

Everything up to here is what anyone can see from public materials. From here on, we stretch the chain up and down: how deposit contracts ended in past materials cycles, when the expansions arrive, and the detour Lumentum itself is building.

Share

## 5. Deposit Economics and the Expansion Race

Let’s look at the $87M deposit from both sides’ books and the character of the contract emerges. From AXT’s side, it is effectively interest-free expansion funding. For a company with annual revenue around $100M [2], the combined deposits are about the size of a full year’s revenue. From Lumentum’s side, it is, in a way, an insurance premium at a ‘reasonable price.’ Without substrates all five fabs stop, so it deposited part of its future wafer payments in advance and bought the right to receive volume even in a shortage.

This structure is actually not a first. In the late 2000s, deposits and take-or-pay long-term contracts of almost the same shape are known to have been common in solar polysilicon. They were rational for everyone while supply was short, but once the expansions arrived and spot prices fell below contract prices, those contracts became subjects of renegotiation. (I did not verify specific company figures for this, so please take it as a rough qualitative comparison.)

Still, one lesson carries over. The fate of a deposit contract is decided not by the contract but by when the expansions arrive.

So when the expansions arrive becomes the next question. Sumitomo Electric announced an investment to raise its InP substrate capacity to a bit over 3x by 2028, and reportedly that was the result of raising, once more, the expansion scale it had announced half a year earlier, citing stronger-than-expected demand [9]. JX Advanced Metals decided on an investment in the JPY 100 billion range over four years, adding a new site on top of expanding its existing plant, and has replaced its expansion announcement three times within a year [10]. AXT’s offering proceeds go to the same place [2], and Lumentum itself is preparing its fifth fab with a ramp target of early 2028 [8].

Put the dates on one line. Sumitomo’s expansion target is 2028, JX’s four-year investment lands around there, Lumentum’s new fab is early 2028, and the year that sets the timing and terms of the second $43.5M deposit is 2028 [1][9][10].

The year the supply arrives and the year the next link of the chain gets tightened or not are the same year. Rather than coincidence, I read it as both sides seeing the shortage holding until that point and leaving what comes after open.

## 6. The 1060nm Detour

Months before the CEO talked shortage in Paris, Chief Strategy Officer Rafik Ward explained a different side of the story in an interview at OFC in March. In a phase where InP supply is tight, it is an approach that eases the pressure on the bottleneck with co-packaged optics based on 1060nm VCSELs (vertical-cavity surface-emitting lasers, which fire light vertically) [11]. Lumentum actually demonstrated it at OFC too. The setup was a VCSEL and photodetector built as a two-dimensional array, placed next to an ASIC [12].

The important point: VCSELs are built not on InP, the protagonist of everything so far, but on wafers of another III-V material called GaAs. Because InP is scarce, the company that talks loudest about the InP shortage is itself developing the option of shifting some links to a different material.

In June’s The AI Light Source War Is Not a Speed Race: InP, VCSEL, and μLED Are Buying Different Distances we went through which distance segment each light source ends up buying. On that map, the 1060nm VCSEL is aimed squarely at the ultra-short box.

Which material ultra-short chip-to-chip links will settle on is not decided yet, but the investment implication is clear. The InP substrate demand curve has a ceiling called architecture substitution, and the height of that ceiling is set by the material choice for chip-to-chip links.

There is also a detour on the area side. Coherent announced it has brought 6-inch InP wafers into volume production, a transition where the same number of wafers yields several times more chips [13]. You can read it as a direction that effectively stretches substrate supply in chip terms, without adding a single wafer. If you are buying the shortage through substrate pure plays, you need to keep in mind that these two detours are variables that shave the upper end of demand estimates.

## 7. Up and Down the Chain: Layer by Layer

Let’s walk the chain one layer at a time, noting the listed entry points and what to watch out for.

The substrate layer. AXT is the direct beneficiary box in this chain, and this contract gives it multi-year volume visibility. That said, the export permit issue is a point that always needs watching. Sumitomo Electric is the protagonist of the expansion but is not an InP-only company; it is a conglomerate where InP is a small share. JX Advanced Metals, in its first year listed in Tokyo, has put InP expansion forward as its growth direction, making it an option with a different character [10]. There was also a recent article noting that the US, China, and Japan have entered the expansion race while Korea alone is missing [14].

The epi layer is the candidate for the shortage’s next stop. If substrates increase, epi capacity to stack the light-emitting layers becomes the next bottleneck, in that order. The UK’s IQE signed a multi-year InP epiwafer supply agreement with Tower Semiconductor [15], evidence that the chain’s contract format has come down to the epi layer. Taiwan’s epi specialists are entry points on the same layer [5]. That said, we wrote in the May piece that this layer has the internalization trend of its big customers hanging over it, and I maintain that view.

The remaining optical module and laser players get caught on allocation order. In a shortage, suppliers fill the big contracts first, so the gap widens between Lumentum and Coherent, who have the strength to put down deposits, and those who don’t. Companies like AAOI, which owns its own laser fab but buys at small scale, and fab-lite Sivers, known to receive InP wafers from IQE, sit on that boundary [16]. Each company’s substrate and epi sourcing comments next earnings season will be the first check.

The raw material layer has an unexpected connection to Korea. Indium has no dedicated mines and comes out as a byproduct of zinc smelting, so supply elasticity is low, and with China putting indium on its export control list, the value of non-Chinese volume has risen and prices are reportedly firm (secondary source) [17]. Since a zinc smelter is by structure an indium producer, Korea’s Korea Zinc is known as one of the world’s top producers, but indium is a negligible share of its revenue, so it is hard to treat as cycle beta.

The equipment layer is a second-order effect. Substrate expansion flows into crystal growth and processing equipment orders, and more substrates flow into MOCVD orders for epi. The stock map for this layer is still valid as drawn in the frame of the May piece. What this contract adds is not the direction of the orders but the length of the contract. Volume reserved through 2031 means equipment orders get planned on a multi-year basis too.

Timeline of the cycle gates, first deposit 2026, capacity arrivals 2027 to 2028, second deposit 2028, agreement end 2031

## 8. Conclusion and the Dates to Check

My conclusion is a modest one. This contract is the strongest disclosed evidence that the InP substrate shortage is real, with the CEO’s remarks landing right on time, and at the same time it is a document with a clock built into the contract for checking how long that shortage lasts. For those betting on the shortage’s direction and for those betting on its end, the reference dates are the same. That is the charm of this contract.

One review of a past call before we go. In the May 7 piece, we put disclosure of Lumentum’s substrate LTA counterparty on the monitoring list, and wrote, based on the call at the time, that the structure would be a deposit with take-or-pay attached. The July 29 8-K confirmed the counterparty as AXT and the deposit structure as-is, so that call stands. In the same piece we wrote that substrate companies carry one notch less internalization risk than epi companies, and this contract, where the biggest customer put a six-year deposit on a substrate company, reads as evidence in the same direction.

The answers will come from the dates below.

- August 2026, AXT earnings: confirmation of the deposit received, expansion progress, and how the contract is reflected in guidance.

- Mid-August 2026, Lumentum earnings: whether the supply gap said to be in the 30s holds, and whether additional substrate LTAs get signed.

- During 2027, Sumitomo and JX expansion volume starts arriving: substrate spot prices and lead times will be the first to react.

- 2028, the timing and terms of the second $43.5M deposit get set: the biggest checkpoint of this article. If it is paid as scheduled, the shortage-persists call stands; if the timing slips or the terms get renegotiated, that should be read as the first disclosed signal that the cycle has turned.

- Ongoing, the material choice for chip-to-chip links: as 1060nm VCSEL adoption news accumulates, the upper end of InP demand estimates has to come down.

The conditions under which I am wrong are in the same list. If substrate prices and lead times hold even after the 2027 expansion arrivals, the shortage is longer than I think.

Conversely, if renegotiation signals show up before 2028, I will withdraw the shortage-persists reading and write up the chain’s reverse rotation instead. The next piece will likely be the one that checks the first two items on this list, after AXT and Lumentum report.

## References

[1] “AXT, Inc. Announces Long-Term Supplier Agreement with Lumentum” AXT IR, 2026-07-29.

[2] “A New AI Shortage Is Coming. One CEO Just Predicted it Will Be “Bigger Than Memory.”“ Yahoo Finance, 2026-07-28.

[3] “BREAKING: Lumentum CEO on How Lasers Are Transforming AI Data Centers” Sourcery, RAISE Summit interview, 2026-07-29.

[4] “Lumentum Stock Slips As Costly Supply Deal Raises Doubts” TipRanks, 2026-07.

[5] “InP substrate shortages emerge as new bottleneck for optical chips” DigiTimes, 2025-12-29.

[6] “Coherent’s Vertical Integration Strategy” Chipstrat (analysis publication), 2026.

[7] “AXT’s revenue grows 17% in Q1 after greater-than-expected export permits” Semiconductor Today, 2026-05-05.

[8] “Lumentum to establish new US plant to manufacture indium phosphide lasers for AI data centers” Semiconductor Today, 2026-03-26.

[9] “Sumitomo Electric to Raise InP Substrate Expansion Scale With JPY 18 Billion” TrendForce, 2026-07-13.

[10] “Decision on Capital Investment Policy to Significantly Expand InP Substrate Production Capacity” JX Advanced Metals, 2026-06-16.

[11] “2026 OFC Showcase” NextGenInfra, Rafik Ward interview, 2026-03.

[12] “Lumentum Showcases Breakthrough Optical Scale-Up Demonstration at OFC 2026 Using VCSEL Technology” Lumentum PR, 2026-03-17.

[13] “World’s First 6-inch InP Scalable Wafer Fabs Paving the Way for the Next Generation of Lasers for AI Transceivers and 6G Wireless Networks” Coherent PR.

[14] “InP Substrate Race Heats Up in U.S., China, and Japan, Leaving Korea Behind” The Electronic Times, 2026-07-08.

[15] “IQE and Tower announce multi-year InP epiwafer supply agreement” Semiconductor Today, 2026-06-15.

[16] “Sivers Semiconductors (SIVE): InP Laser Chokepoint” SEQH Research (analysis publication), 2026.

[17] “Indium Price Outlook 2026: Steady Gains as Export Controls Tighten Supply” Strategic Metals Invest (secondary source), 2026.

would you like to share?

Share

Disclaimer: This article is an independent technical analysis published by PhotonCap, based on an engineering perspective. All content is derived from publicly available information and is intended solely for educational and informational purposes. In other words, nothing in this material should be construed as a recommendation to buy, sell, or hold any specific securities. Please note this carefully. The author may hold positions in the securities mentioned herein and reserves the right to trade such securities at any time without prior notice. Readers should conduct their own thorough review and research before making any investment decisions.
