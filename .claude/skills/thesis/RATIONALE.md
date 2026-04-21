---
type: skill-rationale
skill: /thesis
purpose: Design rationale for /thesis — multi-signal archive-collision detection, new-sector handling, manifest contract, orphan research integration.
last_reviewed: 2026-04-21
---

# /thesis Design Rationale

> SKILL.md contains operational rules. This file explains why duplicate detection requires four independent signals, why Step 5 branches instead of silently skipping on sector resolution miss, why Step 3.5's manifest is a skeleton-first write, and why orphan research integration advances mtime.

---

## §1 Active-thesis check — prefix glob, NOT content grep

### §1.1 Why prefix glob

Short tickers (e.g., `A` for Agilent, `T` for AT&T, `U` for Unity) match too many filenames under content grep — producing false-positive duplicate warnings that block legitimate thesis creation. A grep for `"A"` as a ticker would match every file containing the letter A anywhere.

Prefix glob `Theses/TICKER - *.md` is ticker-exact: the ` - ` separator plus the `.md` suffix anchor the match. No false positives.

### §1.2 When to use content grep instead

Research context grep (Step 1.3) IS content grep, but informational only — surfaces relevant existing research for the new thesis to link to. Does NOT block creation. Prefers frontmatter `ticker: TICKER` match and `tags:` containing the ticker as whole-word over body-text mentions, to filter short-ticker false positives out of the context set.

---

## §2 Multi-signal archive-collision detection (Step 1.2)

### §2.1 Why four signals

Pre-H1 check was filename-glob only (`_Archive/TICKER - *.md`). This missed archived theses whose filenames no longer encoded the ticker — either because the file was renamed before closure, or because the name portion corrupted during manual edits. Silent miss meant `/thesis` created a dual-file state without warning.

Four signals (UNION, dedup):
- **A — Filename glob**: `Glob _Archive/TICKER - *.md`. Catches the common case (archived file still has TICKER prefix).
- **B — Frontmatter ticker**: Grep `_Archive/*.md` for `^ticker: TICKER$` in frontmatter. Catches renamed-then-archived files where the filename drifted.
- **C — Archive-registry lookup**: Check `.archive_ticker_registry.md` (auto-maintained by `/status` Step 7.5b and `/prune` Stage 4). Each line `TICKER|archived_filename|YYYY-MM-DD`. Catches archived files whose frontmatter was also modified post-archival (rare but possible).
- **D — Snapshot trail**: Grep `_Archive/Snapshots/*.md` frontmatter for `snapshot_of:` values containing `Theses/TICKER -`. Catches historical trace when the thesis once existed in `Theses/TICKER - *.md` form, even if renamed/archived under a different filename since.

The UNION of all four signals catches the five archival scenarios: normal closure (A), rename-before-closure (B), multi-closure (C), deep historical trace (D), or any combination.

### §2.2 Why registry stale entries are tolerated

`.archive_ticker_registry.md` is append-only — never rewritten. Stale entries (referenced archived file was subsequently renamed or deleted) are tolerated because Signal C explicitly **verifies the referenced filename still exists in `_Archive/`** before treating the entry as a match.

This lets the registry accumulate without maintenance. `/lint #46` surfaces stale entries for optional cleanup; `/thesis`'s existence check defuses false positives automatically.

### §2.3 Four user options on collision

- **(a) /rollback TICKER — RECOMMENDED**: restores prior thesis with full Log history. Rollback cascade handles status: closed → active and re-attaches to sector note. Ideal when original thesis is being reopened.
- **(b) Proceed with DIFFERENT name suffix**: makes dual-file state intentional and visible (e.g., prior "TICKER - Old Brand" and new "TICKER - New Strategy"). Alternate name required.
- **(c) Proceed with proposed name, accepting dual files**: deliberately abandons archived analysis. Initial Log entry carries one-line caveat noting the retained archive.
- **(d) Cancel**.

Three out of four preserve the archived file; only (a) reverses the prior archival. This matches the intuition that archived analysis is usually worth keeping as historical record even when not being reopened.

### §2.4 Multiple archived files

Rare — typically caused by re-closure with timestamp suffix per `/status` Step 7.5a option (a) or (b). List all matches in the collision prompt. Same four options apply. Option (c)'s initial Log entry wikilinks the most recent archive (highest `closed:` date in frontmatter, or filename timestamp if frontmatter absent).

---

## §3 New-sector handling (Step 5 — 5.4 fix)

### §3.1 Why explicit branch, not silent skip

Pre-5.4 behavior: if `match_confidence: none` for sector resolution, `/thesis` silently skipped the sector update. The new thesis would exist in `Theses/` but no sector note referenced it — downstream skills (`/status`, `/compare`, `/prune`, sector-scoped `/surface`) would emit no-match warnings for this ticker indefinitely until the user manually created the sector note.

The silent skip produced accumulating warnings with no clear resolution path. Users often didn't realize they needed to create `Sectors/[value].md` until weeks later.

### §3.2 Three explicit options

- **(a) Create scaffold now — RECOMMENDED when new thesis is first in a legitimately new sector**: minimal `Sectors/[sector-value].md` from `Templates/Sector Template.md` with frontmatter + section headings + the new thesis as first Active Theses entry. Analytical content can be filled later via `/surface [sector]` or manual edit.
- **(b) Proceed without sector update**: thesis exists in `Theses/` but no sector note references it. Downstream warnings continue until user creates `Sectors/[value].md` manually.
- **(c) Cancel**: abort before writing thesis file. Useful if the sector value is a typo.

### §3.3 Scaffold-only, not deep analysis

Option (a) creates a minimal scaffold, not a full sector analysis. Rationale:
- Deep sector analysis typically requires cross-thesis synthesis that a fresh new thesis doesn't yet support
- Minimum viable scaffold is "section headings + `- _pending_` placeholders" — unblocks downstream resolution without inventing content
- Next `/deepen` or `/surface` against the sector fills in real content

The sector note's Log entry documents its scaffold-origin: `Sector note created by /thesis TICKER — first thesis in this sector. Scaffold-only; analytical content to be added via /deepen or /surface.`

---

## §4 Manifest skeleton contract (Step 3.5 — H1)

### §4.1 Why skeleton before any file modification

Same pattern as `/sync` Step 2.9, `/status` Step 3.0.5, `/prune` Stage 1.5: skeleton written BEFORE any mutation. Skeleton write failure hard-aborts pre-mutation — no orphan thesis file, no orphan sector note edit, no orphan `_hot.md` mention.

### §4.2 Why TICKER-qualified batch ID (C4)

Pre-C4: `thesis-YYYY-MM-DD-HHMMSS` could collide when two concurrent `/thesis NVDA` and `/thesis AMAT` runs hit the same second (per-ticker locks allow this concurrency — each ticker has its own lock).

TICKER-qualified `thesis-TICKER-YYYY-MM-DD-HHMMSS` makes every batch unique even under concurrent invocations.

### §4.3 Deletion-based rollback cascade (2.5f)

Unlike `/sync`/`/status` rollbacks (which restore FROM snapshots), thesis rollback is **deletion-based** because `/thesis` creates new files with no "before state" to snapshot. `/rollback` Step 2.5f cascade:
- **(a) Delete thesis file only** — leaves sector note + `_hot.md` modifications in place (dangles).
- **(b) Full cascade** — delete thesis + revert sector note Active Theses entry + revert `_hot.md` sections + revert orphan research mtimes (if captured in manifest).
- **(c) Cancel** — manual cleanup.

The manifest's intended-operations body + orphan-research list supply `/rollback` with the full state needed to reverse every step.

### §4.4 No regret-recovery window

Unlike `/prune` (30-day window for regret), `/thesis` doesn't need one. `/thesis` is constructive — regret here typically means "I want to edit/expand this thesis" which is `/deepen`'s job, not rollback. `/clean` Step 2a ages `_thesis-manifest` files with standard 90/180 day tiers.

---

## §5 Orphan research integration (Step 5)

### §5.1 Why touch research notes

Research notes created before this thesis existed were skipped by any prior `/sync` (no propagation target). Their mtimes sit behind `.last_sync`, so default `/sync` cannot re-process them via `find -newer .last_sync`.

`touch "Research/[matched-note].md"` advances mtime past `.last_sync`, re-entering them into the changed-file set. Next `/sync` (default OR ticker-scoped) runs standard propagation and appends the canonical `- [[Research/...]]: [what changed] — conviction [impact]` Log entry to this thesis.

Without the touch, the thesis's `## Log` would show only "Initial thesis created" and the research-to-thesis audit trail would be permanently broken — content integrated into sections but never acknowledged in the Log.

### §5.2 Why not edit the research note body

Research notes are Tier 2 append-only per CLAUDE.md Change Safety Rules. `/thesis` adds the research wikilink to THIS thesis's `## Related Research` section — no modification to the research note itself. The `touch` only advances mtime; file contents are untouched.

### §5.3 Resolution order (matches /sync)

Resolution order mirrors `/sync` Step 1 Fallbacks 1-2 for consistency:
- **(a) `ticker:` frontmatter** matching this ticker
- **(b) `tags:`** containing this ticker as a token

Same precedence produces consistent audit behavior — if `/thesis` picks up a research note, subsequent `/sync` runs will too (same resolution rules).

---

## §6 Rename-marker pre-flight (Step 0.2)

### §6.1 Why the edge case matters even for /thesis

`/thesis` creates a NEW thesis. Shouldn't be affected by rename markers (you can't rename a non-existent thesis). But the edge case:
- User previously created thesis TICKER
- Renamed partially (wikilinks fail) — `.rename_incomplete.TICKER` marker written
- Archived via `/status` or `/prune`
- Now creating a NEW thesis for same TICKER

In this case, the marker still exists. Without the pre-flight, `/thesis` would proceed — but Step 3.5's manifest, Step 4's Log entry, Step 5's sector note edits, Step 6's `_hot.md` entries would reference the new name while stale wikilinks still exist somewhere pointing to the pre-rename ORIGINAL name. The new thesis's state is correct but the vault has orphan broken wikilinks that `/lint #3` eventually flags.

Hard-block forces the user to resolve the marker first (complete the prior rename, or accept broken wikilinks via explicit `rm`).

---

## §7 Required-sections contract (Step 4)

### §7.1 Why 13 sections, specific order

Thesis note structure matches CLAUDE.md's Thesis Notes format definition. The order is intentional — analysis flows from concise summary → non-consensus insights → outstanding questions → business model → industry → metrics → bull case → bear case → catalysts → risks → conviction triggers → related research → log.

Deviating from this order breaks `/lint #14` (Template drift) and would confuse users switching between theses.

### §7.2 Why Key Non-consensus Insights is THE most important section

Per CLAUDE.md "Approach & Core Purpose": the vault focuses on non-consensus insights (technological/product, management/culture, competitive dynamics, investor bias, unique business model). The Non-consensus Insights section is where the skill delivers its primary value. Everything else is supporting structure.

### §7.3 Why Conviction Triggers must be falsifiable

Vague triggers ("if competition increases") don't actually govern conviction changes — they're aspirational. Falsifiable triggers ("if TSMC cuts capex guidance by >10% in next 2 quarters") let `/sync` drift detection and `/status` conviction checks fire objectively.

The SKILL.md example contrasts good vs bad to anchor the LLM's generation.

---

## §8 Why initial status is `draft`

New theses land as `status: draft`, not `status: active`. Rationale:
- Draft theses are excluded from `/catalyst`, `/prune` flags, conviction drift detection, sector Active Theses listings — gives the user time to review + refine before the thesis enters the full propagation network
- User explicitly promotes via `/status TICKER status draft→active` when ready — creates an audit point for "I've reviewed this thesis"
- Alternative (auto-active) would flood sector notes + `_hot.md` with incomplete theses before the user has vetted them

Step 8's Next Steps prompt surfaces the promotion path.

---

## §9 Parallel probe batch (Step 1.0)

### §9.1 Why parallelize

Pre-refactor: Step 0.2 + 1.1 + 1.2 Signals A–D + 1.3 ran as seven sequential tool calls. Each call incurs round-trip latency independent of the actual work. At typical latencies, the sequential chain added ~10–15s wall-clock to the skill for zero analytical benefit — probes don't depend on each other.

Post-refactor: all seven probes fire as independent tool calls in a single batch, processed post-return with priority-ordered short-circuit logic. Same semantics, one round-trip instead of seven.

### §9.2 Safety under the lock contract

The parallelization is safe because of three invariants established by `.claude/skills/_shared/preflight.md` Procedure 1:

1. **Lock acquired in 0.1 before any probe fires** — the `ticker:TICKER` lock blocks every skill that could mutate the probed state for the same ticker (`/status`, `/sync TICKER`, `/deepen`, `/stress-test`, `/rename`). Vault-wide skills (`/sync all`, `/graph`, `/prune`, `/clean`, `/ingest`) are also blocked by the existence of our ticker lock (per preflight §1.3b collision check).

2. **Probes are read-only** — none of the seven probes mutate vault state. Concurrent reads are safe even if another skill holds a different ticker lock.

3. **Probes don't consume each other's output** — no probe's input depends on another probe's result. The only post-batch dependency is Signal C's conditional Grep (fires only if the registry exists), which is correctly sequenced as a single follow-up step.

### §9.3 Ownership verification does NOT apply to read-only tools

Preflight §1.5 mandates ownership verification at the start of every **Bash** block. The parallel probe batch uses `Glob` and `Grep` — neither can release or overwrite the lockfile, so verification is unnecessary. The lock established in 0.1 remains valid across the entire probe batch with no additional checks.

This is why parallelization is a pure win for this step: the only tool that would have forced sequential execution (Bash with verification preamble) isn't used here.

### §9.4 Priority ordering of probe results

Post-batch processing short-circuits in this order:

1. **Rename marker (0.2)** — highest priority. A live marker means the vault has in-flight wikilink repair; any other probe result is derived from potentially-stale filenames. Hard-block.
2. **Active thesis (1.1)** — second priority. If a thesis exists for TICKER, the archive/research probes are informational only (no new thesis can be created). Stop.
3. **Archive collision (1.2 UNION)** — third priority. Requires user confirmation via the 4-option prompt (§2). Resolvable in-flow.
4. **Research context (1.3)** — lowest priority. Never blocks. Feeds Step 2.

This ordering matches the "hardness" of each gate: marker is irreversible without repair, active-thesis duplicates are a hard stop, archive collisions need user input, research context is pure information.

### §9.5 Why option (b) re-probes only 1.1

The archive-collision option (b) prompts the user for an alternate company name, then proceeds as if starting fresh with `Theses/TICKER - [alternate-name].md`. Only Step 1.1 (active thesis check) is name-dependent. The rename marker, archive signals, and research grep are all **ticker-dependent** — changing the proposed company name doesn't change whether the marker exists, whether archives for this ticker exist, or what research mentions the ticker.

Re-running only the 1.1 Glob against the alternate name is sufficient. Re-firing the full batch would waste tokens confirming what we already know.

### §9.6 Trade-off: token context vs. wall-clock

Firing seven parallel tool calls consumes slightly more context per message (seven tool-result blocks instead of one). On large vaults where Signal D Grep returns many matches, this could be a noticeable token hit in a single turn. Sequential execution would let earlier short-circuits (e.g., 1.1 active-thesis found) skip the later probes entirely.

The refactor accepts this trade-off because:
- Short-circuit saves on the rare path (active thesis exists → stop); parallel wins on the common path (no duplicate, proceed to Step 2)
- Context cost is bounded: seven small read-only tool results, not thousands of lines
- Wall-clock improvement is consistent across all runs, whereas short-circuit savings are probabilistic

If future profiling shows Signal D Greps are consistently returning >1MB of context on large vaults, revisit: a gated short-circuit (check 1.1 first, fan out only if it returns empty) would recover context at the cost of one extra round-trip.

### §9.7 Cross-skill impact

This refactor touches **only** `/thesis`. The probes themselves are unchanged — same files read, same patterns, same union logic. Cross-skill consumers (`/lint #49` reading thesis manifests, `/rollback` consuming thesis-manifest state, `preflight.md` Procedure 2 defining the rename-marker contract) see identical behavior.

The only external doc touched alongside this refactor is `preflight.md` line 365's reference to "/thesis at Step 1.1.5" (which had drifted from SKILL.md anyway). Updated to reflect the new Step 1.0 parallel-batch location.
