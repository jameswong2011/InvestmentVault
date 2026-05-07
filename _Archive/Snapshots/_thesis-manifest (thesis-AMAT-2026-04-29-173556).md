---
type: thesis-manifest
batch: thesis-AMAT-2026-04-29-173556
status: completed
completed_date: 2026-04-29
ticker: AMAT
proposed_name: Applied Materials
proposed_path: Theses/AMAT - Applied Materials.md
sector: Semiconductor Capital Equipment
date: 2026-04-29
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/AMAT - Applied Materials.md`
- Status: created (13 sections, frontmatter status: draft, conviction: medium, sector: Semiconductor Capital Equipment)

## Sector note update
- Sector resolution: exact (Semiconductor Capital Equipment)
- Sector note path: `Sectors/Semiconductor Capital Equipment.md`
- Edit applied: skipped (draft status) — per Step 5 status-dependent gate; sector wikilink to be added when user runs `/status AMAT draft→active`

## `_hot.md` updates
- Active Research Thread entry: appended (AIXA rotated to *Previous:* one-liner; INTC oldest *Previous:* dropped to make room)
- Recent Conviction Changes entry: appended (AMAT MEDIUM); 4 oldest entries dropped (Iran scenario, NVDA flagged, CRWD active, CRWD init — all audit-trailed in respective thesis Logs)
- Open Questions entries: 3 added (AMAT #27 ASMI ALD threat, #28 EPIC Center stranded-asset risk, #29 China structural-vs-cyclical split); 14 oldest dropped (VRT/CRWD/blind-spot/scenario/NVDA — all audit-trailed); section renumbered 1-29
- Latest Sync: compressed (~700w → ~200w; full audit trail retained in sync manifest)
- Portfolio Snapshot: thesis count 46 → 48 (incl. AIXA from Apr 29 + AMAT)
- File size before: 5,551 words (over 5,000 hard cap pre-edit). After: 4,782 words (under hard cap, near soft cap).

## Orphan research integration
- Orphan research notes touched: 7 paths
  - `Research/2026-02-26 - Semis - Gemini Lam vs AMAT Canvas.md`
  - `Research/2026-03-20 - Lam Research and Applied Materials Evaluation.md`
  - `Research/2026-03-20 - Semis - Gemini WFE Equipment Canvas.md`
  - `Research/2026-04-10 - Hybrid Bonding and BESI Revenue Impact.md`
  - `Research/2026-04-15 - BESI - Hybrid Bonding Market Projections.md`
  - `Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript.md`
  - `Research/2025-07-06 - BESI - Analyst Estimates and Valuation Trends.md`
- Wikilinks added to Related Research: 13 (5 directly relevant research notes + 2 BESI/hybrid bonding notes added during Step 5 + 1 sector + 2 sector cluster theses + 4 cross-thesis cluster wikilinks + 3 memory adjacency wikilinks + 1 macro)

## Archive-collision decision (Step 1.2)
- Archived theses found: none (Signals A/B/C/D all empty)
- User decision: not applicable

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis AMAT`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: 2026-04-29`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
