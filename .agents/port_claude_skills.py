#!/usr/bin/env python3
"""Generate the Codex-native skill tree from the canonical Claude skills.

The Claude and Codex skill formats overlap, but their invocation syntax,
frontmatter, resource layout, and tool vocabulary differ.  This generator keeps
`.claude/skills` untouched and makes `.agents/skills` reproducible.

Usage:
    python3 .agents/port_claude_skills.py
    python3 .agents/port_claude_skills.py --check
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import stat
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".claude" / "skills"
DESTINATION = ROOT / ".agents" / "skills"
CLAUDE_INSTRUCTIONS = ROOT / "CLAUDE.md"
CODEX_INSTRUCTIONS = ROOT / "AGENTS.md"

SKILL_UI = {
    "archive-callouts": (
        "Archive Callouts",
        "Archive old addressed Obsidian callouts",
        "Use $archive-callouts to sweep addressed callouts older than 180 days.",
    ),
    "assumptions": (
        "Thesis Assumptions",
        "Extract a thesis's load-bearing assumptions",
        "Use $assumptions to extract NVDA's load-bearing assumptions.",
    ),
    "brief": (
        "Investment Brief",
        "Create concise one-page investment briefs",
        "Use $brief to create a one-page investment brief for NVDA.",
    ),
    "catalyst": (
        "Catalyst Calendar",
        "Build the portfolio catalyst calendar",
        "Use $catalyst to refresh the portfolio catalyst calendar.",
    ),
    "clean": (
        "Clean Snapshots",
        "Remove stale vault snapshots safely",
        "Use $clean to review snapshots older than 180 days.",
    ),
    "compare": (
        "Compare Companies",
        "Compare companies and competitive dynamics",
        "Use $compare to compare NVDA and AMD side by side.",
    ),
    "conviction-audit": (
        "Conviction Audit",
        "Audit whether a thesis's conviction matches evidence",
        "Use $conviction-audit to check whether NVDA's conviction still matches its evidence.",
    ),
    "deepen": (
        "Deepen Thesis",
        "Deepen thesis sections and synchronize metrics",
        "Use $deepen to strengthen NVDA's Industry Context section.",
    ),
    "dependency-map": (
        "Dependency Map",
        "Map the external variables a thesis depends on",
        "Use $dependency-map to map what NVDA's bull case depends on.",
    ),
    "graph": (
        "Vault Graph",
        "Rebuild the vault dependency graph",
        "Use $graph to rebuild the vault dependency graph.",
    ),
    "ingest": (
        "Ingest Research",
        "Turn source material into research notes",
        "Use $ingest to process the files currently in _Inbox.",
    ),
    "lint": (
        "Vault Lint",
        "Audit vault structure, freshness, and links",
        "Use $lint to run a full vault health audit.",
    ),
    "macro-exposure": (
        "Macro Exposure",
        "Tag a thesis's implicit macro bets",
        "Use $macro-exposure to tag what macro bets NVDA is levered to.",
    ),
    "numbers": (
        "Refresh Numbers",
        "Refresh thesis metrics with current data",
        "Use $numbers to refresh NVDA's Key Metrics table.",
    ),
    "portfolio-snapshot": (
        "Portfolio Snapshot",
        "Publish a static snapshot of the live portfolio",
        "Use $portfolio-snapshot to publish the live portfolio tracker.",
    ),
    "prune": (
        "Prune Theses",
        "Evaluate weak theses and portfolio clutter",
        "Use $prune to identify theses that should be upgraded, monitored, or closed.",
    ),
    "rename": (
        "Rename Thesis",
        "Rename thesis files and repair references",
        "Use $rename to rename a thesis while preserving every inbound reference.",
    ),
    "retro": (
        "Investment Retro",
        "Review vault activity against market action",
        "Use $retro to review the last month of vault activity against the market.",
    ),
    "rollback": (
        "Rollback Note",
        "Restore vault notes from safe snapshots",
        "Use $rollback to list the snapshots available for NVDA.",
    ),
    "scenario": (
        "Portfolio Scenario",
        "Model macro scenarios across the portfolio",
        "Use $scenario to model an oil-price spike across the portfolio.",
    ),
    "status": (
        "Thesis Status",
        "Change thesis conviction or lifecycle status",
        "Use $status to propose changing NVDA's conviction to medium.",
    ),
    "stress-test": (
        "Stress Test Thesis",
        "Challenge an investment thesis adversarially",
        "Use $stress-test to challenge the NVDA investment thesis.",
    ),
    "surface": (
        "Surface Insights",
        "Find portfolio insights and research gaps",
        "Use $surface to find overlooked portfolio insights and research gaps.",
    ),
    "sync": (
        "Sync Research",
        "Propagate research across portfolio notes",
        "Use $sync to propagate recent research across affected vault notes.",
    ),
    "thesis": (
        "Create Thesis",
        "Build a full investment thesis note",
        "Use $thesis to build a new investment thesis for NVDA.",
    ),
    "transcript": (
        "Earnings Transcript",
        "Analyze earnings calls for thesis deltas",
        "Use $transcript to analyze NVDA's latest earnings call.",
    ),
    "value-chain": (
        "Value Chain Map",
        "Map a thesis's position in its value chain",
        "Use $value-chain to map NVDA's position in its value chain.",
    ),
}

SKILL_NAMES = tuple(SKILL_UI)
SKILL_COMMAND_RE = re.compile(
    r"(?<![A-Za-z0-9_.])/(" + "|".join(map(re.escape, SKILL_NAMES)) + r")\b"
)
SHARED_RESOURCE_RE = re.compile(
    r"(?<![A-Za-z0-9_./])_shared/([A-Za-z0-9_.-]+\.md)"
)

SCRIPT_PATHS = {
    ".claude/skills/_shared/extract_sections.py":
        ".agents/skills/_shared/scripts/extract_sections.py",
    ".claude/skills/graph/generate_graph.py":
        ".agents/skills/graph/scripts/generate_graph.py",
    ".claude/skills/ingest/verify_note.py":
        ".agents/skills/ingest/scripts/verify_note.py",
    ".claude/skills/lint/lint.py":
        ".agents/skills/lint/scripts/lint.py",
    ".claude/skills/numbers/numbers_compute.py":
        ".agents/skills/numbers/scripts/numbers_compute.py",
    ".claude/skills/portfolio-snapshot/build_snapshot.py":
        ".agents/skills/portfolio-snapshot/scripts/build_snapshot.py",
    ".claude/skills/transcript/extract_transcript_signals.py":
        ".agents/skills/transcript/scripts/extract_transcript_signals.py",
}

RATIONALE_PATHS = {
    f".claude/skills/{name}/RATIONALE.md":
        f".agents/skills/{name}/references/rationale.md"
    for name in SKILL_NAMES
}

COMPATIBILITY_REFERENCE = """# Codex Compatibility Contract

Read this contract before executing any ported vault skill.

## Invocation inputs

- `SKILL_ARGS` means the text supplied with an explicit `$skill-name` mention.
- For implicit invocation, derive `SKILL_ARGS` from the user's natural-language request.
- Codex invocation uses `$skill-name`; legacy `/skill-name` text in historical vault notes is provenance, not current invocation syntax.

## Legacy tool vocabulary

Some workflow and rationale text retains action-oriented names from Claude Code. Translate them to the tools available in the current Codex surface:

| Legacy label | Codex action |
|---|---|
| `Read` | Read the file with an available file tool or a bounded shell command such as `sed`, `cat`, or `python3`. |
| `Grep` / `Glob` | Use `rg`, `find`, shell globbing, or an equivalent search tool. |
| `Edit` | Prefer `apply_patch` for textual changes; use a deterministic script when the workflow specifies one. |
| `Write` | Create the file with `apply_patch`, a heredoc, or the specified deterministic script. |
| `Bash` / shell block | Use the available shell execution tool from the vault root. Treat separate calls as separate shells unless the runtime explicitly preserves a session. |
| `WebSearch` | Use current web search/browsing. Browse whenever the workflow requires current data. |
| `WebFetch` | Open/fetch the selected page with browsing tools; use `defuddle` or `curl` only when appropriate and allowed. |
| `Task` / `Agent` | Use Codex subagent delegation when the skill explicitly requires it. Prefer the project agents named by the skill when selectable. |

## Codex execution rules

1. Follow the root `AGENTS.md` and all higher-priority runtime instructions. The parent sandbox, approval, network, and multi-agent policies override round-trip optimizations in a skill.
2. Use vault-relative paths. Resolve all commands from the vault root.
3. Preserve every confirmation gate. Ask in the main thread and stop before mutations until the user explicitly approves.
4. Treat "parallel tool-call batch" as an optimization, not permission to violate the current tool surface. If parallel calls are unsupported, use bounded batches or a deterministic shell/script equivalent.
5. Never run concurrent writes to the same file. Combine them into one patch or serialize them, then verify the final live file.
6. After every material edit, verify the live file with a targeted read/search. Do not rely only on a patch tool's success response.
7. Respect the active agent/thread cap. Queue subagent batches when the requested fan-out exceeds available slots.
8. Delegated agents must receive the required task-local instructions explicitly. Read-only agents must not mutate vault content; only the main thread performs writes unless a skill expressly delegates its entire write-safe run.
9. Emit progress as ordinary assistant text between tool calls when a skill requires progress reporting.
10. Release any acquired vault lock on success, decline, error, or early exit. Verify lock ownership before removal.
"""

PDF_EXTRACTOR = r'''#!/usr/bin/env python3
"""Extract text from a local PDF with optional 1-indexed page ranges."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_pages(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(total))
    selected: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start_text, end_text = token.split("-", 1)
            start, end = int(start_text), int(end_text)
        else:
            start = end = int(token)
        if start < 1 or end < start or end > total:
            raise ValueError(
                f"invalid page range {token!r}; PDF contains {total} page(s)"
            )
        selected.update(range(start - 1, end))
    if not selected:
        raise ValueError("page selection is empty")
    return sorted(selected)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument(
        "--pages",
        help='1-indexed pages, for example "1-10" or "1,3,7-9"',
    )
    parser.add_argument(
        "--page-count",
        action="store_true",
        help="print the number of pages and exit",
    )
    args = parser.parse_args()

    try:
        from pypdf import PdfReader
    except ImportError:
        print(
            "pypdf is required for PDF ingestion: python3 -m pip install pypdf",
            file=sys.stderr,
        )
        return 2

    if not args.pdf.is_file():
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        return 2

    try:
        reader = PdfReader(str(args.pdf))
        total = len(reader.pages)
        if args.page_count:
            print(total)
            return 0
        indexes = parse_pages(args.pages, total)
        for index in indexes:
            text = reader.pages[index].extract_text() or ""
            print(f"\n===== PAGE {index + 1} / {total} =====\n")
            print(text.rstrip())
    except Exception as exc:
        print(f"PDF extraction failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'


def metadata_yaml(name: str) -> str:
    display_name, short_description, default_prompt = SKILL_UI[name]
    if not 25 <= len(short_description) <= 64:
        raise ValueError(f"invalid short description length for {name}")
    return "\n".join(
        [
            "interface:",
            f"  display_name: {yaml_quote(display_name)}",
            f"  short_description: {yaml_quote(short_description)}",
            f"  default_prompt: {yaml_quote(default_prompt)}",
            "",
        ]
    )


def destination_relative(source_relative: Path) -> Path:
    if source_relative.name == "RATIONALE.md" and len(source_relative.parts) == 2:
        return Path(source_relative.parts[0]) / "references" / "rationale.md"
    if source_relative.suffix == ".py":
        if source_relative.parts[0] == "_shared":
            return Path("_shared") / "scripts" / source_relative.name
        if len(source_relative.parts) == 2:
            return Path(source_relative.parts[0]) / "scripts" / source_relative.name
    return source_relative


def transform_paths_and_invocations(text: str) -> str:
    for old, new in {**SCRIPT_PATHS, **RATIONALE_PATHS}.items():
        text = text.replace(old, new)
    text = text.replace(".claude/skills/", ".agents/skills/")
    text = text.replace("CLAUDE.md", "AGENTS.md")
    text = text.replace("${CLAUDE_SESSION_ID:-unknown}", "${CODEX_THREAD_ID:-unknown}")
    text = text.replace('<claude-session-id or "unknown">', '<codex-thread-id or "unknown">')
    text = text.replace("user↔Claude", "user↔Codex")
    # Claude skills treat `_shared/...` as collection-relative shorthand. Codex
    # loads each skill from its own directory, so make those references
    # unambiguously vault-relative instead of looking for `<skill>/_shared`.
    text = SHARED_RESOURCE_RE.sub(
        lambda match: f".agents/skills/_shared/{match.group(1)}", text
    )
    text = SKILL_COMMAND_RE.sub(lambda match: f"${match.group(1)}", text)
    text = text.replace("$ARGUMENTS", "SKILL_ARGS")
    return text


def transform_tool_vocabulary(text: str) -> str:
    replacements = (
        ("WebSearches", "web searches"),
        ("WebSearch", "web search"),
        ("WebFetch", "web fetch/open"),
        ("Bash tool-calls", "shell tool calls"),
        ("Bash tool calls", "shell tool calls"),
        ("Bash tool-call", "shell tool call"),
        ("Bash tool call", "shell tool call"),
        ("Bash tool", "shell tool"),
        ("Bash blocks", "shell blocks"),
        ("Bash block", "shell block"),
        ("Bash loop", "shell loop"),
        ("Bash probe", "shell probe"),
        ("Bash+awk", "shell+awk"),
        ("Bash `echo`", "shell `echo`"),
        ("Bash echo", "shell echo"),
        ("Read tool call", "file-read call"),
        ("Read tool", "file-reading tool"),
        ("Edit tool calls", "patch operations"),
        ("Edit tool call", "patch operation"),
        ("Edit tool returned error", "patch operation returned an error"),
        ("Edit outcome", "patch outcome"),
        ("Edit-return inspection — no re-read", "targeted live-file verification"),
        ("Edit-return inspection", "targeted live-file verification"),
        ("Edit-return content", "targeted verification output"),
        ("Edit-return", "targeted verification"),
        ("already in allowed-tools", "already used by this workflow"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    text = text.replace("`Bash`", "`shell`")
    return text


def replace_section(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?(?=" + re.escape(end) + r")", re.S)
    updated, count = pattern.subn(replacement.rstrip() + "\n\n", text, count=1)
    if count != 1:
        raise ValueError(f"could not replace section beginning {start!r}")
    return updated


def adapt_subagent_workflows(name: str, body: str) -> str:
    if name == "deepen":
        body = re.sub(
            r"Dispatch agents \(via `Task`\).*?(?=\n### BM-4:)",
            """Dispatch Codex subagents with the available delegation tool to run **MS-1 → MS-4 only** (resolve, Tier-1 current values from the refreshed Key Metrics table, scan in-scope sections, cluster + materiality) and return a COMPACT report. Prefer the project `vault_readonly` agent when agent selection is available. Non-negotiable guardrails:
- **≤2 theses per agent, and detection-ONLY — NO drafted rewrites in-agent.** Three big theses + verbatim clauses + full rewrites overflowed prior output limits. The verbose deliverable (verbatim anchor clause + re-derived rewrite per location) is the caller's job in BM-5, not the agent's.
- **Hard output cap (<500 words/agent).** Quote only the single stale sentence per location; if nearing the cap, drop detail.
- **Use a read-only agent.** It must not modify vault content or runtime markers.
- **Collect only each subagent's final completion result.** Do not scrape raw thread logs or transcripts into the main context.
- **Respect the active thread cap and do not interrupt agents mid-turn.** Queue groups as needed; if a group must be re-run, wait for it to finish, then re-dispatch only the affected 1–2 tickers.
""",
            body,
            count=1,
            flags=re.S,
        )
        body = body.replace(
            "- **BM-D2. Retrieval is notification-only; `TaskOutput` on `local_agent`s is prohibited** (returns transcript, not results, and corrupts context).\n"
            "- **BM-D3. Agents are never killed mid-run;** correct sizing (≤2 theses, capped, detection-only) removes the need — and mid-run kills wedge the session stop-hook.",
            "- **BM-D2. Collect final completion results only; never import raw subagent thread logs into the main context.**\n"
            "- **BM-D3. Do not interrupt agents mid-turn;** size and queue them correctly (≤2 theses, capped, detection-only), then re-dispatch only after completion if needed.",
        )

    if name == "retro":
        body = replace_section(
            body,
            "## Execution context — subagent delegation (2026-07-08, MANDATORY)",
            "## Arguments",
            """## Execution context — Codex subagent delegation (MANDATORY)

Resolve the window in the main thread, then spawn ONE Codex subagent with the available delegation tool. Prefer the project `vault_worker` agent when selectable. Pass this skill's full instructions plus the resolved window. The subagent performs Step 0 through Phase 9, including reads, current-data web research, transcript fetches, lock handling, and the specified writes. Wait for completion and render its complete Phase 9.2 report **verbatim**; never re-summarize it or drop the Trade Ideas table.

**Mental Models gate:** Do not rely on inherited project context. Embed this text in the delegated prompt: *"Before ranking trade ideas from the narrative-price gaps, read `Mental Models/Generalist - Overview.md` + the matching `Mental Models/Industry - X.md`/`Lens - X.md` for the tickers surfacing. Apply the READING PROTOCOL — the market-vs-vault gap is a hypothesis, not a verdict; run the base-rate adversarially (most gaps close because the market is right); an inverted-bear/inverted-bull signal is a disconfirm trigger on the vault's own stance, not automatic alpha."*

**Recursion guard:** Also embed: *"You are the EXECUTOR of this skill run, not a coordinator. Do not delegate any part of this work to another subagent. Perform all reads, searches, and writes yourself, and end your final message with the complete Phase 9.2 report."*

Delegation keeps the large read/search budget out of the main context. If delegation is unavailable, run inline and preserve the same report and write contract.
""",
        )

    if name == "surface":
        body = replace_section(
            body,
            "## Execution context — subagent delegation (2026-07-08, MANDATORY)",
            "## Step 0: Pre-flight (MANDATORY — runs before Scope Resolution)",
            """## Execution context — Codex subagent delegation (MANDATORY)

The MAIN THREAD resolves scope first, then spawns ONE Codex subagent with the available delegation tool. Prefer the project `vault_worker` agent when selectable. Pass this skill's full instructions plus the resolved scope. The subagent performs Step 0 through Phase 4, including reads, analysis, lock handling, and the specified Research-note and `_hot.md` writes. Wait for completion and render its complete user-facing report **verbatim**.

**Mental Models gate:** Do not rely on inherited project context. Embed this text in the delegated prompt: *"Before ranking any opportunity, read `Mental Models/Generalist - Overview.md` (always) + the matching `Mental Models/Industry - X.md` for sectors in scope + any relevant `Mental Models/Lens - X.md`. Apply the READING PROTOCOL — models are lenses/questions held as hypotheses, never verdicts; run the base-rate/outside view adversarially; treat agreement across models as a trigger to disconfirm, not to commit."*

**Recursion guard:** Also embed: *"You are the EXECUTOR of this skill run, not a coordinator. Do not delegate any part of this work to another subagent. Perform all reads, analysis, and writes yourself, and end your final message with the complete user-facing report."*

Delegation keeps the large read set out of the main context. If delegation is unavailable, run inline. `all` mode still requires the user's explicit request and cost acceptance.
""",
        )
        body = body.replace(
            "## Step 0: Pre-flight (MANDATORY — runs before Scope Resolution)",
            "## Step 0: Pre-flight (MANDATORY — delegated run; scope already resolved)",
        )

    if name == "prune":
        body = replace_section(
            body,
            "## Execution context — split delegation (2026-07-08, MANDATORY)",
            "## Scope Resolution",
            """## Execution context — Codex split delegation (MANDATORY)

`$prune` splits the read-heavy analysis from the approval-gated mutation phase.

**ANALYSIS HALF — one read-only Codex subagent:**
1. Parse `SKILL_ARGS` and acquire the `.vault-lock.readonly` lock in the MAIN THREAD. The main thread owns and later releases this runtime marker so the delegated agent can remain physically read-only.
2. Spawn ONE subagent with the available delegation tool, preferring project agent `vault_readonly` when selectable. Pass the resolved scope, this skill's full instructions, and tell it to run Phase 0.0.2 + Phase 0 + Phases 1–4 only.
3. Embed the Mental Models gate: *"Before judging any thesis for upgrade/monitor/close, read `Mental Models/Generalist - Overview.md` + the matching `Mental Models/Industry - X.md`/`Lens - X.md` for the candidates' sectors. Apply the READING PROTOCOL — a kill/keep call is a hypothesis; run the base-rate adversarially (stale ≠ wrong; a quiet thesis may still be right); read each candidate's own `## Mental Models` disconfirming check before recommending closure."*
4. Embed the recursion guard: *"You are the EXECUTOR of this analysis run, not a coordinator. Do not delegate further. Perform all reads and analysis yourself and return the three required items."*
5. Require exactly: (a) `PREFLIGHT-OK` or `PREFLIGHT-BLOCKED: <rename-marker | first-run | unsynced-research>` with details; (b) the full Phase 4 report; (c) a compact execution plan containing `closures`, `upgrades`, and `affected_sectors` as specified below.
6. Wait for the final completion result, then release the read-only lock in the main thread.

For `unsynced-research` or `first-run`, an approved override must be passed to the fresh analysis subagent as `PREFLIGHT_OVERRIDE: <condition> approved YYYY-MM-DD`. A rename marker is never overridable.

**MUTATION HALF — main thread only:** Render the Phase 4 report verbatim, run the Phase 5 approval gate, acquire the vault-wide write lock, re-read only the approved mutation targets, and execute the full Phase 5 Atomic Batch. Delegated agents never perform these writes. If Codex subagents are unavailable, run the analysis inline under the same read-only/write-lock split.
""",
        )
        body = body.replace(
            "**Under split delegation (see Execution context):** the analysis subagent holds a `read-only` lock (`.vault-lock.readonly`) for Phase 0.0.2 + Phase 0 + Phase 1–4; the **main thread** acquires the `vault-wide` write lock here at the **start of Phase 5**, immediately before the first destructive stage, and releases it in the final Phase 5 block. (Inline-fallback mode without delegation: acquire the `vault-wide` lock at the very start as the original single-lock flow.)",
            "**Under split delegation (see Execution context):** the MAIN THREAD holds `.vault-lock.readonly` while the read-only subagent runs Phase 0.0.2 + Phase 0 + Phases 1–4, then releases it. The main thread acquires the `vault-wide` write lock at the start of Phase 5, immediately before the first destructive stage, and releases it in the final Phase 5 block. In inline fallback, preserve the same two-stage lock sequence.",
        )
        body = body.replace(
            "`vault-wide` scope per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout 15 min (large portfolios are slow). Capture token, verify (Procedure 1.5) every block, release in final.",
            "Use `read-only` scope for the delegated analysis and `vault-wide` scope for Phase 5, per `.claude/skills/_shared/preflight.md` Procedure 1. Timeout 15 min (large portfolios are slow). Capture each token, verify ownership (Procedure 1.5) every block, and release it at the end of its stage.",
        )

    return body


def adapt_pdf_workflow(name: str, body: str) -> str:
    if name != "ingest":
        return body
    old = (
        "   - `.pdf` files: Read with the Read tool (it handles PDFs natively). "
        "For PDFs over 10 pages, read in chunks using the `pages` parameter "
        "(e.g., `pages: \"1-10\"`, then `pages: \"11-20\"`). Process all chunks, "
        "then combine insights into a single research note."
    )
    new = (
        "   - `.pdf` files: run `python3 .agents/skills/ingest/scripts/extract_pdf.py "
        "\"<path>\" --page-count`, then extract text with the same script. For PDFs over "
        "10 pages, use bounded chunks such as `--pages \"1-10\"`, then `--pages "
        "\"11-20\"`. Process every chunk and combine the insights into one research note."
    )
    if old not in body:
        raise ValueError("ingest PDF workflow anchor not found")
    return body.replace(old, new)


def adapt_live_file_verification(body: str) -> str:
    body = re.sub(
        r"inspect the frontmatter-flip Edit's return value(?: in memory)?\. "
        r"The Edit tool reports success iff the replacement landed; the returned snippet "
        r"shows the post-edit frontmatter(?: region)?\.",
        "run a targeted frontmatter read against the live file after applying the patch. "
        "Do not rely only on the patch operation's success status.",
        body,
        flags=re.I,
    )
    body = body.replace(
        "inspect each sector-note Edit's return value.",
        "run a targeted read of each edited sector section in the live file.",
    )
    body = body.replace(
        "Inspect each patch operation's return value (the post-edit content snippet it emits). "
        "The Edit tool reports success iff the replacement landed, and the return value shows "
        "the new content; a separate re-read adds a round-trip without adding information.",
        "Run a targeted read of every edited live-file section. Do not rely only on the patch "
        "operation's success status; the read must show the intended new content.",
    )
    body = body.replace(
        "Re-reads are only required if an targeted verification is genuinely ambiguous "
        "(e.g., the replacement context was truncated in the tool's response); in that case, "
        "issue a targeted section Read — not a full-file Read.",
        "Keep verification targeted to the edited section or frontmatter; do not re-read the full file.",
    )
    body = body.replace(
        "because verification is in-memory targeted live-file verification (no Read round-trip)",
        "after the required targeted live-file verification",
    )
    body = body.replace(
        "Inspect the 7.5b patch operation's return value. The Edit tool reports success iff "
        "the replacement landed; the return value shows the post-edit frontmatter snippet.",
        "Run a targeted frontmatter read against the live manifest after the 7.5b patch.",
    )
    body = body.replace("the Edit tool returned an error", "the patch operation returned an error")
    body = body.replace("lock-release Bash", "lock-release shell block")
    return body


def parse_frontmatter(text: str) -> tuple[str, str, str]:
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not match:
        raise ValueError("SKILL.md has invalid frontmatter")
    frontmatter = match.group(1)
    name_match = re.search(r"^name:\s*(.+?)\s*$", frontmatter, re.M)
    description_match = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.M)
    if not name_match or not description_match:
        raise ValueError("SKILL.md is missing name or description")
    name = name_match.group(1).strip().strip('"')
    description = description_match.group(1).strip()
    body = text[match.end():]
    return name, description, body


def transform_skill(text: str, expected_name: str) -> str:
    name, description, body = parse_frontmatter(text)
    if name != expected_name:
        raise ValueError(f"skill folder/name mismatch: {expected_name} != {name}")
    if name not in SKILL_UI:
        raise ValueError(f"missing UI metadata for {name}")

    description = transform_paths_and_invocations(description)
    body = adapt_subagent_workflows(name, body)
    body = adapt_pdf_workflow(name, body)
    body = transform_paths_and_invocations(body)
    body = re.sub(
        r"(?<![A-Za-z0-9_./])RATIONALE(?=\s*§)",
        f"`.agents/skills/{name}/references/rationale.md`",
        body,
    )
    body = transform_tool_vocabulary(body)
    body = adapt_live_file_verification(body)

    preamble = (
        f"**Codex execution:** Read `.agents/skills/_shared/codex-compat.md` first. "
        f"Treat `SKILL_ARGS` as the arguments supplied with `$%s`, or infer them from "
        f"the user's request when this skill is invoked implicitly.\n\n" % name
    )
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "---\n\n"
        + preamble
        + body.lstrip()
    )


def transform_resource(text: str) -> str:
    text = transform_paths_and_invocations(text)
    text = transform_tool_vocabulary(text)
    text = text.replace(
        "Claude Code's shell tool is stateless — shell state (including `trap` handlers) "
        "does NOT persist across shell tool invocations. Each shell block runs in a fresh "
        "subshell.",
        "Treat Codex shell calls as stateless unless the runtime explicitly continues the same "
        "shell session — shell state (including `trap` handlers) does NOT persist across separate "
        "calls. Each independent shell block may run in a fresh subshell.",
    )
    text = text.replace(
        "(Bash / Read / Edit / Write)",
        "(shell / file-read / patch / file-write)",
    )
    text = text.replace(
        "Claude Code's shell tool is stateless — each block is a fresh subshell with "
        "different `$$`.",
        "Treat independent Codex shell calls as fresh subshells with different `$$`.",
    )
    text = text.replace("which implies Claude was wrong", "which implies the assistant was wrong")
    text = text.replace(
        "stress-test RATIONALE",
        "`.agents/skills/stress-test/references/rationale.md`",
    )
    text = text.replace(
        'SKILLS = VAULT / ".claude" / "skills"',
        'SKILLS = VAULT / ".agents" / "skills"',
    )
    # Codex places bundled executables one level deeper under scripts/.
    text = text.replace(
        'VAULT = Path(__file__).resolve().parents[3]',
        'VAULT = Path(__file__).resolve().parents[4]',
    )
    text = text.replace(
        'os.path.join(_here, "..", "..", "..")',
        'os.path.join(_here, "..", "..", "..", "..")',
    )
    text = text.replace(
        'skip = {".git", ".obsidian", ".claudian", ".claude", ".data"}',
        'skip = {".git", ".obsidian", ".claudian", ".claude", ".agents", '
        '".codex", ".data"}',
    )
    return text


def transform_agents_instructions(text: str) -> str:
    """Create Codex's repository instructions from the canonical vault rules."""
    text = transform_paths_and_invocations(text)
    text = transform_tool_vocabulary(text)
    text = text.replace("Claude addresses", "Codex addresses")
    text = text.replace("Claude's analytical reply", "Codex's analytical reply")
    text = text.replace("user-Claude exchange", "user-Codex exchange")
    text = text.replace("Claude re-addresses", "Codex re-addresses")
    text = text.replace('ask Claude to "address fresh callouts', 'ask Codex to "address fresh callouts')
    text = text.replace("Claude edits sections", "Codex edits sections")
    text = text.replace(
        "- `AGENTS.md` — system instructions; structural changes need explicit ask\n",
        "- `AGENTS.md` — Codex system instructions; generated structural changes need explicit ask\n"
        "- `CLAUDE.md` — canonical cross-agent vault instructions; edit only when asked\n",
    )
    text = text.replace(
        "- `.agents/skills/` — skill definitions; edit only when asked\n",
        "- `.agents/skills/` — generated Codex skill definitions; edit only when asked\n"
        "- `.claude/skills/` — canonical Claude skill definitions; edit only when asked\n",
    )
    text = re.sub(
        r"11\. \*\*Skill-content truncation safeguard\*\*.*?One extra Read at Step 0 "
        r"eliminates this failure class at negligible cost\.",
        "11. **Skill-content loading safeguard** — before any write phase, read the full "
        "`.agents/skills/<skill>/SKILL.md` whenever the workflow arrived as metadata only, a "
        "partial excerpt, or text containing a truncation marker. Never reconstruct missing "
        "steps from memory. Long skills (`$sync`, `$status`, `$deepen`, `$compare`, `$thesis`, "
        "`$rollback`) contain late-stage safety gates that must be loaded from disk before mutation.",
        text,
        count=1,
        flags=re.S,
    )
    return (
        "<!-- Generated from CLAUDE.md by .agents/port_claude_skills.py. "
        "Edit the canonical source, then regenerate. -->\n\n"
        + text
    )


def build_expected() -> dict[Path, tuple[bytes, int]]:
    if not SOURCE.is_dir():
        raise FileNotFoundError(f"source skill directory not found: {SOURCE}")

    expected: dict[Path, tuple[bytes, int]] = {}
    discovered_skills: set[str] = set()
    for source_path in sorted(path for path in SOURCE.rglob("*") if path.is_file()):
        source_relative = source_path.relative_to(SOURCE)
        destination_relative_path = destination_relative(source_relative)
        raw = source_path.read_bytes()
        mode = stat.S_IMODE(source_path.stat().st_mode)

        if source_path.name == "SKILL.md":
            skill_name = source_relative.parts[0]
            discovered_skills.add(skill_name)
            content = transform_skill(raw.decode("utf-8"), skill_name).encode("utf-8")
        elif source_path.suffix in {".md", ".py"}:
            content = transform_resource(raw.decode("utf-8")).encode("utf-8")
        else:
            content = raw
        expected[destination_relative_path] = (content, mode)

    if discovered_skills != set(SKILL_UI):
        missing = sorted(set(SKILL_UI) - discovered_skills)
        extra = sorted(discovered_skills - set(SKILL_UI))
        raise ValueError(f"skill inventory mismatch; missing={missing}, extra={extra}")

    expected[Path("_shared/codex-compat.md")] = (
        COMPATIBILITY_REFERENCE.encode("utf-8"),
        0o644,
    )
    expected[Path("ingest/scripts/extract_pdf.py")] = (
        PDF_EXTRACTOR.encode("utf-8"),
        0o755,
    )
    for name in SKILL_NAMES:
        expected[Path(name) / "agents" / "openai.yaml"] = (
            metadata_yaml(name).encode("utf-8"),
            0o644,
        )
    return expected


def write_tree(expected: dict[Path, tuple[bytes, int]]) -> None:
    staging = DESTINATION.parent / ".skills-port-staging"
    if staging.exists() or staging.is_symlink():
        if staging.is_dir() and not staging.is_symlink():
            shutil.rmtree(staging)
        else:
            staging.unlink()
    staging.mkdir(parents=True)

    for relative, (content, mode) in sorted(expected.items(), key=lambda item: str(item[0])):
        target = staging / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        os.chmod(target, mode)

    if DESTINATION.is_symlink() or (DESTINATION.exists() and not DESTINATION.is_dir()):
        DESTINATION.unlink()
    elif DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    staging.replace(DESTINATION)


def write_agents_instructions(content: bytes) -> None:
    if CODEX_INSTRUCTIONS.is_symlink() or (
        CODEX_INSTRUCTIONS.exists() and not CODEX_INSTRUCTIONS.is_file()
    ):
        CODEX_INSTRUCTIONS.unlink()
    CODEX_INSTRUCTIONS.write_bytes(content)
    os.chmod(CODEX_INSTRUCTIONS, 0o644)


def check_tree(expected: dict[Path, tuple[bytes, int]]) -> list[str]:
    errors: list[str] = []
    if DESTINATION.is_symlink():
        return [f"{DESTINATION.relative_to(ROOT)} is still a symlink"]
    if not DESTINATION.is_dir():
        return [f"{DESTINATION.relative_to(ROOT)} does not exist"]

    actual_paths = {
        path.relative_to(DESTINATION)
        for path in DESTINATION.rglob("*")
        if path.is_file()
    }
    expected_paths = set(expected)
    for path in sorted(expected_paths - actual_paths, key=str):
        errors.append(f"missing: {path}")
    for path in sorted(actual_paths - expected_paths, key=str):
        errors.append(f"unexpected: {path}")
    for path in sorted(expected_paths & actual_paths, key=str):
        expected_content, expected_mode = expected[path]
        actual = DESTINATION / path
        if actual.read_bytes() != expected_content:
            errors.append(f"content drift: {path}")
        if stat.S_IMODE(actual.stat().st_mode) != expected_mode:
            errors.append(f"mode drift: {path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift without writing",
    )
    args = parser.parse_args()

    try:
        expected = build_expected()
        if not CLAUDE_INSTRUCTIONS.is_file():
            raise FileNotFoundError(f"canonical instructions not found: {CLAUDE_INSTRUCTIONS}")
        agents_content = transform_agents_instructions(
            CLAUDE_INSTRUCTIONS.read_text(encoding="utf-8")
        ).encode("utf-8")
        if args.check:
            errors = check_tree(expected)
            if CODEX_INSTRUCTIONS.is_symlink():
                errors.append("AGENTS.md is still a symlink")
            elif not CODEX_INSTRUCTIONS.is_file():
                errors.append("AGENTS.md is missing")
            elif CODEX_INSTRUCTIONS.read_bytes() != agents_content:
                errors.append("content drift: AGENTS.md")
            if errors:
                for error in errors:
                    print(f"ERROR: {error}")
                return 1
            print(f"Codex skill port is current ({len(SKILL_NAMES)} skills).")
            return 0
        write_tree(expected)
        write_agents_instructions(agents_content)
        print(
            f"Ported {len(SKILL_NAMES)} skills and {len(expected)} files "
            f"from {SOURCE.relative_to(ROOT)} to {DESTINATION.relative_to(ROOT)}; "
            "regenerated AGENTS.md."
        )
        return 0
    except Exception as exc:
        print(f"Port failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
