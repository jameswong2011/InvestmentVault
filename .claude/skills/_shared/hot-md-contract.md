---
type: shared-contract
purpose: Canonical compression, section ordering, and word-budget policy for `_hot.md`. Every skill that writes to `_hot.md` follows this contract.
last_reviewed: 2026-04-24
---

<!--
This file is a load-bearing contract. `_hot.md` schema drift causes silent no-ops across 14 skills. `/lint #35` enforces structural compliance (section headings); this contract additionally specifies compression behavior, per-section budgets, and cap handling.

Consumers: `/sync`, `/status`, `/thesis`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/deepen`, `/prune`, `/rollback`, `/catalyst`, `/brief` (Active Research Thread + Open Questions only), `/rename` (free-text mentions of the old name), `/retro` (Active Research Thread + Open Questions only).
-->

# `_hot.md` Compression & Budget Contract

> **Why this exists**: the prior single-value hard cap with unspecified compression behavior produced drift. Different skills compressed different sections with different heuristics; compaction lost high-signal context (conviction rationales, drift flags) while preserving low-signal context (old sync archive entries). This contract specifies per-section compression policy and a soft/hard cap pair so compaction pressure is visible and actionable.

## Section budget table

Total soft cap: **4,000 words**. Total hard cap: **5,000 words**.

| Section | Budget share | Compression policy |
|---|---|---|
| `## Active Research Thread` | 30% (1,200 words soft) | Verbatim entries from the last 48 hours. Older entries compressed to one-line summaries: `*Previous YYYY-MM-DD:* [topic] — [outcome]`. Max 5 `*Previous:*` lines; drop oldest when exceeded. |
| `## Latest Sync` | 15% (600 words soft) | Verbatim. Replaced entirely on each `/sync`. Never compressed within; if over budget alone, shorten the per-thesis bullets (see 2.2). |
| `## Sync Archive` | 20% (800 words soft) | Max 3 archived entries. **Never truncate an individual entry**; when over budget, DROP the oldest entry entirely (preserves audit integrity of what remains). |
| `## Recent Conviction Changes` | 15% (600 words soft) | Last 30 days verbatim. Entries older than 30 days roster-compress to one-liner: `- YYYY-MM-DD — TICKER (Company) [conviction/status change]. Rationale: [[Theses/TICKER - Company]] §Log + body.` The thesis Log is the canonical audit trail; RCC is an index of recent ones. **Aggressive fallback** (trigger order step 6): if still over hard cap after steps 1-5, progressively roster-compress entries younger than 30 days in age order until under hard cap OR only the 5 most-recent verbatim entries remain. |
| `## Open Questions` | 15% (600 words soft) | Merge duplicates: same question from multiple theses collapses to one entry with `[theses: A, B, C]` token. **Cohorts older than 14 days** drop to a single one-line pointer per cohort: `- N-M. [TICKER] questions ([init date] cohort, [N] days old) — see [[Theses/TICKER - Company]] §Outstanding Questions.` Full questions live in the thesis body (canonical home); `_hot.md` is an index. `/catalyst`-pattern entries auto-resolve via `/sync` Step 6 #5b. |
| `## Portfolio Snapshot` | 5% (200 words soft) | Regenerated fresh on each `/sync`. Never compressed-accumulated. If the computed content exceeds 200 words, truncate the generated summary to top-level counts only. |

Budget shares sum to 100% — treat as guidance when compression fires, not hard per-section quotas. A section below its soft share donates spare budget to any section over its share.

## Compression trigger order

When total word count exceeds the soft cap (4,000):

1. **Drop oldest `## Sync Archive` entry** (whole entry, not truncated). Recheck total.
2. **Drop oldest `*Previous:*` line from `## Active Research Thread`**. Recheck total.
3. **Merge duplicate `## Open Questions`** (same question body, different tickers → combine). Recheck total.
4. **Drop Open Questions cohorts older than 14 days** — replace each cohort (consecutive items sharing a single creation-date / ticker origin) with one pointer line: `- N-M. [TICKER] questions ([init date] cohort, [N] days old) — see [[Theses/TICKER - Company]] §Outstanding Questions.` The canonical questions live in thesis bodies; `_hot.md` is an index. Recheck total.
5. **Roster-compress Recent Conviction Changes entries older than 30 days** — replace each entry with one-liner: `- YYYY-MM-DD — TICKER (Company) [conviction/status change]. Rationale: [[Theses/TICKER - Company]] §Log + body.` Thesis Logs preserve full audit fidelity. Recheck total.
6. **Aggressive RCC fallback** — fires only if `total > hard_cap` after step 5. Progressively roster-compress Recent Conviction Changes entries younger than 30 days, in age order (oldest first), until under hard cap OR only the 5 most-recent entries remain verbatim. This intentionally relaxes the 30-day verbatim window to enforce the hard cap; thesis Logs preserve full audit fidelity regardless. Recheck total.
7. **Raise a warning in the skill's Step 8/Phase N report** listing which sections are still over share and by how much. Example: `⚠️ _hot.md approaching soft cap ([N] words / 4,000). Recent Conviction Changes at [M]% of share. Consider review.`

If after all these steps the total still exceeds 5,000 (hard cap):

8. **Abort the skill's `_hot.md` update** with: `❌ _hot.md exceeds hard cap (5,000 words) after full compression (steps 1-7). Diagnose: run /lint #35 and check whether the dashboard layer (Active Research Thread / Latest Sync) is itself oversized — steps 1-7 cannot compress those. Manual cleanup of dashboard required.`

The abort applies only to the `_hot.md` write — the skill's primary operation (thesis edit, sector note update, research note creation) still proceeds. Session-context degradation is tolerable; primary operation correctness is not.

## Truncation-marker detection

Compression above never truncates individual entries. But manual user edits or legacy compaction may have left artifacts. **Forbidden markers** (caught by `/lint #42`):

- Trailing ellipsis `...` on its own line or at the end of a bullet
- Bracketed sentinels `[compressed]`, `[truncated]`, `[...]`
- Unclosed markdown: trailing `**`, `*`, `_`, backtick, `[`, `(`

Any skill writing to `_hot.md` must verify its own section-level writes are free of these markers (post-write re-read + grep). If a skill detects them, it must either repair or log: `⚠️ _hot.md section "## [name]" contains truncation marker — manual review needed.`

## Same-ticker continuation rule

Many skills have "same-ticker continuation" logic in their `## Active Research Thread` update. Canonical behavior:

1. Read current Active Research Thread heading block.
2. Detect primary ticker in the current thread via:
   - First `[[TICKER - ...]]` wikilink in the first 3 non-previous lines, OR
   - Explicit `**[TICKER]**` marker in the first line
3. **Same-ticker skill invocation** (new event references the same TICKER): append a dated line (`YYYY-MM-DD: [update]`) to the existing thread block. Do NOT compress — the active thread stays live.
4. **Different-ticker skill invocation**: compress the outgoing thread into a single `*Previous YYYY-MM-DD:*` line (capture topic + outcome in ≤15 words), prepend that `*Previous:*` line to the block, then replace the thread body with the new event.

When ambiguity exists (no wikilink, multi-ticker thread), treat as different-ticker (safer: forces compression, preserves audit via *Previous:* line).

## Producer checklist

Every skill writing to `_hot.md`:

1. Read `_hot.md` at start of its update step. If file does not exist, create per CLAUDE.md Rule #9 schema.
2. Verify each required section (`## Active Research Thread`, `## Latest Sync`, `## Sync Archive`, `## Recent Conviction Changes`, `## Open Questions`, `## Portfolio Snapshot`) exists. If missing, log warning and skip only that section's update — do NOT add the heading silently (`/lint #35` owns schema enforcement; skills are content producers, not schema fixers).
3. Apply section-specific update using Edit (not Write) to avoid whole-file rewrite.
4. After all section edits complete, count total words.
5. If over soft cap, run compression trigger order above.
6. If over hard cap after compression, abort `_hot.md` write per policy above.
7. Report compression actions in skill's final report under a `_hot.md update:` line.

## Lint enforcement

- `/lint #35` — schema integrity (section headings present and in canonical order)
- `/lint #42` (new) — truncation-marker presence (`...`, `[compressed]`, unclosed formatting)
- `/lint #35` also checks word cap and emits Important if exceeded — matches hard cap here

## Drift policy

If a skill needs a new `_hot.md` section or a new compression rule, update this contract FIRST, then the skill. Never let a skill embed its own section or compression logic — every such divergence becomes a silent drift point.
