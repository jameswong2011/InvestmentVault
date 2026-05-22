---
sync_batch: sync-2026-05-11-110651
status: completed
started_at: 2026-05-11T11:06:51Z
completed_at: 2026-05-11T11:28:55Z
completed_date: 2026-05-11
mode: /sync
watermark_before: 1970-01-01T00:00:00Z (epoch placeholder)
watermark_after: 2026-05-11T11:28:55Z
source_notes_changed:
  - Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive.md
---

# Sync manifest — sync-2026-05-11-110651

## Source notes (changed since watermark, HBM-relevant subset)

| Source | Type | Primary ticker | Sector targets | Macro targets |
|---|---|---|---|---|
| `Research/2026-05-11 - HBM Packaging Equipment Stack - MR-MUF to Hybrid Bonding Transition - deep-dive.md` | deep-dive | 000660.KS | DRAM & HBM Memory; Semiconductor Capital Equipment | AI Bubble Risk and Semiconductor Valuations |

Other files modified today (Indian Financials, BDCs, ServiceNow, Palantir, etc.) are unrelated to this HBM source; they are not in scope for this sync run.

## Step 2.5 skill-origin classification

- `skill_origin_theses`: ∅ (empty) — all 9 thesis targets resolve via HBM research note wikilinks; mixed log_tail classifications fall to research-driven per spec.

## Step 1.7 idempotency

- `wikilink_match_set` = ∅ for HBM research note (note created in this session; no prior Log references).
- `propagated_to:` frontmatter: absent at source note write time → Case 2a (no producer-side dedup).

## Step 1.2.5 target maps

- `sector_targets_per_research_note[HBM-deep-dive]`: `Sectors/DRAM & HBM Memory.md`, `Sectors/Semiconductor Capital Equipment.md`
- `macro_targets_per_research_note[HBM-deep-dive]`: `Macro & Technology/AI Bubble Risk and Semiconductor Valuations.md`

## Affected files

### Tier A (snapshot required — substantive analytical section edits)

#### Theses

| File | Snapshot path | Sections to edit |
|---|---|---|
| `Theses/000660 - SK Hynix.md` | `_Archive/Snapshots/000660 - SK Hynix (pre-sync 2026-05-11-110651).md` | Risks (new #10 Namics); Bull Case (MR-MUF extension); Bear Case (HBM5 timing); Industry Context (HBM4 vendor confirmations); Outstanding Questions (Q2 partial resolution); Conviction Triggers (calibration); Related Research; Log |
| `Theses/BESI - BE Semiconductor Industries.md` | `_Archive/Snapshots/BESI - BE Semiconductor Industries (pre-sync 2026-05-11-110651).md` | Industry Context (Q1 26 +28.3%; March 26 SK Hynix Kinex order context); Bull Case (data validation); Bear Case (order-softness retroactive explanation); Related Research; Log |
| `Theses/AMAT - Applied Materials.md` | `_Archive/Snapshots/AMAT - Applied Materials (pre-sync 2026-05-11-110651).md` | Bull Case #2 (HBM4 Kinex ramp validation); Industry Context (etch revenue); Related Research; Log |
| `Theses/LRCX - Lam Research.md` | `_Archive/Snapshots/LRCX - Lam Research (pre-sync 2026-05-11-110651).md` | Bull Case (Aether/AP data confirmation); Industry Context (DRAM mix); Related Research; Log |
| `Theses/TSM - Taiwan Semiconductor.md` | `_Archive/Snapshots/TSM - Taiwan Semiconductor (pre-sync 2026-05-11-110651).md` | Industry Context (HBM4 base-die wins at 2 of 3 IDMs); Related Research; Log |

#### Sectors

| File | Snapshot path | Sections to edit |
|---|---|---|
| `Sectors/DRAM & HBM Memory.md` | `_Archive/Snapshots/DRAM & HBM Memory (pre-sync 2026-05-11-110651).md` | Macro Shifts (new §8 materials moat); Competitive Dynamics (packaging hierarchy update with Kinex order context); Investor Heuristics #2 (MR-MUF extension); Related Research; Log |
| `Sectors/Semiconductor Capital Equipment.md` | `_Archive/Snapshots/Semiconductor Capital Equipment (pre-sync 2026-05-11-110651).md` | Macro Shifts (equipment-beneficiary bifurcation); Competitive Dynamics (Hanmi/ASMPT/Disco/Towa share confirmation); Product-Level Analysis (Advanced Packaging table update); Related Research; Log |

#### Macro

| File | Snapshot path | Sections to edit |
|---|---|---|
| `Macro & Technology/AI Bubble Risk and Semiconductor Valuations.md` | `_Archive/Snapshots/AI Bubble Risk and Semiconductor Valuations (pre-sync 2026-05-11-110651).md` | Body section (HBM equipment-cohort short-circuit on $650B threshold); Related Theses; Log |

### Tier B (no snapshot — Log + minor mechanical edits only)

| File | Edits |
|---|---|
| `Theses/NVDA - Nvidia.md` | Related Research wikilink + Log entry (Vera Rubin HBM4 split corroboration + HBM supply risk note) |
| `Theses/AMD - Advanced Micro Devices.md` | Related Research wikilink + Log entry (MI400/MI450 HBM4 supplier diversification) |
| `Theses/AVGO - Broadcom.md` | Related Research wikilink + Log entry (Samsung HBM3E 8-Hi lifeline via TPU/Apple/OpenAI) |
| `Theses/KLA - KLA Corporation.md` | Related Research wikilink + Log entry (bump-pitch tightening + HBM4 16-Hi 3x inspection intensity corroboration) |

## Step 6 `_hot.md`

Composite edit: prepend Sync Archive entry summarising this run; refresh Active Research Thread to HBM packaging stack; update Latest Sync to 2026-05-11.

## Step 7 watermark

Touch `.last_sync` at completion (default `/sync` mode).

## Checkpoints

- [x] Checkpoint A — Step 3 thesis edits complete (5 Tier A substantive + 4 Tier B Log+wikilink = 9 Log appends)
- [x] Checkpoint B — Step 4 sector edits complete (2 sectors, both Tier A)
- [x] Checkpoint C — Step 5 macro edit complete
- [x] Checkpoint D — Step 6 `_hot.md` composite edit
- [x] Checkpoint E — Step 7 `.last_sync` touched; Step 7.5 manifest flip

## Failures / skips

(populated at Step 8)
