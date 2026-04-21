# Infrastructure Reference

> Deep technical details for the vault's consistency machinery. **Audience: Claude Code at skill-author / debugger scope.** User-facing summary: [[User Guide#14. How the Vault Stays Consistent]].
>
> **Per-skill deep rationale** lives in `<skill>/RATIONALE.md` (currently 10 skills: `sync`, `graph`, `lint`, `status`, `scenario`, `compare`, `thesis`, `rename`, `prune`, `rollback`). When a skill's design rationale exceeds ~20% of its SKILL.md, extract per §12.3. Cross-skill contracts live in `.claude/skills/_shared/*.md` (§12.2).
>
> **Stable anchors** external files may reference: §1.1 (`_hot.md`), §2.7 (`.drift-config.md`). Do not renumber these without updating consumers.

---

## 0. Orientation

Read this section first on any non-trivial task. It replaces hunting through §1–§13 by giving you lookup tables, critical invariants you cannot violate, and a symptom index that points straight to the deep-dive section.

### 0.1 Reading paths

| Task | Read these sections in order |
|---|---|
| **Debug a symptom** (skill silently no-op'd, wrong propagation, lock stuck, etc.) | §0.3 symptom index → §13 debugging flow → specific deep-dive |
| **Author a new skill** | §0.4 skill landscape → §0.5 glossary → §5 producer contracts → §3 manifest pattern → §6 locks → §12 skill-layer architecture |
| **Add a new runtime marker at vault root** | §11.5 checklist → §2 nearest-sibling marker → Appendix |
| **Extend a shared `_shared/*.md` contract** | §12.2 catalog → §12.4 editing protocol → paired `/lint` check in §10 |
| **Change the `_hot.md` schema or compression** | §1.1 → `.claude/skills/_shared/hot-md-contract.md` → all 13 writers in §0.4 |
| **Add a new `/lint` check** | §10 registry → §12.2 shared-contract consumers → update §12.4 editing protocol |
| **Understand a rollback cascade** | §7 cascade catalogue → §3.2 manifest catalogue → §13.6 if stuck in-progress |
| **Tune model/context for a skill or diagnose a Sonnet regression** | §12.6 performance architecture → §0.4 skill landscape → per-skill RATIONALE.md if present |

### 0.2 Critical invariants

Violating any of these produces silent corruption. Each links to the section that defines it.

1. **Token-based lock ownership, not PID** (§6.2) — Claude Code's Bash tool is stateless; PIDs change between blocks. The LLM carries the run-token string through all tool calls.
2. **Explicit lock release, not trap-based** (§6.2) — `trap` handlers only survive within one Bash block. Release via explicit `rm -f` at skill end.
3. **No lock auto-steal** (§6.2) — stale locks surface via `/lint #43`; never steal based on timeout.
4. **`propagated_to:` is atomic** (§5.1) — field written ONLY after all Log appends succeed. Partial failure omits the field → `/sync` retries.
5. **`propagated_to: []` is terminal** (§5.1) — `synthesis` and `brief` notes carry empty list. Blocks circular self-propagation.
6. **Thesis `## Log` is append-only** (CLAUDE.md Tier 2) — never edit, reorder, or delete existing entries. Log-prefix registry (`_shared/log-prefixes.md`) carries cross-skill semantic weight.
7. **`_hot.md` 6-section schema is load-bearing** (§1.1) — missing sections cause silent skill no-ops. `/lint #35` enforces.
8. **`_hot.md` compression drops whole entries, never truncates** (§1.1) — truncation markers (`...`, `[truncated]`, unclosed `**`) are forbidden. `/lint #42` catches.
9. **`_graph.md` has one owner: `/graph`** (§1.2) — only exception is `/rename`'s surgical adjacency-header update, which does NOT advance `last_graph_write:`.
10. **Manifest skeleton → populate → flip** (§3) — multi-file skills write the manifest BEFORE any destructive mutation, flip to `completed` only after all edits land. `in-progress` = crash signal.
11. **Closure-snapshot 30-day floor is unbypassable** (§3.2) — pre-closure thesis snapshots from `/prune` Stage 1 OR `/status active→closed` are protected across ALL `/clean` modes for 30 days. No flag override.
12. **Rename marker hard-blocks consumers** (§2.4) — `.rename_incomplete.TICKER` presence hard-blocks every ticker-scoped skill on TICKER and most vault-wide skills on ANY marker. Re-run `/rename TICKER "[same new_name]"` to repair.
13. **Sector resolution is a 4-step ladder, not exact match** (§12.2, `_shared/sector-resolution.md`) — exact → normalized → substring → ask. Never silently skip or silently substring-match for destructive writes.
14. **5 canonical wikilink forms** (`_shared/wikilink-forms.md`) — idempotency and cascade detection must match all five. Producers emit form #1 on write.
15. **Forked context is report-only** (§12.1) — `/lint`, `/prune`, `/surface` execute in a `general-purpose` subagent; main conversation receives only the final summary. Do NOT treat the subagent's intermediate reasoning as recoverable into main — it's discarded on return. If main context needs a specific subagent finding, the subagent must emit it in the summary or write it to a vault file.
16. **Model assignment is per-skill, not per-invocation** (§0.4, §12.6) — five skills run on Sonnet max (`/graph`, `/rename`, `/rollback`, `/status`, `/clean`). All others run Opus max. Downgrade is a one-line SKILL.md frontmatter change; revert criteria tracked in §12.6.

### 0.3 Symptom → section index

| Symptom | Likely cause | Read |
|---|---|---|
| Skill silently no-op'd on `_hot.md` | Missing/renamed section heading | §1.1, §13.1 |
| `/sync` didn't propagate a manual thesis edit | Last Log prefix is in skill-origin list (`_shared/log-prefixes.md`) — treated as skill-origin, not research-driven | §5.3, CLAUDE.md Workflow Rule 6, §13.2 |
| `/sync` propagated the same research twice across days | Wikilink drifted after rename → primary key missed | §2.1, `sync/RATIONALE.md §1` |
| `/graph` missed a thesis that `/sync all` touched | `.sync_all_fresh` absent or consumed without force-rebuild | §2.2, §13.3 |
| `/graph last` didn't update neighbor adjacency after closure | `.graph_invalidations` not appended by `/status`/`/prune` | §2.3 |
| `/clean` refused to delete a closure snapshot | 30-day floor (universal across modes) | §3.2 |
| `_graph.md` stale after `/rename` | `/rename` only updates adjacency header; run `/graph last` to reconcile | §1.2, §11.4 chain 4 |
| Ticker-scoped skill hard-blocks with "rename incomplete" | `.rename_incomplete.TICKER` exists | §2.4, §9 |
| Lock acquisition fails | Conflicting lock active OR stale lock (lint #43) | §6, §13.5 |
| Manifest stuck `in-progress` | Skill crashed before flip OR final-flip missed | §3, §13.6 |
| `/ingest` deleted the research note it just created | Quality gate fired (paywall, <150 words, OCR corruption) | §4 |
| `/thesis` refused to create — "prior archived thesis exists" | Multi-signal archive-collision match | §5.3, `.archive_ticker_registry.md` |
| `/compare` locked and then failed mid-way | Partial-acquisition rollback released prior ticker locks | §6.3 |
| Wikilink to note X not matched by consumer | Consumer doesn't handle all 5 forms | `_shared/wikilink-forms.md`, §12.2 |
| Sector note never updated by `/status` | Sector resolution returned `none` confidence | §12.2, `_shared/sector-resolution.md` |
| `/rollback` closure cascade surfaced neighbor citations | H3 premise-dependent vs contextual classification | §5.3, §7.1 |
| `_hot.md` size keeps growing past soft cap | Compression trigger order not firing in order | §1.1, `_shared/hot-md-contract.md` |
| `/surface` missed a cross-section pattern (Business Model / Industry Context similarity) | Default mode is section-targeted; full Business Model / Industry Context reads only happen in `/surface all` | §12.6 (R2), surface/SKILL.md Phase 1 |
| `/status` missed a trigger-conflict that `/lint` later caught | Sonnet max on `/status` (2026-04-21) — may warrant revert to Opus | §12.6 watch list, §0.4 |
| `/rollback` offered single-file restore when user expected cascade | Sonnet max on `/rollback` (2026-04-21) — may warrant revert to Opus | §12.6 watch list, §0.4 |

### 0.4 Skill landscape

17 skills. Lock scope, `_hot.md` writes, and manifests are the three axes that determine every skill's pre-flight and cleanup contract. **Model** and **context** are the two runtime-performance axes (2026-04-21 update).

| Skill | Lock scope | Writes `_hot.md`? | Writes manifest? | Writes snapshot? | Model | Context | Role |
|---|---|---|---|---|---|---|---|
| `/sync` (default) | vault-wide | Yes (all sections) | `_sync-manifest` (T2.1 skeleton) | Tier A per-thesis | opus max | main | Propagation engine — research → thesis → sector/macro |
| `/sync all` | vault-wide | Yes | `_sync-manifest` + `.sync_all_fresh` | Tier A | opus max | main | Forced full-vault propagation |
| `/sync TICKER` | ticker:TICKER | Yes | `_sync-manifest` | Tier A | opus max | main | Ticker-scoped propagation; preserves `.last_sync` |
| `/graph` | vault-wide | No | No | No | **sonnet max** | main | Rebuild `_graph.md`. 3 modes (full, `last`, `[N]`) |
| `/ingest` | vault-wide | No (but may trigger `/sync` downstream) | No | No | opus max | main | Process `_Inbox/` into Research notes; quality gate |
| `/status` | ticker:TICKER | Yes | `_status-manifest` (T2.2) | Per-thesis pre-edit | **sonnet max** | main | Conviction/status changes |
| `/thesis` | ticker:TICKER | Yes (ART + OQ) | `_thesis-manifest` (H1) | No (creation) — manifest enables deletion-based rollback | opus max | main | Create new thesis |
| `/deepen` | ticker:TICKER | Yes | `_deepen-manifest` (M3 — 2026-04-21) | Per-thesis pre-edit | opus max | main | Targeted section deep-research |
| `/stress-test` | ticker:TICKER | Yes | `_stress-test-manifest` (T3.1) | No (Log append only) | opus max | main | Adversarial thesis test |
| `/compare` | N × ticker:TICKER | Yes | `_compare-manifest` | Per-thesis | opus max | main | Competitive comparison |
| `/scenario` | vault-wide | Yes | No | Per-thesis | opus max | main | Macro scenario propagation across portfolio |
| `/brief` | ticker:TICKER | Yes (ART + OQ only) | No | No | opus max | main | 1-page pitch generation |
| `/surface` (unscoped default) | vault-wide | Yes | No | No | opus max | **fork** | Cross-portfolio insight discovery (section-targeted reads) |
| `/surface all` | vault-wide | Yes | No | No | opus max | **fork** | Comprehensive full-read deep scan (legacy pre-2026-04-21 behavior, opt-in) |
| `/surface [sector]` | vault-wide | Yes | No | No | opus max | **fork** | Sector-scoped insight discovery |
| `/surface TICKER` | ticker:TICKER | Yes | No | No | opus max | **fork** | Ticker-scoped insight |
| `/catalyst` | vault-wide | Yes | No | `_catalyst.md` pre-regenerate | opus max | main | Regenerate catalyst calendar |
| `/prune` | vault-wide | Yes | `_prune-manifest` | Per-thesis pre-closure | opus max | **fork** | Weak-thesis evaluation/closure |
| `/rename` | ticker:TICKER | Yes (free-text mentions) | No | Per-thesis pre-rename | **sonnet max** | main | Atomic filename + wikilink rewrite |
| `/rollback` (list) | read-only | No | No | No | **sonnet max** | main | Inventory snapshots |
| `/rollback` (restore) | vault-wide | Yes | No | No | **sonnet max** | main | Restore from snapshot + cascade |
| `/clean` | vault-wide | No | No | No | sonnet max | main | Delete old snapshots/manifests (respects floors) |
| `/lint` (full) | vault-wide | No | No | No | opus max | **fork** | 30+ health checks (§10) |
| `/lint TICKER` | read-only | No | No | No | opus max | **fork** | Scoped subset (§10) |

Ticker-scoped vs vault-wide choice is the single most consequential decision when authoring a new skill — it dictates concurrency, rename-marker behavior, and `.last_sync` semantics.

**Model / context design principles** (2026-04-21):
- **Opus max** for analytical work requiring deep reasoning (propagation, ingestion, thesis construction, stress testing, scenarios, comparison, lint/prune judgment).
- **Sonnet max** for mechanical work (structural extraction in `/graph`, wikilink find/replace in `/rename`, snapshot restoration in `/rollback`, frontmatter nudges in `/status`, snapshot age classification in `/clean`). Each Sonnet-assigned skill was vetted for correctness risk and flagged watch-items (see §12.6).
- **Forked context** (`context: fork` with `agent: general-purpose`) for skills whose reads or analytical span dominate main-context budget but whose output is a bounded report or a handful of file edits (`/lint`, `/prune`, `/surface`). Main conversation receives only the final summary.

### 0.5 Glossary

| Term | Meaning |
|---|---|
| **Adjacency** | Per-thesis entry in `_graph.md` listing `cross-thesis:`, `same-sector:`, and T7.3 cache fields (`status:`, `log_tail:`) |
| **Append-only zone** | File region where historical entries are immutable (thesis `## Log`, `_hot.md` Sync Archive, `.archive_ticker_registry.md`, snapshot bodies). See CLAUDE.md Tier 2. |
| **Batch ID** | `<trigger>-YYYY-MM-DD-HHMMSS` identifier grouping snapshots and manifests from one skill run. Second-precision to avoid collisions. |
| **Cache fields (T7.3)** | `status:` and `log_tail:` appended to each `_graph.md` thesis entry so `/sync` Pass 1 / Step 2.5 can classify without re-reading every thesis. |
| **Closure-snapshot 30-day floor** | Universal `/clean` protection: per-thesis pre-closure snapshots (from `/prune` Stage 1 or `/status active→closed`) cannot be deleted for 30 days after the matching manifest's `completed_date:`. |
| **Consumer** | Any skill that reads a contract or `propagated_to:` field to decide behavior. Opposed to producer. |
| **Drift anchor** | Log prefix (registry §3-§9) that `/sync` Step 3e weights when detecting conviction drift. |
| **Idempotency key** | `/sync` per-thesis propagation check keyed on (1) wikilink presence in Log, then (2) `source:` URL / `date:+ticker:` tuple / `tags:`+date rename-resilience fallbacks. |
| **Load-bearing schema** | File structure whose absence or deviation causes silent no-op, not a crash. `_hot.md` 6 sections, thesis §1–§13 structure, manifest frontmatter. |
| **Manifest** | `_Archive/Snapshots/_<type>-manifest (<type>-*).md` sidecar tracking a multi-file transaction. Skeleton → populate → flip contract. |
| **Primary / secondary key (sync)** | §2.1 two-tier idempotency — wikilink presence is primary, URL/date+ticker/tags+date are secondary rename-resilient fallbacks. |
| **Producer** | Skill that writes content that downstream consumers interpret (Log entries, `propagated_to:`, wikilinks). Every producer has at least one consumer. |
| **Pre-flight** | `_shared/preflight.md` Procedures 1–4: lock, rename-marker, name sanitization, section probe. Runs at Step 0 of every state-modifying skill. |
| **Propagation** | `/sync` propagating a research note's signal into thesis Logs (Pass 1), then sector notes (Step 4), then macro notes (Step 5), then `_hot.md` (Step 6). |
| **Read-only lock** | `.vault-lock.readonly` — multiple readers allowed, blocks vault-wide writers. Used by `/lint TICKER`, `/rollback` list mode. |
| **Regret-recovery window** | 30-day protection period during which `/rollback TICKER` of a closure is still possible. Enforced via closure-snapshot floor (§3.2). |
| **Run token** | Random identifier (`printf '%08x' $RANDOM$RANDOM-$(date +%s)`) generated at Step 0.1, written to lockfile `token:` field, carried by LLM across tool calls for ownership verification. |
| **Same-ticker continuation** | `_hot.md` Active Research Thread rule: same TICKER → append line live; different TICKER → compress outgoing to `*Previous YYYY-MM-DD:*`. |
| **Scope taxonomy** | `vault-wide` \| `ticker:TICKER` \| `read-only`. Determines lockfile name and conflict semantics. |
| **Skeleton manifest** | Pre-mutation write of manifest with `status: in-progress` and placeholder fields, enabling post-crash recovery via `/rollback`. |
| **Skill-origin Log prefix** | Prefix from `_shared/log-prefixes.md` produced by a skill that already handled cross-file propagation (e.g., `Stress test`, `Status change`). `/sync` skips re-propagation when the most-recent Log entry carries one. |
| **Tier A / Tier B (sync)** | Tier A = destructive edits that require pre-edit snapshot. Tier B = Log-only appends, surfaced in `_sync-manifest` for strikethrough during rollback cascade. |
| **Watermark** | Timestamp marking last successful skill run. `.last_sync` mtime for `/sync`, `last_graph_write:` frontmatter for `/graph`. |
| **Forked skill** | Skill whose SKILL.md frontmatter declares `context: fork` + `agent: general-purpose`. Executes in isolated subagent; main context receives only the final report. Currently 3 skills: `/lint`, `/prune`, `/surface` (§12.1, §12.6). |
| **Section-targeted read** | Pattern used by `/catalyst` Phase 1 and `/surface` default-mode Phase 1: awk-extracted subset of a thesis (frontmatter + chosen `##` sections + recent Log) instead of full file. Reduces read cost ~75-85% at minor signal cost. |
| **Mode keyword** | Reserved literal argument for a skill (`/sync all`, `/surface all`, `/graph last`, `/graph [N]`). Disambiguates from ticker/sector arguments — never collides with filesystem names. Case-insensitive for `all`; exact-match for others. |
| **Mechanical skill** | Skill whose operations are structural (extraction, find/replace, copy, frontmatter edits) rather than analytical. Runs on Sonnet max (§0.4, §12.6). Currently: `/graph`, `/rename`, `/rollback`, `/status`, `/clean`. |

---

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

### 1.4 `Templates/_callouts/` — User feedback template files (2026-04-21)

Four Templater source files that insert dated Obsidian callouts at cursor position. Pure user-interaction infrastructure — **not touched by any skill**.

| File | Inserts | Rendering | Hotkey |
|---|---|---|---|
| `user-question.md` | `[!question]` | Yellow ❓ | `Mod+Alt+1` |
| `user-warning.md` | `[!error]` | Red ⚡ | `Mod+Alt+2` |
| `user-tip.md` | `[!tip]` | Teal 🔥 | `Mod+Alt+3` |
| `user-todo.md` | `[!todo]` | Blue ☑ | `Mod+Alt+4` |

Filename `user-warning.md` intentionally decoupled from callout type `[!error]` — filename is the Templater hotkey slot (kept stable across color/type iterations); type inside controls rendering.

Each file contains `<% tp.date.now("YYYY-MM-DD") %>` + `<% tp.file.cursor() %>` — Templater evaluates these at **insert** time, producing a dated callout with cursor positioned in the body.

**Companion config** (both git-tracked, not in `.gitignore` — syncs across machines):
- `.obsidian/hotkeys.json` — key chord bindings (`Mod+Alt+1..4`)
- `.obsidian/plugins/templater-obsidian/data.json` — template registrations via `enabled_templates_hotkeys` array; `templates_folder: "Templates"`; `auto_jump_to_cursor: true`

**Gotcha — recreation**: Templater's `trigger_on_file_creation: true` (enabled for folder templates on `Theses/`, `Research/`, `Macro/`) also fires on ANY new file with `<% %>` syntax. If a `_callouts/` template is deleted and recreated via `Write`, the `<% tp.date.now() %>` gets evaluated and **frozen** at creation time. Workaround: use `Edit` (not `Write`) to modify existing template files; `trigger_on_file_creation` only fires on creation.

**User-facing docs**: [[User Guide#Inline callouts — user feedback markers]] + [[CLAUDE.md]] Workflow Rule 7.

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

Lockfile at vault root, written by Procedure 1 at Step 0.1, released explicitly at final Bash block. Scope taxonomy, conflict matrix, and per-skill assignment live in §6.1 and §0.4 — not duplicated here.

Three file-name patterns:
- `.vault-lock` — vault-wide
- `.vault-lock.TICKER` — per-ticker (one per TICKER; `/compare` acquires N)
- `.vault-lock.readonly` — multiple readers allowed, blocks vault-wide writers

Token-based ownership (§6.2); explicit release (§6.2); no auto-steal (§6.2). Stale locks surface via `/lint #43`; recovery is user-initiated.

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
| `_prune-manifest` | `/prune` Stage 1 (C2 — skeleton before snapshots) | 2.5a generic | #36 | Records closures, upgrades, affected sectors, Stage 4.2 neighbors. Neighbor list populated at Stage 4.5 (C1 fix — prior placeholder broke `/rollback` Step 6.2.5 surfacing). 30-day regret-recovery window floors `/clean` deletion of the manifest AND of every Stage 1.5 closure snapshot whose `snapshot_batch:` matches (universal across `/clean` modes — `/clean` Step 2d). Manifest-first ordering (C2, 2026-04-21) closes invariant #11 orphan-window bypass |
| `_sync-manifest` | `/sync` Step 2.9 (T2.1 skeleton) | 2.5b | #41 | Two-phase: skeleton pre-mutation → phase-boundary checkpoints (T7.4: end-of-Step-3/4/5 + 7.5 flip) → `completed`. Tier B Log entries surfaced for strikethrough review during cascade |
| `_compare-manifest` | `/compare` Phase 5.0 skeleton (M2 — 2026-04-21) → Phase 5.5c flip | — | #45 | Two-phase (M2). Sectors edited/rolled-back, per-target Log outcomes. `status: rolled-back` when 5.5b atomicity fires; `status: in-progress` surfaced by `/lint #45` as Critical |
| `_stress-test-manifest` | `/stress-test` Phase 4.0 skeleton (M1 — 2026-04-21) → Phase 4.6 flip | 2.5d | #47 | Two-phase (M1). Records the Log entry text appended to tested thesis (no snapshot — append-only); `status: in-progress` surfaced by `/lint #47` as Important |
| `_status-manifest` | `/status` Step 3.0.5 (T2.2) | 2.5e | #48 | Two-phase. Records thesis frontmatter change, sector edit, archive move, graph invalidations, `_hot.md`. Reaffirm flow skips manifest (no multi-file transaction). **Closure variant** (`field: status, new_value: closed`): 30-day regret-recovery window floors `/clean` deletion of the Step 3.1 thesis snapshot (universal across `/clean` modes — `/clean` Step 2d) |
| `_thesis-manifest` | `/thesis` Step 3.5 (H1) | 2.5f | #49 | Two-phase. `/rollback` cascade is **deletion-based** (not snapshot restore) since `/thesis` creates new files |
| `_deepen-manifest` (M3 — 2026-04-21) | `/deepen` Phase 4.5 skeleton → Phase 7.5 flip | 2.5g | #50 | Two-phase. Records section deepened, pre-deepen thesis snapshot, Phase 5c Log-append outcome, Phase 6 supporting research note (if created). `/rollback` 2.5g offers thesis-only restore or full cascade with research-note deletion. `status: in-progress` surfaced by `/lint #50` as Important |

**Aging policy**: `in-progress` → Important (crash signal). `completed` → aged per 90/180 day tiers by the paired `/lint` check. `/clean` removes only after both the requested age AND any manifest-specific floor (e.g., prune 30-day window, status closure 30-day window) are satisfied.

**Closure-snapshot 30-day floor (universal — `/clean` Step 2d)**: distinct from manifest aging — applies to the per-thesis snapshots that closure manifests reference. Pre-closure thesis snapshots from `/prune` Stage 1 OR `/status active→closed` Step 3.1 are PROTECTED across ALL `/clean` modes (default age, `orphans`, `--include-orphans`) for 30 days from the matching manifest's `completed_date:`. Cross-reference is by `snapshot_batch:` ↔ manifest `batch:`. Closure detection: prune-manifest match always counts; status-manifest match requires `new_value:` to contain literal token `closed`. In-progress manifests' snapshots are also protected (closure transaction unresolved). The protection cannot be flag-overridden — the only deletion paths are (a) wait for the floor to expire, (b) manual `rm` with full awareness that `/rollback TICKER` becomes impossible.

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
| 2.5c (D1 canonical — 2026-04-21) | **Non-manifest triggers** (`/catalyst`, `/rename`, `/rollback` pre-safety-net snapshots) | 2.5a generic cascade — Tier A only, no Tier B Log auto-handling |
| 2.5d | `/stress-test` — `_stress-test-manifest` sidecar present | Surface only / cascade + strikethrough Log entry on tested thesis / cancel |
| 2.5e | `/status` — `_status-manifest` sidecar present | Thesis-only restore / full transaction restore (thesis + sector + un-archive with collision check C5 + clear invalidations) / cancel |
| 2.5f | `/thesis` — `_thesis-manifest` sidecar present | Delete thesis only / full cascade (delete + revert sector + revert `_hot.md` + revert orphan mtimes) / cancel. **Deletion-based, not snapshot-based** |
| 2.5g (M3 — 2026-04-21) | `/deepen` — `_deepen-manifest` sidecar present | Restore thesis from pre-deepen snapshot (research note preserved) / full cascade (a + delete supporting research note) / cancel |
| `/prune` | `/prune` — `_prune-manifest` + per-file `snapshot_trigger: prune` snapshots | 2.5a generic batch cascade; 30-day regret window enforced by `/clean` floor; Step 6.2.5 intervening-entries scan fires when restoring a reopened closed thesis; manifest neighbor list populated at Stage 4.5 (C1) |
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

Key checks — severity column indicates escalation in the lint report. "If fires, suspect" column is the fast-debug pointer.

| ID | Scope | What it catches | Severity | If fires, suspect |
|---|---|---|---|---|
| #1 | Full | Research note without `propagated_to:` AND no thesis Log reference | Important | `/sync` didn't run or crashed mid-propagation; research note created manually and never synced |
| #16 | Full | Stale snapshots (>180 days) | Nice to Have | `/clean` never run; user may want audit trail |
| #18, #20, #23 | Full | Graph health (existence, staleness, missing/ghost entries) | Important | `/graph last` not run after recent work; `.sync_all_fresh` swallowed without rebuild |
| #29 | Full | Log-prefix registry vs consumer-list drift (`_shared/log-prefixes.md`) | Important | Prefix added/changed in a producer without updating registry; breaks `/sync` skill-origin classification |
| #30 | Scoped | Sector-resolution coverage per thesis (`_shared/sector-resolution.md`) | Important if `none`, Nice to Have if `substring`/`normalized` | Thesis `sector:` drift or new sector needs scaffold note; ran `/rename` on sector without updating theses |
| #34 | Full | Sector frontmatter standardization vault-wide | Nice to Have | Thesis authored with typo/case divergence; sector note renamed without `/sync` catch-up |
| #32 | Full | Orphaned ticker refs (research `ticker:` matches no thesis) | Nice to Have | Thesis archived without `/status closed` (skipped ledger); `ticker:` typo |
| #33 | Full | Closed thesis file still in `Theses/` | Important | `/status active→closed` Step 7 crashed before mv; manual edit bypassed `/status` |
| #35 | Full + scoped | `_hot.md` schema drift | Important (silent no-op source) | Manual edit removed section heading; corruption; a skill wrote a missing section (should never happen — consumer contract violation) |
| #36 | Full | `_prune-manifest` state | Important if in-progress; Nice to Have if completed >30 days | `/prune` crashed before Stage 4 flip; aged completed → cleanable |
| #37 | Full + scoped | `.rename_incomplete.*` markers | Important | Prior `/rename` had post-mv Edit failure; re-run to repair |
| #38 | Full | State marker hygiene (`.sync_all_fresh`, `.graph_invalidations` aging) | Nice to Have | `/graph` not run after `/sync all` (stale `.sync_all_fresh`); `.graph_invalidations` accumulating because `/graph last` not run |
| #39 | Full | `propagated_to:` producer contract | Important (post-spec) / Nice to Have (pre-spec) | Producer skill crashed mid-propagation (partial append → field omitted correctly); or producer contract violation |
| #41 | Full | `_sync-manifest` aging | Important if in-progress; tiered if completed | `/sync` crashed or final-flip missed (check `_sync-manifest` `phase:` field for last checkpoint) |
| #42 | Full + scoped | `_hot.md` truncation markers | Important | Legacy compaction or manual edit left `...`/`[truncated]`/unclosed markdown; a producer violated hot-md-contract §3 |
| #43 | Full | Stale locks | Nice to Have (user-triggered recovery) | Skill crashed mid-run without explicit `rm -f` release; user interrupted (Ctrl-C after the trap block) |
| #45 | Full | `_compare-manifest` aging | Important if in-progress; tiered if completed | `/compare` crashed before Phase 5.5c atomicity flip |
| #46 | Full | `.archive_ticker_registry.md` validation | Nice to Have | Ledger entry references filename that no longer exists (tolerated; `/thesis` verifies before treating as match) |
| #47 | Full | `_stress-test-manifest` aging | Important if in-progress | `/stress-test` crashed before Phase 4.6 manifest flip |
| #48 | Full | `_status-manifest` aging | Important if in-progress | `/status` crashed between Step 3.0.5 skeleton and final flip |
| #49 | Full | `_thesis-manifest` aging | Important if in-progress | `/thesis` crashed before Step 3.5 flip; check whether thesis file was created |

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

**Currently covered runtime markers** (lines 22–38 of `.gitignore`): `.last_sync`, `.sync_all_fresh`, `.graph_invalidations`, `.vault-lock`, `.vault-lock.*`, `.rename_incomplete.*`. Any state-modifying skill that gains a new vault-root marker must extend this list — committing a live lock or repair marker would block every machine that pulls the repo until the offending file is `git rm`'d. Markers intentionally **NOT** ignored (because they are persistent content): `.archive_ticker_registry.md` (append-only ledger per §2.5), `.drift-config.md` (user-authored override per §2.7).

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

**Execution context directive**: SKILL.md frontmatter can include `context: fork` + `agent: general-purpose` to route the skill's execution into a forked subagent. As of 2026-04-21, three skills use this: `/lint`, `/prune`, `/surface`. Forked skills' intermediate reasoning and tool calls stay in the subagent's isolated context; only the final report returns to main. See §12.6 for the rationale and full impact measurements.

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

10 skills currently have a `RATIONALE.md`: `sync`, `graph`, `lint`, `status`, `scenario`, `compare`, `thesis`, `rename`, `prune`, `rollback`. Pattern: when SKILL.md accumulates rationale blocks (`> **Why this is safe**...`, `> **Edge case**...`, `> **T#.# rationale**...`) collectively exceeding ~20% of the file with no impact on LLM execution, extract.

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

**Current RATIONALE.md files and coverage**:

| Skill | RATIONALE.md lines | Primary topics |
|---|---|---|
| `sync` | 270 | 9 sections — idempotency, propagation targets, Pass 1, skill-origin gate, manifest, watermark, `_hot.md` auto-resolve, drift detection, T7 efficiency |
| `lint` | 209 | Check severity taxonomy, per-check rationale, cross-check interactions |
| `compare` | 204 | Phase 5.5c atomicity manifest, multi-ticker lock rollback |
| `prune` | 198 | Stage 4.2 neighbor scan, 30-day regret window, Stage 4.5 `.graph_invalidations` append |
| `rollback` | 188 | Cascade step 2.5a–f design, H3 premise-dependent vs contextual, intervening-entries scan |
| `scenario` | 183 | Phase 6.1.5 Major/Minor/Neutral classification approval, reverse archive-aware iteration |
| `thesis` | 182 | Step 1.2 multi-signal archive collision, H1 deletion-based rollback |
| `graph` | 182 | Three-mode cost model, T7.3 cache fields, reverse index always-rebuild rationale |
| `status` | 180 | T2.2 two-phase manifest, Step 3.0.5 skeleton pre-edit, closure variant snapshot floor integration |
| `rename` | 169 | Pre-flight Read/Write probe, cross-`new_name` guard, wikilink-form overlap with `_shared/wikilink-forms.md` |

Skills without a RATIONALE.md (7): `brief`, `catalyst`, `clean`, `deepen`, `ingest`, `stress-test`, `surface`. Their design rationale remains inline in SKILL.md (within the 20% threshold).

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

### 12.6 Performance architecture — 2026-04-21 optimizations

Audit of main-context usage on Opus 4.7 (1M context, max effort) surfaced three hotspots. Mitigations landed 2026-04-21:

#### R1 — `context: fork` on `/surface`

**Change**: `/surface` frontmatter gains `context: fork` + `agent: general-purpose`. Joins `/lint` and `/prune` in the forked-subagent set (now 3 skills).

**Rationale**: `/surface`'s outputs are clean-bounded (one Research note + `_hot.md` patches + a top-3-insights summary). The whole vault-read, connection analysis, and opportunity generation happens internally — main context does not need the intermediate reasoning. Forking isolates the ~200-300K subagent read budget from the main session.

**Measured impact**: unscoped `/surface` main-context cost drops from ~380K tokens to ~15K (final summary only). Monthly maintenance chain drops from ~847K to ~457K main-context tokens (85% → 46% of 1M).

**Trade-off accepted**: subagent intermediate reasoning is discarded on return (invariant §0.2 #15). If the user asks a follow-up about something `/surface` found but didn't emit to the summary, rerun `/surface TICKER` scoped to the area of interest.

#### R2 — Section-targeted reads in `/surface` Phase 1

**Change**: `/surface` default mode (unscoped, no args) now reads only 4 thesis sections (`Summary`, `Key Non-consensus Insights`, `Risks`, `Catalysts`) + last 5 Log entries per thesis. Same pattern as `/catalyst` Phase 1. `/surface all` opt-in keyword preserves pre-2026-04-21 full-read behavior for users who want maximum signal.

**Rationale**: surface analysis primarily uses cross-thesis pattern matching on high-density sections (Non-consensus Insights is the explicit "what does the market miss" signal, Risks is the explicit "what kills the thesis" signal). Business Model and Industry Context are expensive to read and rarely contribute unique signal to cross-section pattern detection.

**Measured impact**: subagent thesis-read budget drops from ~175K words (41 theses × ~4.3K avg) to ~35-50K words (41 theses × ~1K avg). Subagent read cost reclaimed: ~225K tokens per run.

**Mode matrix** (`/surface` SKILL.md Phase 1):

| Mode | Thesis reads | Read budget | Trigger |
|---|---|---|---|
| `/surface` (default) | Section-targeted | ~50-80K words | Routine / monthly cadence / chain use |
| `/surface all` | Full read | ~220K words | Quarterly deep review, suspected cross-section patterns missed |
| `/surface TICKER` | Scope-bounded full read | ~20-40K words | Ticker-focused insight |
| `/surface [sector]` | Full read ≤6 theses, section-targeted >6 | ~20-80K words | Sector review |

**`scope:` frontmatter** (new): surface-generated Research notes carry `scope: default | all | ticker:TICKER | sector:[Name]` so downstream review can distinguish deep-scans from routine scans. Filename suffixes: `(all)` for comprehensive runs, otherwise standard.

#### R4 — Sonnet max for mechanical skills

**Change**: Five skills downgraded from `model: opus` to `model: sonnet` (effort: max preserved):

| Skill | Operation character | Correctness risk |
|---|---|---|
| `/graph` | Fused Bash wikilink extraction + in-memory reasoning, `_graph.md` Write | Low — output is deterministic; `/lint #23` catches reverse-index drift |
| `/rename` | `mv` + 7-pattern wikilink find/replace | Low — patterns enumerated in `_shared/wikilink-forms.md` + archive variants (§9.1). `/lint #37` catches incomplete reruns |
| `/rollback` | Snapshot `cp` + cascade classification | **Medium** — cascade classification (§7, multi-file vs single-file offer) requires parsing manifests; watch for mis-classification |
| `/status` | Frontmatter edit + sector note + `_hot.md` + trigger-conflict check | **Medium** — trigger-conflict detection requires reading `Conviction Triggers` section and reasoning about logical contradiction with the proposed change |
| `/clean` | Snapshot age classification + deletion | Low — age math + closure-snapshot floor check (§3.2). Was already Sonnet pre-2026-04-21 |

**Wall-time impact** (measured / projected on Opus-vs-Sonnet latency ratios):

| Skill | Before | After | Delta |
|---|---|---|---|
| `/graph` full | 30-90s | 20-45s | ~45% |
| `/graph last` | 15-45s | 8-20s | ~50% |
| `/rename` | 60-120s | 30-60s | ~50% |
| `/rollback` list | 20-40s | 5-15s | ~65% |
| `/rollback` restore | 60-180s | 30-90s | ~50% |
| `/status` conviction | 60-90s | 30-50s | ~45% |
| `/status` draft→active or reaffirm | 30-60s | 10-25s | ~65% |

**Watch list** (first two to revert if Sonnet proves insufficient):
1. `/status` trigger-conflict detection — if `/lint #30` or a subsequent `/stress-test` flags a trigger-evidence mismatch that should have been caught pre-apply.
2. `/rollback` cascade detection — user runs `/rollback NVDA` after a `/sync all`, expects multi-file cascade offer, gets single-file restore.

**Revert procedure**: one-line edit per skill, change `model: sonnet` → `model: opus` in SKILL.md frontmatter. No data migration, no contract changes.

#### R5 — Parallel probe batch in `/thesis` Step 1.0

**Change**: `/thesis` Step 0.2 (rename-marker), 1.1 (active-thesis glob), 1.2 Signals A–D (archive collision, four independent file reads), and 1.3 (research context grep) now execute as a single parallel tool-call batch after Step 0.1 lock acquisition. Post-batch processing applies priority-ordered short-circuit logic (marker → active → archive → context).

**Rationale**: all seven probes are read-only, operate on stable state under the ticker lock, and have no cross-dependencies. Sequential execution added ~10–15s of pure round-trip latency per skill run. See `thesis/RATIONALE.md §9` for full safety analysis.

**Measured impact** (projected): wall-clock Step 0+1 cost drops from ~15s to ~3s. End-to-end `/thesis` skill-run savings ~5–8% of total time on the common path (no duplicate thesis found).

**Trade-off accepted**: slightly higher token context per turn — seven parallel tool-result blocks instead of one — vs. sequential short-circuit savings on the rare "active thesis exists" path. Net positive because the rare path is cheap anyway and the common path happens every run.

**Safety under the lock contract**: preflight Procedure 1 invariants fully preserved. Lock acquired first (0.1 sequential), probes fire after. Probes use `Glob`/`Grep` exclusively — no Bash ownership-verification cost (preflight §1.5 only mandates verification for Bash blocks).

**Cross-skill impact**: none. Step 1.2 multi-signal archive collision retains its 4-signal semantics (§5.3 table entry unchanged). `preflight.md` line 365's reference to `/thesis` rename-marker location updated from "Step 1.1.5" (already drifted) to "Step 0.2, executed within Step 1.0 parallel batch".

#### R6 — `/status` draft→active fast-path + parallelization

**Change**: two-part optimization to `/status`:

1. **Step 2F fast-path** — `status: draft→active` bypasses Step 2's Tier 3 `"Confirm? (y/n)"` gate. Shows a one-line FYI and proceeds directly to Step 3. All safety machinery (manifest skeleton, sector snapshot, Log entry, manifest flip) runs identically to the Step 2 path.
2. **Parallelization** — Step 1 thesis + `_hot.md` reads fire in one parallel batch; Step 5b same-file sector Edits dispatch in one parallel tool-call block (harness serializes server-side); Step 7.9 manifest populate + status-flip + completed_date batch in one message; Step 8 final Bash co-dispatches with manifest verify-read.

**Rationale**:
- **Fast-path**: `draft→active` is the only `status:` transition that is additive (not a reduction), has no analytical content change, has no cascade implications (no sector-list removal, no graph invalidations, no `_hot.md` demotion), and is trivially reversible (manual frontmatter flip per User Guide §13). CLAUDE.md Tier 3's stated examples (`active → monitoring`, `active → closed`) are all reductions. The fast-path formalizes what was already the acknowledged exception in Step 3.1's snapshot-skip and §3.1's snapshot producer table. Full analysis in `status/RATIONALE.md §9`.
- **Parallelization**: six round-trips saved on the mechanical portion by batching reads and consolidating same-file Edits. Full breakdown in `status/RATIONALE.md §10`.

**Measured impact** (projected against a representative `/status VRT draft→active` run):

| Source | Before | After | Saving |
|---|---|---|---|
| User wait on Tier 3 prompt | 10-120s | 0s | Full elision |
| Sequential round-trips (mechanical) | ~17 | ~10-11 | 6-7 round-trips × ~3s = ~18-21s |
| **Total wall-clock** | **~3 min** | **~30-50s** | **~75-85%** on fast-path runs |

For non-`draft→active` transitions, only the parallelization savings apply (~15-20s).

**Trade-off accepted (fast-path)**: one less user-prompt gate. Mitigated by:
- Step 2F FYI message explicitly names the change (user can interrupt before Step 3 dispatches)
- Log entry still recorded
- Scope strictly limited to `draft→active` — all other transitions still gate through Step 2 Tier 3
- Revert to prior behavior is one-line: delete Step 2F + restore Step 1 routing

**Cross-skill impact**: zero. Verified against `/sync` (Log prefix unchanged), `/rollback` (manifest unchanged), `/lint #48` (in-progress check unchanged), `/clean` (manifest aging unchanged), `/graph` (no invalidations from this transition), `/catalyst`/`/prune`/conviction-drift (filter by `status: active` regardless of transition path). CLAUDE.md Tier 3 rule respected — the rule's listed examples are all reductions; `draft→active` is additive and outside the listed scope.

#### R7 — Parallel-batch refactor across 10 skills (quality-preserving)

**Problem**: Audit of skill wall-clock on a 42-thesis / 133-research / 13-sector vault found ~40 instances where independent multi-file reads were being serialized because the SKILL.md prose didn't explicitly mandate parallelism. Subagents (and the main-conversation LLM) default to sequential tool-calling without explicit batching directives — each file read becomes one round-trip, compounding linearly with vault size.

**Design principle adopted: quality-preserving parallelization**. Parallelization is only unambiguously free when the content reaching the LLM is identical to the pre-change state. Two patterns were considered:

**Pattern A — Explicit parallel tool-call batch** (preserves LLM's view of source content): SKILL.md rewrites from `For each X: read X` loops to `Issue ALL X reads in ONE message as a single parallel tool-call batch`. Files are still read in full; the LLM sees the same content, just via parallel tool-call fan-out. **Zero research-quality risk.**

**Pattern B — Pre-extraction via Bash+awk** (reduces what the LLM sees): collapses N serial Reads into 1 Bash tool call by section-extracting only named sections before the LLM sees anything. **Faster and uses less context, but changes the content reaching the analytical LLM** — the LLM no longer sees the full document, only the extracted subset.

**Pattern B was rejected for analytical skills** (`/catalyst`, `/prune`, `/scenario`). Even though these skills' specs had always said "read only frontmatter + [named sections]", Pattern B enforces that narrowing at the tool level, removing the LLM's ability to catch signal outside the target sections — a non-standardly-placed catalyst (embedded in Bull Case), a weakness signal in Non-consensus Insights, a transmission channel in Industry Context. For skills whose output directly drives research decisions, full-file reads are preserved.

**Pattern B was accepted for mechanical skills**: `/lint` (read-only audit, regex-based checks — in-memory set-diff over extracted frontmatter fields carries no analytical quality risk), `/clean` (snapshot metadata extraction only — no research content).

**Applied changes**:

| Skill | Phase/Step | Pattern | Before → After |
|---|---|---|---|
| `/catalyst` | Phase 1 theses + macros | **A** (full-file) | ~48 serial Reads → 1 parallel batch of ~48 full-file Reads |
| `/catalyst` | Phase 2 WebSearch | A | ~42 serial → parallel batches of 10 |
| `/stress-test` | Phase 1 context | A | 5+ serial Reads+grep → 2 parallel rounds |
| `/deepen` | Phase 1 context | A | 5+ serial Reads+grep → 2 parallel rounds |
| `/compare` | Phase 1 per-ticker | A | N-ticker serial loops → 2 parallel rounds (full-file Reads) |
| `/scenario` | Pass 1 | **A** (full-file) | Serial per-thesis Summary extraction → single parallel batch of full-file thesis Reads (+ macros + graph) |
| `/scenario` | Pass 2 | A | Per-thesis deep-reads → sector notes only (theses already loaded) |
| `/sync all` | Pass 2 deep-reads | A | serial per-thesis → 1 parallel batch |
| `/surface` | Phase 1 steps 2-4 | A | serial sector/macro/research Reads → 1 parallel batch |
| `/prune` | Pass 1 lightweight scan | **A** (full-file) | Serial per-thesis section Reads → single parallel batch of full-file Reads |
| `/lint` | Checks #1/#9/#10/#11/#24/#32 | B + in-memory set-diff | naïve per-note Greps (~133 for #1 alone) → 1 consolidated Grep + Bash extraction feeds all 6 checks |
| `/clean` | Step 2 frontmatter | B | N serial Reads → 1 Bash+awk (scales to hundreds of snapshots at O(1) round-trips) |

**Bolded "A (full-file)"** rows = skills where Pattern B was attempted then reverted specifically to preserve research quality.

**`/lint` regex validation**: the consolidated wikilink Grep uses `\[\[[^\]]+\]\]` — confirmed to capture all 5 canonical wikilink forms defined in `_shared/wikilink-forms.md` (folder-qualified, with `.md`, with alias via `|`, with section anchor via `#`, and folder-less legacy form). Zero content-completeness risk vs. the per-note loop.

**Why Phase 3 web-research was NOT capped** (`/stress-test`, `/deepen`): the audit had initially suggested capping at "≤10 WebSearch calls". Rejected. Depth of adversarial / section-targeted web research drives skill quality more than wall-clock; the bottleneck on these skills was Phase 1 context-load, not Phase 3 web depth. Phase 3 remains unbounded — the model decides when enough evidence has been gathered.

**Cross-skill safety analysis** (verified before landing and after quality-revert):

- **Lock contract (preflight §1.5)**: Bash blocks still emit ownership verification before destructive ops. Parallel Read/Grep/WebSearch invocations do not touch the lock file, so batching them carries zero lock-consistency risk.
- **Manifest skeleton → populate → flip** (§3): untouched. All manifest writes still occur in serial order relative to destructive edits.
- **`_hot.md` 6-section schema** (§1.1): untouched. `_hot.md` updates remain serial within each skill (Read → Edit) because they must respect the word-cap check before writing.
- **`propagated_to:` atomicity** (§5.1): untouched. All `/sync`/`/scenario`/`/stress-test`/`/compare`/`/brief` propagation still runs the Log-append-then-frontmatter-write sequence with the same failure handling.
- **`_graph.md` single-owner** (§1.2): untouched. Parallel batching applies to read phases only; `/graph` remains the sole writer.
- **`/lint` read-only guarantee**: preserved. Single-pass Bash extractions are reads; in-memory set operations produce no writes.
- **Subagent fork contract** (§12.1, invariant #15): preserved. `/lint`, `/prune`, `/surface` fork as before; their internal parallel batching stays inside the subagent context.
- **Content completeness for analytical skills**: `/catalyst`, `/prune`, `/scenario` now read thesis bodies in full. Any signal available to the pre-R7 LLM is available to the post-R7 LLM. Quality-regression risk is zero by construction.
- **No shared-contract references to the rejected Bash+awk output formats**: verified via grep across `_shared/*.md`. The awk blocks in the three analytical skills were purely internal to their own SKILL.md and had no downstream consumers.

**Measured wall-clock impact** (42-thesis vault projection, post-revert):

| Skill / chain | Before | After | Delta |
|---|---|---|---|
| `/catalyst` | 8-15 min | 2-4 min | ~75% (WebSearch batching dominates; Phase 1 still reads in full) |
| `/lint` full | 90-120s | 30-45s | ~65% |
| `/stress-test` Phase 1 | 30-40s | 5-10s | ~75% |
| `/deepen` Phase 1 | 30-40s | 5-10s | ~75% |
| `/compare` A vs B vs C | 60-90s | 20-30s | ~65% |
| `/sync all` | 8-12 min | 5-8 min | ~35% |
| `/scenario` | ~2 min | ~50-60s | ~55% |
| `/prune` Pass 1 | ~60s | ~30-40s | ~40% |
| **Monthly maintenance chain** | 28-43 min | **20-30 min** | **~30%** |

Full-Read revert on `/catalyst`/`/prune`/`/scenario` costs ~10 min of chain-level wall-clock vs. the aggressive Pattern-B baseline, but eliminates the quality-regression risk that Pattern B carried.

**Main-context token impact**: the chain now carries ~600-700K main-context tokens (up from ~400-500K with Pattern B aggressive extraction, but down from ~1M+ pre-R7 if reads were both serial AND full-file without forking `/lint`/`/prune`/`/surface` to subagents). Well under the 1M Opus 4.7 context window.

**Revert procedure** (per skill, if a regression appears): restore the serial-loop language. Each skill's parallel-batch directive is a contiguous prose block; git history shows the exact replacement. No data migration, no contract changes, no manifest schema change — the optimization is purely prompt-level.

**Cross-skill impact**: none. Every skill's Phase/Step numbering, manifest schema, log-prefix emission, `_hot.md` section writes, and lock semantics remain bit-identical to pre-R7 behavior.

---

## 13. Common debugging flows

Symptom-first recipes for the failure modes surfaced most often during skill development. Each follows a diagnose → confirm → fix → verify pattern. Section pointers use §N.M; `/lint #N` maps to §10.

### 13.1 Skill silently no-op'd on `_hot.md`

**Diagnose**: `_hot.md` wasn't modified despite the skill running a `_hot.md` update step.

**Confirm**:
1. `Read _hot.md` — scan for the 6 canonical section headings (§1.1).
2. If any heading missing → silent no-op cause (skills are content producers, not schema fixers per `hot-md-contract.md`).
3. Run `/lint #35` — Important severity surfaces the missing heading.

**Fix**: manual edit to re-insert the missing section heading (no body needed; skill will populate on next run). Do NOT let the skill auto-repair — contract keeps schema ownership in `/lint`.

**Verify**: re-run the skill; target section should update.

### 13.2 `/sync` didn't propagate a manual thesis edit

**Diagnose**: user made a manual edit to a thesis body section (Bull Case, Industry Context, etc.), ran `/sync`, but sector/macro notes didn't pick up the change.

**Confirm**:
1. Read the thesis's most-recent `## Log` entry.
2. Check its prefix against `_shared/log-prefixes.md` registry (§12.2). If in the skill-origin list (e.g., `Stress test`, `Status change`, `Deepening`, `Reaffirmed`, `Scenario`) → `/sync` Step 2.5 classified the thesis as skill-origin and skipped re-propagation.

**Fix**: append a Log entry with a non-skill-origin prefix (`Manual edit:`, `Reviewed:`, `Refined:`) describing the change. Re-run `/sync` — Step 2.5 will now classify as research-driven. See CLAUDE.md Workflow Rule 6.

**Verify**: sector note's `## Active Theses` description or macro note's thesis-references section updates with the manual delta.

### 13.3 `/graph last` missed theses after `/sync all`

**Diagnose**: `/sync all` ran, `/graph last` ran, but some thesis adjacencies weren't re-extracted.

**Confirm**:
1. Check if `.sync_all_fresh` exists at vault root. If present → `/graph` hasn't consumed it yet.
2. If absent → `/graph` consumed it but may have skipped theses whose mtime wasn't advanced by `/sync all`'s "No delta" triage (§2.2).

**Fix**: the marker should force full rebuild — if `/graph` consumed it without forcing, that's a `/graph` bug. Run `/graph` (full mode, no `last`) to recover. Verify `.sync_all_fresh` is deleted.

**Verify**: `_graph.md` `last_graph_write:` is post-sync-all; spot-check a "No delta" thesis's adjacency.

### 13.4 `/clean` refused to delete a snapshot

**Diagnose**: user ran `/clean [days]` (even `/clean 0`), but a snapshot older than the threshold survived.

**Confirm**:
1. Read the snapshot's `snapshot_trigger:` frontmatter.
2. If `snapshot_trigger: prune` OR `snapshot_trigger: status` with `new_value: closed` → **closure-snapshot 30-day floor** applies (§3.2). Floor runs from matching manifest's `completed_date:`.
3. Alternative: snapshot's `snapshot_of:` target file is missing → orphan; protected by default unless `/clean orphans` or `/clean [days] --include-orphans` requested.

**Fix**: wait for the floor to expire OR manual `rm` with explicit acceptance that `/rollback TICKER` becomes impossible for that closure. No flag bypass exists — the floor is unbypassable by design (§0.2 invariant 11).

**Verify**: after wait, `/clean` deletes on next run.

### 13.5 Lock acquisition failed

**Diagnose**: Step 0.1 Bash block exited with `LOCK_COLLISION` or `LOCK_LOST`.

**Confirm**:
1. `ls .vault-lock*` — enumerate existing locks.
2. For each: read `timeout_at:` frontmatter. If in the past → stale; if future → live collision.
3. For live collision: read `skill:` field → identifies conflicting skill (may be legitimately running).

**Fix paths**:
- Live collision + conflicting skill truly running → wait for it to finish.
- Stale lock (per `/lint #43`) → user-initiated `rm -f .vault-lock*`. No auto-steal (§6.2 invariant).
- LOCK_LOST mid-run → another skill seized the lock OR user `rm`'d it. Skill must abort; re-run after.

**Verify**: re-run skill; acquisition succeeds.

### 13.6 Manifest stuck `in-progress`

**Diagnose**: `/lint` surfaces a manifest with `status: in-progress` and no recent modification.

**Confirm**:
1. Read the manifest frontmatter — `batch:`, `date:`, `phase:` (if `_sync-manifest` T7.4 checkpointed).
2. Check whether the corresponding skill was running (terminal output history, lock state).
3. If skill crashed → partial transaction.

**Fix paths**:
- **Partial transaction, recoverable**: run `/rollback` — matches `batch:` prefix, offers cascade restore. The manifest-aware cascade (§7) will surface Tier B Log entries for strikethrough review.
- **Partial transaction, not worth recovering**: manually delete the manifest after confirming no destructive edits landed in the vault proper. Re-run the skill.
- **False positive** (skill actually completed but final flip missed): check manifest's recorded edits against file mtimes → if all landed, manually flip `status: completed`. Rare.

**Verify**: `/lint` no longer surfaces the manifest.

### 13.7 `/sync` re-propagated a research note on the next day

**Diagnose**: same research note appears twice in a thesis Log under two dates.

**Confirm**:
1. Check the thesis Log for wikilink form drift — were the two entries' wikilinks to `[[Research/X]]` vs `[[Research/X.md]]` vs alias? All 5 forms should match as "already propagated" per `wikilink-forms.md`.
2. Check if the research note was renamed/moved between the two sync runs — primary key (wikilink presence) misses; secondary keys (`source:` URL, `date:+ticker:`) should have caught it (§2.1).

**Fix**:
- If wikilink form mismatch → consumer regex bug in `/sync`'s idempotency check. Fix by ensuring `/sync` uses `wikilink-forms.md` canonical regex.
- If rename caused miss → secondary keys should have fired; if they didn't, `/lint #1` + #39 cross-check surfaces the double-flag (`sync/RATIONALE.md §1` has the full design).

**Verify**: future `/sync` runs don't duplicate.

### 13.8 `/rename` partial failure

**Diagnose**: `/rename` ran, `mv` succeeded, but some wikilinks weren't rewritten.

**Confirm**:
1. `ls .rename_incomplete.*` — marker present with ticker suffix.
2. Read marker `failed_files:` list.

**Fix**: re-run `/rename TICKER "[same new_name]"` — triggers repair mode (§9.4). Marker shrinks monotonically as Edits retry successfully. Auto-deletes on empty.

**Cross-`new_name` conflict** (Step 1.4.5): if prior marker has different `new_name:`, `/rename` aborts. Options: finish prior with marker's `new_name:`, manually resolve + `rm` marker (losing repair state).

**Verify**: `/lint #37` returns no markers; all inbound wikilinks point to new name.

### 13.9 `propagated_to:` field missing on a producer's research note

**Diagnose**: `/sync` Pass 1 treats the note as not-yet-propagated even though it was.

**Confirm**:
1. Check note's source_type — only `scenario`, `stress-test`, `comparison`, `deepen` are required to emit `propagated_to:` (§5.2). `synthesis`/`brief` must emit `[]`.
2. If missing on a required source_type → producer crashed mid-propagation OR producer bug (atomicity violation).
3. `/lint #39` catches.

**Fix**: if Log appends actually succeeded on all listed tickers, manually add `propagated_to: [list]` to the note frontmatter — this is the post-hoc repair. If appends partially succeeded, rerun the producer (it will dedup via wikilink-presence check).

**Verify**: `/sync` no longer re-processes the note; `/lint #1 + #39` cross-check returns clean.

### 13.10 Sector note never updated by a skill

**Diagnose**: `/status`, `/prune`, `/compare`, `/thesis`, or `/rollback` expected to update a sector note but didn't.

**Confirm**:
1. Read the thesis's `sector:` frontmatter.
2. Run the 4-step sector resolution (`_shared/sector-resolution.md`) mentally: exact filename → exact frontmatter → normalized → substring.
3. Check skill output for `⚠️ No sector note found matching sector:` — confidence `none`.

**Fix paths**:
- `none` + intended sector exists under different name → update thesis `sector:` frontmatter OR create canonical sector note scaffold.
- `none` + sector truly doesn't exist → create `Sectors/[sector-name].md` from `Templates/Sector Template.md`.
- `substring` confidence + destructive rewrite skipped → expected behavior (see §12.2 `_shared/sector-resolution.md` §4). Standardize to promote to `exact`.

**Verify**: `/lint #30` / `#34` on TICKER returns pass.

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
