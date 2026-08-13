---
title: 'Nvidia Ships Co-Packaged Optics Switch as Ecosystem Testing Gap Widens'
source: 'https://www.techtimes.com/articles/324160/20260812/nvidia-ships-co-packaged-optics-switch-ecosystem-testing-gap-widens.htm'
date: 2026-08-13
tags: [daily-intel-triage, news]
holdings: [NVDA, LITE, AAOI, TSM]
---

# Nvidia Ships Co-Packaged Optics Switch as Ecosystem Testing Gap Widens

Source: https://www.techtimes.com/articles/324160/20260812/nvidia-ships-co-packaged-optics-switch-ecosystem-testing-gap-widens.htm

Why it matters: Spectrum-6 CPO is in production and shipping (CoreWeave/Lambda/Meta/MSFT/OCI) via TSMC COUPE — productizes CPO for NVDA/TSM while the testing-gap preserves near-term pluggable content at LITE/AAOI.

## Extracted body

Nvidia Senior Vice President of Networking Gilad Shainer confirmed at the OCP APAC Summit in Taipei this week that the company's Spectrum-6 co-packaged optics switches are in production and shipping — delivering what the networking industry has been waiting years to see. But the most important thing said at that summit may have come from a different stage, where a senior engineer from one of the world's largest chip packaging houses warned that the ecosystem required to generalize that milestone to a multi-vendor market does not yet exist. Hyperscalers evaluating their next network fabric refresh now face a precise question: is Nvidia's confirmed production a signal that co-packaged optics is ready for procurement, or a signal that one company has achieved something the broader supply chain has not yet solved?

The two-day OCP APAC Summit wrapped August 12 at the Taipei Nangang Exhibition Center Hall 2 (TaiNEX2), bringing together cloud service providers, semiconductor firms, advanced packaging houses, silicon photonics startups, and open-hardware advocates. For the first time at a major OCP event, TSMC, Applied Materials, and ASE Group shared the keynote stage alongside Microsoft, Nvidia, and Google — a visible signal of how far upstream the CPO challenge reaches.

### Networking Replaced Compute as AI Infrastructure's Binding Constraint

The summit's opening consensus was that the data center's primary bottleneck has shifted. For most of the past decade, GPU supply and advanced packaging throughput defined the ceiling on AI infrastructure scaling. At OCP APAC 2026, that argument reversed: with GPU supply normalizing and inference workloads spreading AI compute more broadly, the interconnect layer — bandwidth per watt, radix per rack unit, and the sheer physics of copper at scale — has emerged as the new binding limit.

Shainer put it directly: networking, he said, is now the core of AI computing as AI factories scale. The shift in framing matters for buyers: a data center optimized for GPU procurement is not optimized for the agentic AI era, where the orchestration overhead of multi-step autonomous tasks compounds the interconnect burden on every workload.

### What Co-Packaged Optics Actually Does — and Why Copper Hit Its Limit

Co-packaged optics integrates the optical engine — the component that converts electrical signals to light — directly with the switch application-specific integrated circuit (ASIC) in a single package. The practical effect, as Nvidia's silicon photonics page explains, is that the signal conversion happens millimeters from the chip rather than at the switch's front panel, eliminating the digital signal processing retimer that pluggable transceiver modules require and cutting power consumption by as much as five times over pluggable alternatives.

The reason copper forced this transition is physics. At 448G PAM4 signaling — the electrical standard current AI switches require — copper cable can reliably carry a signal only about 25 centimeters (9.8 inches). At 112G, that same copper reached 2 meters (6.6 feet). The collapse in usable reach is not a manufacturing deficiency; it is a fundamental constraint of how high-frequency electrical signals attenuate in a conductor. Routing 448G copper across even a modest multi-rack AI cluster would require retimers and signal conditioning hardware that consume power the data center would far rather spend on compute.

The consequences for compute efficiency are measurable. Bijan Nowroozi, Ecosystem Development Director at Lightmatter and former Chief Technology Officer of the OCP Foundation, told OCP APAC attendees that AI training clusters are currently achieving Model FLOPS Utilization (MFU) of only 38 to 43 percent — meaning more than half of the available compute on any given cluster is lost to interconnect overhead, not doing productive AI work. That figure, applied to a $500 million data center, implies roughly $280 to $310 million worth of compute sitting idle at any moment because the network cannot feed it data fast enough.

### How Nvidia Built the World's First Commercial-Scale CPO Switch

Nvidia's Spectrum-6 CPO achievement depends on a manufacturing platform that took years of bilateral co-development with TSMC to build. The foundation is TSMC's COUPE (Compact Universal Photonic Engine) platform, which Focus Taiwan has confirmed uses SoIC (System on Integrated Chips) stacking to place an electrical die directly on top of a photonic die. The result is an ultra-low impedance die-to-die interface that shortens the electrical-to-optical conversion path to the minimum physically achievable.

TSMC Vice President of Advanced Packaging Technology Jun He, who leads the foundry's CoWoS capacity scaling, told the summit that the COUPE bandwidth density roadmap runs from 0.5 terabits per second per millimeter in 2026 toward 4 terabits per second per millimeter by 2030 — an eightfold improvement over four years, driven by next-generation micro-ring modulator scaling. He also named the three challenges the industry has not yet collectively solved: wafer-level testing protocols, fiber array unit integration, and high-speed optical packaging assembly.

For buyers, Nvidia's CoreWeave, Lambda, Meta, Microsoft, and Oracle Cloud Infrastructure count among the first adopters of its CPO switches. Production capacity, Shainer has indicated, is expected to expand through the second half of 2026.

### What the Production Milestone Actually Means for Buyers — and What It Does Not

The confirmation that Nvidia ships CPO switches is real and significant. It is not sufficient to signal that co-packaged optics is ready for industry-wide procurement — a distinction that matters for every infrastructure buyer planning a network refresh in 2026 or 2027.

Nicole Tien, Senior Technical Program Manager at ASE Group — one of the world's largest outsourced semiconductor assembly and test providers and a mandatory link in any CPO manufacturing chain — stated the ecosystem gap clearly at OCP APAC. Co-packaged optics has become the inflection point for AI infrastructure, she said, but the industry has not yet built the shared testing standards and simulation groundwork the technology needs. Without standardized wafer-level test protocols and agreed-upon simulation methodologies, every participant in the supply chain — foundry, OSAT, system integrator, hyperscaler — must maintain independent verification processes, multiplying cost and slowing the yield learning that would otherwise drive prices down.

The distinction Tien drew is precise: Nvidia's production reflects a deep bilateral integration with TSMC, executed within a tightly controlled and co-developed supply chain. Generalizing that achievement to a multi-vendor ecosystem where any hyperscaler can procure CPO switches from multiple competing vendors — the condition that delivers real market competition and buyer leverage — requires standardization work that has not yet been completed.

Third Bridge industry experts reached the same conclusion independently in June 2026: Nvidia's deployment falls short of signaling that CPO is ready for industry-wide adoption. Those analysts cited manufacturing yields, packaging complexity, and long-term reliability as continuing challenges, and noted that North America's largest cloud providers "may not become major adopters over the near term" from a supply chain perspective.

The absence of shared testing standards is not a minor procedural gap. It is the structural reason that Nvidia's CPO milestone, while real, may accelerate vendor lock-in rather than democratize the technology. A hyperscaler that deploys CPO today does so through Nvidia's proprietary ecosystem — deep co-engineering with TSMC via a platform no independent supplier can yet replicate to spec. Until OCP-standard testing frameworks exist, the choice for any buyer is: Nvidia's ecosystem, or wait.

### Pluggable Optics: An 18-Month Runway Before the Physics Runs Out

For the majority of buyers not yet considering CPO procurement, the clearest signal from OCP APAC came from Andy Bechtolsheim, co-founder and chief architect of Arista Networks, who put a specific expiration date on the current generation of front-panel pluggable optics. Pluggable optics hit their density ceiling at the 49.6T switch generation, he said — a transition point he placed roughly 18 months away. At that density, the radix required for high-performance AI switching cannot be achieved with modules mounted at a switch chassis's front panel.

Bechtolsheim's involvement in the XPO (eXtra-dense Pluggable Optics) multi-source agreement gives his timeline credibility. XPO, backed by more than 100 companies including Microsoft, Marvell, Broadcom, and Ciena, packs substantially more optical density than current OSFP modules — Bechtolsheim has described each XPO module as delivering 12.8 terabits per second of bandwidth, versus 1.6 terabits per second for an OSFP. XPO represents the industry's attempt to extend the serviceable pluggable era by one switch generation — buying time for the CPO ecosystem standardization that ASE's Tien identified as incomplete.

The panel also surfaced Nvidia's nuanced position on copper: the company does not advocate replacing copper wherever physics still permits. "If I'm doing NVLink72 or NVLink 144, for example, and that fits copper dimensions, I'm going to take copper," Shainer has said. The physics, not ideology, determines the medium — and for multi-rack scale-up topologies like NVLink 1152 that span beyond copper's 25-centimeter (9.8-inch) 448G reach, CPO becomes structurally necessary.

### Open Standardization: Lightmatter's OCP Architecture Initiative

The most direct attempt to close the ecosystem gap Tien named is a collaborative workstream Lightmatter launched within OCP in March 2026, at the Optical Fiber Communication conference, aimed at producing open specifications for interoperable CPO across multiple vendor platforms.

Nowroozi's OCP APAC session presented the initiative's technical architecture in detail: a technology-agnostic photonic interconnect framework extending OCP's Modular Hardware System and Open Rack v3 specifications, defining interface contracts and passive infrastructure — faceplates, optical distribution frames, raceway, and external laser small-form-factor pluggable shelves — with link profiles spanning from DR single-wavelength configurations through dense wavelength division multiplexing 16-wavelength links across CPO, near-package optics, XPO, and CPX optical engine classes for both accelerator and switch platforms.

The targets are ambitious: scaling from 72 to more than 1,024 accelerators in scale-up configurations, pushing MFU from its current 38–43% range toward 55–65%, achieving under 5 picojoules per bit energy efficiency, and using generation-invariant fiber infrastructure so that physical plant investments made today are not stranded when CPO switches to the next generation. More than 50 APAC suppliers already build AI Modular Hardware System equipment; the session was designed to recruit them into the interoperability workstream.

Lightmatter's March 2026 launch has already brought Celestica, Corning, Dell Technologies, Flex, Foxconn Interconnect Technology, Hyve Solutions, Keysight, Qualcomm Technologies, and Quanta Cloud Technology into the effort.

### Applied Materials: Energy Efficiency Is the Constraint Behind the Constraint

Subi Kengeri, Corporate Vice President and General Manager of Systems to Materials at Applied Materials, used his keynote to set the problem in its largest frame: the binding constraint on AI infrastructure scaling is not compute throughput and is not even interconnect bandwidth in isolation — it is energy efficiency. As rack power densities climb past 100 kilowatts and toward 200-plus kilowatt configurations, the materials and process decisions made at the silicon level ripple directly into data center power budgets that are already constrained by permitting limits, grid capacity, and cooling infrastructure designed for prior generations.

Applied Materials' co-keynote appearance alongside TSMC, Nvidia, and hyperscaler representatives was itself unusual for an OCP event. Its presence reflects how deep upstream the CPO challenge reaches: co-packaged optics is not a software-defined upgrade, nor a module swap at the front of a switch. It is a materials, packaging, and system co-design problem that requires coordinated innovation from the foundry equipment level through the system integration level simultaneously.

### Taiwan's Role: Engineering Partner, Not Just Assembler

A running theme across the two days was Taiwan's position in the emerging CPO supply chain. Shainer has framed Taiwan as more than an assembly hub — as an engineering partner in the development of CPO manufacturing processes. TSMC's COUPE platform and CoWoS-based CPO integration were co-developed with Nvidia over years of bilateral engineering work. ASE's position as a leading OSAT creates decisive leverage in the packaging and test layer.

The worldwide data center infrastructure market grew 28 percent year-over-year to $12 billion in manufacturer revenue in Q1 2026, according to Dell'Oro Group — the fifth consecutive quarter of more than 20 percent growth. Nvidia's CPO switches are in production and available today, validated at 2.6 million hours of mean time between failures per Lightmatter's summary of hyperscale production data. Their 5x power efficiency advantage over pluggable transceivers is confirmed, and their first-adopter roster — CoreWeave, Lambda, Meta, Microsoft, Oracle Cloud Infrastructure — spans both hyperscaler and neocloud categories.

What buyers cannot assume from that milestone is that a competitive multi-vendor CPO market exists. It does not — not yet. Until that gap closes, CPO procurement is effectively single-source procurement, with all the pricing dynamics and dependency risks that implies. The 18-month timeline Bechtolsheim placed on pluggable optics' useful density life gives buyers a practical planning window.
