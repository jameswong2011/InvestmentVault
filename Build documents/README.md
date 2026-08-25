---
publish: false
date: 2026-07-19
tags: [meta, infrastructure, moc]
status: active
---

# Build Documents — Index

Meta-documentation for the vault system itself. These are not vault research content — no `/ingest`, no propagation, no thesis links; they document how the machine is built and operated.

| Doc | Role | Read when |
|---|---|---|
| [[Vault Explainer]] | **The system explained** (v6, 2026-08-07): LLM-wiki concept, four engines, Mental Models layer, state files, 27-skill catalogue, workflows, n8n sensory layer, safety machinery, publishing stack, FAQ, glossary | Introducing the vault to anyone (including yourself after a break) |
| [[Demo Walkthrough]] | **Scripted 3–4h live demo runbook**: pre-flight checklist, 7 acts (orientation → core loop → callouts → live Tier-3 decision → portfolio workflow → safety → publishing), contingency table | Preparing or running a demo session |
| [[Vault History - Jul-Aug 2026]] | **One month of evolution** (5 Jul → 7 Aug 2026): week-by-week infra + research timeline, conviction ledger, skill-run stats, patterns | Showing how the vault compounds; monthly review reference |
| [[Setup Guide]] | **Zero-to-working replication**: installs (Obsidian, Claude Code), clone, gitignored-file recreation (lift-vs-recreate tables), plugin + Claudian config, first-run bootstrap, automation-layer sequencing, verification checklist | Fresh machine, new clone, or migrating |
| [[User Guide]] | **Daily operation**: core loop, workflow chains, skill dictionary, callout system, prompt library, cadence guide, gotchas | Every day; the operating manual |
| [[INFRASTRUCTURE]] | **Consistency-machinery internals**: locks, manifests, snapshots, runtime markers, shared contracts, `/lint` registry, debugging flows. Audience: Claude Code at skill-author/debugger scope | Authoring or debugging a skill |
| [[Second Brain for Investing - Presentation Outline (2026-08-25)]] | **Presentation** (30 slides, 16:9, built 2026-08-25): Parts 1–2 are general (what AI can do today; how investors use it and what it fixes over a manual process; no vault content); Part 3 introduces the second brain (compiled wiki, how the notes link, context files, mental models, templates, skills, the most powerful skills, the overnight sensing layer); Part 4 is six use cases from the book plus the eight features that matter. No maintenance/plumbing content. Deck file: `Second Brain for Investing - Presentation (2026-08-25).pptx` (same folder); the outline note carries every slide's text + speaker notes and doubles as a prompt pack for regenerating the deck elsewhere | Presenting the system to a beginner/intermediate audience; adapting the laniakea.io/system material into talk form |
| [[n8n Automations]] | **Automation layer** (live): platform build (install, Telegram, credentials, watcher registry, Workflows 1–3), X intelligence (Workflows 4–5, build cards, Code-node source, calibration), operations, decision log, troubleshooting | Building, tuning, or operating Layer 4 |
| [[_Archive/Web UI Build Brief\|Web UI Build Brief]] (archived) | **Spec for past/future work**: briefing pack for an external LLM to build a single-page vault-explainer UI. Dated 2026-05-24, moved to `_Archive/` — statistics inside predate the automation layer entirely | Commissioning the explainer UI |

Known drift in the older docs (as of 2026-08-07): Setup Guide and INFRASTRUCTURE/User Guide cite 21/26 skills respectively (actual: 27 — `/portfolio-snapshot` added 2026-08-04 is undocumented in all of them); Setup Guide has no coverage of the hooks/scheduler/workflows layer; n8n Automations still labels Workflow 3 "In build" though News Briefs have shipped daily since 2026-07-28.

## Reading order by intent

- **Replicate the whole system** → [[Setup Guide]] top-to-bottom (it sequences [[n8n Automations]] at §8)
- **Learn to operate the vault** → [[User Guide]] §0–§5, then §11–§12 as reference
- **Understand why the machinery is safe** → [[User Guide]] §14, then [[INFRASTRUCTURE]] §0
- **Change or add a skill** → [[INFRASTRUCTURE]] §0.4 → §12, plus the skill's own `SKILL.md`/`RATIONALE.md`

## Ownership notes

- `CLAUDE.md` (vault root) is the canonical agent instruction file; `AGENTS.md` is its generated Codex mirror — edit CLAUDE.md, then regenerate via `.agents/port_claude_skills.py`.
- The n8n decision log (X pipeline + workflow history) lives in [[_Archive/Docs/2026-07-20 - n8n Automations (pre-restructure)]] §11 — archived out of the working doc in the 2026-07-20 restructure; equivalent history for the core vault lives in `_Archive/Docs/Changelog.md`.
- Live tuning values for the automation layer live in `_watchers.md` (vault root), not in these docs.
