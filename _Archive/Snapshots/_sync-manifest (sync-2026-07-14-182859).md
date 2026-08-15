---
publish: false
type: sync-manifest
batch: sync-2026-07-14-182859
mode: default
status: completed
date: 2026-07-14
completed_date: 2026-07-14
---

# Sync Batch Manifest (completed)

Default `/sync` **manually scoped** to the single just-ingested research note
[[Research/2026-07-14 - Intel Foveros Direct vs CoWoS Advanced Packaging - deep-dive]].

Scope caveat: `.last_sync` was stale at 2026-04-29, so `find -newer` returned
~130 files (effectively the whole vault). The backlog was NOT reprocessed and
`.last_sync` was deliberately NOT advanced (advancing it would mask any genuinely
unpropagated changes in the backlog). Run `/sync all` for a full reconciliation.

All edits this run were Tier B (Log append + Related Research wikilink) — no
analytical-section rewrites, no conviction changes, no snapshots. The source
corroborated existing vault positions and added a falsifiable framework (already
captured in the research note itself).

## Theses with snapshots taken (Tier A)
None.

## Theses with Log-only appends (Tier B)
- [[Theses/INTC - Intel]] — Log + Related Research (Foveros-Direct yield-parity framework; EMIB-vs-Foveros-Direct split; tempers EMIB-cost read). Conviction unchanged (low).
- [[Theses/TSM - Taiwan Semiconductor]] — Log + Related Research (sizes CoWoS annuity #1; confirms "Intel 18A threat refuted"). Conviction unchanged (high).
- [[Theses/BESI - BE Semiconductor Industries]] — Log + Related Research (Intel's 15-20 bonders sufficient → not the near-term demand driver; TSMC/AMD is). Conviction unchanged (medium).

## Sector notes touched
- [[Sectors/ABF Substrates & Advanced Packaging Supply Chain]] — Log + Related Research (skeptical counterweight to §Investor heuristics Insight #4 EMIB-T cost arbitrage; adds Foveros-Direct yield-parity + supply-chain barbell). No framework change; no active substrate thesis.

## Macro notes touched
- [[Macro & Technology/CoWoS-to-CoPoS Panel-Level Packaging Transition]] — Log (corroborates EMIB-T competing-path + inspection-is-path-agnostic; adds EMIB-vs-CoWoS trade-off + Foveros-Direct yield gate).
- [[Macro & Technology/Organic ABF to Glass-Core Substrate Transition]] — Log (skeptical external-monetization read on Intel first-mover; TSMC owns the profit pool).

## Source research notes processed
- [[Research/2026-07-14 - Intel Foveros Direct vs CoWoS Advanced Packaging - deep-dive]]

## Skipped as low-signal (named beneficiaries, no thesis-specific delta)
Covered via ABF sector Related Research; no individual Log entry to avoid noise:
AMAT, KLA, ONTO, CAMT, 6857 (Advantest), TER, FORM, 000660 (SK Hynix), AMD, AVGO, MRVL, NVDA.

## _hot.md
Updated: heading + Active Research Thread (added ingest→sync thread) + Latest Sync (replaced). Net word change ~0 (stayed under hard cap).
