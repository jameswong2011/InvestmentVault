#!/bin/bash
# Setup script for Investment Research Obsidian Vault
# Usage: cd /path/to/your/vault && bash setup-vault.sh

echo "Setting up Investment Research vault structure..."

# Create folder structure
mkdir -p Theses
mkdir -p Research
mkdir -p Sectors
mkdir -p Macro
mkdir -p Daily
mkdir -p Weekly
mkdir -p Templates
mkdir -p Archive
mkdir -p Canvas

echo "✓ Folders created"

# Create thesis template
cat > Templates/Thesis\ Template.md << 'TEMPLATE'
---
date: {{date}}
tags: [thesis]
status: draft
conviction: 
sector: 
ticker: 
---

# {{title}}

## Summary
<!-- One-paragraph investment case -->

## Key Metrics
| Metric | Value | Notes |
|--------|-------|-------|
| Market Cap | | |
| EV/Revenue | | |
| Revenue Growth | | |
| Gross Margin | | |
| FCF Yield | | |

## Bull Case
- 

## Bear Case
- 

## Catalysts
- 

## Risks
- 

## Position Sizing
**Conviction:** 
**Reasoning:** 

## Related Research
- 

## Log
### {{date}}
- Initial thesis created
TEMPLATE

# Create research template
cat > Templates/Research\ Template.md << 'TEMPLATE'
---
date: {{date}}
tags: [research]
sector: 
ticker: 
source: 
source_type: 
---

# {{title}}

## Key Takeaways
- 

## Details

## Implications for Thesis
<!-- Link to relevant thesis notes -->

## Raw Notes
TEMPLATE

# Create daily note template
cat > Templates/Daily\ Template.md << 'TEMPLATE'
---
date: {{date}}
tags: [daily]
---

# {{date}}

## Market Context
- 

## Research Done
- 

## Thesis Updates
- 

## Tasks
- [ ] 

## Notes
TEMPLATE

# Create weekly review template
cat > Templates/Weekly\ Template.md << 'TEMPLATE'
---
date: {{date}}
tags: [weekly]
week: 
---

# Week of {{date}}

## Thesis Activity
<!-- Which theses were updated, created, or closed -->

## Key Research
<!-- Most important research notes created this week -->

## Market Observations
<!-- Macro and sector-level observations -->

## Patterns
<!-- Recurring themes across research this week -->

## Next Week Priorities
- [ ] 
TEMPLATE

# Create initial sector MOC notes
for sector in "Semiconductors" "Enterprise Software" "Energy & Commodities" "Defense & Geopolitics" "Healthcare & MedTech" "Consumer & Digital"; do
cat > "Sectors/${sector}.md" << SECTOR
---
date: $(date +%Y-%m-%d)
tags: [sector, moc]
---

# ${sector}

## Active Theses
<!-- Links to thesis notes in this sector -->

## Key Dynamics
<!-- Sector-level observations -->

## Watchlist
<!-- Names being tracked but no thesis yet -->

## Research Notes
<!-- Links to research notes in this sector -->
SECTOR
done

echo "✓ Templates created"
echo "✓ Sector MOC notes created"
echo ""
echo "Setup complete! Next steps:"
echo "  1. Copy CLAUDE.md to your vault root"
echo "  2. Copy .clignore to your vault root"
echo "  3. Install Obsidian Agent Skills: npx skills add git@github.com:kepano/obsidian-skills.git"
echo "  4. Open the vault in Obsidian"
echo "  5. Install Dataview plugin: Settings → Community Plugins → Browse → search 'Dataview'"
echo "  6. Install Templater plugin: Settings → Community Plugins → Browse → search 'Templater'"
echo "  7. Run 'claude' from the vault directory to start working"
