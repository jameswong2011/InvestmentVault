---
date: 2026-07-09
tags: [meta, changelog, infrastructure]
status: active
source: Vault infrastructure rollout history — the dated-narrative home referenced by User Guide §13/§14 and INFRASTRUCTURE §12.6
---

# Infrastructure Changelog

> Dated rollout narratives and measured-impact tables for the vault's skill/consistency machinery. INFRASTRUCTURE.md and User Guide.md hold only the **evergreen** contract; time-boxed history lives here. Newest first.

## 2026-07-09 — Skills audit remediation (stages 1–5)

Full findings: [[_Archive/Docs/2026-07-09 - Skills Audit Report]]. Applied in five stages:

- **Stage 1 — vault state**: restored the missing `_hot.md ## Recent Conviction Changes` heading (13 skills were silently no-op'ing conviction writes); rebuilt `_graph.md` (ONTO + 5 drafts were invisible); fixed NVDA/AMD/INTC `sector:` (was `GPU & AI Compute Accelerators`/`Compute & AI Accelerators` → `Compute & AI Compute Accelerators`); added `sector:` frontmatter to 7 `@`-prefixed sector notes; set the 2026-05-24 retro note `propagated_to: []`; repaired ~broken wikilinks; flipped the 41-day stuck `_sync-manifest` to completed; removed dead `.locks/`.
- **Stage 2 — systemic one-liners**: `Macro/` → `Macro & Technology/` across 13 skills/contracts (macro layer was invisible to ~7 skills); zsh-safe lock contract in `preflight.md` (`[ \> ]` → `[[ > ]]`, was classifying every live lock STALE under zsh; + 1.3c leak + noclobber); `lint.py` FP factories (#23 250→0, #26, `\|` table-pipe, list-`ticker:`) — full-vault Important findings 336 → 68.
- **Stage 3 — script gate hardening**: `verify_note.py` #12 (Roman-numeral / decimal-drop) + #13 (query-strip + advisory-not-block) + #5 earnings exemption (was deleting good notes); `extract_transcript_signals.py` Q&A-split BLOCKER (operator-boilerplate mis-split, prep-remarks 51→2,572 words) + flag-gating + analyst-only evasiveness + period label; `numbers_compute.py` forward-P/E next-FY selection + FCF-margin units bug + `%` suffix + slash-normalization.
- **Stage 4 — state-machine consistency**: `/archive-callouts` numeric-ticker misroute (glob-check, was promoting scoped dry-run → unconfirmed vault-wide execute) + `grep -cE` probe + per-scope lock release; `cp & wait` failure-detection (per-PID) across archive-callouts/rollback/compare; `/rollback` list manifest-filter + 6.2b grep-exit + registry dead-code; `/compare` single-ticker re-lock + manifest↔sector batch prefix + 5.5c branch; `/status` batch-ID ticker-qualification + the `! ls` zsh closure bug; `/numbers` Step-4 dir-path (was reading an empty json-dir → all fetch_gap); `/transcript` cache-poisoning (fetch→temp→validate→promote).
- **Stage 5 — contract/doc reconciliation** (this pass): log-prefix registry `#29` Criticals (CLOSED/Initial-thesis consumer drift, 2→0); lint-ID citations (CLAUDE.md #44–48 → #50–53/#56; INFRA #50m collision, #41 phantom `phase:`; archive-callouts #48→#56, #53b/d→#53; deepen #50→#50m; graph #38); skill counts 19→21 + `/numbers`/`/transcript` rows in the §0.4 + §14 matrices; RATIONALE 10→15; contracts 6→7 (mental-models-section.md); `/ingest` "<150 words" → scaling floor.

## Convention

Add a dated `## YYYY-MM-DD — <title>` section per rollout. Keep entries factual (what changed, measured impact, affected files); the reasoning lives in each skill's RATIONALE.md.
