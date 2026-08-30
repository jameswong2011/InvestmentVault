---
publish: false
date: 2026-08-29
tags: [research, daily-intel-triage, news, NVDA, 000660]
sector: DRAM & HBM
ticker: NVDA
source: 'https://sammyfans.com/2026/08/28/samsung-develops-8-layer-hbm4e-for-nvidia-nvhbm'
propagated_to: [NVDA, 000660]
source_type: news
---

# Samsung Building 8-Layer HBM4E for Nvidia NVHBM (SEDaily via SammyFans)

## Thesis Delta
Consensus still models NVHBM as taller stacks plus a custom base die, and prices the HBM race as a 12-Hi / 16-Hi qualification contest. SEDaily (28 August 2026, relayed by SammyFans) says Nvidia asked Samsung for 8-Hi HBM4E at 17–18 Gbps/pin instead of the 12-/16-Hi stacks Samsung had been preparing, trading height for shippable bits, thermals, and pin speed. SammyFans' controller-in-base-die NVHBM claims remain ~30% bandwidth / ~15% power versus commodity HBM4E. For held [[Theses/000660 - SK Hynix]] this is a mix-shift / competitive signal on Insight #1 (Samsung dual-source recovery) and Insight #2 (8-Hi mix already flagged by Damnang), not a Rubin-share print and not a LOW-trigger fire (Samsung >35% of first two Rubin quarters). For [[Theses/NVDA - Nvidia]] it reinforces the NVLink Fusion custom-memory control already logged from the Converge Digest / Nvidia blog notes. Single-source Korean trade press (Lee Suk-jin, AI-translated); treat as unverified until SK Hynix or Samsung primaries. No conviction or status change.

## Summary
SammyFans (28 August 2026) relays Seoul Economic Daily: industry sources said on the 28th that Nvidia asked Samsung Electronics to tailor seventh-generation HBM4E around an 8-layer stack for NVHBM rather than the taller 12-layer and 16-layer configurations the company had been preparing. The relay's pin-speed ask is 17–18 Gbps versus Samsung's initial HBM4E sample specification of 16 Gbps; SEDaily's own English text instead puts the sample baseline at 14.4 Gbps and calls 17–18 Gbps 'about 20% higher', so the 16 Gbps figure is a SammyFans paraphrase that does not match the cited original and should not be collapsed into one number. Nvidia officially introduced NVHBM this week as part of NVLink Fusion (SEDaily: the NVLink standard was unveiled a day earlier); SammyFans says the company is taking a different route, prioritising speed, physical efficiency, and supply scalability.

SEDaily's mechanism, which the SammyFans clip compresses away, is that the historical HBM formula raised capacity by stacking 4-Hi to 8-Hi to 12-Hi, and that taller stacks force thinner DRAM dies and more precise stacking, raising back-end processing difficulty and yield burdens. An 8-layer design lowers those manufacturing burdens and makes larger HBM volumes easier to supply; the piece reads the ask as Nvidia trying to break through a memory shortage rather than maximise bits per stack. Rubin Ultra (reportedly the first application, due next year) expands GPU-to-GPU connections eightfold, from 72 to as many as 576, so even if memory capacity per GPU falls as stack counts are cut, cluster compute can still rise by linking hundreds of GPUs that each carry faster HBM. NVHBM (SammyFans, matching the prior Converge Digest / Nvidia blog) moves the memory controller into the HBM base die, freeing XPU area and claiming up to ~30% higher bandwidth and ~15% lower HBM power versus standard HBM4E.

Samsung's claimed fit is the integrated DRAM / logic / packaging / foundry stack: SEDaily says NVHBM requires not only DRAM but the ability to design and produce logic-based base dies, and that Samsung can handle that work end to end, which the paper ranks as more competitive than SK hynix (000660.KS) or Micron in the custom-HBM market. An unnamed industry official is quoted (via Korean, then AI-translated): 'Samsung proved industry-leading speed with HBM4, so it can play to its strengths in a speed competition rather than in high stacking.' That is a supplier-path claim, not a socket award.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Date / byline | 28 Aug 2026; Lee Suk-jin (SEDaily), relayed by SammyFans | [1×: sammyfans.com / en.sedaily.com] |
| Stack height ask | 8-Hi HBM4E for NVHBM (not 12/16-Hi Samsung had prepared) | [1×: SEDaily via sammyfans.com] |
| Pin speed ask | 17–18 Gbps/pin | [1×: SEDaily via sammyfans.com] |
| Sample baseline (SammyFans) | 16 Gbps | [1×: sammyfans.com] |
| Sample baseline (SEDaily original) | 14.4 Gbps; 17–18 described as ~20% higher | [1×: en.sedaily.com] |
| NVHBM claims | ~+30% BW / ~−15% HBM power vs HBM4E | [1×: sammyfans.com] |
| Controller location | Memory controller into HBM base die; frees XPU area | [1×: sammyfans.com] |
| Rubin Ultra scale | GPU-to-GPU links 72 → as many as 576 (8×); first likely NVHBM application, due next year | [1×: en.sedaily.com] |
| Mechanism | Taller stacks thin dies + raise yield burden; 8-Hi eases volume / shortage | [1×: en.sedaily.com] |
| Custom-HBM ranking | Samsung end-to-end DRAM + logic base die vs SK Hynix / Micron | [1×: en.sedaily.com] |
| Platforms named | Vera Rubin Ultra (reportedly) | [1×: sammyfans.com] |
| Source quality | Secondary (SEDaily → SammyFans); AI-translated Korean | [est.] |

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] NVLink Fusion / custom-memory control (the 27–28 August Converge Digest and Nvidia-blog notes already have the controller-in-base-die claim and Annapurna as first collaborator); this adds a named Samsung 8-Hi / 17–18 Gbps ask and a cluster-scale rationale (NVL72 → NVL576) without a primary confirmation. **Competitive pressure, or industry-wide 8-Hi validation,** on [[Theses/000660 - SK Hynix]] Insight #1 (Samsung dual-source recovery) and Insight #2 (architecture wins; Damnang already had Rubin Ultra moving toward HBM4 8-Hi 192GB with NVL576 absorbing lost per-GPU capacity) and Outstanding Q1 (Samsung's Rubin allocation), not a shipment print. LOW (Samsung >35% of first two Rubin quarters) stays unfired: an unverified request to tailor 8-Hi NVHBM is not an allocation disclosure. Mental-model lenses in play: Semiconductors #8 (architecture remap from stack height to pin speed + supply), #1 (HBM shortage as the bottleneck Nvidia is trying to break), #2 / #10 (custom logic base die + Nvidia as the anchor). Single-source trade press. No conviction or status change.

## Source Excerpts
> "NVIDIA has asked Samsung to tailor its seventh-generation HBM4E around an 8-layer configuration for NVHBM, rather than the taller 12-layer and 16-layer stacks" [1×: SEDaily via sammyfans.com]

> "target speeds of 17 to 18Gbps per pin… above Samsung's initial HBM4E sample specification of 16Gbps." [1×: sammyfans.com]

> "Nvidia has also set a speed specification of 17 to 18 gigabits per second for Samsung, about 20% higher than the 14.4 Gbps of Samsung's initial HBM4E samples." [1×: en.sedaily.com]

> "Rubin Ultra expands the scale of GPU-to-GPU connections eightfold, from 72 to as many as 576." [1×: en.sedaily.com]

> "Samsung proved industry-leading speed with HBM4, so it can play to its strengths in a speed competition rather than in high stacking." [1×: en.sedaily.com]
