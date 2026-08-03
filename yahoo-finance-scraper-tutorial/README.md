# Yahoo Finance Scraper Tutorial: Run This Apify Actor with Python

Pull live and historical stock data from Yahoo Finance with quote, OHLCV history, financials, dividends, splits, news, recommendations, institutional holders. Handles Yahoo's crumb-cookie auth automatically. HTTP-only, no proxy or API key required.

This repository shows how to run [Yahoo Finance Scraper](https://apify.com/crawlerbros/yahoo-finance-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/yahoo-finance-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/yahoo-finance-scraper](https://apify.com/crawlerbros/yahoo-finance-scraper)
- **SEO title:** Yahoo Finance Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Pull live and historical stock data from Yahoo Finance with quote, OHLCV history, financials, dividends, splits, news, recommendations, institutional holders. Handles Yahoo's crumb-cookie auth automatically. HTTP-only, no proxy or API key required.

## Run Locally

```bash
python -m pip install -r requirements.txt
cp .env.example .env
cp input.example.json input.json
python main.py
```

Set `APIFY_TOKEN` in `.env`, then edit `input.json` according to the actor README below. The script calls the actor and prints JSON results from the default dataset.

## Actor README

The following README is copied from the Apify actor page/source and should be treated as the source of truth.

# Yahoo Finance Scraper

Pull live and historical stock data from Yahoo Finance for one or more tickers — quote, OHLCV history, financials, dividends, splits, news, analyst recommendations, and institutional holders. Uses the `yfinance` library, which transparently handles Yahoo's crumb-cookie auth (the crumb expires every ~24h and is refreshed per session). HTTP-only — no proxy, no API key.

## What it does

You provide one or more ticker symbols; the actor:

1. Fetches Yahoo's full quote payload (`Ticker.info`) for each ticker — 180+ fields covering the company, market data, valuation ratios, dividend yield, beta.
2. Optionally pulls daily OHLCV history (`Ticker.history()`) for a configurable date range and interval.
3. Optionally pulls financials (income statement, balance sheet, cash flow), dividends, splits, news headlines, analyst recommendation breakdown, and institutional / mutual-fund holders.
4. Emits one record per ticker. Empty fields are omitted (no nulls). When Yahoo returns nothing for a ticker (delisted, typo, regional restriction), an `error` field is set instead of crashing.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `tickers` | array of strings (required) | `["AAPL", "MSFT"]` | Ticker symbols (US, ETFs, ADRs, foreign suffix tickers like `BP.L`, indices like `^GSPC`, currency pairs like `EUR=X`). |
| `startDate` | string | (today − 30 days) | Earliest date for historical OHLCV (`YYYY-MM-DD`). |
| `endDate` | string | (today) | Latest date for historical OHLCV (`YYYY-MM-DD`). |
| `interval` | enum | `1d` | One of `1d`, `5d`, `1wk`, `1mo`, `3mo`. |
| `includeHistory` | boolean | `true` | Include `history[]` (OHLCV daily candles). |
| `includeFinancials` | boolean | `false` | Include `financials.income` / `.balance` / `.cashflow`. |
| `includeDividends` | boolean | `true` | Include `dividends[]` history. |
| `includeSplits` | boolean | `true` | Include `splits[]` history. |
| `includeNews` | boolean | `true` | Include latest news headlines (capped at 25). |
| `includeRecommendations` | boolean | `true` | Include analyst recommendation breakdown. |
| `includeHolders` | boolean | `false` | Include institutional + mutual-fund holders (capped at 25 each). |
| `includeOptions` | boolean | `false` | Include the next-expiration options chain (calls + puts). Capped at 50 strikes per side. Also surfaces `optionExpirations[]` (next 20 expiry dates). |
| `includeEarningsCalendar` | boolean | `true` | Include `calendar` block with upcoming earnings/dividend dates and analyst earnings/revenue estimates. |
| `includeAnalystPriceTargets` | boolean | `true` | Include `analystPriceTargets` summary `{current, high, low, mean, median}`. |
| `includeInsiderTransactions` | boolean | `false` | Include the 25 most-recent insider transactions. |
| `includeSustainability` | boolean | `false` | Include ESG / sustainability scores when Yahoo publishes them (sparse coverage; many tickers return empty). |
| `includeQuarterlyFinancials` | boolean | `false` | Include quarterly income statement / balance sheet / cash flow under `financials.quarterly`. Only takes effect when `includeFinancials` is also on. |
| `includeEarningsHistory` | boolean | `true` | Include `earningsHistory[]` — last 4 quarters with `epsActual`, `epsEstimate`, `epsDifference`, `surprisePercent`. |
| `concurrency` | integer | `4` (1–16) | Number of tickers fetched in parallel. yfinance is mostly idle waiting on Yahoo, so concurrency speeds up bulk runs. Higher values may hit rate limits. |

### Example input

```json
{
  "tickers": ["AAPL", "MSFT", "GOOGL"],
  "startDate": "2024-01-01",
  "endDate": "2024-12-31",
  "interval": "1d",
  "includeHistory": true,
  "includeFinancials": true,
  "includeNews": true
}
```

## Output

One record per ticker. Empty fields are omitted (no nulls).

```json
{
  "ticker": "AAPL",
  "summaryUrl": "https://finance.yahoo.com/quote/AAPL/",
  "companyName": "Apple Inc.",
  "shortName": "Apple",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "country": "United States",
  "currency": "USD",
  "exchange": "NMS",
  "quoteType": "EQUITY",
  "website": "https://www.apple.com",
  "businessSummary": "Apple Inc. designs, manufactures, and markets…",
  "fullTimeEmployees": 161000,
  "marketCap": 3927938957312,
  "currentPrice": 267.55,
  "previousClose": 271.06,
  "open": 269.50,
  "dayHigh": 270.00,
  "dayLow": 266.50,
  "fiftyTwoWeekHigh": 280.00,
  "fiftyTwoWeekLow": 175.00,
  "volume": 50000000,
  "averageVolume": 60000000,
  "beta": 1.2,
  "trailingPE": 30.5,
  "forwardPE": 28.0,
  "trailingEps": 7.2,
  "dividendYield": 0.005,
  "dividendRate": 1.0,
  "dayChange": -3.51,
  "dayChangePercent": -1.2949,
  "history": [
    {"date": "2024-10-01", "open": 226.05, "high": 229.65, "low": 224.21, "close": 226.21, "volume": 47921400, "dividends": 0.0, "stock_splits": 0.0}
  ],
  "historyCount": 43,
  "dividends": [
    {"date": "2024-08-12", "value": 0.25}
  ],
  "dividendCount": 90,
  "splits": [
    {"date": "2020-08-31", "value": 4.0}
  ],
  "splitCount": 5,
  "financials": {
    "income": {"2024-09-30": {"Total_Revenue": 391035000000, "Net_Income": 93736000000}}
  },
  "news": [
    {"title": "Apple Q4 Earnings Beat Expectations", "url": "https://...", "publisher": "Reuters", "publishedAt": "2024-11-01T20:00:00Z"}
  ],
  "newsCount": 10,
  "recommendations": {
    "strongBuy": 12, "buy": 22, "hold": 13, "sell": 1, "strongSell": 0
  },
  "calendar": {
    "Earnings_Date": ["2026-05-01"],
    "Earnings_High": 2.16,
    "Earnings_Low": 1.75,
    "Earnings_Average": 1.95413,
    "Revenue_Average": 109689807090.0,
    "Dividend_Date": "2026-02-12",
    "Ex_Dividend_Date": "2026-02-09"
  },
  "analystPriceTargets": {
    "current": 267.22, "high": 350.0, "low": 215.0, "mean": 297.7055, "median": 300.0
  },
  "insiderTransactions": [
    {"Insider": "COOK TIMOTHY", "Shares": 5000.0, "Date": "2024-10-15"}
  ],
  "insiderTransactionCount": 25,
  "options": {
    "expiration": "2026-04-29",
    "calls": [
      {"strike": 250.0, "lastPrice": 18.5, "bid": 18.0, "ask": 19.0, "volume": 100, "openInterest": 5000, "impliedVolatility": 0.35, "inTheMoney": true}
    ],
    "puts": [
      {"strike": 250.0, "lastPrice": 1.5, "bid": 1.4, "ask": 1.6, "volume": 200, "openInterest": 3000, "impliedVolatility": 0.30, "inTheMoney": false}
    ]
  },
  "optionExpirations": ["2026-04-29", "2026-05-01", "2026-05-08"],
  "scrapedAt": "2024-12-16T14:23:11+00:00"
}
```

### Output fields

- **`ticker`** — uppercase ticker symbol.
- **`summaryUrl`** — Yahoo Finance summary page URL.
- **`companyName`** / **`shortName`** — full and short legal names.
- **`sector`** / **`industry`** / **`country`** — Yahoo's GICS-ish classification.
- **`currency`** — quote currency (`USD`, `EUR`, `GBP`, `JPY`, etc.).
- **`exchange`** — exchange code (`NMS`, `NYQ`, `LSE`).
- **`quoteType`** — `EQUITY`, `ETF`, `INDEX`, `CURRENCY`, `MUTUALFUND`, `CRYPTOCURRENCY`.
- **`website`** / **`businessSummary`** — company URL + long-form description.
- **`marketCap`** / **`fullTimeEmployees`** — fundamentals.
- **`currentPrice`** / **`previousClose`** / **`open`** / **`dayHigh`** / **`dayLow`** — intraday quote.
- **`fiftyTwoWeekHigh`** / **`fiftyTwoWeekLow`** — 52-week range.
- **`volume`** / **`averageVolume`** — share volume.
- **`beta`** / **`trailingPE`** / **`forwardPE`** / **`trailingEps`** — valuation ratios.
- **`dividendYield`** / **`dividendRate`** — current dividend stats.
- **`dayChange`** / **`dayChangePercent`** — derived from `currentPrice` − `previousClose`.
- **`history[]`** — OHLCV rows with `date`, `open`, `high`, `low`, `close`, `volume`, `dividends`, `stock_splits` (when `includeHistory: true`).
- **`historyCount`** — count of history rows emitted.
- **`dividends[]`** — `{date, value}` rows for each dividend payment in history (when `includeDividends: true`).
- **`splits[]`** — `{date, value}` rows for each stock split (when `includeSplits: true`).
- **`financials`** — nested `{income, balance, cashflow, quarterly?}` blocks, each keyed by period date with snake_cased line-item keys and float values (when `includeFinancials: true`). `quarterly` sub-block only when `includeQuarterlyFinancials: true`.
- **`news[]`** — `{title, url, publisher, publishedAt}` rows, capped at 25 (when `includeNews: true`).
- **`recommendations`** — single-row summary `{strongBuy, buy, hold, sell, strongSell}` of analyst ratings (when `includeRecommendations: true`).
- **`earningsHistory[]`** — up to 4 quarters of EPS data per record: `{quarter, epsActual, epsEstimate, epsDifference, surprisePercent}` (when `includeEarningsHistory: true`).
- **`holders`** — `{institutional[], mutualFund[]}` arrays of holder records (when `includeHolders: true`).
- **`calendar`** — upcoming earnings/dividend dates + analyst earnings/revenue estimates as a flat snake_cased dict (when `includeEarningsCalendar: true`).
- **`analystPriceTargets`** — `{current, high, low, mean, median}` floats (when `includeAnalystPriceTargets: true`).
- **`insiderTransactions[]`** — up to 25 recent insider transactions per record. Each row has the columns Yahoo publishes (insider name, shares, transaction date, etc.) (when `includeInsiderTransactions: true`).
- **`insiderTransactionCount`** — count of rows emitted.
- **`options`** — next-expiration option chain `{expiration, calls[], puts[]}` (when `includeOptions: true`). Each leg row has `{strike, lastPrice, bid, ask, volume, openInterest, impliedVolatility, inTheMoney}`. Capped at 50 strikes per side.
- **`optionExpirations[]`** — first 20 expiration dates (`YYYY-MM-DD`) when `includeOptions: true`.
- **`sustainability`** — ESG scores as a flat dict (when `includeSustainability: true` and Yahoo publishes data for the ticker).
- **`error`** — set when the ticker fetch failed (typo, delisted, regional restriction). When set, most other fields are absent.
- **`scrapedAt`** — ISO-8601 UTC timestamp.

## Use cases

- **Watchlist enrichment** — pull live quote + fundamentals for every ticker in a watchlist on schedule.
- **Backtesting / quant research** — bulk OHLCV history with adjustable date range and interval.
- **News monitoring** — daily run pulls the latest 25 articles per ticker; downstream alerts on title keywords.
- **Dividend / split tracking** — historical dividends + splits for income-portfolio modelling.
- **Analyst-rating aggregation** — track analyst sentiment changes over time by sampling recommendations.
- **Fundamental dumps** — full income statement / balance sheet / cash flow in a structured shape, ready for a spreadsheet.

## FAQ

**Does it need a proxy or API key?**
No. The `yfinance` library handles Yahoo's crumb-cookie authentication automatically (Yahoo started enforcing crumb cookies on their JSON API in 2023; yfinance bootstraps a crumb on first call). No API key, no signup.

**Why is the crumb cookie a thing?**
Yahoo Finance's REST endpoints (`query1.finance.yahoo.com/v10/finance/quoteSummary/...`) return 401 without a valid `Cookie` + `crumb` query param. yfinance acquires both by visiting `finance.yahoo.com` once per session, then attaches them to subsequent calls. This is invisible to you.

**Can I scrape pre-market or extended-hours data?**
The `currentPrice` / `volume` fields reflect Yahoo's regular session. For pre-/post-market quotes, supplement with the `info` keys `preMarketPrice` / `postMarketPrice` (which the actor doesn't currently surface — open an issue if you need them).

**What tickers are supported?**
Any symbol Yahoo Finance recognises:
- US equities: `AAPL`, `MSFT`, `BRK-B`
- ETFs: `SPY`, `VOO`, `QQQ`
- Foreign with suffix: `BP.L` (London), `0700.HK` (Hong Kong), `7203.T` (Tokyo)
- Indices: `^GSPC` (S&P 500), `^DJI` (Dow), `^IXIC` (Nasdaq)
- Currencies: `EUR=X`, `JPY=X`
- Crypto: `BTC-USD`, `ETH-USD`

**How fresh is the data?**
- `currentPrice`, `volume`, intraday OHLC: ~15-minute delayed for most US equities (Yahoo's free terms).
- News: real-time.
- Financials: refreshed within ~24h of company filings.
- History: end-of-day, refreshed after market close.

**What if a ticker is delisted or invalid?**
The record is emitted with `error: "no_data"` and the rest of the fields absent. The run continues for the remaining tickers.

**Why is the financials block sometimes missing for a ticker?**
- ETFs and indices don't report financials.
- Some foreign tickers ship limited statements.
- Yahoo occasionally returns empty financials for newly-IPO'd companies.

The actor follows an omit-empty contract — the `financials` field simply isn't emitted when there's no data.

**How does pagination of history work?**
`yfinance.Ticker.history()` returns the full date range in one call (no pagination needed). For multi-decade history, set `startDate` to your earliest date and `interval` to `1d`. Yahoo serves up to ~25 years of daily candles per request.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/yahoo-finance-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
