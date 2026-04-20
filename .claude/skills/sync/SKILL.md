---
name: sync
description: Synchronize recent research learnings across all affected theses, sector notes, and macro documents. Use after a research session or when user says "sync", "propagate", or "update everything".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * find * cp * mkdir * touch *)
---

**Follow CLAUDE.md Writing Standards strictly in all output.** No hedge words, no restating known context, no connective tissue. Every line must contain a data point, an insight, or a specific claim.

Propagate recent research insights across all affected vault documents. **This is a deep analytical operation — for each affected note, think through the full implications of new research on every substantive section, not just append links.**

## Step 0: Pre-flight (MANDATORY — runs before Step 1)

### 0.1: Acquire vault lock
- **`/sync` (default) and `/sync all`**: acquire `vault-wide` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 15 minutes for `/sync all`, 5 minutes for default.
- **`/sync TICKER`**: acquire `ticker:TICKER` scope lock. Timeout budget: 5 minutes.

Capture the token emitted at Step 0.1, verify ownership (Procedure 1.5) at every subsequent Bash block, release explicitly in the final reporting Bash block via `rm -f "$LOCK_FILE"`.

### 0.2: Rename-marker check
- **`/sync TICKER`**: run `.claude/skills/_shared/preflight.md` Procedure 2. If `.rename_incomplete.TICKER` exists, hard-block.
- **`/sync` (default) and `/sync all`**: glob `.rename_incomplete.*`. If ANY marker exists, hard-block — these modes propagate across the vault; a single mid-rename ticker would have inbound wikilinks split across names, and sync's cross-thesis Log appends would embed the current name while some references remain with the old name.

**Metadata boundary**: `/sync` does not write to `_graph.md`. Graph maintenance is owned exclusively by `/graph` (run `/graph last` after this skill). `/sync`'s job is content propagation only — thesis bodies, sector notes, macro notes, `_hot.md`.

## Sync Modes

Parse `$ARGUMENTS` for mode:

- **`/sync`** (default) — **Graph-assisted targeted sync.** If `_graph.md` exists, use it to resolve dependencies. If absent or stale, fall back to file-traversal resolution (no penalty — research skills don't depend on graph). Use for routine post-ingest propagation.
- **`/sync all`** — **Full brute-force sync.** Reads all theses, all sector notes, all macro notes via two-pass triage. Use after major research sessions or monthly maintenance.
- **`/sync TICKER`** — **Ticker-scoped sync.** Reads the thesis directly and reconstructs its adjacency from outbound wikilinks. No graph dependency. Use after manually editing a thesis or for targeted propagation.

## Watermark

Change detection uses `.last_sync` as the timestamp watermark.

**Touch policy by mode** (Step 7 enforces):
- **`/sync` (default)**: touch `.last_sync` at end of run. The watermark advances to "now" so the next default sync's `find -newer .last_sync` captures only files changed after this run.
- **`/sync all`**: touch `.last_sync` at end of run, AND write `.sync_all_fresh` marker (per Step 7).
- **`/sync TICKER`**: **do NOT touch `.last_sync`**. Ticker-scoped mode operates on a bounded subset (one thesis + its file-direct adjacency) and explicitly ignores the watermark for change detection. Advancing the watermark would silently mark unrelated changes (other theses, macros, sectors modified before this run) as "synced" when ticker-scoped mode never read them. The next default `/sync` would then miss those propagation paths because `find -newer .last_sync` skips them.

If `.last_sync` does not exist (first run), create it with an epoch timestamp and treat all files as changed:
```bash
touch -t 197001010000 .last_sync
```
> **First-run exception for `/sync TICKER`**: if `.last_sync` is absent, ticker-scoped mode also creates the epoch placeholder so subsequent default `/sync` runs have a baseline. Creating an epoch file is not the same as advancing it — the watermark stays maximally permissive ("treat everything as changed since 1970") so the next default `/sync` re-evaluates the full vault.

`/sync` never reads or writes `_graph.md`'s `date:` frontmatter — graph timing is `/graph`'s concern, not `/sync`'s.

---

## Step 1: Identify Changes

- If `$ARGUMENTS` specifies files, use those as the source.
- Otherwise, find all files modified since the last sync:
  ```bash
  find Research/ Theses/ Macro/ Sectors/ -newer .last_sync -name '*.md'
  ```
- If no changed files are found and no files were specified, report "Nothing changed since last sync" and stop.
- Read each modified/new note to extract propagatable insights.

### Pre-propagation deduplication

For each changed research note, the target set is the UNION of every thesis plausibly affected by the note — resolved via graph-assisted mode and the file-direct fallback below. `propagated_to:` frontmatter is treated as a dedup hint (which theses are already marked as propagated-to by the producer skill), **not** as a target cap.

This matters because producer skills embed intentional filtering in `propagated_to:`: `/scenario` includes only Major-impact theses, `/stress-test` only the tested ticker, `/compare` only tickers with existing theses. If `/sync` used `propagated_to:` as the target set, minor-impact theses that wikilink-reference the research note would never receive propagation via `/sync`. Augmenting (not capping) keeps `/sync` the universal propagation mechanism while honoring dedup against producer-embedded targets.

Three checks, applied in order:

1. **Compute full target set** (UNION — never capped by `propagated_to:`):
   - **Graph-assisted resolution** (if `_graph.md` exists): find every thesis that lists the research note in its `research:` adjacency.
   - **File-direct fallback** (always runs to catch targets the graph may miss): resolve via (a) research note's `ticker:` frontmatter matching `Theses/[TICKER] - *.md`, (b) outbound `[[Theses/...]]` wikilinks in the research note body, (c) `tags:` containing ticker-shaped tokens (all-uppercase, 1-5 chars) that match `Theses/[TICKER] - *.md`.
   - Union the results. Dedup thesis filenames.

2. **`propagated_to:` dedup hint**: Three cases based on the field's presence and content:

   **Case 2a — Field absent** (`propagated_to:` not in frontmatter): no producer-side dedup info. Before treating the entire Step 1 target set as needing propagation, run the **Log-history backfill scan** to catch retry cases where a producer skill (`/compare`, `/scenario`, `/stress-test`) wrote Log entries on some tickers, failed on others, and correctly omitted `propagated_to:` per its atomicity rule.

   For each candidate ticker in the Step 1 target set:
   1. Read the thesis's `## Log` section in full.
   2. Search for any `- `-bulleted line referencing the source research note's exact wikilink. Match all five forms the producer skills emit: `[[Research/base-name]]`, `[[Research/base-name.md]]`, `[[Research/base-name|alias]]`, `[[Research/base-name#section]]`, `[[base-name]]` (folder-less form).
   3. If ANY line matches regardless of date → producer-equivalent already-propagated. Skip this ticker for this run. Log: `ℹ️ Log-history backfill skip: [TICKER] already has Log entry referencing [research-note] (dated [found-date]). propagated_to: absent likely indicates prior producer atomicity-rule fire; retry suppressed to prevent cross-day duplicate.`
   4. If no line matches → proceed to Check 3 per-thesis idempotency for this ticker (strict calendar-day match).

   **Why the Log-history backfill is safe**: research notes are Tier 2 "immutable source record" per CLAUDE.md — edits to a research note's body should go into a new note or a thesis Log entry, not retroactively re-propagate. If a producer skill partially failed on day D, succeeded tickers carry a day-D Log entry that the scan finds; failed tickers carry no entry and get retried. The scan's once-propagated-is-terminal semantics match Case 2b exactly — treating an existing Log entry as structurally equivalent to an explicit producer dedup claim.

   **What this fixes**: without the backfill scan, a partial `/compare A vs B vs C` failure (A, B succeed on day D; C fails; `propagated_to:` omitted) causes day-D+N default `/sync` to see Case 2a field-absent and, via Check 3, re-propagate to A and B because their Log entries are dated D, not today. The retry would write duplicate Log entries on already-succeeded tickers. The backfill scan finds A's and B's day-D entries, skips them, and leaves C for Check 3's normal propagation path.

   **Cross-midnight producer-run edge case**: if a producer started at 23:58 on day D and wrote some entries at that timestamp while failing others at 00:02 on day D+1, the scan ignores dates entirely — both successful tickers are correctly skipped on the next `/sync` regardless of when exactly their entries landed.

   **Interaction with user-edited research notes**: if the user manually edits a research note's body after the initial propagation, the scan still skips already-propagated theses. This is the intended Tier 2 behavior (research notes are immutable source records) — intentional re-propagation requires creating a new research note or appending a thesis Log entry directly.

   After the scan: remaining candidates (no matching Log entry found) proceed to Check 3 per-thesis idempotency for the strict today-date check.

   **`propagated_to:` backfill-update on scan-driven skips**: if the scan skipped any ticker in this run, update the research note's `propagated_to:` frontmatter to include those tickers as a union with any already-listed ones. This moves the retry from Case 2a into Case 2b on future `/sync` runs, eliminating the scan cost for this research note going forward. Apply the same all-or-nothing atomicity as Case 2b: only update after the scan + any remaining Check-3 propagation fully succeeds.

   **Case 2b — Field present and non-empty** (e.g., `propagated_to: [TICKER1, TICKER2]`, set by `/stress-test`, `/scenario`, `/compare`, `/deepen`): treat each listed ticker as "already propagated by the producer skill" — **skip them for this run**. These tickers received Log entries directly from the producer; re-propagating would produce near-duplicate entries. Log: `ℹ️ Skipped [TICKER] — producer skill already propagated (in propagated_to).`
     - **Exception — augmented targets**: Tickers in the Step 1 target set that are NOT in `propagated_to:` are new additions via wikilink/tag/ticker resolution. Log: `➕ Augmented propagation: [TICKER] — not in propagated_to but resolved via [wikilink | tag | ticker frontmatter].` Proceed to Check 3 for these tickers.

   **Case 2c — Field present and empty** (`propagated_to: []`, set by `/surface`, `/brief`, or any future producer that emits exploratory/derivative notes): this is a **terminal dedup signal** — the producer explicitly declares "no thesis propagation needed for this note." Skip ALL targets resolved in Step 1 regardless of how they were resolved (graph adjacency, wikilink, ticker frontmatter, tag). Do NOT proceed to Check 3 for any ticker. Log once: `ℹ️ Skipped all propagation for [research-note] — empty propagated_to: signals producer-side terminal decision (e.g., surface scan, brief). No Log entries written, no augmented targets evaluated.`
     - **Why empty-list is terminal, not "nothing yet propagated"**: a producer that wanted "propagate to all wikilink-resolved targets but I haven't done any myself" would simply omit the field (Case 2a). Setting `propagated_to: []` explicitly is a deliberate "this note's body wikilinks are contextual references, not propagation targets" signal. Required for `/surface` (whose scan notes wikilink 10+ theses for context) and `/brief` (derivative summary of an already-existing thesis). Without this case, `/sync` would Log-spam every wikilink-referenced thesis on every surface/brief.
     - **Skill compliance**: producers must set `propagated_to: []` explicitly in frontmatter at note-creation time. `/surface` and `/brief` do so per their respective Phase 4 / Phase 4 specs. Future producers emitting exploratory notes must follow the same pattern.

3. **Per-thesis idempotency check** (research-note-identity keyed, not date-keyed): For each target thesis, determine whether this research note has already propagated via FOUR identity keys checked in order. Any match → skip propagation.

   **Primary key — wikilink presence** (existing): scan the thesis's `## Log` section for any `- `-bulleted line referencing the source research note's wikilink — regardless of the `### YYYY-MM-DD` date header that precedes it. Match rule: research note's wikilink appears in any of five producer forms (`[[Research/base-name]]`, `[[Research/base-name.md]]`, `[[Research/base-name|alias]]`, `[[Research/base-name#section]]`, `[[base-name]]` folder-less).

   **Secondary keys (H4 fix — added to handle research-note renames and moves)** — if the wikilink primary key doesn't match, check these fallback identities before propagating:

   1. **`source:` URL match**: if the current research note's frontmatter `source:` is a URL (not "vault synthesis"), scan the thesis's `## Log` section for any Log entry citing a wikilink to a Research/ note whose own `source:` matches the same URL (requires a brief cross-read of candidate research notes). Match = same URL → treat as already-propagated. Handles the case where the research note was renamed — the wikilink in the Log cites the OLD name, so primary key misses, but the underlying source URL is identical.

   2. **`date: + ticker:` frontmatter tuple match**: if no source URL (vault-synthesis notes like `/scenario`, `/stress-test`, `/compare` outputs), scan the thesis Log for entries citing Research/ notes with the same `date:` AND the same `ticker:` as the current note. Match = same date-and-ticker tuple → treat as already-propagated. Handles research notes moved to a different subfolder OR renamed, where wikilink drifted but the frontmatter identity is stable.

   3. **`tags: [ticker-shaped tokens]` intersection match** (weakest, used only when #1 and #2 both miss): if the current research note's tags include ticker-shaped tokens overlapping with this thesis's `ticker:`, AND the thesis Log has ANY entry citing a Research/ wikilink where the linked note's `tags:` include the same ticker-shaped tokens — treat as already-propagated only if the date on that Log entry matches the current note's `date:`. This weakest key guards against false positives where the same ticker appears in many unrelated research notes.

   If any of the four keys (primary + three fallbacks) matches, skip:
   `ℹ️ Skipped duplicate propagation for [TICKER] — Log already references equivalent research note ([matched key type]: wikilink|source URL|date+ticker|tags). Current wikilink: [[Research/current-name]]. Prior match: [found wikilink/key detail].`

   > **Why secondary keys matter (H4)**: the primary wikilink-based idempotency breaks if a research note is renamed (e.g., user fixes a typo in the filename slug). The old wikilink in thesis Logs doesn't match the new filename, so `/sync` would re-propagate as if it were a new research note — producing duplicate Log entries. Secondary keys preserve idempotency across legitimate user-driven file moves/renames by keying on stable identity properties (source URL, date+ticker tuple, tag intersection) that don't change when filename changes.

   > **Performance note**: secondary key checks read candidate research notes' frontmatter (not bodies) and only fire when the primary key misses. For typical `/sync` runs, the primary key catches all legitimate dedup cases; secondary keys are the exception path.

> **Why research-note-path keying, not today-date keying (6.11)**: the prior spec keyed idempotency on `entry_date == today`. That produced a cross-midnight duplicate: `/sync` at 23:59 on day D writes entry dated `### [D]`; a re-run at 00:01 on day D+1 sees today = D+1, finds only `### [D]` in the Log → mismatch → writes a duplicate entry `### [D+1]` referencing the same research note. Research-note-path keying (wikilink presence anywhere in the Log) eliminates this: once a research note has propagated to a thesis, it is terminal — the thesis's Log is a permanent audit of which research notes have informed it. This also matches the semantic meaning of CLAUDE.md Tier 2 append-only: research notes are immutable source records; after initial propagation, subsequent runs on the same note produce no new signal.

> **Cross-midnight edge case (now correctly handled)**: `/scenario` wrote `### 2026-04-18` at 23:58 citing `[[Research/X]]`. `/sync` at 00:02 on 2026-04-19 scans the thesis's Log, finds the day-D entry wikilinking `[[Research/X]]`, and skips propagation. Correct — the research already propagated; the day boundary is irrelevant.

> **User-intent edge case**: if the user edits the research note's body later and wants to re-propagate, the contract is: create a NEW research note OR append a thesis Log entry directly (CLAUDE.md Tier 2 "research notes are immutable source records"). `/sync` does not re-propagate a research note that has already reached a thesis, regardless of when or how the research note changed. This matches the prior "Log-history backfill" Case 2a skip semantics — consolidating Check 3 with the Case 2a scan.

This idempotency check catches the case where a producer skill wrote Log entries and a subsequent `/sync` finds the same research note via timestamp detection. The window is intentionally simple — no 4-bucket classification, no rolling-time arithmetic, no partial-repair branches. If no Log entry references this research note, propagate normally.

**Atomicity rule for `propagated_to:` update** — update the research note's `propagated_to:` frontmatter **only after EVERY target thesis's Log entry has landed successfully** for this research note in this `/sync` run. If any thesis append failed (Edit error, file locked, missing Log section), do NOT update `propagated_to:` at all for this research note — the next `/sync` will retry the missing target and the `propagated_to:` union will catch up then. A partial `propagated_to:` update would claim theses as propagated when their Log entries never landed, creating a permanent audit gap that future `/sync` runs silently skip because the dedup hint says "already done".

**If every append succeeded**, update the frontmatter by unioning the just-propagated tickers with whatever was already there:
```yaml
propagated_to: [existing, ..., newly_propagated_by_sync, ...]
```
This ensures subsequent `/sync` runs see the augmented targets as already-propagated on the re-run, preventing re-propagation loops without introducing a new silent-skip hazard.

**Scope of the all-or-nothing rule**: the atomicity unit is one research note's propagation set. If `/sync` is processing several research notes in one run and one research note has an append failure, the others that succeeded still get their `propagated_to:` updated — the atomicity is scoped per research note, not per run.

**Per-research-note append-failure reporting**: list the failed target(s) in Step 8 report under a new field `propagated_to: update skipped` with the specific research note and the failed target(s).

### Graph-assisted mode (default)

If `_graph.md` exists, read it to optimize dependency resolution:
1. For each changed Research note → look up which theses link to it in the Adjacency Index. If found, include those theses in the propagation set.
2. For each changed Thesis → look up its sector notes, macro notes, and cross-thesis references in the Adjacency Index.
3. For each changed Macro note → use the Macro reverse index to find affected theses.
4. For each changed Sector note → use the Sector reverse index to find member theses.

**File-direct fallback** (used when `_graph.md` is missing, stale, doesn't list the changed file, or the reverse index returns an empty target set):

For changed research notes not found in the graph:
1. Check the research note's `ticker:` frontmatter — if it matches a `Theses/[TICKER] - *.md` file, include that thesis.
2. Check outbound `[[Theses/...]]` wikilinks in the research note body — include each linked thesis.
3. Check `tags:` for ticker tokens (all-uppercase, 1-5 chars) matching `Theses/[TICKER] - *.md` filenames.
4. If the graph exists, check outbound `[[Macro/...]]` wikilinks against the Macro reverse index.

**For changed macro notes** (mirrors the research-note fallback pattern — runs even when the graph exists, to catch theses that declare `[[Macro/X]]` adjacency without the macro reciprocating `[[Theses/TICKER]]`):

1. **Reverse-index resolution** (graph-assisted, primary): Use the Macro → Theses reverse index in `_graph.md` to find theses whose `cross-thesis: macro:` adjacency lists the changed macro note. This catches the bidirectional case where the macro body wikilinks the thesis.
2. **Body-grep fallback** (always runs to catch one-direction adjacency): grep `Theses/*.md` for wikilink patterns referencing the changed macro filename:
   - `[[Macro/[macro-basename]]]`
   - `[[Macro/[macro-basename]|alias]]`
   - `[[Macro/[macro-basename]#section]]`
   - `[[Macro/[macro-basename].md]]`
   - `[[[macro-basename]]]` (folder-less form, less common)
   For each matching thesis file, include it in the propagation set. Dedup against reverse-index results.

> **Why the body-grep fallback is necessary**: the reverse index is built from the macro note's outbound wikilinks (`[[Theses/...]]` in the macro body). If a thesis declares `[[Macro/X]]` but the macro doesn't reciprocate `[[Theses/TICKER]]`, the reverse index returns empty for that macro, and the thesis silently fails to receive propagation when the macro is edited. The body-grep fallback closes this gap. `/lint #23` (reverse-index consistency) catches the asymmetry periodically; the fallback ensures correct propagation between lint runs.

**For changed sector notes**: graph-assisted reverse-index resolution is sufficient — sector notes are required by template (`Templates/Sector Template.md`) to have `## Active Theses` listing every active thesis. `/lint #2` (Missing MOC entries) catches theses with `sector:` frontmatter missing from their sector note's Active Theses listing. **Caveat**: sector structural compliance (e.g., a sector note that loses its `## Active Theses` heading entirely) is not currently enforced by any `/lint` check — relies on user discipline + Sector Template authoring conventions. If a sector note's reverse-index population becomes unreliable in practice, add a body-grep fallback for sectors mirroring the macro fallback above.

**Closed-status check**: For every thesis identified above, read its frontmatter. If `status: closed` AND the file is still in `Theses/`, skip propagation and log: `⚠️ Skipped [TICKER] — status: closed but file remains in Theses/ (failed archive move). Complete: mv "Theses/[file]" "_Archive/[file]" → /graph last. Or reopen: /status TICKER status closed→active [rationale].`

**Missing file resilience**: If a thesis listed in the graph no longer exists on disk (archived since last graph rebuild), skip it gracefully and log: `⚠️ Skipped [filename] — file not found (likely archived). Run /graph last to refresh the dependency map.`

**Unresolved research notes**: If no target thesis can be identified through any of the above paths, log: `ℹ️ [filename] — no propagation target found. Consider adding ticker: frontmatter or [[Theses/...]] wikilinks, or run /thesis [TICKER] to create the missing thesis.` Include in Step 8 report. The note is left in the vault for future runs.

### All mode (Two-Pass Triage)

Reading all ~40 thesis notes, ~13 sector notes, and ~6 macro notes in full will exceed context limits. Use a lightweight scan to triage by delta significance, then deep-read only notes with meaningful propagation paths.

#### Pass 1 — Lightweight scan
1. Identify changed files using `.last_sync` watermark. If first run, treat all files as changed.
2. For each thesis in `Theses/`, read **only frontmatter + Summary + last 3 Log entries** (stop after the 3rd-most-recent `###` Log heading). ~300-400 words per thesis.
3. For each sector note in `Sectors/`, read **only frontmatter + Active Theses + Log sections**.
4. Read ALL macro notes in full (small set, ~6 files).

#### Pass 2 — Triage and deep read
5. Using the lightweight summaries + the changed file list, classify each thesis:
   - **High delta** (any of):
     - **Self-modified**: the thesis's OWN file mtime is newer than `.last_sync` (the file appears in the changed-file set from Step 1). Captures manual edits where the user rewrote a section without writing a Log entry — those edits would otherwise be invisible to the heuristic-based classification below. Always escalate to High delta and read the **full thesis note**.
     - Directly referenced by a changed research note, OR
     - Shares sector with changed content, OR
     - Has cross-thesis links to changed theses, OR
     - Its own Log shows recent conviction/status changes
     → read the **full thesis note**.
   - **Low delta**: Same macro exposure or adjacent sector to changed content, but no direct reference AND not self-modified → read **Summary + Non-consensus Insights + Outstanding Questions + Bull/Bear Case** sections only (skip Business Model, Industry Context, Key Metrics).
   - **No delta**: No plausible propagation path from any changed content AND not self-modified → do NOT read further.

   > **Why "self-modified" must be its own High-delta trigger**: the four heuristics below it (referenced-by, shares-sector, cross-thesis-link, recent-Log) all infer "this thesis was affected" from external signals. None of them fire when the user manually edited the thesis itself with no Log entry — but that edit is exactly the kind of vault change `/sync all` is supposed to propagate. Classifying a self-edited thesis as No-delta because no other file references it would silently drop the user's manual changes from propagation analysis.
6. Read sector notes in full **only for sectors containing at least one High-delta thesis**.
7. Proceed to Step 2 with the prioritised reading set.

This typically reduces deep reads from ~58 files to 15-25.

### Ticker-scoped mode

1. Locate the thesis file via ticker-prefix glob: `Theses/TICKER - *.md`.
   - If no match, check `_Archive/TICKER - *.md`. If found, stop: `⚠️ [TICKER] is closed — file lives in _Archive/. To reopen: /rollback TICKER → select pre-status snapshot → /sync TICKER.`
   - If not found anywhere, stop: `⚠️ No thesis found for [TICKER]. Run /thesis [TICKER] to create it.`
   - If multiple matches, stop: `⚠️ Multiple Theses/ files match prefix "[TICKER]" — [list]. Resolve filename collision before re-running.`

2. **Closed-status gate**: Read the thesis's frontmatter. If `status: closed`, stop: `⚠️ [TICKER] has status: closed but file remains in Theses/ (failed archive move). Complete: mv "Theses/[file]" "_Archive/[file]" → /graph last. Or reopen: /status TICKER status closed→active [rationale].`

3. **Reconstruct adjacency from the thesis file** (do not read `_graph.md` — file-direct is the only path):
   - Extract outbound `[[wikilinks]]`. Categorize by directory:
     - `Sectors/` → sector adjacency
     - `Macro/` → macro adjacency
     - `Theses/` → cross-thesis adjacency
     - `Research/` → research adjacency
   - Also scan `Research/` for files with `ticker: TICKER` in frontmatter (catches newly-ingested research not yet in `Related Research`).

4. **Read all resolved files** — ignore `.last_sync` watermark (this mode is timestamp-independent).

5. Proceed to Step 2 with all resolved files as the input set.

## Step 2: Deep Implication Analysis

**This is the critical analytical step. Spend maximum reasoning effort here.**

**Source deduplication**: If a thesis appears as a changed source AND research notes referencing that thesis are also in the changed set, analyze the research notes as the primary sources. The thesis Log entries referencing those research notes do not contain additional propagatable information.

For each source note, read fully and analyse:

- **Factual deltas**: New data points, metrics, quotes, events — what is concretely new?
- **Assumption challenges**: Which existing thesis assumptions does this validate, weaken, or invalidate? Be specific — name the assumption.
- **Second-order implications**: What follows from this information that isn't stated explicitly?
- **Competitive dynamics shifts**: Does this change the relative positioning of companies within a sector?
- **Macro linkages**: Does this micro-level data have macro implications, or vice versa?

The quality of the entire propagation depends on the depth of thinking in this step.

## Step 2.5: Classify Change Sources

Before writing to any sector or macro note, classify every changed thesis in the Step 1 target set. The classification gates Step 4 and Step 5 sector/macro propagation — a thesis-only change driven by a skill that already handled downstream sector/macro state should not trigger a redundant `/sync` re-edit.

### Classification rule

For each changed thesis:

- **Research-driven** (default): at least one research note in the changed-file set resolves (via Step 1 target-set resolution) to this thesis, OR the thesis's recent Log entries reference changed research notes. Proceed through Step 3/4/5 normally.
- **Skill-origin**: the thesis is self-modified (`mtime > .last_sync`) AND its most recent Log entry's prefix matches one of the following skill-origin prefixes from `.claude/skills/_shared/log-prefixes.md` AND no research note in the changed-file set resolves to this thesis:
  - `"Status change: conviction"` (registry §6 — `/status` conviction branch; sector already updated in its Step 5)
  - `"Status change:"` (registry §7 — `/status` non-closure status branch; sector already updated)
  - `"Conviction reaffirmed"` (registry §5 — `/status` reaffirm flow; no sector or macro work expected)
  - `"CLOSED"` (registry §8 — `/status` or `/prune` closure; sector already updated, file typically already archived)
  - `"Prune upgrade"` (registry §9 — `/prune` Stage 3; sector conviction display already updated in Stage 4)
  - `"Cross-thesis closure:"` / `"Cross-thesis closures:"` (registry §13 — notification-only Log entry on a neighbor, not a conviction delta)
  - `"Scenario REVERSED"` (registry §14 — `/scenario reverse` R4; corrective Log append with no new research delta)
  - `"ROLLBACK to snapshot"` (registry §12 — `/rollback` Step 5.4; sector already handled in `/rollback` Step 6.1, thesis body reverted to snapshot state with no new research delta)
  - `"Initial thesis created"` (registry §11 — `/thesis` Step 4; sector Active Theses already updated in `/thesis` Step 5 for active theses)
  - `"Renamed file:"` (registry §15 — `/rename` Step 10; filename + wikilink operation with no analytical delta)
- **Mixed**: thesis has both a research-note source AND a skill-origin Log prefix in recent entries → treat as **research-driven**. Research notes drive propagatable content; the skill-origin prefix is informational only.

### Classification output

Maintain an in-memory accumulator `skill_origin_theses: [TICKER, ...]` throughout this step. Steps 4 and 5 consult this set before per-sector / per-macro propagation (see Step 4.-1 and Step 5.-1 below).

### Registry-driven design

The prefix list above is a view of `.claude/skills/_shared/log-prefixes.md`'s skill-origin entries. Each of the listed prefixes has `/sync Step 2.5 skill-origin classification` in its registry `consumers:` block. `/lint` check #29 verifies that every registry prefix with that consumer entry is also referenced in this step's list — any drift between the registry and this enumeration produces an Important lint finding.

**When a new skill-origin prefix is added**: update the registry first (add prefix + consumer entry), then add it to this step's list. The two must move together per the editing protocol in `_shared/log-prefixes.md`.

## Step 3: Update Thesis Notes

### 3a: Read the Full Thesis
Read the entire thesis note. Understand the current state of every section before proposing changes.

### 3b: Analyse Impact Per Section
Map the insights from Step 2 against each thesis section. Be selective — not every piece of research affects every section.

| Section | Update when... |
|---|---|
| **Summary** | The core investment case has shifted — not incremental data, but a change in thesis direction or key assumption |
| **Non-consensus Insights** | New evidence strengthens/weakens an existing insight, OR a genuinely new non-consensus angle emerged |
| **Outstanding Questions** | A question has been answered (mark resolved with answer + date), OR the research raises new questions worth tracking |
| **Business Model** | Structural change to revenue model, product mix, go-to-market, or segment economics |
| **Industry Context** | Competitive positioning, market share, or pricing power shifted |
| **Bull Case** | New supporting evidence, or a bull scenario element was validated/invalidated |
| **Bear Case** | New counter-evidence, or a bear scenario element was validated/invalidated |
| **Catalysts** | New catalyst identified, or existing catalyst resolved — mark outcome |
| **Risks** | New risk emerged, existing risk probability changed materially, or a risk was retired |
| **Conviction Triggers** | New evidence validates/invalidates a trigger condition, OR a trigger threshold needs updating |

**Do NOT update sections where the delta is trivial.** The thesis contains synthesised conclusions, not duplicated research content.

### 3c: Pre-Edit Safety — Snapshot

Classify proposed edits by tier:

**Tier A — Snapshot required:** Editing or rewriting existing text in Summary, Non-consensus Insights, Outstanding Questions, Business Model, Industry Context, Bull Case, Bear Case, Conviction Triggers.

**Tier B — No snapshot needed:** Appending new Catalysts, Risks, or Conviction Triggers. Appending to Log, Related Research. Updating numbers in Key Metrics table.

If any Tier A edits are planned for a thesis:
1. ```bash
   mkdir -p _Archive/Snapshots
   cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-sync YYYY-MM-DD-HHMMSS).md"
   ```
2. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Theses/TICKER - Company Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: sync
   snapshot_batch: sync-YYYY-MM-DD-HHMMSS
   ```
   > **Batch ID**: Generate `HHMMSS` once at the start of the snapshot phase via `date +%H%M%S` (6 digits — second-precision prevents same-minute snapshot batch collisions across skills). Reuse the same `snapshot_batch` value across ALL snapshots (thesis, sector, macro) created in this sync run for `/rollback` cascade detection.

3. Proceed with edits to the ORIGINAL thesis note.

### 3d: Apply Substantive Edits

- **Integrate, don't append** — weave new evidence into existing prose so the section reads as a coherent, up-to-date analysis. Do NOT add "Update (date): ..." blocks within sections.
- **Preserve voice and structure** — match the existing writing style and analytical depth.
- **Net deletions are OK** — if new evidence invalidates a prior claim, remove the claim rather than leaving it alongside its contradiction.
- **Mark resolved Outstanding Questions** — format: ~~Original question~~ → Resolved YYYY-MM-DD: [answer]. Keep resolved questions visible so the analytical trail is preserved.

### 3e: Mechanical Updates (every time)
- **Key Metrics**: Update table if new numbers are available
- **Related Research**: Add wikilink to new research note
- **Conviction trigger check**: If new data satisfies a pre-defined Conviction Trigger condition, flag it:
  `⚡ Trigger hit: [quote the trigger] — [what happened]`
- **Conviction drift detection**:
  > **Log Format Contract** — drift detection depends on exact prefix matching. **Authoritative registry**: `.claude/skills/_shared/log-prefixes.md`. `/lint` check #29 verifies registry consistency.

  Scan Log entries backward from most recent, **unconditionally excluding entries that begin with these prefixes**:
  - `"Stress test"` — periodic adversarial reviews, not deterioration evidence (registry §1).
  - `"Deepening"` — `/deepen` Phase 5a provisional entry; carries no conviction sentiment and is a stuck-state marker if it lingers without a matching `"Deepened"` (registry §2). Counting it would consume a drift-window slot without adding signal, and on failed-`/deepen` states it would bias the window toward "no recent progress."
  - `"Cross-thesis closure:"` and `"Cross-thesis closures:"` — `/prune`-emitted notifications about a DIFFERENT thesis being closed (registry §13). They carry no signal about this thesis's own conviction trajectory.
  - `"Scenario REVERSED"` — `/scenario reverse`-emitted corrective entry that withdraws a prior scenario propagation (registry §14). Counting it would inflate drift on theses that just had a scenario withdrawn — the whole point of reverse mode is to preserve audit trail without producing new drift signal.
  - `"Renamed file:"` — `/rename` Step 10 filename-change record (registry §15). Carries no conviction sentiment; consuming a drift-window slot on a cosmetic filename change would bias drift on recently renamed theses.

  **Conditionally exclude entries that begin with `"Deepened"` or `"↳ CORRECTION: Deepened"`** within **14 calendar days** of a `"Stress test"` entry for the same ticker (registry §3–§4 — T1.3 extended window from 7 to 14 days) — gap-filling research chained to a stress test, not independent evidence. The longer window reflects that `/deepen` runs triggered by stress-test findings can span 2+ weeks as the user works through each identified gap section sequentially.

  **Anchor handling**: If a `"Conviction reaffirmed"` (registry §5) or `"Status change: conviction"` (registry §6) entry is found, anchor the window there — only count entries AFTER the anchor. If fewer than 3 entries exist after the anchor, drift detection has insufficient data and does not fire. If no anchor exists, use the last 5 **non-excluded** entries as the window (i.e., count backward through the Log skipping exclusions until 5 eligible entries accumulate, or until Log exhaustion).

  **Drift threshold** (T1.3 — tunable via `.drift-config.md` at vault root):
  - Default base threshold: **3/5** weakening entries fires drift (conviction: high) or 3/5 strengthening (conviction: low).
  - **Post-stress-test suppression**: if a `"Stress test"` entry exists within the last **30 days** for this ticker, RAISE threshold to **4/5** (requires one more signal). Rationale: stress tests already surfaced vulnerabilities; subsequent "weakened" Log entries often reflect the stress-test-identified risks being incrementally confirmed, not new drift evidence.
  - **Optional config override**: if `.drift-config.md` exists at vault root, read it for overrides. Format:
    ```yaml
    ---
    window_size: 5              # default 5; min 3, max 10
    base_threshold: 3           # default 3/window_size
    post_stress_threshold: 4    # default 4/window_size
    post_stress_window_days: 30 # default 30
    deepened_exclusion_days: 14 # default 14 (was 7 pre-T1.3)
    ---
    ```
    Missing config → use defaults. Malformed config → log `⚠️ .drift-config.md malformed — using defaults.` and proceed.

  - conviction: high but threshold-reached entries in window weakening → `⚠️ Conviction drift — [N]/[window_size] recent updates flagged headwinds ([threshold] required, [post-stress-test suppression active: yes|no]). Reassess. To acknowledge after review: /status TICKER reaffirm [rationale]`
  - conviction: low but threshold-reached entries in window strengthening → `📈 Positive drift — [N]/[window_size] recent updates supportive. Reassess. To acknowledge after review: /status TICKER reaffirm [rationale]`

  > **T1.3 rationale**: prior behavior fired drift on 3/5 regardless of recent stress-test activity, producing false positives during the natural burst of `/stress-test` → `/deepen` → `/sync` cycles. The extended 14-day exclusion window for `Deepened` entries and the post-stress-test 4/5 threshold together reduce false-positive fires without materially changing true-positive detection rate.

### 3f: Log Entry (last)

Append to Log section:
```
### YYYY-MM-DD
- [[Research/source-note]]: [what changed] — [conviction impact: unchanged/strengthened/weakened + 1 reason]
```
Max 2 lines. The log is an audit trail — the analysis lives in the updated sections above.

## Step 4: Update Sector Notes

For each affected Sector Note:

### 4.-1: Skill-origin gate (runs before Step 4.0)

Before running Step 4.0's per-source idempotency check, consult `skill_origin_theses` from Step 2.5. A sector note's "affected thesis set" for this `/sync` run is every changed thesis whose `sector:` frontmatter resolves to this sector (via `_graph.md` reverse index OR `_shared/sector-resolution.md` fallback).

**Gate rule**: if EVERY thesis in this sector's affected set is in `skill_origin_theses` AND no research note in the changed-file set resolves to this sector (via its `sector:` frontmatter OR body `[[Sectors/...]]` wikilinks), skip Step 4.0, 4a, 4b, 4c entirely for this sector. Log: `ℹ️ Skipped sector update [Sector Name] — all [N] affected thesis changes are skill-origin (Status change/Prune upgrade/Scenario REVERSED/ROLLBACK/etc.); originating skills already handled sector state, and no co-changed research note carries propagatable content.`

**Mixed set**: if the affected thesis set contains at least one research-driven thesis, proceed to Step 4.0 per existing logic — the research-driven thesis's propagatable delta applies to the whole sector section (value chain, competitive dynamics, etc.), and the skill-origin theses coincidentally sharing the sector do not suppress the propagation.

**Why this gate is safe**: Step 4b's analytical edits (competitive dynamics, value chain, sector observations, comparison tables) are derived from research-note content. Without a research note driving the edit, there is no propagatable delta — the LLM running Step 4b would either rewrite the same text with cosmetic variation (analytical churn) or no-op. The skill-origin gate makes the no-op decision explicit and cheap rather than leaving it to LLM inference.

**Record in the Step 8 report**: under a new line `Sector skill-origin skips: [list of sector names]` when at least one skip fired. Omit when none.

### 4.0: Per-source idempotency check (NEW — runs before snapshot/edit)

Before snapshotting and editing a sector note, check whether this sector has already received propagation derived from the **same source insight** in this calendar day. This prevents double-propagation when a thesis appears in the changed-set because a prior `/sync TICKER` advanced its mtime — the prior run already propagated to this sector for the same research note, and re-propagating would either duplicate edits or trigger the analytical "no delta" branch wastefully.

Method (per source research note triggering the sector update):
1. **Read the sector note's `## Related Research` section.** Check if the source research note's wikilink (e.g., `[[Research/2026-04-19 - X - earnings]]`) is already present.
   - **Wikilink absent** → first-time propagation; proceed to Step 4a snapshot + 4b edit.
   - **Wikilink present** → ambiguous: was it added today by a prior run, or earlier from independent propagation? Continue to step 2.

2. **Read the sector note's `## Log` section** (if present — sector notes have Log sections per the Sector Note template). Scan for any `### YYYY-MM-DD` entry where `entry_date == today` AND the entry references the source research note's wikilink.
   - **Today-dated entry references this source** → sector already received propagation for this research note today (likely from a prior `/sync TICKER` in the same session). Skip both 4a snapshot and 4b edit. Log: `ℹ️ Skipped sector update [Sector Name] — Log already contains today's entry for [research-note] (likely propagated by earlier /sync TICKER in this session).`
   - **No today-dated entry references this source** → propagation may have happened on an earlier day; proceed normally to 4a snapshot + 4b edit. The deep-analysis step in 4b will determine if there's actual new delta beyond the prior wikilink addition.

3. **Atomicity-with-Step-3 note**: If a thesis change in Step 3 cascades into multiple sector notes (rare — usually 1 sector per thesis), apply this check independently per sector. Skipping one sector does not affect propagation to others.

> **Why strict calendar-day matching here too**: same rationale as Step 1 Check 3 per-thesis idempotency — Log entries are date-only and producer skills always write today's date. Compare `entry_date == today` as `YYYY-MM-DD` strings. Cross-midnight runs are accepted as "slight redundancy; never data loss."

> **Why Related Research presence alone isn't sufficient**: a research note may be added to `Related Research` listing without a corresponding analytical-section update (e.g., the user manually wikilinked it). The Log entry is the authoritative record that `/sync` (or another producer) actually propagated insight content. Checking both gates the edit on actual prior propagation, not just incidental wikilink presence.

### 4a: Pre-Edit Safety — Snapshot
If edits will modify existing analytical text (competitive dynamics, value chain, sector observations, comparison narratives) — not just adding links:
1. ```bash
   cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-sync YYYY-MM-DD-HHMMSS).md"
   ```
2. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Sectors/Sector Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: sync
   snapshot_batch: sync-YYYY-MM-DD-HHMMSS
   ```
   Reuse the batch ID generated in Step 3c.

### 4b: Apply Updates
- **Add new research notes** to the research listing
- **Update competitive dynamics** if research changes relative positioning
- **Update value chain analysis** if supply chain relationships shifted
- **Revise sector-level observations** if cross-company patterns emerged
- **Update company comparison tables** with new data points

Skip snapshot if only adding research note links.

### 4c: Post-Edit Verification

After completing all edits, re-read the modified note and verify each edited section:
1. Ends with a complete sentence (not mid-word, mid-sentence, or with unmatched `**` or `*`)
2. Does not contain incomplete table rows (lines starting with `|` but not ending with `|`)
3. Does not end with a conjunction, preposition, comma, or opening bracket

If any check fails: `⚠️ Sector note may contain a partial edit in [section]. Snapshot available: [[_Archive/Snapshots/...]]. Review manually or /rollback.`

## Step 5: Update Macro Notes

For each affected Macro note:

### 5.-1: Skill-origin gate (mirrors Step 4.-1 for macros)

Consult `skill_origin_theses` from Step 2.5 before Step 5.0. A macro note's "affected thesis set" is every changed thesis that wikilinks this macro note (via `_graph.md` Macro reverse index OR the body-grep fallback from Step 1 "For changed macro notes" logic — running in reverse here: for each thesis in the changed-file set, resolve outbound `[[Macro/...]]` wikilinks to identify which macro notes this thesis affects).

**Gate rule**: if EVERY thesis in this macro's affected set is in `skill_origin_theses` AND no research note in the changed-file set resolves to this macro (via body `[[Macro/...]]` wikilinks or `source_type: scenario` / macro-focused frontmatter), skip Step 5.0, 5a, 5b entirely. Log: `ℹ️ Skipped macro update [Macro Note] — all [N] affected thesis changes are skill-origin; no co-changed research note drives a macro-level delta.`

**Mixed set**: if at least one thesis in the affected set is research-driven OR any research note resolves to this macro, proceed to Step 5.0 per existing logic.

**Rationale**: Step 5b's analytical edits (scenario analysis, probability weightings, trading/allocation implications) are derived from research-note insight. A thesis whose only recent change is a `Status change: conviction` Log entry doesn't carry a macro-level delta — `/status` already captured the conviction change in the thesis frontmatter; the macro note's narrative doesn't need a rewrite to reflect it.

**Record in the Step 8 report**: under a new line `Macro skill-origin skips: [list of macro names]` when at least one skip fired. Omit when none.

### 5.0: Per-source idempotency check (mirrors Step 4.0 for sectors)

Before snapshotting and editing a macro note, check whether this macro note has already received propagation derived from the **same source insight** in this calendar day. Without this check, same-day double-`/sync` runs (e.g., `/sync TICKER` followed by default `/sync`) can compound analytical edits to macro probability weightings, value chain commentary, or trading-allocation paragraphs — producing duplicated text or contradictory updates layered on top of each other.

Method (per source research note triggering the macro update):

1. **Wikilink presence check** — scan the macro note body for the source research note's wikilink (e.g., `[[Research/2026-04-19 - X - earnings]]`).
   - **Wikilink absent** → first-time propagation; proceed to Step 5a snapshot + 5b edit.
   - **Wikilink present** → ambiguous; was it added today by a prior run, or earlier from independent propagation? Continue to step 2.

2. **Log section check** — if the macro note has a `## Log` section (not all macros do — they aren't required by template), scan for any `### YYYY-MM-DD` entry where `entry_date == today` AND the entry references the source research note's wikilink.
   - **Today-dated entry references this source** → macro already received propagation for this research note today (likely from a prior `/sync TICKER` in the same session). Skip both 5a snapshot and 5b edit. Log: `ℹ️ Skipped macro update [Macro Note] — Log already contains today's entry for [research-note] (likely propagated by earlier /sync in this session).`
   - **No today-dated entry references this source** → strong signal that today's propagation hasn't happened. **Skip step 3 entirely; proceed to 5a snapshot + 5b edit.** The Log section gives a stronger signal than mtime (which can be advanced by unrelated user edits), so if the Log says "not propagated today", trust it.
   - **Macro has no `## Log` section** (common — macros are narrative documents without strict template) → fall through to step 3 (mtime is the only available signal).

3. **Mtime fallback** (runs ONLY when step 2 reported "no `## Log` section"): check the macro note's mtime against `.last_sync`. If `mtime > .last_sync` AND the wikilink is present (Step 5.0 step 1 confirmed), this suggests prior propagation in the current `/sync` window (or earlier same-day session) — skip both snapshot and edit to avoid double-edit. Log: `ℹ️ Skipped macro update [Macro Note] — wikilink present and mtime > .last_sync (no Log section to confirm precise propagation date); likely propagated within current sync window. Forced re-propagation requires manual edit or /sync all.`

If all three checks pass without a skip signal (i.e., wikilink absent in step 1, OR step 2 found no today-date entry on a Log-equipped macro, OR step 3 mtime fallback didn't fire on a Log-less macro), proceed to 5a snapshot + 5b edit normally.

> **Step 3 false-positive risk**: the mtime fallback can mistakenly skip when the user manually edited the macro (advancing mtime) AND the source wikilink happens to already be present (added by a prior /sync). Trade-off: mtime is a coarse signal for Log-less macros, but the alternative (no idempotency check at all) leaves macros vulnerable to compounded analytical-text edits across same-day double-syncs. To force re-propagation on a Log-less macro that was incorrectly skipped, run `/sync all` (which uses two-pass triage rather than idempotency-skip) or manually edit the macro to remove the source wikilink before re-running /sync.

> **Why mtime-fallback for macros but not sectors**: sector notes are required by template to have `## Log` sections (per /lint sector template enforcement). Macro notes are narrative documents with variable structure — many have no Log section. The mtime fallback gives macros a same-day double-edit guard without requiring a Log section.

> **Atomicity-with-Step-3 note**: If a thesis change in Step 3 cascades into multiple macro notes (rare — usually 1-2 macros per thesis), apply this check independently per macro. Skipping one macro does not affect propagation to others.

### 5a: Pre-Edit Safety — Snapshot
If edits will modify existing analytical text (scenario analysis, probability weightings, trading/allocation implications) — not just adding wikilinks:
1. ```bash
   cp "Macro/Note Name.md" "_Archive/Snapshots/Note Name (pre-sync YYYY-MM-DD-HHMMSS).md"
   ```
2. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Macro/Note Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: sync
   snapshot_batch: sync-YYYY-MM-DD-HHMMSS
   ```
   Reuse the batch ID generated in Step 3c.

### 5b: Apply Updates
- **Assess macro-micro linkage**: Does the new micro-level research validate, weaken, or complicate the macro framework?
- **Update scenario analysis** if new data changes probability weightings
- **Add wikilinks** to the new research
- **Revise trading/allocation implications** if the macro thesis has shifted

Skip snapshot if only adding wikilinks.

## Step 6: Update _hot.md

Follow the contract at `.claude/skills/_shared/hot-md-contract.md` for all `_hot.md` writes — compression policy, per-section budgets, truncation-marker avoidance, and cap handling are defined there. `/sync` is the canonical owner of Latest Sync and Sync Archive sections.

If `_hot.md` does not exist (first run), create it with sections: `## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`. Use frontmatter: `date: YYYY-MM-DD`, `tags: [meta, hot-cache]`.

**Lifecycle rules:**
1. **Update the date** in frontmatter and heading
2. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write the new thread (current focus + next step), then append `*Previous:*` line(s) — max 5, drop oldest.
3. **Latest Sync**: Replace the existing Latest Sync section entirely with this sync's summary. One bullet per thesis updated, max 1 line each:
   ```
   - **[TICKER]**: [what changed] — [conviction impact]
   ```
4. **Sync Archive**: Compress the outgoing Latest Sync into a single summary line and prepend to `## Sync Archive`. Keep max 3 archived entries.
5. **Open Questions** — two-stage update:

   **5a. Mark resolved Outstanding Questions** (existing behavior): If any Outstanding Questions were resolved on theses during Step 3d, mark them resolved in `_hot.md`'s `## Open Questions`. If conviction triggers or drift were flagged in Step 3e, add the reassessment question.

   **5b. Auto-resolve `/catalyst` no-catalyst questions** (NEW): scan `_hot.md`'s `## Open Questions` section for entries matching the `/catalyst`-emitted pattern:
   ```
   - [[TICKER]]: what catalyst in next 90 days could reignite this thesis? (flagged by /catalyst YYYY-MM-DD)
   ```
   For each match, resolve the question if the linked thesis now has a forward catalyst. Method:
   1. Extract TICKER from the question's wikilink.
   2. Read `Theses/TICKER - *.md`'s `## Catalysts` section.
   3. Parse each catalyst entry for a date token (any of: explicit `YYYY-MM-DD`, calendar quarter like `Q3 2026`, month like `October 2026`, or "next [N] weeks/months").
   4. Resolve any parsed date to an absolute calendar date (use the start of the period for ranges/quarters/months — e.g., `Q3 2026` → `2026-07-01`, `October 2026` → `2026-10-01`).
   5. If ANY parsed catalyst date is `>= today`, the thesis now has a forward catalyst → remove (or mark resolved with strikethrough) the Open Question entry.
      - Removal format: simply delete the bullet line from `## Open Questions`.
      - Resolution format (alternative if user prefers audit trail): replace with `- ~~[[TICKER]]: what catalyst in next 90 days could reignite this thesis?~~ → Resolved YYYY-MM-DD: forward catalyst now exists ([catalyst summary]).`
   6. Use removal format by default; resolution format only if `_hot.md` already shows a pattern of `~~strikethrough~~ → Resolved` entries (preserves user's chosen audit style).

   **Skip safety**: if a thesis has only past-dated catalysts (all catalyst dates < today), the question stays — the no-catalyst flag is still valid. If `## Catalysts` section is missing or unparseable, skip auto-resolution for that ticker (log: `ℹ️ Cannot auto-resolve /catalyst question for [TICKER] — Catalysts section missing or unparseable. Manual review needed.`).

   **Why scoped to `/catalyst` pattern**: Other Open Question producers (`/surface`, `/scenario`, `/stress-test`, `/thesis`) generate freeform questions whose resolution criteria aren't programmatically detectable. Only the `/catalyst`-specific pattern has a clear, parseable resolution condition (forward catalyst exists). Generic accumulation pressure on `_hot.md` Open Questions remains for those — manual cleanup is required.

   **Report**: list auto-resolved tickers in Step 8 under a new field `/catalyst Open Questions auto-resolved: [TICKER1, TICKER2, ...]` or omit if none.
6. **Recent Conviction Changes**: If conviction triggers hit (Step 3e ⚡) or drift was flagged (Step 3e ⚠️/📈), add an entry noting the flag.
7. **Cap enforcement**: After writing, check total word count and follow `.claude/skills/_shared/hot-md-contract.md` §"Compression trigger order": drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → emit warning. Soft cap 4,000 words, hard cap 5,000 words (abort `_hot.md` write on hard-cap breach; primary `/sync` operation still succeeds).

## Step 7: Touch Watermark and (for /sync all) Write Graph-Rebuild Marker

**Mandatory. Runs after ALL content writes (Steps 3–6) are complete, before Step 7.5 manifest write and Step 8 reporting.**

### Mode-conditional watermark behavior

- **`/sync` (default) and `/sync all`**: touch `.last_sync` at the end of the run.
  ```bash
  touch .last_sync
  ```
  This is the last mutation. If any prior step fails or the session is interrupted, the watermark remains unset and the next `/sync` will re-process the same changes — safe by default.

- **`/sync TICKER`**: **do NOT touch `.last_sync`**. Ticker-scoped mode is timestamp-independent and only inspects one thesis's adjacency — advancing the watermark would silently exclude unrelated changes (other theses, sectors, macros) from the next default sync's `find -newer .last_sync` set. Report `Watermark: untouched (ticker-scoped mode preserves baseline for next default /sync)` in Step 8.
  - **First-run exception**: if `.last_sync` does not exist when `/sync TICKER` runs, create the epoch placeholder so the next default `/sync` has a baseline:
    ```bash
    touch -t 197001010000 .last_sync
    ```
    Report `Watermark: epoch placeholder created (was absent — first-run state preserved)` in Step 8.

### Graph-rebuild marker (`/sync all` only)

**Skip for `/sync` (default) and `/sync TICKER`** — those modes touch a bounded subset of files, and `/graph last`'s incremental path handles their changes correctly via mtime watermark.

**For `/sync all` only**: `/sync all`'s two-pass triage intentionally skips "No delta" theses — their mtimes are not advanced, so their adjacency entries never enter `/graph last`'s changed-thesis bucket. If the user deviates from the documented monthly-maintenance chain (which is `/sync all` → `/graph` full) and runs `/graph last` instead, the graph keeps baseline adjacency for every skipped thesis, masking drift. Signal the deviation explicitly:

```bash
touch .sync_all_fresh
```

`/graph` reads this marker at Watermark Resolution and forces a full rebuild (Steps 1–8) regardless of mode, then deletes the marker after a successful write. If the user does follow the recommended chain (`/graph` full), the full rebuild path also deletes the marker naturally.

**Why a marker file (not poisoning `_graph.md date:`)**: `/sync` must not write `_graph.md` — the metadata-cull architecture concentrates graph ownership in `/graph`. A vault-root marker file keeps `/sync` content-only while giving `/graph` an unambiguous signal. The marker is cheap (zero-byte file), ignorable by every other skill, and self-cleaning on the next `/graph` run.

## Step 2.9: Write Sync Batch Manifest — Skeleton (T2.1 fix — two-phase write)

**Mandatory BEFORE any thesis/sector/macro Tier A snapshot or Tier B Log append lands.** Runs once per non-no-op sync run after Step 1/2/2.5 complete their read-only analysis, immediately before Step 3 begins modifying files.

The skeleton manifest is the first mutation of the run. If the skeleton write fails, **hard-abort the whole sync** — do NOT proceed to Tier A snapshots or Tier B appends. This ensures the manifest is always a complete record of any work that landed.

### 2.9a: Generate batch ID and skeleton path

Generate `HHMMSS` once at the start of Step 2.9 via `date +%H%M%S`. This is THE canonical batch ID for the rest of the run — Step 3c reuses it for all Tier A snapshots, Step 7.5 reuses it for the manifest status flip.

**Batch ID format (C4 fix)**:
- **`/sync` (default) and `/sync all`** (vault-wide lock prevents same-second collisions): `sync-YYYY-MM-DD-HHMMSS`
- **`/sync TICKER`** (ticker-scoped; concurrent ticker-scoped runs on different tickers possible): `sync-TICKER-YYYY-MM-DD-HHMMSS` — ticker qualifier prevents collisions between simultaneous `/sync NVDA` and `/sync AMAT`

Skeleton manifest path matches the format chosen above:
```
_Archive/Snapshots/_sync-manifest (sync-YYYY-MM-DD-HHMMSS).md       # default / all
_Archive/Snapshots/_sync-manifest (sync-TICKER-YYYY-MM-DD-HHMMSS).md # ticker-scoped
```

### 2.9b: Write skeleton

Frontmatter:
```yaml
---
type: sync-manifest
batch: sync-YYYY-MM-DD-HHMMSS
mode: default | all | ticker-scoped
status: in-progress
date: YYYY-MM-DD
---

# Sync Batch Manifest (in-progress)

Manifest written at Step 2.9 before any file modifications. Will be populated
with Tier A/B/research-note details as work progresses, then flipped to
`status: completed` at Step 7.5.

If this file persists with `status: in-progress`, the sync crashed or was
interrupted mid-run. Recovery: inspect the manifest's partial accumulator
sections below, then run /rollback to restore any Tier A snapshots listed.

## Theses with snapshots taken (Tier A)
_populated during Step 3c_

## Theses with Log-only appends (Tier B)
_populated during Step 3f and cross-thesis steps_

## Sector notes touched
_populated during Step 4_

## Macro notes touched
_populated during Step 5_

## Source research notes processed
_populated as Step 3 iterates_
```

### 2.9c: Skeleton write failure — hard abort

If the skeleton write fails (disk full, permission, concurrent filesystem issue), abort:

```
❌ Sync manifest skeleton write failed: [path]
   Reason: [error]
   
No vault state has been modified yet. This abort is pre-mutation —
no Tier A snapshots exist, no Tier B Log entries written, no sector or
macro edits applied.

Fix the underlying filesystem issue (disk space, permissions, concurrent
writer) and re-run /sync. Resume state is clean.
```

Exit the skill. Do NOT proceed to Step 3.

### 2.9d: Append-as-you-go (during Steps 3–6)

Each Step 3c snapshot, 3f Log append, 4a sector snapshot, 5a macro snapshot, etc. appends its record to the corresponding section of the manifest in real time (via `Edit` tool). This keeps the manifest current — if the session crashes after Step 3f on thesis #5 but before Step 3f on thesis #6, the manifest already reflects #1-5 for cascade recovery.

Accumulators maintained in-memory per existing Step 7.5d are now written to the manifest INCREMENTALLY rather than in one batch at Step 7.5.

## Step 7.5: Finalize Sync Batch Manifest — Flip to completed (T2.1 fix continuation)

**Mandatory for every `/sync` mode (default, all, TICKER) when Step 2.9 skeleton was written.** Skip only when the run was a pure no-op (Step 1 reported "Nothing changed since last sync") — Step 2.9 also skips in that case.

### Why this manifest exists

`/sync` Step 3c snapshots theses for Tier A edits (rewriting Bull Case, Non-consensus Insights, etc.) but explicitly **does NOT snapshot** for Tier B edits (Log-only appends, Related Research wikilink additions, Key Metrics number updates). Cross-thesis propagation — where a research note triggers a Log entry on TICKER's thesis AND on TICKER's cross-thesis neighbors — produces Tier B appends on neighbors WITHOUT snapshots.

If the user later runs `/rollback TICKER` to undo the sync, the cascade detection finds TICKER's pre-sync snapshot but **cannot find snapshots for the neighbors**. The neighbor Log entries persist after rollback as orphan audit-trail entries citing a research note whose effect on TICKER has been reverted. This is a permanent audit gap that violates Tier 2 append-only semantics if removed manually, and silently corrupts the Log audit trail if left in place.

The sync manifest closes this gap by recording **every thesis touched** in the sync run — including Tier B Log appends without snapshots. `/rollback` Step 2.5 reads the manifest during cascade detection and surfaces the unrecoverable Log entries to the user with their full text, so the user can decide per-entry whether to manually strikethrough/annotate them post-rollback.

### T2.1 change: status flip, not create-and-write

Step 2.9 already wrote the skeleton and Steps 3–6 incrementally appended accumulator entries. Step 7.5 now only:
1. Flips `status: in-progress` → `status: completed`.
2. Adds `completed_date: YYYY-MM-DD`.
3. Verifies the flip landed.

If the flip fails (Edit error), the manifest persists as `status: in-progress`. `/lint #41` (extended) now catches this as Important (same severity as `/prune` #36 in-progress manifests).

### 7.5a: Manifest path (already written in Step 2.9b)

Batch ID and path are already known from Step 2.9a. Re-reference:
```
_Archive/Snapshots/_sync-manifest (sync-YYYY-MM-DD-HHMMSS).md
```

### 7.5b: Flip status frontmatter

Edit the manifest's frontmatter:
- Change `status: in-progress` → `status: completed`
- Add `completed_date: YYYY-MM-DD`

Expected frontmatter state after flip:
```yaml
---
type: sync-manifest
batch: sync-YYYY-MM-DD-HHMMSS
mode: default | all | ticker-scoped
status: completed
date: YYYY-MM-DD
completed_date: YYYY-MM-DD
---
```

Body — populate from tracking accumulators maintained throughout Steps 3–5:

```markdown
# Sync Batch Manifest

> Sidecar manifest listing every file touched by this `/sync` run. Used by `/rollback` Step 2.5 cascade detection to surface Tier B Log appends that weren't snapshotted (cross-thesis neighbors, Related Research additions, Key Metrics updates). Without this manifest, those edits would be invisible to `/rollback` and persist as orphan audit-trail entries after a cascade rollback.

## Theses with snapshots taken (Tier A — recoverable via `/rollback` cascade)
- `Theses/TICKER1 - Name.md` — snapshot: `[[_Archive/Snapshots/TICKER1 - Name (pre-sync YYYY-MM-DD-HHMMSS)]]`
- ... (one per Tier A thesis snapshot)

## Theses with Log-only appends (Tier B — NO snapshot, NOT recoverable via `/rollback` content restore)

For each thesis that received a Log entry but no snapshot in this run, capture the **full Log entry text** so `/rollback` Step 2.5 can present it for manual review:

- `Theses/TICKER2 - Name.md`
  - Log entry appended:
    ```
    ### YYYY-MM-DD
    - [[Research/2026-04-19 - source]]: [what changed] — conviction [impact]
    ```
  - Reason for Tier B classification: cross-thesis propagation from [[Research/...]] (TICKER2 wikilinked from another thesis touched in this run) | augmented target via wikilink/tag/ticker resolution | other
- ... (one per Tier B thesis append)

## Sector notes touched
- `Sectors/Name.md` — snapshot: `[[_Archive/Snapshots/...]]` (Tier A) | no snapshot (link addition only — Tier B)

## Macro notes touched
- `Macro/Name.md` — snapshot: `[[_Archive/Snapshots/...]]` (Tier A) | no snapshot (link addition only — Tier B)

## Source research notes processed
- `[[Research/source-1]]`
- `[[Research/source-2]]`
- ... (every research note that triggered propagation in this run)

## Recovery guidance

- For Tier A entries: `/rollback [any ticker from the manifest]` → select `(pre-sync YYYY-MM-DD-HHMMSS)` snapshot → cascade (a) restores all Tier A files atomically. Tier B Log entries above will be surfaced for manual review.
- For Tier B entries: no automatic restore. After cascade rollback, manually inspect each listed Log entry. Options per entry: (1) leave as historical audit trail (preferred — Tier 2 append-only), (2) strikethrough with `~~entry~~ → Reverted YYYY-MM-DD: rolled back via /rollback batch sync-YYYY-MM-DD-HHMMSS` (preserves audit while signaling reversal), (3) manually delete (violates Tier 2 — only acceptable if the entry was clearly erroneous).
```

### 7.5c: Verify flip landed

Re-read the manifest frontmatter after the Edit. Confirm:
- `status: completed` present
- `status: in-progress` absent
- `completed_date:` present and equals today

**On verification success**: proceed to Step 8 reporting normally. Manifest is now a complete record of the run.

**On verification failure** (flip Edit silently missed — frontmatter format drift, concurrent modification): do NOT retry aggressively. Report `⚠️ Sync manifest status flip failed — manifest at [path] remains status: in-progress despite successful sync completion. /lint #41 will flag this as Important until manually resolved. Manual fix: open the manifest and replace status: in-progress with status: completed (add completed_date: today).` Continue to Step 8 — the sync itself succeeded; only the completion marker failed.

### 7.5d: Lifecycle (unchanged from prior spec except two-phase-write context)

The manifest is a **non-snapshot artifact** (frontmatter `type: sync-manifest`, no `snapshot_date:`):
- `/clean` Step 2a's non-snapshot artifact guard skips it for snapshot-age-based cleanup.
- `/lint #41` (extended by T2.1) distinguishes three states: `status: in-progress` → Important (crash or flip failure), `status: completed` → ages per existing 90/180 day tiers, missing altogether → no op.
- The manifest persists indefinitely until manually deleted OR until `/lint #41` ages it out and the user chooses to clean.

**T2.1 change summary**: prior behavior wrote the manifest at END of run with a "log failure but continue" clause that silently violated the cascade-recovery contract if the end-write failed. New two-phase behavior:
- Step 2.9 writes skeleton BEFORE any mutations — skeleton write failure hard-aborts the sync pre-mutation, preventing any silent audit gap.
- Steps 3–6 incrementally populate the manifest as work lands — crash recovery finds partial-but-consistent state.
- Step 7.5 flips status at end; flip failure is visible via `/lint #41` rather than silent.

### 7.5d: Tracking accumulators (implementation note for the LLM running this skill)

Throughout Steps 3–5, maintain in-memory accumulators that Step 7.5 will write to the manifest:

| Accumulator | Populated when |
|---|---|
| `tier_a_thesis_snapshots: [(path, snapshot_path)]` | Step 3c creates a thesis snapshot |
| `tier_b_thesis_log_appends: [(path, log_entry_text, reason)]` | Step 3f appends a Log entry without a Step 3c snapshot (cross-thesis neighbor; augmented target; etc.) |
| `tier_a_sector_snapshots: [(path, snapshot_path)]` | Step 4a creates a sector snapshot |
| `tier_b_sector_appends: [(path)]` | Step 4b adds a wikilink to a sector note without a Step 4a snapshot |
| `tier_a_macro_snapshots: [(path, snapshot_path)]` | Step 5a creates a macro snapshot |
| `tier_b_macro_appends: [(path)]` | Step 5b adds a wikilink to a macro note without a Step 5a snapshot |
| `source_research_notes: [path]` | Step 1 identifies a changed research note that triggered propagation |

If the run completes with all accumulators empty (pure no-op), skip Step 7.5 entirely.

## Step 8: Report

- **Mode**: default | all | ticker-scoped
- **Files read**: [count]
- **Files updated**: [count]
- **Snapshots created**: [list with paths, or "none"]
- **Thesis updates** (one per thesis):
  - [TICKER]: [sections modified] — [conviction impact]. Snapshot: `[[_Archive/Snapshots/...]]` or N/A
- **Sector Note updates**: [list with one-line summary each]
- **Macro note updates**: [list with one-line summary each]
- **Deduplication skips** (thesis-level, Step 1 Check 3): [list any tickers where propagation was skipped because Log already contained today's entry for the research note. If none, omit this line.]
- **Sector skill-origin skips** (Step 4.-1): [list sector notes where ALL affected thesis changes were skill-origin (no research-driven thesis and no research note resolves to this sector) and Step 4.-1 skipped Step 4 entirely. If none, omit this line.]
- **Macro skill-origin skips** (Step 5.-1): [list macro notes where ALL affected thesis changes were skill-origin and Step 5.-1 skipped Step 5. If none, omit this line.]
- **Log-history backfill skips** (Step 1 Check 2 Case 2a): [list (TICKER, research-note) pairs where the scan found a prior Log entry referencing the research note and suppressed the retry. If none, omit this line.]
- **Sector idempotency skips** (Step 4.0): [list any sector notes where propagation was skipped because Log already contained today's entry for the source research note. If none, omit this line.]
- **`propagated_to:` skips**: [list tickers skipped because the producer skill already marked them propagated via `propagated_to:` frontmatter (Case 2b). If none, omit this line.]
- **Terminal-skip notes**: [list research notes where ALL targets were skipped because the note had explicit `propagated_to: []` (Case 2c — surface scans, briefs, etc.). If none, omit this line.]
- **Augmented targets**: [list tickers NOT in a research note's `propagated_to:` but resolved via wikilink/tag/ticker frontmatter — these are the minor-impact or cross-referenced theses that a producer skill intentionally excluded but that `/sync` correctly picks up. If none, omit this line.]
- **`propagated_to:` updates**: [list research notes whose `propagated_to:` frontmatter was extended with newly propagated tickers. If none, omit this line.]
- **Closed-status skips**: [list TICKERs skipped because status: closed + file still in Theses/. If none, omit this line.]
- **Missing-file skips**: [list any thesis filenames found in graph but not on disk. If none, omit this line.]
- **Unresolved research notes**: [list any research notes where no propagation target was found. If none, omit this line.]
- **Conviction triggers hit**: [list any]
- **Conviction drift flags raised**: [list any]
- **`/catalyst` Open Questions auto-resolved** (Step 6 #5b): [list TICKERs whose no-catalyst question was removed because the thesis now has a forward catalyst. If none, omit this line.]
- **New connections discovered**: [any surprising links worth noting]
- **Watermark**: `touched (default/all)` | `untouched (ticker-scoped mode preserves baseline for next default /sync)` | `epoch placeholder created (was absent — first-run state preserved)`

**Final reminder**: `→ Run /graph last to update the dependency map. Recommended after every /sync.`

## Step 9: Release lock

After Step 8's Report is complete, release the vault lock per `.claude/skills/_shared/preflight.md` §1.7 as the skill's FINAL Bash block. Runs unconditionally — whether `/sync` succeeded, raised advisories, or hit a non-fatal error (e.g., sector resolution `none` for a thesis). If the skill aborts before reaching this step (hard abort on missing Log section, mid-chain crash, user Ctrl-C), the lock persists and appears stale on the next collision / `/lint #43` run; manual `rm .vault-lock*` is the recovery path.

```bash
# Lock release — verify ownership before rm (preflight §1.5) to avoid stealing
# another skill's lock if this skill somehow lost ownership mid-run.
# LOCK_FILE path depends on mode:
#   default or /sync all → .vault-lock
#   /sync TICKER         → .vault-lock.TICKER
LOCK_FILE="<paste-from-Step-0.1>"                # e.g., .vault-lock or .vault-lock.NVDA
EXPECTED_TOKEN="<paste-token-captured-from-Step-0.1>"
if [ -f "$LOCK_FILE" ] && grep -q "token: $EXPECTED_TOKEN" "$LOCK_FILE"; then
  rm -f "$LOCK_FILE" && echo "=== LOCK RELEASED ($LOCK_FILE) ==="
else
  echo "⚠️ Lock ownership check failed at release ($LOCK_FILE) — skipping rm to avoid stealing another skill's lock."
fi
```
