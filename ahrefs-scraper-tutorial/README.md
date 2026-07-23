# Ahrefs Free Website Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape Ahrefs public website stats (Domain Rating, backlinks, global rank, organic traffic) from ahrefs.com/websites/. HTTP-only, no login, no proxy.

This repository shows how to run [Ahrefs Free Website Stats Scraper](https://apify.com/crawlerbros/ahrefs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ahrefs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ahrefs-scraper](https://apify.com/crawlerbros/ahrefs-scraper)
- **SEO title:** Ahrefs Free Website Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Ahrefs public website stats (Domain Rating, backlinks, global rank, organic traffic) from ahrefs.com/websites/. HTTP-only, no login, no proxy.

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

# Ahrefs Free Website Stats Scraper

Scrape public website metrics from [ahrefs.com/websites/<domain>](https://ahrefs.com/websites/wikipedia.org) — a public Ahrefs rank page that server-renders Domain Rating, backlink counts, global rank, and organic traffic estimates for popular indexed domains.

## What this actor extracts

Per domain:

- `type`, `domain`, `sourceUrl`, `scrapedAt`
- `domainRating` (0-100)
- `linkingWebsites` + `linkingWebsitesText`
- `referringDomainsDelta` + direction (month-over-month change)
- `globalRank`
- `organicTraffic` + text + `trafficMonth`
- `asOf` (data freshness month)
- `descriptionMeta` (from JSON-LD)
- `notFound: true` for domains Ahrefs doesn't index

## Input

| Field | Type | Description |
|---|---|---|
| `domains` | string[] | List of domains/URLs to look up. Required. |
| `mode` | enum | `full` (default), `authority_only`, or `backlinks_only` — filters output fields. |

## How it works

Ahrefs publishes a public rank index at `ahrefs.com/websites/<domain>` covering millions of popular sites. The actor issues a single HTTP GET per domain with `curl_cffi` (Chrome TLS fingerprint), parses the server-rendered HTML, and extracts the displayed metrics plus the JSON-LD description block.

- No cookies, no login, no API key
- No proxy (Ahrefs does not block datacenter IPs on this endpoint)
- 1 HTTP request per domain, 1024 MB memory

## Limitations

- **Coverage**: Ahrefs' public index covers popular / established domains. Small or new sites return a `notFound: true` record.
- **Free tool scope**: The actor does **not** scrape the paid Ahrefs dashboard; only the public rank page.
- **Data freshness**: Monthly updates.

## FAQ

**Do I need an Ahrefs account?** No.
**Do I need a proxy?** No.
**Will this work for my personal blog?** Only if Ahrefs has indexed it in their public rank data.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ahrefs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
