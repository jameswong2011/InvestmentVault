---
publish: false
date: 2026-07-09
tags: [meta, audit, skills]
status: active
source: Round-2 full-vault skills test — 6 parallel execution agents; regression-verify of the same-day 5-stage remediation + invocation-permutation coverage
---

# Skills Audit Round 2 — Execution Test — 2026-07-09

**Relationship to Round 1**: [[_Archive/Docs/2026-07-09 - Skills Audit Report]] found the defects; [[_Archive/Docs/Changelog]] Stage 1–5 applied fixes. This pass **executed** the fixed snippets/scripts under the real runtime (zsh 5.9, macOS/BSD awk+sed, PyYAML absent, ugrep shim) and traced the most common invocation permutations of all 21 skills against live vault state. Every claim below was reproduced by execution or exact line-cited spec reading; all mutations ran in /tmp — the vault was not modified. Git-solved issues (pure data-loss recovery) excluded per instruction.

**Headline**: the remediation largely landed — locks, manifests, lint FP-factories, script gates, archive-callouts routing, /compare and /status state machines all verified working by execution. But (a) **four Round-1 fixes never actually shipped** despite audit listing (thesis archive-collision, rename link patterns, sync Step 3a/1.7, catalyst trio), (b) the changelog **overclaims once** (wikilink-forms.md was never touched), (c) execution surfaced **9 new HIGH+ defects** Round 1 missed — including two script gates that still delete good notes and a /graph lock that every other skill classifies as stale — and (d) the vault's **live state makes both non-ticker /sync modes unusable today** (watermark collapse, >1M-token change set).

---

## 1. Remediation scorecard (per changelog claim, by execution)

| Stage | Claim | Verdict |
|---|---|---|
| 1 | `_hot.md` RCC heading restored | ✅ VERIFIED (line 31) — but file is 4,316w, **still over the 4,000 soft cap** (RCC 1,681w + OQ 1,739w are 2.8–2.9× their section budgets); P0.1's "compress below soft cap" did not complete or regrew |
| 1 | `_graph.md` rebuilt | ✅ done 01:41Z — **already stale again**: CBRS thesis (created 12:45) absent, DRAM Memory Cycle macro unlinked, 3 stale `log_tail` caches (6981/CBRS/PLTR). One `/graph last` clears it |
| 1 | NVDA/AMD/INTC `sector:`, 7 `@`-sector frontmatter, retro `propagated_to: []`, stuck sync manifest flipped, `.locks/` removed | ✅ all VERIFIED |
| 1 | Broken wikilinks repaired | ⚠️ PARTIAL — 20 of Round 1's ~25 still broken (lint #3 list in §4) |
| 2 | `Macro/`→`Macro & Technology/` "across 13 skills/contracts" | ⚠️ OVERCLAIMED — sync/retro/prune/archive-callouts/rollback/rename all verified fixed by execution, but **`_shared/wikilink-forms.md:29` still enumerates FOLDER as `Macro`** (`last_reviewed: 2026-04-20`, untouched) |
| 2 | zsh lock contract (`[[ > ]]`, 1.3c leak, noclobber) | ✅ VERIFIED end-to-end in /tmp: live≠stale, backdated→STALE, 3-ticker partial-acquisition rollback incl. BRK-B, noclobber TOCTOU, **10× simultaneous-acquisition race with 0 double-acquires**. Residuals open: §1.7 release still unconditional `rm -f`; early-abort paths never release (stale-out only); `.vault-lock.readonly` still has no acquisition snippet |
| 2 | lint.py FP factories | ✅ VERIFIED — full run: **0 Critical / 71 Important / 149 Nice**, and the 71 are **100% true positives** (full triage in §4). 336→68 claim consistent (+3 = same-day activity) |
| 3 | verify_note.py #12/#13/#5 | ✅ VERIFIED (Roman numerals pass, `$1 5B` caught, NVDA earnings note survives at ADVISORY, earnings exemption works) — but two **new** false-BLOCK bugs found (§3 H3/H4) and the exemption exists only in the script, not the SKILL's manual-fallback text |
| 3 | extract_transcript_signals.py Q&A split | ✅ VERIFIED — NVDA prep remarks 51→2,572w exactly as claimed; 0 boilerplate mis-splits across 23 cached transcripts; flag-gating suppresses the −100% deltas. New gaps: 5/23 transcripts with real Q&A return `qa_detected:false` (marker variants missing); evasiveness now honest-but-always-None (23/23) |
| 3 | numbers_compute.py forward-P/E / FCF-margin / % / slash | ✅ all VERIFIED by synthetic-JSON + NVDA end-to-end (12/21 rows mapped, Notes column preserved 21/21) |
| 4 | archive-callouts ticker routing / probe / lock release | ✅ VERIFIED (7/7 inputs route correctly incl. `2383`, `285A`, `2383 90`) |
| 4 | rollback list filter / 6.2b / registry awk; per-PID `cp & wait` ×3 skills | ✅ all VERIFIED by execution (37 restorable / 31 manifests excluded; forced-fail cp detected) |
| 4 | compare re-lock / batch prefix / 5.5c; status batch-ID / zsh closure | ✅ VERIFIED (3-ticker batch-prefix lookup executed; full GAW closure cascade executed in /tmp) |
| 4 | numbers Step-4 dir path; transcript cache-poisoning | ✅ VERIFIED (end-to-end; 404-sim leaves no poisoned cache) |
| 5 | Lint-ID citations, skill counts, UG/INFRA rows, contracts 6→7 | ✅ VERIFIED with 2 residues (INFRA:396 #43 severity row; UG:18 `/sync TICKER` graph-dependency contradiction) |

**Round-1 items that never shipped (not in any changelog stage):** /thesis archive-collision signals; /rename link-pattern table; /sync Step 3a section-slice + Step 1.7 awk primary-path; /sync Step 2.5 graph-staleness guard; /catalyst trio (rename-marker preflight, lock timeout, format decision); /prune PREFLIGHT-BLOCKED dead end; delegation recursion guard; allowed-tools underscoping (P1.3); scale constants (P1.8).

---

## 2. Blocker — live state makes non-ticker /sync unusable

`.last_sync` = 2026-06-18; **145 files** mtime-newer (77/77 theses, 50/50 sectors, 9/9 macros) vs **2** files actually modified vs git HEAD — the Jul 3–4 bulk-mtime touch. Executed consequences:

- **Default `/sync`**: change-detection admits ~69 changed sources ≈ 500K words of deep reads. **`/sync all`**: Pass 2 classifies all 77 theses High-delta (self-modified) → >1M tokens, not completable; dozens of Body-change-override git-diff prompts.
- Same collapse **poisons /clean**: `/clean 30` → 21 age-expired snapshots, all 21 falsely reclassified "Active-safety-net" (source mtime > snapshot_date) — the mtime heuristic is now spuriously over-protective.
- `/prune` dead-ends with certainty: subagent returns PREFLIGHT-BLOCKED on 145 files; user approval has no override contract → re-invocation re-blocks (prune:30 codifies the loop).

**Decision required (one of):** (a) advance `.last_sync` over mtime-only files after confirming the 2026-06-27 deferred AEHR + AI-Bubble propagations landed, or (b) add the Step 1.1 sanity gate (change-set > N% of vault → cross-check `git diff --name-only` since watermark, offer watermark advance) and then advance. Until then: ticker-scoped `/sync TICKER` works fine (verified).

---

## 3. New findings (execution-verified, deduped across 6 clusters)

### HIGH — wrong results or hard failures on common invocations

| # | Skill : permutation | Defect (executed evidence) | Fix |
|---|---|---|---|
| H1 | `/graph` lock ↔ any concurrent skill | graph's inline lock has no `timeout_at:`/noclobber → preflight consumers grep empty timeout → `[[ "" > now ]]` false → **live /graph lock classified STALE**, message invites force-unlock of a live run (reproduced in /tmp) | Replace graph's snippet with preflight 1.3a |
| H2 | `/transcript` any live fetch | Step 0.4 key extraction: BSD `sed -E` lacks `\s` → API_KEY = whole JSON line → passes `[ -z ]`, prints FMP_KEY_OK, then **every curl exits rc=3**. Reproduced verbatim | `jq -r .fmp_api_key .data/config.json` |
| H3 | `/ingest` url/pdf post-write verify | verify_note.py #1 YAML heuristic false-BLOCKs any unquoted value containing an em-dash (valid YAML) — and the heuristic is the **live path** (PyYAML not installed). Real note `2802 vs 6857 - Competitive Comparison` → BLOCK → url/pdf mode deletes a good note | Drop the `"—" in val` condition, or heuristic-path → advisory |
| H4 | `/ingest` post-write verify | #4 mid-sentence check ignores trailing digits/quotes: line ending `…respectively, in 2026."` → final word "in" → structural BLOCK (real DRAM HBM deep-dive) | Short-circuit when final char ∈ `.!?"')` |
| H5 | `/rename` table/anchor-linked thesis | 7-pattern table misses `.md#anchor` and escaped-table-pipe forms → **silent wikilink breakage** (wrong-result, not git-recoverable). /tmp mini-vault: 4 surviving unrewritten links. Live exposure: 18 `\|` thesis links (INTC/PCOR/PINS/+1) + 2 `.md#` (SOI) | Prefix-rewrite `[[Theses/T - old` and `[[T - old` at the `]] \| # .` boundary set |
| H6 | `/thesis KLAC` (archived-ticker) | All 4 archive-collision signals miss `_Archive/Theses/SEMICAP - ….md` (`ticker: [KLAC, AMAT, …]`, `status: archived`): non-recursive globs, scalar-ticker regex → silent duplicate of archived analysis | Recursive glob + list-form ticker grep + accept `status: archived` |
| H7 | `/numbers 2383`, `6981`, foreign | FMP symbol catch-22 (live-verified: `symbol=2383`→`[]`, `2383.TW`→Elite Material; `6981`→`[]`, `6981.T`→Murata): these theses can **never** succeed. Same class in /transcript (000660). Plus **comma-thousands parse corruption**: `¥35,950`→old=35.0, `₹10,000 crore`→10.0 (4 live rows) | Spec: FMP symbol := frontmatter `ticker:`; normalize 2383→2383.TW, 6981→6981.T, GAW→GAW.L; strip commas in `parse_old_numeric`; add ₹/crore/NT$ |
| H8 | `/surface` default & TICKER | Read budget is fiction: 50 sector notes = 445K words read IN FULL + thesis sections 127K ≈ 620K+ words > subagent context → silent truncation on the exact sections the edge lives in. Sector-scope resolution unfixed: the SKILL's own example `/surface semiconductors` resolves to **0 matches** (case-sensitive keys, no sector-resolution routing, no no-match behavior). `/surface CBRS` (thesis newer than graph) has no spec branch | extract_sections.py targeting for sector notes; route through `_shared/sector-resolution.md`; add adjacency-miss + glob-hit branch |
| H9 | `/retro` after `/sync` | **Zero exclusion** of sync-propagated Log entries: format `- [[Research/note]]: …` has no registered prefix → classified "manual = highest signal" → machine propagation read as user conviction across every synced ticker | Third class `sync-propagated` (bullet starts `[[Research/` under a `(/sync)` date header) |

### MEDIUM (selected; full detail in cluster transcripts)

- **/sync**: Step 3a section-slice awk still returns heading-only (executed on NVDA/PLTR/6981 — `/sync all` Low-delta slices analyze empty sections; extract_sections.py works, only /surface migrated). Step 1.7 broken awk still the primary path (errors on macOS awk; grep alternative works). No Step 2.5 graph-staleness guard (RATIONALE claims it; SKILL doesn't implement). Multi-bullet date-blocks defeat last-bullet-only prefix classification (PLTR deepen block would be counted as sentiment). Lock timeouts contradict preflight (15/5 min vs 10 min; default /sync missing from taxonomy).
- **/status**: no behavior defined for conviction change on the **37/77** theses without `## Conviction Triggers`; nonexistent-ticker abort never releases the lock; paste-value convention only partially adopted (Step 7.5b still uses undefined cross-block $VARS); archive-location conflict (root vs `_Archive/Theses/`) still unresolved (P3.7).
- **/catalyst**: untouched by remediation — no rename-marker preflight (only vault-wide writer without it), 5-min lock vs its own 5–30-min progress contract at now-86 reads, spec-vs-live format decision unmade (spec-literal regeneration drops the live `## Macro / Non-Earnings Catalysts` + `## Notes` sections). Still 47d stale (P0.9 open).
- **/transcript**: FMP dates endpoint returns `fiscalYear` not `year` (spec-driven jq → null → malformed URL); 5/23 cached transcripts with real Q&A silently `qa_detected:false` (marker variants; affects holdings 6857/AIXA); evasiveness metric permanently None — dead weight in the Evidence table.
- **/ingest batch**: `Presentation.pptx` still invisible (no UNSUPPORTED bucket — fix never applied); personal bank PDF still enters TO PROCESS (no out-of-scope gate); both files still sitting in `_Inbox/` (P0.10 open).
- **/brief**: batch mode's "read-only lock acceptable" contradicts its own Phase-4 `_hot.md` writes (reintroduces the audited race); falsifier-from-Conviction-Triggers has no fallback for the 38 theses lacking the section.
- **/compare → /rollback**: `/rollback compare-YYYY-MM-DD-HHMMSS` (the manifest's own recovery command) is not a recognized rollback argument form; 2.5a wording is exact-match while batches are prefix+slug.
- **/prune**: staleness flag keys on ANY last-Log date — one vault-wide realignment reset staleness portfolio-wide (all 35 monitoring theses share the same 2026-05-22 tail); KEEP-MONITORING verdicts have no landing field (evaporate after chat); no downgrade verdict exists.
- **/scenario**: still inline (no delegation) with an ~87-read ≈ 515K-word Pass 1 in main context; allowed-tools can't execute its own lock protocol; reverse mode's fully-live path writes no `## Reversal Notes` and never clears `propagated_to:` (all confirmed against the real Iran scenario — 11/11 tickers live); R2.1 archive glob misses `_Archive/Theses/`.
- **/retro**: unreactive scoring fix is **dead code** — `max(2.0, 0.5×|move|)` with flat defined as ≤3% ⇒ always exactly 2.0, still can't cross the 3.0 cluster threshold. Minimal fix: `2.0 + 0.5×|move|`. 1q window activates 77/77 tickers → 231 cold-cache WebSearches, budget constants stale.
- **allowed-tools underscoping (P1.3) — still unfixed across ~9 skills**; scenario/brief/thesis lock blocks need commands their frontmatter doesn't allow.

### LOW (roll-up)

/graph generator: `bogus` arg stamped as `graph_mode: bogus`, non-UTF-8 crash without filename, body-`status:` matching (all still open); Reverse Index omits zero-inbound macros (DRAM note invisible — no skill will surface it for linking). /sync TICKER: no recency scoping (~60+ full reads for NVDA); draft-thesis propagation unspecified (13 drafts). /deepen: no ART/`_hot.md date:` update from today's live run. hot-md contract: write-then-compress vs sync's stage-then-commit contradiction; word-count method undefined; future-dated OQ entry (2026-08-26) defeats age math. /clean: bare `--include-orphans` empty-token unfixed; 7 invisible artifacts remain (6 frontmatter-less snapshots + 2.2MB tar.gz invisible even to the `-name '*.md'` inventory). /rollback: unparseable-snapshot restore path derivation undefined (VRT case); sync-manifest Tier B header prefix mismatch. /archive-callouts: `--dry-run` (double-dash) aborts; 3 nonconforming pinned headers tolerated by luck. /transcript & /ingest: zsh bare-glob `ls` error leakage; check #5 floor non-monotonic at tier boundaries; SKILL text still calls #13 "BLOCKING" (script says advisory). /stress-test: "13 sections" ×2 stale; no re-run recency guard (real AEHR double exists). Docs: UG:18 sync-graph contradiction; UG `--all` blurb wrong (`--all` = active+high, `--all-active` undocumented); INFRA:396 #43 severity; preflight §1.2 omits /numbers, /transcript, /retro.

---

## 4. Live vault-state actionables (lint triage: 71 Important = 71 true positives)

| Item | n | Detail |
|---|---|---|
| Watermark decision (§2) | 1 | The single highest-leverage action — unblocks /sync default/all, /prune, and un-poisons /clean |
| `## Conviction Triggers` missing | 38 | 285A APP AVGO BESI BTC-CRYPTO CCJ CRCL CSGP DE DUOL EDEL EINK GAW HIMS IOT IQE ISRG KAMBI LITE LNG META MTN NET NFLX NOW NVDA OPEN PANW PLTR PSTG RELIANCE SHOP SNDK SPOT STNG TTWO UBER WTC — now creatable via `/deepen TICKER Conviction Triggers` (Case A scaffold, adopted) |
| Broken wikilinks | 20 | `_Archive/Sectors/` ×5 · `_Inbox/processed/compass_artifact_*` ×6 · Iran `_Archive/Macro & Technology/` ×4 · `[[Macro/AI capex supply chain]]` (AMAT) · `[[Macro & Technology/AI Compute Infrastructure]]` (6857) · `[[Theses/TYL]]` (CSU) · `[[Theses/ASML]]` (DRAM & HBM) · Australian Healthcare (Consumer Telehealth) |
| `/graph last` | 1 | Clears CBRS + DRAM staleness (#19/#23) |
| `/catalyst` re-run | 1 | 47d stale — but fix the MEDIUM catalyst items first or the regeneration drops live sections |
| `_hot.md` compression | 1 | 4,316w > 4,000 soft cap; load is in RCC (>30d entries → one-liners) + OQ (>14d cohorts); also fix the future-dated 2026-08-26 OQ entry |
| `source_type:` missing | 3 | AIXA-VECO synthesis, 2026-05-24 Rebalancing synthesis, today's Automation-Lens synthesis |
| `propagated_to: []` missing | 1 | 2026-05-29 6-Holdings synthesis |
| Sector MOC gaps | 2 | 2802 ← ABF Substrates; VICR ← Data Center Power & Cooling |
| Ticker-no-thesis | 3 | CETY, ETH, BLK research notes |
| Inbox hygiene | 2 | `Presentation.pptx` + personal bank PDF still in `_Inbox/` (P0.10) |
| Foreign-ticker frontmatter | 3 | 2383→2383.TW, 6981→6981.T, GAW→GAW.L (unblocks /numbers + /transcript for those names) |

Judgment candidates: lint #28 TOTO/INTU = FPs (complete sentences); #12 GAW/SPOT/SIVE = legitimate review flags. Noise to tune: #53 ×26 (template-born empty Legacy Callouts), #8 ×55 (monitoring-status inactivity).

---

## 5. Analytical quality — adopted vs still open

**Adopted (verified in spec + live outputs):**
- Mental-models gates (P1.6): `_shared/mental-models-section.md` rewritten as the operational contract; explicit gate blocks in /thesis, /stress-test (incl. fired-triggers-as-disconfirmation-targets), /compare, and all four delegation-cluster prompts (skill-adapted READING PROTOCOL blocks). /brief codified as exempt distiller via the new falsifier requirement.
- /thesis conviction-after-bear-case (live CBRS Log demonstrates it); 14-section list matching template.
- /deepen Case A template-section scaffold — closes the Conviction-Triggers creation dead end.
- /surface ≥2 cross-note datapoints + falsifier per opportunity.
- /sync Step 4b cross-thesis contradiction sweep (but the peer-side action is a dead letter — no accumulator/report field).
- /retro neutral-news 0.5× rung; `Numbers refresh:` registry closure.
- Live-output quality is strong where sampled: PLTR deepen (retires a named bear kill-switch, names the next falsifier, ends "conviction unchanged, two-sided"), 2383 stress test (attacks the thesis's own trigger framework), 2026-06-06 surface scan ("triple-counting the HBM trade"), 2026-05-24 retro (000660 inverted-bear gap). The machinery's stated purpose — non-consensus connection-finding — is observable in the artifacts.

**Still open (ranked by vault-purpose leverage):**
1. **/deepen mental-models reading gate** — the contract lists deepen only as a section-writer; a Bull-Case/Risks deepen escapes the mandate CLAUDE.md explicitly assigns it. (Concrete block drafted in cluster report.) Add /deepen to the judgement-renderer list.
2. **/status falsifiable-rationale requirement** — Tier-3 conviction changes still accept bare assertions; quote the matching trigger or print "no triggers defined — unfalsifiable change", record `trigger_alignment:` in the manifest.
3. **/sync mental-models gate at Step 2** (implication generation) — currently write-time-only, so models never inform what gets propagated; and extend 4b "contradicts" outcomes to permit Tier B appends into peer Risks/Bear Case (propagation is still structurally bull-additive at thesis level).
4. **/stress-test Phase 2.5 mandatory-unless-waived for high-conviction** — still optional; internal-only runs recycle the vault's confirmation set.
5. **/catalyst `Thesis test` column** — calendar captures direction, never falsification; populate `[observable + threshold] → [confirms Insight #n | fires → LOW trigger]` from Conviction Triggers during the Phase-1 read (000660's own Catalysts table is the in-vault exemplar). Add `Falsifiable?` to No-Catalyst list → doubly-dead-capital prune signal.
6. **Delegation recursion guard** — one standard "you are the EXECUTOR, do not re-delegate" paragraph in surface/retro/prune prompts + the /prune `PREFLIGHT_OVERRIDE:` contract.
7. **verify_note.py consensus-contrast advisory check** — spec requires it, notes comply, gate doesn't check (regex drafted: Thesis Delta ~ `/consensus|priced|market (assumes|expects|misses)/i`; Contradiction Check contains `§` or `[[Theses/`).
8. **Stable trigger IDs in `Generalist - Overview`** (`[G-1]`…) — unnamed prose bullets break /sync's Mental-Models merge idempotency; Lens/Industry files already have citable §IDs.
9. **/retro unreactive scoring** — replace dead-code `max(2.0, 0.5×|move|)` with `2.0 + 0.5×|move|`.
10. **Three new lint checks**: #57 watermark-collapse alarm (pending-sync > 20% of vault → CRITICAL with guidance), #58 snapshot-integrity (frontmatter-less snapshots + non-.md artifacts), #59 template-drift-at-birth (new thesis missing template sections → IMPORTANT immediately).

**Snapshot economy under working git** (per instruction, git-solved items excluded from findings; forward guidance only): keep manifests as semantic transaction ledgers + /rollback's cascade brain + the 30-day closure regret floor; retire raw snapshot `cp` in favor of pre-edit git SHAs recorded in manifests (`git show SHA:path` also fixes the VRT unparseable-restore dead end); replace /clean's mtime safety-net with `git log -1 --format=%cI`.

---

## 6. Suggested remediation sequence

1. **Unblock the vault (state, ~20 min)**: watermark decision (§2) → `/graph last` → `_hot.md` compression → the §4 metadata fixes (source_type, propagated_to, foreign tickers, inbox hygiene).
2. **Wrong-result class (H-items)**: H3/H4 verify_note false-BLOCKs (deletes good notes), H5 rename patterns, H7 comma parsing + symbol mapping, H2 transcript key extraction, H1 graph lock, H6 thesis collision signals.
3. **Ship the four Round-1 fixes that never landed**: sync 3a→extract_sections.py + 1.7 grep-primary + 2.5 staleness guard; catalyst trio; thesis Step 7/lock release; prune override contract + recursion guard.
4. **Consistency pass**: H8 surface scoping + sector resolution, H9 retro sync-propagation class, status/brief/compare/scenario MEDIUMs, allowed-tools (P1.3), preflight taxonomy rows, doc residues.
5. **Analytical upgrades** (§5 items 1–10) — highest long-run value.

## Verified-working (no action)

Preflight lock contract end-to-end under zsh incl. 10× concurrency race · manifest lifecycles all 31 live manifests `completed` · full /status closure cascade (executed) · /compare batch naming + per-PID failure detection + competitor re-lock · /rollback list/cascade incl. full PLTR-deepen restore simulation · /rename sanitization + marker hard-block in 14 skills (3 spot-executed) · archive-callouts routing 7/7 + 0 sweep candidates until 2026-10-23 + `[[preserve]]` migration complete · lint.py scoped modes + exit codes + #54/#55 · verify_note #12/#13/#5 (script) · transcript split/flags/cache-promote · numbers_compute forward-P/E/FCF/suffix/slash + Notes invariant · generate_graph full/last idempotence + self-validation · graph-primer consumption in all 6 consumers · dedup paths (URL same-day/cross-day) · today's live `/thesis CBRS` + `/deepen PLTR` runs spec-compliant (2 soft deviations: skipped Mental-Models side-update despite materially-changed trigger; 120-word Log entry vs 2-line contract).
