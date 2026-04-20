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

## Step 5 — Install the 5 skills from the marketplace

Still inside Claude Code, run these one at a time:

```
/plugin marketplace add anthropics/claude-plugins-official
```

```
/plugin install defuddle@claude-plugins-official
```

```
/plugin install json-canvas@claude-plugins-official
```

```
/plugin install obsidian-bases@claude-plugins-official
```

```
/plugin install obsidian-cli@claude-plugins-official
```

```
/plugin install obsidian-markdown@claude-plugins-official
```

Or run `/plugin` without arguments and tick them from the UI.

---

## Step 6 — Enable Obsidian plugins

Open Obsidian → point it at your vault folder → then:

1. Settings → Community plugins → turn off **Restricted Mode**
2. Enable each of: `dataview`, `templater-obsidian`, `obsidian-git`, `claudian`
3. Open Claudian (ribbon icon, or `Cmd+P` → "Claudian") to verify it connects to Claude Code

### If Claudian is not in the plugin list

Claudian is a third-party plugin (not in the official Obsidian marketplace), so Obsidian Sync should have carried it across from the old Mac. If it's missing from the list, install it manually from GitHub:

**Option A — Direct download (fastest)**

1. Go to [github.com/YishenTu/claudian/releases/latest](https://github.com/YishenTu/claudian/releases/latest) in Safari
2. Download these three files from the release assets:
   - `main.js`
   - `manifest.json`
   - `styles.css`
3. Move them into `<vault>/.obsidian/plugins/claudian/` on your new Mac (create the `claudian` folder if it doesn't exist)
4. In Obsidian: Settings → Community plugins → click the refresh icon → enable **Claudian**

**Option B — BRAT (auto-updates)**

If you want Claudian to update itself over time:

1. Obsidian → Settings → Community plugins → browse → install **"Obsidian42 - BRAT"** → enable it
2. Settings → BRAT → **Add Beta plugin**
3. Paste: `https://github.com/YishenTu/claudian`
4. BRAT installs Claudian and pulls new releases automatically

Requirements either way: Claude Code CLI must be installed (done in Step 1d), and Obsidian 1.4.5+.

---

## Step 7 — Reconcile vault graph

Inside Claudian, run:

```
/graph
```

Rebuilds `_graph.md` from scratch so any stale runtime markers that rode along with Obsidian Sync get cleared.

---

## Step 8 — Install GitHub Desktop

Download from [desktop.github.com](https://desktop.github.com), install, sign in with your GitHub account, add the vault as an existing repository.

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

If `/lint` runs clean and both sanity checks pass, the migration is complete. Expect a handful of permission prompts on the first few skill runs — click "always allow" and they stop coming.

---

## Reference — what syncs via what

| Channel | Carries |
|---|---|
| Obsidian Sync | Notes, attachments, `.obsidian/` sub-paths covered by its sub-toggles (plugins, themes, snippets, config). Hard-excludes `.git/` and all other top-level hidden folders including `.claude/`. |
| Git | Skills (`.claude/skills/`, `.claude/commands/`, `.claude/agents/`), CLAUDE.md, all tracked notes. This is the canonical source for anything hidden. |
| Neither | `~/.claude.json`, `~/.gitconfig`, installed CLIs, marketplace plugins (Step 5) |
