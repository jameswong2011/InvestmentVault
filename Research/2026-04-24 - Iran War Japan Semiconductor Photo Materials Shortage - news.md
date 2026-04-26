---
date: 2026-04-24
tags: [research, semiconductors, memory, iran-war, supply-chain, photoresist, HBM, 000660, 285A]
sector: DRAM & HBM Memory
ticker: [000660, 285A]
source: https://x.com/jukan05/status/2046852599622856973
source_type: news
propagated_to: [000660, 285A, NVDA, AMD, TSM, SEMICAP, SNDK]
---

# Iran War Fallout — Japan Semiconductor Photo Materials Supply Chain on the Brink

## Thesis Delta

Iran War's Strait of Hormuz blockade has cut 40%+ of Japan's naphtha supply, collapsing the PGME/PGMEA solvent chain that feeds every photoresist, BARC, SOH, and HBM temporary-bonding adhesive Japan ships to Samsung and SK Hynix. This is the **first material-level threat to the 2026 HBM ramp** — separate from and additive to the Taiwan CoWoS tail already in the [[Theses/000660 - SK Hynix]] and [[Theses/NVDA - Nvidia]] risk frameworks. PCN (Process Change Notification) requalification for alternate solvents takes ~1 year nominal, longer for leading-edge — meaning a disruption that lands in Q2 2026 propagates into 2027 HBM4 / HBM4E output, exactly when [[Theses/NVDA - Nvidia]] Rubin volume ramps and [[Theses/AMD - Advanced Micro Devices]] Helios (MI455X/H2 2026) ships.

## Summary

Iran's March blockade of the Strait of Hormuz cut Japan off from ~40% of its naphtha supply, forcing 6 of 12 Japanese naphtha cracking centers (NCCs) into production cuts and spiking spot naphtha from ~$600/ton to $1,190/ton (+92%). The downstream chain — naphtha → propylene → propylene oxide (PO) → PGME and PGMEA solvents — collapses the solvent inputs to nearly every semiconductor photo-patterning material Japan produces: photoresist (PR), thinner, bottom anti-reflective coating (BARC), spin-on-hardmask (SOH), and temporary bonding adhesives for HBM. Shin-Etsu, Tokyo Ohka Kogyo (TOK), JSR, Fujifilm, and Nissan Chemical — the sole-source or near-sole-source suppliers to Samsung and SK Hynix — began formally notifying Korean customers of raw-material disruptions starting April 21–23.

The asymmetric risk comes from Japan's self-sufficient production structure: Daicel integrates PO→PGMEA; Toagosei refines from Dow raw stock; when one raw-material input breaks, the entire domestic chain shakes simultaneously. Switching to Korean (Chemtronics, Jaewon Industrial) or Chinese PGME/PGMEA triggers Process Change Notification (PCN) requalification at Samsung/Hynix — ~1 year for normal nodes, longer for leading-edge EUV. An industry source characterized the acute tail: "if Japanese supply of PR or BARC is cut off, semiconductor fabs could come to a halt… some evaluation steps will inevitably have to be skipped." Korean alternatives have mass-production PGMEA but the Jaewon Industrial executive qualified that Korea's diversification (US + China sourcing) is only marginally better: "it's essentially the same situation."

The analogy one source offered captures the constraint precisely: "It's like not being able to add water to instant coffee mix." The solvents are cheap commodity inputs at the bottom of the bill of materials; their absence halts the top-of-stack HBM and advanced-logic ramp that drives the 2026 AI capex cycle.

## Evidence

| Data point | Value | Source |
|---|---|---|
| Japan naphtha sourcing from Middle East | ~40%+ of supply | Article |
| Japanese NCCs (naphtha cracking centers) in production cuts | 6 of 12 | Article |
| Japan naphtha spot price, pre-blockade | ~USD 600/ton | Article |
| Japan naphtha spot price, early April 2026 | USD 1,190/ton (+92%) | Article |
| PCN requalification cycle, normal nodes | ~1 year | Article |
| PCN requalification cycle, leading-edge | Longer than 1 year | Article |
| Japanese suppliers affected | Shin-Etsu Chemical, Tokyo Ohka Kogyo (TOK), JSR, Fujifilm, Nissan Chemical | Article |
| Japan PGMEA integrated producers | Daicel (PO → PGMEA), Toagosei (Dow raw → PGMEA) | Article |
| Korean alternative producers | Chemtronics, Jaewon Industrial (PGMEA mass production); Hanwul Soje Science/JK Materials (sourcing from Chinese Company E) | Article |

**Chain of disruption**:
```
Strait of Hormuz blockade → -40% Japan naphtha → 6/12 NCCs cut → -propylene →
-Propylene Oxide (PO) → -PGME/PGMEA solvents → -PR / BARC / SOH / HBM temp-bonding adhesive →
Samsung Electronics + SK Hynix fab risk
```

**Affected materials (covering "almost all photo patterning process materials")**:
- Photoresist (PR)
- Thinner
- Bottom Anti-Reflective Coating (BARC)
- Spin-On-Hardmask (SOH)
- **Temporary bonding adhesives for High Bandwidth Memory (HBM)** ← direct HBM3E/HBM4 production input

**Localization status per source**: "Thinner and SOH have been partially localized, but if Japanese supply of PR or BARC is cut off, semiconductor fabs could come to a halt. If there are major disruptions in material sourcing, some evaluation steps will inevitably have to be skipped."

## Contradiction Check

**Challenges existing conviction on [[Theses/000660 - SK Hynix]]**: 000660 thesis Risk #4 frames the Taiwan tail as the binary kinetic HBM supply risk, with HBM4/HBM4E yields on MR-MUF packaging as the primary execution risk. This adds a **non-binary, non-Taiwan supply disruption mechanism** the thesis does not model. Weakens near-term bull case (2026 HBM revenue at risk from raw material disruption, not demand weakness) but does not invalidate the longer 2027-2028 HBM4E thesis. Conviction directionally: weaker on 2026 HBM revenue ($30B est), unchanged on 5-year thesis.

**Challenges existing conviction on [[Theses/285A - Kioxia]]**: Kioxia Yokkaichi + Kitakami fabs are Japan-located and directly exposed to the same PGME/PGMEA supply chain — BiCS10 332-layer ramp depends on same PR/BARC ecosystem. 285A thesis Key Non-consensus Insight #4 ("Japan-centric manufacturing is a geopolitical moat, not a geographic risk") is now actively challenged: Japanese concentration creates material-input fragility the thesis did not anticipate. Conviction directionally: weaker on "Japan moat" framing; BiCS10 expedited timeline now exposed to dual execution risk (yield + raw material).

**Challenges [[Theses/TSM - Taiwan Semiconductor]]**: TSMC's advanced nodes also consume Japanese PR/BARC (Shin-Etsu, TOK are primary sole-source suppliers for EUV PR). TSM thesis does not model a Japanese materials disruption. However, article notes Taiwan/Korean localization is farther along than Japanese — TSMC may be less exposed than Samsung/Hynix. Outstanding question.

**Supports [[Macro & Technology/Iran War Trading Playbook]]**: this is a direct downstream effect of the Hormuz blockade commodity framework. Fertilizer, LNG, oil disruptions are already in the macro; semiconductor photo materials are an unpriced fifth transmission channel.

**Supports [[Macro & Technology/Iran War Trading Playbook]]**: validates the "sustained-crisis" tail — insurance-mechanism damage persists even after ceasefire, and material-input supply chains (naphtha → PGMEA) have months-to-year rebuild timelines regardless of political resolution.

## Source Excerpts

> "Japan depends on the Middle East for more than approximately 40% of its naphtha. When the Strait of Hormuz was effectively blockaded in early March, Middle Eastern naphtha supply was cut off... As a result, 6 of Japan's 12 naphtha cracking centers (NCCs) have entered production cuts."

> "Semiconductor materials that use PGME and PGMEA include PR, Thinner, Bottom Anti-Reflective Coating (BARC), Spin-On-Hardmask (SOH), and temporary bonding adhesives for High Bandwidth Memory (HBM). This covers almost all photo patterning process materials."

> "If the raw material for photo materials changes, Samsung Electronics and SK Hynix must redo evaluations. This typically takes around one year. For leading-edge processes, it takes even longer."

> "Thinner and SOH have been partially localized, but if Japanese supply of PR or BARC is cut off, semiconductor fabs could come to a halt."

## Related

- [[Theses/000660 - SK Hynix]] — primary HBM producer dependent on Japanese PR/BARC; adds unmodeled 2026 HBM supply risk
- [[Theses/285A - Kioxia]] — Japan-located NAND fabs directly exposed; challenges "Japan moat" framing
- [[Theses/NVDA - Nvidia]] — Rubin 2026 volume ramp depends on Samsung/Hynix HBM delivery; indirect exposure
- [[Theses/AMD - Advanced Micro Devices]] — MI355X/MI450 HBM4 content depends on same supply chain
- [[Theses/TSM - Taiwan Semiconductor]] — leading-edge photoresist consumer; localization status uncertain
- [[Theses/SNDK - SanDisk]] — Japan JV partner with Kioxia; same Flash Ventures exposure
- [[Theses/SEMICAP - Semiconductor Capital Equipment]] — PCN requalification cycle creates near-term equipment demand uncertainty as fabs re-evaluate
- [[Sectors/DRAM & HBM Memory]] — sector-wide HBM ramp risk
- [[Sectors/NAND Memory & Storage]] — Japanese NAND fab exposure
- [[Sectors/Semiconductor Foundries]] — leading-edge PR supply chain
- [[Sectors/Semiconductor Capital Equipment]] — PCN cycle impact
- [[Macro & Technology/Iran War Trading Playbook]] — parent macro framework: this note adds semiconductor photo materials as a fifth commodity transmission channel (alongside energy / fertilizer / LNG / metals); material-chain rebuild timeline extends Scenario A duration; sector-allocation implications include Korean memory + Japanese NAND + Taiwan foundry indirect exposure
