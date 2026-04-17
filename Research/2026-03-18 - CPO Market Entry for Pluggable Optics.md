---
date: 2026-03-18
tags: [research, semiconductors]
status: active
sector: Semiconductors
source: Claude conversation export
---

# CPO Market Entry for Pluggable Optics

## Original Query
> What is the likelihood of LITE and COHR gaining a foothold in the CPO market given today they mostly focus on pluggable opticals. 

Which vendors are most likely to excel in the move to CPO specifically, rather than other aspects of silicon photonics.

---

# Co-packaged optics: who wins the next optical revolution

**Vertically integrated semiconductor companies — Broadcom, NVIDIA, and Marvell — hold decisive structural advantages in CPO, while optical specialists Lumentum and Coherent are pivoting from transceiver makers to indispensable laser foundries.** This bifurcation reshapes the $8 billion CPO market expected by 2030. NVIDIA's $4 billion combined investment in Lumentum and Coherent (March 2026) confirms that InP laser supply — not silicon photonics fabrication — is the critical bottleneck. Broadcom already shipped over **50,000 CPO switches in 2025**, proving production viability, while NVIDIA's Spectrum-X and Quantum-X CPO switches begin shipping in 2026. For investors evaluating LITE and COHR, the central question is not whether these companies participate in CPO, but whether their role as component suppliers commands the same margins and market power as their current position in pluggable transceivers.

## Coherent's broader portfolio creates a different CPO playbook

Unlike Lumentum, Coherent designs silicon photonics PICs in-house (led by VP of Silicon Photonics Technology Po Dong) but outsources fabrication to **Tower Semiconductor's PH18 process**. This fabless SiPh model creates supply chain dependency but mirrors common semiconductor industry practice. Coherent also brings unique complementary assets: silicon carbide thermal management materials, diamond-SiC composite substrates, Thermadite liquid cold plates, and its own Steelerton DSP — capabilities that address CPO's thermal challenges directly. The company is a founding member of both the **Open CPX MSA** (interoperable CPO optical engines) and **XPO MSA** (12.8T liquid-cooled optics), signaling commitment to open CPO standards.

## Lumentum is becoming the "arms dealer" of CPO

What Lumentum conspicuously lacks is any in-house silicon photonics PIC fabrication. It does not design or manufacture the SiPh optical engines that sit inside CPO packages — it supplies the light that feeds them. This positions Lumentum as a critical but narrower participant in the CPO value chain compared to its current role as a vertically integrated transceiver component maker. The hiring of CTO Matt Sysak, formerly VP at Ayar Labs with prior Intel silicon photonics experience, signals awareness of this gap.

## Conclusion: the market splits, and both halves are enormous

The CPO market is not a winner-take-all contest between vertically integrated semiconductor giants and optical specialists. It is splitting into two distinct, complementary markets. **Broadcom, NVIDIA, and Marvell will own CPO system integration** — the design and packaging of optical engines with switch ASICs — because this requires capabilities that optical specialists fundamentally lack: ASIC co-design, advanced 3D packaging through TSMC, and direct hyperscaler system architecture relationships.

The risk for both LITE and COHR is margin compression. In pluggable transceivers, they capture value across multiple components and module assembly. In CPO, they primarily supply laser chips and ELSFP modules — a critical but smaller slice of the total system value. The offsetting factor is volume: if CPO reaches even a fraction of its projected $8-20 billion market by 2030-2036, the laser source TAM alone could exceed current transceiver component revenues. The companies that thrive will be those that expand their CPO footprint beyond lasers — through optical engine design (Coherent's advantage), advanced packaging partnerships, or new architectures like Lumentum's VCSEL-based co-packaged interconnects for AI scale-up.

Great question, Reo — this gets at one of the key strategic tensions in the optical interconnect space. The pluggable-to-CPO transition is a meaningful inflection point, and the competitive dynamics are quite different from traditional transceivers.

**Lumentum and Coherent are transitioning from transceiver makers to laser foundries** — and this role is both more narrow and more critical than it might appear. Every silicon photonics CPO module requires external InP CW lasers, and InP fabrication capacity is the binding constraint on CPO deployment timelines. NVIDIA's combined $4 billion investment in both companies validates their indispensability. Lumentum holds the edge in raw laser power (800 mW SHP) and its NVIDIA-exclusive positioning, while Coherent's broader platform — spanning SiPh design, VCSEL arrays, InP modulators, thermal materials, and standards leadership — offers more pathways into the CPO value chain.

Let me dive deep into this. I'll research LITE and COHR's CPO positioning, their technology portfolios and partnerships, and map out which vendors (including pure-play silicon photonics names, semiconductor companies, and vertically integrated players) are best positioned to win in CPO specifically.

## Five barriers stand between pluggable specialists and CPO leadership

**ASIC co-design proximity** creates the most durable structural advantage for vertically integrated players. CPO requires co-optimization of electrical-optical interfaces, SerDes architecture, power integrity, and thermal management. Broadcom designs both the Tomahawk ASIC and its optical engines; NVIDIA designs its switch ASICs and controls the CPO integration through TSMC SoIC. Optical specialists like Lumentum and Coherent must work within the ASIC vendor's design framework, reducing their position in the value chain.

**Silicon photonics platform transition** is less a barrier than a value-chain redefinition. CPO is overwhelmingly SiPh-based, but InP-focused companies like Lumentum and Coherent are not being displaced — they are being repositioned. Silicon cannot produce laser light efficiently, making InP CW lasers an absolute requirement for every SiPh CPO module. LightCounting projects silicon photonics market share will double from **~30% in 2025 to ~60% by 2030**, driven by LPO and CPO adoption. The InP laser supply chain has become the critical bottleneck, with NVIDIA pre-allocating capacity and lead times extending past 2027.

**Thermal management** is the most critical barrier. Modern switch ASICs dissipate 500-700W+, and co-packaging optical components next to this heat creates severe challenges. Micro-ring resonators shift resonance wavelength with just a 1°C variance, and junction temperatures in CPO systems reach approximately 97°C. The industry's pragmatic solution — external laser sources in front-panel ELSFP modules, combined with mandatory liquid cooling — benefits Lumentum and Coherent as laser suppliers but fundamentally changes data center infrastructure. Coherent's SiC thermal materials and cold plate capabilities provide an additional advantage here.

## Broadcom and NVIDIA dominate through vertical integration

**Marvell** took a different path, acquiring **Celestial AI for $3.25 billion** in December 2025. Celestial AI's Photonic Fabric technology uses an Optical Multi-Chip Interconnect Bridge (OMIB) enabling connectivity from any point on one die to any point on another — not just edge-to-edge like traditional CPO. The first-generation chiplet delivers 16 Tb/s bandwidth, claiming 25× greater bandwidth and 10× lower latency than conventional CPO. Marvell expects meaningful Celestial AI revenue starting H2 FY2028, with a $1 billion annualized run rate by Q4 FY2029. Combined with Marvell's custom ASIC business serving hyperscalers directly, this positions Marvell as a differentiated third force in CPO.

## CPO volume deployment arrives in waves through 2028

The adoption timeline follows a clear pattern: production has begun at small scale, but mass deployment remains two to three years away. **Broadcom's 50,000+ Bailly CPO switches** represent the only true volume production to date. NVIDIA's Quantum-X800 InfiniBand CPO switch shipped in H2 2025, with Spectrum-X Photonics Ethernet switches expected H2 2026. TSMC's COUPE entered risk production with AMD in February 2026, targeting high-volume 6.4T-per-package runs in H2 2026.

---

## Related
- [[Sectors/Semiconductors]]
