# Binance Price Scraper Tutorial: Run This Apify Actor with Python

Scrape historical cryptocurrency price data (OHLCV candlestick data) from Binance. Get open, high, low, close prices and trading volume for any trading pair across multiple timeframes.

This repository shows how to run [Binance Price Scraper](https://apify.com/crawlerbros/binance-price-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/binance-price-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/binance-price-scraper](https://apify.com/crawlerbros/binance-price-scraper)
- **SEO title:** Binance Price Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape historical cryptocurrency price data (OHLCV candlestick data) from Binance. Get open, high, low, close prices and trading volume for any trading pair across multiple timeframes.

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

# Binance Price Scraper

Scrape historical cryptocurrency price data (OHLCV candlestick data) from Binance. Get open, high, low, close prices and trading volume for any trading pair across multiple timeframes.

## What does Binance Price Scraper do?

This actor downloads historical price data directly from Binance's public data archive. It supports all trading pairs available on Binance across Spot, USD-M Futures, and COIN-M Futures markets.

Use it to:

- Download historical Bitcoin, Ethereum, or any crypto price data
- Get OHLCV candle data at any timeframe from 1 second to 1 month
- Build datasets for crypto trading analysis and backtesting
- Track price movements across multiple trading pairs at once
- Access both Spot and Futures market data

## Input

| Field | Type | Description |
|-------|------|-------------|
| Trading Pair Symbols | Array of strings | Binance trading pair symbols in uppercase (e.g. `BTCUSDT`, `ETHUSDT`, `SOLUSDT`) |
| Candle Interval | String | Kline interval: `1s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1mo` |
| Start Date | String | Start date in `YYYY-MM-DD` format |
| End Date | String | End date in `YYYY-MM-DD` format (defaults to today) |
| Market Type | String | `spot`, `futures/um` (USD-M Futures), or `futures/cm` (COIN-M Futures) |
| Proxy | Object | Optional proxy configuration |

### Input example

```json
{
    "symbols": ["BTCUSDT", "ETHUSDT"],
    "interval": "1d",
    "startDate": "2025-01-01",
    "endDate": "2025-03-31",
    "market": "spot"
}
```

## Output

Each record in the output dataset represents one candlestick with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| symbol | String | Trading pair symbol (e.g. `BTCUSDT`) |
| openTime | String | Candle open time in ISO 8601 format |
| open | String | Opening price |
| high | String | Highest price during the candle |
| low | String | Lowest price during the candle |
| close | String | Closing price |
| volume | String | Trading volume in base asset |
| closeTime | String | Candle close time in ISO 8601 format |
| quoteAssetVolume | String | Trading volume in quote asset (e.g. USDT) |
| numberOfTrades | Integer | Number of trades during the candle |
| takerBuyBaseVolume | String | Taker buy volume in base asset |
| takerBuyQuoteVolume | String | Taker buy volume in quote asset |

### Output example

```json
{
    "symbol": "BTCUSDT",
    "openTime": "2025-01-01T00:00:00Z",
    "open": "93500.01000000",
    "high": "94500.00000000",
    "low": "92800.00000000",
    "close": "94200.50000000",
    "volume": "12345.67800000",
    "closeTime": "2025-01-01T23:59:59Z",
    "quoteAssetVolume": "1156789012.34000000",
    "numberOfTrades": 987654,
    "takerBuyBaseVolume": "6543.21000000",
    "takerBuyQuoteVolume": "612345678.90000000"
}
```

## How much will it cost to scrape Binance prices?

This actor downloads data from Binance's free public data archive, so data access is free. You only pay for Apify platform compute time. A typical run downloading daily candles for one trading pair over a year completes in under a minute.

## Supported trading pairs

All trading pairs listed on Binance are supported, including but not limited to:

- **BTC pairs**: BTCUSDT, BTCBUSD, BTCETH
- **ETH pairs**: ETHUSDT, ETHBTC, ETHBUSD
- **Altcoins**: SOLUSDT, ADAUSDT, DOTUSDT, XRPUSDT, DOGEUSDT, AVAXUSDT, LINKUSDT, MATICUSDT
- **Futures**: All USD-M and COIN-M perpetual and delivery contracts

## FAQ

### What timeframes are available?

Binance provides data at these intervals: 1 second, 1 minute, 3 minutes, 5 minutes, 15 minutes, 30 minutes, 1 hour, 2 hours, 4 hours, 6 hours, 8 hours, 12 hours, 1 day, 3 days, 1 week, and 1 month.

### How far back does the data go?

Data availability depends on when the trading pair was listed on Binance. For major pairs like BTCUSDT, data goes back to 2017.

### Is this real-time data?

No, this actor downloads historical data. Daily data is available the following day and monthly data is released on the first Monday of each month.

### Can I use this for backtesting trading strategies?

Yes! The OHLCV data output is in a standard format that can be directly imported into most backtesting frameworks and analysis tools.

### What is the difference between Spot and Futures data?

Spot data reflects prices on Binance's spot exchange (direct buying/selling). USD-M Futures data is from USDT-margined futures contracts, and COIN-M Futures is from coin-margined futures contracts.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/binance-price-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
