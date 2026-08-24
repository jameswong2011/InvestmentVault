---
title: 'Cerebras Supernova 2026: Irrational Recap'
source: 'https://irrationalanalysis.substack.com/p/cerebras-supernova-2026-irrational'
url: 'https://irrationalanalysis.substack.com/p/cerebras-supernova-2026-irrational'
date: 2026-08-19
publication: Irrational Analysis
author: Irrational Analysis
sender: irrationalanalysis@substack.com
gmail_id: 1a017c1337051db2
ticker: CBRS
source_type: news
tags: [research, email-backfill, IrrationalAnalysis, CBRS, NVDA, VICR, wafer-scale, yield, SuperNova]
gmail_full: true
web_teaser: false
---

# Cerebras Supernova 2026: Irrational Recap

**Source:** [Irrational Analysis](https://irrationalanalysis.substack.com/p/cerebras-supernova-2026-irrational) — Gmail thread `1a017c1337051db2` from `irrationalanalysis@substack.com` dated 2026-08-19T02:01:34Z (10:01 Asia/Singapore). Subscriber full body via `get_thread` PLAIN_TEXT. WebFetch of the same URL returned the same plaintext (no additional chart OCR). Subtitle: *Some useful information. Meaningful progress.*

Irrational Analysis is heavily invested in the semiconductor industry.
Positions will change over time and are regularly updated.
Opinions are authors own and do not represent past, present, and/or future employers.
All content published on this newsletter is based on public information and independent research conducted since 2011.
This newsletter is not financial advice and readers should always do their own research before investing in any security.
Feel free to contact me via email at: irrational_analysis@proton.me

---

The one-share activist investor campaign continues.

Snipping a recent funny exchange I had with a much larger fellow shareholder of Cerebras.

Yes, Gavin I have seen their patents.

Their yield issue is not defects. Cerebras solved catastrophic yield. Good for them. 100% of wafers function. At what clock speed and power draw (PARAMETRIC YIELD), unclear which is why I had to model the TOTAL COMPOUND YIELD at 20%.

This is the full editable Excel model that I screenshotted in the argument with Gavin. If you think my assumptions are wrong, go edit it and try to get publicly reported hardware gross margin of WSE3 and rumored ASP to align.

[Attachment: Cerebras Irrational Analysis 062326.xlsx, 1.17MB]

---

Ok on to the event. Most of it was useless with several terrorist attacks against charts, engineering, and basic critical thinking.

But there was some very useful information that is much appreciated.

Also I like Andrew Feldman’s suit.

This chart’s y-axis actually made my blood pressure go up. Whoever made this shit shame on you.

New system has three wafers (same wafer as before) in one much more efficient box.

Looks like it is short enough to have several general-purpose IT equipment (CPU servers, switches) above.

Each wafer also had double I/O. I suspect they doubled the clock speed of the NoC and by extension the I/O.

Highly doubt power is fully disaggregated. Probably the bulk of power delivery is in the front panel modules and final current multiplier stage is on the WSE package/module itself.

https://www.vicorpower.com/resource-library/articles/high-performance-computing/current-multipliers-powering-ai-processors

Really wish there were more details.

You can see there is only one I/O card at the top. So they got the doubling just from clock speed and made zero design changes.

Doubling clocks but slightly better than half the latency. Must have made some improvements on the FPGA side.

Ok now I am confused again. They either doubled NoC+I/O clock or they started using two edges instead of one. Whatever I/O doubled. They need more gains to steam in KV cache but for disagg I guess it works. Will trust them on that given the rumors I am hearing on the scale of Cerebras disagg planned deployments.

This is still terrible but less terrible than the previous 5 us. Real progress but they still need to work on this. One of Sean’s comments implied they made an IO ASIC to replace the FPGA. It’s unclear. If anyone can confirm this please let me know.

*(Chart number not OCR'd by Gmail PLAIN_TEXT or WebFetch. IA's own prose: previous latency 5 us; "slightly better than half the latency" after a clock double. Same-day SemiAnalysis CS-4 recap of the same SuperNova event publishes switched fabric 5 us → 3 us. Keep 5 us → 3 us as the chart claim IA is reacting to.)*

ON HOW MANY WAFERS? YOUR SLIDE IS MISSING SOME IMPORTANT INFORMATION.

---

Overall, generally happy with the progress they have made.

I/O has meaningfully improved. They are still bottlenecked by this probably but credit where credit is due.

Clock speed has doubled which is not interesting by itself. What interests me is this implies parametric yield is a lot better.

https://en.wikipedia.org/wiki/Shmoo_plot

There are claims of large improvements in thermal design, power delivery, and manufacturability. Seems believable but unclear how much given all we have are some basic renders with very little in terms of proper technical details.

Maybe they will show more useful information at Hot Chips.

Need more information before attempting to update my gross-margin model. Certainly, there is an improvement. Is this enough to get them to healthy 60+% hardware gross margins? I have absolutely no idea.

Subscribe for full coverage of Hot Chips 2026.
