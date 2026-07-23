---
date: 2026-07-22
tags: [thesis-breakdown, semiconductors, capital-cycle, demand-architecture]
status: draft
audience: intermediate
source_note: "[[Mental Models/Industry - Semiconductors]]"
source: internal analysis
---

# How to Read the Semiconductor Cycle

**A semiconductor cycle is not one cycle. It is three clocks interacting: the economic cycle changes end demand, the capital-and-inventory cycle changes supply, and the technology cycle changes which part of the system is scarce.** The investment mistake is to follow only one clock. Strong demand can coexist with falling component prices; falling unit sales can coexist with a cycle bottom; peak margins can either collapse or become the next trough floor.

The practical task is to trace the sequence from demand to inventory, from inventory to capital spending, and from architecture to the next bottleneck.

## The three clocks

| Clock | What moves it | What investors often miss |
|---|---|---|
| Economic | Credit, interest rates, consumer spending, enterprise budgets | A tight macro regime can end a semiconductor up-cycle before a local shortage clears |
| Capital and inventory | Hoarding, factory investment, lead times, utilization | Reported demand can include speculative inventory rather than final consumption |
| Technology and architecture | New process nodes, chip designs, interconnects, packaging | Scarcity migrates; the winner from the last shortage may not own the next bottleneck |

These clocks operate at different speeds. Demand can fall within a quarter. A new fabrication plant may take years. A design qualification can lock a supplier into a platform for several product generations. That timing mismatch creates both the cycle and the opportunity.

## 1. A shortage turns inventory into speculation

The semiconductor capital cycle starts with a real constraint. Demand exceeds available supply, delivery times stretch, and customers fear missing production targets. They respond by ordering more than they need. Inventory stops behaving like a buffer and starts behaving like a commodity: buyers hoard it because they expect continued scarcity and higher prices.

Consider an illustrative customer that consumes 100 units each quarter. During allocation, it may order 130 to secure 100. The supplier sees demand for 130 and plans capacity against that number. Yet 30 units represent insurance, not consumption. If supply later improves, the customer can meet current production by drawing down inventory and cutting new orders below 100. The apparent demand decline becomes larger than the decline in final demand.

The cycle then follows a familiar sequence:

| Phase | Customer behavior | Supplier response | Financial effect |
|---|---|---|---|
| Shortage | Over-order and build safety stock | Raise price; maximize output | Revenue and margins rise quickly |
| Extrapolation | Treat scarcity as durable | Announce factories and equipment orders | Capital spending accelerates |
| Supply arrival | Stop hoarding; consume inventory | New capacity starts producing | Units and prices decouple |
| Air pocket | Cut orders below end consumption | Discount to protect utilization | Prices and margins fall |
| Capitulation | Clear excess stock | Cut production and cancel projects | Supply growth stops, preparing the next recovery |

The upturn is fast because every buyer scrambles for the same limited output. The decline is slower because suppliers resist idling expensive plants and customers need time to clear stock. It often ends with a sharp capitulation: price cuts, production shutdowns, and a halt in new factory starts.

For true cyclicals such as commodity DRAM and NAND, this asymmetry matters. The first earnings miss is rarely the clean entry signal. The higher-reliability window appears closer to capitulation, when weak demand is obvious but the supply response has finally turned negative.

## 2. Capacity must also survive the technology race

Semiconductor capacity is not homogeneous. A newer process can produce more useful bits, better performance, or lower cost per effective unit than an older line. A company therefore faces two risks at once:

1. **Invest too little:** remain financially disciplined, but fall behind the technology curve and lose customers or cost competitiveness.
2. **Invest too much:** build advanced capacity before demand is visible, then carry depreciation and debt through a downturn.

The middle path is rare: upgrade technology while staging capacity against credible customer commitments. [[Theses/TSM - Taiwan Semiconductor|TSMC]] illustrates the operating goal—invest ahead of demand without treating every forecast as an order. Samsung Foundry and [[Theses/INTC - Intel|Intel Foundry]] illustrate the two failure modes investors must test for: capacity ambition without enough qualified demand, and delayed execution that forces an expensive catch-up.

The economic cycle sits underneath this race. Higher rates or tighter bank credit can weaken PCs, smartphones, industrial equipment, and enterprise budgets together. A semiconductor bottleneck may remain physically unresolved while the spending cycle removes enough demand to shorten the upturn. Local supply analysis is therefore incomplete without a macro demand case.

## 3. Not every peak margin returns to the old trough

Industrial-cycle models assume that high margins attract new capacity, new capacity restores competition, and profitability returns toward its historical average. That model works best when products are interchangeable. It works less well when customers must qualify a supplier over several years and redesigning around a replacement creates yield, reliability, or schedule risk.

| Segment structure | Supply response | Expected margin pattern |
|---|---|---|
| Commodity output | Buyers can switch; capacity competes mainly on cost | Deep round-trip from peak to trough |
| Qualification-gated product | Few suppliers meet the required grade; switching is slow | Shallower compression and a rising trough floor |
| Temporary capacity bottleneck | Existing vendors can eventually add equivalent output | High margins persist only until capacity catches up |

Wafer-fabrication-equipment leaders such as [[Theses/AMAT - Applied Materials|Applied Materials]] and [[Theses/LRCX - Lam Research|Lam Research]] show why classification matters. Their 2019–2020 trough margins exceeded prior-cycle peaks. The observation does not prove cyclicality disappeared; service revenue, product mix, process complexity, and supplier concentration may all contribute. It does show that blindly forcing margins back to an old industrial average can understate structural improvement.

The test is whether the qualified supplier base expands fast enough to compete price back toward commodity economics. If qualification broadens, switching costs fall, or new tools reach equivalent yields, the rising-floor thesis weakens.

## 4. Units and prices reveal the phase

Revenue blends quantity and price, so it can conceal the turn. Split the two variables:

| Units | Prices | Likely phase |
|---|---|---|
| Rising | Rising | Shortage |
| Rising | Flat | Healthy expansion |
| Falling | Flat | Inventory disposal |
| Falling | Falling | Capitulation |

The strongest early signal is the second derivative: **prices begin to firm while units are still falling**. Final demand can remain weak, but the rate of deterioration has changed. Inventory is closer to balance, production cuts are taking effect, or buyers have exhausted their buffers. Headline revenue may still look poor because price stabilization leads unit recovery.

Three forward indicators help test the signal:

- **Distributor lead times:** stabilization or extension suggests slack is disappearing.
- **OEM inventory days:** a decline shows that customers are consuming stock rather than moving it elsewhere.
- **“Allocation” language:** suppliers ration output only when orders again exceed available supply.

One spot-price move is not enough. It can reflect a thin market, a temporary production outage, or a narrow product mix. A credible bottom call needs confirmation across inventories, contract pricing, lead times, and utilization.

## 5. Architecture moves the bottleneck—and the profit pool

Semiconductor scarcity is not fixed to one component. A system redesign changes the volume, performance, and qualification requirements of every layer around it. Architecture announcements are therefore forward maps of capital spending and pricing power.

| Transition | What changes | Where scarcity can migrate |
|---|---|---|
| Monolithic chips → chiplets | One large die becomes several specialized dies joined together | Advanced packaging, substrates, bonding, and test |
| PCIe Gen5 → Gen6 plus CXL | Memory becomes more pooled and disaggregated | High-speed interconnect, controllers, and memory expansion |
| NRZ → PAM4/PAM6 and co-packaged optics | More data must move through each optical link | Photonic integration rather than the conventional PCB |
| Individual GPUs → rack-scale systems | Performance depends on hundreds of accelerators working as one | Interconnect bandwidth, power delivery, and system integration |

The logic flow is simple: identify the new architecture, translate it into changed physical requirements, find the least elastic input, then ask which supplier is qualified to provide it. That supplier may gain pricing power before its revenue mix visibly changes.

A bottleneck is not automatically a durable moat. The investment value depends on how long qualification, technical difficulty, or capital intensity prevents supply from responding. A transient shortage creates cyclical rent; control of a hard-to-replace layer can create structural rent.

## 6. Inventory turns before consensus does

As a working model, inventory builds through distributors, original-equipment manufacturers, contract manufacturers, and finally the spot channel. The unwind appears in reverse. Spot supply tightens first, contract prices follow one or two quarters later, then OEM and distributor inventories normalize.

This sequence explains why the psychological bottom can lag the operational bottom. Analysts may still be cutting estimates when spot conditions have stopped worsening. Reported revenue confirms the turn later because contracts reset slowly and accounting data describes the previous quarter.

The gap is useful only if the chain is mapped correctly. Spot strength without lower channel inventory may be noise. Lower inventory without price stabilization may mean end demand is still shrinking. The high-quality signal is a sequence: inventory falls, spot prices firm, contract pricing follows, and lead times extend.

## A practical decision framework

1. **Classify the segment.** Is it commodity, semi-cyclical, or qualification-gated? Do not apply NAND margin assumptions to a monopolistic inspection tool.
2. **Locate the cycle phase.** Separate units from prices and focus on the change in direction, not the level.
3. **Strip out speculative demand.** Compare customer orders with end consumption and inventory days.
4. **Map the architecture.** Ask which physical requirement grows fastest and which qualified capacity responds slowest.
5. **Name the falsifier.** A memory-bottom call fails if spot prices firm but inventories keep rising and contract prices do not follow. A structural-margin thesis fails if new qualified suppliers enter and trough margins fall below the prior-cycle floor.

The central lesson is causal, not predictive. Semiconductor returns depend on distinguishing real demand from hoarding, useful capacity from obsolete capacity, and temporary scarcity from a qualification-protected bottleneck. Follow those causal chains and the cycle becomes legible before the income statement makes it obvious.

## Related Notes

- [[Mental Models/Industry - Semiconductors]]
- [[Mental Models/Generalist - Overview]]
- [[Theses/TSM - Taiwan Semiconductor]]
- [[Theses/INTC - Intel]]
- [[Theses/AMAT - Applied Materials]]
- [[Theses/LRCX - Lam Research]]
