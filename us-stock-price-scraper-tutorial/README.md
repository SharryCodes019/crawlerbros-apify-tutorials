# US Stock Price Scraper Tutorial: Run This Apify Actor with Python

Download historical stock price data (OHLCV) for US stocks, ETFs, and indices from Yahoo Finance. Get open, high, low, close prices, trading volume, dividends, and stock splits for any ticker at any timeframe from 1 minute to 1 month.

This repository shows how to run [US Stock Price Scraper](https://apify.com/crawlerbros/us-stock-price-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/us-stock-price-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/us-stock-price-scraper](https://apify.com/crawlerbros/us-stock-price-scraper)
- **SEO title:** US Stock Price Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Download historical stock price data (OHLCV) for US stocks, ETFs, and indices from Yahoo Finance. Get open, high, low, close prices, trading volume, dividends, and stock splits for any ticker at any timeframe from 1 minute to 1 month.

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

# US Stock Market Price Scraper

Download historical stock price data (OHLCV) for US stocks, ETFs, and indices from Yahoo Finance. Get open, high, low, close prices, trading volume, dividends, and stock splits for any ticker — at any timeframe from 1 minute to 1 month.

## What does US Stock Market Price Scraper do?

This actor downloads historical OHLCV (Open, High, Low, Close, Volume) price data from Yahoo Finance. It supports all US-listed stocks, ETFs, mutual funds, and major market indices across multiple timeframes, making it ideal for financial analysis, algorithmic trading, and portfolio research.

Use it to:

- Download historical stock price data for any US-listed ticker (AAPL, MSFT, TSLA, NVDA, etc.)
- Get candlestick OHLCV data at any timeframe from 1 minute to 1 month
- Scrape ETF price history (SPY, QQQ, VOO, VTI, ARKK, etc.)
- Track major index performance (S&P 500, Dow Jones, Nasdaq, Russell 2000)
- Build datasets for backtesting trading strategies
- Capture dividend payments and stock split history
- Scrape price data for crypto-adjacent stocks (COIN, MSTR, RIOT, MARA)
- Download commodity ETF prices (GLD, SLV, USO) and bond ETF prices (TLT, AGG, BND)

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `symbols` | Array of strings | Yes | Stock ticker symbols in uppercase (e.g. `AAPL`, `MSFT`, `SPY`, `^GSPC`) |
| `interval` | String | No | Candle interval: `1m`, `5m`, `15m`, `30m`, `1h`, `1d`, `1wk`, `1mo`. Defaults to `1d` |
| `startDate` | String | Yes | Start date in `YYYY-MM-DD` format |
| `endDate` | String | No | End date in `YYYY-MM-DD` format. **This date is exclusive** — data up to but not including this date is returned. Defaults to today |
| `proxy` | Object | No | Proxy configuration (recommended for datacenter IPs to avoid rate limiting) |

### Input example

```json
{
    "symbols": ["AAPL", "MSFT", "TSLA"],
    "interval": "1d",
    "startDate": "2025-01-01",
    "endDate": "2025-04-01"
}
```

## Output

Each record in the output dataset represents one price candle. All 9 fields are always present.

| Field | Type | Description |
|-------|------|-------------|
| `symbol` | String | Ticker symbol (e.g. `AAPL`) |
| `date` | String | `YYYY-MM-DD` for daily/weekly/monthly intervals; ISO 8601 datetime (e.g. `2025-01-02T09:30:00Z`) for intraday intervals |
| `open` | Number | Opening price |
| `high` | Number | Highest price during the period |
| `low` | Number | Lowest price during the period |
| `close` | Number | Closing price |
| `volume` | Integer | Number of shares traded |
| `dividends` | Number | Dividend amount paid (0 if none) |
| `stockSplits` | Number | Stock split ratio (0 if none) |

### Output example

```json
{
    "symbol": "AAPL",
    "date": "2025-03-10",
    "open": 227.5,
    "high": 230.1,
    "low": 226.8,
    "close": 229.45,
    "volume": 54321000,
    "dividends": 0,
    "stockSplits": 0
}
```

## Supported tickers

All tickers listed on Yahoo Finance are supported, including:

- **US Tech stocks**: AAPL, MSFT, GOOGL, AMZN, META, NVDA, TSLA, AMD, INTC, ORCL
- **Finance stocks**: JPM, BAC, GS, V, MA, WFC, C
- **Healthcare stocks**: JNJ, UNH, PFE, ABBV, LLY, MRK
- **Broad market ETFs**: SPY, QQQ, VOO, VTI, IWM, DIA, ARKK
- **Sector ETFs**: XLF (financials), XLE (energy), XLK (tech), XLV (healthcare), XLY (consumer)
- **Bond ETFs**: TLT, AGG, BND, HYG, LQD
- **Commodity ETFs**: GLD, SLV, USO, GDX
- **US Indices**: ^GSPC (S&P 500), ^DJI (Dow Jones), ^IXIC (Nasdaq Composite), ^RUT (Russell 2000)
- **Crypto-adjacent stocks**: COIN, MSTR, RIOT, MARA

## How much does it cost?

This actor uses Yahoo Finance as its data source, which is free. You only pay for Apify platform compute time. A typical run fetching daily data for multiple stocks over a year completes in under a minute.

## Limitations

- **Intraday data availability**: 1-minute data is available for the **last 7 days** only. 5m, 15m, 30m, and 1h intervals are available for the **last 60 days** only.
- **Market hours only**: Intraday data covers regular trading hours only (9:30 AM – 4:00 PM ET). Pre-market and after-hours trading data is not included.
- **End date is exclusive**: If you set `endDate` to `2025-03-15`, the last record returned will be March 14. To include March 15, set `endDate` to `2025-03-16`.
- **Weekend and holiday dates**: If `startDate` falls on a weekend or holiday, data starts from the next trading day automatically.
- **Historical depth**: Daily, weekly, and monthly data is available for decades on major tickers. Availability varies for smaller or newer stocks.
- **Delisted tickers**: Tickers that have been delisted may return no data or partial data depending on when they were removed.

## FAQ

### What timeframes are available?

`1m`, `5m`, `15m`, `30m`, `1h`, `1d`, `1wk`, `1mo`. The default is `1d` (daily).

### How far back does historical data go?

Daily, weekly, and monthly data goes back decades for major US stocks. Intraday intervals have limits: 1-minute data is only available for the **last 7 days**; 5m–1h data is available for the **last 60 days**.

### Why does my result start later than my startDate?

If `startDate` falls on a weekend, public holiday, or before a stock's IPO date, the first record will be from the next available trading day.

### Why does my result not include my endDate?

The `endDate` is exclusive — it is not included in the results. To include a specific date, set `endDate` to the following calendar day.

### Is this real-time data?

No. This actor downloads historical data. Intraday prices are typically delayed by at least 15–20 minutes from real-time. For the most recent trading day, data may not be available until after market close.

### Can I use this for backtesting trading strategies?

Yes. The OHLCV output format is compatible with most backtesting frameworks (Backtrader, Zipline, VectorBT, etc.) and financial analysis libraries (pandas, TA-Lib).

### Does it include pre-market and after-hours data?

No. Only regular trading hours (9:30 AM – 4:00 PM ET for US markets) are included in intraday intervals.

### What happens if I request an invalid ticker?

The actor pushes an error record to the dataset for that ticker and continues processing the remaining symbols. The run does not fail.

### Can I scrape multiple stocks in one run?

Yes. Pass multiple symbols in the `symbols` array. Each symbol is processed sequentially and all results are saved to the same dataset.

### Can I scrape crypto or forex?

Yahoo Finance lists some crypto pairs (e.g. `BTC-USD`, `ETH-USD`) and forex pairs (e.g. `EURUSD=X`). These tickers are supported and work the same way as stock tickers.

### Why does a valid ticker return no data?

Possible reasons: the date range is before the stock's IPO date, the ticker has been delisted, or you requested intraday data outside the supported lookback window (7 days for 1m, 60 days for 5m–1h).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/us-stock-price-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
