---
type: thesis-manifest
batch: thesis-SPCX-2026-08-13-124943
status: completed
completed_date: 2026-08-13
ticker: SPCX
proposed_name: SpaceX
proposed_path: Theses/SPCX - SpaceX.md
sector: Neoclouds & GPU-as-a-Service
date: 2026-08-13
---

# Thesis Transaction Manifest (in-progress)

Manifest written at Step 3.5 before any file modifications. **Rebuild-from-scratch run**: user chose to rebuild over the malformed-filename panel thesis `Theses/@SPCX - @SpaceX.md` (created earlier today by batch thesis-SPCX-2026-08-13-120215); that file will be archived and its inbound wikilinks repointed to the new canonical file. Intended operations:

## Thesis file creation
- Target path: `Theses/SPCX - SpaceX.md`
- Status: created ✓ (all 14 sections; Mental Models populated with G-3/4/5/7/10/12/13/14, VLM §1–3, Automation §2/§5, Semis #1/#10; conviction medium set after Bear Case per discipline)
- Note: carries forward `status: active` + `conviction: medium` from the superseded file per the user's same-day `/status SPCX draft→active` run (batch status-SPCX-2026-08-13-120952) — the rebuild replaces the analysis document, not the investment-state decisions.

## Predecessor archival (user-approved via rebuild choice)
- Move: `Theses/@SPCX - @SpaceX.md` → `_Archive/Theses/@SPCX - @SpaceX.md`
- Append supersession Log entry to predecessor before move; set `status: archived` on archived copy
- Status: archived ✓ (Log appended, status flipped, moved)

## Inbound wikilink repoint (@-name → canonical)
- `Sectors/Neoclouds & GPU-as-a-Service.md` Active Theses entry: repointed ✓
- `_hot.md` mentions (5): repointed ✓ (replace_all)
- `Live Portfolio.md` mention (1): §Notes line repointed ✓; §Log line 844 left untouched (append-only historical)
- Sector-note + predecessor `## Log` entries referencing the @-name are Tier 2 append-only and left untouched (bare wikilinks resolve to the archived file by name).

## Sector note update
- Sector resolution: exact (`Sectors/Neoclouds & GPU-as-a-Service.md` — filename literal match)
- Edit applied: active_theses_entry_repointed ✓

## `_hot.md` updates
- Active Research Thread entry: continuation line appended ✓ (same-ticker rule; web deltas + next step)
- Recent Conviction Changes entry: repointed ✓ (no new entry — initial-MEDIUM entry from prior run stands)
- Open Questions entries: #167–169 repointed ✓ (no new entries — cohort current)
- Word count: ~4,915 post-edit — over 4,000 soft cap (pre-existing), under 5,000 hard cap. Compression steps 1–4 had nothing actionable (empty Sync Archive, no *Previous:* lines, no >14d cohorts); step-7 warning raised in run report; standing "dedicated /sync cleanup" flag remains.

## Orphan research integration
- Orphan research notes touched: 1 — `Research/2026-08-05 - SPCX Shanaka Capital Recovery Clock - deep-dive.md` (sole `ticker:`/`tags:` SPCX match; mtime advanced past `.last_sync`)
- Wikilinks added to Related Research: 18 (sector note + 10 peer theses + 7 research notes)

## Archive-collision decision (Step 1.2)
- Archived theses found: none (Signals A/B/C/D/E all empty)
- User decision (non-canonical active-file collision, outside Step 1.2 taxonomy): rebuild from scratch + archive predecessor (AskUserQuestion 2026-08-13)

## Graph-primer peer decision (Step 2.5)
- Accepted set: CRWV, NBIS, NVDA, LITE, AMAT, LRCX, KLA, TSM, 000660, INTC ("prior curated set")

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed mid-run:
- **Skeleton only**: no thesis file yet; no sector or _hot.md edits; predecessor untouched at `Theses/@SPCX - @SpaceX.md`. Recovery: `rm` manifest; re-run `/thesis SPCX`.
- **Thesis file created, repoint/archival incomplete**: two SPCX thesis files may coexist (`Theses/SPCX - SpaceX.md` + `Theses/@SPCX - @SpaceX.md`). Recovery: complete remaining steps manually per manifest body (archive predecessor, repoint sector/_hot.md/Live Portfolio links) OR `rm` new thesis + manifest and re-run.
- **All steps landed but flip failed** (Step 7.5): manually edit frontmatter to `status: completed` + `completed_date: 2026-08-13`. Manifest ages out via `/lint #49`.

Flipped to `status: completed` at Step 7.5 after all stages succeed.
/lint #49 surfaces in-progress as Important.
