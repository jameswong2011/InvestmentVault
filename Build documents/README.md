---
date: 2026-07-19
tags: [meta, infrastructure, moc]
status: active
---

# Build Documents — Index

Meta-documentation for the vault system itself. These are not vault research content — no `/ingest`, no propagation, no thesis links; they document how the machine is built and operated.

| Doc | Role | Read when |
|---|---|---|
| [[Setup Guide]] | **Zero-to-working replication**: installs (Obsidian, Claude Code), clone, gitignored-file recreation (lift-vs-recreate tables), plugin + Claudian config, first-run bootstrap, automation-layer sequencing, verification checklist | Fresh machine, new clone, or migrating |
| [[User Guide]] | **Daily operation**: core loop, workflow chains, skill dictionary (all 21), callout system, prompt library, cadence guide, gotchas | Every day; the operating manual |
| [[INFRASTRUCTURE]] | **Consistency-machinery internals**: locks, manifests, snapshots, runtime markers, shared contracts, `/lint` registry, debugging flows. Audience: Claude Code at skill-author/debugger scope | Authoring or debugging a skill |
| [[n8n]] | **Automation layer** (live): n8n install, Telegram, credentials, watcher registry, Workflows 1–3 (price tripwires, catalyst reminders, news sweep), operations + machine migration (§5.1) | Building or operating Layer 4 |
| [[Twitter API Build]] | **Workflows 4–5** (live): X Canary + X Harvester — architecture review, click-level build cards, Code-node source, calibration runbook, decision log | Building, tuning, or debugging the X pipeline |
| [[Web UI Build Brief]] | **Spec for future work**: briefing pack for an external LLM to build a single-page vault-explainer UI. Dated 2026-05-24 — vault statistics and skill counts inside are as-of-then; predates the automation layer entirely | Commissioning the explainer UI |

## Reading order by intent

- **Replicate the whole system** → [[Setup Guide]] top-to-bottom (it sequences [[n8n]] and [[Twitter API Build]] at §8)
- **Learn to operate the vault** → [[User Guide]] §0–§5, then §11–§12 as reference
- **Understand why the machinery is safe** → [[User Guide]] §14, then [[INFRASTRUCTURE]] §0
- **Change or add a skill** → [[INFRASTRUCTURE]] §0.4 → §12, plus the skill's own `SKILL.md`/`RATIONALE.md`

## Ownership notes

- `CLAUDE.md` (vault root) is the canonical agent instruction file; `AGENTS.md` is its generated Codex mirror — edit CLAUDE.md, then regenerate via `.agents/port_claude_skills.py`.
- [[Twitter API Build]] §5 is the append-only decision log for the X pipeline; equivalent history for the core vault lives in `_Archive/Docs/Changelog.md`.
- Live tuning values for the automation layer live in `_watchers.md` (vault root), not in these docs.
