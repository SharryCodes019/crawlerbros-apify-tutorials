# Trolley Grocery Price Comparison Scraper Tutorial: Run This Apify Actor with Python

Scrape UK grocery prices from Trolley.co.uk - compare Tesco, Asda, Sainsbury's, Morrisons, Waitrose, Ocado & more. Search, browse categories, get per-retailer price comparisons with weekly history, or list current retailer deals.

This repository shows how to run [Trolley Grocery Price Comparison Scraper](https://apify.com/crawlerbros/trolley-grocery-price-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/trolley-grocery-price-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/trolley-grocery-price-scraper](https://apify.com/crawlerbros/trolley-grocery-price-scraper)
- **SEO title:** Trolley Grocery Price Comparison Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape UK grocery prices from Trolley.co.uk - compare Tesco, Asda, Sainsbury's, Morrisons, Waitrose, Ocado & more. Search, browse categories, get per-retailer price comparisons with weekly history, or list current retailer deals.

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

# Trolley Grocery Price Comparison Scraper

Scrape **Trolley.co.uk** — a UK grocery & household price comparison service covering Tesco, Asda, Sainsbury's, Morrisons, Co-op, ALDI, Waitrose, Ocado, Iceland, Boots, Superdrug, Poundland, Savers, Amazon, Ebay, Pets At Home and more. Search for any product by keyword (with sort, dietary, brand, size and retailer filters), browse curated "Top products" categories, pull a full per-retailer price comparison with weekly price history for a specific product, or list today's live deals at a chosen retailer. HTTP-only, no auth, no login, no proxy required.

## What this actor does

- **Four modes:** `search`, `byCategory`, `byProductIds`, `dealsByStore`
- **Multi-retailer price comparison:** see the same product's price across up to 16 UK retailers side by side
- **Weekly price history:** up to 52 weeks of historical pricing per product (mode = `byProductIds`)
- **Live deals feed:** current price-cut deals at a specific retailer (mode = `dealsByStore`)
- **Search filters:** sort by price, dietary tag (vegetarian/organic/vegan/halal/kosher/not tested on animals), brand, pack size, and retailer — all applied server-side by Trolley.co.uk
- **Star ratings** on every product record, plus review snippets, category rankings, allergen/dietary info, alternate pack sizes, and related products on the full product-detail lookup
- **Related searches** surfaced alongside keyword search results
- **Filters:** min/max price, filter results to a specific retailer
- **Empty fields are omitted** — a field only appears on a record when real data was found for it

## Output: per-product (mode = `search` / `byCategory` / `dealsByStore`)

- `productId` — Trolley.co.uk product ID (e.g. `MOZ184`)
- `productUrl` — canonical product page URL
- `name` — full product title, including pack size
- `brand`
- `description` — short product description (without brand/size)
- `size` — pack size / volume (e.g. `2l`, `900ml`)
- `imageUrl`
- `price` — lowest listed price found on the page (GBP)
- `currency` — always `GBP`
- `pricePerUnit` — e.g. `£0.13 per 100ml` (mode = `search` / `dealsByStore`)
- `rating` — average shopper star rating, 0–5
- `storePrices[]` — per-retailer `{store, price, currency}` snapshot (mode = `byCategory` only)
- `storeCount` — number of retailers with a listed price (mode = `byCategory` only)
- `promotionalOffer` — e.g. `2 FOR £4`, when present
- `wasPrice`, `savingText` — original price and saving description, for deals
- `dealAge` — how long ago the deal was spotted (mode = `dealsByStore`)
- `store` — retailer name (mode = `dealsByStore`)
- `reviewCount`
- `sampleReviews[]` — a few real shopper review snippets (mode = `byCategory` only)
- `relatedSearches[]` — related keyword suggestions shown alongside the results (mode = `search` only)
- `recordType`, `scrapedAt`

## Output: per-product detail (mode = `byProductIds`)

- `productId`, `productUrl`, `name`, `brand`, `description`, `size`, `imageUrl`
- `storePrices[]` — full per-retailer comparison: `{store, price, currency, pricePerUnit, promotionalOffer, visitUrl}`
- `storeCount` — number of retailers compared
- `price`, `currency` — the lowest price across all compared retailers
- `lowestPriceStore` — which retailer has the lowest price
- `priceHistory[]` — `{week, price}` for up to the last 52 weeks
- `rating` — average shopper star rating, 0–5
- `sampleReviews[]` — real shopper review text from the product page
- `productInfo` — allergen/ingredient/origin facts shown in the product's "Good to know" panel, e.g. `{"Contains": "Milk and Lactose"}`
- `dietaryBadges[]` — dietary badges shown on the product, e.g. `["Vegetarian"]`
- `categoryRankings[]` — `{rank, category, categorySlug}` for any "#1 in X" category leaderboard the product appears on
- `otherSizes[]` — alternate pack sizes of the same product, each `{productId, size, price, currency, pricePerUnit, badge, isCurrentSize}`
- `relatedProducts[]` — other products from the same brand shown on the product page
- `recordType`, `scrapedAt`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `search` | `search` / `byCategory` / `byProductIds` / `dealsByStore` |
| `searchQuery` | string | `milk` | Free-text product search (mode=search) |
| `categorySlug` | string | `vanilla-ice-creams` | Category slug from a Trolley.co.uk `/explore/...` URL (mode=byCategory) |
| `productIds` | array | – | Product IDs, paths, or full URLs (mode=byProductIds) |
| `store` | string | `tesco` | Retailer to pull deals from — one of 16 retailers: `asda` / `tesco` / `sainsburys` / `morrisons` / `coop` / `iceland` / `boots` / `superdrug` / `aldi` / `waitrose` / `poundland` / `savers` / `ocado` / `amazon` / `ebay` / `petsathome` (mode=dealsByStore) |
| `sortOrder` | string | `relevance` | `relevance` or `price` (lowest price first) — mode=search |
| `dietary` | string | – | Filter by dietary tag: `vegetarian` / `organic` / `vegan` / `halal` / `kosher` / `not tested on animals` — mode=search |
| `brandFilter` | string | – | Only return results from this brand, e.g. `Arla` — mode=search |
| `sizeFilter` | string | – | Only return results of this pack size, e.g. `1l` — mode=search |
| `minPrice` | number | – | Drop products cheaper than this (GBP) |
| `maxPrice` | number | – | Drop products more expensive than this (GBP) |
| `filterByStore` | string | – | Only keep products confirmed sold at this retailer (one of the same 16 retailers). Applied server-side for mode=search; applied to per-retailer data on other modes |
| `maxItems` | int | `20` | Hard cap on emitted records (1–500) |

### Example: search for a product

```json
{
  "mode": "search",
  "searchQuery": "chocolate",
  "maxPrice": 3,
  "maxItems": 30
}
```

### Example: search with sort, dietary and retailer filters

```json
{
  "mode": "search",
  "searchQuery": "milk",
  "sortOrder": "price",
  "dietary": "organic",
  "filterByStore": "Waitrose",
  "maxItems": 20
}
```

### Example: browse a curated category

```json
{
  "mode": "byCategory",
  "categorySlug": "single-malt-whiskeys",
  "maxItems": 20
}
```

### Example: full price comparison + history for specific products

```json
{
  "mode": "byProductIds",
  "productIds": ["MOZ184", "SOY634"]
}
```

### Example: today's deals at a retailer

```json
{
  "mode": "dealsByStore",
  "store": "tesco",
  "filterByStore": "Tesco",
  "maxItems": 20
}
```

## Use cases

- **Price-comparison shopping apps** — power a "cheapest place to buy X" feature across UK supermarkets
- **Grocery budgeting tools** — track weekly price history to time purchases
- **Market research** — monitor retailer pricing strategy and promotional cadence for a product category
- **Deal-alert services** — surface today's live price cuts at a favourite retailer
- **CPG brand monitoring** — see how a brand's products are priced across the UK grocery market

## FAQ

**What is the data source?**
All data comes from the public pages of [Trolley.co.uk](https://www.trolley.co.uk), a UK price-comparison website that aggregates live pricing from major UK grocery and health & beauty retailers.

**Is this affiliated with Trolley.co.uk or any retailer it compares?**
No. This is an independent, third-party actor that reads Trolley.co.uk's public web pages. It is not affiliated with Trolley.co.uk, Tesco, Asda, Sainsbury's, or any other retailer mentioned.

**Why do some products only show 3-4 retailer prices while the site shows more?**
Trolley.co.uk requires a free account login to reveal additional retailer prices beyond the first few on some products. This actor only extracts what's publicly visible without logging in.

**Does this cover fresh in-store prices or online prices?**
Prices reflect what each retailer lists online at the time Trolley.co.uk last checked, and may differ slightly from in-store pricing.

**Which retailers are covered?**
Trolley.co.uk tracks 16 retailers: Tesco, Asda, Sainsbury's, Morrisons, Co-op, ALDI, Waitrose, Ocado, Iceland, Boots, Superdrug, Poundland, Savers, Amazon, Ebay and Pets At Home. Coverage per individual product varies — not every retailer stocks every product.

**Is this UK-only?**
Yes — Trolley.co.uk covers UK retailers and prices in GBP.

**How far back does the price history go?**
Up to 52 weeks (about a year) where available.

**What happens if a search or category returns no results?**
The run finishes successfully with 0 items and a status message explaining why (e.g. unknown category slug, no matches for the query).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/trolley-grocery-price-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
