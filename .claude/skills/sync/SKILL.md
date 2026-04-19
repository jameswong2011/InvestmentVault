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

Change detection uses `.last_sync` as the timestamp watermark. Touched at the end of every sync (Step 7), so `find -newer .last_sync` captures exactly the files changed since the last run.

If `.last_sync` does not exist (first run), create it with an epoch timestamp and treat all files as changed:
```bash
touch -t 197001010000 .last_sync
```

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

For each changed research note, check whether any target thesis already has a Log entry referencing this note. Two checks:

1. **`propagated_to:` frontmatter check**: If the research note has `propagated_to: [TICKER1, TICKER2, ...]` (set by `/stress-test`, `/scenario`, `/compare`, `/deepen`), use this as the initial target list.
2. **Per-thesis idempotency check**: For each target thesis, scan its `## Log` section for any `### YYYY-MM-DD` entry within the last 24 hours that references this research note's wikilink. If found, the note has already been propagated to this thesis — skip it for this thesis. Log: `ℹ️ Skipped duplicate propagation for [TICKER] — Log already contains today's entry for [research-note].`

This 24-hour idempotency window catches the case where a producer skill (e.g., `/scenario`) already wrote Log entries to its target theses, and a subsequent `/sync` finds the same research note via timestamp detection. The window is intentionally simple — no 4-bucket classification, no partial-repair branches. If the Log entry is missing, propagate normally.

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
   cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-sync YYYY-MM-DD-HHMM).md"
   ```
2. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Theses/TICKER - Company Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: sync
   snapshot_batch: sync-YYYY-MM-DD-HHMM
   ```
   > **Batch ID**: Generate `HHMM` once at the start of the snapshot phase. Reuse the same `snapshot_batch` value across ALL snapshots (thesis, sector, macro) created in this sync run for `/rollback` cascade detection.

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

  Scan Log entries backward from most recent, **excluding entries that begin with "Stress test"** (periodic adversarial reviews, not deterioration evidence). **Also exclude entries that begin with "Deepened" or "↳ CORRECTION: Deepened"** within 7 calendar days of a "Stress test" entry for the same ticker (gap-filling research, not independent evidence). If a "Conviction reaffirmed" or "Status change: conviction" entry is found, anchor the window there — only count entries AFTER the anchor. If fewer than 3 entries exist after the anchor, drift detection has insufficient data and does not fire. If no anchor exists, use the last 5 entries as the window.
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

### 4a: Pre-Edit Safety — Snapshot
If edits will modify existing analytical text (competitive dynamics, value chain, sector observations, comparison narratives) — not just adding links:
1. ```bash
   cp "Sectors/Sector Name.md" "_Archive/Snapshots/Sector Name (pre-sync YYYY-MM-DD-HHMM).md"
   ```
2. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Sectors/Sector Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: sync
   snapshot_batch: sync-YYYY-MM-DD-HHMM
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
   cp "Macro/Note Name.md" "_Archive/Snapshots/Note Name (pre-sync YYYY-MM-DD-HHMM).md"
   ```
2. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Macro/Note Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: sync
   snapshot_batch: sync-YYYY-MM-DD-HHMM
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
5. **Open Questions**: If any Outstanding Questions were resolved on theses (Step 3d), mark them resolved. If conviction triggers or drift were flagged (Step 3e), add the reassessment question.
6. **Recent Conviction Changes**: If conviction triggers hit (Step 3e ⚡) or drift was flagged (Step 3e ⚠️/📈), add an entry noting the flag.
7. **Hard cap**: After writing, check total word count. If `_hot.md` exceeds 2,000 words, prune Sync Archive entries (oldest first) until under the cap.

## Step 7: Touch Watermark

**Mandatory. Runs after ALL writes are complete, immediately before reporting.**

```bash
touch .last_sync
```

This is the last mutation. If any prior step fails or the session is interrupted, the watermark remains unset and the next `/sync` will re-process the same changes — safe by default.

## Step 8: Report

- **Mode**: default | all | ticker-scoped
- **Files read**: [count]
- **Files updated**: [count]
- **Snapshots created**: [list with paths, or "none"]
- **Thesis updates** (one per thesis):
  - [TICKER]: [sections modified] — [conviction impact]. Snapshot: `[[_Archive/Snapshots/...]]` or N/A
- **Sector Note updates**: [list with one-line summary each]
- **Macro note updates**: [list with one-line summary each]
- **Deduplication skips**: [list any tickers where propagation was skipped because Log already contained today's entry for the research note. If none, omit this line.]
- **Closed-status skips**: [list TICKERs skipped because status: closed + file still in Theses/. If none, omit this line.]
- **Missing-file skips**: [list any thesis filenames found in graph but not on disk. If none, omit this line.]
- **Unresolved research notes**: [list any research notes where no propagation target was found. If none, omit this line.]
- **Conviction triggers hit**: [list any]
- **Conviction drift flags raised**: [list any]
- **New connections discovered**: [any surprising links worth noting]

**Final reminder**: `→ Run /graph last to update the dependency map. Recommended after every /sync.`
