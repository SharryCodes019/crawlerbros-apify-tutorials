# eBay Items Scraper Tutorial: Run This Apify Actor with Python

Scrape eBay search results, category pages, and item listings. Extract product titles, prices, conditions, sellers, shipping costs, images, and more.

This repository shows how to run [eBay Items Scraper](https://apify.com/crawlerbros/ebay-items-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ebay-items-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ebay-items-scraper](https://apify.com/crawlerbros/ebay-items-scraper)
- **SEO title:** eBay Items Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape eBay search results, category pages, and item listings. Extract product titles, prices, conditions, sellers, shipping costs, images, and more.

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

# eBay Items Scraper

Scrape eBay search results, category pages, and item listings at scale. Extract product titles, prices, conditions, seller information, shipping costs, images, and more from any eBay page.

## What does eBay Items Scraper do?

This actor lets you extract structured data from eBay search results and category pages. Simply provide one or more eBay URLs and the scraper will automatically paginate through results and collect item data.

Whether you need to monitor competitor pricing, track product availability, conduct market research, or build a product database, this scraper handles the heavy lifting.

## Features

- Scrape eBay search results with full pagination support
- Extract up to 60 items per page automatically
- Support for multiple search URLs in a single run
- Works with eBay search pages and category pages
- Extracts 13 data fields per item
- Handles both "Buy It Now" and auction listings
- Optional proxy support for large-scale scraping
- No login or cookies required

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `startUrls` | Array | Yes | One or more eBay search or category URLs to scrape |
| `maxItems` | Integer | No | Maximum number of items to scrape (default: 50) |
| `proxy` | Object | No | Proxy configuration for Apify platform |

### Supported URL Formats

- **Search results**: `https://www.ebay.com/sch/i.html?_nkw=laptop`
- **Search with filters**: `https://www.ebay.com/sch/i.html?_nkw=laptop&_sop=12&LH_BIN=1`
- **Category pages**: `https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276`
- **Seller listings**: `https://www.ebay.com/sch/m.html?_ssn=sellername`

### Example Input

```json
{
    "startUrls": [
        { "url": "https://www.ebay.com/sch/i.html?_nkw=laptop&_sop=12" }
    ],
    "maxItems": 50
}
```

## Output

Each scraped item contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | String | eBay item ID |
| `url` | String | Direct URL to the item listing |
| `title` | String | Item title |
| `price` | String | Item price (e.g., "$299.99") |
| `condition` | String | Item condition (New, Used, Refurbished, etc.) |
| `seller` | String | Seller name |
| `shippingCost` | String | Shipping cost or "Free shipping" |
| `location` | String | Item location |
| `imageUrl` | String | URL of the item thumbnail image |
| `listingType` | String | "Buy It Now" or "Auction" |
| `bids` | String | Number of bids (for auction listings) |
| `searchUrl` | String | The search URL this item was found on |
| `scrapedAt` | String | ISO timestamp when the item was scraped |

### Example Output

```json
{
    "id": "123456789012",
    "url": "https://www.ebay.com/itm/123456789012",
    "title": "Dell Latitude 15.6\" Laptop Intel Core i7 16GB RAM 512GB SSD",
    "price": "$299.99",
    "condition": "Refurbished",
    "seller": "best_deals_store",
    "shippingCost": "Free shipping",
    "location": "United States",
    "imageUrl": "https://i.ebayimg.com/images/g/.../s-l500.jpg",
    "listingType": "Buy It Now",
    "bids": "",
    "searchUrl": "https://www.ebay.com/sch/i.html?_nkw=laptop&_sop=12",
    "scrapedAt": "2026-04-01T12:00:00.000000+00:00"
}
```

## Use Cases

- **Price monitoring**: Track prices for specific products across sellers
- **Market research**: Analyze pricing trends and product availability in a category
- **Competitor analysis**: Monitor competitor product listings and pricing strategies
- **Lead generation**: Find sellers and products in specific niches
- **Product sourcing**: Discover deals and compare prices across listings
- **Inventory tracking**: Monitor stock levels and new listings for specific items

## How Much Will It Cost?

The scraper uses Playwright with Chromium, so it requires compute units (CUs) for browser automation. A typical run scraping 50 items costs approximately 0.01-0.03 CUs depending on the number of pages paginated.

## Tips for Best Results

- Use eBay's built-in search filters in your URL (sort order, condition, price range) to get the most relevant results
- Set `maxItems` to limit costs on large searches
- For very large scrapes, consider using proxy configuration to avoid rate limiting
- The scraper extracts ~60 items per search results page

## Frequently Asked Questions

### Does this scraper require an eBay account?
No. The scraper works with publicly available eBay pages and does not require any login or authentication.

### Can I scrape eBay sites outside the US?
Yes, you can provide URLs from any eBay domain (ebay.co.uk, ebay.de, ebay.com.au, etc.). Prices and text will be in the local format.

### How many items can I scrape per run?
You can scrape hundreds of items per run. Each search results page contains approximately 60 items. Set the `maxItems` parameter to control how many items are collected.

### Do I need a proxy?
For small runs and testing, a proxy is generally not needed. For larger or frequent scrapes on the Apify platform, using a proxy is recommended to avoid potential rate limiting.

### What if some fields are empty?
Some fields may be empty depending on the listing type and available information. For example, `bids` is only populated for auction listings, and `location` may not be shown for all items. Empty fields return an empty string, never null.

### Can I scrape individual item detail pages?
This scraper focuses on search results and category listing pages. It extracts the data visible in search results without visiting each individual item page, which makes it fast and efficient.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ebay-items-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
