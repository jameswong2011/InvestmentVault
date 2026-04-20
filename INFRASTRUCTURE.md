# Infrastructure Reference

> Deep technical details for the vault's consistency machinery. User-facing summary: [[User Guide#14. How the Vault Stays Consistent]]. Read this file when debugging an edge case, extending a contract, or authoring a new skill.
>
> **Per-skill deep rationale** lives in `<skill>/RATIONALE.md` (currently only `sync/RATIONALE.md`). When a skill's design rationale exceeds ~20% of its SKILL.md, extract per §12.3. Cross-skill contracts live in `.claude/skills/_shared/*.md` (§12.2).

## 1. Vault content files

User Guide §14 covers basics. This section captures the operational nuance `/lint` and skill authors depend on.

### 1.1 `_hot.md` — Session context cache

Full compression contract at `.claude/skills/_shared/hot-md-contract.md`. Key rules:

- **Six-section schema** (load-bearing; missing sections cause silent skill no-ops): `## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`
- **Caps**: soft 4,000 words / hard 5,000
- **Compression trigger order** over soft cap: drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → warn in skill report
- **Never compressed**: Recent Conviction Changes (every entry is a high-signal audit record)
- **Forbidden truncation markers**: `...` trailing bullets, `[compressed]`, `[truncated]`, unclosed `**`/`*`/backtick — compression drops whole entries, never truncates
- **Same-ticker continuation**: same-ticker Active Research Thread stays live; different-ticker compresses outgoing to `*Previous YYYY-MM-DD:*` line

Writers (13 skills): `/sync`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/thesis`, `/deepen`, `/prune`, `/status`, `/rollback`, `/catalyst`, `/brief` (Active Research Thread + Open Questions only), `/rename` (free-text mentions of the old name). Lint enforcement: `#35` (schema), `#42` (truncation markers).

### 1.2 `_graph.md` — Vault dependency map

Owned exclusively by `/graph`. Three modes (full rebuild, `/graph last` incremental, `/graph [N]` catch-up). Watermark in frontmatter:
- `last_graph_write: YYYY-MM-DDThh:mm:ssZ` — ISO second-precision (T6.10)
- `date: YYYY-MM-DD` — display-only; legacy fallback when `last_graph_write:` missing

**Reverse indexes always rebuild from scratch in-memory** on every `/graph` run — prevents drift even when incremental adjacency extraction skips unchanged theses.

**T7.3 cache fields** (added per-thesis adjacency entry): `status:` and `log_tail:` (last 3 Log `date | prefix` pairs). `/sync` Pass 1 and Step 2.5 consume these instead of re-reading every thesis. Pre-T7.3 graph files upgrade on next `/graph last` — entries missing the fields are flagged as invalidated and re-extracted.

**Write-avoidance exceptions**: only `/rename` writes `_graph.md` outside `/graph` (surgical adjacency-header update; does NOT advance `last_graph_write:`). All other research skills accumulate changes into `.graph_invalidations` (§2.3) and leave the rewrite to `/graph last`.

### 1.3 `_catalyst.md` — Catalyst calendar

Regenerated each `/catalyst` run. Timeline: next 2 weeks (daily), weeks 3-4 (weekly), months 2-3 (grouped by week). Flags catalyst gaps and stale events.

**Pre-regenerate snapshot** (H2): if web search fails mid-run, recover via `/rollback` batch `catalyst-YYYY-MM-DD-HHMMSS`. Snapshot failure **hard-aborts** `/catalyst` — the prior `_catalyst.md` is always preserved; no partial overwrite path exists.

---

## 2. Runtime state markers at vault root

All markers here are ephemeral and git-ignored. Complete inventory (including static directories) in §11.

### 2.1 `.last_sync` — Sync watermark + idempotency keying

Touched at the end of `/sync` (default) and `/sync all`. Next run uses `find -newer .last_sync` to detect changed files.

| Mode | Touches `.last_sync`? |
|---|---|
| `/sync` (default) | Yes |
| `/sync all` | Yes + writes `.sync_all_fresh` |
| `/sync TICKER` | **No** — preserves baseline for next default sync. First-run exception: creates epoch placeholder `touch -t 197001010000` if absent |
| `/graph` | Never (owns its own watermark via `_graph.md` frontmatter) |

**Idempotency keying** (H4): `/sync`'s per-thesis check keys on two tiers:

1. **Primary key — wikilink presence** in thesis `## Log` section (the 5 canonical forms — see `_shared/wikilink-forms.md`). Once a research note has propagated, it is terminal regardless of calendar day.
2. **Secondary keys — rename/move resilience**: `source:` URL, `date: + ticker:` tuple, `tags:` intersection + date match. Fire only when primary misses (rename/move scenarios where wikilink drifted).

Eliminates midnight-rollover duplicates and rename-induced re-propagation. Full mechanics in `sync/RATIONALE.md §1`.

### 2.2 `.sync_all_fresh` — Full-rebuild signal

Written by `/sync all` Step 7. Read by `/graph` pre-watermark check: present → force full rebuild regardless of mode → delete marker after successful write.

Closes the gap where `/sync all`'s two-pass triage leaves "No delta" thesis mtimes untouched; without the marker, incremental `/graph last` would miss them. `/lint #38` ages stale markers.

### 2.3 `.graph_invalidations` — Deferred graph update list

Written (appended) on thesis closure by `/status` Step 7.6 and `/prune` Stage 4.5. Contains relative paths of neighbor theses whose `cross-thesis:` references are now stale (pointing to an archived thesis).

Read by `/graph last` Step I.2.5, folded into the changed-thesis bucket, deleted only after successful write. Dedup via `sort -u`; repeated closures safely accumulate.

### 2.4 `.rename_incomplete.TICKER` — Failed-rename repair marker

Written by `/rename` Step 5.5 when one or more wikilink Edits fail after the `mv` completed. Per-ticker filename so concurrent repairs coexist.

Marker frontmatter: `ticker`, `old_name`, `new_name`, `batch_id`, `failed_files:`.

**Pre-flight check in consumers**: ticker-scoped skills hard-block on an active marker for their ticker; vault-wide skills hard-block on ANY active marker (exceptions: `/lint`, `/rollback` list mode, `/graph` read-only, `/rename` itself, `/ingest` advisory-only).

**Cross-new_name guard** (Step 1.4.5): if marker exists with different `new_name:` than proposed re-run, `/rename` aborts — prevents two target names from corrupting each other's repair state.

Re-run `/rename TICKER "[same new_name]"` triggers repair mode: mv skipped, only failed Edits retried. Marker shrinks monotonically, auto-deletes when empty. `/lint #37` surfaces active markers.

### 2.5 `.archive_ticker_registry.md` — Archive lookup

Flat append-only log of thesis archival events, maintained by `/status` Step 7.5b and `/prune` Stage 2. One line per event:
```
TICKER|archived_filename.md|YYYY-MM-DD|conviction_at_closure|closure_rationale
```

Consumed by `/thesis` Step 1.2 archive-collision check (Signal C) — catches prior archived theses whose filename no longer matches `_Archive/TICKER - *.md` (renamed-then-archived). Stale entries tolerated — `/thesis` verifies existence before treating an entry as a match. `/lint #46` validates.

### 2.6 `.vault-lock*` — Concurrency locks

Brief summary here; deep-dive in §6.

| Scope | File | Skills |
|---|---|---|
| Vault-wide | `.vault-lock` | `/sync all`, `/graph`, `/prune`, `/lint` full, `/clean`, `/catalyst`, `/ingest`, `/scenario`, `/surface` (unscoped/sector), `/rollback` restore |
| Ticker | `.vault-lock.TICKER` | `/sync TICKER`, `/deepen`, `/stress-test`, `/status TICKER`, `/brief`, `/rename`, `/thesis`, `/surface TICKER` |
| Multi-ticker | N separate per-ticker locks | `/compare A vs B vs C` |
| Read-only | `.vault-lock.readonly` | `/lint TICKER`, `/rollback` list |

Token-based ownership; explicit release; no auto-steal. `/lint #43` surfaces stale locks.

### 2.7 `.drift-config.md` (optional) — Drift tuning

User-authored override for `/sync` Step 3e conviction-drift heuristics:
```yaml
---
window_size: 5                 # min 3, max 10
base_threshold: 3              # weakening entries in window fires drift
post_stress_threshold: 4       # within 30 days of stress test
post_stress_window_days: 30
deepened_exclusion_days: 14
---
```

Missing → defaults. Malformed → warning + defaults. Heuristic rationale: `sync/RATIONALE.md §8`.

---

## 3. Snapshots & transaction manifests

Multi-file skills use **skeleton → populate → flip** pattern: manifest written BEFORE any destructive mutation lands, populated incrementally (or at phase boundaries, per T7.4), then flipped to `status: completed`. An `in-progress` manifest signals skill crash or final-flip miss.

### 3.1 `_Archive/Snapshots/` — Version control

Created before destructive edits by: `/sync` (Tier A), `/deepen`, `/status` (except draft→active), `/compare`, `/prune`, `/catalyst`, `/rollback`, `/rename`.

**Batch ID**: `<trigger>-YYYY-MM-DD-HHMMSS` (6-digit second-precision). `/rollback` cascade detection matches by batch-ID prefix.

**Orphan protection** (user-facing detail in User Guide §8): snapshots whose `snapshot_of:` source is missing default to PROTECTED by `/clean`. Explicit opt-in via `/clean orphans` or `/clean [days] --include-orphans`.

### 3.2 Manifest catalogue

All manifests at `_Archive/Snapshots/_<type>-manifest (<type>-*).md` with `type: <type>-manifest`, `status: in-progress | completed | rolled-back`, `batch:`, `date:`, `completed_date:`.

| Manifest | Producer | `/rollback` cascade | `/lint` | Notes |
|---|---|---|---|---|
| `_prune-manifest` | `/prune` Stage 1.5 | 2.5c | #36 | Records closures, upgrades, affected sectors, Stage 4.2 neighbors. 30-day regret-recovery window floors `/clean` deletion regardless of `/clean [days]` arg |
| `_sync-manifest` | `/sync` Step 2.9 (T2.1 skeleton) | 2.5b | #41 | Two-phase: skeleton pre-mutation → phase-boundary checkpoints (T7.4: end-of-Step-3/4/5 + 7.5 flip) → `completed`. Tier B Log entries surfaced for strikethrough review during cascade |
| `_compare-manifest` | `/compare` Phase 5.5c | — | #45 | Sectors edited/rolled-back, per-target Log outcomes. `status: rolled-back` when atomicity fires |
| `_stress-test-manifest` | `/stress-test` Phase 4.6 (T3.1) | 2.5d | #47 | Records the Log entry text appended to tested thesis (no snapshot — append-only) |
| `_status-manifest` | `/status` Step 3.0.5 (T2.2) | 2.5e | #48 | Two-phase. Records thesis frontmatter change, sector edit, archive move, graph invalidations, `_hot.md`. Reaffirm flow skips manifest (no multi-file transaction) |
| `_thesis-manifest` | `/thesis` Step 3.5 (H1) | 2.5f | #49 | Two-phase. `/rollback` cascade is **deletion-based** (not snapshot restore) since `/thesis` creates new files |

**Aging policy**: `in-progress` → Important (crash signal). `completed` → aged per 90/180 day tiers by the paired `/lint` check. `/clean` removes only after both the requested age AND any manifest-specific floor (e.g., prune 30-day window) are satisfied.

---

## 4. Content-quality gate (`/ingest`)

URL and PDF ingests block on failure; manual local files receive advisory logs.

### 4.1 Structural checks
- ≥150 word body
- No paywall/CAPTCHA/anti-bot sentinels
- ≥2 of 4 expected body sections populated

### 4.2 Domain-specific checks by `source_type:`

| `source_type` | Requirements |
|---|---|
| `earnings` | Period tokens (Q1/Q2/Q3/Q4/FY20XX) + 2+ currency figures + ticker/company reference |
| `analyst-report` | Rating token (Buy/Sell/Hold/Overweight/…) + price-target reference + ticker |
| `news` | Ticker + dated event reference (absolute date or temporal token) |
| `deep-dive` | ≥500 words + ≥3 substantive sections |
| `web-clip`, `data` | Skip domain checks |

### 4.3 Integrity checks
- **Numerical integrity**: detects OCR corruption (capital-O-as-zero, decimal-dropped currency like `$1 5B`, `II` as `11`)
- **Title-URL consistency** (URL mode): first heading tokens overlap ≥50% (Jaccard) with URL path slug — catches redirects to login/subscribe pages

### 4.4 Failure handling

Failed gate → research note deleted, source retained for re-ingest. Blocks the most damaging silent-corruption path: paywalled or wrong-content URLs propagating into thesis Log entries via `/sync`.

### 4.5 Source-URL dedup
- **Mode A URL / Mode B single-file**: exact-match grep against `Research/*.md` `source:` frontmatter. Same-day → hard-block. Cross-day → prompts skip/re-ingest/cancel
- **Batch Mode C**: `_Inbox/processed/` filename-based guard

---

## 5. Producer contracts & atomicity

Cross-skill contracts that gate propagation correctness. Skill-specific rationale (classification gates, archive-aware iteration, etc.) lives in per-skill RATIONALE.md files where they exist.

### 5.1 `propagated_to:` — the atomicity signal

Research notes from `/scenario`, `/stress-test`, `/compare`, `/deepen` carry `propagated_to:` frontmatter listing tickers whose Logs received propagation.

**Atomicity rule**: field written ONLY after all Log appends succeed. Partial failure → field omitted → signal to `/sync` to retry via file-direct fallback.

**Terminal signals**:
- `synthesis` and `brief` notes carry `propagated_to: []` — terminal. Blocks `/sync` from spamming 10+ theses with circular self-propagation Log entries (common in `/surface` scans and `/brief` outputs).

`/sync` Case handling in `sync/SKILL.md §1.7` (Case 2a absent, 2b non-empty, 2c empty-terminal). Full mechanics in `sync/RATIONALE.md §1.5-§1.6`.

### 5.2 `/lint #39` — producer contract verification

Vault-wide. For each `Research/*.md`:

| `source_type` | `propagated_to:` requirement | Severity if missing |
|---|---|---|
| `synthesis`, `brief` | Must be `[]` | Important regardless of date |
| `scenario`, `stress-test`, `comparison` | Must be present unless atomicity rule fired | Important if absent and date ≥ 2026-04-19; Nice to Have if pre-spec |
| Other source types | No requirement | — |

Cross-checks with `/lint #1`. Notes flagged by both are strongest cleanup candidates.

### 5.3 Cross-skill classification & approval gates (condensed)

| Skill | Gate | Purpose |
|---|---|---|
| `/thesis` Step 1.2 | Multi-signal archive-collision (4 signals: filename glob, `ticker:` frontmatter, `.archive_ticker_registry.md`, `_Archive/Snapshots/` `snapshot_of:`) | Prevent duplicate theses for tickers with prior archived analysis. On match: 4 options (rollback, new-suffix, proceed-accepting-dual-files, cancel) |
| `/thesis` Step 5 | New-sector handling | If `sector:` doesn't resolve, prompt: create scaffold, proceed without sector update, or cancel. No silent skip |
| `/scenario` Phase 6.1.5 | Major/Minor/Neutral classification approval | Explicit user review before Log writes. Catches LLM misclassification both ways |
| `/scenario reverse` | Archive-aware iteration | Live theses receive `Scenario REVERSED` Log entry; archived theses get a `## Reversal Notes` append to the scenario research note body (Tier 3 archive protection) |
| `/rollback` closure cascade | H3 neighbor-citation scan | Scans Macro + Sector body prose outside Log sections for `[[TICKER]]` citations. Classifies premise-dependent vs contextual. Surfaces for manual review — no auto-edit (body prose is not Log-tier append-only) |

---

## 6. Locks (deep-dive)

Consolidates the full lock contract. User-facing summary in User Guide §14.

### 6.1 Canonical procedures

Procedures 1–4 of `.claude/skills/_shared/preflight.md`:

| Procedure | Purpose |
|---|---|
| 1 — Acquisition | Write lockfile at Step 0.1 with token, skill, scope, timeouts. Scope taxonomy per §2.6 |
| 1.5 — Ownership verification | Every subsequent Bash block verifies the lock's `token:` field matches the run-token captured at 0.1. Mismatch → abort (`LOCK_LOST`) — another skill seized the lock or user `rm`'d it |
| 2 — Rename-marker check | Hard-block on `.rename_incomplete.*` per §2.4 |
| 3 — Name sanitization | Whitelist + NFC for user-supplied filenames (currently only `/rename` new_name). Rejects `/\:*?"<>|`, leading dot, reserved names, length >100 |
| 4 — Section existence probe | Skills editing a specific `## Heading` abort if absent |

Release at skill's final Bash block: `rm -f "$LOCK_FILE"`.

### 6.2 Design rationale

- **Token-based not PID-based**: Claude Code's Bash tool is stateless; each block is a fresh subshell with different `$$`. The LLM captures the token at 0.1 and carries it as a literal string through subsequent tool calls; lock ownership keys on the token.
- **Explicit release not trap-based**: `trap "... INT TERM"` only handles signals within the acquisition block; subsequent blocks don't inherit. Explicit `rm -f` at skill end is more reliable. Mid-run abort → lock persists stale → `/lint #43` surfaces for manual recovery.
- **No auto-steal**: timeout-based stealing would race legitimately long-running skills (web research, `/sync all` on mature vault). Manual recovery is the safer default.

### 6.3 Multi-ticker partial-acquisition rollback (`/compare`)

`/compare A vs B vs C` acquires `.vault-lock.A` + `.vault-lock.B` + `.vault-lock.C` sequentially. If any acquisition fails:
1. Release all previously-acquired locks in reverse order (C, B) — not orphan them
2. Abort with `Partial lock acquisition failed on TICKER`
3. User waits for conflicting lock to clear, re-runs

Per-ticker scheme (C4 fix) handles hyphen-containing tickers (`BRK-B`, `BF-A`, `PBR-A`) that the prior `+`-delimited scheme corrupted.

---

## 7. Rollback cascade catalogue

Each multi-file skill writes a manifest (§3.2); `/rollback` reads the manifest to offer atomic restore.

| Cascade step | Trigger matched | Options offered |
|---|---|---|
| 2.5a | Generic `snapshot_batch:` prefix lookup across `_Archive/Snapshots/` — base path for every trigger | Cascade all matched files / Single / Cancel |
| 2.5b | `/sync` — `_sync-manifest` sidecar present | Tier B Log entry review: surface-only / cascade + strikethrough / single / cancel |
| 2.5c | Non-manifest triggers (`/deepen`, `/catalyst`, `/rename`, `/rollback` pre-safety-net snapshots) | 2.5a generic cascade — Tier A only, no Tier B Log auto-handling |
| 2.5d | `/stress-test` — `_stress-test-manifest` sidecar present | Surface only / cascade + strikethrough Log entry on tested thesis / cancel |
| 2.5e | `/status` — `_status-manifest` sidecar present | Thesis-only restore / full transaction restore (thesis + sector + un-archive + clear invalidations) / cancel |
| 2.5f | `/thesis` — `_thesis-manifest` sidecar present | Delete thesis only / full cascade (delete + revert sector + revert `_hot.md` + revert orphan mtimes) / cancel. **Deletion-based, not snapshot-based** |
| `/prune` | `/prune` — `_prune-manifest` + per-file `snapshot_trigger: prune` snapshots | 2.5a generic batch cascade; 30-day regret window enforced by `/clean` floor; Step 6.2.5 intervening-entries scan fires when restoring a reopened closed thesis |
| `/catalyst` | `/catalyst` — `snapshot_trigger: catalyst` on selected snapshot | Restore prior `_catalyst.md` from pre-regenerate snapshot via 2.5a generic path |
| `/rename` | `/rename` — `snapshot_trigger: rename` with `rename_target:` field on selected snapshot | Step 4a rename-undo branch: symmetric reverse-rename via `/rename` inverse (recommended) / content-only restore (creates duplicate) / cancel |

### 7.1 Intervening-entries scan (closed theses only, Step 6.2.5)

When rolling back a closed thesis, scan all neighbor theses + (H3-extended) Macro + Sector notes for Log entries or prose dated after the closure referencing the closed thesis. Options:
- Surface-only (manual handling)
- Auto-strikethrough `Cross-thesis closure:`-tagged entries (premise-dependent)
- Auto-strikethrough ALL intervening references
- Skip

Premise-dependent vs contextual classification drives default recommendation.

---

## 8. `/graph last` cost model

| Vault state | Work performed |
|---|---|
| No files changed since last graph + no invalidations | Skip — zero reads |
| 1-5 thesis files changed | Re-extract those + read 19 sector/macro files for reverse indexes |
| 30+ thesis files changed | Approaches full rebuild cost |

Watermark precision: ISO second-level (`last_graph_write:`). Legacy graph files without this field fall back to `date:` at 00:00:00 UTC; next write upgrades. Running twice within the same minute re-processes files modified between runs — output idempotent, just wasted compute.

---

## 9. `/rename` atomicity details

### 9.1 Wikilink patterns (7 variants)

`/rename` Edits scan for and update:
1. `[[TICKER - OldName]]`
2. `[[TICKER - OldName.md]]`
3. `[[TICKER - OldName|alias]]`
4. `[[Theses/TICKER - OldName]]`
5. `[[Theses/TICKER - OldName.md]]`
6. `[[_Archive/TICKER - OldName]]`
7. `[[_Archive/TICKER - OldName.md]]`

Partially overlaps the 5-form wikilink contract (`_shared/wikilink-forms.md`) but includes 2 archive-specific forms for the archived-then-renamed case.

### 9.2 Pre-flight Read/Write probe (Step 3.5)

Before the `mv`, `/rename` reads every file containing an inbound wikilink (glob across `Theses/`, `Research/`, `Sectors/`, `Macro/`, `_Archive/`, `_hot.md`, `_graph.md`). If any file unreachable → abort BEFORE the mv; no partial state.

### 9.3 Cross-`new_name` guard (Step 1.4.5)

Marker exists from prior failed rename:
- `new_name` matches → repair mode (skip mv, retry Edits only)
- `new_name` differs → abort with "In-flight rename conflict"

Options on conflict: finish prior with marker's `new_name:`, manually resolve + `rm` marker, or accept repair-state loss.

### 9.4 Post-mv Edit failure

Writes `.rename_incomplete.TICKER` listing failed files. Re-run triggers repair mode: mv skipped, failed Edits retried, marker shrinks monotonically until empty → auto-delete.

`/lint #37` globs `.rename_incomplete.*`; each marker surfaces independently. Scoped `/lint TICKER` runs only for that ticker.

---

## 10. `/lint` registry (by ID)

Key checks — severity column indicates escalation in the lint report.

| ID | Scope | What it catches | Severity |
|---|---|---|---|
| #1 | Full | Research note without `propagated_to:` AND no thesis Log reference | Important |
| #16 | Full | Stale snapshots (>180 days) | Nice to Have |
| #18, #20, #23 | Full | Graph health (existence, staleness, missing/ghost entries) | Important |
| #29 | Full | Log-prefix registry vs consumer-list drift (`_shared/log-prefixes.md`) | Important |
| #30 | Scoped | Sector-resolution coverage per thesis (`_shared/sector-resolution.md`) | Important if `none`, Nice to Have if `substring`/`normalized` |
| #34 | Full | Sector frontmatter standardization vault-wide | Nice to Have |
| #32 | Full | Orphaned ticker refs (research `ticker:` matches no thesis) | Nice to Have |
| #33 | Full | Closed thesis file still in `Theses/` | Important |
| #35 | Full + scoped | `_hot.md` schema drift | Important (silent no-op source) |
| #36 | Full | `_prune-manifest` state | Important if in-progress; Nice to Have if completed >30 days |
| #37 | Full + scoped | `.rename_incomplete.*` markers | Important |
| #38 | Full | State marker hygiene (`.sync_all_fresh`, `.graph_invalidations` aging) | Nice to Have |
| #39 | Full | `propagated_to:` producer contract | Important (post-spec) / Nice to Have (pre-spec) |
| #41 | Full | `_sync-manifest` aging | Important if in-progress; tiered if completed |
| #42 | Full + scoped | `_hot.md` truncation markers | Important |
| #43 | Full | Stale locks | Nice to Have (user-triggered recovery) |
| #45 | Full | `_compare-manifest` aging | Important if in-progress; tiered if completed |
| #46 | Full | `.archive_ticker_registry.md` validation | Nice to Have |
| #47 | Full | `_stress-test-manifest` aging | Important if in-progress |
| #48 | Full | `_status-manifest` aging | Important if in-progress |
| #49 | Full | `_thesis-manifest` aging | Important if in-progress |

Scoped mode always runs #35 and (if marker exists) #37 — these are vault-global concerns whose cost is low enough to gate weekly rather than monthly.

---

## 11. Vault root hidden files — complete inventory

Complete catalog of dotfiles and dot-directories at the vault root. Runtime markers (§2) deep-detailed above; this section covers the static infrastructure not otherwise documented.

### 11.1 Static infrastructure directories

| Entry | Type | Purpose | Tracked in git? |
|---|---|---|---|
| `.git/` | dir | Git repository metadata and object store | Self |
| `.claude/` | dir | Claude Code harness: `agents/`, `commands/`, `settings.json`, `skills/` | Partially — skills/commands/agents tracked; local settings ignored |
| `.claudian/` | dir | Claudian Obsidian plugin state (`claudian-settings.json`, per-conversation sessions) | No — entirely git-ignored |
| `.obsidian/` | dir | Obsidian vault config: workspace, plugins, themes, graph view | Partially — personal UI state git-ignored |

#### 11.1.1 `.claude/` layout

```
.claude/
├── agents/           — Subagent definitions (vault-explorer.md)
├── commands/         — Slash-command shortcuts (currently empty)
├── settings.json     — Tool permission allowlist + hooks (git-ignored)
└── skills/           — 17 skill definitions + _shared/
    ├── _shared/      — Cross-skill contracts (§12.2)
    ├── sync/         — SKILL.md + RATIONALE.md
    ├── graph/        — SKILL.md
    └── [15 others]/  — brief, catalyst, clean, compare, deepen, ingest,
                        lint, prune, rename, rollback, scenario, status,
                        stress-test, surface, thesis
```

#### 11.1.2 `.claudian/` and `.obsidian/`

Neither is read or written by any skill. Both are plugin/app-managed:
- `.claudian/`: per-conversation sessions + global settings; entirely git-ignored.
- `.obsidian/`: mixed tracking — personal UI state (`workspace.json`, `cache/`) ignored; vault-shared config (`core-plugins.json`, `community-plugins.json`, installed plugins) tracked. Skills write `.md` files that Dataview queries read live; `obsidian-git` plugin may auto-commit depending on user config (skills never commit — commits are user-initiated).

### 11.2 Version control and OS files

| File | Purpose | Modifier |
|---|---|---|
| `.gitignore` | Exclusion rules: UI state, runtime markers, Claudian state, secrets, macOS metadata | Manual |
| `.gitattributes` | Text normalization (`* text=auto`, LF line endings) | Manual |
| `.DS_Store` | Finder view metadata | Git-ignored; auto-created by macOS |

`.gitignore` is the **authoritative runtime-marker registry**. Adding a new ephemeral marker requires: updating the producing skill's spec AND `.gitignore` AND §2 here AND the Appendix ownership matrix.

### 11.3 Reserved / optional markers

| Marker | Status | Purpose |
|---|---|---|
| `.drift-config.md` | Optional, user-authored | `/sync` drift detection parameter overrides (§2.7) |
| `.archive_ticker_registry.md` | Auto-maintained, append-only | Archive lookup (§2.5) |
| `.sync-progress.jsonl` | **Reserved, not implemented** | T7.4 optional intra-phase crash-granularity scratch log. Namespace claimed in `sync/RATIONALE.md §5.3.1`; not written by any current skill |

### 11.4 Causal dependency chains

Five chains connect runtime markers to skill behavior:

1. **Sync → Graph (full rebuild signal)**: `/sync all` writes `.sync_all_fresh` → `/graph` forces full rebuild → deletes marker.
2. **Sync → Sync (watermark progression)**: `.last_sync` touched end-of-run (except ticker-scoped) → next `/sync` uses for `find -newer`.
3. **Closure → Graph (neighbor re-extraction)**: `/status` / `/prune` append to `.graph_invalidations` → `/graph last` consumes → deletes.
4. **Rename → ticker-scoped skills (repair gate)**: `/rename` partial Edit failure writes `.rename_incomplete.TICKER` → consumer skills hard-block → repair retry shrinks marker → auto-delete when empty.
5. **Locking**: Skill 0.1 writes `.vault-lock*` → subsequent blocks verify `token:` → final block releases. Abandonment → stale lock → `/lint #43`.

### 11.5 Adding a new hidden marker — checklist

When a new skill needs a vault-root marker:
1. Spec contract in producing skill's SKILL.md (writer, reader, deletion, absence-vs-presence semantics)
2. Add to `.gitignore` "Vault runtime state markers" section with inline provenance comment
3. Add subsection here (§2)
4. Add row to Appendix ownership matrix
5. Add `/lint` check if marker can accumulate stale state
6. Add to User Guide §14 if user-visible

Skipping any surface produces silent drift (committed by accident; accumulates stale state; mystery file on disk for users).

---

## 12. Skill-layer architecture

Under `.claude/skills/`, three kinds of markdown files compose each skill. Load semantics matter: every byte in `SKILL.md` is paid for per invocation (prompt load + cache cost); `_shared/*.md` contracts are paid only when explicitly `Read`; `RATIONALE.md` is free at runtime.

### 12.1 Three file kinds

| Kind | Location | Auto-loaded by harness? | Read by LLM at runtime? |
|---|---|---|---|
| `SKILL.md` | `.claude/skills/<skill>/SKILL.md` | **Yes** — injected into system prompt on invocation | — (already in prompt) |
| `_shared/*.md` | `.claude/skills/_shared/*.md` | No | Only when explicit `Read`; most skills inline critical procedures and treat shared contract as the fuller reference |
| `RATIONALE.md` | `.claude/skills/<skill>/RATIONALE.md` | **No** | Rarely — maintainers editing the skill, not the LLM executing it |

**T7 optimization consequence**: the split that produced `sync/RATIONALE.md` and `_shared/wikilink-forms.md` migrated non-operational text from paid-per-invocation SKILL.md to free-at-runtime RATIONALE.md or paid-on-demand `_shared/`. Savings: ~9,200 tokens per `/sync` invocation.

### 12.2 Shared contracts catalog

Five contracts under `.claude/skills/_shared/`. Editing any requires coordinated update across all consumers.

| Contract | Lines | Purpose | Consumers | Enforcing `/lint` |
|---|---|---|---|---|
| `preflight.md` | 525 | Lock acquisition (Procedures 1/1.5), rename-marker check (2), name sanitization (3), section probe (4) | Every state-modifying skill (17) | #43 |
| `log-prefixes.md` | 402 | Registry of Log-entry prefixes with producer/consumer bindings | `/sync` (§2.5 classification, §3e drift), `/lint` (#29), every producer | #29 |
| `hot-md-contract.md` | 90 | Per-section budget, soft/hard caps, compression trigger order, same-ticker continuation rule | 13 writers of `_hot.md` | #35, #42 |
| `sector-resolution.md` | 110 | Thesis `sector:` → sector note resolution (exact → normalized → substring → ask) | `/status`, `/thesis`, `/compare`, `/prune`, `/rollback` | #30, #31 |
| `wikilink-forms.md` | 59 | 5 canonical wikilink forms producers emit (T7.1) | `/sync` (§1.7, §4.0, §5.0), `/rollback` cascade, `/lint` #23, `/prune` closure cascade | — (convention-enforced) |

**Drift risk per contract**: if a producer diverges from its contract without updating consumers, silent failures result (concurrent-writer race, miscategorized Log entry, truncated `_hot.md` section, unresolved sector, missed wikilink match). Every contract has at least one `/lint` check except `wikilink-forms.md` which relies on the editing protocol (§12.4) alone.

### 12.3 RATIONALE.md pattern

Currently only `sync/RATIONALE.md` exists. Pattern: when SKILL.md accumulates rationale blocks (`> **Why this is safe**...`, `> **Edge case**...`, `> **T#.# rationale**...`) collectively exceeding ~20% of the file with no impact on LLM execution, extract.

**Must stay in SKILL.md**:
- Every operational rule the LLM applies at runtime
- All Log messages (user-visible surface)
- Critical-path Bash snippets that get inlined into execution
- Error/abort messages and their triggering conditions

**Should move to RATIONALE.md**:
- Historical context ("prior spec keyed on X; caused bug Y; switched to Z")
- Edge-case trade-off discussions
- Cross-midnight / renamed-file / concurrent-writer scenarios
- "Why we chose A over B" design dialectics
- Performance expectations and benchmarks

`sync/RATIONALE.md` has 9 sections (§1-§9) covering idempotency design, propagation-target resolution, Pass 1 logic, skill-origin gate, manifest contract, watermark semantics, _hot.md auto-resolve, drift detection, T7 efficiency principles. SKILL.md references via `§N.M` anchors.

**Reference format in SKILL.md**: use `§N.M` for same-file (SKILL.md) or RATIONALE.md references; use `registry §N` for `_shared/log-prefixes.md` registry entries; use `_shared/<contract>.md §N` for other shared contracts. Disambiguation prevents ambiguous cross-document pointers.

### 12.4 Editing protocol

1. **SKILL.md only** (operational rule change): edit, run `/lint` for affected skill, commit.
2. **`_shared/*.md` only** (contract tightening): edit contract, grep all consumers for affected references, verify every consumer behaves, run paired `/lint` checks, commit.
3. **Both**: edit contract FIRST, then consumers. Commits in this order → intermediate state is self-consistent (stricter contract may flag pre-existing behavior, but won't silently break).
4. **RATIONALE.md**: free-form; may commit independently of SKILL.md. Split maintained by convention, not enforced.
5. **New `_shared/*.md` contract**: update §12.2 + all consumer SKILL.md files + add `/lint` check if drift detection warranted.
6. **New `RATIONALE.md`**: update §12.3 listing.

### 12.5 Cross-skill contract-consumption graph

```
  preflight.md ◄──── every state-modifying skill (17) at Step 0

  log-prefixes.md ◄─ /sync (Step 2.5 + 3e)
                     /lint (#29)
                     /stress-test, /deepen, /status, /prune, /scenario,
                     /rollback, /rename, /thesis, /compare (as producers)

  hot-md-contract.md ◄── 13 writers: /sync, /status, /thesis, /surface,
                         /stress-test, /scenario, /compare, /deepen,
                         /prune, /rollback, /catalyst,
                         /brief (ART + OQ only), /rename (free-text mentions)
                         /lint (#35, #42)

  sector-resolution.md ◄ /status, /thesis, /compare, /prune, /rollback
                         /lint (#30, #31)

  wikilink-forms.md ◄─── /sync (Step 1.7, 4.0, 5.0)
                         /rollback (2.5 cascade), /prune (closure cascade)
                         /lint (#23, orphan checks)
```

Adding a new consumer: update this graph + add paired `/lint` check in the same commit.

---

## Appendix: File ownership matrix

| File / directory | Creators | Modifiers | Cleaners |
|---|---|---|---|
| `Theses/*.md` | `/thesis` | `/sync`, `/deepen`, `/status`, `/compare`, `/scenario`, `/stress-test`, `/prune`, `/rename`, `/rollback` | `/status` (archive), `/prune` (archive) |
| `Research/*.md` | `/ingest`, `/thesis`, `/deepen`, `/compare`, `/scenario`, `/stress-test`, `/surface`, `/brief`, manual | — (Tier 2 immutable bodies) | manual `mv` to `_Archive/Briefs/` |
| `Sectors/*.md` | manual, `/thesis` (scaffold) | `/sync`, `/status`, `/compare`, `/prune`, manual | — |
| `Macro/*.md` | manual | `/sync`, `/scenario` | — |
| `_hot.md` | `/sync` (auto-create) or any of 11 writers via CLAUDE.md rule #9 | 11 skills | manual when `/lint #35` or `#42` fires |
| `_graph.md` | `/graph` | `/graph`, `/rename` (adjacency header only) | `/graph` |
| `_catalyst.md` | `/catalyst` | `/catalyst` | `/catalyst` (overwrite) |
| `.claude/` | Git (tracked skills/commands/agents); Claude Code (local settings) | Users (skill spec edits); Claude Code | Manual |
| `.claude/skills/<skill>/SKILL.md` | Skill author | Skill editor; loaded per invocation by harness | Manual |
| `.claude/skills/<skill>/RATIONALE.md` | Manual (when SKILL.md split warranted; currently only `sync/`) | Manual alongside SKILL.md | Manual |
| `.claude/skills/_shared/*.md` | Contract author | Manual (coordinated with consumers) | Manual |
| `.claudian/` | Claudian plugin | Claudian plugin | Claudian plugin; manual |
| `.obsidian/` | Obsidian + plugins | Obsidian + plugins | Manual |
| `.git/` | Git | Git | `git gc` |
| `.gitignore`, `.gitattributes` | Manual | Manual | Manual |
| `.DS_Store` | macOS Finder | macOS Finder | Git-ignored |
| `.last_sync` | `/sync`, `/sync all` | `/sync`, `/sync all` | — |
| `.sync_all_fresh` | `/sync all` | — | `/graph` (consume & delete) |
| `.graph_invalidations` | `/status` closure, `/prune` | append-only | `/graph last` (consume & delete) |
| `.rename_incomplete.TICKER` | `/rename` on post-mv Edit failure | `/rename` (repair retries) | `/rename` (auto-delete when empty) |
| `.archive_ticker_registry.md` | `/status`, `/prune` closures | append-only | — (stale tolerated by `/thesis` verification) |
| `.vault-lock*` | all state-modifying skills | own skill only | own skill (explicit release); manual on abandonment |
| `.drift-config.md` | manual (optional) | manual | manual |
| `.sync-progress.jsonl` | **Reserved — not yet written** | — | — |
| `_Archive/Snapshots/*.md` | destructive skills (pre-edit) | — | `/clean` |
| `_Archive/Snapshots/_*-manifest-*.md` | multi-file skills (skeleton) | own skill (populate + flip) | `/clean` (after manifest-specific aging) |
