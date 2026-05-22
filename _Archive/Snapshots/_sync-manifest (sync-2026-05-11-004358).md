---
type: sync-manifest
batch: sync-2026-05-11-004358
mode: default
status: in-progress
date: 2026-05-11
---

# Sync Batch Manifest (in-progress)

Manifest written at Step 2.9 before any file modifications. Populated at
phase boundaries (end of Step 3, 4, 5) then flipped to status: completed
at Step 7.5.

If this file persists with status: in-progress, the sync crashed or was
interrupted. Recovery: inspect the sections below, then /rollback to
restore any Tier A snapshots listed.

## Theses with snapshots taken (Tier A)
- [[Theses/EDEL - Edelweiss Financial Group]] → [[_Archive/Snapshots/EDEL - Edelweiss Financial Group (pre-sync 2026-05-11-004358)]]

## Theses with Log-only appends (Tier B)
- [[Theses/STNG - Scorpio Tankers]] — cross-thesis propagation (BDC private-credit clockwork ↔ §Risks 9.2% PC default trajectory)
- [[Theses/PLTR - Palantir]] — cross-thesis propagation (tangential AI productivity disruption echo)
- [[Theses/NOW - ServiceNow]] — cross-thesis propagation (tangential AI productivity disruption echo)
- [[Theses/CRWD - CrowdStrike Holdings]] — cross-thesis propagation (tangential AI productivity disruption echo)
- [[Theses/PANW - Palo Alto Networks]] — cross-thesis propagation (tangential AI productivity disruption echo)
- [[Theses/RELIANCE - Reliance Industries]] — sector→thesis propagation ([[Sectors/Indian Digital Conglomerates]] 2026-05-07 §Network quality differential update)

## Sector notes touched
- [[Sectors/@Indian Financial Services]] (Tier A) → [[_Archive/Snapshots/@Indian Financial Services (pre-sync 2026-05-11-004358)]]

## Macro notes touched
_(none — empty macro target set; BDC research note has no `[[Macro/...]]` wikilinks and no `source_type: scenario` / `tags: macro` flags)_

## Source research notes processed
- [[Research/2026-05-11 - Private Credit BDC Redemption Gating Wave - news]] — primary source; propagated to STNG, EDEL, PLTR, NOW, CRWD, PANW + sector @Indian Financial Services
- [[Sectors/Indian Digital Conglomerates]] — changed source (2026-05-07 sector edit); propagated to RELIANCE (sector→thesis Log entry)
- [[Research/2026-05-11 - 000660 - Investment Brief]] — terminal skip (Case 2c: `propagated_to: []` signals producer-side terminal decision)
- [[Sectors/DRAM & HBM Memory]] — mtime newer than `.last_sync` but no new Log entry since 2026-04-27 (likely metadata touch from /brief); no analytical delta to propagate
