---
name: sync
description: Synchronize recent research learnings across all affected theses, sector notes, and macro documents. Use after a research session or when user says "sync", "propagate", or "update everything".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * find * cp * mkdir * touch *)
---

**Follow CLAUDE.md Writing Standards strictly in all output.** No hedge words, no restating known context, no connective tissue. Every line must contain a data point, an insight, or a specific claim.

Propagate recent research insights across all affected vault documents. **This is a deep analytical operation — for each affected note, think through the full implications of new research on every substantive section, not just append links.**

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

   **Case 2a — Field absent** (`propagated_to:` not in frontmatter): no producer-side dedup info. Treat the entire Step 1 target set as needing propagation. Proceed to Check 3 for every ticker.

   **Case 2b — Field present and non-empty** (e.g., `propagated_to: [TICKER1, TICKER2]`, set by `/stress-test`, `/scenario`, `/compare`, `/deepen`): treat each listed ticker as "already propagated by the producer skill" — **skip them for this run**. These tickers received Log entries directly from the producer; re-propagating would produce near-duplicate entries. Log: `ℹ️ Skipped [TICKER] — producer skill already propagated (in propagated_to).`
     - **Exception — augmented targets**: Tickers in the Step 1 target set that are NOT in `propagated_to:` are new additions via wikilink/tag/ticker resolution. Log: `➕ Augmented propagation: [TICKER] — not in propagated_to but resolved via [wikilink | tag | ticker frontmatter].` Proceed to Check 3 for these tickers.

   **Case 2c — Field present and empty** (`propagated_to: []`, set by `/surface`, `/brief`, or any future producer that emits exploratory/derivative notes): this is a **terminal dedup signal** — the producer explicitly declares "no thesis propagation needed for this note." Skip ALL targets resolved in Step 1 regardless of how they were resolved (graph adjacency, wikilink, ticker frontmatter, tag). Do NOT proceed to Check 3 for any ticker. Log once: `ℹ️ Skipped all propagation for [research-note] — empty propagated_to: signals producer-side terminal decision (e.g., surface scan, brief). No Log entries written, no augmented targets evaluated.`
     - **Why empty-list is terminal, not "nothing yet propagated"**: a producer that wanted "propagate to all wikilink-resolved targets but I haven't done any myself" would simply omit the field (Case 2a). Setting `propagated_to: []` explicitly is a deliberate "this note's body wikilinks are contextual references, not propagation targets" signal. Required for `/surface` (whose scan notes wikilink 10+ theses for context) and `/brief` (derivative summary of an already-existing thesis). Without this case, `/sync` would Log-spam every wikilink-referenced thesis on every surface/brief.
     - **Skill compliance**: producers must set `propagated_to: []` explicitly in frontmatter at note-creation time. `/surface` and `/brief` do so per their respective Phase 4 / Phase 4 specs. Future producers emitting exploratory notes must follow the same pattern.

3. **Per-thesis idempotency check** (applies to every remaining ticker after Check 2): For each target thesis, scan its `## Log` section for any `### YYYY-MM-DD` entry **whose date equals today's date** that references this research note's wikilink. Match rule is strict calendar-day: compare `entry_date == today` as `YYYY-MM-DD` strings. If found, skip: `ℹ️ Skipped duplicate propagation for [TICKER] — Log already contains today's entry for [research-note].`

> **Strict calendar-day rule (authoritative)**: Log entries are date-only (`### YYYY-MM-DD`) — they do not carry wall-clock time. The idempotency check compares today's date against the Log entry's date with exact string equality. A "rolling 24-hour window" interpretation (e.g., entry dated `2026-04-18` at 23:58 counted as "within 24h" of `2026-04-19` at 00:02) is **explicitly rejected** because (a) it cannot be computed from date-only entries without parasitic mtime reads that couple correctness to filesystem metadata outside this skill's control, and (b) producer skills always write today's calendar date, making `entry_date == today` the dimensionally matched check.
>
> **Cross-midnight edge case**: if `/scenario` wrote `### 2026-04-18` at 23:58 and `/sync` runs at 00:02 on 2026-04-19, today = `2026-04-19`, the Log has only `### 2026-04-18`, so the check misses → propagate normally → a new `### 2026-04-19` entry is added. This is the correct audit outcome: the research was still relevant the next calendar day. Slight redundancy; never data loss.

This idempotency check catches the case where a producer skill wrote Log entries and a subsequent `/sync` finds the same research note via timestamp detection. The window is intentionally simple — no 4-bucket classification, no rolling-time arithmetic, no partial-repair branches. If no today-dated entry references this research note, propagate normally.

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

**File-direct fallback** (used when `_graph.md` is missing, stale, or doesn't list the changed file):

For changed research notes not found in the graph:
1. Check the research note's `ticker:` frontmatter — if it matches a `Theses/[TICKER] - *.md` file, include that thesis.
2. Check outbound `[[Theses/...]]` wikilinks in the research note body — include each linked thesis.
3. Check `tags:` for ticker tokens (all-uppercase, 1-5 chars) matching `Theses/[TICKER] - *.md` filenames.
4. If the graph exists, check outbound `[[Macro/...]]` wikilinks against the Macro reverse index.

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
   - **High delta**: Directly referenced by a changed research note, shares sector with changed content, has cross-thesis links to changed theses, or its own Log shows recent conviction/status changes → read the **full thesis note**.
   - **Low delta**: Same macro exposure or adjacent sector to changed content, but no direct reference → read **Summary + Non-consensus Insights + Outstanding Questions + Bull/Bear Case** sections only (skip Business Model, Industry Context, Key Metrics).
   - **No delta**: No plausible propagation path from any changed content → do NOT read further.
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

  **Conditionally exclude entries that begin with `"Deepened"` or `"↳ CORRECTION: Deepened"`** within 7 calendar days of a `"Stress test"` entry for the same ticker (registry §3–§4) — gap-filling research chained to a stress test, not independent evidence.

  **Anchor handling**: If a `"Conviction reaffirmed"` (registry §5) or `"Status change: conviction"` (registry §6) entry is found, anchor the window there — only count entries AFTER the anchor. If fewer than 3 entries exist after the anchor, drift detection has insufficient data and does not fire. If no anchor exists, use the last 5 **non-excluded** entries as the window (i.e., count backward through the Log skipping exclusions until 5 eligible entries accumulate, or until Log exhaustion).
  - conviction: high but 3+ entries in window weakening → `⚠️ Conviction drift — [N]/[window size] recent updates flagged headwinds. Reassess. To acknowledge after review: /status TICKER reaffirm [rationale]`
  - conviction: low but 3+ entries in window strengthening → `📈 Positive drift — [N]/[window size] recent updates supportive. Reassess. To acknowledge after review: /status TICKER reaffirm [rationale]`

### 3f: Log Entry (last)

Append to Log section:
```
### YYYY-MM-DD
- [[Research/source-note]]: [what changed] — [conviction impact: unchanged/strengthened/weakened + 1 reason]
```
Max 2 lines. The log is an audit trail — the analysis lives in the updated sections above.

## Step 4: Update Sector Notes

For each affected Sector Note:

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
7. **Hard cap**: After writing, check total word count. If `_hot.md` exceeds 2,000 words, prune Sync Archive entries (oldest first) until under the cap.

## Step 7: Touch Watermark and (for /sync all) Write Graph-Rebuild Marker

**Mandatory. Runs after ALL writes are complete, immediately before reporting.**

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
