---
type: thesis-manifest
batch: thesis-AMD-2026-04-21-110557
status: completed
completed_date: 2026-04-21
ticker: AMD
proposed_name: Advanced Micro Devices
proposed_path: Theses/AMD - Advanced Micro Devices.md
sector: Semiconductors
date: 2026-04-21
---

# Thesis Transaction Manifest (completed)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/AMD - Advanced Micro Devices.md`
- Status: created

## Sector note update
- Sector resolution: exact (literal filename match `Sectors/Semiconductors.md`)
- Sector note path: `Sectors/Semiconductors.md`
- Edit applied: skipped (draft status) — thesis added to `Sectors/Semiconductors.md ## Active Theses` at `/status AMD status draft→active` promotion per sector-resolution contract

## `_hot.md` updates
- Active Research Thread entry: replaced (different-ticker compression — outgoing TSM compressed to `*Previous 2026-04-19:*` line; new AMD thread body written)
- Recent Conviction Changes entry: added (`AMD initial conviction: MEDIUM` 2026-04-21, full rationale)
- Open Questions entries: 3 added (OpenAI warrant vesting mechanics; MI450/Helios vs Rubin rack competitiveness; OpenAI/Meta 6GW contractual firmness)
- Word count post-edit: 1,637 (well under 4,000 soft cap — no compression triggered)

## Orphan research integration
- Orphan research notes touched: none — no research notes have `ticker: AMD` frontmatter or `tags:` containing AMD as primary. All existing AMD mentions in Research/ are competitive/comparative references in other tickers' notes (NVDA, AVGO, TSM, SNDK, 285A, LITE, IQE) and are captured via the thesis's Related Research section.
- Wikilinks added to Related Research: 14 (sector/thesis/macro/research — see thesis file)

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none — all four signals (filename glob, frontmatter ticker, archive registry, snapshot trail) returned empty
- User decision: n/a

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis AMD`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
