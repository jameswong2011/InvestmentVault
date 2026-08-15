---
publish: false
date: 2026-07-15
tags: [meta, audit, capability-review]
status: active
source: Full-vault capability & engineering review — 4 parallel read-only agents (content layer, core pipeline skills + shared contracts, remaining 17 skills, infrastructure/config/docs); benchmarked against LLM-vault ecosystem archetypes
---

# Vault Capability & Engineering Review — 2026-07-15

**Scope**: all 21 skills + 11 shared contracts read in full; content layer sampled across 81 theses / 204 research notes / 50 sector notes / 9 macro notes; infrastructure layer (settings.json, git, snapshots, multi-frontend dirs, doc triad) inventoried. Comparison basis: ecosystem archetypes from model training knowledge (public CLAUDE.md setups, RAG plugins, memory-MCP systems, agentic skill repos) — not other private vaults. Related prior audits: [[_Archive/Docs/2026-07-09 - Skills Audit Report]], [[_Archive/Docs/2026-07-09 - Skills Audit Round 2 - Execution Test Report]].

**Verdict: Capability 9/10 · Engineering quality 7.5/10.** The most sophisticated LLM-augmented personal research vault in the reviewed archetype space — top ~1%. The design layer (contracts, transactionality, self-linting governance) exceeds most professional internal research tooling. The gap between design and guarantee is the story: every safety invariant is model-cooperative prose with zero harness enforcement, the most destructive skill is the least deterministic, and several flagship subsystems are specified but not operationally adopted.

---

## 1. Position vs. the ecosystem

| Archetype | What they typically have | This vault vs. them |
|---|---|---|
| CLAUDE.md + folder conventions (90% of LLM vaults) | One instructions file, ad-hoc prompts, no write governance | Generations ahead — 21 skills, 11 shared contracts, 66-check linter |
| RAG-plugin vaults (Smart Connections, Copilot, Khoj) | Semantic retrieval, zero write-path safety | Ahead on everything except embedding search, which this vault lacks entirely |
| Memory-MCP / basic-memory systems | Structured write APIs, no domain workflow | Ahead — domain workflow (ingest→sync→graph→retro) is the whole point here |
| Serious agentic skill repos (best public examples) | 5–10 skills, no shared contracts, no transactions | Ahead — nobody else has manifests + rollback cascades + a linter that lints its own governance |
| Institutional research platforms (Tegus/AlphaSense + internal tools) | Hard enforcement, databases, alerting, position links | **Behind on all four** — exactly this vault's gaps |

Four mechanisms essentially unseen elsewhere:
1. `/lint` mechanizing 62 checks that validate the governance layer itself (lock hygiene, manifest integrity, contract drift, callout schema).
2. Dated post-mortems embedded in specs driving rule evolution (2026-04-22 sector-skip → CLAUDE.md Rule #11; 2026-06-04 token-ceiling failure → deterministic graph generator).
3. Epistemics-as-code: READING PROTOCOL with stable `[G-n]` merge keys used for skill idempotency, falsifiable conviction triggers, `[1×: source]` provenance tags, append-only calibration JSONL.
4. Generated multi-frontend parity: `port_claude_skills.py` → AGENTS.md + `.agents/skills` with `--check` mode; Codex read-only/worker privilege split.

## 2. Capability scorecard

| Dimension | Score | Evidence |
|---|---|---|
| Ingest & structuring | 9 | `verify_note.py`: 16 checks, regressive retention curve (0.65→0.18 by source size), per-source_type domain validators, verify-before-commit with source-as-marker |
| Propagation (/sync) | 8.5 | Manifest+snapshot transactions, cross-thesis contradiction sweep, skill-origin gating via log-prefix registry — capability best-in-class; execution risk docks it |
| Knowledge graph | 8.5 | Deterministic union-find generator, body-diff idempotency, self-validation, off the token path — but silently drops folderless wikilinks |
| Adversarial analytics | 9 | Stress-test anti-anchoring independent draft, scenario market-pricing calibration ("market implies X% / I estimate Y%"), retro narrative-vs-price gap ranking |
| Feedback loops | 9 | 259 callouts (195 addressed, 28 pinned files, 0 deprecated markers), Prompt/Response audit-trail contract, calibration logs — used, not just specified |
| Market data | 8 | FMP fail-closed numbers/transcripts/catalyst, poisoned-cache prevention, Notes-column preservation invariant; no scheduled refresh |
| Safety & undo | 8 design / 5 guarantee | 305 snapshots (2 months), 7-branch rollback cascades, 30-day closure regret floor — all cooperative, nothing enforced |
| **Portfolio integration** | **3** | 34 real holdings in [[Live Portfolio.md]], 81 theses, zero skills connecting conviction to position sizing; 0 wikilinks from portfolio to theses |
| **Alerting/monitoring** | **2** | trigger-touch fires only when a skill happens to run; nothing watches conviction-trigger thresholds between runs |
| Conviction backtesting | 3 | `/retro` calibration scores only its own directional calls; `/status` conviction changes are never graded against realized outcomes |

## 3. Engineering quality scorecard

| Dimension | Score | Evidence |
|---|---|---|
| Architecture | 9 | `_shared/` contracts with producer/consumer/breakage registries; single-owner metadata files; no circular dependencies found |
| Documentation | 9.5 | [[CLAUDE.md]] (LLM) / [[User Guide]] (human) / [[INFRASTRUCTURE]] (ops) triad verified mutually consistent; AGENTS.md deterministically generated |
| Determinism | 7 | Bimodal: graph/lint/ingest/numbers/transcript script-backed; `/sync` is 968 lines of pure LLM prose on the highest-blast-radius op, with 3 documented silent failures |
| **Enforcement** | **3** | settings.json contains only a permissions allowlist (136 entries, ~40+ single-use forensic one-offs). Zero hooks. Locks/snapshots/Tier-3 gates depend on model compliance; Claudian runs `permissionMode: yolo` |
| Spec consistency | 6.5 | Canonical lock table (preflight §1.2) missing `/numbers`, `/transcript`, default `/sync`; 10m-vs-15m `/sync all` timeout contradiction; phantom `.drift-config.md`; stale scale counts (catalyst "65", surface "~76" vs actual 81) |
| Spec economy | 6.5 | Fat right tail: rollback 811 / retro 733 / transcript 665 / deepen 610 lines — the 5 longest files are ~34% of the corpus and exceed reliable single-pass LLM execution |
| Repo/ops hygiene | 5 | 45MB chat-export zips tracked in git; commit messages "Big Fix"/"Mac 3"; plaintext FMP key in `.data/config.json`; `Bash(python3)` arbitrary execution pre-approved |

### Per-skill engineering scores (0–10)

| Skill | Lines | Score | | Skill | Lines | Score |
|---|---|---|---|---|---|---|
| lint (+lint.py) | 84+1199 | 8.5 | | scenario | 357 | 8 |
| clean | 318 | 9 | | thesis | 431 | 8 |
| numbers | 528 | 9 | | status | 551 | 8 |
| brief | 147 | 8.5 | | ingest (+verify_note.py) | 356+399 | 8 |
| catalyst | 354 | 8.5 | | graph (+generate_graph.py) | 132+327 | 8 |
| stress-test | 348 | 8.5 | | surface | 272 | 7.5 |
| archive-callouts | 452 | 8 | | prune | 544 | 7.5 |
| compare | 450 | 8 | | transcript | 665 | 7.5 |
| rename | 509 | 8 | | deepen | 610 | 7 |
| shared-contract layer | 11 files | 8 | | retro | 733 | 7 |
| sync | 968 | 7 | | rollback | 811 | 7 |

Pattern: the lean skills (brief 147, surface 272, clean 318, stress-test 348) are the most reliably executable; length correlates with mode-cramming (deepen, retro, transcript) or cross-skill coupling (rollback's 7 hardcoded manifest branches).

## 4. Highest-severity findings

1. **No enforcement layer.** A PreToolUse hook could deterministically block writes without a held lock, protect Tier-1 files, and enforce append-only Logs. Today one non-compliant run bypasses everything the 569-line preflight contract promises. Compounded by yolo-mode frontend + pre-approved arbitrary `python3`.
2. **Determinism is inverted.** `/graph` (read-only output) got a script; `/sync` (mutates theses, sectors, macros, `_hot.md`) did not — and its own spec records three silent failures (2026-04-22 sector-skip, 2026-04-26 awk misclassification, Rule #11 truncation class).
3. **Adoption gaps in flagship systems.** [[_followups.md]] empty despite 10 stress-tests that should have populated it — the INTU "reassess HIGH→medium" finding (the exact failure the contract cites as its raison d'être) sits unactioned; sector `## Mental Models` populated in 2/50 vs 76/81 at thesis layer; `.last_sync` broken (0 bytes, 2026-04-29) so incremental `/sync` silently degrades to full-vault scans; [[_catalyst.md]] ~7.5 weeks stale; [[_graph.md]] 3 theses behind (LYV, TSEM).
4. **Legacy content contamination.** 139/204 (68%) research notes miss ≥1 required section, concentrated pre-April-2026. `Research/2025-02-19 - PLTR - Palantir Valuation Analysis.md` is ~70% off-topic raw chat export including verbatim NSFW content with named external sites — scrub regardless of broader remediation.
5. **Graph blind spot.** `generate_graph.py` ignores folderless `[[wikilinks]]` — a canonical form per `wikilink-forms.md` — so adjacency, reverse indexes, and orphan detection under-count silently; every graph-primer consumer inherits the gap.
6. **Lock protocol edge cases.** No guaranteed release (traps don't survive across Bash tool calls — hard-abort paths leak locks until manual `rm` or staleness); a lock with empty `timeout_at` evaluates as STALE, inviting force-unlock of a live run.
7. **Filename-vs-frontmatter split.** Research filenames ~76% non-compliant at the letter of the spec (50/204 missing source-type segment; 31 end in non-enum "Canvas") while `source_type:` frontmatter is 97% enum-correct — metadata is the real source of truth; the filename spec has drifted from practice.

## 5. Improvement roadmap

**P0 — close the guarantee gap:**
1. **Add hooks**: PreToolUse blocking Edit/Write to `Theses/|Sectors/|Macro*` without a live `.vault-lock*`; deny-list Tier-1 paths (`Templates/`, `.claude/skills/`) and bare `python3`. Converts ~2,000 lines of cooperative prose into hard invariants at ~50 lines of config.
2. **Script-back `/sync`**: extract changed-set computation, log-prefix classification, idempotency checks, and manifest writes into a `sync_helper.py`; leave analytical propagation to the model. Fix `.last_sync` immediately (one `touch` after a `/sync all`).
3. **Fix the drift set** (~half day): lock-table rows for `/numbers`/`/transcript`/default-`/sync`; the 10m/15m timeout; create-or-remove `.drift-config.md` references; folderless-wikilink handling in the graph generator; stale scale counts; `vault-explorer.md`'s deleted-folder references; preflight's phantom `/lint #1.4` pointer.

**P1 — close the capability gaps (highest analytical ROI):**
4. **`/reconcile` skill**: diff [[Live Portfolio.md]] holdings against theses — held-without-thesis, closed-but-still-held, HIGH-conviction-at-minimal-weight, sizing-vs-conviction mismatch. The suite optimizes the research layer while blind to the actual book.
5. **Scheduled automation**: nightly `/graph last`, weekly `/numbers --all` + trigger-touch (crossings → `_followups.md`), monthly `/catalyst`. Conviction triggers are falsifiable but unwatched between manual runs.
6. **Grade the caller**: extend `/retro` calibration to score actual `/status` conviction changes against realized prices — the vault cannot currently measure whether its conviction discipline works.
7. **Adoption backfill**: populate `_followups.md` from the 10 existing stress-tests; run the sector Mental Models pass (2/50 — the merge machinery exists, it never fired at sector level).

**P2 — hygiene:**
8. Quarantine or re-`/ingest` the pre-April-2026 research layer (PLTR note first). Relax the filename spec to match frontmatter-as-truth, or add a `/lint` auto-fix.
9. Purge 45MB chat zips from git history (or git-lfs); adopt a commit convention or post-skill auto-commit hook; move FMP key to keychain/env; prune the allowlist; delete `.tmp`, empty `.locks/`, and the stale `.claude/locks` reference.
10. Spec diet: split `--sync-metrics` out of `/deepen` into its own skill; replace rollback's 7 hardcoded manifest branches with a single manifest-schema contract producers must conform to; move `/transcript` detection prose into the script's docstring.

## 6. Evidence appendix (key stats)

- Content: 81 theses (~6,590 avg words, none <3,000), 204 research, 50 sectors (~8,951 avg words), 9 macro. Frontmatter 100% on 6 core fields across all theses.
- Conviction: high 21 / medium 52 / low 8. Status: active 33 / monitoring 31 / draft 17. 64% of theses created in a single April 2026 bulk event.
- Research required-section compliance: 65/204 (32%) fully compliant; failures concentrate pre-2026-04 (48 pre-2026 notes ≈ the raw-dump layer).
- Quality bimodality is temporal, not size-based: post-April-2026 output (LYV thesis, [[Sectors/Semiconductor Capital Equipment]] at 16,494 words with quantified switching costs and falsifiable position triggers) is institutional-grade; the legacy layer is raw deposits.
- Snapshots: 305 files / 15MB over ~2 months; trigger mix dominated by pre-numbers (156). Nothing yet eligible for `/clean` (180-day floor).
- `_hot.md`: 4,260 words (over 4,000 soft cap, under 5,000 hard cap), all 6 sections present, disciplined inline compression audit trail; self-flags the stale `.last_sync` watermark.
- Multi-frontend: `.claude` (canonical) / `.agents` (generated) / `.codex` (read-only + worker TOMLs) / `.claudian` (plugin, 123 session logs).
