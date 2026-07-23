# Etsy Scraper Tutorial: Run This Apify Actor with Python

Scrape product listings from Etsy search results, categories, shops, and product pages. Extract prices, ratings, reviews, seller info, badges, and product details.

This repository shows how to run [Etsy Scraper](https://apify.com/crawlerbros/etsy-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/etsy-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/etsy-scraper](https://apify.com/crawlerbros/etsy-scraper)
- **SEO title:** Etsy Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape product listings from Etsy search results, categories, shops, and product pages. Extract prices, ratings, reviews, seller info, badges, and product details.

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

# Etsy Scraper

Scrape product listings from Etsy search results, categories, and shops. Extract prices, ratings, seller info, badges, and more from Etsy.com.

## What can this scraper do?

- **Search Etsy** — Enter keywords and extract matching product listings with prices, ratings, and seller info
- **Product details** — Extract full product information from individual listing URLs (description, materials, variations, tags)
- **Scrape categories** — Extract all listings from Etsy category pages
- **Shop products** — Get all products from a specific Etsy shop
- **Badge detection** — Identify Star Seller, Free Shipping, Bestseller, Etsy's Pick, and ad listings
- **Large result sets** — Automatically uses search variants (different sort/filter combinations) to collect more unique results
- **Bulk extraction** — Process multiple URLs and queries in a single run

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `startUrls` | URL[] | No* | — | Etsy URLs to scrape (search, category, or shop pages) |
| `searchQueries` | string[] | No* | — | Keywords to search on Etsy |
| `maxItems` | integer | No | 100 | Maximum items per URL/query (1–1,000) |
| `includeDetails` | boolean | No | false | Attempt to visit each product page for full details |

*At least one of `startUrls` or `searchQueries` is required.

### Supported URL formats

| URL Pattern | Example |
|-------------|---------|
| Search results | `https://www.etsy.com/search?q=handmade+jewelry` |
| Product listing | `https://www.etsy.com/listing/1808282840/sterling-silver-ring` |
| Shop page | `https://www.etsy.com/shop/GlassHouseDesignsUS` |
| Category page | `https://www.etsy.com/c/jewelry-and-accessories` |

### Example input

```json
{
    "startUrls": [
        {"url": "https://www.etsy.com/search?q=vintage+rings"}
    ],
    "maxItems": 50
}
```

```json
{
    "searchQueries": ["handmade candles", "personalized gifts"],
    "maxItems": 100
}
```

## Output

### Listing fields

| Field | Type | Description |
|-------|------|-------------|
| `listingId` | string | Unique Etsy listing ID |
| `shopId` | string | Etsy shop ID |
| `url` | string | Product page URL |
| `title` | string | Product title |
| `price` | string | Current price |
| `originalPrice` | string | Original price before discount |
| `currency` | string | Currency symbol |
| `discountPercent` | string | Discount percentage |
| `imageUrl` | string | Main product image URL |
| `shopName` | string | Seller shop name |
| `shopUrl` | string | Shop page URL |
| `rating` | string | Average star rating |
| `reviewCount` | string | Number of reviews |
| `badges` | object | `{starSeller, freeShipping, bestseller, etsyChoice, ad}` |
| `scrapedAt` | string | ISO 8601 timestamp |

### Sample output

```json
{
    "listingId": "1588968371",
    "shopId": "10932069",
    "url": "https://www.etsy.com/listing/1588968371/rainbow-moonstone-necklace-copper-wire",
    "title": "Rainbow Moonstone Necklace Copper Wire Wrapped Necklace Natural Gemstone Jewelry",
    "price": "31.18",
    "originalPrice": "124.73",
    "currency": "$",
    "discountPercent": "75",
    "imageUrl": "https://i.etsystatic.com/10932069/r/il/5d01ee/5450878877/il_300x300.5450878877_qp6p.jpg",
    "shopName": "tanaygemsandjewels",
    "shopUrl": "https://www.etsy.com/shop/tanaygemsandjewels",
    "rating": "4.6",
    "reviewCount": "19100",
    "badges": {
        "starSeller": false,
        "freeShipping": true,
        "bestseller": false,
        "etsyChoice": false,
        "ad": false
    },
    "scrapedAt": "2026-03-23T07:10:18.494241+00:00"
}
```

## How it works

1. **URL processing** — Accepts search URLs, product URLs, shop URLs, category URLs, and keyword queries
2. **Multi-layer extraction** — Uses HTTP requests with Chrome TLS fingerprint impersonation, with browser automation as fallback
3. **Search flow** — For keyword searches, types queries into Etsy's search bar (mimics real user behavior)
4. **Data extraction** — Extracts listing data from JSON-LD structured data and page DOM with multiple fallback selectors
5. **Search variants** — When more items are needed, automatically tries different sort orders and price filters to collect unique results beyond the first page
6. **Pagination** — Automatically loads multiple pages to reach the requested number of items
7. **Session rotation** — If a session is blocked, automatically retries with a fresh browser session

## Tips for best results

- Start with a small `maxItems` (10-50) to test before running large jobs
- Use `searchQueries` for the most reliable results
- Each search page contains up to 64 products — `maxItems: 64` gets one page of results
- For larger result sets (100+), the scraper automatically uses search variants to collect more unique items
- Shop pages work well for getting a specific seller's product catalog
- Enable `includeDetails` to get full product descriptions, materials, variations, and tags
- Allow some time between runs to avoid IP rate limiting

## Limitations

- Etsy uses aggressive anti-bot protection; some sessions may be blocked
- The scraper automatically retries with fresh sessions (up to 5 attempts)
- **Rating and review count** are available on search result cards but not on shop page cards
- **Product page details** use an HTTP-first approach with Chrome TLS fingerprint impersonation, which works in most cases but may occasionally be blocked
- International Etsy pages (etsy.com/uk/, etsy.com/de/) are supported but results default to English
- Running too many requests in a short period from the same IP may trigger temporary blocks

## Frequently Asked Questions

**Do I need an Etsy account or API key?**
No. This scraper works without any login or API credentials.

**Why does the scraper take time to start?**
The scraper launches a real browser and visits Etsy's homepage first to establish a valid session. This warmup step takes a few seconds but is necessary to bypass anti-bot protection.

**How many products are on each Etsy search page?**
Etsy displays up to 64 products per search results page. For larger requests, the scraper uses search variants (different sort orders and filters) to collect more unique products.

**Can I scrape a single product listing?**
Yes. Provide the product URL (e.g., `https://www.etsy.com/listing/1234567890/product-name`) in `startUrls`. The scraper extracts full product details including description, materials, variations, and tags.

**Can I scrape a specific Etsy shop?**
Yes. Provide the shop URL (e.g., `https://www.etsy.com/shop/ShopName`) in `startUrls`.

**What badges are detected?**
Star Seller, Free Shipping, Bestseller, Etsy's Pick, and Ad (sponsored listing) badges.

**Can I search for products by keyword?**
Yes. Use the `searchQueries` input field with an array of keywords. Each keyword generates a separate Etsy search.

**Why are some fields empty?**
Some fields like `originalPrice` and `discountPercent` are only populated for items on sale. Rating and review count are available on search result cards but may not appear on shop page listings.

**What happens if the scraper gets blocked?**
The scraper automatically retries with a fresh browser session. It tries up to 5 sessions per task, first without proxy, then with residential proxy. If all attempts fail, the task is skipped and the next URL/query is processed.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/etsy-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
