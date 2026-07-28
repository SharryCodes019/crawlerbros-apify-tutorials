# Domain.com.au Real Estate Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings from Domain.com.au with addresses, prices, bedrooms, images, inspections, agents. HTTP-only; no login or proxy required.

This repository shows how to run [Domain.com.au Real Estate Scraper](https://apify.com/crawlerbros/domain-au-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/domain-au-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/domain-au-scraper](https://apify.com/crawlerbros/domain-au-scraper)
- **SEO title:** Domain.com.au Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings from Domain.com.au with addresses, prices, bedrooms, images, inspections, agents. HTTP-only; no login or proxy required.

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

# Domain.com.au Real Estate Scraper

Scrape Australian property listings from [Domain.com.au](https://www.domain.com.au) — addresses, asking prices, bedrooms/bathrooms/carspaces, images, inspection times, agents, and coordinates. Parses the `__NEXT_DATA__` JSON blob Domain ships in every search page. HTTP-only; no login, no cookies, no proxy required.

## Output (per listing)

- `type` = `domain_listing`
- `id` — Domain listing ID (e.g. `2020305174`)
- `url` — canonical listing URL (`https://www.domain.com.au/...`)
- `title` — first line of address + suburb (e.g. `107/104 Fairway Drive, Norwest`)
- `price` — numeric price when published (e.g. `1000000`)
- `priceLabel` — price string as displayed (e.g. `"$1,000,000"`, `"Auction"`, `"Contact agent"`)
- `propertyType` — `House`, `ApartmentUnitFlat`, `Townhouse`, `Land`, etc.
- `bedrooms`, `bathrooms`, `carspaces` (integers)
- `address`, `suburb`, `state`, `postcode`
- `latitude`, `longitude`
- `images` — array of photo URLs
- `inspections` — array of `{openTime, closeTime}` ISO strings (when listed)
- `agent` — `{name, photo}` for the primary agent
- `agencyName` — brand/agency name
- `scrapedAt`

If no listings match, the actor emits a single `domain_blocked` sentinel record so runs exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | Domain.com.au search URLs. Prefill: `https://www.domain.com.au/sale/sydney-nsw/`. Any `/sale/`, `/rent/`, or region URL works. |
| `maxItems` | integer | Max listings per run. Default 3. |
| `proxyConfiguration` | object | Optional — disabled by default. Domain works fine from datacenter IPs. |

## Example output

```json
{
  "type": "domain_listing",
  "id": "2020305174",
  "url": "https://www.domain.com.au/107-104-fairway-drive-norwest-nsw-2153-2020305174",
  "title": "107/104 Fairway Drive, Norwest",
  "price": 1000000,
  "priceLabel": "$1,000,000",
  "propertyType": "ApartmentUnitFlat",
  "bedrooms": 2,
  "bathrooms": 2,
  "carspaces": 1,
  "suburb": "Norwest",
  "state": "NSW",
  "postcode": "2153",
  "latitude": -33.730362,
  "longitude": 150.95859,
  "images": ["https://rimh2.domainstatic.com.au/..."],
  "agencyName": "Obsidian Property Pty Ltd",
  "scrapedAt": "2026-04-20T10:00:00Z"
}
```

## How it works

1. For each entry in `searchUrls`, the actor fetches the page with `curl_cffi` (Chrome 131 TLS fingerprint).
2. The `__NEXT_DATA__` script is parsed for `props.pageProps.componentProps.listingsMap` — every property card is serialised there with full metadata.
3. Pagination is followed via `totalPages` / `?page=N` up to `maxItems`.
4. Fields are only emitted when populated (no nulls).

## FAQ

**Do I need a proxy?** No. Domain.com.au is reachable from Apify datacenter IPs.
**Can I scrape `/rent/` too?** Yes — any URL under `https://www.domain.com.au/sale/...` or `/rent/...` works.
**What about individual property pages?** Provide any Domain listing detail URL; the actor will fetch just that one listing.
**Why a sentinel record?** If a search has no matches or the region slug is wrong, the actor still emits one record so downstream pipelines never see empty output.
**Rate limits?** Domain has no aggressive anti-bot system, but we cap at `maxItems` (500) and add a polite 0.4s delay between pages.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/domain-au-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
