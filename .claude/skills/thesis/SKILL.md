---
name: thesis
description: Create a new investment thesis note with full analysis. Use when user says "create thesis", "new thesis", or "build a case for TICKER"
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * defuddle * touch *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, lead with insights/numbers, tables over prose, every sentence must earn its place.

Create a comprehensive thesis note for $ARGUMENTS.

## Step 1: Duplicate Check
Before creating anything, search the vault for existing notes on this ticker/topic. Active-thesis detection must use a **prefix glob**, not content grep — short tickers (e.g., `A` for Agilent, `T` for AT&T, `U` for Unity) match too many filenames under content grep, producing false-positive duplicate warnings that block legitimate thesis creation.

1. **Active thesis check (prefix glob)**: `Glob Theses/TICKER - *.md`. If any file matches, an active thesis already exists — stop and suggest `/deepen TICKER` instead. Report the matching filename.
2. **Archived thesis check (prefix glob)** — Tier 3 confirmation gate: `Glob _Archive/TICKER - *.md` (non-recursive — snapshots live under `_Archive/Snapshots/` and must not match). If one or more files match:

   a. **Read the archived thesis(es)** — extract from each: filename, last Log entry (typically the closure rationale), `conviction:` at closure, `status:` (should be `closed`).

   b. **Present a structured prompt — wait for explicit user choice. Do NOT proceed silently.**

   ```
   ⚠️ Archived thesis exists for TICKER:
     - [[_Archive/TICKER - Old Company Name]]
       closed: [date] · conviction at closure: [level]
       closure rationale: [last Log entry, truncated to 1 line]

   Creating a new thesis at Theses/TICKER - [proposed-name].md will produce
   TWO distinct files for the same ticker. Downstream skills (/sync, /graph,
   /catalyst) operate on Theses/* and ignore _Archive/* — the prior analysis,
   Log audit trail, and conviction journey become invisible to the new thesis.

   Options:
     (a) /rollback TICKER  — RECOMMENDED. Restores the prior thesis with
         its full Log history. Use this if the original thesis is being
         reopened (rather than starting fresh on the same ticker).
         The rollback flow handles status: closed → active and re-attaches
         the thesis to its sector note.

     (b) Proceed with new thesis under a DIFFERENT name suffix to make the
         dual-file state intentional and visible (e.g., the prior thesis
         was "TICKER - Old Brand" and you want "TICKER - New Strategy").
         Provide an explicit alternate name. The archived file is preserved.

     (c) Proceed with the proposed name, accepting that two files for the
         same ticker will exist (one in Theses/, one in _Archive/) and that
         the archived analysis is being deliberately abandoned. Useful only
         if the prior thesis is irrelevant to the new investment case.
         The archived file is preserved.

     (d) Cancel.

   Confirm (a/b/c/d):
   ```

   c. **Branch on user choice:**
   - **(a)**: Stop the skill. Output: `→ Run: /rollback TICKER` and exit. Do not create any new thesis. The user runs `/rollback` separately.
   - **(b)**: Re-prompt for the alternate company name. Compute the new filename `Theses/TICKER - [alternate-name].md`. Re-run Step 1.1 (active thesis check) against the alternate name to ensure no live-file collision. Then proceed to Step 2 with the alternate name.
   - **(c)**: Proceed to Step 2 with the originally proposed name. Add a one-line caveat to the new thesis's initial Log entry: `Initial thesis created. Conviction: [level] — [rationale]. Note: prior archived thesis at [[_Archive/TICKER - Old Name]] retained for reference but not connected to this thesis.`
   - **(d)**: Stop the skill silently.

   d. **Multiple archived files** (rare — typically caused by re-closure with timestamp suffix per `/status` Step 7.5a option (a) or (b)): list all matches in the prompt above. The same options apply; the user's "prior archived thesis" reference in option (c)'s log entry should wikilink the most recent archive (highest `closed:` date in frontmatter, or filename timestamp if frontmatter absent).
3. **Research context grep (content search is appropriate here)**: Grep `Research/` for the ticker string to surface relevant existing research that the new thesis should link to. This is informational only — does not block creation. Prefer frontmatter `ticker: TICKER` match and `tags:` containing the ticker as whole-word matches over body-text mentions to keep short-ticker false positives out of the context set.

## Step 2: Vault Research
- Read the relevant Sector Note to understand existing coverage and competitive context
- Search /Research and /Macro for any notes mentioning this ticker or topic
- Read related thesis notes for competitive dynamics and cross-thesis connections

## Step 3: Web Research
- Search for recent earnings results, analyst consensus, key financials
- Search for competitive dynamics, market share data, industry trends
- Search for bear cases and risks — actively look for reasons NOT to invest
- Search for sell-side consensus to identify where a non-consensus view could exist

## Step 4: Create the Thesis
Save to `Theses/TICKER - Company Name.md` with:

```yaml
---
date: [today's date]
tags: [thesis, SECTOR-TAG, TICKER]
status: draft
conviction: [high|medium|low — assess honestly]
sector: [primary sector]
ticker: TICKER
source: [primary source URL or description]
---
```

### Required Sections (all 13, in this order):

1. **Summary** — One paragraph investment case. Lead with the non-consensus angle, not a business description.

2. **Key Non-consensus Insights** — 3-5 one-paragraph summaries of perspectives foreign to the mainstream narrative. THIS IS THE MOST IMPORTANT SECTION. Think deeply about what the market is missing — technological shifts, management/culture edges, competitive dynamics, investor biases, business model transitions.

3. **Outstanding Questions** — 3-10 one-paragraph summaries of what a skeptical investment committee would ask before approving. These should be genuinely hard questions, not softballs. Each should identify what data or event would answer it.

4. **Business Model & Product Description** — In-depth breakdown of the business model with analogies/comparisons to make it intuitive. Key revenue/profit-generating products with technical specs where relevant. Revenue segmentation by reported segment or a novel heuristic that better captures the economics.

5. **Industry Context** — Competitive dynamics, market share and pricing power shifts, value chain analysis. Where does this company sit in the value chain? Who has leverage over whom? What structural forces are reshaping the industry?

6. **Key Metrics** — Table format:

| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | | |
| EV/Revenue | | |
| Revenue Growth | | |
| Gross Margin | | |
| FCF Yield | | |

7. **Bull Case** — Explicit upside scenario with specific drivers. What has to go right? Include valuation target or framework if possible.

8. **Bear Case** — Explicit downside scenario with specific drivers. Be genuinely adversarial — don't softball this. What does the world look like where this investment loses money?

9. **Catalysts** — Near-term events with approximate dates that could move the stock. Include both positive and negative catalysts.

10. **Risks** — What breaks the thesis. Minimum 3 risks. Distinguish between thesis risks (the investment case is wrong) and position risks (the thesis is right but the stock goes down anyway).

11. **Conviction Triggers** — Pre-defined, falsifiable if/then statements that govern conviction changes:
    ```
    → HIGH if: [specific observable condition]
    → LOW if: [specific observable condition]
    → CLOSE if: [specific observable condition]
    ```
    These must be concrete and testable, not vague ("if competition increases"). Good example: "→ LOW if TSMC cuts capex guidance by >10% in next 2 quarters."

12. **Related Research** — Wikilinks to all relevant vault notes (research, sector notes, macro notes, related theses).

13. **Log** — Initial entry:
    ```
    ### YYYY-MM-DD
    - Initial thesis created. Conviction: [level] — [one-line rationale]
    ```

## Step 5: Update the Vault
- **Sector Note update**: Resolve the sector note via canonical procedure **`.claude/skills/_shared/sector-resolution.md`** using the thesis's `sector:` frontmatter. If `match_confidence` is `none`, emit the contract's no-match warning and skip to the next bullet. If `match_confidence` is `normalized` or `substring`, emit the contract's `log_message` in the Step 7 report. **If status is `active`**: add the thesis to the resolved Sector Note "Active Theses" section. **If status is `draft`**: skip — the thesis will be added when promoted via `/status TICKER status draft→active`.
- **Integrate orphan research notes**: Search `Research/` for notes that predate this thesis and reference it. Resolution order (same as `/sync` Step 1 Fallbacks 1–2): (a) `ticker:` frontmatter matching this ticker, (b) `tags:` containing this ticker as a token. For each match:
  1. Add a wikilink to the new thesis's `## Related Research` section (do NOT modify the research note itself — Tier 2 append-only zone per CLAUDE.md).
  2. `touch` the research note to advance its mtime past `.last_sync`:
     ```bash
     touch "Research/[matched-note].md"
     ```
  > **Why the `touch`**: Research notes created before this thesis existed were skipped by any prior `/sync` (no propagation target). Their mtimes sit behind `.last_sync`, so default `/sync` cannot re-process them via `find -newer .last_sync`. Advancing mtime re-enters them into the changed-file set, so the next `/sync` (default OR ticker-scoped) runs the standard propagation and appends the canonical `- [[Research/...]]: [what changed] — conviction [impact]` Log entry to this thesis. Without the touch, the thesis's `## Log` would show only "Initial thesis created" and the research-to-thesis audit trail would be permanently broken — content integrated into sections but never acknowledged in the Log.

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the new thesis (full adjacency entry: sector, macro, cross-thesis, research) in the dependency map. Until `/graph last` runs, ticker-scoped operations resolve adjacency directly from the thesis file via Outcome B fallback.

## Step 6: Update _hot.md

Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: new thesis created for [TICKER], conviction [level], and the logical next research step. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry for the new thesis with initial conviction level
3. **Open Questions**: Add the 2-3 most critical Outstanding Questions from the new thesis

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Step 7: Suggest Next Steps
- **Activate**: This thesis was created as `status: draft`. Run `/status TICKER status draft→active` when ready to promote it — draft theses are excluded from some downstream skills (`/catalyst`, `/prune` flags, conviction drift detection).
- What 2-3 research questions would most increase or decrease conviction?
- Any upcoming catalysts to monitor with dates?
- Which existing vault theses have the strongest competitive tension with this one?
