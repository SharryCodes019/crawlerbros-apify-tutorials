# Rightmove Property Scraper Tutorial: Run This Apify Actor with Python

Scrape Rightmove - UK's largest property portal. Search properties for sale, to rent, or fetch any listing page by URL. Returns price, bedrooms, bathrooms, address, agent, images, and more.

This repository shows how to run [Rightmove Property Scraper](https://apify.com/crawlerbros/rightmove-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/rightmove-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/rightmove-scraper](https://apify.com/crawlerbros/rightmove-scraper)
- **SEO title:** Rightmove Property Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Rightmove - UK's largest property portal. Search properties for sale, to rent, or fetch any listing page by URL. Returns price, bedrooms, bathrooms, address, agent, images, and more.

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

# Rightmove Property Scraper

Scrape property listings from **Rightmove** — the UK's largest property portal. Find properties for sale, to rent, or fetch any Rightmove search page by URL.

## What You Can Scrape

- **Properties for sale** — any UK city, town, or region
- **Rental properties** — flats, houses, rooms to rent across the UK
- **Any Rightmove listing page** — paste a URL and extract all listings

## Output Fields

Each record contains:

| Field | Description |
|---|---|
| `listingId` | Rightmove property ID |
| `url` | Full URL to the property listing |
| `title` | Property summary / description snippet |
| `address` | Display address (e.g. `"Cart Lane, London, E4"`) |
| `price` | Price as integer (GBP or per-month for rentals) |
| `priceText` | Formatted price string (e.g. `"£580,000"`) |
| `currency` | Currency code (`"GBP"`) |
| `priceFrequency` | Price period for rentals (e.g. `"monthly"`) |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `propertyType` | Property subtype (e.g. `"Apartment"`, `"Detached"`) |
| `tenure` | Tenure (e.g. `"Leasehold"`, `"Share Of Freehold"`) |
| `displaySize` | Floor area if available (e.g. `"786 sq. ft."`) |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |
| `agentName` | Estate agent / branch trading name |
| `branchName` | Branch display name |
| `agentPhone` | Agent contact telephone |
| `agentUrl` | Agent branch page URL |
| `imageUrls` | Array of property image URLs (up to 15) |
| `keyFeatures` | Bullet-point features from the listing |
| `listedDate` | Date the listing first appeared on Rightmove |
| `lastUpdatedDate` | Date of the most recent listing update |
| `updateReason` | Why the listing was updated (e.g. `"price_reduced"`) |
| `addedOrReduced` | Summary of when added or price reduced |
| `transactionType` | `"buy"` or `"rent"` |
| `isPremiumListing` | Whether this is a premium listing |
| `countryCode` | Country code (`"GB"`) |
| `scrapedAt` | ISO 8601 timestamp of when the record was scraped |

## Input

| Parameter | Type | Description |
|---|---|---|
| `mode` | select | `forSale` (default), `toRent`, or `byUrl` |
| `location` | string | UK city or region name (e.g. `London`, `Manchester`) |
| `startUrls` | array | Rightmove search or listing URLs (mode=byUrl only) |
| `propertyType` | select | Filter by property type (blank = any) |
| `minPrice` | integer | Minimum price in GBP |
| `maxPrice` | integer | Maximum price in GBP |
| `minBedrooms` | integer | Minimum number of bedrooms |
| `maxBedrooms` | integer | Maximum number of bedrooms |
| `radius` | select | Search radius in miles (default: this area only) |
| `sortBy` | select | Sort order: most recent, price high/low, etc. |
| `includeSSTC` | boolean | Include Sold STC / Let Agreed properties |
| `newHomesOnly` | boolean | New-build properties only |
| `maxItems` | integer | Max records to return (default: 50) |

## Example Inputs

**Properties for sale in Manchester:**
```json
{
  "mode": "forSale",
  "location": "Manchester",
  "maxItems": 50
}
```

**Rentals in Leeds under £1,500/month:**
```json
{
  "mode": "toRent",
  "location": "Leeds",
  "maxPrice": 1500,
  "maxItems": 30
}
```

**3+ bedroom detached houses in Bristol:**
```json
{
  "mode": "forSale",
  "location": "Bristol",
  "propertyType": "detached",
  "minBedrooms": 3,
  "maxItems": 50
}
```

**Fetch a specific search URL:**
```json
{
  "mode": "byUrl",
  "startUrls": ["https://www.rightmove.co.uk/property-for-sale/Birmingham.html?maxPrice=300000"],
  "maxItems": 100
}
```

## Use Cases

- **Property market research** — track pricing trends across UK cities
- **Investment analysis** — compare yields in different postcodes
- **Lead generation** — find recently listed or price-reduced properties
- **Portfolio monitoring** — track specific area markets over time
- **Data journalism** — housing affordability analysis

## Data Source

This actor scrapes **Rightmove** (`rightmove.co.uk`), the UK's largest property portal with over 900,000 properties listed at any time. Data is publicly accessible — no account or API key required.

## FAQ

**Which locations are supported?**
Any UK city, town, or region that Rightmove recognises by name. Examples: `London`, `Manchester`, `Edinburgh`, `Cardiff`, `Belfast`, `Oxford`, `Cambridge`, `Yorkshire`.

**How many properties can I scrape?**
Rightmove paginates results in groups of 24. The actor will paginate through all pages up to your `maxItems` limit.

**Does this scrape new-build developments?**
Yes — use the `newHomesOnly` flag to restrict to new builds, or leave it off to include all properties.

**Can I filter by postcode?**
Use the `byUrl` mode with a Rightmove search URL that includes your postcode as the location.

**What's the price format?**
Prices are returned as integers (GBP) in the `price` field, and as formatted strings in `priceText`. For rentals, the frequency (monthly/weekly) is in `priceFrequency`.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/rightmove-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
