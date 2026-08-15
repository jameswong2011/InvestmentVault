---
publish: false
date: 2026-08-05
tags: [research, Semiconductors, NVDA, MRVL, SerDes]
sector: Custom Silicon & Networking Semiconductors
ticker: MRVL
propagated_to: [MRVL, NVDA]
source: 'https://nuttycld.substack.com/p/public-serdes-part-1-the-technology'
source_type: deep-dive
---

## Thesis Delta
Consensus equates "optics era" with the death of electrical high-speed design → Nutty (analog IC designer) argues SerDes remains at both ends of every electrical or optical link; CPO/LPO move problems, they do not eliminate DAC/ADC-based serializers, and 224G+ forces chip-package-board co-design. Investing implication deferred to Part 2: identify who monetizes SerDes skill in systems/products/components, not "best SerDes IP" pure-plays. Context for [[Theses/MRVL - Marvell Technology]] optical DSP/SerDes adjacency and [[Theses/NVDA - Nvidia]] networking growth.

## Summary
Bandwidth via parallel wires hits physical limits; SerDes serializes at 112G/224G/lane (PAM4). PAM6/8 raise bits/symbol but erode noise margin (PAM8 needs ~4× SNR of PAM4). LPO removes module DSP and pushes recovery into host SerDes; CPO shortens board copper so a lighter SerDes DSP replaces heavy module DSP (NVIDIA: pluggable ~30W with ~20W DSP vs CPO ~9W). WDM multiplies lanes rather than eliminating SerDes. Talent market: senior/staff/principal SerDes roles; Alphabet-wave style M&A (QCOM/Alphawave) as roster restock. NVIDIA FY26 networking rev +142% vs compute +59%.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| Lane rates | 112G → 224G; 448G in development | [1×: Nutty / industry] |
| Modulation | PAM4 standard; PAM6 probed for 448G | [1×: Nutty / OIF] |
| Copper reach targets | ~2m @112G; ~1m @224G | [1×: OIF via Nutty] |
| Energy | ~0.7 pJ in-package vs ~3.5 pJ ~1m board | [1×: OIF via Nutty] |
| Pluggable vs CPO power | ~30W (20W DSP) vs ~9W | [1×: NVIDIA via Nutty] |
| NVDA networking vs compute growth | +142% vs +59% FY26 | [1×: NVDA AR via Nutty] |

## Contradiction Check
Challenges "CPO kills electrical/SerDes content." Does not by itself pick winners—Part 2 required. Falsifiers: optical I/O eliminates host SerDes earlier than expected; PAM4 hits a wall that freezes lane rates.
