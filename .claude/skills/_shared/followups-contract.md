# Open-Findings Register Contract (`_followups.md`)

Consumed by: **writers** — `/stress-test`, `/retro`, `/surface`, `/numbers` (any skill that emits an actionable recommendation it cannot itself execute); **resolvers** — `/status`, `/sync`.
Owned by: **shared append/resolve** — no single skill owns the file. Every writer appends; the two resolvers mark entries done. Distinct from `_hot.md` (which compresses and evicts) — `_followups.md` is a durable ledger.
Governs: the `_followups.md` register at vault root — a persistent to-do list of actionable findings surfaced by analytical skills, so a recommendation ("reassess NVDA HIGH→medium") survives past the run that produced it.

## Why this exists

Analytical skills routinely surface actions the user should take next — a stress-test concluding "conviction should drop," a retro flagging a trade idea, a surface run finding an opportunity, a numbers refresh crossing a conviction trigger. Today these die in the research note or chat report that produced them. `_hot.md` cannot serve as the backstop: its compression contract evicts Open-Questions cohorts after 14 days and roster-compresses conviction entries after 30. A recommendation that needs three weeks to act on is gone before it is actioned. The INTU stress-test that concluded "reassess HIGH→medium" and sat unactioned is the exact failure this register closes.

`_followups.md` is the durable layer: findings persist until a resolver marks them done or the user dismisses them.

## File schema

Vault root, `_followups.md`. Auto-created by the first writer if absent.

```markdown
---
date: YYYY-MM-DD
tags: [meta, followups]
---
# Open Findings Register

## Open
<!-- newest first; each entry one line -->

## Resolved
<!-- newest first; entries moved here by resolvers, retained 90 days then eligible for /clean -->
```

### Entry format (one line, in `## Open`)

```
- [ ] YYYY-MM-DD · <skill> · [[Theses/TICKER - Name]] · <finding> → <resolve-when> · src [[Research/…]] | chat
```

- **date** — when the finding was raised.
- **skill** — the producer (`stress-test`, `retro`, `surface`, `numbers`).
- **thesis wikilink** — the affected thesis (or `portfolio` for cross-ticker findings).
- **finding** — the actionable claim, ≤ 20 words, lead with the action (`reassess conviction HIGH→medium`, `investigate flow-bull divergence`, `GM crossed → LOW trigger`).
- **resolve-when** — the observable/action that closes it (`user runs /status or dismisses`, `next earnings confirms`, `absorbed into thesis via /deepen`).
- **src** — provenance: the research note wikilink, or `chat` if the finding lived only in a run report.

### Resolved entry format (moved to `## Resolved`)

```
- [x] YYYY-MM-DD raised → YYYY-MM-DD resolved · <skill> · [[Theses/TICKER]] · <finding> — <outcome: actioned via /status | dismissed | absorbed | superseded>
```

## Writer responsibilities

Each writer, when it produces an actionable recommendation, appends ONE entry to `## Open` (Edit, prepend under the heading — newest first). Selectivity is the same bar as the rest of the vault: only genuinely actionable findings, never routine output.

- **`/stress-test`** — a conclusion that conviction should change, or a kill-trigger that has effectively fired. NOT every 🔴 assumption; only the run-level verdict.
- **`/retro`** — each Top-3 Trade Idea whose delta signals a vault-market mismatch requiring action (mirrors the Phase 7 `Retro insight:` Log entries; the register is the cross-run index of them).
- **`/surface`** — each surfaced opportunity that warrants a concrete next skill (`/thesis`, `/deepen`, `/ingest`).
- **`/numbers`** — a conviction-trigger CROSS per `_shared/trigger-touch.md` (Step 5b). Only crossings, not "approaching."

**Dedup (mandatory).** Before appending, grep `## Open` for an existing entry with the same thesis wikilink AND a finding of the same kind. If present, do not duplicate — update the existing entry's date if the signal re-fired, else skip. Prevents a weekly `/retro` from stacking the same idea.

**Cap.** Soft cap 50 open entries. When exceeded, the writing skill surfaces `⚠️ _followups.md over 50 open entries — review/resolve backlog` in its report; it never auto-drops open entries (unlike `_hot.md`, open findings are not evictable — that is the point).

## Resolver responsibilities

- **`/status`** — after executing a conviction/status change, grep `## Open` for entries on that thesis. Any whose finding the change satisfies (`reassess conviction` when conviction changed; `GM crossed → LOW trigger` when the matching downgrade happened) → move to `## Resolved` with outcome `actioned via /status`. Present the match in the Step 2 confirmation context so the user sees the loop closing.
- **`/sync`** — when propagating research that absorbs an open finding into a thesis body (a surface opportunity written into Bull Case; a retro divergence resolved by new evidence) → move the entry to `## Resolved` with outcome `absorbed`. Sync is the natural resolver because it is the skill that writes research conclusions into thesis spines.

Neither resolver deletes entries — they move Open→Resolved so the audit trail survives.

## Interaction with `_hot.md`

`_followups.md` and `_hot.md` `## Open Questions` overlap but differ: Open Questions are analytical prompts ("what is the market seeing?"); open findings are actionable to-dos ("run /status NVDA"). A writer may emit both — the Open Question for the thinking, the finding for the action. Do not merge them; the compression policies differ (Open Questions evict, findings persist).

## Lint coupling (future)

A `/lint` freshness check should flag `## Open` entries older than 30 days (stale to-do — either act or dismiss) and `## Resolved` entries older than 90 days (eligible for `/clean`). Until that check exists, the 50-entry soft-cap warning is the only backpressure.
