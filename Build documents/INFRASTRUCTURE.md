# Infrastructure Reference

> Deep technical details for the vault's consistency machinery. **Audience: Claude Code at skill-author / debugger scope.** User-facing summary: [[User Guide#14. How the Vault Stays Consistent]].
>
> **Per-skill deep rationale** lives in `<skill>/RATIONALE.md` (15 skills — see §12.3). Cross-skill contracts live in `.claude/skills/_shared/*.md` (§12.2).
>
> **Stable anchors** external files reference: §1.1 (`_hot.md`), §2.7 (`.drift-config.md`), §3.1 (snapshot table). Do not renumber without updating consumers.

---

## 0. Orientation

Read this section first on any non-trivial task: lookup tables, critical invariants, and a symptom index pointing to the deep-dive sections.

### 0.1 Reading paths

| Task | Read in order |
|---|---|
| **Debug a symptom** | §0.3 symptom index → §13 flow → deep-dive |
| **Author a new skill** | §0.4 → §0.5 → §5 → §3 → §6 → §12 |
| **Add a vault-root marker** | §11.5 checklist → §2 nearest sibling → Appendix |
| **Extend a `_shared/*.md` contract** | §12.2 catalog → §12.4 protocol → paired `/lint` check (§10) |
| **Change `_hot.md` schema/compression** | §1.1 → `_shared/hot-md-contract.md` → all 14 writers |
| **Add a `/lint` check** | §10 → §12.2 consumers → §12.4 |
| **Understand a rollback cascade** | §7 → §3.2 → §13.6 if stuck in-progress |
| **Tune model/context for a skill** | §12.6 → §0.4 → per-skill RATIONALE.md |
| **Hooks / scheduled runs / workflows** | §14 (harness automation layer) |

### 0.2 Critical invariants

Violating any of these produces silent corruption.

1. **Locks: token-based, explicit release, no auto-steal** (§6.2) — Bash blocks are stateless subshells; ownership keys on a token string the LLM carries. Release via `rm -f` at skill end. Stale locks surface via `/lint #43`; never steal on timeout.
2. **`propagated_to:` atomicity** (§5.1) — written ONLY after all Log appends succeed; partial failure omits the field so `/sync` retries. Terminal `propagated_to: []` on `synthesis`/`brief`/`retrospective` notes blocks circular self-propagation.
3. **Thesis `## Log` is append-only** (CLAUDE.md Tier 2) — never edit/reorder/delete. Log prefixes (`_shared/log-prefixes.md`) carry cross-skill semantics.
4. **`_hot.md` schema + compression contract** (§1.1) — missing sections cause silent no-ops (`/lint #35`). Compression drops whole entries, never truncates (`/lint #42`).
5. **`_graph.md` has one owner: `/graph`** (§1.2) — sole exception: `/rename`'s surgical adjacency-header update (does NOT advance `last_graph_write:`).
6. **Manifest skeleton → populate → flip** (§3) — manifest written BEFORE any destructive mutation; flipped to `completed` only after all edits land. `in-progress` = crash signal.
7. **Closure-snapshot 30-day floor is unbypassable** (§3.2) — pre-closure snapshots from `/prune` or `/status active→closed` are protected across ALL `/clean` modes for 30 days. No flag override.
8. **Rename marker hard-blocks consumers** (§2.4) — `.rename_incomplete.TICKER` blocks ticker-scoped skills on TICKER and most vault-wide skills on ANY marker. Repair: re-run `/rename TICKER "[same new_name]"`.
9. **Sector resolution is a 4-step ladder** (`_shared/sector-resolution.md`) — exact → normalized → substring → ask. Never silently skip or substring-match for destructive writes.
10. **5 canonical wikilink forms** (`_shared/wikilink-forms.md`) — idempotency and cascade detection must match all five. Producers emit form #1.
11. **Forked context is report-only** (§12.1) — forked skills' intermediate reasoning is discarded; if main needs a finding, the subagent must emit it in the summary or write it to a vault file.
12. **Model assignment is per-skill** (§0.4, §12.6) — mechanical skills run Sonnet max; all others Opus max. Downgrade/revert is a one-line SKILL.md frontmatter change.

### 0.3 Symptom → section index

| Symptom | Likely cause | Read |
|---|---|---|
| Skill silently no-op'd on `_hot.md` | Missing/renamed section heading | §1.1, §13.1 |
| `/sync` didn't propagate a manual thesis edit | Last Log prefix is skill-origin | §5.3, §13.2 |
| `/sync` propagated the same research twice | Wikilink drifted after rename → primary key missed | §2.1, `sync/RATIONALE.md §1` |
| `/graph` missed a thesis `/sync all` touched | `.sync_all_fresh` absent or consumed without rebuild | §2.2, §13.3 |
| `/graph last` didn't update neighbors after closure | `.graph_invalidations` not appended | §2.3 |
| `/clean` refused to delete a snapshot | 30-day closure floor or orphan protection | §3.2, §13.4 |
| `_graph.md` stale after `/rename` | `/rename` only updates the adjacency header | §1.2, §11.4 |
| Ticker skill blocks with "rename incomplete" | `.rename_incomplete.TICKER` exists | §2.4, §9 |
| Lock acquisition fails | Live collision or stale lock | §6, §13.5 |
| Manifest stuck `in-progress` | Skill crashed before flip | §3, §13.6 |
| `/ingest` deleted its own research note | Quality gate fired | §4 |
| `/thesis` refused — "prior archived thesis exists" | Multi-signal archive collision | §5.3 |
| `/compare` locked then failed mid-way | Partial-acquisition rollback | §6.3 |
| Wikilink not matched by a consumer | Consumer misses one of the 5 forms | `_shared/wikilink-forms.md` |
| Sector note never updated | Sector resolution returned `none` | §13.10 |
| `/rollback` closure cascade surfaced neighbor citations | H3 premise-dependent vs contextual | §5.3, §7.1 |
| `_hot.md` grows past soft cap | Compression trigger order not firing | §1.1 |
| `/surface` missed a cross-section pattern | Default mode is section-targeted; use `/surface all` | §12.6 |
| `/retro` returned every ticker as `data-gap` | WebSearch burst limit on Phase 3 fan-out | §13.11 |

### 0.4 Skill landscape

26 skills — 21 state/analysis skills plus **5 read-only analytical skills** (`dependency-map`, `macro-exposure`, `value-chain`, `assumptions`, `conviction-audit`) added 2026-07-22. The extractors report analysis, take no lock / manifest / snapshot, and each pairs with a portfolio workflow that fans its `## Method` out (§14.3). Lock scope, `_hot.md` writes, and manifests determine each skill's pre-flight and cleanup contract; **model** and **context** are the runtime-performance axes.

| Skill | Lock scope | `_hot.md`? | Manifest? | Snapshot? | Model | Context | Role |
|---|---|---|---|---|---|---|---|
| `/sync` | vault-wide † | Yes (all sections) | `_sync-manifest` | Tier A per-thesis | opus | main | Propagation engine |
| `/graph` | vault-wide | No | No | No | **sonnet** | main | Rebuild `_graph.md` (3 modes) |
| `/ingest` | vault-wide | No | No | No | opus | main | `_Inbox/` → Research; quality gate |
| `/status` | ticker | Yes | `_status-manifest` | Per-thesis (not draft→active/reaffirm) | **sonnet** | main | Conviction/status changes |
| `/thesis` | ticker | Yes (ART + OQ) | `_thesis-manifest` | No (deletion-based rollback) | opus | main | Create thesis |
| `/deepen` | ticker | Yes | `_deepen-manifest` | Per-thesis pre-edit | opus | main | Section deep-research |
| `/stress-test` | ticker | Yes | `_stress-test-manifest` | No (Log-append only) | opus | main | Adversarial test |
| `/compare` | N × ticker | Yes | `_compare-manifest` | Per-sector | opus | main | Competitive comparison |
| `/scenario` | vault-wide | Yes | No | No (Log-append only) | opus | main | Macro scenario propagation |
| `/brief` | ticker | Yes (ART + OQ) | No | No | opus | main | 1-page pitch |
| `/surface` | vault-wide ‡ | Yes | No | No | opus | **fork** | Insight discovery |
| `/catalyst` | vault-wide | Yes | No | `_catalyst.md` pre-regenerate | opus | **fork** | Catalyst calendar |
| `/retro` | vault-wide | Yes (ART + OQ) | No | No (immutable output) | opus | **fork** | Narrative-price delta review |
| `/prune` | vault-wide | Yes | `_prune-manifest` | Per-thesis pre-closure | opus | **fork** | Weak-thesis evaluation |
| `/rename` | ticker | Yes (mentions) | No | Per-thesis pre-rename | **sonnet** | main | Atomic rename + wikilink rewrite |
| `/rollback` | vault-wide (restore) / read-only (list) | Yes (restore) | No | Pre-rollback safety | **sonnet** | main | Snapshot restore + cascade |
| `/clean` | vault-wide | No | No | No | **sonnet** | main | Delete old snapshots/manifests |
| `/archive-callouts` | vault-wide (unscoped) / ticker | No | No | Per-file pre-sweep | **sonnet** | main | Sweep addressed callouts to Legacy |
| `/lint` | vault-wide (full) / read-only (scoped) | No | No | No | opus | **fork** | ~64 health checks (§10) |
| `/numbers` | ticker / vault-wide (`--all`) | No | No | Per-thesis pre-edit | **sonnet** | main | Refresh Key Metrics from FMP |
| `/transcript` | ticker (read-only for `--list`) | Yes (ART + OQ) | No | No (Log-append + immutable note) | opus | main | Earnings-transcript signal extraction |
| `/dependency-map` | none (read-only) | No | No | No | opus | main | Extract a thesis's dependency fingerprint (pairs → `portfolio-correlation`) |
| `/macro-exposure` | none (read-only) | No | No | No | opus | main | Tag a thesis's implicit macro bets (pairs → `portfolio-macro-exposure`) |
| `/value-chain` | none (read-only) | No | No | No | opus | main | Map a thesis's value-chain position (pairs → `portfolio-supply-chain`) |
| `/assumptions` | none (read-only) | No | No | No | opus | main | Load-bearing assumptions + internal-contradiction scan (pairs → `vault-contradictions`) |
| `/conviction-audit` | none (read-only) | No | No | No | opus | main | Conviction-evidence mismatch + silently-fired-trigger scan (pairs → `portfolio-conviction-audit`) |

**† `/sync` variants**: default scans changed files + adjacencies; `all` reads everything and writes `.sync_all_fresh`; `TICKER` uses a ticker lock and preserves `.last_sync`.
**‡ `/surface` variants**: default reads 4 sections per thesis; `all` full reads; `[sector]` sector-scoped; `TICKER` uses a ticker lock. All fork.

Design principles: **Opus max** for analytical work; **Sonnet** for mechanical work (`/graph`, `/rename`, `/rollback`, `/status`, `/clean`, `/archive-callouts`, `/numbers` — the last at effort `medium`, the only non-max skill, since its arithmetic is fully delegated to `numbers_compute.py`); **forked context** (5 skills: `/lint`, `/prune`, `/surface`, `/catalyst`, `/retro`) where reads dominate but output is bounded — main receives only the final summary. Ticker-scoped vs vault-wide is the most consequential authoring choice: it dictates concurrency, rename-marker behavior, and `.last_sync` semantics.

### 0.5 Glossary

| Term | Meaning |
|---|---|
| **Adjacency** | Per-thesis `_graph.md` entry: `cross-thesis:`, `same-sector:`, plus T7.3 cache fields (`status:`, `log_tail:`) |
| **Batch ID** | `<trigger>-YYYY-MM-DD-HHMMSS` grouping snapshots + manifests from one run |
| **Cache fields (T7.3)** | `status:` + `log_tail:` per graph entry so `/sync` classifies without re-reading every thesis |
| **Closure-snapshot 30-day floor** | Universal `/clean` protection on pre-closure snapshots (§3.2) |
| **Drift anchor** | Log prefix `/sync` Step 3e weights when detecting conviction drift |
| **Idempotency key** | `/sync` per-thesis check: wikilink-in-Log (primary), then `source:` URL / `date:+ticker:` / `tags:`+date fallbacks |
| **Load-bearing schema** | Structure whose absence causes silent no-op, not a crash (`_hot.md` sections, thesis sections, manifest frontmatter) |
| **Manifest** | `_Archive/Snapshots/_<type>-manifest (<type>-*).md` sidecar tracking a multi-file transaction |
| **Producer / consumer** | Skill that writes interpreted content (Log entries, `propagated_to:`, wikilinks) / skill that reads it to decide behavior |
| **Pre-flight** | `_shared/preflight.md` Procedures 1–4: lock, rename-marker, name sanitization, section probe |
| **Read-only lock** | `.vault-lock.readonly` — multi-reader, blocks vault-wide writers |
| **Regret-recovery window** | 30 days during which `/rollback TICKER` of a closure remains possible |
| **Run token** | Random ID written to the lockfile at Step 0.1 and carried by the LLM for ownership verification |
| **Skill-origin Log prefix** | Registry prefix meaning the producer already propagated; `/sync` skips re-propagation |
| **Tier A / Tier B (sync)** | Destructive edits requiring pre-edit snapshot / Log-only appends (strikethrough-reviewed on rollback) |
| **Watermark** | Last-successful-run timestamp: `.last_sync` mtime (`/sync`), `last_graph_write:` frontmatter (`/graph`) |
| **Delegated skill** | A skill whose heavy read/analysis runs off the main thread via **Agent-tool delegation** (a `general-purpose` subagent runs the work and returns the report; the main thread re-emits it verbatim). NOT frontmatter `context: fork` — that mechanism was reverted 2026-06-07 (unrendered-stdout blank panel). `/surface`, `/retro` delegate fully; `/prune` delegates its analysis half only; `/lint` uses `lint.py` instead. |
| **Section-targeted read** | awk-extracted subset of a thesis (frontmatter + chosen sections + recent Log); ~75-85% cheaper reads |
| **Mode keyword** | Reserved literal skill argument (`all`, `last`, `[N]`) — never collides with ticker/sector names |
| **Mechanical skill** | Structural operations (extraction, find/replace, frontmatter, age math) → Sonnet max |

---

## 1. Vault content files

### 1.1 `_hot.md` — Session context cache

Full contract: `.claude/skills/_shared/hot-md-contract.md`. Key rules:

- **Six-section schema** (load-bearing): `## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`
- **Caps**: soft 8,000 / hard 10,000 words. Over hard cap → abort the `_hot.md` write only; the skill's primary operation proceeds
- **Compression trigger order** over soft cap: drop oldest Sync Archive entry → drop oldest `*Previous:*` line → merge duplicate Open Questions → warn in report. Recent Conviction Changes is NEVER compressed
- **Forbidden truncation markers**: trailing `...`, `[compressed]`, `[truncated]`, unclosed `**`/`*`/backtick — compression drops whole entries, never truncates
- **Same-ticker continuation**: same ticker → append to live thread; different ticker → compress outgoing to one `*Previous YYYY-MM-DD:*` line

Writers (14): `/sync`, `/status`, `/thesis`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/deepen`, `/prune`, `/rollback`, `/catalyst`, `/brief` (ART + OQ only), `/rename` (free-text mentions), `/retro` (ART + OQ only). Enforcement: `/lint #35` (schema), `#42` (truncation markers).

### 1.2 `_graph.md` — Vault dependency map

Owned exclusively by `/graph` (full rebuild, `last` incremental, `[N]` catch-up). Watermark: `last_graph_write:` (ISO second-precision; legacy fallback `date:` at 00:00 UTC).

- **Reverse indexes always rebuild from scratch** on every run — prevents drift even when incremental extraction skips unchanged theses.
- **T7.3 cache fields** (`status:`, `log_tail:` per adjacency entry) let `/sync` classify without re-reading theses. Entries missing them are re-extracted on next `/graph last`.
- **Write-avoidance**: only `/rename` writes `_graph.md` outside `/graph` (adjacency header only; does not advance the watermark). All other skills accumulate into `.graph_invalidations` (§2.3).
- **Auto-refresh hook**: the `Stop` hook `refresh-graph.py` (§14.1) runs `generate_graph.py last` when `.claude/.graph_dirty` is set by a thesis/sector/macro edit — automating core-loop step 4. Runs the generator directly (no skill lock); still `/graph`-owned output.

### 1.3 `_catalyst.md` — Catalyst calendar

Regenerated each `/catalyst` run (next 2 weeks daily, weeks 3-4 weekly, months 2-3 by week; flags gaps and stale events). Pre-regenerate snapshot (batch `catalyst-*`) protects against mid-run web failure; snapshot failure **hard-aborts** — no partial-overwrite path exists.

### 1.4 `Templates/_callouts/` — User feedback templates

Four Templater files inserting dated callouts at cursor; pure user-interaction infrastructure, **not touched by any skill**.

| File | Inserts | Hotkey |
|---|---|---|
| `user-question.md` | `[!question]` yellow ❓ | `Mod+Alt+1` |
| `user-warning.md` | `[!error]` red ⚡ | `Mod+Alt+2` |
| `user-tip.md` | `[!tip]` teal 🔥 | `Mod+Alt+3` |
| `user-todo.md` | `[!todo]` blue ☑ | `Mod+Alt+4` |

`user-warning.md` filename is intentionally decoupled from `[!error]` — the filename is the stable Templater hotkey slot. Companion config (both git-tracked): `.obsidian/hotkeys.json`, `.obsidian/plugins/templater-obsidian/data.json`.

**Gotcha — recreation**: Templater's `trigger_on_file_creation: true` fires on ANY new file with `2026-07-19` syntax; recreating a template via `Write` freezes `undefined` at creation time. Use `Edit` on existing template files.

**Propagation + drift**: callout-addressing must use a non-skill-origin Log prefix (recommended: `Addressed user callouts:`) or `/sync` silently skips sector/macro propagation — full spec in CLAUDE.md Workflow Rule 7 and [[User Guide#Inline callouts — user feedback markers]]. Accumulated `[!error]`-addressing entries count toward `/sync` Step 3e conviction-drift detection (windowing in `sync/SKILL.md §3e` + `_shared/log-prefixes.md`).

### 1.5 `_followups.md` — Open-findings register

Durable ledger of actionable findings that analytical skills cannot execute themselves. Contract: `_shared/followups-contract.md` (§12.2). Writers append one-line entries (`/stress-test`, `/retro`, `/surface`, `/numbers`); resolvers move Open → Resolved (`/status`, `/sync`); auto-created by the first writer; Resolved entries retained 90 days, then `/clean`-eligible. Unlike `_hot.md` it never auto-evicts — closes the finding-dies-in-the-report failure class (the unactioned INTU stress-test).

### 1.6 `_watchers.md` + `Daily Intel/` — automation-layer surfaces

Owned by the n8n layer ([[n8n Automations]]); no vault skill reads or writes either file.

- **`_watchers.md`** — the single registry every n8n workflow re-parses per run: News & Thematic (Workflow 3), Price Tripwires (Workflow 1), X Watchers incl. `### Tuning` thresholds + `### LLM prompt` (Workflow 5), Alt-Data backlog. User/Claude-edited in natural language; a table edit changes what's pulled with no redeploy. Constraint: no aliased wikilinks in cells — the `|` breaks both the table render and the parser.
- **`Daily Intel/`** — write-once dated outputs (X Dashboards, trending digests) from Workflows 3/5; newest file = current dashboard; never hand-edited; scanning surfaces, not ingest candidates.
- **Boundary** (n8n hard rules 1–4): n8n writes only NEW files into `Daily Intel/`, `.data/`, `_Inbox/`; never Theses/Research/Sectors/Macro or metadata files; no Tier 3 operations; lock-aware for any future headless invocation (composes with §6).

---

## 2. Runtime state markers at vault root

All ephemeral and git-ignored. Complete inventory in §11.

### 2.1 `.last_sync` — Sync watermark + idempotency keying

Touched at end of `/sync` (default) and `/sync all`; next run uses `find -newer`. `/sync TICKER` preserves it (first-run exception: creates epoch placeholder). `/graph` never touches it.

**Idempotency keying**: per-thesis propagation check keys on (1) **wikilink presence** in thesis `## Log` (all 5 forms) — terminal once present; (2) rename-resilient fallbacks (`source:` URL, `date:+ticker:` tuple, `tags:`+date) that fire only when the primary misses. Eliminates midnight-rollover duplicates and rename-induced re-propagation. Full mechanics: `sync/RATIONALE.md §1`.

### 2.2 `.sync_all_fresh` — Full-rebuild signal

Written by `/sync all`; read by `/graph` pre-watermark check → forces full rebuild → deleted after successful write. Closes the gap where `/sync all` triage leaves "No delta" thesis mtimes untouched. `/lint #38` ages stale markers.

### 2.3 `.graph_invalidations` — Deferred graph update list

Appended on thesis closure by `/status` and `/prune`: relative paths of neighbor theses whose `cross-thesis:` references went stale. Consumed and deleted by `/graph last`. Dedup via `sort -u`.

### 2.4 `.rename_incomplete.TICKER` — Failed-rename repair marker

Written by `/rename` when wikilink Edits fail after the `mv`. Frontmatter: `ticker`, `old_name`, `new_name`, `batch_id`, `failed_files:`. Per-ticker filename so concurrent repairs coexist.

Consumers: ticker-scoped skills hard-block on their ticker's marker; vault-wide skills hard-block on ANY marker (exceptions: `/lint`, `/rollback` list, `/graph`, `/rename` itself, `/ingest` advisory-only). **Cross-new_name guard**: a re-run proposing a different `new_name:` aborts. Repair: re-run `/rename TICKER "[same new_name]"` — mv skipped, failed Edits retried, marker shrinks monotonically, auto-deletes when empty. `/lint #37` surfaces.

### 2.5 `.archive_ticker_registry.md` — Archive lookup

Append-only log of archival events (`/status`, `/prune`): `TICKER|archived_filename.md|YYYY-MM-DD|conviction|rationale`. Consumed by `/thesis` archive-collision Signal C (catches renamed-then-archived theses). Stale entries tolerated — `/thesis` verifies existence. `/lint #46` validates.

### 2.6 `.vault-lock*` — Concurrency locks

Three patterns: `.vault-lock` (vault-wide), `.vault-lock.TICKER` (per-ticker; `/compare` acquires N), `.vault-lock.readonly` (multi-reader, blocks writers). Full contract in §6.

### 2.7 `.drift-config.md` (optional) — Drift tuning

User-authored override for `/sync` Step 3e drift heuristics:
```yaml
---
window_size: 5                 # min 3, max 10
base_threshold: 3              # weakening entries in window fires drift
post_stress_threshold: 4       # within 30 days of stress test
post_stress_window_days: 30
deepened_exclusion_days: 14
---
```
Missing → defaults. Malformed → warning + defaults. Rationale: `sync/RATIONALE.md §8`.

---

## 3. Snapshots & transaction manifests

Multi-file skills use **skeleton → populate → flip**: manifest written BEFORE any destructive mutation, populated at phase boundaries, flipped to `status: completed` last. An `in-progress` manifest signals a crash or missed flip.

### 3.1 `_Archive/Snapshots/` — Version control

Snapshot producers: `/sync` (Tier A), `/deepen`, `/status` (except draft→active and reaffirm), `/compare`, `/prune`, `/catalyst`, `/rollback`, `/rename`, `/archive-callouts`. Batch ID `<trigger>-YYYY-MM-DD-HHMMSS`; `/rollback` cascade detection matches by batch prefix.

**Orphan protection**: snapshots whose `snapshot_of:` source is missing default to PROTECTED by `/clean`; explicit opt-in via `/clean orphans` or `--include-orphans`.

### 3.2 Manifest catalogue

All at `_Archive/Snapshots/_<type>-manifest (<type>-*).md` with `type:`, `status: in-progress | completed | rolled-back`, `batch:`, `date:`, `completed_date:`.

| Manifest | Producer (skeleton → flip) | `/rollback` | `/lint` | Notes |
|---|---|---|---|---|
| `_prune-manifest` | `/prune` Stage 1 → Stage 4 | 2.5a generic | #36 | Records closures, upgrades, sectors, neighbors (populated Stage 4.5). Manifest-first ordering binds the 30-day floor before snapshots exist |
| `_sync-manifest` | `/sync` Step 2.9 → 7.5 | 2.5b | #41 | Phase checkpoints at Steps 3/4/5. Tier B Log entries surfaced for strikethrough during cascade |
| `_compare-manifest` | `/compare` Phase 5.0 → 5.5c | — | #45 | `status: rolled-back` when sector-edit atomicity fires |
| `_stress-test-manifest` | `/stress-test` Phase 4.0 → 4.6 | 2.5d | #47 | Records the Log entry appended (no snapshot — append-only) |
| `_status-manifest` | `/status` Step 3.0.5 → flip | 2.5e | #48 | Records frontmatter change, sector edit, archive move, invalidations. Reaffirm skips the manifest. Closure variant (`new_value:` contains `closed`) binds the 30-day floor |
| `_thesis-manifest` | `/thesis` Step 3.5 → flip | 2.5f | #49 | Cascade is **deletion-based** (new files, not snapshot restore) |
| `_deepen-manifest` | `/deepen` Phase 4.5 → 7.5 | 2.5g | #50m | Records section, pre-deepen snapshot, Log outcome, supporting research note |

**Aging**: `in-progress` → Important (crash signal); `completed` → aged per 90/180-day tiers by the paired `/lint` check; `/clean` removes only after both the requested age AND any manifest-specific floor.

**Closure-snapshot 30-day floor (universal — `/clean` Step 2d)**: pre-closure thesis snapshots from `/prune` Stage 1 or `/status active→closed` are PROTECTED across ALL `/clean` modes for 30 days from the matching manifest's `completed_date:` (cross-referenced by `snapshot_batch:` ↔ `batch:`; in-progress manifests' snapshots also protected). Cannot be flag-overridden — the only paths are waiting out the floor or manual `rm` (which forfeits `/rollback TICKER`).

---

## 4. Content-quality gate (`/ingest`)

URL and PDF ingests block on failure; manual local files get advisory logs only.

**Structural**: ≥150-word body; no paywall/CAPTCHA sentinels; ≥2 of 4 expected sections populated.

**Domain-specific by `source_type:`**:

| `source_type` | Requirements |
|---|---|
| `earnings` | Period tokens (Q1–Q4/FY20XX) + 2+ currency figures + ticker reference |
| `analyst-report` | Rating token + price-target reference + ticker |
| `news` | Ticker + dated event reference |
| `deep-dive` | ≥500 words + ≥3 substantive sections |
| `web-clip`, `data` | Skip domain checks |

**Integrity**: numerical OCR-corruption detection (O-as-zero, `$1 5B`, `II`-as-`11`); title-URL Jaccard ≥50% (catches redirects to login/subscribe pages).

**Failure handling**: failed gate → research note deleted, source retained for re-ingest. Blocks paywalled/wrong-content URLs from propagating into thesis Logs via `/sync`.

**Source-URL dedup**: exact-match grep against `Research/*.md` `source:`. Same-day → hard-block; cross-day → skip/re-ingest/cancel prompt. Batch mode uses `_Inbox/processed/` filename guard.

---

## 5. Producer contracts & atomicity

### 5.1 `propagated_to:` — the atomicity signal

Research notes from `/scenario`, `/stress-test`, `/compare`, `/deepen` carry `propagated_to:` listing tickers whose Logs received propagation. Written ONLY after all Log appends succeed; partial failure → field omitted → `/sync` retries file-direct.

**Terminal signal**: `synthesis`, `brief`, and `retrospective` notes carry `propagated_to: []` — their body wikilinks reference many theses as context, not per-thesis evidence; the empty list blocks `/sync` from circular self-propagation. Case handling: `sync/SKILL.md §1.7`; mechanics: `sync/RATIONALE.md §1.5-1.6`.

### 5.2 `/lint #39` — producer contract verification

| `source_type` | Requirement | Severity if missing |
|---|---|---|
| `synthesis`, `brief`, `retrospective` | Must be `[]` | Important |
| `scenario`, `stress-test`, `comparison` | Present unless atomicity rule fired | Important (≥2026-04-19); Nice to Have pre-spec |
| Others | None | — |

Cross-checks with `/lint #1`; notes flagged by both are the strongest cleanup candidates.

### 5.3 Cross-skill classification & approval gates

| Skill | Gate | Purpose |
|---|---|---|
| `/thesis` Step 1.2 | Multi-signal archive collision (filename glob, `ticker:` frontmatter, registry, snapshot `snapshot_of:`) | Prevent duplicate theses; on match: rollback / new-suffix / proceed-dual / cancel |
| `/thesis` Step 5 | New-sector handling | Unresolvable `sector:` → prompt (scaffold / proceed / cancel); no silent skip |
| `/scenario` Phase 6.1.5 | Major/Minor/Neutral classification approval | User review before any Log write |
| `/scenario reverse` | Archive-aware iteration | Live theses get `Scenario REVERSED` Log; archived theses get `## Reversal Notes` in the scenario note (Tier 3 protection) |
| `/rollback` closure cascade | H3 neighbor-citation scan | Classifies premise-dependent vs contextual `[[TICKER]]` citations in Macro/Sector prose; surfaces for manual review, never auto-edits |

---

## 6. Locks (deep-dive)

### 6.1 Canonical procedures (`_shared/preflight.md`)

| Procedure | Purpose |
|---|---|
| 1 — Acquisition | Lockfile at Step 0.1 with token, skill, scope, timeouts |
| 1.5 — Ownership verification | Every subsequent Bash block checks the lockfile `token:` against the run token; mismatch → abort (`LOCK_LOST`) |
| 2 — Rename-marker check | Hard-block per §2.4 |
| 3 — Name sanitization | Whitelist + NFC for user-supplied filenames; rejects `/\:*?"<>|`, leading dot, reserved names, length >100 |
| 4 — Section existence probe | Abort if the target `## Heading` is absent |

Release at the skill's final Bash block: `rm -f "$LOCK_FILE"`.

### 6.2 Design rationale

- **Token-based, not PID-based**: each Bash block is a fresh subshell; the LLM carries the token as a literal string across tool calls.
- **Explicit release, not trap-based**: traps don't survive across blocks. Mid-run abort → stale lock → `/lint #43` surfaces for manual recovery.
- **No auto-steal**: timeout stealing would race legitimately long runs (web research, `/sync all`). Manual recovery is the safer default.

### 6.3 Multi-ticker partial-acquisition rollback (`/compare`)

`/compare A vs B vs C` acquires per-ticker locks sequentially. Any failure → release already-acquired locks in reverse order, abort with `Partial lock acquisition failed on TICKER`. Per-ticker lockfiles (not `+`-delimited) handle hyphenated tickers (`BRK-B`, `BF-A`).

---

## 7. Rollback cascade catalogue

`/rollback` reads the manifest (§3.2) to offer atomic restore.

| Step | Trigger | Options |
|---|---|---|
| 2.5a | Generic `snapshot_batch:` prefix lookup (base path for every trigger) | Cascade all / single / cancel |
| 2.5b | `_sync-manifest` | Tier B Log review: surface-only / cascade + strikethrough / single / cancel |
| 2.5c | Non-manifest triggers (`/catalyst`, `/rename`, `/rollback` safety nets, `/archive-callouts`) | 2.5a generic — Tier A only |
| 2.5d | `_stress-test-manifest` | Surface only / cascade + strikethrough Log entry / cancel |
| 2.5e | `_status-manifest` | Thesis-only / full transaction (thesis + sector + un-archive + clear invalidations) / cancel |
| 2.5f | `_thesis-manifest` | Delete thesis only / full cascade (delete + revert sector + `_hot.md` + orphan mtimes) / cancel. **Deletion-based** |
| 2.5g | `_deepen-manifest` | Restore thesis (research note preserved) / full cascade (+ delete research note) / cancel |
| — | `_prune-manifest` | 2.5a batch cascade; 30-day regret window; Step 6.2.5 intervening-entries scan on reopened theses |
| — | `snapshot_trigger: rename` | Symmetric reverse-`/rename` (recommended) / content-only restore (creates duplicate) / cancel |

### 7.1 Intervening-entries scan (closed theses, Step 6.2.5)

When rolling back a closure, scan neighbor theses + Macro + Sector notes for post-closure entries/prose referencing the closed thesis. Options: surface-only / auto-strikethrough `Cross-thesis closure:` entries (premise-dependent) / auto-strikethrough all / skip.

---

## 8. `/graph last` cost model

| Vault state | Work |
|---|---|
| Nothing changed, no invalidations | Skip — zero reads |
| 1-5 theses changed | Re-extract those + read sector/macro files for reverse indexes |
| 30+ theses changed | Approaches full-rebuild cost |

Watermark is ISO second-precision (`last_graph_write:`); legacy files fall back to `date:` at 00:00 UTC and upgrade on next write. Same-minute double-runs waste compute but stay idempotent.

---

## 9. `/rename` atomicity details

- **Wikilink patterns (7)**: `[[TICKER - Old]]`, `[[TICKER - Old.md]]`, `[[TICKER - Old|alias]]`, `[[Theses/...]]` (±`.md`), `[[_Archive/...]]` (±`.md`) — the 5-form contract plus 2 archive variants for archived-then-renamed theses.
- **Pre-flight Read/Write probe (Step 3.5)**: reads every file with an inbound wikilink; any unreachable → abort BEFORE the `mv`. No partial state.
- **Cross-`new_name` guard (Step 1.4.5)**: existing marker with matching `new_name` → repair mode (skip mv, retry Edits); different → abort ("in-flight rename conflict").
- **Post-mv Edit failure**: writes `.rename_incomplete.TICKER` (§2.4); re-runs shrink it monotonically to auto-delete. `/lint #37` surfaces.

---

## 10. `/lint` registry (by ID)

Key checks (the full registry runs #1–#66, ~64 active — `#31`/`#40` unused; `#50m` for `_deepen-manifest` distinct from `#50` callout-sweep-freshness — see `lint/SKILL.md`). Scoped mode always runs #35 and, if a marker exists, #37.

| ID | Scope | Catches | Severity | If fires, suspect |
|---|---|---|---|---|
| #1 | Full | Research note without `propagated_to:` AND no thesis Log reference | Important | `/sync` never ran or crashed mid-propagation |
| #16 | Full | Stale snapshots (>180 days) | Nice to Have | `/clean` never run |
| #18/#20/#23 | Full | Graph health (existence, staleness, missing/ghost entries) | Important | `/graph last` not run after recent work |
| #29 | Full | Log-prefix registry vs consumer drift | Important | Prefix changed without registry update |
| #30 | Scoped | Sector-resolution coverage per thesis | Important if `none` | `sector:` drift or missing scaffold |
| #32 | Full | Orphaned ticker refs | Nice to Have | Archive bypassed `/status closed`; `ticker:` typo |
| #33 | Full | Closed thesis still in `Theses/` | Important | `/status` crashed before archive `mv` |
| #34 | Full | Sector frontmatter standardization | Nice to Have | Typo/case divergence |
| #35 | Both | `_hot.md` schema drift | Important (silent no-op source) | Manual edit removed a heading |
| #36 | Full | `_prune-manifest` state | Important if in-progress | `/prune` crashed before flip |
| #37 | Both | `.rename_incomplete.*` markers | Important | Re-run `/rename` to repair |
| #38 | Full | State-marker hygiene (`.sync_all_fresh`, `.graph_invalidations` aging) | Nice to Have | `/graph` not run after `/sync all` |
| #39 | Full | `propagated_to:` producer contract (§5.2) | Important post-spec | Producer crashed mid-propagation |
| #41 | Full | `_sync-manifest` aging | Important if in-progress | Read the Step 3/4/5 checkpoints in the manifest body (no `phase:` field exists) |
| #42 | Both | `_hot.md` truncation markers | Important | Legacy compaction or manual edit |
| #43 | Full | Stale locks | Nice to Have | Skill crashed without release |
| #45 | Full | `_compare-manifest` aging | Important if in-progress | Crashed before atomicity flip |
| #46 | Full | `.archive_ticker_registry.md` validation | Nice to Have | Stale entries (tolerated) |
| #47 | Full | `_stress-test-manifest` aging | Important if in-progress | Crashed before flip |
| #48 | Full | `_status-manifest` aging | Important if in-progress | Crashed between skeleton and flip |
| #49 | Full | `_thesis-manifest` aging | Important if in-progress | Check whether the thesis file was created |
| #50m | Full | `_deepen-manifest` aging | Important if in-progress | Crashed before Phase 7.5 flip (ID is `#50m`, distinct from callout `#50`) |
| #50–#53, #56 | Both | Callout hygiene: sweep freshness (#50), stale fresh callouts (#51), malformed/orphan Legacy entries (#52/#53), deprecated `[[preserve]]` (#56) | Varies | See `lint/SKILL.md` |
| #54/#55 | Full | Graph-primer compliance / filter anti-pattern | Important | Skill used graph to skip content reads |
| #57 | Full | Watermark collapse (pending-sync > 20% of vault notes) | **Critical** | Bulk mtime touch (git ops) or stuck `.last_sync` — /sync default/all intractable, /prune blocks, /clean over-protects; decide sync-all vs advance |
| #58 | Full | Snapshot integrity: missing `snapshot_of:`/`snapshot_date:` frontmatter; non-.md artifacts in Snapshots/ | Important | Legacy/hand-made snapshot or stray archive file — invisible to /clean, unrestorable-by-spec for /rollback |
| #59 | Full | Template-drift-at-birth (thesis <7d old missing template sections) | Important | /thesis section list drifted from `Templates/` on that run — fix thesis via /deepen scaffold + check /thesis spec |
| #60 | Full | `## Conviction Triggers` present-but-unfilled scaffold, or filled with no falsifiable numeric/dated/named threshold | Important / Nice | `/thesis` scaffold never filled — the precondition `_shared/trigger-touch.md` depends on |
| #61 | Full | `key_metrics_last_refreshed:` missing or >90d | Important (high-conviction active) | `/numbers` not run recently — Step 11 writes the field |
| #62–#66 | Full | Analytical tier: non-consensus insight names no consensus (#62), Mental-Models stable-ID citations (#63), hedge words in spines (#64), Summary-vs-frontmatter conviction mismatch (#65), weakly-sourced spine figures (#66 — pairs with `provenance-tags.md`) | Nice / candidate | See `lint/SKILL.md` |

---

## 11. Vault root hidden files — complete inventory

### 11.1 Static infrastructure directories

| Entry | Purpose | Git |
|---|---|---|
| `.git/` | Repository metadata | Self |
| `.claude/` | Harness: `agents/`, `commands/`, `settings.json` (ignored), `skills/` (21 skills + `_shared/`), `hooks/` (§14.1), `schedule/` (§14.2), `workflows/` (§14.3) | Partial |
| `.claudian/` | Claudian plugin state; not read/written by any skill | Ignored |
| `.obsidian/` | Obsidian config; personal UI state ignored, shared config (plugins, hotkeys) tracked | Partial |
| `.data/` | FMP key (`config.json`) + X-harvester state/archive (machine-local, disposable — [[n8n Automations]] §8.4) | Ignored |

Skills never commit — commits are user-initiated (obsidian-git may auto-commit per user config).

### 11.2 Version control and OS files

`.gitignore` is the **authoritative runtime-marker registry** — adding a new ephemeral marker requires updating the producing skill's spec AND `.gitignore` AND §2 AND the Appendix. Currently ignored markers: `.last_sync`, `.sync_all_fresh`, `.graph_invalidations`, `.vault-lock*`, `.rename_incomplete.*`, `.claude/.graph_dirty` (§14.1), `.claude/.allow-protected` (§14.1 guard escape hatch), `.claude/schedule/logs/` (§14.2). Intentionally NOT ignored (persistent content): `.archive_ticker_registry.md`, `.drift-config.md`. `.gitattributes` normalizes line endings; `.DS_Store` is ignored macOS noise.

### 11.3 Reserved / optional markers

| Marker | Status |
|---|---|
| `.drift-config.md` | Optional, user-authored (§2.7) |
| `.archive_ticker_registry.md` | Auto-maintained, append-only (§2.5) |
| `.sync-progress.jsonl` | **Reserved, not implemented** — namespace claimed in `sync/RATIONALE.md §5.3.1` |

### 11.4 Causal dependency chains

1. **Sync → Graph**: `/sync all` writes `.sync_all_fresh` → `/graph` forces full rebuild → deletes marker.
2. **Sync → Sync**: `.last_sync` touched end-of-run (except ticker-scoped) → next `/sync` uses `find -newer`.
3. **Closure → Graph**: `/status`/`/prune` append `.graph_invalidations` → `/graph last` consumes → deletes.
4. **Rename → ticker skills**: partial Edit failure writes `.rename_incomplete.TICKER` → consumers hard-block → repair shrinks → auto-delete.
5. **Locking**: Step 0.1 writes `.vault-lock*` → blocks verify `token:` → final block releases. Abandonment → stale lock → `/lint #43`.

### 11.5 Adding a new hidden marker — checklist

1. Spec the contract in the producing skill's SKILL.md (writer, reader, deletion, absence-vs-presence semantics)
2. Add to `.gitignore` with provenance comment
3. Add a §2 subsection here
4. Add an Appendix ownership-matrix row
5. Add a `/lint` check if the marker can accumulate stale state
6. Add to User Guide §14 if user-visible

Skipping any surface produces silent drift.

---

## 12. Skill-layer architecture

Load semantics: every byte of `SKILL.md` is paid per invocation; `_shared/*.md` is paid only when explicitly Read; `RATIONALE.md` is free at runtime.

### 12.1 Three file kinds

| Kind | Auto-loaded? | Read at runtime? |
|---|---|---|
| `SKILL.md` | **Yes** — injected on invocation | Already in prompt |
| `_shared/*.md` | No | On explicit Read; skills inline critical procedures |
| `RATIONALE.md` | No | Rarely — for maintainers, not execution |

**Execution context directive (2026-07-08)**: heavy read/analysis is routed off the main thread via **Agent-tool delegation** (SKILL.md "Execution context" section instructs the skill to spawn one `general-purpose` subagent that runs the work and returns the report; the main thread re-emits it verbatim). This replaced frontmatter `context: fork` + `agent: general-purpose`, which was reverted 2026-06-07 because the harness returned the report as unrendered stdout (blank panel). Current state: `/surface`, `/retro` delegate their whole run; `/prune` delegates only its read/analysis half (mutations + approval gate stay in the main thread); `/lint` instead moved its ~40 mechanical checks into `lint.py` and reads only flagged files; `/catalyst` still runs inline (its live-progress contract conflicts with delegation — pending decision).

### 12.2 Shared contracts catalog

Ten contracts under `.claude/skills/_shared/` (plus the shared helper scripts `extract_sections.py`, and the per-skill helpers `verify_note.py`/`extract_transcript_signals.py`/`numbers_compute.py`/`generate_graph.py`/`lint.py`). Editing any contract requires coordinated consumer updates (§12.4).

| Contract | Purpose | Consumers | `/lint` |
|---|---|---|---|
| `preflight.md` | Lock acquisition/verification, rename-marker check, name sanitization, section probe | Every state-modifying skill | #43 |
| `log-prefixes.md` | Registry of Log prefixes with producer/consumer bindings | `/sync` (classification + drift), `/retro`, `/lint`, every producer | #29 |
| `hot-md-contract.md` | Section budgets, caps, compression order, same-ticker continuation | 14 writers (§1.1) | #35, #42 |
| `mental-models-section.md` | `## Mental Models` section merge contract (fired triggers as hypotheses, not verdicts) | `/ingest` (identifies), `/sync`, `/deepen` (merge) | — |
| `sector-resolution.md` | `sector:` → sector-note ladder (exact → normalized → substring → ask) | `/status`, `/thesis`, `/compare`, `/prune`, `/rollback`, `/rename` | #30, #34 |
| `wikilink-forms.md` | 5 canonical wikilink forms | `/sync`, `/rollback`, `/prune`, `/lint` | #23 |
| `graph-primer.md` | `_graph.md` as primer (orient reads), never filter (skip reads) | `/ingest`, `/compare`, `/thesis`, `/stress-test`, `/brief`, `/deepen`, `/scenario`, `/surface`, `/retro` | #54, #55 |
| `followups-contract.md` | `_followups.md` open-findings register — durable ledger of actionable findings (writers append, resolvers move Open→Resolved) | Writers: `/stress-test`, `/retro`, `/surface`, `/numbers`; resolvers: `/status`, `/sync` | — |
| `provenance-tags.md` | Inline source tags on quantitative claims (`[1×: …]`, `[FMP]`, `[N sources]`) so sourcing travels with the number through propagation | `/ingest`, `/deepen`, `/transcript` (writers), `/sync` (preserver), `verify_note.py` check #16 | — |
| `trigger-touch.md` | Diff NEW datapoints against `## Conviction Triggers`; mandatory `Trigger touch:` report line on any touch/cross | `/numbers` (5b), `/transcript` (6.3), `/sync` (3e), `/deepen` (Phase 3), `/ingest` (Step 1) | — |

Producer divergence from a contract without consumer updates → silent failures (races, misclassified Log entries, truncated sections, missed wikilink matches).

### 12.3 RATIONALE.md pattern

15 skills have one: `sync`, `graph`, `lint`, `status`, `scenario`, `compare`, `thesis`, `rename`, `prune`, `rollback`, `archive-callouts`, `deepen`, `ingest`, `stress-test`, `surface`. Extract when rationale blocks exceed ~20% of SKILL.md with no execution impact.

**Stays in SKILL.md**: operational rules, Log messages, critical-path Bash, error/abort messages. **Moves to RATIONALE.md**: historical context, edge-case trade-offs, "why A over B" dialectics, benchmarks.

Reference format: `§N.M` for same-file/RATIONALE refs; `registry §N` for log-prefixes entries; `_shared/<contract>.md §N` otherwise.

### 12.4 Editing protocol

1. **SKILL.md only**: edit, run `/lint` for the affected skill, commit.
2. **`_shared/*.md` only**: edit contract, grep all consumers, verify each, run paired `/lint` checks, commit.
3. **Both**: contract FIRST, then consumers — intermediate state stays self-consistent.
4. **RATIONALE.md**: free-form, independent commits.
5. **New contract**: update §12.2 + all consumer SKILL.md files + add a `/lint` check if drift detection is warranted.
6. **New RATIONALE.md**: update §12.3.

### 12.5 Cross-skill contract-consumption graph

```
  preflight.md ◄──── every state-modifying skill at Step 0
  log-prefixes.md ◄─ /sync (Step 2.5 + 3e), /retro, /lint (#29), all producers
  hot-md-contract.md ◄── 14 writers (§1.1), /lint (#35, #42)
  graph-primer.md ◄──── 9 consumers (§12.2), /lint (#54, #55)
  sector-resolution.md ◄ /status, /thesis, /compare, /prune, /rollback, /rename, /lint (#30, #34)
  wikilink-forms.md ◄─── /sync, /rollback, /prune, /lint (#23)
  followups-contract.md ◄ writers /stress-test /retro /surface /numbers · resolvers /status /sync
  provenance-tags.md ◄── /ingest, /deepen, /transcript, /sync, verify_note.py (#16)
  trigger-touch.md ◄──── /numbers, /transcript, /sync, /deepen, /ingest
```

Adding a consumer: update this graph + add the paired `/lint` check in the same commit.

### 12.6 Performance architecture

Dated rollout narratives and measured-impact tables live in [[_Archive/Docs/Changelog.md]] and per-skill RATIONALE.md files. The durable design decisions:

- **Forked context (5 skills)** — `/lint`, `/prune`, `/surface`, `/catalyst`, `/retro`: reads dominate but output is bounded, so the vault-read budget stays off main context (e.g. unscoped `/surface`: ~380K → ~15K main-context tokens). Trade-off: intermediate reasoning is discarded (invariant #11); re-run scoped if a follow-up needs it.
- **Section-targeted reads** — `/surface` default and `/catalyst` Phase 1 read only high-signal sections (Summary, Key Non-consensus Insights, Risks, Catalysts + recent Log) at ~25% of full-read cost. `/surface all` preserves full reads for quarterly deep review. Surface notes carry `scope:` frontmatter so deep-scans are distinguishable.
- **Sonnet for mechanical skills** — `/graph`, `/rename`, `/rollback`, `/status`, `/clean`, `/archive-callouts` (all max), `/numbers` (effort `medium` — arithmetic delegated to `numbers_compute.py`) (~40-60% faster). **Watch list** (first to revert if Sonnet underperforms): `/status` trigger-conflict detection; `/rollback` cascade classification. Revert = one-line `model:` frontmatter change.
- **Parallel-batch reads** — independent multi-file reads issue as one parallel tool-call batch, not serial loops. Pattern B (Bash+awk pre-extraction) is accepted only for mechanical skills (`/lint` set-diff, `/clean` metadata); it was rejected for analytical skills because tool-level narrowing blinds the LLM to out-of-section signal.
- **`/status` draft→active fast-path** — bypasses the Tier 3 confirm (additive, no analytical change, trivially reversible); all manifest/Log/sector machinery unchanged.

Safety envelope for all of the above: lock contract, manifest skeleton→flip, `_hot.md` schema, `propagated_to:` atomicity, `_graph.md` single-owner, and the fork report-only contract are untouched — optimizations apply to read phases and prompts only.

---

## 13. Common debugging flows

Symptom-first recipes: diagnose → fix → verify.

### 13.1 Skill silently no-op'd on `_hot.md`
`/lint #35` surfaces missing section headings. Fix: manually insert the missing heading (§1.1) with no body — skills populate content but never add headings (schema ownership stays with `/lint`).

### 13.2 `/sync` didn't propagate a manual thesis edit
Most-recent Log entry uses a skill-origin prefix → Step 2.5 classified it skill-origin and skipped. Fix: append a non-skill-origin entry (`Manual edit:`, `Reviewed:`, `Refined:`), re-run `/sync`. Verify: sector `## Active Theses` description updates. See CLAUDE.md Workflow Rule 6.

### 13.3 `/graph last` missed theses after `/sync all`
`.sync_all_fresh` present → `/graph` hasn't consumed it; absent → consumed without rebuilding "No delta" theses (§2.2). Fix: run `/graph` (full). Verify: `last_graph_write:` advances; spot-check a "No delta" thesis's adjacency.

### 13.4 `/clean` refused to delete a snapshot
Closure floor (`snapshot_trigger: prune`, or `status` + `new_value: closed`) or orphan protection (§3.2). Fix: wait out the floor, or manual `rm` (forfeits `/rollback TICKER`).

### 13.5 Lock acquisition failed
`ls .vault-lock*`; read `timeout_at:` (past = stale) and `skill:`. Live → wait; stale → `rm -f`. `LOCK_LOST` mid-run → lock was seized or removed; abort and re-run. No auto-steal (§6.2).

### 13.6 Manifest stuck `in-progress`
Read `batch:`, `date:`, `phase:` to locate the crash. Recoverable → `/rollback` matches the batch and offers cascade. Not worth recovering → delete the manifest after confirming no destructive edits landed, re-run. False positive (all edits landed, flip missed) → manually set `status: completed`.

### 13.7 `/sync` re-propagated a research note next day
Wikilink form drift (all 5 forms must match) or a rename where the secondary keys didn't fire. Fix: align with `wikilink-forms.md`; `/lint #1 + #39` cross-check surfaces rename misses. See `sync/RATIONALE.md §1`.

### 13.8 `/rename` partial failure
`.rename_incomplete.TICKER` present. Re-run `/rename TICKER "[same new_name]"` — repair mode retries failed Edits until the marker auto-deletes. Different `new_name` → aborts (§9). Verify: `/lint #37` clean.

### 13.9 `propagated_to:` missing on a producer's note
Producer crashed mid-propagation (§5.2). If all Log appends landed → manually add the field. If partial → re-run the producer (wikilink dedup skips already-propagated tickers).

### 13.10 Sector note never updated by a skill
`sector:` resolves to `none` (`⚠️ No sector note found matching sector:`). Fix: align thesis `sector:` with the canonical note name, or create `Sectors/[name].md` from template. Verify: `/lint #30`/`#34` pass.

### 13.11 `/retro` returned every ticker as `data-gap`
WebSearch rate-limited during Phase 3 (3 queries/ticker ≈ ~126 for a full universe). Fix: wait 5-10 minutes, re-run — output is immutable, so the retry creates a new note with counter suffix. A SINGLE `data-gap` ticker among healthy peers is the per-channel fallback (thin/sanctioned/renamed ticker), not rate-limiting — no action.

---

## 14. Harness automation layer (hooks · schedule · workflows)

Three automation surfaces under `.claude/` (added 2026-07-22). Unlike the skill layer (model-driven, one invocation per request), these are **harness- or OS-driven** — they fire on lifecycle events or a clock with no prompt. Scripts are git-tracked and portable; `settings.json` hooks and the installed launchd plists are per-machine.

### 14.1 Hooks — `.claude/hooks/` + `settings.json` `hooks`

Deterministic shell commands the harness runs on lifecycle events (not model-judged). Three registered:

| Hook | Event · matcher | Script | Effect |
|---|---|---|---|
| Tier-1 guard | `PreToolUse` · `Write\|Edit\|MultiEdit` | `guard-protected.py` | Denies writes to `CLAUDE.md`, `Templates/`, `.obsidian/`, `.claude/skills/` (mirrors Change-Safety Tier 1). Emits `hookSpecificOutput.permissionDecision: deny`. |
| Graph dirty-flag | `PostToolUse` · `Write\|Edit\|MultiEdit` | `mark-graph-dirty.py` | Touches `.claude/.graph_dirty` when a `Theses/`, `Sectors/`, or `Macro & Technology/` `.md` is written. Fast, no scan. |
| Graph refresh | `Stop` | `refresh-graph.py` | If `.graph_dirty` exists, runs `generate_graph.py last`, clears the flag. Debounced — one rebuild per turn regardless of edit count. |

**Design invariants**:
- **Fail-open** — guard parse errors → allow. A guard that misfires must never block legitimate work.
- **Escape hatches** (protected set mirrors CLAUDE.md Tier 1) — two, checked at fire-time before the deny path:
  - `CLAUDE_VAULT_ALLOW_PROTECTED=1` (shell env or `settings.json` `env`) — session-wide, set at launch. Use to disable the guard entirely for a working session.
  - `.claude/.allow-protected` sentinel file — mid-session, per-request. Claude drops it (`touch`) on an *explicit* user request to edit a guarded file, makes the edit, removes it. The `Stop` hook (`refresh-graph.py`) deletes it at turn end regardless, so the guard re-arms every turn. This is what makes "edit CLAUDE.md to add X" work without a restart while still blocking accidental/unrequested edits (git-ignored, §11.2).
- **Debounce, not eager** — PostToolUse only marks; the ~80-note scan runs once at `Stop`, never per-edit.
- **No stop-loop** — `refresh-graph.py` emits only `systemMessage` (never `decision:block` / `continue:false`), so it cannot re-trigger itself.
- **Single-owner nuance** (invariant #5) — the refresh hook runs the `/graph` engine (`generate_graph.py`) directly, WITHOUT the skill's vault lock. Sanctioned because the generator is deterministic (same vault state → identical bytes); a rare race with a manual `/graph` self-heals. `_graph.md`'s logical owner is still `/graph`.

**Watcher caveat**: a newly-edited `hooks` block loads only when the settings watcher re-reads `.claude/` — open `/hooks` once or restart. `settings.json` is git-ignored (§11.1), so hooks are per-machine; the scripts are tracked.

**`.graph_dirty`** — ephemeral marker at `.claude/.graph_dirty` (git-ignored, §11.2). Presence = a graph-relevant note was edited this turn. Created by `mark-graph-dirty.py`, consumed + deleted by `refresh-graph.py`. Complements `.graph_invalidations` (§2.3): closures still route through that path; `.graph_dirty` closes the routine edit→graph-drift gap that previously needed a manual `/graph last` (core-loop step 4).

### 14.2 Local scheduler — `.claude/schedule/` + launchd

Weekly unattended skill runs via macOS launchd. Chosen over cloud `/schedule` routines because the vault is local-first: launchd runs against the LIVE local files with the skills' own lock/snapshot machinery intact, needing no GitHub sync, cloud environment, or GitHub App.

| Component | Path | Role |
|---|---|---|
| Runner | `.claude/schedule/run-vault-skill.sh <skill> [model]` | `cd`s vault, sets PATH, runs `claude -p "/<skill>" --model <m> --dangerously-skip-permissions`, appends `logs/<skill>.log`. Branches on skill (below) |
| Lint publisher | `.claude/schedule/publish-lint-note.py` | `/lint` runs with `--output-format json`; this extracts the final report and writes `Daily Intel/<date> - Vault Health - lint.md` so the headless run is visible in Obsidian. Defensive: writes a fallback note pointing at the log if extraction fails |
| Job — catalyst | `~/Library/LaunchAgents/com.investmentvault.catalyst.plist` | Sunday 18:00 local → `/catalyst` (opus) |
| Job — lint | `~/Library/LaunchAgents/com.investmentvault.lint.plist` | Sunday 20:00 local → `/lint` (sonnet), 2 h after catalyst so they never overlap |
| Canonical plists | `.claude/schedule/com.investmentvault.*.plist` | Git-tracked reference copies; installed copies live in `~/Library/LaunchAgents/` |

- **Output visibility** — `/catalyst` writes its own durable artifact (`_catalyst.md`), so its run narration just goes to the log. `/lint` is a read-only report with no artifact, so the runner captures its clean output and publishes `Daily Intel/<date> - Vault Health - lint.md` (via `publish-lint-note.py`) — the report surfaces in Obsidian's morning-scan folder instead of dying in a log. Pruned by `/clean daily-intel`.
- **Permission bypass** — unattended runs use `--dangerously-skip-permissions` (personal machine, own skills, no human to answer prompts). Tighten by swapping to `--permission-mode acceptEdits` + a Bash allowlist.
- **Lock coordination** — scheduled runs execute each skill's pre-flight (§6), so they serialize safely against a live interactive session rather than racing it.
- **Sleep behavior** — `StartCalendarInterval` coalesces missed runs: Mac asleep at the scheduled time → the job fires once on next wake.
- **Manage** — `launchctl list | grep investmentvault` (status); `launchctl bootout gui/$(id -u) <plist>` (disable); edit the plist `Hour`/`Weekday`, then `launchctl bootstrap gui/$(id -u) <plist>` (reschedule).
- **Test before trusting** — run `.claude/schedule/run-vault-skill.sh catalyst` manually once and inspect `.claude/schedule/logs/catalyst.log`.

### 14.3 Workflows — `.claude/workflows/`

Deterministic multi-agent orchestration scripts (the `Workflow` tool) for expensive parallelizable sweeps the single-thread skills don't cover.

| Workflow | File | Shape |
|---|---|---|
| `portfolio-stress-test` | `portfolio-stress-test.js` | Enumerate → per-thesis run of `stress-test/SKILL.md` **Phases 1-3, read-only** (pipelined) → 3 skeptics refute each flagged weakness → rank into one report → **sequential** skill-faithful persist when `persist:true` |
| `portfolio-correlation` | `portfolio-correlation.js` | Fan out `dependency-map` → cluster shared load-bearing dependencies into correlated-bet groups → synthesis note (`persist`) |
| `portfolio-macro-exposure` | `portfolio-macro-exposure.js` | Fan out `macro-exposure` → conviction-weighted concentration by macro variable → note |
| `portfolio-supply-chain` | `portfolio-supply-chain.js` | Fan out `value-chain` → stitch shared suppliers/customers + cross-thesis SPOFs → note + optional Canvas |
| `vault-contradictions` | `vault-contradictions.js` | Fan out `assumptions` → pair opposing industry-level assumptions → adversarially verify each → note |
| `portfolio-scenario` | `portfolio-scenario.js` | Fan out `scenario` impact method per thesis (needs `args.event`) → winners/losers + Major/Minor/Neutral → Major Logs + scenario note (`persist`) |
| `portfolio-retro` | `portfolio-retro.js` | Fan out `retro` per-ticker overlay, throttled (fixes the ~126-query rate-limit) → ranked trade ideas → immutable note (`persist`) |
| `portfolio-conviction-audit` | `portfolio-conviction-audit.js` | Fan out `conviction-audit` → rank over-conviction + fired triggers → `_followups` (`persist`; never touches `conviction:`) |

- **Invoke** — `Workflow({name:"portfolio-stress-test"})` or `Workflow({scriptPath:".claude/workflows/portfolio-stress-test.js"})`. Requires explicit opt-in — it spawns ~1 agent/thesis plus up to 3 verifiers per at-risk name.
- **Args** (all optional) — `tickers[]` (explicit set, overrides status), `status[]` (default `['active','monitoring']`), `limit`, `model` (default `sonnet`), `severityToVerify` (default 3), `persist` (default false = read-only report).
- **find→verify pattern** — the stress pass is the finder; the 3-skeptic majority-refute pass is the adversarial verifier (majority CANNOT refute → weakness confirmed → full severity kept; else severity −2). Mirrors single-name `/stress-test` but adds a verification gate at portfolio scale.
- **Skill reuse (analysis) + write split** — each Stress agent reads `stress-test/SKILL.md` and runs its **Phases 1-3 only** (analysis), so the sweep uses the real skill method and tracks its future edits. It explicitly does NOT run the skill's Step 0 lock or Phase 4 writes: ~1 agent/thesis each writing a manifest / Research note / thesis Log / `_followups.md` / `_hot.md` in parallel would race the shared files (`_followups.md`, `_hot.md` especially). All writes defer to the **Persist phase — a single writer, one thesis at a time** (`await` in a `for` loop over the at-risk names), replaying the skill's Phase 4 from each agent's pre-computed `shortCaseMarkdown`. **Analysis fans out; writes serialize** — the general rule for any write-capable fan-out (§14.3 is the reference implementation).
- **Relation to `/stress-test`** — same analytical method now (shared SKILL.md). `/stress-test TICKER` is the interactive single-name tool; the workflow is the batch sweep — read-only unless `persist:true`, which writes skill-faithful notes for the at-risk names only (not all N).
- **Skill/workflow pairing (Tier-1, 2026-07-22)** — the four cross-portfolio workflows each fan out a **read-only extraction skill's `## Method`**: `portfolio-correlation`←`dependency-map`, `portfolio-macro-exposure`←`macro-exposure`, `portfolio-supply-chain`←`value-chain`, `vault-contradictions`←`assumptions`. The skill is the single-name tool AND the single source of truth; the workflow is the portfolio sweep. Same invariant as stress-test: **analysis fans out (read-only), writes serialize** (a single-writer Persist phase when `persist:true`; `vault-contradictions` adds a find→verify pass since a claimed contradiction can be a framing difference).
- **Tier-2 pairing (parallelize existing skills)** — `portfolio-scenario`←`scenario` and `portfolio-retro`←`retro` fan out skills you already had: each agent runs the skill's per-thesis **analysis** phases and explicitly skips its Step-0 lock, approval gate, and write phases (which the workflow's sequential Persist owns). `portfolio-conviction-audit`←the new `conviction-audit` skill. Two specifics: `portfolio-scenario` requires `args.event`; `portfolio-retro` exists precisely to fix retro's ~126-query WebSearch rate-limit — the per-ticker fan-out is throttled by the workflow concurrency cap (~10-16), so no burst.
- **Registry / discoverability** — `_workflows.md` (vault root) is the generated catalog of every workflow, built from each script's `meta` block by `.claude/workflows/_generate_registry.mjs` (mirrors how `/graph` generates `_graph.md`). **Re-run the generator after adding or editing a workflow.** Skills self-list in the `/` menu; workflows do not, so this file is how the user sees what's at hand.

---

## Appendix: File ownership matrix

| File / directory | Creators | Modifiers | Cleaners |
|---|---|---|---|
| `Theses/*.md` | `/thesis` | `/sync`, `/deepen`, `/status`, `/compare`, `/scenario`, `/stress-test`, `/prune`, `/rename`, `/rollback`, `/retro` (Log), `/archive-callouts` (Legacy sweep) | `/status`, `/prune` (archive) |
| `Research/*.md` | `/ingest`, `/thesis`, `/deepen`, `/compare`, `/scenario`, `/stress-test`, `/surface`, `/brief`, `/retro`, manual | — (Tier 2 immutable bodies) | manual |
| `Sectors/*.md` | manual, `/thesis` (scaffold) | `/sync`, `/status`, `/compare`, `/prune`, `/archive-callouts`, manual | — |
| `Macro & Technology/*.md` | manual | `/sync`, `/scenario`, `/archive-callouts` | — |
| `_hot.md` | any of 14 writers (auto-create per CLAUDE.md Rule #9) | 14 writers (§1.1) | manual when `/lint #35`/`#42` fires |
| `_graph.md` | `/graph` | `/graph`; `/rename` (adjacency header only) | `/graph` |
| `_catalyst.md` | `/catalyst` | `/catalyst` (overwrite) | `/catalyst` |
| `.claude/skills/**` | Skill authors | Manual (SKILL.md per §12.4) | Manual |
| `.claude/hooks/*.py` | Manual (§14.1) | Manual | Manual |
| `.claude/schedule/**` (runner + canonical plists) | Manual (§14.2) | Manual | Manual (`logs/` disposable) |
| `.claude/workflows/*.js` | Manual (§14.3) | Manual | Manual |
| `.claude/workflows/_generate_registry.mjs` | Manual (§14.3) | Manual | Manual |
| `_workflows.md` | `_generate_registry.mjs` (from workflow `meta` blocks) | regenerate after adding/editing a workflow | regenerate |
| `~/Library/LaunchAgents/com.investmentvault.*.plist` | Manual install (§14.2) | Manual | `launchctl bootout` + `rm` |
| `.claude/.graph_dirty` | `mark-graph-dirty.py` hook | — | `refresh-graph.py` hook (consume + delete) |
| `.claudian/`, `.obsidian/`, `.git/` | Their apps | Their apps | Manual / `git gc` |
| `.last_sync` | `/sync` (default, all) | same | — |
| `.sync_all_fresh` | `/sync all` | — | `/graph` (consume + delete) |
| `.graph_invalidations` | `/status`, `/prune` closures | append-only | `/graph last` (consume + delete) |
| `.rename_incomplete.TICKER` | `/rename` on post-mv failure | `/rename` repairs | `/rename` (auto-delete when empty) |
| `.archive_ticker_registry.md` | `/status`, `/prune` closures | append-only | — (stale tolerated) |
| `.vault-lock*` | all state-modifying skills | own skill only | own skill; manual on abandonment |
| `.drift-config.md` | manual (optional) | manual | manual |
| `_followups.md` | first writer (auto-create) | writers append; `/status`, `/sync` resolve | `/clean` (Resolved >90d) |
| `_watchers.md` | manual | manual / Claude NL edits; n8n read-only | manual (monthly review) |
| `Daily Intel/*.md` | n8n Workflows 3, 5 | — (write-once snapshots) | manual |
| `.data/config.json`, `.data/x_engagement_state.json` | manual / n8n Workflow 5 | n8n Workflow 5 (state, single-writer) | manual (state disposable) |
| `.sync-progress.jsonl` | **Reserved — not written** | — | — |
| `_Archive/Snapshots/*.md` | destructive skills (pre-edit) | — | `/clean` |
| `_Archive/Snapshots/_*-manifest*.md` | multi-file skills (skeleton) | own skill (populate + flip) | `/clean` (after aging + floors) |
