---
title: "HBM Density Peak: Why AI Value Is Moving From Memory to Connectivity"
source: Damnang
url: "https://damnang2.substack.com/p/hbm-density-peak-why-ai-value-is"
date: 2026-08-20
publication: Damnang
gmail_id: 1a02017d034c2aaa
tags: [research, email-backfill, Damnang, 000660, NVDA, MRVL, SNDK, HBM, CPO, CXL, optics]
source_type: web-clip
sender: damnang2@substack.com
gmail_full: true
---
# HBM Density Peak: Why AI Value Is Moving From Memory to Connectivity

**Pub:** Damnang
**URL:** https://damnang2.substack.com/p/hbm-density-peak-why-ai-value-is
**Date:** 2026-08-20
**Sender:** damnang2@substack.com
**Gmail id:** 1a02017d034c2aaa
**Email timestamp (Gmail):** 2026-08-20T16:53:33Z (2026-08-21 00:53 SGT)
**Subtitle:** Rubin Ultra’s lower HBM stack count, SK hynix’s CPO review paper and Marvell’s optical portfolio read as one shift in where system budget goes
**Note:** Full subscriber Gmail body (`messageFormat: PLAIN_TEXT`). User is a subscriber. Substack tracking pixels stripped. Repeated "reader-supported publication" CTAs collapsed. Image-only figures (NPO vs CPO energy/bandwidth-density table; Nature Electronics Fig. 4 XPU/memory-pool drawing; Fig. 4c MCM cross-section) are described in the text, not transcribed as a BOM. Unsubscribe chrome omitted.

## ARTICLE TAKEAWAYS

Rubin Ultra HBM is being reviewed downward from HBM4E 12-Hi toward HBM4 8-Hi 192GB (SemiAnalysis main SKU; The Information 192GB and 256GB prototypes; TrendForce Aug 4: several lower-capacity configs under evaluation, final spec unset). Supply through 2027 plus HBM4E qualification uncertainty and 12-Hi stacking cost are the direct cause. The choice is workable because NVL576 (eight 72-GPU racks → 576-GPU NVLink domain with direct optical rack-to-rack links) plus software tiering absorb lost per-GPU capacity. Local HBM stays fastest: ~21–22TB/s vs NVLink 6 ~3.6TB/s GPU-to-GPU. Peer HBM does not replace local HBM.

That direction leads to optics (NPO → CPO → photonic interposer) and memory disaggregation. A Nature Electronics review published 20 August 2026 lists an SK hynix researcher as corresponding author (Kim, B. et al., *Co-packaged optics for high-performance computing and artificial intelligence*). Compute throughput has tripled roughly every two years; interconnect bandwidth advanced only about 1.4-fold over the same cycle. Marvell co-develops NVLink Fusion scale-up networking and silicon photonics with NVIDIA (NVIDIA invested $2B, announced Mar 31 2026) and CXL-based CMM-Ax with SK hynix (Marvell Structera A + SK hynix DRAM/software, disclosed Aug 5 2026). At FMS August, Marvell disclosed Photonic Fabric (Celestial AI, acquisition completed Feb 2 2026) targeting a shared warm KV cache tier of up to 32TB over an optical fabric within 50m, with 2 to 3x token throughput as vendor targets — not commercial-deployment figures. Photonic Fabric Module: 2.5D, ASIC + HBM cache + DDR5 on an active photonic interposer; up to eight DDR5 DIMMs, 72GB of HBM cache, 7.2Tbps of optical bandwidth.

HBM implications if 8-Hi is confirmed: mix-down in HBM content per GPU, but not a 1:1 revenue decline. Stacking time up to 1.5x and stack yield 1.084x under a 98% per-core-die yield assumption multiply to an effective output ceiling of about 1.63x. If NVIDIA absorbs that volume into additional GPU shipments, total HBM revenue lands at about 81.5% of plan if 8-Hi is priced at 50% of planned HBM4E, and about 98% at 60%. Sensitivities, not shipment forecasts. Competitive axis: if 8-Hi life extends, yield, capacity, supply stability and base-die functionality outweigh 12-Hi/16-Hi stack-height qualification premium.

Disclaimer in source: 8-Hi for Rubin Ultra is unconfirmed industry-check information; yield and revenue figures are scenario sensitivities, not company guidance.

---

Rubin Ultra’s HBM configuration is being reviewed downward, from HBM4E 12-Hi toward HBM4 8-Hi. Supply constraint is the direct cause, but supply alone does not make the choice work. It works because a wider scale-up domain and software tiering absorb the loss of per-GPU memory capacity at the system level.
That direction leads to optics and memory disaggregation. A Nature Electronics review published on August 20 lists an SK hynix researcher as a corresponding author. Marvell is co-developing scale-up networking and silicon photonics with NVIDIA, and CXL-based CMM-Ax with SK hynix.
This piece connects those three threads as one system architecture change.
Disclaimer This article is written for informational purposes and does not recommend buying or selling any security. The 8-Hi configuration for Rubin Ultra is unconfirmed information based on industry checks, and the final specification may change. The yield and revenue figures in this article are scenario sensitivities, not company guidance or shipment forecasts.

## 1. The stack count fell because the GPU domain grew

On August 4, TrendForce said NVIDIA is evaluating several lower-capacity configurations alongside 12-Hi HBM4E and that the final specification has not been set. The Information reported prototype testing of 192GB and 256GB configurations, and SemiAnalysis sees the main SKU moving down to HBM4 8-Hi 192GB while compute performance holds and memory bandwidth rises slightly.

As someone who has covered this issue before, what I hear from the field is that the major memory makers are now running daily meetings with the customer on the basis of HBM4 8-Hi as the main Rubin Ultra configuration and are entering spec decisions on that footing. Some sources mention a 4-Hi configuration, but there is no verifiable basis for it, so it is not treated here.

All of this points to one thing.

On Rubin Ultra, pushing HBM density as high as it will go is no longer the only path to system optimization.

Why is this happening?

The first reason for the spec change is supply.

DRAM is likely to stay tight through 2027, and HBM4E still carries schedule uncertainty in qualification at the performance level NVIDIA is asking for. Twelve-layer stacking also costs more in throughput and yield than eight.

The second is system structure.

The field view is that on Rubin Ultra, bandwidth and data movement are becoming a larger constraint than memory density. In other words, the system has entered a regime where improving how data moves contributes more to performance than adding capacity.

Package-level constraints compound this.

Adding HBM stacks around the GPU raises package area and interposer-edge I/O cost. Raising the layer count inside the same stack instead increases stacking process complexity, yield loss, thermal load and package complexity. The higher HBM density goes, the more the system has to pay for each additional unit of capacity.

A wider scale-up domain, by contrast, lets some of that capacity move to peer HBM and to memory tiers outside the package. Where the gap narrows between the value of additional local capacity and the package cost of obtaining it, improving data movement can serve system efficiency better than pushing memory density further.

8-Hi is a response to supply constraint. What makes it workable is a system structure that leans on scale-up bandwidth and memory placement instead of pushing local memory density higher.

The software and memory placement techniques that keep performance intact at HBM4 8-Hi 192GB were covered separately in “What Does Rubin Ultra’s 8-Hi HBM Mean?” on August 10. Details are here.

I see two changes following from this. Optics widens the physical reach of the NVLink domain, and memory disaggregation narrows the range of memory capacity that must sit inside the GPU package.

SK hynix and NVIDIA each gave their own reasons for the CPO paper and for the $2B investment in Marvell. The public statements from NVIDIA and Marvell cite NVLink Fusion, custom XPU, scale-up networking and silicon photonics.

What I do is read both moves as signals from the same system-level data movement problem. NVIDIA, SK hynix and Marvell: the sections below look at the picture the three are drawing, and at what this change could mean for memory makers and for HBM.

## 2. From NPO to CPO: optics moves from rack-to-rack links toward package I/O

The difference between NPO and CPO is how close the optical engine sits to the ASIC. NPO keeps the optical engine outside the XPU or switch package but places it as close as possible on the board. Marvell cites the advantage that optics can be adopted without redesigning the XPU package.

CPO puts the photonic die and the electronic die inside the same package or interposer. That shortens the distance high-speed electrical signals travel outside the package, which helps bandwidth density and energy efficiency, but it raises the burden of thermal management, optical alignment, package yield and reliability.

SemiAnalysis reads the optical technology used in Rubin Ultra NVL576 as an NPO structure, and my previous article was written on that basis. Public disclosure and industry reporting should be separated here, though. NVIDIA has disclosed that NVL576 binds eight racks of 72 GPUs into a single 576-GPU NVLink domain and uses direct optical connections between racks.

NVIDIA’s public technical material does not state whether the packaging topology of that optical link is NPO or CPO.

What it does provide is the technical basis for why optical I/O has to move closer to the package after NPO, and how the next step leads to CPO and the photonic interposer.

For a detailed discussion of the technological evolution and market dynamics of NPO and CPO, please refer to the article below.

The Nature Electronics review with an SK hynix corresponding author sets out the physical background of this shift. In the paper, compute throughput has tripled roughly every two years, while over the same two-year cycle interconnect bandwidth advanced only about 1.4-fold. Even when HBM lifts bandwidth inside the package, resistive loss and capacitive loading on copper traces grow again once data crosses the board and cables. At high rates, equalization, retimers, DSP and FEC correct for that while adding power and latency.

The integration roadmap in the paper points the same way. From pluggable and on-board optics through 2.5D CPO, 3D TSV, hybrid bonding and monolithic integration, the optical conversion point moves closer to compute at each step. 2.5D is the compromise between manufacturability and performance, while 3D delivers higher bandwidth density and lower energy per bit at the cost of thermal and bonding yield.

On that reading, the NPO reported for NVL576 is better understood as an intermediate step that lowers package redesign and serviceability burden, rather than the end of the optical transition. The move to CPO gains economic footing as bandwidth density and I/O power become the binding constraints.

The energy and bandwidth density figures are the representative values the paper gives for each integration method. The pluggable column is on a transceiver basis.

The significance of this paper is that a technical review with a memory maker involved extends the AI system bottleneck from HBM bandwidth itself to data movement between compute and memory, and sets out a direction that pulls optical I/O closer to the package.

It is also the reason raising local HBM density and improving the interconnect are now compared inside the same system budget.

I read this as the key technical inflection in the memory and optics roadmap that SK hynix, Marvell and NVIDIA are drawing.

## 3. Disaggregation: extending local HBM capacity into a system memory domain

Local HBM remains the fastest memory tier. On the field checks used in my earlier work, Rubin’s local HBM bandwidth is about 21 to 22TB/s, while NVLink 6 delivers roughly 3.6TB/s of GPU-to-GPU bandwidth per GPU. Another GPU’s HBM does not replace local HBM. What changes is how much of the weights and KV cache must sit in one GPU’s HBM.

NVL576 implements that change inside the scale-up domain first. Active weights and hot KV stay in local HBM, while distributable weights and KV spread to peer HBM. Software hides remote memory latency by prefetching what is needed or by sending the token to the GPU that holds the data. One step further and capacity itself moves outside the GPU package, which is memory disaggregation.

This is not a structure that removes local HBM. Latency-sensitive data stays in HBM, and only data that needs capacity and reach moves to a larger memory tier.

The long-term structure in the Nature Electronics review takes this further. Fig. 4 shows XPU pool and memory pool separated and linked by a photonic interposer. The paper does not treat this as a finished architecture. It names an optical memory interface that preserves coherence while lowering latency, low-power photonic switching and multi-hop signal regeneration as problems still to be solved. The drawing is therefore a research direction for the optical architecture that separating memory and compute would require, not an SK hynix commercial product roadmap.

XPU pool and memory pool are separated and linked by a photonic interposer and optical fibre. This is the long-term direction the paper sets out, not a commercial product roadmap.

SK hynix’s shipping products move on electrical disaggregation first. CXL pooled memory lets multiple hosts share memory, and CMM-Ax attaches compute to CXL memory so that long-context inference can handle a KV cache larger than GPU HBM. Disclosed in August 2026, CMM-Ax is a co-developed product combining Marvell Structera A with SK hynix DRAM and software stack. The actual link between SK hynix and Marvell shows up first in the CXL memory tier, not in optical memory.

This widens the scope of SK hynix’s business from the DRAM die itself to a broader memory architecture. HBM and custom base die sit in the local fast tier, CXL and CMM-Ax in the external capacity tier, and the photonic memory pool in the paper in a longer-dated optical tier.

Disclosed products and one paper are not enough to confirm a transition into a system-level memory vendor, but the direction is visible: the scope that has to be co-designed with the customer widens from the memory die to the controller, base die, packaging and memory placement. If that structure does reach commercial deployment, the value-added and customer stickiness SK hynix captures could exceed what selling bits alone provides.

Marvell is extending its portfolio into the next layer. It secured Photonic Fabric through the Celestial AI acquisition in February 2026, and at FMS in August it disclosed a structure in which multiple XPUs and racks reach a shared warm KV cache tier of up to 32TB over an optical fabric within 50m. The 32TB, the 50m and the 2 to 3x token throughput are vendor targets set by Marvell. They are not figures that indicate commercial deployment.

What deserves attention here is that the optical structure Marvell presents and the drawings in this Nature Electronics review share the same layer structure.

Fig. 4c of the paper shows a multi-chip module cross-section with ASIC, CPU, HPU and HBM chiplets placed together on a photonic interposer with embedded optical waveguides.

The Photonic Fabric Module Marvell obtained through the Celestial AI acquisition is a 2.5D package that places an ASIC, HBM cache and DDR5 channels together on an active photonic interposer.

On Marvell’s disclosed specification it supports up to eight DDR5 DIMMs, 72GB of HBM cache and 7.2Tbps of optical bandwidth. If Fig. 4b of the paper is a structure that links XPU pool and memory pool through a photonic interposer, Marvell’s memory module and PF-NIC configuration is closer to an implementation of that structure at module level, arriving first.

The problem definitions overlap as well.

The paper points to I/O density at the die periphery limiting channel count and routing flexibility in 2D configurations, and in Fig. 4d it sets out vertical connection between stacked PIC and EIC through optical TSVs. Marvell instead takes optical I/O out from the middle of the die rather than the die edge. The implementation differs, the constraint being solved is the same.

That similarity is an observation at the structural level. The inclusion of Celestial AI’s Photonic Fabric in the paper’s table of industrial platforms is verifiable, but there is no announcement that SK hynix and Marvell are co-developing in the optical memory space. The confirmed contact points between the two remain custom HBM and CMM-Ax. Sharing a structure and having a joint product are two different things.

In parallel, NVIDIA and Marvell announced co-development of NVLink Fusion compatible scale-up networking and silicon photonics in March 2026, and NVIDIA invested $2B in Marvell. Marvell sits at the point where optical I/O for XPU scale-up and CXL-based memory disaggregation meet.

NVIDIA offsets local HBM density with system-level scale-up, SK hynix extends the memory tier outside HBM, and Marvell supplies the electrical and optical interconnect both structures require. The link between the three companies is built out of that division of roles. Moving right, verifiable evidence thins out and the content moves closer to a research direction.

## 4. HBM implications: bandwidth, yield and memory hierarchy matter more than stack height

If the 8-Hi transition is confirmed as the final specification, HBM capacity per GPU clearly falls.

Against the same GPU shipment volume, that is a mix down in HBM content. Under the current supply constraint, though, the per-GPU bit decline cannot be applied directly as a decline in HBM market revenue. Lowering stack height raises the number of stacks that can be built from the same DRAM and stacking capacity, and NVIDIA can absorb that into additional GPU shipments.

HBM does not lose its role. Local HBM stays the fastest tier, and part of the additional capacity spreads into peer HBM, CXL memory and optical shared memory.

In the sensitivity used in my earlier work, moving from 12-Hi to 8-Hi gives up to a 1.5x effect from stacking time and a 1.084x improvement in stack yield under a 98% per-core-die yield assumption.

Multiplying the two puts the effective output ceiling at about 1.63x. Assuming all of that volume is absorbed into additional NVIDIA GPU shipments, total HBM revenue lands at about 81.5% of plan if 8-Hi is priced at 50% of the planned HBM4E, and about 98% at 60%. These are sensitivities to stack count, not shipment forecasts.

The competitive variables change too. In the regime where 12-Hi and 16-Hi stack height was itself the axis of differentiation, high-stack qualification and stacking technology carried a large premium. If the life of 8-Hi extends, yield, capacity, supply stability and base die functionality carry more weight. SK hynix expanding custom base die and a CXL-based memory tier together sits against the same change.

For Marvell the read-through runs the other way. Keeping accelerator utilization intact while lowering local HBM capacity raises the importance of scale-up bandwidth, optical reach and external memory tiers. That is why NVLink Fusion and silicon photonics work with NVIDIA, CMM-Ax with SK hynix, and Photonic Fabric through the Celestial AI acquisition connect inside one portfolio.

As optics moves closer to compute, from pluggable through NPO, CPO and the photonic interposer, supply chain value moves with it. Volume growth in optical engines and laser sources comes first, and silicon photonics PICs, drivers and TIAs, fiber coupling, 2.5D interposers and 3D bonding gain weight after that. If CPO and optical memory reach high-volume production, the beneficiary set is not limited to light source makers but widens across photonics and advanced packaging.

This is why I keep calling for a second round in optical investing, and why I keep saying that the start of the optical theme is the reason the memory theme is running. My belief is that only by following this technology and market shift can you hold real conviction and a real thesis in semiconductor, memory and optical investing from here.

I will keep publishing analysis and articles at this level, and I am open to collaboration proposals around that work. Any form of collaboration is welcome. Please reach me at damnang2.official@gmail.com.

## Sources and verification

TrendForce, reporting on Rubin Ultra HBM configuration review, Aug. 4, 2026. Confirms evaluation of multiple configurations including 8-Hi HBM4E, 12-Hi HBM4 and 8-Hi HBM4 alongside 12-Hi HBM4E, and that the final spec is unset.

The Information, reporting on lower-capacity Rubin Ultra prototypes, 2026. Confirms prototype testing of 192GB and 256GB configurations.

SemiAnalysis, Vera Rubin analysis, 2026. Confirms the main configuration moving to HBM4 8-Hi 192GB with compute held and memory bandwidth slightly higher, and the view on the rack-to-rack optical link.

Damnang Research, What Does Rubin Ultra’s 8-Hi HBM Mean?, Aug. 10, 2026. Basis for the Section 1 field checks, the NVL576 and NPO structure, the software hierarchy and the HBM revenue sensitivity.

Kim, B. et al., Co-packaged optics for high-performance computing and artificial intelligence, Nature Electronics (2026). Basis for electrical interconnect limits, the CPO integration hierarchy, and the photonic interposer and XPU/memory pool architecture.

NVIDIA, “NVIDIA Vera Rubin POD: Seven Chips, Five Rack-Scale Systems, One AI Supercomputer,” 2026. Confirms the 8-rack, 576-GPU NVLink domain and the direct optical rack-to-rack connection in NVL576.

Marvell, “Scale-up Network Solutions for AI Infrastructure,” 2026. Confirms NPO and CPO product positioning and packaging differences.

Marvell, “The Evolution of AI Interconnects.” Describes the architecture in which the optical engine moves closer to the XPU from NPO to CPO.

NVIDIA, “NVIDIA AI Ecosystem Expands as Marvell Joins Forces Through NVLink Fusion,” Mar. 31, 2026. Confirms Marvell’s NVLink Fusion compatible scale-up networking, the silicon photonics collaboration and NVIDIA’s $2B investment.

Marvell / SK hynix, “Accelerating AI Infrastructure with Marvell Structera A and SK hynix CXL Memory,” Aug. 5, 2026. Confirms CMM-Ax co-development and the CXL-PNM structure.

Marvell, “Marvell Advances AI Memory Infrastructure Portfolio to Accelerate Agentic AI Inference,” Aug. 4, 2026. Confirms the 32TB, 50m and 2 to 3x token throughput vendor targets for the Photonic Fabric shared-memory tier.

Marvell, “Marvell Completes Acquisition of Celestial AI,” Feb. 2, 2026. Confirms completion of the Photonic Fabric acquisition.
