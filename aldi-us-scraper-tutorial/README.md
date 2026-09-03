# Aldi US Scraper Tutorial: Run This Apify Actor with Python

Scrape Aldi US groceries - search products by keyword, browse curated collections (Weekly Specials, ALDI Finds, Price Drops, ALDI Brands), real prices, discounts and images.

This repository shows how to run [Aldi US Scraper](https://apify.com/crawlerbros/aldi-us-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/aldi-us-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/aldi-us-scraper](https://apify.com/crawlerbros/aldi-us-scraper)
- **SEO title:** Aldi US Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Aldi US groceries - search products by keyword, browse curated collections (Weekly Specials, ALDI Finds, Price Drops, ALDI Brands), real prices, discounts and images.

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

# Aldi US Scraper

Scrape [Aldi US](https://www.aldi.us) groceries — search for products by keyword, or browse Aldi's curated storefront collections: Weekly Specials, ALDI Finds, Price Drops, and ALDI Exclusive Brands. Real prices, discounts, brands, and images, straight from Aldi's own storefront data. No login, no cookies required.

## What this actor does

- **Three modes:** `search`, `byCategory` (curated collections), `weeklyDeals`
- **Free-text search** across Aldi's full US catalog
- **Curated collections:** Weekly Specials, Price Drops, This Week's ALDI Finds, ALDI Finds, ALDI Exclusive Brands, Upcoming ALDI Finds
- **Filters:** price range, on-sale only, brand
- **Empty fields are omitted** — every record only contains what Aldi actually returned

## Output per product

- `productId`, `name`, `brand`, `unit` (pack size, e.g. `8 oz`, `1 gal`)
- `price` — current price (USD)
- `originalPrice`, `discount`, `discountPercent` — only present when the product is discounted
- `subcategory` — Aldi's own fine-grained product category (e.g. `Hass Avocado`, `Canned Coconut Milk and Cream`)
- `category` — the collection name, when browsing a collection or weekly deals
- `imageUrl`, `productUrl`
- `isOnSale`, `inStock`, `stockLevel` (e.g. `High stock`, `In stock`, `Limited stock`)
- `pricePerUnit` — Aldi's own per-unit price string (e.g. `$0.13/oz`, `$1.10 each`)
- `isStoreBrand` — `true` when the product is one of Aldi's own private-label brands
- `dietaryAttributes` — dietary/shopping tags when Aldi flags them (e.g. `Organic`, `Gluten Free`, `Low Sugar`, `Lactose Free`, `Preservative Free`)
- `sourceUrl`, `scrapedAt`, `recordType: "product"`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `search` | `search` / `byCategory` / `weeklyDeals` |
| `searchQuery` | string | `milk` | Free-text query (mode=search) |
| `category` | string | `weekly-specials` | Collection to browse (mode=byCategory) |
| `minPrice` / `maxPrice` | number | – | Price range filter (USD) |
| `onSaleOnly` | bool | `false` | Only emit discounted products |
| `brand` | string | – | Filter by brand (case-insensitive substring) |
| `maxItems` | int | `24` | Hard cap, 1–50 |
| `proxyConfiguration` | object | AUTO proxy | Apify proxy config (free datacenter group) |

### Example: search for chicken under $10

```json
{
  "mode": "search",
  "searchQuery": "chicken",
  "maxPrice": 10,
  "maxItems": 24
}
```

### Example: browse ALDI Finds

```json
{
  "mode": "byCategory",
  "category": "aldi-finds",
  "maxItems": 20
}
```

### Example: this week's deals

```json
{
  "mode": "weeklyDeals",
  "maxItems": 24,
  "onSaleOnly": true
}
```

## Use cases

- **Price monitoring** — track Aldi US prices and promotions over time
- **Deal alerts** — surface products newly on offer or freshly price-dropped
- **Grocery comparison apps** — feed real Aldi US pricing into a comparison tool
- **Market research** — analyse Aldi's private-label ("ALDI Exclusive Brands") assortment and pricing
- **Meal planning apps** — pull ingredient prices for a shopping list

## FAQ

**Do I need an Aldi account or cookies?** No — this actor reads Aldi's own public storefront data (Aldi's US online ordering runs on Instacart's platform), the same data your browser receives when you visit the site.

**Why does `byCategory` use collections instead of aisles like "Dairy" or "Bakery"?** Aldi's US storefront doesn't expose a stable, directly-browsable aisle/department page — product grids for aisles are assembled client-side per shopper. The collections offered here (Weekly Specials, ALDI Finds, Price Drops, ALDI Exclusive Brands) are Aldi's own official curated navigation pages and are fully reliable to scrape.

**What does `isOnSale` mean?** `true` when Aldi is currently running a promotional price on that product; `originalPrice`/`discount`/`discountPercent` are populated alongside it.

**Why is `category` sometimes missing?** In `search` mode there's no single collection context, so only the more specific `subcategory` (Aldi's own product-category label) is populated. In `byCategory` / `weeklyDeals` mode, `category` is set to the collection name.

**Is this free to run?** Yes — the actor uses Apify's free `AUTO` datacenter proxy group (falling back to a direct connection automatically), so it works on the Apify free plan with no paid add-ons.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/aldi-us-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
