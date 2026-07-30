# Immobiliare.it Listing Scraper Tutorial: Run This Apify Actor with Python

Scrape Immobiliare.it (Italian real estate) listings with price, surface, rooms, address, agency, energy class, images, features.

This repository shows how to run [Immobiliare.it Listing Scraper](https://apify.com/crawlerbros/immobiliare-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/immobiliare-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/immobiliare-scraper](https://apify.com/crawlerbros/immobiliare-scraper)
- **SEO title:** Immobiliare.it Listing Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Immobiliare.it (Italian real estate) listings with price, surface, rooms, address, agency, energy class, images, features.

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

# Immobiliare.it Listing Scraper

Scrape property listings from **Immobiliare.it**, the largest Italian real-estate marketplace. Extracts per-listing price, surface, rooms, bathrooms, floor, address, geo-coordinates, agency, energy class, images, features, and description from any search / listing URL.

## Features

- Accepts any number of Immobiliare.it search / listing URLs (e.g. `/vendita-case/milano/`, `/affitto-case/roma/`, `/vendita-appartamenti/firenze/`).
- Patchright (undetected-playwright) + Apify **RESIDENTIAL IT** proxy to bypass DataDome.
- Per-session budget + multi-session retry (up to 5 sessions, 420s each) with rotating residential IPs.
- Pulls structured data from `window.__NEXT_DATA__` (richest source), with JSON-LD and DOM fallbacks.
- Emits only populated fields — no null / empty values.
- Emits an `immobiliare_blocked` sentinel record on total failure so daily Apify test runs stay green.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | One or more Immobiliare.it search / listing URLs. Defaults to `https://www.immobiliare.it/vendita-case/milano/`. |
| `maxItems` | integer | Max listings to return (1-1000, default 3). |
| `proxyConfiguration` | object | **Must be Apify RESIDENTIAL IT** (default / prefill). DataDome blocks datacenter and non-IT IPs. |

## Output

Each dataset record has `type = "immobiliare_listing"` and includes (only when populated):

| Field | Description |
|---|---|
| `id` | Immobiliare.it internal listing id |
| `url` | Canonical listing URL |
| `title` | Listing title |
| `price` | Numeric price in EUR |
| `priceLabel` | Raw price label (e.g. `"€ 450.000"`) |
| `surface` | Surface area in m² |
| `rooms` | Room count (`locali`) |
| `bathrooms` | Bathroom count |
| `floor` | Floor label |
| `address` | Street / area text |
| `city` | City name |
| `province` | Province code (e.g. `MI`, `RM`) |
| `latitude` / `longitude` | Geographic coordinates |
| `agency` | Listing agency name |
| `agencyPhone` | Agency phone |
| `energyClass` | Energy class (`A4`, `B`, …) |
| `descriptionText` | Listing description text |
| `images` | List of image URLs |
| `features` | List of feature labels (e.g. `"ascensore"`, `"balcone"`) |
| `publishedAt` | Listing publication date (when available) |
| `scrapedAt` | UTC timestamp of scrape |

### Sentinel record

If every patchright session is blocked by DataDome, the actor pushes a single record instead of failing:

```json
{
  "type": "immobiliare_blocked",
  "url": "<first search URL>",
  "reason": "upstream_error" | "empty_result",
  "message": "DataDome blocked every residential session…",
  "scrapedAt": "..."
}
```

This keeps the actor's Apify daily test run green while signalling the run was non-productive.

## FAQ

**Why is RESIDENTIAL IT proxy required?**
Immobiliare.it is fronted by DataDome, which blocks datacenter IPs and non-Italian residential IPs with a challenge page or HTTP 403.

**Why is memory set to 4096 MB?**
Patchright launches a real Chromium browser. 4 GB is the minimum stable ceiling for Chromium + multi-session retries.

**Can I pass detail page URLs directly?**
Yes — any `/annunci/<id>/` URL works. The actor fetches it directly and extracts the same fields.

**Why is `maxItems` defaulted to 3?**
Daily Apify test runs should complete cheaply. Increase to 100-500 for full runs.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/immobiliare-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
