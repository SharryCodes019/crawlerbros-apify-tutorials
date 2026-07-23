# Wellfound (AngelList) Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape public job listings from Wellfound.com. Extracts job ID, title, compensation, remote status, location, company name, company logo. HTTP-only, no login.

This repository shows how to run [Wellfound (AngelList) Jobs Scraper](https://apify.com/crawlerbros/wellfound-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/wellfound-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/wellfound-scraper](https://apify.com/crawlerbros/wellfound-scraper)
- **SEO title:** Wellfound (AngelList) Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public job listings from Wellfound.com. Extracts job ID, title, compensation, remote status, location, company name, company logo. HTTP-only, no login.

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

# Wellfound Jobs Scraper

Scrape public job listings from [Wellfound](https://wellfound.com) (formerly AngelList Talent). HTTP-only, no login.

## What this actor extracts

Per job:

- `type`, `jobId`, `title`, `slug`, `jobUrl`
- `compensation`, `remote`, `locations`
- `companyId`, `companyName`, `companySlug`, `companyUrl`, `companyLogo`
- `postedAt` (when available)
- `scrapedAt`

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | string[] | Wellfound URLs. Default is `https://wellfound.com/jobs`. Supports `?remote=true`, `/location/<city>`, and custom query filters. |
| `remoteOnly` | boolean | Filter to remote-only jobs. Also appends `?remote=true` to default URLs. |
| `maxItems` | integer | Maximum jobs to return. Default 50, cap 500. |

## How it works

Wellfound's `/jobs` landing feed is a Next.js app that ships an Apollo Client cache in the page's `__NEXT_DATA__` script block. Each page returns up to ~47 `JobListing` entries along with their linked `Startup` entries. The actor fetches the HTML with `curl_cffi` (Chrome TLS fingerprint) and walks the cache to extract every job.

Deep-filter URLs (`/role/l/<role>/<city>`) are DataDome-protected — the actor escalates those to Apify RESIDENTIAL US proxy automatically.

## Limitations

- The `/jobs` feed serves a single page (~47 jobs) without client-side pagination. Use multiple `startUrls` or filtered URLs for more.
- Deep job details (descriptions, skills, benefits) require hitting individual `/jobs/<id>-<slug>` pages — these are DataDome-protected and may fall back to the proxy pool.

## FAQ

**Do I need cookies or login?** No.

**Do I need to configure a proxy?** No — residential proxy is hardcoded for URLs that need it; everything else goes direct.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/wellfound-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
