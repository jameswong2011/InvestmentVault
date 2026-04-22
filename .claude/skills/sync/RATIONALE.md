---
type: skill-rationale
skill: /sync
purpose: Design rationale and edge-case documentation for /sync. NOT loaded by the skill at invocation — SKILL.md references specific sections here by anchor. Readers/maintainers consult this file; the runtime skill does not.
last_reviewed: 2026-04-20
---

# /sync Design Rationale

> This file documents **why** /sync's rules are shaped the way they are. SKILL.md contains only the operational rules and references this document for justification. This separation keeps SKILL.md's loaded prompt size bounded while preserving the maintenance-critical reasoning.

---

## §1 Idempotency & dedup design

### §1.1 Why research-note-path keying, not today-date keying

The prior spec (6.11 and earlier) keyed idempotency on `entry_date == today`. That produced a cross-midnight duplicate:
- `/sync` at 23:59 on day D writes entry dated `### [D]`.
- Re-run at 00:01 on day D+1 sees today = D+1, finds only `### [D]` in the Log → mismatch → writes a duplicate entry `### [D+1]` referencing the same research note.

Research-note-path keying (wikilink presence anywhere in the Log) eliminates this: once a research note has propagated to a thesis, it is terminal — the thesis's Log is a permanent audit of which research notes have informed it. This also matches the semantic meaning of CLAUDE.md Tier 2 append-only: research notes are immutable source records; after initial propagation, subsequent runs on the same note produce no new signal.

### §1.2 Cross-midnight edge case — handled

`/scenario` wrote `### 2026-04-18` at 23:58 citing `[[Research/X]]`. `/sync` at 00:02 on 2026-04-19 scans the thesis's Log, finds the day-D entry wikilinking `[[Research/X]]`, and skips propagation. Correct — the research already propagated; the day boundary is irrelevant.

Same for producer runs that straddle midnight (started at 23:58, completed at 00:02 next day): the wikilink-presence check ignores dates entirely.

### §1.3 User-intent edge case — re-propagation

If the user edits a research note's body later and wants to re-propagate, the contract is: create a NEW research note OR append a thesis Log entry directly (CLAUDE.md Tier 2 "research notes are immutable source records"). `/sync` does not re-propagate a research note that has already reached a thesis, regardless of when or how the research note changed.

### §1.4 Why secondary identity keys matter (H4)

The primary wikilink-based idempotency breaks if a research note is renamed (e.g., user fixes a typo in the filename slug). The old wikilink in thesis Logs doesn't match the new filename, so `/sync` would re-propagate as if it were a new research note — producing duplicate Log entries.

Secondary keys preserve idempotency across legitimate user-driven file moves/renames by keying on stable identity properties:
- **Source URL** — if research note has a URL in `source:` frontmatter, match Log entries whose cited research notes share the same URL (requires a cross-read of candidate research notes' frontmatter).
- **`date: + ticker:` tuple** — for vault-synthesis notes without URLs (`/scenario`, `/stress-test`, `/compare` outputs).
- **`tags:` intersection + date match** — weakest key, used when URL and tuple both miss.

Secondary keys only fire when primary key misses. For typical `/sync` runs, the primary key catches all legitimate dedup cases; secondary keys are the exception path.

### §1.5 Why the unified Log-scan (T7.1) replaces separate Check 2a and Check 3

The prior design had two distinct Log scans:
- **Check 2a (Log-history backfill)** when `propagated_to:` frontmatter was absent — searches Log for prior wikilink references to this research note.
- **Check 3 (primary-key idempotency)** — searches Log for prior wikilink references to this research note.

Both scans did the same work against the same data. The T7.1 consolidation runs ONE vault-wide `Grep` per research note across `Theses/*.md` (using the five wikilink forms from `_shared/wikilink-forms.md`). The result set is used for both:
- Case 2a backfill-update decision (frontmatter union update after successful propagation).
- Case 2b augmented-target evaluation (tickers in wikilink set but not in producer's `propagated_to:`).
- Check 3 primary-key skip (tickers in wikilink set are already propagated).

Secondary-key evaluation only fires for candidates NOT matched by the grep — typically zero or one ticker per research note. Tool-call count drops from O(N_candidates) Read per research note to O(1) Grep per research note.

### §1.6 Why empty `propagated_to: []` is terminal, not "nothing yet propagated"

A producer that wanted "propagate to all wikilink-resolved targets but I haven't done any myself" would simply omit the field (Case 2a). Setting `propagated_to: []` explicitly is a deliberate "this note's body wikilinks are contextual references, not propagation targets" signal.

Required for `/surface` (whose scan notes wikilink 10+ theses for context) and `/brief` (derivative summary of an already-existing thesis). Without this case, `/sync` would Log-spam every wikilink-referenced thesis on every surface/brief.

### §1.7 Why strict calendar-day matching for sector/macro idempotency

Step 4.0 and Step 5.0 idempotency (same-day double-sync guard for sector/macro analytical edits) uses `entry_date == today` as `YYYY-MM-DD` strings. Cross-midnight runs are accepted as "slight redundancy; never data loss."

Different from research-note keying (§1.1) because sector/macro edits are analytical text rewrites, not source-record propagation. A same-day double-edit can produce contradictory text layered on top; preventing that requires date matching. A cross-day legitimate re-edit (user wants fresh propagation) is rare and the cost of re-propagation is a one-edit overwrite, not a duplicate audit-trail entry.

### §1.8 Why "Related Research" presence alone isn't sufficient for sector idempotency

A research note may be added to `Related Research` listing without a corresponding analytical-section update (e.g., the user manually wikilinked it). The Log entry is the authoritative record that `/sync` (or another producer) actually propagated insight content. Checking both gates the edit on actual prior propagation, not just incidental wikilink presence.

### §1.9 Why mtime-fallback for macros but not sectors

Sector notes are required by template to have `## Log` sections (per /lint sector template enforcement). Macro notes are narrative documents with variable structure — many have no Log section. The mtime fallback gives macros a same-day double-edit guard without requiring a Log section.

### §1.10 Step 5.0 mtime fallback — false-positive risk

The macro mtime fallback can mistakenly skip when the user manually edited the macro (advancing mtime) AND the source wikilink happens to already be present (added by a prior /sync). Trade-off: mtime is a coarse signal for Log-less macros, but the alternative (no idempotency check at all) leaves macros vulnerable to compounded analytical-text edits across same-day double-syncs. To force re-propagation on a Log-less macro that was incorrectly skipped, run `/sync all` or manually edit the macro to remove the source wikilink before re-running /sync.

### §1.11 Why Step 1.2.5 exists — the 2026-04-22 CRWD sector-propagation failure

**Symptom**: `/sync` at batch `sync-2026-04-22-144403` ran immediately after `/thesis crwd` + `/status CRWD active`. Changed-file set included the CRWD-vs-PANW comparison research note (`sector: Cybersecurity` in frontmatter, `[[Sectors/Cybersecurity]]` in body). Run reported "no-op propagation." Sector note was NOT updated despite the CRWD thesis carrying three sector-level insights (architectural-purity-cannot-be-acquired, Falcon Flex consumption-pricing vs PANW platformization-tax, mega-deal vs tuck-in integration-risk asymmetry) absent from the sector note's Key Dynamics.

**Root cause — chained failure of three factors**:

1. **Skill content was truncated in the initial context.** The system-reminder delivered Steps 0 through 2.9 of SKILL.md inline and then marked `[... skill content truncated for compaction ...]`. Step 4.-1 (the sector skill-origin gate) was NOT visible during execution. The LLM filled in Step 4 behavior from memory and general reasoning rather than explicit rules. This is the proximate cause. CLAUDE.md Operational Rule #11 (added 2026-04-22) requires Reading the full SKILL.md before any write phase when truncation is detected.

2. **Step 2's source-dedup clause was over-applied.** Original wording: "analyse the research notes as primary sources. The thesis's Log entries citing those research notes contain no additional propagatable information." The LLM extrapolated "no additional propagatable information" from analysis-scope (don't re-read the thesis Log) to propagation-scope (don't fire Step 4/5). The new wording scopes the rule explicitly to analysis and adds the "Common mis-application" warning citing this failure.

3. **Sector targets were resolved only lazily inside Step 4.-1's gate.** Steps 1.2/1.3/1.4 have explicit thesis-target resolution, but research-note → sector targets were computed implicitly as part of gate condition (ii). Once the LLM concluded "thesis targets are all idempotent (Step 1.7)", the mental model was "nothing upstream to propagate → skip Step 4 entirely" — Step 4.-1's gate was never reached. Step 1.2.5 makes these targets first-class at Step 1 time, so the gate's inputs are pre-computed and the gate cannot be bypassed by cognitive shortcut.

**Why the fix is three layers**: any one of the three factors alone could have caught the bug (full skill visible → Step 4.-1 seen; tighter source-dedup wording → no extrapolation; explicit Step 1.2.5 → target map exists regardless). Defense-in-depth reduces probability-weighted recurrence to negligible.

**Verification**: a `/sync` run after these patches on a research note with `sector:` frontmatter but fully-idempotent thesis targets must produce a non-empty `sector_targets_per_research_note` entry at Step 1.2.5, fail Step 4.-1 condition (ii), and proceed to Step 4.0. The sector note should either pick up analytical deltas or emit the Step 4.0 per-source idempotency skip. Silent no-op is the failure signature.

---

## §2 Propagation-target resolution

### §2.1 Why the macro body-grep fallback is necessary

The reverse index is built from the macro note's outbound wikilinks (`[[Theses/...]]` in the macro body). If a thesis declares `[[Macro/X]]` but the macro doesn't reciprocate `[[Theses/TICKER]]`, the reverse index returns empty for that macro, and the thesis silently fails to receive propagation when the macro is edited.

The body-grep fallback closes this gap. `/lint #23` (reverse-index consistency) catches the asymmetry periodically; the fallback ensures correct propagation between lint runs.

### §2.2 Why file-direct fallback runs only on empty graph result (T7.2)

The prior spec ran file-direct fallback (ticker frontmatter + outbound wikilinks + tag match) UNCONDITIONALLY — even when graph-assisted resolution returned a non-empty target set. This doubled the per-research-note resolution work.

The graph's reverse index is kept consistent by `/graph`'s "always rebuild reverse indexes" rule (drift-prevention design). When `/graph last` has run since the vault was last modified, the graph is the authoritative dependency source and the fallback is redundant.

T7.2 makes the fallback conditional:
- Graph-assisted returns ≥1 target → skip fallback. Trust the graph.
- Graph-assisted returns empty for a given research note → run fallback (original safety-net behavior for notes not yet in graph, stale graph, or graph-missing scenarios).
- Graph file absent → fallback becomes the primary path, as before.

`/lint #23` still surfaces residual reverse-index drift; on fire, re-run `/graph` (full) and the next `/sync` benefits immediately.

### §2.3 Why include closed-status check as a Grep batch

Old spec: read each target thesis's frontmatter individually to check `status: closed`. For a `/sync all` with 20 targets, 20 Read calls just for a frontmatter field.

Single `Grep "^status: closed" Theses/ --glob='*.md' --output_mode=files_with_matches` returns the closed-status set vault-wide in one call. Intersect with target set in memory. Byte-identical outcome for the skip-list logic that follows.

---

## §3 Pass 1 lightweight scan (for /sync all)

### §3.1 Why "self-modified" must be its own High-delta trigger

Pass 2 triage uses four heuristics (referenced-by, shares-sector, cross-thesis-link, recent-Log) that all infer "this thesis was affected" from EXTERNAL signals. None of them fire when the user manually edited the thesis itself with no Log entry — but that edit is exactly the kind of vault change `/sync all` is supposed to propagate. Classifying a self-edited thesis as No-delta because no other file references it would silently drop the user's manual changes from propagation analysis.

### §3.2 Why the log_tail graph cache replaces lightweight scans (T7.3)

Pass 1 read "only frontmatter + Summary + last 3 Log entries" per thesis. In practice, `Read` returns the whole file (Read tool semantics), and selective section reads require bash extraction that LLMs inconsistently apply.

T7.3 moves the "last 3 Log entry prefixes + dates" AND `status:` into `_graph.md` (as `log_tail:` and `status:` per-thesis adjacency fields). `/graph` already reads each thesis during rebuild — capturing these fields is free within /graph. /sync then reads only `_graph.md` (already loaded for dependency resolution) for the Pass 1 triage inputs.

Falls back to bash-extracted section reads only if the graph is missing/stale or lacks `log_tail:` fields (pre-T7.3 graph files).

The Step 2.5 skill-origin classification also consumes `log_tail:` for prefix matching — same data, different consumer.

---

## §4 Skill-origin gate (Step 2.5)

### §4.1 Why the gate is safe

Step 4b's (sector) and Step 5b's (macro) analytical edits are derived from research-note content. Without a research note driving the edit, there is no propagatable delta — the LLM running 4b/5b would either rewrite the same text with cosmetic variation (analytical churn) or no-op.

The skill-origin gate makes the no-op decision explicit and cheap rather than leaving it to LLM inference. For changes whose only source is a `Status change:` Log entry or similar skill-origin marker, the originating skill already updated sector/macro state per its own spec — /sync need not re-edit.

### §4.2 Mixed-set rule

If the affected thesis set for a sector/macro contains at least one research-driven thesis, proceed normally — the research-driven thesis's propagatable delta applies to the whole sector section (value chain, competitive dynamics, etc.), and the skill-origin theses coincidentally sharing the sector do not suppress the propagation.

---

## §5 Manifest contract (Step 2.9 + Step 7.5)

### §5.1 Why this manifest exists

`/sync` Step 3c snapshots theses for Tier A edits (rewriting Bull Case, Non-consensus Insights, etc.) but explicitly **does NOT snapshot** for Tier B edits (Log-only appends, Related Research wikilink additions, Key Metrics number updates). Cross-thesis propagation — where a research note triggers a Log entry on TICKER's thesis AND on TICKER's cross-thesis neighbors — produces Tier B appends on neighbors WITHOUT snapshots.

If the user later runs `/rollback TICKER` to undo the sync, the cascade detection finds TICKER's pre-sync snapshot but **cannot find snapshots for the neighbors**. The neighbor Log entries persist after rollback as orphan audit-trail entries citing a research note whose effect on TICKER has been reverted. This is a permanent audit gap that violates Tier 2 append-only semantics if removed manually, and silently corrupts the Log audit trail if left in place.

The sync manifest closes this gap by recording **every thesis touched** in the sync run — including Tier B Log appends without snapshots. `/rollback` Step 2.5 reads the manifest during cascade detection and surfaces the unrecoverable Log entries to the user with their full text, so the user can decide per-entry whether to manually strikethrough/annotate them post-rollback.

### §5.2 Two-phase write (T2.1) — skeleton + flip

Prior behavior wrote the manifest at END of run with a "log failure but continue" clause that silently violated the cascade-recovery contract if the end-write failed. New two-phase behavior:
- Step 2.9 writes skeleton BEFORE any mutations — skeleton write failure hard-aborts the sync pre-mutation, preventing any silent audit gap.
- Steps 3–6 incrementally populate the manifest as work lands — crash recovery finds partial-but-consistent state.
- Step 7.5 flips status at end; flip failure is visible via `/lint #41` rather than silent.

### §5.3 Why phase-boundary checkpoints (T7.4) replace per-event appends

Prior design: one Edit per snapshot / Log append / sector / macro. On `/sync all` touching 20 theses + 5 sectors + 2 macros: ~49 Edit operations on the manifest alone.

T7.4 changes the flush granularity. In-memory accumulators (already defined in Step 7.5d) are flushed as one Edit per phase boundary:
- **End of Step 3** (all thesis snapshots + Log appends written) → one batch Edit populating "Theses with snapshots" + "Theses with Log-only appends" sections.
- **End of Step 4** (all sector updates written) → one Edit for "Sector notes touched".
- **End of Step 5** (all macro updates written) → one Edit for "Macro notes touched".
- **Step 3/4/5 entry** (first source research note processed) → append to "Source research notes processed".
- **Step 7.5 status flip** — unchanged.

Total: 4-5 Edit operations on the manifest instead of ~49.

#### §5.3.1 Crash-recovery implications

- **Crash during Step 3** (before the Step-3-end checkpoint): the manifest skeleton exists (`status: in-progress`), but has not yet captured any thesis details. `/rollback Step 2.5` sees the skeleton, warns the user that Tier B details are missing, and surfaces via `/lint #41`. Tier A snapshots on disk are still findable by filename pattern — `/rollback` cascade can operate from the snapshot filename set directly, falling back to manifest data when present. **Mitigation**: Step 3c/3f MAY optionally append to a `.sync-progress.jsonl` append-only scratch log for intra-phase crash granularity, read by `/rollback` when the manifest is missing Step-3-end data. (Optional in T7.4 — skip unless crash-in-flight proves common.)

- **Crash during Step 4** (after Step-3-end checkpoint, before Step-4-end): manifest has complete thesis records, no sector records. `/rollback` has full Tier A + Tier B coverage for theses; sector wikilink additions are unrecoverable orphans, but sector wikilink additions are explicitly marked Tier B "harmless" in the existing spec (§5.1) — the same treatment applies.

- **Crash during Step 5**: manifest has theses + sectors, no macros. Same reasoning as above.

The phase-boundary design accepts intra-phase granularity loss as the cost. `/rollback` still operates correctly; the degradation is that mid-phase crash theses/sectors/macros appear ONLY via snapshot-file glob, not via manifest listing. For the common case (no crash), the user sees a complete manifest; for the rare crash case, the user sees a degraded manifest plus the snapshot file set, sufficient for cascade-recovery.

### §5.4 Why a marker file (not poisoning `_graph.md date:`) for `.sync_all_fresh`

`/sync` must not write `_graph.md` — the metadata-cull architecture concentrates graph ownership in `/graph`. A vault-root marker file keeps `/sync` content-only while giving `/graph` an unambiguous signal. The marker is cheap (zero-byte file), ignorable by every other skill, and self-cleaning on the next `/graph` run.

---

## §6 Watermark semantics

### §6.1 Why `/sync TICKER` does not touch `.last_sync`

Ticker-scoped mode operates on a bounded subset (one thesis + its file-direct adjacency) and explicitly ignores the watermark for change detection. Advancing the watermark would silently mark unrelated changes (other theses, macros, sectors modified before this run) as "synced" when ticker-scoped mode never read them. The next default `/sync` would then miss those propagation paths because `find -newer .last_sync` skips them.

First-run exception: if `.last_sync` is absent when `/sync TICKER` runs, create the epoch placeholder (`touch -t 197001010000 .last_sync`) so subsequent default `/sync` runs have a baseline. Creating an epoch file is not the same as advancing it — the watermark stays maximally permissive so the next default `/sync` re-evaluates the full vault.

---

## §7 _hot.md auto-resolve (Step 6 #5b)

### §7.1 Why scoped to /catalyst pattern

Other Open Question producers (`/surface`, `/scenario`, `/stress-test`, `/thesis`) generate freeform questions whose resolution criteria aren't programmatically detectable. Only the `/catalyst`-specific pattern has a clear, parseable resolution condition (forward catalyst exists). Generic accumulation pressure on `_hot.md` Open Questions remains for those — manual cleanup is required.

---

## §8 Drift detection (Step 3e)

### §8.1 T1.3 tuning rationale

Prior behavior fired drift on 3/5 regardless of recent stress-test activity, producing false positives during the natural burst of `/stress-test` → `/deepen` → `/sync` cycles. The extended 14-day exclusion window for `Deepened` entries (up from 7) and the post-stress-test 4/5 threshold (up from 3/5 if `Stress test` entry within 30 days) together reduce false-positive fires without materially changing true-positive detection rate.

### §8.2 Why these prefixes are excluded from the drift window

Each excluded prefix represents an entry that is structurally a Log event but carries no conviction-deterioration signal for the subject thesis:
- **`Stress test`** — adversarial review, not deterioration evidence.
- **`Deepening`** — provisional stuck-state marker; no sentiment.
- **`Cross-thesis closure:`/`Cross-thesis closures:`** — notifications about a DIFFERENT thesis's closure.
- **`Scenario REVERSED`** — corrective entry withdrawing a prior scenario propagation.
- **`Renamed file:`** — cosmetic filename change record.

Counting any of these would either inflate drift or consume a drift-window slot without signal. See `_shared/log-prefixes.md` registry entries for exact producer/consumer linkage.

---

## §9 Tool-call efficiency principles (T7.*)

These optimisations landed together in the T7 series:
- **T7.1** — Unified Check 2a + Check 3 Log scan using shared wikilink-forms grep.
- **T7.2** — File-direct fallback conditional on empty graph result.
- **T7.3** — `log_tail:` + `status:` cached in `_graph.md`; Pass 1 and Step 2.5 consume graph data instead of re-reading theses.
- **T7.4** — Phase-boundary manifest checkpoints (4-5 Edits) replace per-event appends (~49 Edits).
- **T7.5** — Section-scoped Step 3a thesis reads driven by Step 3b impact map.
- **T7.6** — Batched macro body-grep fallback (one regex union across changed macro basenames).
- **T7.7** — Single-Grep closed-status check replaces per-thesis frontmatter reads.
- **T7.8** — Emit-if-non-empty Step 8 report template.

Combined expected saving on a typical `/sync all` run (20 High-delta theses, 5 sectors, 2 macros, 10 research notes): ~400-700K tokens per run, 50-60% reduction from pre-T7 baseline.

---

## §10 Pre-T7.3 graph fallback (transitional)

When `_graph.md` was upgraded with T7.3 cache fields (`status:` + `log_tail:`), any graph file written by an earlier build lacks those fields. SKILL.md's Pass 1 needs log-tail data to triage theses; without the cache it falls back to extracting per-thesis section data with a single batched Bash call.

**Operational rule in SKILL.md** (§1.10 Pass 1 "Pre-T7.3 fallback"): if `log_tail:` fields are absent from `_graph.md`, extract frontmatter + Summary + last 3 Log entries per thesis via a single batched Bash call; treat as a transient in-memory substitute for the cache.

**Full AWK implementation** (preserved here; never loaded at runtime once every `_graph.md` has been rebuilt at least once under T7.3):

```bash
# Frontmatter + Summary + last 3 Log entries per thesis
for f in Theses/*.md; do
  echo "=== $f ==="
  awk 'BEGIN{in_fm=0; fm_done=0}
       /^---$/ {if(!fm_done){in_fm=!in_fm; print; if(!in_fm) fm_done=1; next}}
       in_fm{print; next}
       /^## Summary/,/^## /{if($0!~/^## /||$0~/^## Summary/) print}
      ' "$f"
  # Last 3 Log entries
  awk '/^## Log/{in_log=1} in_log' "$f" | awk '
    /^### [0-9]{4}-/ {if(header_count>=3){exit} header_count++}
    {print}' | tail -40
done
```

One Bash call for all theses with `=== FILE ===` separators.

**When it re-fires**: only if `_graph.md` is restored from a pre-T7.3 backup, or if a future schema change removes `log_tail:` without migrating consumers. Otherwise dead code. Kept here for disaster recovery, not SKILL.md.
