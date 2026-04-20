---
type: skill-rationale
skill: /lint
purpose: Design rationale and check-introduction context for /lint. NOT loaded at invocation — SKILL.md references by §N.M.
last_reviewed: 2026-04-20
---

# /lint Design Rationale

> SKILL.md contains check definitions, methods, severity classifications, and user-visible report messages. This file explains scope design, definition contracts with other skills, and the historical context of each check's introduction. Maintainers read this; the LLM executing /lint does not.

---

## §1 Scope design — full vs scoped mode

### §1.1 Why #35 runs in both modes

`_hot.md` schema drift causes silent skill no-ops across 11 skills. The defect surfaces only via `/lint #35`. A user who runs scoped `/lint TICKER` weekly (per User Guide §14 Cadence — weekly) and full `/lint` monthly can carry the bug for ~30 days, during which every `/status`, `/deepen`, `/stress-test`, `/scenario`, `/compare`, `/sync`, `/surface`, `/prune`, `/rollback`, `/catalyst`, or `/thesis` invocation against this ticker writes nothing to `_hot.md` while reporting success.

Running #35 in scoped mode catches this within one weekly check rather than one monthly check. The check is cheap (single file read + section grep) — no scoped-mode performance penalty.

### §1.2 Why #42 runs in both modes

Same reasoning as #35: `_hot.md` truncation markers indicate lossy compression drift that affects every subsequent write. Scoped mode catches this early rather than deferring to monthly full lint.

### §1.3 Why #37 runs scoped-if-marker-exists

`.rename_incomplete.TICKER` hard-blocks all ticker-scoped skills for that ticker until cleared. A user running `/lint TICKER` wants to know about this state immediately — it's the reason their `/status`, `/deepen`, or `/sync` for that ticker isn't working. Full-mode sweep is also valuable (catches markers for OTHER tickers).

### §1.4 Vault-wide-only checks — why

Checks skipped in scoped mode are those whose cost scales with vault size (graph health, orphan detection, registry alignment) OR whose scope is inherently vault-global (archive registry, state marker hygiene, producer contract enforcement). Running these per-ticker would either waste cycles or produce confusingly partial reports.

---

## §2 Definition contracts with producer skills

### §2.1 #1 orphan research — thesis-centric predicate

The orphan predicate is "not linked from any thesis" — NOT "not linked from any thesis OR sector note". Sector-only-linked research notes are still orphans.

This matches `/graph` Step 5's thesis-centric adjacency model. Sector note references are advisory context; they do not rescue a note from orphan status.

**Why thesis-centric**: `_graph.md` is the authoritative dependency map, and its orphan list is the source of truth for cleanup decisions. Divergent definitions would produce conflicting signals between `/lint` and `/graph`, leading users to chase ghost orphans (notes rescued by sector-only references in one view but flagged in another).

### §2.2 #18 graph staleness — T6.10 ISO precision fallback

`last_graph_write: YYYY-MM-DDThh:mm:ssZ` is preferred (T6.10). Legacy graphs without this field fall back to `date: YYYY-MM-DD` at 00:00:00 UTC, which may over-report age by up to 24h for recent runs. The advisory `ℹ️ _graph.md lacks last_graph_write: — next /graph run will upgrade frontmatter to ISO precision.` makes the degradation visible without blocking.

### §2.3 #28 partial-write detection — the self-corrected `/deepen` exception

A `"Deepening"` Log entry followed IMMEDIATELY by `"↳ CORRECTION: Deepened"` indicates `/deepen`'s retry mechanism fired successfully. The audit trail is complete — the section was rewritten, the correction is documented — but the cosmetic residue remains. Downgrade to Nice to Have because no data was lost.

### §2.4 #32 orphaned ticker references — what replaced self-healing

Pre-T7, `/sync` Step 1 Fallback 1 self-healed this case silently: if a Research note's `ticker:` didn't match any thesis, `/sync` ignored it. The silent behavior led to orphan research accumulating undetected.

Surfacing at `/lint #32` lets the user decide rather than letting orphans accumulate. Fix options are documented in the check itself (create missing thesis, edit ticker, accept orphan).

### §2.5 #33 closed-thesis files in `Theses/` — what replaced inline gates

Pre-T7, `/sync` handled this state inline with 5 separate gates (each skill's closed-status guard). Surfacing here makes the failed-archive-move state visible once rather than silently propagating warnings every sync.

---

## §3 #29 log-prefix registry — three-way alignment check

### §3.1 Why three-way check (producer + consumer + vault presence)

The registry at `.claude/skills/_shared/log-prefixes.md` defines the contract. Three independent dimensions can drift:
- **Producer drift**: the skill was edited to stop emitting the prefix, but registry wasn't updated.
- **Consumer drift**: the skill was edited to stop matching the prefix, but registry wasn't updated.
- **Vault drift**: the prefix is still emitted and matched, but no vault thesis Log actually contains it — producer may be silently broken, or no triggering events have occurred.

Each dimension gets its own check (a/b/c in the method). Drift in any dimension breaks the contract differently.

### §3.2 Why vault-presence is Important not Critical

A vault may legitimately have no recent rollbacks, prune upgrades, or specific edge-case events. The absence of a prefix in vault state doesn't prove the producer is broken — it just says "no recent trigger". Important severity flags the gap for investigation without crying wolf.

### §3.3 Reverse check — orphan coupling

SKILL.md files may contain "Drift coupling" blocks or Log format code fences citing prefixes not in the registry. Either the registry is incomplete, or the skill's reference is stale. Both are fixable; the check surfaces them.

---

## §4 #36/#41/#47/#48/#49 manifest aging — common pattern

### §4.1 Why status-first, then age-based

Every manifest has two potential failure modes:
1. **In-progress** — skill crashed, or flip-to-completed silently missed.
2. **Completed but stale** — aged past useful cascade-recovery window.

Status-first classification catches the critical state (crash) regardless of age. Completed manifests age per 90/180-day tiers; in-progress stays Important until investigated.

### §4.2 Why `/prune` has a 30-day floor and others don't

`/prune` cascades can surface Tier B "Cross-thesis closure" Log entries (written without per-neighbor snapshots) via the prune manifest's 30-day retention window. Deleting before 30 days eliminates the regret-recovery path; the floor prevents `/clean [short-days]` from accidentally nuking useful crash-recovery history.

Other manifests (sync, status, thesis) are more constrained in their cascade scope — aging past 90/180 days is safe because the companion Tier A snapshots have typically been cleaned too.

### §4.3 In-progress sync manifest — three possible causes

The Important message walks through:
- **(1) Mid-run crash** — inspect body for landed Tier A + Tier B, use `/rollback`.
- **(2) Flip-only failure** — Tier B entries actually present on listed theses → flip succeeded but manifest status didn't update → manually edit manifest.
- **(3) `/lint` during active sync** — ignore this finding; running sync will flip when complete.

The user's recovery path depends on distinguishing these. The message is long because the distinction matters.

### §4.4 Pre-T2.1 legacy manifests — "treat as completed"

Manifests written before T2.1 (2026-04-19) didn't have `status:` frontmatter. They're always complete by construction (prior behavior wrote manifest at end-of-run only). Missing-status treatment: classify as completed for aging purposes; emit Nice to Have advisory to upgrade.

---

## §5 #35 `_hot.md` schema — why silence is dangerous

### §5.1 Required sections contract

11 skills write `_hot.md` via targeted Edit operations on specific `##` headings. A missing heading causes the Edit to silently miss — the skill reports success, the update is lost, the user has no indication.

The six required sections (`## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`) are the contract every writer depends on.

### §5.2 Why frontmatter checks are softer

`date:` and `tags:` are informational — skills don't depend on them for Edit targeting. Malformed or missing frontmatter degrades readability but doesn't cause silent no-ops. Hence Important (malformed) vs Nice to Have (tags differ) rather than Critical.

### §5.3 Order check — Nice to Have only

Skills tolerate section reordering because Edit operations match by heading string, not position. Canonical order is a readability convention; violating it doesn't break behavior. Nice to Have surfaces the drift without blocking.

### §5.4 Word-cap check — why Important

The hot-md-contract (§1.1 of INFRASTRUCTURE.md) sets caps (soft 4,000 / hard 5,000). Exceeding the hard cap should trigger auto-prune on next write. Persistent over-cap means the prune logic drifted; investigating is warranted.

---

## §6 #39 `propagated_to:` producer contract

### §6.1 Why per-source_type mandate

Different producers have different contracts:
- `/surface` and `/brief`: terminal `[]` (unconditional — "no thesis propagation for this note")
- `/scenario`: Major-impact tickers, atomicity-skip allowed
- `/stress-test`: single `[TICKER]`, atomicity-skip allowed
- `/compare`: tickers with existing theses, atomicity-skip allowed

The table in SKILL.md #39 enumerates. Atomicity-skip allowed means the field legitimately may be absent if all Log appends failed at producer time.

### §6.2 Why `deep-dive` is excluded

`deep-dive` is used both by `/deepen`'s supporting research note (where `propagated_to: [TICKER]` IS mandated) AND by manually-created deep-dive notes (no requirement). Distinguishing the two requires fragile filename-pattern heuristics. Surface in `#4 (missing frontmatter)` instead if needed.

### §6.3 Pre-spec downgrade — 2026-04-19 boundary

The contract was introduced 2026-04-19. Notes dated before this cutoff predate the spec; backfill is optional. Post-cutoff violations are Important; pre-cutoff are Nice to Have ("pre-spec gap").

### §6.4 Why terminal producers (`synthesis`, `brief`) get no pre-spec downgrade

Terminal `[]` is unconditional — the alternative is `/sync` spamming 10+ theses per circular propagation. Pre-spec notes are still at risk of causing this spam on next `/sync` run, so Important severity regardless of date.

### §6.5 Cross-check with #1 — double-flagged orphans

A note flagged as orphan in #1 AND missing `propagated_to:` in #39 is a strong cleanup signal: no Log audit trail anywhere, no producer-contract record. Combined flag `🚨 Double-flagged orphan` surfaces this intersection.

---

## §7 #43 vault-lock staleness — why no auto-steal

Claude Code's Bash tool is stateless — each block is a fresh subshell with different `$$`. PID-based ownership would require carrying parent-process context across invocations, which isn't possible.

Token-based ownership (T6 fix): the LLM captures a run-token at Step 0.1 and carries it through every subsequent Bash block. Lock staleness is determined purely from `timeout_at:` frontmatter — not PID state.

**No auto-steal**: timeout-based stealing would race legitimately long-running skills (web research, `/sync all` on mature vault). Manual recovery is the safer default. `/lint #43` surfaces stale locks with full context (skill, token, scope, ages) so the user can decide to `rm` after confirming abandonment.

**Multi-ticker lock reporting**: `/compare A vs B vs C` acquires per-ticker locks (C4 fix — handles hyphen-containing tickers like `BRK-B`). Partial acquisition state (some peer locks missing) is a distinct failure mode; report together for diagnostic clarity.

---

## §8 #46 archive-ticker registry — why stale entries tolerated

`.archive_ticker_registry.md` is consumed by `/thesis` Step 1.2 Signal C (multi-signal archive-collision check). `/thesis` verifies file existence before treating a registry entry as a match — so stale entries (archived file since deleted/renamed) are tolerated without causing false collisions.

`/lint #46` surfaces stale entries for user awareness but does not auto-delete. Manual cleanup is optional; the consumer self-corrects.

---

## §9 #44 scenario-note reversal completeness — H3 archive protection

### §9.1 Why scan both live and archived tickers

`/scenario reverse` handles two cases:
- **Live theses** (`Theses/TICKER - *.md` exists) → append `Scenario REVERSED` Log entry
- **Archived theses** (`_Archive/TICKER - *.md` exists) → document archive-skip in scenario note body's `## Reversal Notes` section (Tier 3 archive protection — do NOT modify archived theses)

#44 verifies every `propagated_to:` ticker received one of these two treatments. Missing coverage (ticker in `propagated_to:` but no Log entry AND no archive-skip note) indicates an incomplete reversal — either re-run `/scenario reverse` or manually reconcile.

---

## §10 Output format — why three severity tiers

Critical / Important / Nice to Have matches the standard severity taxonomy of operational checks:
- **Critical**: breaks research quality — must fix before further operations (corrupt graph, in-progress manifests blocking writes).
- **Important**: gaps in coverage — should fix but operations remain safe (stale data, schema drift).
- **Nice to Have**: optimization — fix when convenient (aging aged artifacts, cosmetic residue).

The stats block at report end provides vault-level context (note counts, thesis status distribution, orphan count) that helps the user assess overall health independent of specific findings.
