# Codex Compatibility Contract

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
