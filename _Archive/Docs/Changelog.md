---
date: 2026-04-24
tags: [meta, changelog]
---

# Infrastructure Changelog

Time-boxed infrastructure changes extracted from [[User Guide]] §13. Evergreen user-facing caveats stay in the User Guide; this file holds dated rollouts whose operational details live in [[INFRASTRUCTURE.md]] §12.6.

---

## 2026-04-22

### WebSearch batching extension
Two web-research speed wins, both mirror the `/catalyst` Phase 2 batched-WebSearch pattern:

1. **`/catalyst` WebSearch batch cap raised 10 → 25.** Same parallel pattern, larger per-batch fan-out. For ~42 tickers, Phase 2 earnings enrichment drops from ~4-5 rounds of ~5s each to ~2 rounds. Expected ~40-60% wall-clock reduction on the Phase 2 step.
2. **`/thesis` Step 3 Web Research now explicitly batches WebSearch/WebFetch calls** (up to 25 per message, independent searches only). Step 2 vault Reads and Step 3 web searches are also now explicitly parallel — no ordering dependency. Expected ~30-50% wall-clock reduction.
3. **`/stress-test` Phase 2.5 (new, optional) documents the batching pattern** for opportunistic external-evidence lookups. Does NOT mandate web research — `/stress-test` remains vault-content-driven by default.

No behavior changes beyond parallelization. Regression recovery: revert to serial if a batch-too-large error surfaces (unlikely at cap=25).

---

## 2026-04-21

### `/surface` section-targeting vs `/surface all`
Default `/surface` now reads only 4 sections per thesis (Summary, Non-consensus Insights, Risks, Catalysts) + last 5 Log entries — ~25% of the token cost of the pre-2026-04-21 behavior. Use `/surface all` if you explicitly want the legacy full-read behavior (e.g., once-off quarterly deep review). Both modes fork to a subagent. If a cross-section pattern seems systematically missed by default mode, switch to `/surface all`.

### `/thesis` parallel probe batch
`/thesis` Step 0+1 duplicate-detection probes (rename-marker, active-thesis glob, 4 archive-collision signals, research-context grep) now fan out as a single parallel tool-call batch after lock acquisition. Same semantics, same 4-option archive-collision prompt, same priority-order short-circuit — just fewer round-trips. ~5–8% end-to-end wall-clock improvement. Rationale: `.claude/skills/thesis/RATIONALE.md §9`.

### `/status draft→active` fast-path
`/status TICKER status draft→active` now **skips the Tier 3 `"Confirm? (y/n)"` gate** and proceeds directly after a one-line FYI message. Every other safety mechanic (manifest skeleton, sector snapshot, Log entry, manifest flip) runs identically. Scope is narrow: ONLY `draft→active`. All other transitions still require Tier 3 confirmation.

Why safe for this transition: CLAUDE.md Tier 3's examples are all reductions (`active→monitoring`, `active→closed`); `draft→active` is additive. No analytical content changes. No cascade implications. Easily reversible via manual frontmatter flip. Full analysis: `.claude/skills/status/RATIONALE.md §9`.

Combined with Step 1/5b/7.9 parallelization, a typical `/status TICKER draft→active` completes in ~30–50s (down from ~3min). To opt back into the prompt, interrupt after the Step 2F FYI.

### Parallel-batch refactor across 10 skills
Ten skills (`/catalyst`, `/stress-test`, `/deepen`, `/compare`, `/scenario`, `/sync all`, `/surface`, `/prune`, `/lint`, `/clean`) had their multi-file read phases converted from serial loops to parallel tool-call batches. For `/catalyst`, `/prune`, `/scenario`, full-file Reads are preserved (research-quality gated). ~30–60% wall-clock speedup on monthly maintenance chain; no user-visible behavior change. Per-skill breakdown: [[INFRASTRUCTURE.md]] §12.6.

### Sonnet-max downgrade for 5 mechanical skills
`/graph`, `/rename`, `/rollback`, `/status`, `/clean` moved from Opus 4.7 max to Sonnet max (effort: max preserved). ~40-60% faster wall-clock with no correctness impact observed. Watch for regressions on `/status` trigger-conflict detection and `/rollback` multi-file cascade classification — the first two to revert if Sonnet proves insufficient. Revert is a one-line SKILL.md frontmatter change per skill.

### Forked context on `/surface`
`/surface` joined `/lint` and `/prune` in the forked-subagent set (now 3 skills). Unscoped `/surface` main-context cost drops from ~380K tokens to ~15K (final summary only). Monthly maintenance chain main-context tokens: ~847K → ~457K. Trade-off: subagent intermediate reasoning discarded on return — follow-ups on `/surface` findings require a scoped re-run.
