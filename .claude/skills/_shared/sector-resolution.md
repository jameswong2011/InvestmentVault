---
type: shared-contract
purpose: Canonical procedure for resolving a thesis's `sector:` frontmatter to a sector note in Sectors/.
last_reviewed: 2026-04-17
---

# Sector Resolution Contract

> **This file is a load-bearing contract.** Every skill that resolves a thesis's `sector:` frontmatter to a `Sectors/*.md` note must use this canonical procedure. Inconsistent matching across skills produces silent failures (sector note never updated, propagation drift) — the same `sector: semiconductors` value silently resolves in `/status` but not in `/prune`.
>
> **Consumers**: `/status` Step 5.0, `/thesis` Step 5, `/compare` Phase 5, `/prune` Stage 1 (sector-affected resolution).

## Inputs

- `thesis_sector`: the thesis's `sector:` frontmatter value as a string (may have varied case / whitespace / trailing punctuation)

## Outputs

- `sector_note_path`: relative path to matching sector note (e.g., `Sectors/Semiconductors & AI Infrastructure.md`)
- `match_confidence`: `exact` | `normalized` | `substring` | `none`
- `log_message`: human-readable note to surface in skill report when confidence is not `exact`

## Procedure

### Step 1 — Normalize

Define `normalize(s) = lowercase(s).strip().collapse_whitespace()`. Whitespace collapse: multiple spaces/tabs become single space.

Compute `norm_thesis = normalize(thesis_sector)`.

### Step 2 — Try exact match (case-sensitive, original strings)

In this order:
1. Check `Sectors/[thesis_sector].md` exists as a literal filename → return path, confidence `exact`, no log.
2. Grep `Sectors/*.md` for `sector: [thesis_sector]` (exact frontmatter match) → return that file's path, confidence `exact`, no log.

If neither matches, proceed to Step 3.

### Step 3 — Try normalized match (case-insensitive, whitespace-collapsed)

For each `Sectors/*.md`:
1. Compute `norm_filename = normalize(filename without .md extension)`.
2. Compute `norm_frontmatter = normalize(sector frontmatter value)`.
3. If `norm_thesis == norm_filename` OR `norm_thesis == norm_frontmatter` → return that file's path, confidence `normalized`, log: `ℹ️ Sector resolved via case/whitespace normalization: thesis sector "[thesis_sector]" → "[matched filename]". Consider standardizing one of them.`

If multiple match (rare — would require near-duplicate sector notes), prefer the one whose `norm_frontmatter` matches over `norm_filename`. If still tied, prefer the most recently modified file. Log the disambiguation.

If no match, proceed to Step 4.

### Step 4 — Try substring match (case-insensitive, normalized)

This catches sector renames like `Semiconductors` → `Semiconductors & AI Infrastructure`.

For each `Sectors/*.md`:
1. Compute `norm_filename` and `norm_frontmatter` as above.
2. If `norm_thesis` is a substring of `norm_filename` OR `norm_filename` is a substring of `norm_thesis`, OR same for `norm_frontmatter`:
   - Compute edit distance between `norm_thesis` and the matching name.
   - Track as a candidate with that distance.
3. If exactly one candidate: return it, confidence `substring`, log: `⚠️ Sector resolved via substring match: thesis sector "[thesis_sector]" → "[matched filename]" (edit distance [N]). Likely a rename or typo — consider running /rename or updating thesis frontmatter.`
4. If multiple candidates: prefer the smallest edit distance. If still tied, **stop and ask the user** which to use. Do NOT silently choose. Emit: `⚠️ Multiple sector notes match "[thesis_sector]" via substring: [list]. Please specify the canonical sector or run /rename to standardize.`

If no candidate, proceed to Step 5.

### Step 5 — No match

Return null path, confidence `none`. Caller emits:

```
⚠️ No sector note found matching sector: [thesis_sector]. Skipping sector note update. Consider:
  - Creating a sector note: Sectors/[thesis_sector].md (use Templates/Sector Template.md)
  - Or correcting the thesis's `sector:` frontmatter to match an existing sector note.
```

## Caller responsibilities

Skills using this procedure must:

1. **Always log non-exact matches** — never silently use a `normalized` or `substring` resolution. The log message exists to make divergence visible to the user.

2. **Treat `substring` matches as advisory** — proceed with the resolved sector note, but the log message must encourage standardization.

3. **Treat `none` as a graceful skip** — emit the warning above, skip the sector update, continue with the rest of the skill (do not abort the entire skill on missing sector note).

4. **Never write to a sector note resolved with confidence `substring`** without explicit user confirmation if the operation is destructive (e.g., rewriting analytical content). Adding a wikilink to Active Theses is fine; rewriting a section is not.

## Drift prevention (`/lint` enforcement)

The contract is enforced by two `/lint` checks (implemented in `.claude/skills/lint/SKILL.md`):

- **Check #30 (Sector resolution coverage)** — scoped-eligible: For every `Theses/*.md` with `sector:` frontmatter, runs this procedure. `none` confidence flagged Important; `substring` and `normalized` flagged Nice to Have. Pass for `exact`.
- **Check #31 (Sector frontmatter standardization)** — vault-wide only: For each unique `sector:` frontmatter value across `Theses/`, verifies it matches at least one sector note's filename or frontmatter exactly. Reports divergences with edit distance and closest match.

If either check is missing from `/lint`, this contract is unenforced and drift will accumulate silently.

## Editing protocol

1. **Before any edit**: identify every consumer skill (`/status`, `/thesis`, `/compare`, `/prune`) and verify each references this file.
2. **Edit this file first** — single source of truth.
3. **Run `/lint`** — once checks #30 and #31 are added, lint validates the contract automatically.
4. **Update `last_reviewed:` frontmatter** to today's date.

## Rationale

Original problem: sector matching was inline in each skill, using exact case-sensitive string comparison against either filename or frontmatter. A thesis with `sector: semiconductors` (lowercase) and a sector note with `Sectors/Semiconductors & AI Infrastructure.md` would silently fail to match in `/status`, but `/prune` might match by a different heuristic, leading to inconsistent state across skills.

This contract:
- Eliminates skill drift by centralizing the procedure.
- Surfaces divergences instead of silently failing.
- Provides a clear escalation path (exact → normalized → substring → user prompt → skip).
- Enforced by `/lint` checks #30 (per-thesis resolution coverage) and #31 (vault-wide standardization).
