---
date: 2026-04-21
tags: [meta, convention, templates]
---

# Callout Conventions

Visual markers for inline user feedback on LLM-generated content. Drop callouts inside any section; Claude addresses them on demand via chat.

## The 4 Types

| Callout | Hotkey (macOS / Windows) | Use when |
|---|---|---|
| `> [!question]` | `⌘+Option+1` / `Ctrl+Alt+1` | You want Claude to answer something |
| `> [!tip]` | `⌘+Option+2` / `Ctrl+Alt+2` | Suggestion for how the section should change |
| `> [!error]` | `⌘+Option+3` / `Ctrl+Alt+3` | Disagreement or "don't miss this" |
| `> [!todo]` | `⌘+Option+4` / `Ctrl+Alt+4` | Explicit action (research X, add Y, fetch Z) |

Urgency escalates: 1 asks, 2 suggests, 3 flags, 4 demands action.

## Lifecycle

| State | Syntax | When |
|---|---|---|
| **Fresh** | `> [!question] 2026-04-21` | Just dropped, waiting for response |
| **Addressed** | `> [!question] 2026-04-21 → Addressed 2026-04-22` + `**Response:**` block | Claude handled it |
| **Pinned** | `> [!question] 2026-04-21 [[pinned]]` | Intentionally left open |

### Example — fresh → addressed

Before:

```markdown
> [!question] 2026-04-21
> Pricing-power argument is thin — need Q4 transcript evidence.
```

After Claude addresses it:

```markdown
> [!question] 2026-04-21 → Addressed 2026-04-22
> Pricing-power argument is thin — need Q4 transcript evidence.
> 
> **Response:** Integrated Q4 Stagwell economics (+46% ROAS, 57%
> go-live conversion) into Bull Case bullet #1. See Log 2026-04-22.
```

The callout persists — visual audit trail co-located with the edit. Delete addressed callouts or keep them; both patterns work.

## Workflow

```
1. Drop callouts inline (hotkey ⌘/Ctrl+Alt+1..4)
2. Ask Claude to address them
3. Claude edits sections, marks callouts addressed, writes Log entries
4. /sync TICKER  (one thesis)
   /sync         (multiple theses)
   /sync all     (whole vault)
5. /graph last
```

## Chat Prompt Template

Copy-paste, swap the target:

> Read [[Theses/TICKER - Company Name]] and address every fresh `[!question]`, `[!tip]`, `[!error]`, and `[!todo]` callout. For each: edit the surrounding section to incorporate the feedback, rewrite the callout header to `→ Addressed YYYY-MM-DD` with a one-line response inside the callout, and append a Log entry summarizing what changed.

For multi-note scope, replace the wikilink with "every thesis I've touched since [date]" or "every thesis in [[Sectors/X]]".

## Setup (One-Time Per Vault Clone)

Only required on the FIRST machine — later clones inherit via git.

1. Settings → Templater → Template Hotkeys → add all 4 files in `Templates/callouts/`.
2. Settings → Hotkeys → search `Templater: callouts/user-<type>` → bind `⌘/Ctrl+Alt+1..4`.
3. Commit `.obsidian/hotkeys.json` and `.obsidian/plugins/templater-obsidian/data.json` — both are git-tracked.

After git pull on a new machine, hotkeys and templates work immediately. No re-binding.

## Cross-Platform Notes

- Hotkeys store in `.obsidian/hotkeys.json` as `Mod+Alt+<N>` — Obsidian auto-maps `Mod` to `⌘` on macOS and `Ctrl` on Windows/Linux; `Alt` maps to `Option` on macOS. Avoids `⌘+Shift+3/4/5` which macOS reserves for screenshots.
- Templater template registration in `.obsidian/plugins/templater-obsidian/data.json` — identical behavior across platforms.
- Both files are git-tracked (not in `.gitignore`); pulling the vault on a new machine inherits hotkeys and registrations automatically.

## Why Callouts, Not Sections

Callouts give **co-located visual provenance** — you see what you wrote vs what the LLM wrote in the exact spot the decision matters. Zero template changes, zero skill changes, cross-platform via git.

## See Also

- [[CLAUDE.md]] Workflow Rule #7
- [[User Guide]] §2 "User callouts — inline feedback on LLM output"
