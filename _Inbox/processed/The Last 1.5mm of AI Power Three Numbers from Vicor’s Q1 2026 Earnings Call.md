---
title: "The Last 1.5mm of AI Power: Three Numbers from Vicor’s Q1 2026 Earnings Call"
source: "https://photoncap.net/p/the-last-15mm-of-ai-power-three-numbers"
author:
  - "[[PhotonCap]]"
published: 2026-04-22
created: 2026-04-28
description: "3 A/mm², 40x current multiplication, 1.5mm. Three numbers disclosed for the first time on Vicor's Q1 2026 call that mark the inflection point in AI power architecture."
tags:
  - "clippings"
---
### 3 A/mm², 40x current multiplication, 1.5mm. Three numbers disclosed for the first time on Vicor's Q1 2026 call that mark the inflection point in AI power architecture.

### Abstract

On April 21, 2026, Vicor Corporation (NASDAQ: $VICR) held its Q1 2026 earnings call, where CEO Patrizio Vinciarelli made two explicit technical claims. First, the company put hard numbers on its second-generation Vertical Power Delivery (VPD) solution for the first time: 3 A/mm² current density, up to 40x current multiplication, 1.5mm package thickness. Second, Patrizio directly rebutted a proposed 800V-to-6V bus architecture now circulating in the industry, calling it structurally misguided. This piece unpacks why those two claims showed up on the same call and what they imply for AI data center power architecture.

![](https://substackcdn.com/image/fetch/$s_!8nn8!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5196c602-8808-4e7f-80b4-978978376c7b_2656x1600.jpeg)

---

### Contents

1. Intro
2. Background: why capacity expansion is part of the thesis
3. 2nd-gen VPD specs, what each number actually means
4. The 800V→6V debate: solving the wrong problem *(paid)*
5. Vicor’s business model, structurally read *(paid)*
6. Scenario analysis *(paid)*
7. Closing
8. References & Sources

---

## 1\. Intro

A state-of-the-art AI rack now draws around 100kW. NVIDIA’s GB200 NVL72, for instance, lands at roughly 120kW at the rack level. \[1\]

Not many people track what happens in the last few millimeters before that power reaches the processor surface. The 48 volts arriving at the server rack has to be stepped down to the ~0.7 volts the processor actually uses. If that conversion is handled poorly, and specifically if the heat and losses it generates aren’t managed, the GPU underperforms regardless of how good the silicon is. The one-line physics behind this, **P = I²R**, which says power loss scales with the square of current, is the equation I covered in detail in my prior piece on why it reshapes AI infrastructure. \[4\]

**The next bottleneck in AI data centers isn’t the semiconductor process. It’s how power gets delivered. Vicor used this call to forcefully assert that it is the only company with a commercialized solution combining all the conditions that bottleneck demands.**

This piece walks through the technical statements from Vicor’s Q1 2026 earnings call on April 21, 2026, and lays out the power architecture constraints they imply. It isn’t a stock pick. It’s a breakdown of the technical landscape and the business consequences that came out of the call.

---

## 2\. Background: why capacity expansion is part of the thesis

Good technology with constrained supply tells a different story. That’s why capacity expansion took up more airtime on this call than anything else.

Vicor’s VPD modules are produced at one site today: the CHiP fab in Andover, Massachusetts. That fab had been mapped to roughly $1B/year in revenue capacity. On this call, Patrizio said they can push it to **$1.5B/year**. \[3\]

There are two mechanisms. One, shorter cycle times at bottleneck process steps inside the existing fab. Two, relocating some process steps to a nearby building to lift effective throughput at Fab 1. His phrase was that they’d found “significant elasticity,” and the capacity step-up could be as much as 50% above what had been planned. \[3\]

A second 3Di (3D interconnect) line is set to go in during Q3/Q4. \[3\]

What about Fab 2? The prior plan contemplated securing new land. On this call, the approach shifted to an **existing building**. The reason is simple: speed. An existing building lets them add capacity much faster than ground-up construction.

The key quote: “We see ourselves being essentially sold out in terms of capacity for the foreseeable future.” \[3\] Demand stays ahead of supply for a while, which is also why Vicor is being selective about which customers it onboards.

The customer mix currently disclosed:

- **Lead computing customer**: Maker of a wafer-scale-engine-based AI accelerator. Given the direct reference to wafer-scale engines on the call, this is likely Cerebras, though Vicor did not confirm the name.
- **Hyperscalers**: Referenced in plural. No names disclosed, but flagged as a major driver of the Q1 backlog surge.
- **Industrial and defense**: ATE (semiconductor test equipment), aerospace, and defense continued to place strong orders.

![](https://substackcdn.com/image/fetch/$s_!n-x5!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F590c0a68-d003-4dcb-a3d6-71696439ae25_2656x1600.jpeg)

\[Figure 1: Vicor capacity expansion roadmap, Fab 1 ($1B→$1.5B) + Fab 2 plan\]

Q1 backlog hit $301M, up 70% sequentially. That’s 2.7x the quarterly revenue of $113M. \[2\]

> **One-line takeaway**: The bottleneck that turns technical lead into actual revenue today is fab capacity. Vicor is working the bottleneck, and demand is already ahead of supply.

---

## 3\. 2nd-gen VPD specs, what each number actually means

Phil Davies put concrete numbers on 2nd-gen VPD for the first time on this call. Three of them:

- **Current density**: 3 A/mm²
- **Current multiplication**: up to 40x
- **Package thickness**: 1.5mm, with thinner on the roadmap \[3\]

The point is the combination of all three.

### Why current density matters

Here’s the simple version. Low current density means you can only deliver so much current per unit area. To get more, you stack modules. The problem with stacking is that heat gets trapped inside. The bottom modules heat the ones above them, efficiency drops, and the package gets thicker on top of that.

Vicor management, on this call, directly called out competitor solutions as having “inadequate” current density, with stacked packages suffering from thermal and mechanical issues. \[3\] Management’s position is that their 3 A/mm² is the most aggressive number currently on the table. A quantitative head-to-head comparison with specific competitors wasn’t presented on the call, so this remains Vicor’s view, not a third-party benchmark.

### Why current multiplication is the real differentiator

This is the core point.

Most IVR (Integrated Voltage Regulator) solutions multiply current by about 2x. To deliver 2000A to the processor, that means feeding 1000A on the bus. A 1000A feed needs extremely thick wiring, and thermal management at that current level is impractical.

40x multiplication completely changes the arithmetic. 2000A to the processor needs only a 50A feed. That’s why Vicor positions VPD as a current multiplier rather than a voltage converter.

### How 1.5mm stacks up

On this call, one analyst cited recent APEC (Applied Power Electronics Conference) discussions suggesting that NVIDIA, Google, and similar buyers are asking suppliers for packages under 3mm. Vicor pushed back with the fact that its 1.5mm is half that threshold. \[3\]

And it doesn’t stop there. Patrizio: “we’re not stopping at 1.5 millimeter, we’re going thinner.” \[3\] Next-generation chiplet-based packaging (like CoWoS) will demand thinner modules still.

![](https://substackcdn.com/image/fetch/$s_!sOkw!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07352990-1064-41b3-af6b-3b4855899c62_2656x1600.jpeg)

\[Figure 2: Three key specs of 2nd-gen VPD\]

The lead customer’s Gen4 → Gen5 transition is slated to be enabled in **H2 2026**, with ramp beginning before year-end. Additional HPC customers follow on second-gen VPD after that transition. \[3\]

> **One-line takeaway**: 3 A/mm², 40x multiplication, 1.5mm. Meeting all three at once is Vicor’s claim, and no other company has publicly disclosed a spec combination on this set of axes.

---

Here’s the natural question.

The specs are impressive. So why aren’t competitors going this route? Actually, more precisely: a part of the industry is trying to solve the problem with a **different architecture** altogether. Stepping directly from 800 volts down to 6 volts.

What that debate actually means, and who ends up making money in that setup, is what I unpack below.

---

## 4\. The 800V→6V debate: solving the wrong problem

An idea getting attention in some parts of the industry: raise the server rack’s distribution voltage from 48V to 800V, then drop that 800V straight to 6V near the processor.

To make sense of this debate, you have to separate two axes first.

**Axis 1: Distribution voltage.** At what voltage do you run cables and busbars from the PSU to the vicinity of the processor? 48V, 400V, 800V are the options.

**Axis 2: Physical topology of the converter.** Where do you place the final power converter relative to the processor? Next to it is lateral. Directly underneath is vertical (VPD).

These two axes are **independent**. You can have 800V distribution with either lateral or vertical final conversion, and the same applies to 48V. Vicor’s VPD is an Axis-2 (placement) innovation. The 800V→6V proposal is an Axis-1 (distribution) proposal. The two camps aren’t actually head-on, they’re working on different problems.

![](https://substackcdn.com/image/fetch/$s_!OtF-!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12e85de8-ea01-4bc9-ae33-ca267f8a3faf_2656x1600.jpeg)

\[Figure 3: Two camps compared, architecture side-by-side\]

### Vicor actually supports 800V

Here’s something that gets missed. Vicor isn’t against 800V distribution on the upstream side. Patrizio on this call: “Vicor has proprietary technology at 800 volts. We did a lot of pioneering developments with respect to bus conversion from 800 volts.” \[3\] The 800V-to-48V bus conversion IP was developed by Vicor.

What Vicor actually opposes is the specific step of **going directly from 800V down to 6V**. Vicor’s ideal path looks like this:

PSU → 800V distribution → \[800V→48V conversion\] → 48V distribution (all the way under the processor) → \[VPD: 48V→0.7V in 1.5mm\] → Processor

So 48V isn’t the end goal. It’s the means. The three reasons the path stops at 48V aren’t laid out by management on this call. They’re my technical read on why Vicor lands where it does.

**Safety (SELV)**: 60V is the Safety Extra-Low Voltage ceiling. Cross it and you trigger a completely different regime for insulation, connectors, and maintenance, with costs rising accordingly. 48V sits cleanly under that ceiling, which is why it became the data center standard.

**Converter thickness**: Ultra-thin 1.5mm converters are feasible with 48V input. Going straight from 800V to below 1V in one step drives extreme demands on transformer turn ratios, insulation clearance, and switching devices, none of which fit a thin package. VPD hits 1.5mm because the input is 48V.

**Wiring loss vs distance**: The advantage of 800V distribution only matters over **long distances** (rack-to-rack, vertical busbars inside the rack). Across the few millimeters directly below the processor, 48V versus 800V makes almost no difference. The distance is too short for distribution-voltage gains to show up.

### The core logic: losses always blow up in the high-current zone

This is where Patrizio’s math pushback actually lands.

Start from the first principle: **for a given amount of power delivered over a bus, a lower voltage means higher current, and wiring loss scales with the square of current**. Numerically, then:

Take 48V bus distribution as the reference point (current X, baseline loss). Drop that to 6V, and current becomes 8x (48/6), with loss at **64x** (8²). \[3\] Drop further to 2V for an IVR-style approach, and the current ratio is 24x (48/2). Phil Davies on the call stated the 2V-reference loss figure as **526x** \[3\]. A simple I²-proportional calculation gives 576x, but the assumptions underlying the company’s figure weren’t detailed on the call.

Either way, the structural problem with the 800V→6V camp is this: it trades a few percentage points of upstream 800V distribution gain for a **64x wiring-loss penalty** on the downstream 6V bus, compared to a 48V bus. The 6V bus only holds efficiency over extremely short distances, and practical packaging makes those distance constraints hard to meet.

Vicor’s answer is to **eliminate the 6V bus stretch entirely**. Bring 48V directly under the processor package, and let the VPD finish the 48V → 0.7V conversion inside 1.5mm. Compress the high-current zone down to 1.5mm and the loss source disappears with it.

Patrizio’s framing of the 800V→6V proposal: “frankly ill-conceived.” \[3\]

### Why competitors can’t take this path

So why is that direction being pursued at all? Two reasons.

First, a full VPD implementation is hard. Without a technology that hits high current density, high current multiplication, and thin package thickness simultaneously, suppliers go looking for what they can build now. Phil Davies described this as the reason “competitors go lateral with a bit of vertical.” \[3\]

Second, solutions that copied Vicor’s 1st-gen VPD are already in the market, and those solutions are structurally blocked from moving to 2nd-gen. They run into the same limits on density, stacking, and thermal handling.

One interesting note. Patrizio pointed out that Vicor holds IP in the 800V→6V space as well. \[3\] “… successful to any degree, there’s going to be issues with respect to IP there too.” In other words, even if the industry goes that way, it opens a royalty path for Vicor.

![](https://substackcdn.com/image/fetch/$s_!FfE1!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1efdf236-2c63-4735-96c5-b89e36b12f72_1211x360.png)

---

## 5\. Vicor’s business model, structurally read

Vicor frames itself as two businesses in one: module maker plus IP licensor. Management’s position is that the two reinforce each other. \[3\]

Q1 royalty revenue came in at $15M. Annualized, that’s around $60M. \[2\]

Here’s the important piece. FY2026 guidance of $570M assumes **zero new licensing agreements**. \[3\] The reason: Vicor is currently pursuing a second ITC (International Trade Commission) case with a final determination expected in 2027. Management’s reading is straightforward: settling before that final determination means worse terms. Waiting until after a second exclusion order is issued allows Vicor to negotiate licensing from a stronger position.

Patrizio also hinted at a third ITC case. “In Italy we say there is no two without three.” \[3\]

### Valuation breakdown

Laying out the numbers. FY2026 revenue guidance is around $570M, which is **combined product and royalty** revenue. Of that, royalty is expected to run around $60M+ on existing contracts, leaving product alone at roughly $510M. The key detail: **no new licensing is built into that guidance**. Royalty margins are, in management’s phrasing, “nearly 100%” \[3\], and the long-term framing management has cited in the past is that royalty could reach up to 50% of product revenue at the upper bound. \[3\]

The 50% figure tracks a stretch case Phil Davies has referenced in past interviews and conferences, which he touched on again on this call. That section of the call was fragmentary, so this should be read as management’s long-term framing rather than a committed target.

Under the stretch case, using a ~$510M product base puts additional royalty at ~$255M. At nearly 100% margin, that’s a profit structure very different from what a typical semiconductor equipment company carries.

### One correction: the direction of the $28.6M

Q1 operating cash flow included a one-time **$28.6M payment for a past litigation award**. \[2\] In other words, it was an outflow, not an inflow. Without that item, operating cash flow would have looked meaningfully better. This is a separate item from any royalty stream Vicor could receive from the ongoing second ITC case.

### Royalty scenarios (author’s model)

**Base case**: Existing licensing contracts continue and no new deals are signed. Guidance of $570M holds, with $60M+ of that being royalty.

**Upside case**: One to two new contracts signed after the second ITC final determination. Royalty potentially exceeds $100M.

**Stretch case**: Over multiple years, royalty reaches 50% of product revenue at the upper end. Royalty potentially reaches $250M+ in a multi-year horizon.

These three numbers are not company guidance. They’re my estimates built on base/upside/stretch assumptions. What the company has officially stated is limited to two things: “existing licensing is included, new licensing is not included before the 2027 final determination” and “50% is the long-term framing we’ve talked about before.”

---

## 6\. Scenario analysis

AI data center power architecture can converge toward three different paths. Walking through each:

**Scenario A: VPD becomes the norm.** Vicor’s module business hits the best case: fully utilized capacity, gross margin expansion. Royalty accelerates on new deals. NVIDIA benefits if it adopts VPD because GPU performance ceilings rise. On the other side, competing power suppliers find the structural limits of copying 1st-gen VPD exposed, and the IVR camp gets pushed out of the hyperscale segment on current multiplication limits.

**Scenario B: Mixed 800V→6V and VPD.** Vicor captures part of the demand on module, and per management’s own remarks, there’s royalty exposure on the 800V side as well. NVIDIA takes on architecture transition costs. Competing power suppliers hold parts of the market. IVR still struggles to fit the point-of-load requirements in this scenario.

**Scenario C: IVR breakthrough.** Short-term wins for the IVR camp and some competing power suppliers in specific segments. Vicor’s module growth slows, and if that coincides with litigation delays, royalty ramp also gets pushed out. From NVIDIA’s side, the power bottleneck persists, which isn’t a good outcome.

This framework sits on top of Vicor management’s framing. Actual market outcomes will be more complicated than this. In particular, competing power suppliers and the IVR camp could flip from negative to positive depending on their own R&D progress.

### Monitoring points

1. **Lead customer Gen5 transition timing**: Enabled in H2 2026, ramp starts before year-end per management. Delays push Vicor’s revenue ramp. Track Cerebras public announcements and Vicor quarterly guidance.
2. **Second ITC final determination**: Expected 2027 per company guidance. Faster-than-expected outcome accelerates new licensing. Track SEC filings and public ITC dockets.
3. **Fab 2 site confirmation**: Currently searching for an existing building. Announcement concretizes the capacity expansion timeline.
4. **Royalty QoQ trajectory**: If royalty grows without new deals purely on existing contracts, it reveals how conservative the guidance is. Track the royalty line in quarterly results.
5. **Frequency of 800V→6V research papers and presentations at APEC and similar conferences**: The fastest leading indicator of whether the industry is tilting that way.

---

## 7\. Closing

Vicor did more than release numbers on this call. Putting 3 A/mm², 40x multiplication, and 1.5mm on the record is a statement of technical confidence. And pushing back on 800V→6V with a math argument tells you how they see the competitive landscape.

Capacity running behind demand, guidance staying conservative, and the second ITC outcome not yet priced in. Those three things overlap right now.

AI data center power ultimately has to be delivered right beneath the processor. Whoever controls that last few millimeters will control the power market for the next decade.

---

## References & Sources

\[1\] [GB200 NVL72 Power Specifications, NVIDIA Mission Control Documentation](https://docs.nvidia.com/mission-control/docs/systems-administration-guide/2.0.0/prs/faq.html). Rack-level power specification (~120kW) for NVIDIA GB200 NVL72 rack-scale systems.

\[2\] [Vicor Corporation Reports Results for the First Quarter Ended March 31, 2026](https://vicorcorporation.gcs-web.com/news-releases/news-release-details/vicor-corporation-reports-results-first-quarter-ended-march-13). Q1 2026 earnings press release. Revenue, gross margin, backlog, cash flow items (including the $28.6M past litigation payment).

\[3\] [Earnings call transcript: Vicor Q1 2026 beats estimates but sees stock dip](https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-q1-2026-beats-estimates-but-sees-stock-dip-93CH-4626358). Full Q1 2026 earnings call transcript (Investing.com, secondary source). Covers all management remarks on fab capacity expansion, 2nd-gen VPD specs, 800V→6V rebuttal, and royalty strategy. To be replaced with Vicor IR official webcast replay or 10-Q filing when posted.

\[4\] [P = I²R: The One-Line Equation Shaping AI Infrastructure and Vicor’s ($VICR) VPD](https://photoncap.net/p/p-ir-the-one-line-equation-shaping). PhotonCap prior article. Detailed analysis of how the physics of current-squared loss shapes AI infrastructure power architecture. Technical premise for this article.

---

Disclaimer: This article is an independent, engineering-driven technical analysis published by *PhotonCap*. All content is based on publicly available information and is intended for educational and informational purposes only. Nothing herein constitutes a recommendation to buy, sell, or hold any security. The author may hold positions in securities discussed and may transact at any time without notice. Readers should conduct their own due diligence before making any investment decisions.