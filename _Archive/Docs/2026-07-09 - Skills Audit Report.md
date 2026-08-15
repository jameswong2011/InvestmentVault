---
publish: false
date: 2026-07-09
tags: [meta, audit, skills]
status: active
source: Full-vault skills audit — 6 parallel read-only agents + executed script/bash repros
---

# Skills Audit — 2026-07-09

**Scope**: all 21 skills, shared contracts, 4 new Python helpers, cross-checked against CLAUDE.md / User Guide / INFRASTRUCTURE.md and live vault state. Every mechanical claim below was reproduced by execution (lint.py, generate_graph.py, verify_note.py, extract_transcript_signals.py, numbers_compute.py, extract_sections.py, and every preflight/skill bash snippet in /tmp under the real runtime: **zsh 5.9, grep→ugrep shim, macOS/BSD tools**). Issues that a working git setup already covers (pure data-loss recovery) are excluded per instruction.

**Headline**: the skill layer's *architecture* is sound (manifest lifecycles, propagated_to atomicity, dedup keys, snapshot discipline all verified working), but the recent cleanup left (a) one systemic path bug that blinds ~7 skills to the entire Macro layer, (b) a lock contract that fails under the actual shell, (c) a metadata layer (graph/watermark/hot/catalyst) that has drifted badly out of date, and (d) brand-new helper scripts with false-positive gates that would **delete good research notes**.

---

## P0 — Live vault state to fix before running anything else

| # | Item | Evidence | Fix |
|---|---|---|---|
| P0.1 | `_hot.md` missing `## Recent Conviction Changes` → every RCC write from 13 skills silently no-ops; also 4,885 words (over 4,000 soft cap, 115 under hard-cap abort) | lint #35 fires; heading absent between lines 27→72 | Reinsert heading manually; compress Sync Archive below soft cap |
| P0.2 | `_graph.md` 29d stale: ONTO thesis absent entirely, 7 stale `log_tail` caches (2383, 3110, 6981, AEHR, NOW, PLTR, WTC), 6 drifted adjacencies, 5 of 12 drafts invisible to all scoped skills | fresh-generate diff in /tmp | Run `/graph` (full) |
| P0.3 | `.last_sync` watermark collapse: 140 files newer (bulk mtime touch from Jul 3-4 git ops, content unchanged); 2026-06-27 manifest used illegal `mode:` value and deferred AEHR + AI-Bubble macro propagation with no tracked home | `find -newer` repro | Decide: `/sync all` once, or advance watermark after confirming deferred items are propagated |
| P0.4 | `_sync-manifest (sync-2026-05-29-025634)` stuck `in-progress` 41 days (companion snapshots: 2802, 6857, AIXA, VICR) | lint #41 | Inspect; flip to completed or `/rollback` |
| P0.5 | Sector propagation dead for flagships: NVDA + AMD `sector: GPU & AI Compute Accelerators`, INTC `Compute & AI Accelerators` — no such notes → ladder returns `none` → /sync, /status, /rollback, /compare silently skip their sector edits forever | ladder walk | Fix 3 frontmatter values to `Compute & AI Compute Accelerators` |
| P0.6 | 7 of 9 `@`-prefixed sector notes lack `sector:` frontmatter → resolve only at `substring` confidence → perpetual ⚠️ warnings + permanent confirmation gates on /compare & /rollback | ladder walk on all 9 | Add `sector:` frontmatter (matching @Telecommunications Services.md pattern) |
| P0.7 | `Research/2026-05-24 - Retrospective 1w` has `propagated_to: [6 tickers]` — must be `[]` (retro Invariant 3, INFRA §5.1); risks circular self-propagation on next /sync | lint #39 | Set to `[]` |
| P0.8 | ~25 real broken wikilinks (PLTR sell-off note missing ` - news` suffix ×4, `_Archive/Sectors/…` ×5, dead `_Inbox/processed/compass_artifact_*` ×6, `[[Theses/285A - SK Hynix (KOSPI).md]]` wrong company in LRCX, legacy `[[Macro/…]]` ×3, etc.) | lint #3, hand-verified | Batch link-fix pass |
| P0.9 | `_catalyst.md` 47 days stale (window ended Jun 6; says 65 theses vs 76) | mtime | Re-run `/catalyst` after P0.1–P0.5 |
| P0.10 | Cosmetic/janitorial: empty `.locks/` dir (dead convention — only referenced by Web UI Build Brief), `Presentation.pptx` + personal bank PDF sitting in `_Inbox/`, `.gitignore` comment says "Finnhub" (it's FMP) | — | rmdir; remove/relocate inbox items |

---

## P1 — Systemic spec bugs (cross-skill; fix once at the contract, inherits everywhere)

### P1.1 `Macro/` hardcode — the vault's macro layer is invisible to ~7 skills [BLOCKER]
Folder is `Macro & Technology/`; specs written against `Macro/`:
- `sync/SKILL.md:67` (change detection — `find` errors), `:98` (Step 1.2.5 target map), `:115` (Step 1.3 fallback grep), `:681` (snapshot cp) → **macro-side /sync is structurally dead**; only the stale graph reverse-index path survives
- `retro/SKILL.md:86,94` → macro activity bucket always empty
- `prune/SKILL.md:115,395` → unsynced-count undercounts; Stage 4.2c macro scan always empty
- `archive-callouts/SKILL.md:67` → macro callouts never swept (CXL note has callouts)
- `rollback/SKILL.md:637` → closure-cascade neighbor scan misses macro premise citations
- `rename/SKILL.md:122,140,180,468` → Step 3.5 pre-flight reachability probe omits macro files
- `_shared/wikilink-forms.md:29` → FOLDER enumeration wrong
- Correct in: catalyst:128, transcript:517. 37 theses use `[[Macro & Technology/…]]` links; only 3 carry legacy broken `[[Macro/…]]`.

### P1.2 Lock contract fails under the real shell (zsh) [HIGH]
- `preflight.md:100,146,200,215` — `[ "$EX_TIMEOUT" \> "$NOW" ]` errors in zsh → **live locks always classified STALE**; the guard invites stealing an active lock. Fix: `[[ … > … ]]`.
- 1.3c multi-ticker stale branch exits without releasing `$ACQUIRED` → partial-lock leak (proven: /compare 3-ticker collision leaves 2 locks).
- Check-then-write TOCTOU (no noclobber); read-only lock "multi-reader" promise has no acquisition snippet and can't work with one token-owned file; §1.7 release snippet is unconditional `rm -f` while consumers use the safer ownership-verified release (contract lags consumers).
- Early-abort paths (e.g. /status unknown ticker) never release the lock — unspecified.

### P1.3 `allowed-tools` frontmatter is nonstandard and under-scoped in ~9 skills [MEDIUM]
`Bash(date * find * …)` single-specifier form matches nothing; and even read as intended, the lists omit commands the skills' own snippets require (lock blocks need cat/grep/sed/rm everywhere; ingest Mode C needs sort/comm/rm; scenario allows only `date`/`defuddle` yet must run the full lock protocol inline). Effect: permission prompts or hard blocks mid-skill in non-interactive runs. Affected: sync, ingest, transcript, numbers, thesis, stress-test, deepen, brief, scenario, retro.

### P1.4 lint.py false-positive factories bury the real signal [HIGH]
~70% of the current 325-finding report is noise:
- **#23 structurally broken** (225 FPs live; 253 against a *freshly generated* graph): compares Reverse Index vs adjacency as if transposes — they are different relations by construction (`generate_graph.py:114` vs `:64`).
- **#26** counts adjacency-only wikilinks vs frontmatter `edges:` that includes reverse indexes → permanent ~15% "drift".
- No `\|` un-escape in `WIKILINK_RE` → 14 false #3 broken-links + 1 false #1 orphan (generator handles it; lint doesn't).
- List-valued `ticker: [AMD, NVDA]` stringified → false #32 + ~30 suspect #8 lines.
- UTC date math → all age arithmetic off-by-one for this user.
Suggested replacement: one "graph dry-run diff" check calling the generator's `build_body()` instead of six re-implementations (#19–#24/#26).

### P1.5 /lint check-ID citations are wrong across the doc layer [DOC-DRIFT, but misdirects Tier-1 instructions]
Ground truth from lint.py: #44 scenario-reversal, #45 compare-manifest, #46 registry, #47 stress-manifest, #48 status-manifest, #49 thesis-manifest, **#50m** deepen-manifest (undocumented ID), #50–#53 callout hygiene, #54/#55 graph-primer, #56 deprecated `[[preserve]]`. Wrong citations: **CLAUDE.md:210** ("#44–#48" for callout checks), INFRASTRUCTURE §10 (#50 collision row, "#1–#55" range, preserve folded into #50–53), `archive-callouts/SKILL.md:105,406` (#48 → should be #56; phantom #53b/#53d), `deepen/SKILL.md:369` (#50 → #50m), `graph/SKILL.md:87` (#38 doesn't read `graph_mode:`), INFRA:392 (#41 `phase:` field doesn't exist in sync manifests).

### P1.6 Mental Models mandate is not operationalized in any skill that owes it [HIGH — this is the vault's stated edge]
`grep -ci 'mental model'`: **thesis 0**, stress-test 0, compare 0, brief 0, surface 0, retro 0, scenario 0, prune 0; deepen 3 (references contract but no reading gate); sync gates only at section-write time (Step 3b/4b), not at implication-generation (Step 2). `/thesis` also omits `## Mental Models` from its required-section list ("all 13, in order" vs the template's 15) — the next new thesis will be template-drifted and permanently un-populatable by /sync's merge (section probe skips absent headings). All 76 existing theses have populated sections (backfill worked); only *new* theses drift. The mandate currently survives on ambient CLAUDE.md context alone — which does not reach delegated subagents (/surface, /retro, /prune).

### P1.7 Log-prefix registry vs the wild [MEDIUM]
- `Transcript ingested:` — produced by a real skill, zero registry entry.
- `Numbers refresh:` (§18) missing from **sync Step 3e drift-exclusion** (SKILL:522–528) and **retro's skill-origin list** (retro:154) → consumes drift-window slots and pollutes retro's "manual = highest signal" triage.
- Manual entry `Status change: portfolio-wide realignment…` (2802) line-prefix-matches §7 → misclassified skill-origin → propagation silently skipped for a genuine manual realignment.
- Unregistered wild prefixes: `Wikilink cleanup:`, `Sector re-scoped:`, `Template restructure:`, `Sell-off analysis:`, `Retro insight:` (deliberate but unregistered), ~15 legacy bracketed forms.
- Deepened-exclusion window: registry says 7 days, sync SKILL says 14.

### P1.8 Stale scale constants everywhere [LOW]
Specs still assume the ~42-thesis vault: retro "~126 WebSearches" (now 228 worst-case at 1q), catalyst "65+6 reads" (now 76+8) with a 5-min lock timeout vs its own 5–30-min progress contract, surface/scenario/prune read budgets understated 40–80%. INFRA §13.11 math stale.

---

## P2 — Per-skill findings (severity-ordered within skill)

### /sync (further to P1.1)
- **Step 3a section-slice awk returns zero body content** (`/^## X/,/^## /` self-terminates — proven on macOS awk). T7.5 scoped reads and `/sync all` Low-delta slices analyze empty sections. Fix exists in-repo: `_shared/extract_sections.py` (only /surface migrated).
- **Step 1.7 Log-confirmation awk doubly broken** (reversed match `ENVIRON[…] ~ $0`; env var never exported) → wikilink_match_set always empty → duplicate Log propagation for Case 2a notes. The prose grep alternative at :170 is correct — make it primary.
- Step 2.5 trusts stale graph `log_tail` with no staleness guard (fallback fires only when *missing*): 8 theses currently misclassifiable. Guard: thesis mtime > `last_graph_write:` → bash extractor.
- Idempotency keys verified working (3/3 real notes, all 5 wikilink forms) — via the grep path only.
- User Guide:18 says `/sync TICKER` blocks without graph; SKILL says ticker mode has no graph dependency. Contradiction.

### /ingest + verify_note.py
- **Gate deletes good notes**: #13 Jaccard keeps the query string (real NVDA earnings note + correct FMP URL → 22% < 50% → BLOCK/delete); #12 `\b[Il]{2,}\b` matches Roman numerals (14 existing notes would trip); #12 decimal-drop regex can't catch the spec's own `$1 5B` example.
- Batch mode silently ignores unsupported extensions (`Presentation.pptx` in no bucket, ever) — add UNSUPPORTED reporting.
- No relevance gate: the personal bank PDF enters TO PROCESS; typed `data`/`web-clip` it passes every check. Add explicit Step 1 out-of-scope abort.
- Same-source dedup solid (same-day hard-block, cross-day prompt verified in spec); topic-level near-dupes (two EDA primers) invisible by design → double-propagation via /sync.

### /transcript + extract_transcript_signals.py
- **BLOCKER: Q&A split fires on operator boilerplate** ("…there will be a question and answer session" at ~char 280) → prepared-remarks = 51 words → hedging/specificity deltas −100% with confident flags. Only ~9/23 cached transcripts split plausibly. Fix: ignore markers in first ~15% + gate flags on `prepared_word_count > 500`.
- Foreign-ticker catch-22: `/transcript 000660` passes thesis probe but FMP needs `000660.KS`; `.KS` form fails the probe. No spec line says FMP symbol = frontmatter `ticker:` (and Murata/GAW frontmatter lack suffixes). Same issue class for /numbers.
- Evasiveness metric pairs *every* adjacent turn (op hand-offs, mgmt→mgmt) → 86.7% "evasive", no signal.
- Cache poisoning: `curl -sf | tee` writes empty cache on failure; prior-quarter failures poison permanently. Write-temp-then-mv.
- Step 7.5 word floors cite the old flat curve; the vault's own exemplar transcript note fails even the new curve (2,270w < 2,941w floor) — transcript notes are delta-analyses, not compressions; exempt or re-floor.

### /numbers + numbers_compute.py
- Forward P/E takes `est.json[0]` regardless of ordering (proven wrong-year pick) → silently wrong multiple written to theses. Select earliest FY > today.
- `fcf margin` fallback divides total FCF by revenue *per share* — units garbage; drop it.
- Field-map coverage 27% (345/1,283 rows; 3/76 theses fully mapped); near-canonical variants missed (`net debt/ebitda` spacing, `fwd p/e`); forward-period multiples silently stale forever — add `skipped-forward` status.
- Step 4 writes flat `/tmp/numbers_${TICKER}_*.json`; script requires `/tmp/numbers_${TICKER}/*.json`; Step 12 cleanup removes neither.

### /graph + generate_graph.py
- Generator solid (markers consumed correctly, idempotent `last`, self-validation, unicode/numeric/@ handled). Residuals: non-UTF-8 file crashes run (no `errors=`); `status:` matched anywhere in body, not just frontmatter; `/graph bogus` silently accepted and stamped as `graph_mode: bogus`.

### /status
- Batch-ID format fork: line 166 says ticker-qualified (C4 fix) but all executable templates (172, 177, 249, 329, 499 + rollback:236) use the unqualified pre-C4 form.
- Cross-block `$HHMMSS`/`$TICKER`/registry-var reliance contradicts preflight's own statelessness rule → empty-suffix snapshots, blank registry rows when followed verbatim by Sonnet. Convert to paste-value convention.
- Conviction-trigger conflict check under-specified for a mechanical model; 38/76 theses have no `## Conviction Triggers` section and behavior is undefined; no escaping rule for `|` in closure rationale.

### /rollback
- List mode surfaces 29 manifests as restorable candidates (no `_*-manifest` filter at :40); 6 legacy snapshots have no snapshot frontmatter (`/rollback VRT` prefix-matches the broken one first) — define a failure path for unparseable snapshots.
- 6.2b invalidation-clearing `grep -Fxv && mv` fails on the last matching entry (grep exit 1) and orphans `.tmp.new` — the single-neighbor common case always hits it.
- 6.2a registry-removal count includes frontmatter lines → dead code.
- `cp … & wait` can't detect snapshot failure (wait exits 0) — same bug in archive-callouts 4.2 and compare 5.5a; spec demands abort-on-failure in all three.

### /rename
- SKILL's 7-pattern table ≠ RATIONALE's (archive variants missing from the table); real vault contains `[[Theses/SOI - Soitec.md#Outstanding Questions]]` (.md+anchor) matching none of the 7 → silent link break on rename. Regex-metachar tickers verified fine.

### /archive-callouts
- **Numeric tickers misroute**: `2383` parses as a *2383-day vault-wide EXECUTE*; `285A` degrades to vault-wide dry-run. 10 real theses affected. Ticker detection should be thesis-glob-based.
- Phase 4.4 verification probe uses BRE `{4}` → always 0 → false verification pass (plus `|| echo 0` double-print).
- 5.3 release hardcodes `.vault-lock` → scoped runs strand their ticker lock every time.
- Current sweep state healthy: 0 candidates until ~2026-10-22; all 26 Legacy sections and anchors verified safe; 3 nonconforming (pinned) headers tolerated by luck.

### /thesis
- All four archive-collision signals miss the only real archived thesis (`_Archive/Theses/` subdir never scanned; list-valued `ticker: [KLAC, AMAT, …]` unmatchable; registry nonexistent; snapshot trail cleaned) — `/thesis KLAC` would silently duplicate archived analysis. Signals need recursive glob + list-form ticker matching.
- No Step 7; no final report/lock-release block; "13 sections" vs template's 15 (Mental Models + Legacy Callouts missing — see P1.6).

### /compare
- Single-ticker mode adds competitors *after* locking only the supplied ticker — added tickers get Log appends with no lock, no rename-marker check.
- Manifest batch (unslugged) vs sector snapshot batch (sector-slugged) — `/rollback compare-…` prefix lookup matches zero snapshots.
- 5.5a "check exit status of all background jobs" after bare `wait` — impossible as written (see /rollback).
- 5.5c failure branch says "Continue to 5.5 Sector edits" — they already ran.

### /stress-test
- Contract-clean (propagated_to lifecycle, manifest, conviction-neutrality all verified against 8 real notes). Gap: CLAUDE.md's callout-handling contract (read fresh `[!error]` as identified weakness; don't read Legacy) absent from the SKILL — survives only on ambient context.

### /brief
- Read-only-lock justification races `_hot.md` (Phase 4 writes it); diverges from preflight's ticker-lock assignment. Prior-brief warning + callout exclusion verified correct; `:39` still names deprecated "preserved" state.

### /surface, /retro, /prune (delegation cluster)
- Delegated prompt = "this skill's full instructions" **including the delegation mandate itself** → recursion invitation; no "you are the executor, do not re-delegate" line. /surface's Scope Resolution (lines 31–93) has no assigned owner (main vs subagent). /prune's block never specifies prompt content at all → paraphrase loses the rubric.
- **/prune PREFLIGHT-BLOCKED dead end**: user approves "proceed anyway" → no re-invocation contract, no override flag → fresh subagent re-blocks on the same condition. Fires today with certainty (Phase 0.B: 132 files unsynced).
- /prune's `.vault-lock.readonly` has no acquisition snippet in preflight and a 2-min taxonomy timeout vs a 76-thesis read; /retro absent from lock taxonomies entirely.
- /surface sector-scope: case-sensitive graph-index keys (incl. `@`), no sector-resolution routing, no no-match behavior; live proof of improvisation: existing scan note with `scope: sector:Semiconductors` (no such key). Draft-invisibility caveat's mechanism claim is wrong (graph index *does* contain drafts; they're invisible only via graph staleness).
- /scenario reverse: R2.1 archive glob misses `_Archive/Theses/`; fully-live reversals write **no** `## Reversal Notes` at all (loop only over archive-skipped set) and `propagated_to:` keeps all tickers. `allowed-tools` can't execute its own lock protocol (inline skill, no delegation escape).
- /catalyst: no rename-marker pre-flight (only vault-wide writer without it); 5-min lock vs 9-min observed runtime → mid-run "stale" lock; live `_catalyst.md` format is *better* than the spec's Phase 4 schema — pick a winner explicitly before regenerating.
- /retro scoring gaps: `neutral`-news large moves (beat + guidance-cut) zero out of Trade Ideas; unreactive 2.0 fixed weight can never cross the 3.0 cluster threshold — cluster-level unreactive signal unreachable by construction. Phantom refs: log-prefixes "§47", catalyst "§148".

### /clean
- Simulated on real inventory (66 files): 0 deletable at 180d, 0 orphans, floors consistent with /prune. Gaps: 7 artifacts permanently invisible to its decision logic (no `snapshot_date:` → skipped forever, incl. the misnamed VRT snapshot and a 23MB tar.gz no skill can ever age out); in-progress *sync* manifests never reported (report category exists only for prune manifests); `--include-orphans` with no day count leaves an empty token.

---

## P3 — Documentation drift ledger (single pass fixes all)

1. "19 skills" → 21: INFRA:71, :413; §0.4 table + §12.6 Sonnet list + CLAUDE.md Rule 10 lock enumeration need `/numbers` (sonnet, ticker lock, only non-max-effort skill) and `/transcript` (opus, ticker lock, ART+OQ hot writes) rows.
2. User Guide §5 has no `/numbers` or `/transcript` entries; §14 matrix omits both; §7 earnings recipe should route to `/transcript`; §5 ingest blurb says "<150 words" (now scaling floor, min 300).
3. `[[_Archive/Docs/Changelog.md]]` referenced ×3 (UG:1114, 1151; INFRA:513) — did not exist until this audit created the folder; either create the Changelog or repoint.
4. hot-md-contract says "11 skills" vs its own list of 14; INFRA §12.2 "six contracts" omits mental-models-section.md (a 7th) and extract_sections.py; §12.3 RATIONALE count says 10, disk has 14.
5. INFRA §0.4 `/thesis` hot-writes row says "ART + OQ" but Step 6 also writes RCC; CLAUDE.md preflight enumeration omits default `/sync` from vault-wide list.
6. `.locks/` dead convention (Web UI Build Brief only) — delete dir or align the UI spec.
7. Archive-location convention: spec says closures land at `_Archive/` root; reality is `_Archive/Theses/` with `status: archived` (outside the taxonomy). Pick one and align /status:398, /thesis signals, /rollback 6.2, /scenario R2.1.
8. Lint-ID corrections per P1.5.

---

## Analytical quality — top improvements (vault-purpose-weighted)

1. **Operationalize the Mental Models gate** (P1.6): one standard block ("read `[[Generalist - Overview]]` + in-scope industry/lens files; record fired triggers as hypotheses") added to thesis/stress-test/compare/surface/retro/scenario/prune — and inside the *delegated prompts*, since subagents never see CLAUDE.md's mandate.
2. **/thesis: conviction after the bear case, not before** — frontmatter `conviction:` is currently written before Bear Case/Risks are drafted; require a one-line "why it survives the bear case" (READING PROTOCOL: agreement → disconfirm).
3. **/ingest: consensus-contrast requirement** — Thesis Delta must contain one "consensus assumes X → source implies Y" line; Contradiction Check must name a specific thesis section (verify_note can regex for it). Converts the gate from "sections exist" to "non-consensus work happened".
4. **/sync Step 4b: cross-thesis contradiction sweep** — "for each other Active Thesis in this sector, name one assumption this research validates or contradicts; update `## Investor heuristics` if the priced-in read shifted." Propagation is currently structurally bull-additive.
5. **Close the Conviction Triggers dead end** — 38/76 theses lack the section; /deepen refuses to create sections and /stress-test's handoff points at it. Whitelist template-mandated sections for explicit-name /deepen creation.
6. **/retro scoring**: score `neutral`-news large moves at 0.5×|move| instead of zeroing; revisit the unreactive fixed 2.0 vs 3.0 cluster threshold.
7. **/stress-test**: make Phase 2.5 external evidence mandatory-unless-waived for high-conviction theses (internal-only runs recycle the vault's own confirmation set); consume the thesis's `## Mental Models` fired-trigger list as disconfirmation targets.
8. **/surface**: require each opportunity to cite ≥2 cross-note datapoints + one falsifier; the "optically insignificant datapoints" the vault hunts live in the sections default mode skips.

---

## Verified-working (no action)

Manifest skeleton→populate→flip across all producers · propagated_to atomicity (/stress-test 8/8 notes correct) · /sync idempotency keys (3/3, all 5 wikilink forms) · /ingest dedup paths · graph generator marker consumption + idempotence + self-validation · lint #35 catches the hot-md schema break in both modes · /clean floors vs /prune retention · callout Legacy-section anchors safe vault-wide (26/26) · preflight zsh NULL_GLOB handling · name sanitization · numeric/hyphenated ticker globs & locks · FMP key present; both API skills abort gracefully without it.

## Suggested remediation sequence

1. **P0 vault-state fixes** (30 min, no spec edits): P0.1–P0.10.
2. **One-line class fixes with system-wide yield**: `Macro/` → `Macro & Technology/` (P1.1); zsh lock comparison + 1.3c leak + noclobber (P1.2); lint.py three FP factories (P1.4).
3. **Script gate hardening before trusting deletion/writes**: verify_note #12/#13, transcript Q&A split, numbers est-row selection + fcf fallback.
4. **State-machine consistency passes**: /status batch-ID + paste-value convention; /archive-callouts ticker parse + probes + lock release; /rollback list filter + 6.2b; /compare wait/batch/single-ticker-lock.
5. **Contract/doc single pass**: P1.5 lint IDs, P1.7 registry, P3 ledger.
6. **Analytical upgrades** (quality items 1–8) — highest long-run value, zero urgency.
