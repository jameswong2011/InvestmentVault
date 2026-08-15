---
publish: false
date: 2026-08-12
tags: [research, semiconductors, test, 6857, 000660, BESI]
sector: semiconductors
ticker: 6857
propagated_to: [6857]
source: 'https://semiengineering.com/hbm-becomes-testbed-for-3d-assembly-yield/'
source_type: news
---

# 6857 / 000660 / BESI — HBM as 3D Assembly Yield Testbed

## Thesis Delta
Consensus under-models HBM test-time/DFT step-up; SemiEngineering’s industry survey reinforces [[Theses/6857 - Advantest]] non-consensus that HBM4/HBM5 hybrid-bonding and 24-Hi stacks make **bond/TSV/microbump test** the bottleneck — insertions multiply rather than consolidate — while raising the hybrid-bonding yield bar for [[Theses/000660 - SK Hynix]] and equipment pull for [[Theses/BESI - BE Semiconductor Industries]].

## Summary
HBM5 prep at 24-die stacks; HBM4 advanced flows moving to hybrid bonding. Microbumps <40µm largely unprobeable → BiST, embedded monitors, Kelvin bond metrology, in-system lane repair. Custom HBM base dies blur DFT ownership between SoC and memory vendors (Advantest). Synopsys/Siemens/proteanTecs/Modus describe test-program development and individual-bond visibility as the gating items for yield entitlement and data-center reliability.

## Evidence
| Metric | Figure | Tag |
|---|---|---|
| HBM5 stack height | 24 dies | [web: semiengineering.com] |
| HBM3 reference | 12+ dies | [web: semiengineering.com] |
| Microbump pitch | <40µm (20–25µm bumps) | [web: semiengineering.com] |
| Bonding transition | HBM4 advanced → hybrid bonding | [web: semiengineering.com] |
| Custom HBM | Logic base die option alters DFT | [web: semiengineering.com] |
| Metrology need | Kelvin individual-bond µΩ-range | [1×: Modus Test via SE] |

## Contradiction Check
Directly supports [[Theses/6857 - Advantest]] §Key Non-consensus Insights (HBM4 test-time step-function / DFT expansion) and the HIGH-trigger logic around >14h HBM4 final test — qualitative confirmation, not a stack-time disclosure. Supports BESI hybrid-bonding thread; raises yield execution risk in [[Theses/000660 - SK Hynix]] HBM4E path.

## Source Excerpts
> "Now we are preparing for HBM 5 technology, which will increase that stack height to 24… These tight pitches make the DFT aspects of testing… much more complicated in multi-die technology."
