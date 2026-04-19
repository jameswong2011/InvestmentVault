---
name: lint
description: Run health checks on the vault for inconsistencies, stale data, orphaned notes, and missing connections. Use periodically or when user says "lint", "health check", or "audit".
model: opus
effort: max
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Bash(find * wc * date *)
---

## Scope Resolution

Parse `$ARGUMENTS` to determine scope:

- **Ticker** (e.g., `NVDA`): Scoped audit — run only checks relevant to that thesis and its graph adjacencies. Read the thesis, its linked research notes, its sector note, and its `_graph.md` entry. Much faster than a full audit.
- **No arguments / empty**: Full vault audit — run all checks (current behaviour).

**Scoped checks** (run for `/lint TICKER`):
#2 (Missing MOC entry), #4 (Missing frontmatter), #5 (Empty critical sections), #6 (Stale active thesis), #7 (Old financial data), #8 (Inactive research for this ticker), #12 (Conviction-evidence mismatch), #13 (Bull/Bear asymmetry), #14 (Template drift), #15 (Verbose Log entries), #19 (Graph entry exists), #21 (Graph edge validity for this thesis), #28 (Partial write detection for this thesis + its sector note), #30 (Sector resolution coverage for this thesis), **#35 (`_hot.md` schema integrity — always run, vault-global concern that affects every skill writing to `_hot.md` for this thesis)**.

**Vault-wide only** (skipped in scoped mode):
#1 (Orphaned research), #3 (Broken wikilinks), #9 (Unlinked mentions), #10 (Disconnected macro), #11 (Missing thesis candidates), #16 (Stale snapshots), #17–18 (Graph existence/staleness), #20 (Ghost entries), #22–24 (Graph consistency checks), #25 (Pending sync), #26 (Edge count accuracy), #27 (Catalyst calendar staleness), #29 (Log-prefix registry alignment), #32 (Orphaned ticker references), #33 (Closed-thesis files in Theses/), #34 (Sector frontmatter standardization), #36 (Prune batch-manifest state), **#37 (Incomplete-rename marker — runs scoped if marker's `ticker:` matches the scoped TICKER, otherwise vault-wide only)**.

> **Rationale for #35 in scoped mode**: `_hot.md` schema drift causes silent skill no-ops across 11 skills. The defect surfaces only via `/lint #35`, but a user who runs scoped `/lint TICKER` weekly (per User Guide §13 cadence) and full `/lint` monthly can carry the bug for ~30 days, during which every `/status`, `/deepen`, `/stress-test`, `/scenario`, `/compare`, `/sync`, `/surface`, `/prune`, `/rollback`, `/catalyst`, or `/thesis` invocation against this ticker writes nothing to `_hot.md` while reporting success. Running #35 in scoped mode catches this within one weekly check rather than one monthly check. The check is cheap (single file read + section grep) — no scoped-mode performance penalty.

---

Perform a comprehensive vault health audit:

## Structural Checks

1. **Orphaned research notes** — Find Research/ notes not linked from ANY Thesis note's adjacency (Related Research section, Log entry wikilinks, or body references).
   - Method: List all Research/ files, then grep `Theses/` for references to each. This is thesis-centric matching the authoritative definition used by `/graph` Step 5 (which populates `_graph.md`'s Orphan Research Notes section).
   - **Definition contract**: The orphan predicate is "not linked from any thesis" — NOT "not linked from any thesis OR sector note." Sector-only-linked research notes are still orphans under this definition. This matches `/graph`'s thesis-centric adjacency model. Sector note references are advisory context; they do not rescue a note from orphan status.
   - Rationale: `_graph.md` is the authoritative dependency map, and its orphan list is the source of truth for cleanup decisions. Divergent definitions would produce conflicting signals between `/lint` and `/graph`, leading users to chase ghost orphans (notes rescued by sector-only references in one view but flagged in another).

2. **Missing MOC entries** — Find Theses/ notes not listed in their Sector Note
   - Method: For each thesis with `status: active` or `status: monitoring`, check its `sector:` frontmatter, verify it appears in that Sector Note
   - Exclude `status: draft` theses — these are intentionally omitted from sector notes until promotion via `/status draft→active`

3. **Broken wikilinks** — Find [[links]] that point to non-existent notes
   - Method: Extract all [[...]] patterns, verify each target file exists

4. **Missing frontmatter** — Notes without required fields:
   - All notes: date, tags
   - Thesis notes: status, conviction, sector, ticker
   - Research notes: source, source_type

5. **Empty critical sections** — Thesis notes with:
   - Empty Key Metrics table
   - Empty Bull Case or Bear Case
   - No Log entries
   - Empty Non-consensus Insights

28. **Partial write detection** — Find notes with indicators of a failed mid-edit (truncated section from a skill that crashed mid-write)
    - Method: For each `##` section in Theses/ and Sectors/ notes, check for:
      - Unclosed formatting markers: unmatched `**` or `*` within a section (odd count = unclosed)
      - Incomplete table rows: line starting with `|` but not ending with `|`
      - Trailing fragment: section's last non-empty line ends with a conjunction (`and`, `but`, `or`), preposition (`of`, `in`, `for`, `to`, `with`, `from`, `by`), comma, or opening bracket
      - Incomplete `/deepen` operation: Log entry starting with `"Deepening"` instead of `"Deepened"` — indicates `/deepen` wrote the pre-announcement Log but failed before finalizing (section may or may not have been rewritten; check snapshot). **Self-corrected variant**: if a `"↳ CORRECTION: Deepened"` entry exists immediately after the `"Deepening"` entry, the skill's retry mechanism fired and the audit trail is complete — downgrade to Nice to Have (cosmetic residue, not data loss)
    - Exclusions: `## Log` sections (entries are intentionally terse), frontmatter, fenced code blocks (` ``` `). **Exception**: Log sections ARE scanned for the `"Deepening"` prefix check above
    - Impact: A truncated section indicates a skill (`/compare`, `/sync`, `/deepen`) failed mid-write. A pre-edit snapshot should exist in `_Archive/Snapshots/` — report the likely matching snapshot if one exists (match by file + nearest `snapshot_date`)
    - Severity: Important — manual review or `/rollback` needed. **Exception**: self-corrected `/deepen` entries (see above) are Nice to Have

## Freshness Checks

6. **Stale active theses** — status: active but no Log entry in >30 days
7. **Old financial data** — Key Metrics that reference data older than 6 months
8. **Inactive research** — Tickers with no new Research/ note in >60 days

25. **Pending sync detection** — Files modified since last `/sync` run
    - Method: Check if `.last_sync` exists, then `find Research/ Theses/ Macro/ Sectors/ -newer .last_sync -name '*.md'`
    - `.last_sync` missing: Important — no sync baseline exists, run `/sync`
    - Modified files found: Important — `/ingest`, `/thesis`, or manual edits haven't been propagated. List files and recommend `/sync`
    - No modified files: Pass

## Connection Checks

9. **Unlinked mentions** — Notes mentioning the same ticker/topic but not linked
10. **Disconnected macro notes** — Macro/ notes not referenced from any Thesis
11. **Missing thesis candidates** — Tickers mentioned in 3+ Research notes without a Thesis note

## Analytical Checks

12. **Conviction-evidence mismatch** — Flag theses where:
    - conviction: high but fewer than 3 research notes support it (over-conviction)
    - conviction: low but 5+ research notes exist with supporting evidence (under-conviction)
    - Method: Count Research/ notes linked from each thesis (Related Research + Log mentions), compare against conviction level

13. **Bull/Bear asymmetry** — Flag thesis notes where:
    - The Bull Case section is more than 3x longer than the Bear Case (or vice versa)
    - This suggests biased analysis — a good thesis should have roughly balanced coverage
    - Method: Compare word count of Bull Case vs Bear Case sections

14. **Template drift** — Compare each thesis against the Thesis Template structure and flag missing sections:
    - Priority flags: missing Key Non-consensus Insights, missing Outstanding Questions (CLAUDE.md calls these the two most important sections), missing Conviction Triggers
    - Secondary flags: missing Business Model & Product Description, missing Industry Context, missing Catalysts, missing Risks
    - Method: Check for the presence of each ## heading from the template

15. **Verbose Log entries** — Flag thesis Log entries exceeding 2 lines (max 2 per CLAUDE.md Writing Standards)
    - Method: Parse Log sections, check line count between consecutive ### date headers

## Snapshot Hygiene

16. **Stale snapshots** — Find snapshots in `_Archive/Snapshots/` older than 180 days
    - Method: Parse `snapshot_date:` from each snapshot's frontmatter, flag any where today minus snapshot_date > 180 days
    - Action: List stale snapshots in the report under "Nice to Have" with recommendation to delete
    - Do NOT auto-delete — list them for user confirmation
    - Report format: `- [ ] Stale snapshot: [[_Archive/Snapshots/TICKER - Company (pre-sync DATE)]] — [age] days old`

## Graph Health

These checks validate `_graph.md` — the pre-computed dependency map that `/sync` relies on for fast, targeted propagation. A stale or inaccurate graph means `/sync` silently misses updates.

17. **Graph existence** — Verify `_graph.md` exists at vault root
    - If missing: Important — `/sync` falls back to file-traversal resolution (slower, less precise). Fix: run `/graph`

18. **Graph staleness** — Check `date:` in `_graph.md` frontmatter
    - **Auto-fixable by `/graph last`** — these are not errors per se; the new workflow expects `/graph last` after every `/sync`
    - Pass: ≤24 hours old
    - Nice to Have: >24 hours but ≤7 days. Fix: run `/graph last`
    - Important: >7 days. Fix: run `/graph` (full rebuild) or `/graph [N]` for catch-up
    - Critical: >30 days. Fix: run `/graph`

19. **Missing thesis entries** — Find thesis notes in `Theses/` with no entry in the Thesis Adjacency Index
    - Method: List all `Theses/*.md` files, check each has a matching `### TICKER - Name` heading in `_graph.md`
    - Impact: `/sync` will never propagate TO these theses in graph-assisted mode. Fix: run `/graph`

20. **Ghost thesis entries** — Find adjacency entries for theses that no longer exist in `Theses/`
    - Method: Extract all `### TICKER - Name` headings from the adjacency index, verify each file exists in `Theses/`
    - Impact: `/sync` wastes time trying to read non-existent files. Fix: run `/graph`

21. **Broken graph edges** — Verify wikilinks listed in adjacency entries point to files that exist
    - Method: For each thesis entry, check that sector, macro, cross-thesis, and research wikilinks resolve to real files
    - Priority: Cross-thesis and research links (these drive propagation paths)

22. **Stale frontmatter counts** — Compare `_graph.md` frontmatter stats against actual vault file counts
    - `theses:` vs count of `Theses/*.md` files
    - `sectors:` vs count of `Sectors/*.md` files
    - `macro:` vs count of `Macro/*.md` files
    - Flag if any count is off by more than 2

23. **Reverse index consistency** — Verify forward and reverse indexes agree
    - Forward → reverse: For each thesis listing a macro note in its adjacency entry, verify that macro note's reverse index row includes the thesis (and same for sectors)
    - Reverse → forward: For each thesis listed in a reverse index row, verify the thesis's adjacency entry references that macro/sector note
    - Inconsistency means `/sync` will propagate in one direction but miss the other. Fix: run `/graph`

24. **Orphan list accuracy** — Cross-check the `## Orphan Research Notes` section
    - **False orphans**: Notes listed as orphans that ARE now linked from a thesis → flag for removal
    - **Missing orphans**: Research notes not linked from any thesis but absent from orphan list → flag for addition
    - Method: For each listed orphan, grep `Theses/` for references. For unlisted research notes, verify they are linked from at least one thesis adjacency entry

26. **Edge count accuracy** — Verify `edges:` frontmatter in `_graph.md` matches actual edge count
    - Method: Count all `[[...]]` wikilinks within the Thesis Adjacency Index section (each wikilink = one edge). Compare to `edges:` frontmatter value
    - Drift >25%: Important — graph metadata unreliable, `/sync` validation checks may give false results. Fix: run `/graph`
    - Drift 10–25%: Nice to Have — minor accumulation from incremental updates. Fix: run `/graph`
    - Drift <10%: Pass

## Utility File Health

27. **Catalyst calendar staleness** — Check `_catalyst.md` freshness
    - If `_catalyst.md` does not exist: Nice to Have — no catalyst calendar generated. Fix: run `/catalyst`
    - If `_catalyst.md` exists: check `date:` in frontmatter
      - >14 days old: Important — catalyst calendar likely contains expired events and missing new ones. Fix: run `/catalyst`
      - 7–14 days old: Nice to Have — catalyst calendar aging, consider `/catalyst` refresh
      - ≤7 days: Pass
    - Also flag any thesis `## Catalysts` section containing only dates that have passed — these theses have no forward catalyst (overlaps with #5 but catches non-empty-yet-expired sections)

35. **`_hot.md` schema integrity** — Verify `_hot.md` has the canonical section layout that skills depend on. Skills like `/sync`, `/status`, `/thesis`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/deepen`, `/prune`, `/rollback`, and `/catalyst` all Edit specific sections by heading match. A missing heading causes those Edits to silently miss, leaving session-context updates unpersisted.
    - **Precondition**: If `_hot.md` does not exist, report: Nice to Have — `ℹ️ _hot.md absent. First `/sync` will auto-create per CLAUDE.md Rule #9.` Then stop this check.
    - **Frontmatter checks**:
      - `date:` field present and in `YYYY-MM-DD` format → Important if malformed or missing.
      - `tags:` field includes `meta` and `hot-cache` tokens → Nice to Have if missing or different.
    - **Required `##` sections** (exact heading strings, case-sensitive):
      - `## Active Research Thread`
      - `## Latest Sync`
      - `## Sync Archive`
      - `## Recent Conviction Changes`
      - `## Open Questions`
      - `## Portfolio Snapshot`
    - For each missing section: Important — `⚠️ _hot.md missing required section "## [Section Name]". Skills that Edit this section will silently no-op. Fix: add the heading with an empty body (`- _pending_` under it), or delete _hot.md and let the next /sync auto-create the full schema.`
    - **Order check** (Nice to Have): canonical order is the list above. If sections are present but out of order, report: `🔖 _hot.md sections present but out of canonical order. Skills tolerate reordering; consider restoring canonical order for readability.`
    - **Word-cap check**: if total word count > 2,000, report: Important — `⚠️ _hot.md exceeds 2,000-word cap ([N] words). Skills should auto-prune on next update; manual `/sync` or `/status` will truncate. If persists across multiple runs, the word-cap logic may have drifted — investigate.`
    - **Runs in BOTH full and scoped modes** — `_hot.md` schema integrity is a vault-global concern that affects every skill writing to `_hot.md` for the scoped ticker. Single-file read + grep cost is negligible.

36. **Prune batch-manifest state** — Scan `_Archive/Snapshots/` for `_prune-manifest*.md` files. These are crash-recovery artifacts from `/prune` Stage 1.5; their presence indicates a prune operation state.
    - **Precondition**: list `_Archive/Snapshots/_prune-manifest*.md` via Glob. If none: Pass (no manifest, clean state).
    - For each manifest found, read frontmatter and classify by `status:`:
      - **`status: in-progress`** → Critical — `❌ In-progress /prune manifest: [[_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS)]]. Two possible causes — verify which one BEFORE taking recovery action:`
        - `(1) Genuinely failed /prune — the batch did not complete. Recovery: /rollback [any ticker in the manifest body's "Intended Closures" or "Intended Upgrades" list] → select (pre-prune) snapshot → cascade (a) to undo all completed actions. Then delete this manifest and re-run /prune if desired.`
        - `(2) Successful /prune with stuck status-flip — all closures/upgrades/sector updates succeeded, but /prune Stage 5 could not flip the manifest to status: completed. Recovery: DO NOT /rollback (it would destroy valid work). Instead, verify success by spot-checking: (a) does _hot.md's "Recent Conviction Changes" section contain the closures from the manifest's Intended Closures list? (b) do the Intended-Closures theses live in _Archive/ with status: closed frontmatter? If both yes → prune succeeded; manually edit the manifest to set status: completed and then rm it.`
        - `To distinguish the two causes quickly: if /prune's final report mentioned "flip verification failed" then it is cause (2); otherwise cause (1) is more likely. The safe default when uncertain is to inspect the manifest body + target theses before running /rollback.`
      - **`status: completed`** → Nice to Have — `🧹 Stale completed manifest: [[_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS)]]. /prune finished successfully but Stage 5 cleanup did not delete this breadcrumb. Safe to delete manually: rm "_Archive/Snapshots/_prune-manifest (prune-YYYY-MM-DD-HHMMSS).md". /clean also surfaces these.`
      - **Missing or malformed `status:`** → Important — `⚠️ Prune manifest [filename] has no parseable `status:` frontmatter. Legacy format or corruption. Inspect manually.`
    - Do NOT delete manifests from `/lint` — lint is read-only. Report only.
    - **Vault-wide only** (skipped in scoped mode).

## Cross-Skill Contract Health

29. **Log-prefix registry alignment** — Verify `.claude/skills/_shared/log-prefixes.md` is in sync with producer skills and actual vault state. This is the enforcement mechanism for the cross-skill Log-prefix contract (defined in the registry itself; consumed by `/sync` Step 3e Log Format Contract, `/lint` #28, and several audit-only contexts).
    - **Precondition**: read `.claude/skills/_shared/log-prefixes.md`. If it does not exist: Critical — the contract registry is missing. Fix: restore from git history or recreate per Fix #8 spec.
    - For each prefix entry in the registry, perform THREE checks:
      a. **Producer alignment** — grep the producer skill's `SKILL.md` for the exact prefix string (case-sensitive). If not found: Critical — `❌ Producer drift: /skill [skill-name] no longer emits prefix "[prefix]" per registry.` This indicates a skill was edited but the registry wasn't, or vice versa.
      b. **Consumer alignment** — for each listed consumer, grep its `SKILL.md` for the exact prefix string. If not found: Critical — `❌ Consumer drift: /skill [consumer] no longer searches for prefix "[prefix]" per registry.`
      c. **Vault presence** — grep `Theses/**/*.md` for the prefix as a line-prefix match (after `- ` bullet marker). If NOT found in any thesis AND the producer's `emits_when` condition indicates a common path ("always", "every successful rollback", etc.): Important — `⚠️ Prefix "[prefix]" absent from Theses/ Log sections despite producer /skill [X] claiming to emit it. Producer may be silently broken, OR no triggering events have occurred yet.` (Note: this is an Important check, not Critical — a vault may legitimately have no rollbacks or prune upgrades yet.)
    - **Reverse check** — for each SKILL.md file in `.claude/skills/`, extract all quoted prefix strings from "Drift coupling" blocks or Log format code fences. For any such string NOT in the registry: Important — `⚠️ Orphan coupling: /skill [X] references prefix "[string]" not in _shared/log-prefixes.md. Either add it to the registry or remove the reference.`
    - **Registry freshness** — check the registry's `last_reviewed:` frontmatter. If >90 days old: Nice to Have — `🔖 Log-prefix registry last reviewed [N] days ago. Consider re-validating the coupling contract.`

30. **Sector resolution coverage** — Verify every thesis's `sector:` frontmatter resolves to a sector note via the canonical procedure in `.claude/skills/_shared/sector-resolution.md`. This is the enforcement mechanism for the cross-skill sector resolution contract (consumed by `/status`, `/thesis`, `/compare`, `/prune`, `/rename`).
    - **Precondition**: read `.claude/skills/_shared/sector-resolution.md`. If it does not exist: Critical — the contract is missing. Fix: restore from git history or recreate per the contract spec.
    - **Scoped mode** (`/lint TICKER`): run resolution for one thesis only.
    - **Full mode**: for every `Theses/*.md` with a `sector:` frontmatter value, execute the contract's 5-step procedure (exact → normalized → substring → user prompt would-fire → none). Record `match_confidence` per thesis.
    - Severity classification:
      - `match_confidence: none` → **Important**: `⚠️ Sector resolution failed for [TICKER] — sector "[value]" matches no Sectors/*.md by exact, normalized, or substring. Skills /status, /thesis, /compare, /prune, /rename will silently skip sector updates for this thesis. Fix: create Sectors/[value].md OR correct the thesis frontmatter to match an existing sector note.`
      - `match_confidence: substring` → **Nice to Have**: `🔖 Sector resolved via substring for [TICKER]: thesis sector "[value]" → "[matched]" (edit distance [N]). Standardize one of them to upgrade to exact match.`
      - `match_confidence: normalized` → **Nice to Have**: `🔖 Sector resolved via case/whitespace normalization for [TICKER]: thesis sector "[value]" → "[matched]". Standardize for exact match.`
      - `match_confidence: exact` → Pass (no report line).
    - **Aggregate report** in full mode: include a stats line: `Sector resolution: [exact_count] exact, [normalized_count] normalized, [substring_count] substring, [none_count] none.`

32. **Orphaned ticker references in research** — Find research notes whose `ticker:` frontmatter or ticker-shaped tags do not match any file in `Theses/`. These notes were created before a thesis existed (or for a thesis that was archived) and have no propagation target.
    - Method: For each `Research/*.md` with a `ticker:` frontmatter value, check `Theses/[ticker] - *.md` exists. Also check `tags:` for ticker-shaped tokens (all-uppercase, 1-5 chars) without matching `Theses/` files.
    - Severity: Important — `/sync` cannot propagate these notes to any thesis. Their content is invisible to the propagation pipeline.
    - Fix options: (a) `/thesis [TICKER]` to create the missing thesis, then `/sync [TICKER]` to integrate the orphaned research; (b) edit the research note's `ticker:` frontmatter to point to an existing thesis; (c) accept as orphan (no action — note remains as standalone research).
    - This check covers what `/sync` Step 1 Fallback 1 used to self-heal silently. Surfacing here lets the user decide rather than letting orphans accumulate undetected.

33. **Closed-thesis files in `Theses/`** — Find files in `Theses/` with `status: closed` frontmatter. These are failed archive moves from `/status active→closed` or `/prune` Stage 2 — the metadata flipped to closed but the `mv` to `_Archive/` didn't complete.
    - Method: Grep `Theses/*.md` for `status: closed` in frontmatter.
    - Severity: Important — every skill that reads thesis files must handle this state defensively. Subsequent `/sync` runs and `/graph last` skip these files with warnings.
    - Fix options: (a) Complete the archive: `mv "Theses/[file]" "_Archive/[file]"` then `/graph last`; (b) Reopen the thesis: `/status TICKER status closed→active [rationale]` then `/sync TICKER`.
    - This check covers what 5 separate gates in `/sync` used to handle inline. Surfacing here makes the failed-archive-move state visible rather than silently propagating warnings every sync.

37. **Incomplete-rename marker** — Detect `.rename_incomplete` at vault root. Written by `/rename` Step 5.5 when wikilink Edits failed mid-run; signals that the renamed thesis has stale inbound wikilinks pointing to its prior path.
    - **Precondition**: check whether `.rename_incomplete` exists at vault root. If absent → Pass (no incomplete rename in flight).
    - For the marker file, read frontmatter (`type: rename-incomplete`, `ticker:`, `old_name:`, `new_name:`, `batch:`, `date:`) and the body's "Failed files" list.
    - **Severity**: Important — `❌ Incomplete /rename in progress: [[.rename_incomplete]]. /rename TICKER "[new_name]" completed the filename move but [N] inbound wikilink Edit(s) failed. Affected files retain stale wikilinks to the now-missing path [[Theses/TICKER - [old_name]]]. Recovery: re-run /rename TICKER "[new_name]" — the skill detects this marker (Step 1.3 exception), skips the already-completed mv, and retries failed Edits. The marker auto-deletes when all repairs succeed. Manual repair option: edit the listed files and replace [old_name] with [new_name] across the 7 wikilink patterns documented in /rename Step 5.`
    - **Stale-marker check**: if the marker's `date:` is >7 days old, additionally flag: `⚠️ Marker is [N] days old — repair has been deferred. The longer it persists, the more likely the failed files have drifted further (other edits, additional wikilinks). Re-run /rename promptly.`
    - **Per-file existence check**: for each path in the "Failed files" list, verify the file still exists. If a listed path no longer exists (deleted, archived, renamed), append: `ℹ️ Listed failed file [path] no longer exists on disk — was it manually fixed/removed? Marker may need manual edit to drop the stale entry.`
    - **Scope behavior**: in scoped mode `/lint TICKER`, run this check only if the marker's `ticker:` matches the scoped TICKER. In full mode, always run.
    - Do NOT delete the marker from `/lint` — `/lint` is read-only. The marker's lifecycle is owned by `/rename`.

34. **Sector frontmatter standardization** — Cross-check thesis `sector:` frontmatter values against canonical sector note names to surface divergence patterns the user should standardize.
    - **Vault-wide only** (skipped in scoped mode).
    - For each unique `sector:` frontmatter value across `Theses/*.md`, count how many theses use it.
    - For each unique value, check whether it matches at least one `Sectors/*.md` filename (without `.md`) or `sector:` frontmatter EXACTLY (case-sensitive, whitespace-exact).
    - Report:
      - **Important**: `⚠️ [N] thesis files use sector value "[value]" which has no exact match in Sectors/. Closest match: "[closest]" (edit distance [M]). Theses: [list].` — these will silently rely on normalized or substring resolution by all consumer skills.
      - **Nice to Have**: `🔖 [N] thesis files use sector value "[value]" — exact match exists, no action needed (informational).` (Only emit if the user wants the inventory; suppress by default.)
    - **Stats line**: `Sector taxonomy: [unique_count] distinct sector values across [thesis_count] theses; [exact_value_count] match Sectors/ exactly, [divergent_value_count] require normalization or substring resolution.`

## Output Format

Report as a prioritized checklist:

### Critical (breaks research quality)
- [ ] [Issue] — [File path] — [Specific problem]

### Important (gaps in coverage)
- [ ] [Issue] — [File path] — [Specific problem]

### Nice to Have (optimization)
- [ ] [Issue] — [File path] — [Specific problem]

### Stats
- Total notes: X
- Thesis notes: X (active: X, draft: X, monitoring: X)
- Research notes: X
- Average thesis age: X days since last Log entry
- Orphaned notes: X
- Broken links: X
