---
date: 2026-07-27
tags: [research, Semiconductors, FORM, Optics, CPO]
sector: Semiconductor Equipment
ticker: FORM
propagated_to: [FORM]
source: 'https://tspasemiconductor.substack.com/p/cpos-biggest-bottleneck-is-not-opticsit'
source_type: deep-dive
---

## Thesis Delta
Consensus frames CPO readiness as laser/PIC/packaging → SemiVision/TSPA (Advantest SEMICON Taiwan framing) argues HVM electro-optical test is the binding industrialization constraint: Known Good Optical Engine before SoC attach, shift-left insertions (PIC wafer → EIC-PIC → optical engine → package), and three gaps—optical probing standards, fiber-connector handling, rack-and-stack instrumentation. 12-inch PIC wafer test can take up to 12 hours. Investing implication: test/prober/handler/FAU ecosystem (and Taiwan's electrical-ATE strength) becomes yield-engineering, not back-end commodity.

## Summary
AI fabrics push optics from rack edge into packages/xPU scale-up. Lab-proven SiPh ≠ millions of hybrid devices on a line. Advantest stages: wafer PIC, wafer EIC-PIC, singulated optical engine, then advanced ASIC/CPO final/SLT—goal is KGOE before expensive packaging (CoWoS/EMIB/3D). Gaps: no true optical-probe standard (active multi-axis alignment; passive explored); fiber-connector handling still manual; optical instruments custom rack-and-stack with calibration error dominating DUT error. Direction: Automation/Collaboration/Innovation/Standardization—standard electrical probers/handlers + high-density optical instruments as one test cell. DfT must grow optical loopback, monitor PDs, thermal sense. Commercialization pace = f(yield, test time, test cost). Adjacent: 448G/lane and TE Connectivity mentioned as signal-chain context.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| PIC 12-inch wafer test time | up to 12 hours (PIC portion) | [1×: SemiVision / TSPA] |
| Test insertions | PIC WL → EIC-PIC WL → engine → package/SLT | [1×: Advantest via TSPA] |
| Three gaps | probing / connector handling / instrumentation | [1×: Advantest via TSPA] |
| Packaging cost of late optical fail | entire high-value xPU package | [1×: TSPA] |

## Contradiction Check
Extends optics scarcity thesis from lasers/InP into test CapEx and standards. Watch FORM/Advantest/ATE names and FAU alignment tooling. Falsifiers: passive optical probe + standardized FAU sockets arrive fast; hyperscalers accept lower outgoing quality with system-level screen; CPO volumes stay niche.
