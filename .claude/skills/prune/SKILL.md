---
name: prune
description: Systematically evaluate weak, stale, or low-conviction theses for upgrade, monitoring, or closure. Use when user says "prune", "kill list", "clean up theses", "what should I close", or "reduce portfolio".
model: opus
effort: max
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Edit Write Bash(date * find * wc * mv * cp * mkdir * rm *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Systematically evaluate the thesis portfolio and recommend what to keep, upgrade, or kill. Be ruthless — cognitive overhead of tracking weak positions has a real cost.

## Scope Resolution

Parse `$ARGUMENTS` to determine scope. Arguments can be combined (e.g., `/prune semiconductors stale`):

- **Sector** (e.g., `semiconductors`): Only evaluate theses with matching `sector:` frontmatter.
- **Flag filter** (e.g., `stale`, `low`, `draft`): Pre-filter before reading full notes:
  - `stale` → only theses with last Log entry >60 days old
  - `low` → only theses with `conviction: low` frontmatter
  - `draft` → only theses with `status: draft` frontmatter
  - `monitoring` → only theses with `status: monitoring` frontmatter
- **No arguments / empty**: Evaluate all theses (current behaviour).

Pre-filtering method: Grep `Theses/` frontmatter for the relevant field before reading full notes. This avoids loading 39+ files when only a subset matches.

## Phase 0: Pre-flight — Check for Unsynced Research

Before evaluating any theses, check whether unsynced research exists:
```bash
find Research/ Theses/ Macro/ Sectors/ -newer .last_sync -name '*.md' 2>/dev/null
```

If `.last_sync` does not exist, skip this check (first-run state — no baseline to compare against).

If changed files are found, warn the user before proceeding:
```
⚠️ Unsynced research detected ([N] files modified since last /sync):
  [list files]

Running /prune before /sync risks archiving theses before recent research insights
have been propagated. Recommended: run /sync first, then re-run /prune.

Proceed anyway? (y/n)
```

**Do NOT proceed without explicit user confirmation.** If the user declines, stop and suggest `/sync`.

## Phase 1: Identify Candidates (Two-Pass Triage)

**If scoped**: Read only thesis notes matching the scope filter(s) from Scope Resolution. Apply the flag criteria below only to the scoped set. (Scoped sets are typically small enough that full reads are fine — skip the two-pass triage.)

**If unscoped (Two-Pass Triage):**

Reading all ~40 thesis notes in full will exceed context limits. Most flag criteria can be assessed from frontmatter + Log alone. Use a lightweight scan to triage, then deep-read only flagged candidates in Phase 2.

### Pass 1 — Lightweight scan
1. For each thesis in Theses/, read **only frontmatter + Related Research section + Catalysts section + Log section** (stop before Summary, Non-consensus Insights, Business Model, Industry Context, Bull/Bear Case, etc.). This yields ~200-400 words per thesis — manageable for the full set.
2. From this lightweight read, apply ALL flag criteria:

| Flag | Criteria | Assessed from |
|------|----------|---------------|
| 🟡 Low conviction | `conviction: low` in frontmatter | frontmatter |
| 🟡 Monitoring | `status: monitoring` in frontmatter | frontmatter |
| 🔴 Stale | Last Log entry is >60 days old | Log dates |
| 🔴 Very stale | Last Log entry is >120 days old | Log dates |
| 🟡 Thin research | Fewer than 3 research notes linked | Related Research section |
| 🟡 Draft limbo | `status: draft` with only 1 Log entry (created but never developed) | frontmatter + Log entry count |
| 🟡 Orphaned from sector | Not referenced in its Sector Note | deferred — check in Pass 2 |
| 🔴 No catalyst | Catalysts section is empty or all dates have passed | Catalysts section |

3. Also flag: high conviction theses with stale research (last Log entry >90 days old despite `conviction: high`)

### Pass 2 — Deep read flagged candidates only
4. For each thesis flagged in Pass 1 → proceed to Phase 2 (read full note there).
5. For each UNFLAGGED thesis, check the one deferred flag (orphaned from sector) by cross-referencing the thesis ticker against its Sector Note's Active Theses section. If the flag triggers, add to the flagged set.
6. Unflagged theses that pass all checks are excluded from Phase 2 entirely — no further reads needed.

This typically reduces full reads from ~40 files to 10-20 depending on portfolio health.

Also flag theses that are NOT on this list but should be reviewed:
- High conviction theses with stale research (>90 days since last research note)
- Theses where the Sector Note has been updated significantly but the thesis Log hasn't reflected it

## Phase 2: Assess Each Candidate
For each flagged thesis, read the full note and its supporting research. Assess:

1. **Evidence trajectory**: Has the evidence been strengthening, weakening, or going stale since creation?
2. **Thesis integrity**: Does the original non-consensus insight still hold? Has the market moved toward or away from the thesis?
3. **Opportunity cost**: Is research time on this thesis coming at the expense of higher-conviction ideas?
4. **Catalyst horizon**: Is there a specific upcoming event that could reignite the thesis?
5. **Vault connectivity**: Is this thesis well-connected to the rest of the portfolio (wikilinks, sector note presence, macro relevance) or is it an isolated bet?

## Phase 3: Recommendation
For each candidate, recommend ONE of:

### ⬆️ UPGRADE
- Evidence has quietly strengthened
- Recent research or sector developments support the thesis but haven't been reflected in conviction
- Specify: new conviction level, what justifies it, what Log entry to add

### ➡️ KEEP MONITORING
- Thesis is still valid but needs a specific trigger before it becomes actionable
- Specify: the exact trigger to watch for (make it falsifiable and time-bounded)
- Specify: a review date — if the trigger hasn't fired by then, downgrade to CLOSE

### ⬇️ CLOSE
- Evidence has weakened, the insight has been absorbed by consensus, no catalyst exists, or the thesis was never properly developed
- Specify: one-line rationale for closure
- Offer to move to _Archive/ with a final Log entry

## Phase 4: Portfolio Health Summary

### Recommendation Table
| Ticker | Company | Current Status | Current Conviction | Flag(s) | Recommendation | Rationale |
|--------|---------|---------------|-------------------|---------|---------------|-----------|
| | | | | | ⬆️/➡️/⬇️ | [one line] |

### Portfolio Stats
- Total theses: X
- Active / Draft / Monitoring: X / X / X
- Flagged for review: X
- Recommended closures: X
- Recommended upgrades: X
- Average thesis age (days since last Log): X
- Theses with no catalyst: X

### Attention Allocation Insight
- What % of theses are high-conviction? Is this appropriate or should more be pruned?
- Are there sectors with too many thin theses that should be consolidated?
- Which 3 theses deserve MORE research time based on conviction + evidence strength?

## Phase 5: Execute (WITH USER APPROVAL) — Atomic Batch

**Do NOT auto-execute. Present the table and wait for user confirmation.**

Execution uses an **atomic batch** approach: all safety snapshots are created before any destructive modifications begin. This ensures that if the skill fails mid-execution, every affected file can be recovered via `/rollback` (cascade detection will find them all via matching `snapshot_batch`).

The batch has five sequential stages. Each stage completes fully before the next begins:
1. **Snapshot** all affected files (safety net)
2. **Close** all approved theses (log + status + move)
3. **Upgrade** all approved theses (frontmatter + log)
4. **Update** all affected sector notes
5. **Update** graph and hot cache

### Stage 1: Snapshot ALL Affected Files

Generate a single batch ID for the entire prune run:
```bash
HHMM=$(date +%H%M)
mkdir -p _Archive/Snapshots
```
Use `prune-YYYY-MM-DD-$HHMM` as the `snapshot_batch` value for ALL snapshots below.

**Thesis snapshots** — one per approved closure AND one per approved upgrade:
```bash
cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-prune YYYY-MM-DD-HHMM).md"
```
Read each newly created snapshot and add to its frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - Company Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: prune
snapshot_batch: prune-YYYY-MM-DD-HHMM
```

**Sector note snapshots** — one per affected sector note (any sector that will have a thesis removed or a conviction level updated). Resolve affected sectors using the canonical procedure **`.claude/skills/_shared/sector-resolution.md`** for each approved thesis's `sector:` frontmatter. Deduplicate the resolved set, then snapshot each unique sector note:
```bash
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-prune YYYY-MM-DD-HHMM).md"
```
Read each newly created snapshot and add `snapshot_of: "[[Sectors/Sector Name]]"`, `snapshot_date`, `snapshot_trigger: prune`, `snapshot_batch: prune-YYYY-MM-DD-HHMM` to its frontmatter.

> If `match_confidence` is `none` for a thesis's sector value, emit the contract's no-match warning suffixed with `Skipping sector snapshot for [TICKER].` — sector update for that thesis will also be skipped in Stage 4. If `match_confidence` is `normalized` or `substring` for any thesis, collect the contract's `log_message` for the final report.

**Abort gate**: If any snapshot creation fails (file not found, write error), **STOP immediately**. No destructive modifications have been made — the vault is in its original state. Report: `❌ Snapshot failed for [file]. Prune aborted — no changes made. Fix the issue and re-run /prune.`

### Stage 1.5: Write Batch Manifest

Create a manifest note that persists if the session crashes mid-execution. This is the discovery mechanism for partial prune operations — without it, a session crash between Stages 2–5 leaves the vault in a mixed state that requires `/lint` to diagnose.

```bash
# Reuse the HHMM from Stage 1
```

Write `_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMM).md`:
```yaml
---
type: prune-manifest
batch: prune-YYYY-MM-DD-HHMM
status: in-progress
date: YYYY-MM-DD
---
```

Body — list every intended action:
```markdown
# Prune Batch Manifest

> **If this file exists, a `/prune` operation did not complete successfully.**
> Recovery: `/rollback [any ticker below]` → select `(pre-prune)` snapshot → cascade (a) to undo all completed actions.
> Then delete this manifest and re-run `/prune`.

## Intended Closures
- TICKER1 - Company1
- TICKER2 - Company2

## Intended Upgrades
- TICKER3 - Company3 (conviction low → medium)

## Affected Sector Notes
- Sector Name (closures: TICKER1, TICKER2; upgrades: TICKER3)
```

This file is deleted at the end of Phase 5 after all stages succeed (see Stage 5 below).

### Stage 2: Process ALL Thesis Closures

For each approved closure:
1. Add final Log entry: `### YYYY-MM-DD\n- CLOSED: [rationale]. Archived.`
2. Change frontmatter: `status: closed`
3. Move file to `_Archive/`:
   ```bash
   mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
   ```

Do NOT update sector notes here — batched in Stage 4.

**If a closure fails mid-stage**: Report which closures completed and which failed. All pre-prune snapshots from Stage 1 are available for recovery. The batch manifest from Stage 1.5 persists and records all intended actions:
```
⚠️ Closure failed for [TICKER] at step [N]. Completed: [list]. Failed: [list]. Pending: [list].
All pre-prune snapshots available (batch: prune-YYYY-MM-DD-HHMM).
Batch manifest: [[_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMM)]]
To recover: /rollback [any affected ticker] → select (pre-prune) snapshot → choose cascade (a) to restore all.
Sector notes have NOT been modified — no sector inconsistency from this partial failure.
After recovery, delete the batch manifest.
```
**If the session crashes** (no error message delivered): the manifest persists in `_Archive/Snapshots/` with embedded recovery instructions. The user or `/lint` can discover it on the next session.

### Stage 3: Process ALL Upgrades

For each approved upgrade:
1. Update `conviction:` in frontmatter
2. Add Log entry (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Prune upgrade [old] → [new]: [what justified the upgrade] — conviction strengthened, [reason]
   ```

### Stage 4: Update ALL Sector Notes

For each affected sector note (identified in Stage 1):
1. Read the current sector note
2. **Closures**: Remove archived theses from the Active Theses section. If a "Closed/Archived" section exists, add them there
3. **Upgrades**: If the sector note displays conviction levels alongside thesis links, update to reflect the new levels

Do NOT rewrite wikilinks across the vault — `/lint` will detect broken links from the archive moves. Report expected breakages: `⚠️ [N] notes contain wikilinks to archived theses. Run /lint to review.`

> **Why sector notes are updated last**: Stages 2–3 modify thesis files only. If the skill fails during Stages 2–3, sector notes remain untouched and internally consistent — they still reference the original thesis paths. The snapshots from Stage 1 enable full cascade recovery. Only after all thesis modifications succeed do sector notes get updated.

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to update the dependency map for archived theses (Adjacency Index removal, reverse-index cleanup, ghost cross-thesis ref scrubbing, orphan reclassification of research notes that were only linked from archived theses).

Update `_hot.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: pruned portfolio — [N] closed, [N] upgraded, and the logical next step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry for each ticker where conviction was upgraded; add entry for each closure
3. **Open Questions**: Remove questions related to closed theses; add any new questions raised by upgrades
4. **Portfolio Snapshot**: Update conviction-level counts and sector coverage if materially changed

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

### Manifest Cleanup

All stages completed successfully. Delete the batch manifest:
```bash
rm "_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMM).md"
```
If the manifest delete fails, warn but do not abort — the manifest is a diagnostic artifact, not vault content. `/lint` or the user can clean it up.

Report final count of actions taken.
