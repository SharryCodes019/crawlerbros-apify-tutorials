# WooCommerce Scraper Tutorial: Run This Apify Actor with Python

Scrape products, categories, tags, attributes, and reviews from any WooCommerce store.

This repository shows how to run [WooCommerce Scraper](https://apify.com/crawlerbros/woocommerce-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/woocommerce-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/woocommerce-scraper](https://apify.com/crawlerbros/woocommerce-scraper)
- **SEO title:** WooCommerce Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape products, categories, tags, attributes, and reviews from any WooCommerce store.

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

# WooCommerce Scraper

Extract products, categories, tags, attributes, and reviews from any WooCommerce-powered online store. Get structured product data including prices, images, stock status, ratings, and more.

## What can this scraper do?

- **Scrape product data** from any WooCommerce store — names, prices, descriptions, images, SKUs, stock status, ratings, and reviews
- **Extract categories, tags, and attributes** to map the store's product catalog structure
- **Collect customer reviews** with ratings, reviewer names, and verification status
- **Handle multiple stores** in a single run — scrape products from several WooCommerce stores at once
- **Search and filter** products by keyword and sort by date, price, popularity, rating, or title
- **Automatic fallback** — uses the WooCommerce Store API when available, with HTML scraping as a backup for maximum compatibility

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `storeUrls` | Array of strings | Yes | — | WooCommerce store URLs to scrape (e.g., `https://example.com`) |
| `maxProductsPerStore` | Integer | No | `100` | Maximum products to extract per store. Set to `0` for unlimited (up to 10,000) |
| `resources` | Array | No | `["products"]` | What to scrape: `products`, `categories`, `tags`, `attributes`, `reviews` |
| `searchQuery` | String | No | — | Filter products by keyword |
| `sortBy` | String | No | Default | Sort products: `date`, `price`, `popularity`, `rating`, `title` |
| `proxyConfiguration` | Object | No | — | Proxy settings (usually not needed) |

### Example input

```json
{
    "storeUrls": ["https://example-store.com"],
    "maxProductsPerStore": 50,
    "resources": ["products", "categories", "reviews"],
    "searchQuery": "organic"
}
```

## Output

### Products

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Product ID |
| `name` | String | Product name |
| `slug` | String | URL-friendly slug |
| `type` | String | Product type: `simple`, `variable`, `grouped`, or `external` |
| `url` | String | Full product page URL |
| `sku` | String | Stock Keeping Unit |
| `description` | String | Full product description (plain text) |
| `shortDescription` | String | Short product description |
| `price` | String | Current price |
| `regularPrice` | String | Regular price (before any discount) |
| `salePrice` | String | Sale price (empty if not on sale) |
| `currency` | String | ISO 4217 currency code (e.g., `USD`, `EUR`, `GBP`) |
| `currencySymbol` | String | Currency symbol (e.g., `$`, `€`, `£`) |
| `onSale` | Boolean | Whether the product is currently on sale |
| `priceHtml` | String | Formatted price with currency |
| `averageRating` | String | Average customer rating (0-5) |
| `reviewCount` | Integer | Number of customer reviews |
| `images` | Array | Product images with `src` and `alt` fields |
| `mainImageUrl` | String | URL of the main product image |
| `categories` | Array | Product categories with `id`, `name`, `slug` |
| `tags` | Array | Product tags with `id`, `name`, `slug` |
| `attributes` | Array | Product attributes (e.g., Size, Color) with terms |
| `variationCount` | Integer | Number of product variations |
| `inStock` | Boolean | Whether the product is in stock |
| `isPurchasable` | Boolean | Whether the product can be purchased |
| `storeUrl` | String | The store URL that was scraped |
| `scrapedAt` | String | ISO 8601 timestamp of when data was collected |

### Categories

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Category ID |
| `name` | String | Category name |
| `slug` | String | URL-friendly slug |
| `parent` | Integer | Parent category ID (0 if top-level) |
| `count` | Integer | Number of products in this category |
| `description` | String | Category description |
| `image` | String | Category image URL |

### Tags

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Tag ID |
| `name` | String | Tag name |
| `slug` | String | URL-friendly slug |
| `count` | Integer | Number of products with this tag |

### Attributes

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Attribute ID |
| `name` | String | Attribute name (e.g., Color, Size) |
| `slug` | String | URL-friendly slug |
| `type` | String | Attribute type |
| `terms` | Array | Available terms/values for this attribute |

### Reviews

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Review ID |
| `productId` | Integer | ID of the reviewed product |
| `productName` | String | Name of the reviewed product |
| `reviewer` | String | Reviewer name |
| `rating` | Integer | Star rating (1-5) |
| `review` | String | Review text (plain text) |
| `dateCreated` | String | Review date |
| `verified` | Boolean | Whether the reviewer is a verified buyer |

### Sample product output

```json
{
    "resourceType": "product",
    "id": 63344,
    "name": "Beef Fajita Meat – 2LB",
    "slug": "beef-fajita-meat-2lb",
    "type": "simple",
    "url": "https://porterandyork.com/product/beef-fajita-meat-2lb/",
    "sku": "PY0775",
    "description": "Elevate your next meal with our premium Beef Fajita Meat...",
    "shortDescription": "",
    "price": "15",
    "regularPrice": "15",
    "salePrice": "",
    "currency": "USD",
    "currencySymbol": "$",
    "onSale": false,
    "priceHtml": "$15",
    "averageRating": "0",
    "reviewCount": 0,
    "images": [
        {
            "src": "https://porterandyork.com/wp-content/uploads/Beef-Fajita-Meat-scaled.jpg",
            "alt": "Beef Fajita Meat"
        }
    ],
    "mainImageUrl": "https://porterandyork.com/wp-content/uploads/Beef-Fajita-Meat-scaled.jpg",
    "categories": [
        { "id": 591, "name": "Poultry", "slug": "poultry" },
        { "id": 17, "name": "Chicken", "slug": "buy-chicken-online" }
    ],
    "tags": [],
    "attributes": [],
    "variationCount": 0,
    "inStock": true,
    "isPurchasable": true,
    "storeUrl": "https://porterandyork.com",
    "scrapedAt": "2026-04-06T16:49:59.137187+00:00"
}
```

## Supported stores

This scraper works with any online store powered by WooCommerce, including stores using:

- Default WooCommerce themes (Storefront, etc.)
- Custom themes built on WooCommerce
- Page builders (Elementor, Divi, etc.) with WooCommerce integration
- WooCommerce with multi-currency plugins

## Tips for best results

- **Start small**: Set `maxProductsPerStore` to 10-20 for your first run to test compatibility with the target store
- **Use the Store API path**: Most WooCommerce stores have the public Store API enabled by default. The scraper automatically detects and uses it — no configuration needed
- **Proxy is optional**: The API path usually works without proxies. Only enable a proxy if the store blocks direct requests
- **Multiple resource types**: Scrape products, categories, tags, and attributes in a single run to build a complete catalog picture
- **Search feature**: Use `searchQuery` to find specific products instead of scraping the entire catalog

## Limitations

- **Reviews**: Some stores restrict the WordPress comments API (used for reviews). If reviews return empty, the store has this endpoint locked down
- **HTML fallback**: When the Store API is unavailable, the HTML scraper provides fewer data fields. Some fields like `sku` and detailed attributes may be limited
- **Private stores**: Stores behind login walls or password protection cannot be scraped
- **Custom endpoints**: Stores with heavily customized REST API routes may need manual URL adjustment

## FAQ

**Does this scraper work with all WooCommerce stores?**
Yes, it works with any publicly accessible WooCommerce store. It automatically detects the best scraping method (API or HTML) for each store.

**Do I need a proxy?**
Usually no. The WooCommerce Store API is a public endpoint designed for storefront use, so most stores allow direct access. Enable a proxy only if you experience blocking.

**How many products can I scrape?**
Set `maxProductsPerStore` to `0` to scrape up to 10,000 products per store. For larger catalogs, consider running multiple times with different search queries.

**Can I scrape product variations?**
The scraper reports the number of variations (`variationCount`) and the available attributes. Individual variation details (specific prices, SKUs per variant) are included in the attributes field.

**What currencies are supported?**
All currencies supported by WooCommerce are handled automatically. The `currency` field contains the ISO 4217 code (e.g., USD, EUR, GBP, AED) and `currencySymbol` contains the display symbol.

**How do I scrape only specific categories?**
Use the `searchQuery` field to filter products by keyword. For category-specific scraping, you can combine search terms that match the category names.

**What happens if a store URL is invalid?**
Invalid URLs are handled gracefully — the scraper logs a warning and continues to the next store. It will not crash or fail the entire run.

**Can I export the data?**
Yes, results can be exported as JSON, CSV, Excel, or XML directly from the Apify platform.

**How often is the data updated?**
Each run extracts fresh data. You can schedule recurring runs on Apify to keep your data current.

**Is there a limit on the number of stores per run?**
There is no hard limit. You can scrape multiple stores in a single run by adding them to the `storeUrls` array.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/woocommerce-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
