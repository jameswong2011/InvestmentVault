---
name: status
description: Change conviction level or status on a single thesis. Use when user says "change conviction", "downgrade", "upgrade", "move to monitoring", "close [TICKER]", or "set [TICKER] to [level]".
model: sonnet
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * cp * mkdir * mv * find * grep * cat * sort * printf * ls *)
---

Execute a conviction or status change on a single thesis. Atomic operation that closes the loop after `/stress-test`, `/scenario`, `/deepen`, `/compare`, or manual reassessment.

Design rationale in `.claude/skills/status/RATIONALE.md` (§N.M anchors).

## Arguments

`$ARGUMENTS` should follow one of:

**Conviction or status change**: `TICKER field old→new [rationale]`
- `NVDA conviction medium→low China risk unhedgeable`
- `BESI status active→monitoring awaiting Q3 earnings`
- `SHOP status active→closed thesis invalidated by margin compression`

**Drift acknowledgment**: `TICKER reaffirm [rationale]`
- `NVDA reaffirm earnings miss was one-time; competitive position unchanged`

Ambiguous/incomplete → ask user to clarify ticker, field, direction, rationale. If matches `reaffirm` pattern → jump to **Step 2R**.

## Step 0: Pre-flight

### 0.1: Acquire vault lock

`ticker:TICKER` scope per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout: 3 min (extend to 5 min for `status: active→closed` — cascade may take longer). Capture token, verify (Procedure 1.5) every subsequent block, release in final block.

### 0.2: Rename-marker pre-flight

Procedure 2. If `.rename_incomplete.TICKER` exists at vault root, hard-block per contract 2.3. Sector note edits, archive moves, and `_hot.md` mentions all rely on stable naming — mid-rename repair must complete first.

## Step 1: Validate

1. **Find thesis**: search `Theses/` for ticker match. Not found → `⚠️ No thesis found for [TICKER] in Theses/. Nothing to update.`
2. **Read full thesis note** — understand current state.
3. **Verify current value**: confirm `old` value in $ARGUMENTS matches actual frontmatter. Mismatch → `⚠️ Expected [field]: [old] but found [field]: [actual]. Confirm the intended change.`
4. **Parse change type**:
   - `conviction` change → Step 2
   - `status` change to `closed` → Step 2 (triggers archive flow)
   - `status` change to anything else (`active→monitoring`, `draft→active`, `monitoring→active`) → Step 2

## Step 2R: Reaffirm Flow (drift acknowledgment)

Entered only when $ARGUMENTS matches `TICKER reaffirm [rationale]`. Lightweight — no frontmatter change, no snapshot, no sector/graph update. Idempotent-safe (§1.1). Skips Step 3.0.5 manifest (§3.2).

1. **Find and read thesis** (same as Step 1.1-1.2).
2. **Extract drift context and classify state**:
   - Scan last 5 Log entries. Identify `"weakened"` or `"strengthened"` sentiment. Count drift pattern.
   - Scan `_hot.md`'s `## Recent Conviction Changes` for active drift flag matching this TICKER (e.g., `⚠️ Conviction drift — [TICKER]: ...`).
   - **drift_flag_active: true | false**
3. **Present evidence and wait for confirmation**:

   **If drift_flag_active = true:**
   ```
   Drift review for [[Theses/TICKER - Company Name]]:
     Current conviction: [level]
     Active drift flag: [flag text from _hot.md, dated YYYY-MM-DD]
     Recent log sentiment:
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
     Recent log sentiment: [list]

     Reaffirming conviction at [level] with rationale: [from $ARGUMENTS]
     No active drift to clear — Log entry recorded for audit trail.
     Drift window anchor advances regardless.

   Confirm? (y/n)
   ```
   **Do NOT proceed without explicit user confirmation.**

4. **Append Log entry** (MANDATORY regardless of drift state — §1.1 — max 2 lines):
   ```
   ### YYYY-MM-DD
   - Conviction reaffirmed at [level] after [drift review | proactive review] — [rationale from $ARGUMENTS]
   ```
   Use `drift review` when `drift_flag_active = true`, `proactive review` otherwise. Prefix `"Conviction reaffirmed"` is canonical in both cases — `/sync` Step 3e drift anchor (registry §5). Do not change without updating `_shared/log-prefixes.md` + `/sync`; `/lint #29` flags drift.

5. **Update _hot.md** (follow `_shared/hot-md-contract.md`; do NOT touch Latest Sync / Sync Archive):
   - **Recent Conviction Changes**: add `- **[TICKER]**: conviction [level] reaffirmed — [rationale]`
   - **Drift flag cleanup** (only if `drift_flag_active = true`): locate active drift flag entry for TICKER, mark inline `⚠️ Conviction drift — [TICKER] ... → Resolved YYYY-MM-DD: reaffirmed ([level])` (§1.2 — prevents stale flag re-appearing as Open Question on next `/sync`).

6. **Report**:
   - **Reaffirmed**: [TICKER] conviction [level] maintained
   - **Drift state at entry**: `active flag cleared (from YYYY-MM-DD)` | `no active flag — proactive reaffirm for audit trail`
   - **Log entry appended**: 1 line (`Conviction reaffirmed`)
   - **Drift window reset**: next /sync anchors drift detection after this entry
   - **No snapshot, sector, or graph changes**

**Stop here — do not continue to Step 2 or beyond.**

---

## Step 2: Confirm (Tier 3 — Mandatory)

Present the proposed change and **wait for user confirmation**:

```
Proposed change:
  Thesis: [[Theses/TICKER - Company Name]]
  Field: [conviction | status]
  Change: [old] → [new]
  Rationale: [from $ARGUMENTS]
  Side effects: [list what will be updated — sector note, archive move, graph cleanup]

Confirm? (y/n)
```

**Do NOT proceed without explicit user confirmation.** Investment decisions per CLAUDE.md Tier 3.

## Step 3: Snapshot

### 3.0: Generate batch ID (always — §2.2)

```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
```

Batch ID format: `status-TICKER-YYYY-MM-DD-$HHMMSS` (§2.1 — ticker qualifier prevents concurrent-run collisions). Used across all snapshots in this run (thesis Step 3.1, sector Step 5a) for atomic cascade restore.

### 3.0.5: Write status transaction manifest skeleton (T2.2 — §3)

**Mandatory BEFORE any file modifications.** Step 3.1 snapshot, Step 4 frontmatter edit, Step 5 sector edit, Step 7.5 archive move, Step 7.6 invalidation write are ALL gated on this skeleton.

Write `_Archive/Snapshots/_status-manifest (status-YYYY-MM-DD-HHMMSS).md`:

```yaml
---
type: status-manifest
batch: status-YYYY-MM-DD-HHMMSS
status: in-progress
ticker: TICKER
transition_type: conviction | status | reaffirm
field: conviction | status
old_value: [parsed]
new_value: [parsed]
date: YYYY-MM-DD
---

# Status Transaction Manifest (in-progress)

Manifest written at Step 3.0.5 before any file modifications. Intended edits:

## Thesis frontmatter edit
- Target: `Theses/TICKER - Name.md`
- Field: [conviction | status]
- Change: [old] → [new]
- Snapshot taken: (populated in Step 3.1 — or "skipped (draft→active)")

## Sector note edit (if applicable per Step 5.1 dry-run)
- Resolution: (populated)
- Edit planned: yes | no | skipped (no match)
- Snapshot taken: (populated in Step 5a)

## Archive move (closure only)
- Source: `Theses/TICKER - Name.md`
- Target: `_Archive/TICKER - Name.md`
- Status: (populated in Step 7.5)

## Graph invalidations (closure only)
- Neighbors queued: (populated in Step 7.6)

## Archive registry append (closure only)
- Line added to `.archive_ticker_registry.md`: (populated in Step 7.5b)

## _hot.md edits
- (populated in Step 7)

## Recovery guidance

If this file persists with `status: in-progress`, /status crashed mid-run:
- (a) Skeleton only → thesis unchanged; rm manifest.
- (b) Thesis edited but later steps failed → /rollback [snapshot_batch].
- (c) Partial closure (archived but sector not updated) → /rollback handles both via snapshots.

Flipped to `status: completed` at Step 7.9 after all stages succeed.
/lint #48 surfaces in-progress as Important.
```

**Skeleton write failure — hard abort** (§3.1):
```
❌ Status transaction manifest skeleton write failed: [path]
   Reason: [error]
No vault state modified. Fix filesystem issue and re-run /status.
```

Exit. Reaffirm flow (Step 2R) does NOT need a manifest (§3.2).

**Incremental population**: each subsequent step (3.1, 4, 5a, 7.5, 7.6) appends completion state via `Edit` (§3.3).

### 3.1: Thesis snapshot

```bash
cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-$HHMMSS).md"
```

Read snapshot, add frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - Company Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMMSS
```

**Exception**: skip thesis snapshot for `status: draft→active` (no analytical content change, only frontmatter `status:` flip). Sector snapshot in Step 5a still runs because Step 5b modifies the sector note for this transition.

## Step 4: Apply Change

### Conviction changes

1. Update `conviction:` in frontmatter.
2. Append Log entry (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Status change: conviction [old] → [new] — [rationale]. Snapshot: [[_Archive/Snapshots/...]]
   ```
   Prefix `"Status change: conviction"` — `/sync` Step 3e drift anchor (registry §6). Do not change; `/lint #29` flags drift.
3. **Conviction trigger check** (§7): read Conviction Triggers section. New level contradicts active trigger (e.g., → `high` but a `→ LOW if X` trigger is active) → `⚠️ Active trigger conflicts with new conviction: [quote trigger]. Confirm this is intentional.`

### Status changes (non-closure)

1. Update `status:` in frontmatter.
2. Append Log entry:
   ```
   ### YYYY-MM-DD
   - Status change: [old] → [new] — [rationale]. Snapshot: [[_Archive/Snapshots/...]]
   ```

### Status → closed (archive flow — §4)

1. Append final Log entry:
   ```
   ### YYYY-MM-DD
   - CLOSED: [rationale]. Archived.
   ```
2. Change frontmatter: `status: closed`.

**File not moved yet** (§4.1). Archive move runs in Step 7.5 after all metadata updates succeed. Intermediate state (`status: closed` in `Theses/`) is safe and recoverable — `/sync` skips closed theses; `/lint #33` flags pending move; manual `mv` completes.

## Step 5: Update Sector Note

### 5.0: Locate the sector note

Resolve via `.claude/skills/_shared/sector-resolution.md`. Inputs: thesis `sector:`. Outputs: `sector_note_path`, `match_confidence`, `log_message`.

- `none` → emit no-match warning, skip rest of Step 5, proceed to Step 6.
- `normalized` / `substring` → emit `log_message` in Step 8 report, proceed with resolved path.
- `exact` → silent, proceed.

### 5.1: Dry-run — determine if edit needed (§5)

Read sector note. Analyze what Step 5b would do for this transition. Set `edit_planned: true` only when at least one condition below matches.

| Transition | Check against sector note | `edit_planned: true` when... |
|---|---|---|
| `draft→active` | Wikilink in Active Theses? | ABSENT |
| `monitoring→active` | Wikilink in Active Theses (not annotated as monitoring)? | Absent OR present but annotated monitoring |
| `closed→active` (reopen) | (1) in Active Theses? (2) in Closed/Archived? | ABSENT from Active **OR** PRESENT in Closed/Archived (§6) |
| `active→monitoring` | Sector distinguishes monitoring AND thesis not annotated? | Both true |
| `active→closed` | Wikilink in Active Theses? | PRESENT (remove) |
| Conviction change | Sector displays conviction AND displayed differs from new? | Both true |

Detection indicators (§5.3):
- **Monitoring distinction**: `## Monitoring` section, `(monitoring)` suffix, `monitoring:` annotation
- **Conviction display**: `(high|medium|low)` adjacent, `| Conviction |` column, grouped-by-conviction sections

**`edit_planned: false`** → skip 5a and 5b. Report in Step 8: `Sector note: no edit needed — [TICKER] transition [old→new] already reflects current sector note state.` Proceed to Step 6.

**`edit_planned: true`** → proceed to 5a.

### 5a: Pre-edit snapshot (conditional)

```bash
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-$HHMMSS).md"
```

Read snapshot, add frontmatter (reuse Step 3.0 batch ID):
```yaml
snapshot_of: "[[Sectors/Sector Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: status
snapshot_batch: status-YYYY-MM-DD-HHMMSS
```

Runs for every transition where Step 5.1 set `edit_planned: true` — including `draft→active` (where thesis snapshot was skipped but sector note IS being modified). Without this snapshot, a corrupted Edit would leave no recovery path.

### 5b: Apply sector edit (conditional)

1. **Status → active** (from draft/monitoring/closed): add to Active Theses. If previously present with monitoring annotation, remove annotation. For `closed→active`: if `## Closed/Archived` section exists and contains this thesis, remove entry (prevents dual listing).
2. **Conviction change** (when sector displays conviction): update displayed level to new value.
3. **Status → monitoring** (when sector distinguishes): move or annotate per sector convention.
4. **Status → closed**: remove from Active Theses. Add to `## Closed/Archived` if exists.

## Step 6: Graph update deferred

`_graph.md` owned exclusively by `/graph`.

- **Conviction and non-closure status changes**: no graph impact (graph tracks links, not conviction/status metadata).
- **Status → closed**: after this skill (Step 7.5 archive + Step 7.6 invalidation), run `/graph last`. Step 7.6's invalidation list forces re-extraction of neighbor theses that referenced the closed thesis (§4.4).

## Step 7: Update _hot.md

Follow `.claude/skills/_shared/hot-md-contract.md`. Read first, then edit. Do NOT touch Latest Sync / Sync Archive.

1. **Active Research Thread**: follow contract's same-ticker-continuation rule.
2. **Recent Conviction Changes**: add `- **[TICKER]**: [field] [old] → [new] — [rationale]`. **Never compressed** per contract.
3. **Open Questions**: if closing, remove open questions specific to this ticker. Dedupe by merging duplicates.
4. **Portfolio Snapshot**: update conviction-level counts (if conviction changed) or active/monitoring/closed counts (if status changed). Regenerated fresh per contract.

**Cap enforcement**: after all edits, run compression trigger order. Over soft cap → apply drops per contract. Over hard cap → abort `_hot.md` update per contract §Compression trigger order step 5. Do NOT block the primary `/status` operation.

## Step 7.5: Archive Move (closure only)

**Skip for conviction changes, non-closure status changes, reaffirmations.**

### 7.5a: Pre-move archive-collision check (§4.2)

```bash
ls "_Archive/TICKER - Company Name.md" 2>/dev/null
```

If file exists at destination (prior closure of same ticker-and-name), pause:

```
⚠️ Archive-path collision: _Archive/TICKER - Company Name.md already exists from a
   prior closure. Running mv would silently overwrite.

Options:
  (a) Timestamp-suffix the old archive, then proceed:
      mv "_Archive/TICKER - Company Name.md" "_Archive/TICKER - Company Name (closed YYYY-MM-DD).md"
      then mv the new thesis to the clean path.
  (b) Timestamp-suffix the NEW archive path instead:
      mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name (closed YYYY-MM-DD).md"
  (c) Cancel — leave thesis in Theses/ with status: closed; resolve manually.

Confirm (a/b/c):
```

Wait for selection. (c) → report metadata updates (sector, `_hot.md`, invalidations) already completed; thesis remains in `Theses/` pending manual archive resolution.

### 7.5b: Move + update archive-ticker registry

```bash
mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
```

Append to `.archive_ticker_registry.md` at vault root (supports `/thesis` multi-signal archive-collision check — Signal C):

Format: `TICKER|archived_filename.md|YYYY-MM-DD|conviction_at_closure|closure_rationale_line1`

Create file with header on first write; otherwise append:

```bash
REGISTRY=".archive_ticker_registry.md"
if [ ! -f "$REGISTRY" ]; then
  cat > "$REGISTRY" <<'HEADER'
---
type: archive-ticker-registry
purpose: Flat append-only log of thesis archival events. Consumed by /thesis Step 1.2 Signal C (multi-signal archive-collision check).
---

# Archive Ticker Registry

HEADER
fi

printf '%s|%s|%s|%s|%s\n' \
  "$TICKER" \
  "$ARCHIVED_FILENAME" \
  "$(date +%Y-%m-%d)" \
  "$CONVICTION_AT_CLOSURE" \
  "$CLOSURE_RATIONALE_LINE" \
  >> "$REGISTRY"
```

Registry append failure (extremely unlikely — single-line append): `⚠️ Archive registry append failed: [reason]. Signal C in future /thesis [TICKER] may miss this entry. /lint #46 will flag on next run.` Does NOT abort closure — archival succeeded; only the lookup aid is missing. Signals A/B/D still cover common cases.

**Verification**: confirm file at new path, absent from old:
```bash
ls "_Archive/TICKER - Company Name.md"
ls "Theses/TICKER - Company Name.md" 2>/dev/null
```

**If move fails** (§4.3): all metadata already succeeded. Do NOT attempt to undo. Report:
```
⚠️ Archive move failed — thesis remains in Theses/ with status: closed.
Metadata (sector note, graph, _hot.md) already updated.
To complete manually: mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
```

## Step 7.6: Write Graph Invalidation List (closure only)

**Skip for non-closure transitions.** Skip silently if Step 7.5 reported move failed (§4.5) — closure incomplete; invalidation must wait.

### 7.6a: Identify neighbor theses

Grep `Theses/` (excluding just-archived thesis) for wikilink patterns referencing closed thesis:

Patterns (each ticker/name occurrence, any form):
- `[[Theses/TICKER - Company Name]]`, `[[Theses/TICKER - Company Name|alias]]`, `[[Theses/TICKER - Company Name#section]]`, `[[Theses/TICKER - Company Name.md]]`
- `[[TICKER - Company Name]]`, `[[TICKER - Company Name|alias]]`, `[[TICKER - Company Name#section]]`

Use `Grep` with `output_mode: files_with_matches`, multiple pattern runs. Dedup. Exclude just-archived thesis.

### 7.6b: Append to `.graph_invalidations`

One relative thesis path per line (e.g., `Theses/NVDA - Nvidia.md`). If file exists (prior closure produced unconsumed entries — `/graph last` hasn't run), append then dedupe:

```bash
{
  [ -f .graph_invalidations ] && cat .graph_invalidations
  printf '%s\n' "Theses/NEIGHBOR1 - ...md" "Theses/NEIGHBOR2 - ...md"
} | sort -u > .graph_invalidations.tmp && mv .graph_invalidations.tmp .graph_invalidations
```

No neighbors (isolated thesis): skip file creation. Report `Invalidation: no neighbors — isolated thesis.`

### 7.6c: Validate and report

After write, verify file exists + contains expected entries. Include in Step 8:
- **Graph invalidation**: `[N] neighbors added to .graph_invalidations: [first 5, truncate with "...+M more"]`
- **Graph reminder**: `/graph last` now mandatory — without it, invalidation list accumulates.

## Step 7.9: Finalize status transaction manifest

**Only runs if Step 3.0.5 wrote a manifest** (skipped for Reaffirm flow Step 2R).

Flip manifest frontmatter:
- `status: in-progress` → `status: completed`
- Add `completed_date: YYYY-MM-DD`

Verify flip landed by re-reading frontmatter. Verify fails (§3.4):
```
⚠️ Status manifest status flip failed — manifest at [path] remains in-progress despite successful /status completion. /lint #48 will flag as Important. Manual fix: edit the manifest frontmatter to status: completed.
```

Do NOT rollback — all stages already succeeded.

Manifest retained. `/clean` handles aging via 90-day threshold (§8 — no regret-recovery window like `/prune`).

## Step 8: Report

- **Change applied**: [TICKER] [field] [old] → [new]
- **Rationale**: [from $ARGUMENTS]
- **Thesis snapshot**: `[[_Archive/Snapshots/TICKER - Company Name (pre-status YYYY-MM-DD-HHMMSS)]]` | `skipped (draft→active)`
- **Sector note snapshot**: `[[_Archive/Snapshots/Sector Name (pre-status YYYY-MM-DD-HHMMSS)]]` | `skipped (no matching sector note)` | `skipped (no edit needed — sector state already reflects transition)`
- **Batch ID**: `status-YYYY-MM-DD-HHMMSS` (cascade-restore via /rollback)
- **Sector Note updated**: [sector] — [what changed] | `no edit needed (dry-run)`
- **Graph reminder**: `→ Run /graph last` (closure only — conviction/non-closure have no graph impact). For closures, invalidation list is unconsumed until `/graph last` runs.
- **Archived** (closure only): `[[_Archive/TICKER - Company Name]]` | `⚠️ Archive move failed — see Step 7.5 output`
- **Graph invalidation** (closure only): `[N] neighbors queued in .graph_invalidations: [first 5 paths, truncate "...+M more"]` | `no neighbors — isolated thesis` | `skipped — archive move failed`
- **Wikilink breakages** (closure only): `⚠️ [N] notes contain wikilinks to this thesis. Run /lint to review.`
- **Trigger conflict** (if any): `⚠️ [quote conflicting trigger]`
