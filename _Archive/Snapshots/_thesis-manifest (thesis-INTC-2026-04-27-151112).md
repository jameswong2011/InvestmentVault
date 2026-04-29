---
type: thesis-manifest
batch: thesis-INTC-2026-04-27-151112
status: completed
completed_date: 2026-04-27
ticker: INTC
proposed_name: Intel
proposed_path: Theses/INTC - Intel.md
sector: GPU & AI Compute Accelerators
date: 2026-04-27
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/INTC - Intel.md`
- Status: created

## Sector note update
- Sector resolution: exact (`GPU & AI Compute Accelerators` → `Sectors/GPU & AI Compute Accelerators.md`)
- Sector note path: `Sectors/GPU & AI Compute Accelerators.md`
- Edit applied: skipped (draft status — promotion via `/status INTC status draft→active` will add to Active Theses)

## `_hot.md` updates
- Active Research Thread entry: appended new INTC head; compressed prior SKM thread to single `*Previous 2026-04-26:*` line; dropped oldest `*Previous:*` line (2026-04-23 MRVL) per soft-cap compression trigger
- Recent Conviction Changes entry: added (medium initial, with full rationale + decision points)
- Open Questions entries: 3 added (#43 18A yield by end-2026, #44 14A external customer commitments by H1 2027, #45 Coral Rapids SMT-restoration disclosure by H2 2027)
- Sync Archive: dropped oldest entry (2026-04-23 orphan remediation) per soft-cap compression trigger #1
- Word count post-edits: 4828 (over 4000 soft cap, under 5000 hard cap; surfaced as warning per contract step 4)

## Orphan research integration
- Orphan research notes touched: 0 (none have `ticker: INTC` frontmatter; Intel mentions in existing research are tangential to the ticker primary, not orphan candidates)
- Wikilinks added to Related Research: 16 (sector notes ×4, thesis cross-references ×7, macro ×1, research ×4 — including [[Research/2026-04-24 - Agentic AI CPU Bottleneck and Server CPU Framework - deep-dive]] which contains the most Intel-relevant analysis (Diamond Rapids SMT regression scoring))

## Archive-collision decision
- Archived theses found: none (Step 1.0 probe batch returned all-clear)
- User decision: n/a — no collision

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis Intel`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
