---
type: skill-rationale
skill: /thesis
purpose: Design rationale for /thesis — multi-signal archive-collision detection, new-sector handling, manifest contract, orphan research integration.
last_reviewed: 2026-04-20
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
