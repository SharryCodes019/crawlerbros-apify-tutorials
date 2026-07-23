# MercadoLibre Product Scraper Tutorial: Run This Apify Actor with Python

Scrape products from MercadoLibre across Mexico. Returns product title, price, currency, condition, seller, thumbnail, and permalink.

This repository shows how to run [MercadoLibre Product Scraper](https://apify.com/crawlerbros/mercadolibre-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/mercadolibre-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/mercadolibre-scraper](https://apify.com/crawlerbros/mercadolibre-scraper)
- **SEO title:** MercadoLibre Product Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape products from MercadoLibre across Mexico. Returns product title, price, currency, condition, seller, thumbnail, and permalink.

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

# MercadoLibre Scraper

Scrape products from **[MercadoLibre](https://www.mercadolibre.com)** — Latin America's largest e-commerce marketplace. Returns product ID, title, URL, price, currency, condition, seller, thumbnail, rating, and more. Supports Argentina, Brazil, and Mexico.

## What it does

- Scrapes MercadoLibre search results across **3 LatAm country sites** (AR, BR, MX)
- Extracts product ID, title, URL, price, currency, thumbnail, rating, reviews, seller, brand, and shipping info
- Hardcoded residential proxy handles MercadoLibre's account-verification block wall
- Automatic session rotation — up to 6 retries on flagged sessions
- Clean, non-null output — empty fields are omitted from records

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `country` | enum | `AR` | Which MercadoLibre site to scrape: `AR` (Argentina), `BR` (Brazil), `MX` (Mexico) |
| `searchQuery` | string | `"iphone"` | Free-text keyword (required unless `startUrls` is set) |
| `condition` | enum | `any` | `any` / `new` / `used` |
| `priceMin` | integer | — | Minimum price in local currency |
| `priceMax` | integer | — | Maximum price in local currency |
| `startUrls` | array | — | Direct MercadoLibre search URLs (override structured filters) |
| `maxItems` | integer | `50` | Maximum results to return (1–1000) |

### Example input

```json
{
    "country": "BR",
    "searchQuery": "notebook",
    "priceMin": 2000,
    "priceMax": 10000,
    "maxItems": 20
}
```

## Output

Each product is a JSON record with the following fields (missing fields are omitted, never `null`):

| Field | Type | Always present | Description |
|---|---|---|---|
| `id` | string | ✓ | MercadoLibre item ID (e.g. `MLA1018500855`) |
| `title` | string | ✓ | Product title |
| `url` | string | ✓ | Full product URL |
| `countryCode` | string | ✓ | Country code (e.g. `AR`) |
| `scrapedAt` | string | ✓ | UTC ISO 8601 scrape timestamp |
| `price` | number | — | Current price in local currency |
| `originalPrice` | number | — | Strikethrough / original price (before discount) |
| `currency` | string | — | Currency code (e.g. `ARS`, `BRL`, `MXN`) |
| `currencySymbol` | string | — | Currency symbol as displayed on the site |
| `discountPercentage` | number | — | Percentage off (0–100) |
| `thumbnail` | string | — | Product image URL |
| `sellerName` | string | — | Seller / brand name |
| `brand` | string | — | Brand attribute |
| `shippingLabel` | string | — | Shipping badge text (e.g. `Envío gratis`, `Frete grátis`) |
| `rating` | number | — | Seller or product star rating |
| `reviewsCount` | number | — | Number of reviews |

### Sample output

```json
{
    "id": "MLA1018500855",
    "title": "iPhone 13 128 GB 4 GB RAM Blanco estelar Apple - Distribuidor Autorizado",
    "url": "https://articulo.mercadolibre.com.ar/MLA-1018500855-iphone-13-128-gb-...",
    "countryCode": "AR",
    "price": 999999,
    "currency": "ARS",
    "currencySymbol": "$",
    "thumbnail": "https://http2.mlstatic.com/D_Q_NP_2X_787642-MLA95698363690_102025-E.webp",
    "sellerName": "DistribuidorOficial",
    "shippingLabel": "Envío gratis",
    "scrapedAt": "2026-04-14T06:38:23Z"
}
```

## FAQ

**Do I need a proxy?**
No configuration needed — an Apify **residential proxy** is applied automatically, matching the selected country. MercadoLibre blocks direct datacenter access and even many residential sessions, so the scraper rotates proxy session IDs up to 6 times per run on flagged sessions. The first half of attempts use the target country's residential pool; the second half falls back to any residential IP for resilience.

**Why only 3 countries?**
At the time of writing, MercadoLibre's smaller-market sites (Chile, Colombia, Peru, Uruguay, Venezuela, Ecuador, Dominican Republic, Costa Rica) return a hard-block response on every residential session in Apify's pool. Only AR, BR, and MX reliably serve scrapable HTML. The scraper's country enum has been trimmed accordingly.

**How many results can I get per run?**
Up to 1,000 items (theoretically). Each search page returns 40–50 cards; the scraper paginates via the MercadoLibre page index when `maxItems` exceeds a single page. Practical cap depends on how deep the search goes before MercadoLibre starts returning "no more results".

**Does the scraper call MercadoLibre's public API?**
No. `api.mercadolibre.com` now returns 403 for anonymous traffic. The scraper uses the HTML search listings page (`listado.mercadolibre.com.ar/<query>`, etc.) and parses the `poly-card` server-rendered product tiles.

**What happens if the target site is blocked?**
The scraper retries with a fresh residential session. If all 6 retries fail, the run exits with a fail status and no records — the residential pool was exhausted for that country. Rerun in a few minutes.

**How fresh is the data?**
Every run hits the live search page. Prices and availability are always current.

## Use cases

- **Price monitoring** — daily runs to track competitor prices in AR/BR/MX
- **Trend research** — ingest product names and prices across major keywords
- **Cross-border arbitrage** — compare pricing between AR, BR, and MX markets
- **Inventory alerts** — monitor specific SKUs via the `startUrls` override

## Notes

- Pricing is configured in the Apify UI (pay-per-result).
- MercadoLibre's HTML can change; if the scraper starts returning 0 items, check the `poly-card` class markers in `src/main.py:parse_search_html`.
- The daily Apify test run uses `country=AR`, `searchQuery=iphone`, `maxItems=5`.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/mercadolibre-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
