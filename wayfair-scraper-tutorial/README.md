# Wayfair Scraper Tutorial: Run This Apify Actor with Python

Scrape Wayfair product listings, product details, category browses, and brand pages from Wayfair.com (US), Wayfair.ca (Canada), Wayfair.co.uk (UK), and Wayfair.ie (Ireland). Extract title, SKU, brand, price, currency, rating, review count, image, breadcrumbs, and product URL.

This repository shows how to run [Wayfair Scraper](https://apify.com/crawlerbros/wayfair-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/wayfair-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/wayfair-scraper](https://apify.com/crawlerbros/wayfair-scraper)
- **SEO title:** Wayfair Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Wayfair product listings, product details, category browses, and brand pages from Wayfair.com (US), Wayfair.ca (Canada), Wayfair.co.uk (UK), and Wayfair.ie (Ireland). Extract title, SKU, brand, price, currency, rating, review count, image, breadcrumbs, and product URL.

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

## Wayfair Scraper

Scrape Wayfair product listings, product detail pages, category browses, and brand pages from Wayfair's regional storefronts. Extract title, SKU, brand, price (incl. previous/sale price), currency, rating, review count, breadcrumbs, image, and product URL.

### Why this scraper

- **No login, no cookies, no API key required** — works against the public Wayfair site.
- **5 modes** — `search`, `byUrl`, `byCategory`, `byBrand`, `byProduct`.
- **4 regional storefronts** — `wayfair.com` (US), `wayfair.ca` (CA), `wayfair.co.uk` (UK), `wayfair.ie` (IE).
- **HTTP-only via `curl_cffi` chrome131 impersonation** — fast, low-memory, no browser overhead.
- **Apify residential proxy by default** — Wayfair blocks Apify datacenter IPs with 429s, so the actor uses residential proxy out of the box.
- **Filters** — price range, minimum rating, sort order.
- **Optional PDP enrichment** — set `fetchProductDetails=true` to fetch the product detail page for every listing card and add brand, full description, breadcrumbs, and high-res image.

### Input

| Field | Type | Description |
|---|---|---|
| `mode` | enum | `search`, `byUrl`, `byCategory`, `byBrand`, `byProduct` |
| `country` | enum | `com`, `ca`, `co.uk`, `ie` |
| `text` | string | Search keyword (`search` mode) |
| `category` | enum | Top-level Wayfair category (`byCategory` mode) — Furniture, Outdoor, Decor & Pillows, Rugs, Kitchen & Tabletop, Bed & Bath, Lighting, Storage & Organization, Appliances, Home Improvement, Baby & Kids, Holiday Decor, Office, Pet |
| `urls` | array | Direct Wayfair URLs (`byUrl` / `byBrand` modes) |
| `skus` | array | Wayfair SKUs (e.g. `W118077895`, `CXVA1530`) for `byProduct` mode |
| `sortBy` | enum | `relevance`, `price_low_to_high`, `price_high_to_low`, `top_rated`, `newest`, `best_seller` |
| `priceMin` / `priceMax` | int | Drop products outside the price range |
| `ratingMin` | float | Drop products with rating below this (0.0-5.0) |
| `fetchProductDetails` | bool | Enrich every listing card with PDP data |
| `maxItems` | int | Hard cap on emitted records |
| `maxPagesPerListing` | int | Max paginated listing pages to crawl per seed |
| `proxyConfiguration` | proxy | Apify proxy configuration (defaults to RESIDENTIAL — required for cloud runs) |
| `brand` | string | Brand name for `byBrand` mode (e.g. "Latitude Run") |

### Output

Each record represents a single Wayfair product:

```json
{
  "sku": "CXVA1530",
  "title": "Latitude Run Ilkeston 81.6\" Wide Vegan Leather Manual Reclining Sofa",
  "brand": "Latitude Run",
  "productUrl": "https://www.wayfair.com/furniture/pdp/latitude-run-ilkeston-...-cxva1530.html",
  "canonicalUrl": "https://www.wayfair.com/furniture/pdp/latitude-run-ilkeston-...-cxva1530.html",
  "price": 689.99,
  "previousPrice": 1098.99,
  "currency": "USD",
  "ratingValue": 4.63,
  "reviewCount": 648,
  "imageUrl": "https://assets.wfcdn.com/im/.../Ilkeston+81.6+...+Cup+Holders.jpg",
  "description": "Choose a delivery day that works for you...",
  "breadcrumbs": ["Furniture", "Living Room Furniture", "Sofas"],
  "category": "Furniture",
  "subCategory": "Sofas",
  "promoFlag": "72-Hour Clearout",
  "country": "com",
  "siteName": "Wayfair",
  "recordType": "product",
  "scrapedAt": "2026-05-08T17:24:33.123456+00:00",
  "sourceUrl": "https://www.wayfair.com/keyword.php?keyword=sofa"
}
```

Empty / null fields are omitted from the record (no sentinel values).

### Modes

#### Search

Free-text keyword search across the country's catalog.

```json
{
  "mode": "search",
  "country": "com",
  "text": "sofa",
  "sortBy": "top_rated",
  "maxItems": 50
}
```

#### By URL

Paste any Wayfair search results, category, brand, or product detail URL. The scraper auto-detects the URL kind and the country from the host.

```json
{
  "mode": "byUrl",
  "urls": [
    "https://www.wayfair.com/furniture/cat/sofas-c413894.html",
    "https://www.wayfair.com/furniture/pdp/latitude-run-ilkeston-...-cxva1530.html"
  ]
}
```

#### By Category

Browse a top-level Wayfair category.

```json
{
  "mode": "byCategory",
  "country": "com",
  "category": "lighting",
  "sortBy": "newest"
}
```

#### By Brand

Search by brand name. The scraper performs a brand-scoped keyword search.

```json
{
  "mode": "byBrand",
  "country": "com",
  "brand": "Latitude Run"
}
```

#### By Product

Look up products by SKU.

```json
{
  "mode": "byProduct",
  "country": "com",
  "skus": ["W118077895", "CXVA1530"]
}
```

### FAQs

**Q: Does this work without a proxy?** Locally yes (from your home/office IP), but on Apify cloud Wayfair returns 429 from every Apify datacenter IP. The actor defaults to RESIDENTIAL proxy for that reason.

**Q: Does it support Wayfair.de?** No. Wayfair shut down its German storefront in 2020; the `wayfair.de` domain redirects to a permanent announcement page.

**Q: Do search results include all fields?** Search-result HTML embeds full data (title, price, currency, rating, reviewCount) for the first 3-5 cards above-the-fold, and partial data (title, sku, productUrl, image) for the remaining 45+ cards on the page. To get full data for every card, enable `fetchProductDetails=true`.

**Q: How many products per page?** ~48 unique SKUs per Wayfair listing page.

**Q: How does the price filter work?** Products without a price are kept (the user opted into a filter, not into requiring the field). Products with a price outside `[priceMin, priceMax]` are dropped.

**Q: Does the scraper extract reviews?** Not in this version. The Wayfair review widget loads via XHR after click; this scraper focuses on product-level data (title, price, rating aggregate, review count). Per-review extraction is on the roadmap.

**Q: What about international currency?** Each country has its native currency: USD (com), CAD (ca), GBP (co.uk), EUR (ie). The scraper extracts the actual currency code embedded in the JSON for each listing.

### Limitations

- **wayfair.de is not supported** (storefront closed).
- **Reviews-per-product** are not yet extracted (only the aggregate `ratingValue` and `reviewCount`).
- **Brand pages**: Wayfair's brand URL format varies; the easiest way to scrape a brand is via `byUrl` with the brand listing URL copied from the site.
- **Product detail data** for sponsored/ad placements may be sparser than for organic results.

### Test plan

Run `python -m pytest tests/ -q` from the actor folder. The suite covers 100+ unit tests across URL handling, listing extraction (US/CA/UK fixtures), product record extraction (real PDP fixture), filter helpers (per-type edge cases), and recursive null-walking.

# Actor input Schema

## `mode` (type: `string`):

Discovery axis. search: keyword search. byUrl: paste any Wayfair search/category/brand/product URL(s). byCategory: top-level category browse. byBrand: brand listing URL(s). byProduct: SKU lookup (product detail page).

## `country` (type: `string`):

Wayfair regional domain. com=US, ca=Canada, co.uk=UK, ie=Ireland. (Wayfair.de shut down in 2020 and is not supported.)

## `text` (type: `string`):

Free-text keyword (used in search mode). Examples: "sofa", "office chair", "throw pillow", "area rug".

## `category` (type: `string`):

Top-level Wayfair category (resolves to a category browse URL). Used for byCategory mode.

## `urls` (type: `array`):

Direct Wayfair URLs (search results, category page, or product detail page). Domain auto-detected from URL.

## `brand` (type: `string`):

Brand / manufacturer name (e.g. "Latitude Run", "Wade Logan", "Hokku Designs"). The scraper performs a brand-scoped search on Wayfair.

## `skus` (type: `array`):

Wayfair product SKUs (e.g. "W118077895", "CXVA1530"). The scraper resolves each SKU to its detail page.

## `sortBy` (type: `string`):

Sort order on listing pages. Wayfair maps these to its sortby URL parameter.

## `priceMin` (type: `integer`):

Drop products priced below this value (in the destination country's currency).

## `priceMax` (type: `integer`):

Drop products priced above this value (in the destination country's currency).

## `ratingMin` (type: `number`):

Drop products with rating below this value (0.0-5.0). Products with no rating are kept (the user opted into the filter, not into requiring the field).

## `fetchProductDetails` (type: `boolean`):

For each listing card, fetch the product detail page to enrich with brand, full description, breadcrumbs, and high-resolution image. Adds 1 HTTP request per product.

## `maxItems` (type: `integer`):

Hard cap on emitted product records.

## `maxPagesPerListing` (type: `integer`):

Maximum paginated listing pages (?page=N) to crawl per search/category/brand seed (~48 products per page).

## `proxyConfiguration` (type: `object`):

Apify proxy configuration. Wayfair blocks Apify datacenter IPs, so RESIDENTIAL proxy is required. Default is RESIDENTIAL. Leaving blank disables proxy and the actor will likely 429 on every request from Apify cloud.

## Actor input object example

```json
{
  "mode": "search",
  "country": "com",
  "text": "sofa",
  "category": "furniture",
  "urls": [],
  "brand": "",
  "skus": [],
  "sortBy": "relevance",
  "fetchProductDetails": false,
  "maxItems": 5,
  "maxPagesPerListing": 2,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ]
  }
}
```

# Actor output Schema

## `products` (type: `string`):

Dataset containing Wayfair product records.

# API

You can run this Actor programmatically using our API. Below are code examples in JavaScript, Python, and CLI, as well as the OpenAPI specification and MCP server setup.

## JavaScript example

```javascript
import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with your Apify API token
// Replace the '<YOUR_API_TOKEN>' with your token
const client = new ApifyClient({
    token: '<YOUR_API_TOKEN>',
});

// Prepare Actor input
const input = {
    "mode": "search",
    "country": "com",
    "text": "sofa",
    "category": "furniture",
    "urls": [],
    "brand": "",
    "skus": [],
    "sortBy": "relevance",
    "fetchProductDetails": false,
    "maxItems": 5,
    "maxPagesPerListing": 2,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ]
    }
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/wayfair-scraper").call(input);

// Fetch and print Actor results from the run's dataset (if any)
console.log('Results from dataset');
console.log(`💾 Check your data here: https://console.apify.com/storage/datasets/${run.defaultDatasetId}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.forEach((item) => {
    console.dir(item);
});

// 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/js/docs

```

## Python example

```python
from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
# Replace '<YOUR_API_TOKEN>' with your token.
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the Actor input
run_input = {
    "mode": "search",
    "country": "com",
    "text": "sofa",
    "category": "furniture",
    "urls": [],
    "brand": "",
    "skus": [],
    "sortBy": "relevance",
    "fetchProductDetails": False,
    "maxItems": 5,
    "maxPagesPerListing": 2,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
    },
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/wayfair-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "mode": "search",
  "country": "com",
  "text": "sofa",
  "category": "furniture",
  "urls": [],
  "brand": "",
  "skus": [],
  "sortBy": "relevance",
  "fetchProductDetails": false,
  "maxItems": 5,
  "maxPagesPerListing": 2,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ]
  }
}' |
apify call crawlerbros/wayfair-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/wayfair-scraper",
                "--header",
                "Authorization: Bearer <YOUR_API_TOKEN>"
            ]
        }
    }
}

```

## OpenAPI specification

Download the OpenAPI definition: https://api.apify.com/v2/acts/g0TvR2oIcet86fqxn/builds/KiSUfscwwPdwljRhy/openapi.json

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/wayfair-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
