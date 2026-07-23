# SEMrush Free Website Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape SEMrush public website overview (Authority Score, Visits, Referring Domains, Backlinks) from semrush.com/website/. HTTP-only, no login, no proxy.

This repository shows how to run [SEMrush Free Website Stats Scraper](https://apify.com/crawlerbros/semrush-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/semrush-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/semrush-scraper](https://apify.com/crawlerbros/semrush-scraper)
- **SEO title:** SEMrush Free Website Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape SEMrush public website overview (Authority Score, Visits, Referring Domains, Backlinks) from semrush.com/website/. HTTP-only, no login, no proxy.

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

# SEMrush Free Website Stats Scraper

Scrape **SEMrush** public website overview metrics — authority score, monthly visits, referring domains, backlinks, and organic search traffic — for any domain. No SEMrush account, no cookies, no API key required. Uses a Chrome TLS fingerprint for fast-path domains and a Patchright anti-detect browser with residential proxy for domains behind SEMrush's reCAPTCHA v3 gate.

## What this actor does

- **Four modes:** `full`, `authority_only`, `backlinks_only`, `traffic_only`
- **Fast path:** curl_cffi with Chrome TLS fingerprint parses the public overview HTML directly
- **Browser fallback:** Patchright (undetected Chrome) + residential proxy + Google cookie warmup for domains where the overview route returns a false 404
- **reCAPTCHA v3 bypass:** real Chrome binary (no HeadlessChrome leak), persistent context for cookie accumulation, 8 proxy IP rotations per domain
- **Empty fields are omitted** — no nulls, no sentinels

## Output per domain

- `type` — `"semrush_website_stats"`
- `domain` — the normalized domain (e.g. `custify.com`)
- `authorityScore` — 0–100 SEMrush Authority Score
- `visits` + `visitsText` — estimated monthly visits
- `organicSearchTraffic` + `organicSearchTrafficText` — organic search visits
- `referringDomains` + `referringDomainsText` + `referringDomainsChange` — referring domain count + delta
- `backlinks` + `backlinksText` + `backlinksChange` — backlink count + delta
- `asOf` — data month (e.g. `July 2026`)
- `sourceUrl` — SEMrush URL the data was scraped from
- `scrapedAt` — UTC ISO timestamp
- `notFound` + `reason` — present only when SEMrush has no data for the domain

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `domains` | string[] | `["wikipedia.org"]` | List of domains to look up (e.g. `wikipedia.org`, `github.com`). Required. |
| `mode` | enum | `full` | `full` / `authority_only` / `backlinks_only` / `traffic_only` |
| `enableBrowserFallback` | boolean | `true` | Use Patchright anti-detect Chrome when the overview page has no metrics. |
| `proxyConfiguration` | object | Residential US | Apify Proxy Residential is prefilled. SEMrush rejects datacenter sessions via reCAPTCHA v3. |

### Example: single domain lookup

```json
{
    "domains": ["wikipedia.org"],
    "mode": "full"
}
```

### Example: batch of domains

```json
{
    "domains": ["amazon.com", "youtube.com", "twitter.com", "facebook.com", "linkedin.com"],
    "mode": "full"
}
```

### Example: authority score only

```json
{
    "domains": ["google.com"],
    "mode": "authority_only"
}
```

### Example: domain with URL prefix

```json
{
    "domains": ["https://www.custify.com/"],
    "mode": "full"
}
```

## Use cases

- **SEO agencies** — pull authority score and backlink counts for client reporting
- **Sales intelligence** — estimate competitor website traffic before outreach
- **Market research** — compare referring domains and backlink growth across niche sites
- **Lead enrichment** — append website traffic data to company profiles
- **Backlink audits** — track referring domain and backlink deltas over time

## FAQ

**Do I need a SEMrush account?** No. The actor scrapes SEMrush's free public Website Traffic Checker — no login, no cookies, no API key.

**Do I need a paid proxy?** Yes. SEMrush gates its free checker with reCAPTCHA v3, which scores datacenter IPs as 0.0 (bot). Residential proxy is prefilled because residential IPs get higher reCAPTCHA scores.

**Why does the actor take 60+ seconds for some domains?** Domains that SEMrush doesn't have a public overview page for (e.g. `custify.com`) require the browser fallback: launching real Chrome, warming Google cookies, navigating to SEMrush, and rotating through up to 8 residential proxy IPs to find one with sufficient reCAPTCHA score. Fast-path domains (e.g. `wikipedia.org`) complete in under 5 seconds.

**Why not full keyword/competitor data?** Those require a paid SEMrush subscription and are not exposed to anonymous users. Only free-tier fields are returned.

**Is this affiliated with SEMrush?** No, this is a third-party actor using SEMrush's public free tools.

**What's the difference between `visits` and `organicSearchTraffic`?** `visits` is total estimated monthly traffic. `organicSearchTraffic` is the portion that comes from organic search results.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/semrush-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
