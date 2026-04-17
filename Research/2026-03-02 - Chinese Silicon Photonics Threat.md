---
date: 2026-03-02
tags: [research, semiconductors]
status: active
sector: Semiconductors
source: Claude conversation export
---

# Chinese Silicon Photonics Threat

## Original Query
> Assess the market share and competitive threat in the Copackged Optics / Silicon Photonics space from the Chinese supply chain. How does this translate to competitive risk for the US/Western dominated supply chain’s listed stocks like Lumentum / Coherent / AAOI etc.
> Thanks good work

---

## How each Western stock faces the competitive threat

**Coherent Corp (COHR)** is the most directly exposed. As the #2 global transceiver vendor, Coherent competes head-to-head with Innolight and Eoptolink for hyperscaler volume. FY2025 revenue hit a record **$5.81B** (+23% YoY) with networking growth of 45–56%, and datacom revenue surged 79% YoY in Q2 — but this growth is market-driven, not share-driven. Coherent holds roughly 20% of Nvidia's optical wallet. Its estimated production costs run **10–20% higher than Innolight's**, creating structural margin pressure as the market matures. The defensive strategy centers on vertical integration (in-house InP lasers, VCSELs, and silicon photonics PICs) and a pivot toward optical circuit switches for AI datacenters. Coherent's FY2026 Q2 data center revenue grew 36% YoY. Analyst consensus is Strong Buy with a median price target of ~$240 and market cap of ~$48.5B, but the bull case depends on component leadership rather than module volume growth.

**Applied Optoelectronics (AAOI)** is the most vulnerable. With ~$456M in 2025 revenue and ongoing net losses, AAOI is dwarfed by both Chinese and Western competitors. Its US-based manufacturing (Sugar Land, TX) carries **3x higher labor costs** than Chinese/Southeast Asian alternatives. Customer concentration is extreme — 95.8% of revenue comes from its top 10 customers, with Microsoft as the anchor. AAOI received a multi-million-dollar 800G OSFP order from a North American hyperscaler in December 2025, but short-seller Culper Research has questioned the company's 800G manufacturing claims. At ~$5B market cap with a beta of 7.18, AAOI trades as a speculative option on AI infrastructure spending rather than a structural competitive advantage. Analyst consensus is Buy with an average target of ~$49, but the company's survival in a market dominated by Innolight-class competitors is uncertain.

**Marvell (MRVL)** benefits from its PAM4 DSP near-duopoly but faces long-term disruption. Q3 FY2026 revenue hit a record **$2.1B** (+37% YoY) with data center at $1.5B. The $3.25B acquisition of Celestial AI (completed February 2026) positions Marvell in photonic fabric interconnects for scale-up connectivity, expected to contribute **$500M annually by late 2028**. However, the LPO trend, Nvidia's in-house DSP development, and eventual Chinese DSP alternatives all threaten Marvell's core optical DSP franchise. Analyst consensus is Strong Buy with an average target of ~$116.

**Cisco** is playing a longer game through its Acacia integration, which yielded the **Kibo 3nm 1.6T PAM4 DSP** — entering direct competition with Marvell and Broadcom in client optics. Silicon One G300 (102.4 Tbps) was announced in February 2026 for AI clusters, with AI infrastructure orders from hyperscalers reaching $2.1B in Q2 FY2026. Cisco is pursuing both CPO and LPO but maintaining a measured timeline, with CEO Robbins stating CPO will happen but "is not imminent."

**Lumentum (LITE)** has perhaps the most compelling strategic pivot. FY2026 Q2 EPS of **$1.67 beat consensus by 36%**, and the company guided to ~$790M Q3 revenue. Stock appreciated ~287% in 2025. Lumentum is deliberately retreating from direct transceiver competition and repositioning as a **component supplier** — EML chips, pump lasers, CW lasers for CPO, and silicon photonics modules through its Cloud Light subsidiary (acquired for ~$750M). The company closed two photonic factories in China and is shifting production to Thailand and a new US indium phosphide wafer fab for CPO components. Management targets "significant revenue ramp in CPO by 2026." Lumentum is named as a CPO ecosystem partner for both Nvidia and Broadcom. Average analyst price target is ~$505 (13 analysts, consensus Buy), with Rosenblatt modeling $14–19 FY2027 EPS in upside scenarios. The risk is that CPO timelines slip and Chinese competitors close the laser technology gap.

**Broadcom** holds the strongest structural position through vertical integration of switch ASICs (Tomahawk/Jericho), silicon photonics, and CPO. Its Bailly CPO platform is the **only CPO solution validated in production** at a hyperscaler (Meta). Broadcom's third-generation 200G/lane CPO (Davisson) was previewed in May 2025, and a 102.4 Tbps CPO switch is expected in H2 2026. If CPO captures a significant share of the optical interconnect market (projected >$20B by 2036), Broadcom could effectively disintermediate both Chinese and Western transceiver module vendors. This makes Broadcom the primary beneficiary of the CPO transition and the greatest long-term threat to the pluggable transceiver market.

# China's optical dominance threatens Western photonics incumbents

**Chinese manufacturers now control more than half the global high-speed optical transceiver market, dominating the 800G generation and positioning to capture 50–60% of 1.6T shipments — yet they remain critically dependent on Western DSP chips and laser technology, and trail by 3–5 years in co-packaged optics.** This asymmetry defines the competitive threat: Chinese module assemblers are winning the volume battle today, while Western firms retreat up the value chain into components, CPO integration, and silicon IP where margins and defensibility are higher. The AI infrastructure supercycle, projected to push the optical transceiver market past **$23 billion in 2025** (LightCounting), is temporarily masking this structural market share shift — every major Western optical stock posted record revenues in 2025 even as their unit share eroded. But as growth normalizes toward 2027–2028, the pricing pressure from Chinese competitors operating with **20–25% lower costs** will become the dominant narrative.

## The 1.6T generation reinforces Chinese leadership, but CPO changes the game

Chinese firms are pursuing CPO but lag significantly. Huagong Zhengyuan demonstrated a **3.2T DWDM CPO optical engine** at CIOE 2025, and Innolight has tested 3.2T optical engines — but no Chinese company has CPO in commercial production. The critical bottleneck is advanced packaging: TSMC's COUPE platform controls the integration of photonic chips with switching ASICs, and Chinese foundries have nothing comparable. The CPO market, valued at just ~$120M in 2025, is projected to reach **$20B+ by 2036** (IDTechEx), representing a potential paradigm shift that could redirect value from Chinese module assemblers to Western chip-and-packaging leaders.

Innolight was the first vendor to complete **1.6T transceiver testing with Nvidia** and began phased shipments in Q2 2025. The company is projected to capture **50–60% of the 1.6T module market** in 2025, with volume inflection expected in 2026 when shipments could reach 3–5 million units. Eoptolink launched a fully retimed 1.6T OSFP with 3nm DSP at OFC 2025 and plans mass production of its VCSEL-based 1.6T variant by Q4 2025. Accelink's 1.6T monthly capacity already reaches **500,000 units**.

## Conclusion: a bifurcating market with different winners at each layer

The optical interconnect market is splitting into two distinct competitive arenas with different dynamics. In **pluggable transceivers** (800G through 1.6T), Chinese dominance is structural and accelerating — Innolight and Eoptolink have superior scale economics, faster time-to-market, and consistent profitability that Western module competitors cannot match. This arena will see persistent pricing pressure, with Chinese vendors pricing 20–25% below Western alternatives while maintaining higher margins. AAOI and Coherent's module business face the most direct competitive threat here.

In **co-packaged optics and silicon photonic integration**, Western companies hold a 3–5 year lead that could prove durable. Broadcom, Nvidia, and Marvell are integrating optics with switch silicon and AI accelerators at a level of system complexity that Chinese module assemblers cannot replicate — particularly given TSMC's central role in advanced packaging. The CPO market is projected to grow from ~$120M today to over $20B within a decade. If CPO captures even 30–40% of high-speed optical interconnect spending by 2030, it would fundamentally restructure who captures value in the optical supply chain.

The most important insight is that **the AI supercycle is temporarily obscuring a structural market share shift**. With the datacom optical market growing 60%+ annually, every company is posting record revenues regardless of competitive position. When growth normalizes toward 15–20% annually in 2027–2028, the pricing pressure from Chinese competitors will become the dominant investment narrative for Western optical stocks. The Western companies best positioned are those pivoting toward component-level and system-level integration — Lumentum in lasers and CPO components, Broadcom in full-stack CPO, and Marvell in DSP and photonic fabric — rather than those competing directly for pluggable transceiver volume against Innolight's manufacturing machine.

**Biggest open question:** Whether CPO timelines slip (again). Broadcom and Nvidia are committed, but actual hyperscaler deployment at scale beyond Meta's initial rollout remains to be seen. If CPO gets pushed out to 2028+, the pluggable transceiver market (and Chinese dominance of it) persists longer — which is actually better for Innolight/Eoptolink and worse for the CPO-centric Western bull thesis.

**Near-term catalysts to watch:** Broadcom's Bailly CPO ramp at Meta through 2026, Innolight's 1.6T volume inflection (likely H2 2026), and whether the 200G EML laser shortage eases — that bottleneck is currently the single biggest constraint on the entire 1.6T transition.

**The "hidden" risk for bulls on Western optical names:** If you're long COHR or LITE primarily on the AI transceiver volume story, it's worth stress-testing what happens when growth decelerates to ~15–20% in 2027–28 and Innolight is still pricing 20%+ below. The stocks that hold up best will be the ones that have successfully pivoted to CPO components and vertical integration by then.

## Trade policy provides limited protection as Chinese firms adapt

Export controls are more targeted but also limited in their optical-specific impact. The 42 PRC entities added to the Entity List in March 2025 and 23 more in September 2025 primarily target advanced logic chips and GPUs, not optical components directly. The indirect vulnerability for Chinese transceiver makers lies in their dependence on Western DSPs manufactured at TSMC on 3nm/5nm nodes — but restricting DSP sales to Chinese optical vendors would immediately disrupt supply to Nvidia and all major hyperscalers, making such action self-defeating. The Trump-Xi Busan meeting in late 2025 produced a mutual tariff reduction, and the new USTR Section 301 investigation specifically targeting semiconductors set an initial tariff of 0%, with increases not scheduled until June 2027.

The tariff regime on Chinese optical components is theoretically severe — **25% Section 301 tariffs** plus 20% IEEPA fentanyl duties plus regular MFN duties could bring total effective tariffs to 55–65%+ on Chinese-origin transceivers. But the practical impact has been minimal. Chinese manufacturers have systematically shifted final assembly to Thailand, Vietnam, and Malaysia under a **"China design + Southeast Asia manufacturing"** model, with combined monthly capacity exceeding **1.5 million units**. LightCounting's July 2025 assessment was unambiguous: "The trade war has had no significant impact on sales of optical transceivers to US-based Cloud companies."

## Critical dependencies give Western firms structural leverage

- **High-speed lasers:** EML and InP laser technology for 200G-per-lane applications remains dominated by Coherent and Lumentum. A severe shortage of **200G EML chips** currently constrains the entire 1.6T ramp, with Nvidia reportedly assisting suppliers to accelerate production. Source Photonics has made progress with in-house EML and monolithic InP PICs, but Coherent and Lumentum retain the technology lead. China's JFS Laboratory in Wuhan achieved the country's first integrated laser-on-silicon demonstration, but this is R&D-stage, not production-ready.

The **LPO (Linear Pluggable Optics)** trend partially mitigates DSP dependency by eliminating the DSP chip entirely, using only analog driver/TIA chips. Eoptolink has aggressively commercialized LPO for specific hyperscale customers. But DSP-based retimed optics remain the interoperability standard, and Nvidia is developing its own 1.6T DSP (via its Mellanox team) that could eventually cover >50% of its own volume — further squeezing Chinese module makers' wallet share at the system vendor level.

- **PAM4 DSP chips:** Marvell holds **80%+ share** at 800G speeds, with Broadcom as the primary alternative. These chips represent ~30% of transceiver BOM cost, and Chinese vendors are entirely dependent on them. Marvell's Ara (3nm, 1.6T) won the industry's Leading EDGE Award in 2025; no Chinese alternative operates at competitive performance. Over a dozen Chinese DSP startups exist (Aluksen, EOChip, Hengxin Semitech), but **none have achieved meaningful market penetration** at 800G/1.6T speeds. LightCounting estimates Chinese DSP development trails by **2–3 years**.

- **Advanced packaging for CPO:** TSMC's COUPE platform is the de facto standard for next-generation CPO, adopted by both Nvidia and Broadcom. Chinese packaging capability has no equivalent. However, silicon photonics fabrication itself does **not require EUV lithography**, giving China a potential long-term pathway using domestic DUV equipment — a strategically significant fact as export controls tighten.

---

## Related
- [[Sectors/Semiconductors]]
