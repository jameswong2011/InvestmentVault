---
title: "P = I²R: The One-Line Equation Shaping AI Infrastructure and Vicor's ($VICR) VPD"
source: "https://photoncap.net/p/p-ir-the-one-line-equation-shaping"
author:
  - "[[PhotonCap]]"
published: 2026-04-13
created: 2026-04-28
description: "Why the architecture that lost the H100 socket could win the CPO era"
tags:
  - "clippings"
---
**Note.** As mentioned in [an earlier X post](https://x.com/PhotonCap/status/2016273355759067267), I first came across $VICR in November 2025 thanks to [@butchertrader](https://x.com/butchertrader), studied and bought the stock, then sold my entire position in January 2026 after concluding I hadn't done enough homework. This piece is the study material I put together to get ready to buy it again.

![](https://substackcdn.com/image/fetch/$s_!pR47!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f3e92c8-5358-4ea5-a4c3-763e0446a0f0_869x834.png)

### Abstract

Next-generation AI accelerators demand roughly 1000A steady-state and 2000A peak current at a core voltage of about 0.7V. Because of P = I²R, tens of watts per module evaporate as heat while that current traverses the “last inch” of copper on the PCB. Vicor’s ($VICR) Factorized Power Architecture (FPA) and Vertical Power Delivery (VPD) attack this segment, cutting PDN (power delivery network) impedance by up to 50× versus conventional multiphase solutions. This piece starts from P = I²R and works through (1) a decomposition of PDN losses, (2) how FPA and the SAC topology work, (3) the transition from LPD to VPD and the GCM structure, (4) the design intent behind ChiP packaging, (5) the space and thermal constraints that co-packaged optics (CPO) bring, (6) the thermo-optic sensitivity of micro-ring resonators and why VPD pairs with it, and (7) a quantitative analysis centered on NVIDIA’s Quantum-X, with comparison points to Broadcom’s Tomahawk CPO line (Bailly, Davisson).

![](https://substackcdn.com/image/fetch/$s_!GtUp!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67a81532-bd7b-4bb6-8d94-acc60c2401bf_2752x1536.jpeg)

![](https://substackcdn.com/image/fetch/$s_!PnLT!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b19c851-3b88-4ba9-8802-fa69aa4ca27f_3455x2024.png)

---

### Contents

1. Intro: The weight of a one-line equation
2. The company called Vicor
	- 2.1 Founding and governance
		- 2.2 Business structure and financial snapshot
		- 2.3 Position in the competitive landscape
3. Problem definition: P = I²R and the last inch
	- 3.1 Delivering 0.7V × 2000A through the last inch
		- 3.2 Decomposing PDN impedance
		- 3.3 The limits of conventional solutions: multiphase buck and TLVR
4. Vicor’s answer: FPA, SAC, ChiP
	- 4.1 FPA: separating regulation from transformation
		- 4.2 SAC topology: why a sine amplitude converter
		- 4.3 From LPD to VPD: moving the conversion point under the processor *(paid)*
		- 4.4 GCM structure: gearbox and BGA pin mapping *(paid)*
		- 4.5 ChiP packaging: heat extraction and EMI shielding *(paid)*
5. Where CPO meets VPD
	- 5.1 CPO overview: the ASIC + PIC + ELS package *(paid)*
		- 5.2 The optical power budget: ELS, coupling loss, micro-ring modulator *(paid)*
		- 5.3 The thermal problem: 1°C produces an 80 pm shift *(paid)*
		- 5.4 Why CPO and VPD end up bound together *(paid)*
		- 5.5 Quantitative analysis: the NVIDIA Quantum-X case *(paid)*
6. Closing
7. References & Sources

---

## 1\. Intro: The weight of a one-line equation

V = IR. Ohm’s law, the one most of us learned back in school. Pair it with another basic equation, P = V × I (power equals voltage times current), and substitute IR for V. You get **P = I²R**. Power loss in a resistor scales with the square of the current. Double the current and the loss quadruples. Ten times the current, a hundred times the loss.

This one equation from physics class now defines the physical limits of AI infrastructure. The bottleneck is not only FLOPS. Compute performance and memory bandwidth are already well-known constraints, and **power delivery itself has joined them as a first-order limit**. The core of this new limit is the **last inch of copper** that has to carry over 1000A at 0.7V into the processor, and co-packaged optics (CPO) is turning that copper problem back into a game for power module companies.

Current-generation AI accelerators pack anywhere from 80 billion transistors (H100, on TSMC 4N) to 208 billion or more (Blackwell B200, on TSMC 4NP) into a single die. The core supply voltage (VDD) has dropped to around 0.7V.\[1\] Yet the same chip demands 1000A steady-state and 2000A peak current.\[1\] That translates to roughly 700W continuous and 1400W peak power events. The transient side is even harder. Under the load swings of neural network workloads, current slews at **2000A/μs**, and during those swings the supply voltage must stay within ±10% (about 0.07V) overshoot and undershoot to keep the transistors alive.\[1\]

This is where P = I²R goes to work, mercilessly. Even if the last segment of resistance between the PCB and the processor is only 70 microhms (µΩ), pushing 800A through it costs about 45W.\[2\] That loss is not from the compute, not from moving data to memory. It is just current passing through copper.

This article is about how that loss gets reduced. It takes a look at how Vicor’s ($VICR) Factorized Power Architecture and Vertical Power Delivery, developed over three decades, attack that one-line equation, and why the answer becomes decisive again in the CPO era.

![](https://substackcdn.com/image/fetch/$s_!Zpd0!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49714590-11a7-4894-94a1-5697251271db_2656x1600.jpeg)

\[Figure 1: Intuitive diagram of P = I²R, transmission line vs. PCB\]

---

## 2\. The company called Vicor

Before jumping into the technical analysis, a quick orientation on the company itself.

### 2.1 Founding and governance

Vicor Corporation was founded in 1981 in Andover, Massachusetts, by Dr. Patrizio Vinciarelli.\[3\] Vinciarelli earned his PhD in physics from the University of Rome, served as a fellow at CERN from 1973 to 1976 researching particle physics, and moved to the United States to hold fellow and instructor positions at the Institute for Advanced Study and Princeton University before founding Vicor in 1981. In interviews, he has described frustration with the limits of academia as what pushed him into power conversion as an industry. He personally holds more than 150 patents in power conversion and received the 2019 IEEE William E. Newell Power Electronics Award. The award citation reads “for visionary leadership in the development of high-efficiency, high-power-density power conversion components for distributed power system applications.”\[3\]

One governance detail worth flagging. Vicor has a dual-class structure with Common Stock and Class B Common Stock. Class B carries 10 votes per share versus 1 for Common, and is held almost entirely by Vinciarelli. Per the 2025 year-end 10-K, roughly 11.72 million Class B shares are outstanding.\[4\] Between his Common and Class B holdings, Vinciarelli controls roughly 47% of the economic interest and about 80% of the voting power.\[4\] In other words, the 44-year-old founder-CEO structure is not symbolic. It is rooted in voting control.

### 2.2 Business structure and financial snapshot

Vicor listed on NASDAQ in April 1990 (ticker VICR), and its headquarters along with all core manufacturing sits in Andover, Massachusetts. The company frames in-U.S., vertically integrated manufacturing as a core differentiator. A new ChiP fab in Andover went live in 2018, expanding capacity roughly 2.5×, and an additional fab (referred to as Fab 5) is in progress.

Revenue splits three ways. In fiscal year 2025, product revenue was $350.3M, up 12.1% year over year, with royalty revenue of $57.4M (+23.2%) and a $45M patent litigation settlement bringing total annual revenue to $452.7M.\[5\] Product revenue itself breaks into two segments: the Brick Products segment, with traditional brick form-factor DC-DC converters for industrial, aerospace/defense, and telecom infrastructure, and the Advanced Products segment, with ChiP-based modules including the VPD/LPD solutions that go into AI/HPC data centers. Royalty revenue comes from licensing Vicor’s patents to other power module manufacturers. That creates a structure where, as AI accelerator power modules sell, Vicor benefits both from its own product revenue and from royalties paid by competitors. Q4 2025 posted product revenue of $92.7M, gross margin of 55.4%, and net income of $46.5M ($1.01 EPS), with full-year net income of $118.6M ($2.61 EPS).\[5\]

Financial snapshot in numbers (**all as of the 2026-04-17 close**): share price $218.05, market cap roughly $9.89B, 52-week range from $38.93 to $224.76. Trailing P/E sits in the 83 to 85 area, TTM net margin 26.2%, gross margin 57.3%. Cash and cash equivalents were $402.8M as of Q4 2025, with a debt/equity ratio of 0.01, effectively net cash. Headcount is around 1,000. A P/E in the 80s is firmly in highly-priced territory, and the stock is up roughly 5.6× from $38.93 a year ago. One reading is that the market is pricing in the Gen 5 VPD ramp and a rise in licensing revenue ahead of time. P/S works out to roughly 22× revenue. Q1 2026 earnings are scheduled for 2026-04-21.\[6\] Price figures are volatile and should be read as a snapshot.

### 2.3 Position in the competitive landscape

On competition, the power module market splits into two camps. On one side are integrated semiconductor IDMs: Texas Instruments ($TXN, with roughly 12.5% of global PMIC revenue share), Analog Devices ($ADI), Infineon ($IFNNY), Renesas ($RNECY), STMicroelectronics ($STM), and NXP ($NXPI).\[7\] They carry broad catalogs and thick bases in automotive and industrial markets. On the other side are power-specialized players: Monolithic Power Systems ($MPWR), Power Integrations ($POWI), and Vicor itself. MPWR in particular is widely regarded as having captured the majority of AI accelerator power sockets.

Vicor’s position inside this landscape is distinctive. On absolute share of the AI accelerator power market, the market view is that MPWR has taken the larger socket.\[8\] MPWR locked in that position with the cost structure of multi-phase buck solutions and the simplicity of lateral integration. Vicor’s VPD is technically more sophisticated but has faced a longer adoption cycle and heavier reliance on a single lead customer. In return, Vicor carries in-U.S. vertically integrated manufacturing, a thick patent portfolio around FPA/SAC/ChiP (the foundation of the licensing revenue), and a technical edge in structurally high-current, high-voltage territory like 800V distribution, automotive Gen 5, and AI VPD. Brick products deliver long-tail revenue in industrial and aerospace/defense, while Advanced Products and royalties act as the growth driver tied to the AI infrastructure cycle. It is a dual structure.

> In summary, Vicor is an Andover, Massachusetts-based power module specialist founded in 1981 by founder-CEO Patrizio Vinciarelli. FY2025 revenue of $452.7M, net margin 26%, market cap in the $10B range makes it a mid-cap. A P/E in the 80s reflects the market pricing in the Gen 5 VPD ramp and licensing revenue up front. On absolute share of AI accelerator power, MPWR leads. But Vicor holds differentiated position through in-U.S. manufacturing, its patent portfolio, and structural strongholds in areas like 800V distribution. Now into the technical core.

---

## 3\. Problem definition: P = I²R and the last inch

### 3.1 Delivering 0.7V × 2000A through the last inch

Why do AI accelerators demand such a low voltage at such a high current? Two reasons.

**First, transistor scaling.** As process nodes move from 7nm to 5nm to 4nm to 3nm, transistor gate oxide thins out, and the upper limit of the supply voltage that can switch the transistor reliably comes down. At 4nm, core voltage sits around 0.7V.\[1\] There is not much room to push it lower. The noise margin and transistor reliability limits take over.

**Second, transistor count.** More transistors on the same die means more transistors switching simultaneously, and leakage current accumulates too. As noted earlier, current-generation AI accelerators integrate roughly 80 billion to 208 billion transistors in a 4nm-class process, and at that level chip-level current crosses 1000A easily.\[1\]

Since P = V × I and V cannot go lower, I has to rise to deliver the same P. The result is 1000A steady-state, 2000A peak.

An intuition check. Why do power transmission lines run at hundreds of thousands of volts? For the same power delivered, higher voltage means lower current, and lower current squared means exponentially lower P = I²R loss. From power plant to transmission tower, electricity flows at high voltage and low current, and only at the neighborhood level does the transformer step it down. Data centers follow the same principle, moving from 12V to 48V and now toward 800V DC distribution.\[1\]

The problem is the final step. Somewhere, 48V (or 800V) has to be stepped down to 0.7V, and **the farther that conversion point sits from the processor, the larger the P = I²R loss becomes.** The industry calls this final segment the “last inch.” For a standard 60×60mm AI processor package, even sitting a voltage regulator right at the package edge still leaves about 30mm of PCB path to the core.\[9\]

One more variable. Transients. The load swings from 0 to 2000A in under a microsecond, and if voltage deviates more than ±10% during that swing, the transistors take damage. That requires around 3mF of decoupling capacitance directly under the processor package.\[1\] Where those capacitors physically fit becomes another design conflict.

> The problem is this. AI accelerators demand low-voltage high-current (0.7V × 1000A+) and 2000A/μs transients simultaneously. Meeting that requires (1) moving the conversion point close to the processor, (2) placing decoupling capacitors directly beneath the processor, and (3) minimizing PDN impedance aggressively. Solving any one creates tension with the others.

### 3.2 Decomposing PDN impedance

The PDN (power delivery network) is the full path from the power source to the transistor. Its total impedance Z\_total is the sum of several components.

```markup
Z_total = Z_distribution + Z_regulator + Z_pcb + Z_package + Z_die
```

Breaking down the loss each component contributes shows where P = I²R hits hardest.

- **Z\_distribution**: data center power to rack. The 12V vs 48V choice is decisive. Delivering the same power at 12V means 4× the current and 16× the loss versus 48V.
- **Z\_regulator**: conversion loss in the voltage regulator itself. 95% efficiency means 5% loss.
- **Z\_pcb**: trace resistance on the PCB. Copper sheet resistance × length / width.
- **Z\_package**: BGA pins and redistribution layer inside the processor package substrate.
- **Z\_die**: metal layers and TSVs inside the die.

To revisit, from a PDN perspective, the example from Section 1. At 100°C, with a voltage regulator at the edge of a 60×60mm processor package pushing 800A through the PCB, assuming 70µΩ of trace resistance, the loss is 800² × 70 × 10⁻⁶ = about 45W.\[2\] That is loss from a single PCB segment alone. This is why Z\_pcb dominates total PDN loss.

If current rises to 1000A, the loss at the same resistance becomes 70W. At 1500A, 158W. **The current increase drives loss up as a square.** This is why, for multi-kilowatt AI accelerators, PDN design is essentially system efficiency itself.

Two ways to reduce Z\_pcb. **Make traces thicker, or make the distance shorter.** Thickening traces eats PCB area and cost and hits hard limits. That leaves the other option: shortening the distance, which means bringing the voltage regulator closer to the processor. Ideally, directly underneath. That direction converges on VPD (Vertical Power Delivery).

![](https://substackcdn.com/image/fetch/$s_!MIWP!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F553eb2c4-a03b-43bc-b09d-bfef8d10ebb7_2656x1600.jpeg)

\[Figure 2: PDN impedance decomposition\]

### 3.3 The limits of conventional solutions: multiphase buck and TLVR

The industry-standard solution is the multiphase buck regulator. It steps down 12V or 48V input to 0.7V by sharing the job across parallel inductors and switches. Each phase switches with an offset to reduce output ripple, and together they deliver large current.

A recent variant in GenAI accelerator modules is the TLVR (trans-inductor voltage regulator), a buck topology that magnetically couples the inductors to speed up transient response. In theory, it works.

The problem is scaling.

As current rises, more phases are needed. For 1000A, assuming 50A per phase, roughly 20 phases. Each phase requires a separate inductor, switch, control IC, and cooling path. Modular integration is low.\[9\]

That grows PCB area, and the larger area pushes the voltage regulator farther from the processor. More distance means higher Z\_pcb, which means higher P = I²R loss. The contradiction is that adding phases to handle more power ends up increasing the loss that drove the need.

Another limit. Multiphase PWM (pulse-width modulation) buck is fundamentally current averaging. It creates an average current by switching phases on and off with time offsets. That approach has a response-speed limit. To handle 2000A/μs transients, more decoupling capacitors are needed, and those capacitors again occupy space around the processor.\[1\]

All of these tensions point in one direction. **As long as the conversion point stays separated from the processor, the problem does not resolve.** This is where Vicor proposed a different answer.

> The important point here. Multiphase buck and TLVR scale current by adding phases, but adding phases consumes PCB space, and the space consumed pushes the conversion point farther from the processor, where P = I²R loss rises again. A self-contradiction.

---

## 4\. Vicor’s answer: FPA, SAC, ChiP

### 4.1 FPA: separating regulation from transformation

The core idea of Factorized Power Architecture boils down to one sentence. **Physically separate regulation (voltage control) from transformation (voltage conversion).**\[10\]\[11\]

A typical buck regulator handles both inside a single module. Neither function gets optimized. Regulation needs a precise feedback loop and fast response, which requires a stable location for the controller. Transformation handles large current and heat, and gets closer to the processor as PDN loss drops. The two requirements conflict inside one module.

FPA separates them and places each at its optimal location.

- **PRM (Pre-Regulator Module)**: regulates input voltage to a stable intermediate voltage (the “Factorized Bus”). Can sit anywhere on the motherboard. Optimized for response speed and accuracy.
- **VTM (Voltage Transformation Module) or GCM (Geared Current Multiplier)**: takes the Factorized Bus, steps voltage down by a factor of K, and multiplies current by K on the way into the processor. Sits directly next to or beneath the processor. Optimized for current density and PDN distance.

The K factor is the multiplication ratio of the current multiplier. For K = 1/48, an input of 48V becomes 1V output, and input current X becomes 48X on output. Impedance seen from the input side appears K² times smaller on the output side.\[10\]

One number that captures what this separation produces. Combined PRM and VTM system efficiency runs 90% to 95%, and a single VTM’s output impedance (R\_OUT) can reach as low as 0.8 milliohms (mΩ).\[11\] 0.8 milliohms is an order of magnitude below conventional multiphase impedance.

![](https://substackcdn.com/image/fetch/$s_!msTC!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80d26837-15e7-4de8-bccb-b90775004752_2656x1600.jpeg)

\[Figure 3: Multiphase buck vs FPA structure comparison\]

### 4.2 SAC topology: why a sine amplitude converter

If FPA is the architecture, SAC (Sine Amplitude Converter) is the circuit topology that actually implements it.\[10\]\[12\]

SAC boils down to two words. **Resonant + fixed-ratio.**

A standard PWM buck hard-switches the transistors. It turns them on and off while current and voltage are both large. That creates switching loss, and voltage spikes from interrupted inductor current produce significant EMI (electromagnetic interference).

SAC is different. It operates under **ZCS (Zero-Current Switching) + ZVS (Zero-Voltage Switching)** conditions.\[10\] An LC tank formed from a transformer and a resonant capacitor produces a sinusoidal current waveform at its natural resonant frequency, and the controller times the switching precisely at the waveform’s zero crossings. Switching happens at the moment current (or voltage) is zero, so switching loss is minimal. Efficiency reaches around 97%.\[11\]

The other feature is fixed-ratio. Unlike a typical regulator that adjusts output voltage variably, the K ratio (e.g., 1/48) is fixed. This sounds like a drawback but is actually a major advantage.

- **No control loop burden**: no fast feedback loop for output voltage regulation means response speed is set by the circuit’s resonant frequency itself.
- **Wide bandwidth**: on a VTM module, effective switching frequency is around 3.5 MHz, and output impedance stays flat out to about 1 MHz.\[10\] Load variations below 1 MHz get near-instant response.
- **Sub-microsecond load response**: 1μs or less to a load step.\[11\] This is the decisive reason why 2000A/μs transients can be handled.

And the sinusoidal waveform carries far less harmonic content than PWM’s square waves, so EMI emissions are fundamentally lower.\[10\] That’s a large signal-integrity advantage on high-density boards.

To put the whole flow together: PRM turns input voltage into a stable Factorized Bus (e.g., 48V regulated), and VTM or GCM steps that bus down by 1/K while multiplying current by K and feeding the processor. PRM can go anywhere on the PCB, while VTM/GCM sits next to or directly beneath the processor. Total system efficiency 90% to 95%, single-VTM output impedance around 0.8 mΩ.\[11\]

> The SAC dynamics in one line. SAC is a fixed-ratio resonant converter operating under ZCS/ZVS, achieving 97% efficiency, sub-microsecond response time, and output impedance as low as 0.8 mΩ. It produces a dynamic region hard-switching PWM buck cannot reach, and that behavior is the foundation that turns FPA into a real product.

That closes out the free section. We have walked through the 0.7V × 2000A problem, the PDN impedance decomposition, the limits of conventional solutions, and the different answer Vicor’s FPA + SAC provides. But the problem does not end here. Once optics starts sitting next to the ASIC, the lateral power delivery familiar from the H100 era physically loses its footing. The story of VPD almost landing in the H100 socket, then losing it to MPWR’s multiphase solution, is well known, but **the point is that the structure that lost on cost and manufacturing ease in H100 could actually be advantaged in CPO.**

But how much of “could be advantaged” is technical inference, and how much shows up in actual numbers? What happens when you decompose NVIDIA’s officially disclosed 9W per port and tens-of-megawatts data center savings through the lens of power delivery architecture? And where does something like Vicor’s GCM sit in that decomposition? We unpack each of these below.

### 4.3 From LPD to VPD: moving the conversion point under the processor (paid)

Within FPA, where the current multiplier (VTM or GCM) gets placed yields two options.

**LPD (Lateral Power Delivery)**: VTM modules flank the processor on its left and right (or top and bottom). Effective up to roughly 800A.\[11\] At an 800A 0.8V load with about 70µΩ PDN resistance, loss is around 45W.\[11\] Delivering current from both sides cuts loss 50% versus one-sided delivery.

**VPD (Vertical Power Delivery)**: The conversion part of the GCM (Geared Current Multiplier), meaning the VTM Array + Gearbox, sits directly beneath the processor on the opposite side of the PCB, while the PRM sits remotely elsewhere. VPD comes into its own above 1000A. From here on, “VPD” refers to this placement method as a whole, and “VPD module” or “GCM” refers specifically to the conversion part that sits directly beneath the processor.

Three quantitative advantages of VPD over LPD.

1. **Lower PDN impedance**: VPD reduces PDN impedance by roughly 20× versus a conventional lateral arrangement.\[1\] Combining FPA + VPD against a typical multiphase buck PCB solution, Vicor reports up to 50× PDN resistance reduction.\[9\] A 50× factor goes straight into P = I²R, meaning the same current produces 50× lower loss.
2. **Roughly 100W saved per module**: on a GenAI accelerator module, Vicor estimates that factorized VPD saves about 100W versus a TLVR-based lateral solution.\[1\] Across a 20,000-accelerator-module supercomputer, that is 2MW, or roughly 17.5 GWh annually at 24/7 operation, worth millions of dollars at industrial power rates.\[1\]
3. **Topside space freed**: moving the conversion module under the processor opens up 100% of the PCB area above the processor.\[13\] That space becomes available for high-speed I/O, memory routing, and, as we will see, optical I/O placement.

![](https://substackcdn.com/image/fetch/$s_!gskI!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41bc4702-8272-4858-8637-a8f6febb8c01_2656x1600.jpeg)

\[Figure 4: LPD vs VPD cross-section\]

### 4.4 GCM structure: gearbox and BGA pin mapping (paid)

VPD doesn’t end at “put the current multiplier under the processor.” In practice, it has to solve two additional problems simultaneously.

**Problem 1: Where decoupling capacitors go**

Directly under the processor is normally the space for high-frequency decoupling capacitors (>10MHz).\[14\] Roughly 3mF of decoupling capacitance needs to sit close to the processor package to absorb transient load swings. But VPD needs that same space. A conflict.

**Problem 2: Pin-map mapping**

A VTM module’s output pin pattern is determined by its internal circuit structure, while the processor’s power input pin pattern (BGA) is determined by the die’s power map. They usually don’t match. Connecting the two patterns directly causes asymmetry, with some pins carrying much more current than others, dropping efficiency.

GCM (Geared Current Multiplier) is the structure that solves both problems at once.\[14\] The vertical stack that sits directly beneath the processor is layered, top to bottom, as follows.

1. **Gearbox** (topmost, directly under the processor): performs two functions simultaneously
	- Remaps the current multiplier’s output pin pattern onto the processor’s power pin map (solves the pin-map mapping problem)
		- Integrates high-frequency decoupling capacitance inside the module itself (solves the decoupling-space problem)
2. **VTM Current Multiplier Array** (below the Gearbox): SAC-based fixed-ratio conversion, stepping the Factorized Bus down by 1/K and supplying K× current

And **the PRM Regulator is NOT part of this vertical stack. It sits remotely on another location on the board.** It takes the 48V input, creates the stable Factorized Bus, and feeds it to the VTM Array. The FPA principle of separating regulation from transformation shows up physically in the placement as well.

The name Gearbox is meaningful. Just as a car’s gearbox converts engine rotation into wheel rotation, the Gearbox converts the current multiplier’s output pattern into the processor’s power pattern.

The quantitative results this structure produces.\[15\]

- **Current density around 2 A/mm²**: a 1cm × 1cm GCM can deliver 200A
- **Output current 1000A+**: on a single module
- **Interconnect loss reduced by up to 90%**: with substrate-level integration (Vicor + Kyocera)\[13\]
- **VPD loss reduction of 95%**: versus TLVR lateral\[15\]

![](https://substackcdn.com/image/fetch/$s_!hDZk!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5c3df60-40e8-40fb-8d2f-03d9d57f0d08_2656x1600.jpeg)

\[Figure 5: GCM internal structure (PRM + VTM Array + Gearbox)\]

### 4.5 ChiP packaging: heat extraction and EMI shielding (paid)

No matter how good the circuit topology and module structure are, they mean little without a package that supports them. Vicor positions its ChiP™ (Converter housed in a Package) technology as the core differentiator in power modules.\[16\]\[17\]

ChiP’s design intent comes in three parts.

**1\. Panel-level manufacturing**: typical power modules are built by placing components one at a time into individual cavities. ChiP is different. Multiple modules are built simultaneously on a standard-sized panel and cut like wafers.\[17\] What enables this is that Vicor standardized its SAC-based fixed-ratio converters. Just by varying the K factor and voltage rating, different products get built on the same panel. The result is wafer-fab-like yield management and cost reduction.

**2\. Double-sided cooling**: the ChiP package places components on both sides of an internal mid-plane substrate.\[16\] That allows heat to exit both the top and bottom of the package. Typical power modules only cool from one side, so their thermal impedance runs roughly twice as high. ChiP cuts thermal impedance in half through double-sided cooling.

**3\. EMI shielding in SM-ChiP**: SM-ChiP™ (Surface-Mount ChiP) is the surface-mount version. Much of the package surface has grounded metal shielding plated onto it.\[15\]\[17\] That metal layer does two things. (1) adds a thermal path, (2) confines high-frequency parasitic current inside the module, preventing external emission. The latter is decisive for signal integrity on high-density boards. On top of the sinusoidal SAC waveform that fundamentally lowers EMI, the package itself acts as a Faraday cage.

**Stacked ChiP**: the decisive advance that made VPD possible is stacked ChiP, which stacks ChiP vertically.\[17\] The PRM layer, VTM array layer, and gearbox layer stack vertically into a single module. That multilayer structure makes integrated VPD solutions like GCM possible as actual products.

Power density improvements are quantitatively striking. Per Vicor, from the early brick form factor of the 1990s to stacked ChiP today, power density has reduced loss by roughly 25% every 2.5 years.\[15\] This is not marketing. For the same output, the module’s volume shrinks, which lets it move closer to the processor, which shortens PDN distance, which creates a virtuous cycle.

> One thing worth pinning down. ChiP packaging is the physical base that turns SAC topology and FPA architecture into an actual product. Panel-level manufacturing for wafer-level yield management, double-sided cooling for half the thermal impedance, metal shielding for EMI, stacked ChiP for the multilayer integration VPD needs. All four have to work at once for a module like GCM to matter.

That covers Vicor’s power architecture itself. Now we shift to optics. Why does CPO inevitably demand VPD?

---

## 5\. Where CPO meets VPD

### 5.1 CPO overview: the ASIC + PIC + ELS package (paid)

CPO (co-packaged optics) integrates optical transceivers inside the same package as the switch ASIC. Co-packaged, literally. The typical structure looks like this.\[18\]\[19\]

- **Compute ASIC** (switch or GPU): center of the package
- **Photonic Integrated Circuit (PIC)**: 4 to 8 chiplets around the ASIC
- **Electronic Integrated Circuit (EIC)**: contains TIA (transimpedance amplifier) and driver; either sits alongside the PIC or stacks on top
- **External Laser Source (ELS)**: outside the package, connected via optical fiber

Why keep ELS external matters. The laser is the least reliable component in the system. Low mean time between failures (MTBF) and weak at high temperature. Putting it next to the ASIC (1) transfers ASIC heat directly to the laser, shortening its life further, and (2) forces replacing the entire package when the laser fails. So the industry converged on separating ELS into an external module and connecting it through fiber.\[19\]\[20\]

Why build CPO at all. One line. **Pluggable optics has hit its limit.**

Traditional pluggable transceivers plug into the switch front panel. From the ASIC to the front panel, electrical signals traverse tens of centimeters of PCB. As 800G and 1.6T arrived, the SerDes (serializer/deserializer) in that path had to burn more and more power to preserve signal integrity. A single 1.6T pluggable module consumes roughly 30W, over half of which is in the DSP.\[20\]

CPO attaches the optical conversion almost right up against the ASIC. Electrical signal distance drops from tens of centimeters on the PCB to about 100µm inside the package.\[21\] Signal loss the SerDes has to handle drops from roughly 22 dB to about 4 dB on 200Gbps channels, and SerDes power drops with it.\[22\] DSPs can even be removed entirely. The net effect is per-port 1.6T consumption dropping from 30W to roughly 9W.\[22\] A 70% reduction.

This is the core motivation behind NVIDIA’s announcement of the Quantum-X and Spectrum-X CPO switches at GTC 2025.\[22\] In a million-GPU AI factory, network power is a significant share of total system power. At his GTC 2025 keynote, Jensen Huang noted that at data center scale, the CPO solution could save “tens of megawatts” of power.\[27\]

![](https://substackcdn.com/image/fetch/$s_!Kb2L!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8571dc0-1170-4246-ba27-d65ba167be12_2656x1600.jpeg)

\[Figure 6: CPO package internal structure\]

### 5.2 The optical power budget: ELS, coupling loss, micro-ring modulator (paid)

Where does power go in the CPO optical system? Let’s decompose.

**ELS (External Laser Source)**: the starting point for all optical power in the system. Laser wall-plug efficiency is typically 10% to 30%. That is, producing 1W of optical output consumes 3 to 10W of electrical input. ELS power efficiency therefore shapes system efficiency significantly.

In the NVIDIA Quantum-X case, the ELS design shows an interesting choice. The Quantum-X switch system Q3450 uses just 18 ELS modules to drive all 144 800G ports (576 transmit lanes at 200Gbps each).\[23\] Each ELS module contains 8 lasers and powers 32 transmit lanes. By NVIDIA’s own numbers, this structure cuts laser count roughly 4× versus pluggable.\[22\] Fewer lasers means lower total wall-plug loss, and higher reliability as well.

**Coupling loss**: coupling the laser output into fiber and the fiber into the PIC waveguide. Fiber-to-PIC coupling loss typically runs 1 to 3 dB.\[19\] 1 dB means about 20% of optical power is lost, 3 dB means 50%. Several approaches exist, including edge coupling, grating coupling, and V-groove, each with different trade-offs.

**Micro-ring modulator (MRM)**: NVIDIA’s Quantum-X uses MRM.\[21\] An MRM is a ring-shaped micro-resonator. Electrical signals shift the ring’s resonance wavelength to modulate light. Roughly 100× smaller than a Mach-Zehnder modulator (MZM), with better power efficiency (MRM at ~1-2 pJ/bit vs MZM at ~5-10 pJ/bit).\[21\] Processes only a single wavelength, which naturally pairs with WDM (wavelength division multiplexing). Broadcom’s current-generation Bailly (Tomahawk 5-based, 51.2T), by contrast, is reported to use MZM for its laser-stability and temperature-tolerance advantages.\[21\] Broadcom has not officially disclosed the modulator used in its next-generation Davisson (Tomahawk 6-based, 102.4T).

NVIDIA’s optical engine handles 1.6Tbps transmit + 1.6Tbps receive. Eight 200Gbps PAM4 lanes per direction, and **per engine**, 8 transmit fibers, 8 receive fibers, and 2 laser input fibers.\[23\]

**TIA + Driver**: the TIA converts photodetector-received optical signals to amplified electrical output, and the driver converts electrical signals into modulator drive voltage on the transmit side. Combined, they run in the single-watt range per optical-engine chiplet.

**Total energy per bit**: pluggable modules run roughly 15 to 20 pJ/bit, current CPO systems around 5 pJ/bit, with sub-1 pJ/bit as the target.\[18\]\[24\] NVIDIA’s official figures center on 1.6T port at 9W, and electrical loss dropping from about 22 dB to about 4 dB.\[22\] Some secondary sources interpret TSMC COUPE-based NVIDIA CPO at roughly 2 pJ/bit, but this is not a NVIDIA-disclosed number.\[21\]

One particular feature of optical systems to flag. All the loss items above are **losses in the optical path**, but compensating them requires **a stronger laser**. If coupling loss or modulator insertion loss rises 1 dB, maintaining the same SNR forces the ELS to produce about 26% (10^0.1 - 1) more optical power, which translates into ELS electrical consumption.

But you cannot just push laser power arbitrarily higher to compensate. Silicon waveguides in the 1550nm band exhibit two-photon absorption (TPA, where two photons are absorbed simultaneously) and free-carrier absorption (FCA) from the free carriers TPA generates. Above a certain laser power level, loss starts to grow nonlinearly. The practical side effects are three. First, absorbed light becomes heat, which raises waveguide temperature, which amplifies the 80 pm/°C ring resonance shift noted later, which drives up active-heater correction power. Second, Kerr nonlinearity causes self-phase modulation, broadening the signal spectrum and creating leakage into adjacent WDM channels, which degrades BER. Third, the laser itself, when its drive current rises, heats at the junction, which drifts its wavelength and shortens MTBF (mean time between failures). The ELS operating point is constrained to a narrow window where “output is enough but does not cross into the nonlinear regime.” Optics and electrical are not separate systems, and this is one reason the optical power budget stays tight.

### 5.3 The thermal problem: 1°C produces an 80 pm shift (paid)

The trickiest variable in a CPO system is thermal. The core of the problem is the thermo-optic sensitivity of the micro-ring modulator.

Silicon’s thermo-optic coefficient (TOC, how refractive index depends on temperature) at 1550nm is roughly **1.8 × 10⁻⁴/K** (per Komma et al. 2012).\[25\] What does this mean? Silicon waveguide refractive index rises by about 0.018% per 1°C. A small number on paper, but it directly drives the ring resonator’s resonant wavelength.

Silicon micro-ring resonator resonance wavelength shift is typically measured at around **80 pm/°C**.\[26\] A 1°C change shifts resonance by about 80 picometers.

Why is this a problem?

WDM systems commonly use 100 GHz or 200 GHz channel spacing. Near 1550nm, 100 GHz is about 0.8 nm = 800 pm, and 200 GHz is about 1.6 nm = 1600 pm. At 80 pm/°C, **a 10°C temperature change shifts the wavelength by nearly a full channel width at 100 GHz spacing, or about half a channel width at 200 GHz.** In practice, active heaters continuously correct the wavelength, so this shift does not immediately break the link. But once the variation exceeds the heater’s tuning range and the channel’s margin, the data link breaks, and even before that, adjacent-channel interference degrades BER rapidly. Either way, thermal variation is a first-order constraint in optical system design.

Two categories of solutions.

**1\. Athermal design**: make the cladding from a polymer (such as SU-8) with a TOC of opposite sign to silicon, so net TOC approaches zero.\[26\] Downside: polymer is poorly compatible with CMOS fabrication, and optical loss can rise.

**2\. Active control**: place a micro-heater next to the ring, measure ring temperature in real time, and correct the wavelength. Currently closer to the industry standard. Downside: the heater itself consumes power.

NVIDIA’s Quantum-X, MRM-based, adopts active control. It applies liquid cooling to both ASIC and optical engines to minimize thermal variation, and adds active wavelength tuning on top.\[23\]

Here is where Vicor’s VPD contributes directly to the overall efficiency of the optical system.

**Scenario A: Lateral power delivery + CPO**

Voltage regulators sitting on the top side of the PCB, flanking the ASIC, conduct their heat through the PCB plane directly into adjacent photonic chiplets. When photonic chiplet temperature rises by 5 to 10°C, ring resonance shifts by 400 to 800 pm, and active heaters have to burn more power to correct. Lateral placement also conflicts with the space the photonic chiplets need to occupy in the first place.

**Scenario B: VPD + CPO**

With the voltage regulator (GCM) on the opposite side of the PCB, directly under the ASIC, its heat dissipates through a separate heat sink on the package’s bottom side rather than going through the ASIC. The photonic chiplets on top of the ASIC only have to manage their own thermal. ASIC and photonic chiplet thermal paths are decoupled. Thermal variation that active heaters must compensate drops, and so does heater power.

![](https://substackcdn.com/image/fetch/$s_!DyeY!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e89d78c-1b06-4da1-ad68-b531ef5151d8_2922x1760.png)

\[Figure 7: Ring resonator thermal sensitivity\]

### 5.4 Why CPO and VPD end up bound together (paid)

Putting the analysis so far together, VPD’s advantages over lateral solutions in the CPO era come down to three.

But why wouldn’t the judgment from the H100 era repeat inside the same NVIDIA ecosystem? In the H100 socket, MPWR’s multiphase buck won on simplicity of lateral integration, shorter adoption cycle, and volume cost structure. Vicor’s VPD was technically more refined, but reliance on a single lead customer and slow adoption cadence worked against taking the socket. In the CPO structure, the judgment criteria themselves shift. With the ASIC topside occupied by optical I/O, there is less room for lateral multiphase that grows by adding phases, and the thermal sensitivity of photonic chiplets barely tolerates the heat of a voltage regulator sitting right next to the ASIC. The environment that favored lateral multiphase under “cost and manufacturing ease” in H100 can tilt the opposite way in CPO under “space and thermal.” This is the structural reason the VPD story is getting louder now.

**1\. Topside space**

A CPO package’s topside is claimed by optical I/O. For a 28.8Tbps Quantum-X ASIC, 18 optical engines need to sit on the package topside around the ASIC, and over 1,000 optical fibers exit the package edge across 144 ports.\[23\] Most of the topside space a lateral voltage regulator would need is gone. Based on the publicly known CPO structure, **VPD is the architecture that fits this constraint most naturally**.

**2\. Current density under space constraints**

Quantum-X ASIC’s own power is not publicly disclosed by NVIDIA. Given TSMC 4nm, 28.8Tbps full-duplex bandwidth, and optical engine integration, it very likely runs well above kW-class, but this is the author’s estimate, not NVIDIA’s official number. Whatever level it is, the core-voltage-at-0.7-to-0.8V with kilo-amp-range current is clear. Delivering that current in a constrained package area requires current density of 2 A/mm² or more, a regime conventional multiphase struggles to reach.\[15\] Vicor’s GCM is already there.

**3\. Thermal isolation**

As shown earlier, the thermo-optic sensitivity of photonic chiplets demands minimizing ASIC heat conduction into the photonic region. VPD, by placing the voltage regulator on the opposite side of the PCB, routes the voltage regulator’s heat through a separate cooling path rather than through the ASIC. Some degree of thermal isolation between ASIC and photonic chiplets becomes achievable.

**Substrate-level integration prospect**

Vicor and Kyocera’s Power-on-Package collaboration goes a step further.\[13\] Integrating the current multiplier into the substrate itself. If this materializes, the power converter sits inside the same substrate as the ASIC rather than on the opposite side of the PCB. PDN distance drops to microns, and in theory, optical chiplets, electrical ASIC, and power converter can be co-designed inside a single substrate. A truly fully co-packaged system.

One thing to pin down. NVIDIA has not publicly disclosed the Quantum-X power supply vendor from GTC 2025. Whether Vicor is in this platform is not publicly verified. This article argues that “VPD fits CPO well” technically, not that “Vicor is in Quantum-X.” That distinction matters.

> At this point, the power story and the optics story overlap. The CPO package structure (1) claims the topside for optical I/O, (2) pushes ASIC current requirements into the kW class, and (3) demands protecting the thermal sensitivity of photonic chiplets. That set of problems is hard to solve with lateral power delivery. VPD is one of the architectures that fits this constraint most naturally.

### 5.5 Quantitative analysis: the NVIDIA Quantum-X case (paid)

A final quantitative exercise on a specific system. First, separate officially disclosed figures from author estimates.

**\[Official disclosed figures\]**

The NVIDIA Quantum-X800 Q3450 system has 4 Quantum-X800 ASICs, each handling 28.8 Tbps full-duplex bandwidth.\[23\] Total system is 144 ports × 800 Gbps = 115.2 Tbps, liquid-cooled, with 18 optical engines (1.6 Tbps × 18) per ASIC. Total ELS modules in Q3450: 18. Commercial launch: early 2026.\[22\] Spectrum-X Photonics is scheduled for 2H 2026.\[22\] On power, NVIDIA’s disclosed numbers are clear. **1.6T pluggable module about 30W, CPO port about 9W, per-port savings about 21W.**\[22\] Electrical loss drops from roughly 22 dB to about 4 dB.\[22\] At his GTC 2025 keynote, Jensen Huang noted that at data center scale, CPO could save “tens of megawatts” of power.\[27\]

A simple multiplier for the Q3450 system: 144 ports × 21W = **about 3 kW of optical interconnect power savings**. All of this comes directly from NVIDIA’s official figures.

**\[Author estimates\]**

From here on, not official figures but author modeling. NVIDIA does not disclose the Quantum-X ASIC’s own TDP, and the author does not pretend to know it. Given optical engine integration and 28.8Tbps bandwidth, per-ASIC power likely sits in the kW range, with system-level ASIC power in the multi-kW range.

Additional savings from adopting VPD split three ways. First, PDN loss itself. Vicor’s reported “50× PDN resistance reduction vs multiphase” or “95% loss reduction vs lateral” are PDN-limited numbers; translated into system efficiency versus a lateral solution, a few-percentage-point differential is more realistic. Across 4 ASICs, that suggests hundreds of watts of additional per-system savings. Second, thermal compensation power. Active wavelength tuning heater power drops at photonic chiplets, a few-watt-per-engine differential at most; across 18 × 4 = 72 engines, that is roughly tens of watts per system. Third, indirect reliability and lifetime effects, harder to quantify.

**\[Aggregation and data center scaling\]**

Here is the picture as the author sees it. For a single Q3450 system, CPO adoption saves about 3 kW (official), and VPD may add a few hundred watts more (estimated). At the single-system level, not a large number. But the AI factory NVIDIA is designing toward scales to thousands of switch systems. For 1,000 systems, CPO alone is 3 MW, or roughly 26 GWh annually at 24/7 operation. At industrial power rates in the U.S., that is millions of dollars annually. VPD’s additional effect stacks on top at the incremental tens-of-megawatts scale.

NVIDIA has not broken down what portion of its tens-of-megawatts data center savings estimate comes from CPO versus from power delivery architecture. But the direction is clear. CPO resolves the large chunk of power savings, and power delivery architecture makes additional room on top of that.

![](https://substackcdn.com/image/fetch/$s_!frHJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e579613-f0fe-4e87-b385-095fa1b8b6ea_2922x1760.png)

\[Figure 8: System power comparison (Pluggable vs CPO + VPD)\]

---

## 6\. Closing

We have seen how a one-line equation, P = I²R, governs the entire system design of AI infrastructure. Transistors cannot go below 0.7V, so current keeps rising, and rising current drives P = I²R loss up as a square. The answer is to reduce R, and reducing R requires moving the conversion point closer to the processor. Vicor’s FPA separated regulation from transformation and let the conversion module sit next to or under the processor. SAC topology made that conversion happen under ZCS/ZVS at 97% efficiency. ChiP packaging became the base that takes all of this and manufactures it at wafer-level yields.

CPO extends the same problem structure into optics. Placing photonic chiplets next to the ASIC, it cuts the electrical signal distance from centimeters to microns, and SerDes power falls accordingly. But that structure claims the space voltage regulators used to occupy, and the thermo-optic sensitivity of photonic chiplets (80 pm/°C) demands isolating ASIC heat too. Those two constraints push power delivery from lateral to vertical.

CPO looks like an optics story, but it is really the force that rewrites the power delivery story. The next generation of AI data centers is converging on a direction where power and photonics get co-designed inside the same package.

---

## 7\. References & Sources

\[1\] [Tackling Power Challenges of GenAI Data Centers](https://www.vicorpower.com/resource-library/articles/high-performance-computing/tackling-power-challenges-of-genai-data-centers): Vicor / Electronic Design interview (Maury Wood). 0.7V VDD, 1000A steady-state, 2000A peak, 700W TDP, 2000A/μs transients, ±10% overshoot, 3mF decoupling capacitance, TLVR limits, 100W per module savings, 12V→48V→800V distribution.

\[2\] [Vertical Power Delivery Enables Cutting-Edge Processing](https://www.vicorpower.com/resource-library/articles/high-performance-computing/vertical-power-delivery-enables-cutting-edge-processing): Vicor technical article (Ajith Jain). 800A / 70µΩ / 45W loss example, FPA separation principle, core voltage 0.75 to 0.85V range.

\[3\] [Vicor Corporate Governance, Patrizio Vinciarelli bio](https://www.vicorpower.com/about-the-company/corporate-governance): Vicor official site. CEO biography (founded 1981, University of Rome PhD physics, CERN 1973-1976 fellow, Princeton IAS 1977-1980), 150+ power conversion patents, 2019 IEEE William E. Newell Power Electronics Award.

\[4\] [Vicor Corporation Form 10-K, FY2025](https://www.sec.gov/Archives/edgar/data/0000751978/000119312526085102/vicr-20251231.htm): SEC filing. Dual-class structure (Common + Class B, Class B = 10 votes/share), 2025-12-31 Class B shares outstanding 11,726,718, Common 45,910,601, Vinciarelli’s capital/voting power disclosures.

\[5\] [Vicor Q4 and Full Year 2025 Results (official IR)](https://vicorcorporation.gcs-web.com/news-releases/news-release-details/vicor-corporation-reports-results-fourth-quarter-and-year-8): Vicor official press release. FY2025 product revenue $350.3M, royalty $57.4M, Q4 product revenue $92.7M (+15.3% YoY), Q4 net income $46.5M ($1.01 EPS), Q4 gross margin 55.4%, FY2025 net income $118.6M, backlog $176.9M, cash $402.8M.

\[6\] [Vicor Investor Overview](https://vicorcorporation.gcs-web.com/): Vicor official IR page. Q1 2026 earnings conference call scheduled 2026-04-21.

\[7\] [PMIC Market Share Report 2025](https://dataintelo.com/report/power-management-integrated-circuit-pmic-market): Dataintelo industry report. Texas Instruments global PMIC revenue share ~12.5%, 5,000+ product catalog, Vicor / MPWR / Renesas as main competitors in AI accelerator power.

\[8\] [Monolithic Power Systems competitive analysis](https://markets.financialcontent.com/stocks/article/finterra-2026-4-9-the-power-behind-the-brain-a-deep-dive-into-monolithic-power-systems-mpwr-in-the-ai-era): FinancialContent analysis. MPWR share in AI accelerator power estimated 15-20%, MPWR secured most GPU sockets via lateral integration cost structure, Vicor VPD technical edge + slow adoption cycle assessment.

\[9\] [Powering High-Performance Computing](https://www.vicorpower.com/resource-library/articles/high-performance-computing/powering-high-performance-computing): Vicor technical article (Paul Yeaman). 60×60mm processor package “last inch” definition, multiphase VR phase-addition limits, VPD 95% loss reduction.

\[10\] [Factorized Power Architecture and VI Chips (FPA101)](https://www.vicorpower.com/documents/whitepapers/fpa101.pdf): Vicor white paper. SAC ZCS/ZVS operation, VTM output impedance 0.8 mΩ, K factor definition, capacitance multiplication, 3.5 MHz effective switching frequency.

\[11\] [Factorized Power Architecture: Achieving high density and efficiency](https://www.vicorpower.com/documents/whitepapers/wp-FPA-Achieving-high-density-efficiency-VICOR.pdf): Vicor white paper (Tom Curatolo). PRM + VTM 90-95% system efficiency, 1:48 current gain, 1μs response time, 97% efficiency.

\[12\] [Powering Clustered AI Processors](https://www.vicorpower.com/resource-library/articles/high-performance-computing/powering-clustered-ai-processors): Vicor technical article. LPD vs VPD quantitative comparison, 50% loss reduction with dual-sided placement.

\[13\] [Kyocera and Vicor to collaborate on next-generation Power-on-Package solutions](https://www.vicorpower.com/press-room/kyocera-and-vicor-collaborate): Vicor press release. Substrate-level Power-on-Package integration, 90% interconnect loss reduction, 100% perimeter freed by VPD.

\[14\] [Power-on-Package vertical and lateral power delivery](https://www.vicorpower.com/industries-and-innovations/power-on-package): Vicor industries page. GCM gearbox structure, decoupling integration, BGA pin-map mapping, 1000A output.

\[15\] [Vicor 1200A ChiP-set enables higher performance AI accelerator cards](https://www.vicorpower.com/press-room/2016-2021/hydra-ii): Vicor press release. Current density 2 A/mm², GCM definition, VPD loss reduction, 25%/2.5 year power loss reduction trend.

\[16\] [Innovating Power Module Packaging](https://www.vicorpower.com/resource-library/articles/innovating-power-module-packaging): Vicor technical article. Stacked ChiP, panel fabrication, current density, VPD multilayer structure (current multiplier + gearbox), SM-ChiP plated metal shielding.

\[17\] [Attributes of high-performance power module packaging](https://www.vicorpower.com/documents/whitepapers/wp-Attributes-of-High-Performance-Power-Module-Packaging-VICOR.pdf): Vicor white paper. ChiP panel-level manufacturing, double-sided cooling, mid-plane substrate, multiple-reflow soldering, four pillars of innovation.

\[18\] [Co-Packaged Optics Reaches Power Efficiency Tipping Point](https://semiengineering.com/co-packaged-optics-reaches-power-efficiency-tipping-point/): Semiconductor Engineering. CPO structure (ASIC + 4-8 PIC + ELS), 15→5 pJ/bit, fiber-to-PIC alignment, electrical signal distance 100µm vs 30cm, MRM vs MZM.

\[19\] [Co-packaged optics (CPO): status, challenges, and solutions](https://pmc.ncbi.nlm.nih.gov/articles/PMC10027985/): Frontiers of Optoelectronics review (He et al.). Reasons for external ELS, 2.5D vs 3D integration, optical power delivery analysis, fiber-to-PIC coupling loss.

\[20\] [Co-packaged datacenter optics: Opportunities and challenges](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/ote2.12020): IET Optoelectronics (Minkenberg et al.). Gen 1 CPO 10-15 pJ/bit target, sub-10 pJ/bit next-gen feasible, laser power ≤20 dBm recommended, 1.6T pluggable 30W analysis.

\[21\] [Co-Packaged Optics, a deep dive](https://blog.apnic.net/2025/05/07/co-packaged-optics-a-deep-dive/): APNIC blog. NVIDIA Quantum-X / Spectrum-X analysis, COUPE EIC stacked on PIC, 4× laser reduction via ELS, beachfront density, MRM vs MZM, Broadcom Bailly comparison.

\[22\] [Scaling AI Factories with Co-Packaged Optics](https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/): NVIDIA Developer Blog. CPO 1.6T port 9W measurement, 3.5× power efficiency, 10× resiliency, electrical loss 22 dB → 4 dB, GTC 2025 announcement.

\[23\] [How Industry Collaboration Fosters NVIDIA Co-Packaged Optics](https://developer.nvidia.com/blog/how-industry-collaboration-fosters-nvidia-co-packaged-optics/): NVIDIA Developer Blog. Quantum-X 28.8Tbps/ASIC specs, 6 OSA/ASIC, 3 COUPE engines/OSA, 8 × 200Gbps PAM4 lanes/engine, 8 lasers/ELS module, Q3450 144 ports / 800Gbps, liquid cooling.

\[24\] [What is Co-packaged Optics?](https://www.ansys.com/blog/what-is-co-packaged-optics): Ansys blog. Pluggable vs CPO comparison, sub-1 pJ/bit target, signal integrity, 1 Tbps/mm beachfront density.

\[25\] [Thermo-optic coefficient of silicon at 1550 nm and cryogenic temperatures](https://pubs.aip.org/aip/apl/article/101/4/041905/111710/Thermo-optic-coefficient-of-silicon-at-1550-nm-and): Appl. Phys. Lett. 101, 041905 (2012) (Komma et al.). Silicon thermo-optic coefficient measurement from 5 K to 300 K, dn/dT ≈ 1.8 × 10⁻⁴/K reconfirmed at 300 K. Extends Cocorullo & Rendina (1992)’s silicon etalon method to cryogenic temperatures.

\[26\] [Resolving the thermal challenges for silicon microring resonator devices](https://www.degruyterbrill.com/document/doi/10.1515/nanoph-2013-0013/html?lang=en): Nanophotonics review (Padmaraju et al.). Athermal vs control-based solutions comparison, micro-heater + photodetector structure, laser wavelength locking necessity, ring modulator WDM applications, typical silicon ring shift ~80 pm/°C.

\[27\] [Nvidia reveals plan to scale AI ‘factories’ with co-packaged optics](https://optics.org/news/16/3/26): optics.org coverage (2025-03). Coverage of Jensen Huang’s GTC 2025 keynote. “Tens of megawatts” data center savings mentioned, Lumentum lasers, Coherent silicon photonics collaboration, 2H 2025 Quantum-X and 2H 2026 Spectrum-X launch plans.

## READ MORE:[NuttyCLD](https://nuttycld.substack.com/p/the-ai-power-crisis-part-3?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

[

In Part 1, we stayed at the grid level. Roughly 135 years after the original AC-DC rivalry, DC began to challenge AC again, and the reason was the evolution of power semiconductors. In Part 2, that voltage moved inside the data center and climbed to 800V at the rack. The 48V standard, which had held for more than a decade, began to run into the current …

](https://nuttycld.substack.com/p/the-ai-power-crisis-part-3?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

---

Disclaimer: This article is an independent, engineering-driven technical analysis published by *PhotonCap*. All content is based on publicly available information and is intended for educational and informational purposes only. Nothing herein constitutes a recommendation to buy, sell, or hold any security. The author may hold positions in securities discussed and may transact at any time without notice. Readers should conduct their own due diligence before making any investment decisions.