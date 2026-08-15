---
publish: false
date: 2026-07-23
tags: [research, Semiconductors, NVDA]
sector: Semiconductors
ticker: NVDA
propagated_to: [NVDA]
source: 'https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference'
source_type: deep-dive
---

## Thesis Delta
Consensus treats Rubin as a linear GB200 refresh → SemiAnalysis’s Vera Rubin NVL72 vs GB200 NVL72 inference TCO/architecture piece argues the jump is **LUT-based 3-bit tensor-core / SM140 (Feynman) + rack-scale software** that changes perf-per-MW and perf-per-dollar curves, not just TOPs marketing. That supports [[Theses/NVDA - Nvidia]] next-cycle ASP/TCO leadership if public Rubin software (PyTorch, vLLM, OpenAI Triton paths) lands on schedule; challenges bears who model Rubin as a muted upgrade cycle.

## Summary
The deep-dive compares Vera Rubin NVL72 to GB200 NVL72 on inference TCO and architecture: 3-bit Rubin LUT-based tensor cores, SM140 “Feynman,” rack-scale design, and software readiness (public Rubin software, PyTorch, vLLM, OpenAI Triton). Evaluation axes are perf/MW and perf/$ rather than peak FLOPs. SemiAnalysis emphasizes that software maturity will gate whether architectural advantages translate into customer-measured tokens/$—consistent with their InferenceX philosophy. For investors, the note is a checklist for Rubin ramp: silicon features matter only alongside rack-scale networking and a CUDA-ecosystem software drop that customers can actually run.

## Evidence
| Theme | Detail | Tag |
|---|---|---|
| Platforms compared | Vera Rubin NVL72 vs GB200 NVL72 | [1×: SemiAnalysis] |
| Architecture hooks | 3-bit LUT tensor core; SM140 Feynman; rack scale | [1×: SemiAnalysis] |
| Economic axes | perf per MW; perf per dollar | [1×: SemiAnalysis] |
| Software surface | public Rubin software; PyTorch; vLLM; OpenAI Triton | [1×: SemiAnalysis] |
| Analytical goal | inference TCO & architecture | [1×: SemiAnalysis] |

## Contradiction Check
Supports NVDA generational pricing power if Rubin delivers on perf/MW. Challenges “CUDA moat irrelevant if ASIC wins” only insofar as Rubin software ships broadly—monitor InferenceX Rubin submissions Nvidia committed to.

## Source Excerpts
> Email framing: "3 bit Rubin LUT Based Tensor Core, SM140 Feynman, Rack Scale, Perf Per MegaWatt, Perf Per Dollar, Software Improvements"

