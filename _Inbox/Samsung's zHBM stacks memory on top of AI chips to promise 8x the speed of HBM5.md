---
title: "Samsung's zHBM stacks memory on top of AI chips to promise 8x the speed of HBM5"
source: "https://gagadget.com/en/720940-samsungs-zhbm-stacks-memory-on-top-of-ai-chips-to-promise-8x-the-speed-of-hbm5/"
author:
  - "[[Anton Kratiuk]]"
published: 2026-08-05
created: 2026-08-07
description: "Samsung showed up to the Future of Memory and Storage (FMS) 2026 conference with its most ambitious memory roadmap in years. The centerpiece is zHBM—a vertical"
tags:
  - "clippings"
---
By: [Anton Kratiuk](https://gagadget.com/en/authors/213350/) | 05.08.2026, 16:01

 ![Samsung's next-generation memory technology showcase at FMS 2026. Photo: Samsung](https://gagadget.com/media/cache/2f/0c/2f0c9795017e55e8ab5d59ba6960451b.webp "Samsung's next-generation memory technology showcase at FMS 2026. Photo: Samsung")*Samsung's next-generation memory technology showcase at FMS 2026. Photo: Samsung. Source: Photo: Samsung*

Samsung showed up to the Future of Memory and Storage (FMS) 2026 conference with its most ambitious memory roadmap in years. The centerpiece is zHBM—a vertical stacking architecture that places memory directly on top of an AI accelerator chip rather than beside it—claiming 8x the performance of HBM5, 10x the density, and 50% lower thermal resistance. None of it is in production yet, but the direction is clear: Samsung wants to reclaim the AI memory lead it lost to SK Hynix.

## The vertical bet

Today's HBM (High Bandwidth Memory) sits next to a GPU or AI accelerator on a shared substrate. Samsung's zHBM concept cuts the signal path dramatically by stacking memory wafers directly above the compute die using wafer-bonding techniques. According to [Samsung Newsroom](https://news.samsung.com/global/samsung-unveils-next-gen-3d-memory-vision-at-fms-2026-charting-the-future-of-ai-infrastructure), the theoretical gains are striking: 8x HBM5 performance, 10x density improvement, and 3x better power efficiency. Samsung itself flags these as engineering projections, not measured results from physical silicon.

![](https://gagadget.com/media/uploads2/samsung-semiconductors-next-gen-3d-memory-vision-fms-2026main4.jpg)

![](https://gagadget.com/media/uploads2/samsung-semiconductors-next-gen-3d-memory-vision-fms-2026main5.jpg)

![](https://gagadget.com/media/uploads2/samsung-semiconductors-next-gen-3d-memory-vision-fms-2026main6.jpg)

![](https://gagadget.com/media/uploads2/samsung-semiconductors-next-gen-3d-memory-vision-fms-2026main7.jpg)

![](https://gagadget.com/media/uploads2/samsung-semiconductors-next-gen-3d-memory-vision-fms-2026main8.jpg)

![](https://gagadget.com/media/cache/2a/4f/2a4fabde548cde4865ae4b65b9175b26.webp) ![](https://gagadget.com/media/cache/8a/5c/8a5ce8417fa7031cc781f28c38a171d4.webp) ![](https://gagadget.com/media/cache/3f/11/3f1123c867f315c9828d74740f5cd7d1.webp) ![](https://gagadget.com/media/cache/65/29/6529cf33dcd95af466c471ae15465157.webp) ![](https://gagadget.com/media/cache/d6/a4/d6a4b031d5c6384aaa0231455eca43de.webp)

The thermal reduction figure—50% less resistance—matters most for real-world data center operators. AI servers already burn through hundreds of watts per accelerator; anything that keeps chips cooler at scale is worth watching.

## The NAND race and what's shipping now

Alongside zHBM, Samsung revealed the V10 Bonding V-NAND prototype, which exceeds 400 layers. The trick is a wafer-bonding process (BV-NAND) that manufactures the memory cell array and control logic on separate wafers, then bonds them together. The result is a 58% density jump over the current V9 generation, per [StorageReview](https://www.storagereview.com/news/samsung-outlines-3d-memory-roadmap-for-ai-infrastructure-at-fms-2026). Samsung also floated zNAND-O, a low-latency NAND concept aimed at AI edge systems that need to process data locally.

On the products-you-can-actually-buy side, Samsung confirmed mass production of the PM1763 and BM1773 enterprise SSDs, and began shipping samples of its LPDDR5X-PIM—an industry-first LPDDR memory module with processing-in-memory capability that offloads compute tasks from the main processor. HBM4 has been in mass production since February 2026, with HBM4E samples shipping from May 2026.

## Caveats worth noting

The bigger concepts—zHBM and zNAND-O—have no announced production timeline and no confirmed compatibility with NVIDIA or AMD accelerators. No third-party validation has been announced. SK Hynix is developing a competing 375-layer V10 4D NAND with earlier production targets, and Intel holds patents in adjacent vertical memory territory. Samsung is rebuilding its position in the AI memory market, but the gap between concept and chip fab is wide. Data center operators should treat today's announcements as a directional signal, not a procurement decision.