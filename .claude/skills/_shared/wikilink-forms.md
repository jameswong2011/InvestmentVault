---
type: shared-contract
purpose: Canonical list of wikilink forms every skill must match when searching for a reference to a vault note. Prevents 5-fold repetition across SKILL.md files.
last_reviewed: 2026-04-20
---

# Wikilink Form Matching Contract

> **Why this exists**: Every skill that checks whether "note X is referenced in note Y" must match the same five wikilink forms producers emit. Listing them inline in each SKILL.md is a drift hazard — a producer adds a sixth form and consumers silently miss it. Centralizing here keeps producers and consumers aligned.
>
> **Consumers**: `/sync` (Step 1 Check 2/3, Step 4.0, Step 5.0), `/rollback` (Step 2.5 cascade detection), `/lint` (orphan checks, reverse-index validation), `/prune` (closure cascade detection).

## The five canonical forms

For a research/thesis/sector/macro note whose filename (without `.md`) is `BASE` (e.g., `2026-04-19 - NVDA - earnings` or `Theses/NVDA - Nvidia`), producers emit wikilinks in exactly these forms:

| # | Form | Example |
|---|---|---|
| 1 | `[[Folder/BASE]]` — folder-qualified, no extension | `[[Research/2026-04-19 - NVDA - earnings]]` |
| 2 | `[[Folder/BASE.md]]` — folder-qualified, explicit `.md` | `[[Research/2026-04-19 - NVDA - earnings.md]]` |
| 3 | `[[Folder/BASE\|alias]]` — folder-qualified with display alias | `[[Research/2026-04-19 - NVDA - earnings\|Q1 earnings]]` |
| 4 | `[[Folder/BASE#section]]` — folder-qualified with section anchor | `[[Research/2026-04-19 - NVDA - earnings#Key Takeaways]]` |
| 5 | `[[BASE]]` — folder-less (legacy / Obsidian short-form) | `[[2026-04-19 - NVDA - earnings]]` |

Forms 3 and 4 can combine: `[[Folder/BASE#section|alias]]`.

## Canonical regex (Grep pattern)

For a wikilink-presence check where `BASE` is the note basename and `FOLDER` is one of `Research`, `Theses`, `Sectors`, `Macro`:

```regex
\[\[(FOLDER/)?BASE(\.md)?(#[^\]|]+)?(\|[^\]]+)?\]\]
```

Escape `BASE` for regex metacharacters first (spaces, `-`, `&`, `.`, `(`, `)` are all legal in vault filenames). A safe construction pattern in Bash:

```bash
BASE='2026-04-19 - NVDA - earnings'
BASE_ESC=$(printf '%s' "$BASE" | sed 's/[][\\.^$*+?(){}|/]/\\&/g')
PATTERN="\[\[(Research/)?${BASE_ESC}(\.md)?(#[^]|]+)?(\|[^]]+)?\]\]"
```

Use this pattern with `Grep` (tool) or `grep -E` (shell). The tool uses `ripgrep` which accepts this syntax directly.

## Match semantics

A "match" means the note is referenced — regardless of which form. Consumers should treat all five forms as equivalent for:
- **Idempotency checks** (has this note already been propagated?)
- **Reverse-index construction** (which theses link to this research note?)
- **Cascade detection** (which notes would be affected by renaming this file?)
- **Orphan detection** (is this note linked from anywhere?)

## Producer conformance

Every skill that writes wikilinks **should emit form #1 by default** (folder-qualified, no extension, no alias). Other forms are tolerated on read but not preferred on write. This keeps the written corpus consistent while preserving read-compatibility with manual user edits and legacy notes.

## Drift prevention

If a new form emerges (e.g., Obsidian adds a new syntax), update this contract FIRST, then every consumer skill. `/lint` check #23 (reverse-index consistency) surfaces discrepancies that may indicate unmatched forms.
