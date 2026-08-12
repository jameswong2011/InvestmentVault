---
title: "The Economics of a Neocloud - 5 Jul 26"
source: "https://degentradingdaily.substack.com/p/the-economics-of-a-neocloud-5-jul"
author:
  - "[[degentrading]]"
published: 2026-07-05
created: 2026-08-05
description: "Why does everyone want to be a neocloud?"
tags:
  - "clippings"
---
“XAI striking a deal with Google”

“Meta signaling that they are open to selling excess computing infrastructure”

“Softbank plans to offer AI Compute in US at 10GWs”

Everywhere you go turn, it looks like everyone wants to become a neocloud and start selling compute. Why is this the case?

Let’s start off by examining a real life case scenario as i walk through the economics of a neocloud with you.

On the 5th June 26, [Google announced a deal to pay Space X 920million a month for compute capacity at XAI data centers](https://www.cnbc.com/2026/06/05/google-to-pay-spacex-920-million-a-month-for-xai-compute-capacity.html).

This was for 110,000 NVDA GPUs as well as CPUs and other memory components i.e a fully furnished datacenter (Colossus 2)

The GPUs in question are the NVDA GB200s NVL72.

For that amount, we can see that each GPU fetched 920M/110,000/720 = 11.6 per hour

Let us construct a fictitious 100MW datacenter filling it with GB200s

![](https://substackcdn.com/image/fetch/$s_!7esR!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc1dde63-858a-4313-b6b3-42f098471e5a_690x512.png)

My estimates land us at about 50B per GW. In this case, our 100MW buildout will cost us about 5B.

Which references well with [industry estimates](https://www.youtube.com/watch?v=4zk-hJ50vmU). Note, this is for GB200 buildout. As you get more advanced, the chips are more expensive. For example, the GB300 buildout, the compute cost is 20% higher.

Jenson saying that 100B per GW is actually realistic when you factor in that compute costs for Rubin will be twice as much as the Blackwell costing. The cost of power etc, are also rising.

We also know that each GB200 draws about 1200Ws, hence 100MW converts to about 83,333 GPUs.

On the XAI deal economics, this would land us at 83333\*11.6\*365\*24 = 8467M/year …

On the following cost structures  
  
0.74M/MW per year for electricity  
0.25M/MW per year for infrastructure maintenance  
0.3M/MW per year for staffing

![](https://substackcdn.com/image/fetch/$s_!OO_N!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58e73ca5-d1c5-412a-81f1-eba915369a01_428x191.png)

We have this insane looking scenario where your payback period is less than 1 year.

This is where i would come in and say that the Space X deal was **remarkably generous.** Was Google facing a massive compute shortage?  
  
If we were to run this on less insane and more normal looking assumptions like a price of ~6/hr

![](https://substackcdn.com/image/fetch/$s_!h9L7!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbda00ebf-0025-40f5-800f-d4d8d855d72c_384x165.png)

Our payback period stretches to about 2 years.

I am estimating that on long term deals that the neoclouds sign with the hyperscalers, it is done at about $4/ equivalent. The hyperscalers in turn are able to monetize the compute out at much higher rates, like $12+ (AWS).

Just for fun, if we do a pro-forma of a singular build out - it would look like this

![](https://substackcdn.com/image/fetch/$s_!hGED!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d268efa-85a9-4c69-9a9f-483595573fef_872x415.png)

Now, of course - we can dispute that GB200s will have no value after 5 or 6 years. But A100s came out in 2020 - they are still being rented out at $1 - $2/hr. This was ~ $3 in 2021. The hyperscalers are still renting them out at anywhere from $2 - 3.5/hr

Gavin Baker made the case for the GPU depreciation timeline to run for about 10 years. I would agree with him especially as agentic AI and inference usage pick ups.

In essence - **current compute markets are pricing a severe shortage.**

Anyone that tells you otherwise is covering their eyes.

Space X is renting out compute, because at those rates that they rent out, they are making a ton of cash (also because they face issues with connecting Colossus 1 and 2). Musk also made the deal with the right to cut the lease short saying that “If compute gets super tight I said we might need it back at some point”

*Tldr: Everyone wants to be a neocloud now because compute is super tight and it mints cash.*

From the facts of the matter, being able to construct a datacenter and to sell compute is the best business right now.

This is why the hyperscalers are willing to prepay neoclouds for compute availability.

Again, a neocloud’s valuation should be the summation of the NPV of all the compute deals that it can do. **Hence the ability to obtain financing, the exact depreciation schedule and the ability to execute are the 3 most important levers impacting it.**

For those, who then cry that it is all circular financing etc (insert whatever phrase), know that Anthropic now is making more than 70% gross margins on serving inference. The frontier labs that are the biggest users of compute can switch over to become cash flow positive if they want to.