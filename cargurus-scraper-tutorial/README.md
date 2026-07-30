# CarGurus Car Listings Scraper Tutorial: Run This Apify Actor with Python

Scrape CarGurus car listings with search by make/model/zip/price, fetch single listings by ID, or scrape from a CarGurus search URL. Extracts pricing, deal ratings, mileage, dealer info, and more.

This repository shows how to run [CarGurus Car Listings Scraper](https://apify.com/crawlerbros/cargurus-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/cargurus-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/cargurus-scraper](https://apify.com/crawlerbros/cargurus-scraper)
- **SEO title:** CarGurus Car Listings Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape CarGurus car listings with search by make/model/zip/price, fetch single listings by ID, or scrape from a CarGurus search URL. Extracts pricing, deal ratings, mileage, dealer info, and more.

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

# CarGurus Car Listings Scraper

Scrape CarGurus car listings — search by make, model, ZIP code, and price range. Fetch single listings by ID or scrape all results from a CarGurus search URL. Extracts pricing, deal ratings, mileage, dealer info, fuel economy, and more.

## What data can you scrape?

- **Search listings** — find cars by make/model/ZIP/price with sort and filter options
- **Single listing** — full details for any car by its CarGurus listing ID
- **From URL** — paste any CarGurus search URL and scrape all results

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | select | `search`, `byListingId`, or `byUrl` |
| `make` | select | Car manufacturer (Toyota, Honda, BMW, etc.) |
| `model` | string | Model name (e.g. Camry, F-150) |
| `condition` | select | New, Used, or Certified Pre-Owned |
| `sortBy` | select | Sort order: best_deal, lowest_price, etc. |
| `zipCode` | string | 5-digit US ZIP code |
| `minPrice` | integer | Minimum price in USD |
| `maxPrice` | integer | Maximum price in USD |
| `maxMileage` | integer | Maximum odometer reading |
| `listingId` | string | Listing ID for byListingId mode |
| `url` | string | CarGurus search URL for byUrl mode |
| `maxItems` | integer | Max records to emit (default: 50) |

## Output

```json
{
  "listingId": "listing_12345",
  "vin": "1HGCV1F34KA123456",
  "url": "https://www.cargurus.com/Cars/inventorylisting/vdp.action?listingId=12345",
  "year": 2022,
  "make": "Toyota",
  "model": "Camry",
  "trim": "XSE",
  "price": 28500,
  "dealRating": "Great Deal",
  "mileage": 15000,
  "condition": "Used",
  "exteriorColor": "Midnight Black",
  "interiorColor": "Black",
  "transmission": "Automatic",
  "driveType": "FWD",
  "fuelType": "Gasoline",
  "mpgCity": 28,
  "mpgHighway": 39,
  "dealerName": "Toyota of Springfield",
  "dealerCity": "Springfield",
  "dealerState": "IL",
  "daysOnMarket": 12,
  "photoCount": 24,
  "primaryPhotoUrl": "https://static.cargurus.com/...",
  "recordType": "listing",
  "siteName": "CarGurus",
  "scrapedAt": "2026-05-10T12:00:00+00:00"
}
```

## FAQs

**Do I need a CarGurus account?**
No. CarGurus listings are publicly accessible.

**Why might I get no results?**
CarGurus uses JavaScript rendering for search results. The scraper extracts embedded JSON from HTML pages. Provide a ZIP code for more reliable broad searches. For deterministic smoke tests or exact-listing retrieval, prefer `byListingId` or `byUrl`.

**Why can make-specific searches drift?**
CarGurus sometimes serves a generic result set even when a make filter is present in the URL. The actor still applies client-side filters before emitting records, so an overly specific search can legitimately end up empty. When you need guaranteed output for monitoring, use a direct listing ID or a known-good search URL.

**What deal ratings does CarGurus use?**
Great Deal, Good Deal, Fair Deal, High Price, and Overpriced — based on market comparison.

**How many listings can I scrape?**
Set `maxItems` up to 1000. Pagination is handled automatically.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/cargurus-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
