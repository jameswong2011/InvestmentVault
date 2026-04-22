---
type: sync-manifest
batch: sync-2026-04-22-145012
status: completed
completed_date: 2026-04-22
mode: default-followup
date: 2026-04-22
parent_batch: sync-2026-04-22-144403
---

# Sync Batch Manifest (completed) — follow-up sector propagation

Manifest written at Step 2.9 before any file modifications.

## Reason this follow-up run exists

The prior `/sync` at batch `sync-2026-04-22-144403` misapplied Step 2's source-deduplication clause to suppress Step 4 (sector propagation). Step 4.-1's gate requires BOTH (i) every affected thesis in `skill_origin_theses` AND (ii) no research note in the changed-file set resolves to the sector. Condition (ii) fails for Cybersecurity: [[Research/2026-04-21 - CRWD vs PANW - Competitive Comparison]] has `sector: Cybersecurity` frontmatter + `[[Sectors/Cybersecurity]]` body wikilink. Step 4 therefore should have fired. The prior run left the sector note with stale content on three distinct analytical dimensions the CRWD thesis makes explicit.

## Changed files in scope

- [[Sectors/Cybersecurity]] — Tier A target (deep analytical edits planned)
- Source theses/research unchanged since 144403; no thesis Log appends or macro edits this run.

## Step 2 analytical delta — insights missed by prior sync

Three sector-level insights from [[Theses/CRWD - CrowdStrike Holdings]] Non-consensus Insights section + [[Research/2026-04-21 - CRWD vs PANW - Competitive Comparison]] that are NOT captured in the sector note's current Key Dynamics:

1. **Architectural purity cannot be acquired** — single-agent vs five-pillar federation is a structural cost substrate dynamic, not a deployment convenience. Prior sync captured "single-agent architecture" as a phrase inside the best-of-breed bullet; missed the sector-level framing that this moat compounds every quarter a new module ships on the existing agent AND cannot be retrofitted via M&A (only rebuilt from scratch, 5-year exposure window).
2. **Commercial-model divergence as GM-durability dynamic** — Falcon Flex ($1.69B ARR, +120%, 27% of ending ARR) is consumption-pricing architecturally, not just a renewal-flexibility feature. Preserves list-price economics on module expansion. PANW platformization accepts margin compression (77%→74-75% GM) in exchange for lock-in. Two structurally different answers to consolidation — absent from sector note.
3. **Integration-risk asymmetry in M&A discipline** — PANW's 4 simultaneous mega-integrations ($25B CyberArk, $3.35B Chronosphere, IBM QRadar SaaS, Koi) vs CRWD's <$2B tuck-in discipline over 5 years represents a sector-level execution-risk divergence. 60%+ historical mega-deal underperformance rate (HP-Autonomy, Broadcom-VMware reference class) makes this a probability-weighted 2-4qtr relative-execution drag on PANW. Absent.

## Step 3 thesis updates

None. Thesis propagation was correctly resolved in the parent batch.

## Step 4 sector updates — planned

- [[Sectors/Cybersecurity]] — Tier A edit:
  - Add 3 new Key Dynamics bullets covering the three insights above.
  - Append Log entry for 2026-04-22 documenting the propagation.
  - Snapshot: `_Archive/Snapshots/Cybersecurity (pre-sync 2026-04-22-145012).md` (taken before edits; populated below).

## Step 5 macro updates

None. CRWD thesis has no `[[Macro/...]]` wikilinks; comparison research note has no Macro targets.

## Step 6 _hot.md updates — planned

- Replace Latest Sync with this batch's summary.
- Prepend the 144403 Latest Sync entry to Sync Archive.
- Update header + frontmatter date (already today's date; no change).
- No Active Research Thread / Recent Conviction Changes / Open Questions edits — this is a propagation correction, not new investment-decision content.

## Recovery guidance

If this file persists with `status: in-progress`, the follow-up sync crashed mid-run:
- Sector snapshot at `_Archive/Snapshots/Cybersecurity (pre-sync 2026-04-22-145012).md` is the rollback target; `/rollback` will find it via batch ID `sync-2026-04-22-145012`.
- Thesis notes are unmodified; only the sector note + `_hot.md` may be in partial state.

Flipped to `status: completed` at Step 7.5 after all edits land.
