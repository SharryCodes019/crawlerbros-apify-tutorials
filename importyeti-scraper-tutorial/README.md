# ImportYeti Trade Intelligence Scraper Tutorial: Run This Apify Actor with Python

Scrape US import/export trade data from ImportYeti: companies, suppliers, shipments, top trading partners, trademarks, countries, and shipment recency. HTTP-only, no login, no proxy.

This repository shows how to run [ImportYeti Trade Intelligence Scraper](https://apify.com/crawlerbros/importyeti-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/importyeti-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/importyeti-scraper](https://apify.com/crawlerbros/importyeti-scraper)
- **SEO title:** ImportYeti Trade Intelligence Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape US import/export trade data from ImportYeti: companies, suppliers, shipments, top trading partners, trademarks, countries, and shipment recency. HTTP-only, no login, no proxy.

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

# ImportYeti Trade Intelligence Scraper

Scrape US import/export trade data from [ImportYeti](https://www.importyeti.com). For each query, returns a list of companies / suppliers with shipment counts, most-recent-shipment date, top trading partners, trademarks, and country of operation.

## Input

| Field | Type | Description |
|---|---|---|
| `query` | string | Company name, supplier name, trademark, or product keyword. Required. |
| `type` | enum | `any`, `company`, or `supplier`. |
| `mostRecentShipment` | enum | `any`, `6mo`, or `12mo` (include only companies active in the window). |
| `minShipments` | integer | Exclude companies with fewer lifetime shipments. |
| `maxResults` | integer | Max records to return (1–1000, 10 per page). |

## Output

Per record:
- `type` = `importyeti_record`
- `name` — company / supplier name
- `recordType` — `company` or `supplier`
- `countryCode` — ISO 2-letter
- `address`
- `totalShipments` — lifetime shipment count
- `mostRecentShipment` — DD/MM/YYYY of latest shipment
- `topSuppliers` — list of the top trading partners (filtered for placeholders)
- `trademarks` — list of associated trademarks (when present)
- `detailUrl` — direct link to the ImportYeti profile page
- `scrapedAt` — ISO timestamp

## How it works

- Hits `https://www.importyeti.com/api/search?q=<query>&page=<N>` (10 results/page).
- Paginates until `maxResults` is reached or no new data appears.
- All filters (`type`, `mostRecentShipment`, `minShipments`) are applied client-side because the public API ignores those parameters.
- `curl_cffi` with Chrome-131 TLS fingerprint; no cookies, no proxy required.

## FAQ

**Do I need a proxy or login?** No.
**Why are the filters applied client-side?** ImportYeti's public search API ignores filter parameters and always returns 10 mixed results per page. The actor fetches more pages than requested and filters down.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/importyeti-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
