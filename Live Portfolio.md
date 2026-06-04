---
date: 2026-05-22
tags: [portfolio, tracker, watchlist]
status: active
---

# Live Portfolio Tracker

**Last refreshed:** 2026-05-29 01:42 — 27/27 tickers (FMP)

> [!tip] How this works
> Data fetched live from Financial Modeling Prep (FMP) when you click **Refresh**. Weights are user-edited and preserved across refreshes. API key lives in `.data/config.json` (gitignored — safe to flip repo public). All 34 holdings × 15 columns in one API cycle (~3–5 seconds).

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
  { n: 'Palantir',                t: 'PLTR',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Cloudflare',              t: 'NET',        ex: 'NYSE',          cur: 'USD' },
  { n: 'TSMC',                    t: 'TSM',        ex: 'NYSE (ADR)',    cur: 'USD' },
  { n: 'Broadcom',                t: 'AVGO',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Aixtron',                 t: 'AIXA.DE',    ex: 'XETRA',         cur: 'EUR' },
  { n: 'Advantest',               t: '6857.T',     ex: 'TSE',           cur: 'JPY' },
  { n: 'Ajinomoto',               t: '2802.T',     ex: 'TSE',           cur: 'JPY' },
  { n: 'Lumentum',                t: 'LITE',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Shopify',                 t: 'SHOP',       ex: 'NYSE',          cur: 'USD' },
  { n: 'Take-Two Interactive',    t: 'TTWO',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Lam Research',            t: 'LRCX',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Applied Materials',       t: 'AMAT',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'KLA Corp',                t: 'KLAC',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'ASM International',       t: 'ASM.AS',     ex: 'Euronext AMS',  cur: 'EUR' },
  { n: 'Palo Alto Networks',      t: 'PANW',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'ServiceNow',              t: 'NOW',        ex: 'NYSE',          cur: 'USD' },
  { n: 'BE Semiconductor',        t: 'BESI.AS',    ex: 'Euronext AMS',  cur: 'EUR' },
  { n: 'Murata Manufacturing',    t: '6981.T',     ex: 'TSE',           cur: 'JPY' },
  { n: 'Spotify',                 t: 'SPOT',       ex: 'NYSE',          cur: 'USD' },
  { n: 'Vicor',                   t: 'VICR',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Marvell',                 t: 'MRVL',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'Games Workshop',          t: 'GAW.L',      ex: 'LSE',           cur: 'GBp' },
  { n: 'Aehr Test Systems',       t: 'AEHR',       ex: 'NASDAQ',        cur: 'USD' },
  { n: 'United States Oil Fund',  t: 'USO',        ex: 'NYSE Arca',     cur: 'USD', etf: true },
  { n: 'Sivers Semiconductors',   t: 'SIVE.ST',    ex: 'Nasdaq SE',     cur: 'SEK' },
  { n: 'Occidental Petroleum',    t: 'OXY',        ex: 'NYSE',          cur: 'USD' },
  { n: 'IQE',                     t: 'IQE.L',      ex: 'AIM (LSE)',     cur: 'GBp' },
  { n: 'Applied Optoelectronics', t: 'AAOI',       ex: 'NASDAQ',        cur: 'USD' },
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
const ES_MARK = '<' + '!--EARNINGS-START-->';
const EE_MARK = '<' + '!--EARNINGS-END-->';
const EARNINGS_RE = new RegExp(ES_MARK + '([\\s\\S]*?)' + EE_MARK);
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
function fmtEps(v) {
  if (!isNum(v)) return '—';
  return '$' + v.toFixed(2);
}
function fmtRevenue(v) {
  if (!isNum(v)) return '—';
  if (Math.abs(v) >= 1e9) return '$' + (v / 1e9).toFixed(1) + 'B';
  if (Math.abs(v) >= 1e6) return '$' + (v / 1e6).toFixed(0) + 'M';
  if (Math.abs(v) >= 1e3) return '$' + (v / 1e3).toFixed(0) + 'K';
  return '$' + v.toFixed(0);
}
function fmtTime(t) {
  if (!t || typeof t !== 'string') return '—';
  const lower = t.toLowerCase();
  if (lower.includes('amc') || lower.includes('after')) return 'AMC';
  if (lower.includes('bmo') || lower.includes('before')) return 'BMO';
  return '—';
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
  status.innerText = '';  // set after activeHoldings is computed

  const file = app.workspace.getActiveFile();
  if (!file) {
    status.innerText = '⚠️ No active file';
    btn.disabled = false; btn.innerText = '↻ Refresh portfolio data';
    return;
  }
  const content = await app.vault.read(file);

  // Preserve user-entered weights AND user-deleted rows — the rendered table is the
  // active set. Any HOLDINGS ticker not present in the existing table is treated as
  // deleted-by-user and excluded from this refresh. To restore deleted tickers, clear
  // the entire table body (leave just header + separator) — empty-presentTickers
  // falls back to full HOLDINGS. To add a new ticker not yet in the table, type the
  // ticker into column 3 (Ticker) of any non-header row before refreshing.
  const weightMap = {};
  const presentTickers = new Set();
  const tblMatch = content.match(TABLE_RE);
  if (tblMatch) {
    for (const line of tblMatch[1].split('\n')) {
      if (!line.startsWith('|') || line.includes('---')) continue;
      const cells = line.split('|').map(c => c.trim());
      if (cells.length >= 6 && cells[2] && !['Stock', '**Total**'].includes(cells[2])) {
        weightMap[cells[2]] = cells[5];
        if (cells[3]) presentTickers.add(cells[3]);  // ticker is column 3
      }
    }
  }
  const activeHoldings = presentTickers.size > 0
    ? HOLDINGS.filter(h => presentTickers.has(h.t))
    : HOLDINGS;

  const fromDate = (() => {
    const d = new Date();
    d.setDate(d.getDate() - 380);
    return d.toISOString().slice(0, 10);
  })();
  const thisYear = new Date().getFullYear();

  let done = 0;
  status.innerText = `0 / ${activeHoldings.length}`;
  // Per-ticker fundamentals batch + ONE universe earnings-calendar call in parallel.
  // The earnings endpoint is universe-only on FMP stable — passing symbol=X is silently
  // ignored, so we fetch and filter in JS. The endpoint caps each call at 4000 records,
  // and at ~110 events/day globally a 30-day window stays comfortably under that cap.
  const earningsFrom = new Date().toISOString().slice(0, 10);
  const earningsTo = (() => {
    const d = new Date(); d.setDate(d.getDate() + 30);
    return d.toISOString().slice(0, 10);
  })();

  const [results, universeEarnings] = await Promise.all([
    Promise.all(activeHoldings.map(async (h) => {
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
        done++; status.innerText = `${done} / ${activeHoldings.length}`;
        return { h, ok: true, quote, ratios, km, est, growth, income, hist };
      } catch (e) {
        done++; status.innerText = `${done} / ${activeHoldings.length}`;
        return { h, ok: false, reason: e.message };
      }
    })),
    fetchJson(`${BASE}/earnings-calendar?from=${earningsFrom}&to=${earningsTo}&apikey=${API_KEY}`)
      .catch(() => null),
  ]);

  const headerCells = ['#', 'Stock', 'Ticker', 'Exchange', 'Weight', 'Price', '1W %', '1M %', '3M %', '1Y %', 'P/E LTM', 'P/E NTM', 'EV/EBIT LTM', 'EV/EBIT NTM', 'ROIC LTM', 'ROIC NTM', 'Rev Gr LFY', 'Rev Gr CFY', 'EPS Gr LFY', 'EPS Gr CFY'];

  const rows = results.map((r) => {
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

    return [r.h.n, r.h.t, exLabel, w, ...cells];
  });

  // Auto-sort by weight tier (Full → High → Medium → Low → unweighted) on every refresh, so the
  // rendered order self-maintains regardless of HOLDINGS array order or later weight edits in the
  // table. Array.sort is stable, so within a tier the existing order (HOLDINGS sequence) is
  // preserved. Weight is at index 3 of each row here — the display number is prepended afterward.
  const weightRank = (w) => {
    const s = (w || '').toLowerCase();
    if (s.startsWith('full')) return 0;
    if (s.startsWith('high')) return 1;
    if (s.startsWith('medium')) return 2;
    if (s.startsWith('low')) return 3;
    return 4;
  };
  rows.sort((a, b) => weightRank(a[3]) - weightRank(b[3]));
  const numberedRows = rows.map((row, i) => [String(i + 1), ...row]);

  // Pad columns so the markdown source stays visually aligned (matches Obsidian Linter)
  const allRows = [headerCells, ...numberedRows];
  const colWidths = headerCells.map((_, i) => Math.max(3, ...allRows.map(r => (r[i] || '').length)));
  const fmtRow = (cells) => '| ' + cells.map((c, i) => (c || '').padEnd(colWidths[i])).join(' | ') + ' |';
  const sepRow = '| ' + colWidths.map(w => '-'.repeat(w)).join(' | ') + ' |';
  const tableBody = [fmtRow(headerCells), sepRow, ...numberedRows.map(fmtRow)].join('\n');
  // Blank line after the start marker AND before the end marker is required
  // — Obsidian/CommonMark won't recognise the block as a table otherwise.
  const newTable = `${TS_MARK}\n\n${tableBody}\n\n${TE_MARK}`;

  // ----- Earnings table (next upcoming earnings per ticker, sorted ascending) -----
  // Built by symbol-matching the universe response against activeHoldings (which respects
  // user deletions from the Holdings table — see weight-parsing block above for details).
  // Tickers without an upcoming earnings entry in the 30-day window are silently dropped.
  const nowDate = new Date(new Date().toISOString().slice(0, 10));

  const symbolMap = new Map();
  if (Array.isArray(universeEarnings)) {
    for (const e of universeEarnings) {
      if (!e || !e.symbol) continue;
      if (!symbolMap.has(e.symbol)) symbolMap.set(e.symbol, []);
      symbolMap.get(e.symbol).push(e);
    }
  }

  const earningsRows = activeHoldings
    .map(h => {
      const entries = symbolMap.get(h.t) || [];
      const upcoming = entries
        .filter(e => e && e.date && new Date(e.date) >= nowDate)
        .sort((a, b) => new Date(a.date) - new Date(b.date));
      return upcoming.length > 0 ? { h, next: upcoming[0] } : null;
    })
    .filter(Boolean)
    .sort((a, b) => new Date(a.next.date) - new Date(b.next.date));

  const eHeaderCells = ['Date', 'Days', 'Stock', 'Ticker', 'EPS Est', 'Rev Est', 'Time'];
  const eBodyRows = earningsRows.map(({h, next}) => {
    const daysOut = Math.round((new Date(next.date) - nowDate) / 86400000);
    // Defensive field reads — FMP has shipped multiple field-name variants across
    // API tiers (epsEstimated / estimatedEPS / eps; revenueEstimated / estimatedRevenue / revenue).
    const eps = next.epsEstimated ?? next.estimatedEPS ?? next.eps ?? null;
    const rev = next.revenueEstimated ?? next.estimatedRevenue ?? next.revenue ?? null;
    const time = next.time ?? next.eventTime ?? null;
    return [
      next.date,
      String(daysOut),
      h.n,
      h.t,
      fmtEps(eps),
      fmtRevenue(rev),
      fmtTime(time),
    ];
  });

  // One-line diagnostic — records fetched vs portfolio tickers matched.
  const totalRecords = Array.isArray(universeEarnings) ? universeEarnings.length : 0;
  const earningsDiag = `_FMP returned ${totalRecords.toLocaleString('en-US')} earnings records in the next 30 days. Matched ${eBodyRows.length} portfolio tickers._`;

  let newEarningsTable;
  if (eBodyRows.length === 0) {
    newEarningsTable = `${ES_MARK}\n\n${earningsDiag}\n\n_No portfolio ticker reports earnings in the next 30 days._\n\n${EE_MARK}`;
  } else {
    const eAllRows = [eHeaderCells, ...eBodyRows];
    const eColWidths = eHeaderCells.map((_, i) => Math.max(3, ...eAllRows.map(r => (r[i] || '').length)));
    const eFmtRow = (cells) => '| ' + cells.map((c, i) => (c || '').padEnd(eColWidths[i])).join(' | ') + ' |';
    const eSepRow = '| ' + eColWidths.map(w => '-'.repeat(w)).join(' | ') + ' |';
    const eTableBody = [eFmtRow(eHeaderCells), eSepRow, ...eBodyRows.map(eFmtRow)].join('\n');
    newEarningsTable = `${ES_MARK}\n\n${earningsDiag}\n\n${eTableBody}\n\n${EE_MARK}`;
  }

  const now = new Date();
  const pad = n => String(n).padStart(2, '0');
  const ts = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}`;
  const okCount = results.filter(r => r.ok).length;
  const refreshLine = `**Last refreshed:** ${ts} — ${okCount}/${results.length} tickers (FMP)`;

  // IMPORTANT: use the function-form of replace() for any replacement string that
  // might contain `$` characters (EPS estimates, revenue figures). The string-form
  // interprets `$N` as a backreference — e.g. `$159M` would expand to `<capture
  // group 1 content>` + `59M`, re-injecting the prior EARNINGS region into the new
  // one. After repeated refreshes the region accumulates corrupted layers.
  let newContent = content.replace(TABLE_RE, () => newTable);
  newContent = newContent.replace(EARNINGS_RE, () => newEarningsTable);
  newContent = newContent.replace(/\*\*Last refreshed:\*\* .*/, () => refreshLine);

  await app.vault.modify(file, newContent);

  btn.disabled = false;
  btn.innerText = '↻ Refresh portfolio data';
  status.innerText = `✓ ${okCount}/${results.length} ok · ${ts}`;
};
```

## Holdings

<!--TABLE-START-->

| #   | Stock                | Ticker    | Exchange           | Weight           | Price     | 1W %   | 1M %   | 3M %    | 1Y %     | P/E LTM | P/E NTM | EV/EBIT LTM | EV/EBIT NTM | ROIC LTM | ROIC NTM | Rev Gr LFY | Rev Gr CFY | EPS Gr LFY | EPS Gr CFY |
| --- | -------------------- | --------- | ------------------ | ---------------- | --------- | ------ | ------ | ------- | -------- | ------- | ------- | ----------- | ----------- | -------- | -------- | ---------- | ---------- | ---------- | ---------- |
| 1   | SK Hynix             | 000660.KS | KRX (KRW)          | Full (25%+)      | 2,289,000 | +17.9% | +77.0% | +115.7% | +979.7%  | 21.5    | 8.1     | 19.9        | 25.3        | +28.5%   | +29.7%   | +46.8%     | +234.5%    | +118.7%    | +356.5%    |
| 2   | Sandisk              | SNDK      | NASDAQ (USD)       | High (10-25%)    | 1,679.4   | +13.6% | +57.8% | +164.3% | +4250.7% | 55.2    | 26.0    | 45.4        | -185.6      | +31.2%   | -9.0%    | +10.4%     | +166.8%    | -142.4%    | -670.5%    |
| 3   | AMD                  | AMD       | NASDAQ (USD)       | Medium (3.5-10%) | 520.59    | +11.4% | +54.4% | +160.0% | +360.6%  | 169.5   | 69.9    | 167.2       | 166.7       | +6.2%    | +8.1%    | +34.3%     | +44.0%     | +165.0%    | +178.8%    |
| 4   | Nvidia               | NVDA      | NASDAQ (USD)       | Medium (3.5-10%) | 213.39    | -0.9%  | +2.0%  | +20.4%  | +53.3%   | 32.5    | 45.5    | 27.3        | 50.3        | +63.0%   | +60.3%   | +65.5%     | -1.1%      | +66.7%     | -4.8%      |
| 5   | Palantir             | PLTR      | NASDAQ (USD)       | Medium (3.5-10%) | 141.84    | +3.6%  | +2.8%  | +3.4%   | +16.0%   | 148.8   | 97.3    | 162.5       | 193.5       | +22.3%   | +20.1%   | +56.2%     | +72.5%     | +231.6%    | +111.2%    |
| 6   | Cloudflare           | NET       | NYSE (USD)         | Medium (3.5-10%) | 226.58    | +4.8%  | +6.9%  | +31.6%  | +38.0%   | -921.1  | 189.1   | -1225       | 129.9       | -4.2%    | +18.4%   | +29.8%     | +29.8%     | -26.1%     | -513.2%    |
| 7   | TSMC                 | TSM       | NYSE (ADR) (USD)   | Medium (3.5-10%) | 422.67    | +4.5%  | +7.3%  | +12.8%  | +114.4%  | 30.9    | 0.8     | 25.4        | 23.0        | +25.8%   | +32.3%   | +33.0%     | +36.6%     | +49.8%     | +49.7%     |
| 8   | Broadcom             | AVGO      | NASDAQ (USD)       | Medium (3.5-10%) | 427.35    | +3.2%  | +5.4%  | +33.7%  | +76.6%   | 81.1    | 37.9    | 74.1        | 53.3        | +17.6%   | +26.2%   | +23.9%     | +61.6%     | +287.8%    | +129.5%    |
| 9   | Aixtron              | AIXA.DE   | XETRA (EUR)        | Medium (3.5-10%) | 59.20     | +10.3% | +32.5% | +114.5% | +374.0%  | 114.7   | 82.8    | 98.3        | 53.1        | +5.3%    | +11.1%   | -12.1%     | +2.2%      | -19.1%     | -6.0%      |
| 10  | Advantest            | 6857.T    | TSE (JPY)          | Medium (3.5-10%) | 26,340    | -1.9%  | -11.5% | -1.9%   | +244.6%  | 51.0    | 56.8    | 37.5        | 58.4        | +42.6%   | +32.8%   | +44.7%     | -4.0%      | +135.4%    | -10.0%     |
| 11  | Ajinomoto            | 2802.T    | TSE (JPY)          | Medium (3.5-10%) | 5,142     | -3.0%  | +7.9%  | +3.5%   | +41.3%   | 36.9    | 38.5    | 30.3        | 31.5        | +9.1%    | +11.0%   | +3.5%      | +0.0%      | +98.3%     | -3.6%      |
| 12  | Murata Manufacturing | 6981.T    | TSE (JPY)          | Medium (3.5-10%) | 8,538     | +19.7% | +76.4% | +107.8% | +295.0%  | 66.6    | 71.3    | 49.9        | 45.0        | +8.4%    | +9.1%    | +5.0%      | -1.2%      | +2.0%      | -6.2%      |
| 13  | Vicor                | VICR      | NASDAQ (USD)       | Medium (3.5-10%) | 346.01    | +29.1% | +34.8% | +71.8%  | +709.0%  | 115.1   | 124.9   | 132.5       | 205.7       | +12.9%   | +10.4%   | +13.5%     | +39.8%     | +1764.3%   | +5.4%      |
| 14  | Lumentum             | LITE      | NASDAQ (USD)       | Low<br>(<3.5%)   | 875.37    | -7.6%  | +2.0%  | +24.9%  | +1060.8% | 142.3   | 106.4   | 243.8       | -3343       | +3.7%    | -0.7%    | +21.0%     | +81.9%     | +104.6%    | +2064.5%   |
| 15  | Shopify              | SHOP      | NYSE (USD)         | Low<br>(<3.5%)   | 112.57    | +9.3%  | -7.2%  | -6.8%   | +4.5%    | 110.1   | 61.6    | 91.9        | 58.6        | +10.4%   | +25.6%   | +30.1%     | +26.6%     | -39.4%     | +92.3%     |
| 16  | Take-Two Interactive | TTWO      | NASDAQ (USD)       | Low<br>(<3.5%)   | 218.04    | -4.2%  | +1.3%  | +3.1%   | -3.3%    | -135.5  | 55.8    | -707.7      | -20.5       | -0.8%    | -49.8%   | +18.2%     | +0.5%      | +93.7%     | -341.2%    |
| 17  | Lam Research         | LRCX      | NASDAQ (USD)       | Low<br>(<3.5%)   | 317.33    | +3.9%  | +27.6% | +35.7%  | +277.1%  | 59.1    | 55.9    | 52.3        | 54.8        | +42.8%   | +50.6%   | +23.7%     | +25.7%     | +43.1%     | +36.2%     |
| 18  | Applied Materials    | AMAT      | NASDAQ (USD)       | Low<br>(<3.5%)   | 449.79    | +4.1%  | +17.6% | +20.8%  | +182.0%  | 42.0    | 36.9    | 33.5        | 29.0        | +21.6%   | +44.0%   | +4.4%      | +17.3%     | +0.6%      | +39.9%     |
| 19  | KLA Corp             | KLAC      | NASDAQ (USD)       | Low<br>(<3.5%)   | 1,928.6   | +2.1%  | +6.2%  | +26.5%  | +149.2%  | 54.1    | 52.1    | 46.5        | 49.5        | +36.3%   | +40.6%   | +23.9%     | +11.2%     | +49.8%     | +21.3%     |
| 20  | ASM International    | ASM.AS    | Euronext AMS (EUR) | Low<br>(<3.5%)   | 894.00    | -0.8%  | +10.4% | +25.2%  | +79.7%   | 44.1    | 40.9    | 36.8        | 32.5        | +17.1%   | +29.7%   | +8.2%      | +24.5%     | +5.8%      | +47.9%     |
| 21  | Palo Alto Networks   | PANW      | NASDAQ (USD)       | Low<br>(<3.5%)   | 257.80    | -1.1%  | +42.0% | +73.1%  | +38.7%   | 139.8   | 69.9    | 100.2       | 36.9        | +5.8%    | +34.2%   | +14.9%     | +22.4%     | -56.0%     | +115.7%    |
| 22  | ServiceNow           | NOW       | NYSE (USD)         | Low<br>(<3.5%)   | 108.98    | +6.7%  | +22.6% | +0.9%   | -46.3%   | 64.2    | 26.2    | 50.5        | 21.6        | +10.1%   | +56.7%   | +20.9%     | +22.0%     | +21.9%     | +145.8%    |
| 23  | BE Semiconductor     | BESI.AS   | Euronext AMS (EUR) | Low<br>(<3.5%)   | 287.60    | +5.1%  | +20.1% | +51.8%  | +160.3%  | 150.2   | 72.3    | 110.7       | 67.7        | +17.0%   | +30.4%   | -2.7%      | +57.4%     | -27.8%     | +139.5%    |
| 24  | Spotify              | SPOT      | NYSE (USD)         | Low<br>(<3.5%)   | 518.51    | -0.3%  | +16.9% | +0.7%   | -18.6%   | 33.6    | 40.3    | 32.8        | 16.5        | +27.1%   | +76.9%   | +9.7%      | +14.5%     | +91.1%     | +19.4%     |
| 25  | Marvell              | MRVL      | NASDAQ (USD)       | Low<br>(<3.5%)   | 204.28    | +4.0%  | +30.5% | +150.1% | +220.5%  | 71.3    | 71.8    | 60.6        | -1192       | +4.9%    | -0.6%    | +42.1%     | -0.1%      | +401.0%    | -8.2%      |
| 26  | Games Workshop       | GAW.L     | LSE (GBp)          | Low<br>(<3.5%)   | 19,750    | -3.9%  | +1.9%  | +10.4%  | +28.2%   | 31.6    | 3351    | 23.1        | 25.0        | +55.1%   | +55.9%   | +17.5%     | +5.5%      | +29.7%     | -0.9%      |
| 27  | Aehr Test Systems    | AEHR      | NASDAQ (USD)       | Low<br>(<3.5%)   | 100.33    | +5.6%  | +22.6% | +168.0% | +907.3%  | -269.8  | -748.7  | -201.8      | 788.0       | -8.3%    | +2.5%    | -10.9%     | -15.4%     | -111.6%    | +3.1%      |

<!--TABLE-END-->

## Charts

> [!tip] Holdings visualizer
> Reads the **Holdings table above** — no extra API calls. Renders from the last refresh and re-renders automatically when you click **Refresh** (Dataview re-runs on file change). Pick a metric (Returns / Valuation / Growth) from the dropdown; bars sort high→low and diverge from a zero center line for +/− metrics. Price is intentionally excluded — mixed currencies (KRW/JPY/EUR/USD) aren't comparable; all charted metrics are currency-neutral.

```dataviewjs
// =====================================================================
// Holdings chart — reads the rendered Holdings table above (no API calls).
// Renders from the last-refreshed table on note-open and re-renders
// automatically after a Refresh (Dataview re-runs dataviewjs on file change).
// Markers built by concatenation so this block's own source can't self-match.
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
if (!m) { dv.paragraph('⚠️ Holdings table not found — click **Refresh** above first.'); return; }

// ----- Parse the markdown table into row-cell arrays -----
const data = [];
for (const line of m[1].split('\n')) {
  if (!line.trim().startsWith('|') || line.includes('---')) continue;
  const c = line.split('|').map(x => x.trim());
  c.shift(); c.pop();                       // drop the empties around the outer pipes
  if (c.length < 20 || c[1] === 'Stock') continue;
  data.push(c);
}
// Cell indices match the Holdings header:
// 1 Stock · 6 1W · 7 1M · 8 3M · 9 1Y · 10 PE-LTM · 11 PE-NTM
// 12 EVEBIT-LTM · 13 EVEBIT-NTM · 16 RevGr-LFY · 17 RevGr-CFY · 18 EPSGr-LFY · 19 EPSGr-CFY

const METRICS = {
  'Return 1W':   { idx: 6,  unit: '%', sign: true  },
  'Return 1M':   { idx: 7,  unit: '%', sign: true  },
  'Return 3M':   { idx: 8,  unit: '%', sign: true  },
  'Return 1Y':   { idx: 9,  unit: '%', sign: true  },
  'P/E NTM':     { idx: 11, unit: 'x', sign: false },
  'P/E LTM':     { idx: 10, unit: 'x', sign: false },
  'EV/EBIT NTM': { idx: 13, unit: 'x', sign: false },
  'EV/EBIT LTM': { idx: 12, unit: 'x', sign: false },
  'Rev Gr CFY':  { idx: 17, unit: '%', sign: true  },
  'EPS Gr CFY':  { idx: 19, unit: '%', sign: true  },
  'Rev Gr LFY':  { idx: 16, unit: '%', sign: true  },
  'EPS Gr LFY':  { idx: 18, unit: '%', sign: true  },
};
const GROUPS = {
  'Returns':   ['Return 1W', 'Return 1M', 'Return 3M', 'Return 1Y'],
  'Valuation': ['P/E NTM', 'P/E LTM', 'EV/EBIT NTM', 'EV/EBIT LTM'],
  'Growth':    ['Rev Gr CFY', 'EPS Gr CFY', 'Rev Gr LFY', 'EPS Gr LFY'],
};

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

// ----- Controls -----
const wrap = dv.el('div', '', { attr: { style: 'padding:4px 0 2px;' } });
const ctrl = wrap.createEl('div', { attr: { style: 'display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin-bottom:12px;' } });
ctrl.createEl('span', { text: 'Metric', attr: { style: 'color:var(--text-muted); font-size:13px; font-weight:600;' } });
const sel = ctrl.createEl('select', { attr: { style: 'padding:5px 8px; border-radius:6px; font-size:13px; background:var(--background-primary); color:var(--text-normal); border:1px solid var(--background-modifier-border);' } });
for (const [grp, keys] of Object.entries(GROUPS)) {
  const og = sel.createEl('optgroup', { attr: { label: grp } });
  for (const k of keys) { const o = og.createEl('option', { text: k }); o.value = k; }
}
sel.value = 'Return 1Y';
const sortBtn = ctrl.createEl('button', { text: 'Sort ▼ high→low', attr: { style: 'padding:5px 10px; font-size:12px; cursor:pointer; border-radius:6px; border:1px solid var(--background-modifier-border); background:var(--background-primary); color:var(--text-normal);' } });
let descending = true;

const chart = wrap.createEl('div', {});

// ----- Render -----
function render() {
  const key = sel.value;
  const meta = METRICS[key];
  const idx = meta.idx, unit = meta.unit, sign = meta.sign;
  chart.empty();

  const series = data.map(c => ({ name: c[1], v: parseNum(c[idx]) }));
  const present = series.filter(s => s.v != null);
  const missing = series.filter(s => s.v == null);
  present.sort((a, b) => descending ? b.v - a.v : a.v - b.v);
  const ordered = [...present, ...missing];

  if (!present.length) {
    chart.createEl('div', { text: 'No data for this metric yet — click Refresh above.', attr: { style: 'color:var(--text-muted); padding:8px 0;' } });
    return;
  }

  // Robust scale: cap bar length at the 90th percentile of |value| so one outlier
  // (e.g. a 3351x P/E) doesn't crush every other bar. True values still print as labels.
  const cap = Math.max(pctile(present.map(s => Math.abs(s.v)), 0.90), 1e-9);
  const hasNeg = present.some(s => s.v < 0);

  const fmt = (v) => v == null ? '—'
    : unit === '%' ? (v >= 0 ? '+' : '') + v.toFixed(1) + '%'
    : v.toFixed(Math.abs(v) >= 1000 ? 0 : 1) + 'x';

  const GREEN = 'var(--color-green, #3aa675)';
  const RED   = 'var(--color-red, #c0504d)';
  const ACC   = 'var(--interactive-accent, #5b6bf0)';
  const colorOf = (v) => sign ? (v >= 0 ? GREEN : RED) : (v >= 0 ? ACC : RED);

  const grid = chart.createEl('div', { attr: { style: 'display:flex; flex-direction:column; gap:3px; font-size:12px;' } });
  for (const s of ordered) {
    const row = grid.createEl('div', { attr: { style: 'display:grid; grid-template-columns:150px 1fr 70px; align-items:center; gap:8px;' } });
    row.createEl('div', { text: s.name, attr: { style: 'text-align:right; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; color:var(--text-normal);' } });

    const track = row.createEl('div', { attr: { style: 'position:relative; height:15px; background:var(--background-modifier-border); border-radius:3px; overflow:hidden;' } });
    if (s.v != null) {
      const frac = Math.min(Math.abs(s.v), cap) / cap;
      const pos = s.v >= 0;
      if (hasNeg) {
        const half = frac * 50;
        track.createEl('div', { attr: { style:
          'position:absolute; top:0; height:100%; background:' + colorOf(s.v) + '; ' +
          (pos ? 'left:50%; width:' + half + '%; border-radius:0 3px 3px 0;'
               : 'right:50%; width:' + half + '%; border-radius:3px 0 0 3px;') } });
        track.createEl('div', { attr: { style: 'position:absolute; left:50%; top:0; bottom:0; width:1px; background:var(--text-faint);' } });
      } else {
        track.createEl('div', { attr: { style:
          'position:absolute; left:0; top:0; height:100%; width:' + (frac * 100) + '%; background:' + colorOf(s.v) + '; border-radius:3px;' } });
      }
    }
    row.createEl('div', { text: fmt(s.v), attr: { style: 'text-align:left; font-variant-numeric:tabular-nums; color:' + (s.v == null ? 'var(--text-faint)' : 'var(--text-muted)') + ';' } });
  }

  const note = chart.createEl('div', { attr: { style: 'color:var(--text-faint); font-size:11px; margin-top:10px; line-height:1.5;' } });
  note.setText(key + ' · ' + present.length + ' holdings'
    + (missing.length ? ' (+' + missing.length + ' with no data)' : '')
    + ' · bars scaled to ' + fmt(cap) + '; outliers max out, labels show true values'
    + (hasNeg ? ' · diverging from a zero center line' : ''));
}

sel.onchange = render;
sortBtn.onclick = () => { descending = !descending; sortBtn.setText(descending ? 'Sort ▼ high→low' : 'Sort ▲ low→high'); render(); };
render();
```

> [!tip] Scatter — plot any two of growth / valuation / ROIC
> Two dropdowns set the **X** and **Y** axes (Growth, Valuation P/E & EV/EBIT, or ROIC). Each dot is a holding; **size & colour = weight tier**. The dashed **median crosshair** splits the book into quadrants — with ROIC on X and EV/EBIT on Y, the bottom-right is the quality-at-a-discount corner. Hover a dot for exact values. Axes auto-clip to an IQR fence so one extreme multiple doesn't flatten the cloud; off-scale names pin to the edge with a ring.

```dataviewjs
// =====================================================================
// Holdings scatter — plot any two metrics (growth / valuation / ROIC) on
// X vs Y. Reads the Holdings table above (no API calls); re-renders on
// Refresh. Median crosshair = quadrants; dots colour-/size-coded by weight
// tier. Axes clipped to a Tukey (IQR) fence so one outlier doesn't squash
// the cloud — off-scale points pin to the edge with a ring.
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
if (!m) { dv.paragraph('⚠️ Holdings table not found — click **Refresh** above first.'); return; }

const data = [];
for (const line of m[1].split('\n')) {
  if (!line.trim().startsWith('|') || line.includes('---')) continue;
  const c = line.split('|').map(x => x.trim());
  c.shift(); c.pop();
  if (c.length < 20 || c[1] === 'Stock') continue;
  data.push(c);
}

const METRICS = {
  'Rev Gr CFY':  { idx: 17, unit: '%' },
  'Rev Gr LFY':  { idx: 16, unit: '%' },
  'EPS Gr CFY':  { idx: 19, unit: '%' },
  'EPS Gr LFY':  { idx: 18, unit: '%' },
  'P/E NTM':     { idx: 11, unit: 'x' },
  'P/E LTM':     { idx: 10, unit: 'x' },
  'EV/EBIT NTM': { idx: 13, unit: 'x' },
  'EV/EBIT LTM': { idx: 12, unit: 'x' },
  'ROIC NTM':    { idx: 15, unit: '%' },
  'ROIC LTM':    { idx: 14, unit: '%' },
};
const GROUPS = {
  'Growth':    ['Rev Gr CFY', 'Rev Gr LFY', 'EPS Gr CFY', 'EPS Gr LFY'],
  'Valuation': ['P/E NTM', 'P/E LTM', 'EV/EBIT NTM', 'EV/EBIT LTM'],
  'ROIC':      ['ROIC NTM', 'ROIC LTM'],
};

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
const median = (arr) => pctile(arr, 0.5);
const fence = (vals) => {                 // Tukey IQR fence → robust axis domain
  const q1 = pctile(vals, 0.25), q3 = pctile(vals, 0.75), iqr = q3 - q1;
  let lo = Math.max(Math.min(...vals), q1 - 1.5 * iqr);
  let hi = Math.min(Math.max(...vals), q3 + 1.5 * iqr);
  if (lo === hi) { lo -= 1; hi += 1; }
  const pad = (hi - lo) * 0.08;
  return [lo - pad, hi + pad];
};
const fmt = (v, unit) => v == null ? '—'
  : unit === '%' ? (v >= 0 ? '+' : '') + v.toFixed(0) + '%'
  : v.toFixed(Math.abs(v) >= 1000 ? 0 : 1) + 'x';

const TIERS = [
  { test: w => /^Full/.test(w),   label: 'Full',   color: 'var(--color-red, #d4504e)',    r: 8 },
  { test: w => /^High/.test(w),   label: 'High',   color: 'var(--color-orange, #e08c3b)', r: 7 },
  { test: w => /^Medium/.test(w), label: 'Medium', color: 'var(--color-green, #3aa675)',  r: 6 },
  { test: w => /^Low/.test(w),    label: 'Low',    color: 'var(--text-muted, #8a8f98)',   r: 5 },
];
const tierOf = (w) => TIERS.find(t => t.test(w)) || TIERS[3];

// ----- Controls -----
const wrap = dv.el('div', '', { attr: { style: 'padding:4px 0 2px;' } });
const ctrl = wrap.createEl('div', { attr: { style: 'display:flex; gap:14px; align-items:center; flex-wrap:wrap; margin-bottom:8px;' } });
const mkSel = (label, def) => {
  const g = ctrl.createEl('span', { attr: { style: 'display:inline-flex; gap:6px; align-items:center;' } });
  g.createEl('span', { text: label, attr: { style: 'color:var(--text-muted); font-size:13px; font-weight:600;' } });
  const s = g.createEl('select', { attr: { style: 'padding:5px 8px; border-radius:6px; font-size:13px; background:var(--background-primary); color:var(--text-normal); border:1px solid var(--background-modifier-border);' } });
  for (const [grp, keys] of Object.entries(GROUPS)) {
    const og = s.createEl('optgroup', { attr: { label: grp } });
    for (const k of keys) { const o = og.createEl('option', { text: k }); o.value = k; }
  }
  s.value = def;
  return s;
};
const xSel = mkSel('X', 'Rev Gr CFY');
const ySel = mkSel('Y', 'EV/EBIT NTM');

const chart = wrap.createEl('div', {});
const SVGNS = 'http://www.w3.org/2000/svg';
const svgAdd = (parent, tag, attrs, text) => {
  const e = document.createElementNS(SVGNS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (text != null) e.textContent = text;
  parent.appendChild(e);
  return e;
};

function render() {
  chart.empty();
  const xk = xSel.value, yk = ySel.value;
  const xm = METRICS[xk], ym = METRICS[yk];

  const pts = data.map(c => ({
    name: c[1], ticker: c[2], tier: tierOf(c[4]),
    x: parseNum(c[xm.idx]), y: parseNum(c[ym.idx]),
  })).filter(p => p.x != null && p.y != null);
  const dropped = data.length - pts.length;

  if (pts.length < 2) {
    chart.createEl('div', { text: 'Not enough data for this pair yet — click Refresh above.', attr: { style: 'color:var(--text-muted); padding:8px 0;' } });
    return;
  }

  const W = 720, H = 470, mL = 60, mR = 18, mT = 16, mB = 54;
  const plotW = W - mL - mR, plotH = H - mT - mB;
  const xDom = fence(pts.map(p => p.x)), yDom = fence(pts.map(p => p.y));
  const clamp = (v, d) => Math.max(d[0], Math.min(d[1], v));
  const sx = v => mL + (clamp(v, xDom) - xDom[0]) / (xDom[1] - xDom[0]) * plotW;
  const sy = v => mT + plotH - (clamp(v, yDom) - yDom[0]) / (yDom[1] - yDom[0]) * plotH;

  const svg = svgAdd(chart, 'svg', { viewBox: `0 0 ${W} ${H}`, style: 'width:100%; height:auto;', preserveAspectRatio: 'xMidYMid meet' });
  const AXIS = 'var(--text-faint, #999)', TXT = 'var(--text-muted, #888)', GRID = 'var(--background-modifier-border, #ddd)';

  svgAdd(svg, 'rect', { x: mL, y: mT, width: plotW, height: plotH, fill: 'none', stroke: GRID, 'stroke-width': 1 });

  for (let i = 0; i <= 4; i++) {
    const xv = xDom[0] + (xDom[1] - xDom[0]) * i / 4;
    const px = mL + plotW * i / 4;
    svgAdd(svg, 'line', { x1: px, y1: mT, x2: px, y2: mT + plotH, stroke: GRID, 'stroke-width': 0.5, 'stroke-dasharray': '2 3' });
    svgAdd(svg, 'text', { x: px, y: mT + plotH + 16, fill: TXT, 'font-size': 10, 'text-anchor': 'middle' }, fmt(xv, xm.unit));
    const yv = yDom[0] + (yDom[1] - yDom[0]) * i / 4;
    const py = mT + plotH - plotH * i / 4;
    svgAdd(svg, 'line', { x1: mL, y1: py, x2: mL + plotW, y2: py, stroke: GRID, 'stroke-width': 0.5, 'stroke-dasharray': '2 3' });
    svgAdd(svg, 'text', { x: mL - 6, y: py + 3, fill: TXT, 'font-size': 10, 'text-anchor': 'end' }, fmt(yv, ym.unit));
  }

  const mx = sx(median(pts.map(p => p.x))), my = sy(median(pts.map(p => p.y)));
  svgAdd(svg, 'line', { x1: mx, y1: mT, x2: mx, y2: mT + plotH, stroke: AXIS, 'stroke-width': 1, 'stroke-dasharray': '5 4', opacity: 0.7 });
  svgAdd(svg, 'line', { x1: mL, y1: my, x2: mL + plotW, y2: my, stroke: AXIS, 'stroke-width': 1, 'stroke-dasharray': '5 4', opacity: 0.7 });

  for (const p of pts) {
    const cx = sx(p.x), cy = sy(p.y);
    const off = (p.x < xDom[0] || p.x > xDom[1] || p.y < yDom[0] || p.y > yDom[1]);
    const dot = svgAdd(svg, 'circle', { cx, cy, r: p.tier.r, fill: p.tier.color, 'fill-opacity': 0.78, stroke: off ? 'var(--text-normal)' : 'var(--background-primary)', 'stroke-width': off ? 1.5 : 1, 'stroke-dasharray': off ? '2 2' : '' });
    svgAdd(dot, 'title', {}, `${p.name} (${p.ticker})\n${xk}: ${fmt(p.x, xm.unit)}\n${yk}: ${fmt(p.y, ym.unit)}`);
    svgAdd(svg, 'text', { x: cx + p.tier.r + 2, y: cy + 3, fill: 'var(--text-normal)', 'font-size': 9.5 }, p.ticker);
  }

  svgAdd(svg, 'text', { x: mL + plotW / 2, y: H - 6, fill: 'var(--text-normal)', 'font-size': 12, 'font-weight': 600, 'text-anchor': 'middle' }, xk);
  svgAdd(svg, 'text', { x: 15, y: mT + plotH / 2, fill: 'var(--text-normal)', 'font-size': 12, 'font-weight': 600, 'text-anchor': 'middle', transform: `rotate(-90 15 ${mT + plotH / 2})` }, yk);

  const leg = chart.createEl('div', { attr: { style: 'display:flex; gap:14px; flex-wrap:wrap; margin-top:8px; font-size:11px; color:var(--text-muted);' } });
  for (const t of TIERS) {
    const item = leg.createEl('span', { attr: { style: 'display:inline-flex; align-items:center; gap:5px;' } });
    item.createEl('span', { attr: { style: `width:${Math.round(t.r * 1.4)}px; height:${Math.round(t.r * 1.4)}px; border-radius:50%; background:${t.color}; display:inline-block;` } });
    item.createEl('span', { text: t.label });
  }
  const cap = chart.createEl('div', { attr: { style: 'color:var(--text-faint); font-size:11px; margin-top:6px; line-height:1.5;' } });
  cap.setText(`${pts.length} holdings${dropped ? ` (${dropped} missing a value, omitted)` : ''} · dashed crosshair = medians (quadrants) · dot size/colour = weight tier · axes clipped to the IQR fence; ringed dots are off-scale, pinned to the edge (hover for true values)`);
}

xSel.onchange = render;
ySel.onchange = render;
render();
```

## Upcoming Earnings

> [!tip] FMP earnings calendar — next 30 days
> Refreshes with the **same button above**. One row per ticker reporting in the next 30 days, sorted by date. Tickers reporting later (or not at all in this window) are silently omitted.

<!--EARNINGS-START-->

_FMP returned 4,000 earnings records in the next 30 days. Matched 2 portfolio tickers._

| Date       | Days | Stock              | Ticker | EPS Est | Rev Est | Time |
| ---------- | ---- | ------------------ | ------ | ------- | ------- | ---- |
| 2026-06-02 | 5    | Palo Alto Networks | PANW   | $0.81   | $2.9B   | —    |
| 2026-06-03 | 6    | Broadcom           | AVGO   | $2.40   | $22.0B  | —    |

<!--EARNINGS-END-->

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
- **Active set = rendered table** (not the `HOLDINGS` array): the script parses the existing markdown table on every refresh to determine which tickers are currently active, and only fetches data for those. So:
  - **Deleting a row from the Holdings table → stays gone** on next refresh.
  - **Restore all**: clear the entire table body (leave just header + separator) → next refresh repopulates from full `HOLDINGS`.
  - **Adding a NEW ticker** that's already in `HOLDINGS` but deleted from the table: type the ticker into column 3 (Ticker) of any non-header row, refresh fills the rest.
  - **Adding a ticker NOT in `HOLDINGS`**: edit the `HOLDINGS = [...]` array in the dataviewjs block above (format: `{ n: 'Name', t: 'FMP_ticker', ex: 'Exchange', cur: 'Currency' }`), AND add a row with that ticker to the table. Refresh wires it up.
- **Row order auto-sorts by weight** on every refresh — Full → High → Medium → Low → unweighted (`—`). Within a tier, order follows the `HOLDINGS` array sequence (`Array.sort` is stable). Manual row reordering in the table is not preserved across a refresh; to reposition a name, change its Weight cell (moves it across tiers) or its `HOLDINGS` position (within a tier). The `#` column renumbers from the sorted result.
- **Upcoming Earnings table**: populated by the same Refresh click via a single FMP `earnings-calendar?from=today&to=today+30d` call. Endpoint is universe-only (symbol param is silently ignored), so we fetch and filter in JS against `HOLDINGS`. 30-day window stays comfortably under FMP's 4000-record-per-call cap. A failed call just empties the table — Holdings refresh is unaffected. **Important code invariant**: the `replace(EARNINGS_RE, ...)` call MUST use the function-form `() => newEarningsTable`, not the string-form. EPS/Rev cell values contain `$` followed by digits (e.g. `$159M`) which the string-form interprets as backreferences (`$1` = capture group 1 = the prior EARNINGS region content), causing the region to accumulate corrupted layers on every refresh.

## Log
- 2026-05-22: Initialised tracker — 32 holdings, 15 data columns + ticker/exchange/weight. Wired live refresh via FMP wholesale tier (`.data/config.json` gitignored). All 32 tickers verified coverable on wholesale. Native intl tickers chosen over ADRs where available (Hynix `000660.KS`, Murata `6981.T`, ASM/BESI Euronext `.AS`, Aixtron `AIXA.DE`, Games Workshop `GAW.L`, IQE `IQE.L`, Sivers `SIVE.ST`, Yancoal `YAL.AX`). EV/EBIT computed from EV/EBITDA × margin ratio. Note: existing weight column values preserved by the script — first click overwrites tickers/exchange labels with the script's authoritative HOLDINGS list.
- 2026-05-23: Added Upcoming Earnings widget below Holdings table. Same Refresh button populates both regions. New region marked by `<!--EARNINGS-START-->` / `<!--EARNINGS-END-->`. Schema: Date, Days, Stock, Ticker, EPS Est, Rev Est, Time — one row per ticker, sorted ascending. Empty-result fallback message rendered when no FMP earnings returned for any ticker.
- 2026-05-23: Fixed earnings widget data shape — first refresh populated every ticker row with the same garbage date (2026-05-22) and empty EPS/Rev/Time, because FMP's stable `earnings-calendar?symbol=X` ignores the `symbol` param and returns universe data. Reworked to make ONE universe call `from=today&to=today+90d` in parallel with the per-ticker holdings batch, then symbol-match the response against `HOLDINGS` in JS via a `Map`. Net: 32 redundant per-ticker fetches → 1 universe call (faster + correct). Added defensive field-name fallbacks (`epsEstimated` / `estimatedEPS` / `eps`; same for revenue) since FMP has shipped multiple variants across tiers.
- 2026-05-23: Widened earnings window 90d → 180d after first correct refresh returned only 3 rows (SNDK / AMAT / YAL.AX). Cause was not FMP coverage (YAL.AX is Australian — confirms international ARE covered on wholesale tier) but window timing: most semis report late August through mid-September, just past the 90d cutoff from May. 180d covers the next quarterly report for every holding regardless of cadence position. Also rewrote `[!tip]` callout + Notes section + empty-fallback message to stop blaming non-existent FMP international coverage gaps.
- 2026-05-23: Split earnings fetch into TWO parallel 90-day calls after 180d single call returned only 1 row (IQE.L) with the previously-visible Aug rows missing. FMP's earnings-calendar endpoint appears to cap `from`–`to` at ~90 days — wider ranges silently degrade the response. Two parallel calls (today→+90d, +91d→+180d) merge in JS. Also added a visible diagnostic line above the earnings table showing per-window record counts and portfolio match count — makes future "table looks wrong" failures fast to triage (zero counts vs. non-zero-but-no-matches indicate different root causes).
- 2026-05-23: Diagnostic line confirmed the real root cause — both 90d windows returned EXACTLY 4000 records each (a hard pagination cap, not a date-range cap). At ~110 earnings events/day globally, 90d × 110 = ~10,000 events, of which only 4000 survive truncation. Switched to **twelve parallel 15-day windows** (~1500 events each normal, ~2500 peak — safely under 4000 cap even in peak earnings weeks of late Jul / late Oct), generalized via a loop over `EARNINGS_WINDOW_DAYS` / `EARNINGS_TOTAL_DAYS`. Diagnostic line now shows per-window record counts (`w1=N, w2=M, ...`) with a ⚠️ warning if any window hits 4000 — automatic detection of needing to shrink further.
- 2026-05-23: Two-bug fix + simplification. **Bug 1 (formatting corruption)**: EARNINGS region accumulated stacked, mangled fragments across refreshes because JavaScript's `String.replace(regex, str)` interprets `$N` in the replacement string as a regex backreference. EPS / revenue cell values like `$159M` got expanded to `<capture group 1 content>59M`, re-injecting the previous EARNINGS region into the new one — recursively layering corruption. Fix: use function-form `replace(regex, () => str)` for all three replace calls (TABLE, EARNINGS, refreshLine) so `$` characters stay literal. **Bug 2 (overengineering)**: 12 parallel windows × 15 days = 180-day coverage was overkill. Dropped to **single 30-day window**, single fetch — covers actual user need (next month). Removed all window-array machinery, per-window diagnostic, and cap warning. Cleaned out the accumulated corruption inside `<!--EARNINGS-START-->` / `<!--EARNINGS-END-->` back to placeholder.
- 2026-05-23: Made the rendered Holdings table the active-set source of truth (previously `HOLDINGS` array was sole authority and re-added user-deleted rows on every refresh). Script now parses existing table rows during the same pass that preserves weights, collects a `presentTickers` Set, and filters `HOLDINGS` → `activeHoldings` accordingly. Both per-ticker fundamentals fetches and earnings-table builder now iterate `activeHoldings`. Recovery path: clear the table body to restore all (`presentTickers.size === 0` falls back to full `HOLDINGS`). Add path: type a ticker into column 3, refresh fills the row via `HOLDINGS` metadata lookup. Notes section updated to document the new mental model.
- 2026-05-29: Added Advantest (`6857.T`, TSE) and Ajinomoto (`2802.T`, TSE) at Medium — semis ATE + ABF-substrate supply-chain names. Sorted Holdings by weight desc (Full→High→Medium→Low) and reordered the `HOLDINGS` array to match so the sort persists across Refresh (script renders in array order). New rows show `—` until first Refresh populates them; deleted tickers moved to the array tail.
- 2026-05-29: Refresh now auto-sorts the Holdings table by weight tier (Full→High→Medium→Low→unweighted) on every click — `weightRank()` + stable `rows.sort()` before the `#` column is assigned, so order self-maintains regardless of `HOLDINGS` order or later in-table weight edits. Within-tier order still follows `HOLDINGS` sequence. Display number renumbered from sorted result. Makes the prior manual sort + array reorder self-correcting.
- 2026-05-29: Added `## Charts` section — a read-only companion `dataviewjs` block that parses the rendered Holdings table (no extra FMP calls) and draws diverging horizontal bars with a Returns/Valuation/Growth metric dropdown + sort toggle. Renders on note-open from the last refresh and re-renders automatically when Refresh modifies the file. Bar scale capped at the 90th percentile of |value| so outliers (e.g. GAW 3351x P/E, SNDK +4264% 1Y) don't crush the chart; true values always shown as labels. Price excluded (mixed-currency). Zero plugin dependency (no Charts plugin installed). Separate block by design — the refresh script is untouched.
- 2026-05-29: Added a second chart to `## Charts` — an SVG **scatter** (`document.createElementNS`, no plugin) with independent **X/Y dropdowns** spanning Growth (Rev/EPS, CFY & LFY), Valuation (P/E & EV/EBIT, NTM & LTM) and ROIC (LTM & NTM). Default X=Rev Gr CFY, Y=EV/EBIT NTM. Dots sized/coloured by weight tier; dashed median crosshair draws quadrants; hover shows name + true values. Axes clipped to a Tukey IQR fence so a single extreme multiple (e.g. GAW 3351x) doesn't flatten the cloud — off-scale names pin to the edge with a dashed ring. Same read-only table-parse + auto-rerender contract as the bar chart.
