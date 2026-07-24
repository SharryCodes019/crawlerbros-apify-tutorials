# TradingView Scraper Tutorial: Run This Apify Actor with Python

Scrape TradingView's public scanner & symbol APIs with screen stocks / crypto / forex / futures, fetch ticker overviews, and run preset top-gainer / top-loser / most-active screens. Pure HTTP, no auth, no proxy.

This repository shows how to run [TradingView Scraper](https://apify.com/crawlerbros/tradingview-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tradingview-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tradingview-scraper](https://apify.com/crawlerbros/tradingview-scraper)
- **SEO title:** TradingView Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TradingView's public scanner & symbol APIs with screen stocks / crypto / forex / futures, fetch ticker overviews, and run preset top-gainer / top-loser / most-active screens. Pure HTTP, no auth, no proxy.

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

# TradingView Scraper

Pull live market data from **TradingView** — screen stocks, crypto, forex, futures, commodities, ETFs, bonds, and indices; fetch quotes for specific tickers; or run preset top-gainer / top-loser / most-active screens. Pure HTTP via TradingView's public scanner & symbol-search APIs. No auth, no proxy, no Playwright.

## What this actor does

- Hits the same `scanner.tradingview.com/{market}/scan` POST endpoint TradingView's screener UI uses — direct, deterministic, fast.
- 14 modes covering every reliable scanner axis + symbol search + URL-routing.
- 47 country / market codes for stock screening (`america`, `uk`, `germany`, `japan`, `india`, `brazil`, `australia`, …).
- Filter by market cap, daily volume, price range, sector, plus client-side keyword filtering.
- Symbol search via the typeahead endpoint — returns ISIN / CUSIP / CIK / exchange / type.
- Pagination handled automatically; up to 2000 records per run.

## Modes

| Mode | Endpoint | What you get |
|---|---|---|
| `screenStocks` | `/{market}/scan` POST | Stock screener — every fundamental & technical TradingView surfaces. |
| `screenCrypto` | `/crypto/scan` POST | Cryptocurrency pairs across major exchanges. |
| `screenForex` | `/forex/scan` POST | Currency pairs (G10 + emerging markets). |
| `screenFutures` | `/futures/scan` POST | Futures contracts globally. |
| `screenCommodities` | `/futures/scan` POST + subtype filter | Energy / metals / softs futures. |
| `screenETFs` | `/{market}/scan` POST + subtype filter | ETF rows from the stock scanner. |
| `screenBonds` | `/bonds/scan` POST | Bond instruments. |
| `screenIndices` | `/global/scan` POST | World indices. |
| `byTicker` | `/{market}/scan` POST + `symbols.tickers` | Specific symbols (`NASDAQ:AAPL`, `NYSE:JPM`, …). |
| `searchSymbol` | `symbol-search.tradingview.com/v3/` | Typeahead search — returns symbol metadata, ISIN/CUSIP. |
| `topGainers` / `topLosers` / `mostActive` | `/{market}/scan` POST + preset filters | Curated screens with liquidity floors. |
| `byUrl` | any | Paste a tradingview.com URL; auto-routes. |

## Output

Each row is a flat omit-empty record with `recordType` tagging the row.

Common fields:

- `symbol` (`NASDAQ:AAPL`), `ticker` (`AAPL`), `exchange` (`NASDAQ`), `name`, `description`
- `close`, `changePercent`, `changeAbsolute`, `volume`
- `marketCap`, `peRatio`, `epsTtm`, `dividendYield`
- `sector`, `industry`, `country`, `currency`
- `rsi`, `weeklyVolatility`, `perfWeek`, `perfMonth`, `perf3Month`, `perfYtd`, `perfYear`
- `high52Week`, `low52Week`
- `employeeCount`, `recommendAll`, `logoId`
- `url` — `https://www.tradingview.com/symbols/EXCH-TICKER/`
- Crypto: `rank`, `marketCap`, `volume24h`, `changePercent24h`, `circulatingSupply`, `totalSupply`
- Search: `isin`, `cusip`, `cikCode`, `typespecs[]`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | enum | `screenStocks` | One of the 14 modes above. |
| `market` | enum (47 countries) | `america` | Country code for stock-scanner modes. |
| `tickers` | array | – | List of `EXCHANGE:TICKER` strings (mode=byTicker). |
| `searchQuery` | string | `AAPL` | Free-text query (mode=searchSymbol). |
| `url` | string | – | tradingview.com URL (mode=byUrl). |
| `sortBy` | enum (22 options) | `market_cap_basic_desc` | Column + direction for the screener sort. |
| `minMarketCap` / `maxMarketCap` | int | – | USD market cap bounds. |
| `minVolume` | int | – | Daily volume floor. |
| `minPrice` / `maxPrice` | number | – | Last-price bounds. |
| `sectors` | array | – | Restrict to specific sectors. |
| `containsKeyword` | string | – | Client-side substring filter on symbol/name. |
| `maxItems` | int | `50` | Hard cap (1-2000). |

### Examples

**Top 20 US stocks by market cap**
```json
{
  "mode": "screenStocks",
  "market": "america",
  "sortBy": "market_cap_basic_desc",
  "maxItems": 20
}
```

**Today's biggest US gainers (liquid stocks only)**
```json
{
  "mode": "topGainers",
  "market": "america",
  "maxItems": 50
}
```

**Quotes for specific tickers**
```json
{
  "mode": "byTicker",
  "tickers": ["NASDAQ:AAPL", "NASDAQ:MSFT", "NYSE:JPM", "NYSE:BRK.B"]
}
```

**Indian stocks above 1B market cap, sorted by RSI (overbought)**
```json
{
  "mode": "screenStocks",
  "market": "india",
  "sortBy": "RSI_desc",
  "minMarketCap": 1000000000,
  "maxItems": 100
}
```

**Top 50 cryptocurrencies by market cap**
```json
{ "mode": "screenCrypto", "maxItems": 50 }
```

**Symbol search**
```json
{ "mode": "searchSymbol", "searchQuery": "Tesla" }
```

## FAQ

**Where does the data come from?** The same JSON the TradingView screener UI hits. Snapshot at request time, ~real-time for major exchanges, 15-min delayed for some.

**Why are my results cut at 150 / 300 / etc.?** The actor paginates in 150-row batches; raise `maxItems` (up to 2000) to get more. TradingView's screener returns up to ~5000 per market.

**Does it support all 47 markets?** Yes — every market in the dropdown is a valid `scanner.tradingview.com/{market}/scan` host.

**Can I get the symbol's price history / OHLC bars?** No — that requires WebSocket auth. This actor sticks to the snapshot scanner + symbol-search endpoints; both are anonymous and stable.

**Why is `sortBy` an enum and not a free-form column name?** A finite list of well-known sortable columns is more reliable. If you need a column that isn't in the dropdown, file a request.

## Limitations

- Real-time bid/ask, time-series OHLC, and watchlist sync require TradingView account auth — out of scope.
- Some markets (e.g. `bonds`, `global` indices) have a sparser column set; expect fewer fields per record.
- The `searchSymbol` endpoint returns up to ~150 results per query (TradingView's limit), regardless of `maxItems`.
- The actor calls `scanner.tradingview.com/{market}/scan` — the same JSON endpoints that power TradingView's own screener UI. These are public, anonymous, snapshot-only and rate-limited per IP; please respect TradingView's terms of service and avoid hammering the API at high concurrency.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tradingview-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
