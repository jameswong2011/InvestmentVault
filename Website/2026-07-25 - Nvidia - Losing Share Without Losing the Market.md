---
date: 2026-07-25
tags:
  - essay
  - investment-case
  - laniakea-partners
  - semiconductors
  - AI
  - NVDA
status: draft
audience: intermediate
source_note:
  - "[[Theses/NVDA - Nvidia]]"
  - "[[Thesis Breakdowns/2026-07-25 - NVDA]]"
  - "[[Website/2026-07-22 - How Laniakea Partners Invests]]"
  - "[[Theses/AMD - Advanced Micro Devices]]"
  - "[[Theses/AVGO - Broadcom]]"
  - "[[Theses/CRWV - CoreWeave]]"
  - "[[Theses/NBIS - Nebius Group]]"
  - "[[Sectors/Compute & AI Compute Accelerators]]"
  - "[[Sectors/Custom Silicon & Networking Semiconductors]]"
  - "[[Sectors/Neoclouds & GPU-as-a-Service]]"
  - "[[AI Bubble Risk and Semiconductor Valuations]]"
  - "[[Mental Models/Generalist - Overview]]"
  - "[[Mental Models/Industry - Semiconductors]]"
  - "[[Mental Models/Lens - Automation & AI Readiness]]"
  - "[[Mental Models/Lens - Value Layer Monopoly]]"
source: internal synthesis
---

# Nvidia: Losing Share Without Losing the Market

**The bullish case for Nvidia does not require 87% market share, an uninterrupted AI spending boom or a successful conversion into a conventional software company. It requires AI compute to expand faster than Nvidia’s share declines, CUDA to remain the default starting point for new workloads, and free software to keep turning silicon into a premium-priced platform. At roughly 21 times forward earnings, the market is pricing either a much faster collapse in those advantages or an AI capital-spending bust.**

Both risks are real. Nvidia’s largest customers are building competing chips. AMD finally has anchor customers. Huawei has removed most of China from Nvidia’s addressable market. GPU rental rates are falling at the margin while hyperscaler capital spending is approaching the cash their operations generate.

The same evidence also supports a different conclusion. Nvidia produced $215.9 billion of revenue in its last fiscal year, up 65%. Its latest quarter grew 85%, gross margin reached 74.9%, and the next-quarter revenue guide rose to $91 billion. Earnings grew faster than the share price, compressing the multiple from more than 45 times in 2024 to about 21 times today. The business is still behaving like a compounder while the stock is being valued as though the present economics are near a cyclical peak.

The investment question is therefore not whether Nvidia will lose share. It will. The question is whether share loss matters more than market expansion, and whether the company owns enough of the software and system layer to preserve pricing power as the chip layer fragments.

## A market-average multiple is a forecast of an ending

Calling Nvidia cheap requires precision. A roughly $5 trillion company trading near 20 times trailing revenue is not conventionally cheap. Its earnings multiple is low relative to its growth, margins and strategic position. At about 21 times next year’s expected profit—roughly the multiple of a mature large American company—the price is forecasting an ending rather than another beginning.

That ending can take two forms:

1. **Share loss:** Google TPU, Amazon Trainium, Meta MTIA, Microsoft Maia, OpenAI’s Jalapeño, AMD and specialist inference chips take enough workloads to push Nvidia’s revenue and margins toward ordinary semiconductor economics.
2. **Demand loss:** AI infrastructure spending outruns the revenue it can support, hyperscalers enter a digestion phase, neocloud financing tightens and today’s earnings prove to be a peak.

The market does not need either outcome to arrive next quarter. It only needs to believe that one will arrive soon enough to truncate the duration of Nvidia’s cash flows. This explains why a $4 billion quarterly beat barely moved the stock: investors are no longer debating the next print. They are debating what the business looks like after the buildout.

## Nvidia sells an AI factory, not a GPU

The competitive debate is often reduced to accelerator benchmarks. Nvidia increasingly sells a coordinated system: GPUs, CPUs, high-bandwidth interconnect, Ethernet or InfiniBand networking, rack architecture, compilers, libraries, deployment software and domain-specific frameworks. A buyer is purchasing time-to-working-compute, not a transistor count.

This matters because competitors attack different pieces of the system. AMD can match selected inference benchmarks. Broadcom can help a hyperscaler design a cheaper chip for a stable workload. Groq can improve low-latency token generation. Open Ethernet can weaken proprietary networking. None yet reproduces the full training-to-deployment path across data centres, industrial simulation, robotics and edge inference.

Nvidia’s product has expanded in three directions at once:

- **Inside the rack:** Vera CPUs, Rubin GPUs, NVLink, BlueField and Spectrum-X increase Nvidia content per AI factory.
- **Across customers:** sovereign AI adds governments and national clouds to hyperscalers and model laboratories.
- **Beyond language models:** Omniverse, PhysX, Warp, Cosmos, Isaac, GR00T, Jetson and DRIVE extend the platform into factories, robots and vehicles.

A rival can win a chip socket without displacing the system. That distinction is the foundation of the bullish case.

## The attackers are real, but each attacks a narrower surface

| Attacker | Where it is strongest | Evidence the threat is real | Structural limit today |
|---|---|---|---|
| **AMD** | Merchant second source; standard inference; customers that need pricing leverage | OpenAI and Meta committed 6GW each; MI355X reached near-B200 performance on selected inference tests | Roughly 11% of critical CoWoS capacity versus Nvidia near 60%; no demonstrated large-scale training parity; no equivalent simulation or Physical AI stack |
| **Google, Amazon, Meta, Microsoft and OpenAI custom silicon** | Captive, high-volume workloads whose architecture has stabilised | TPU and Trainium run large shares of Gemini and Claude inference; MTIA, Maia and Jalapeño are scaling | Each program requires dedicated software, kernels and multi-year re-spins; best suited to repetitive workloads rather than a changing frontier |
| **Broadcom, Marvell and other design partners** | Turning hyperscaler specifications into leading-edge ASICs and open networking | Broadcom’s AI revenue and customer list are compounding faster than merchant GPU growth | They capture silicon rent rather than eliminate it; custom-ASIC margins remain close to Nvidia’s, and they do not own the end-to-end developer platform |
| **Groq, Cerebras and inference specialists** | Decode, latency-sensitive serving and memory-bandwidth-bound workloads | Nvidia replaced its planned Rubin CPX path with a roughly $20 billion Groq licensing arrangement | Specialist architectures address one stage of the workload; Nvidia can license or bundle them into the broader platform |
| **Huawei and China’s domestic stack** | China, where export controls forced a parallel ecosystem | Ascend 950PR is shipping, ByteDance has committed orders, and Nvidia’s China share is effectively zero | Primarily a geopolitically separate market; manufacturing yield, HBM and global software adoption still constrain expansion outside the Chinese bloc |
| **Open networking standards** | Weakening Nvidia’s proprietary fabric toll | UEC, UALink and Broadcom Ethernet offer multi-vendor alternatives | Nvidia now competes in Ethernet through Spectrum-X and licenses NVLink Fusion to partner silicon, converting part of the threat into ecosystem participation |

The outside view is hostile to permanent dominance. There is almost no precedent for one supplier retaining more than 80% of a market worth hundreds of billions of dollars while its largest customers build substitutes. A bullish thesis that assumes Nvidia keeps peak share ignores the base rate.

The stronger thesis accepts the base rate and asks a different question: which workloads leave, and how quickly does the denominator grow?

## Nvidia does not need to retain peak share

AI accelerator share is becoming a misleading statistic because captive silicon expands the measured market even when Nvidia sales continue rising. A new Google TPU deployment counts as Nvidia share loss whether it replaces an Nvidia order or adds capacity Google could not otherwise obtain.

The arithmetic allows substantial erosion:

| Illustrative scenario | AI accelerator market | Nvidia share | Nvidia-addressable revenue pool |
|---|---:|---:|---:|
| Current industry estimate | More than $200B | ~75% | More than $150B |
| 2030 scenario | $500B | 60% | $300B |

This is not a forecast. It shows why share and revenue can move in opposite directions. Nvidia can lose 15 percentage points of share and still roughly double the accelerator revenue pool available to it. The calculation also excludes CPUs, networking, sovereign systems, automotive, robotics and industrial simulation.

The decisive variable is the mix of **new** and **frozen** workloads. Stable workloads migrate toward ASICs because repeated execution justifies the fixed engineering cost. New architectures, research workloads and smaller domains begin on general-purpose hardware because flexibility matters more than the last increment of cost per token. Nvidia wins if the pool of new workloads grows faster than old workloads become stable enough to specialise.

AI has repeatedly changed the target: diffusion, mixture-of-experts models, long-context inference, agents, world models and Physical AI have each altered the optimal compute pattern. Every change rewards a programmable platform and forces custom silicon to catch up. DeepSeek’s reported frontier-class training run on non-Nvidia hardware is the clearest adverse signal because it suggests the frontier can migrate too. Large-scale training parity—not another inference benchmark—is the test that can break the bullish segmentation argument.

## Free software is the source of the hardware premium

CUDA is often described as switching cost. That understates what Nvidia gives customers.

CUDA lets developers express general computing tasks on Nvidia GPUs. More than 400 CUDA-X libraries then provide pre-optimised building blocks for model training, inference, genomics, fluid dynamics, quantum simulation, medical imaging, robotics and data science. Code written for Pascal in 2016 can run on Rubin in 2026 because Nvidia has preserved compatibility while changing the hardware underneath it. Six million developers now build inside the ecosystem, up from 1.8 million in 2020.

The bundle performs four economic jobs:

1. **It removes engineering work.** A new workload can inherit libraries, compilers, tools and framework integrations rather than rebuilding low-level kernels.
2. **It reduces deployment risk.** Enterprises buy a tested path from prototype to production rather than a chip plus an integration project.
3. **It transfers each hardware generation to the installed base.** Existing applications gain from new silicon without being rewritten from scratch.
4. **It makes experimentation cheap.** Developers can test a new architecture before its economics are stable enough to justify custom silicon.

Rivals pay a replication tax. Amazon describes Anthropic engineers helping build the Trainium software library base. TPU developers tune Pallas and XLA. Trainium users tune Neuron kernels and custom operators. AMD’s ROCm is closing this gap at the framework layer, but every missing library or debugging tool consumes scarce engineering labour that Nvidia customers receive as part of the platform.

The software is free because the scarce complement is the hardware. Nvidia gives away the low-marginal-cost layer, expands the developer ecosystem, and charges through GPUs, networking and complete systems. The hardware carries the software rent.

## Giving software away protects margins better than charging for it

Nvidia’s 70–75% gross margins look anomalous for hardware because the income statement records a physical product while the customer pays for an accumulated intangible asset. Twenty years of software development, compatibility and developer support are monetised inside the price of each new system.

This structure makes the margin more durable in three ways:

- Software costs are largely fixed and can be amortised across a rapidly expanding hardware base.
- Customers compare total cost and time to deployment, not the GPU’s manufacturing cost in isolation.
- A lower software price expands adoption while making departure more expensive as code, skills and workflows accumulate.

Nvidia may also be undercharging deliberately. Rental-economics work places Rubin’s value-based ceiling near twice its cost-anchored floor, leaving meaningful server-price headroom before neocloud returns become uneconomic. Extracting all of that value today would be strategically destructive. It would weaken customers, invite regulators and give hyperscalers a larger economic incentive to accelerate custom silicon.

Pricing below the theoretical maximum can therefore sustain premium pricing for longer. Nvidia resembles a central bank for AI compute: it leaves some surplus with customers so the ecosystem can reinvest, while keeping enough of the value to earn software-like hardware margins.

The failure condition is clear. If AI architectures stabilise, framework abstractions make backends interchangeable and rivals reproduce the required library depth, the cost of leaving CUDA falls. At that point free software becomes an expense rather than a toll-generating asset. Margin durability depends on continued platform differentiation, not on the word “CUDA.”

## The neocloud game is about who owns the customer

Nvidia and the hyperscalers are playing mirror-image strategies.

| Player | Dependency it wants to avoid | Strategic countermove |
|---|---|---|
| **Nvidia** | Amazon, Microsoft and Google controlling the cloud customer relationship while designing replacement chips | Allocate GPUs to and invest in CoreWeave, Nebius, Nscale, Lambda and other neoclouds; invest directly in major AI labs |
| **Hyperscalers** | Nvidia controlling the silicon roadmap, allocation and economics | Fund TPU, Trainium, MTIA and Maia; commit to AMD as a merchant second source |
| **AI laboratories** | Captivity to either one cloud or one silicon supplier | Multi-source across Nvidia, AMD, TPU and Trainium while accepting capital and capacity from every side |

If all AI compute lived inside three hyperscalers, those companies would own distribution, customer billing and the alternative silicon. Nvidia could be squeezed between a concentrated buyer group and its own customers’ chips. Neoclouds fragment that layer. They give AI labs an outside option, create additional routes to market, and preserve a class of cloud operator whose business depends on Nvidia rather than on replacing it.

GPU allocation is the mechanism. During scarcity, an Nvidia-backed neocloud receives hardware, the hardware wins customers, those contracts unlock financing, and financing funds the next order. Nvidia’s investment is therefore not only a financial stake; it is a credential that determines which downstream capacity providers can scale.

The equilibrium is not Nvidia defeating the hyperscalers. Each side wants diversity in the other side’s layer. Hyperscalers will keep buying Nvidia while building ASICs. Nvidia will keep selling to hyperscalers while supporting alternative clouds. The laboratories will arbitrage both. Nvidia wins this equilibrium if it remains the common flexible substrate across the fragmented demand channels.

## Vendor financing is the fault line in the strategy

The same loop can become circular. Nvidia invests in a neocloud or laboratory; the recipient buys Nvidia systems; Nvidia recognises revenue; the buyer reports backlog; and Nvidia’s equity stake appreciates as the boom it financed expands. Lucent and the competitive telecom carriers followed a similar pattern around 2000.

CoreWeave’s roughly $46 billion of liabilities against about $3.3 billion of equity makes the risk visible. Meta’s move into third-party GPU rental also proves that hyperscalers can attack the neocloud layer directly. Falling spot rental prices may eventually flow into contract renewals and the value of GPU collateral.

The bullish distinction is that Nvidia is not the leveraged owner of most data-centre assets. It earns cash when systems ship; neocloud shareholders and creditors bear the depreciation, power and refinancing risk. Take-or-pay contracts and deep-pocketed counterparties also make present demand more substantial than the speculative telecom orders of 1999.

That distinction narrows as Nvidia’s equity and credit exposure grows. The neocloud strategy is a moat only while end demand exists independently of Nvidia’s financing. A rise in cancelled contracts, credit support or unsold capacity would turn strategic distribution into evidence that the supplier is manufacturing its own customer.

## The AI bubble can be real without invalidating Nvidia

The bear arithmetic deserves full weight. Hyperscalers plan roughly $725–785 billion of capital spending in 2026, while annual AI-related revenue is estimated near $280–320 billion even when infrastructure vendors are included. Capital spending may exceed hyperscaler operating cash flow during 2026. B200 rental prices fell roughly 30% in three weeks. These are late-cycle signals, not noise.

The counter-evidence is equally concrete. Data-centre vacancy remains near record lows. TSMC says advanced packaging capacity is limiting customer growth. Sovereign AI produced about $30 billion for Nvidia last fiscal year and is growing across 40 countries. Token consumption and leading laboratory revenue are compounding even as the price per token collapses.

This looks less like demand fabricated from nothing than a timing mismatch between infrastructure installation and application monetisation. Historical technology booms often overbuild the network before users discover its most valuable applications. The overbuild can destroy leveraged financiers while making the installed capacity cheap enough to unlock the next adoption wave.

Nvidia is better positioned than the owners of dark fibre because it is fabless, collects cash on shipment and owns the software standard used to exploit the installed base. It is still exposed to a digestion phase through its 90% data-centre revenue concentration. The bullish claim is not that cyclicality disappears. It is that the next trough leaves a much larger installed base, a broader developer ecosystem and more recurring workloads than the last one.

## Omniverse is a software option hidden inside hardware economics

Nvidia is already software-defined, but it is not yet a software business in the conventional financial sense. The segment containing Omniverse generated only about $3.2 billion in the last fiscal year, less than 2% of total revenue. Omniverse is now free for production use. Direct subscription revenue cannot explain the current valuation.

The software transition is occurring in three stages:

| Stage | Product role | Primary monetisation |
|---|---|---|
| **Today: software prices hardware** | CUDA, CUDA-X, PhysX, Warp and AI frameworks make Nvidia systems easier to adopt and harder to replace | GPU, networking and rack premium |
| **Emerging: enterprise and licensed services** | AI Enterprise support, DSX deployment software, licensed architectures and revenue-sharing structures | Subscriptions, licensing, support and participation in customer economics |
| **Long term: operating layer for the physical world** | Omniverse and OpenUSD connect industrial design tools, digital twins, simulation, synthetic data and robot deployment | OVX/RTX compute, Jetson and DRIVE attach, enterprise services and potential platform revenue |

OpenUSD is the strategic wedge. The standard moved under Linux Foundation governance, so Nvidia does not own it. That openness encourages Siemens, Dassault, PTC, Cadence, Synopsys and customers such as BMW and General Motors to integrate without accepting a proprietary file-format trap. Nvidia wrote much of the reference implementation and supplies the compute, simulation libraries and edge hardware that make the standard useful.

This is an “open standard, preferred implementation” strategy. HTML is open, yet browsers, cloud platforms and developer tools still captured enormous value around it. If OpenUSD becomes the common representation of factories, warehouses and robots, Omniverse can sit in the execution path where industrial context is assembled, simulated and converted into machine behaviour.

The opportunity extends beyond selling software seats. A factory twin creates demand for simulation compute; synthetic data trains a model on Nvidia systems; the trained policy runs on Jetson or DRIVE at the edge; operating data returns to the simulation loop. Nvidia can monetise every transition even if the core file standard remains free.

The risk is that industrial software incumbents retain the customer relationship while treating Nvidia as a replaceable backend. Physical deployment also moves more slowly than data-centre AI because factories, vehicles and robots face safety, integration and capital-budget constraints. Omniverse is an option on a roughly $600 billion industrial-software market, not a proven second revenue engine.

Nvidia does not need to replace hardware revenue with SaaS. The more plausible transition is from a hardware company with free software to a systems platform with recurring, software-shaped economics. Direct software revenue is upside; software-supported hardware pricing is already the business.

## What the bullish lens requires

The bull case survives even with material competition if five conditions hold:

1. **Market growth outruns share loss.** Nvidia can fall toward 60% share and still compound revenue if AI accelerator demand reaches the projected scale.
2. **New workloads continue to begin on Nvidia.** ASICs may absorb mature inference while CUDA remains the research, training and emerging-workload default.
3. **Software preserves system-level pricing.** Gross margins can moderate without collapsing toward commodity hardware economics because customers still pay for time-to-deployment and compatibility.
4. **Demand channels remain independent.** Neocloud and laboratory purchases must be supported by real end customers and durable contracts rather than Nvidia capital alone.
5. **At least one platform expansion works.** Sovereign AI, networking, Vera CPUs or Physical AI does not need to replace the GPU franchise; one or two becoming material would extend earnings duration beyond what a 21 times multiple implies.

The valuation creates the asymmetry. The price already assumes that peak share cannot last and that present growth fades. It assigns little value to Omniverse, Physical AI or a durable software-supported margin floor. The bull does not need every option to succeed.

## What would prove the case wrong

The thesis fails if share loss reaches the flexible frontier rather than remaining concentrated in mature workloads.

The clearest evidence would be a competitor demonstrating large-scale mixture-of-experts training parity in an independent benchmark, followed by production adoption without a material software or reliability penalty. That would show CUDA’s last exclusive stronghold becoming interchangeable.

A second failure path is demand. Hyperscaler guide-downs combined with GPU rental prices falling toward cash-cost levels would show that the market grew through duplicated or speculative capacity rather than workload consumption. Neocloud contract cancellations or credit deterioration would amplify the signal.

A third is margin. Sustained gross-margin compression alongside falling software switching costs would prove that Nvidia’s bundle no longer carries a premium. Share loss with stable margins is manageable; share loss and declining system economics are not.

Omniverse has its own test. Industrial partners must move from announcements and pilots into repeatable production deployments that drive compute, edge-hardware or software revenue. If OpenUSD adoption grows while Nvidia attach does not, the standard succeeded and the investment thesis did not.

## Nvidia can lose share and remain the toll road

Nvidia’s peak market share was a product of an industry with one viable general-purpose AI platform and customers desperate for any available compute. That condition was never permanent. AMD has become a real second source, hyperscaler ASICs have become real products, Huawei has built a parallel Chinese stack, and specialist architectures will take parts of inference.

The market may be drawing the wrong conclusion from that inevitability. Nvidia does not need to own every chip. It needs to remain the place where new workloads begin, the system against which alternatives are measured, and the software layer whose free tools make its hardware the lowest-risk path to deployment. It can give up frozen workloads while expanding into networking, CPUs, sovereign systems and the physical world.

At roughly 21 times forward earnings, investors are being paid to test duration rather than dream about dominance. If AI spending collapses before applications monetise, the multiple is a warning. If the market expands through share loss and the software bundle holds system economics above semiconductor norms, the same multiple is misclassifying a platform as a cycle.

Nvidia can lose share without losing the market. The bullish case is that the market has already priced the former and is still underestimating the latter.
