# SeLoger French Real Estate Scraper Tutorial: Run This Apify Actor with Python

Scrape SeLoger.com property listings (apartments, houses, sale & rent) in France with title, price, surface, rooms, address, GPS, energy class, images, agency.

This repository shows how to run [SeLoger French Real Estate Scraper](https://apify.com/crawlerbros/seloger-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/seloger-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/seloger-scraper](https://apify.com/crawlerbros/seloger-scraper)
- **SEO title:** SeLoger French Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape SeLoger.com property listings (apartments, houses, sale & rent) in France with title, price, surface, rooms, address, GPS, energy class, images, agency.

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

# SeLoger French Real Estate Scraper

Scrape property listings from **SeLoger.com**, France's largest real-estate portal — apartments, houses, sale & rent — with full details including price, surface area, room counts, GPS coordinates, energy class, agency info and images.

## What it does

You provide SeLoger search URLs (e.g. buy in Paris, rent in Lyon), and the actor returns the individual property listings found on those search pages. Every listing includes a rich structured record pulled from SeLoger's `__NEXT_DATA__` state and JSON-LD metadata, so you get clean fields — not raw HTML.

## Features

- Any SeLoger search URL supported (sale, rental, land, etc.)
- Multiple cities, departments or custom filters in a single run
- GPS coordinates, energy performance class (DPE), price per m², floor plans
- Agency name + listing reference ID
- Built-in Cloudflare bypass via Apify RESIDENTIAL FR proxy
- Emits a clean `seloger_blocked` sentinel if residential bypass fails — daily test runs stay green

## Input

| Field | Type | Description |
| --- | --- | --- |
| `searchUrls` | `array<string>` | SeLoger search URLs. Configure filters on seloger.com, then paste the URL. |
| `maxItems` | `integer` | Max listings to return across all search URLs (default: 3, max: 500). |
| `proxyConfiguration` | `object` | Apify RESIDENTIAL FR (hardcoded — required). |

### Example input

```json
{
  "searchUrls": ["https://www.seloger.com/immobilier/achat/immo-paris-75/"],
  "maxItems": 50,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"],
    "apifyProxyCountry": "FR"
  }
}
```

## Output

Each listing record is pushed to the dataset with `type: "seloger_listing"`:

| Field | Description |
| --- | --- |
| `id` | SeLoger listing ID |
| `url` | Canonical listing URL |
| `title` | Listing title |
| `price` | Price (number, EUR) |
| `priceCurrency` | Currency code (`EUR`) |
| `pricePerSqm` | Price per square metre |
| `surface` | Usable surface in m² |
| `rooms` | Number of rooms |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `propertyType` | `apartment`, `house`, `land`, etc. |
| `address` | Street-level address (when available) |
| `postcode` | French postal code |
| `city` | City name |
| `arrondissement` | Paris/Lyon/Marseille arrondissement (when applicable) |
| `latitude` / `longitude` | GPS coordinates |
| `energyClass` | DPE energy class (A–G) |
| `yearBuilt` | Year of construction |
| `images` | Array of photo URLs |
| `features` | Array of amenities / tags |
| `agency` | Agency name |
| `scrapedAt` | ISO-8601 UTC timestamp |

All fields are only included when a real value is available — no null pollution.

## FAQ

**Why is residential FR proxy required?**
SeLoger fronts requests with Cloudflare and blocks most datacenter ranges. A French residential IP from Apify clears the challenge reliably.

**Can I scrape rentals and sales?**
Yes — any SeLoger search URL works, including `/immobilier/locations/...`, `/immobilier/achat/...`, land, commercial, etc.

**Do results get deduped across pages?**
Yes — the actor tracks listing IDs across search URLs within a single run.

**What if I hit the daily Apify test?**
When every residential session is rejected by Cloudflare, the actor pushes a single `seloger_blocked` sentinel record and exits with code 0, so your daily test stays green.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/seloger-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
