```
Fill this sector note. Web-primary research, vault-secondary (theses in Active Theses + linked research via _graph.md). Use exhaustive deep thinking based websearch using maximum thinking budget. After writing: in each Active Thesis, replace any stale [[Sectors/OLD_PARENT]] wikilinks with this sector's wikilink and append a "Wikilink cleanup:" log entry. In each research note cited, add this sector as a back-reference under ## Related Sectors. Populate the sector's ## Related Research with vault notes. Flip status to active when ≥5 sections filled. Don't edit thesis bodies or callouts.
```



## Two things to verify before you push from the other Macs

1. **Check `.gitignore` on the working mac doesn't exclude `.claude/`.** Some default gitignores for Obsidian vaults exclude all hidden folders with a line like `.*/`. Run this on the other mac:
    
    ```bash
    cd /path/to/vault
    git check-ignore -v .claude/skills/sync/SKILL.md
    ```
    
    bash
    
    If it prints nothing, the file is tracked — good. If it prints a rule, that rule needs to be removed or you need an override (`!.claude/`).
    
2. **Check the skills are actually committed**, not just in the working tree:
    
    ```bash
    git ls-tree -r HEAD --name-only | grep '^\.claude/skills' | head
    ```
    
    bash
    
    If empty, they were never committed on that mac either.
    

Once confirmed, push, then on this mac the `git checkout -- .claude/ .gitignore` from my previous reply will bring everything across.


.claude/skills/_shared/hot-md-contract.md

.claude/skills/_shared/log-prefixes.md

.claude/skills/_shared/preflight.md

.claude/skills/_shared/sector-resolution.md

.claude/skills/_shared/wikilink-forms.md

.claude/skills/brief/SKILL.md

.claude/skills/catalyst/SKILL.md

.claude/skills/clean/SKILL.md

.claude/skills/compare/RATIONALE.md

.claude/skills/compare/SKILL.md


```bash
git ls-tree -r HEAD --name-only | grep -c '^\.claude/skills'
```