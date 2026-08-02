# 10times.com Events Scraper Tutorial: Run This Apify Actor with Python

Scrape trade shows, conferences, and workshops from 10times.com. Extract event name, dates, venue, organiser, categories, description, and attendance stats. HTTP-only with hardcoded residential proxy.

This repository shows how to run [10times.com Events Scraper](https://apify.com/crawlerbros/tentimes-events-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tentimes-events-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tentimes-events-scraper](https://apify.com/crawlerbros/tentimes-events-scraper)
- **SEO title:** 10times.com Events Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape trade shows, conferences, and workshops from 10times.com. Extract event name, dates, venue, organiser, categories, description, and attendance stats. HTTP-only with hardcoded residential proxy.

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

# 10times.com Events Scraper

Scrape public trade shows, conferences, workshops, and festivals from [10times.com](https://10times.com). HTTP-only with **hardcoded Apify RESIDENTIAL proxy** (Cloudflare blocks datacenter IPs).

## Output (per event)

- `type` = `event_10times`
- `url`, `slug`, `id`
- `name`, `description`
- `startDate`, `endDate`, `eventStatus`, `eventAttendanceMode`
- `image`, `tags`
- `location` — object with `name`, `addressLocality`, `addressRegion`, `addressCountry`, `streetAddress`, `postalCode`, `latitude`, `longitude`
- `organizer` — object with `name`, `url`, `email`, `telephone`
- `pricing` — object with `price`, `priceCurrency`, `availability`
- `scrapedAt`

When every proxy attempt is blocked, the actor emits a single `event_10times_blocked` sentinel record so runs exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | string[] | 10times URLs (event detail or city/listing). Prefill: `https://10times.com/ces-las-vegas`. |
| `query` | string | Free-text search (constructs `?query=...`). |
| `city` | string | City slug (e.g. `berlin`). |
| `country` | enum | `WW` or 2-letter code. |
| `eventType` | enum | `all / tradeshow / conference / workshop / festival` (client-side keyword filter). |
| `onlineOnly` | boolean | Only online events. |
| `startDate`, `endDate` | string | ISO date filter (YYYY-MM-DD). |
| `sortBy`, `sortType` | enum | Sorting (currently client-side by startDate). |
| `maxItems` | integer | Max events returned. Default 20. |

## How it works

1. Build URLs from `startUrls`, `query`, or `city + country`.
2. Fetch each URL via `curl_cffi` with Chrome-131 TLS fingerprint through RESIDENTIAL proxy (country rotated across US / GB / DE / any / IN between retries).
3. Parse event detail pages by extracting `application/ld+json` Event schema + OG meta tags.
4. For listing pages, collect single-slug event links and fetch each detail page.
5. Apply client-side filters (`eventType`, `onlineOnly`, `startDate`, `endDate`).

## FAQ

**Do I need a proxy?** No — it's hardcoded.
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tentimes-events-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
