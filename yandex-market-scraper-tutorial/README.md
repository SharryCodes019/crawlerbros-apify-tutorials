# Yandex Market Scraper Tutorial: Run This Apify Actor with Python

Scrape product listings, prices, seller offers, and reviews from Yandex Market, Russia's largest e-commerce platform. Supports search, category browsing, product details with all seller offers, and review scraping.

This repository shows how to run [Yandex Market Scraper](https://apify.com/crawlerbros/yandex-market-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/yandex-market-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/yandex-market-scraper](https://apify.com/crawlerbros/yandex-market-scraper)
- **SEO title:** Yandex Market Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape product listings, prices, seller offers, and reviews from Yandex Market, Russia's largest e-commerce platform. Supports search, category browsing, product details with all seller offers, and review scraping.

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

# Yandex Market Scraper

Extract product data, prices, seller offers, and reviews from [Yandex Market](https://market.yandex.ru) — Russia's largest e-commerce and price comparison platform used by 60M+ monthly shoppers.

## What You Can Scrape

- **Product listings** — name, brand, SKU, price (current + original + discount %), rating, review count, seller details, availability, delivery info, specs, images, category hierarchy
- **All seller offers** — every seller's price for a single product, with individual seller ratings and delivery options
- **Product reviews** — author, star rating, title, text, pros/cons, date, helpful votes, photos
- **Seller reviews** — customer reviews for marketplace sellers

## Use Cases

- **Price monitoring** — track price changes across dozens of sellers for the same product
- **Competitor intelligence** — benchmark your pricing against all sellers on Yandex Market
- **Product research** — collect specs, ratings, and reviews at scale before entering a market
- **Market entry analysis** — understand price ranges, top sellers, and consumer sentiment for Russian markets

## Modes

| Mode | Description |
|------|-------------|
| `searchProducts` | Search by keyword — returns product cards with prices and ratings |
| `browseCategory` | Scrape all products in a category by URL |
| `getProductDetails` | Full product data + all seller offers for specific product URLs |
| `getReviews` | Product reviews or seller reviews from specific URLs |

## Input

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `mode` | enum | Yes | `searchProducts` | Scraping mode |
| `searchQueries` | string[] | searchProducts | — | Search keywords, e.g. `["iPhone 15", "Samsung Galaxy"]` |
| `categoryUrls` | string[] | browseCategory | — | `market.yandex.ru/catalog` URLs |
| `productUrls` | string[] | getProductDetails, getReviews | — | `market.yandex.ru/product--{slug}/{id}` URLs |
| `sellerUrls` | string[] | getReviews | — | `market.yandex.ru/shop--{slug}/{id}` URLs |
| `maxItems` | integer | No | 50 | Records per query/URL (1–1000) |
| `sortOrder` | enum | No | `relevance` | relevance, priceAsc, priceDesc, rating, popularity |
| `minPrice` | integer | No | — | Minimum price in RUB |
| `maxPrice` | integer | No | — | Maximum price in RUB |
| `minRating` | enum | No | `any` | any, 3, 3.5, 4, 4.5 |
| `reviewsSortOrder` | enum | No | `newest` | newest, highestRating, lowestRating, mostHelpful |
| `proxyConfiguration` | proxy | No | Apify RESIDENTIAL | Strongly recommended |

## Output

### Product record

```json
{
  "recordType": "product",
  "productId": "1926025774",
  "name": "Apple iPhone 15 128GB Black",
  "brand": "Apple",
  "url": "https://market.yandex.ru/product--apple-iphone-15/1926025774",
  "categoryPath": ["Electronics", "Phones", "Smartphones"],
  "rating": 4.8,
  "reviewCount": 3241,
  "price": 79990,
  "originalPrice": 89990,
  "discount": 11,
  "currency": "RUB",
  "sellerName": "re:Store",
  "sellerRating": 4.9,
  "availability": "in_stock",
  "deliveryInfo": "Delivery tomorrow",
  "specs": { "RAM": "6 GB", "Storage": "128 GB" },
  "images": ["https://avatars.mds.yandex.net/..."],
  "offers": [],
  "scrapedAt": "2026-05-18T10:00:00+00:00"
}
```

In `getProductDetails` mode, `offers[]` is populated with all seller listings:

```json
{
  "sellerName": "Связной",
  "sellerRating": 4.7,
  "price": 81500,
  "originalPrice": 85000,
  "discount": 4,
  "condition": "new",
  "deliveryInfo": "2–3 days",
  "offerUrl": "https://market.yandex.ru/offer/..."
}
```

### Review record

```json
{
  "recordType": "review",
  "reviewType": "product",
  "productId": "1926025774",
  "productName": "Apple iPhone 15 128GB Black",
  "author": "Ivan Petrov",
  "rating": 5,
  "title": "Excellent phone",
  "text": "Battery lasts all day...",
  "pros": "Great camera, fast",
  "cons": "Expensive",
  "date": "2026-01-15",
  "helpfulVotes": 42,
  "scrapedAt": "2026-05-18T10:00:00+00:00"
}
```

## Proxy

Yandex Market blocks datacenter IPs. **Apify Residential proxy is strongly recommended** and is set by default. The actor rotates proxy sessions between queries and retries failed requests with a fresh session.

## FAQs

**Does this work for Russian-language searches?**
Yes — search queries can be in Russian or English. The platform serves results in the configured locale.

**Can I scrape prices from all sellers for one product?**
Yes — use `getProductDetails` mode and set your product URL. The `offers[]` field in each result contains every seller's price, rating, and delivery info.

**How many results can I get per query?**
Up to 1000 per query/URL (set `maxItems`). Pagination is handled automatically.

**What happens if a CAPTCHA appears?**
The actor attempts automatic CAPTCHA resolution via checkbox click. If that fails, it rotates the proxy session and retries once before skipping to the next URL.

**Is this actor maintained?**
Yes — it is tested daily via Apify's automated run system. Open an issue or contact support if you encounter problems.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/yandex-market-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
