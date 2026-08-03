# Angi Home Services Scraper Tutorial: Run This Apify Actor with Python

Scrape Angi home-service provider listings (plumbers, electricians, HVAC, etc.) with phone, website, rating, reviews, services, service areas, licenses. Requires hardcoded Apify RESIDENTIAL US proxy.

This repository shows how to run [Angi Home Services Scraper](https://apify.com/crawlerbros/angi-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/angi-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/angi-scraper](https://apify.com/crawlerbros/angi-scraper)
- **SEO title:** Angi Home Services Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Angi home-service provider listings (plumbers, electricians, HVAC, etc.) with phone, website, rating, reviews, services, service areas, licenses. Requires hardcoded Apify RESIDENTIAL US proxy.

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

# Angi Home Services Scraper

Scrape home-service provider listings from [Angi.com](https://www.angi.com) — plumbers, electricians, HVAC technicians, roofers, landscapers and 500+ other service categories. Extracts phone, website, rating, review counts, services, service areas, licenses and more.

## Output (per provider)

- `type` = `angi_business`
- `id`, `url`, `name`
- `description`
- `phone`, `website`
- `address` — `{ street, city, state, zipCode, country }`
- `latitude`, `longitude`
- `rating`, `grade` (A-F), `reviewCount`, `yearsInBusiness`
- `yearsInAngi` — years active on Angi ("On Angi since YYYY")
- `ownerName` — owner/founder name when listed
- `services`, `specialties`, `serviceAreas` (arrays)
- `hours`
- `licenses`, `certifications`, `isInsured`
- `paymentMethods`
- `awards`, `professionalAssociations`
- `responseTime` (e.g. "2 hours"), `responseRate` (percent), `projectsCompleted`
- `emergencyService` (24/7), `offersSeniorDiscount`, `offersFreeEstimate`, `isEco`
- `warrantyOffered` — warranty text or yes/no
- `pricingTiers` — flat-rate / hourly amounts when published
- `highlightedReviews` — featured review excerpts `[{ author, rating, text }]`
- `photos` — gallery image URLs
- `scrapedAt`

Fields are only emitted when populated (no nulls). When every residential session is blocked, the actor emits a single `angi_blocked` sentinel record so runs exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `category` | string | Service slug, e.g. `plumbing`, `electrical`, `hvac`. Prefill `plumbing`. |
| `state` | string | Optional 2-letter US state code, e.g. `ny`. |
| `city` | string | Optional city slug (requires `state`), e.g. `new-york`. |
| `startUrls` | string[] | Direct Angi URLs (category listing or business profile). Overrides `category`/`state`/`city`. |
| `maxItems` | integer | Max providers to return (default 3). |
| `proxyConfiguration` | object | **Required** Apify RESIDENTIAL US proxy (hardcoded — do not change). |

## How it works

1. Build listing URL from `category + state + city` or use `startUrls`.
2. Fetch via `curl_cffi` with Chrome-131 TLS fingerprint through RESIDENTIAL US proxy — fresh session per retry (up to 5 attempts).
3. For listing pages, collect `/business/<slug>/<id>` and `/companyreviews.htm?spid=<id>` links and fetch each profile.
4. Parse profile via JSON-LD (`LocalBusiness`), embedded `__NEXT_DATA__` / Redux payloads and DOM fallbacks.

## FAQ

**Do I need a proxy?** Yes — Apify RESIDENTIAL US is hardcoded. Datacenter IPs are blocked by Cloudflare. The actor fails fast if the proxy stanza is absent.

**What URL formats are supported?**
- Category nationwide: `https://www.angi.com/companylist/plumbing/`
- Category by state: `https://www.angi.com/companylist/us/ny/plumbing.htm`
- Category by city: `https://www.angi.com/companylist/us/ny/new-york/plumbing.htm`
- Profile: `https://www.angi.com/companyreviews.htm?spid=12345` or `https://www.angi.com/business/<slug>/<id>`

**What is the grade?** Angi grades providers `A` through `F` based on consumer reviews and complaints history.

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

- [Run this actor on Apify](https://apify.com/crawlerbros/angi-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
