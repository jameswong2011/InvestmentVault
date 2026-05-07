---
type: thesis-manifest
batch: thesis-INTU-2026-05-01-200051
status: completed
completed_date: 2026-05-01
ticker: INTU
proposed_name: Intuit
proposed_path: Theses/INTU - Intuit.md
sector: Consumer & SMB Financial Software
date: 2026-05-01
---

# Thesis Transaction Manifest (completed)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/INTU - Intuit.md`
- Status: created

## Sector note update
- Sector resolution: none (no existing match — new sector created via Step 5 option (a))
- Sector note path: `Sectors/Consumer & SMB Financial Software.md`
- Edit applied: new_sector_note_created (INTU added as first Active Theses entry; status: draft, but new-sector scaffold rule requires at least one thesis entry per spec)

## `_hot.md` updates
- Active Research Thread entry: appended (different-ticker compression applied — PINS thread compressed to *Previous 2026-04-30:* line; SEMICAP *Previous 2026-04-29:* line dropped per compression trigger #2)
- Recent Conviction Changes entry: prepended (INTU MEDIUM initial)
- Open Questions entries: 3 added (TurboTax ARPC AI commoditization / QBO agentic workflow disintermediation / IES mid-market execution); items 4-24 renumbered
- Portfolio Snapshot: updated (53 theses across 39 sectors; INTU + new sector listed in conviction actions)
- ⚠️ **WORD CAP WARNING**: _hot.md = 6,475 words after compression triggers #1-#3; **exceeds 5,000 hard cap by 1,475 words**. Per hot-md-contract trigger #5, this is reported as warning — primary operations (thesis file, sector note) unaffected. Recent Conviction Changes section is NEVER-COMPRESS per contract; bulk of overflow is in detailed initial-conviction entries from late-Apr/May 2026 thesis cluster. Recommended manual cleanup: trim oldest Recent Conviction Changes entries (Apr 26-27 SKM/INTC) to ledger-format summaries, OR run `/lint #35` for full diagnosis. Header date updated 2026-04-29 → 2026-05-01.

## Orphan research integration
- Orphan research notes touched: none (no Research/ notes with `ticker: INTU` or `tags: [...INTU...]`)
- Wikilinks added to Related Research: 0 (orphan scan empty)

## Archive-collision decision (Step 1.2)
- Archived theses found: none (Signals A/B/C/D all empty for INTU)
- User decision: n/a (no collision)

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis INTU`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
