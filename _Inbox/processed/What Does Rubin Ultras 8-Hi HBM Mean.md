---
publish: false
date: 2026-08-11
tags: [research, email-backfill, Damnang]
source: 'https://damnang2.substack.com/p/what-does-rubin-ultras-8-hi-hbm-mean'
source_type: web-clip
sender: damnang2+memory-intelligence@substack.com
---

# What Does Rubin Ultras 8-Hi HBM Mean

Since SemiAnalysis published its institutional report on the HBM4 8-Hi despec, a wide range of interpretations and speculation surrounding it has spread quickly through the market.

As someone who covered the HBM4 8-Hi story in an article about a week ahead of SemiAnalysis, I will also admit that every time I saw misunderstandings and conjecture get amplified and reproduced from fragmentary numbers and information, without a sufficient understanding of the technical context of the matter, it genuinely saddened me.

This article was written conclusion first, and that part will be open to both free and paid subscribers. There is a lot of market misunderstanding around this HBM4 8-Hi move, and I judged that making my analytical view on it public would be meaningful in its own right.

In the paid section that follows, I will walk through, in order, why HBM4 8-Hi emerged, how it became possible, whether memory makers’ revenue will actually head lower, and what to watch going forward for each memory maker. I am confident that this article will be the deepest analysis yet of the technical background and meaning of HBM4 8-Hi, which the market has not properly covered so far.

I hope this piece clears up at least some of the market’s unnecessary misunderstandings around HBM4 8-Hi, and helps investors view this change on a more accurate technical footing.

## Disclaimer

This article is written for informational purposes and does not recommend buying or selling any particular stock. Responsibility for investment decisions and their outcomes rests with the investor. The Rubin Ultra specifications in this article are reported configurations under review, not confirmed facts, and the final specifications may change. The figures are based on public reporting, standard specifications, and my own calculations and illustrative assumptions. Anything attributed to industry chatter is hearsay that has not been publicly confirmed.

## Conclusion

To sum up this article, I do not see this 8-Hi transition as a bad signal for memory. This is a market where HBM cannot be sold for lack of it, and I see the HBM4 8-Hi despec as a special measure by NVIDIA to build more GPUs out of that scarce HBM. As discussed in the body, this despec is a move that would be hard for anyone but NVIDIA, which has built technical vertical integration spanning chip design, optics, and software.

Also, despite this despec, my calculations suggest the ratio of output gains to HBM price decline can come out higher, so total HBM revenue holds at 81.5% to 98% of planned 4E revenue. This means that if 12-Hi HBM4E could not actually meet more than 81.5% of the required volume, this despec can actually result in higher revenue.

Of course, what this NVIDIA request means for the memory makers is also significant. As I said in a previous article, NVIDIA has shown through this despec card that it has the influence to actually steer memory price negotiations.

Conversely, I think this may be a case that illustrates the view of SK hynix Chairman Choi Tae-won, that current memory prices are too high and that suppliers should move forward together with customers by coordinating them well.

In the end, I think it would be hasty to read this despec as a signal that the memory cycle has broken, and the right way to read it is as a signal that suppliers and customers have entered a phase of moving together, coordinating price, volume, and even design approaches.

## Table of Contents

- Why 8-Hi HBM4 Instead of 12-Hi HBM4E

- Is the Performance Possible with 8-Hi 192GB

- Does Memory Supplier Revenue Shrink

- What It Means for Each Memory Supplier and the Optical Names

## Further reading

### I Met with Semiconductor Experts in Korea

### The Laser Market Repriced by Scale-Up CPO

### How the Memory Tax Gets Solved

## Why 8-Hi HBM4 Instead of 12-Hi HBM4E

The causes of this Rubin Ultra despec, as heard from the field, are being grouped as follows.

First, HBM4’s better than expected pin speed and the burden of HBM4E qualification testing

According to people in the field, NVIDIA has been demanding a pin speed on HBM4E at around the 16Gbps level, far above the spec, and the HBM4E samples submitted so far by the three memory makers are reportedly having a harder time than expected passing qualification tests at that spec. This resembles the situation when NVIDIA demanded 12Gbps on HBM4, and considering how long it took to pass qualification on HBM4, it looks plausible that NVIDIA judged it would not be easy to make the launch of Rubin Ultra, which is scheduled for the second half of 2027.

In particular, since HBM4 itself is already holding 10 to 11Gbps, far above the original JEDEC baseline of 8Gbps, NVIDIA appears to have judged that using already proven HBM4 with just a modest bandwidth bump is better than forcing Rubin Ultra onto 4E.

> Note1 According to some experts, there are reports that the pin speed requirement NVIDIA newly asked to be improved while lowering the HBM4 stack height comes close to the 15 to 16Gbps it had demanded on the earlier HBM4E.

> Note2 On pin speed alone, the newly demanded HBM4 could just as well be called HBM4E class. However, taking together the core die density actually used (3GB), the various qualification test processes, and the verification engineers actually allocated at the memory makers, it looks reasonable to call the HBM that NVIDIA has requested for Rubin Ultra HBM4.

Second, DRAM supply constraints

The current DRAM supply constraint is expected to last through 2027, and whichever specification is chosen, the situation looks unable to satisfy the Vera Rubin Ultra volume NVIDIA wants. So NVIDIA chose 8-Hi instead of 12-Hi HBM4 for Rubin Ultra. Lowering the HBM stack height not only enables more HBM and commodity DRAM supply but can also be a factor that lifts yield, which appears to be why this step was taken.

According to what is heard from the field, the background to this decision looks like the following. First, rather than letting Rubin rack shipments fall because HBM was squeezing commodity DRAM supply, NVIDIA lowered the HBM stack height so that overall rack supply would not be disrupted. Second, since bandwidth may be a bigger problem than memory density on Rubin Ultra than expected, NVIDIA lowered the stack height while giving customers some bandwidth improvement in exchange for giving up some capacity.

What investors should know, though, is that while the market has reacted strongly every time news of a memory spec cut has come out, this is in fact not a new phenomenon. Rubin Ultra’s planned capacity has been cut at every revision, from the 4-die 1,024GB announced at GTC 2025, through the 12-Hi reduction and the 2-die transition, down to today’s 192GB, and Vera Rubin’s SOCAMM loadout is also reported to have been cut to about half. Looked at the other way, this may be evidence of just how serious the memory supply constraint is, serious enough that the chip designer has to keep changing the spec.

## Is the Performance Possible with 8-Hi 192GB?

According to field checks, the technical background that let NVIDIA decide to take Rubin Ultra to HBM4 8-Hi can be summarized in two points.

First, extending the existing NVLink based distributed memory structure from one rack to multiple racks, greatly widening the range of HBM that can be used (using an NPO structure)

Second, software techniques such as Wide Expert Parallelism, DWDP, Helix, and Dynamo make it possible to share that widened memory in a way that matches its speed

In other words, instead of stacking more HBM on a single GPU, NVIDIA is changing the structure toward growing the scale of the existing NVLink memory domain and distributing the data inside it better.

NVL576’s expanded scale-up domain

In the existing NVL72, the HBM of 72 GPUs was connected over NVLink. Because the connection was copper based, its limit was confined to the inside of a rack. Rubin Ultra, however, ties eight 72-GPU racks into a single NVLink domain. Keeping copper inside the rack while using NPO based optical links between racks, it effectively extends the scale-up network that was trapped in one rack out to 576 GPUs.

What should not be misunderstood is that NPO does not make another GPU’s HBM as fast as local HBM.

Rubin’s local HBM bandwidth is about 21 to 22TB/s, and NVLink 6’s GPU-to-GPU bandwidth is 3.6TB/s per GPU. Another GPU’s HBM is still far slower. What NPO changes is not speed but range. Peer HBM that could previously be used only within 72 GPUs is extended out to 576 GPUs, creating a much larger space to distribute model weights and KV cache even as HBM capacity per GPU shrinks.

In other words, NPO alone cannot make this approach work. What matters is NVIDIA’s software technology that makes this structure run well.

The software techniques that make the expanded memory structure possible

Wide Expert Parallelism places the experts of an MoE model across multiple GPUs and, instead of fetching the needed weights from another GPU, sends the token to the GPU where that expert lives. Because only small activations move over the network rather than large weights, the actual weight computation can be handled in each GPU’s fast local HBM.

When weights sitting on another GPU do need to be fetched directly, DWDP comes in. The weights needed for the next layer are fetched from a peer GPU’s HBM in advance, and this transfer runs concurrently while the current layer is being computed. Remote HBM does not become as fast as local HBM, but by moving data ahead of the moment it is needed, this approach covers the slow stretch.

KV cache handling uses the same approach. Helix stores the KV cache of long contexts across multiple GPUs, reducing the need for one GPU to hold it all, and Dynamo pushes KV that is not in immediate use down to CPU memory or storage. So memory gets shared out with frequently read weights and active KV kept in local HBM, distributable data placed in the HBM of other GPUs connected over NVLink, and rarely used data placed in CPU and storage.

These NVIDIA software techniques could be used under the previous approach as well, but back then they were tied to 72 GPUs. Now the NPO approach has extended this, and model weights and KV can be distributed across a larger NVLink domain.

To pull this together, I think the biggest reason for NVIDIA’s transition to HBM4 8-Hi is the HBM supply constraint.

But at the same time, I believe NVIDIA could not have decided on the move to 8-Hi this easily without its own NPO based optics and the software technology backing it.

It was a choice made possible because NVIDIA had, in house, the means to compensate at the system level even as capacity per GPU shrank.

I see this as a decision that only a vertically integrated company can make, one that goes beyond simply selling GPUs to designing the entire AI Factory including the optics and the software.

Share

## Does Memory Supplier Revenue Shrink?

The market’s worry about the HBM4 8-Hi transition is that with the HBM capacity per GPU coming in at half of what was expected, memory makers’ revenue would shrink by that much too. But I think this deserves a closer look rather than a simple calculation by HBM capacity ratio. Actual HBM revenue comes from HBM prices and from the volume memory suppliers can actually sell.

Thinking from the production side, lowering 12-Hi to 8-Hi means fewer layers to stack, so the same equipment can actually produce more HBM stacks. If stacking time scales with layer count, that is up to 1.5x, and stacking fewer layers also improves yield, so with each DRAM core die’s yield set at around 98%, the overall HBM yield improvement works out to 1.084x (based on the 4 fewer layers stacked versus 12-Hi). Multiplying the two, total effective output can rise up to 1.63x. Of course, the process also has fixed time unrelated to layer count, so the real number may be lower. These numbers should be read not as yield forecasts but as a sensitivity to stacking count.

What about price? With total bits reduced, total HBM prices will naturally come down. The easiest estimate is to assume price scales with bit count and apply a 10% per-GB discount. In that case the price versus HBM4E can fall to 45%, and multiplying by the 1.63x output increase calculated above gives a result of about 73% of planned 4E revenue.

But I think this per-bit calculation is too simple. The actual bit count falls by half, but the core die count is 8 versus 12, about two thirds, and the base die goes in the same whether it is 8-Hi or 12-Hi. On top of that, factoring in the bandwidth increase design that field chatter points to, the overall HBM price estimate can move higher. Calculating the HBM4 8-Hi price by die count ratio rather than in proportion to bits, at half price (same price per GB) total HBM revenue comes to 0.5 x 1.63 = 81.5% of planned 4E revenue, and at 60%, close to the die count ratio, 0.6 x 1.63 = 98%.

To sum up, if the memory makers could have supplied the full planned volume of 384GB HBM4E, the 8-Hi transition is indeed a clear mix down.

But as discussed earlier, my view is that applying that assumption as-is under the current supply constraint is a stretch. The situation right now is one where suppliers cannot sell more HBM because there is none left to sell.

One more thing worth noting is that this calculation rests on the premise that NVIDIA takes all of the volume freed up by the lower stack height. Since the 8-Hi transition is itself a move to build more GPUs out of scarce HBM, I take that as a natural premise in a sold-out market.

That said, if the bottleneck moves from stacking to packaging or rack integration, there is a possibility that this 1.63x assumption does not carry through to actual sales volume.

## What It Means for Each Memory Supplier and the Optical Names

The analysis in this section addresses only the HBM4 8-Hi move and the resulting impact of NPO adoption, and does not take other market factors into account. Once again, this is not investment advice and not a recommendation to buy or sell any security.

SK hynix

For Hynix, after falling behind in the HBM4 spec race, HBM4E and custom HBM were the stretch where it planned to open the next gap, so if 8-Hi HBM4’s life gets longer, the realization of that premium mix could also get pushed out, and that risk is real. Still, given Hynix’s high market share and the base die’s shift to TSMC logic process, it is worth watching what improvement Hynix can show through this 8-Hi despec change.

Samsung Electronics

Personally, I see Samsung as the biggest relative beneficiary of this change among the three memory makers. As the share of standard 8-Hi product rises, the axis of competition moves back from HBM4E qualification and custom design to yield, capacity, and supply stability. On top of that, if the lower HBM cost per GPU actually drives higher accelerator and rack shipments, Samsung can benefit across not just HBM but SOCAMM and server DRAM at the same time, which also matters.

Micron

The later the HBM4E transition, the more time there is to catch up on qualification and yield, but Micron’s NVIDIA-facing HBM capacity is relatively small, so a rise in 8-Hi volume is hard to capture one-for-one. Instead, I see the meaning for Micron in keeping the technology gap on HBM4E from widening quickly, and in continuing to benefit from growing AI server DRAM demand.

Beyond the three memory makers, the places I personally think deserve more attention in this change are optical and scale-up connectivity.

As explained above, the 8-Hi transition is not a simple HBM saving but a change premised on NPO based multi rack scale-up like NVL576, so the reduced memory content inside the system is matched by an increase in connectivity content.

ALAB, and Marvell

ALAB and Marvell are companies tied to the change in NVIDIA’s scale-up architecture, which makes them among the names that must be watched on this rise in connectivity content.

Coherent, and Lumentum

In NVIDIA’s multi rack scale-up structure, light source demand grows with the number of racks, so these two companies must be watched more closely as NVIDIA’s optical architecture takes concrete shape.

MACOM

As NPO or CPO expands, some of the functions that used to sit inside pluggable modules move out toward the package, and through that process optical semiconductors such as drivers, TIAs, and photodiodes gain importance. For this reason I personally think MACOM’s benefit case can also get stronger.

Credo

For Credo, the expansion of multi rack deployment itself is positive, but if scale-up optics heads in the direction of minimizing DSP, it can actually weigh on existing optical DSP content. So in this 8-Hi despec thesis, Credo carries the burden of confirming how much DSP the optical architecture leaves in place, rather than being a pure beneficiary.
