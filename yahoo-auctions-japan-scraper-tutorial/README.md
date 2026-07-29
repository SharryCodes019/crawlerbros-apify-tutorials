# Yahoo Auctions Japan Scraper Tutorial: Run This Apify Actor with Python

Scrape auctions.yahoo.co.jp - Japan's largest auction site. Search auction listings by keyword, browse categories, filter by price range and sort order. Extracts titles, current bids, Buy It Now prices, conditions, end dates, seller info, and images.

This repository shows how to run [Yahoo Auctions Japan Scraper](https://apify.com/crawlerbros/yahoo-auctions-japan-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/yahoo-auctions-japan-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/yahoo-auctions-japan-scraper](https://apify.com/crawlerbros/yahoo-auctions-japan-scraper)
- **SEO title:** Yahoo Auctions Japan Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape auctions.yahoo.co.jp - Japan's largest auction site. Search auction listings by keyword, browse categories, filter by price range and sort order. Extracts titles, current bids, Buy It Now prices, conditions, end dates, seller info, and images.

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

# Yahoo Auctions Japan Scraper

Scrape auction listings from [auctions.yahoo.co.jp](https://auctions.yahoo.co.jp) — Japan's largest online auction platform. Search by keyword, browse categories, filter by price range, and sort by end time, price, or bids. No login or API key required.

## Features

- **Search auctions** by keyword
- **Browse categories** by category ID
- **Filter** by minimum/maximum bid price (JPY)
- **Sort** by ending soon, price, bids, newest, or popular
- Extracts titles, current prices, Buy It Now prices, conditions, end dates, bids, seller info, and images

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | string | `searchItems` (default) or `browseCategory` |
| `query` | string | Keyword to search (mode=searchItems) |
| `category` | string | Category ID for browsing (mode=browseCategory) |
| `sortBy` | string | `endTime`, `price_asc`, `price_desc`, `bids`, `new`, `popular` |
| `minPrice` | integer | Minimum current bid price in JPY |
| `maxPrice` | integer | Maximum current bid price in JPY |
| `maxItems` | integer | Maximum auctions to return (default: 20, max: 500) |

## Output

Each auction record includes:

| Field | Description |
|-------|-------------|
| `itemId` | Yahoo Auctions item ID |
| `title` | Auction listing title |
| `currentPrice` | Current bid price in JPY |
| `currency` | Always `JPY` |
| `buyItNowPrice` | Buy It Now price in JPY (if available) |
| `condition` | Item condition (New, Used, Used - Like New, etc.) |
| `bids` | Number of bids placed |
| `endDate` | Auction end date/time |
| `seller` | Seller name or ID |
| `imageUrl` | Item image URL |
| `category` | Auction category |
| `itemUrl` | Direct link to the auction listing |
| `scrapedAt` | ISO 8601 scrape timestamp |

## Usage Examples

**Search for PlayStation 5 ending soon:**
```json
{
  "mode": "searchItems",
  "query": "PlayStation 5",
  "sortBy": "endTime",
  "maxItems": 50
}
```

**Browse electronics category, sorted by bids:**
```json
{
  "mode": "browseCategory",
  "category": "23336",
  "sortBy": "bids",
  "maxItems": 100
}
```

## FAQ

**Does this require login or an API key?**
No. Yahoo Auctions Japan publicly accessible pages are scraped directly.

**What currency are prices in?**
All prices are in Japanese Yen (JPY).

**Can I search in Japanese?**
Yes — the `query` field accepts Japanese text.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/yahoo-auctions-japan-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
