---
type: thesis-manifest
batch: thesis-SOI-2026-06-08-211941
status: completed
completed_date: 2026-06-08
ticker: SOI
proposed_name: Soitec
proposed_path: Theses/SOI - Soitec.md
sector: Semiconductor Capital Equipment
date: 2026-06-08
---

# Thesis Transaction Manifest (completed)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/SOI - Soitec.md`
- Status: created (Step 4 — 2026-06-08; 13/13 required sections present; frontmatter complete with status: draft + conviction: medium; sector: Semiconductor Capital Equipment; ticker: SOI)

## Sector note update
- Sector resolution: exact (frontmatter `sector: Semiconductor Capital Equipment` matches `Sectors/Semiconductor Capital Equipment.md` directly)
- Sector note path: `Sectors/Semiconductor Capital Equipment.md`
- Edit applied: skipped (draft status) — per SKILL.md Step 5 status-dependent behavior. Soitec will be added to `## Active Theses` when promoted via `/status SOI status draft→active`.

## `_hot.md` updates
- Active Research Thread entry: appended new SOI thread block (~300 words) demoting WinWay 6515 to *Previous:* line per same-ticker-continuation rule (different ticker → compress prior + prepend new). Pre-existing 036930 Jusung + LPKF *Previous:* lines compressed under hot-md-contract step 2 (drop oldest *Previous:*) to clear budget headroom for RCC + OQ adds. Net active-thread state: 1 live SOI block + 1 *Previous:* line for WinWay 6515 (Jun 8, full RCC entry retained in Recent Conviction Changes). Older *Previous* lines (036930, LPKF, /surface semis, /sync AI Silicon Shortage) all audit-trailed via HTML comment + thesis Logs.
- Recent Conviction Changes entry: prepended compact SOI initial MEDIUM entry (~85 words) above existing WinWay 2026-06-08 entry. Compact-format used (vs full ~400-word standard) because _hot.md was at 4,944 words after thread update — within 56-word headroom of hard cap. Full conviction rationale + complete CLOSE/LOW/HIGH triggers + 5 non-consensus angles live in [[Theses/SOI - Soitec]] body + Log.
- Open Questions entries: 1 added (item #85) as merged pointer entry collapsing the three highest-information Soitec Outstanding Questions (Photonics-SOI ramp velocity + RF-SOI cycle bottom + Rémont AGM strategic intent) into a single ledger line that converges at Q1'27 print (Jul-Aug 2026). Compressed format per hot-md-contract step 3 (merge duplicates / collapse cohorts). Three individual questions retained in full detail at [[Theses/SOI - Soitec]] §Outstanding Questions.
- Final word count: 4,996 / 5,000 hard cap (under by 4 words). Compression actions: 4 historical *Previous:* lines dropped, RCC entry trimmed to ~85 words from ~300-word draft, OQ collapsed to single pointer. ⚠️ _hot.md is at the absolute ceiling of the hard cap — next skill writing to _hot.md should expect to either drop additional RCC roster or initiate proactive Sync Archive maintenance.

## Orphan research integration
- Orphan research notes touched: 0 — no Research/*.md file contains "Soitec" by name or has `ticker: SOI` frontmatter (verified via Grep against Research/ at Step 5)
- Wikilinks added to Related Research: 0 orphan adjacency. Thesis Related Research cites 8 existing research notes (LITE Silicon Photonics Supply Chain, Gemini SiPh Canvas, CPO Investment Outlook, LITE Gemini CPO Canvas, Chinese SiPh Threat, AIXA/VECO MOCVD synthesis, Semi Portfolio Rebalancing) on adjacent CPO / silicon-photonics topics — these notes do NOT reference Soitec, so no mtime touch (a touch would falsely re-enter them into `/sync`'s changed-file set).

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none — Step 1.2 Signals A/B/C/D all clean (verified at 21:19:31 UTC, 2026-06-08)
- User decision: n/a

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits. Recovery: `rm` manifest; re-run `/thesis Soitec`.
- **Thesis file created, sector/hot.md incomplete**: thesis exists but disconnected from sector + _hot.md. Recovery: complete remaining steps manually per manifest body OR `rm` thesis file + manifest, then re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: YYYY-MM-DD`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
