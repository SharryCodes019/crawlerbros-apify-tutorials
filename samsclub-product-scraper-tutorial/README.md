# Sam's Club Product Scraper Tutorial: Run This Apify Actor with Python

Scrape Sam's Club wholesale products - search by keyword, browse by category, or enrich specific product URLs. Extracts prices, ratings, availability, descriptions, specs, and images.

This repository shows how to run [Sam's Club Product Scraper](https://apify.com/crawlerbros/samsclub-product-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/samsclub-product-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/samsclub-product-scraper](https://apify.com/crawlerbros/samsclub-product-scraper)
- **SEO title:** Sam's Club Product Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Sam's Club wholesale products - search by keyword, browse by category, or enrich specific product URLs. Extracts prices, ratings, availability, descriptions, specs, and images.

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

# Sam's Club Product Scraper

Extract wholesale product data from [Sam's Club](https://www.samsclub.com) — the membership warehouse club owned by Walmart. Search by keyword, browse by category, or enrich a list of product URLs to get prices, ratings, availability, descriptions, specifications, and images.

## What does this scraper do?

- **Keyword search** — find products by name, brand, or description
- **Category browsing** — explore Electronics, Appliances, Groceries, Clothing, and more
- **Product URL enrichment** — fetch complete details for a list of Sam's Club product links
- Extracts: name, price, original price, savings, member pricing, stock status, ratings, reviews, specifications, feature bullets, images, and more
- Supports sorting by relevance, price, rating, or best-selling
- Supports price and rating filters

## Input

| Field | Type | Description | Default |
|---|---|---|---|
| `mode` | select | `search`, `byCategory`, or `byProductUrls` | `search` |
| `searchQuery` | string | Keyword to search (mode=search) | `laptop` |
| `category` | select | Product category (mode=byCategory) | `electronics` |
| `sortBy` | select | Sort order: relevance, price-asc, price-desc, top-rated, bestselling | `relevance` |
| `minPrice` | integer | Minimum price filter ($) | — |
| `maxPrice` | integer | Maximum price filter ($) | — |
| `minRating` | number | Minimum average rating (0.0–5.0) | — |
| `startUrls` | list | Product URLs to enrich (mode=byProductUrls) | — |
| `maxItems` | integer | Maximum products to return (1–5000) | `50` |
| `clubId` | string | Sam's Club store ID for pricing (default: 6372 = Dallas, TX) | `6372` |

### Available categories

| Value | Label |
|---|---|
| `electronics` | Electronics |
| `appliances` | Appliances |
| `groceries` | Groceries & Food |
| `clothing` | Clothing & Shoes |
| `sporting-goods` | Sports & Outdoors |
| `home` | Home & Garden |
| `toys` | Toys & Baby |
| `health` | Health & Beauty |
| `auto` | Auto & Tires |
| `all` | All Categories |

### Example input (search)

```json
{
  "mode": "search",
  "searchQuery": "laptop",
  "sortBy": "price-asc",
  "maxPrice": 800,
  "minRating": 4.0,
  "maxItems": 50
}
```

### Example input (byProductUrls)

```json
{
  "mode": "byProductUrls",
  "startUrls": [
    "https://www.samsclub.com/ip/HP-Laptop/13576272587",
    "https://www.samsclub.com/ip/Samsung-TV/15234957453"
  ]
}
```

## Output

Each record contains:

| Field | Type | Description |
|---|---|---|
| `productId` | string | Sam's Club internal product ID |
| `name` | string | Full product name |
| `url` | string | Product page URL |
| `imageUrl` | string | Primary product image URL |
| `images` | array | All product image URLs |
| `price` | number | Current selling price (USD) |
| `originalPrice` | number | Original/was price before discount |
| `memberPrice` | number | Member price (same as price for Sam's Club) |
| `savings` | number | Dollar savings amount |
| `inStock` | boolean | Whether the product is currently in stock |
| `membershipRequired` | boolean | Always `true` — Sam's Club is membership-only |
| `itemNumber` | string | Sam's Club item number (usItemId) |
| `brand` | string | Product brand name |
| `category` | string | Product category/type |
| `rating` | number | Average customer rating (0–5) |
| `reviewCount` | integer | Number of customer reviews |
| `description` | string | Product description text |
| `specifications` | object | Key-value technical specifications (detail pages) |
| `features` | array | Bullet-point product features |
| `onlineOnly` | boolean | True if the product is only available online |
| `clubId` | string | Sam's Club store ID used for pricing |
| `recordType` | string | Always `"samsClubProduct"` |
| `scrapedAt` | string | ISO 8601 UTC timestamp of when the record was scraped |

### Example output record

```json
{
  "productId": "3VU6BX9X6KQ1",
  "name": "ASUS Vivobook 17X Laptop - 17.3\" FHD Display - Intel Core i9-13900H - 16GB RAM - 1TB SSD",
  "url": "https://www.samsclub.com/ip/ASUS-Vivobook-17X/13576272587?classType=REGULAR",
  "imageUrl": "https://i5.samsclubimages.com/asr/4731cb28-173f-4de0-83b4-3928fa27634c.jpeg",
  "images": ["https://i5.samsclubimages.com/asr/4731cb28-173f-4de0-83b4-3928fa27634c.jpeg"],
  "price": 999.0,
  "memberPrice": 999.0,
  "inStock": true,
  "membershipRequired": true,
  "itemNumber": "13576272587",
  "brand": "ASUS Vivobook",
  "category": "Laptop Computers",
  "rating": 4.4,
  "reviewCount": 46,
  "description": "The ASUS Vivobook 17X is equipped with Intel Core i9-13900H...",
  "specifications": {
    "Processor": "Intel Core i9-13900H",
    "RAM": "16GB DDR4",
    "Storage": "1TB PCIe SSD"
  },
  "features": [
    "Intel Core i9-13900H Processor",
    "16GB DDR4 RAM",
    "1TB PCIe G3 SSD"
  ],
  "onlineOnly": true,
  "clubId": "6372",
  "recordType": "samsClubProduct",
  "scrapedAt": "2026-05-15T12:00:00+00:00"
}
```

## Frequently Asked Questions

**Do I need a Sam's Club membership to use this scraper?**
No. The scraper accesses Sam's Club's public website and does not require a membership account or login. However, note that all prices shown on Sam's Club are member prices — a Sam's Club membership is required to actually purchase items.

**How many products can I scrape?**
The scraper supports up to 5,000 products per run. Sam's Club search results typically return 45–50 products per page. The scraper automatically paginates through all available pages up to your `maxItems` limit.

**Why are some products missing a price?**
Some items display a "See price in cart" or "Sign in to see price" message. These prices are intentionally hidden by Sam's Club and cannot be extracted without a logged-in session. Those products will appear without a price field.

**Can I filter by price range?**
Yes. Set `minPrice` and/or `maxPrice` (in whole dollars) to filter results. For example, `"minPrice": 200, "maxPrice": 800` returns only products priced between $200 and $800.

**What is the `clubId` field for?**
Sam's Club prices can vary by location. The `clubId` is the store number used for pricing lookups. The default (6372 = Dallas, TX) works for typical online prices. You can find your local club ID on the [Sam's Club Club Finder](https://www.samsclub.com/club).

**Does this scraper work for club-only (in-store) items?**
Yes. Items available in-store will have `"onlineOnly": false`. Items that are exclusively online will have `"onlineOnly": true`.

**Can I scrape product specifications?**
Yes, when using `mode=byProductUrls`. The scraper fetches the full product detail page which includes specifications like processor, RAM, storage, dimensions, etc. In `search` and `byCategory` modes, a shorter description and feature bullets are extracted from the search result data.

**How often does Sam's Club update its prices?**
Sam's Club prices, particularly Instant Savings, change weekly (Thursday to Wednesday). Re-run the scraper regularly if you need up-to-date pricing.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/samsclub-product-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
