---
name: stress-test
description: Adversarial thesis testing — act as a short seller to find the weakest points in a thesis. Use when user says "stress test", "devil's advocate", "challenge this thesis", or "break [TICKER]".
model: opus
effort: max
allowed-tools: Read Grep Glob Edit Write WebSearch WebFetch Bash(date * defuddle *)
---

**Follow CLAUDE.md Writing Standards strictly.** No hedge words, no qualifiers, no softening. Dense, specific, evidence-backed.

Perform an adversarial stress test on a thesis. Your job is to find reasons this investment FAILS. Do not be balanced — be a prosecutor building the strongest possible case against the position.

## Arguments
$ARGUMENTS should be a ticker (e.g., "NVDA") or a thesis name. If empty, ask the user which thesis to stress test.

## Phase 1: Load the Thesis and All Supporting Evidence
1. Read the thesis note from Theses/
2. Read EVERY research note linked from the thesis (Related Research + Log entries)
3. Read the relevant Sector Note for competitive context
4. Read any Macro notes referenced or relevant to the sector
5. Grep the vault for the ticker to catch any mentions in other notes the thesis doesn't link to

## Phase 2: Internal Contradiction Scan
Look specifically for:
- Does the Bull Case rely on assumptions that the Bear Case or Risks section already contradicts?
- Do research notes contain data points that undermine the Non-consensus Insights?
- Has the competitive landscape shifted since the thesis was last updated? (Check research note dates vs thesis Log dates)
- Are the Key Metrics internally consistent? (e.g., high revenue growth + high FCF yield is rare — is the company sacrificing one for the other?)
- Does the conviction level match the strength of evidence? (High conviction with thin research = red flag)
- Are Outstanding Questions still unanswered? If yes, how can conviction be high?
- Are existing Conviction Triggers well-defined? Do they cover the actual failure modes, or are the real risks outside the trigger framework? A thesis with vague triggers ("if competition increases") has a hidden vulnerability — it can degrade without ever formally triggering a reassessment.

## Phase 3: Build the Short Case
Structure as a short seller would pitch to an investment committee:

1. **Thesis Vulnerability Summary** — One paragraph: the single biggest reason this investment fails
2. **Evidence Against** — 3-5 points, each citing specific data from vault notes:
   - Market structure risks the thesis underweights
   - Competitive threats documented in sector note but not reflected in thesis
   - Macro sensitivities that are unhedged
   - Financial assumptions that don't hold under stress
   - Management or execution risks
3. **Assumption Stress Table**:

| Bull Assumption | What Must Be True | Evidence For | Evidence Against | Fragility |
|---|---|---|---|---|
| [from thesis] | [specific condition] | [cite vault note] | [cite vault note or gap] | 🟢🟡🔴 |

4. **Research Gaps** — What does the thesis NOT know that it needs to? Which Outstanding Questions remain unanswered? What data would a serious short seller have that this vault doesn't?
5. **Kill Trigger** — What single observable event would invalidate the thesis? Be specific and falsifiable (not "competition increases" but "[COMPANY X] launches [PRODUCT Y] at [PRICE Z] by [DATE]")

## Phase 4: Update the Vault
1. Save the stress test to `Research/YYYY-MM-DD - [TICKER] - Stress Test.md` with:
   ```yaml
   ---
   date: YYYY-MM-DD
   tags: [research, stress-test, TICKER]
   sector: [from thesis]
   ticker: TICKER
   source: vault synthesis
   source_type: stress-test
   propagated_to: [TICKER]
   ---
   ```
2. Append a Log entry to the thesis note (max 2 lines):
   ```
   ### YYYY-MM-DD
   - Stress test [[Research/YYYY-MM-DD - TICKER - Stress Test]]: [top vulnerability], X/Y assumptions rated 🔴 — conviction [unchanged/weakened: reassess + reason]
   ```
   > **Drift coupling**: `/sync` Step 3e excludes entries starting with `"Stress test"` from drift detection. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §1. Do not change this prefix without updating the registry, `/sync`, and `/lint` check #29 will flag any drift.

   Use "weakened" (not "unchanged") when any assumption is rated 🔴 — this ensures `/sync` conviction drift detection counts the entry correctly. The conviction level itself is not changed; the log wording reflects that evidence weakened the case even if the user hasn't acted yet.
3. Add the stress test to the thesis's `## Related Research` section (if not already present):
   ```
   - [[Research/YYYY-MM-DD - TICKER - Stress Test]]
   ```
4. Do NOT change the conviction level — flag it for the user to decide

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the stress test research note in the dependency map.

## Phase 5: Update _hot.md

Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: stress tested [TICKER], top vulnerability found, and whether conviction reassessment was flagged. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry if conviction reassessment was flagged (note: conviction not changed, flagged for user)
3. **Open Questions**: Add any critical research gaps or unanswered questions the stress test exposed

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Phase 6: Report
Present findings directly to the user. Lead with the scariest finding. End with a clear verdict: "This thesis survives stress testing" or "This thesis has N critical vulnerabilities that need resolution before conviction can be maintained."

**Run `/sync` to propagate stress test findings to affected sector notes and cross-thesis references.**
