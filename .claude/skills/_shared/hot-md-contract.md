---
type: shared-contract
purpose: Canonical compression, section ordering, and word-budget policy for `_hot.md`. Every skill that writes to `_hot.md` follows this contract.
last_reviewed: 2026-04-20
---

<!--
This file is a load-bearing contract. `_hot.md` schema drift causes silent no-ops across 11 skills. `/lint #35` enforces structural compliance (section headings); this contract additionally specifies compression behavior, per-section budgets, and cap handling.

Consumers: `/sync`, `/status`, `/thesis`, `/surface`, `/stress-test`, `/scenario`, `/compare`, `/deepen`, `/prune`, `/rollback`, `/catalyst`.
-->

# `_hot.md` Compression & Budget Contract

> **Why this exists**: the prior 2,000-word hard cap with unspecified compression behavior produced drift. Different skills compressed different sections with different heuristics; compaction lost high-signal context (conviction rationales, drift flags) while preserving low-signal context (old sync archive entries). This contract specifies per-section compression policy and a soft/hard cap pair so compaction pressure is visible and actionable.
>
> **2026-04-20 cap raise**: soft cap moved from 2,000 → **4,000** and hard cap from 2,500 → **5,000** to accommodate richer session context without triggering compression during normal work. Per-section budget shares (percent of soft cap) unchanged; absolute word counts scale accordingly.

## Section budget table

Total soft cap: **4,000 words**. Total hard cap: **5,000 words**.

| Section | Budget share | Compression policy |
|---|---|---|
| `## Active Research Thread` | 30% (1,200 words soft) | Verbatim entries from the last 48 hours. Older entries compressed to one-line summaries: `*Previous YYYY-MM-DD:* [topic] — [outcome]`. Max 5 `*Previous:*` lines; drop oldest when exceeded. |
| `## Latest Sync` | 15% (600 words soft) | Verbatim. Replaced entirely on each `/sync`. Never compressed within; if over budget alone, shorten the per-thesis bullets (see 2.2). |
| `## Sync Archive` | 20% (800 words soft) | Max 3 archived entries. **Never truncate an individual entry**; when over budget, DROP the oldest entry entirely (preserves audit integrity of what remains). |
| `## Recent Conviction Changes` | 15% (600 words soft) | **NEVER compress.** Every conviction/status/reaffirm entry is a high-signal audit record. If this section alone exceeds its budget, raise the global soft cap warning in the skill's report rather than dropping entries. |
| `## Open Questions` | 15% (600 words soft) | Merge duplicates: same question from multiple theses collapses to one entry with `[theses: A, B, C]` token. Drop oldest only after merging has saturated. `/catalyst`-pattern entries auto-resolve via `/sync` Step 6 #5b. |
| `## Portfolio Snapshot` | 5% (200 words soft) | Regenerated fresh on each `/sync`. Never compressed-accumulated. If the computed content exceeds 200 words, truncate the generated summary to top-level counts only. |

Budget shares sum to 100% — treat as guidance when compression fires, not hard per-section quotas. A section below its soft share donates spare budget to any section over its share.

## Compression trigger order

When total word count exceeds the soft cap (4,000):

1. **Drop oldest `## Sync Archive` entry** (whole entry, not truncated). Recheck total.
2. **Drop oldest `*Previous:*` line from `## Active Research Thread`**. Recheck total.
3. **Merge duplicate `## Open Questions`** (same question body, different tickers → combine). Recheck total.
4. **Raise a warning in the skill's Step 8/Phase N report** listing which sections are over share and by how much — do NOT truncate any remaining section. Example: `⚠️ _hot.md approaching soft cap ([N] words / 4,000). Recent Conviction Changes at [M]% of share. Consider review.`

If after these steps the total still exceeds 5,000 (hard cap):

5. **Abort the skill's `_hot.md` update** with: `❌ _hot.md exceeds hard cap (5,000 words) after compression. Manual cleanup required. Either remove outdated Sync Archive entries or run /lint #35 to diagnose.`

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
