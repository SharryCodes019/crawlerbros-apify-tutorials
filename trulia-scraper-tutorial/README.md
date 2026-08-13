# Trulia Property Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings from Trulia, for sale, for rent, and sold. Supports search pages and direct property URLs. No login required.

This repository shows how to run [Trulia Property Scraper](https://apify.com/crawlerbros/trulia-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/trulia-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/trulia-scraper](https://apify.com/crawlerbros/trulia-scraper)
- **SEO title:** Trulia Property Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings from Trulia, for sale, for rent, and sold. Supports search pages and direct property URLs. No login required.

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

# Trulia Property Scraper

Extract publicly available property listing data from [Trulia](https://www.trulia.com) — no account or subscription required. Supports for-sale, for-rent, and sold listings. Accepts Trulia search pages and direct property URLs.

## What This Scraper Does

This actor fetches Trulia listing pages and extracts all publicly visible metadata: address, price, beds/baths, square footage, property type, listing date, agent details, photos, and more. With **Fetch Property Details** enabled, it also retrieves price history, tax history, full feature lists, and open house schedules.

## Input

| Field | Type | Description |
|---|---|---|
| **Start URLs** | List of strings | Trulia search pages (e.g. `https://www.trulia.com/for_sale/Austin,TX/`) or individual property pages. Apply filters on Trulia first, then paste the URL. |
| **Max Items** | Integer | Maximum number of listings to return from search pages (1–10,000). Default: 50. Ignored for direct property URLs. |
| **Fetch Property Details** | Boolean | Fetch the full detail page for each listing. Adds price history, tax history, features, and open house data. Doubles request count. Default: false. |
| **Proxy Configuration** | Proxy object | Residential proxy is **required** for reliable scraping. Trulia's PerimeterX protection blocks datacenter IPs. Defaults to Apify Residential proxy. |

### How to Use Filters

Apply any filter directly on Trulia's website (price range, beds, baths, property type, neighbourhood, etc.), then copy the URL from your browser's address bar and paste it as a Start URL. The scraper will paginate through all results matching those filters.

**Examples:**
- For-sale homes in Austin under $600K: `https://www.trulia.com/for_sale/Austin,TX/0-600000_price/`
- 3+ bedroom rentals in NYC: `https://www.trulia.com/for_rent/New_York,NY/3p_beds/`
- Recently sold condos in Boston: `https://www.trulia.com/sold/Boston,MA/CONDO_type/`

## Output

Each record represents one property listing. Fields marked `?` are optional and appear only when Trulia makes them publicly available.

| Field | Type | Description |
|---|---|---|
| `url` | string | Canonical Trulia property URL |
| `listingType` | string | `for_sale`, `for_rent`, or `sold` |
| `propertyType` | string? | e.g. Single Family Residential, Condo, Townhouse |
| `price` | integer? | Price in USD |
| `priceLabel` | string? | Formatted price (e.g. `$485,000`) |
| `address` | string? | Street address |
| `city` | string? | City |
| `state` | string? | State abbreviation |
| `zipCode` | string? | ZIP code |
| `neighborhood` | string? | Neighbourhood name |
| `latitude` | number? | Latitude |
| `longitude` | number? | Longitude |
| `bedrooms` | integer? | Number of bedrooms |
| `bathrooms` | number? | Number of bathrooms |
| `sqft` | integer? | Living area in square feet |
| `photos` | string[]? | Photo URLs |
| `listingDate` | string? | Date listed (ISO 8601) |
| `daysOnMarket` | integer? | Days on market |
| `agentName` | string? | Listing agent name |
| `brokerName` | string? | Brokerage name |
| `mlsId` | string? | MLS listing number |
| `priceHistory` | array? | Price change history *(requires Fetch Details)* |
| `taxHistory` | array? | Tax assessment history *(requires Fetch Details)* |
| `features` | object? | Full feature categories *(requires Fetch Details)* |
| `openHouses` | array? | Scheduled open houses *(requires Fetch Details)* |
| `agentPhone` | string? | Agent phone number *(requires Fetch Details)* |
| `scrapedAt` | string | ISO 8601 UTC scrape timestamp |

### Error Records

If a listing cannot be fetched or parsed, the record contains:

| Field | Description |
|---|---|
| `inputUrl` | The URL that was attempted |
| `error` | Human-readable error message |
| `scrapedAt` | Timestamp |

## Frequently Asked Questions

**Do I need a Trulia or Zillow account?**
No. This scraper only extracts data from public Trulia pages visible to any visitor without logging in.

**Is a proxy required?**
Yes, residential proxy is required when running on Apify cloud. Trulia uses PerimeterX bot detection that blocks datacenter IP addresses. The scraper defaults to Apify Residential proxy — no extra configuration needed. Running locally without proxy may work depending on your IP.

**How many listings can I get from one search URL?**
Trulia displays up to 40 listings per page. The scraper paginates automatically. A typical city search returns 100–2,000+ listings depending on market size. Use Max Items to cap the total.

**What data is NOT available?**
Fields requiring a Trulia/Zillow account: full school ratings and reports, detailed neighbourhood demographics, crime scores, mortgage pre-qualification data, full contact phone numbers (partial numbers may appear publicly), and private listing notes.

**Can I scrape sold listings?**
Yes. Use a URL starting with `https://www.trulia.com/sold/` — for example `https://www.trulia.com/sold/Austin,TX/`.

**What is the difference between search mode and direct property mode?**
Search mode paginates a search results page and collects many listings. Direct mode fetches a single property page — useful when you already have a list of specific property URLs. Both modes can be mixed in the same run.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/trulia-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
