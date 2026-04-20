---
type: skill-rationale
skill: /prune
purpose: Design rationale for /prune — batch atomicity, 30-day retention, downstream propagation boundary. NOT loaded at invocation.
last_reviewed: 2026-04-20
---

# /prune Design Rationale

> SKILL.md contains operational rules. This file explains the atomic batch pattern, the 30-day regret-recovery window (T5 5.2), the macro-note hands-off policy, and the Stage 4.2/4.5 downstream propagation split.

---

## §1 Atomic batch design

### §1.1 Why snapshot-everything-first

Stage 1 creates ALL safety snapshots before any Stage 2+ modification begins. If the skill fails mid-execution, every affected file has a snapshot — `/rollback` cascade detection finds them via matching `snapshot_batch` and restores atomically.

Interleaved per-thesis (snapshot → close → snapshot → close) would leave not-yet-processed theses without safety snapshots if the run aborted mid-batch.

### §1.2 Why five sequential stages

1. **Snapshot** (Stage 1) — safety net
2. **Close** (Stage 2) — thesis-only modifications
3. **Upgrade** (Stage 3) — thesis-only modifications
4. **Sector** (Stage 4) — multi-file, read after thesis work complete
5. **Downstream** (Stage 4.2/4.5) + **Graph/hot** (Stage 5) — cross-vault propagation last

Thesis edits first keeps sector notes consistent with original state until all thesis work is known-good. Sector edits after means mid-run failure leaves sector notes untouched + consistent; only theses + snapshots need cascade restore.

### §1.3 Abort gate semantics

Stage 1 snapshot failure → abort immediately. No destructive modifications yet, vault in original state. This is the ONLY clean-abort point — after Stage 2 begins, partial state requires cascade restore rather than simple re-run.

### §1.4 6-digit HHMMSS batch ID

Same rationale as /sync, /status, /rollback: second-precision prevents same-minute collisions across concurrent skill invocations. All Stage 1 snapshots share one `prune-YYYY-MM-DD-HHMMSS` batch ID for coupled cascade restore.

---

## §2 Stage 1.5 manifest contract

### §2.1 Why the manifest persists

The manifest is the discovery mechanism for partial prune operations. Session crash between Stages 2-5 leaves vault in mixed state (some closures done, sector notes partially updated, neighbor Logs partially annotated). Without the manifest, `/lint` would need deep cross-file heuristics to reconstruct the intended batch.

With the manifest: `_prune-manifest (prune-...)` with `status: in-progress` is an unambiguous "prune crashed here" signal. Recovery via `/rollback` uses it to identify every file that needs restoration.

### §2.2 Why the manifest includes Stage 4.2 targets

Stage 4.2 "Cross-thesis closure" Log appends on neighbor theses are Tier B (append-only) — they have NO per-neighbor snapshots. The manifest records them so `/rollback` Step 2.5c cascade can surface these entries for strikethrough review during regret-recovery.

Without the manifest's neighbor list, rolling back a prune closure would leave orphan audit-trail entries on neighbor theses citing an un-archived thesis.

---

## §3 30-day regret-recovery retention (T5 5.2)

### §3.1 Why 30 days

Matches typical investment-decision regret window:
- Quarterly earnings cycle
- Position sizing review
- Macro shock digestion

Beyond 30 days, Tier B cascade recovery has diminishing value — the user's vault has absorbed the closure; neighbor Logs are now read as historical context, not stale premise.

### §3.2 Why NOT delete manifest at Stage 5

Prior behavior (pre-T5 5.2) deleted the manifest at Stage 5 success. This closed the cascade-recovery window immediately — a user realizing a closure was wrong 3 days later had no tooling to surface Tier B neighbor Log entries for strikethrough.

New behavior: flip `status: in-progress` → `completed`, verify flip landed, leave manifest in place. `/clean` Step 2a extension removes aged completed manifests after the 30-day window.

### §3.3 Verify-only Stage 5 (flip + verify, no delete)

Post-T5 5.2 Stage 5 is verify-only. Flip-failure handling:
- On success → manifest stays, `/lint #36` Pass within 30 days, Nice to Have beyond
- On verification failure → do NOT attempt repair. Prune succeeded; only the completion marker missed. Manual fix required (user edits manifest frontmatter). `/lint #36` flagging as Critical is a false alarm in this specific case — the error message explicitly warns against `/rollback`.

### §3.4 Why verification failure is not self-repair

If the flip Edit silently missed, attempting a second Edit might:
- Succeed silently (now flipped) — no observable difference from success
- Fail the same way — wasted round trip
- Race with some concurrent writer — unlikely but possible

The safer design: report clearly, do not retry, surface via `/lint #36`, require manual intervention. `/rollback` would be destructive (undo valid prune work).

---

## §4 Stage 4.2 downstream propagation — why split from sector stage

### §4.1 Scope difference

Stage 4 (sector notes): structured, required edits — remove archived theses from Active Theses, update conviction displays. Every affected sector receives predictable Edit operations.

Stage 4.2 (neighbor theses + macro notes): content propagation across the vault — notification-only Log entries on neighbors, review-only reporting on macros. Different operation class; separating preserves Stage 4's clean structural-edit semantics.

### §4.2 Why neighbor Log entries are Tier B (no snapshots)

Log appends are append-only per CLAUDE.md Change Safety Rules. Snapshotting every affected neighbor would explode the batch size — a thesis closure with 20 cross-references would create 20 additional snapshots. The append operation is atomic Edit; if it fails, the thesis is unchanged (no partial state).

Failure handling: report failed appends individually, continue with remaining neighbors. User inspects post-run. `/rollback` cascade via manifest (§2.2) handles regret-recovery for the whole batch.

### §4.3 Why `[[_Archive/TICKER - Name]]` not `[[Theses/...]]` in cross-thesis closure Logs

The closed thesis actually lives at `_Archive/` after the move. Obsidian resolves `_Archive/` wikilinks natively — no broken-link indicator in the Backlinks pane. Using `[[Theses/...]]` would produce a broken-link display plus require the user to click into `_Archive/` manually to view.

### §4.4 Why macro notes are detect-and-report only

Macro notes are narrative documents with variable structure — not every macro has a `## Log` section. Body prose embeds thesis wikilinks in analytical sentences (e.g., "Iranian retaliation risk most directly affects [[Theses/LITE - Lumentum]]..."). Auto-editing such prose can destroy analytical coherence:
- If LITE was closed because its thesis is now wrong, but the macro sentence is about geopolitical transmission pathways, the sentence may still be informative as historical macro analysis.
- Inserting `~~strikethrough~~` or rewriting `[[Theses/...]]` → `[[_Archive/...]]` might read as "this macro assertion is invalid", which could be misleading.

User judgment required. `/prune` surfaces the occurrences; the user decides per-macro: (a) rewrite prose, (b) leave as historical context, (c) add annotation. No auto-edit.

### §4.5 Combined closures in single neighbor Log entry

If thesis NVDA cross-references three theses all closed in this run (TICKER1, TICKER2, TICKER3), the neighbor Log entry NAMES ALL THREE in one bullet:
```
- Cross-thesis closures: [[_Archive/TICKER1 - ...]], [[_Archive/TICKER2 - ...]], [[_Archive/TICKER3 - ...]] archived this run — ...
```

Rationale: max 2 lines per CLAUDE.md Writing Standards. One entry per neighbor regardless of how many closures affected it. Collapse rationales if the list runs long (`... and 2 more — see /prune output`).

---

## §5 Stage 4.5 graph invalidation — batched, not per-closure

### §5.1 Why write `.graph_invalidations` once per prune, not per-closure

Every closure stales some neighbors' `cross-thesis:` references. Writing `.graph_invalidations` per-closure would thrash the file during a large batch (20 closures × append-and-dedup = 20 file writes). Batched write (merge all closures' neighbor sets into one deduplicated union, write once) is cleaner and cheaper.

The file is processed and cleared by the first `/graph last` after this skill.

### §5.2 Graceful degradation on write failure

If `.graph_invalidations` write fails, the prune itself is complete — closures, upgrades, sector updates all succeeded. Graph invalidation is a downstream optimization signal, not a correctness requirement. User can recover with a full `/graph` rebuild (vs incremental `/graph last`).

Report the failure + recommend `/graph` (full) instead of `/graph last`.

### §5.3 Why Stage 4.5 runs only on closures

Upgrades don't archive thesis files. Neighbor `cross-thesis:` references remain valid pre-and-post upgrade — the target file still exists at the same path; only the conviction display differs. No graph invalidation needed.

Stage 4.5 skips entirely for upgrade-only prune runs.

---

## §6 Phase 1 two-pass triage

### §6.1 Why lightweight scan first

Reading all ~40 thesis notes in full would exceed context limits. Most flag criteria (conviction level, last Log date, research note count, catalyst presence) are assessable from frontmatter + a few sections, not the full body.

Pass 1 reads ~200-400 words per thesis (frontmatter + Related Research + Catalysts + Log). Pass 2 deep-reads only flagged candidates. Reduces full reads from ~40 files to 10-20.

### §6.2 Orphan-from-sector check deferred to Pass 2

All other flag criteria can be assessed from single-file reads. Orphan-from-sector requires cross-referencing each thesis against its Sector Note — a second lookup. Deferring to Pass 2 (where sector notes are already needed for Stage 4) amortizes that cost.

### §6.3 Pass 2 also covers high-conviction-with-stale-research

Flags that don't fit the binary pattern ("high conviction AND last research >90 days old") are evaluated in Pass 2 after the deeper context is available. A high-conviction thesis with stale research may be intentionally in a quiet monitoring phase; Pass 2's full-read lets Phase 2's "Evidence trajectory" analysis decide.

---

## §7 Phase 0 unsynced-research warning

Running `/prune` before `/sync` risks archiving theses before recent research insights propagate. The Phase 0 warning surfaces this — `⚠️ Unsynced research detected. [N] files modified since last /sync. Proceed anyway? (y/n)`.

User-confirmation gate; not a hard block. Some users intentionally prune based on stale research (e.g., closing a thesis where fresh research strengthens a new non-consensus angle they're developing separately).

---

## §8 Rename-marker hard block (Phase 0.0.2)

### §8.1 Why all-or-nothing

The Phase 0.0.2 check is all-or-nothing — a prune batch cannot safely skip individual tickers based on markers because the manifest integrity depends on a closed set of affected files decided at Stage 1. Partial skips would produce misleading manifest content.

### §8.2 Why vault-wide marker check, not per-thesis

Even if the tickers affected by this prune don't include mid-rename tickers, Stage 4.2 scans ALL thesis files for cross-references. A mid-rename thesis could appear in Stage 4.2's neighbor set via its old-name wikilink still present in another thesis — Stage 4.2 would write the closure-notification Log entry using the old name, splitting state.

All-or-nothing block is safer than trying to filter.

---

## §9 Report structure

Phase 4 "Portfolio Health Summary" precedes Phase 5 execution. The table + stats + attention-allocation insight give the user full context before requesting execution approval:
- Recommendation table: per-ticker decisions with rationale
- Portfolio stats: aggregate health
- Attention allocation: meta-reflection on where to invest research time

The attention-allocation section answers "given all this, what should I focus on?" — a step most portfolio-pruning tools omit, leaving the user with a clean list but no prioritization signal.
