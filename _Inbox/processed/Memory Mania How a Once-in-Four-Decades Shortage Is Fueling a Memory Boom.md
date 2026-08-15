---
publish: false
title: "Memory Mania: How a Once-in-Four-Decades Shortage Is Fueling a Memory Boom"
source: "https://substack.com/home/post/p-186096534"
author:
  - "[[Dylan Patel]]"
published: 2026-02-06
created: 2026-05-31
description: "Prices are doubling again, Supercycle is bigger, and could last longer than you think"
tags:
  - "clippings"
---
Prices of memory are going crazy. SemiAnalysis has been calling this out for over a year since late 2024. The scariest thing is that we aren't even close to the peak. We go through [fab by fab production](https://semianalysis.com/memory-model/) and [expansion](https://semianalysis.com/memory-model/) versus [detailed end market demand](https://semianalysis.com/memory-model/) by memory type to [forecast memory revenue, pricing, and margin](https://semianalysis.com/memory-model/) better than anyone else. This has all been detailed in the [SemiAnalysis memory model](https://semianalysis.com/memory-model/) for a while, but we will share it more publicly today. First some background.

## The Inevitability of Memory Cycles: A History of Booms and Busts

Since its commercial introduction in the 1970s, DRAM has benefited from the two scaling laws that defined the semiconductor industry: Moore’s Law and Dennard scaling. The 1T1C DRAM cell, with one access transistor and one storage capacitor, scaled for decades. Shrinking transistors reduced cost per bit, while clever capacitor engineering preserved sufficient charge to maintain signal integrity.

For much of the industry’s history, DRAM density scaled faster than logic, doubling roughly every 18 months instead of 24 months and driving dramatic cost reductions. As a commoditized product, manufacturers needed to sustain cost-per-bit declines to stay competitive. Suppliers who couldn’t compete on cost fell into a downward spiral: low sales left them short on cash to finance next-generation nodes, which in turn left them further behind on cost-per-bit. Many DRAM producers fell victim and went into bankruptcy, resulting in consolidation to just a few major players today.

For more details on the industry and DRAM basics, check out our technical deep dive:

Yet DRAM scaling has slowed significantly over the past few decades, and density gains over time have shrunk. Over the past decade, DRAM density has increased by only ~2× in total, versus roughly ~100× per decade during the industry’s peak scaling era. Capacitors are now extreme three-dimensional structures with aspect ratios approaching 100:1, storing just tens of thousands of electrons. For comparison, a small static shock when you touch a metal doorknob might involve the transfer of billions of electrons. The static charge on just a speck of dust might be 10,000x what is stored in a modern DRAM cell.

Bitlines and sense amplifiers, once secondary concerns, are now dominant constraints. Every incremental shrink reduces signal margin, increases variability, and raises cost.

![](https://substackcdn.com/image/fetch/$s_!CvGg!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda0878c8-fd9f-4bef-8ffc-109915c2a982_1001x558.jpeg)

Source: Micron

An easy way to understand the technical challenge in DRAM scaling is to think of a DRAM cell as a tiny bucket that holds electricity instead of water. Each bucket stores a bit of data by holding a small electrical charge. Over the years, engineers made these buckets smaller to fit more memory on a chip. At first this worked well. But today, those buckets are not just tall they are tall and narrow, each is like a tiny drinking straw standing upright. Because of the size each bucket now holds very very few electrons.

This is a problem. When the system tries to read the data, it has to detect this very faint electrical signal and distinguish it from noise. The wires that connect these cells (the “bitline”) and the tiny sensors that read them (called sense amplifiers) are now the main bottleneck. The signal is so weak that even small variations in manufacturing or temperature can cause errors.

![A graph showing a line of gold

Description automatically generated with medium confidence](https://substackcdn.com/image/fetch/$s_!Lw1D!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9f2fca5-03aa-4d33-96d8-cdace84b33b3_1379x684.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

Together, these constraints explain why DRAM density has stagnated and why DRAM scaling has slowed down significantly over the years. The collapse of DRAM scaling has far-reaching consequences across cost, architecture, and industry structure.

As density gains slow, cost per bit reductions have slowed down. DRAM pricing is now more dependent on capacity additions and cyclical supply-demand dynamics rather than technology-driven cost reductions which have been a powerful deflationary force.

## Memory Cycle Part II: Key Features of a Cycle

The memory industry has been defined by commoditization, which comes with cyclicality. This outcome reflects a combination of industry-wide competitive behavior, recurring lapses in capital discipline, and the nature of DRAM scaling we explained earlier.

At its core, memory’s cyclicality is driven by timing mismatches between demand changes and corresponding supply responses. Aside from the buffer of short-term inventories, DRAM supply is not very flexible. It can take years to bring meaningful new DRAM supply online, trying to meet demand that fluctuates daily.

Memory manufacturing, much like logic, is among the most capital-intensive industries in the world. Building leading-edge DRAM and NAND fabs requires multi-billion-dollar investments (which have steadily increased over the past few decades), multi-year construction timelines, extended yield-learning curves across successive process nodes, and lengthy ramp-up periods before meaningful volume production is achieved.

![A graph with blue and yellow lines

AI-generated content may be incorrect.](https://substackcdn.com/image/fetch/$s_!7rCY!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F215bf7a5-3f55-4472-bb84-fef718e8573f_908x602.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

These heavy capital investments mean that suppliers need to operate with high utilization rates to generate cash profits to earn a payback. However, utilization rates ultimately depend on market demand, which is influenced by a range of external factors (macroeconomy, end market sentiment, product cycle, etc). In practice, utilization can swing dramatically across cycles, ranging from roughly 95% in a supercycle to as low as 50% in significant downcycles.

Still, because the majority of the cost is already sunk, the fab is built and equipment purchased, suppliers are better off running wafers so long as they can sell bits above cash operating costs. Where demand is weaker than bit supply, prices go down as you’d expect. Elasticity within the market is always a hot debate.

Memory supply can be expanded by migrating to more advanced process nodes with yield improvements, which increases bit supply without requiring new “greenfield” wafer capacity additions. For example, Samsung’s leading-edge 1c DRAM process node delivers roughly ~70% higher bits output per wafer compared with its 1a node. This means that on a per-wafer basis, a 1c-node DRAM wafer can deliver roughly 70% higher bit output than a 1a-node wafer (assuming the same yield), meaning significantly more memory supply from the same amount of raw material.

The impact of node migration, however, is dynamic over time. When a new node is first introduced, initial yields are typically lower, limiting effective output as well as wafer capacity, given the potential new equipment introduction, replacement, and ramp-up timeline. As yield learning progresses and node migration expands, the bit output per wafer increases materially, resulting in more bit supply even if wafer output is held constant.

Another thing is that node transitions do not halt simply because demand weakens. Consequently, bit supply growth can remain robust well into downturns. This exacerbates oversupply and downward price pressure.

In a downturn, the impact of pricing declines can be existential for memory suppliers. By the time pricing rolls over, manufacturers have already committed and deployed multi-billion-dollar capital investments into fabs and equipment that cannot be economically idled. As demand weakens, utilization rates fall, fixed costs are under-absorbed, and cash generation deteriorates rapidly. The result is a sharp compression in gross margins and an inability to earn an adequate return on invested capital precisely when balance-sheet stress is rising.

The risks inherent in “memory economics” are high. A highly commoditized product with elastic demand versus a capex-heavy, long-timeline, inelastic supply produces a challenging, cyclical market.

During the Windows PC supercycle of the early to mid-1990s, there were approximately 20 meaningful DRAM suppliers. Elevated demand and strong pricing attracted aggressive capital investment and new entrants. Subsequent downcycles systematically eliminated the weaker players. From roughly 20+ players in the mid-1990s, the number of players contracted to the mid-teens in the 2000s and early 2010s, to fewer than 10 relevant suppliers in the 2020s. Today, there are only 3-4 material suppliers.

![A table with text on it

AI-generated content may be incorrect.](https://substackcdn.com/image/fetch/$s_!hXg_!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fb0f177-f9a5-4147-9e2f-0841704ab3ba_1000x492.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

From a demand perspective, memory consumption is not always linear or predictable. During mature phases of existing product cycles, demand growth can be relatively stable, driven primarily by incremental unit growth or stable increases in memory content per device. However, during “inflection periods,” when new computing platforms or architectures emerge as primary demand drivers, memory demand can shift abruptly. During these periods, memory consumption tends to grow non-linearly if not explosively.

There have been several of these product cycle inflections over the past few decades. New computing platforms like the PC, the smartphone, cloud computing, and now AI accelerators drove abrupt increases in both the number of systems and memory content per system. In prior cycles, these demand inflections often caught memory suppliers off guard, a dynamic we will discuss in the following section.

However, such inflection-driven upcycles have not been sustainable in the long run. Prior memory supercycles have tended to peak and roll into downcycles within one or two years, as elevated profitability drives aggressive capital investment, accelerated capacity expansion, and faster-than-anticipated bit supply growth. These supply responses, combined with the inherently cyclical nature of end demand, have consistently led to oversupply and subsequent market corrections.

![A graph showing a line graph

AI-generated content may be incorrect.](https://substackcdn.com/image/fetch/$s_!TIHQ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F850df7aa-8ff6-4027-a6bd-fb09a5539e63_1176x678.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

From a financial market perspective, participants are forward-looking. Investors anticipate shifts in the supply–demand balance and pricing well before supplier earnings and margins actually peak. We see this almost in every single memory cycle over the past three decades.

There are a few especially interesting examples, worth revisiting in the context of the current memory supercycle: the 1993 Windows PC supercycle, the cloud and mobile upcycle in 2010, the 2017-2018 supercycle from cloud and NAND, and the unexpected upcycle during Covid-19.

During the 1993 memory supercycle, the DRAM industry entered a strong upcycle driven by the rapid adoption of Windows PCs and the broad implementation of graphical operating systems. Unlike prior generations of personal computers, Windows PCs transitioned from text-based interfaces to GUI (Graphical User Interface)-driven computing, which dramatically increased DRAM requirements per system. Average DRAM content per PC jumped from roughly 1–2MB to 4–8MB, representing an approximate 4× increase in memory content per device. This step-function increase in DRAM intensity coincided with accelerating PC adoption, with unit shipments growing at roughly double-digit rates.

![A graph with a line going up

AI-generated content may be incorrect.](https://substackcdn.com/image/fetch/$s_!KY1M!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5bd12968-1a9f-42fc-a873-dd2333a6f405_1232x752.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

On the supply side, the industry was emerging from a prolonged downturn in the late 1980s because of intensified competition, declining margins, and a significant shakeout among U.S. and European DRAM suppliers. As a result, capacity expansion had been constrained and yields were uneven, leaving the supply suppliers ill-prepared to absorb the sudden surge in demand. With this perfect setup in both supply and demand, an industry shortage inevitably occurred. During 1993 and 1994, DRAM demand outpaced supply despite most fabs running at full utilization. Spot and contract prices for 4Mb and 16Mb DRAM rose sharply, and gross margins for leading suppliers surged well above 50%.

![](https://substackcdn.com/image/fetch/$s_!H3iI!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe984e7a-d5c7-4e92-9147-bc1b3009e075_986x676.png)

Source: SemiAnalysis estimates

Unsurprisingly, this set the stage for a downturn. Japanese incumbents and then-emerging Korean players responded with aggressive capacity expansion—bringing new fabs online and accelerating process shrinks. This was reflected in global semiconductor manufacturing spend as the supercycle took hold, with capex as a percentage of semiconductor production rising steadily and at one point exceeding 30%. Reinforcing this late-cycle signal, roughly 50 fab construction plans were announced during 1995–1996 alone.

Rapid yield improvements further amplified supply, driving a sharp increase in bits per wafer. By 1995–1996, the market gradually flipped from shortage to oversupply. This led to sharp price declines of more than 60%, forcing widespread exits and accelerating industry consolidation.

![](https://substackcdn.com/image/fetch/$s_!qAAO!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43d9692c-b9f0-4d1f-a448-be98079aa4aa_1074x644.png)

Source: Integrated Circuit Engineering, SemiAnalysis

The 2010 memory supercycle started in roughly the 2nd half of 2009, driven by two simultaneous demand inflections: (1) the smartphone rapid adoption globally, led by the iPhone and a rapidly proliferating Android ecosystem, and (2) the early hyperscaler buildout wave (e.g., Google, Amazon, Facebook). Server DRAM intensity increased due to virtualization and scale-out services. Supply growth was muted as suppliers drastically cut investment in the poor macro environment post the Global Financial Crisis.

On top of this, smartphone demand growth was a near-vertical volume step-up. Global smartphonec by broader Android price-tier penetration and iPhone scaling. On the cloud side, while the servers’ shipment growth increased much more slowly compared to mobile during that period, the key change was the DRAM content per server. The industry was shifting toward higher-memory configurations to support consolidation, virtualization density, and early big-data workloads. DRAM content per server increased from single-digit gigabytes (GBs) to tens of GBs, representing a significant step-function increase in memory intensity per system.

![](https://substackcdn.com/image/fetch/$s_!5i8t!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a8fc3e9-5953-4099-a61b-6e348ad015e6_988x676.png)

Source: SemiAnalysis estimates

Similar to prior cycles, the sudden demand surge combined with constrained supply drove a meaningful increase in DRAM pricing. What differentiated the 2010 cycle, however, was the rapid rise of LPDDR within the overall DRAM mix as mobile demand scaled. Because LPDDR products are mostly more cost- and price-efficient and are sold into more price-sensitive end markets, the resulting pricing uplift was materially less dramatic than prior PC-driven supercycles. The pricing characteristics of LPDDR have remained structurally consistent to this day.

Moreover, DRAM pricing in this cycle peaked earlier and rolled over more quickly than in previous upcycles. Pricing momentum proved difficult to sustain even within the nominal upcycle window. The DDR3 2Gb contract pricing fell ~46% from its 1H10 peak of ~$46.5 to ~$25 by November 2010. By 2011, the correction had broadened further, with a further correction of DRAM pricing.

Another key development of this cycle was the rapid standardization of mobile DRAM which further accelerated commoditization. LPDDR2 was standardized by JEDEC in 2009, pushing mobile DRAM into a tightly specified, consumer-oriented market structure that limited supplier differentiation and therefore pricing power. These factors together only compressed the length of the upcycles and time to reach the downcycle starting roughly in 2nd half of 2010 and following years.

The 2017–2018 memory supercycle is still a fresh memory for many in the industry and is oft-cited as a good analogue for today’s supercycle. On the demand side, the key driver was server upgrades and buildouts, driven by virtualization, scale-out architectures, and increasingly memory-intensive workloads. DRAM content per server increased materially, shifting demand toward higher-capacity configurations. Server DRAM also enjoys higher ASP and margins compared to PC and mobile, and is therefore more profitable for suppliers.

This pricing environment translated directly into record financial performance, peaking in 2H18. Memory suppliers generated unprecedented levels of free cash flow, and gross margins expanded to levels previously thought unattainable for a commoditized industry.

Yet, as with the prior cycles, the fundamental cyclical dynamics of the industry prevailed. A few familiar factors developed in late 2018 and 2019: (1) supply growth re-accelerated as manufacturers responded to elevated pricing with aggressive capacity additions and technology ramps, and (2) demand growth normalized as end markets absorbed excess inventory and hyperscaler purchasing slowed. Oversupply drove pricing down, and the cycle spiraled downwards.

The most recent DRAM upcycle was catalyzed during the COVID-era “chip crisis,” an unprecedented synchronization of demand shock and supply disruption. Global lockdowns caused abrupt shifts in end markets, including work-from-home, remote education, cloud usage, and digital entertainment. These unexpected social changes drove a sudden surge in demand for PCs, servers, networking equipment, and consumer electronics. All of these categories are DRAM-intensive, and no pre-pandemic forecast could have reasonably foreseen the changes.

Beyond surging end-demand, purchasing behavior amplified the cycle, especially from the enterprise side. OEMs, hyperscalers, and channel partners were taking a defensive posture, aggressively placing years’ worth of orders to secure supply amidst uncertainty. This led to widespread double- and triple-ordering across the supply chain.

From the DRAM suppliers’ perspective, it became increasingly difficult to distinguish true end-demand from panic ordering. The result was a rapid drawdown of industry inventories and a sharp tightening of spot and contract markets, pushing DRAM prices materially higher at their 2021 peak.

On the supply side, the industry was structurally constrained. During the pandemic, suppliers faced additional friction from labor shortages, logistics disruptions, and delayed equipment deliveries. Even where capex budgets existed, wafer output could not be ramped quickly. At the same time, most suppliers had entered the pandemic period with a relatively disciplined supply posture following the painful 2018–2019 downturn, limiting their ability and willingness to add more capacity in response to short-term pricing signals.

Capex decisions during this period were therefore cautious and selective. Rather than aggressive greenfield expansion, memory suppliers prioritized node migration and productivity improvements within existing fabs. Advanced-node DRAM transitions were already becoming more complex and capital-intensive, with diminishing bit-growth returns per wafer as scaling challenges increased. This meant that even elevated capex levels translated into less incremental supply than in prior cycles. The pandemic-era upcycle thus reinforced a structural shift: supply growth became increasingly constrained not just by capital discipline, but by physics and process complexity.

Crucially, this cycle reset industry behavior and expectations. Memory suppliers emerged with a stronger appreciation for disciplined capex, tighter inventory management, and the value of prioritizing higher-margin products over pure bit growth. Customers, meanwhile, recognized the fragility of semiconductor supply chains and the strategic importance of securing memory capacity. These dynamics laid the foundation for the current supercycle by creating a structurally tighter supply. In this sense, the COVID-era DRAM upcycle was not just a temporary dislocation, but a formative event that reshaped the memory industry’s supply-demand balance heading into the current cycle.

## AI-Driven Memory Supercycle: Bigger, Longer, and a Shortage that is Harder to Solve

For those who have lived through multiple memory cycles, the central question when it comes to this supercycle is the same: *when will this cycle peak?* It is natural that both investors and the supply chain remain cautious, particularly as memory stocks rally sharply over short periods. In our view, however, while there are clear similarities to prior cycles, this supercycle is shaping up to be both larger and longer in duration, driven by dynamics that are very much unique to this cycle.

Currently, the DRAM industry is operating in a deeply supply-constrained environment, and based on our [Memory Industry Model](https://semianalysis.com/memory-model/), we believe the supply–demand imbalance is deteriorating rather than normalizing. Total DRAM supply is projected to remain approximately…

*Below, we share:*

- *Our forecast for DRAM and HBM supply/demand mismatch from our Memory Industry Model, through 2027*
- *HBM4 qualification: how is each supplier doing, market share % for Rubin*
- *DRAM wafer- and bit-capacity data with HBM broken out*
- *Upgrades forecast: trends in wafer capacity by node with fab-by-fab details*
- *DRAM pricing forecast out through 2027*
- *Last, we discuss the factors and timing for the end of the cycle*
- *As a bonus, we’ve also included DRAM EUV layer trends and WFE capex forecasts*

…7% below demand in 2026. Within this, the HBM shortfall is expected to widen from ~5% this year to ~6% in 2026, and further to ~9% in 2027.

Importantly, commodity DRAM is also forecast to remain structurally tight, with an estimated ~7% supply deficit persisting through both 2026 and 2027. At this degree of imbalance, the DRAM market is confronting what we characterize as a “dual-shortage dilemma,” a dynamic we will explore in greater detail later.

![A graph of a supply and demand

AI-generated content may be incorrect.](https://substackcdn.com/image/fetch/$s_!6F4h!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cdcbeda-96ec-45ed-b1c7-d79f6d9901e0_984x644.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

This magnitude of shortage is rare in the modern history of the memory industry, both in terms of its severity and its duration. Even during the 2017–2018 memory supercycle, the supply–demand gap was closer to the mid-single-digit range, making the current environment meaningfully tighter by comparison. Moreover, this shortage is likely to persist for far longer than the prior upcycles discussed above.

In our view, three key and interrelated drivers underpin this ongoing supercycle and are likely to sustain the supply shortfall through 2027 and potentially 2028, with each continuing to play a critical role as the cycle evolves:

![](https://substackcdn.com/image/fetch/$s_!lsKv!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce44efb7-39b3-4b9a-840b-cf3d48965a29_692x492.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

First is the accelerating HBM/DRAM demand and HBM’s rapidly expanding capacity. The surge in compute demand is translating into a sharp increase in memory requirements over a very short period, driven by DRAM demand across the data center. This includes DDDR/LPDDR/HBM in AI servers and DDR in general-purpose servers. As a result, demand has risen meaningfully across both commodity DRAM and HBM, which both obviously will utilize a lot of industry’s capacity.

Beginning around 2023, we have observed a clear and steadily accelerating trend in HBM demand, accompanied by increasingly aggressive responses from memory suppliers to expand HBM production capacity and step up investment to capture this rapidly growing compute demand. Exiting 2023, the three major memory suppliers had dedicated only **~123kwspm** of wafer capacity to HBM. By **year-end 2025**, this figure had increased to **~331kwspm,** representing **more than a ~2.7× expansion** in wafer capacity allocated to HBM over just two years.

![](https://substackcdn.com/image/fetch/$s_!-f7p!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8ff2338-f109-4e9e-98bb-1ae3edc90396_1452x1054.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

And the capacity expansion in HBM is far from complete. We believe additional capacity expansion is already underway, with HBM wafer capacity reaching approximately 473kwspm by year-end 2026 and ~668kwspm by year-end 2027. This implies that over the next two years, HBM wafer capacity will expand by more than 2× (again), meaning the HBM wafer capacity of three memory players is going to 5x within 4 years.

But what’s important here is not just the significant capacity expansion in HBM, but also a meaningful trade-off between HBM and commodity DRAM wafer allocation, given the limited existing capacity as well as time for incremental wafer capacity to come in the next two years

The impact of materially expanding HBM capacity is unambiguous. When we examine HBM’s wafer intensity within overall DRAM production, we find that HBM wafer capacity as a share of total DRAM wafer capacity at Samsung, SK hynix, and Micron was below 5% in 2022, but has already increased to approximately 20% by year-end 2025. By the end of 2027, we estimate this figure will reach ~35%. This implies that HBM alone will consume more than one-third of the combined DRAM wafer capacity across the three suppliers, directly displacing capacity that would otherwise be available for commodity DRAM production.

One may ask why memory makers are moving so aggressively to expand HBM capacity. We believe the rationale is twofold. First, HBM is increasingly viewed as a structural and sustainable growth engine that extends well beyond traditional memory end markets such as PCs, mobile, and automotive. This is reinforced by the continued increase in HBM intensity within AI servers (both GPU and ASIC), where HBM remains indispensable for both model training and inference. As a result, rising HBM content per AI server should meaningfully drive incremental demand going forward.

Second, HBM’s complex front-end and back-end manufacturing requirements enable greater product differentiation relative to commodity DRAM. Performance characteristics such as pin speed, power efficiency, thermal capability, and packaging integration vary meaningfully by supplier compared to conventional DRAM, allowing memory makers to distinguish their products more clearly. This differentiation creates room for pricing power, incremental margin capture, and market share gain, in contrast to commodity DRAM where competition is driven largely by cost and scale. SK hynix’ success in both HBM3 and HBM3E should be the best example for this.

Yet, such a significant expansion of HBM capacity carries meaningful cost and strategic challenges. As memory manufacturers increasingly allocate both existing and incremental wafer capacity to HBM, they not only materially constrain capacity available to traditional DRAM end markets but also reduce overall DRAM bit output due to HBM’s lower bit conversion rate. The result is an even tighter commodity DRAM supply environment, even as total industry wafer capacity expands—reinforcing supply pressure across the broader DRAM market.

The first-order impact requires little explanation: reallocating wafer capacity to HBM directly reduces the number of wafers available for commodity DRAM production. However, the second-order effect is equally important and sometimes underappreciated. A wafer dedicated to commodity DRAM typically delivers roughly 3× the bit output of a wafer dedicated to HBM in the case of HBM3E 12-Hi. Based on our estimates, this gap is likely to widen to nearly 4× as the industry transitions to HBM4 later this year and potentially even more in HBM4E the following year.

![](https://substackcdn.com/image/fetch/$s_!WeYd!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4c4173d-ea41-412f-9176-c109c78f42e9_1274x810.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

HBM uses larger die sizes as each HBM stack consists of multiple large DRAM dies optimized for bandwidth rather than density. HBM’s larger die size is due to the presence of through-silicon vias (TSVs), which require dedicated keep-out zones that reduce usable array area and inflate die size. This materially reduces the number of dies that can be harvested per wafer compared to commodity DRAM dies. HBM, compared to commodity DDR DRAM, also demands much greater cell performance, which dramatically reduces front-end sort yields for HBM wafers.

HBM also requires TSV and a series of incremental process steps—including wafer thinning and backside processing—that do not exist in standard DRAM manufacturing. These steps add complexity and introduce incremental yield loss, further reducing effective bit output per wafer.

![A screenshot of a computer

Description automatically generated](https://substackcdn.com/image/fetch/$s_!rRPm!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17e81e7d-7b59-452d-9392-3b6c882c74ec_1205x672.png)

Source: Applied Materials

Stacking and advanced packaging (primary bonding) yields also meaningfully impact HBM output. Even when individual DRAM die yields are high, the compounded yield across 8-high or 12-high stacks is structurally lower, as a single defective die can compromise the usability of an entire stack. This stands in contrast to commodity DRAM, where each die is sold independently, and yield losses are more localized. Finally, HBM products prioritize bandwidth and power efficiency over maximum density, limiting the degree to which bit scaling can offset these inherent inefficiencies.

![A diagram of a graph

Description automatically generated](https://substackcdn.com/image/fetch/$s_!8I-r!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F837ce30a-e3d0-49e4-ade6-5054a2205f43_1171x660.png)

Source: SK Hynix

We think what distinguishes this cycle is that the product transition driving demand - HBM - is far more manufacturing-intensive, effectively introducing a form of reverse scaling. Unlike prior computing platform inflections that primarily expanded demand without materially constraining supply, the AI-driven shift toward HBM simultaneously boosts demand while tightening supply. This dynamic is further amplified by rising server DRAM content, including emerging LPDDR5-based products such as SOCAMM and SOCAMM2.  
  
NVIDIA, for example, the transition from Blackwell to Blackwell Ultra and Rubin increases HBM capacity by ~50%, with Rubin Ultra driving a further ~4× jump in system memory from 288 GB to ~1 TB. Similarly, ASICs such as Goole’s TPU v8AX and Amazon’s Trainium3 also migrating from HBM3E 8-Hi to 12-Hi stacks, while AMD’s memory capacity increases materially from ~288 GB in MI350 to ~432 GB in MI400. At a high level, it is not difficult to envision the magnitude of DRAM demand required to support both existing and next-generation AI compute platforms.

We estimate that HBM demand alone will account for more than 10% of total DRAM demand by the end of 2027, layered on top of the already substantial server DRAM contribution, which is about 40% of total DRAM end market. Given the DRAM content increases discussed earlier and robust demand across both AI and general-purpose servers, we believe the importance of servers within the overall DRAM end market will continue to increase over the next few years, and is already seen as a top priority for memory suppliers over other categories.

![](https://substackcdn.com/image/fetch/$s_!Deks!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d99059a-6f0d-43a6-bd30-ef787589ccc8_1130x742.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

The HBM–DRAM conundrum becomes even more complex when factoring in market reactions to the worsening DRAM shortage driven by HBM capacity reallocation. As commodity DRAM supply has tightened materially due to HBM expansion, pricing and margins have surged over the past several quarters. Commodity DRAM margins are now on par with—or in many cases exceeding—HBM margins since late 4Q, a trend we believe will persist over the next few quarters. This is particularly the case for Samsung, which has lower margin in producing HBM. We first highlighted this development in our [Core Research](https://semianalysis.com/core-research/) numerous times last year.

We view this as a significant and crucial challenge for memory suppliers. Given the combination of an attractive margin outlook and superior bit output from manufacturing and selling commodity DRAM, alongside the increased manufacturing complexity associated with HBM4, some suppliers may adopt a more deliberate approach in 2026—carefully balancing HBM capacity expansion against conventional DRAM production. This dynamic is likely to be more pronounced for suppliers that perceive their near-term ability to gain HBM share to be constrained by product competitiveness and aim to exploit commodity DRAM to maintain it memory business performance.

One major contributor to the current shortage that we have not yet discussed in depth is limited cleanroom availability. Following the memory upcycle during the pandemic, memory suppliers adopted a more conservative approach to capex and capacity expansion. This caution resulted in an underinvestment backdrop entering 2025 and extending into 2026. As demand has continued to accelerate, memory suppliers are now constrained by insufficient cleanroom capacity, limiting their ability to respond on the supply side.

As we track DRAM capacity additions across all major suppliers, we estimate that virtually all incremental wafer capacity in 2026 will be concentrated in just three fabs: Samsung’s P4 (mostly Phase 1 and Phase 3 with limited input for Phase 4 in late ‘26), SK hynix’s M15X, and Micron’s A3. Importantly, both Micron’s A3 and SK Hynix’s M15X are expected to be predominantly allocated to HBM production rather than conventional DRAM, which will limit the incremental wafer and bit output.

Samsung’s P4 Phase 4 is likely to come online later this year, following the fully equipped Phase 1 and 3. Although Phase 2 of P4 was initially scheduled to come online in 1Q27, we believe the timeline could be pulled forward. Even that, we think the material wafer output contribution of Phase 2 should still come in 1H27.

SK hynix’s Yongin Phase 1 is not expected to bring its cleanroom online until February 2027, with only limited wafer output beginning in 3Q27 due to time for equipment move-in and qualification, while Micron’s Idaho Fab 1 is now targeting mid-2027 with wafer output likely also in 3Q27.

Even Micron’s recently acquired P5 Tongluo fab from PSMC is unlikely to contribute meaningful wafer output until 2H27. At full utilization, the site offers a maximum capacity of approximately 45k wafers per month for commodity DRAM, with effective output potentially lower if the fab is configured for HBM production due to greater cleanroom requirements for back-end equipment such as TC bonders and a more complex manufacturing process.

With these constraints in mind, the central question is how the industry can meaningfully expand bit supply. We currently forecast ~21% bit growth this year and ~19% next year. In our view, the primary driver of this growth will be accelerated node migration to 1b and 1c across the three major memory suppliers. Achieving this growth requires a faster pace of transition to these nodes, which deliver materially higher bit output per wafer than trailing nodes and seem to be t the most effective remaining lever for bit expansion in a wafer-constrained environment.

Accordingly, we expect the combined 1b and 1c capacity across the three major memory suppliers to increase by approximately 80% from year-end 4Q25 through 4Q27. Specifically, we believe that by the end of 2026, Samsung and SK Hynix should have close to 30% of their DRAM wafer production on the 1c process node, or at least be targeting a level approaching this threshold. Micron should also be able to allocate roughly 30% of its DRAM production to the 1c (or 1γ) node.

![](https://substackcdn.com/image/fetch/$s_!X-sw!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa112c5f0-8638-410d-ac1f-81cbf973347d_1047x757.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

This is a storyline we have mentioned and seen in previous DRAM upcycles, where the memory suppliers are leveraging node migration for more bit output to fulfill demand.

Yet one should note that DRAM node migration introduces meaningful execution friction. New tool sets must be installed, process windows re-optimized, and yields typically deteriorate during the initial ramp phase. As a result, effective wafer capacity and bit output at transitioning fabs often decline for a few quarters before recovering as yields stabilize and learning curves are climbed. The practical implication is that portions of the installed base across all three major memory suppliers will likely experience temporary overall capacity and bit-output disruptions during this transition but a long-term gain in terms of bit output.

## Supercycle Could be a Double-Edged Sword

Unsurprisingly, the first dynamic to emerge in a memory supercycle is an accelerating price uptrend across DRAM products, consistent with patterns observed in prior cycles. For example, DDR5 and LPDDR5 pricing have surged over the past year. We model 1Q26 QoQ contract price increases of 70% for DDR5 and 35% for LPDDR5, pushing prices to approximately $14/GB and $11.5/GB, respectively, by the end of the quarter. Relative to 1Q25, this implies extraordinary YoY price increases of 638% for DDR5 and 369% for LPDDR5.

As we believe the structural shortage is unlikely to improve and the supply environment is set to worsen, DRAM pricing could increase by another ~2× on a 4Q25 versus 4Q26 basis. This is a very favorable setup for leading memory suppliers, although not necessarily beneficial for everyone.

![](https://substackcdn.com/image/fetch/$s_!M-HO!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff863035e-5d8c-4655-97cf-b4222b9eba04_1094x616.png)

Source: SemiAnalysis Memory Model - Sales@SemiAnalysis.com

Memory price increases are clearly beneficial for memory manufacturers, they come at the expense of customers and the broader end markets. Rising memory content as a share of BoM is creating broad-based margin pressure for mobile and PC OEMs, with the impact varying by scale, pricing power, and product mix. Tier-1 players such as Apple are structurally better positioned due to superior procurement leverage and strong iPhone 17 demand. We estimate Apple faces roughly ~15% memory price increases versus ~20% for the broader industry; however, even Apple is unlikely to be immune, as higher memory costs should still weigh on margins into 2026, with limited evidence to date of ASP increases sufficient to fully offset this pressure. Apple’s latest earnings commentary confirmed this and suggested that the larger impact from memory will begin in 2H26, despite more favorable positioning in 1H26.

In contrast, Tier-1.5 and Tier-2 mobile OEMs—particularly Chinese vendors—face significantly greater margin stress given limited ability to pass through higher costs. This is already driving selective price increases and potential specification downgrades, especially in entry- and mid-range devices, where gross margins could compress sharply if memory prices rise further. High-end models are less likely to see specification cuts but may eventually face price increases should elevated pricing persist. With the price hike, we think the mobile shipment outlook should be downgraded in 2026, and we are seeing clear signs across companies participating in the supply chain.

A similar dynamic is emerging in PCs, where OEMs have already implemented selective price increases and are considering specification downgrades in mid- and lower-tier products since 4Q25. Compounding the pressure from rising memory costs, PC OEMs are also facing higher processor pricing. This “double hike” materially increases the risk of ASP inflation, weaker demand elasticity, shipment declines into 2026, and downstream earnings pressure for chipmakers and ODMs with high exposure to PC and mobile volumes.

As a result, we remain cautious—and in some cases bearish—on select names across this ecosystem. Given the potential impact on demand elasticity, it will be critical to closely monitor shipment trends in both PCs and mobile, which together account for roughly ~30% of total DRAM end demand, as any meaningful volume deterioration could weigh on overall end-market demand. Nonetheless, given the increasing weight of servers in the DRAM end market and accelerating server DRAM demand, we believe this should more than offset demand softness in consumer DRAM.

Beyond mobile, PCs, and other consumer electronics, we believe it is also important to consider the impact of “memoryflation” on AI servers and ODMs as the industry should gradually see a meaningful impact from the memory and storage price hike. We highlighted this last week on our institutional platform, Core Research.

For further details, please refer to our [AI TCO Model](https://semianalysis.com/ai-cloud-tco-model/) and [Core Research](https://semianalysis.com/core-research/), where we provide a detailed BoM breakdown and analysis of memory’s impact on AI server economics.

![](https://substackcdn.com/image/fetch/$s_!h9Ft!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5806b684-cf4c-47f2-980e-77f9a0f42515_1638x1152.png)

Source: SemiAnalysis Core Research, AI Cloud TCO Model, and Memory Model

## HBM4 Competition and HBM3E Pricing

Unlike commodity DRAM, HBM typically provides suppliers with greater visibility and long-term volume commitments, but it also limits the ability to raise prices intra-year. This model is advantageous during downcycles or modest upcycles, as it supports more stable earnings and margins. However, in a supercycle of this magnitude, it can cap upside relative to commodity DRAM, where pricing can “re-rate” much more rapidly. This asymmetry is a key reason we turned bullish on Samsung while holding a bullish view on SK Hynix, which [Core Research](https://semianalysis.com/core-research/) subscribers learned in our November note. There, we highlighted Samsung’s significantly greater exposure to commodity DRAM relative to its peers.

The pricing impact is evident, but in reality, it has proven far more significant than many expected. The rapid escalation in commodity DRAM pricing is now influencing pricing negotiations for HBM3E 12-hi and, likely, HBM4 this year.

Back in early 4Q25, market consensus shifted toward a roughly 15–20% ASP decline for HBM3E 12-hi in 2026. This will not be the case in our view, which we noted to our institutional client last month. Flat pricing for HBM3E 12-hi in 2026 is now a more reasonable assumption, given the current pricing environment, a higher-than-expected mix of HBM3E, potential incremental orders tied to H200 demand, and tightening HBM3E supply as HBM4 ramps later this year. For Samsung, which priced HBM3E below both SK Hynix and Micron in 2025, a 10–15% price increase is achievable this year, supported by improving HBM3E 12-hi performance and rising shipment volumes this year.

It’s also important to address the HBM4 qualification progress: based on our supply-chain checks, the latest HBM4 engineering samples from memory suppliers remain below target specifications in terms of pin speed. We [noted](https://semianalysis.com/accelerator-hbm-model/) this to our client of the [Accelerator & HBM model](https://semianalysis.com/accelerator-hbm-model/) update in early January. The samples from both Samsung and SK Hynix are operating at approximately 10 Gbps, while Micron’s HBM4 samples are exhibiting much lower pin speeds, which will impact their share and ramp-up timeline for HBM4. This gap underscores the increased technical complexity of HBM4 and the higher likelihood of issues during ramp-up for memory suppliers.

At a more granular level, Samsung’s HBM4 front-end (1c) appears competitive on both performance and power efficiency, in some cases consuming less power than SK Hynix. However, Hynix continues to demonstrate an advantage in signal integrity, with lower jitter reflecting stronger package-level execution. With respect to Micron, despite management’s stated confidence in HBM4, we remain skeptical of execution given persistent challenges in meeting NVIDIA’s required pin speeds. More specifically, we believe the HBM4 competition is likely to consolidate into a two-player race led by the Korean memory suppliers, particularly in the case of NVIDIA, the largest end customer for HBM4.

That said, even as Samsung narrows the performance gap in HBM4, SK Hynix’s proven track record and reliability continue to position it as the dominant HBM supplier for Rubin. Accordingly, for R200-class HBM supply, we envision SK hynix capturing approximately ~60% share, followed by Samsung at ~30%, with Micron accounting for none in the first 12 months of Rubin.

As we move into 2Q this year, we expect to gain improved visibility into the HBM4 competitive landscape. Memory suppliers should continue to enhance HBM4 quality and yield and actively advance mass-production readiness as the industry transitions from HBM3E to HBM4.

We believe the technical complexity of HBM4 could pressure supplier margins due to a more difficult yield learning curve and slow the pace of the product mix transition relative to prior expectations. As a result, HBM3E is likely to represent a higher mix of the overall HBM portfolio in 2026 than some initially forecasted. We think the meaningful crossover to HBM4 should happen in 2H26.

## How the Cycle Will Evolve

History suggests that even the largest memory supercycles do not last indefinitely, and we believe this cycle will be no exception. That said, as we have previously maintained, we think this cycle could be larger and last longer than prior cycles. In our view, the supercycle can extend through 2027, with conditions becoming more challenging and volatile in late 2027 and into 2028—a view some may consider aggressive, but one echoed by many industry participants we spoke with, though not universally shared. A few things we think are going to happen, and some are already happening:

- **More fab pull-ins and capacity expansion:** We expect additional fab schedule pull-ins across all three major memory suppliers as capacity expansion plans accelerate, and we are already seeing early evidence of this trend. SK hynix has pulled in the schedules for both its M15X and Yongin Phase 1 fabs. Micron is also accelerating capacity, pulling in its Idaho 1 ramp from 2H27 to mid-2027, while its recent acquisition of PSMC’s fab adds up to ~45k wafers per month of potential capacity, which is expected to begin contributing wafer output in 2H27 with gradual ramp-up timeframe. Capacity expansion will come more meaningfully when memory supplier’s cleanroom coming online mostly by the end of 2027, and we might hear additional news on its future capacity expansion plan.
- **Significant node migration:** As previously outlined, we believe the industry will undergo large-scale node migration to 1b and 1c over the next two years, which is confirmed by ASML and LRCX’s management in the latest earnings call. This shift is driven by 1) a significant need to increase bit output without much new wafer capacity and 2) 1c-based HBM4E in 2027
- **Ongoing HBM acceleration and sustained pressure on commodity:** We believe memory suppliers will continue to prioritize HBM as their top strategic focus, given its structurally superior returns and long-term growth potential relative to commodity DRAM. While conventional DRAM is also entering a highly favorable pricing environment, HBM represents a more sustainable and strategically important opportunity over the long term. As a result, we expect the tension between allocating capacity to HBM versus commodity DRAM to remain top of mind for memory company executives.

A unifying theme across these three developments - fab pull-ins, accelerated node migration, and increased HBM prioritization - is rising demand for WFE. To enable this development, memory suppliers are likely to materially increase DRAM capex to support fab build-outs, advanced-node transitions, and incremental HBM wafer capacity. The market has already priced in at least some of this cycle, especially in logic, after the TSMC 2026 capex came in much higher than expected, with much stronger conviction for the capex increase in the next few years.

We expect this dynamic to increasingly extend into the memory ecosystem, benefiting both front-end and back-end equipment suppliers. In fact, just this week, ASML management also expressed a very strong memory outlook for EUV driven by 1) Strong HBM wafer capacity expansion and EUV layer count requirement, 2) Strong demand for node migration to 1b and 1c from the suppliers.

All 3 leading memory producers are increasing EUV layer counts in newer processes. This is necessary for scaling in general, and helps with HBM performance as it becomes a larger part of the product mix.

![](https://substackcdn.com/image/fetch/$s_!bxgD!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb33e346a-a9b6-4360-8524-fd0fc99b2756_864x541.png)

Source: SemiAnalysis WFE Model - Sales@SemiAnalysis.com

There are a few clear areas where EUV can replace DUV multipatterning, most in the congested region where access transistors (the devices that allow read and write to the memory cell) meet the memory storage capacitors (which stores the charge representing a 1 or 0). Contacts between access transistor source and storage capacitor, along with the transistor drain to bitline, are probably the first to go to EUV. They are cylindrical vias with small dimension in both X and Y, which generally makes them more difficult than narrow lines. It’s similar to 7nm logic, where the tightest pitch via layers were the first to adopt EUV.

Next the bitline, wordline, gate, and active area cuts are good candidates for EUV. Narrow lines are relatively easy to produce with DUV multipatterning (pitch splitting), but cutting the line ends is very difficult. You can see in the diagram below how small the tip-to-tip distance needs to be in some cases - look at the ends of the bitlines. Other line ends aren’t shown but have a similar challenge.

We wrote more about this 6F <sup>2</sup> architecture, how it scales, and what will break first as it continues to scale in future nodes [as part of our VLSI 2025 recap](https://newsletter.semianalysis.com/i/174558662/dram-4f2-and-3d).

![](https://substackcdn.com/image/fetch/$s_!M1y7!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe41583fc-a320-4da1-9d3c-d017b89bd9e2_757x575.png)

Storage node contact (denoted BC for buried contact), bitline cut (the narrow gap between bitline ends), and bitline contact (denoted DC here) are the first layers where EUV is adopted. Source: Samsung

DRAM EUV intensity will increase substantially in the short term, as chipmakers are rushing to convert as much capacity as they can to the latest, EUV-heavy, processes. Longer term, they are taking steps to rein in cost. SK Hynix will continue to increase EUV layer count in the upcoming 1γ process, but predicts EUV spend will begin to level off. This is due to likely MOR adoption, which effectively increases throughput per tool without paying ASML for an upgrade, and possibly other improvements. Still, a *slower* increase in EUV spend is still an increase and great for ASML.

*Want complete details on the WFE supercycle? Model subscribers had them long before this report: [https://semianalysis.com/wafer-fab-model/](https://semianalysis.com/wafer-fab-model/)*

![](https://substackcdn.com/image/fetch/$s_!78Ir!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24839116-a43e-40fe-9a59-2d9c470627f5_889x508.png)

Source: SemiAnalysis WFE Model - Sales@SemiAnalysis.com

DRAM WFE capex will increase by roughly 26%, 34%, and 20% for Samsung, SK hynix, and Micron, respectively, in 2026. These increases are driven by aggressive HBM capacity expansion, rapid migration to 1b and 1c nodes with higher EUV layer intensity, and fab build-outs slated to come online in 2027, alongside accelerating node migration across the industry. We expect this view to be validated as the upcoming earnings season reflects semiconductor management commentary, alongside capital expenditure guidance from the memory companies.