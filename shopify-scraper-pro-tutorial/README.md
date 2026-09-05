# Shopify Scraper Pro Tutorial: Run This Apify Actor with Python

Scrape any Shopify store(s) at scale: products, collections, search, on-sale tracking, multi-store batches. Filters: price/vendor/type/tags/title/sale/availability/date. Multi-endpoint fallback. HTTP-only, no auth, no proxy.

This repository shows how to run [Shopify Scraper Pro](https://apify.com/crawlerbros/shopify-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/shopify-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/shopify-scraper-pro](https://apify.com/crawlerbros/shopify-scraper-pro)
- **SEO title:** Shopify Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Scrape any Shopify store(s) at scale: products, collections, search, on-sale tracking, multi-store batches. Filters: price/vendor/type/tags/title/sale/availability/date. Multi-endpoint fallback. HTTP-only, no auth, no proxy.

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

# Shopify Scraper Pro

The most capable Shopify catalog scraper on Apify Store. **Multi-store batches**, **collection-scoped scraping**, **in-store search**, **sale tracking with discount %**, **endpoint fallback chain**, **image quality control**, **13 filter dimensions**, and **automatic proxy fallback**. Pulls structured product data from any Shopify-powered store via public APIs — no login, no cookies, no proxy required for most stores.

## What's "Pro" about it

| Capability | Basic Shopify scrapers | **Shopify Pro** |
|---|---|---|
| Stores per run | 1 | **N** (multi-store batch) |
| Collection-scoped | ❌ | ✅ `collectionHandles` |
| In-store search | ❌ | ✅ `searchQuery` via `/search/suggest.json` |
| Endpoint fallback | `/products.json` only | `/products.json` → `/collections/all/products.json` → collection-specific |
| Sort options | ❌ | 8 (best-selling, price asc/desc, title, created…) |
| Image quality | original only | 7 sizes (small/medium/large/grande/1024/2048/master) |
| Filters | 0-2 | **13 dimensions** |
| Sale tracking | ❌ or basic | `onSale`, `comparePrice`, `discountPercent` (derived) |
| Date filters | ❌ | `createdSince`, `updatedSince` |
| SKU search | ❌ | `skuContains` |
| Auto proxy fallback | ❌ | ✅ retries with Apify proxy on first failure |
| Output fields | ~17 | **27** (incl. `discountPercent`, `maxPrice`, `availableVariantCount`, `storeCollections`) |

## Modes

The actor runs in one of three modes per store:

1. **Full catalog** (default) — walks `/products.json` (and falls back to `/collections/all/products.json`) until the catalog is exhausted
2. **Collection** (`collectionHandles=[...]`) — fetches `/collections/<handle>/products.json` with the chosen `sortBy`
3. **Search** (`searchQuery=...`) — uses `/search/suggest.json` to find the most relevant matches

## Output per product

- `productId`, `handle`, `productUrl`, `storeUrl`
- `title`, `vendor`, `productType`
- `description` (HTML stripped, capped at 5000 chars)
- `tags[]`
- `price` (lowest variant), `maxPrice` (when range), `comparePrice`, `onSale`, **`discountPercent`** (derived)
- `currency` — when discoverable
- `variantCount`, `availableVariantCount`, `available`
- `skus[]` (up to 20)
- `variants[]` (up to 30 — `id`, `title`, `sku`, `price`, `comparePrice`, `available`, `option1/2/3`)
- `imageUrl` (cover, transformed to chosen `imageQuality`), `images[]` (up to 15, all transformed)
- `options[]` (size/color etc — `name`, `values[]`)
- `createdAt`, `updatedAt`, `publishedAt`
- `collections[]` — when `enrichWithCollections=true` and product matches store collections
- `storeCollections[]` — flat list of all collections in the store
- `scrapedFromCollection` — when scraped via collection mode
- `recordType: "product"`, `scrapedAt`

Empty fields are omitted from the output (no nulls).

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `storeUrls` | array | `["allbirds.com","kith.com"]` | Shopify store domains. Accepts full URLs, bare domains, or `*.myshopify.com` handles |
| `collectionHandles` | array | `[]` | When set, fetch `/collections/<handle>/products.json` instead of full catalog. Applies to ALL stores |
| `searchQuery` | string | – | When set, runs in-store search via `/search/suggest.json` |
| `sortBy` | enum | `best-selling` | Collection mode sort: `best-selling`, `manual`, `price-ascending`, `price-descending`, `title-ascending`, `title-descending`, `created-ascending`, `created-descending` |
| `imageQuality` | enum | `master` | Image URL quality: `small`/`medium`/`large`/`grande`/`1024x1024`/`2048x2048`/`master` |
| `enrichWithCollections` | bool | `false` | Fetch each store's `/collections.json` to enrich products with collection metadata |
| `maxItemsPerStore` | int | `250` | Hard cap per store (1-5000) |
| `maxItems` | int | `1000` | Global hard cap (1-50000) |
| `includeUnavailable` | bool | `false` | Drop products whose variants are all out-of-stock |
| `minPrice` | number | – | Drop products below this price |
| `maxPrice` | number | – | Drop products above this price |
| `vendorContains` | string | – | Only emit products whose vendor contains this substring |
| `productTypeContains` | string | – | Only emit products whose `product_type` contains this substring |
| `tagAnyOf` | array | `[]` | Only emit products whose tags contain at least one of these |
| `tagNoneOf` | array | `[]` | Drop products whose tags contain any of these |
| `titleContains` | string | – | Only emit products whose title contains this substring |
| `onSaleOnly` | bool | `false` | Only emit products with `compare_at_price > price` |
| `minDiscountPercent` | int | – | Only emit products discounted by at least this % |
| `createdSince` | string | – | Drop products created before this ISO date (`YYYY-MM-DD`) |
| `updatedSince` | string | – | Drop products updated before this ISO date |
| `skuContains` | string | – | Only emit products with at least one variant whose SKU contains this substring |
| `useApifyProxy` | bool | `false` | Force proxy from start. Auto-fallback to proxy happens regardless |
| `requestDelaySecs` | int | `1` | Pause between page fetches (0–10s) |

### Example: full catalog from one store

```json
{
  "storeUrls": ["allbirds.com"],
  "maxItemsPerStore": 500,
  "imageQuality": "large"
}
```

### Example: men's sale collection sorted by price

```json
{
  "storeUrls": ["allbirds.com"],
  "collectionHandles": ["mens-sale"],
  "sortBy": "price-ascending",
  "onSaleOnly": true,
  "minDiscountPercent": 30,
  "maxItems": 50
}
```

### Example: in-store search across multiple stores

```json
{
  "storeUrls": ["allbirds.com", "rothys.com"],
  "searchQuery": "wool runner",
  "maxItems": 30
}
```

### Example: track new arrivals from competitors

```json
{
  "storeUrls": ["kith.com", "endclothing.com", "ssense.com"],
  "createdSince": "2026-04-01",
  "tagAnyOf": ["new-arrivals", "new"],
  "minPrice": 100,
  "imageQuality": "1024x1024"
}
```

### Example: sale tracker with rich output

```json
{
  "storeUrls": ["allbirds.com", "everlane.com", "rothys.com"],
  "onSaleOnly": true,
  "minDiscountPercent": 40,
  "enrichWithCollections": true,
  "maxItems": 200
}
```

## Use cases

- **Competitor monitoring** — pull a competitor's full catalog weekly, track new launches with `createdSince`
- **Sale tracking** — daily run with `onSaleOnly: true` + `minDiscountPercent: 30` to alert on deep discounts
- **Multi-brand aggregator** — feed a price-comparison site with N store catalogs in one run
- **Inventory snapshot** — combine `availableVariantCount` and `updatedSince` to track stock churn
- **Brand intelligence** — `vendorContains` to extract products from a specific brand carried by a multi-brand store
- **Product-feed migration** — export a Shopify catalog as clean JSON for import elsewhere
- **In-store search analytics** — `searchQuery` mode to see what each store surfaces for a keyword

## FAQ

**Does it require a login or cookies?**  No. The actor uses public Shopify storefront endpoints.

**Is a proxy needed?**  Usually no — most Shopify stores serve datacenter IPs. The actor automatically retries with Apify proxy on the first failure, so stores that block cloud IPs still work transparently.

**Which stores does it work on?**  Any store using Shopify with the public products feed enabled — the vast majority of the 5M+ live Shopify stores. Some stores explicitly disable `/products.json`; for those, the `/collections/all/products.json` fallback often still works.

**How is `discountPercent` calculated?**  When a product's lowest variant price (`price`) is below the `compare_at_price`, we compute `100 * (1 - price/comparePrice)` and round down. Only emitted when the value is between 1 and 99.

**Why is `currency` not always included?**  Shopify's `/products.json` doesn't include a currency field at the product level. We add it when discoverable elsewhere; otherwise it's omitted (no nulls).

**Can I scrape a specific collection?**  Yes — set `collectionHandles: ["sale", "new-arrivals"]`. The actor will hit `/collections/<handle>/products.json` with your chosen `sortBy`.

**What does `imageQuality` actually do?**  Shopify's CDN serves multiple sizes via URL suffixes. e.g. `abc.jpg` → `abc_small.jpg` → `abc_1024x1024.jpg`. The actor rewrites every image URL to the chosen size. `master` returns the original.

**How does `searchQuery` differ from `titleContains`?**  `searchQuery` calls Shopify's own search backend (returns ranked, server-side relevance). `titleContains` is a client-side substring filter applied AFTER fetching the catalog. Use `searchQuery` for relevance, `titleContains` for catalog scans.

**How fresh is the data?**  Real-time. Endpoints serve the live catalog snapshot.

**What's the difference between `available` and `availableVariantCount`?**  `available` is `true` when at least one variant is in stock. `availableVariantCount` is the integer count of in-stock variants. Both are reliable sale indicators.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/shopify-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
