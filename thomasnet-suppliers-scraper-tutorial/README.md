# Thomasnet Suppliers Scraper Tutorial: Run This Apify Actor with Python

Scrape B2B supplier company profiles from Thomasnet.com (industrial manufacturers, machinists, distributors).

This repository shows how to run [Thomasnet Suppliers Scraper](https://apify.com/crawlerbros/thomasnet-suppliers-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/thomasnet-suppliers-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/thomasnet-suppliers-scraper](https://apify.com/crawlerbros/thomasnet-suppliers-scraper)
- **SEO title:** Thomasnet Suppliers Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape B2B supplier company profiles from Thomasnet.com (industrial manufacturers, machinists, distributors).

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

# Thomasnet Suppliers Scraper

Scrape B2B industrial supplier company profiles from [Thomasnet.com](https://www.thomasnet.com). HTTP-only with **hardcoded Apify RESIDENTIAL US proxy** (Cloudflare blocks datacenter IPs).

## Output (per supplier)

- `type` = `supplier_thomasnet`
- `url`, `tgramsId`, `slug`
- `name`, `description`, `type`, `tier`
- `yearFounded`, `annualSales`, `numberEmployees`
- `primaryPhone`, `website`, `logoUrl`
- `address` — `{ address1, city, state, zip, country, latitude, longitude }`
- `locations` — multi-location list
- `products`, `brands`, `certifications`, `headings`
- `personnel` — `[{ name, title, email, phone }]`
- `social` — `{ linkedin, twitter, ... }`
- `scrapedAt`

When every residential attempt is blocked, the actor emits a single `supplier_thomasnet_blocked` sentinel record so runs exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `query` | string | Product / category / company name (required). Prefill `valve`. |
| `startUrls` | string[] | Direct Thomasnet URLs (profile or listing). Overrides `query`. |
| `mode` | enum | `all` (product category) or `name` (company name). Default `all`. |
| `area` | enum | `NA` or US state / province code. Default `NA`. |
| `maxResults` | integer | Max suppliers. Default 25. |
| `includeFamilies` | boolean | Include product family capability data. |

## How it works

1. Build listing URL from `query + mode + area`, or use `startUrls`.
2. Fetch via `curl_cffi` with Chrome-131 TLS fingerprint through RESIDENTIAL US proxy (fresh session per retry, up to 5 attempts with country rotation US → US → CA → US → any).
3. For listing pages, collect `/profile/{id}/{slug}.html` links and fetch each.
4. Parse profile via Next.js `__NEXT_DATA__` payload (richest source) + JSON-LD Organization + OG meta fallbacks.

## FAQ

**Do I need a proxy?** No — it's hardcoded RESIDENTIAL US.
**Why a sentinel record sometimes?** Cloudflare occasionally rejects even residential sessions. The sentinel keeps the run non-empty.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/thomasnet-suppliers-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
