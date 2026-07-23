# Home Depot Product Scraper Tutorial: Run This Apify Actor with Python

Scrape product listings from homedepot.com by keyword or direct URL. Returns product ID, title, brand, price, rating, reviews, image, and URL.

This repository shows how to run [Home Depot Product Scraper](https://apify.com/crawlerbros/homedepot-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/homedepot-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/homedepot-scraper](https://apify.com/crawlerbros/homedepot-scraper)
- **SEO title:** Home Depot Product Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape product listings from homedepot.com by keyword or direct URL. Returns product ID, title, brand, price, rating, reviews, image, and URL.

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

# Home Depot Product Scraper

Scrape product listings from **[homedepot.com](https://www.homedepot.com)** by keyword or direct URL. Returns product ID, title, brand, price, original price, rating, reviews, image, and URL.

## What it does

- Scrapes `www.homedepot.com/s/<query>` search results
- Parses `data-testid="product-pod"` cards for product metadata
- Solves Home Depot's Akamai Bot Manager behavioral challenge with **patchright stealth Chromium**
- Hardcoded **RESIDENTIAL/US** proxy (required — Home Depot geo-gates to US-only and blocks non-US IPs)
- Clean, non-null output — empty fields are omitted from records
- Up to 8 retry sessions per URL on Akamai challenge failures

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `searchQuery` | string | `"drill"` | Free-text keyword. Required unless `startUrls` is set. |
| `priceMin` | number | — | Minimum price in USD |
| `priceMax` | number | — | Maximum price in USD |
| `sortBy` | enum | `relevance` | `relevance`, `top_sellers`, `price_low_to_high`, `price_high_to_low`, `top_rated`, `newest` |
| `startUrls` | array | — | Direct Home Depot **search** URLs (`/s/<query>`). Category (`/b/...`) URLs are less reliable and may trigger Akamai differently. |
| `maxItems` | integer | `50` | Maximum products to return (1–500) |

### Example input

```json
{
    "searchQuery": "cordless drill",
    "priceMin": 50,
    "priceMax": 300,
    "sortBy": "top_sellers",
    "maxItems": 20
}
```

## Output

Each product is a JSON record with the following fields (missing fields are omitted, never `null`):

| Field | Type | Always present | Description |
|---|---|---|---|
| `itemId` | string | ✓ | Home Depot internal product ID |
| `url` | string | ✓ | Full product URL |
| `title` | string | ✓ | Product label (brand stripped) |
| `scrapedAt` | string | ✓ | UTC ISO 8601 scrape timestamp |
| `brand` | string | — | Brand name (DEWALT, RYOBI, etc.) |
| `price` | number | — | Current price in USD |
| `originalPrice` | number | — | "Was" / strikethrough price if on sale |
| `currency` | string | — | Always `"USD"` when price is set |
| `rating` | number | — | Average star rating (0–5) |
| `reviewCount` | number | — | Number of customer reviews |
| `imageUrl` | string | — | Product thumbnail URL |
| `modelNumber` | string | — | Manufacturer model number |

### Sample output

```json
{
    "itemId": "204279858",
    "url": "https://www.homedepot.com/p/DEWALT-20V-MAX-Cordless-1-2-in-Drill-Driver.../204279858",
    "title": "20V MAX Cordless 1/2 in. Drill/Driver, (2) 20V 1.3Ah Batteries, Charger and Bag",
    "brand": "DEWALT",
    "price": 99.00,
    "originalPrice": 179.00,
    "currency": "USD",
    "imageUrl": "https://images.thdstatic.com/productImages/.../DCD771C2-64_1000.jpg",
    "scrapedAt": "2026-04-14T07:49:08Z"
}
```

## FAQ

**Do I need a proxy?**
No configuration needed — a **US residential proxy** is hardcoded and applied automatically. Home Depot uses Akamai Bot Manager with a JavaScript behavioral challenge that rejects datacenter IPs. The scraper launches patchright stealth Chromium under xvfb on Apify, waits for the challenge to clear (2–30 seconds typical), and only then extracts content.

**Why does the scraper occasionally retry?**
Akamai's challenge can stick on unlucky sessions. The scraper retries up to 8 times per URL with fresh residential sessions before failing. In the 10-run stability test all runs succeeded on the first or second attempt.

**Does it support category (`/b/...`) URLs?**
Best-effort. Category pages use a different React component and the Akamai challenge there is harder to clear reliably from this scraper. For best results, use **search URLs** (`/s/<query>?...`) which are fully supported. If you paste a `/b/...` URL into `startUrls` and the scraper fails, switch to a search query for the same topic.

**How many results can I get per run?**
Up to 500 items theoretically. Each search page returns ~24–50 cards. For larger sets, split your query into narrower keywords (e.g. by brand) and push multiple `startUrls`.

**How fresh is the data?**
Every run fetches live Home Depot HTML. Prices and availability are always current.

## Use cases

- **Price monitoring** — daily runs on specific SKUs or keywords
- **Competitive analysis** — compare prices vs Lowe's / Amazon / Menards
- **Deal hunting** — filter on `originalPrice > price` to find active sales
- **Catalog enrichment** — pull metadata for a list of Home Depot item IDs via `startUrls`

## Notes

- Pricing is configured in the Apify UI (pay-per-result).
- The daily Apify test run uses `searchQuery=drill`, `maxItems=5`.
- Home Depot's HTML markup can change; if the scraper starts returning 0 items, re-inspect the `data-testid="price-simple"` and `data-testid="attribute-brandname-inline"` selectors in `src/main.py:parse_search_html`.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/homedepot-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
