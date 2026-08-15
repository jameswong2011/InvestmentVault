---
publish: false
type: sync-manifest
batch: sync-2026-07-15-173001
mode: all
status: completed
date: 2026-07-15
completed_date: 2026-07-15
---

# Sync Batch Manifest (completed)

Manifest written at Step 2.9 before any file modifications. Populated at
phase boundaries (end of Step 3, 4, 5) then flipped to status: completed
at Step 7.5.

If this file persists with status: completed, the sync crashed or was
interrupted. Recovery: inspect the sections below, then /rollback to
restore any Tier A snapshots listed.

**Run context**: backlog reconciliation. `.last_sync` had been stuck at
2026-04-29 20:38 for ~2.5 months because every intervening sync was
ticker- or file-scoped and therefore not entitled to advance the
watermark. `find -newer` consequently flagged 218 files (82/82 theses,
51/51 sectors, 9/9 macros) — phantom. Step 1.7 idempotency scan across
the 76 changed research notes isolated 20 genuinely un-propagated notes;
those 20 are this run's working set. The watermark advance at Step 7 is
legitimate only because that residue is reconciled here.

## Theses with snapshots taken (Tier A)
- Theses/ISRG - Intuitive Surgical.md → _Archive/Snapshots/ISRG - Intuitive Surgical (pre-sync 2026-07-15-173001).md
- Theses/ONON - On Holding.md → _Archive/Snapshots/ONON - On Holding (pre-sync 2026-07-15-173001).md
- Theses/SPOT - Spotify.md → _Archive/Snapshots/SPOT - Spotify (pre-sync 2026-07-15-173001).md
- Theses/LYV - Live Nation Entertainment.md → _Archive/Snapshots/LYV - Live Nation Entertainment (pre-sync 2026-07-15-173001).md
- Theses/NVDA - Nvidia.md → _Archive/Snapshots/NVDA - Nvidia (pre-sync 2026-07-15-173001).md

## Theses with Log-only appends (Tier B)
- None. All five theses touched took Tier A snapshots (each involved rewriting existing analytical prose).

## Sector notes touched
- Sectors/Surgical Robotics.md (Tier A) → _Archive/Snapshots/Surgical Robotics (pre-sync 2026-07-15-173001).md — added §Industry History "The 2013 demand shock" (absent from the entire vault); first-populated §Mental Models per CHG-14 empty-scaffold exception
- Sectors/Athletic Footwear & Apparel.md (Tier B) — Related Research wikilink only; all 8 analytical sections remain `_pending_`

## Macro notes touched
- None. The macro-relevant residue (800VDC Adoption 4-phase model + regulatory gate; AI Bubble Risk EDA insulation stratum) was analysed and verified but NOT written — registered in `_followups.md` instead. See "Scope reality" below.

## Source research notes processed
Residue identified by the Step 1.7 idempotency scan: **20** of 76 changed research notes.

**Written this run (7):**
- 2026-07-14 - ISRG - Intuitive Surgical Business Breakdown - deep-dive → ISRG + Surgical Robotics (propagated_to backfilled)
- 2026-07-14 - LYV - Live Nation Business Breakdown - deep-dive → LYV + SPOT (propagated_to backfilled)
- 2026-07-14 - ONON - On Holding Business Breakdown - deep-dive → ONON + Athletic Footwear (propagated_to backfilled)
- 2026-06-06 - 800VDC Revolution Part 1 - deep-dive → NVDA (monopolar-800V correction only; VRT/VICR/sectors/macro registered in _followups)
- 2026-07-09 - Automation AI Readiness Lens - synthesis → propagated_to backfilled (SUPERSEDED — see below)
- 2026-07-09 - Value Layer Monopoly Lens - synthesis → propagated_to backfilled (SUPERSEDED — see below)
- 2026-07-11 - Gating Thresholds for AI Adoption → no propagation owed (raw Gemini source, no frontmatter; content carried by the propagated 2026-07-12 Enterprise AI Adoption synthesis)

**Analysed + verified but NOT written — registered in `_followups.md` (13):**
EDA Primer Pt1/Pt2 (→ TSM/INTC/AVGO/ARM/NVDA/AI-Bubble macro) · RDDT breakdown (→ PINS + Social Platforms sector) · GAW + TTWO breakdowns (→ GAW/TTWO + 2 sector notes) · 800VDC residue (→ VRT/VICR + 3 sectors + 800VDC macro) · AAPL/MCO breakdowns (no propagation warranted — links incidental) · MONC / Citadel / DE Shaw (Step 1.6 unresolved — no thesis, no sector note) · Silver + Commodity 2026 + India-Pak Defence (already superseded by the 2026-04-22 Precious Metals fill).

## Key finding: the two lens syntheses were FALSE residue
Both 2026-07-09 lens syntheses flagged as un-propagated because they have no `## Log` entry and no `propagated_to:`. They were in fact already applied via **2026-07-10 batch Mental Models passes** — one day *fresher* than the syntheses, using better evidence — and a **vault-wide `/status` scoreboard on 2026-07-11** then changed conviction on 5 of the VLM note's 20 names, in several cases executing or refuting the syntheses' own recommendations (WTC "understates" → already upgraded 07-11; NET "already HIGH" → downgraded *because* its stated variant perception was refuted by AWS x402). Propagating them wholesale would have been a regression. `propagated_to:` is now backfilled on both so no future sync re-flags them. The genuine residue is 8 specific structural gaps, registered in `_followups.md`.

## Scope reality (read this before trusting the counts above)
The run analysed all 20 residue notes at full spec depth via 8 read-only subagents, then hit its working limit after writing 7. Everything analysed-but-unwritten is in `_followups.md`, which never auto-evicts. `.last_sync` was advanced to 2026-07-15 **only because** that register exists — mtime cannot surface this work again (see the 2026-07-13 mass-mtime finding in the run context above).
