---
date: 2026-05-22
tags: [portfolio, tracker, watchlist]
status: active
---

# Live Portfolio Tracker

**Last refreshed:** 2026-05-22 17:41 — 32/32 tickers (FMP)

> [!tip] How this works
> Data fetched live from Financial Modeling Prep (FMP) when you click **Refresh**. Weights are user-edited and preserved across refreshes. API key lives in `.data/config.json` (gitignored — safe to flip repo public). All 32 holdings × 15 columns in one API cycle (~3–5 seconds).

```dataviewjs
// =====================================================================
// Live Portfolio refresh — FMP wholesale tier
// Reads .data/config.json for fmp_api_key (gitignored)
// =====================================================================

const { requestUrl } = require('obsidian');

const HOLDINGS = [
  { n: 'SK Hynix',                t: '000660.KS',  ex: 'KRX',           cur: 'KRW' },
  { n: 'Sandisk',                 t: 'SNDK',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'AMD',                     t: 'AMD',        ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Nvidia',                  t: 'NVDA',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Lumentum',                t: 'LITE',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Palantir',                t: 'PLTR',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Cloudflare',              t: 'NET',        ex: 'NYSE',          cur: 'USD' },
  { n: 'TSMC',                    t: 'TSM',        ex: 'NYSE (ADR)',    cur: 'USD' },
  { n: 'Broadcom',                t: 'AVGO',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Shopify',                 t: 'SHOP',       ex: 'NYSE',          cur: 'USD' },
  { n: 'Take-Two Interactive',    t: 'TTWO',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Lam Research',            t: 'LRCX',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Applied Materials',       t: 'AMAT',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'KLA Corp',                t: 'KLAC',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'ASM International',       t: 'ASM.AS',     ex: 'Euronext AMS',  cur: 'EUR' },
  { n: 'United States Oil Fund',  t: 'USO',        ex: 'NYSE Arca',     cur: 'USD', etf: true },
  { n: 'Palo Alto Networks',      t: 'PANW',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'ServiceNow',              t: 'NOW',        ex: 'NYSE',          cur: 'USD' },
  { n: 'BE Semiconductor',        t: 'BESI.AS',    ex: 'Euronext AMS',  cur: 'EUR' },
  { n: 'Murata Manufacturing',    t: '6981.T',     ex: 'TSE',           cur: 'JPY' },
  { n: 'Spotify',                 t: 'SPOT',       ex: 'NYSE',          cur: 'USD' },
  { n: 'Vicor',                   t: 'VICR',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Marvell',                 t: 'MRVL',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Games Workshop',          t: 'GAW.L',      ex: 'LSE',           cur: 'GBp' },
  { n: 'Sivers Semiconductors',   t: 'SIVE.ST',    ex: 'Nasdaq SE',     cur: 'SEK' },
  { n: 'Aixtron',                 t: 'AIXA.DE',    ex: 'XETRA',         cur: 'EUR' },
  { n: 'Occidental Petroleum',    t: 'OXY',        ex: 'NYSE',          cur: 'USD' },
  { n: 'IQE',                     t: 'IQE.L',      ex: 'AIM (LSE)',     cur: 'GBp' },
  { n: 'Applied Optoelectronics', t: 'AAOI',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Aehr Test Systems',       t: 'AEHR',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Cheniere Energy',         t: 'LNG',        ex: 'NYSE',          cur: 'USD' },
  { n: 'Yancoal',                 t: 'YAL.AX',     ex: 'ASX',           cur: 'AUD' },
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
const btn = bar.createEl('button', { text: '↻ Refresh portfolio data' });
btn.style.cssText = 'padding:10px 18px; font-size:14px; cursor:pointer; background:var(--interactive-accent); color:var(--text-on-accent); border:none; border-radius:6px; font-weight:600;';
const status = bar.createEl('span', { text: '' });
status.style.cssText = 'color:var(--text-muted); font-size:13px;';

// ----- Helpers -----
const BASE = 'https://financialmodelingprep.com/stable';
// Markers built from concatenation so the regex CANNOT match its own source code
// (the previous version overwrote its own regex literal on first refresh)
const TS_MARK = '<' + '!--TABLE-START-->';
const TE_MARK = '<' + '!--TABLE-END-->';
const TABLE_RE = new RegExp(TS_MARK + '([\\s\\S]*?)' + TE_MARK);
const isNum = v => typeof v === 'number' && isFinite(v);

async function fetchJson(url) {
  const r = await requestUrl({ url, throw: false });
  if (r.status !== 200) throw new Error(`HTTP ${r.status}`);
  return r.json;
}

function fmtPrice(v) {
  if (!isNum(v)) return '—';
  if (Math.abs(v) >= 10000) return v.toLocaleString('en-US', { maximumFractionDigits: 0 });
  if (Math.abs(v) >= 1000) return v.toLocaleString('en-US', { maximumFractionDigits: 1 });
  return v.toFixed(2);
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

// ----- Refresh handler -----
btn.onclick = async () => {
  btn.disabled = true;
  btn.innerText = 'Refreshing…';
  status.innerText = `0 / ${HOLDINGS.length}`;

  const file = app.workspace.getActiveFile();
  if (!file) {
    status.innerText = '⚠️ No active file';
    btn.disabled = false; btn.innerText = '↻ Refresh portfolio data';
    return;
  }
  const content = await app.vault.read(file);

  // Preserve user-entered weights — match by Stock name
  const weightMap = {};
  const tblMatch = content.match(TABLE_RE);
  if (tblMatch) {
    for (const line of tblMatch[1].split('\n')) {
      if (!line.startsWith('|') || line.includes('---')) continue;
      const cells = line.split('|').map(c => c.trim());
      if (cells.length >= 6 && cells[2] && !['Stock', '**Total**'].includes(cells[2])) {
        weightMap[cells[2]] = cells[5];
      }
    }
  }

  const fromDate = (() => {
    const d = new Date();
    d.setDate(d.getDate() - 380);
    return d.toISOString().slice(0, 10);
  })();
  const thisYear = new Date().getFullYear();

  let done = 0;
  const results = await Promise.all(HOLDINGS.map(async (h) => {
    try {
      const t = encodeURIComponent(h.t);
      const [quote, ratios, km, est, growth, income, hist] = await Promise.all([
        fetchJson(`${BASE}/quote?symbol=${t}&apikey=${API_KEY}`),
        fetchJson(`${BASE}/ratios-ttm?symbol=${t}&apikey=${API_KEY}`),
        fetchJson(`${BASE}/key-metrics-ttm?symbol=${t}&apikey=${API_KEY}`),
        fetchJson(`${BASE}/analyst-estimates?symbol=${t}&period=annual&apikey=${API_KEY}`),
        fetchJson(`${BASE}/income-statement-growth?symbol=${t}&apikey=${API_KEY}`),
        fetchJson(`${BASE}/income-statement?symbol=${t}&period=annual&limit=2&apikey=${API_KEY}`),
        fetchJson(`${BASE}/historical-price-eod/light?symbol=${t}&from=${fromDate}&apikey=${API_KEY}`),
      ]);
      done++; status.innerText = `${done} / ${HOLDINGS.length}`;
      return { h, ok: true, quote, ratios, km, est, growth, income, hist };
    } catch (e) {
      done++; status.innerText = `${done} / ${HOLDINGS.length}`;
      return { h, ok: false, reason: e.message };
    }
  }));

  const headerCells = ['#', 'Stock', 'Ticker', 'Exchange', 'Weight', 'Price', '1W %', '1M %', '3M %', '1Y %', 'P/E LTM', 'P/E NTM', 'EV/EBIT LTM', 'EV/EBIT NTM', 'ROIC LTM', 'ROIC NTM', 'Rev Gr LFY', 'Rev Gr CFY', 'EPS Gr LFY', 'EPS Gr CFY'];

  const rows = results.map((r, i) => {
    const idx = i + 1;
    const w = weightMap[r.h.n] || '—';
    const exLabel = `${r.h.ex} (${r.h.cur})`;
    const cells = Array(15).fill('—');

    if (r.ok) {
      const q = (r.quote?.[0]) || {};
      const ratios = (r.ratios?.[0]) || {};
      const km = (r.km?.[0]) || {};
      const growthRow = (r.growth?.[0]) || {};
      const income = r.income || [];
      const hist = r.hist || [];
      const lfy = income[0] || {};

      const price = q.price;
      cells[0] = fmtPrice(price);
      cells[1] = fmtPct(trailingReturn(price, hist, 7));
      cells[2] = fmtPct(trailingReturn(price, hist, 30));
      cells[3] = fmtPct(trailingReturn(price, hist, 90));
      cells[4] = fmtPct(trailingReturn(price, hist, 365));

      cells[5] = fmtRatio(ratios.priceToEarningsRatioTTM);

      const cfy = findEstimate(r.est, thisYear) || findEstimate(r.est, thisYear + 1);

      if (cfy && isNum(cfy.epsAvg) && cfy.epsAvg !== 0 && isNum(price)) {
        cells[6] = fmtRatio(price / cfy.epsAvg);
      }

      const evMult = ratios.enterpriseValueMultipleTTM;
      const em = ratios.ebitMarginTTM, edm = ratios.ebitdaMarginTTM;
      if (isNum(evMult) && isNum(em) && isNum(edm) && em !== 0) {
        cells[7] = fmtRatio(evMult * (edm / em));
      }

      if (cfy && isNum(cfy.ebitAvg) && cfy.ebitAvg !== 0 && isNum(km.enterpriseValueTTM)) {
        cells[8] = fmtRatio(km.enterpriseValueTTM / cfy.ebitAvg);
      }

      if (isNum(km.returnOnInvestedCapitalTTM)) {
        cells[9] = fmtPct(km.returnOnInvestedCapitalTTM * 100);
      }

      const tax = ratios.effectiveTaxRateTTM;
      if (cfy && isNum(cfy.ebitAvg) && isNum(tax) && isNum(km.investedCapitalTTM) && km.investedCapitalTTM !== 0) {
        const nopat = cfy.ebitAvg * (1 - Math.max(0, Math.min(0.5, tax)));
        cells[10] = fmtPct(nopat / km.investedCapitalTTM * 100);
      }

      if (isNum(growthRow.growthRevenue)) cells[11] = fmtPct(growthRow.growthRevenue * 100);

      if (cfy && isNum(cfy.revenueAvg) && isNum(lfy.revenue) && lfy.revenue !== 0) {
        cells[12] = fmtPct((cfy.revenueAvg / lfy.revenue - 1) * 100);
      }

      if (isNum(growthRow.growthEPSDiluted)) cells[13] = fmtPct(growthRow.growthEPSDiluted * 100);

      const lfyEps = isNum(lfy.epsdiluted) ? lfy.epsdiluted : lfy.eps;
      if (cfy && isNum(cfy.epsAvg) && isNum(lfyEps) && lfyEps !== 0) {
        cells[14] = fmtPct((cfy.epsAvg / lfyEps - 1) * 100);
      }
    }

    return [String(idx), r.h.n, r.h.t, exLabel, w, ...cells];
  });

  // Pad columns so the markdown source stays visually aligned (matches Obsidian Linter)
  const allRows = [headerCells, ...rows];
  const colWidths = headerCells.map((_, i) => Math.max(3, ...allRows.map(r => (r[i] || '').length)));
  const fmtRow = (cells) => '| ' + cells.map((c, i) => (c || '').padEnd(colWidths[i])).join(' | ') + ' |';
  const sepRow = '| ' + colWidths.map(w => '-'.repeat(w)).join(' | ') + ' |';
  const tableBody = [fmtRow(headerCells), sepRow, ...rows.map(fmtRow)].join('\n');
  // Blank line after the start marker AND before the end marker is required
  // — Obsidian/CommonMark won't recognise the block as a table otherwise.
  const newTable = `${TS_MARK}\n\n${tableBody}\n\n${TE_MARK}`;

  const now = new Date();
  const pad = n => String(n).padStart(2, '0');
  const ts = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}`;
  const okCount = results.filter(r => r.ok).length;
  const refreshLine = `**Last refreshed:** ${ts} — ${okCount}/${results.length} tickers (FMP)`;

  let newContent = content.replace(TABLE_RE, newTable);
  newContent = newContent.replace(/\*\*Last refreshed:\*\* .*/, refreshLine);

  await app.vault.modify(file, newContent);

  btn.disabled = false;
  btn.innerText = '↻ Refresh portfolio data';
  status.innerText = `✓ ${okCount}/${results.length} ok · ${ts}`;
};
```

## Holdings

<!--TABLE-START-->

| #   | Stock                   | Ticker    | Exchange           | Weight           | Price     | 1W %   | 1M %    | 3M %     | 1Y %     | P/E LTM | P/E NTM | EV/EBIT LTM | EV/EBIT NTM | ROIC LTM | ROIC NTM | Rev Gr LFY | Rev Gr CFY | EPS Gr LFY | EPS Gr CFY |
| --- | ----------------------- | --------- | ------------------ | ---------------- | --------- | ------ | ------- | -------- | -------- | ------- | ------- | ----------- | ----------- | -------- | -------- | ---------- | ---------- | ---------- | ---------- |
| 1   | SK Hynix                | 000660.KS | KRX (KRW)          | Full (25%+)      | 1,941,000 | +6.7%  | +58.7%  | +104.5%  | +885.8%  | 18.2    | 6.9     | 16.8        | 21.6        | +28.5%   | +29.5%   | +46.8%     | +232.6%    | +118.7%    | +353.2%    |
| 2   | Sandisk                 | SNDK      | NASDAQ (USD)       | High (10-25%)    | 1,542.2   | +9.6%  | +57.5%  | +137.3%  | +3975.7% | 50.6    | 23.9    | 41.6        | -170.1      | +31.2%   | -9.0%    | +10.4%     | +166.8%    | -142.4%    | -671.0%    |
| 3   | AMD                     | AMD       | NASDAQ (USD)       | Medium (3.5-10%) | 449.59    | +6.0%  | +48.2%  | +124.6%  | +306.1%  | 146.4   | 60.4    | 144.3       | 143.9       | +6.2%    | +8.1%    | +34.3%     | +44.0%     | +165.0%    | +178.8%    |
| 4   | Nvidia                  | NVDA      | NASDAQ (USD)       | Medium (3.5-10%) | 219.51    | -2.6%  | +8.4%   | +15.6%   | +65.3%   | 33.4    | 46.8    | 28.0        | 51.7        | +63.0%   | +60.3%   | +65.5%     | -1.1%      | +66.7%     | -4.8%      |
| 5   | Lumentum                | LITE      | NASDAQ (USD)       | Medium (3.5-10%) | 964.50    | -0.6%  | +10.4%  | +44.4%   | +1171.1% | 156.8   | 117.3   | 268.4       | -3685       | +3.7%    | -0.7%    | +21.0%     | +81.7%     | +104.6%    | +2064.5%   |
| 6   | Palantir                | PLTR      | NASDAQ (USD)       | Medium (3.5-10%) | 137.41    | +2.6%  | -10.0%  | +1.6%    | +12.4%   | 144.2   | 94.3    | 157.3       | 187.4       | +22.3%   | +20.1%   | +56.2%     | +72.5%     | +231.6%    | +111.2%    |
| 7   | Cloudflare              | NET       | NYSE (USD)         | Medium (3.5-10%) | 212.65    | +7.6%  | +2.5%   | +20.0%   | +34.4%   | -864.5  | 177.8   | -705.5      | 106.1       | -4.1%    | +21.2%   | +29.8%     | +29.6%     | -26.1%     | -512.4%    |
| 8   | TSMC                    | TSM       | NYSE (ADR) (USD)   | Medium (3.5-10%) | 407.15    | +0.7%  | +5.1%   | +9.9%    | +107.5%  | 30.3    | 0.8     | 24.9        | 22.5        | +25.8%   | +32.3%   | +33.0%     | +36.6%     | +49.8%     | +49.6%     |
| 9   | Broadcom                | AVGO      | NASDAQ (USD)       | Medium (3.5-10%) | 414.57    | -2.5%  | -1.9%   | +24.6%   | +79.8%   | 78.7    | 36.8    | 72.0        | 51.7        | +17.6%   | +26.2%   | +23.9%     | +61.8%     | +287.8%    | +129.5%    |
| 10  | Shopify                 | SHOP      | NYSE (USD)         | Low<br>(<3.5%)   | 104.86    | +4.6%  | -20.5%  | -16.9%   | +1.5%    | 102.6   | 57.2    | 85.5        | 54.3        | +10.4%   | +25.7%   | +30.1%     | +27.0%     | -39.4%     | +93.1%     |
| 11  | Take-Two Interactive    | TTWO      | NASDAQ (USD)       | Low<br>(<3.5%)   | 238.08    | -1.8%  | +9.1%   | +19.2%   | +5.3%    | -147.9  | 61.0    | -360.4      | -24.5       | -1.5%    | -42.7%   | +18.2%     | +0.4%      | +93.7%     | -340.8%    |
| 12  | Lam Research            | LRCX      | NASDAQ (USD)       | Low<br>(<3.5%)   | 302.24    | +6.2%  | +13.8%  | +23.4%   | +266.1%  | 56.3    | 53.2    | 49.8        | 52.2        | +42.8%   | +50.6%   | +23.7%     | +25.7%     | +43.1%     | +36.2%     |
| 13  | Applied Materials       | AMAT      | NASDAQ (USD)       | Low<br>(<3.5%)   | 427.36    | -2.1%  | +5.9%   | +13.8%   | +166.2%  | 39.9    | 35.1    | 31.8        | 27.5        | +21.6%   | +44.0%   | +4.4%      | +17.3%     | +0.6%      | +39.8%     |
| 14  | KLA Corp                | KLAC      | NASDAQ (USD)       | Low<br>(<3.5%)   | 1,842.2   | +2.1%  | +1.7%   | +23.1%   | +140.0%  | 51.6    | 49.7    | 44.5        | 47.4        | +36.3%   | +40.6%   | +23.9%     | +11.2%     | +49.8%     | +21.3%     |
| 15  | ASM International       | ASM.AS    | Euronext AMS (EUR) | Low<br>(<3.5%)   | 886.00    | +2.6%  | +5.8%   | +24.9%   | +83.9%   | 43.7    | 40.6    | 36.5        | 32.3        | +17.1%   | +29.7%   | +8.2%      | +24.5%     | +5.8%      | +47.9%     |
| 16  | United States Oil Fund  | USO       | NYSE Arca (USD)    | Low<br>(<3.5%)   | 142.54    | -3.8%  | +10.2%  | +76.3%   | +112.3%  | —       | —       | —           | —           | —        | —        | —          | —          | —          | —          |
| 17  | Palo Alto Networks      | PANW      | NASDAQ (USD)       | Low<br>(<3.5%)   | 252.92    | +4.2%  | +39.6%  | +70.1%   | +35.9%   | 137.1   | 68.6    | 98.3        | 36.2        | +5.8%    | +34.2%   | +14.9%     | +22.4%     | -56.0%     | +115.7%    |
| 18  | ServiceNow              | NOW       | NYSE (USD)         | Low<br>(<3.5%)   | 99.69     | +4.9%  | -3.3%   | -4.4%    | -50.9%   | 58.7    | 24.0    | 46.2        | 19.8        | +10.1%   | +56.7%   | +20.9%     | +22.0%     | +21.9%     | +145.8%    |
| 19  | BE Semiconductor        | BESI.AS   | Euronext AMS (EUR) | Low<br>(<3.5%)   | 275.90    | +5.4%  | +18.8%  | +49.5%   | +155.2%  | 144.1   | 69.5    | 106.3       | 64.9        | +17.0%   | +30.4%   | -2.7%      | +57.4%     | -27.8%     | +139.3%    |
| 20  | Murata Manufacturing    | 6981.T    | TSE (JPY)          | Low<br>(<3.5%)   | 7,130     | +15.9% | +45.2%  | +94.0%   | +243.0%  | 55.6    | 59.5    | 41.4        | 37.3        | +8.4%    | +9.1%    | +5.0%      | -1.2%      | +2.0%      | -6.2%      |
| 21  | Spotify                 | SPOT      | NYSE (USD)         | Low<br>(<3.5%)   | 489.93    | +12.1% | -6.3%   | -0.1%    | -23.1%   | 31.9    | 38.0    | 31.0        | 15.6        | +27.1%   | +77.1%   | +9.7%      | +14.8%     | +91.1%     | +19.9%     |
| 22  | Vicor                   | VICR      | NASDAQ (USD)       | Low<br>(<3.5%)   | 268.29    | -2.0%  | +1.2%   | +57.8%   | +545.7%  | 89.2    | 96.8    | 102.0       | 158.3       | +12.9%   | +10.4%   | +13.5%     | +39.8%     | +1764.3%   | +5.4%      |
| 23  | Marvell                 | MRVL      | NASDAQ (USD)       | Low<br>(<3.5%)   | 190.69    | +7.8%  | +21.2%  | +139.9%  | +208.3%  | 60.6    | 67.0    | 52.1        | -1118       | +6.0%    | -0.8%    | +42.1%     | -0.1%      | +401.0%    | -8.2%      |
| 24  | Games Workshop          | GAW.L     | LSE (GBp)          | Low<br>(<3.5%)   | 19,590    | +1.0%  | +1.3%   | +12.9%   | +23.4%   | 31.3    | 3349    | 23.0        | 24.9        | +55.1%   | +55.7%   | +17.5%     | +5.2%      | +29.7%     | -1.7%      |
| 25  | Sivers Semiconductors   | SIVE.ST   | Nasdaq SE (SEK)    | Low<br>(<3.5%)   | 65.70     | +18.0% | +119.0% | +1979.1% | +1479.3% | -102.9  | -193.2  | -128.2      | -71.1       | -10.1%   | -18.2%   | +24.7%     | +18.3%     | -40.8%     | -50.7%     |
| 26  | Aixtron                 | AIXA.DE   | XETRA (EUR)        | Low<br>(<3.5%)   | 53.84     | +3.6%  | +15.5%  | +133.9%  | +333.1%  | 104.3   | 75.3    | 89.2        | 48.2        | +5.3%    | +11.1%   | -12.1%     | +2.2%      | -19.1%     | -6.0%      |
| 27  | Occidental Petroleum    | OXY       | NYSE (USD)         | Low<br>(<3.5%)   | 58.83     | -1.3%  | +3.1%   | +13.5%   | +43.2%   | 12.2    | 12.0    | 21.4        | 11.0        | +2.6%    | +6.5%    | -20.3%     | +18.5%     | -34.0%     | +190.7%    |
| 28  | IQE                     | IQE.L     | AIM (LSE) (GBp)    | Low<br>(<3.5%)   | 43.20     | -6.1%  | -31.0%  | +312.2%  | +292.7%  | -8.5    | -3781   | -13.9       | -18.9       | -17.9%   | -15.0%   | +2.4%      | +0.5%      | -20.7%     | -71.1%     |
| 29  | Applied Optoelectronics | AAOI      | NASDAQ (USD)       | Low<br>(<3.5%)   | 176.81    | -7.1%  | +18.3%  | +242.1%  | +904.0%  | -310.0  | 171.1   | -287.4      | -43.7       | -3.7%    | -22.1%   | +82.8%     | +128.3%    | +85.8%     | -261.4%    |
| 30  | Aehr Test Systems       | AEHR      | NASDAQ (USD)       | Low<br>(<3.5%)   | 91.30     | -8.2%  | -6.2%   | +171.7%  | +934.0%  | -245.5  | -681.3  | -183.5      | 716.5       | -8.3%    | +2.5%    | -10.9%     | -15.4%     | -111.6%    | +3.1%      |
| 31  | Cheniere Energy         | LNG       | NYSE (USD)         | Low<br>(<3.5%)   | 240.45    | -0.6%  | -6.6%   | +6.2%    | +5.2%    | 34.3    | 14.9    | 7.4         | 9.7         | +11.2%   | +15.4%   | +24.4%     | +13.2%     | +69.9%     | -33.2%     |
| 32  | Yancoal                 | YAL.AX    | ASX (AUD)          | Low<br>(<3.5%)   | 6.55      | -2.4%  | -4.4%   | +7.4%    | +27.2%   | 19.7    | 8.4     | 11.0        | 3.3         | +3.8%    | +14.2%   | -13.1%     | +19.4%     | -64.1%     | +136.9%    |

<!--TABLE-END-->

## Column Legend

| Column              | Definition                                                             |
| ------------------- | ---------------------------------------------------------------------- |
| Weight              | Position weight in portfolio                                           |
| Price               | Last close, in listing currency                                        |
| 1W / 1M / 3M / 1Y % | Trailing price return — week / month / quarter / year                  |
| P/E LTM             | Price / earnings, trailing 12 months                                   |
| P/E NTM             | Price / consensus earnings, next 12 months                             |
| EV/EBIT LTM         | Enterprise value / EBIT, trailing 12 months — GAAP including SBC       |
| EV/EBIT NTM         | Enterprise value / consensus EBIT, next 12 months — GAAP including SBC |
| ROIC LTM            | Return on invested capital, trailing 12 months                         |
| ROIC NTM            | Return on invested capital, next 12 months (consensus)                 |
| Rev Gr LFY          | Revenue growth, last full fiscal year                                  |
| Rev Gr CFY          | Revenue growth, current fiscal year (consensus)                        |
| EPS Gr LFY          | EPS growth, last full fiscal year                                      |
| EPS Gr CFY          | EPS growth, current fiscal year (consensus)                            |

## Notes

- **Currency mixing**: Price column shows raw listing-currency prices — USD for US names, KRW for Hynix, JPY for Murata, EUR for ASM/BESI/Aixtron, GBp (pence) for Games Workshop and IQE, AUD for Yancoal, SEK for Sivers. The Exchange column carries the currency tag after first refresh. Multiples (P/E, EV/EBIT, ROIC) are currency-neutral so cross-table comparison stays valid.
- **LSE pence**: Games Workshop and IQE quote in pence (GBp) — divide by 100 for pounds.
- **USO** is a commodity ETF. Price + returns refresh normally; ratio/growth columns will show `—` since there are no fundamentals.
- **Sandisk** trades standalone post-Feb 2025 spin from Western Digital; pre-spin LFY comparables may be noisy or null until a full standalone fiscal year reports.
- **EV/EBIT** is computed on the fly from `EV/EBITDA × (EBITDA margin ÷ EBIT margin)` because FMP exposes EV/EBITDA directly but not EV/EBIT. Mathematically identical to direct EV/EBIT.
- **ROIC NTM** is computed (FMP doesn't publish forward ROIC anywhere): `forward EBIT × (1 − LTM effective tax rate) ÷ LTM invested capital`. Invested capital is held constant, so this reflects forward operating-income evolution only — not balance-sheet changes.
- **Empty cells** after refresh mean FMP returned null for that field (common for loss-makers, recent spins, or thin-coverage names). Not an error.
- **Adding a holding**: edit the `HOLDINGS = [...]` array in the dataviewjs block above. Format: `{ n: 'Name', t: 'FMP_ticker', ex: 'Exchange', cur: 'Currency' }`. Then click Refresh — the script rebuilds the table from the array.

## Log
- 2026-05-22: Initialised tracker — 32 holdings, 15 data columns + ticker/exchange/weight. Wired live refresh via FMP wholesale tier (`.data/config.json` gitignored). All 32 tickers verified coverable on wholesale. Native intl tickers chosen over ADRs where available (Hynix `000660.KS`, Murata `6981.T`, ASM/BESI Euronext `.AS`, Aixtron `AIXA.DE`, Games Workshop `GAW.L`, IQE `IQE.L`, Sivers `SIVE.ST`, Yancoal `YAL.AX`). EV/EBIT computed from EV/EBITDA × margin ratio. Note: existing weight column values preserved by the script — first click overwrites tickers/exchange labels with the script's authoritative HOLDINGS list.
