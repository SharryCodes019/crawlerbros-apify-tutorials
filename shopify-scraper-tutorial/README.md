# Shopify Scraper Tutorial: Run This Apify Actor with Python

Scrape products from any Shopify store. Extract product titles, prices, variants, SKUs, images, descriptions, inventory availability, and more using Shopify's public products.json API.

This repository shows how to run [Shopify Scraper](https://apify.com/crawlerbros/shopify-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/shopify-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/shopify-scraper](https://apify.com/crawlerbros/shopify-scraper)
- **SEO title:** Shopify Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape products from any Shopify store. Extract product titles, prices, variants, SKUs, images, descriptions, inventory availability, and more using Shopify's public products.json API.

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

# Shopify Scraper

Scrape product data from any Shopify store. Extract product titles, descriptions, prices, variants, SKUs, images, tags, inventory availability, and more.

## What can this scraper do?

- **Scrape any Shopify store** — Works with all Shopify-powered online stores (custom domains and .myshopify.com)
- **Product details** — Extract titles, descriptions, vendors, product types, and tags
- **Pricing data** — Get current prices and compare-at prices for sale detection
- **Variants and SKUs** — Full variant information including SKU, price, and stock availability per variant
- **Product images** — All image URLs for each product
- **Inventory status** — Check which products and variants are currently in stock
- **Fast and lightweight** — Uses Shopify's public products.json API with pure HTTP requests (no browser needed)
- **Bulk extraction** — Scrape hundreds or thousands of products with automatic pagination

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `storeUrl` | string | Yes | — | Shopify store URL (e.g., `https://www.allbirds.com` or `https://shop-name.myshopify.com`) |
| `maxProducts` | integer | No | 50 | Maximum number of products to scrape (minimum 1) |
| `proxy` | object | Yes | Apify Proxy (AUTO) | Proxy configuration. The scraper automatically escalates to a residential proxy if the datacenter proxy gets rate-limited |

### Example input

```json
{
    "storeUrl": "https://www.allbirds.com",
    "maxProducts": 100
}
```

## Output

Each product in the dataset contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | number | Shopify product ID |
| `title` | string | Product title |
| `handle` | string | URL-friendly product slug |
| `url` | string | Full product page URL |
| `description` | string | Product description (HTML stripped) |
| `vendor` | string | Product vendor or brand name |
| `productType` | string | Product category or type |
| `tags` | array | List of product tags |
| `price` | string | Current price (from first variant) |
| `compareAtPrice` | string | Original price before discount |
| `available` | boolean | Whether any variant is in stock |
| `variants` | array | All product variants with id, title, sku, price, compareAtPrice, available, option1/2/3 |
| `images` | array | All product image URLs |
| `createdAt` | string | When the product was created in the store |
| `updatedAt` | string | When the product was last updated |
| `storeUrl` | string | The store URL that was scraped |
| `scrapedAt` | string | ISO 8601 timestamp of when the data was collected |

### Sample output

```json
{
    "id": 6707741982800,
    "title": "Men's Tree Runners",
    "handle": "mens-tree-runners",
    "url": "https://www.allbirds.com/products/mens-tree-runners",
    "description": "Our breathable, silky-smooth sneaker made with responsibly sourced eucalyptus tree fiber.",
    "vendor": "Allbirds",
    "productType": "Shoes",
    "tags": ["men", "runners", "tree"],
    "price": "98.00",
    "available": true,
    "variants": [
        {
            "id": 39804040413264,
            "title": "8 / Kauri Marine Blue (Medium Grey Sole)",
            "sku": "TR-MBG-08",
            "price": "98.00",
            "available": true,
            "option1": "8",
            "option2": "Kauri Marine Blue (Medium Grey Sole)"
        }
    ],
    "images": [
        "https://cdn.shopify.com/s/files/1/0018/6832/2368/products/image.jpg"
    ],
    "createdAt": "2022-07-08T14:11:57-07:00",
    "updatedAt": "2026-04-02T03:26:57-07:00",
    "storeUrl": "https://www.allbirds.com",
    "scrapedAt": "2026-04-02T12:00:00.000000+00:00"
}
```

## How it works

1. **URL normalization** — Extracts the store domain from any input URL
2. **API pagination** — Fetches products from the Shopify `/products.json` endpoint in batches of up to 250
3. **Data parsing** — Converts raw Shopify JSON into a clean, consistent output format
4. **Rate limiting** — Adds a polite 1-second delay between page requests to avoid overwhelming the store

## Tips for best results

- Start with a small `maxProducts` value (5-10) to verify the store works before running larger jobs
- Most Shopify stores support the `/products.json` endpoint, but some may have it disabled or behind a WAF
- If a store's WAF blocks the default datacenter proxy, the scraper automatically retries through a residential proxy — no configuration needed
- The scraper fetches up to 250 products per API request, so even large catalogs are scraped efficiently
- Custom Shopify domains (e.g., `www.allbirds.com`) and default `.myshopify.com` domains both work

## Limitations

- Only works with Shopify-powered stores — other e-commerce platforms are not supported
- Some stores disable the `/products.json` API endpoint or protect it with a firewall
- Product descriptions are stripped of HTML formatting (plain text only)
- The `price` and `compareAtPrice` fields reflect the first variant's pricing
- Stores with password-protected storefronts cannot be scraped

## Frequently Asked Questions

**Do I need an API key or Shopify account?**
No. This scraper uses the public `/products.json` endpoint that is available on most Shopify stores without authentication.

**How do I know if a store is built with Shopify?**
Try adding `/products.json` to the store URL. If it returns a JSON response with a `products` array, the store is Shopify-powered and this scraper will work.

**Can I scrape a password-protected Shopify store?**
No. Password-protected Shopify storefronts require authentication that this scraper does not support.

**How many products can I scrape?**
There is no hard limit. Set `maxProducts` to any value. The scraper paginates automatically through the store's entire catalog. Shopify returns up to 250 products per page.

**Why am I getting no results / access errors?**
Some Shopify stores use a Web Application Firewall (WAF) or rate-limiter that blocks datacenter proxy IPs. The scraper detects this automatically and retries through a residential proxy — this happens transparently, no configuration needed. If a store still returns no products, it may have disabled the `/products.json` API entirely or isn't a Shopify store.

**What data is available per variant?**
Each variant includes its ID, title, SKU, price, compare-at price, stock availability, and up to three option values (e.g., size, color, material).

**Can I get the full HTML product description?**
The scraper strips HTML tags for clean text output. The raw HTML is not included in the output.

**Does this work with Shopify Plus stores?**
Yes. Shopify Plus stores use the same `/products.json` endpoint as standard Shopify stores.

**How fast is this scraper?**
Very fast. Since it uses direct HTTP requests (no browser), it can scrape 250 products per second. A 1-second delay between pages keeps requests polite and avoids rate limiting.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/shopify-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
