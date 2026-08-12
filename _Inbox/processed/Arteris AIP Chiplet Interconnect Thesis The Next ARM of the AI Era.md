---
date: 2026-08-06
tags: [research, email-backfill, Temple8]
source: 'https://temple8capital.substack.com/p/arteris-aip-chiplet-interconnect-thesis'
source_type: web-clip
sender: temple8capital@substack.com
---

# Arteris AIP Chiplet Interconnect Thesis The Next ARM of the AI Era

Temple 8 Long Thesis: Arteris (AIP) —August 2026

This is another example of an exceptionally rare company that once you understand it, you can see the potential a decade into the future where this company is uniquely positioned to become an IP giant of the AI chiplet era.

Arteris is rising as the leading edge independent vendor of network on chip (NoC) interconnect IP, the packet-switched routing fabric that moves data between processor cores, accelerators, and memory inside modern system on chip (SoC) and multi-die “chiplet” designs. The company monetizes through the same upfront license and per-unit royalty archetype as Arm Holdings, but where Arm licenses CPU cores, Arteris licenses the interconnect between them. They also offer SoC integration automation software (Magillem) and as of January 2026 they also offer hardware security verification tools via the Cycuity acquisition.

The bull case is built on a solid foundation as monolithic dies transition to chiplet-based, multi-die architectures, the number of interconnect networks per design multiplies. Arteris cites 5 to 20 NoCs per modern chiplet, and interconnect content per design rises. Design-win evidence in 2025 and 2026 is unusually strong with extensive design wins as follows; AMD licensed FlexGen for next-generation AI chiplets (August 2025), Renesas deployed FlexNoC in its 3 nm R-Car Gen 5 automotive platform with UCIe chiplet extensions (March 2026), SiEngine, NXP, Black Sesame, Blaize, and a hyperscaler security win followed. Financially, the company is accelerating: Q1 2026 revenue grew 39% YoY to $22.94M, FY2026 revenue guidance was raised to $91M to $95M (+32% at midpoint), ACV plus royalties hit a record $92.8M (+39%), and trailing-twelve-month variable royalties grew 67%, early confirmation that the license to royalty “J-curve” is beginning to bend upward.

## 1. Company Overview and Business Model

### 1.1 What Arteris sells

Founded in 2003 and headquartered in Campbell, California, Arteris pioneered commercial NoC interconnect IP and reports that its technology has been incorporated into more than four billion production SoCs and chiplets since inception.

The company went public on October 26, 2021, pricing 5.0M shares at $14.00 for $70M gross proceeds; Jefferies and Cowen were lead bookrunners, notable because the same two firms (Jefferies, TD Cowen) remain covering analysts today. Arteris remains a small organization, 299 employees at year-end 2025 (353 per more recent data), offices across the US, France, China, Korea, Japan, Taiwan, and Poland, that punches far above its headcount because its customers’ design teams embed Arteris IP deep into multi-year silicon programs.

### 1.2 The License-plus-Royalty Engine

The monetization model mirrors Arm’s: customers pay upfront licensing, support and maintenance fees to integrate Arteris IP into a design (FY2025: $63.9M, 90% of revenue), and Arteris later collects variable royalties per chip shipped once designs reach high-volume manufacturing (FY2025: $6.6M, +50% YoY), plus a small professional-services line. The strategic consequence is a deliberate J-curve: today’s licensing harvest funds R&D, while the 2024 to 2026 wave of AI and automotive design starts, 83 confirmed design starts in 2025 versus 76 in 2024, against a cumulative base of 725 or more, incubates the royalty streams of 2027 to 2030. Historically the company reports ~90% average customer retention, reflecting multi-year embedded relationships.

Because royalties carry near-zero marginal cost, the mix shift matters enormously for terminal economics. Arm, the model’s proof case at scale, derived 53% of its $4.92B FY2026 revenue from royalties at ~97% to 98% non-GAAP gross margin; Arteris today is at the opposite end of the same journey, with royalties at ~9% of revenue but compounding at 50% to 67%. The entire long term bull thesis, addressed quantitatively in Section 8, is a bet on that convergence.

### 1.3 Key performance indicators and disclosure quality

Because Arteris sells chip blueprints (intellectual property) rather than physical hardware, standard accounting numbers look jumpy and messy from quarter to quarter depending on when big checks happen to clear.

To see if the business is actually healthy, you have to look at their contracted backlog and recurring fees. Right now, those underlying metrics are hitting record highs.

## 2. The Technology: Why the Interconnect Became the Bottleneck

### 2.1 From buses to networks-on-chip

In traditional chips, data moved between the processor, graphics unit, and memory on simple, direct physical wires (called buses or crossbars). It worked fine when chips were simpler. Today, chips are so tiny and complex that engineers stitch together dozens of specialized mini-chips (chiplets) into a single tiny footprint. The following problems emerge:

- Routing Congestion. There is literally not enough physical space on the chip to lay down the trillions of individual copper wires needed to connect every single piece directly.

- Timing-Closure Failure = Data Arriving Late In a microchip, signals must arrive in perfect rhythm (down to a fraction of a nanosecond). When wires are crammed and tangled, data gets delayed in transit. If a signal arrives even slightly out of sync, the whole chip glitches.

- Power Draw = Overheating Shoving electrical signals down miles of cramped, high-resistance copper wire requires massive amounts of power and generates high amounts of heat.

- Deadlock Risk = Total Gridlock Imagine 20 delivery trucks (processing cores) all trying to enter the exact same warehouse loading dock (shared memory) at the exact same second. If nobody can back up or yield, the entire system completely freezes.

Arteris explains in its annual reports that as microchips become smaller and more complex, managing internal traffic becomes one of the most critical challenges in chip design. A Network-on-Chip solves these physical challenges by breaking data into small packets and steering them through mini digital routers, essentially embedding a tiny internet inside the chip to manage data flow smoothly. Arteris’s design software automates this process to dramatically lower costs, reduce power consumption, and speed up development time. By using this software, engineers can complete design iterations up to ten times faster, cut manual adjustments by more than ninety percent, and reduce total wire length inside the chip by up to thirty percent.

The semiconductor industry’s shift toward chiplets multiplies this opportunity dramatically. Instead of making one giant chip, companies now stitch together multiple smaller mini-chips into a single package. Because each individual mini-chip needs its own internal networks plus additional routing to talk to its neighbors, a single modern chiplet system can contain anywhere from five to twenty separate interconnect networks. This creates a toll booth business model for Arteris, where revenue grows with every additional network instance designed into a system rather than depending on a single client’s success. The power of this model is proven by major industry players like AMD, which openly admitted that despite having its own world-class internal networking technology, it still licenses Arteris software across a wide range of its chiplets.

### 2.2 Ncore, coherence, and the CXL bridge

Ncore is Arteris’s flagship product, serving as the central traffic controller inside complex microchips. It ensures that various processing elements, including Arm CPUs, RISC-V CPUs, GPUs, and AI accelerators, can seamlessly work on the same shared data pool simultaneously without reading outdated information or causing system conflicts, effectively solving a major technical challenge known as cache coherence. By moving data at ultra-fast speeds with minimal latency, Ncore prevents expensive AI processors from sitting idle while waiting for memory to catch up. Furthermore, Arteris uses universal plug-and-play standards such as AMBA CXS, CXL and UCIe, allowing chip designers to deploy a consistent data routing strategy across a single die, stacked modular chiplets, or an entire server rack. This technology includes a version certified to ASIL-D, the highest automotive safety standard required by law, which has helped Arteris capture an estimated 70% to 80% market share in the advanced driver-assistance chip sector.

Despite this strong market position, describing Arteris as a total monopoly overstates its competitive moat. The largest semiconductor companies, such as NVIDIA, Intel, AMD, and Arm, possess the immense financial and engineering resources required to develop their own proprietary internal traffic controllers and interconnects. Instead, Arteris thrives as the indispensable vendor for the broader market of mid-tier silicon developers and custom chip creators who lack hundred-million-dollar budgets to build complex traffic management systems from scratch. As the semiconductor industry increasingly shifts toward stitching together smaller, modular mini-chips, this addressable market of independent chip designers continues to expand rapidly.

## 3. Market Context: The Chiplet Tailwind Is Real and Measurable

### 3.1 The semiconductor IP layer

The overall market for microchip design blueprints sits around eight billion to nine billion dollars, but exact market estimates vary too wildly between research firms to take any single top-line number as gospel. What actually matters is the heavy concentration at the top, which is verified by official corporate filings rather than third-party reports. Arm alone commands roughly forty-one percent of all design licensing revenue, and the top five players combined control up to three-quarters of total customer spending. However, measuring Arteris against this entire multi-billion-dollar pool is misleading because Arteris does not sell central processors or graphics chips. It operates exclusively in the system traffic and interconnect sub-segment, which is a much more focused market worth roughly one point two billion to one point five billion dollars.

Against this specific target market, Arteris’s seventy-seven million dollars in trailing revenue represents roughly a five to six percent market share, which is considerable. This interconnect niche is benefiting directly from the biggest modern tech trends, including artificial intelligence, automated driving, and modular chiplet design. The bullish thesis for Arteris simply requires the interconnect sub-segment to outgrow the broader chip market as multi-chiplet designs become standard, allowing Arteris to ride a powerful industry wave while defending its current position.

### 3.2 Chiplet and UCIe adoption

Headline market estimates project the chiplet industry to surge from roughly fifty-two billion dollars in 2025 to over one hundred fifty-seven billion by 2030, but raw market size can be misleading when evaluating Arteris. That is because Arteris gets paid for every unique chip design project rather than earning a percentage of total silicon sales volume. The metrics that actually drive revenue are design penetration and network density. The proportion of new chip designs built on chiplet technology is jumping from around five percent to more than thirty percent, with each system requiring anywhere from five to twenty separate internal networks. This creates a compounding growth engine driven by both breadth and depth, as more client projects switch to chiplets and each project consumes a larger stack of interconnect licenses.

This expansion is closely tied to standard connection technologies like UCIe, which allow mini-chips from different suppliers to communicate seamlessly. The dedicated market for these chiplet interconnects is expected to leap from two point six billion dollars in 2025 to over twenty-three billion by 2034, spearheaded by universal open standards that now count more than one hundred thirty member companies. A practical example of this architecture in action is the Renesas R-Car X5H automotive processor. Built on an advanced three-nanometer manufacturing process, it uses Arteris networks to connect its central processing, graphics, and AI blocks under strict automotive safety standards. By adding modular mini-chips through standard connections, it multiplies its AI processing speed fourfold, proving how Arteris directly monetizes the industry transition toward larger and more powerful multi-chip systems.

Two key drivers propel Arteris’s future revenue, starting with the automotive market as its primary volume engine. Car technology is already Arteris’s strongest sector, where the company commands an estimated seventy to eighty percent market share in driver-assistance chips. This market is expanding rapidly as modern vehicles incorporate more digital features, with automotive chiplet demand growing at an estimated twenty-eight percent annually.

The second growth driver is artificial intelligence, which acts as the complexity engine that creates massive royalty upside. Company disclosures show that AI and machine learning account for roughly forty-two percent of customer demand, while enterprise systems represent another thirty percent. This exposure ties Arteris’s long-term financial upside directly to advanced AI chip programs, such as AMD chiplets, hyperscaler ASICs, and Blaize edge AI chips. While production timelines for these complex AI chips can be unpredictable and irregular, successful launches yield massive royalty payouts once manufacturing ramps up to full speed.

## 4. Competitive Landscape and Moat Assessment

### 4.1 Who actually competes with Arteris

The competitive landscape for Arteris spans several distinct tiers, but the most significant threat comes from large tech companies and cloud providers attempting to poach Arteris’s own engineers to build systems internally. Major semiconductor giants like NVIDIA and Intel already design their own internal traffic controllers, and cloud giants will build custom systems whenever high production volume justifies the massive investment. Arteris wins business when this build versus buy calculation favors speed and safety over custom development. Creating an in-house traffic system requires years of work, tens of millions of dollars, and enormous technical risk, whereas buying Arteris’s pre-verified and safety-certified blueprints gets a chip team to market in just months.

The strongest proof of this business model is AMD’s decision to license Arteris software alongside its own proprietary Infinity Fabric technology. Even though AMD possesses one of the best internal networking technologies in the world, the company still buys from Arteris to speed up development and handle traffic across a wide range of modular mini-chips. AMD’s choice demonstrates that Arteris wins by making chip design faster, cheaper, and far less risky than doing everything in-house.

### 4.2 Moat Durability: Switching Costs and Certification

Once a chip maker chooses Arteris for a project, swapping it out later is extraordinarily difficult. Replacing it requires redesigning the entire data movement system from scratch and repeating costly safety certifications for automotive products. Because switching is such a massive headache, customer retention remains near ninety percent, and clients regularly expand their partnerships with Arteris across multiple generations of chip designs, as seen with major players like Renesas and NXP. This stickiness is backed by over seventy patents and two decades of field-tested chip blueprints. Early investment from industry heavyweights like Arm, Qualcomm, and Synopsys before Arteris went public further proves that the biggest semiconductor players recognized the strategic value of this technology long ago.

The main risk to Arteris’s business is its smaller size compared to giant chip software vendors like Synopsys and Cadence. These massive multi-billion-dollar platform providers could attempt to squeeze Arteris out by bundling good-enough networking blueprints into their software suites for practically free. To fight back, Arteris positions itself as a neutral player, working seamlessly with any processor type, manufacturing partner, or design software. Instead of trying to replace the major software platforms, Arteris designs its tools to run smoothly inside software programs made by Synopsys, Cadence, and Siemens. The central question for Arteris over the coming years is whether chip designers will prefer this complete neutrality and flexibility over the cheap software bundles offered by larger rivals?

## 5. Customer Wins and Ecosystem Validation (2024 to 2026)

Arteris’s growing list of customer deals provides the strongest real-world proof that its business strategy is working, with new contract wins picking up significant momentum throughout 2025 and 2026. Rather than relying on just one type of client, Arteris is winning business across the entire semiconductor landscape. Its recent deals include major cloud computing giants, top-tier processor makers, leading Japanese and Chinese automakers, a European chiplet consortium, and specialized artificial intelligence companies.

This diverse client base highlights the core strength of Arteris’s business model. By securing customers across so many different corners of the tech world, the company functions like a universal toll booth on chip complexity. Whenever a team needs to build a sophisticated microchip system, regardless of the industry or application, Arteris is positioned to collect a fee.

Up to this point, the core thesis is straightforward: interconnect technology is becoming to the chiplet era what mobile CPU architecture was to the smartphone revolution. Arteris stands alone as the only independent, battle-tested, and safety-certified provider positioned at the center of this transition.

The second half of this analysis focuses on valuation, execution, and potential risks. We evaluate the trajectory of future royalty revenues, break down our perspective on the $47.5 million in insider stock sales, and examine what expectations are already priced into the current stock valuation. Finally, we lay out detailed return scenarios through 2030, provide a comprehensive risk assessment, and map out the key timeline of upcoming catalysts.

SHARE TO GAIN ACCESS

Share
