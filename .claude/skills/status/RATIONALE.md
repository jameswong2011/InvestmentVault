---
type: skill-rationale
skill: /status
purpose: Design rationale and transaction-ordering context for /status. NOT loaded at invocation — SKILL.md references by §N.M.
last_reviewed: 2026-04-21
---

# /status Design Rationale

> SKILL.md contains operational rules. This file explains the T2.2 manifest contract, C4 batch-ID qualification, reaffirm audit-trail requirement, sector-note dry-run design, reopen anti-collision semantics, and the closure ordering contract. Maintainers read this; the LLM executing /status does not.

---

## §1 Reaffirm flow design (Step 2R)

### §1.1 Why always write the Log entry

Prior spec suggested reaffirm was "lightweight", which some implementations interpreted as "skip Log entry when no drift flag exists." That created an audit gap — a user's proactive conviction reaffirmation left no trace in the Log. The resulting audit story was "user never reviewed this thesis" even when they explicitly did.

Always writing the Log entry closes that gap; the tiny overhead is worth the auditability. Reaffirm is idempotent-safe: it can be run even if no drift flag is currently active, because the operation always appends a Log entry and always resets the drift detection window (resetting an already-clean window is harmless).

### §1.2 Drift flag cleanup coupling

Step 2R.5's Recent Conviction Changes entry + `## Open Questions` drift-flag resolve work together. `/sync` Step 6 checks `_hot.md` for active drift flags; clearing the flag here prevents it from re-appearing as an Open Question on the next sync.

### §1.3 Why `"Conviction reaffirmed"` prefix must not change

`/sync` Step 3e drift detection uses `"Conviction reaffirmed"` as the window anchor. Registry entry: `.claude/skills/_shared/log-prefixes.md §5`. Changing the prefix silently breaks drift detection's anchor logic — drift windows would count entries from before the reaffirm, producing false positives.

`/lint #29` enforces registry alignment across producer + consumer + vault presence.

---

## §2 Batch ID qualification (C4 fix)

### §2.1 Why ticker qualifier in batch ID

Pre-C4 format `status-YYYY-MM-DD-HHMMSS` could collide when two concurrent `/status` runs on different tickers hit the same HHMMSS. Simultaneous `/status NVDA conviction...` and `/status AMAT status...` would write two snapshots with identical `snapshot_batch:` values — `/rollback` cascade detection would then pair them incorrectly.

New format `status-TICKER-YYYY-MM-DD-HHMMSS` makes every batch unique even under concurrent invocations.

### §2.2 Why batch ID always generated — even when thesis snapshot is skipped

`draft→active` skips the thesis snapshot (no analytical content changes; only frontmatter `status:` field flips). But Step 5a still needs the batch ID for the sector note snapshot — a batch ID ties the sector snapshot to this `/status` run for cascade restore.

Generate HHMMSS unconditionally at Step 3.0; reuse in Step 5a regardless of whether Step 3.1 ran.

---

## §3 Manifest skeleton contract (T2.2 fix)

### §3.1 Why skeleton before any file modification

Prior behavior: manifest written at end of run as "best-effort audit trail". End-write failure silently violated the cascade-recovery contract — `/rollback` saw pre-status snapshots but no manifest to distinguish partial from complete runs.

T2.2 pattern matches `/sync` Step 2.9 and `/prune` Stage 1.5: skeleton written BEFORE any mutation. Skeleton write failure hard-aborts pre-mutation — no thesis snapshot, no frontmatter edit, no sector edit, no archive move. User re-runs after fixing filesystem issue; no silent corruption possible.

### §3.2 Why Reaffirm flow (Step 2R) skips the manifest

Reaffirm is a single Log append. No multi-file transaction, no snapshot, no sector/graph/archive work — nothing to manifest. Skipping the skeleton keeps the fast-path operation fast.

### §3.3 Incremental population across Steps 3.1 → 7.5 → 7.6 → 7.9

Each step appends completion state to the manifest via Edit. Crash between Step 5a and Step 7.5 → manifest reflects thesis + sector edits but NOT archive move → `/rollback` sees this partial state and offers appropriate cascade options (either thesis-only restore or full transaction restore).

### §3.4 Flip-failure handling at Step 7.9

If the status flip fails silently (Edit landed but frontmatter didn't update), manifest persists as `in-progress`. `/lint #48` surfaces it as Important. Do NOT rollback the `/status` on flip failure — all stages already succeeded; only the completion marker failed. User manually edits manifest to `status: completed`.

---

## §4 Closure ordering contract (Steps 4/5/6/7.5/7.6/7.9)

### §4.1 Why archive move is at Step 7.5, not Step 4

Change order matters for closure transactions:
1. Step 4: frontmatter edit (`status: closed`)
2. Step 5: sector note edit (remove from Active Theses)
3. Step 6: graph update deferred (no-op — `/graph` owns `_graph.md`)
4. Step 7: `_hot.md` update (Recent Conviction Changes, Portfolio Snapshot)
5. **Step 7.5: archive `mv` (final)**
6. Step 7.6: `.graph_invalidations` write
7. Step 7.9: manifest flip

If Step 4 archived the file immediately, subsequent steps (5, 7, 7.6) would need to reference the archived path in `_Archive/`, creating ordering complexity. Keeping the file in `Theses/` with `status: closed` until all metadata updates succeed means every reader sees the thesis in its original location with a consistent "closed" signal.

The intermediate state (`status: closed` in `Theses/`) is **safe and recoverable**:
- `/sync` skips `status: closed` theses in propagation analysis (§2.5 skill-origin gate)
- `/lint #33` flags the pending move for user awareness
- Re-running the closure OR manual `mv "Theses/[file]" "_Archive/[file]"` completes it

### §4.2 Archive-path collision check (Step 7.5a)

`mv` on POSIX silently overwrites. Prior closures of the same ticker-and-name combination would produce silent data loss. Pre-move check + three user options (suffix old, suffix new, cancel) prevents this.

### §4.3 Archive move failure — metadata updates already landed

If the `mv` fails, all metadata (sector note, graph invalidations, `_hot.md`) already succeeded. Do NOT attempt to undo — the intermediate state is self-consistent. Report the completion command for manual resolution. The closure is logically complete.

### §4.4 Graph invalidation (Step 7.6) — why before `/graph last`, not inline

`/graph last`'s incremental path only re-extracts adjacency for thesis files whose mtime advanced since the last graph write. Untouched neighbors keep stale `cross-thesis:` references until their next edit, accumulating dangling graph edges (`/lint #21` flags).

`.graph_invalidations` — written here, consumed by next `/graph last` — forces re-extraction of neighbors that referenced the closed thesis even if they haven't been edited. Without this list, the graph would need a full rebuild every closure.

### §4.5 Why skip Step 7.6 if Step 7.5 move failed

If archive move failed, the closure is incomplete — thesis still in `Theses/`. Writing `.graph_invalidations` for neighbors would force them to re-extract adjacency against a still-living thesis, which correctly preserves their `cross-thesis:` references. Better to skip and let the next run (after manual completion) write the invalidation list correctly.

---

## §5 Sector note dry-run (Step 5.1)

### §5.1 Why dry-run before snapshot

Unconditional snapshotting creates orphan snapshot files for no-op transitions (e.g., `active→monitoring` on a sector note that doesn't track monitoring status). These accumulate disk usage, clutter `/rollback` snapshot lists, and dilute cascade-detection signal.

The dry-run keeps snapshots aligned with actual edits without sacrificing safety. When `edit_planned: false`, no snapshot, no edit — the transition already reflects current sector state.

### §5.2 Decision matrix per transition

Different transitions require different sector-note reactions:
- `draft→active`, `monitoring→active`, `closed→active`: add to Active Theses (with cleanup variations)
- `active→monitoring`: annotate per sector convention (only if sector distinguishes monitoring)
- `active→closed`: remove from Active Theses
- conviction change: update displayed conviction level (only if sector displays conviction)

The matrix column "Set `edit_planned: true` when..." captures the specific precondition for each row.

### §5.3 Detection indicators — how to tell if sector distinguishes monitoring/conviction

Sector notes have variable structure. The heuristics:
- **Monitoring distinction**: section heading `## Monitoring`, suffix `(monitoring)` on wikilinks, `monitoring:` annotation, or any thesis wikilink with monitoring marker
- **Conviction display**: `(high|medium|low)` suffix adjacent to wikilinks, `| Conviction |` column header, or sections grouped by conviction level

Absence of these indicators → sector doesn't distinguish that dimension → `edit_planned: false` for transitions touching only that dimension.

---

## §6 Reopen anti-collision check (closed→active)

### §6.1 Why the two-check composition exists

`closed→active` has a specific double-listing hazard absent in other transitions. The typical path:

1. User closes thesis via `/status active→closed` → Step 5b removes wikilink from sector Active Theses → `/status` archives.
2. User later runs `/rollback TICKER` to reopen. Rollback cascade (Step 2.5) typically restores BOTH thesis AND sector-note snapshot taken before closure — sector note reverts to PRE-closure state, which already has the wikilink in Active Theses.
3. User (per User Guide §3.F "Undo a closure") checks restored `status:` frontmatter. If pre-closure snapshot: status is already `active`, no `/status` run. If post-closure snapshot: user runs `/status TICKER status closed→active`.

At step 3, if sector was already restored by rollback cascade, wikilink is present — unconditional Step 5b would add a duplicate. The check-before-add prevents this.

### §6.2 Four case outcomes

The composed "present in Active OR present in Closed/Archived" check handles every scenario:
- **In Active only** (clean rollback-restored state): no edit needed
- **In Closed/Archived only** (manual mv reopen without sector restore): edit — add to Active, remove from Closed/Archived
- **In both** (double-listed from messy prior state): edit — leave Active alone (or dedupe), remove from Closed/Archived
- **In neither** (partial rollback or fresh manual reopen): edit — add to Active

Single presence check → all four cases handled without separate "did the user just run /rollback?" detection.

### §6.3 Closed/Archived cleanup as second composition

If a prior closure added the thesis to a sector's `## Closed/Archived` section, that stale entry persists until explicitly removed. Sector note snapshot rollback (scenario 1 above) gets it for free. Manual reopen (`mv` + `/status closed→active` without sector restore) would leave it stale — second check catches this.

---

## §7 Trigger conflict warning (Step 4 conviction)

When new conviction contradicts an active Conviction Trigger condition (e.g., moving to `high` but a `→ LOW if X` trigger is currently active), warn the user. This isn't a block — the user may knowingly override the trigger (e.g., trigger condition was transient, thesis revised). Warning surfaces the contradiction so the override is explicit.

`⚠️ Active trigger conflicts with new conviction: [quote trigger]. Confirm this is intentional.`

---

## §8 `/clean` interaction — status manifest 90-day threshold

Unlike `/prune`'s 30-day regret-recovery retention (T5 5.2), `/status` does not have a defined regret-recovery window. Conviction and status changes are typically intentional single-thesis operations, not mass-triggered events. 90-day `/clean` threshold is sufficient.

`/lint #48` surfaces in-progress status manifests as Important regardless of age (crash recovery signal). Completed manifests age per the 90-day threshold with Nice to Have severity beyond.

---

## §9 Draft→active fast-path (Step 2F)

### §9.1 The exemption

`/status TICKER status draft→active` bypasses Step 2's Tier 3 "Confirm? (y/n)" gate. Every other mechanic (manifest at Step 3.0.5, sector dry-run at Step 5.1, `Status change:` Log prefix, Step 7 `_hot.md` updates, Step 7.9 manifest flip) runs identically. Only the user-prompt step is elided.

### §9.2 Why draft→active specifically

CLAUDE.md Tier 3's stated rule: "These changes represent investment decisions, not formatting — confirm with the user before applying". The listed examples are:
- `conviction:` frontmatter changes (high → medium, etc.)
- `status:` transitions (active → monitoring, active → closed)
- Moving a thesis to `/_Archive`
- Removing any wikilink
- Deleting or renaming any file

Every listed example is either an analytical change (conviction) or a **reduction / removal** (active→monitoring demotes visibility; active→closed archives; moving to _Archive; removing wikilinks; deleting/renaming). The common thread: reductions have cascading downstream effects (sector-list removal, graph invalidations, _hot.md Portfolio Snapshot counts, skills that silently skip closed theses).

`draft→active` is an **additive** transition:
- No existing sector presence to remove — the thesis wasn't in Active Theses yet
- No analytical content changes (frontmatter flip only)
- No graph invalidation cascade (no closure)
- No `_hot.md` demotion (thesis enters conviction-drift + /catalyst + /prune scope, doesn't leave it)

The blast radius of a mistaken draft→active is: one sector note entry added, one `_hot.md` line added, thesis becomes visible to routine skills. All reversible with `/status TICKER active→draft` (which goes through Tier 3, where the reduction is gated).

### §9.3 Why not extend exemption to monitoring→active or closed→active

Both look "additive" superficially — also promote to active. But:

- **`monitoring→active`**: the thesis was DEMOTED to monitoring via an earlier Tier 3-gated decision. Reversing that decision deserves the same friction as the original decision. The user may have forgotten why the thesis was moved to monitoring; the Tier 3 prompt surfaces "you're reversing your earlier decision — do the conditions that triggered monitoring still hold?" as a reflection prompt.
- **`closed→active` (reopen)**: invokes the reopen anti-collision composition (§6). Sector note is probably already in a restored-but-maybe-double-listed state from a `/rollback` cascade. This transition has the highest edit-count and trickiest state of any status change — not a fast-path candidate.
- **`active→draft`**: a demotion — explicitly Tier 3 per CLAUDE.md.

Only `draft→active` satisfies ALL of: additive, first-time promotion, no prior Tier 3 decision being reversed, no reopen complexity, no cascade implications.

### §9.4 Precedent alignment

The fast-path formalizes what was already informally the case:
- Step 3.1 "Exception: skip thesis snapshot for `status: draft→active`" — recognizes this transition has no analytical content to protect
- INFRASTRUCTURE.md §3.1 snapshot table lists `/status (except draft→active)` as a snapshot producer — draft→active is already the acknowledged exception
- User Guide §13 "Draft→active has no snapshot" — instructs users that reversal is a manual frontmatter flip, not a `/rollback` operation

The Tier 3 exemption is the third expression of the same underlying insight: draft→active is the "I've reviewed this draft and want it live" audit gesture, not an investment decision.

### §9.5 Cross-skill impact check — zero breakages

Verified against every skill that touches `/status` outputs:

| Consumer | Dependency | Impact |
|---|---|---|
| `/sync` Step 2.5 skill-origin classification | Reads Log prefix `"Status change:"` from `_shared/log-prefixes.md` | **Zero** — prefix written identically by Step 2F and Step 2 |
| `/sync` Step 3e drift detection | Reads conviction reaffirmation anchor prefixes | **Zero** — draft→active doesn't change conviction |
| `/rollback` cascade | Reads `_status-manifest` (T2.2) | **Zero** — manifest written identically |
| `/lint #48` in-progress manifest check | Checks `status: in-progress` age | **Zero** — manifest flip happens identically at Step 7.9 |
| `/clean` 90-day manifest aging | Reads `completed_date:` + `type: status-manifest` | **Zero** — same frontmatter |
| `/graph` invalidation consumption | Reads `.graph_invalidations` (closure only) | **Zero** — draft→active produces no invalidations |
| `/catalyst`, `/prune`, conviction-drift | Filter by `status: active` | **Zero** — transition runs to completion identically |
| CLAUDE.md Tier 3 rule | Lists examples of confirmation-required transitions | **Compatible** — examples are reductions; draft→active is additive and isn't listed |

No skill imports the "Tier 3 confirmation happened" state anywhere. The confirmation is purely a user-facing gate.

### §9.6 Safety compensations

The fast-path retains every NON-prompt safety:
- Manifest skeleton at Step 3.0.5 (crash-recovery) still runs
- Sector snapshot at Step 5a still runs (batch-ID-tied)
- Log entry "Status change: status draft → active" still recorded (audit trail)
- Step 2F FYI message explicitly shows the change being applied (user can still interrupt before Step 3 dispatches)
- Manifest flip at Step 7.9 still verifies

The only change is: one less "y" keystroke waiting for user.

### §9.7 Opt-back-in path

If a user wants the Tier 3 prompt back for a specific `draft→active` (maybe they set status: draft 6 months ago and don't remember the thesis content), they can manually cancel after the Step 2F FYI message by interrupting the skill before Step 3 begins. The FYI message explicitly names what's about to happen so the user has a "last look" even without a y/n gate.

If the exemption proves problematic (user regret surfaces), revert is one-line: delete Step 2F, restore the old Step 1 routing line for `draft→active` to Step 2. No data migration.

---

## §10 Parallelization patterns (2026-04-21 refactor)

### §10.1 Step 1 parallel reads

Pre-refactor: thesis read → (after Tier 3) → sector note read → `_hot.md` read ran as three sequential round-trips. The Tier 3 wait between them kept the pattern invisible because the user-prompt latency dominated.

Post-refactor: thesis + `_hot.md` read in a single parallel batch at Step 1 (sector note read deferred until Step 5.0 because sector resolution may rewrite the path). Saves 1 round-trip on every /status run regardless of transition type.

### §10.2 Same-file Edit batching (Step 5b)

The harness serializes same-file `Edit` tool calls on the server side — each Edit validates its unique `old_string` against the current file state before applying. But the LLM still pays a round-trip per Edit if they're dispatched in separate messages.

Dispatching 3 Edits to the same file in ONE parallel tool-call block = 1 LLM round-trip + 3 serial server-side applies, instead of 3 LLM round-trips. Saves ~6-10s per multi-edit sector update (draft→active on a thesis currently on Watchlist is a common case).

### §10.3 Step 7.9 consolidated manifest flip

Pre-refactor: incremental population at Steps 3.1/5a/7.5/7.6 + separate population edits at 7.9 + separate frontmatter flip + separate verify-read. Five sequential manifest touches minimum.

Post-refactor: §3.3 incremental population preserved (crash recovery depends on it), but Step 7.9 fires its final-populate + status-flip + completed_date in one parallel block, then verifies once. Two round-trips saved.

### §10.4 Final Bash batching

Step 7.9 manifest verification re-read can dispatch in parallel with Step 8's final `rm -f $LOCK_FILE` Bash block — different files, no dependency. One more round-trip saved.

### §10.5 Cumulative impact

Measured on a representative `/status VRT draft→active` run (17 total round-trips pre-refactor, excluding user-wait):

| Saving | Mechanism | Round-trips |
|---|---|---|
| Parallel Step 1 reads | §10.1 | -1 |
| Same-file Edit batching | §10.2 | -2 to -3 |
| Consolidated 7.9 | §10.3 | -2 |
| Final Bash parallel | §10.4 | -1 |
| **Total** | | **-6 to -7 round-trips** |

At ~3s per round-trip, ~18-21s saved on the mechanical portion. Combined with §9's Tier 3 elision (saves user-wait latency entirely — variable 10-120s), a `/status VRT draft→active` that took 3 minutes should complete in 30-50s.

### §10.6 What was NOT parallelized and why

- **Lock acquisition (Step 0.1)**: must complete first (safety contract per preflight §1.3). No parallelization.
- **Thesis Edit before sector Edit**: thesis frontmatter change is the semantic state transition; sector edit reacts to it. Sequential for auditability (Log entry lands before sector-list change reflects it).
- **Manifest skeleton (Step 3.0.5)**: must land before ANY destructive edit per T2.2. Not batchable with subsequent edits.
- **Snapshot `cp` before sector Edit (Step 5a before 5b)**: `cp` must read pre-edit state. Sequential by definition.
- **Step 7.5 archive `mv` (closure only)**: ordering contract §4.1 requires `mv` last — not batchable with earlier edits.
