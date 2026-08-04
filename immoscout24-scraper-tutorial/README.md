# ImmobilienScout24 Real Estate Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings (apartments, houses, for-sale and rental) from ImmobilienScout24.de with price, living space, rooms, address, realtor, features, images.

This repository shows how to run [ImmobilienScout24 Real Estate Scraper](https://apify.com/crawlerbros/immoscout24-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/immoscout24-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/immoscout24-scraper](https://apify.com/crawlerbros/immoscout24-scraper)
- **SEO title:** ImmobilienScout24 Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings (apartments, houses, for-sale and rental) from ImmobilienScout24.de with price, living space, rooms, address, realtor, features, images.

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

# ImmobilienScout24 Real Estate Scraper

Scrape property listings from [ImmobilienScout24.de](https://www.immobilienscout24.de), Germany's largest real-estate portal — apartments (`Wohnung`), houses (`Haus`), for-sale and rental inventory. Extracts price, living space, room count, address, realtor, features, images and more.

## Output (per listing)

- `type` = `immoscout24_listing`
- `id`, `url`, `title`
- `price`, `priceCurrency` (`EUR`)
- `livingSpace` (m2), `rooms`, `floor`, `yearBuilt`, `energyCertificate`
- `address`, `postcode`, `city`, `district`
- `latitude`, `longitude`
- `images` (array), `features` (array)
- `realtor`, `realtorPhone`
- `scrapedAt`

Fields are only emitted when populated (no nulls). When every residential session is blocked by Cloudflare, the actor emits a single `immoscout24_blocked` sentinel record so the run exits 0.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | ImmoScout24 search result URLs (`https://www.immobilienscout24.de/Suche/...`) or direct exposé URLs. Default: `Wohnung-Kauf` nationwide. |
| `maxItems` | integer | Max listings to return (default 3, max 500). |
| `proxyConfiguration` | object | **Required** Apify RESIDENTIAL DE proxy (hardcoded — do not change). |

## How it works

1. Each `searchUrls` entry is visited through a Patchright (undetected Chromium) session routed over Apify RESIDENTIAL DE.
2. Cloudflare JS challenge is polled for up to 30s per page before giving up on the session.
3. Search results are parsed for expose IDs; each exposé is fetched, parsed from the inline `window.IS24` JSON and JSON-LD fallbacks.
4. Up to 5 residential sessions are rotated with fresh session IDs if a proxy IP is flagged.

## FAQ

**Why do I need a RESIDENTIAL DE proxy?** ImmoScout24 is fronted by Cloudflare and geo-checks visitors. Datacenter IPs and non-DE IPs are challenged and return CAPTCHA pages. A German residential IP is required for consistent access.

**Can I scrape rentals (`Wohnung-Miete`)?** Yes. Pass any ImmoScout24 search URL, including rental searches (`/Suche/de/wohnung-mieten`), house searches (`/Suche/de/haus-kaufen`, `/Suche/de/haus-mieten`), city-specific paths (`/Suche/de/berlin/berlin/wohnung-kaufen`), or direct exposé URLs (`/expose/<id>`).

**Why is my run reporting `immoscout24_blocked` with 0 listings?** Residential IPs rotate — Cloudflare occasionally flags a fresh IP. Simply re-run the actor and a new session will be issued.

**Are the fields always populated?** The scraper only emits fields it can extract, so the output is free of null values. Required-always fields are `type`, `url`, `id`, `scrapedAt` on every listing record.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/immoscout24-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
