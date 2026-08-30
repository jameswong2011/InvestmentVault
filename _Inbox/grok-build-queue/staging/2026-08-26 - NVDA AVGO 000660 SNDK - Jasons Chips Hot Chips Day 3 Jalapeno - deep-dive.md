---
publish: false
date: 2026-08-26
tags: [research, NVDA, AVGO, 000660, SNDK, Hot-Chips]
sector: Compute & AI Compute Accelerators
ticker: NVDA
source: 'https://www.jasonschips.ai/p/hot-chips-day-3-spicy-jalapeno-chips'
source_type: deep-dive
---

# Hot Chips Day 3 - Spicy (Jalapeno) Chips

## Thesis Delta

Consensus still prices [[Theses/NVDA - Nvidia]] as the general-purpose CUDA platform with Spectrum-X Ethernet already winning scale-out share, prices [[Theses/AVGO - Broadcom]] as the indispensable custom-XPU + Tomahawk networking substrate (OpenAI already counted as an XPU customer; ASIC in-sourcing structurally hard), and prices [[Theses/SNDK - SanDisk]] / [[Theses/285A - Kioxia]] NAND upside mainly through HBF rather than CXL memory-tier attach. Optics names ([[Theses/LITE - Lumentum]], [[Theses/COHR - Coherent]]) are priced for CPO / 1.6T content growth as AI fabrics densify. Jason's free Hot Chips Day 3 note (investor explainer, not a PhD verdict; companion to [[Research/2026-08-24 - 000660 MU SNDK - Hot Chips Day 1 Precious Memories - deep-dive]]) implies a different set of axes for the **whole day**, not a Jalapeño-only clip (those already live as [[Research/2026-08-27 - AVGO NVDA 000660 - OpenAI Jalapeno ASIC Hot Chips - news]] and [[Research/2026-08-28 - AVGO NVDA - OpenAI Jalapeno InferenceX First Results - news]]): **(1)** Spectrum-X multiplane trades reliability and fewer switches (**1.7×** less) for optics TAM on scale-out; CPO on scale-out is a **power** argument, not a reach argument; **(2)** BlueField-4 (Grace + ConnectX-9, **7.2 Tbps**) is the scale-in DPU that offloads networking/storage/security so host CPUs stay on OS/apps; **(3)** Samsung LPDDR5X PIM claims **8×** LPDDR5X bandwidth via bank-local logic, while XCENA MX1 CXL near-memory is separately **NAND-bullish** ("infinite memory"; SSDs as memory, DRAM as cache); **(4)** OpenAI Jalapeño is less "another custom ASIC socket" and more a **process/moat** story (9-month tapeout, small team, ASTRA, new Rust-like hardware language so AIs write correct RTL), with rack math of **128**/rack and **>1 PB** memory BW similar to VR200 NVL72, and a bigger interactivity than throughput gain; Jason closes **long-term bearish any bloated fabless**. Flag only (no conviction/status change): touches NVDA Outstanding Q on hyperscaler-ASIC / CUDA durability and the Groq-inference Q (platform still owns fabric + DPU even as inference ASICs proliferate); touches AVGO Insight #3 (in-sourcing risk overstated) and Insight #4/#5 (Ethernet tip + OpenAI XPU flywheel) via Thor Ultra + Jalapeño process risk; touches SNDK Insight #1 / 000660 Insight #3 only as a **CXL/NAND-tier** companion to the Day-1 HBF realism pass, not as HBF bandwidth news; touches LITE/COHR via the **1.7× fewer switches** optics headwind on multiplane scale-out; touches [[Theses/CBRS - Cerebras Systems]] Insight #3 lightly (CS-6 hybrid-bonded DRAM on SRAM wafer = capacity fix for SRAM-only decode). Does **not** fire NVDA / AVGO / 000660 → HIGH/LOW/CLOSE (no allocation %, ASP, yield, Namics, or registered trigger print). SNDK / LITE / COHR / CBRS have no registered Conviction Triggers section exercised here. MU is a thesis name, not in the live book.

## Summary

Jason (Jason's Chips) covered Hot Chips 2026 Day 3 as a free full post spanning memory-side compute (Samsung LPDDR5X PIM; XCENA MX1 CXL), networking (Broadcom Thor Ultra NIC; NVIDIA BlueField-4 DPU; NVIDIA Spectrum-X multiplane), rack-scale challengers (Cerebras CS-4/CS-6; SambaNova SN50), Google TPU v8, and the closing OpenAI Jalapeño talk. Standing rule from Day 1 carries forward: he is an investor, not a PhD; he will not immediately opine on whether an architecture "works"; companies shill their own stuff. Every load-bearing number below is tagged **[1×: Jason]** unless a slide is clearly the origin.

Memory day-extension, not HBM packaging. Samsung keeps shilling PIM: a small logic block next to each DRAM bank that can support **8×** the bandwidth of LPDDR5X by returning only the data the host needs, usable on server and edge. Jason's take is that Samsung is "really the only ones who can do this and benefit from it." XCENA MX1, jointly presented with Samsung, is CXL computational / near-memory: software sees SSDs as memory, DRAM as cache ("infinite memory"), which Jason reads as **generally very bullish for NAND** because it invites NAND into DRAM's tier by softening latency. MX1 is a RISC-V many-small-core "memory accelerator" fabbed by Samsung; not PIM, but near-memory compute with the same effective-bandwidth pitch. ELI5 in the note: files in the basement; local DRAM = filing cabinet; CXL = slow stairs; MX1 = hire someone who lives in the basement and sends only the answer.

Networking is the Day-3 center of mass for book names. Broadcom Thor Ultra is the Ethernet NIC that lets GPUs talk RDMA-direct to the scale-out fabric (and is where the transceiver plugs in) without bouncing through a host CPU. NVIDIA BlueField-4 is framed as a **datacenter** processing unit: Grace CPU + ConnectX-9 NIC, offloading networking / storage / security so the main CPU keeps OS and apps. Jason's scale taxonomy: scale-up / scale-out / scale-across connect GPUs to each other; **scale-in** (DPUs) connects GPUs to datacenter resources. Differentiator vs traditional cloud DPUs is bandwidth: BlueField-4 at **7.2 Tbps**.

Spectrum-X is NVIDIA's Ethernet scale-out, "way more popular than InfiniBand," built for higher bandwidth and lower jitter, with **1.9×** better multi-tenancy performance when one fabric hosts multiple jobs. CPO on scale-out is not a reach question (scale-out is already optical); it is a **power** question: co-packaging kills the long copper trace to the faceplate and the DSP that would otherwise correct the degraded signal. The architectural headline is multiplane. Traditional scale-out is one port per GPU. A Spectrum-X switch with **64 × 1.6T** ports is **102.4 Tbps** total. The multiplane trick: **512 × 200G** ports across **8 planes**, so each GPU gets access to eight 200G planes instead of one fat port. Claimed effects: much higher reliability, and **1.7× fewer switches**, which Jason flags as **bad for optics**.

Challenger compute is thin on conviction signal. Cerebras announced CS-4 (Jason: "No one cared") and CS-6 with hybrid-bonded DRAM on the SRAM wafer: insane bandwidth, zero capacity today; if thermals and capacity are solved, "they'll be a huge company." SambaNova SN50 is a decode-specialist RDU: decode is the inference bottleneck, HBM BW is the decode bottleneck, and most HBM BW is spent moving neither weights nor KV; SN50 answers with lots of SRAM plus one-kernel / spatial-dataflow tricks. Google TPU v8 splits **8t** (training) and **8i** (inference); inference wants more HBM BW per compute unit because of decode, plus lots of SRAM. Training keeps 3D torus + OCS for bisection; the scale-up all-reduce domain is **9,600** with **2 PB** total memory.

Jalapeño closes the day and is the spicy headline, but this note's job is process/moat + rack context, not a duplicate news clip. Sam Altman / SemiAnalysis framing in Jason's recap: inference chip, better-than-Blackwell chatter, successful tapeout. Load-bearing process facts Jason stresses: taped out in **9 months**, extremely small team, **ASTRA** helped, "no chip design experience," designed around **speculative decode** (cheap draft model predicts ahead; main model checks), built for both prefill and decode and for both throughput and interactivity, with a **much bigger improvement on high interactivity than high throughput**. Rack: **128** Jalapeños with **>1 PB** total memory bandwidth, similar to VR200 NVL72. The smartest move, per Jason, is not the silicon: a new hardware language "kinda similar to Rust" so AIs can write correct RTL out of the box, plus a tiny AI-native team. Long-term read: **pretty bearish any fabless chip designer** that looks like a bloated 2,000-engineer corpo versus a small pilled team with a chip-design harness. Talent today at the giants can be poached.

## Framework / Mental Model

**Scale-up / scale-out / scale-across / scale-in** (Jason paraphrase of the NVIDIA networking day). Re-applicable when mapping which socket owns which hop.

| Axis | Connects | Day-3 exhibit | What changes for the book |
|---|---|---|---|
| Scale-up | GPUs inside a domain (NVLink-class) | (background; CPO power argument shared with scale-out) | CPO content is power-driven once copper+DSP dominate the energy bill |
| Scale-out | Rack/cluster Ethernet fabric | Spectrum-X; multiplane **512×200G / 8 planes** vs **64×1.6T = 102.4 Tbps**; **1.9×** multi-tenancy | Fewer switches (**1.7×**) → optics unit headwind even if BW/GPU holds; Thor Ultra still the NIC/transceiver seat |
| Scale-across | Domain-to-domain / campus | (named, not detailed) | Separate from DPU |
| Scale-in | GPUs ↔ storage / security / infra | BlueField-4 = Grace + ConnectX-9 at **7.2 Tbps** | DPU is infra offload, not a training FLOPS competitor |

**Companion contrast (PIM vs CXL near-memory):**

| Mode | Where compute sits | Bandwidth claim in source | Memory-tier implication |
|---|---|---|---|
| Samsung LPDDR5X PIM | Logic next to each DRAM bank | **8×** LPDDR5X BW by returning only needed data | DRAM product differentiation; Samsung-foundry self-dealing |
| XCENA MX1 CXL | Near-memory accelerator on CXL pool (RISC-V manycore; Samsung-fabbed) | Higher *effective* BW; ELI5 basement worker | NAND invited into memory tier ("infinite memory"); **bullish NAND** [1×: Jason] |

**Companion contrast (Spectrum-X multiplane vs one-port-per-GPU):** same switch BW budget (**102.4 Tbps**), more ports, more planes, higher reliability, **1.7× fewer switches** (optics-negative), multi-tenancy **1.9×**.

**Companion contrast (Jalapeño process moat vs silicon moat):** 9-month tapeout + small team + ASTRA + Rust-like HDL for AI-written RTL is the investor frame; chip claims (speculative decode; interactivity > throughput; 128/rack; >1 PB BW ≈ VR200 NVL72) are the product frame. Prior vault news notes already hold the ASIC/InferenceX facts; this note holds Jason's process/moat and Day-3 networking+memory envelope.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Source type / access | Free full post; audience everyone; author: investor not PhD, companies shill | [web: jasonschips.ai] |
| Conference | Hot Chips 2026 Day 3: PIM, XCENA MX1, Thor Ultra, BlueField-4, Spectrum-X multiplane, Cerebras, SambaNova, TPU v8, Jalapeño | [1×: Jason] |
| Prior Day 1 vault note | Memory day (HBM / PIM / HBF) companion | [[Research/2026-08-24 - 000660 MU SNDK - Hot Chips Day 1 Precious Memories - deep-dive]] |
| Prior Jalapeño news (vault) | ASIC Hot Chips clip; InferenceX first results | [[Research/2026-08-27 - AVGO NVDA 000660 - OpenAI Jalapeno ASIC Hot Chips - news]] [[Research/2026-08-28 - AVGO NVDA - OpenAI Jalapeno InferenceX First Results - news]] |
| Samsung PIM BW | **8×** LPDDR5X bandwidth | [1×: Jason] |
| PIM mechanism | Small logic block next to each DRAM bank; return only needed data; server + edge | [1×: Jason] |
| PIM vendor read (author) | Samsung "really the only ones who can do this and benefit" | [1×: Jason] |
| XCENA MX1 | CXL computational / near-memory; RISC-V many small cores; Samsung-fabbed | [1×: Jason] |
| CXL / NAND (author) | "Generally very bullish for NAND"; SSDs as memory, DRAM as cache; "infinite memory" | [1×: Jason] |
| Thor Ultra | Broadcom Ethernet NIC; RDMA to GPU HBM; transceiver attach | [1×: Jason] |
| BlueField-4 composition | Grace CPU + ConnectX-9 NIC | [1×: Jason] |
| BlueField-4 BW | **7.2 Tbps** | [1×: Jason] |
| DPU job (author) | Offload networking, storage, security; "datacenter processing unit" | [1×: Jason] |
| Scale taxonomy | Scale-up/out/across = GPU↔GPU; scale-in = GPU↔datacenter resources via DPU | [1×: Jason] |
| Spectrum-X role | NVIDIA Ethernet scale-out; higher BW, lower jitter; "way more popular than InfiniBand" | [1×: Jason] |
| Multi-tenancy | **1.9×** better performance when one fabric hosts multiple jobs | [1×: Jason] |
| CPO on scale-out (author) | Already optical; need CPO for **power** (eliminate faceplate copper + DSP) | [1×: Jason] |
| Traditional switch config | **64 × 1.6T** ports = **102.4 Tbps** (Spectrum-X switch) | [1×: Jason] |
| Multiplane config | **512 × 200G** ports; **8 planes**; each GPU gets 8×200G plane access | [1×: Jason] |
| Switch / optics implication | **1.7×** fewer switches; "bad for optics" | [1×: Jason] |
| Cerebras CS-6 | Hybrid-bonded DRAM on SRAM wafer; BW without capacity until solved; thermal caveat | [1×: Jason] |
| SambaNova SN50 | Decode beast; HBM BW bottleneck on non-weight/non-KV traffic; SRAM + spatial dataflow | [1×: Jason] |
| Google TPU v8 | Split **8t** training / **8i** inference; inference needs more HBM BW per compute | [1×: Jason] |
| TPU v8 scale-up domain | **9,600** all-reduce; **2 PB** total memory | [1×: Jason] |
| Jalapeño tapeout | **9 months**; extremely small team; ASTRA assisted; little prior chip-design experience | [1×: Jason] |
| Jalapeño workload | Speculative decode; prefill + decode; throughput + interactivity; bigger interactivity gain | [1×: Jason] |
| Jalapeño rack | **128** / rack; **>1 PB** total memory BW; similar to VR200 NVL72 | [1×: Jason] |
| Jalapeño process moat | New Rust-like hardware language so AIs write correct RTL; tiny AI-native team | [1×: Jason] |
| Fabless long-term (author) | "Pretty bearish any fabless chip designer" / bloated corpo vs small AI-native team | [1×: Jason] |

## Contradiction Check

- **Supports [[Theses/NVDA - Nvidia]] fabric/DPU half; flags the Outstanding Q on hyperscaler-ASIC durability without firing triggers.** Spectrum-X multiplane + BlueField-4 **7.2 Tbps** are platform-deepening on scale-out and scale-in, consistent with Data Center networking as a co-equal vector beside GPUs. Jalapeño (and TPU v8 / SN50 / CS-6) is the other side of the same Outstanding Q: inference ASICs keep landing, and Jason's process story (9-month tapeout, AI-written RTL) is a sharper version of "ASIC complexity is falling" than a single OpenAI socket print. Does **not** answer CUDA inheritance or share-path triggers; does **not** fire → HIGH/LOW/CLOSE. Interactivity-biased Jalapeño gains sit next to the Groq/LPX inference Q already on the thesis, as color, not a close.

- **Challenges the strongest reading of [[Theses/AVGO - Broadcom]] Insight #3 (custom ASIC in-sourcing structurally overstated) and lightly supports Insight #4/#5.** Thor Ultra keeps Broadcom in the NIC/transceiver seat on Ethernet scale-out. OpenAI-as-XPU-customer (Insight #5) is already in the thesis; Day 3 adds Jason's **process** bear on bloated fabless design, which is the in-sourcing / AI-native-team risk Insight #3 says the market overstates. Treat as a **flag on Insight #3 and the "can AVGO sustain 5+ XPU customers" Outstanding Q**, not a customer-loss print. Does **not** fire AVGO conviction moves (no NRR, EU, or $100B AI-revenue falsifier here).

- **Supports [[Theses/SNDK - SanDisk]] / [[Theses/285A - Kioxia]] NAND-tier optionality via CXL, separate from Day-1 HBF realism.** MX1 "infinite memory" / SSD-as-memory is a **utilization and tier** story that Jason explicitly calls NAND-bullish. It does **not** revive Investor Day "near-HBM bandwidth" wording already challenged on Day 1; it is a different attach path (CXL pool + near-memory compute). Touches 000660 Insight #3 (HBF option) only by analogy: memory-tier expansion can be NAND-sided without being HBF. No SNDK Conviction Triggers registered; no 000660 → HIGH/LOW/CLOSE fire.

- **Flags optics unit-growth on [[Theses/LITE - Lumentum]] / [[Theses/COHR - Coherent]] without killing the CPO power thesis.** Multiplane's **1.7× fewer switches** is directly optics-negative on switch-attached modules even while Jason says CPO on scale-out is still needed for **power**. That is a volume-vs-content tension: fewer switch hops, more reason for co-packaged optics on the ports that remain, plus NVIDIA's existing Spectrum-X / CPO lock narrative on LITE. Flag only; no registered LITE/COHR trigger fired.

- **Supports [[Theses/CBRS - Cerebras Systems]] Insight #3 directionally (SRAM-only decode needs a capacity fix):** CS-6 hybrid-bonded DRAM on the SRAM wafer is exactly the capacity leg Jason says would make Cerebras "a huge company" if thermals work. Room reaction ("No one cared" on CS-4) is author color, not a backlog print.

- **[[Theses/MRVL - Marvell Technology]]:** BlueField-4 / Ethernet-attached storage sits near MRVL Insight #2's falsifier language (NVLink + Ethernet-attached NAND + HBF capturing KV-cache sockets). Day 3 is NVIDIA showing the DPU/NIC half of that stack, not a Celestial win/loss. No conviction change.

- Honest low-signal caveat (Jason's own): investor explainer; shill pattern; no ASPs, yields, switch attach rates, Jalapeño foundry node, or OpenAI volume. Prior vault Jalapeño news notes hold the ASIC/InferenceX facts; this note holds Day-3 networking + memory + process/moat as a whole.

## Source Excerpts

> "Samsung will not stop shilling processing in memory (PIM). Honestly very reasonable. They are really the only ones who can do this and benefit from it."

> "It can support 8x the bandwidth of LPDDR5X. If you add processing you can just send only the data that needs to go back to the main processor."

> "Generally very bullish for NAND since it invites it to DRAM's memory tier by solving some of the latency problem."

> "ELI5: files in basement. Local DRAM = filing cabinet. CXL = basement (slow stairs). MX1 = hire someone who lives in the basement, reads the files there, and sends you only the answer."

> "Bluefield 4 is made up of a Grace CPU and a ConnectX-9 NIC. Basically the difference between an AI DPU and traditional cloud DPU is the insane bandwidth. Bluefield 4 has 7.2Tbps."

> "Spectrum-X was specifically designed for this and has 1.9x better performance in multi-tenancy."

> "We know why you need CPO for scale-up. But why do you need it for scale-out? It's already optical. The answer is power."

> "Say you have 64 1.6T ports on your switch for 102.4 Tpbs total bandwidth (which is what Spectrum-X switch actually has). You can do a neat trick where you have 512 200G ports instead and each GPU gets 8 ports or more specifically access to 8 planes of network, each with one port of 200G."

> "Second, you need less switches which is bad for optics. 1.7x less to be precise."

> "They also announced CS-6, which has hybrid-bonded DRAM on the SRAM wafer. If they can solve the thermal issues associated with this and actually get it to work, they'll be a huge company."

> "9,600 all-reduce scale-up domain 2PB total memory as typical of Google."

> "They taped out in 9 months. Apparently an extremely small team too. And one of the first things they said was ASTRA helped them build this thing."

> "Much bigger improvement on high interactivity side rather than high throughput."

> "They have 128 jalapenos in a rack with over 1PB of total memory bandwidth (similar to VR200 NVL72)."

> "But most importantly, they made a new hardware language (!!!) which is kinda similar to Rust so AIs could write correct code out of the box."

> "But over the long term I think this is pretty bearish any fabless chip designer."
