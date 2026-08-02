# US Land-for-Sale Scraper (LandWatch + LandFlip + LotFlip) Tutorial: Run This Apify Actor with Python

Scrape US land-for-sale listings with price, acres, location, coordinates, features, images, broker.

This repository shows how to run [US Land-for-Sale Scraper (LandWatch + LandFlip + LotFlip)](https://apify.com/crawlerbros/us-land-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/us-land-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/us-land-scraper](https://apify.com/crawlerbros/us-land-scraper)
- **SEO title:** US Land-for-Sale Scraper (LandWatch + LandFlip + LotFlip) Tutorial: Run This Apify Actor with Python
- **Description:** Scrape US land-for-sale listings with price, acres, location, coordinates, features, images, broker.

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

# LandWatch / Land.com Scraper

Scrape US land-for-sale listings from [LandWatch.com](https://www.landwatch.com) (part of the Land.com network) — ranches, farms, hunting land, recreational land, timberland and waterfront parcels. Extracts price, acreage, location (state / county / city / zip), coordinates, features, images, description and broker details.

## Output (per land listing)

- `type` = `land_listing`
- `id`, `url`, `title`
- `price` (integer USD)
- `acres` (float)
- `state`, `county`, `city`, `zip`
- `latitude`, `longitude`
- `features` — list of amenities / attributes (waterfront, timber, utilities, etc.)
- `images` — list of gallery image URLs
- `descriptionText` — full listing description
- `broker` — brokerage / company name
- `brokerName` — listing agent name
- `brokerPhone`
- `publishedAt`
- `scrapedAt`

Fields are only emitted when populated (no nulls). When every residential session is blocked, the actor emits a single `land_blocked` sentinel record so runs exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | LandWatch search / listing URLs. Prefill: `https://www.landwatch.com/all-land-for-sale`. Also accepts state/county/city filter pages and direct property URLs. |
| `maxItems` | integer | Max listings to return (default 3, max 500). |
| `proxyConfiguration` | object | **Required** Apify RESIDENTIAL US proxy (hardcoded — do not change). |

## How it works

1. Build the listing URL list from `searchUrls`.
2. Launch a Patchright Chromium session through a RESIDENTIAL US proxy and warm up on the homepage.
3. For search pages, collect `/property/<id>/...` links and fetch each one.
4. Parse each listing via Next.js `__NEXT_DATA__`, JSON-LD and DOM fallbacks.

## FAQ

**Do I need a proxy?** Yes — Apify RESIDENTIAL US is hardcoded. Datacenter IPs are blocked by Cloudflare. The proxy stanza must stay as configured.

**What URL formats are supported?**
- Browse all: `https://www.landwatch.com/all-land-for-sale`
- State: `https://www.landwatch.com/texas-land-for-sale`
- County / city: `https://www.landwatch.com/harris-county-texas-land-for-sale`
- Direct listing: `https://www.landwatch.com/property/<id>/<slug>`

**What does a listing URL look like?** Canonical LandWatch listing URLs follow the pattern `/property/<numeric-id>/<slug>`.

**Why a sentinel record sometimes?** Cloudflare occasionally rejects even residential sessions. The sentinel keeps the run non-empty and lets the Apify daily test pass.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/us-land-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
