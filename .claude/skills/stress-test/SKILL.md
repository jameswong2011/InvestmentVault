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

## Step 0: Pre-flight (MANDATORY — runs before Phase 1)

### 0.1: Acquire vault lock
Acquire a `ticker:TICKER` scope lock per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout budget: 5 minutes. Release via `trap` on exit.

### 0.2: Rename-marker pre-flight
Run `.claude/skills/_shared/preflight.md` Procedure 2. If `.rename_incomplete.TICKER` exists at vault root, hard-block per the contract's 2.3 collision message. Appending a stress-test Log entry and a new research note while inbound wikilinks are split between old and new names would produce audit artifacts keyed to one name while some vault references still point to the other — compounding the split.

Both checks must pass before proceeding to Phase 1.

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

### 4.1: Write the research note (without `propagated_to:`)

Save the stress test to `Research/YYYY-MM-DD - [TICKER] - Stress Test.md` with:
```yaml
---
date: YYYY-MM-DD
tags: [research, stress-test, TICKER]
sector: [from thesis]
ticker: TICKER
source: vault synthesis
source_type: stress-test
# propagated_to: omitted intentionally — set in Phase 4.4 only after Log append succeeds
---
```

> **Why omitted at write time**: mirrors `/scenario` Phase 6.1 + 6.3 atomicity. If the Log append in Phase 4.2 fails (file lock, missing `## Log` section, malformed frontmatter), writing `propagated_to: [TICKER]` here would falsely claim propagation succeeded. Future `/sync` Case 2b would then skip TICKER as already-propagated, never retrying the failed append — permanent audit gap. The all-or-nothing rule trades a single trivial frontmatter Edit at Phase 4.4 for guaranteed eventual consistency.

### 4.2: Append Log entry to thesis (track outcome)

Append a Log entry to the thesis note (max 2 lines):
```
### YYYY-MM-DD
- Stress test [[Research/YYYY-MM-DD - TICKER - Stress Test]]: [top vulnerability], X/Y assumptions rated 🔴 — conviction [unchanged/weakened: reassess + reason]
```
> **Drift coupling**: `/sync` Step 3e excludes entries starting with `"Stress test"` from drift detection. **Registry entry**: `.claude/skills/_shared/log-prefixes.md` §1. Do not change this prefix without updating the registry, `/sync`, and `/lint` check #29 will flag any drift.

Use "weakened" (not "unchanged") when any assumption is rated 🔴 — this ensures `/sync` conviction drift detection counts the entry correctly. The conviction level itself is not changed; the log wording reflects that evidence weakened the case even if the user hasn't acted yet.

**Track outcome**: capture the Edit result as `log_append_succeeded: true | false`. On success, proceed to 4.3 normally. On failure (Edit error, missing `## Log` section), do NOT abort — proceed to 4.3, but skip 4.4's `propagated_to:` write per the atomicity rule below.

### 4.3: Add to Related Research (independent of Log append outcome)

Add the stress test to the thesis's `## Related Research` section (if not already present):
```
- [[Research/YYYY-MM-DD - TICKER - Stress Test]]
```

This is a wikilink registration, not a propagation claim — runs regardless of Phase 4.2 outcome. The Related Research listing is a presence record; `propagated_to:` is the propagation contract.

### 4.4: Atomicity rule for `propagated_to:` update

**Update the research note's `propagated_to:` frontmatter only if Phase 4.2 Log append succeeded.** Mirrors the `/scenario` Phase 6.3 atomicity rule.

- **Log append succeeded** (`log_append_succeeded: true`): edit the research note's frontmatter to add `propagated_to: [TICKER]`. Insertion point: immediately before the closing `---` of frontmatter. This signals to subsequent `/sync` runs that producer-side propagation is complete; `/sync` Case 2b will skip TICKER as already-propagated.
- **Log append failed** (`log_append_succeeded: false`): do **NOT** write `propagated_to:` at all. Leave the frontmatter without the field. The next `/sync` (default mode) will detect TICKER via the file-direct fallback (research note's `ticker: TICKER` frontmatter), apply the per-thesis idempotency check (today's date entry referencing this note? no), and retry the Log append.

> **Why never partial**: matches `/scenario` Phase 6.3 rationale — a partial `propagated_to:` would create a permanent audit gap that future `/sync` runs silently skip because the dedup hint says "already done." For single-ticker `/stress-test`, the partial case is binary (either present-with-TICKER or absent), but the rule is the same: omit on failure, write only on success.

### 4.5: Conviction unchanged (manual decision)

Do NOT change the conviction level — flag it for the user to decide via `/status TICKER conviction old→new [rationale]`.

> **Graph update deferred**: `_graph.md` is now owned exclusively by `/graph`. After this skill, run `/graph last` to register the stress test research note in the dependency map.

## Phase 5: Update _hot.md

Follow `.claude/skills/_shared/hot-md-contract.md` for all _hot.md writes. Read `_hot.md` then edit (do NOT touch Latest Sync or Sync Archive — owned by `/sync`):

1. **Active Research Thread**: **Same-ticker continuation** — if the current thread already covers the same primary ticker/topic, append a dated line (`YYYY-MM-DD: [update]`) to the existing thread instead of compressing. **New topic**: compress the outgoing thread into a single `*Previous:*` entry (date + one-phrase summary). Write: stress tested [TICKER], top vulnerability found, and whether conviction reassessment was flagged. Append `*Previous:*` line(s) — max 5, drop oldest.
2. **Recent Conviction Changes**: Add entry if conviction reassessment was flagged (note: conviction not changed, flagged for user)
3. **Open Questions**: Add any critical research gaps or unanswered questions the stress test exposed

**Word cap**: After all `_hot.md` edits, check total word count. If over 2,000 words, prune `## Sync Archive` entries (oldest first), then `*Previous:*` lines in Active Research Thread (oldest first), until under cap.

## Phase 6: Report
Present findings directly to the user. Lead with the scariest finding. End with a clear verdict: "This thesis survives stress testing" or "This thesis has N critical vulnerabilities that need resolution before conviction can be maintained."

Include in the report:
- **Research note**: `[[Research/YYYY-MM-DD - TICKER - Stress Test]]`
- **Log append**: `succeeded` | `failed (reason — next /sync will retry via file-direct fallback)`
- **`propagated_to:` frontmatter**: `set ([TICKER])` | `omitted (Log append failed — next /sync will retry)`

**Run `/sync` to propagate stress test findings to affected sector notes and cross-thesis references.** If the Log append failed, `/sync` will additionally retry the append via file-direct fallback (research note's `ticker: TICKER` resolves to the thesis, today's-date idempotency check passes since no entry was written, and the Log entry lands on retry).
