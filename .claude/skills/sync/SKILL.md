---
name: sync
description: Synchronize recent research learnings across all affected theses, sector notes, and macro documents. Use after a research session or when user says "sync", "propagate", or "update everything".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write Bash(date * find * cp * mkdir * touch *)
---

**Follow CLAUDE.md Writing Standards strictly in all output.** No hedge words, no restating known context, no connective tissue. Every line must contain a data point, an insight, or a specific claim.

Propagate recent research insights across all affected vault documents. **This is a deep analytical operation — for each affected note, think through the full implications of new research on every substantive section, not just append links.**

## Sync Modes

This skill supports three modes based on `$ARGUMENTS`:

- **`/sync`** (default) — **Graph-assisted targeted sync.** Uses `_graph.md` to resolve dependencies without brute-force file traversal. Reads only the files that need updating. Performs incremental `_graph.md` update after propagation. Use for routine post-ingest propagation.
- **`/sync all`** — **Full brute-force sync.** Reads all theses, all sector notes, all macro notes regardless of graph. Content propagation only — does NOT update `_graph.md` (run `/graph` afterward to rebuild). Use after major research sessions or monthly maintenance.
- **`/sync TICKER`** — **Ticker-scoped sync.** Uses `_graph.md` to resolve the ticker's full adjacency set (thesis, sector notes, macro notes, cross-thesis references, linked research). Reads all resolved files and propagates regardless of timestamps. Performs incremental `_graph.md` update. Use after manually editing a thesis or for targeted propagation to a specific area.

Parse `$ARGUMENTS` for mode: if "all", run all mode. If a ticker (matches a `Theses/` filename prefix), run ticker-scoped mode. Otherwise, run default graph-assisted mode.

## Watermark

Change detection uses `.last_sync` (not `_graph.md`) as the timestamp watermark. This decouples the dependency graph from sync timing — accidental edits to `_graph.md` or standalone `/graph` runs cannot cause `/sync` to miss changes.

- `.last_sync` is touched at the end of every sync (Step 7.5 — after all writes including graph update)
- `/graph` never touches `.last_sync`
- `_graph.md` is purely a dependency map — its mtime has no operational meaning for `/sync`

---

## Step 0: Read and Validate Dependency Graph (default mode only)

Read `_graph.md` to load the pre-computed dependency map. This eliminates the need to read 30-50 files just to discover which files are connected.

The graph provides:
- **Thesis Adjacency Index**: For each thesis — its sector notes, macro notes, research notes, and cross-thesis references
- **Reverse Index: Macro → Theses**: Which theses are exposed to each macro note
- **Reverse Index: Sector → Theses**: Which theses are in each sector
- **Cross-Thesis Clusters**: Bidirectional propagation paths (highest priority)

**After reading, validate the graph before trusting it:**
1. YAML frontmatter parses without error (all expected fields present: `date`, `theses`, `sectors`, `macro`, `research`, `edges`)
2. `## Thesis Adjacency Index` section heading exists
3. `## Reverse Index: Macro → Theses` and `## Reverse Index: Sector → Theses` headings exist
4. Every `### TICKER - Name` entry in the adjacency index has at least a `sector:` field
5. All wikilinks have valid `[[...]]` syntax (no unclosed brackets)
6. Frontmatter counts (`theses:`, `sectors:`, `macro:`) are within ±2 of actual file counts in those directories

**Fallback triggers:**
- `_graph.md` does not exist → fall back to all-mode. Warn: `⚠️ Graph missing — running all-mode. Run /graph afterward to rebuild.` Record `fallback_reason: missing` for Step 8.
- `date:` is >30 days old → fall back to all-mode. Warn: `⚠️ Graph stale ([N] days old) — running all-mode. Run /graph afterward to rebuild.` Record `fallback_reason: stale-[N]-days` for Step 8. **Note**: date `1970-01-01` is the canonical all-mode-poisoned value left by a prior `/sync all` — detect this specifically and record `fallback_reason: poisoned-by-prior-sync-all` for targeted Step 8 messaging (see rule below).
- Validation checks 1-3 fail → fall back to all-mode. Warn: `⚠️ Graph structurally corrupt — [specific failure]. Running all-mode. Run /graph to rebuild.` Record `fallback_reason: corrupt-[failure-code]` for Step 8.
- Validation checks 4-6 fail → proceed with graph-assisted mode but warn: `⚠️ Graph has minor issues — [specific failure]. Sync will proceed but run /graph soon to repair.`

**Persist fallback_reason**: whatever fallback code is recorded here is passed forward to Step 8 so the user sees a prominent reminder at the end of the run, not only the inline Step 0 warning that scrolls past during a long sync.

## Step 1: Identify Changes

- If `$ARGUMENTS` specifies files, use those as the source
- Otherwise, use timestamp-based detection to find all files modified since the last sync:
  ```bash
  find Research/ Theses/ Macro/ Sectors/ -newer .last_sync -name '*.md'
  ```
  `.last_sync` is the watermark — touched at the end of every sync, so `-newer .last_sync` captures exactly the files changed since the last run. If `.last_sync` does not exist (first run), create it with an epoch timestamp so all files appear changed, then fall back to all mode. Warn: `⚠️ No .last_sync found — first run. Reading all files.`
  ```bash
  touch -t 197001010000 .last_sync
  ```
- If no changed files are found and no files were specified, report "Nothing changed since last sync" and stop
- Read each modified/new note to extract propagatable insights

### Pre-propagation deduplication
After reading each changed research note, check its frontmatter for a `propagated_to:` field. This field is set by skills (`/stress-test`, `/scenario`, `/compare`, `/deepen`) that create a research note AND directly append Log entries to thesis notes in the same operation.

**Verification pass** — `propagated_to` is not trusted at face value. Two distinct failure modes exist:
- **Cross-thesis failure**: source skill crashed between theses (e.g., `/scenario` affecting 10 theses, interrupted after ticker 3). Tickers 4–10 are claimed but never updated.
- **Intra-thesis partial write**: source skill crashed between appending to `## Log` and appending to `## Related Research` (or vice versa) within a single thesis. One section has the wikilink; the other does not.

For each ticker listed in `propagated_to:`:

1. Locate the thesis file in `Theses/` (match by ticker prefix, e.g., `NVDA` → `Theses/NVDA - *.md`).
2. **Perform TWO independent section checks** — partial-write detection requires checking each section separately. For research note `Research/2026-04-17 - Scenario - China Taiwan.md`, the filename to search is `2026-04-17 - Scenario - China Taiwan`:
   - **Log check**: Does the thesis's `## Log` section contain the filename?
   - **Related Research check**: Does the thesis's `## Related Research` section contain the filename?
3. Classify into one of four buckets based on the two check results:

   | Log | Related Research | Bucket | Action |
   |---|---|---|---|
   | ✓ | ✓ | **Complete** | Exclude from propagation set (no work). |
   | ✓ | ✗ | **Partial-repair (RR-only)** | Include in propagation set with flag `partial_repair: related_research_only`. Step 3 appends the missing Related Research wikilink only. Warn: `⚠️ Partial-write repair — [TICKER] Log has [research-note] but Related Research missing. Adding wikilink.` |
   | ✗ | ✓ | **Partial-repair (Log-only)** | Include in propagation set with flag `partial_repair: log_only`. Step 3 appends the missing Log entry only. Warn: `⚠️ Partial-write repair — [TICKER] Related Research has [research-note] but Log missing. Adding Log entry.` |
   | ✗ | ✗ | **Full-repair** | Propagation failed silently. Include in propagation set with no flag — run full Step 2–3 treatment. Warn: `⚠️ propagated_to claimed [TICKER] but no Log/Related Research reference found — re-propagating fully.` |

> **Partial-repair semantics**: entries flagged `partial_repair: *` receive ONLY the specific missing mechanical update (Log OR Related Research). The research note's source skill (`/stress-test`, `/scenario`, `/compare`, `/deepen`) owns any analytical section rewrites it may perform; `/sync`'s role in partial-repair is mechanical append-only. Skip Step 2 (Deep Implication Analysis), Steps 3b–3e analytical work, drift detection, and conviction-trigger check for these tickers.

The research note may still propagate to OTHER theses not listed in `propagated_to:` (e.g., cross-thesis references, sector peers) via the normal Step 1 graph/fallback resolution.

### Graph-assisted mode (default):
After identifying changed files, use `_graph.md` to resolve the propagation set:
1. For each changed Research note → look up which theses link to it (check Thesis Adjacency Index for any thesis listing that research note)
   - **Fallback 1 (new/unlinked notes)**: if no thesis is found in the Adjacency Index, check the research note's `ticker:` frontmatter and outbound `[[Theses/...]]` wikilinks to identify the target thesis directly. **Closed-status gate**: before including a matched thesis, read its frontmatter. If `status: closed` (file still in `Theses/` from a failed archive move), skip it and log: `⚠️ [TICKER] matched via Fallback 1 but status: closed — skipping propagation. Complete the archive move: mv "Theses/[file]" "_Archive/[file]" → /graph. Or reopen via /status TICKER status closed→active.` Include only non-closed matched theses in the propagation set.
   - **Fallback 2 (tag + macro heuristics)**: if Fallback 1 yields no match for any reason — `ticker:` is absent/empty, `ticker:` is present but does not resolve to a `Theses/` file (e.g., thesis does not exist yet), OR no `[[Theses/...]]` wikilinks exist — apply two additional heuristics:
     1. **Tag scan**: Check `tags:` for ticker-like tokens (all-uppercase, 1-5 characters). For each candidate, verify it matches a `Theses/` filename prefix (e.g., tag `NVDA` → `Theses/NVDA - *.md`). **Closed-status gate**: before including, read the matched thesis's frontmatter; skip if `status: closed` with the same warning as Fallback 1. Include any non-closed matched thesis in the propagation set. (Note: if the ticker from Fallback 1 also failed because no matching file exists, the tag scan for the same token will fail too — this heuristic primarily helps when the research note's `ticker:` differs from a `tags:` entry that does resolve.)
     2. **Macro reverse lookup**: Collect all outbound `[[Macro/...]]` wikilinks from the research note. For each, look up the Macro → Theses reverse index in `_graph.md` to resolve affected theses. Include all matched theses in the propagation set. This catches research where the intended ticker has no thesis yet but the macro linkages identify related theses that should be updated.
   - If all fallbacks yield no match, log: `ℹ️ [filename] — no propagation target found. Consider adding ticker: frontmatter or [[Theses/...]] wikilinks, or run /thesis [TICKER] then /sync [TICKER] to establish the linkage.` Include in Step 8 report.
2. For each changed Thesis → look up its sector notes, macro notes, and cross-thesis references
3. For each changed Macro note → look up the Macro reverse index to find affected theses
4. For each changed Sector note → look up the Sector reverse index to find member theses
5. Union all affected files → this is the set of files to read and potentially update

**Missing file resilience**: When reading files in the propagation set, if a file does not exist (e.g., a thesis was archived by `/prune` or `/status` since the graph was last built), skip it gracefully and log: `⚠️ Skipped [filename] — file not found (likely archived). Run /graph to rebuild.` **Closed-status resilience**: for every thesis file actually read in the propagation set, check its frontmatter. If `status: closed` with the file still in `Theses/` (failed archive move from `/status` Step 7.5 or `/prune` Stage 2), skip propagation to it and log: `⚠️ Skipped [TICKER] — status: closed but file remains in Theses/ (failed archive move). Propagation suppressed to prevent closed-thesis contamination. Complete: mv "Theses/[file]" "_Archive/[file]" → /graph. Or reopen: /status TICKER status closed→active [rationale].` Do NOT fail the sync. Continue processing remaining files. Collect all skipped files (both branches) and include them in the Step 8 report.

### All mode (Two-Pass Triage):

Reading all ~40 thesis notes, ~13 sector notes, and ~6 macro notes in full will exceed context limits. Use a lightweight scan to triage by delta significance, then deep-read only notes with meaningful propagation paths.

#### Pass 1 — Lightweight scan
1. Identify changed files using `.last_sync` watermark (same as default mode). If first run, treat all files as changed.
2. For each thesis in Theses/, read **only frontmatter + Summary + last 3 Log entries** (stop reading after the 3rd-most-recent `###` Log heading). This yields ~300-400 words per thesis — manageable for the full set.
3. For each sector note in Sectors/, read **only frontmatter + Active Theses + Log sections**.
4. Read ALL macro notes in full (small set, ~6 files — always worth full context).

#### Pass 2 — Triage and deep read
5. Using the lightweight summaries + the changed file list from Pass 1, classify each thesis:
   - **High delta**: Directly referenced by a changed research note, shares sector with changed content, has cross-thesis links to changed theses, or its own Log shows recent conviction/status changes → read the **full thesis note**
   - **Low delta**: Same macro exposure or adjacent sector to changed content, but no direct reference → read **Summary + Non-consensus Insights + Outstanding Questions + Bull/Bear Case** sections only (skip Business Model, Industry Context, Key Metrics)
   - **No delta**: No plausible propagation path from any changed content → do NOT read further. Carry forward the Pass 1 summary for completeness checks only.
6. Read sector notes in full **only for sectors containing at least one High-delta thesis**. For other sectors, the Pass 1 scan is sufficient.
7. Proceed to Step 2 with the prioritised reading set.

This typically reduces deep reads from ~58 files to 15-25 depending on how broadly the changes propagate.

### Ticker-scoped mode:

1. **Pre-check**: If `_graph.md` does not exist, warn: `⚠️ Graph missing — cannot resolve ticker scope. Run /graph first, or use /sync (default) instead.` Then stop.

2. **Read `_graph.md`** and attempt to locate the ticker's entry in the Thesis Adjacency Index. Three outcomes:

   **Outcome A — Entry found**: proceed to step 3.

   **Outcome B — Entry absent, thesis file exists in `Theses/`** (graph is stale; common after chain-deferred `/thesis` graph updates, after Rule 9 mistakenly removed an active entry, or after manual graph edits):
   1. Locate the thesis file via ticker-prefix glob: `Theses/TICKER - *.md`.
      - If multiple matches, stop: `⚠️ Multiple Theses/ files match prefix "[TICKER]" — [list]. Resolve filename collision before re-running.`
   2. **Closed-status gate** — read the thesis's frontmatter first. If `status: closed`, the file is in `Theses/` only because a prior `/status active→closed` (Step 7.5) or `/prune` (Stage 2) archive move failed. Reconstructing its graph entry would silently re-embed the closed thesis into the adjacency index, reverse-indexes, and cluster tables, producing a silent re-opening that every downstream skill would then treat as legitimate. Stop with:
      ```
      ⚠️ [TICKER] has status: closed but file remains in Theses/ (failed archive move).
      Refusing to reconstruct graph entry — would silently re-open the closed thesis.
      To complete the closure: mv "Theses/TICKER - [name].md" "_Archive/TICKER - [name].md", then /graph.
      To reopen instead: /status TICKER status closed→active [rationale], then /sync TICKER.
      ```
      Otherwise proceed.
   3. Extract outbound `[[wikilinks]]` from the thesis file. Categorize by target directory:
      - `Sectors/` → sector adjacency
      - `Macro/` → macro adjacency
      - `Theses/` → cross-thesis adjacency
      - `Research/` → research adjacency
   4. Use the reconstructed adjacency as the resolved set for step 3.
   5. Mark this thesis for **graph entry creation** in Step 7 Rule 4 (the standard "new thesis" path will write the entry — this rule treats reconstructed entries identically to genuinely new ones).
   6. Warn: `⚠️ Graph missing entry for [TICKER] — reconstructed adjacency from thesis file. Entry will be added to _graph.md in Step 7. Run /lint after sync to confirm graph health.`
   7. Persist `entry_reconstructed: TICKER` for the Step 8 report.

   **Outcome C — Entry absent AND `Theses/TICKER - *.md` does not exist**:
   1. Check `_Archive/` for the file: `_Archive/TICKER - *.md`.
   2. **If found in archive** (thesis is closed): stop with:
      ```
      ⚠️ [TICKER] is closed — file lives in _Archive/. Sync targets only active or monitoring theses.
      To reopen: /rollback TICKER → select the most recent (pre-status) snapshot, then /sync TICKER.
      ```
   3. **If not found anywhere**: stop with:
      ```
      ⚠️ No thesis found for [TICKER] in Theses/ or _Archive/. Did you mean a different ticker? Run /thesis [TICKER] to create it.
      ```

3. **Resolve the full adjacency set**: the thesis note, all listed sector notes, macro notes, cross-thesis references, and research notes.
   - **Also scan for unlinked research**: grep `Research/` for files with `ticker: TICKER` in frontmatter not already in the adjacency entry's `research:` list — these are newly ingested notes the graph doesn't know about yet. Include them in the resolved set.

4. **Read all resolved files** — ignore `.last_sync` watermark (this mode is timestamp-independent).

5. **Proceed to Step 2** with all resolved files as the input set.

## Step 2: Deep Implication Analysis

**This is the critical analytical step. Spend maximum reasoning effort here. Do NOT proceed to writing updates until this analysis is complete for all source notes.**

**Source deduplication**: If a thesis appears as a changed source AND one or more Research notes referencing that thesis are also in the changed set, analyze the Research notes as the primary sources. The thesis log entries referencing those Research notes do not contain additional propagatable information — focus analysis effort on the Research notes themselves.

For each source note (new/changed research), read it fully and analyse:

- **Factual deltas**: New data points, metrics, quotes, events — what is concretely new?
- **Assumption challenges**: Which existing thesis assumptions does this validate, weaken, or invalidate? Be specific — name the assumption.
- **Second-order implications**: What follows from this information that isn't stated explicitly? (e.g., "TSMC capex cut → ASML order book at risk → BESI utilisation rates drop")
- **Competitive dynamics shifts**: Does this change the relative positioning of companies within a sector?
- **Macro linkages**: Does this micro-level data have macro implications, or vice versa?

The quality of the entire propagation depends on the depth of thinking in this step.

## Step 3: Update Thesis Notes

### 3.0: Partial-Repair Fast Path (from Step 1 verification)

Before the full analytical pass, handle any `partial_repair`-flagged thesis pairs from Step 1's verification pass. These are mechanical append-only fixes — no snapshot, no Step 3b–3e analytical work, no drift detection.

For each ticker with flag `partial_repair: log_only`:
- Append to the thesis's `## Log` section:
  ```
  ### YYYY-MM-DD
  - [[Research/source-note]]: partial-write repair — Log entry was missing while Related Research wikilink existed. Restored by /sync.
  ```
- Skip retry-dedup check (Step 3f) — by construction, Log did not contain this research note, so there is nothing to deduplicate against.
- Run Step 7 Rule 1 in this sync: verify the research note is listed in the thesis's `research:` field in the adjacency index. If missing, add it. Rationale: although Related Research wikilink existed (implying the source skill reached its RR-append step), the source skill may have crashed BEFORE its own graph update (most producers update graph last). Running Rule 1 here as a safety net costs nothing if the graph entry already exists.

For each ticker with flag `partial_repair: related_research_only`:
- Append to the thesis's `## Related Research` section:
  ```
  - [[Research/source-note]]
  ```
- Do NOT append a Log entry — Log already contains the research note's reference, adding another would be a duplicate audit trail.
- Run Step 7 Rule 1 in this sync: verify the research note is listed in the thesis's `research:` field in the adjacency index. If missing, add it (this catches the case where the source skill's graph update was deferred or skipped).

**Report** all partial-repair actions in Step 8 under a dedicated line:
- `Partial-write repairs: [N] Log appends, [M] Related Research appends — [list TICKER/research-note pairs]`

After Step 3.0, proceed to the normal full-propagation pass below **only for tickers in the full-repair bucket and for tickers/files not previously dedup-skipped**. Complete-bucket and partial-repair-bucket tickers are done.

### 3a: Read the Full Thesis
Read the entire thesis note. Understand the current state of every section before proposing changes.

### 3b: Analyse Impact Per Section
Map the insights from Step 2 against each thesis section. For each, determine: does the new research provide a meaningful delta? Be selective — not every piece of research affects every section.

**Section-by-section analysis framework:**

| Section | Update when... |
|---|---|
| **Summary** | The core investment case has shifted — not incremental data, but a change in the thesis direction or key assumption |
| **Non-consensus Insights** | New evidence strengthens/weakens an existing insight, OR a genuinely new non-consensus angle emerged |
| **Outstanding Questions** | A question has been answered (mark resolved with answer + date), OR the research raises new questions worth tracking |
| **Business Model** | Structural change to revenue model, product mix, go-to-market, or segment economics |
| **Industry Context** | Competitive positioning, market share, or pricing power shifted |
| **Bull Case** | New supporting evidence, or a bull scenario element was validated/invalidated |
| **Bear Case** | New counter-evidence, or a bear scenario element was validated/invalidated |
| **Catalysts** | New catalyst identified, or existing catalyst resolved — mark outcome |
| **Risks** | New risk emerged, existing risk probability changed materially, or a risk was retired |
| **Conviction Triggers** | New evidence validates/invalidates a trigger condition, OR a trigger threshold needs updating based on changed fundamentals |

**Do NOT update sections where the delta is trivial or where you'd be restating what the research note already says. The thesis contains synthesised conclusions, not duplicated research content.**

### 3c: Pre-Edit Safety — Snapshot

Classify proposed edits by tier:

**Tier A — Snapshot required:** Editing or rewriting existing text in Summary, Non-consensus Insights, Outstanding Questions, Business Model, Industry Context, Bull Case, Bear Case, Conviction Triggers.

**Tier B — No snapshot needed:** Appending new Catalysts, Risks, or Conviction Triggers. Appending to Log, Related Research. Updating numbers in Key Metrics table.

**If any Tier A edits are planned for a thesis:**
1. Create snapshot directory if needed:
   ```bash
   mkdir -p _Archive/Snapshots
   ```
2. Copy the current thesis note (preserving the original at its path so all wikilinks remain intact):
   ```bash
   cp "Theses/TICKER - Company Name.md" "_Archive/Snapshots/TICKER - Company Name (pre-sync YYYY-MM-DD-HHMM).md"
   ```
3. Read the newly created snapshot, then add to its frontmatter:
   ```yaml
   snapshot_of: "[[Theses/TICKER - Company Name]]"
   snapshot_date: YYYY-MM-DD
   snapshot_trigger: sync
   snapshot_batch: sync-YYYY-MM-DD-HHMM
   ```
   > **Batch ID**: Generate the `HHMM` timestamp once at the start of the snapshot phase (e.g., via `date +%H%M`). Reuse the same `snapshot_batch` value across ALL snapshots created in this sync run (thesis, sector, macro). This enables `/rollback` cascade detection to distinguish same-day repeat operations.

4. Proceed with edits to the ORIGINAL thesis note.

### 3d: Apply Substantive Edits
For each section identified in 3b, make precise edits:

- **Integrate, don't append** — weave new evidence into existing prose so the section reads as a coherent, up-to-date analysis. Do NOT add "Update (2026-04-16): ..." blocks within sections.
- **Preserve voice and structure** — match the existing writing style and analytical depth of the section.
- **Net deletions are OK** — if new evidence invalidates a prior claim, remove the claim rather than leaving it alongside its contradiction.
- **Mark resolved Outstanding Questions** — format: ~~Original question~~ → Resolved YYYY-MM-DD: [answer]. Keep resolved questions visible so the analytical trail is preserved.

### 3e: Mechanical Updates (every time)
- **Key Metrics**: Update table if new numbers are available
- **Related Research**: Add wikilink to new research note
- **Conviction trigger check**: If new data satisfies a pre-defined Conviction Trigger condition, flag it:
  `⚡ Trigger hit: [quote the trigger] — [what happened]`
- **Conviction drift detection**:
  > **Log Format Contract** — drift detection depends on exact prefix matching across skills. Changing any prefix in the source skill breaks detection here. **Authoritative registry**: `.claude/skills/_shared/log-prefixes.md` — entries §1, §3, §4, §5, §6 govern drift behavior. The table below is a local quick-reference; on any discrepancy, the registry wins. `/lint` check #29 verifies the two stay in sync.
  > | Prefix | Registry § | Source | Drift role |
  > |---|---|---|---|
  > | `"Stress test"` | §1 | `/stress-test` Phase 4 step 2 | Excluded from drift window |
  > | `"Deepened"` / `"↳ CORRECTION: Deepened"` | §3, §4 | `/deepen` Phase 5c | Excluded if chain-linked to stress test (Session Chain §3g), else ≤7 day heuristic |
  > | `"Conviction reaffirmed"` | §5 | `/status` Step 2R | Anchors (resets) drift window |
  > | `"Status change: conviction"` | §6 | `/status` Step 4 | Anchors (resets) drift window |

  Scan Log entries backward from most recent, **excluding entries that begin with "Stress test"** (these are periodic adversarial reviews, not evidence of fundamental deterioration — counting them inflates drift signals). **Also exclude entries that begin with "Deepened" or "↳ CORRECTION: Deepened"** when either condition is met:
  - **(a) Session Chain awareness** (preferred): `_hot.md` `## Session Chain` contains both `/stress-test ✅` and `/deepen ✅` in the same chain, with scope overlapping this thesis's ticker → exclude regardless of date. This covers chain §3g even when it spans multiple calendar days.
  - **(b) Date heuristic** (fallback when the chain has already been cleared by a prior `/sync`): the entry occurs within 7 calendar days of a "Stress test" entry for the same ticker. Window calibrated to match the natural workflow — chain §3g (`/stress-test → /deepen → /sync`) often spans multiple days as the user reflects on stress-test findings before commissioning targeted research. The 1-day window left a hole; 7 days catches typical reflection-then-deepen rhythm. Trade-off: a Deepened entry truly unrelated to a stress test from 2-7 days ago is excluded → potential false negative for drift signal. Acceptable because (i) /deepen Log entries explicitly state conviction impact in their text, providing direct human-readable signal independent of the drift count, and (ii) drift detection is additive evidence, not the only signal.
  These are gap-filling research triggered by the stress test (chain §3g), not independent evidence of deterioration. If a "Conviction reaffirmed" or "Status change: conviction" entry is found, anchor the window there — only count entries AFTER the anchor. If fewer than 3 entries exist after the anchor, drift detection has insufficient data and does not fire. If no anchor exists, use the last 5 entries as the window.
  - conviction: high but 3+ entries in window weakening → `⚠️ Conviction drift — [N]/[window size] recent updates flagged headwinds. Reassess. To acknowledge after review: /status TICKER reaffirm [rationale]`
  - conviction: low but 3+ entries in window strengthening → `📈 Positive drift — [N]/[window size] recent updates supportive. Reassess. To acknowledge after review: /status TICKER reaffirm [rationale]`

### 3f: Log Entry (last — summarises everything above)

**Retry deduplication** (24-hour window): Before appending, scan the thesis's `## Log` section for all `### YYYY-MM-DD` heading blocks whose date is within the last 24 hours of current time (today's date OR yesterday's date — Log entries carry dates only, no timestamps, so the practical window is "today and yesterday"). For each in-window entry, check whether it references the same source research note wikilink (`[[Research/...]]`). If a match is found, this thesis was already updated by a prior `/sync` run or by a chain-participant skill that failed before completing all propagation — skip the Log append for this thesis to avoid duplicates. Log: `ℹ️ Skipped duplicate Log entry for [TICKER] — already contains [matching-date] + [[research-note]].` Include skipped theses in the Step 8 report under the **Deduplication skips** line.

> **Why 24 hours instead of last-3-entries**: a single workflow chain (e.g., 3e: `/scenario` → `/status` → `/compare` → `/sync`) can produce 3+ Log entries on one thesis in a single day. A retry `/sync` scanning only the "last 3" blocks misses earlier same-day entries and re-appends duplicates. The 24-hour window captures every entry from the in-progress session regardless of volume. It remains safe across day-boundary crossings (23:59 → 00:01) because "yesterday" is still included.

> **Performance note**: scanning all in-window entries is at most dozens of blocks per thesis — cheaper than re-reading the thesis itself, which Step 3a already does. No additional I/O cost.

Append to Log section:
```
### YYYY-MM-DD
- [[Research/source-note]]: [what changed] — [conviction impact: unchanged/strengthened/weakened + 1 reason]
```
Max 2 lines. The log is an audit trail — the analysis lives in the updated sections above.

## Step 4: Update Sector Notes

For each affected Sector Note:

### 4a: Pre-Edit Safety — Snapshot
If edits will modify existing analytical text (competitive dynamics, value chain analysis, sector-level observations, company comparison narratives) — not just adding links or new research entries:
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
- **Update competitive dynamics** if the research changes relative positioning of companies in the sector
- **Update value chain analysis** if supply chain relationships shifted
- **Revise sector-level observations** if cross-company patterns emerged from the new research
- **Update company comparison tables** with new data points if available

Skip snapshot if only adding research note links to the listing.

### 4c: Post-Edit Verification

After completing all edits to a sector note, re-read the modified note and verify each edited section:
1. Ends with a complete sentence (not mid-word, mid-sentence, or with an unclosed formatting marker like unmatched `**` or `*`)
2. Does not contain incomplete table rows (lines starting with `|` but not ending with `|`)
3. Does not end with a conjunction, preposition, comma, or opening bracket

If any check fails: `⚠️ Sector note may contain a partial edit in [section]. Snapshot available: [[_Archive/Snapshots/...]]. Review manually or /rollback.` Include in the Step 8 report. This mirrors `/compare`'s post-edit verification and catches truncation from mid-edit failures.

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
- **Revise trading/allocation implications** if the macro thesis has shifted based on new evidence

Skip snapshot if only adding wikilinks to the research.

## Step 6: Update _hot.md

> **Chain finalization (_hot.md)**: If `## Session Chain` shows active entries from a workflow chain, the Active Research Thread already contains short per-step lines from prior skills. Apply this sync's update as a full entry (normal compress/Previous logic), consolidating the chain's work into a final thread state. The Session Chain section itself is cleared in Step 7.

If `_hot.md` does not exist (first run), create it with sections: `## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`, `## Session Chain` (set to `*No active chain.*`). Use frontmatter: `date: YYYY-MM-DD`, `tags: [meta, hot-cache]`.

**Lifecycle rules — enforce strictly:**
1. **Update the date** in frontmatter and heading
2. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write the new thread (current focus + next step), then append `*Previous:*` line(s) — max 5, drop oldest.
3. **Latest Sync**: Replace the existing Latest Sync section entirely with this sync's summary. One bullet per thesis updated, max 1 line each. Format:
   ```
   - **[TICKER]**: [what changed] — [conviction impact]
   ```
4. **Previous Syncs**: Compress the outgoing Latest Sync into a single summary line and prepend it to a "## Sync Archive" section. Keep max 3 archived entries. Delete oldest if over 3.
5. **Open Questions**: If any Outstanding Questions were resolved on theses during this sync (Step 3d), mark them resolved in _hot.md's Open Questions. If conviction triggers or drift were flagged (Step 3e), add the reassessment question.
6. **Recent Conviction Changes**: If any conviction triggers hit (Step 3e ⚡) or drift was flagged (Step 3e ⚠️/📈), add an entry noting the flag (not the change itself — conviction changes require `/status`).
7. **Hard cap**: After writing, check total word count. If _hot.md exceeds 2,000 words, prune Sync Archive entries (oldest first) until under the cap.

## Step 7: Incremental Graph Update (default mode only)

> **Chain finalization (graph — default/ticker mode)**: After completing the incremental graph update, clear `## Session Chain` in `_hot.md` to `*No active chain.*` **and remove any Graph Debt line**. The sync's incremental update captures all graph changes deferred by prior chain steps because Step 7 reconciles the full Step 1 changed-file set against the graph (rule 8 below), not just files that this sync modified in Steps 3–5. When a Graph Debt line was present at the start of this sync, Rule 8.ii additionally expands the reconciliation sweep to every `Research/` file with mtime > `_graph.md`'s `date:` frontmatter — this catches debt research notes whose mtimes sit behind `.last_sync` from a prior session's dedup-skip. This makes `/sync` the natural endpoint for any workflow chain, including those that crossed a session boundary into debt.

**Skip this step entirely in all mode** — but **do reset `_graph.md`'s `date:` frontmatter to `1970-01-01`** if the file exists. This forces the next default `/sync` into all-mode fallback (date >30 days), preventing it from relying on a now-stale graph. All-mode runs should still be followed by `/graph` for a full rebuild — incremental updates after touching 30+ files would produce an unreliable graph.

**All-mode Graph Debt preservation**: Before resetting the graph date, read `## Session Chain` in `_hot.md`. If an active chain exists with `Graph deferred: [N]` where N > 0:
1. Warn in the Step 8 report:
   ```
   ⚠️ Active chain had [N] deferred graph changes. /sync all cannot capture them.
   Converting to Graph Debt. Run /graph to resolve.
   ```
2. Clear the active chain steps but **preserve as Graph Debt**:
   ```
   *No active chain.*
   **⚠️ Graph debt**: [N] deferred from [YYYY-MM-DD] (/skill1, /skill2). Run `/graph` to capture.
   ```
   Extract the date and skill names from the cleared chain's `Steps` and `Date` fields. If Graph Debt already exists from a prior chain, accumulate: add the new deferred count to the existing debt count and note both dates.

If the chain has `Graph deferred: 0` (or no active chain), clear normally to `*No active chain.*` — but **preserve any existing Graph Debt line** (all-mode does not resolve debt since it skips the incremental graph update).

**Scope**: Rules 1–7 below apply to files that this sync modified in Steps 3–5 (thesis, sector, macro note edits). Rule 8 is a reconciliation pass that sweeps the Step 1 changed-file set (8.i) plus — when Graph Debt is present at sync start — research notes with mtime > `_graph.md`'s `date:` (8.ii); this captures graph changes deferred by chain-participant skills whose research notes were dedup-skipped, including across sessions. Rule 9 is the structural cleanup pass that sweeps `_graph.md`'s adjacency index against the current `Theses/` directory to remove ghost entries from chain-deferred `/status active→closed` operations and prior-session closures.

For each file modified by this sync in Steps 3–5:
1. **New research note linked** → Add it to the relevant thesis's `research:` list in the Thesis Adjacency Index
2. **New wikilink added to a thesis** → Add the target to the appropriate field (cross-thesis, sector, macro, or research). **Reverse index**: if the added link is a sector or macro note, also add the thesis ticker to that note's row in the corresponding reverse index table
3. **New wikilink removed from a thesis** → Remove the target from the appropriate field. **Reverse index**: if the removed link is a sector or macro note, also remove the thesis ticker from that note's row in the corresponding reverse index table
4. **New thesis created** → Add a full adjacency entry with all fields populated. **Reverse index**: add the thesis ticker to every sector and macro row it references. **Includes reconstructed entries from Step 1 Outcome B** — when ticker-scoped mode self-healed a missing graph entry, this rule writes that entry. The thesis is "new to the graph" even if not new to `Theses/`. Reverse-index updates apply equally.
5. **Thesis archived/deleted** → Remove its adjacency entry and remove it from all reverse indexes and cluster tables
6. **New cross-thesis connection discovered** → Update the Cross-Thesis Clusters table if it represents a new cluster or extends an existing one
7. **Orphan status changed** → If a previously orphan research note was linked to a thesis, remove it from the Orphan list

### Reconciliation of dedup-skipped research notes (chain-deferred capture)

8. **Sweep the reconciliation set against the graph.** The reconciliation set is the union of:
   - **(8.i)** All `Research/` files in the Step 1 changed-file set that were NOT already handled by rules 1–7 above. In practice, these fall into two categories:
     1. **Dedup-skipped research notes** — research notes with `propagated_to:` frontmatter whose Step 1 verification classified the target thesis as Complete-bucket (both Log and Related Research present), causing Steps 2–5 to skip the research-note → thesis pair. Producers that can trigger this path: `/stress-test`, `/deepen`, `/compare`, `/scenario` (the four skills that set `propagated_to:`).
     2. **Chain-deferred non-propagator research notes** — research notes without `propagated_to:` (from `/surface`, `/brief`) whose source skill deferred its own graph update as a chain participant. Normally Rule 1 captures these when the target thesis is read in Steps 3–5; Rule 8 provides a safety net when the thesis was NOT in the propagation set (e.g., unscoped `/surface` writing a scan note without a resolvable target, or a thesis that fell out of the set via graph-assisted resolution failure).
   - **(8.ii) Graph Debt expansion — applies only when `_hot.md` contains a `⚠️ Graph debt` line at the start of this sync.** Additionally include every `Research/` file whose mtime is greater than `_graph.md`'s `date:` frontmatter value, regardless of its `.last_sync` watermark position. This catches research notes created by chain-participant skills during the debt accumulation period — their graph indexing was deferred and their mtimes may already be behind `.last_sync` (e.g., a prior session's dedup-skip advanced the watermark past them without registering them in the graph).

   For each research note in the reconciliation set:

   a. **Resolve the target thesis** using the research note's `ticker:` frontmatter, outbound `[[Theses/...]]` wikilinks, or `tags:` matching a `Theses/` filename prefix (same resolution logic as Step 1 Fallback 1–2).

   b. **Check the graph**: Look up each resolved thesis in the Thesis Adjacency Index. If the research note is absent from that thesis's `research:` list, **add it**. This covers two deferral paths: (i) `propagated_to:` producers whose content propagation was dedup-skipped but whose graph entry was deferred by Session Chain protocol; (ii) non-propagator research creators (`/surface`, `/brief`) whose chain participation skipped their own graph update and whose thesis was not read in Steps 3–5 this sync.

   c. **Orphan list cleanup**: If the research note appears in `## Orphan Research Notes`, remove it (it is now linked from a thesis's adjacency entry).

   d. **Reverse index maintenance**: If the research note contains outbound `[[Macro/...]]` or `[[Sectors/...]]` wikilinks not already reflected in the graph's reverse indexes, add the appropriate reverse mappings.

   If no target thesis can be resolved (all fallbacks fail), leave the note unindexed and include it in the Step 8 report under **Unresolved research notes**.

   **Graph Debt resolution**: After the expanded sweep completes, remove the `⚠️ Graph debt` line from `## Session Chain` in `_hot.md` (handled in Step 7's chain-finalization block — mentioned here so the sweep's purpose is visible in the report logic). Step 8 reports the resolved debt count under **Graph reconciliation**.

   > **Why expand to `_graph.md`'s date**: the debt line marks that one or more chain-deferred graph updates from a prior session were converted (by `/sync all`) or abandoned (by a session ending mid-chain) without being applied. The research notes involved may have mtimes that precede the current `.last_sync` (because a prior `/sync` touched the watermark but dedup-skipped them). Using `_graph.md`'s `date:` — which `/graph` and /sync rule 7's post-write updates advance only on actual graph writes — gives a lower watermark that covers the debt period. The sweep is scoped to `Research/` only (the set of files that chain-participant skills create and whose indexing typically defers), keeping the cost bounded.

### Archived-thesis cleanup sweep (default mode only — skip in ticker-scoped mode)

9. **Sweep `_graph.md`'s Thesis Adjacency Index against the current `Theses/` directory.** This captures closures whose graph updates were deferred by Session Chain protocol (e.g., `/status active→closed` that joined an active chain and incremented `Graph deferred` instead of applying the closure cleanup) or closures from prior sessions that never ran `/graph`.

   For each `### TICKER - Name` entry in the Thesis Adjacency Index whose corresponding `Theses/[TICKER] - *.md` file does NOT exist on disk:

   a. **Remove the adjacency entry** from the `## Thesis Adjacency Index` section.

   b. **Remove from reverse indexes**: delete the ticker from every row in both `## Reverse Index: Macro → Theses` and `## Reverse Index: Sector → Theses`. If removing the ticker leaves a row empty, keep the row (other theses may be added later).

   c. **Remove from Cross-Thesis Clusters**: delete the ticker from every cluster. If removing it reduces a cluster to <2 members, dissolve the cluster.

   d. **Cross-thesis reference cleanup**: scan every remaining entry in the Thesis Adjacency Index and remove the archived ticker from their `cross-thesis:` fields. These are ghost references — leaving them would cause a future `/sync` to attempt to read the archived thesis file.

   e. **Orphan reclassification**: for each research note listed in the removed thesis's `research:` field, check whether it appears in any other thesis's `research:` field. If not, add it to `## Orphan Research Notes`.

   f. **Log**: include in Step 8 report: `🧹 Archive cleanup: [TICKER] — removed adjacency entry, [N] cross-thesis refs scrubbed, [M] research notes moved to orphan.`

   **Scope**: this sweep applies in default mode unconditionally, AND in ticker-scoped mode WHEN `_hot.md` contained a `⚠️ Graph debt` line at sync start. Rationale: Graph Debt explicitly signals known deferred cleanup work — resolving it during any /sync run (not just default) honors the debt mechanism's intent. Skip in ticker-scoped mode without Graph Debt — ticker-scoped sync focuses on a single adjacency set and should not mutate unrelated graph entries unless debt explicitly signals known cleanup is owed. Skip in all-mode — Step 7 does not run there.

   **Note on closure-exception interaction**: As of `/status` Step 6 closure-immediate override, `/status active→closed` operations apply graph cleanup at the time of the closure (not deferred). Rule 9 still serves as a safety net for: (a) closures from prior versions of `/status` that did defer, (b) manual file deletions outside any skill, and (c) closures via `/prune` whose Stage 4 graph step was interrupted before completion.

   **Why here (not Step 1)**: Step 1's "Missing file resilience" detects archived files during propagation reads but only warns; it cannot mutate `_graph.md` because all graph edits are gathered into Step 7 for transactional consistency. Rule 9 is the structural cleanup counterpart.

### New-thesis adjacency sweep (symmetric counterpart to Rule 9)

10. **Sweep the current `Theses/` directory against `_graph.md`'s Thesis Adjacency Index.** This captures chain-deferred `/thesis` creations whose graph entries were skipped by Session Chain protocol (e.g., `/thesis` joining a `/surface`-started chain and incrementing `Graph deferred` rather than creating the adjacency entry in its Step 5). Symmetric to Rule 9: Rule 9 removes ghost entries for deleted files; Rule 10 adds missing entries for newly-created files. Without Rule 10, a chain-deferred `/thesis` followed by default `/sync` as finalizer leaves the new thesis permanently missing from the graph — default `/sync` cannot resolve its outbound adjacencies (sector, macro, cross-thesis) for any subsequent run until `/graph` is invoked manually.

   For each `Theses/[TICKER] - [Name].md` on disk whose corresponding `### TICKER - Name` entry does NOT exist in the Thesis Adjacency Index:

   a. **Closed-status gate** — read the thesis's `status:` frontmatter. If `status: closed`, skip and log: `⚠️ [TICKER] has status: closed but file remains in Theses/. Adjacency entry NOT reconstructed (would silently re-open closed thesis). Complete the archive move: mv "Theses/[file]" "_Archive/[file]" → /graph. Or reopen: /status TICKER status closed→active.` This gate mirrors Step 1 Outcome B's closed-status gate — both paths guard against the same failed-archive-move corruption vector.

   b. **Read outbound `[[wikilinks]]`** from the thesis file. Categorize by target directory:
      - `Sectors/` → sector adjacency
      - `Macro/` → macro adjacency
      - `Theses/` → cross-thesis adjacency
      - `Research/` → research adjacency

   c. **Write a full adjacency entry** under `## Thesis Adjacency Index` (sort lexicographically among existing entries). Populate all four fields (or `—` when empty).

   d. **Reverse index update**: add the ticker to every sector and macro reverse-index row it references. If a referenced row does not yet exist for a particular sector or macro, create it.

   e. **Cross-thesis cluster update**: if the new entry's `cross-thesis:` list creates a bidirectional link with an existing adjacency entry that also references this new ticker, add or extend a row in the `## Cross-Thesis Clusters` table.

   f. **Log**: include in Step 8 report: `✨ New-thesis sweep: [TICKER] — adjacency entry created, [N] reverse-index rows updated, [M] cluster edges added.`

   **Scope**: default mode unconditionally (symmetric to Rule 9). Also applies in ticker-scoped mode WHEN `_hot.md` contains a `⚠️ Graph debt` line at sync start — debt explicitly signals known deferred creation work owed. Skip in ticker-scoped mode without Graph Debt (Rule 4 via Outcome B already handles the single-ticker case). Skip in all-mode — Step 7 does not run there (use `/graph` for full rebuild).

   **Why here (not Step 1)**: same rationale as Rule 9 — Step 1 resolves propagation targets but cannot mutate `_graph.md`; all graph edits are gathered into Step 7 for transactional consistency. Rule 10 is the structural addition counterpart to Rule 9's structural removal.

Update the frontmatter:
- `date:` → today's date
- `edges:` → increment/decrement based on links added/removed (estimate is fine)

### Post-write validation
After completing all graph edits, re-read `_graph.md` and verify:
1. YAML frontmatter still parses without error
2. All three section headings still present (Thesis Adjacency Index, both Reverse Indexes)
3. No unclosed `[[` wikilink brackets introduced by the edits
4. The adjacency entry count matches the `theses:` frontmatter value (±2)

If any check fails, warn: `⚠️ Graph may have been corrupted by this sync's incremental update — [specific failure]. Run /graph to rebuild.` Include this warning in the Step 8 report.

## Step 7.5: Touch Watermark

**Mandatory. Runs after ALL writes are complete (content + graph), immediately before reporting.**

```bash
touch .last_sync
```

This is the last mutation in the sync. If any prior step fails or the session is interrupted, the watermark remains unset and the next `/sync` will re-process the same changes — safe by default.

## Step 8: Report

- **Mode**: default (graph-assisted) | all
- **Files read**: [count]
- **Files updated**: [count]
- **Snapshots created**: [list with paths, or "none"]
- **Thesis updates** (one per thesis):
  - [TICKER]: [sections modified] — [conviction impact]. Snapshot: `[[_Archive/Snapshots/...]]` or N/A
- **Sector Note updates**: [list with one-line summary each]
- **Macro note updates**: [list with one-line summary each]
- **Propagation recovery**: [list any tickers where `propagated_to` was claimed but verification found NEITHER Log nor Related Research reference — these received full re-propagation. If none, omit this line.]
- **Partial-write repairs**: [list any tickers where Step 1 verification detected a partial-write state and Step 3.0 applied a targeted mechanical fix. Format: `[TICKER] — [Log append | Related Research append] — [research-note]`. If none, omit this line.]
- **Deduplication skips**: [list any tickers where a Log entry was skipped because the same date + research note wikilink already existed from a prior partial sync. If none, omit this line.]
- **Unresolved research notes**: [list any research notes where all fallbacks (graph, ticker/thesis links, tags, macro reverse index) yielded no propagation target. If none, omit this line.]
- Conviction triggers hit: [list any]
- Conviction drift flags raised: [list any]
- New connections discovered: [any surprising links]
- **Graph reconciliation** (default mode): [count of dedup-skipped research notes added to adjacency entries, orphans resolved via reconciliation. If the sync began with a Graph Debt line, additionally report: `+ [K] debt notes resolved via Rule 8.ii expansion`. If none needed, omit this line.]
- **Graph Debt resolved** (if Graph Debt was present at sync start): `⚠️ → ✅ Graph Debt line cleared — [N] debt items reconciled from [YYYY-MM-DD] ([skill list from debt line]).`
- **Archive cleanup** (default mode, Rule 9): [list any ticker whose adjacency entry was removed because the thesis file no longer exists, with counts of cross-thesis refs scrubbed and research notes moved to orphan. If none, omit this line.]
- **New-thesis sweep** (default mode or ticker-with-debt, Rule 10): [list any ticker whose adjacency entry was created because the thesis file exists but was missing from the graph, with counts of reverse-index rows updated and cluster edges added. Also list any ticker SKIPPED by Rule 10a's closed-status gate (file in Theses/ with status: closed). If none, omit this line.]
- **Entry reconstruction** (ticker-scoped mode, Step 1 Outcome B): [list TICKERs whose missing graph entries were reconstructed from thesis files and written via Step 7 Rule 4. If none, omit this line.]
- **Closed-status skips** (Fallback 1/2 or Missing-file-resilience): [list TICKERs skipped because status: closed + file still in Theses/ (failed archive move). If none, omit this line.]
- Graph updates (default mode): [edges added/removed, orphans resolved]
- **All-mode only**: `⚠️ Graph not updated. Run /graph to rebuild.`
- **All-mode Graph Debt** (if triggered): `⚠️ [N] deferred graph changes converted to Graph Debt. Run /graph to resolve.`

### Prominent fallback warning (when mode was all-mode due to a forced fallback from Step 0)

If the sync landed in all-mode via Step 0's fallback triggers (not because the user explicitly typed `/sync all`), emit this block at the VERY END of the Step 8 report, under a highlighted heading. This is the primary prevention for silent degradation after a monthly-maintenance interruption:

**For `fallback_reason: poisoned-by-prior-sync-all`** (graph date = 1970-01-01, set by a prior `/sync all`):
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 CRITICAL — This sync ran in fallback all-mode.

Cause: _graph.md is poisoned (date: 1970-01-01) from a prior `/sync all`
that was never followed by `/graph`. Every subsequent `/sync` will keep
hitting this fallback until you run `/graph`.

Consequences while unresolved:
  • Every /sync reads ALL ~58 vault files (expensive, slow)
  • Incremental graph updates (Rules 1–9) are skipped
  • Orphan list, reverse indexes, cross-thesis clusters drift
  • Graph Debt cannot accumulate or resolve normally

Action: run `/graph` now.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**For `fallback_reason: stale-[N]-days`** (N > 30, not from /sync all):
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ This sync ran in fallback all-mode.

Cause: _graph.md is [N] days old (>30 day staleness threshold).
Subsequent /sync runs will also fall back until you run /graph.

Action: run `/graph` to rebuild from vault state.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**For `fallback_reason: missing` or `fallback_reason: corrupt-*`**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ This sync ran in fallback all-mode.

Cause: [graph missing | graph structurally corrupt — [specific failure]]
_graph.md is required for graph-assisted sync. Without a rebuild, every
/sync will fall back to all-mode.

Action: run `/graph` to rebuild.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If the user explicitly invoked `/sync all` (user-chosen all-mode), suppress this block — Step 8's existing "⚠️ Graph not updated. Run /graph to rebuild." line is sufficient because the user chose the mode consciously. The prominent warning is reserved for **unintended** fallbacks.
