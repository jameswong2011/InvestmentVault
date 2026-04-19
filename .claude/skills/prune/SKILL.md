---
name: prune
description: Systematically evaluate weak, stale, or low-conviction theses for upgrade, monitoring, or closure. Use when user says "prune", "kill list", "clean up theses", "what should I close", or "reduce portfolio".
model: opus
effort: max
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Edit Write Bash(date * find * wc * mv * cp * mkdir * rm * grep * cat * sort * printf *)
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

## Phase 0.0: Pre-flight (MANDATORY — runs before Phase 0)

### 0.0.1: Acquire vault lock
Acquire a `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 15 minutes (prune over a large portfolio can be slow). Release via `trap` on exit. `/prune` blocks on conflicting vault-wide or ticker-level locks.

### 0.0.2: Check for rename markers across the whole vault
Glob `.rename_incomplete.*` at vault root. If ANY marker exists, hard-block:

```
❌ In-flight rename repair detected — /prune would compound split state.

Markers found:
  - .rename_incomplete.TICKER1 ([new_name from marker])
  - ...

/prune closes, upgrades, and reshapes sector notes — each operation keyed to
the CURRENT thesis filename. Any of the affected theses that is also mid-rename
repair would leave inbound references split across old and new names.

Complete or abandon all in-flight renames first:
  /rename TICKER "[new_name]"    # per marker
  OR
  rm .rename_incomplete.TICKER   # accept broken wikilinks
```

Wait for user to resolve externally. Do NOT proceed. The check is all-or-nothing — a prune batch cannot safely skip individual tickers from the batch based on markers because the manifest integrity depends on a closed set of affected files decided at Stage 1.

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

Generate a single batch ID for the entire prune run (6-digit second-precision prevents same-minute batch collisions across skills):
```bash
HHMMSS=$(date +%H%M%S)
mkdir -p _Archive/Snapshots
```
Use `prune-YYYY-MM-DD-$HHMMSS` as the `snapshot_batch` value for ALL snapshots below.

**Thesis snapshots** — one per approved closure AND one per approved upgrade:
```bash
cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-prune YYYY-MM-DD-HHMMSS).md"
```
Read each newly created snapshot and add to its frontmatter:
```yaml
snapshot_of: "[[Theses/TICKER - Company Name]]"
snapshot_date: YYYY-MM-DD
snapshot_trigger: prune
snapshot_batch: prune-YYYY-MM-DD-HHMMSS
```

**Sector note snapshots** — one per affected sector note (any sector that will have a thesis removed or a conviction level updated). Resolve affected sectors using the canonical procedure **`.claude/skills/_shared/sector-resolution.md`** for each approved thesis's `sector:` frontmatter. Deduplicate the resolved set, then snapshot each unique sector note:
```bash
cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-prune YYYY-MM-DD-HHMMSS).md"
```
Read each newly created snapshot and add `snapshot_of: "[[Sectors/Sector Name]]"`, `snapshot_date`, `snapshot_trigger: prune`, `snapshot_batch: prune-YYYY-MM-DD-HHMMSS` to its frontmatter.

> If `match_confidence` is `none` for a thesis's sector value, emit the contract's no-match warning suffixed with `Skipping sector snapshot for [TICKER].` — sector update for that thesis will also be skipped in Stage 4. If `match_confidence` is `normalized` or `substring` for any thesis, collect the contract's `log_message` for the final report.

**Abort gate**: If any snapshot creation fails (file not found, write error), **STOP immediately**. No destructive modifications have been made — the vault is in its original state. Report: `❌ Snapshot failed for [file]. Prune aborted — no changes made. Fix the issue and re-run /prune.`

### Stage 1.5: Write Batch Manifest

Create a manifest note that persists if the session crashes mid-execution. This is the discovery mechanism for partial prune operations — without it, a session crash between Stages 2–5 leaves the vault in a mixed state that requires `/lint` to diagnose.

```bash
# Reuse the HHMMSS from Stage 1
```

Write `_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS).md`:
```yaml
---
type: prune-manifest
batch: prune-YYYY-MM-DD-HHMMSS
status: in-progress
date: YYYY-MM-DD
---
```

Body — list every intended action:
```markdown
# Prune Batch Manifest

> **If this file exists AND its frontmatter says `status: in-progress`, a `/prune` operation did not complete successfully.**
> Recovery: `/rollback [any ticker below]` → select `(pre-prune)` snapshot → cascade (a) to undo all completed actions.
> Then delete this manifest and re-run `/prune`.
>
> **If this file's frontmatter says `status: completed`**, the prune finished but Stage 5 manifest cleanup did not. Safe to delete manually (e.g., `rm "_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS).md"`). `/clean` also surfaces these under "Completed prune manifests — safe to delete manually".

## Intended Closures
- TICKER1 - Company1
- TICKER2 - Company2

## Intended Upgrades
- TICKER3 - Company3 (conviction low → medium)

## Affected Sector Notes
- Sector Name (closures: TICKER1, TICKER2; upgrades: TICKER3)

## Downstream Content Propagation (Stage 4.2 targets)
- Neighbor theses receiving closure-notification Log entries: [list from Stage 2 step 3 neighbor scans]
- Macro notes referencing closed theses (reported only, not edited): [list from 4.2a step 2 scan]
```

This file is marked `status: completed` then deleted at the end of Stage 5 after all stages succeed (see Manifest Cleanup below).

### Stage 2: Process ALL Thesis Closures

For each approved closure:
1. Add final Log entry: `### YYYY-MM-DD\n- CLOSED: [rationale]. Archived.`
2. Change frontmatter: `status: closed`
3. **Record neighbor list for graph invalidation** (before the move, while the thesis filename is still easy to grep against). Grep `Theses/` (excluding the thesis about to be archived) for wikilink patterns `[[Theses/TICKER - Name]]`, `[[Theses/TICKER - Name|...]]`, `[[Theses/TICKER - Name#...]]`, `[[Theses/TICKER - Name.md]]`, `[[TICKER - Name]]`, `[[TICKER - Name|...]]`, `[[TICKER - Name#...]]`. Dedup the file list, collect as this closure's neighbor set.
4. Move file to `_Archive/`:
   ```bash
   mv "Theses/TICKER - Company Name.md" "_Archive/TICKER - Company Name.md"
   ```
5. **Archive-ticker registry update** (per `/status` Step 7.5b spec — supports `/thesis` Signal C): append to `.archive_ticker_registry.md` at vault root. Create with canonical header on first write, otherwise append:
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
     "$TICKER" "$ARCHIVED_FILENAME" "$(date +%Y-%m-%d)" \
     "$CONVICTION_AT_CLOSURE" "$CLOSURE_RATIONALE_LINE" \
     >> "$REGISTRY"
   ```
   Registry append failure does not abort the closure — log a warning and continue. The appends for all closures in this prune batch happen within Stage 2 iteration; there is no separate batching stage.

Do NOT update sector notes here — batched in Stage 4. Do NOT write `.graph_invalidations` per-closure — batched in Stage 4.5 so the file is written once for the whole prune run.

**If a closure fails mid-stage**: Report which closures completed and which failed. All pre-prune snapshots from Stage 1 are available for recovery. The batch manifest from Stage 1.5 persists and records all intended actions:
```
⚠️ Closure failed for [TICKER] at step [N]. Completed: [list]. Failed: [list]. Pending: [list].
All pre-prune snapshots available (batch: prune-YYYY-MM-DD-HHMMSS).
Batch manifest: [[_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS)]]
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

Do NOT rewrite wikilinks across the vault in this stage. Downstream content propagation (Log annotations on neighbor theses, macro-note surfacing) happens in Stage 4.2 and is append-only — no body-prose or existing-wikilink edits.

> **Why sector notes are updated last among same-type targets**: Stages 2–3 modify thesis files only. If the skill fails during Stages 2–3, sector notes remain untouched and internally consistent — they still reference the original thesis paths. The snapshots from Stage 1 enable full cascade recovery. Only after all thesis modifications succeed do sector notes get updated.

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to update the dependency map for archived theses (Adjacency Index removal, reverse-index cleanup, ghost cross-thesis ref scrubbing, orphan reclassification of research notes that were only linked from archived theses).

### Stage 4.2: Propagate Closures to Downstream Content (only if closures occurred)

Skip entirely if Stage 2 processed zero closures. For closure runs, extend propagation beyond sector notes — macro notes and cross-referencing theses also need to reflect the closure. Without this stage, a macro note's "affected theses" list or another thesis's cross-thesis narrative silently references an archived thesis; users discover the staleness only via `/lint` or by accidentally pitching a closed position.

Neighbor thesis sets were collected at Stage 2 step 3 (used by Stage 4.5 for graph invalidation). Stage 4.2 reuses those sets for content propagation, plus scans `Macro/*.md` for wikilink references.

#### 4.2a: Identify downstream files per closure

For each closed thesis, two target groups:

1. **Cross-referencing theses**: already collected in Stage 2 step 3. These are `Theses/*.md` files whose body contains a wikilink to the closed thesis.
2. **Macro notes with references**: grep `Macro/*.md` for the same wikilink patterns used in Stage 2 step 3 (`[[Theses/TICKER - Name]]`, `[[Theses/TICKER - Name|alias]]`, `[[TICKER - Name]]`, etc.). Collect the affected macro file list.

Exclude `_Archive/`, `_Archive/Snapshots/`, `_Inbox/processed/`, and `.git/` from both scans — closures don't propagate into historical or already-archived content.

#### 4.2b: Append closure-notification Log entry to each affected thesis

For every neighbor thesis identified in 4.2a step 1, append a single dated Log entry to the thesis's `## Log` section:

```
### YYYY-MM-DD
- Cross-thesis closure: [[_Archive/CLOSED_TICKER - Company Name]] archived — [one-line rationale from the /prune recommendation]. Cross-thesis and Related Research wikilinks retained; review body prose if thesis impact has changed.
```

Rules:
- **One Log entry per affected thesis** regardless of how many closures affected it. If thesis NVDA cross-references three closed theses (TICKER1, TICKER2, TICKER3) in this prune run, the Log entry names all three as one bullet: `Cross-thesis closures: [[_Archive/TICKER1 - ...]], [[_Archive/TICKER2 - ...]], [[_Archive/TICKER3 - ...]] archived this run — ...`
- **Max 2 lines per CLAUDE.md Writing Standards**. Collapse rationales if the list runs long: `... and 2 more — see /prune output`
- **Archive path wikilinks**: use `[[_Archive/TICKER - Company Name]]` (not `[[Theses/...]]`) so the link points to where the closed thesis actually lives. Obsidian resolves `_Archive/` wikilinks natively.
- **Do NOT modify body prose** — wikilinks to the closed thesis in the thesis's Cross-Thesis section, Related Research, or body narrative are preserved intact. The Log annotation is the notification; the user reviews the body at their pace.
- **Do NOT snapshot for 4.2b** — Log appends are Tier B (append-only) per CLAUDE.md Change Safety Rules. Stage 1 thesis snapshots don't cover neighbor theses, and snapshotting every neighbor would explode the batch size. If an append fails, the thesis is unchanged.

**Failure handling**: if an Edit to append the Log entry fails for a given neighbor thesis, do NOT abort the stage. Log the failure and continue with the next neighbor. Report all failed appends in the final summary so the user can inspect.

#### 4.2c: Macro note handling — detect and report, do not auto-edit

Macro notes are narrative documents with variable structure; not every macro note has a `## Log` section, and body prose often embeds thesis wikilinks in analytical sentences (e.g., "Iranian retaliation risk most directly affects [[Theses/LITE - Lumentum]]..."). Auto-editing these can destroy analytical coherence.

For each macro note identified in 4.2a step 2:
- Do NOT edit the file.
- Collect the `(macro note path, affected-thesis list)` pairs for the final Stage 4.2 report.
- Surface in the user-facing report as: `⚠️ Macro references to closed theses — review manually:`
  ```
  - [[Macro/Iran conflict — Transmission Map]] references [[CLOSED_TICKER1 - ...]] (now archived)
  - [[Macro/AI capex cycle]] references [[CLOSED_TICKER1 - ...]], [[CLOSED_TICKER2 - ...]] (now archived)
  ```

The user can then decide per macro note whether to: (a) rewrite the prose to reflect closure, (b) leave as-is (historical macro analysis that remains informative), or (c) add a note/strikethrough. `/prune` takes no action.

#### 4.2d: Stage report

Include in the final Stage 5 report:
- **Cross-thesis Log annotations**: `[N] neighbor theses received closure-notification Log entries: [list]. [M] Edit failures: [list with reason].`
- **Macro notes referencing closures**: `[N] macro notes contain wikilinks to archived theses — manual review recommended: [list pairs].`

### Stage 4.5: Write Graph Invalidation List (only if closures occurred)

Skip entirely if Stage 2 processed zero closures. For prune runs with closures, merge every closure's neighbor set (collected at Stage 2 step 3) into a single deduplicated list, then append to `.graph_invalidations` at vault root:

```bash
{
  [ -f .graph_invalidations ] && cat .graph_invalidations
  # Deduplicated union of Stage 2 neighbor sets (all closures):
  printf '%s\n' "Theses/NEIGHBOR1 - ...md" "Theses/NEIGHBOR2 - ...md" ...
} | sort -u > .graph_invalidations.tmp && mv .graph_invalidations.tmp .graph_invalidations
```

Rationale: every closure made some neighbors' `cross-thesis:` references stale. `/graph last` uses this file to re-extract those neighbors on its next run. Writing once per prune (rather than per-closure) keeps the file from thrashing during a large prune batch; the file is processed and cleared by the first `/graph last` after this skill.

**Failure handling**: If the file write fails, report the failure but do NOT abort the prune — closures/upgrades/sector updates already succeeded. User can manually rebuild via `/graph` (full). Report: `⚠️ .graph_invalidations write failed — run /graph (full rebuild) instead of /graph last to clean stale cross-thesis refs.`

Update `_hot.md` per `.claude/skills/_shared/hot-md-contract.md` (read first, then edit — do NOT touch Latest Sync or Sync Archive, owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: pruned portfolio — [N] closed, [N] upgraded, and the logical next step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry for each ticker where conviction was upgraded; add entry for each closure
3. **Open Questions**: Remove questions related to closed theses; add any new questions raised by upgrades
4. **Portfolio Snapshot**: Update conviction-level counts and sector coverage if materially changed

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

### Manifest Retention (5.2 fix — 30-day regret-recovery window)

All stages completed successfully. **Change from prior behavior**: `/prune` no longer deletes the manifest at Stage 5. The manifest is **retained for 30 days** as a regret-recovery breadcrumb — if the user realizes within 30 days that an approved closure was wrong, the manifest enables `/rollback` cascade detection to find every affected file (including neighbor theses' Tier B "Cross-thesis closure" Log entries from Stage 4.2, which are otherwise orphan audit entries).

Cleanup is now a verify-only sequence: flip status, verify the flip landed, then leave in place. `/clean` Step 2a (extended) handles eventual deletion on age.

1. **Flip manifest status**: Edit the manifest's frontmatter — change `status: in-progress` to `status: completed` and add `completed_date: YYYY-MM-DD`.

2. **Verify the flip landed**: re-read the manifest frontmatter and confirm `status: completed` is present AND `status: in-progress` is absent.
   - **On verification success** → the manifest stays in `_Archive/Snapshots/` with `status: completed`. `/clean` and `/lint #36` handle aging per the new retention policy (below).
   - **On verification failure** (flip Edit silently missed): do NOT attempt any repair. Report `❌ Manifest status flip failed: [[_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS)]] is still marked in-progress despite successful prune completion. DO NOT run /rollback — the prune closures/upgrades/sector updates/downstream propagation have all succeeded; rolling back would undo valid work. Manual fix: open the manifest and replace status: in-progress with status: completed. The manifest will then age out via /clean after 30 days. /lint #36 flagging it as Critical is a false alarm in this specific case.` Exit the skill with this explicit warning.

3. **NO deletion step.** The manifest persists until `/clean` removes it (30 days after `completed_date:`) or the user manually `rm`s it after confirming the prune is no longer a regret candidate.

### Retention policy & downstream contract

- **Days 0–30 after `completed_date:`**: manifest stays. `/rollback` cascade-detection can find the batch and surface Tier B Log entries for neighbor review during regret-recovery. `/lint #36` treats as Pass.
- **Days 30+**: `/clean` (any mode — default 180, custom, or orphans) removes completed prune manifests via the new Step 2a extension. `/lint #36` begins emitting Nice to Have at 30+ days, advising `/clean` or manual `rm`.

**Why 30 days**: matches typical investment-decision regret window — quarterly earnings cycle, position sizing review, macro shock digestion. Beyond 30 days, Tier B cascade recovery has diminishing value (the user's vault has absorbed the closure; neighbor Logs are now read as historical context, not stale premise).

**User regret-recovery flow** (now supported):
```
User realizes an approved /prune closure was wrong.
If `completed_date:` is within 30 days:
  /rollback [any ticker from manifest's Intended Closures]
  → select (pre-prune) snapshot → cascade (a) to restore all files
  → /rollback Step 6.5 (new — see /rollback SKILL.md) surfaces neighbor
    Tier B Log entries for strikethrough review
  → delete the manifest manually after recovery: rm "_Archive/Snapshots/_prune-manifest..."
```

Report final count of actions taken. Include the manifest's final state:
- `completed — retained for 30-day regret-recovery window` (happy path)
- `⚠️ flip verification failed — manifest still in-progress despite prune success; do NOT /rollback, resolve manually per the warning above`
