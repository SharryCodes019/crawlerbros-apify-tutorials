# EBAY | Single Item | Store | Store Categories Tutorial: Run This Apify Actor with Python

Extract detailed product data from eBay individual item pages, seller store fronts, and store category pages. Get rich data including item specifics, all images, seller details, shipping/return terms, and more.

This repository shows how to run [EBAY | Single Item | Store | Store Categories](https://apify.com/crawlerbros/ebay-item-store-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ebay-item-store-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ebay-item-store-scraper](https://apify.com/crawlerbros/ebay-item-store-scraper)
- **SEO title:** EBAY | Single Item | Store | Store Categories Tutorial: Run This Apify Actor with Python
- **Description:** Extract detailed product data from eBay individual item pages, seller store fronts, and store category pages. Get rich data including item specifics, all images, seller details, shipping/return terms, and more.

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

# eBay Product Details Scraper — Single Item, Store & Store Categories

Extract detailed product data from eBay individual item pages, seller store fronts, and store category pages. Get comprehensive product information including item specifics, all high-resolution images, seller details, shipping terms, return policies, and more.

## What does this scraper do?

This actor extracts **rich, detailed product data** from three types of eBay pages:

- **Individual item pages** (`/itm/` URLs) — full product details with 22 data fields
- **Seller store pages** (`/str/` URLs) — discovers and scrapes all products from a seller's store
- **Store category pages** — scrapes products from specific categories within a seller's store

Unlike search result scrapers that only extract card-level data, this actor visits each product page to collect complete item specifics, all images, seller ratings, shipping/return terms, stock levels, and sales data.

> **Note**: Some fields may be empty for certain listings: `originalPrice` (only when discounted), `soldCount`/`watchCount`/`availableQuantity` (not shown on all listings), `bids` (only for auctions), and `sellerFeedbackPercent` (new sellers with zero feedback).

## Features

- Extract 22 detailed data fields per product
- Full item specifics extraction (Brand, Model, Processor, RAM, etc.)
- All high-resolution product images (up to 1600px)
- Seller details with feedback score and positive rating percentage
- Shipping cost, return policy, and item location
- Stock availability and units sold count
- Works with Buy It Now and Auction listings
- Automatic pagination for store pages
- Lightweight HTTP-based extraction for item pages (low compute cost)
- No login or cookies required

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `startUrls` | Array | Yes | — | eBay item, store, or store category URLs |
| `maxItems` | Integer | No | 50 | Maximum number of items to scrape |
| `proxy` | Object | No | No proxy | Proxy configuration. Works without proxy by default. Enable residential proxy if you experience blocks. |

### Supported URL Formats

- **Single item**: `https://www.ebay.com/itm/267153498498`
- **Single item (with title)**: `https://www.ebay.com/itm/Product-Title-Here/267153498498`
- **Seller store**: `https://www.ebay.com/str/thriftbooks`
- **Store category**: `https://www.ebay.com/str/thriftbooks/Fiction/_i.html?_sacat=261186`

### Example Input

```json
{
    "startUrls": [
        { "url": "https://www.ebay.com/itm/267153498498" }
    ],
    "maxItems": 10
}
```

### Scraping a Seller Store

```json
{
    "startUrls": [
        { "url": "https://www.ebay.com/str/thriftbooks" }
    ],
    "maxItems": 50
}
```

## Output

Each scraped product contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `url` | String | Direct URL to the item listing |
| `id` | String | eBay item ID |
| `title` | String | Full product title |
| `price` | String | Current price with currency (e.g., "US $384.92") |
| `originalPrice` | String | Original price if item is discounted |
| `condition` | String | Item condition (New, Used, Refurbished, etc.) |
| `seller` | String | Seller name |
| `sellerFeedbackScore` | String | Seller total feedback count |
| `sellerFeedbackPercent` | String | Seller positive feedback percentage (empty for new sellers with no feedback) |
| `sellerUrl` | String | URL to seller's eBay store |
| `availableQuantity` | String | Number of items in stock |
| `soldCount` | String | Number of units sold |
| `watchCount` | String | Number of people watching this item |
| `location` | String | Item geographic location |
| `shippingCost` | String | Shipping cost or "Free shipping" |
| `returnPolicy` | String | Return policy terms |
| `images` | Array | All high-resolution product image URLs |
| `itemSpecifics` | Object | Key-value pairs of item specifics (Brand, Model, etc.) |
| `categories` | Array | Breadcrumb category path |
| `listingType` | String | "Buy It Now" or "Auction" |
| `bids` | String | Number of bids (for auction listings) |
| `scrapedAt` | String | ISO timestamp when the item was scraped |

### Example Output

```json
{
    "url": "https://www.ebay.com/itm/267153498498",
    "id": "267153498498",
    "title": "HP Pro X360 435 G10 Laptop Touch 13.3\" AMD Ryzen 7 PRO 16GB 512GB SSD Win 11 Pro",
    "price": "US $384.92",
    "originalPrice": "",
    "condition": "Refurbished",
    "seller": "Discount Computer Depot",
    "sellerFeedbackScore": "156714",
    "sellerFeedbackPercent": "99.3%",
    "sellerUrl": "https://www.ebay.com/str/discountcomputerdepot",
    "availableQuantity": "10",
    "soldCount": "5",
    "watchCount": "12",
    "location": "Jacksonville, TX, United States",
    "shippingCost": "Free shipping",
    "returnPolicy": "30 days returns",
    "images": [
        "https://i.ebayimg.com/images/g/example1/s-l1600.jpg",
        "https://i.ebayimg.com/images/g/example2/s-l1600.jpg"
    ],
    "itemSpecifics": {
        "Brand": "HP",
        "Model": "HP Pro X360 435 G10",
        "Processor": "AMD Ryzen 7 PRO 7730U",
        "RAM Size": "16 GB",
        "SSD Capacity": "512 GB",
        "Screen Size": "13.3 in",
        "Operating System": "Windows 11 Pro",
        "Type": "Notebook/Laptop"
    },
    "categories": ["eBay", "Electronics", "Computers/Tablets & Networking", "Laptops & Netbooks"],
    "listingType": "Buy It Now",
    "bids": "",
    "scrapedAt": "2026-04-07T12:00:00.000000+00:00"
}
```

## Use Cases

- **Market Research**: Analyze product pricing, conditions, and availability across sellers
- **Price Monitoring**: Track price changes on specific eBay listings over time
- **Competitor Analysis**: Scrape competitor store inventories with full product details
- **Product Catalog Building**: Extract complete product specifications for catalog databases
- **Seller Intelligence**: Collect seller ratings, feedback scores, and store inventory data
- **Supply Chain Research**: Monitor product availability and shipping terms from suppliers

## How much does it cost to scrape eBay?

This scraper uses lightweight HTTP requests for individual item pages, keeping compute costs minimal. Store pages use a browser for initial product discovery, then HTTP for detail extraction.

| Scenario | Estimated Cost |
|----------|----------------|
| 10 individual items | ~$0.01 |
| 50 items from a store | ~$0.05 |
| 200 items from a store | ~$0.15 |

Costs depend on proxy usage and the number of pages scraped.

## Tips for Best Results

1. **Start with individual item URLs** for the lowest cost and fastest results
2. **Use store URLs** when you need to scrape an entire seller's inventory
3. **Set maxItems** to control costs when scraping large stores
4. **Works without proxy** by default. Enable residential proxies only if you experience access blocks

## FAQ

### Can I scrape eBay search results with this actor?

This actor is designed for individual item pages and seller stores. For scraping eBay search results, use the companion [eBay Items Scraper](https://apify.com/) which is optimized for search result pages and category listings.

### Does this actor support international eBay sites?

Yes, the scraper works with eBay domains worldwide including ebay.com, ebay.co.uk, ebay.de, ebay.fr, ebay.com.au, and others.

### How many items can I scrape per run?

There is no hard limit. Use the `maxItems` parameter to control the number of items scraped per run. For large stores with thousands of products, consider splitting into multiple runs.

### Does this actor need cookies or login?

No. The scraper works with publicly available eBay pages and does not require any authentication.

### What happens if an item is no longer available?

The scraper handles ended and unavailable listings gracefully. It will extract whatever data is still visible on the page.

### How is this different from eBay search scrapers?

Search scrapers extract basic card-level data (title, price, thumbnail) from search result pages. This actor visits each individual product page to extract 22 fields including full item specifics, all images, seller details, shipping/return terms, and sales data.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ebay-item-store-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
