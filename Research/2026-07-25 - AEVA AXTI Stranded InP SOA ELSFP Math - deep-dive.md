---
date: 2026-07-25
tags: [research, Semiconductors, LITE, AXTI, AEVA, Optics]
sector: Custom Silicon & Networking Semiconductors
ticker: AXTI
propagated_to: [LITE]
source: 'https://irrationalanalysis.substack.com/p/stranded-indium-phosphide'
source_type: deep-dive
---

## Thesis Delta
Consensus ignores LiDAR remnants as dead capital → IA models a "stranded InP" path where high-power SOA (Aeva + Seivers fab) seeds ELSFP modules for NPO/CPO when discrete DFB supply is apocalyptically tight. Device-level SOA looks InP-area efficient; product-level math still shows ~17% GM vs ~51% for 8× discrete DFB. Author still prefers LITE/AXTI/AAOI over AEVA/Seivers, but flags AEVA as the only public high-quality SOA path for this niche.

## Summary
Follow-up to the SOA primer. Industry analogy: ~80% of InP already goes to AI vs ~25% of DRAM—InP has no consumer spillover to annex. Design objective: single-λ 1310nm ELSFP, 22 dBm coupled per fiber × 8 fibers. Compares 8× discrete DFB vs LiDAR-style 650 mW SOA boost. Caveats: still need CW seed laser; coupling/isolator losses after weird SOA beam shape. Spreadsheet (public in post): normal path ~51% GM, SOA path ~17% GM—still sellable into starved CPO/NPO. Only two viable high-power SOA makers per IA: unnamed private IDM + $AEVA (Seivers InP partner). Seivers DWDM array yield called horrific; Aeva SOA may earn Seivers more than Ayar ever did. Lumentum cut non-Nvidia customers; Ayar still listed Lumentum until LITE removed Ayar.

## Evidence
| Item | Figure | Tag |
|---|---|---|
| SOA class modeled | 650 mW | [1×: AEVA claims / IA] |
| ELSFP GM discrete DFB path | ~51% | [est.: IA model] |
| ELSFP GM SOA path | ~17% | [est.: IA model] |
| Target coupled power | 22 dBm × 8 fibers | [1×: IA design obj.] |
| Author holdings | LITE, AXTI, AAOI (not AEVA) | [1×: IA] |

## Contradiction Check
Supports InP scarcity premium for [[Theses]] on LITE/AXTI; opens a low-quality-supply option via AEVA that caps how "unsolvable" UHP lasers look. Falsifiers: Broadcom/Lumentum UHP DFB ramps crush the need for SOA kludges; AEVA SOA fails reliability/coupling; Seivers cannot scale.
