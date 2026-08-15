---
publish: false
type: thesis-manifest
batch: thesis-NBIS-2026-06-02-180429
status: completed
completed_date: 2026-06-02
ticker: NBIS
proposed_name: Nebius Group
proposed_path: Theses/NBIS - Nebius Group.md
sector: Neoclouds & GPU-as-a-Service
date: 2026-06-02
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/NBIS - Nebius Group.md`
- Status: created (2026-06-02)

## Sector note update
- Sector resolution: exact (Sectors/Neoclouds & GPU-as-a-Service.md)
- Sector note path: Sectors/Neoclouds & GPU-as-a-Service.md
- Edit applied: skipped (draft status — added to Active Theses on promotion via /status draft→active)

## `_hot.md` updates
- Active Research Thread entry: added (NBIS /thesis entry; outgoing CPU-Landscape sync thread compressed to *Previous:* line)
- Recent Conviction Changes entry: added (NBIS initial MEDIUM)
- Open Questions entries: added (3 — items 71-73)
- Compression applied: trigger steps 1 (dropped oldest Sync Archive entry), 2 (dropped oldest *Previous:* line), 4 (compressed 5 OQ cohorts >14d), 5 (roster-compressed 3 RCC entries >30d). Started 4,829 words; ended under hard cap. Over soft cap (4,000) → step-7 warning surfaced in report; under hard cap (5,000) — no abort.

## Orphan research integration
- Orphan research notes touched: none (no NBIS-primary research notes — `ticker: NBIS` frontmatter + `tags: NBIS` greps both empty)
- Wikilinks added to Related Research: 15 (5 sector/macro + 6 cross-thesis + 4 research notes; all peer/context links, none orphan-integration)

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (Signals A/B/C/D all empty — clean creation)
- User decision: n/a

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis NBIS`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
