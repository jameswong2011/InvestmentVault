---
publish: false
date: 2026-08-06
tags: [research, email-backfill, Viks]
source: 'https://www.viksnewsletter.com/p/post-astera-labs-is-a-switch-company'
source_type: web-clip
sender: viksnewsletter@substack.com
---

# Astera Labs is a Switch Company in Connectivity Clothing

Astera Labs built its fortunes by retiming signals for intra-tray connectivity, but their pivot to becoming a switch company is turning the tide for them.

Here are some key earnings takeaways:

- Revenue of $392.4 million, up 27% sequentially and 104% year over year, against a Q2 guide of $355-365 million given in May.

- PCIe 6 products, meaning Scorpio switches plus Gen 6 Aries retimers, crossed 50% of revenue for the first time, up from roughly a third in Q1.

- Q3 guidance of $540-560 million, non-GAAP gross margin of about 72%, and non-GAAP EPS of $1.16-1.21.

Their Scorpio line of switches is expected to become the largest product family in Q3, one quarter ahead of what management guided in May. Part of their uniqueness comes from their COSMOS software platform which does more than just telemetry and health monitoring.

Astera Labs should be viewed as a switch company – along the lines of Broadcom – going forward, as their 320-lane Scorpio X switch gains larger adoption, notably even with neoclouds and inference GPU providers.

CXL is an interesting segment that shows some promise, but is really a 2027 story. Optics is a 2027 story regarding NPO, while CPO lies even beyond that. The Q2 earnings call provided quite a bit of color regarding where things are headed.

For a deeper-dive on Astera Labs, see the post below.

## Astera Labs: From the Tray to the Rack, and What Comes After

Astera Labs’ expansion out of the tray, where they built the company using their Aries PCIe retimers for XPU-CPU-NIC connectivity, and into the rack via their Scorpio switches is their biggest near term growth move. From the 1Q2026 earnings call:

By reading this post, you agree to the terms and conditions. Also see the full ethics statement. For institutional research, contact SemiExponent.

If you’re new, check out the About page. A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

If you are not a paid subscriber, you can purchase just this article using the button below. You can find the whole catalog of articles for purchase at this link.

Buy the article

### Scorpio X Acceleration

Around the time of IPO, the dollar content of Astera products per XPU was $50-$100. In the Q2 earnings call, COO Sanjay Gajendra said that he sees their business contributing multiple $1,000s per XPU with the 320-lane Scorpio-X scale-up switch itself contributing $1,000 per XPU.

In SemiAnalysis’ Trainium 3 deep dive, they estimate that the 320-lane Scorpio X has an attach rate of 0.25-0.28 per XPU depending on the switched rack Trn3 SKU. We’ll reproduce that table below for convenience.

At $1,000 of Scorpio X content per XPU, a 32-XPU Gen2 Trn3 rack carries $32,000 worth of 320-lane Scorpio X content, delivered as 8 scale-up switches. The 72-XPU variant Gen2 Trn3 rack carries $72,000 across 20 switches. All this points to an ASP of $3,600-$4,000 per Scorpio X switch.

This is consistent with Tomahawk 6 pricing. Broadcom priced Tomahawk 6 below $20,000 at launch, before volume discounts, for a total switch bandwidth of 102.4 Tbps. That works out to roughly $200/Tbps. Scorpio X has 5x lower switch bandwidth at 20.48 Tbps, and at $200/Tbps, that prices it right at $4,000.

Additionally, for the Gen2 variant, we are not counting the lower lane count Scorpio-P switches (144 32-lane, 72 64-lane, or 36 128-lane) that are on the PCB per rack. That would add even more incremental revenue for Astera Labs, and Aries retimers would be on top of that. You can see how much PCIe Gen 6 content exists in a rack, and how that can contribute to 50% of total revenue as stated in the earnings call.

Another bit of color in the Scorpio acceleration story stems from the fact that companies that are building add-in card GPUs like SambaNova or d-Matrix (for example) would also be interested in Scorpio X switches, and not just AWS. This becomes even more important if companies like these can buy NVLink Fusion interfaces in the future, so that they can work better with Nvidia hardware. This NVLink aspect will become important in Trainium 4. Similarly, neoclouds are a potential buyer of Scorpio scale-up switches too.

Gajendra said that there are 10 customers getting into pre-production and qualification cycles. It remains to be seen how many will materialize into revenue in future quarters.

### COSMOS

A part of the switch story that we did not cover fully in the deep dive was their COSMOS software platform. Deep telemetry was an important part of Astera’s growth strategy in the early retimer days. Today, COSMOS is much more. Its Hypercast and in-network compute features are advanced hardware-accelerated networking technologies that offload data processing and multi-destination packet distribution directly onto smart fabric switches to speed up large language model (LLM) training and inference. This essentially speeds up collective operations during training and enables greater utilization of GPUs.

Thus, the Scorpio X switch story does not stand alone. It is closely coupled with the software to extract the maximum performance of switches and GPUs within a rack.

### CXL

Compute eXpress Link (CXL) solutions are becoming increasingly popular in the industry now as memory shortages stay acute, and hardware makers scramble to provide alternatives for a variety of use cases. Gajendra points out a few in the earnings call:

- High cost of DRAM is driving people to stick different kinds of memory behind a CXL bus

- When CXL is attached to an XPU, KV cache acceleration drives lower inference latency

- In general compute applications that are memory intensive, CXL provides a way of adding more memory to the CPU

CXL is a story that is just beginning for Astera Labs via their Leo series of products. In Q2, they closed a design win with a US hyperscaler. In 2027, they expect to ship CXL memory controllers to two US hyperscalers. But most of the volume and associated revenue is really a 2027 story.

After the paywall are some thoughts about where Astera Labs goes from here, what can fail, and what to watch for.
