---
date: 2026-08-12
tags: [research, daily-intel-triage, semiconductors, memory, NVDA, 000660]
sector: semiconductors
ticker: NVDA
propagated_to: [000660, NVDA]
source: 'https://wccftech.com/nvidias-kyber-racks-to-sport-340-4tb-of-dram-with-hbm4e-priced-at-19-76-gb-and-each-rack-reportedly-priced-at-41-6-million/'
source_type: news
---

# NVDA / 000660 — Kyber Rack HBM4E Pricing and Memory Bill Shift

## Thesis Delta
Consensus prices Kyber/Rubin as an HBM volume/ASP windfall for SK Hynix; BofA’s rack math implies HBM stays only ~5–6% of Kyber rack value while LPDDR5X SOCAMM2 outspends HBM4E ($2.8M vs $2.5M per-rack bill) — memory cost pressure migrates to commodity LPDDR even as HBM4E prints at $19.76/GB. Supports [[Theses/NVDA - Nvidia]] system-ASP framing more than a pure HBM-monopoly extension for [[Theses/000660 - SK Hynix]].

## Summary
Wccftech summarizes Bank of America work on Vera Rubin Ultra–based Kyber racks: 144 GPUs, 340.4TB total DRAM, rack ASP ~$41.6M. HBM4E at $19.76/GB on 124.4TB costs ~$2.5M per rack; 216TB LPDDR5X costs ~$2.8M. UBS component costs put ~half of Rubin GPU BOM and nearly all of Vera CPU BOM in DRAM after stripping non-memory content. Versus Blackwell, the memory pool jumps from ~74.7TB on Vera Rubin racks to 340.4TB on Kyber — but HBM’s share of rack dollars falls.

## Evidence
| Metric | Figure | Tag |
|---|---|---|
| HBM4E price | $19.76/GB | [1×: BofA via Wccftech] |
| Kyber rack ASP | $41.6M | [1×: BofA via Wccftech] |
| HBM4E per Kyber rack | 124.4TB / ~$2.5M | [1×: BofA via Wccftech] |
| LPDDR5X per Kyber rack | 216TB / ~$2.8M | [1×: BofA via Wccftech] |
| Rubin GPU BOM (UBS) | ~$9,247 incl. HBM4/packaging | [1×: UBS via Wccftech] |
| Vera CPU BOM (UBS) | ~$20,059 incl. SOCAMM2; ~$704 ex-memory | [1×: UBS via Wccftech] |
| HBM share of Kyber rack | ~5–6% (vs ~7.5% Blackwell Ultra) | [1×: BofA via Wccftech] |

## Contradiction Check
Supports [[Theses/NVDA - Nvidia]] rack/system monetization and challenges a naive “all memory dollars = HBM to 000660” read in [[Theses/000660 - SK Hynix]].

## Source Excerpts
> "Bank of America has just published a new report detailing that HBM4E within Rubin costs $19.76 per GB… each 144-GPU Kyber rack will sport 216TB of LPDDR5X that costs around $2.8 million, and above the $2.5 million bill for 124.4TB of HBM4E. In total, each Kyber rack will cost $41.6 million."
