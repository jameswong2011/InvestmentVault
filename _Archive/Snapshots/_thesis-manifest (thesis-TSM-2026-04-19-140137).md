---
type: thesis-manifest
batch: thesis-TSM-2026-04-19-140137
status: completed
completed_date: 2026-04-19
ticker: TSM
proposed_name: Taiwan Semiconductor
proposed_path: Theses/TSM - Taiwan Semiconductor.md
sector: Semiconductors
date: 2026-04-19
---

# Thesis Transaction Manifest (completed)

Manifest written at Step 3.5 before any file modifications. Intended operations:

## Thesis file creation
- Target path: `Theses/TSM - Taiwan Semiconductor.md`
- Status: `created` (13 sections, ~4,200 words, conviction: medium, status: draft)

## Sector note update
- Sector resolution: `exact` (matched `Sectors/Semiconductors.md`)
- Sector note path: `Sectors/Semiconductors.md`
- Edit applied: `skipped (draft status)` — thesis will be added to Active Theses when promoted via `/status TSM status draft→active`

## `_hot.md` updates
- Active Research Thread entry: new thread "TSMC monopoly thesis initiated" — prior NVDA China thread compressed to *Previous:* line
- Recent Conviction Changes entry: "2026-04-19 — TSM initial conviction: MEDIUM" (replaced prior "[None recorded yet]" placeholder)
- Open Questions entries: 3 added (items 6, 7, 8 — CoWoS 2027 allocation, Intel 18A external customer, Arizona yield parity timing)

## Orphan research integration
- Orphan research notes touched: none (Grep `^ticker: TSM` and `^tags:.*TSM` in `Research/` returned zero matches — no orphan notes keyed to this ticker)
- Wikilinks added to Related Research: 3 (Huawei Ascend roadmap, Hybrid Bonding/BESI, NVDA Jensen Huang interview) — these were existing research notes linked in the Related Research section, not auto-integrated orphans

## Archive-collision decision (if Step 1.2 found matches)
- Archived theses found: none
- User decision: n/a (no archived thesis for TSM)

## Recovery guidance

If this file persists with `status: in-progress`, /thesis crashed or was
interrupted mid-run. Likely partial states:

- **Skeleton written only** (this case): no thesis file exists yet; no sector
  or _hot.md edits. Recovery: `rm` this manifest; re-run `/thesis TSM`.
- **Thesis file created, sector/hot.md incomplete**: the thesis exists at
  `Theses/TSM - Taiwan Semiconductor.md` but is disconnected from sector note
  and _hot.md. Recovery: either (a) manually complete the remaining steps
  per the manifest body's intended operations, OR (b) `rm` the thesis file
  and the manifest, then re-run `/thesis TSM`.
- **All steps landed but flip to completed failed** (Step 8): manually edit
  frontmatter to `status: completed` + add `completed_date: YYYY-MM-DD`,
  then leave the manifest for its 90-day aging window per `/lint #49`.

Flipped to `status: completed` at Step 8 (final) after all stages succeed.
/lint #49 surfaces in-progress manifests as Important.
