---
date: 2025-11-26
tags: [research, semiconductors, photonics, CPO, silicon-photonics, gemini-canvas]
status: active
sector: Semiconductors & Photonics
source: Gemini Canvas export
propagated_to: [LITE, IQE]
---

# Silicon Photonics Supply Chain: The Investment Architecture for the Post-Copper Era

## 1. Executive Strategic Overview: The Inevitability of Light

The global digital infrastructure is currently colliding with a fundamental limit of physics known in the semiconductor industry as the "Copper Wall." For decades, the movement of data between processors, memory, and switches has relied on the flow of electrons through copper traces and cables. As the industry advances into the era of Artificial Intelligence (AI) and hyperscale computing, demanding data transfer rates of 800 Gigabits per second (Gbps), 1.6 Terabits (Tbps), and beyond, copper interconnects are becoming physically untenable. They are too slow, too hot, and too limited in reach to support the "Million-GPU" clusters required to train next-generation Large Language Models (LLMs).

This physical bottleneck has catalyzed a structural shift toward Silicon Photonics (SiPh)—a technology that manufactures optical devices using standard silicon semiconductor processes. This transition is not merely a component upgrade; it is a wholesale architectural reimagining of the data center, moving the optical interface from the rack faceplate directly into the processor package. This report provides an exhaustive investment analysis of the silicon photonics supply chain, identifying the constituents positioned to capture value in this multi-year secular trend.

The investment thesis is grounded in three critical pillars:
1.  **The AI Scaling Imperative:** AI model complexity is growing 32-fold every three years.[1] To support this, interconnect bandwidth must scale exponentially. Optical interconnects are the only viable path to achieving the required bandwidth density and energy efficiency (picojoules per bit) for future AI clusters.
2.  **The Rise of Co-Packaged Optics (CPO):** The industry is migrating from pluggable transceivers to Co-Packaged Optics, where the optical engine is integrated with the host ASIC. This shift redistributes the profit pool from traditional module makers to semiconductor foundries, advanced packaging providers, and switch silicon vendors.[2, 3]
3.  **Sovereign Supply Chain Reconstruction:** Geopolitical friction is driving a bifurcation of the supply chain, creating distinct investment opportunities in Western-aligned manufacturing (e.g., GlobalFoundries, Fabrinet, Amkor) versus the dominant incumbent Chinese module ecosystem (InnoLight, Eoptolink).[4, 5]

Current market forecasts project the silicon photonics market to grow from approximately $3.11 billion in 2025 to over $10 billion by 2030, with some aggressive estimates reaching nearly $29 billion by 2034.[4, 6, 7] This growth trajectory signifies an inflection point where photonics moves from a niche technology to a ubiquitous utility in the compute fabric.

---

## 2. The Physics and Economics of the Interconnect Transition

To accurately assess the investment potential of specific companies, one must first understand the technical friction driving the market. The incumbent technology—copper—is failing due to signal attenuation and power consumption.

### 2.1 The Copper Wall and Signal Integrity
In traditional data center architectures, electrical signals travel from a switch ASIC, through a PCB, to a connector, and then across a copper cable. At lower speeds (10G, 25G), copper is highly conductive and efficient. However, at the high frequencies required for 112G and 224G SerDes (Serializer/Deserializer) lanes, the "skin effect" and dielectric loss cause the signal to degrade rapidly.

At 224Gbps, a copper signal can barely travel a few inches on a standard PCB before becoming indistinguishable from noise. To counteract this, chip designers must employ increasingly complex Digital Signal Processors (DSPs) to re-time and equalize the signal. These DSPs are power-hungry. In a traditional transceiver-based switch, the power consumed just to move data to the edge of the box is approaching 30-40% of the total system power.[8] This is energy not used for compute, but wasted on transport.

### 2.2 The Energy Equation: Picojoules per Bit (pJ/bit)
The core metric for AI infrastructure is energy efficiency, measured in picojoules per bit (pJ/bit).
*   **Electrical Interconnects:** Typically consume 10-20 pJ/bit for board-level reach.
*   **Pluggable Optics:** Reduce this for longer reaches but still require power-intensive DSPs at the edge.
*   **Silicon Photonics (CPO/Optical I/O):** Targets <5 pJ/bit by eliminating the long electrical trace and the need for heavy signal conditioning.[9]

For an AI cluster with thousands of XPUs (accelerators), this efficiency delta translates to megawatts of power. Nvidia's CEO Jensen Huang noted that if the NVL72 rack system had used traditional optics instead of copper for its specific short-reach backplane, it would have required an additional 20 kilowatts of power—illustrating the complex trade-offs currently being managed. However, as scaling goes beyond the rack, optics become mandatory. Ayar Labs and other disruptors contend that integrated optical I/O is the only way to break the power-bandwidth bottleneck permanently.[1]

### 2.3 The Latency Imperative
AI training is a synchronous workload. Thousands of GPUs must update their weights simultaneously. If one link is slow, the entire cluster waits. Traditional transceivers introduce latency via the DSP and the physical distance. Silicon photonics, specifically architectures that remove the DSP (like Linear Drive Optics) or integrate it (CPO), drastically reduce latency. Integrated silicon photonics can achieve latencies of less than 100ns, a critical threshold for maintaining high utilization in AI clusters.[9]

---

## 3. Market Dynamics and Quantitative Forecasts

The silicon photonics market is entering a phase of hyper-growth, but the landscape is nuanced by varying adoption rates of different technologies.

### 3.1 Market Sizing and CAGR
Analyst consensus points to a market growing at roughly 25-30% annually.
*   **MarketsandMarkets** projects a jump from $2.65 billion in 2025 to $9.65 billion by 2030 (CAGR ~30%).[6]
*   **Precedence Research** is more bullish, forecasting $28.75 billion by 2034, driven by the ubiquity of optical I/O in consumer devices beyond the data center.[7]
*   **Mordor Intelligence** estimates the 2025 market at $3.11 billion, growing to $10.36 billion by 2030.[4]

These figures suggest that while the base is currently modest compared to the broader semiconductor industry, the velocity of capital allocation is accelerating.

### 3.2 Segmentation by Data Rate
The investment cycle is defined by transceiver speeds:
*   **400G:** The current volume workhorse. Commodity status is approaching, leading to margin compression for suppliers.
*   **800G:** The current high-growth segment. Ramping heavily in 2024-2025, driven by Nvidia's H100/H200 deployments. Suppliers like InnoLight and Eoptolink dominate here.[10]
*   **1.6T:** The next frontier. Expected to see initial volumes in late 2025/2026. This generation acts as the bridge to CPO.
*   **3.2T and Beyond:** The CPO era. Traditional pluggables become physically too large and power-inefficient for the faceplate density required.

### 3.3 Geographic Drivers
*   **North America:** Leads in demand (Hyperscalers: Google, Amazon, Microsoft, Meta) and design innovation (Nvidia, Broadcom, Marvell). Accounts for ~38% of the market.[4]
*   **Asia Pacific:** Leads in manufacturing and module assembly. China is aggressively investing in domestic silicon photonics to reduce reliance on Western DSPs and lasers.[11]

---

## 4. Technological Architectures: The Battle for the Socket

The silicon photonics market is not a monolith; it is a battleground between competing architectures. Understanding these is crucial for stock selection.

### 4.1 Pluggable Optics (The Incumbent)
This is the current standard. A module plugs into the switch faceplate.
*   **Pros:** Flexibility, serviceability (if a module breaks, you replace it), established ecosystem.
*   **Cons:** Power inefficient, faceplate density limits.
*   **Investment Implications:** Beneficiaries are **InnoLight**, **Coherent**, **Lumentum**, **Fabrinet**. This segment remains robust through the 800G and early 1.6T cycle but faces long-term existential risk from CPO.

### 4.2 Linear Pluggable Optics (LPO)
A halfway house between standard pluggables and CPO. LPO removes the DSP from the optical module, relying on the switch ASIC's SerDes to drive the optics directly.
*   **Pros:** Lower power, lower latency, lower cost (no DSP in module).
*   **Cons:** Requires very high-quality electrical channels; interoperability challenges.
*   **Investment Implications:** **Macom** and **Credo** are key players here, alongside module makers adapting to LPO designs. It extends the life of the pluggable form factor.[12]

### 4.3 Co-Packaged Optics (CPO)
The optical engine moves inside the package, sitting next to the switch ASIC.
*   **Pros:** Maximum energy efficiency, highest bandwidth density.
*   **Cons:** Thermal management (lasers hate heat), serviceability (if optics fail, the whole switch might need replacement), ecosystem immaturity.
*   **Investment Implications:** **Broadcom** and **Marvell** are the drivers. **TSMC** and **Advanced Packaging** firms (Amkor, Besi) are the enablers. This is the highest-value long-term bet.[2, 13]

### 4.4 Optical I/O and Wafer-Scale Integration
The most disruptive architecture. Optics are not just for switching but for processor-to-memory communication.
*   **Concept:** Companies like **Lightmatter** and **Ayar Labs** utilize interposers to connect XPUs optically.
*   **Investment Implications:** This threatens standard SerDes providers and creates a new class of "optical compute" companies. Lightmatter’s recent $4.4B valuation underscores the market's belief in this architecture.[14]

---

## 5. Supply Chain Vertical: The Architects (Switch Silicon & DSP)

The "brains" of the operation. These companies define the specifications and control the high-margin silicon at the heart of the network.

### 5.1 Broadcom Inc. (NASDAQ: AVGO)
Broadcom is the undisputed heavyweight champion of networking silicon. Their "Tomahawk" line of switch ASICs is the industry standard for hyperscalers.
*   **CPO Leadership:** Broadcom is aggressively driving CPO to defend its switch dominance. Their "Bailly" CPO switch (51.2T) integrates their silicon photonics engines directly. By controlling the switch, the DSP, and the optics, Broadcom captures the entire value chain.
*   **Technical Execution:** Broadcom has demonstrated 512-lane CPO systems with high reliability, releasing shock/vibe and thermal cycling data to assuage hyperscaler fears.[15]
*   **Strategic Positioning:** Broadcom effectively acts as the "arms dealer" for AI. Whether the market uses pluggables or CPO, Broadcom wins via its switch silicon. However, CPO allows them to capture the ~$5000+ of optical content per switch that previously went to transceiver vendors.

### 5.2 Marvell Technology (NASDAQ: MRVL)
Marvell acts as the primary counterweight to Broadcom, offering a merchant alternative with a focus on DSP excellence.
*   **Inphi Legacy:** The acquisition of Inphi gave Marvell best-in-class DSP technology (PAM4). Their "Nova" DSPs are critical for 1.6T optical modules.[16]
*   **Platform Strategy:** Marvell’s "Teralynx" switch combined with "Perseus" optical engines offers a full stack. Unlike Broadcom's more closed integrated approach, Marvell emphasizes interoperability and open standards, appealing to hyperscalers who want to avoid vendor lock-in.[17, 18]
*   **AI Scale-Up:** Marvell is heavily focused on the "scale-up" market—connecting GPUs within a cluster. Their optical interconnects are designed to compete with or complement proprietary fabrics like NVLink.

### 5.3 Nvidia (NASDAQ: NVDA)
Nvidia is the system architect. While they don't manufacture the raw optical components, their architectural decisions dictate the market.
*   **NVLink & InfiniBand:** Nvidia's acquisition of Mellanox was a strategic move to control the interconnect. The NVLink Switch system is increasingly reliant on optical backplanes to scale beyond a single rack.
*   **Supply Chain Kingmaker:** Nvidia's selection of **Fabrinet** for optical assembly and **TSMC** for packaging effectively mints these companies as Tier 1 investments. The "Million-GPU" cluster roadmap necessitates a move to optical switching to manage power, keeping Nvidia at the forefront of SiPh adoption.[19, 20]

### 5.4 Intel Corporation (NASDAQ: INTC)
Intel remains a complex but vital player.
*   **Hybrid Laser Technology:** Intel's key differentiator is its ability to bond III-V laser material onto silicon wafers at scale. This "hybrid integration" solves the light source problem better than many competitors who rely on external lasers.[6]
*   **Foundry Pivot:** Intel is opening its SiPh process to external customers via Intel Foundry. While the company faces broader financial headwinds, its photonics IP remains a crown jewel. The restructuring of Intel Foundry into an independent subsidiary may unlock value here, allowing it to serve competitors to its own product groups.[21, 22]

---

## 6. Supply Chain Vertical: The Foundries (Manufacturing the Light)

Manufacturing photonic chips requires different tools and processes than logic chips. The foundry market is bifurcating into specialized players and volume giants.

### 6.1 GlobalFoundries (NASDAQ: GFS)
GlobalFoundries (GF) has positioned itself as the premier "More-than-Moore" foundry, with silicon photonics as a cornerstone of its strategy.
*   **GF Fotonix Platform:** This is a monolithic platform, meaning GF manufactures the optical components (waveguides, modulators) and the RF/CMOS control electronics on the *same* chip. This eliminates the need for complex wire-bonding between a photonics die and an electronics die, improving performance and reliability.[23, 24]
*   **300mm Scale:** GF is the only foundry offering this monolithic capability on 300mm wafers at high volume. This scale is critical for lowering costs to levels acceptable for mass AI deployment.
*   **Ecosystem:** GF has built a robust ecosystem (EDA partners like Cadence/Synopsys, packaging partners) to lower the barrier to entry for fabless design houses.[24]

### 6.2 Tower Semiconductor (NASDAQ: TSEM)
Tower is a specialty foundry that punches above its weight in photonics.
*   **PH18 Platform:** Tower’s PH18 silicon photonics process is an open platform widely used by leading transceiver makers (like InnoLight). They specialize in high-performance modulators.[25]
*   **Strategic Expansion:** Tower has aggressively moved into 300mm production to support the volume demands of 1.6T and 3.2T transceivers. Their partnership with Intel in New Mexico provides them with 300mm capacity without the massive capital expenditure of building a new shell.[26, 27]
*   **Recent Wins:** Tower recently announced volume production of 1.6T products with a Tier 1 customer, signaling their readiness for the next upgrade cycle.[28]

### 6.3 TSMC (NYSE: TSM)
The world's largest foundry is the linchpin for the most advanced integration: Co-Packaged Optics.
*   **COUPE (Compact Universal Photonic Engine):** TSMC's proprietary technology for integrating photonics with logic. It leverages their SoIC-X (System on Integrated Chips) 3D stacking technology to place the electrical IC directly on top of the photonic IC.
*   **Roadmap:** TSMC is verifying 2nd-generation COUPE for 2026 production. As the manufacturer of Nvidia's GPUs and Broadcom's switches, TSMC is the natural integration point for CPO. If optics go "on-package," TSMC captures the packaging value that previously went to module assemblers.[29]

---

## 7. Supply Chain Vertical: The Module Makers & OSATs (Packaging the Light)

This segment is currently realizing the most immediate revenue from the AI boom, but faces the most long-term disruption from CPO.

### 7.1 Fabrinet (NYSE: FN)
Fabrinet is unique. It is not a designer but a specialized contract manufacturer for high-complexity optical/electro-mechanical packaging.
*   **The Nvidia Proxy:** Fabrinet manufactures the optical interconnects for Nvidia's systems. This relationship is a primary driver of their recent growth, with datacom revenue exploding. Nvidia and Cisco combined account for ~46% of revenue.[30, 31]
*   **Moat:** Optical alignment requires extreme precision (sub-micron). While automation is increasing, Fabrinet's skilled workforce in Thailand provides a cost and quality advantage that is hard to replicate. They are the "safe pair of hands" for high-value optical assembly.
*   **Financials:** Revenue for FY2025 reached $3.42 billion, with consistent earnings beats. They are a cash-rich, low-debt company serving the hottest customers in tech.[32]

### 7.2 InnoLight Technology (300308.SZ) & Eoptolink (300502.SZ)
These Chinese companies are the volume leaders in the global transceiver market.
*   **Market Dominance:** Together, they control an estimated 60% of the 800G optical module market.[10] They are known for aggressive pricing and rapid time-to-market, often qualifying new speeds with hyperscalers (Google, Amazon) faster than Western competitors.
*   **Risks:** Geopolitical risk is high. U.S. tariffs or entity list restrictions could severely impact their ability to serve Western hyperscalers. Both are expanding manufacturing into Southeast Asia (Thailand) to mitigate this.[33]

### 7.3 Amkor Technology (NASDAQ: AMKR)
Amkor is a top-tier OSAT (Outsourced Semiconductor Assembly and Test) expanding into photonics.
*   **Advanced Packaging:** As optics move from the faceplate (pluggables) to the package (CPO), the value shifts to players like Amkor who can handle 2.5D/3D integration.
*   **Lightmatter Partnership:** Amkor is building the world's largest 3D photonics package for Lightmatter. This involves a massive multi-reticle die complex on an organic substrate, showcasing Amkor's ability to handle wafer-scale photonics.[34]
*   **US Footprint:** Amkor's new Arizona facility (supported by Apple and CHIPS Act funding) positions them as a secure, domestic packaging hub for critical AI silicon.[35]

### 7.4 Coherent (NYSE: COHR) & Lumentum (NASDAQ: LITE)
The diversified optical giants.
*   **Coherent:** A vertically integrated powerhouse. They produce the InP wafers, the lasers, and the finished transceiver modules. This vertical control allows them to manage margins better than pure assemblers.[25]
*   **Lumentum:** A leader in telecom and datacom optics. Their strategic opportunity lies in **External Laser Sources (ELS)**. In CPO architectures, the laser is often kept *outside* the hot switch package to prevent thermal degradation. Lumentum is positioning itself as the primary supplier of these ELS modules, ensuring they have a role in the CPO future.[25, 36]

---

## 8. Supply Chain Vertical: Emerging Disruptors & Deep Tech

This is the high-risk, high-reward frontier. These companies are betting on new architectures to solve the bottlenecks that standard silicon photonics cannot.

### 8.1 Ayar Labs
A private unicorn backed by Nvidia and Intel Capital.
*   **Technology:** Ayar Labs replaces the electrical SerDes on a processor with an optical I/O chiplet ("TeraPHY"). This allows the processor to communicate with high bandwidth at very low power (<5pJ/bit) over distances up to 2km.
*   **Implication:** This enables "disaggregated computing"—separating memory from compute and pooling it. This solves the "memory wall" in AI training.[1, 37]

### 8.2 Lightmatter
*   **Photonic Computing:** Lightmatter uses light not just for transport, but for calculation (matrix multiplication). Their "Passage" interconnect is a wafer-scale programmable optical fabric.
*   **Valuation:** Recently raised $400M at a $4.4B valuation, creating a massive war chest to scale their technology. They are positioning themselves as a platform company for the post-Moore's Law era.[14, 38]

### 8.3 POET Technologies (NASDAQ: POET)
*   **The Optical Interposer:** POET's innovation is a "hybrid integration" platform. Instead of trying to force lasers onto silicon (which is hard), they use a novel interposer material that allows them to "flip-chip" lasers and detectors with passive alignment.
*   **Cost Advantage:** This eliminates the expensive active alignment process required by traditional assembly, potentially lowering the cost of optical engines by 20-40%. They have demonstrated 800G and 1.6T engines and are targeting the AI market.[39, 40]

### 8.4 Lightwave Logic (NASDAQ: LWLG)
*   **Polymer Modulators:** Silicon modulators have physical speed limits. Lightwave Logic develops electro-optic polymers that can switch faster (100GHz+) with less voltage.
*   **The Thesis:** As lane speeds hit 200G and 400G, silicon may run out of steam. Polymers could be the material that extends the roadmap. However, integrating organic polymers into standard fab processes is a significant hurdle.[41]

---

## 9. Supply Chain Vertical: Equipment & EDA (The Enablers)

You cannot build what you cannot design or test. This often-overlooked segment provides the picks and shovels for the photonics gold rush.

### 9.1 Equipment: Besi & ficonTEC
*   **Besi (BE Semiconductor):** Holds a dominant 75% market share in advanced die attach equipment. Their hybrid bonding tools are essential for the 3D stacking used in TSMC's COUPE and other CPO processes.[42]
*   **ficonTEC:** A specialized German firm (private) that builds the automated assembly lines for photonics. Their machines handle the sub-micron alignment of fibers to chips—the most critical step in manufacturing.[43, 44]

### 9.2 Test & Measurement: Keysight & FormFactor
*   **The Challenge:** How do you test a chip that uses light? You can't just touch a metal probe to a pad. You have to couple light in and out.
*   **Solution:** Keysight (electronics/optics test) and FormFactor (wafer probing) have partnered to create integrated SiPh test stations. These automated systems are critical for yield management as volumes ramp.[45, 46]

### 9.3 EDA: Synopsys & Cadence
*   **Design Tools:** Designing photonics requires simulating light physics (Maxwell's equations) alongside electrical circuits. Synopsys (with Ansys) and Cadence have monopolized the EDA flow for photonics. Every chip designed by Nvidia, Broadcom, or Marvell pays a toll to these duopolists.[47, 48]

---

## 10. Geopolitical & Macro Risks

### 10.1 The China Factor
The current supply chain is dangerously concentrated. A vast majority of the world's optical transceivers are assembled in China by InnoLight, Eoptolink, and others.
*   **Risk:** If the U.S. government restricts the import of Chinese optics (similar to Huawei restrictions) or restricts the export of advanced DSPs to these entities, the supply chain would fracture.
*   **Mitigation:** Investors should look for companies with diversified footprints. **Fabrinet** (Thailand), **Amkor** (Vietnam/US), and **GlobalFoundries** (US/Singapore/Germany) are beneficiaries of this "China Plus One" strategy.[5]

### 10.2 The CPO "Osborne Effect"
The industry is currently buying 800G pluggables in massive volumes. However, the looming promise of CPO (more efficient, denser) could cause a pause in spending or "inventory digestion" as hyperscalers wait for the next generation. Companies heavily exposed to pluggables (InnoLight, Coherent) face a long-term terminal value risk if they do not successfully pivot to supplying CPO components (like ELS).

### 10.3 Technical Execution
Integrating lasers on silicon is arguably one of the hardest problems in hardware engineering. Thermal mismatch, yield loss, and reliability are constant battles. Any high-profile failure of a CPO deployment (e.g., widespread field failures of an optical switch) could set the industry back years and chill investment.

---

## 11. Investment Synthesis and Conclusion

The transition from copper to silicon photonics is one of the most certain structural trends in technology. The physics of AI scaling dictate it. For the investment analyst, the key is to separate the hype from the deployable reality and to identify where the value accrues in the stack.

### Tiered Investment Framework

| Tier | Investment Profile | Top Picks | Rationale |
| :--- | :--- | :--- | :--- |
| **Tier 1: The Core Foundation** | **Defensive Growth** | **Broadcom (AVGO)** | Captures value across the entire stack (Switch + DSP + Optics). The safest way to play the trend. |
| **Tier 2: The Direct AI Play** | **Aggressive Growth** | **Fabrinet (FN)** | The manufacturing engine for Nvidia. Direct correlation to AI hardware volume with a strong competitive moat. |
| **Tier 3: The Enablers** | **Cyclical/Industrial** | **GlobalFoundries (GFS), Besi (BESI)** | The manufacturing and equipment backbone. GFS is a strategic sovereignty play; Besi is a monopoly on the necessary packaging tools. |
| **Tier 4: The Speculative Upside** | **Venture/High-Beta** | **POET Technologies (POET), Lightwave Logic (LWLG)** | High risk, but massive potential if their specific architectures (Interposer/Polymer) are adopted as industry standards. |

**Conclusion:** The "Copper Wall" is real, and the bridge across it is built of silicon photonics. The supply chain has matured from a scientific curiosity to a critical industrial ecosystem. As 2025 approaches, the market is shifting from early adoption to mass deployment, creating a prime window for capital allocation into the leaders of this optical revolution. The winners will be those who can manufacture light at the scale of silicon.

---
### Data Tables

**Table 1: Market Growth Forecasts**

| Source | 2025 Market Size ($B) | 2030 Market Size ($B) | CAGR | Key Driver Note |
| :--- | :--- | :--- | :--- | :--- |
| **MarketsandMarkets** | $2.65 | $9.65 | ~30% | AI & Data Center focus |
| **Precedence Research** | $2.86 | $28.75 (by 2034) | 29.25% | Long-term ubiquity |
| **Mordor Intelligence** | $3.11 | $10.36 | 27.21% | High-speed transceivers |

**Table 2: Key Company Revenue Exposure & Positioning**

| Company | Ticker | Primary Role | Key Customer/Partner | Strategic Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **Broadcom** | AVGO | IDM (Switch/DSP/Optics) | Hyperscalers (Google/Meta) | Vertical Integration, CPO Leadership |
| **Fabrinet** | FN | Optical Assembly Services | Nvidia, Cisco | Precision Manufacturing Monopoly |
| **InnoLight** | 300308.SZ | Transceiver Module Maker | Google, Amazon | Speed to Market, Cost Structure |
| **GlobalFoundries** | GFS | Pure-Play Foundry | Broadcom, Cisco, Nvidia | Monolithic Fotonix Platform, US Fabs |
| **Marvell** | MRVL | Fabless (DSP/Optics) | Hyperscalers | Open Ecosystem, DSP Leadership |
| **Amkor** | AMKR | OSAT (Packaging) | Apple, Lightmatter | 2.5D/3D Packaging Scale |
| **POET Tech** | POET | Platform Provider | AI Hardware Makers | Optical Interposer Cost Reduction |
Nov 25, 2025, 4:14:45 PM AEST
Products:
 Gemini Apps
Why is this here?
 This activity was saved to your Google Account because the following settings were on: Gemini Apps Activity. You can control these settings  here.Gemini Apps

---

## Related
- [[Theses/LITE - Lumentum]] — Photonics supply chain positioning
- [[Theses/IQE - IQE]] — III-V semiconductor substrates for photonics
- [[Research/2026-03-10 - LITE - Gemini Photonics CPO Canvas]] — Later CPO adoption analysis
- [[Sectors/Semiconductors]]
