---
publish: false
date: 2026-08-11
tags: [research, email-backfill, PhotonCap]
source: 'https://photoncap.net/p/five-days-after-innolights-68b-the'
source_type: web-clip
sender: photoncap@substack.com
---

# Five Days After Innolights 6.8B FCC Ban Draft and AI Optical Module Supply Chain

### Abstract

The Trump administration suddenly came out saying it would block Chinese transceivers. In the early hours of August 4, Reuters reported the FCC’s import ban draft, and communities everywhere got excited. And as you’d expect, US optical stocks rose double digits intraday. In the market, an interpretation was going around that AXTI gets hurt if China retaliates, and I think that’s a one-dimensional reading. Then a few days later, commentators like Jukan, separately from this news, started talking about a short-term short memory, long optical trade based on NVIDIA’s roadmap, so regulation and architecture are pointing at optics for different reasons. This article checks the disclosure documents of Innolight, which raised $6.8B five days earlier, to see how much of its volume is actually US-bound, and works down through capacity and the InP substrate chain to ask whether US-made supply can absorb that demand. To note my direction up front, I think the essence of this regulation is that it exposes the fact that without transceivers, even the US cannot build AI data centers.

### Contents

- A Draft Out of Nowhere

- The $6.8B Five Days Earlier

- The US-Bound Volume in the Disclosures

- A One-Line Fight over the Text: Nationality or Origin (Paywall)

- Can US-Made Supply Absorb the Demand

- Going Down to InP: AXTI

- Can You Build an AIDC Without Transceivers

## 1. A Draft Out of Nowhere

The Trump administration suddenly came out saying it would block Chinese transceivers. It was a Reuters exclusive on the morning of August 4 (US time): the FCC is drafting an import ban on Chinese data center equipment including new Chinese optical transceivers, aiming for publication within the year and immediate effect [1]. The stated grounds are concerns over data theft, malware, and remote service disruption. I remember people getting very excited. Especially on X, saying that because of the FCC event, US optics-related stocks, for example AAOI, COHR, LITE, would be the beneficiaries.

Reuters exclusive headline, FCC drafting ban on Chinese data center devices, 2026-08-04

Let me start with the market reaction. AAOI rose around 20% intraday, Coherent and Lumentum double digits, and Corning around 8% (intraday figures that vary by when you sampled them) [2]. The Chinese side reacted a day late since the report came out after their market close: on August 5, Innolight’s A-shares fell as much as 16% intraday before closing down 7%, the H-shares fell 5.2%, and the next day they bounced right back to near record highs. The swings continued after that, and on August 10, the same day as a broad optics pullback ahead of earnings season, it closed down 6.9% at HK$1,033. Still 5% above the offer price [3].

And there was one more interpretation people attached to this news. That if China retaliates by squeezing InP exports, AXTI, which makes substrates in China, gets hurt. I think this is a one-dimensional reading, and why becomes visible only once you go down the InP chain, so I’ll write about it later.

What to look at first is the company that is number one in the transceiver industry and sits right in the middle of the ban’s target. This company, of all times, had just raised money in Hong Kong five days earlier.

## 2. The $6.8B Five Days Earlier

A few days before the FCC event, on July 30, Zhongji Innolight listed its H-shares in Hong Kong. At an offer price of HK$980, it raised HK$53.4 billion (about $6.8B), the largest in Hong Kong since Alibaba in 2019 [4][5]. The Hong Kong retail tranche was 16.8x subscribed and the international tranche 9.7x, and 33 cornerstone investors including Temasek, ADIA, BlackRock, Alibaba, and Tencent took half of the offering (about HK$26.7 billion worth) under a six-month lock-up [4][5].

The ten days around the listing were noisy in the headlines. When the offer price printed around 11% below the A-shares (per press reports), the A-shares plunged 15.7% on the pricing disclosure day [6][7], and on debut day, sitting on top of a chip selloff week, the stock fell as much as 9.8% intraday before closing 2% below the offer price [8][3]. But look at the closing-price chart and there is no stretch you could call a crash. It recovered the offer price the next day, and through the swings since, it sits at HK$1,033, 5% above the offer price even as of the August 10 close [3]. One fact remains. The world’s largest optical module company is holding net proceeds of HK$52.9 billion [5].

How they should use this money, honestly, is the part I’m most curious about. The uses listed in the prospectus are R&D, overseas production capacity expansion, supply chain strengthening, M&A, and general working capital [9]. Five items, and where the weight lands is open, and the FCC draft that came five days later added a variable to that answer. The meaning of the overseas capacity item now changes completely depending on the regulatory text.

Figure: Four forces on the debut day

## 3. The US-Bound Volume in the Disclosures

Look at the disclosures and quite a lot is US-bound. US customer revenue was 75.9% in 2023, 57.3% in 2025, and 61.7% in Q1 2026 [9]. Overseas revenue overall is above 90% as of Q1. So this is a Chinese company where 60% of revenue comes from the US. This is exactly where the FCC draft is aiming.

But the same disclosures carry numbers pointing the other way. Goods made in mainland China and sold to the US were under 1% of total revenue throughout the track record period. By year: 0.3%, 0.9%, 0.2%, and 0.0% in Q1 2026 [9]. Which means the US-bound volume has effectively already been moved entirely to offshore production. The Singapore entity TeraHop Pte is the hub of overseas production, and the main base for North America-bound goods is Thailand [9][10]. The way Chinese vendors have been adding capacity in Thailand and Indonesia is exactly the layout we covered in April in Chinese Optical Modules Own 7 of the Top 10 Seats.

US revenue is 60%, but mainland-origin US-bound is around 0%. The gap between these two numbers decides the entire effectiveness of this regulation. As the optical communications research firm Cignal AI pointed out, the draft does not yet have a definition of “Chinese” [10]. Do you look at the company’s nationality, or the place of production. The question Cignal posed compresses this ambiguity. Is a module that combines Marvell’s DSP and Lumentum’s optics, assembled in Malaysia, Chinese [10]?

Why does the definition matter this much: because the same module from the same company is a legal import under one criterion and a banned item under the other. Unlike routers or drones, transceivers sit on a layout that a definition clause is perfectly positioned to split: the top suppliers are Chinese by nationality and Southeast Asian by production. One sentence in the Federal Register will decide whether billions of dollars of volume crosses the border.

Prospectus, origin of US-bound shipments and regional revenue pages, 2026-07-22

Share

## 4. A One-Line Fight over the Text: Nationality or Origin

Start with precedent. The FCC’s Covered List (the roster of equipment deemed a national security concern) is an old institution, but recently a mode of designating entire foreign-made equipment categories, rather than individual companies, has been used twice. Foreign-made drones and key components in December 2025, and foreign-made consumer routers in March 2026 [11].

Both measures blocked FCC authorization of new models while allowing the import and sale of already-approved models, and opened exceptions for new authorizations through a separate Conditional Approval process [11]. The “new models” wording in this draft has the same shape [1]. And in June, the Department of Defense put Innolight on the 1260H list (the roster of Chinese military-linked companies) [12].

Now plug in the two numbers from section 3.

Under a narrow criterion that only looks at country of production, direct exposure sits at the lower bound. Mainland-origin US-bound is around 0%, so there is almost no volume to block. In the prospectus’s origin-based revenue accounting, Thai-made TeraHop modules are classified as Thai production [9]. Though there is no guarantee that classification holds if the FCC or customs separately weighs component origin and substantial transformation. If the regulation lands on this end, I think the August 4 rally in US optical stocks gets given back in large part, ‘as far as the FCC-event-driven portion of the gains goes.’

Under a supplier-nationality criterion, the story is different. Innolight’s goods get blocked no matter where they were made, so US customer revenue of 61.7% hangs as the upper bound of exposure [9]. The actual blocked share can come in below that depending on the status of already-approved models and exception clauses. In this case, the $6.8B of overseas capacity expansion changes character: less a means of circumventing regulation, more a redeployment fund aimed at markets outside the US. The question left open in section 2, that is, where this money goes, has its answer subordinated to the regulatory text.

Figure: Two definitions of Chinese, two exposures

There is also no rule that the actual text comes out as only one of these two ends. It can combine production location with entity designation, or layer on component-origin criteria. So the 0% range and the 60% should be read as the two ends of a lower and upper bound.

The way I see it, the real battlefield of this draft is the definition clause that will be printed in the Federal Register. The lobbying will converge there too. For hyperscalers, an origin-based criterion hurts their procurement network less; for the US optical module industry, only a nationality-based criterion justifies the rally. The stated rationale being security, that is, distrust of equipment made by Chinese companies, puts weight on the nationality side. And compromises like the router precedent are entirely possible [11]. At the draft stage, neither can be called.

Beijing is in this fight too. The Chinese embassy in the US said it would take all necessary measures against actions that materially harm its interests, Reuters reported [1]. This company’s biggest risk is a regulation made by the US, yet its biggest customers are also US companies, and the cornerstone list includes US institutions like BlackRock [5]. I read this situation less as a narrative of decoupling in progress, and more as one where no one has yet agreed on who pays the cost of decoupling.

## 5. Can US-Made Supply Absorb the Demand

In the US, AAOI, LITE, COHR stock prices did go up. But I do wonder whether the demand can be absorbed, by US-made supply as it stands.

Look at the numbers. Per Cignal AI’s tally, the global datacom optical component market in Q1 2026 was $7.7B. Innolight alone was $2.6B for a 34% share, Eoptolink $1.1B, and with HG Genuine the top three Chinese suppliers pass half, with Chinese-headquartered suppliers at around 60% overall [10]. On the US side, the pure-play module maker AAOI’s datacom revenue in the same quarter was $81M [10]. One thirty-second of Innolight’s. AAOI’s CFO himself says demand exceeding capacity will continue “at least until middle of 2027, maybe beyond” [13], and contract manufacturer Fabrinet is already supply-constrained, with Cignal’s assessment being that building replacement capacity takes years [10].

Figure: The absorption gap in 1Q26 datacom optics

So if the ban takes effect on a nationality basis, what comes first is a supply bottleneck. A clean market-share transfer is the story after that. Bottlenecks push up selling prices. A short-term tailwind for US optical stock earnings, and a burden on hyperscalers’ capex costs. The press coverage carried warnings that a short-term cutoff could raise construction costs for North American data centers and pressure the capex of the big cloud providers [2], and advice to stockpile Chinese modules before it takes effect even showed up in trade media [14]. If stockpiling actually happens, you also get the distortion of shipments getting pulled forward into the quarters before effectivity.

The US side had also moved in advance. In March, NVIDIA went into Lumentum with $2B in convertible preferred and into Coherent with a $2B equity investment, signing multi-year purchase commitments and capacity access rights with both [15][16]. It reserved optical capacity ahead of time. That structure is what we covered in Coherent, Lumentum, Marvell, and Now Corning: NVIDIA’s 4 Photonics Bets and the Path of Light, and the FCC draft is an event that pulls forward the payoff timing of those bets.

What to listen for in earnings season is the language more than the revenue numbers. Whether lead times (the time from order to delivery) are stretching, whether 1.6T capacity is already booked, whether phrases like annual price-down are returning to pricing negotiations. If the language of shortage holds, it points to the bottleneck scenario; if the language of price returns, it means replacement capacity is catching up faster than expected. On a slightly longer clock, the more module supply becomes a political variable, the stronger the hyperscalers’ incentive to tilt toward architectures that reduce dependence on pluggable modules altogether (the CPO direction).

Let me also check our April call here. The conclusion then was that the module layer is thin on profit from price competition while the chip and component layers above it make the money. What the FCC draft does is twist that structure temporarily. If politics creates artificial scarcity in the module layer, non-Chinese module capacity briefly gains pricing power, and once the scarcity lifts, I think the profit returns to the chip and component layers. The call stands, with the caveat that its effective timing is subordinated to the text.

By name, here is how I see it. The heaviest multiple is Lumentum. At a $63B-range market cap and a TTM P/E in the 150s (as of 2026-08-10) [15], it is the most sensitive seat in a rally-give-back scenario, but with NVIDIA money behind a new US fab plan in motion, it also has the biggest seat to catch if the nationality criterion is confirmed [15]. Coherent is a $63B-range market cap at a P/E around 135 [16], and among US names it overlaps Innolight’s revenue footprint the most. It also has NVIDIA’s $2B investment and multi-year purchase commitments for laser and optical networking products [16].

AAOI rose the most that day of the report, around 20% intraday [2], but as we saw above it is an $81M-sized vessel in datacom revenue [10], so the time until volume-transfer benefits show up in its actual numbers could be the longest of the four. In fact, the Q2 results that came out on August 6 showed exactly this double face. Revenue was $191.9M, a record for the fifth consecutive quarter, while GAAP gross margin was 27.7%, the lowest in six quarters [17].

Volume is already overflowing but profit is not there yet: the same picture as the vessel story above. Fabrinet (market cap in the $18B range, P/E around 45, as of 2026-08-10 [18]) is a different animal. The value of non-Chinese contract capacity goes up, so under a nationality criterion it is on the structural-beneficiary side, but Cignal’s assessment that expansion takes years [10] is both the cap on that benefit and part of the bottleneck thesis. Earnings come August 11 for Lumentum, the 12th for Coherent, the 17th for Fabrinet.

## 6. Going Down to InP: AXTI

Now for the AXTI story I put off in section 1. The question of why US optical names can’t just add capacity has a back end. The EML and DFB lasers used in AI data centers’ 800G and 1.6T links, and many of silicon photonics’ external light sources, are made on InP (indium phosphide) substrates (short-reach VCSELs are mostly GaAs-family, so they’re the exception).

The supply chain for these substrates and the raw indium hangs substantially on China. The point that what limits the pace of Western replacement capacity is the substrate and materials underneath, more than the assembly lines, came out right after the FCC report (per secondary coverage) [19]. We covered this chain last week in AXT and Lumentum’s Prepayment Deal: The InP Substrate LTA Chain. The deal where Lumentum put down $87M in prepayments to reserve AXT’s substrate capacity.

The basis for the AXTI-victim view is real in itself. It is a Nasdaq-listed company whose substrate production sits entirely in a Chinese subsidiary (Tongmei), so if Beijing squeezes InP exports, revenue gets pressed immediately. There is precedent, too. After China put indium under export controls in February 2025, permit delays left Q4 2025 revenue below guidance [20].

But follow the story after that, and this frame is half the picture. Tongmei received its first InP export permits in June 2025 [21], and in 2026, with permits coming through better than expected, Q1 revenue rose 17% quarter over quarter, and Q2 saw record InP revenue of $30.7M and a swing to companywide profit (the profit swing is the company’s announcement; the InP detail is trade-press tally) [22]. Look at the institutional side too.

Under the Trump-Xi truce (October 2025), the US-bound embargo on gallium, germanium, and antimony is suspended until November 27, 2026 [23]. Indium is left out of that suspension and is managed under a separate licensing regime. The May 2026 White House fact sheet says China will address supply concerns including indium, but it is a unilateral US document, with no Chinese confirmation and no specific terms disclosed [24]. To sum up, the current regime is a licensing regime. Permits are still coming through in recent quarters, and easing is a direction on paper, not a confirmation.

Nor, of course, is AXT the only substrate company. Japan’s Sumitomo Electric and JX Advanced Metals are named alongside it as major suppliers, and we laid out this supply chain structure in AXT Inc. (AXTI) Deep Dive: The Hidden Bottleneck in AI Optical Interconnects. But the existence of alternative suppliers fails as a basis for AXTI falling. Indium metal, the substrate’s raw material, is mostly recovered from zinc-smelting byproduct streams, and China holds close to 70% of primary refining (about 68% per USGS, 2023) [19].

The actual sourcing and inventories of the Japanese substrate makers are not confirmable from public data, but it is hard to see them as fully free of that refining network. Coherent management, too, has said it sources substrates from multiple outside suppliers under multi-year contracts, and is understood to run the processes above that in its own fabs [19]. If China really squeezes indium, this entire layer goes on alert together. The picture of AXTI getting hit alone does not hold up.

Flip it around: AXT has to sell substrates for Coherent to make anything, and the same goes for AAOI. The very goal of US optical module expansion requires AXT’s shipments. So I put my weight on Trump and Xi keeping the dealmaking going and AXTI’s exports getting eased. The permit track record and the fact-sheet language above are the extent of my basis, and it is a forecast, not a confirmation.

And suppose the retaliation actually comes. What happens if InP exports get squeezed. If anything, InP becomes scarcer and more important. The burden gets shared across the entire Western optics industry that builds InP lasers, and within the range where permits hold, the scarcity value of whoever holds substrates goes up. Lumentum putting down $87M in prepayments to reserve capacity is the evidence of that scarcity value. So I read AXTI as a thermometer that shows the intensity of Chinese retaliation first.

Let me write down the limits too. One, scarcity only turns into money while shipments are possible. In a stretch where permits actually stop (Q4 2025 was that), thermometer or not, it is simply a victim. Two, the truce has an expiry. November 27, 2026 [23]. The fourth quarter, where the FCC text publication and this expiry overlap, is the test bench.

The more a regulation blocking Chinese modules succeeds, the more the West’s dependence on Chinese-linked materials chains surfaces as the next bottleneck. That is where the irony of this regulation lives.

## 7. Can You Build an AIDC Without Transceivers

In a situation where capex keeps growing, transceivers become more and more necessary, and more essential. We covered this in The GPU Repricing Cycle and Q2 Hyperscaler Earnings: Which Hardware Layer the Capex Flows To.

Buy tens of thousands of GPUs and without the optical links to tie them together, they don’t bind into a cluster. Just an expensive warehouse. So the question has to be flipped. Not who gets hurt if Chinese transceivers are blocked, but whether US hyperscalers can build AIDCs (AI data centers) without transceivers.

My answer is that they can’t, and so I think the essence of this draft is a repricing negotiation across the supply chain.

The case for buying optics is also coming through a path separate from the FCC. Jukan (@jukan05 on X), long read in semiconductor circles, wrote that in the short term the market has no choice but to sell memory and buy optical, and that some hedge funds already seem to have the position on [25].

The reasons are several, and the technical core is a reading of NVIDIA’s roadmap. The observation is that NVIDIA is responding to trimming Rubin Ultra’s HBM by tying multiple racks together with optics to hold the edge at the cluster level, and it holds even if the HBM trim is a supply-side rather than demand-side problem (both the positioning observation and the roadmap reading are per X commentary, not company-confirmed) [25].

If this observation is right, optical demand gets a third axis stacked on top of capex growth and regulation-driven scarcity: HBM substitution demand. Regulation and architecture are pointing at the same place for different reasons, that is, optical capacity. The bottleneck premium we covered in Compute Short, Memory Long is, this time, the picture of it moving one seat over from memory to optics.

Under an origin criterion, the regulation is close to symbolic and the rally gets given back. Under a nationality criterion, non-Chinese capacity gains temporary pricing power, but the size of that capacity (the $81M class) and the InP chain at the back end limit the transfer speed, so the stretch where hyperscalers pay bottleneck prices comes first. Either way, Innolight is holding the $6.8B, and judging by the first reaction on August 5 (A-shares -7.3%, H-shares -5.2%, recovered the next day), the market isn’t reading this as an existential threat either [3].

But let me also write down where I’d be wrong. If the FCC blocks new models from Chinese-designated entities immediately while minimizing the sale of already-approved models and the transition period, then it is not a repricing but an actual cutoff, and this article’s tone will have been too relaxed.

Conversely, if the draft itself runs aground (Cignal wrote that it is not yet convinced this situation is real [10]), the August 4 rally is material that gets handed straight back. Hyperscalers succeeding in buffering through stockpiling, so that the price spike never shows up, would also be a refutation of the bottleneck thesis.

The verdict material comes from dates. Whether the language of demand and lead times holds in the earnings calls packed into the week this article goes out: Lumentum August 11, Coherent the 12th, Fabrinet the 17th [15][16][18]. Let me also note the scene right before the gate. On August 10, Coherent fell 14% and Lumentum close to 9%, with the read being profit-taking ahead of earnings [26]. They enter the verdict days having already handed back part of the August 4 rally, which leaves that much more room for the earnings-call language to move prices. The FCC text publication and its definition clause, flagged for within the year [1]. Innolight’s interim report and the end of the listing stabilization period at the end of August. The November 27 expiry of China’s minerals embargo suspension [23]. And the cornerstone lock-up expiry on January 29, 2027 [5]. This article is the map from before those dates arrive. Whether the map was wrong is something I’ll write again then.

One addendum. The first piece of verdict material landed while this article was being finalized. Lumentum posted revenue of $1.006B (up 109% year over year), a non-GAAP gross margin of 50.4%, and guided next quarter to the mid-$1.2B range [27]. That is the language of shortage. And yet the stock slipped after hours. At a multiple in the 150s, even a beat is not enough, and now the ball moves to Coherent on the 12th.

### Acknowledgment

One trigger for this article was Cignal AI’s August post “FCC Ban on New Chinese Optical Modules”. The problem framing that the ban criterion (nationality versus production location) is undecided, and the initial awareness of the datacom market share figures, are borrowed from that post. Quantifying that undecided issue with the origin-based revenue in Innolight’s prospectus, the frame connecting the IPO proceeds’ uses to the enforcement gap, and the extension into the InP chain and the AXTI read are this article’s work. Where interpretations overlap (replacement capacity shortfall, transition taking years), they agree with Cignal’s assessment, and no paid subscription materials were used.

### References & Sources

[1] “Exclusive-Trump administration drafting ban on Chinese data center devices, sources say”, Reuters via AOL, 2026-08-04

[2] “Optical component stocks rally on proposed U.S. ban on Chinese tech”, Investing.com via Yahoo Finance, 2026-08-04 / “Optical Communication Stocks Rally as Trump Administration Plans to Ban Chinese Modules”, TradingKey, 2026-08-04 (intraday figures and cloud capex warning)

[3] “Zhongji Innolight (HKG:3308) Stock Price” / “Zhongji Innolight (SHE:300308) Stock Price”, Stock Analysis and HKEX quotes, as-of dates stated inline in the body

[4] “China AI supplier Zhongji Innolight slips in Hong Kong debut after $6.8 billion IPO”, CNBC, 2026-07-30

[5] “Zhongji Innolight Co., Ltd. Announcement of Final Offer Price and Allotment Results”, HKEX, 2026-07-29

[6] “Zhongji Innolight raises $6.81 billion in Asia’s second-largest listing of 2026”, Reuters via Yahoo Finance, 2026-07-29

[7] “Zhongji Innolight Rebounds After Buyback Plan, Easing Jitters Ahead of Hong Kong Debut”, Caixin Global, 2026-07-29

[8] “Zhongji Innolight Plunges In Hong Kong Debut As Global AI Trade Loses Steam”, Forbes, 2026-07-30

[9] “Zhongji Innolight Co., Ltd. Global Offering (Prospectus)”, HKEX, 2026-07-22 (US revenue share p.57, origin-based revenue p.213, TeraHop p.162)

[10] “FCC Ban on New Chinese Optical Modules”, Cignal AI, 2026-08

[11] “FCC Fact Sheet: Foreign-Produced Routers, Covered List and Conditional Approvals”, FCC, 2026-03 (primary) / “FCC bans Chinese routers over security risks”, FDD, 2026-03-25

[12] “Pentagon Adds 65 New Entities to the 1260H List of Chinese Military Companies”, WilmerHale, 2026-06-11

[13] “AAOI at 21st Annual Needham Technology, Media, & Consumer Conference (Transcript)”, 2026-05-13, remarks by CFO Stefan Murry

[14] “With FCC ban on new Chinese-made optical transceivers for DCs likely, it may be time to stock up”, Network World, 2026-08 (secondary)

[15] “Lumentum (LITE) Stock Price”, Stock Analysis, quotes as of 2026-08-10 close / “NVIDIA Announces Strategic Partnership With Lumentum”, Lumentum IR, 2026-03-02 / “Lumentum Form 8-K (Series A Convertible Preferred, $2B)”, SEC EDGAR / “Lumentum Announces Reporting Date for Q4 FY2026 Results”, Lumentum IR (August 11 schedule)

[16] “Coherent (COHR) Stock Price”, Stock Analysis, quotes as of 2026-08-10 close / “NVIDIA and Coherent Announce Strategic Partnership”, Coherent, 2026-03-02 / “Coherent Form 8-K (Common Stock Private Placement, $2B)”, SEC EDGAR / “Coherent Corp. FY2026 Fourth Quarter Conference Call Announced”, Coherent IR, 2026-07-22

[17] “Applied Optoelectronics Reports Second Quarter 2026 Results”, AAOI IR, 2026-08-06

[18] “Fabrinet (FN) Stock Price”, Stock Analysis, quotes as of 2026-08-10 close

[19] “FCC Transceiver Ban Would Cut 60% of AI Data Center Supply; Western Replacements Need Chinese Indium”, Tech Times, 2026-08-05 (secondary) / “Indium Statistics and Information”, USGS (basis for China’s ~68% of primary refining, 2023) / “Coherent’s Vertical Integration Strategy”, Chipstrat (management remarks summary, secondary)

[20] “AXT’s Q4/2025 revenue constrained by delay in China export permits”, Semiconductor Today, 2026-03

[21] “AXT Inc. Form 8-K: Tongmei Receives Initial Export Permits for Indium Phosphide”, SEC EDGAR, 2025-06-11

[22] “AXT, Inc. Announces Second Quarter 2026 Financial Results”, AXT IR, 2026-07-30 / “AXT returns to profit, driven by record quarterly revenue from InP”, Semiconductor Today, 2026-08 / “AXT’s revenue grows 17% in Q1 after greater-than-expected export permits”, Semiconductor Today, 2026-05

[23] “China suspends some critical mineral export curbs to the U.S. as trade truce takes hold”, CNBC, 2025-11-10

[24] “Fact Sheet: President Donald J. Trump Secures Historic Deals with China”, The White House, 2026-05 (indium mentioned, unilateral US document) / “China Rare Earth Export Controls: April Curbs Still Bite After Beijing Summit”, Tech Times, 2026-05-26 (secondary)

[25] Jukan (@jukan05) on X: short memory, long optical positioning comment, X, 2026-08-08 (market commentary, not company-confirmed)

[26] “Coherent Falls 12%, Lumentum Drops 7% as AI Optics Stocks Cool Ahead of Earnings”, Yahoo Finance, 2026-08-10 (intraday figures per the report; closes were COHR -14.2%, LITE -8.6%)

[27] "Lumentum Announces Fourth Quarter and Full Fiscal Year 2026 Results", Lumentum via Business Wire, 2026-08-11

> This article is an independent technical analysis published by PhotonCap, based on an engineering perspective. All content is derived from publicly available information and is intended solely for educational and informational purposes. In other words, nothing in this material should be construed as a recommendation to buy, sell, or hold any specific securities. Please note this carefully. The author may hold positions in the securities mentioned herein and reserves the right to trade such securities at any time without prior notice. Readers should conduct their own thorough review and research before making any investment decisions.
