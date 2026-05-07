---
type: thesis-manifest
batch: thesis-ASMI-2026-04-29-190755
status: completed
completed_date: 2026-04-29
ticker: ASMI
proposed_name: ASM International
proposed_path: Theses/ASMI - ASM International.md
sector: Semiconductor Capital Equipment
date: 2026-04-29
---

# Thesis Transaction Manifest (completed)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/ASMI - ASM International.md`
- Status: created

## Sector note update
- Sector resolution: exact (`Sectors/Semiconductor Capital Equipment.md`)
- Sector note path: `Sectors/Semiconductor Capital Equipment.md`
- Edit applied: skipped (draft status) — per /thesis spec, draft theses are not added to sector Active Theses lists; user must promote via `/status ASMI draft→active` first

## `_hot.md` updates
- Active Research Thread entry: appended (ASMI full paragraph; LRCX demoted to *Previous* one-liner)
- Recent Conviction Changes entry: appended (ASMI MEDIUM with full audit)
- Open Questions entries: 3 added (items 22-24: 1.4nm POR slot count, ALTUS Halo/Trillium HKMG threat, ASMPT stake resolution)
- Portfolio Snapshot: updated (50 theses; 6 WFE theses)

## Orphan research integration
- Orphan research notes referenced in Related Research: 4 (wikilinks added to thesis):
  - `Research/2026-03-20 - Lam Research and Applied Materials Evaluation.md`
  - `Research/2026-03-20 - Semis - Gemini WFE Equipment Canvas.md`
  - `Research/2026-04-15 - BESI - Hybrid Bonding Market Projections.md`
  - `Research/2026-04-24 - Dylan Patel on AI Token Supply and Demand - video-transcript.md`
- Wikilinks added to Related Research: 4 research + 4 thesis peers (BESI, NVDA, TSM, AIXA) + 1 sector + 1 macro = 10 total

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none (all four signals A/B/C/D returned empty)
- User decision: N/A — proceeded with original proposed name

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis ASMI`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: 2026-04-29`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
