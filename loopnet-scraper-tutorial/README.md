# LoopNet.com Commercial Real Estate Scraper Tutorial: Run This Apify Actor with Python

Scrape commercial real estate listings, broker profiles, and businesses for sale from LoopNet.com. Extracts title, price, address, property type, size, broker info.

This repository shows how to run [LoopNet.com Commercial Real Estate Scraper](https://apify.com/crawlerbros/loopnet-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/loopnet-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/loopnet-scraper](https://apify.com/crawlerbros/loopnet-scraper)
- **SEO title:** LoopNet.com Commercial Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape commercial real estate listings, broker profiles, and businesses for sale from LoopNet.com. Extracts title, price, address, property type, size, broker info.

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

# LoopNet.com Commercial Real Estate Scraper

Scrape commercial real estate listings from [loopnet.com](https://www.loopnet.com/). Supports for-sale, for-lease, businesses-for-sale, and broker search pages.

## What this actor extracts

Per listing (when Akamai permits):

- `type`, `url`, `listingId`, `title`
- `priceText`, `priceNumeric`
- `address`, `sizeText`, `imageUrl`
- `scrapedAt`

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | string[] | LoopNet URLs (search/listing/broker pages). |
| `searchType` | enum | `for-sale` / `for-lease` / `businesses-for-sale` / `brokers` (used when building URL). |
| `propertyType` | enum | `any`, `office`, `retail`, `industrial`, `multifamily`, `land`, `hotel`, `health-care`, `specialty`. |
| `maxItems` | integer | Max listings per run. |

## ⚠️ Important: Akamai Bot Manager

LoopNet.com is protected by **Akamai Bot Manager** with JS-challenge enforcement. This actor uses `curl_cffi` (Chrome TLS fingerprint) with a rotating Apify RESIDENTIAL US/CA proxy pool — but even residential sessions frequently get 403 responses. Akamai requires browser-level JS execution to issue session tokens.

**When the actor cannot retrieve listings**, it emits a single `loopnet_akamai_blocked` sentinel record with attempted URLs and a description.

**For guaranteed scraping**, route this actor through a paid anti-bot service (ZenRows, ScrapingBee, ScraperAPI).

## How it works

1. Rotate through 5 proxy configurations (RES-US → RES-CA → RES-any → RES-US → direct).
2. `curl_cffi` chrome131 impersonation + organic-traffic headers (Google referer, sec-fetch-\*).
3. Parse listing cards by finding anchors pointing at `/Listing/<id>/` and walking up to a container.
4. Detail pages parse `<h1>` + page text for price / address / size.

## Limitations

- **High 403 rate** — Akamai is tougher than DataDome or Cloudflare.
- **No demographic / broker-detail enrichment** — those require rendering the full SPA.
- **No pagination beyond first page of startUrl**.

## FAQ

**Do I need a proxy?** No — RESIDENTIAL is baked in, but it may not bypass Akamai on every run.
**Do I need cookies or login?** No.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/loopnet-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
