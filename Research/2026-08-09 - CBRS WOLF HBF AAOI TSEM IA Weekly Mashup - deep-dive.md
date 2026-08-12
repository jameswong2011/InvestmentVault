---
date: 2026-08-09
tags: [research, Semiconductors, AAOI, TSEM, LITE, HBF, CBRS]
sector: Optical Networking & Photonics
ticker: LITE
propagated_to: [CBRS, LITE]
source: 'https://irrationalanalysis.substack.com/p/cbrs-update-wolfnvts-lawsuit-hbf'
source_type: deep-dive
---

## Thesis Delta
Mish-mash weekly: softens prior "HBF never works" to "solution looking for a problem"; flags Cerebras WSE4 as gen-3.5 possibly fixing **parametric** (not just packaging) yield via cleaner power delivery/Vicor; AAOI CPO laser claims lack public linewidth/phase-noise data vs Lumentum/Broadcom duopoly; Tower Openlight + 300mm SiGe expansion bullish for Semtech-class amps; micro-LED dismissed as phase-noise dead-end vs micro-VCSEL. Trading color only — no conviction changes. Touches [[Theses/LITE - Lumentum]], SNDK/HBF watch, TSEM SiPh.

## Summary
**Cerebras:** WSE4 event as gen 3.5 focused on power delivery/clocks; Feldman "doubling clocks" may signal parametric yield fix (voltage domains/ripple) after years of packaging-assumed 20% final yield model; disagg rumors (Trainium progress, Blackwell third-party, MI450 slide allegedly last-minute); interrogation guide for Feldman. **WOLF vs NVTS:** GaN patent suit odd (WOLF sells no GaN; one patent expires ~4m); WOLF SiC patent vs NVTS SiC IA calls "dogshit." **HBF base die:** UCIe options include slow 8G (implies NAND PHY limit); Softens to might-work-not-optimal; prefers fan-out I/O over stacking. **Aeva:** optical connectivity first customer — guess/confirm Innolight; hyperscaler suspected Amazon; SOA/high-power laser shortage → LITE. **Taalas (AMD buy):** burn weights into upper metal masks; ~2–3m model→chip; IA thinks FPGA/embedded more than datacenter AI. **AAOI call:** Sugar Land transceiver ramp is the story; CEO CPO laser focus = cope; demand public linewidth/phase-noise at full power/50C/ELSFP driver; high-power CPO = Broadcom+Lumentum; AAOI 2–3y away. **Tower:** Openlight PDK; dunks GF OCI MSA insertion loss; 300mm SiGe for TIA/drivers → Semtech. **Micro-LED jihad:** Avicina 4G NRZ BER ~1e-7 typical vs 1e-12 no-FEC bar; phase noise fundamental; micro-VCSEL real (Coherent 106G PAM4 demo OK path; Lumentum 32G eyes noisy).

## Evidence
| Item | Figure | Tag |
|---|---|---|
| Cerebras final yield model (IA) | ~20% | [est.: IA prior] |
| HBF UCIe options | includes 8G (slow) | [1×: HBF spec / IA] |
| Aeva first optical customer | Innolight (confirmed to IA) | [1×: IA edit] |
| High-power CPO laser | Broadcom + Lumentum duopoly | [est.: IA] |
| Avicina micro-LED BER | best ~7e-9; typical ~1e-7 @4G | [1×: IA live demo] |
| No-FEC BER bar (IA) | ≤1e-12 all lanes | [est.: IA] |

## Contradiction Check
Challenges SemiAnalysis-adjacent micro-LED optimism; softens own prior HBF dismissal. Supports LITE high-power laser scarcity and Tower SiPh quality vs GF. Falsifiers: AAOI publishes credible linewidth data; Cerebras shows packaging-not-parametric yield; HBF wins hyperscaler capacity-tier sockets.
