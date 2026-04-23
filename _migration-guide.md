---
date: 2026-04-20
tags: [meta, migration]
---

# Mac Migration Guide

All steps run on the **new Mac**. Order matters:

- **Git** is the canonical source for skills (`.claude/`), CLAUDE.md, and all tracked notes
- **Obsidian Sync** tops it off with anything not yet committed: recent notes, attachments, `.obsidian/plugins/*`

Obsidian Sync alone is **not enough**. It hard-excludes `.git/` and every top-level hidden folder that isn't `.obsidian/` — including `.claude/`. Skip the git clone and you end up with empty `.claude/skills/`, no git history, broken slash commands. There is no Obsidian Sync toggle that fixes this.

Assumes:
- New Mac vault path matches old Mac path (Obsidian remembers paths by exact match)
- Old Mac is not needed during setup

---

## Step 0 — Clone the vault from Git (before opening Obsidian)

Fresh Macs ship without git. Trigger Xcode Command Line Tools (CLT) install — this gets you git without needing Homebrew yet:

```bash
xcode-select --install
```

Click through the GUI dialog and wait for it to finish. If the dialog errors out with "not currently available from the update server," jump to the CLT troubleshooting section at the end of Step 1, fix it, then come back.

Once git is available, clone the vault:

```bash
git clone git@github.com:<your-user>/<your-repo>.git ~/InvestmentVault
```

Match the path to the old Mac's vault path exactly.

**Do not open Obsidian yet.** If Obsidian Sync is already running and you open the app before the clone completes, Obsidian will create the vault folder itself and race the clone. Clone first, open Obsidian second — it will see the existing folder and layer synced content (notes, attachments) on top of the git-tracked content (skills, CLAUDE.md).

Verify:
```bash
cd ~/InvestmentVault
git status                    # on main, clean
ls .claude/skills/ | head     # should list /sync, /ingest, /graph, /lint, etc.
```

If `.claude/skills/` is empty, the clone didn't work — investigate before continuing.

---

## Step 1 — Install the stack

Run each sub-step **in order**, wait for each to finish before starting the next.

### 1a — Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Takes 3–10 minutes. When it finishes, it prints something like:

```
==> Next steps:
- Run these commands in your terminal to add Homebrew to your PATH:
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/YOU/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 1b — Add Homebrew to PATH

Copy the two `echo` / `eval` lines Homebrew printed above and run them. If you missed them, use these (pick the right one for your chip):

**Apple Silicon (M1/M2/M3/M4)**:
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**Intel Mac**:
```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

Confirm:
```bash
brew --version
```

### 1c — Install Node.js and Git LFS via Homebrew

```bash
brew install node git-lfs
```

Confirm:
```bash
node --version
npm --version
```

### 1d — Install Claude Code and Defuddle CLI via npm

```bash
npm install -g @anthropic-ai/claude-code defuddle-cli
```

Confirm:
```bash
claude --version
defuddle --version
```

`defuddle-cli` is the web-content extractor the vault skills shell out to via `Bash(defuddle *)` clauses (used by `/ingest`, `/deepen`, `/catalyst`, `/surface`, `/compare`, `/thesis`). It's an npm CLI, not a Claude Code plugin — no marketplace step needed.

### 1e — Verify everything at once

```bash
brew --version && node --version && npm --version && claude --version && defuddle --version
```

All five should print a version number. If any says `command not found`, that sub-step failed — re-run it or check the troubleshooting section below.

### If Homebrew install fails

#### Error: "not currently available from the update server" (Xcode Command Line Tools)

Homebrew requires Xcode Command Line Tools (CLT) — git, compilers, headers. On a fresh Mac, Homebrew triggers `xcode-select --install` which pops a GUI dialog that fetches CLT from Apple's update server. That server is flaky and often returns this error.

**Before trying to fix**, verify two things:

```bash
# System date must be correct — SSL certs fail if clock is skewed
date
```
If wrong: System Settings → General → Date & Time → enable "Set time and date automatically."

Also: System Settings → Apple ID → must be signed in. Silent failures happen when not signed in.

**Fix 1 — Retry from terminal** (fastest, often works):

```bash
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
```

Second attempt often succeeds because the request reset server-side state.

**Fix 2 — Manual download from Apple** (most reliable):

1. Open [developer.apple.com/download/all](https://developer.apple.com/download/all) in Safari
2. Sign in with Apple ID (free, no paid developer account needed)
3. Search **"Command Line Tools for Xcode"** — grab the latest version matching your macOS
4. Download the `.dmg`, open it, run the installer
5. Verify:
```bash
xcode-select -p
# Should print: /Library/Developer/CommandLineTools
```

**Fix 3 — Full Xcode from App Store** (~15GB, overkill but bulletproof). Only if Fixes 1 & 2 fail.

After CLT is installed, retry the Homebrew curl command — it'll skip the CLT step and proceed.

#### Error: network / DNS / blocked URL

Run these diagnostics:

```bash
curl -I https://raw.githubusercontent.com
curl -I https://brew.sh
```

If blocked (VPN / firewall / corporate proxy), either disable the blocker or use the browser fallback:

1. Open `https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh` in Safari
2. Save as `install.sh` to Downloads
3. In Terminal:
```bash
bash ~/Downloads/install.sh
```

---

## Step 2 — Set up Git identity

```bash
git config --global user.name "jameswong2011"
git config --global user.email "jameswong2121@protonmail.com"
git lfs install
```

---

## Step 3 — Recreate Claude preferences

```bash
mkdir -p ~/.claude
cat > ~/.claude/settings.json <<'EOF'
{
  "model": "claude-opus-4-7",
  "autoCompactWindow": 1000000,
  "effortLevel": "max"
}
EOF
```

---

## Step 4 — Launch Claude Code and authenticate

```bash
claude
```

Inside Claude Code:

```
/login
```

Follow the browser prompt.

---

## Step 5 — Install Obsidian plugins

Do not rely on Obsidian Sync to have carried the plugin binaries across. Install all four from scratch — three from the official Community marketplace, Claudian via BRAT (it is not in the marketplace).

Open Obsidian → point it at your vault folder → Settings → Community plugins → turn off **Restricted Mode**.

### 5a — Install the three marketplace plugins

Community plugins → **Browse**, then for each of the plugins below: search, install, and enable.

| Plugin | Marketplace name | Purpose |
|---|---|---|
| `dataview` | **Dataview** | Powers inline queries used by a few thesis/sector notes |
| `templater-obsidian` | **Templater** | Template engine used by `Templates/` |
| `obsidian-git` | **Obsidian Git** | In-app commit/push to the vault's git remote |

### 5b — Install Claudian via BRAT

Claudian is third-party (not in the Obsidian marketplace). BRAT installs it from its GitHub release and keeps it up-to-date automatically.

1. Community plugins → **Browse** → search for **"Obsidian42 - BRAT"** → install → enable
2. Settings → **BRAT** → **Add Beta plugin**
3. Paste: `https://github.com/YishenTu/claudian`
4. BRAT downloads the latest release into `<vault>/.obsidian/plugins/claudian/`
5. Back in Community plugins → enable **Claudian**

### 5c — Verify Claudian

Open Claudian (ribbon icon, or `Cmd+P` → "Claudian"). It should connect to Claude Code using the `/login` from Step 4.

Requirements: Claude Code CLI installed (Step 1d) and Obsidian 1.4.5+.

---

## Step 6 — Reconcile vault graph

Inside Claudian, run:

```
/graph
```

Rebuilds `_graph.md` from scratch so any stale runtime markers that rode along with Obsidian Sync get cleared.

**Run in a fresh Claudian session.** `/graph` full rebuild reads every thesis file; session compaction mid-run forces it to restart, turning a ~10-min rebuild into 15+ min. Open a new Claudian tab before invoking.

---

## Step 7 — Install GitHub Desktop

Download from [desktop.github.com](https://desktop.github.com), install, sign in with your GitHub account. Then **File → Add local repository** → select your vault path (the vault is already a git clone from Step 0, so this just registers it with GitHub Desktop — do not "Clone repository" again).

---

## Smoke test

Inside Claudian:

```
/lint
```

Also verify on the command line (catches Step 0 silently failing):

```bash
ls .claude/skills/ | wc -l   # must be > 0
git status                   # must not say "not a git repository"
```

### Expected findings — do not treat as migration failures

| Finding | What it actually is |
|---|---|
| Edge count drift 15–25% between `/lint` and `/graph` | `/lint` counts only forward adjacency; `/graph` counts forward + both reverse indexes (sector-reverse, macro-reverse). Total drift ≈ reverse edges ÷ forward edges. Not a bug. |
| Reverse-index inconsistencies | Source-file wikilink asymmetry (thesis forward-links a Macro note, that Macro note doesn't wikilink back). Real data debt, not a graph rebuild bug. Leave unless auditing manually. |

### Real debt commonly surfaced on the first post-migration run

- **Triple-bracket wikilinks** (`[[[Research/X]]]`) from hand-edits — Obsidian renders them as literal `[` + valid link + `]`, but `/lint` flags as malformed. Fix to `[[Research/X]]`.
- **Stale-rename wikilinks** — references to old filenames after a `/rename` or manual rename. Examples seen: `[[Theses/PSTG - Pure Storage (Everpure)]]` after renaming to `PSTG - Pure Storage`; `[[Macro/AI Bubble Risk]]` after renaming to `AI Bubble Risk and Semiconductor Valuations`. Fix by Edit in the source file(s).
- **Missing ticker frontmatter** — common on newer theses. Add `ticker: TICKER` after `sector:`. Sub-sector theses covering multiple companies use an array: `ticker: [KLAC, AMAT, LRCX, ASMI, BESI]`.

### After applying fixes

```
/graph last
```

`/graph last` is the incremental form — re-extracts adjacency only for theses modified since the last graph write, rebuilds reverse indexes from scratch to prevent drift. Typically 30–60s vs 10min for a full rebuild.

Then commit the cleanup:

```bash
git add <specific files> _graph.md
git commit -m "Post-migration vault cleanup"
```

If `/lint` runs clean and both sanity checks pass, the migration is complete. Expect a handful of permission prompts on the first few skill runs — click "always allow" and they stop coming.

---

## Step 8 — Clean up legacy vault folders

Migration attempts can leave stray `InvestmentVault/` directories in `~/Documents/`. Two patterns seen:

- **Scratch copy** (~100M+): a full clone from an abandoned migration attempt. Has notes, `.git/`, `.obsidian/`, `.claude/`.
- **Obsidian stub** (~28K): an empty folder with only default `.obsidian/*.json` files. Created when Obsidian was briefly pointed at that path during setup before the real vault was moved into place.

Check for them:

```bash
ls -la ~/Documents/ | grep -iE "investmentvault"
```

Before deleting, verify nothing unique lives in the scratch copy:

```bash
diff -rq --exclude='.git' --exclude='.claude' --exclude='.obsidian' \
  ~/Documents/InvestmentVault-scratch/ ~/InvestmentVault/ | head -20
```

Safe to remove if:
- Only files you edited today differ (and your active vault has the newer version)
- Git remote on the scratch matches your active vault's remote (`cd ~/Documents/InvestmentVault-scratch && git remote -v`) — history lives on GitHub either way

Move to Trash (recoverable via drag-out in Finder):

```bash
TS=$(date +%Y%m%d-%H%M%S)
mv ~/Documents/InvestmentVault-scratch ~/.Trash/InvestmentVault-scratch-$TS
mv ~/Documents/InvestmentVault ~/.Trash/InvestmentVault-stub-$TS
```

**Do not use `osascript` Finder-delete on folders >100M.** AppleEvent times out at ~60s (error −1712), leaving the folder in place. `mv ~/.Trash/` is faster and deterministic. Trade-off: no "Put Back" metadata, but the content is intact and macOS auto-empties Trash after 30 days.

---

## Reference — what syncs via what

| Channel | Carries |
|---|---|
| Obsidian Sync | Notes, attachments, `.obsidian/` sub-paths covered by its sub-toggles (plugins, themes, snippets, config). Hard-excludes `.git/` and all other top-level hidden folders including `.claude/`. |
| Git | Skills (`.claude/skills/`, `.claude/commands/`, `.claude/agents/`), CLAUDE.md, all tracked notes. This is the canonical source for anything hidden. |
| Neither | `~/.claude.json`, `~/.gitconfig`, installed CLIs (Step 1) |

---

# Fresh-user setup — clone from a public GitHub URL

The sections above assume Mac-to-Mac migration by the original owner with Obsidian Sync carrying plugins, attachments, and `.obsidian/` config. This section is a standalone path for someone adopting the vault as-is from a public GitHub clone, with no Obsidian Sync, no inherited Anthropic account, and no inherited git identity. Every command below is self-contained — you do not need to read the Mac-migration flow first unless you want the deeper "why" behind each install.

## What transfers via git alone

Everything required to run the skills and the Obsidian workflow is tracked in the repo. Verified by `git ls-files .obsidian/`:

| Tracked in git (you get these automatically) | Not in git (you provide these) |
|---|---|
| All vault content: `Theses/`, `Research/`, `Sectors/`, `Macro/`, `Templates/`, `Canvas/`, `_Archive/`, `_inbox/` | Your own Anthropic account (`/login` in Claude Code writes to `~/.claude.json`) |
| All skills: `.claude/skills/`, `.claude/commands/`, `.claude/agents/` | Your own git identity (`user.name`, `user.email`) |
| `CLAUDE.md` project instructions | Your own `~/.claude/settings.json` user prefs |
| All 4 community plugins with binaries in `.obsidian/plugins/`: `claudian`, `dataview`, `obsidian-git`, `templater-obsidian` | Homebrew, Node.js, Claude Code CLI, `defuddle-cli` (installed system-wide) |
| Obsidian config: `community-plugins.json`, `core-plugins.json`, `graph.json`, `appearance.json`, `daily-notes.json` | Obsidian workspace layout (`.obsidian/workspace.json` is git-ignored — Obsidian auto-creates a default on first open) |

Because binaries for the third-party Claudian plugin are committed, you do not need the BRAT / GitHub-release install steps from the Mac-migration flow. Open the cloned folder in Obsidian and enable the plugin — done.

## Fork or clone?

| Intent | Path |
|---|---|
| Customize privately, own remote, own commits | **Fork** on GitHub first, clone your fork |
| Try read-only, keep local edits but never push upstream | **Clone** the public URL directly (local commits stay local; `git push` will fail against the original repo unless you have write access) |
| Keep skills + workflow, start with a blank content slate | Clone, then run Step F6 content reset |

## Step F0 — System prerequisites

Fresh Macs ship without git. Install Apple's Command Line Tools:

```bash
xcode-select --install
```

If the dialog errors with "not currently available from the update server," scroll up to **Step 1 — If Homebrew install fails** in the Mac-migration flow; the three fixes there (retry, manual `.dmg` from developer.apple.com, full Xcode from App Store) apply identically.

Install the stack:

```bash
# Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Apple Silicon path setup (use /usr/local/bin on Intel)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# Node + git-lfs
brew install node git-lfs

# Claude Code CLI + defuddle
npm install -g @anthropic-ai/claude-code defuddle-cli
```

Verify all five:
```bash
brew --version && node --version && claude --version && defuddle --version && git --version
```

## Step F1 — Set up YOUR git identity

Do not copy the original owner's identity. Use your own:

```bash
git config --global user.name "<your-name>"
git config --global user.email "<your-email>"
git lfs install
```

## Step F2 — Clone the vault

```bash
git clone <public-url> ~/InvestmentVault
cd ~/InvestmentVault
```

Replace `<public-url>` with the HTTPS or SSH URL of the public repo (or your fork). Path is your choice — the Mac-migration flow matches paths for Obsidian Sync compatibility, but you aren't running Obsidian Sync, so any writable location works.

Verify the clone has the skills, plugins, and content:

```bash
ls .claude/skills/ | head            # should list graph, ingest, sync, lint, /status, etc.
ls .obsidian/plugins/                # claudian, dataview, obsidian-git, templater-obsidian
ls Theses/ | wc -l                   # > 0 (original owner's theses)
```

If any are empty, the clone didn't complete — investigate before continuing.

## Step F3 — Configure YOUR Claude Code

```bash
mkdir -p ~/.claude
cat > ~/.claude/settings.json <<'EOF'
{
  "model": "claude-opus-4-7",
  "autoCompactWindow": 1000000,
  "effortLevel": "max"
}
EOF
claude
```

Inside Claude Code, authenticate with your own Anthropic account:

```
/login
```

Follow the browser prompt. Credentials are written to `~/.claude.json` (outside the repo), so your auth never collides with the original owner's.

## Step F4 — Open Obsidian

File → Open folder as vault → select `~/InvestmentVault`.

Obsidian auto-creates a default `workspace.json` (the original's is git-ignored). Expected.

Enable community plugins — all 4 are already on disk from the clone:

1. Settings → Community plugins → turn off **Restricted Mode**
2. For each of `claudian`, `dataview`, `obsidian-git`, `templater-obsidian`: click "Enable" in the installed-plugins list
3. Open Claudian (ribbon icon, or `Cmd+P` → "Claudian"). It should connect to Claude Code using your `/login` from Step F3.

## Step F5 — (Optional) Re-point the git remote

If you forked the repo, swap origin to your fork:

```bash
git remote set-url origin git@github.com:<your-github-user>/<your-fork>.git
git remote -v   # verify
```

If you cloned read-only and don't plan to push, skip this step. `git push` against someone else's repo will fail with a permission error — that's the intended safety behavior.

## Step F6 — (Optional) Start with a blank content slate

The clone includes the original owner's active research — 40+ theses, 130+ research notes, live sector notes. If you want the skill framework without inheriting someone else's investment views:

```bash
# inside vault root
rm -rf Theses Research Sectors Macro Canvas _Archive _inbox
mkdir -p Theses Research Sectors Macro Canvas _Archive _inbox
# Empty the hot cache (retains structure; /sync rebuilds content)
: > _hot.md
git add -A
git commit -m "Reset content — retain skills, templates, Obsidian config"
```

Retain: `Templates/`, `.claude/`, `CLAUDE.md`, `.obsidian/`, `_migration-guide.md`.

Then rebuild the graph against the empty state:

```
/graph
```

## Step F7 — Smoke test

Inside Claudian:

```
/lint
```

Expectations match the Mac-migration **Smoke test** section above: some findings are false-positive by design (edge-count drift between `/lint` and `/graph`, reverse-index asymmetry), others are real debt the original owner left in. Fresh-clone scenario is cleaner than Mac-migration because there's no Obsidian-Sync-vs-git race — any debt present is structural, not a migration artifact.

Rebuild the graph for your local state:

```
/graph
```

The committed `_graph.md` reflects the original owner's last write. Running `/graph` realigns it with any edits made since clone (including Step F6 if you ran it).

Command-line sanity checks:

```bash
ls .claude/skills/ | wc -l   # must be > 0
git status                   # must not say "not a git repository"
```

First few skill runs will prompt for permission approvals — click "always allow." The prompts stop after 5–10 skill invocations.

## What this setup does NOT include

- **Personal attachments** in custom media folders, if the original owner used any (check `git ls-files` for image/PDF extensions to confirm)
- **Claude Code permission whitelist** — `.claude/settings.json` and `.claude/settings.local.json` are git-ignored, so you'll re-approve skill permissions on first use
- **Runtime watermarks** — `.last_sync`, `.sync_all_fresh`, `.graph_invalidations` are git-ignored by design; first `/sync` run does a full scan to establish baseline
- **The original owner's GitHub Desktop / Obsidian-Git credentials** — configure your own via each tool's settings if you want push access
