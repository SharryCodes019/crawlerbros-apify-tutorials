# Noon.com E-Commerce Scraper Tutorial: Run This Apify Actor with Python

Scrape Noon.com products across UAE, Saudi Arabia, and Egypt. Search by keyword or browse by category to extract product names, prices, ratings, reviews, brands, discounts, and promotional data. No authentication required

This repository shows how to run [Noon.com E-Commerce Scraper](https://apify.com/crawlerbros/noon-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/noon-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/noon-scraper](https://apify.com/crawlerbros/noon-scraper)
- **SEO title:** Noon.com E-Commerce Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Noon.com products across UAE, Saudi Arabia, and Egypt. Search by keyword or browse by category to extract product names, prices, ratings, reviews, brands, discounts, and promotional data. No authentication required

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

## Noon.com E-Commerce Scraper

Scrape **Noon.com** products across UAE, Saudi Arabia, and Egypt — the Middle East's leading e-commerce platform. Search by keyword or browse by category to extract product names, prices, ratings, reviews, brands, discounts, and promotional labels. No authentication or proxy required.

### What this actor does

- **Three modes:** `search` (keyword), `byCategory` (category path), `byUrl` (from any Noon search or category URL)
- **Multi-market:** UAE (AED), Saudi Arabia (SAR), Egypt (EGP)
- **Full pricing detail:** selling price, original price, discount percentage, and currency
- **Sort options:** popularity, price (low/high), biggest discount, new arrivals
- **Promotional data:** Noon Express delivery tag, free delivery, stock warnings
- **Empty fields are omitted** — records only contain fields that have real values

### Output per product

- `name` — full product name
- `sku` — Noon product identifier (e.g. `N70154922V`)
- `url` — direct link to the Noon product page
- `price` — current selling price (numeric)
- `originalPrice` — pre-discount price (numeric, when discounted)
- `discountPercent` — percentage saved (numeric, when discounted)
- `currency` — ISO currency code (`AED`, `SAR`, `EGP`)
- `rating` — average star rating (0–5 scale)
- `reviewCount` — number of customer reviews
- `brand` — brand name (when shown on listing card)
- `imageUrl` — primary product image URL from Noon CDN
- `promotionTags` — active tags, e.g. `["Noon Express", "Free Delivery"]`
- `stockWarning` — low-stock message when shown (e.g. `Only 2 left`)
- `market` — market code: `uae`, `saudi`, or `egypt`
- `scrapedAt` — ISO 8601 timestamp of the scrape

### Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `search` | `search` / `byCategory` / `byUrl` |
| `market` | string | `uae` | `uae` (UAE), `saudi` (Saudi Arabia), `egypt` (Egypt) |
| `searchQuery` | string | `moisturizer` | Keyword to search for (mode=search) |
| `categoryPath` | string | – | Category URL path, e.g. `beauty-personal-care` (mode=byCategory) |
| `startUrls` | array | – | Noon search or category URLs (mode=byUrl) |
| `sortBy` | string | `popularity` | `popularity`, `price_asc`, `price_desc`, `discount`, `new_arrivals` |
| `minRating` | number | – | Only emit products with rating ≥ this value (0–5) |
| `maxItems` | int | `50` | Hard cap on emitted records (1–1000) |

#### Example: search for laptops in UAE

```json
{
  "mode": "search",
  "market": "uae",
  "searchQuery": "laptop",
  "sortBy": "popularity",
  "maxItems": 50
}
```

#### Example: browse beauty products in Saudi Arabia

```json
{
  "mode": "byCategory",
  "market": "saudi",
  "categoryPath": "beauty-personal-care",
  "sortBy": "discount",
  "maxItems": 100
}
```

#### Example: top-rated electronics in Egypt

```json
{
  "mode": "search",
  "market": "egypt",
  "searchQuery": "smartphone",
  "sortBy": "popularity",
  "minRating": 4.0,
  "maxItems": 50
}
```

#### Example: scrape from a Noon URL

```json
{
  "mode": "byUrl",
  "startUrls": [
    "https://www.noon.com/uae-en/search?q=perfume&sort%5Bby%5D=discount"
  ],
  "maxItems": 50
}
```

### Use cases

- **Price comparison** — track Noon prices against other MENA e-commerce platforms
- **Discount monitoring** — identify products with the highest discounts in real time
- **Brand presence analysis** — measure brand reach and product count across Noon's categories
- **Market research** — compare product availability and pricing between UAE, Saudi Arabia, and Egypt
- **Inventory intelligence** — monitor stock warnings and availability for competitive products
- **E-commerce analytics** — analyze rating distributions and review counts by category

### FAQ

**What is Noon.com?**
Noon.com is a major e-commerce marketplace in the Middle East, operating in the UAE, Saudi Arabia, and Egypt. It offers millions of products across electronics, fashion, beauty, home goods, and more.

**Which markets are supported?**
UAE (`noon.com/uae-en`), Saudi Arabia (`noon.com/saudi-en`), and Egypt (`noon.com/egypt-en`). Each market has its own product catalogue, pricing, and currency.

**How fresh is the data?**
The actor fetches live Noon pages, so prices and stock status reflect what is visible on Noon at the time of scraping.

**How many products can I scrape per run?**
Set `maxItems` up to 1000. Noon returns approximately 50 products per search/category page and the actor paginates automatically.

**What category paths can I use?**
Use the URL segment after `/uae-en/` on any Noon category page. Examples: `electronics`, `beauty-personal-care`, `fashion-women`, `home-kitchen`, `sports-outdoors`. Browse `noon.com/uae-en/electronics/` to discover paths.

**Why are some products missing brand or image?**
Noon's listing cards include brand and image data for most products, but some listings omit these. Fields that have no value are simply omitted from the output record.

**Is this actor affiliated with Noon?**
No. This is an independent third-party actor. It is not affiliated with or endorsed by Noon E-Commerce LLC or Emaar Malls Group.

**Does the actor work without a proxy?**
Yes. Noon.com is publicly accessible from Apify's datacenter IPs without requiring a proxy. If you encounter issues, running without a proxy is still the recommended configuration.

# Actor input Schema

## `mode` (type: `string`):

What to fetch from Noon.

## `market` (type: `string`):

Noon regional website to scrape.

## `searchQuery` (type: `string`):

Keyword to search for (mode=search).

## `categoryPath` (type: `string`):

Noon category URL path segment, e.g. `beauty-personal-care`, `electronics`, `home-kitchen`. From the URL after /uae-en/.

## `startUrls` (type: `array`):

Noon search or category URLs. E.g. https://www.noon.com/uae-en/search?q=serum

## `sortBy` (type: `string`):

Product sort order.

## `minRating` (type: `number`):

Only emit products with rating >= this value (0–5).

## `maxItems` (type: `integer`):

Hard cap on emitted records.

## Actor input object example

```json
{
  "mode": "search",
  "market": "uae",
  "searchQuery": "moisturizer",
  "startUrls": [],
  "sortBy": "popularity",
  "maxItems": 50
}
```

# Actor output Schema

## `products` (type: `string`):

Dataset containing all scraped Noon product records.

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
    "market": "uae",
    "searchQuery": "moisturizer",
    "startUrls": [],
    "sortBy": "popularity",
    "maxItems": 50
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/noon-scraper").call(input);

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
    "market": "uae",
    "searchQuery": "moisturizer",
    "startUrls": [],
    "sortBy": "popularity",
    "maxItems": 50,
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/noon-scraper").call(run_input=run_input)

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
  "market": "uae",
  "searchQuery": "moisturizer",
  "startUrls": [],
  "sortBy": "popularity",
  "maxItems": 50
}' |
apify call crawlerbros/noon-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/noon-scraper",
                "--header",
                "Authorization: Bearer <YOUR_API_TOKEN>"
            ]
        }
    }
}

```

## OpenAPI specification

Download the OpenAPI definition: https://api.apify.com/v2/acts/NDE38xgqtwGqpv6v6/builds/ETPYfnq67Cyq5YIG2/openapi.json

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/noon-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
