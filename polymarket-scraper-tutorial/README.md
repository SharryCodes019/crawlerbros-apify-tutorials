# Polymarket Prediction Market Scraper Tutorial: Run This Apify Actor with Python

Scrape Polymarket prediction markets like search markets, trending by volume, browse events, fetch single market details, and get recently resolved markets. No auth required.

This repository shows how to run [Polymarket Prediction Market Scraper](https://apify.com/crawlerbros/polymarket-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/polymarket-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/polymarket-scraper](https://apify.com/crawlerbros/polymarket-scraper)
- **SEO title:** Polymarket Prediction Market Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Polymarket prediction markets like search markets, trending by volume, browse events, fetch single market details, and get recently resolved markets. No auth required.

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

# Polymarket Prediction Market Scraper

Scrape prediction market data from [Polymarket](https://polymarket.com) — the world's largest decentralized prediction market platform. Get real-time market probabilities, volumes, liquidity, and resolution data across categories like Politics, Sports, Crypto, Science, and more.

No API key required. No authentication needed.

## What data can you scrape?

- **Search markets** — find markets by keyword across all categories
- **Trending markets** — top markets sorted by 24-hour trading volume
- **Markets by event** — all markets within a specific event (e.g., "2024 US Election")
- **Single market lookup** — full details for a market by its condition ID
- **Resolved markets** — recently closed/resolved prediction markets

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | select | What to fetch: `search`, `trending`, `byEvent`, `byConditionId`, `resolved` |
| `query` | string | Search keyword (mode=search or mode=byEvent) |
| `conditionId` | string | Market condition ID (mode=byConditionId) |
| `category` | select | Filter by category: Sports, Politics, Crypto, Science, Business, Entertainment, Pop Culture, Other |
| `minVolume` | number | Filter markets below this total USD volume |
| `resolvedOnly` | boolean | Only return resolved/closed markets (default: false) |
| `activeOnly` | boolean | Only return currently active markets (default: true) |
| `maxItems` | integer | Maximum records to emit (1–1000, default 50) |

### Example inputs

**Trending markets:**
```json
{
  "mode": "trending",
  "maxItems": 20
}
```

**Search politics markets:**
```json
{
  "mode": "search",
  "query": "election",
  "category": "Politics",
  "maxItems": 50
}
```

**Get a specific market:**
```json
{
  "mode": "byConditionId",
  "conditionId": "0x..."
}
```

**Recently resolved markets:**
```json
{
  "mode": "resolved",
  "maxItems": 100
}
```

## Output

Each record contains:

| Field | Description |
|-------|-------------|
| `conditionId` | Unique market condition ID |
| `marketSlug` | URL slug for the market |
| `question` | The prediction question |
| `description` | Market description and resolution criteria |
| `outcomePrices` | Current probabilities as floats, e.g. [0.97, 0.03] |
| `outcomes` | Outcome labels, e.g. ["Yes", "No"] |
| `volume` | Total trading volume (USD) |
| `volume24hr` | 24-hour trading volume (USD) |
| `liquidity` | Current market liquidity (USD) |
| `startDate` | Market open date (ISO-8601) |
| `endDate` | Market resolution date (ISO-8601) |
| `resolved` | Whether the market has been resolved |
| `active` | Whether the market is currently active |
| `closed` | Whether the market is closed |
| `resolutionSource` | Data source used for resolution |
| `category` | Market category (Politics, Sports, Crypto, etc.) |
| `image` | Market image URL |
| `recordType` | Always "market" |
| `siteName` | Always "Polymarket" |
| `scrapedAt` | ISO-8601 scrape timestamp |

### Example output record

```json
{
  "conditionId": "0xabc123...",
  "marketSlug": "will-trump-win-2024",
  "question": "Will Trump win the 2024 US Presidential Election?",
  "outcomePrices": [0.97, 0.03],
  "outcomes": ["Yes", "No"],
  "volume": 12500000.0,
  "volume24hr": 450000.0,
  "liquidity": 3200000.0,
  "startDate": "2024-01-01T00:00:00Z",
  "endDate": "2024-11-05T23:59:59Z",
  "resolved": true,
  "active": false,
  "closed": true,
  "category": "Politics",
  "image": "https://polymarket-upload.s3.amazonaws.com/...",
  "recordType": "market",
  "siteName": "Polymarket",
  "scrapedAt": "2026-05-10T12:00:00+00:00"
}
```

## Market Categories

Sports, Politics, Crypto, Science, Business, Entertainment, Pop Culture, Other

## FAQ

**Do I need an API key?**
No. Polymarket's public Gamma API and CLOB API require no authentication.

**What does `outcomePrices` represent?**
The current market-implied probability for each outcome, expressed as a float between 0 and 1. For a YES/NO market, [0.97, 0.03] means 97% chance of YES.

**What is `conditionId`?**
A unique identifier (hash) for each market on Polymarket's CLOB (Central Limit Order Book). You can use it in `byConditionId` mode to fetch a specific market.

**Can I get historical data?**
The scraper fetches current/live data. For resolved markets, use `mode=resolved`.

**How is `volume24hr` different from `volume`?**
`volume` is the all-time total trading volume; `volume24hr` is the rolling 24-hour volume used to rank trending markets.

**What is `byEvent` mode?**
Events are groups of related markets (e.g., "2024 US Presidential Election" contains multiple individual candidate markets). This mode searches for an event by name and returns all markets within it.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/polymarket-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
