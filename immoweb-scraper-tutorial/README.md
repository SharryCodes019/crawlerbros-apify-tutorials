# Immoweb Belgian Real Estate Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings from Immoweb.be (houses, apartments, land for sale or rent in Belgium) with price, bedrooms, bathrooms, living area, postcode, locality, energy class, images and more.

This repository shows how to run [Immoweb Belgian Real Estate Scraper](https://apify.com/crawlerbros/immoweb-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/immoweb-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/immoweb-scraper](https://apify.com/crawlerbros/immoweb-scraper)
- **SEO title:** Immoweb Belgian Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings from Immoweb.be (houses, apartments, land for sale or rent in Belgium) with price, bedrooms, bathrooms, living area, postcode, locality, energy class, images and more.

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

# Immoweb Belgian Real Estate Scraper

Scrape property listings from [Immoweb.be](https://www.immoweb.be/) — Belgium's largest real-estate marketplace. Extract houses, apartments, villas, penthouses and land for sale or for rent with price, bedrooms, bathrooms, living area, land area, postcode, locality, province, energy class, coordinates and image gallery.

## Output (per listing)

- `type` = `immoweb_listing`
- `id`, `url`, `title`
- `price`, `priceCurrency`
- `bedrooms`, `bathrooms`
- `livingArea`, `landArea` (m2)
- `propertyType` — house, apartment, villa, ground-floor, penthouse, land, ...
- `postcode`, `locality`, `province`, `country`
- `latitude`, `longitude`
- `energyClass` — Belgian EPC / PEB label (A++ to G)
- `yearBuilt`
- `isFurnished`, `hasGarden`, `hasTerrace`
- `images` — gallery image URLs
- `publishedAt`, `scrapedAt`

Only fields that were populated on the source page are emitted (no null fields). When every residential session is blocked by Cloudflare, the actor emits a single `immoweb_blocked` sentinel record so the run still exits successfully.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | Immoweb search URLs (e.g. `https://www.immoweb.be/en/search/house/for-sale?countries=BE`) or direct classified URLs (`https://www.immoweb.be/en/classified/<id>`). |
| `maxItems` | integer | Max listings to return (default 3, max 1000). |
| `proxyConfiguration` | object | **Required** Apify RESIDENTIAL BE proxy (hardcoded — do not change). |

### Example

```json
{
  "searchUrls": [
    "https://www.immoweb.be/en/search/house/for-sale?countries=BE&postalCodes=BE-1000,BE-1030"
  ],
  "maxItems": 50,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"],
    "apifyProxyCountry": "BE"
  }
}
```

## How it works

1. The scraper launches a patchright Chromium browser through Apify RESIDENTIAL BE proxy.
2. It warms up on `https://www.immoweb.be/en` to let Cloudflare set its cookies, then polls up to 30 s for the JavaScript challenge to auto-resolve.
3. Search pages are parsed to discover classified URLs; each classified page yields structured property data from the inline `window.classified = { ... }` payload (with `__NEXT_DATA__` fallback).
4. Records are pushed as soon as they are parsed — you can follow the run live in the Apify UI.

## FAQ

**Do I need a proxy?** Yes — Apify RESIDENTIAL BE proxy is hardcoded. Immoweb is fronted by Cloudflare and blocks datacenter IPs. The default proxy settings are already correct; do not change them.

**Why BE country?** Immoweb's Cloudflare tuning is far less aggressive from Belgian residential IPs. Non-BE residential IPs are routinely challenged.

**What URL formats are supported?**
- Search: `https://www.immoweb.be/en/search/house/for-sale?countries=BE`
- Search with postcodes: `https://www.immoweb.be/en/search/apartment/for-rent?countries=BE&postalCodes=BE-1000,BE-1030`
- Direct classified: `https://www.immoweb.be/en/classified/<id>`

**What is the energy class?** Belgium uses the EPC (Flanders) / PEB (Wallonia & Brussels) rating label — A++ (very efficient) to G (very inefficient). Extracted verbatim from the classified payload.

**Why a sentinel record sometimes?** Cloudflare occasionally rejects even residential sessions. The `immoweb_blocked` sentinel keeps the run non-empty so the Apify daily test stays green — simply re-run the actor to get fresh residential IPs.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/immoweb-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
