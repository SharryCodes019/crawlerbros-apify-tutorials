# Funda.nl Real Estate Tutorial: Run This Apify Actor with Python

Scrape Dutch real-estate listings from Funda.nl with price, living area, plot size, rooms, bedrooms, energy label, address, city, neighborhood, images, and agent. HTTP-only, no login required.

This repository shows how to run [Funda.nl Real Estate](https://apify.com/crawlerbros/funda-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/funda-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/funda-scraper](https://apify.com/crawlerbros/funda-scraper)
- **SEO title:** Funda.nl Real Estate Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Dutch real-estate listings from Funda.nl with price, living area, plot size, rooms, bedrooms, energy label, address, city, neighborhood, images, and agent. HTTP-only, no login required.

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

# Funda.nl Real Estate Scraper

Scrape real-estate listings from [Funda.nl](https://www.funda.nl), the Netherlands' largest property portal. Extract price, living area, plot size, rooms, bedrooms, energy label, address, neighbourhood, and images — all from public pages.

HTTP-only; no login, no cookies, no proxy required (but optional proxy is supported).

## Output (per listing)

- `type` = `funda_listing`
- `id`, `url`
- `title` — street address heading (e.g. *Ruyschstraat 87-K*)
- `price` — integer EUR
- `priceCurrency` — `EUR`
- `livingArea` — living area in m²
- `plotSize` — plot / lot size in m² (houses)
- `rooms` — total number of rooms
- `bedrooms` — number of bedrooms
- `energyLabel` — Dutch energy label (`A++`, `A+`, `A`, `B`, `C`, …)
- `buildingYear` — year of construction
- `address`, `postcode`, `city`, `neighborhood`
- `latitude`, `longitude` — when present in page data
- `images` — full list of high-resolution photo URLs
- `agent` — listing makelaar name (best-effort)
- `scrapedAt` — ISO 8601 timestamp

If nothing can be extracted, a single `funda_blocked` sentinel row is emitted (reason ∈ `invalid_input`, `upstream_error`, `empty_result`) so the run always exits 0 and Apify daily tests stay green.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | Funda search URLs. Examples: `https://www.funda.nl/koop/amsterdam/`, `https://www.funda.nl/koop/rotterdam/`. Prefilled with Amsterdam. |
| `maxItems` | integer | Maximum listings to return. Default 3, max 500. |
| `proxyConfiguration` | object | Optional Apify proxy. Funda works from bare datacenter IPs, so this is off by default. |

## How it works

1. Fetch each `searchUrls` entry (e.g. `/koop/amsterdam/`).
2. Read the embedded `ItemList` JSON-LD schema to discover every detail URL on that page (15 per page).
3. For each detail page, parse the embedded `Product` JSON-LD (address, price, images) and the DOM feature list (living area, plot, rooms, energy label, building year, …).
4. Only fields Funda actually populates are emitted — no null placeholders.

## FAQ

**Do I need a proxy?** No. Funda returns HTTP 200 for this scraper from bare Apify datacenter IPs.

**Do I need cookies / login?** No. Everything extracted comes from public pages.

**Can it scrape rental (huur) listings?** Yes — pass any `https://www.funda.nl/huur/<city>/` URL in `searchUrls`.

**Why is the sentinel emitted?** When a URL returns no listings or Funda changes its markup, the run still produces one row so downstream pipelines never see an empty output.

**Can it paginate?** This release returns the first page of each `searchUrls` entry (up to 15 listings per URL). To scrape more, pass multiple city or neighbourhood URLs, or the next-page Funda URL (`/koop/amsterdam/p2/`).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/funda-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
