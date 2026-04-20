---
name: lint
description: Run health checks on the vault for inconsistencies, stale data, orphaned notes, and missing connections. Use periodically or when user says "lint", "health check", or "audit".
model: opus
effort: max
context: fork
agent: general-purpose
allowed-tools: Read Grep Glob Bash(find * wc * date * grep * sed * cat * printf * rm * mkdir * ls *)
---

Comprehensive vault health audit. Read-only — never deletes, never edits. Report only.

Design rationale in `.claude/skills/lint/RATIONALE.md` (§N.M anchors).

## Step 0: Pre-flight (MANDATORY — runs before Scope Resolution)

### 0.1: Acquire vault lock (mode-dependent)

Per `.claude/skills/_shared/preflight.md` Procedure 1. Even though `/lint` never writes to vault content files, a lock is still acquired so that concurrent writers (e.g., a mid-flip `/sync` manifest, an in-flight `/prune` sector edit) do not cause `/lint` to see transient inconsistent state and raise false-positive Important / Critical flags.

- **Full mode** (`/lint` with no arguments): acquire a `vault-wide` scope lock. Timeout budget: 5 minutes. Full mode reads every `Theses/*.md`, `Sectors/*.md`, `Macro/*.md`, `Research/*.md`, `_graph.md`, `_hot.md`, `_catalyst.md`, every `_Archive/Snapshots/_*-manifest*.md`, plus the `.vault-lock*`, `.rename_incomplete.*`, `.graph_invalidations`, `.sync_all_fresh`, `.archive_ticker_registry.md` state markers. The read window is long enough that a concurrent writer mid-flip could produce a false `in-progress` manifest flag. Vault-wide scope serializes against writers.
- **Scoped mode** (`/lint TICKER`): acquire a `.vault-lock.readonly` lock. Timeout budget: 2 minutes. Scoped mode's read set is small (one thesis + its sector note + `_hot.md` + any active `.rename_incomplete.TICKER` marker); read-only scope lets two `/lint TICKER` invocations against different tickers run in parallel while still blocking vault-wide writers from producing mid-read state transitions.

Capture the token emitted at Step 0.1. Every subsequent Bash block in the skill verifies ownership (Procedure 1.5) against the captured token before issuing any Read / Grep / Glob. Release the lock explicitly in the final reporting Bash block via `rm -f "$LOCK_FILE"`. On token mismatch (`LOCK_LOST` / `LOCK_STOLEN`), abort and report the partial check results captured so far.

### 0.2: No rename-marker check

`/lint` is a read-only diagnostic skill and is an explicit exception in `.claude/skills/_shared/preflight.md` §2.1. `/lint #37` surfaces active `.rename_incomplete.*` markers as its own check output — hard-blocking on the marker would defeat lint's purpose (surfacing repair-state issues is exactly what a user running lint wants to see).

---

## Scope Resolution

Parse `$ARGUMENTS`:

- **Ticker** (e.g., `NVDA`): Scoped audit — run only checks relevant to that thesis and its graph adjacencies.
- **No arguments / empty**: Full vault audit — run all checks.

**Scoped checks** (run for `/lint TICKER`):
#2, #4, #5, #6, #7, #8, #12, #13, #14, #15, #19, #21, #28 (for this thesis + sector), #30 (for this thesis), **#35 always** (§1.1 — catches `_hot.md` schema drift within one weekly check), **#37 if `.rename_incomplete.TICKER` exists** (§1.3), **#42 always** (§1.2 — truncation markers).

**Vault-wide only** (skipped in scoped mode — §1.4):
#1, #3, #9, #10, #11, #16, #17, #18, #20, #22, #23, #24, #25, #26, #27, #29, #32, #33, #34, #36, #38, #39, #41, #43, #44, #45, #46, #47, #48, #49.

---

## Structural Checks

1. **Orphaned research notes** — Research/ notes not linked from ANY Thesis adjacency (Related Research, Log wikilinks, body references).
   - Method: list `Research/*.md`, grep `Theses/` for each.
   - **Definition contract** (§2.1): orphan = "not linked from any thesis" (NOT "not linked from any thesis OR sector"). Thesis-centric to match `/graph` Step 5.

2. **Missing MOC entries** — Theses/ notes not listed in their Sector Note.
   - Method: for each thesis with `status: active` or `status: monitoring`, check `sector:` frontmatter, verify appears in that Sector.
   - Exclude `status: draft` (intentionally omitted until `/status draft→active`).

3. **Broken wikilinks** — `[[links]]` pointing to non-existent notes.
   - Method: extract all `[[...]]`, verify each target file exists.

4. **Missing frontmatter** — Notes without required fields:
   - All notes: `date`, `tags`
   - Thesis notes: `status`, `conviction`, `sector`, `ticker`
   - Research notes: `source`, `source_type`

5. **Empty critical sections** — Thesis notes with:
   - Empty Key Metrics table
   - Empty Bull Case or Bear Case
   - No Log entries
   - Empty Non-consensus Insights

28. **Partial write detection** — Notes with indicators of a failed mid-edit.
    - Method: for each `##` section in Theses/ and Sectors/, check:
      - Unclosed formatting: unmatched `**` or `*` (odd count) within a section
      - Incomplete table rows: line starting `|` but not ending `|`
      - Trailing fragment: section ends with conjunction (`and`, `but`, `or`), preposition (`of`, `in`, `for`, `to`, `with`, `from`, `by`), comma, or opening bracket
      - Incomplete `/deepen`: Log entry starting `"Deepening"` instead of `"Deepened"`. **Self-corrected variant** (§2.3): `"↳ CORRECTION: Deepened"` immediately after → downgrade to Nice to Have (audit trail complete, cosmetic residue only)
    - Exclusions: `## Log` sections (except the `"Deepening"` prefix check), frontmatter, fenced code blocks.
    - Severity: Important. A pre-edit snapshot should exist in `_Archive/Snapshots/` — report the likely matching snapshot if one exists.

## Freshness Checks

6. **Stale active theses** — `status: active` but no Log entry in >30 days.
7. **Old financial data** — Key Metrics referencing data older than 6 months.
8. **Inactive research** — Tickers with no new Research/ note in >60 days.

25. **Pending sync detection** — Files modified since last `/sync`.
    - Method: `.last_sync` exists, then `find Research/ Theses/ Macro/ Sectors/ -newer .last_sync -name '*.md'`.
    - `.last_sync` missing → Important — no sync baseline, run `/sync`.
    - Modified files found → Important — list + recommend `/sync`.
    - No modified files → Pass.

## Connection Checks

9. **Unlinked mentions** — Notes mentioning the same ticker/topic but not linked.
10. **Disconnected macro notes** — Macro/ notes not referenced from any Thesis.
11. **Missing thesis candidates** — Tickers in 3+ Research notes without a Thesis note.

## Analytical Checks

12. **Conviction-evidence mismatch**:
    - `conviction: high` but <3 research notes supporting it (over-conviction)
    - `conviction: low` but 5+ research notes exist with supporting evidence (under-conviction)
    - Method: count Research/ notes linked from each thesis (Related Research + Log mentions), compare against conviction level.

13. **Bull/Bear asymmetry** — Bull Case >3× longer than Bear Case (or vice versa). Suggests biased analysis.
    - Method: word count per section.

14. **Template drift** — Compare each thesis against Thesis Template structure.
    - Priority flags: missing Key Non-consensus Insights, Outstanding Questions, Conviction Triggers.
    - Secondary: missing Business Model, Industry Context, Catalysts, Risks.
    - Method: check presence of each `##` heading from template.

15. **Verbose Log entries** — Thesis Log entries exceeding 2 lines (max 2 per CLAUDE.md Writing Standards).
    - Method: parse Log sections, check line count between consecutive `###` date headers.

## Snapshot Hygiene

16. **Stale snapshots** — `_Archive/Snapshots/` entries older than 180 days.
    - Method: parse `snapshot_date:` from frontmatter; flag if `today - snapshot_date > 180 days`.
    - Action: list under "Nice to Have". Do NOT auto-delete.
    - Format: `- [ ] Stale snapshot: [[_Archive/Snapshots/TICKER - Company (pre-sync DATE)]] — [age] days old`

## Graph Health

17. **Graph existence** — verify `_graph.md` at vault root.
    - Missing → Important. Fix: run `/graph`.

18. **Graph staleness** — check `last_graph_write:` (preferred) or `date:` (legacy fallback).
    - Preferred: ISO precision from `last_graph_write:` (§2.2).
    - Legacy fallback: `date:` with implicit 00:00:00 UTC — may over-report age by up to 24h. Advisory: `ℹ️ _graph.md lacks last_graph_write: — next /graph run will upgrade frontmatter to ISO precision.`
    - Thresholds: ≤24h Pass; 24h-7d Nice to Have (run `/graph last`); >7d Important (run `/graph`); >30d Critical.

19. **Missing thesis entries** — `Theses/*.md` files with no entry in `_graph.md` Adjacency Index.
    - Method: list `Theses/*.md`, check each has matching `### TICKER - Name` heading in `_graph.md`.
    - Impact: `/sync` won't propagate TO these in graph-assisted mode. Fix: `/graph`.

20. **Ghost thesis entries** — Adjacency entries for theses not in `Theses/`.
    - Method: extract `### TICKER - Name` headings, verify each file exists.
    - Impact: `/sync` wastes time on non-existent files. Fix: `/graph`.

21. **Broken graph edges** — Wikilinks in adjacency entries pointing to missing files.
    - Method: for each thesis entry, verify sector, macro, cross-thesis, research wikilinks resolve.
    - Priority: cross-thesis and research links.

22. **Stale frontmatter counts** — `_graph.md` frontmatter stats vs actual file counts.
    - `theses:` vs count of `Theses/*.md`; `sectors:` vs `Sectors/*.md`; `macro:` vs `Macro/*.md`.
    - Flag if off by >2.

23. **Reverse index consistency** — Forward and reverse indexes agree.
    - Forward→reverse: each thesis listing a macro note, verify that macro's reverse-index row includes the thesis (same for sectors).
    - Reverse→forward: each thesis in a reverse-index row, verify its adjacency references that macro/sector.
    - Fix: `/graph`.

24. **Orphan list accuracy** — Cross-check `## Orphan Research Notes` section.
    - **False orphans**: listed as orphan but IS now linked from a thesis → flag for removal.
    - **Missing orphans**: not linked from any thesis but absent from orphan list → flag for addition.
    - Method: grep `Theses/` for each listed orphan; verify unlisted research notes are linked.

26. **Edge count accuracy** — `edges:` frontmatter vs actual count.
    - Method: count `[[...]]` wikilinks in Thesis Adjacency Index section. Compare to `edges:`.
    - Drift >25% → Important; 10-25% → Nice to Have; <10% → Pass.

## Utility File Health

27. **Catalyst calendar staleness** — `_catalyst.md` freshness.
    - Missing → Nice to Have (run `/catalyst`).
    - >14 days → Important; 7-14 days → Nice to Have; ≤7 days → Pass.
    - Also flag thesis `## Catalysts` with only past-dated entries.

35. **`_hot.md` schema integrity** — Verify canonical section layout (§5).
    - **Precondition**: `_hot.md` missing → Nice to Have `ℹ️ _hot.md absent. First /sync will auto-create per CLAUDE.md Rule #9.` Stop.
    - **Frontmatter**: `date:` present + `YYYY-MM-DD` format → Important if malformed/missing. `tags:` includes `meta` + `hot-cache` → Nice to Have if missing.
    - **Required `##` sections** (exact, case-sensitive):
      - `## Active Research Thread`
      - `## Latest Sync`
      - `## Sync Archive`
      - `## Recent Conviction Changes`
      - `## Open Questions`
      - `## Portfolio Snapshot`
    - Missing section → Important: `⚠️ _hot.md missing required section "## [Section Name]". Skills that Edit this section will silently no-op. Fix: add the heading with an empty body (- _pending_), or delete _hot.md and let the next /sync auto-create the full schema.`
    - **Order check** (Nice to Have): canonical order = list above. Reordered → `🔖 _hot.md sections present but out of canonical order. Skills tolerate reordering; consider restoring for readability.`
    - **Word-cap check**: total word count > 4,000 (soft cap per `_shared/hot-md-contract.md`) → Nice to Have: `🔖 _hot.md over soft cap ([N] words / 4,000). Skills auto-prune on next update — no action unless persistent across multiple runs.` Total word count > 5,000 (hard cap) → Important: `⚠️ _hot.md exceeds 5,000-word hard cap ([N] words). Skills abort _hot.md updates at this size. Manual cleanup required: remove outdated Sync Archive entries.`
    - **Runs in BOTH full and scoped modes** (§1.1).

### Manifest-aging shared pattern (applies to #36, #41, #45, #47, #48, #49)

Common skeleton. Each check below lists only what differs from this pattern.

- **Vault-wide only.** Read-only — never delete manifests.
- **Precondition**: no matching manifests → Pass silently.
- **Parse frontmatter** per check-specific key list.
- **Severity by `status:`**:
  - `in-progress` → Important (or Critical per check); emit check-specific recovery guidance.
  - `completed` (from `completed_date:`): ≤90d Pass; 90–180d Nice to Have (`🔖 Stale … manifest: [[…]] is [N] days old.`); >180d Important (`⚠️ Very stale … manifest: [[…]]. Safe to delete.`).
  - Missing/malformed `status:` → Important (`⚠️ … manifest [filename] has no parseable status. Legacy format or corruption. Inspect manually.`).

Per-check entries below specify only: (1) manifest filename glob, (2) frontmatter keys beyond the common set, (3) in-progress recovery text, (4) any deviation from the default age ladder.

36. **Prune batch-manifest state** — Scan `_Archive/Snapshots/_prune-manifest*.md`. Crash-recovery artifacts from `/prune` Stage 1.5.
    - **Precondition**: none → Pass.
    - For each manifest, classify by `status:`:
      - **`in-progress`** → Critical: `❌ In-progress /prune manifest: [[...]]. Two possible causes — verify BEFORE recovery:`
        - `(1) Genuinely failed /prune — batch did not complete. Recovery: /rollback [any ticker in manifest body] → select (pre-prune) snapshot → cascade (a) to undo. Then delete manifest and re-run /prune.`
        - `(2) Successful /prune with stuck flip — all closures/upgrades/sector updates succeeded, Stage 5 flip silently missed. Recovery: DO NOT /rollback. Spot-check: (a) _hot.md Recent Conviction Changes contains the closures? (b) Intended-Closures theses live in _Archive/ with status: closed? If both yes → succeeded; manually edit manifest to status: completed and rm it.`
        - `Distinguishing: if /prune's final report mentioned "flip verification failed" → cause (2). Otherwise cause (1) likely. Safe default: inspect manifest body + target theses before /rollback.`
      - **`completed`** (30-day regret window — §4.2):
        - Age ≤30d from `completed_date:` → Pass: `🔒 Completed prune manifest: [[...]] is in 30-day regret-recovery window ([N] days remaining). /rollback cascade can surface Tier B Log entries.`
        - Age >30d → Nice to Have: `🧹 Expired completed prune manifest: [[...]] is [N] days past window. /clean removes on next run.`
        - Missing `completed_date:` → Nice to Have: `🧹 Legacy completed manifest. Flip-verification may have silently missed the timestamp, OR pre-retention-policy prune. /clean treats as eligible.`
      - **Missing/malformed `status:`** → Important: `⚠️ Prune manifest [filename] has no parseable status. Legacy format or corruption. Inspect manually.`
    - Do NOT delete manifests — read-only.
    - **Vault-wide only**.

## Cross-Skill Contract Health

29. **Log-prefix registry alignment** — Verify `.claude/skills/_shared/log-prefixes.md` sync with producers + consumers + vault state (§3).
    - **Precondition**: registry missing → Critical — restore from git or recreate.
    - Per registry entry, three checks:
      - **(a) Producer alignment**: grep producer's `SKILL.md` for exact prefix (case-sensitive). Not found → Critical: `❌ Producer drift: /skill [X] no longer emits prefix "[P]" per registry.`
      - **(b) Consumer alignment**: grep each consumer's `SKILL.md`. Not found → Critical: `❌ Consumer drift: /skill [Y] no longer searches for prefix "[P]" per registry.`
      - **(c) Vault presence**: grep `Theses/**/*.md` for prefix as line-prefix match (after `- `). If absent AND producer's `emits_when` is common path ("always", "every successful rollback"): Important — `⚠️ Prefix "[P]" absent from Theses/ Logs despite producer /skill [X] claiming to emit. Producer may be silently broken, OR no triggering events yet.`
    - **Reverse check**: each SKILL.md's quoted prefix strings (in Drift coupling blocks or Log format fences). Not in registry → Important: `⚠️ Orphan coupling: /skill [X] references prefix "[S]" not in _shared/log-prefixes.md.`
    - **Registry freshness**: `last_reviewed:` >90 days → Nice to Have.

30. **Sector resolution coverage** — Verify every thesis `sector:` resolves via `.claude/skills/_shared/sector-resolution.md` canonical procedure.
    - **Precondition**: contract missing → Critical — restore.
    - **Scoped**: one thesis. **Full**: every `Theses/*.md` with `sector:`.
    - Severity by `match_confidence`:
      - `none` → Important: `⚠️ Sector resolution failed for [TICKER] — sector "[V]" matches no Sectors/*.md. Skills /status, /thesis, /compare, /prune, /rename will silently skip sector updates. Fix: create Sectors/[V].md OR correct thesis frontmatter.`
      - `substring` → Nice to Have: `🔖 Sector resolved via substring for [TICKER]: "[V]" → "[M]" (edit distance [N]). Standardize.`
      - `normalized` → Nice to Have: `🔖 Sector resolved via case/whitespace normalization for [TICKER]. Standardize.`
      - `exact` → Pass.
    - **Aggregate** (full mode): `Sector resolution: [exact] exact, [norm] normalized, [sub] substring, [none] none.`

32. **Orphaned ticker references in research** — Research/ notes whose `ticker:` or ticker-shaped tags don't match any `Theses/`.
    - Method: for each `Research/*.md` with `ticker:`, check `Theses/[ticker] - *.md` exists. Also check `tags:` for ticker-shaped tokens (all-uppercase, 1-5 chars) without matching files.
    - Severity: Important — `/sync` cannot propagate to any thesis; content invisible.
    - Fix options: (a) `/thesis [TICKER]` + `/sync [TICKER]`; (b) edit `ticker:` to existing thesis; (c) accept as orphan.
    - Surfaces what `/sync` Step 1 Fallback 1 used to self-heal silently (§2.4).

33. **Closed-thesis files in `Theses/`** — `Theses/*.md` with `status: closed`. Failed archive moves from `/status active→closed` or `/prune` Stage 2.
    - Method: grep `Theses/*.md` for `status: closed`.
    - Severity: Important — defensive handling in every reader skill.
    - Fix options: (a) `mv "Theses/[file]" "_Archive/[file]"` → `/graph last`; (b) `/status TICKER status closed→active [rationale]` → `/sync TICKER`.
    - Surfaces what 5 separate `/sync` gates used to handle inline (§2.5).

37. **Incomplete-rename markers** — Detect `.rename_incomplete.*` at vault root. Per-ticker files written by `/rename` Step 5.5 on partial failure.
    - **Precondition**: glob `.rename_incomplete.*`. None → Pass.
    - For each marker, read frontmatter (`type: rename-incomplete`, `ticker:`, `old_name:`, `new_name:`, `batch:`, `date:`) + body's "Failed files" list.
    - **Severity per marker**: Important — `❌ Incomplete /rename in progress: [[.rename_incomplete.TICKER]]. /rename TICKER "[new_name]" completed the mv but [N] inbound wikilink Edit(s) failed. Affected files retain stale wikilinks to [[Theses/TICKER - [old_name]]]. Recovery: re-run /rename TICKER "[new_name]" — skill detects marker (Step 1.3 exception), skips mv, retries failed Edits. Auto-deletes on success. Manual option: edit listed files replacing [old_name] with [new_name] across 7 wikilink patterns (per /rename Step 5).`
    - **Stale-marker** (`date:` >7 days old): append `⚠️ Marker is [N] days old — repair deferred. Files likely drifted further. Re-run /rename promptly.`
    - **Per-file existence**: listed path no longer exists → `ℹ️ Listed failed file [path] no longer exists — manually fixed/removed? Marker may need manual edit.`
    - **Scope**: scoped `/lint TICKER` runs only if `.rename_incomplete.TICKER` exists. Full mode processes every marker.
    - **Multi-marker**: `[N] in-flight rename repairs detected: [TICKER1, TICKER2, ...].`

38. **State marker hygiene** — Aging vault-root state markers.
    - **`.sync_all_fresh`** — written by `/sync all` Step 7, consumed by next `/graph`. Expected lifetime <24h.
      - <24h → Pass.
      - 24h-7d → Important: `⚠️ .sync_all_fresh is [N] hours old. /graph hasn't consumed. Run /graph (full rebuild).`
      - >7d → Critical: `❌ .sync_all_fresh is [N] days old. _graph.md significantly stale. Run /graph immediately.`
    - **`.graph_invalidations`** — accumulates closure neighbors, consumed by next `/graph last`. Expected lifetime <24h.
      - <24h → Pass.
      - 24h-7d → Nice to Have: `🔖 .graph_invalidations is [N] hours old. Run /graph last.`
      - >7d → Important: `⚠️ .graph_invalidations is [N] days old. Stale cross-thesis adjacency. Run /graph last.`
    - **Cross-marker** (advisory): both present → `ℹ️ Both markers pending — single /graph (full rebuild) consumes both atomically.`
    - **Vault-wide only**.

39. **`propagated_to:` producer contract enforcement** — Every Research/ note whose `source_type:` mandates the field carries it (§6).
    - **Vault-wide only**. **Spec date**: `2026-04-19`.
    - **Per-source_type mandate**:
      | `source_type:` | Required | Atomicity-skip | Producer |
      |---|---|---|---|
      | `scenario` | `[Major-impact tickers]` | Yes | `/scenario` |
      | `stress-test` | `[TICKER]` | Yes | `/stress-test` |
      | `comparison` | `[TICKER, ...]` | Yes | `/compare` |
      | `synthesis` | `[]` (terminal) | No | `/surface` |
      | `brief` | `[]` (terminal) | No | `/brief` |
      
      Other types: no requirement. `deep-dive` intentionally excluded (§6.2).
    - **Severity rules**:
      - `synthesis` / `brief` missing `[]` → Important: `❌ Producer contract violation: [[Research/note]] has source_type: [X] but missing propagated_to: []. Terminal-skip producers must explicitly emit the empty list — without it, /sync Case 2a writes Log entries to every body-wikilinked thesis (10+), spamming the vault. Fix: add propagated_to: [].`
      - `scenario`/`stress-test`/`comparison` missing AND `date:` ≥ 2026-04-19 → Important: `⚠️ Producer contract may be violated: [[Research/note]] has source_type: [X] but no propagated_to:. Either (a) producer atomicity fired (expected — /sync retries), or (b) producer drift. Verify referenced theses' Logs for today-date entries; if present on all expected tickers, backfill propagated_to: [TICKERS]. If missing, run /sync to trigger retry.`
      - `scenario`/`stress-test`/`comparison` missing AND `date:` <2026-04-19 → Nice to Have: `🔖 Pre-spec note: [[...]] predates contract. Backfill optional.`
      - `synthesis`/`brief` pre-spec → also Important (§6.4 — terminal unconditional).
    - **Aggregate**: `propagated_to: contract — [exact] compliant, [violation] violations (post-spec), [pre_spec] pre-spec gaps.`
    - **Cross-check with #1** (§6.5): note flagged in both → `🚨 Double-flagged orphan: [[...]] — orphan (#1) AND missing propagated_to: (#39). Strongest cleanup candidate.`

41. **Sync manifest aging + status** — `_Archive/Snapshots/_sync-manifest*.md`. Written by `/sync` Step 2.9 (skeleton) → Step 7.5 (flip). See shared pattern above.
    - **Frontmatter keys**: `type: sync-manifest`, `batch`, `status`, `date`, optional `completed_date`.
    - **`in-progress` recovery — three possible causes** (§4.3): `⚠️ In-progress sync manifest: [[...]]. /sync Step 2.9 wrote skeleton but Step 7.5 flip didn't land.`
      - `(1) /sync crashed mid-run — inspect body for landed Tier A + Tier B; use /rollback.`
      - `(2) /sync completed but flip silently missed — check if Tier B Log entries actually exist on listed theses. If yes, manually edit manifest to status: completed + completed_date: today.`
      - `(3) /lint was run DURING an active /sync — ignore; /sync will flip when complete.`
    - **Missing-`status:` addendum**: pre-T2.1 (before 2026-04-19) has no in-progress state; treat as completed for aging.
    - **Age-message addenda** (append to shared ladder messages): 90–180d `(Companion Tier A snapshots may be cleaned per /clean 180-day default.)`; >180d `(Snapshots almost certainly cleaned.)`
    - **Orphan cross-check**: all Tier A snapshots for batch deleted → Nice to Have regardless of age: `🔖 Orphan sync manifest — all Tier A snapshots cleaned. Safe to delete.`

47. **Stress-test manifest aging + status (T3.1)** — `_stress-test-manifest*.md`. See shared pattern above.
    - **Frontmatter keys**: `type: stress-test-manifest`, `batch`, `status`, `ticker`, `date`.
    - **`in-progress` severity — Nice to Have, not Important** (rare — `/stress-test` writes as completed in a single step): `🔖 In-progress stress-test manifest. Unusual. Inspect: if research note + thesis Log entry exist, manually edit to completed. If either missing, partial failure; consider re-running.`

48. **Status manifest aging + status (T2.2)** — `_status-manifest*.md`. Written by `/status` Step 3.0.5 (skeleton) → Step 7.9 (flip). See shared pattern above.
    - **Frontmatter keys**: `type: status-manifest`, `batch`, `status`, `ticker`, `transition_type`, `date`, optional `completed_date`.
    - **`in-progress` recovery**: `⚠️ In-progress /status manifest: [[...]]. Inspect body: (1) Thesis frontmatter change (Theses/[ticker]); (2) Sector note edit; (3) Archive move (closure). If transaction complete on inspection, manually edit to completed. If incomplete, /rollback [batch] to pre-status state.`

49. **Thesis manifest aging + status (H1)** — `_thesis-manifest*.md`. Written by `/thesis` Step 3.5 (skeleton) → Step 7.5 (flip). See shared pattern above.
    - **Frontmatter keys**: `type: thesis-manifest`, `batch`, `status`, `ticker`, `proposed_name`, `proposed_path`, `sector`, `date`, optional `completed_date`.
    - **`in-progress` recovery**: `⚠️ In-progress /thesis manifest: [[...]]. Inspect body: (1) Thesis file at [proposed_path]; (2) Sector note Active Theses entry; (3) _hot.md sections. If all landed, manually edit to completed. If partial, either complete remaining manually or rm thesis + manifest and re-run /thesis.`
    - **Pre-existing thesis check** for `in-progress`: if `Theses/[proposed_path]` exists with valid frontmatter → likely flip-failure (cause 2, §4.3). If NOT → skeleton written but Step 4 failed — simpler recovery (rm manifest, re-run).

34. **Sector frontmatter standardization** — Thesis `sector:` values vs canonical sector note names.
    - **Vault-wide only**.
    - For each unique `sector:` across `Theses/*.md`, count using theses + check exact match (case-sensitive, whitespace-exact) against `Sectors/*.md` filename or `sector:` frontmatter.
    - Report:
      - Important: `⚠️ [N] thesis files use sector "[V]" — no exact match. Closest: "[M]" (edit distance [K]). Theses: [list]. Will silently rely on normalized/substring resolution.`
      - Nice to Have (suppressed by default): `🔖 [N] thesis files use sector "[V]" — exact match exists.`
    - **Stats**: `Sector taxonomy: [unique] distinct values across [thesis_count] theses; [exact] exact match, [divergent] normalization/substring.`

42. **`_hot.md` truncation-marker detection** — Per `hot-md-contract.md §Truncation-marker detection`.
    - **Vault-wide AND scoped** (§1.2).
    - **Forbidden markers**:
      - Trailing `...` at end of a bullet line (literal, not mid-sentence ellipsis)
      - Bracketed sentinels: `[compressed]`, `[truncated]`, `[...]`
      - Unclosed markdown: odd count of `**`, `*`, `_`, backtick within a section; trailing `[` or `(` without closing bracket
    - **Severity**: Important — `⚠️ _hot.md contains truncation marker(s): [list with section name]. Compression policy forbids truncating; legitimate compression drops whole entries. Investigate: manual edit or skill drift. If user edit, consolidate/remove. If skill drift, re-check producer compliance.`
    - **Cross-check with #35**: both flagged → recommend deletion + letting next `/sync` recreate from canonical schema.

43. **Vault lock staleness detection** — `.vault-lock*` files classified by `timeout_at:` (§7).
    - **Vault-wide only**. **Precondition**: none → Pass.
    - Parse each (`token:`, `skill:`, `scope:`, `started_at:`, `timeout_at:`, optional `multi_scope:`).
    - **Classification**:
      - **Active** (`timeout_at:` > now): Pass silently.
      - **Stale** (`timeout_at:` < now): Important — `⚠️ Stale vault lock: [[...]]. Skill [X] (token [T]), scope [scope], started [started_at], timeout [timeout_at] ([N] min ago). May have crashed OR still legitimately running (long web-research, large batches). Recovery USER-INITIATED — no auto-steal. If confirmed abandoned: rm "[path]". If manifest exists (#36/#41/#47/#48), consult those first.`
      - **Malformed** (missing required fields): Important — `⚠️ Malformed vault lock: [[...]] missing [list]. Unknown ownership. Safe to rm only if confirmed no skill running.`
    - **Multi-ticker**: report all N peer locks together. Partial acquisition: `⚠️ Partial multi-ticker lock: token [T] expected [peers] but only [actual] exist. /compare may have crashed mid-acquisition.`

44. **Scenario-note reversal completeness** — Every `Research/*.md` with `source_type: scenario` + reversal evidence, verify each `propagated_to:` ticker got either Log entry OR archive-skip note.
    - **Vault-wide only**.
    - For each scenario note with reversal evidence:
      - Parse `propagated_to:`.
      - Each ticker: live (`Theses/TICKER - *.md`) → Log must contain `Scenario REVERSED [[Research/scenario-note]]` entry. Archived (`_Archive/TICKER - *.md`) → scenario note's `## Reversal Notes` section must list. Missing from disk → already flagged by `/scenario reverse` R6.
    - **Severity**: Important — `⚠️ Scenario reversal incomplete: [[...]] reversal applied [date], but [N] ticker(s) from propagated_to: lack reversal record: [list]. Either re-run /scenario reverse [scenario], or manually add REVERSED entry to live thesis Log / document archive-skip per /scenario R4.5 spec.`

45. **Compare manifest aging** — `_compare-manifest*.md`. Written by `/compare` Phase 5.5c.
    - **Vault-wide only**. **Precondition**: none → Pass.
    - Parse (`type: compare-manifest`, `batch:`, `status: completed | rolled-back | in-progress`, `date:`).
    - **Severity**:
      - `in-progress` → Critical: `❌ In-progress /compare manifest: [[...]]. Crashed or interrupted mid-transaction. Recovery: inspect body for intended sector writes, verify current state, complete missing writes OR /rollback individual sectors using per-sector snapshots.`
      - `completed` + age >90d → Nice to Have: `🔖 Stale completed compare manifest ([N] days old). Safe to delete.`
      - `rolled-back` (clean abort) → Pass — records successful atomicity rollback.

46. **Archive-ticker registry integrity** — Validate `.archive_ticker_registry.md` entries.
    - **Vault-wide only**. **Precondition**: file missing → Pass.
    - Parse each line: `TICKER|archived_filename.md|date|conviction|rationale`.
    - Verify `archived_filename` exists in `_Archive/`. Missing → Nice to Have: `🔖 Stale archive-registry entry: TICKER|[filename] — not at _Archive/[filename]. /thesis Signal C verifies existence before matching, so stale tolerated; remove manually if desired.`
    - **Aggregate**: `Archive registry: [N] entries, [M] verified, [K] stale.`

---

## Output Format

Prioritized checklist:

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
