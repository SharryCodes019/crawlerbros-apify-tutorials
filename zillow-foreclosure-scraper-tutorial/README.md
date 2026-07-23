# Zillow Foreclosure & Pre-Foreclosure Scraper Tutorial: Run This Apify Actor with Python

Scrape distressed properties from Zillow including foreclosures, pre-foreclosures, bank-owned (REO), and auctions. Returns property details plus auction date, lender, and loan amount.

This repository shows how to run [Zillow Foreclosure & Pre-Foreclosure Scraper](https://apify.com/crawlerbros/zillow-foreclosure-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/zillow-foreclosure-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/zillow-foreclosure-scraper](https://apify.com/crawlerbros/zillow-foreclosure-scraper)
- **SEO title:** Zillow Foreclosure & Pre-Foreclosure Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape distressed properties from Zillow including foreclosures, pre-foreclosures, bank-owned (REO), and auctions. Returns property details plus auction date, lender, and loan amount.

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

# Zillow Foreclosure & Pre-Foreclosure Scraper

Scrape distressed properties from Zillow — **foreclosures, pre-foreclosures, bank-owned (REO), and auctions**. Returns standard property fields plus distress-specific data including auction date, lender, and loan amount. Built for real estate investors tracking distressed inventory.

## What You Get

Each record includes:

| Field | Description |
|-------|-------------|
| `zpid` | Zillow property ID |
| `url` | Property detail page URL |
| `distressType` | `foreclosure`, `preForeclosure`, `bankOwned`, or `auction` |
| `address`, `city`, `state`, `zipCode` | Full address |
| `price` | Listing price |
| `zestimate` | Zillow home value estimate |
| `taxAssessedValue` | Tax-assessed value |
| `beds`, `baths`, `sqft` | Property specs |
| `lotAreaValue`, `lotAreaUnit` | Lot size |
| `daysOnZillow` | Days on market |
| `scrapedAt` | Scrape timestamp |

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `search` | string | — | Location: city (e.g. `Austin, TX`), neighborhood, or ZIP |
| `startUrls` | URL[] | — | Direct Zillow search URLs |
| `distressTypes` | string[] | all four | `foreclosure`, `preForeclosure`, `bankOwned`, `auction` |
| `maxItems` | integer | 100 | Max listings to return (1–500) |

One of `search` or `startUrls` is required.

## Use Cases

- **Real estate investing** — track distressed inventory before it hits the broader market
- **Wholesaling** — identify pre-foreclosure properties to approach owners directly
- **Auction prep** — research properties scheduled for foreclosure auction
- **REO acquisition** — surface bank-owned properties for buy-and-hold portfolios
- **Market intelligence** — quantify distress rate by city / ZIP / market cycle

## Usage Examples

**Find foreclosures and auctions in Phoenix:**
```json
{
  "search": "Phoenix, AZ",
  "distressTypes": ["foreclosure", "auction"],
  "maxItems": 50
}
```

## FAQs

**What's the difference between distress types?**
- `foreclosure` — active foreclosure listings for sale
- `preForeclosure` — properties in early foreclosure process (not yet listed)
- `bankOwned` — REO properties already owned by the lender
- `auction` — properties scheduled for foreclosure auction

**How many results can I get?**
Up to 500 per run. Zillow limits search results to 40 per page.

**Can I search multiple locations?**
Yes — provide multiple URLs via `startUrls`, or run the actor multiple times.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/zillow-foreclosure-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
