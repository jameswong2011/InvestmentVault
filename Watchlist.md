---
date: 2026-06-08
tags: [watchlist, tracker, theses]
status: active
---

# Watchlist — All Theses

**Last refreshed:** 2026-06-29 20:06 — 69/69 tickers (FMP) · 27 live holdings

> [!tip] How this works
> Tracks every thesis ticker (active / monitoring / draft — `closed` excluded) against trailing returns and NTM P/E. Pulls live from FMP using the same `.data/config.json` key as [[Live Portfolio]]. Click **Refresh** to pull the latest data. In the chart below: **green** = currently held in [[Live Portfolio]], **red** = watchlist only (researched, not held). Live-Portfolio membership is re-read from its rendered Holdings table on every refresh — add/remove a row there and Watchlist's green/red flips on next refresh.

```dataviewjs
// =====================================================================
// Watchlist refresh — FMP wholesale tier
// Mirrors Live Portfolio's contract: same .data/config.json key, marker-
// delimited table, function-form replace (avoids $-backref EARNINGS bug),
// active-set = rendered table (so user-deleted rows stay gone).
//
// Extra: reads Live Portfolio.md and parses its rendered Holdings table
// for column-3 tickers — feeds the "Live" Y/N column so green/red in the
// chart below auto-updates whenever the holdings table is edited. The
// literal marker string is NEVER written into JS comments / markdown
// prose anywhere in this file — every reference uses string concatenation
// or rephrasing to keep the regex from matching its own source.
// =====================================================================

const { requestUrl } = require('obsidian');

const TICKERS = [
  // — Held in Live Portfolio (Refresh re-checks Live Portfolio.md for source of truth) —
  { n: 'SK Hynix',                t: '000660.KS',    s: 'active'     },
  { n: 'Sandisk',                 t: 'SNDK',         s: 'active'     },
  { n: 'AMD',                     t: 'AMD',          s: 'active'     },
  { n: 'Nvidia',                  t: 'NVDA',         s: 'active'     },
  { n: 'Palantir',                t: 'PLTR',         s: 'active'     },
  { n: 'Cloudflare',              t: 'NET',          s: 'active'     },
  { n: 'TSMC',                    t: 'TSM',          s: 'active'     },
  { n: 'Broadcom',                t: 'AVGO',         s: 'active'     },
  { n: 'Aixtron',                 t: 'AIXA.DE',      s: 'active'     },
  { n: 'Advantest',               t: '6857.T',       s: 'monitoring' },
  { n: 'Ajinomoto',               t: '2802.T',       s: 'monitoring' },
  { n: 'Lumentum',                t: 'LITE',         s: 'active'     },
  { n: 'Shopify',                 t: 'SHOP',         s: 'active'     },
  { n: 'Take-Two Interactive',    t: 'TTWO',         s: 'active'     },
  { n: 'Lam Research',            t: 'LRCX',         s: 'active'     },
  { n: 'Applied Materials',       t: 'AMAT',         s: 'active'     },
  { n: 'KLA Corp',                t: 'KLAC',         s: 'active'     },
  { n: 'ASM International',       t: 'ASM.AS',       s: 'active'     },
  { n: 'Palo Alto Networks',      t: 'PANW',         s: 'active'     },
  { n: 'ServiceNow',              t: 'NOW',          s: 'active'     },
  { n: 'BE Semiconductor',        t: 'BESI.AS',      s: 'active'     },
  { n: 'Murata Manufacturing',    t: '6981.T',       s: 'active'     },
  { n: 'Spotify',                 t: 'SPOT',         s: 'active'     },
  { n: 'Vicor',                   t: 'VICR',         s: 'active'     },
  { n: 'Marvell',                 t: 'MRVL',         s: 'active'     },
  { n: 'Games Workshop',          t: 'GAW.L',        s: 'active'     },
  { n: 'Aehr Test Systems',       t: 'AEHR',         s: 'active'     },
  { n: 'Sivers Semiconductors',   t: 'SIVE.ST',      s: 'active'     },
  { n: 'IQE',                     t: 'IQE.L',        s: 'active'     },
  { n: 'Applied Optoelectronics', t: 'AAOI',         s: 'draft'      },
  { n: 'Cheniere Energy',         t: 'LNG',          s: 'active'     },
  // — Watchlist only (researched, not held) —
  { n: 'Kioxia',                  t: '285A.T',       s: 'monitoring' },
  { n: 'Jusung Engineering',      t: '036930.KS',    s: 'draft'      },
  { n: 'TOTO',                    t: '5332.T',       s: 'draft'      },
  { n: 'AppLovin',                t: 'APP',          s: 'monitoring' },
  { n: 'Cameco',                  t: 'CCJ',          s: 'monitoring' },
  { n: 'Circle Internet',         t: 'CRCL',         s: 'monitoring' },
  { n: 'CrowdStrike',             t: 'CRWD',         s: 'monitoring' },
  { n: 'CoreWeave',               t: 'CRWV',         s: 'monitoring' },
  { n: 'CoStar Group',            t: 'CSGP',         s: 'monitoring' },
  { n: 'Constellation Software',  t: 'CSU.TO',       s: 'draft'      },
  { n: 'John Deere',              t: 'DE',           s: 'monitoring' },
  { n: 'Duolingo',                t: 'DUOL',         s: 'monitoring' },
  { n: 'Edelweiss Financial',     t: 'EDELWEISS.NS', s: 'monitoring' },
  { n: 'E Ink Holdings',          t: '8069.TW',      s: 'monitoring' },
  { n: 'FormFactor',              t: 'FORM',         s: 'monitoring' },
  { n: 'SPDR Gold Shares',        t: 'GLD',          s: 'monitoring' },
  { n: 'Hims & Hers Health',      t: 'HIMS',         s: 'monitoring' },
  { n: 'Intel',                   t: 'INTC',         s: 'monitoring' },
  { n: 'Intuit',                  t: 'INTU',         s: 'monitoring' },
  { n: 'Samsara',                 t: 'IOT',          s: 'monitoring' },
  { n: 'Intuitive Surgical',      t: 'ISRG',         s: 'monitoring' },
  { n: 'Kambi Group',             t: 'KAMBI.ST',     s: 'monitoring' },
  { n: 'LPKF Laser',              t: 'LPK.DE',       s: 'draft'      },
  { n: 'Meta',                    t: 'META',         s: 'monitoring' },
  { n: 'Vail Resorts',            t: 'MTN',          s: 'monitoring' },
  { n: 'Nebius Group',            t: 'NBIS',         s: 'draft'      },
  { n: 'Netflix',                 t: 'NFLX',         s: 'monitoring' },
  { n: 'Opendoor',                t: 'OPEN',         s: 'monitoring' },
  { n: 'Procore Technologies',    t: 'PCOR',         s: 'active'     },
  { n: 'Pinterest',               t: 'PINS',         s: 'monitoring' },
  { n: 'Pure Storage',            t: 'PSTG',         s: 'monitoring' },
  { n: 'Reliance Industries',     t: 'RELIANCE.NS',  s: 'monitoring' },
  { n: 'SK Telecom',              t: 'SKM',          s: 'monitoring' },
  { n: 'Scorpio Tankers',         t: 'STNG',         s: 'monitoring' },
  { n: 'Teradyne',                t: 'TER',          s: 'monitoring' },
  { n: 'Uber',                    t: 'UBER',         s: 'monitoring' },
  { n: 'Vertiv Holdings',         t: 'VRT',          s: 'monitoring' },
  { n: 'WiseTech Global',         t: 'WTC.AX',       s: 'monitoring' },
];

// ----- Config load -----
let API_KEY;
try {
  const raw = await app.vault.adapter.read('.data/config.json');
  API_KEY = JSON.parse(raw).fmp_api_key;
  if (!API_KEY) throw new Error('fmp_api_key missing from .data/config.json');
} catch (e) {
  dv.el('div', '⚠️ Config error: ' + e.message, {
    attr: { style: 'color:#c00; padding:12px; border:1px solid #c00; border-radius:4px;' }
  });
  return;
}

// ----- UI -----
const bar = dv.el('div', '', {
  attr: { style: 'display:flex; gap:14px; align-items:center; padding:10px 0; flex-wrap:wrap;' }
});
bar.innerHTML = '';
const btn = bar.createEl('button', { text: '↻ Refresh watchlist data' });
btn.style.cssText = 'padding:10px 18px; font-size:14px; cursor:pointer; background:var(--interactive-accent); color:var(--text-on-accent); border:none; border-radius:6px; font-weight:600;';
const status = bar.createEl('span', { text: '' });
status.style.cssText = 'color:var(--text-muted); font-size:13px;';

// ----- Helpers -----
const BASE = 'https://financialmodelingprep.com/stable';
// Markers built by concatenation so the regex CANNOT match its own source code
// (Live Portfolio learned the hard way — same defense applies here).
const TS_MARK = '<' + '!--TABLE-START-->';
const TE_MARK = '<' + '!--TABLE-END-->';
const TABLE_RE = new RegExp(TS_MARK + '([\\s\\S]*?)' + TE_MARK);
const isNum = v => typeof v === 'number' && isFinite(v);

async function fetchJson(url) {
  const r = await requestUrl({ url, throw: false });
  if (r.status !== 200) throw new Error(`HTTP ${r.status}`);
  return r.json;
}

function fmtRatio(v) {
  if (!isNum(v)) return '—';
  if (Math.abs(v) > 1000) return v.toFixed(0);
  return v.toFixed(1);
}
function fmtPct(v) {
  if (!isNum(v)) return '—';
  return (v >= 0 ? '+' : '') + v.toFixed(1) + '%';
}
function priceNDaysAgo(history, daysAgo) {
  if (!Array.isArray(history) || history.length === 0) return null;
  const target = new Date();
  target.setDate(target.getDate() - daysAgo);
  let best = null, bestDiff = Infinity;
  for (const row of history) {
    const d = new Date(row.date);
    const diff = Math.abs(d - target);
    if (diff < bestDiff) { bestDiff = diff; best = row; }
  }
  return best ? best.price : null;
}
function trailingReturn(curPrice, history, daysAgo) {
  const past = priceNDaysAgo(history, daysAgo);
  if (!isNum(past) || !isNum(curPrice) || past === 0) return null;
  return (curPrice / past - 1) * 100;
}
function findEstimate(estimates, year) {
  if (!Array.isArray(estimates)) return null;
  return estimates.find(e => e.date && e.date.startsWith(String(year))) || null;
}

// Live Portfolio cross-read: pull current holdings tickers from its rendered
// table. Wrap in try/catch so a missing or malformed Live Portfolio.md just
// degrades the Live column to all "N" rather than blocking the refresh.
async function readLiveHoldings() {
  try {
    const lp = await app.vault.adapter.read('Live Portfolio.md');
    const m = lp.match(TABLE_RE);
    if (!m) return new Set();
    const held = new Set();
    for (const line of m[1].split('\n')) {
      if (!line.startsWith('|') || line.includes('---')) continue;
      const cells = line.split('|').map(c => c.trim());
      // Live Portfolio table columns: # | Stock | Ticker | Exchange | ...
      // After splitting on |, cells[0] is empty (leading pipe), so Ticker is cells[3].
      if (cells.length >= 6 && cells[3] && cells[3] !== 'Ticker') {
        held.add(cells[3]);
      }
    }
    return held;
  } catch (e) {
    return new Set();
  }
}

// ----- Refresh handler -----
btn.onclick = async () => {
  btn.disabled = true;
  btn.innerText = 'Refreshing…';
  status.innerText = '';

  const file = app.workspace.getActiveFile();
  if (!file) {
    status.innerText = '⚠️ No active file';
    btn.disabled = false; btn.innerText = '↻ Refresh watchlist data';
    return;
  }
  const content = await app.vault.read(file);

  // Active set = rendered table (same contract as Live Portfolio). Tickers in
  // TICKERS but absent from the rendered table are treated as user-deleted and
  // excluded. Clear the entire table body (header + separator only) to restore.
  const presentTickers = new Set();
  const tblMatch = content.match(TABLE_RE);
  if (tblMatch) {
    for (const line of tblMatch[1].split('\n')) {
      if (!line.startsWith('|') || line.includes('---')) continue;
      const cells = line.split('|').map(c => c.trim());
      // Header row has Ticker in cells[3]; data rows match the same layout.
      if (cells.length >= 6 && cells[3] && cells[3] !== 'Ticker') {
        presentTickers.add(cells[3]);
      }
    }
  }
  const activeTickers = presentTickers.size > 0
    ? TICKERS.filter(h => presentTickers.has(h.t))
    : TICKERS;

  const fromDate = (() => {
    const d = new Date();
    d.setDate(d.getDate() - 380);
    return d.toISOString().slice(0, 10);
  })();
  const thisYear = new Date().getFullYear();

  let done = 0;
  status.innerText = `0 / ${activeTickers.length}`;

  // Per-ticker batch: quote + history + analyst-estimates in parallel.
  // Live-holdings read kicks off in parallel with the first ticker batch.
  const [results, heldSet] = await Promise.all([
    Promise.all(activeTickers.map(async (h) => {
      try {
        const t = encodeURIComponent(h.t);
        const [quote, est, hist] = await Promise.all([
          fetchJson(`${BASE}/quote?symbol=${t}&apikey=${API_KEY}`),
          fetchJson(`${BASE}/analyst-estimates?symbol=${t}&period=annual&apikey=${API_KEY}`),
          fetchJson(`${BASE}/historical-price-eod/light?symbol=${t}&from=${fromDate}&apikey=${API_KEY}`),
        ]);
        done++; status.innerText = `${done} / ${activeTickers.length}`;
        return { h, ok: true, quote, est, hist };
      } catch (e) {
        done++; status.innerText = `${done} / ${activeTickers.length}`;
        return { h, ok: false, reason: e.message };
      }
    })),
    readLiveHoldings(),
  ]);

  const headerCells = ['#', 'Name', 'Ticker', 'Status', 'Live', '1W %', '1M %', '3M %', '1Y %', 'NTM P/E'];

  const rows = results.map((r) => {
    const cells = Array(5).fill('—');
    if (r.ok) {
      const q = (r.quote?.[0]) || {};
      const hist = r.hist || [];
      const price = q.price;
      cells[0] = fmtPct(trailingReturn(price, hist, 7));
      cells[1] = fmtPct(trailingReturn(price, hist, 30));
      cells[2] = fmtPct(trailingReturn(price, hist, 90));
      cells[3] = fmtPct(trailingReturn(price, hist, 365));
      const cfy = findEstimate(r.est, thisYear) || findEstimate(r.est, thisYear + 1);
      if (cfy && isNum(cfy.epsAvg) && cfy.epsAvg !== 0 && isNum(price)) {
        cells[4] = fmtRatio(price / cfy.epsAvg);
      }
    }
    const live = heldSet.has(r.h.t) ? 'Y' : 'N';
    return [r.h.n, r.h.t, r.h.s, live, ...cells];
  });

  // Sort: status tier (active → monitoring → draft) → name alphabetical within tier.
  // Stable visual layout regardless of TICKERS order; chart sorts dynamically by metric.
  const statusRank = (s) => ({ active: 0, monitoring: 1, draft: 2 }[s] ?? 3);
  rows.sort((a, b) => statusRank(a[2]) - statusRank(b[2]) || a[0].localeCompare(b[0]));
  const numberedRows = rows.map((row, i) => [String(i + 1), ...row]);

  // Pad columns for stable markdown alignment (Obsidian Linter friendly).
  const allRows = [headerCells, ...numberedRows];
  const colWidths = headerCells.map((_, i) => Math.max(3, ...allRows.map(r => (r[i] || '').length)));
  const fmtRow = (cells) => '| ' + cells.map((c, i) => (c || '').padEnd(colWidths[i])).join(' | ') + ' |';
  const sepRow = '| ' + colWidths.map(w => '-'.repeat(w)).join(' | ') + ' |';
  const tableBody = [fmtRow(headerCells), sepRow, ...numberedRows.map(fmtRow)].join('\n');
  // Blank lines around start/end markers required for Obsidian to recognise the table.
  const newTable = `${TS_MARK}\n\n${tableBody}\n\n${TE_MARK}`;

  const now = new Date();
  const pad = n => String(n).padStart(2, '0');
  const ts = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}`;
  const okCount = results.filter(r => r.ok).length;
  const refreshLine = `**Last refreshed:** ${ts} — ${okCount}/${results.length} tickers (FMP) · ${heldSet.size} live holdings`;

  // Function-form replace — keeps any literal `$` in cell values from being
  // interpreted as backreferences (the bug that corrupted Live Portfolio's
  // earnings region across refreshes; pre-emptive defense here).
  let newContent = content.replace(TABLE_RE, () => newTable);
  newContent = newContent.replace(/\*\*Last refreshed:\*\* .*/, () => refreshLine);

  await app.vault.modify(file, newContent);

  btn.disabled = false;
  btn.innerText = '↻ Refresh watchlist data';
  status.innerText = `✓ ${okCount}/${results.length} ok · ${heldSet.size} live · ${ts}`;
};
```

## Universe

<!--TABLE-START-->

| #   | Name                    | Ticker       | Status     | Live | 1W %   | 1M %   | 3M %    | 1Y %     | NTM P/E |
| --- | ----------------------- | ------------ | ---------- | ---- | ------ | ------ | ------- | -------- | ------- |
| 1   | Aehr Test Systems       | AEHR         | active     | Y    | -10.3% | -1.9%  | +131.8% | +610.1%  | -685.1  |
| 2   | Aixtron                 | AIXA.DE      | active     | Y    | -6.9%  | -7.2%  | +53.6%  | +231.0%  | 71.1    |
| 3   | AMD                     | AMD          | active     | Y    | +0.3%  | +2.2%  | +148.1% | +267.6%  | 69.8    |
| 4   | Applied Materials       | AMAT         | active     | Y    | +7.0%  | +36.8% | +77.2%  | +242.4%  | 51.2    |
| 5   | ASM International       | ASM.AS       | active     | Y    | -3.9%  | +10.1% | +41.8%  | +75.8%   | 43.1    |
| 6   | BE Semiconductor        | BESI.AS      | active     | Y    | -6.2%  | +0.1%  | +48.4%  | +119.1%  | 68.0    |
| 7   | Broadcom                | AVGO         | active     | Y    | -4.0%  | -20.6% | +16.4%  | +32.4%   | 31.5    |
| 8   | Cheniere Energy         | LNG          | active     | N    | +3.2%  | +6.0%  | -12.4%  | -0.8%    | -242.6  |
| 9   | Cloudflare              | NET          | active     | Y    | +5.4%  | -12.5% | +15.4%  | +21.1%   | 197.9   |
| 10  | Games Workshop          | GAW.L        | active     | Y    | +8.7%  | +12.4% | +25.6%  | +36.3%   | 3691    |
| 11  | IQE                     | IQE.L        | active     | N    | -2.3%  | -11.7% | +93.8%  | +372.3%  | -3498   |
| 12  | KLA Corp                | KLAC         | active     | Y    | +1.7%  | +28.2% | +63.6%  | +177.6%  | 67.1    |
| 13  | Lam Research            | LRCX         | active     | Y    | +2.1%  | +19.5% | +70.8%  | +289.4%  | 66.7    |
| 14  | Lumentum                | LITE         | active     | Y    | -1.3%  | -9.7%  | +6.8%   | +759.4%  | 99.6    |
| 15  | Marvell                 | MRVL         | active     | Y    | -4.4%  | +21.6% | +150.0% | +244.7%  | 93.8    |
| 16  | Murata Manufacturing    | 6981.T       | active     | Y    | -2.4%  | +2.4%  | +192.6% | +398.6%  | 89.7    |
| 17  | Nvidia                  | NVDA         | active     | Y    | -3.8%  | -14.2% | +9.5%   | +21.9%   | 41.0    |
| 18  | Palantir                | PLTR         | active     | Y    | -3.2%  | -29.7% | -22.9%  | -17.2%   | 77.7    |
| 19  | Palo Alto Networks      | PANW         | active     | Y    | +4.6%  | +1.2%  | +89.3%  | +48.7%   | 80.6    |
| 20  | Procore Technologies    | PCOR         | active     | N    | +7.7%  | -24.1% | -26.9%  | -38.7%   | 24.9    |
| 21  | Sandisk                 | SNDK         | active     | Y    | +6.5%  | +18.7% | +201.8% | +4510.2% | 31.9    |
| 22  | ServiceNow              | NOW          | active     | Y    | +2.5%  | -27.6% | -5.5%   | -52.2%   | 23.7    |
| 23  | Shopify                 | SHOP         | active     | Y    | +8.5%  | -5.8%  | -1.4%   | +1.3%    | 65.7    |
| 24  | Sivers Semiconductors   | SIVE.ST      | active     | N    | -22.6% | +11.4% | +508.1% | +1642.9% | -171.6  |
| 25  | SK Hynix                | 000660.KS    | active     | Y    | +2.9%  | +11.2% | +194.3% | +800.0%  | 8.4     |
| 26  | Spotify                 | SPOT         | active     | Y    | +1.0%  | -9.4%  | -2.1%   | -40.1%   | 36.3    |
| 27  | Take-Two Interactive    | TTWO         | active     | Y    | -1.7%  | +5.1%  | +20.3%  | -1.8%    | 61.0    |
| 28  | TSMC                    | TSM          | active     | Y    | -0.9%  | -0.8%  | +26.6%  | +90.9%   | 0.9     |
| 29  | Vicor                   | VICR         | active     | Y    | -2.7%  | -0.6%  | +106.7% | +620.7%  | 107.4   |
| 30  | Advantest               | 6857.T       | monitoring | Y    | +1.7%  | +24.4% | +42.0%  | +199.9%  | 68.9    |
| 31  | Ajinomoto               | 2802.T       | monitoring | Y    | +2.9%  | +8.1%  | +25.8%  | +48.8%   | 43.6    |
| 32  | AppLovin                | APP          | monitoring | N    | +2.2%  | -22.3% | +23.0%  | +36.3%   | 29.6    |
| 33  | Cameco                  | CCJ          | monitoring | N    | -4.0%  | -7.2%  | -6.0%   | +40.8%   | 65.9    |
| 34  | Circle Internet         | CRCL         | monitoring | N    | -2.8%  | -29.9% | -18.9%  | -59.4%   | 72.1    |
| 35  | CoreWeave               | CRWV         | monitoring | N    | -8.6%  | -22.6% | +23.1%  | -40.8%   | -28.5   |
| 36  | CoStar Group            | CSGP         | monitoring | N    | -0.0%  | -10.7% | -23.7%  | -62.4%   | 22.3    |
| 37  | CrowdStrike             | CRWD         | monitoring | N    | +3.0%  | -10.4% | +78.3%  | +37.7%   | 188.8   |
| 38  | Duolingo                | DUOL         | monitoring | N    | -8.1%  | +3.0%  | +26.3%  | -70.4%   | 42.9    |
| 39  | E Ink Holdings          | 8069.TW      | monitoring | N    | —      | —      | —       | —        | —       |
| 40  | Edelweiss Financial     | EDELWEISS.NS | monitoring | N    | -5.1%  | +8.8%  | +13.8%  | +4.3%    | —       |
| 41  | FormFactor              | FORM         | monitoring | N    | -8.4%  | +13.6% | +29.6%  | +279.9%  | 53.3    |
| 42  | Hims & Hers Health      | HIMS         | monitoring | N    | +3.0%  | +22.3% | +71.1%  | -31.9%   | -282.6  |
| 43  | Intel                   | INTC         | monitoring | N    | -3.0%  | +17.4% | +167.2% | +472.9%  | 119.3   |
| 44  | Intuit                  | INTU         | monitoring | N    | +3.7%  | -24.3% | -37.1%  | -66.0%   | 11.2    |
| 45  | Intuitive Surgical      | ISRG         | monitoring | N    | +0.3%  | -1.9%  | -13.0%  | -25.6%   | 38.7    |
| 46  | John Deere              | DE           | monitoring | N    | +3.6%  | +13.1% | +7.5%   | +20.6%   | 33.9    |
| 47  | Kambi Group             | KAMBI.ST     | monitoring | N    | -2.5%  | -10.0% | +35.8%  | +16.3%   | 274.6   |
| 48  | Kioxia                  | 285A.T       | monitoring | N    | -4.2%  | +22.0% | +305.7% | +3433.8% | 92.8    |
| 49  | Meta                    | META         | monitoring | N    | -2.1%  | -8.4%  | -5.0%   | -25.4%   | 16.7    |
| 50  | Netflix                 | NFLX         | monitoring | N    | +1.4%  | -14.0% | -22.8%  | -44.9%   | 20.7    |
| 51  | Opendoor                | OPEN         | monitoring | N    | +4.0%  | -17.7% | -4.4%   | +719.9%  | -12.7   |
| 52  | Pinterest               | PINS         | monitoring | N    | +6.4%  | -2.6%  | +13.6%  | -42.0%   | 11.0    |
| 53  | Pure Storage            | PSTG         | monitoring | N    | +15.6% | +2.1%  | +41.2%  | +49.7%   | 44.3    |
| 54  | Reliance Industries     | RELIANCE.NS  | monitoring | N    | -0.6%  | -1.4%  | -5.0%   | -13.3%   | 21.6    |
| 55  | Samsara                 | IOT          | monitoring | N    | -0.5%  | -19.2% | -2.2%   | -21.7%   | 61.4    |
| 56  | Scorpio Tankers         | STNG         | monitoring | N    | -11.2% | -5.0%  | -2.1%   | +85.5%   | 5.8     |
| 57  | SK Telecom              | SKM          | monitoring | N    | -4.1%  | -27.8% | +9.1%   | +37.3%   | 0.0     |
| 58  | SPDR Gold Shares        | GLD          | monitoring | N    | -1.0%  | -9.1%  | -14.7%  | +22.6%   | —       |
| 59  | Teradyne                | TER          | monitoring | N    | +4.0%  | +18.2% | +39.9%  | +385.8%  | 58.6    |
| 60  | Uber                    | UBER         | monitoring | N    | +9.4%  | +3.3%  | +6.3%   | -18.3%   | 23.1    |
| 61  | Vail Resorts            | MTN          | monitoring | N    | -3.1%  | +3.3%  | +7.6%   | -12.2%   | 31.9    |
| 62  | Vertiv Holdings         | VRT          | monitoring | N    | -4.5%  | -6.0%  | +17.2%  | +136.7%  | 46.9    |
| 63  | WiseTech Global         | WTC.AX       | monitoring | N    | +17.6% | -13.6% | -14.6%  | -69.0%   | 31.2    |
| 64  | Applied Optoelectronics | AAOI         | draft      | N    | -8.0%  | -26.9% | +57.1%  | +428.2%  | 131.3   |
| 65  | Constellation Software  | CSU.TO       | draft      | N    | +1.0%  | -3.9%  | +15.3%  | -43.6%   | 23.8    |
| 66  | Jusung Engineering      | 036930.KS    | draft      | N    | —      | —      | —       | —        | —       |
| 67  | LPKF Laser              | LPK.DE       | draft      | N    | -22.0% | +0.5%  | +214.3% | +147.9%  | -82.0   |
| 68  | Nebius Group            | NBIS         | draft      | N    | -12.7% | -9.2%  | +135.7% | +334.3%  | -113.8  |
| 69  | TOTO                    | 5332.T       | draft      | N    | -4.1%  | +12.0% | +60.6%  | +133.5%  | 43.1    |

<!--TABLE-END-->

## Chart

> [!tip] One row per ticker — 3 return bars + NTM P/E dot
> Reads the Universe table above (no extra API calls). Each row shows trailing 1W / 1M / 3M returns as diverging bars (green up, red down, zero-centered), and a dot for NTM P/E on a peer-relative scale (left = cheap, right = expensive). **Green name = held in [[Live Portfolio]]**, **red name = watchlist only**. Pick a sort metric (default 3M return); the direction toggle flips high↔low. Bars scaled to the 90th percentile of |value| per metric so one outlier doesn't crush the rest; off-scale rows still show the true value as a label. (1Y returns remain in the Universe table above for reference — only removed from the chart to keep NTM P/E in view.)

```dataviewjs
// =====================================================================
// Watchlist chart — reads the rendered Universe table above (no API).
// Renders one row per ticker: 4 return bars (1W/1M/3M/1Y) side-by-side
// + a peer-relative NTM P/E ruler with a dot. Re-renders on Refresh.
// Markers built by concatenation so this block's own source can't match.
// =====================================================================

const TS = '<' + '!--TABLE-START-->';
const TE = '<' + '!--TABLE-END-->';
const TABLE_RE = new RegExp(TS + '([\\s\\S]*?)' + TE);

const page = dv.current();
const path = page && page.file ? page.file.path : null;
const file = path ? app.vault.getAbstractFileByPath(path) : app.workspace.getActiveFile();
if (!file) { dv.paragraph('⚠️ Could not resolve the current file.'); return; }
const content = await app.vault.cachedRead(file);
const m = content.match(TABLE_RE);
if (!m) { dv.paragraph('⚠️ Universe table not found — click **Refresh** above first.'); return; }

// ----- Parse rendered table -----
// Column layout (post split on '|', leading/trailing empties dropped):
// 0:#  1:Name  2:Ticker  3:Status  4:Live  5:1W  6:1M  7:3M  8:1Y  9:NTM P/E
const data = [];
for (const line of m[1].split('\n')) {
  if (!line.trim().startsWith('|') || line.includes('---')) continue;
  const c = line.split('|').map(x => x.trim());
  c.shift(); c.pop();
  if (c.length < 10 || c[1] === 'Name') continue;
  data.push(c);
}
if (!data.length) {
  dv.paragraph('⚠️ No data rows in Universe table — click **Refresh** above first.');
  return;
}

const parseNum = (s) => {
  if (s == null) return null;
  const t = s.replace(/,/g, '').replace(/[+%x]/g, '').trim();
  if (t === '' || t === '—' || t === '-') return null;
  const v = parseFloat(t);
  return Number.isFinite(v) ? v : null;
};
const pctile = (arr, p) => {
  if (!arr.length) return 0;
  const s = [...arr].sort((a, b) => a - b);
  return s[Math.min(s.length - 1, Math.round(p * (s.length - 1)))];
};

const METRICS = {
  '1W %':    { idx: 5, unit: '%' },
  '1M %':    { idx: 6, unit: '%' },
  '3M %':    { idx: 7, unit: '%' },
  'NTM P/E': { idx: 9, unit: 'x' },
};

// ----- Controls -----
const wrap = dv.el('div', '', { attr: { style: 'padding:4px 0 2px;' } });
const ctrl = wrap.createEl('div', { attr: { style: 'display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin-bottom:12px;' } });
ctrl.createEl('span', { text: 'Sort by', attr: { style: 'color:var(--text-muted); font-size:13px; font-weight:600;' } });
const sel = ctrl.createEl('select', { attr: { style: 'padding:5px 8px; border-radius:6px; font-size:13px; background:var(--background-primary); color:var(--text-normal); border:1px solid var(--background-modifier-border);' } });
for (const k of Object.keys(METRICS)) { const o = sel.createEl('option', { text: k }); o.value = k; }
sel.value = '3M %';
const sortBtn = ctrl.createEl('button', { text: 'Sort ▼ high→low', attr: { style: 'padding:5px 10px; font-size:12px; cursor:pointer; border-radius:6px; border:1px solid var(--background-modifier-border); background:var(--background-primary); color:var(--text-normal);' } });
let descending = true;

// Status filter dropdown — defaults to "All" so the user sees every thesis,
// but they can narrow to just active / monitoring / draft when needed.
ctrl.createEl('span', { text: 'Status', attr: { style: 'color:var(--text-muted); font-size:13px; font-weight:600; margin-left:8px;' } });
const statusSel = ctrl.createEl('select', { attr: { style: 'padding:5px 8px; border-radius:6px; font-size:13px; background:var(--background-primary); color:var(--text-normal); border:1px solid var(--background-modifier-border);' } });
for (const k of ['All', 'active', 'monitoring', 'draft']) { const o = statusSel.createEl('option', { text: k }); o.value = k; }
statusSel.value = 'All';

const liveCtrl = ctrl.createEl('span', { attr: { style: 'display:inline-flex; gap:6px; align-items:center; margin-left:8px;' } });
const liveCb = liveCtrl.createEl('input', { attr: { type: 'checkbox', id: 'live-only' } });
liveCtrl.createEl('label', { text: 'Live holdings only', attr: { for: 'live-only', style: 'color:var(--text-muted); font-size:13px; cursor:pointer;' } });

const chart = wrap.createEl('div', {});

// ----- Render -----
const GREEN = 'var(--color-green, #3aa675)';
const RED   = 'var(--color-red, #c0504d)';
const ACC   = 'var(--interactive-accent, #5b6bf0)';
const FAINT = 'var(--text-faint, #8a8f98)';

function render() {
  chart.empty();

  // Filter
  let rows = data.slice();
  if (statusSel.value !== 'All') rows = rows.filter(r => r[3] === statusSel.value);
  if (liveCb.checked) rows = rows.filter(r => r[4] === 'Y');

  if (!rows.length) {
    chart.createEl('div', { text: 'No rows match the current filters.', attr: { style: 'color:var(--text-muted); padding:8px 0;' } });
    return;
  }

  // Parse all values once
  const parsed = rows.map(c => ({
    name:  c[1],
    tick:  c[2],
    stat:  c[3],
    live:  c[4] === 'Y',
    v: {
      '1W %':    parseNum(c[5]),
      '1M %':    parseNum(c[6]),
      '3M %':    parseNum(c[7]),
      'NTM P/E': parseNum(c[9]),
    },
  }));

  // Sort by selected metric — nulls sink to the bottom regardless of direction.
  const sortKey = sel.value;
  parsed.sort((a, b) => {
    const av = a.v[sortKey], bv = b.v[sortKey];
    if (av == null && bv == null) return 0;
    if (av == null) return 1;
    if (bv == null) return -1;
    return descending ? bv - av : av - bv;
  });

  // Per-metric cap: 90th percentile of |value| (returns) / 90th percentile (P/E).
  // P/E is unidirectional so we use a [0, cap] scale with the dot positioned by
  // ticker's value clamped at the cap.
  // 1Y intentionally excluded from chart bars (still in Universe table) — keeps
  // NTM P/E inside the visible viewport. To restore: add '1Y %' back here, add
  // '1Y %': { idx: 8, unit: '%' } to METRICS, and bump the grid templates from
  // 5→6 fixed cols (add another 110px column for the extra return bar).
  const RET_KEYS = ['1W %', '1M %', '3M %'];
  const retCaps = {};
  for (const k of RET_KEYS) {
    const vals = parsed.map(p => p.v[k]).filter(v => v != null).map(Math.abs);
    retCaps[k] = Math.max(pctile(vals, 0.90), 1e-9);
  }
  const peVals = parsed.map(p => p.v['NTM P/E']).filter(v => v != null && v > 0);
  const peCap = peVals.length ? Math.max(pctile(peVals, 0.90), 1e-9) : 100;
  const peMin = 0;

  const fmtRet = (v) => v == null ? '—' : (v >= 0 ? '+' : '') + v.toFixed(1) + '%';
  const fmtPe  = (v) => v == null ? '—' : v.toFixed(Math.abs(v) >= 1000 ? 0 : 1) + 'x';

  // Layout: name(170) | 1W(110) | 1M(110) | 3M(110) | 1Y(110) | NTM P/E(140)
  // Each bar slot: 70px bar + 35px value label.
  const grid = chart.createEl('div', {
    attr: { style: 'display:flex; flex-direction:column; gap:3px; font-size:12px; overflow-x:auto;' }
  });

  // Header strip
  const hdr = grid.createEl('div', {
    attr: { style: 'display:grid; grid-template-columns:170px 110px 110px 110px 140px; align-items:center; gap:8px; padding:4px 0 6px; border-bottom:1px solid var(--background-modifier-border); color:var(--text-faint); font-size:11px; font-weight:600;' }
  });
  hdr.createEl('div', { text: 'Ticker', attr: { style: 'text-align:right;' } });
  for (const k of RET_KEYS) hdr.createEl('div', { text: k, attr: { style: 'text-align:center;' } });
  hdr.createEl('div', { text: 'NTM P/E (peer scale)', attr: { style: 'text-align:center;' } });

  for (const p of parsed) {
    const row = grid.createEl('div', {
      attr: { style: 'display:grid; grid-template-columns:170px 110px 110px 110px 140px; align-items:center; gap:8px; padding:1px 0;' }
    });

    // Name — green if held, red if watchlist only. Status badge subscripted.
    const nameCell = row.createEl('div', {
      attr: { style: 'text-align:right; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;' }
    });
    nameCell.createEl('span', {
      text: p.name,
      attr: { style: 'color:' + (p.live ? GREEN : RED) + '; font-weight:600;' }
    });
    nameCell.createEl('span', {
      text: ' · ' + p.stat,
      attr: { style: 'color:var(--text-faint); font-size:10px;' }
    });

    // 4 return bars: diverging from a central zero line, scaled to per-metric cap.
    for (const k of RET_KEYS) {
      const v = p.v[k];
      const cap = retCaps[k];
      const cell = row.createEl('div', {
        attr: { style: 'display:grid; grid-template-columns:65px 40px; align-items:center; gap:3px;' }
      });
      const track = cell.createEl('div', {
        attr: { style: 'position:relative; height:12px; background:var(--background-modifier-border); border-radius:2px; overflow:hidden;' }
      });
      if (v != null) {
        const frac = Math.min(Math.abs(v), cap) / cap;
        const half = frac * 50;
        const color = v >= 0 ? GREEN : RED;
        track.createEl('div', { attr: { style:
          'position:absolute; top:0; height:100%; background:' + color + '; ' +
          (v >= 0 ? 'left:50%; width:' + half + '%; border-radius:0 2px 2px 0;'
                  : 'right:50%; width:' + half + '%; border-radius:2px 0 0 2px;') } });
        track.createEl('div', { attr: { style: 'position:absolute; left:50%; top:0; bottom:0; width:1px; background:var(--text-faint); opacity:0.5;' } });
      } else {
        track.createEl('div', { attr: { style: 'position:absolute; left:50%; top:0; bottom:0; width:1px; background:var(--text-faint); opacity:0.5;' } });
      }
      cell.createEl('div', {
        text: fmtRet(v),
        attr: { style: 'text-align:left; font-variant-numeric:tabular-nums; color:' + (v == null ? 'var(--text-faint)' : 'var(--text-muted)') + '; font-size:11px;' }
      });
    }

    // NTM P/E: peer-relative ruler [0, peCap] with a dot at the ticker's value.
    // Off-scale (above peCap, e.g. GAW 3241x) clamps to the right edge.
    const peV = p.v['NTM P/E'];
    const peCell = row.createEl('div', {
      attr: { style: 'display:grid; grid-template-columns:90px 45px; align-items:center; gap:3px;' }
    });
    const peTrack = peCell.createEl('div', {
      attr: { style: 'position:relative; height:12px; background:var(--background-modifier-border); border-radius:2px;' }
    });
    if (peV != null) {
      // Negative P/E = loss-maker. Render the ruler greyed-out with a small red marker
      // at the left edge so the user can see "loss-maker" at a glance.
      if (peV < 0) {
        const negDot = peTrack.createEl('div', {
          attr: { style: 'position:absolute; left:4px; top:50%; transform:translateY(-50%); width:8px; height:8px; border-radius:50%; background:' + RED + '; border:1.5px solid var(--background-primary); box-shadow:0 0 0 0.5px ' + RED + ';' }
        });
        negDot.title = `${p.name}: NTM P/E ${peV.toFixed(1)}x (negative — loss-maker)`;
      } else {
        const clamped = Math.min(peV, peCap);
        const fracPe = (clamped - peMin) / (peCap - peMin);
        const offScale = peV > peCap;
        const dot = peTrack.createEl('div', {
          attr: { style:
            'position:absolute; left:calc(' + (fracPe * 100) + '% - 5px); top:50%; transform:translateY(-50%); ' +
            'width:10px; height:10px; border-radius:50%; background:' + ACC + '; ' +
            'border:1.5px solid var(--background-primary); box-shadow:0 0 0 0.5px ' + ACC + ';' +
            (offScale ? ' outline:1.5px dashed var(--text-normal); outline-offset:1px;' : '') }
        });
        dot.title = `${p.name}: NTM P/E ${peV.toFixed(1)}x` + (offScale ? ' (off-scale — pinned to edge)' : '');
      }
      // Faint quartile ticks for visual reference
      for (const q of [0.25, 0.5, 0.75]) {
        peTrack.createEl('div', {
          attr: { style: 'position:absolute; left:' + (q * 100) + '%; top:0; bottom:0; width:1px; background:var(--text-faint); opacity:0.3;' }
        });
      }
    }
    peCell.createEl('div', {
      text: fmtPe(peV),
      attr: { style: 'text-align:left; font-variant-numeric:tabular-nums; color:' + (peV == null ? 'var(--text-faint)' : 'var(--text-muted)') + '; font-size:11px;' }
    });
  }

  // Footer caption — counts, scale notes, color key
  const liveCount = parsed.filter(p => p.live).length;
  const note = chart.createEl('div', { attr: { style: 'color:var(--text-faint); font-size:11px; margin-top:10px; line-height:1.6;' } });
  note.innerHTML =
    `<span style="color:${GREEN}; font-weight:600;">●</span> Live holding (${liveCount}) · ` +
    `<span style="color:${RED}; font-weight:600;">●</span> Watchlist only (${parsed.length - liveCount}) · ` +
    `total ${parsed.length} tickers · ` +
    `return bars capped at 90th percentile of |value| per metric · ` +
    `NTM P/E scale [0, ${peCap.toFixed(0)}x] · ` +
    `<span style="color:${ACC};">●</span> ringed dots are off-scale (>${peCap.toFixed(0)}x), pinned to right edge · ` +
    `<span style="color:${RED};">●</span> at left edge = negative NTM P/E (loss-maker)`;
}

sel.onchange = render;
statusSel.onchange = render;
liveCb.onchange = render;
sortBtn.onclick = () => { descending = !descending; sortBtn.setText(descending ? 'Sort ▼ high→low' : 'Sort ▲ low→high'); render(); };
render();
```

## Notes

- **Universe**: every thesis in `/Theses` except those with `status: closed` (currently zero). BTC-CRYPTO excluded — no NTM P/E concept for a non-equity asset.
- **Refresh budget**: ~69 tickers × 3 FMP endpoints (`quote`, `analyst-estimates`, `historical-price-eod/light`) = ~207 parallel calls per refresh. Lighter than [[Live Portfolio]]'s 7-endpoint Holdings cycle.
- **Live column**: Y/N flag re-read from [[Live Portfolio]]'s rendered Holdings table on every refresh — its column-3 Ticker values are the source of truth. Delete a row from Live Portfolio and its name flips from green to red here on next Watchlist refresh. Add a row there and it flips back to green.
- **Currency-neutrality**: returns are %, P/E is unitless — no currency-mixing problem (unlike Live Portfolio's Price column). Cross-row comparison is always valid.
- **Active set = rendered Universe table** (not the `TICKERS` array): same contract as Live Portfolio. Delete a row → stays gone on next refresh. Type a new ticker into column 3 of any non-header row → next refresh fills it via TICKERS metadata lookup. Clear the table body (header + separator only) → next refresh repopulates from full TICKERS.
- **Adding a NEW ticker not yet in TICKERS**: edit the `TICKERS = [...]` array in the dataviewjs block above (format: `{ n: 'Name', t: 'FMP_ticker', s: 'status' }`), then add the row to the table.
- **International tickers — best-effort FMP symbols**: where the thesis frontmatter `ticker:` field omits the exchange suffix (e.g., `IQE` → `IQE.L`, `KLA` → `KLAC`, `GAW` → `GAW.L`, `WTC` → `WTC.AX`, `RELIANCE` → `RELIANCE.NS`, `EDEL` → `EDELWEISS.NS`, `EINK` → `8069.TW`, `KAMBI` → `KAMBI.ST`, `LPKF` → `LPK.DE`, `CSU` → `CSU.TO`, `TOTO` → `5332.T`) the TICKERS array carries the FMP-correct form. If a ticker returns `—` cells across the board after refresh, the FMP symbol is likely wrong — check the `t:` value in TICKERS.
- **ETFs (GLD)**: returns refresh normally; NTM P/E shows `—` since there are no earnings estimates.
- **Loss-makers** (negative trailing EPS or negative NTM EPS): P/E LTM-style "negative multiple" is mathematically defined but economically meaningless. The chart renders a small red dot at the left edge of the P/E ruler for negative NTM P/E so loss-makers are visually flagged rather than dropped or rendered as misleading high values.
- **Bar scaling**: each return metric (1W / 1M / 3M) is independently scaled to the 90th percentile of |value| across the current filter set — so one outlier doesn't crush every other bar. True values always shown as labels next to the bar. NTM P/E uses [0, 90th percentile] scaling on the same principle. **1Y returns are kept in the Universe table but dropped from the chart** so the NTM P/E ruler fits inside the visible viewport on a standard Obsidian editor width — restore via the inline instructions next to `RET_KEYS` in the chart block.
- **Sort & filter**: chart-only — does not modify the table. Sort metric defaults to 3M return (the user's chosen workhorse timeframe — long enough to filter noise, short enough to surface recent moves). Status filter ("All" / active / monitoring / draft) and "Live holdings only" checkbox compose freely.
- **Auto-rerender**: the Chart block re-runs whenever the file changes (Dataview's default behavior), so clicking Refresh in the fetcher block updates the visualization automatically.

## Log
- 2026-06-08: Dropped the 1Y return bar from the chart so the NTM P/E ruler fits inside a standard Obsidian editor viewport (was being clipped on the right edge). 1Y data is still fetched and stored in the Universe table — restoration is 3 lines: re-add `'1Y %'` to `RET_KEYS`, re-add `'1Y %': { idx: 8, unit: '%' }` to `METRICS`, bump both `grid-template-columns` from 5 fixed cols (170/110/110/110/140) back to 6 (170/110/110/110/110/140). Inline restoration comment placed next to `RET_KEYS`. Sort dropdown auto-drops 1Y because it's populated from `Object.keys(METRICS)`.
- 2026-06-08: Initialised Watchlist tracker — 69 tickers covering every active / monitoring / draft thesis (BTC-CRYPTO excluded). Reuses [[Live Portfolio]]'s FMP fetch pattern, marker-delimited table contract, and read-only chart-parses-table pattern. New cross-file read: parses Live Portfolio's rendered Holdings table on every refresh to derive the Live Y/N flag, so green (held) / red (watchlist-only) coloring in the chart auto-syncs with portfolio edits. Chart layout: one row per ticker, four diverging return bars (1W/1M/3M/1Y, green up / red down, zero-centered, per-metric 90th-pct scale) + a NTM P/E peer-relative ruler with a dot (loss-makers flagged red at the left edge, off-scale names ringed at the right edge). Sort default 3M return desc; metric and direction both toggleable. Status dropdown and Live-only checkbox layer on top of sort. FMP budget ~207 calls per refresh (3 endpoints × 69 tickers in parallel). Note: the literal table-marker string is intentionally never written into JS comments or markdown prose in this file — every reference uses string concatenation or rephrasing so the matching regex can't match its own source (the same defense Live Portfolio uses).
