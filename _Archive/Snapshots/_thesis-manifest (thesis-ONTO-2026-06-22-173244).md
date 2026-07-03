---
type: thesis-manifest
batch: thesis-ONTO-2026-06-22-173244
status: completed
ticker: ONTO
proposed_name: Onto Innovation
proposed_path: Theses/ONTO - Onto Innovation.md
sector: Advanced Semi Metrology
date: 2026-06-22
completed_date: 2026-06-22
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/ONTO - Onto Innovation.md`
- Status: created

## Sector note update
- Sector resolution: exact
- Sector note path: Sectors/Advanced Semi Metrology.md
- Edit applied: skipped (draft status — added to Active Theses on promotion via /status draft→active)

## `_hot.md` updates
- Active Research Thread entry: new ONTO live block written (different-ticker rule); CoPoS /sync block demoted to *Previous* one-liner; ARM *Previous* dropped
- Recent Conviction Changes entry: ONTO initial MEDIUM prepended
- Open Questions entries: 1 cohort pointer added (items 95-97, 3 questions)
- Compression (hard-cap fallback per hot-md-contract; file 5,292 → 4,643 words): dropped oldest Sync Archive entry (2383) + oldest *Previous* (2383); compressed OQ cohorts >14d to pointers (NBIS 71-73, MLCC 74, item 75, LPKF 76-78, 036930 79-81). Now under 5,000 hard cap (over 4,000 soft — normal for this dense dashboard).

## Orphan research integration
- Orphan research notes touched: none — no Research/ note carries ticker:ONTO or tags:ONTO (resolution order (a)/(b) empty). Body-only mention in HBM Packaging Equipment Stack deep-dive wikilinked in Related Research without mtime touch (not a ticker/tags match).
- Wikilinks added to Related Research: 0 orphan-driven; ~14 authored cross-thesis/sector/macro/research links

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (Signals A/B/C/D all empty)
- User decision: n/a — no collision

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis ONTO`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
