---
publish: false
date: 2026-08-14
tags: [research, daily-intel-triage, news, SNDK, 000660]
sector: NAND Memory & Storage
ticker: SNDK
propagated_to: [SNDK, 000660]
source: 'https://cryptobriefing.com/sandisk-high-bandwidth-flash-2027/'
source_type: news
---

# SanDisk Tapes Out First HBF Die; 512GB/Stack, 1.6 TB/s; Samples Targeted 2027

## Thesis Delta
Consensus still prices [[Theses/SNDK - SanDisk]] HBF and [[Theses/000660 - SK Hynix]] Insight #3 as a 2027 OCP-spec option — this 13 August 2026 Crypto Briefing recap says SanDisk has finished designing (taped out) its first High Bandwidth Flash die, with gen-1 up to 512 GB per stack and ~1.6 TB/s read, 8-Hi/16-Hi stacks, 0.4–3 TB/s grades, SK hynix MoU (August 2025) to co-develop specs, first open specs “scheduled for August 2026,” and product samples in 2027 (the piece also says “initial HBM samples… late 2026,” which looks like a wording slip next to HBF). That is a design-complete milestone, not a revenue line. Hypothesis: tape-out plus the existing SK hynix OCP workstream reduces Betamax risk; 2027 samples vs the thesis’s older “H2 2026 samples” is a slip if the dates are right. 000660 → HIGH/LOW/CLOSE are Rubin/CXMT handles — HBF does not fire them.

## Summary
Crypto Briefing positions HBF as NAND stacked to approach HBM economics for inference, “within 2.2% of theoretical HBM limits” on SanDisk projections, at far higher capacity (8–16× vs comparable HBM configs). Gen-1: 512 GB/stack, ~1.6 TB/s; roadmap 2.0 then 3.2 TB/s. Configurations 8-high and 16-high; bandwidth grades 0.4–3 TB/s. Process: CBA + BiCS NAND. Workload split: HBM for training; HBF for inference (answers, images, recommendations).

Governance: technical advisory board July 2025; MoU with SK hynix August 2025 — notable because SK hynix is the HBM share leader. Open specs due August 2026 (stack configs, bandwidths, power). Flash Memory Summit recognition. Related primary (SK hynix newsroom 4 August, not this fetch): 512 GB stacks, 0.4–3.0 TB/s, UCIe host, Google and Tenstorrent in the consortium. If August 2026 specs get buy-in, integrators can plan 2028–29 products. Production scales on existing NAND infrastructure rather than a greenfield memory.

## Evidence

| Item | Figure | Tag |
|---|---|---|
| Milestone | first HBF die taped out | [1×: Crypto Briefing 2026-08-13] |
| Samples | 2027 | [1×: Crypto Briefing] |
| Gen-1 capacity / BW | 512 GB/stack; ~1.6 TB/s | [1×: Crypto Briefing] |
| vs HBM | “within 2.2%” of theoretical HBM limits (SanDisk proj.) | [1×: SanDisk via CB] |
| Capacity vs HBM | ~8–16× comparable configs | [1×: Crypto Briefing] |
| Roadmap BW | 2 TB/s then 3.2 TB/s | [1×: Crypto Briefing] |
| Stacks / grades | 8-Hi and 16-Hi; 0.4–3 TB/s | [1×: Crypto Briefing] |
| Process | CBA + BiCS | [1×: Crypto Briefing] |
| SK hynix MoU | August 2025; co-develop HBF specs | [1×: Crypto Briefing] |
| Open specs | August 2026 | [1×: Crypto Briefing] |
| Advisory board | July 2025 | [1×: Crypto Briefing] |
| OCP companion | 512GB; 0.4–3.0 TB/s; UCIe; Google + Tenstorrent | [1×: SK hynix IR 2026-08-04] |

## Contradiction Check
**Supports** [[Theses/SNDK - SanDisk]] Insight #1 (HBF as TAM creation; SK hynix partnership kills Betamax) and [[Theses/000660 - SK Hynix]] Insight #3 (unpriced HBF option) — tape-out is the first silicon-design print, not $5–10B TAM realization. **Challenges** the thesis’s “samples targeted H2 2026” if 2027 is the live date. **Does not fire** 000660 Rubin/CXMT triggers. **Does not** put HBF on a 2026 Rubin board.

## Source Excerpts
> “SanDisk just finished designing its first High Bandwidth Flash memory die… product samples in 2027.”
> “The first generation targets up to 512 GB per stack with read bandwidths around 1.6 TB/s.”
> “In August 2025, SanDisk signed a memorandum of understanding with SK hynix.”
