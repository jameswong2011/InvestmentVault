---
name: status
description: Change conviction level or status on a single thesis. Use when user says "change conviction", "downgrade", "upgrade", "move to monitoring", "close [TICKER]", or "set [TICKER] to [level]".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * cp * mkdir * mv * find * grep * cat * sort * printf * ls *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Execute a conviction or status change on a single thesis. This is the atomic operation that closes the loop after `/stress-test`, `/scenario`, `/deepen`, `/compare`, or any manual reassessment.

## Arguments

$ARGUMENTS should follow one of these patterns:

**Conviction or status change**: `TICKER field old→new [rationale]`
- `NVDA conviction medium→low China risk unhedgeable`
- `BESI status active→monitoring awaiting Q3 earnings`
- `LITE conviction low→medium photonics design wins accelerating`
- `SHOP status active→closed thesis invalidated by margin compression`

**Drift acknowledgment**: `TICKER reaffirm [rationale]`
- `NVDA reaffirm earnings miss was one-time; competitive position unchanged`
- `BESI reaffirm hybrid bonding thesis intact despite cycle weakness`

If $ARGUMENTS is ambiguous or incomplete, ask the user to clarify the ticker, field, direction, and rationale before proceeding.

If $ARGUMENTS matches the `reaffirm` pattern, skip to **Step 2R (Reaffirm Flow)** below.

## Step 0: Pre-flight (MANDATORY)

### 0.1: Acquire vault lock

Acquire a `ticker:TICKER` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 3 minutes (closure may take longer if sector note edits cascade — extend to 5m if `status → closed`). Capture the token at Step 0.1, verify ownership (Procedure 1.5) at every subsequent Bash block, release in the final reporting Bash block. If another skill holds a conflicting lock, abort with the collision message from Procedure 1.4.

### 0.2: Rename-marker pre-flight

Run `.claude/skills/_shared/preflight.md` Procedure 2. If `.rename_incomplete.TICKER` exists at vault root, hard-block per the contract's 2.3 collision message. This skill does not proceed on a thesis mid-rename repair because:
- Sector note edits would keep referencing the prior name if sector note wikilinks weren't in the successful Edit set
- `/status active→closed` archive move would strand the still-wrong-named inbound wikilinks
- `_hot.md` mentions would inherit whichever name `/status` finds, compounding split state

User must complete or explicitly abandon the rename first (see Procedure 2.3 options).

## Step 1: Validate

1. **Find the thesis**: Search `Theses/` for a file matching the ticker. If not found, stop: `⚠️ No thesis found for [TICKER] in Theses/. Nothing to update.`
2. **Read the full thesis note** to understand current state.
3. **Verify current value**: Confirm the `old` value in $ARGUMENTS matches the actual frontmatter. If it doesn't, stop and report the mismatch: `⚠️ Expected [field]: [old] but found [field]: [actual]. Confirm the intended change.`
4. **Parse the change type**:
   - `conviction` change → proceed to Step 2
   - `status` change to `closed` → proceed to Step 2 (will trigger archive flow)
   - `status` change to anything else (`active→monitoring`, `draft→active`, `monitoring→active`) → proceed to Step 2

## Step 2R: Reaffirm Flow (drift acknowledgment)

**Only entered when $ARGUMENTS matches `TICKER reaffirm [rationale]`.** This is a lightweight operation — no frontmatter change, no snapshot, no sector/graph update.

**Reaffirm is idempotent-safe.** It can be run even if no drift flag is currently active — the operation always appends a Log entry for audit trail completeness and always resets the drift detection window (resetting an already-clean window is harmless). The operation is safe to run at any time to proactively confirm conviction.

1. **Find and read the thesis** (same as Step 1.1–1.2).
2. **Extract drift context and classify state**:
   - Scan the last 5 Log entries. Identify entries with "weakened" or "strengthened" sentiment. Count the drift pattern.
   - Scan `_hot.md`'s `## Recent Conviction Changes` section for a recent drift flag entry matching this TICKER (e.g., `⚠️ Conviction drift — [TICKER]: ...`). Record whether an active flag exists.
   - **drift_flag_active: true | false**
3. **Present the evidence summary and wait for confirmation**:

   **If drift_flag_active = true:**
   ```
   Drift review for [[Theses/TICKER - Company Name]]:
     Current conviction: [level]
     Active drift flag: [flag text from _hot.md, dated YYYY-MM-DD]
     Recent log sentiment:
       - YYYY-MM-DD: [summary] — [weakened/strengthened/unchanged]
       - YYYY-MM-DD: [summary] — [weakened/strengthened/unchanged]
       - ...
     Drift signal: [N]/[window] entries flagged headwinds (or tailwinds)

     Reaffirming conviction at [level] with rationale: [from $ARGUMENTS]
     This resets the drift detection window AND clears the drift flag.

   Confirm? (y/n)
   ```

   **If drift_flag_active = false:**
   ```
   Proactive reaffirm for [[Theses/TICKER - Company Name]]:
     Current conviction: [level]
     Active drift flag: none
     Recent log sentiment:
       - YYYY-MM-DD: [summary] — [weakened/strengthened/unchanged]
       - ...

     Reaffirming conviction at [level] with rationale: [from $ARGUMENTS]
     No active drift to clear — Log entry recorded for audit trail.
     The drift detection window anchor advances regardless.

   Confirm? (y/n)
   ```
   **Do NOT proceed without explicit user confirmation.**
4. **Append Log entry** (MANDATORY regardless of drift state — max 2 lines):
   ```
   ### YYYY-MM-DD
   - Conviction reaffirmed at [level] after [drift review | proactive review] — [rationale from $ARGUMENTS]
   ```
   Use `drift review` in the prefix when `drift_flag_active = true`, `proactive review` otherwise. The canonical `"Conviction reaffirmed"` prefix is preserved in both cases (drift coupling registry §5 relies on the prefix, not the suffix).
   > **Drift coupling**: `/sync` Step 3e uses `"Conviction reaffirmed"` as a drift window anchor. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §5. Do not change this prefix without updating the registry and `/sync`; `/lint` check #29 flags drift.

   > **Why always-log**: the prior spec suggested the reaffirm was "lightweight" which some implementations interpreted as "skip Log entry when no drift flag exists." That created an audit gap — a user's proactive conviction reaffirmation left no trace in the Log. The resulting audit story was "user never reviewed this thesis" even when they explicitly did. Always writing the Log entry closes that gap; the tiny overhead is worth the auditability.

5. **Update _hot.md** (read first, then edit — do NOT touch Latest Sync or Sync Archive; follow `.claude/skills/_shared/hot-md-contract.md`):
   - **Recent Conviction Changes**: Add entry: `- **[TICKER]**: conviction [level] reaffirmed — [rationale]`
   - **Drift flag cleanup** (only if `drift_flag_active = true`): locate the active drift flag entry for this TICKER and mark it resolved inline (`⚠️ Conviction drift — [TICKER] ... → Resolved YYYY-MM-DD: reaffirmed ([level])`). This prevents the stale drift flag from re-appearing as an Open Question on the next `/sync`.

6. **Report**:
   - **Reaffirmed**: [TICKER] conviction [level] maintained
   - **Drift state at entry**: `active flag cleared (from YYYY-MM-DD)` | `no active flag — proactive reaffirm recorded for audit trail`
   - **Log entry appended**: 1 line (`Conviction reaffirmed`)
   - **Drift window reset**: next /sync will anchor drift detection after this entry
   - **No snapshot, sector, or graph changes**

**Stop here — do not continue to Step 2 or beyond.**

---

## Step 2: Confirm (Tier 3 — Mandatory)

Present the proposed change and **wait for user confirmation** before proceeding:

```
Proposed change:
  Thesis: [[Theses/TICKER - Company Name]]
  Field: [conviction | status]
  Change: [old] → [new]
  Rationale: [from $ARGUMENTS]
  Side effects: [list what will be updated — sector note, archive move, graph cleanup]

Confirm? (y/n)
```

**Do NOT proceed without explicit user confirmation.** These are investment decisions per CLAUDE.md Tier 3.

## Step 3: Snapshot

### 3.0: Generate batch ID (always)

Generate `HHMMSS` once at the start of this step (6-digit second-precision prevents same-minute batch collisions across skills):
```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
```
Use `status-TICKER-YYYY-MM-DD-$HHMMSSSS` as the `snapshot_batch` value across **all** snapshots created in this run (thesis snapshot in Step 3.1, sector note snapshot in Step 5a). Reusing a single batch ID lets `/rollback` cascade detection restore both files atomically as a single operation.

> **Batch ID format (C4 fix)**: ticker qualifier prevents collisions when two concurrent `/status` runs on different tickers hit the same HHMMSS. Prior `status-YYYY-MM-DD-HHMMSS` could collide between simultaneous `/status NVDA conviction...` and `/status AMAT status...`; new `status-NVDA-YYYY-MM-DD-HHMMSS` and `status-AMAT-YYYY-MM-DD-HHMMSS` are distinct.

> **Draft→active note**: The batch ID is still generated even when Step 3.1 is skipped — Step 5a needs it for the sector note snapshot.

### 3.0.5: Write status transaction manifest skeleton (T2.2 fix)

**Mandatory BEFORE any file modifications** — Step 3.1 thesis snapshot, Step 4 frontmatter edit, Step 5 sector note edit, Step 7.5 archive move, Step 7.6 invalidation write are ALL gated on this skeleton landing first. Like `/sync` Step 2.9 and `/prune` Stage 1.5, the manifest skeleton is the first mutation of the run.

Write `_Archive/Snapshots/_status-manifest (status-YYYY-MM-DD-HHMMSS).md`:

```yaml
---
type: status-manifest
batch: status-YYYY-MM-DD-HHMMSS
status: in-progress
ticker: TICKER
transition_type: conviction | status | reaffirm
field: conviction | status
old_value: [parsed from $ARGUMENTS]
new_value: [parsed from $ARGUMENTS]
date: YYYY-MM-DD
---

# Status Transaction Manifest (in-progress)

Manifest written at Step 3.0.5 before any file modifications. Intended edits:

## Thesis frontmatter edit
- Target: `Theses/TICKER - Name.md`
- Field: [conviction | status]
- Change: [old] → [new]
- Snapshot taken: (to be populated in Step 3.1 — or "skipped (draft→active)")

## Sector note edit (if applicable per Step 5.1 dry-run)
- Resolution: (to be populated)
- Edit planned: yes | no | skipped (no match)
- Snapshot taken: (to be populated in Step 5a)

## Archive move (closure only)
- Source: `Theses/TICKER - Name.md`
- Target: `_Archive/TICKER - Name.md`
- Status: (to be populated in Step 7.5)

## Graph invalidations (closure only)
- Neighbors queued: (to be populated in Step 7.6)

## Archive registry append (closure only)
- Line added to `.archive_ticker_registry.md`: (to be populated in Step 7.5b)

## _hot.md edits
- (to be populated in Step 7)

## Recovery guidance

If this file persists with `status: in-progress`, /status crashed or was
interrupted mid-run. Likely states:

- (a) Skeleton written but no other edits landed → thesis still has original
      frontmatter; no recovery needed; manually `rm` this manifest.
- (b) Thesis frontmatter edited but subsequent steps failed → /rollback
      [snapshot_batch] restores pre-status thesis state.
- (c) Partial closure (thesis moved to _Archive/ but sector note not updated)
      → /rollback handles via the thesis snapshot + sector note snapshot.

Flipped to `status: completed` at Step 8 (final) after all stages succeed.
/lint #48 (new) surfaces in-progress manifests as Important.
```

**Skeleton write failure — hard abort**: if this Edit/Write fails, do NOT proceed to Step 3.1. Report:

```
❌ Status transaction manifest skeleton write failed: [path]
   Reason: [error]
No vault state has been modified. The thesis, sector note, and _hot.md are
unchanged. Fix the underlying filesystem issue and re-run /status.
```

Exit the skill. Reaffirm flow (Step 2R) does NOT need a manifest — it's a single Log append with no multi-file transaction; 2R skips Step 3.0.5 entirely.

**Incremental population**: each subsequent step (3.1, 4, 5a, 7.5, 7.6) appends its completion state to the manifest via `Edit`. This keeps the manifest current — if the session crashes after Step 5a but before 7.5, the manifest reflects the thesis and sector edits but not the archive move.

### 3.1: Thesis snapshot

Create a pre-change snapshot (conviction and most status changes are Tier A edits on the thesis body):

```bash
cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-$HHMMSS).md"
```

Read the newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - Company Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMMSS
```

**Exception**: Skip the thesis snapshot for `status: draft→active` (no analytical content is being changed on the thesis body — only the status frontmatter field is flipped). The sector note snapshot in Step 5a still runs, because Step 5b modifies the sector note even for this transition (adding the thesis to Active Theses).

## Step 4: Apply Change

### For conviction changes:
1. Update `conviction:` in frontmatter
2. Append Log entry (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Status change: conviction [old] → [new] — [rationale from $ARGUMENTS]. Snapshot: [[_Archive/Snapshots/...]]
   ```
   > **Drift coupling**: `/sync` Step 3e uses `"Status change: conviction"` as a drift window anchor. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §6. Do not change this prefix without updating the registry and `/sync`; `/lint` check #29 flags drift.

3. **Conviction trigger check**: Read the Conviction Triggers section. If the new level contradicts a trigger condition (e.g., moving to high but a → LOW trigger is active), warn: `⚠️ Active trigger conflicts with new conviction: [quote trigger]. Confirm this is intentional.`

### For status changes (non-closure):
1. Update `status:` in frontmatter
2. Append Log entry (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Status change: [old] → [new] — [rationale from $ARGUMENTS]. Snapshot: [[_Archive/Snapshots/...]]
   ```

### For status → closed (archive flow):
1. Add final Log entry:
   ```
   ### YYYY-MM-DD
   - CLOSED: [rationale from $ARGUMENTS]. Archived.
   ```
2. Change frontmatter: `status: closed`

> **The file is NOT moved yet.** The archive move runs in Step 7.5, after all metadata updates (sector note, graph, `_hot.md`) succeed. This ordering guarantees that if the skill fails mid-execution, the thesis file remains in `Theses/` with `status: closed` — no ghost graph entries, no broken wikilinks, no stale sector note references. The intermediate state (`status: closed` in `Theses/`) is recoverable by re-running the closure or manually executing the `mv` command from Step 7.5.

## Step 5: Update Sector Note

### 5.0: Locate the sector note

Resolve the sector note using the canonical procedure: **`.claude/skills/_shared/sector-resolution.md`**. Inputs: thesis's `sector:` frontmatter. Outputs: `sector_note_path`, `match_confidence`, `log_message`.

- If `match_confidence` is `none`: emit the contract's no-match warning, skip the rest of Step 5, and proceed to Step 6.
- If `match_confidence` is `normalized` or `substring`: emit the contract's `log_message` in the Step 8 report, then proceed with the resolved sector note.
- If `match_confidence` is `exact`: proceed silently with the resolved sector note.

### 5.1: Dry-run — determine whether an edit is actually needed

Read the sector note's content and analyze what Step 5b would do for this specific transition. The goal is to avoid a redundant snapshot (and redundant downstream noise) when the transition is a no-op against the current sector note state.

Decision matrix — set `edit_planned: true` only when at least one of the conditions below is met:

| Transition | Check against sector note | Set `edit_planned: true` when... |
|---|---|---|
| `draft→active` | Is the thesis wikilink already present in the Active Theses section? | Thesis wikilink ABSENT — Step 5b will add it. |
| `monitoring→active` | Is the thesis wikilink already in the Active Theses section (not annotated as monitoring)? | Thesis wikilink absent from Active Theses, OR present but annotated as monitoring (annotation will be removed). |
| `closed→active` (reopen) | (1) Is the thesis wikilink already present in the Active Theses section? (2) Is the thesis wikilink also present in a Closed/Archived section? | Thesis wikilink ABSENT from Active Theses **OR** PRESENT in a Closed/Archived section (stale entry from a prior closure that needs cleanup). The two checks compose independently — either condition alone triggers `edit_planned: true`. See "Reopen anti-collision check" below for why this row exists. |
| `active→monitoring` | Does the sector note distinguish monitoring (e.g., separate "Monitoring" section, `(monitoring)` suffix on wikilink, conviction column, or annotation convention)? | Sector note distinguishes monitoring AND the thesis is NOT already annotated as such. |
| `active→closed` | Is the thesis wikilink in the Active Theses section? | Thesis wikilink present — Step 5b will remove it (and optionally add to Closed/Archived). |
| Conviction change | Does the sector note display conviction levels alongside thesis links (e.g., `[[TICKER]] (medium)`, a conviction column, or a grouped-by-conviction structure)? | Sector note displays conviction AND the displayed value differs from the new conviction. |

Distinguish "sector note distinguishes monitoring" and "sector note displays conviction" by grepping the sector note body:
- Monitoring distinction indicators: `## Monitoring`, `(monitoring)`, `monitoring:`, or any thesis wikilink suffixed with a monitoring marker.
- Conviction display indicators: `(high)`, `(medium)`, `(low)` adjacent to thesis wikilinks, OR a `| Conviction |` column header, OR section headings grouped by conviction level.

### Reopen anti-collision check (closed→active only)

`closed→active` has a specific double-listing hazard that doesn't apply to other transitions. The typical path to this transition is:

1. User closes thesis via `/status active→closed` → Step 5b removes the wikilink from sector Active Theses, `/status` archives the thesis.
2. User later runs `/rollback TICKER` to reopen. The rollback cascade (Step 2.5) typically restores BOTH the thesis file AND the sector-note snapshot taken before closure — so the sector note is reverted to its PRE-closure state, which already has the wikilink in Active Theses.
3. User (per User Guide §3.F — Recover archetype, "Undo a closure") checks the restored `status:` frontmatter. If the snapshot was pre-closure: status is already `active`, no `/status` run needed. If the snapshot was post-closure: user runs `/status TICKER status closed→active`.

At step 3, if the sector was already restored by the rollback cascade, the wikilink is present — Step 5b would add a duplicate and the sector note would end up double-listing the thesis. The decision-matrix row above prevents this: check wikilink presence first, only set `edit_planned: true` when ABSENT.

Manual `mv` reopens (user moved the file from `_Archive/` back to `Theses/` without running `/rollback`) follow the same logic: sector note was never restored, wikilink IS absent from Active Theses, `edit_planned: true`, Step 5b adds it.

**Closed/Archived section cleanup** is the second composition check. If a prior closure added the thesis to a Closed/Archived section and the user then rolled back to a pre-closure sector snapshot (which has the thesis only in Active Theses), the Closed/Archived section is now clean. But if the user manually reopened (`mv` from `_Archive/` + `/status closed→active`) WITHOUT restoring the sector note, the Closed/Archived section still carries the stale entry even though Active Theses may or may not have it. The composed check catches every case:
- In Active only → no edit (from rollback, already clean)
- In Closed/Archived only → edit (add to Active, remove from Closed/Archived)
- In both (double-listed from a messy prior state) → edit (leave Active alone or dedupe, remove from Closed/Archived)
- In neither → edit (add to Active)

Either way, the presence check in Step 5.1 is the single source of truth — no separate "did the user just run /rollback?" detection is needed.

If `edit_planned: false` after evaluating: skip both Step 5a and Step 5b. Report in Step 8 as `Sector note: no edit needed — [TICKER] transition [old→new] already reflects current sector note state.` Proceed to Step 6.

### 5a: Pre-edit snapshot (conditional on Step 5.1 `edit_planned: true`)

Only runs if Step 5.1 set `edit_planned: true`. Before modifying the sector note, snapshot it:
```bash
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-$HHMMSS).md"
```
Read the newly created snapshot, then add to its frontmatter:
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMMSS
```
Reuse the batch ID generated in Step 3.0. The snapshot runs for every transition where Step 5.1 determined an edit is required — including `draft→active`, where the thesis snapshot is skipped but the sector note IS being modified. Without this snapshot, a corrupted Edit to the sector note would leave no recovery path.

> **Skip cases**:
> - Step 5.0 returned "no matching sector note" → Steps 5.1, 5a, 5b are all skipped.
> - Step 5.1 determined `edit_planned: false` → Steps 5a, 5b are skipped; no snapshot, no edit.

### 5b: Apply the sector note update (conditional on Step 5.1 `edit_planned: true`)

Only runs if Step 5.1 set `edit_planned: true`. Apply the specific edit identified in Step 5.1's decision matrix:

1. **For status → active** (e.g., draft→active, monitoring→active, closed→active): Add the thesis to the Active Theses section. If it was present with a monitoring annotation, remove the annotation. For `closed→active` specifically, if a "Closed/Archived" section exists in the sector note and contains this thesis, remove the entry from there as well (prevents dual listing: active AND closed).
2. **For conviction changes** (when sector note displays conviction): Update the displayed conviction level for this thesis to the new value.
3. **For status → monitoring** (when sector note distinguishes monitoring): Move or annotate the thesis to reflect monitoring status per the sector note's convention.
4. **For status → closed**: Remove the thesis from the Active Theses section. If a "Closed/Archived" section exists, add it there. If not, just remove.

> **Why the dry-run matters**: Unconditional snapshotting creates orphan snapshot files for no-op transitions (e.g., `active→monitoring` on a sector note that doesn't track monitoring status). These accumulate disk usage, clutter `/rollback` snapshot lists, and dilute cascade-detection signal. The dry-run keeps snapshots aligned with actual edits without sacrificing safety.

## Step 6: Graph update deferred

`_graph.md` is now owned exclusively by `/graph`.

- **Conviction and non-closure status changes**: no graph impact (graph tracks links, not conviction/status metadata).
- **Status → closed**: after this skill (and after Step 7.5 archive move and Step 7.6 invalidation write), run `/graph last` to remove the archived thesis from the Adjacency Index, reverse indexes, Cross-Thesis Clusters, and other theses' `cross-thesis:` fields. Step 7.6 writes an invalidation list that forces `/graph last` to re-extract adjacency for every neighbor thesis that referenced the closed thesis — without the list, neighbors keep stale `cross-thesis:` references until the neighbor is next edited. Research notes orphaned by the closure are moved to the Orphan list automatically by `/graph last` rebuild.

> **Why deferred**: The incremental path of `/graph last` — augmented by the Step 7.6 invalidation list — captures closure cleanup from current vault state without requiring a full rebuild. No skill-level graph cleanup logic; `/graph` remains the sole writer of `_graph.md`.

## Step 7: Update _hot.md

Follow the contract at `.claude/skills/_shared/hot-md-contract.md` for all `_hot.md` writes — compression policy, per-section budgets, truncation-marker avoidance, and cap handling are defined there. Read `_hot.md` first, then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: follow the contract's same-ticker-continuation rule (§Same-ticker continuation rule).
2. **Recent Conviction Changes**: Add entry: `- **[TICKER]**: [field] [old] → [new] — [rationale]`. Per contract, this section is NEVER compressed — if soft cap pressure, other sections must absorb first.
3. **Open Questions**: If closing a thesis, remove any open questions specific to that ticker. Per contract, dedupe by merging duplicates (same question across multiple theses).
4. **Portfolio Snapshot**: Update conviction-level counts if conviction changed; update active/monitoring/closed counts if status changed. Per contract, regenerated fresh each time — never compressed-accumulated.

**Cap enforcement**: after all edits, run the contract's Compression trigger order. If over soft cap (4,000), apply drops in the contract's specified order; if still over hard cap (5,000), abort the `_hot.md` update per contract §Compression trigger order step 5 — do NOT block the primary `/status` operation.

## Step 7.5: Archive Move (closure only)

**Only runs for `status → closed` changes. Skip for conviction changes, non-closure status changes, and reaffirmations.**

### 7.5a: Pre-move archive-collision check

`mv` on POSIX silently overwrites the destination if it exists. If the target archive path already contains a file from a prior closure of the same ticker-and-name, silent overwrite would destroy the old archive copy. Check before moving:

```bash
ls "_Archive/TICKER - Company Name.md" 2>/dev/null
```

If a file exists at the destination: pause and present options to the user — do NOT proceed silently:

```
⚠️ Archive-path collision: _Archive/TICKER - Company Name.md already exists from a
   prior closure of this ticker-name combination. Running mv would silently
   overwrite the old archive copy.

Options:
  (a) Timestamp-suffix the old archive, then proceed:
      mv "_Archive/TICKER - Company Name.md" "_Archive/TICKER - Company Name (closed YYYY-MM-DD).md"
      then mv the new thesis to the clean path.
  (b) Timestamp-suffix the NEW archive path instead:
      mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name (closed YYYY-MM-DD).md"
  (c) Cancel — leave thesis in Theses/ with status: closed; user resolves manually.

Confirm (a/b/c):
```

Wait for user selection. If (c), report that metadata updates (sector note, `_hot.md`, invalidation list) already completed and the thesis remains in `Theses/` with `status: closed` pending manual archive resolution.

### 7.5b: Move to `_Archive/` and update archive-ticker registry

Move the closed thesis to `_Archive/` (using the path determined in 7.5a — either the clean target or a timestamp-suffixed path):
```bash
mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
```

**Archive-ticker registry update (NEW — supports `/thesis` multi-signal archive-collision check Signal C):**

After the `mv` succeeds, append a line to `.archive_ticker_registry.md` at vault root. This is a flat text registry enabling future `/thesis TICKER` invocations to discover prior archived theses via ticker lookup even if the archived filename later drifts (e.g., a subsequent manual rename).

Format: pipe-delimited, one line per archive event:
```
TICKER|archived_filename.md|YYYY-MM-DD|conviction_at_closure|closure_rationale_line1
```

Create the file with the canonical header on first write; otherwise append.

```bash
REGISTRY=".archive_ticker_registry.md"
if [ ! -f "$REGISTRY" ]; then
  cat > "$REGISTRY" <<'HEADER'
---
type: archive-ticker-registry
purpose: Flat append-only log of thesis archival events. Consumed by /thesis Step 1.2 Signal C (multi-signal archive-collision check). Format per line after header: TICKER|archived_filename.md|YYYY-MM-DD|conviction_at_closure|closure_rationale_first_line
---

# Archive Ticker Registry

HEADER
fi

# Append the new entry
printf '%s|%s|%s|%s|%s\n' \
  "$TICKER" \
  "$ARCHIVED_FILENAME" \
  "$(date +%Y-%m-%d)" \
  "$CONVICTION_AT_CLOSURE" \
  "$CLOSURE_RATIONALE_LINE" \
  >> "$REGISTRY"
```

If the registry append fails (extremely unlikely — single-line append), log `⚠️ Archive registry append failed: [reason]. Signal C in future /thesis [TICKER] may miss this entry. /lint #40 will flag on next run.` This does not abort the closure — the archival itself succeeded; only the lookup aid is missing. Signals A/B/D still cover the common cases.

**Registry integrity** — the registry is append-only; never rewritten. Stale entries (where the archived file was subsequently manually moved or renamed) are tolerated: `/thesis` Signal C verifies the referenced filename still exists on disk before treating the entry as a match.

**Verification**: After the `mv`, confirm the file exists at the new path and no longer exists at the old path:
```bash
ls "_Archive/TICKER - Company Name.md"
ls "Theses/TICKER - Company Name.md" 2>/dev/null
```

**If the move fails**: All metadata updates (sector note, graph, `_hot.md`) have already succeeded — the closure is logically complete. The thesis file remains in `Theses/` with `status: closed`. Report:
```
⚠️ Archive move failed — thesis remains in Theses/ with status: closed.
Metadata (sector note, graph, _hot.md) already updated.
To complete manually: mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
```
Do NOT attempt to undo the metadata updates. The intermediate state (`status: closed` in `Theses/`) is safe: `/sync` will skip a closed thesis in its propagation analysis, and `/lint` will flag the pending move. The next session can complete the move with the single `mv` command above.

## Step 7.6: Write Graph Invalidation List (closure only)

**Only runs for `status → closed` changes. Skip for conviction changes, non-closure status changes, and reaffirmations.** Skip silently if Step 7.5 reported the archive move failed — the closure is incomplete; invalidation must wait until the move completes.

Closure removes the thesis from `Theses/`, but neighbor theses (those that referenced the closed thesis via `[[wikilinks]]`) still have `cross-thesis:` entries in `_graph.md` pointing to the now-archived thesis. `/graph last`'s incremental path only re-extracts adjacency for thesis files whose mtime advanced since the last graph write — so untouched neighbors keep stale `cross-thesis:` references until their next edit. This accumulates dangling graph edges that `/lint` #21 flags.

Fix: write the neighbor list to `.graph_invalidations` at vault root. `/graph last` reads this file on its next run, folds the listed theses into the changed-file set for re-extraction, then deletes the file.

### 7.6a: Identify neighbor theses

Grep the `Theses/` directory (excluding the just-archived thesis) for wikilink patterns that reference the closed thesis:

```bash
# Patterns to search (each ticker/name occurrence matching any):
#   [[Theses/TICKER - Company Name]]
#   [[Theses/TICKER - Company Name|alias]]
#   [[Theses/TICKER - Company Name#section]]
#   [[Theses/TICKER - Company Name.md]]
#   [[TICKER - Company Name]]
#   [[TICKER - Company Name|alias]]
#   [[TICKER - Company Name#section]]
```

Use `Grep` with `output_mode: files_with_matches` and multiple pattern runs (one per form). Deduplicate the resulting file list. Exclude the just-archived thesis itself (if any match surfaced from _Archive/, ignore — only `Theses/*.md` neighbors matter for graph re-extraction).

### 7.6b: Append to `.graph_invalidations`

Create or append to `.graph_invalidations` at vault root (relative path `.graph_invalidations`). Format: one relative thesis path per line (e.g., `Theses/NVDA - Nvidia.md`). If the file already exists (prior closure produced unconsumed entries — `/graph last` hasn't run yet), append rather than overwrite, then deduplicate.

```bash
{
  # Existing entries (if any)
  [ -f .graph_invalidations ] && cat .graph_invalidations
  # New neighbors from 7.6a
  printf '%s\n' "Theses/NEIGHBOR1 - ...md" "Theses/NEIGHBOR2 - ...md"
} | sort -u > .graph_invalidations.tmp && mv .graph_invalidations.tmp .graph_invalidations
```

If no neighbors found (closed thesis was isolated): skip file creation. Report `Invalidation: no neighbors — isolated thesis.`

### 7.6c: Validate and report

After write, verify the file exists and contains the expected entries. Include in Step 8 report:
- **Graph invalidation**: `[N] neighbors added to .graph_invalidations: [list first 5, truncate with "...+M more" if longer]`
- **Graph reminder**: emphasize `/graph last` is now mandatory — without it, the invalidation list accumulates.

## Step 7.9: Finalize status transaction manifest (T2.2 fix)

**Only runs if Step 3.0.5 wrote a manifest** (skipped for Reaffirm flow Step 2R).

Flip the manifest's frontmatter:
- `status: in-progress` → `status: completed`
- Add `completed_date: YYYY-MM-DD`

Verify the flip landed by re-reading the frontmatter. If the verify fails:
- Report `⚠️ Status manifest status flip failed — manifest at [path] remains in-progress despite successful /status completion. /lint #48 will flag as Important. Manual fix: edit the manifest frontmatter to status: completed.`
- Do NOT rollback the prune — all stages already succeeded.

The manifest is retained. Unlike `/prune`'s 30-day regret-recovery retention (T5 5.2), `/status` does not have a defined regret-recovery window (conviction and status changes are typically intentional and not mass-triggered). `/clean` Step 2a handles aging via a new 90-day threshold for `status-manifest` files (see `/clean` SKILL.md extension).

## Step 8: Report

- **Change applied**: [TICKER] [field] [old] → [new]
- **Rationale**: [from $ARGUMENTS]
- **Thesis snapshot**: `[[_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-HHMMSS)]]` or "skipped (draft→active)"
- **Sector note snapshot**: `[[_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-HHMMSS)]]` OR "skipped (no matching sector note)" OR "skipped (no edit needed — sector note state already reflects transition)"
- **Batch ID**: `status-YYYY-MM-DD-HHMMSS` (cascade-restore with /rollback if needed)
- **Sector Note updated**: [sector name] — [what changed] OR "no edit needed (dry-run determined current state already matches the transition)"
- **Graph reminder**: `→ Run /graph last` (closure only — conviction/non-closure changes have no graph impact). For closures the invalidation list from Step 7.6 is unconsumed until `/graph last` runs; a stale list accumulates across successive closures but does no harm beyond slightly wider re-extraction on the next `/graph last`.
- **Archived** (closure only): `[[_Archive/TICKER - Company Name]]` or `⚠️ Archive move failed — see Step 7.5 output`
- **Graph invalidation** (closure only): `[N] neighbor theses queued for re-extraction in .graph_invalidations: [first 5 relative paths, truncate with "...+M more" if longer]` OR `no neighbors — isolated thesis` OR `skipped — archive move failed at Step 7.5`
- **Wikilink breakages** (closure only): `⚠️ [N] notes contain wikilinks to this thesis. Run /lint to review.`
- **Trigger conflict** (if any): `⚠️ [quote conflicting trigger]`

## Step 9: Release lock

After Step 8's Report is complete, release the ticker lock per `.claude/skills/_shared/preflight.md` §1.7 as the skill's FINAL Bash block. Runs unconditionally — whether `/status` succeeded, was a no-op reaffirm, or hit a non-fatal error. If the skill aborts before reaching this step (trigger-conflict refusal, archive-move failure, Ctrl-C), the lock persists and appears stale on the next collision / `/lint #43` run.

```bash
# Lock release — verify ownership before rm (preflight §1.5)
LOCK_FILE=".vault-lock.TICKER"                   # TICKER from $ARGUMENTS, e.g., .vault-lock.NVDA
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ($LOCK_FILE) ==="
else
  echo "⚠️ Lock ownership check failed at release ($LOCK_FILE) — skipping rm to avoid stealing another skill's lock."
fi
```
