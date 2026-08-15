---
publish: false
date: 2026-08-14
tags: [research, daily-intel-triage, news, NVDA]
sector: Compute & AI Compute Accelerators
ticker: NVDA
propagated_to: [NVDA]
source: 'https://wccftech.com/nvidia-800-vdc-platforms-break-past-traditional-power-distros-to-scale-up-performance/'
source_type: news
---

# Nvidia 800 VDC OCP With Microsoft, Google and 80 Firms; Rubin MGX Production 2H26

## Thesis Delta
Consensus already knows [[Theses/NVDA - Nvidia]] is pushing 800 VDC (vault macro [[Macro & Technology/800VDC Adoption]]) — this 13 August 2026 Wccftech piece restates the OCP architecture with Microsoft and Google plus “more than 80” ecosystem firms, DSX reference designs for “fully native 800 VDC,” Rubin MGX racks “already in production” for 2H 2026 (Taiwan industry sources), incremental adopt-on-AC path, and a 2027 “row power center” overhead 800 VDC busway up to 2 MW/row scaling to Rubin Ultra / Feynman on Kyber. NVDA has no formal Conviction Triggers section (gap). Hypothesis: this is ecosystem-standardization and rack-power-path confirmation, not a new demand print; it supports the DSX / AI-factory lock-in already in the Omniverse/GTC spine.

## Summary
Hassan Mujtaba: AC conversion stages waste power as rack density rises; 800 VDC cuts stages between grid and GPU. NVIDIA, Microsoft, and Google are developing the first 800 VDC architecture via OCP; 80 equipment firms are building to the spec for 2H 2026 platforms. Vladimir Troy (NVDA VP data-center infrastructure): “800 VDC unlocks the compute performance and power density required for AI at scale… a practical path forward — not just a future vision.” IEA: data-center electricity +17% in 2025, AI half of that; global consumption ~950 TWh by 2030; Wood Mackenzie $9T AI/data infrastructure through 2040.

Rubin MGX on 800 VDC is “already in production” for 2H 2026 per Taiwan sources — customers can drop DC racks onto existing AC sites incrementally. A comparison table (fault current, arc flash, protection devices) flags DC as harder to interrupt and more severe on arc/shock — the adoption cost is protection engineering, not just busbars. 2027 row-power center: centralized row station, overhead 800 VDC busway, up to 2 MW per row, path to Kyber / Rubin Ultra / Feynman.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Standard | 800 VDC via OCP; MSFT + GOOGL | [1×: Wccftech 2026-08-13] |
| Ecosystem | >80 equipment/infrastructure firms | [1×: NVDA via Wccftech] |
| First platforms | 2H 2026 | [1×: Wccftech] |
| Rubin MGX | 800 VDC; in production; roll-out 2H 2026 | [1×: Taiwan sources via Wccftech] |
| Adopt path | incremental on existing AC; no major rip-and-replace | [1×: Wccftech] |
| Row power center | 2027; overhead 800 VDC busway; up to 2 MW/row | [1×: Wccftech] |
| Next racks | Rubin Ultra + Feynman on Kyber “next year” | [1×: Wccftech] |
| IEA | DC electricity +17% in 2025; AI 50%; ~950 TWh by 2030 | [1×: IEA via Wccftech] |
| Capex cite | $9T through 2040 | [1×: Wood Mackenzie via Wccftech] |
| Quote | Vladimir Troy, VP DC infrastructure | [1×: NVDA via Wccftech] |

The source’s AC-vs-DC hazard table is the adoption-cost qualifier: DC fault current is high and sustained (no zero crossing), interruption needs specialized breakers, ground-fault detection is harder, and series/parallel arcing persists. That is why the “drop MGX onto existing AC” path still requires a protection-device refresh even when the busway is incremental.

## Contradiction Check
**Supports** [[Theses/NVDA - Nvidia]] §Summary factory/DSX lock-in and the existing [[Macro & Technology/800VDC Adoption]] note — production MGX + 80-firm OCP is the “practical path” claim becoming a ship date. **Does not** speak to CUDA vs ASIC or Omniverse TAM. **Supports** [[Theses/VRT - Vertiv Holdings]] / data-center power names only as ecosystem demand; VRT is not named here. No NVDA triggers to test.

## Source Excerpts
> “partnered with Google and Microsoft to develop the industry’s first 800 VDC architecture through the Open Compute Project… backed by a tally of 80 equipment/infrastructure companies… first platforms in the second half of 2026.”
> “NVIDIA’s Rubin MGX platforms based on the 800 VDC power architecture are already in production and will be rolling out in the second half of 2026.”
> “row power center… overhead 800 VDC busway… up to 2 MW of power per row… expected in 2027.”
