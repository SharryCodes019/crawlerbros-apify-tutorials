# Google Shopping Scraper Tutorial: Run This Apify Actor with Python

Scrape Google Shopping search results. Extract product titles, prices, merchant names, ratings, reviews, images, and shipping info for any search query.

This repository shows how to run [Google Shopping Scraper](https://apify.com/crawlerbros/google-shopping-insights) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-shopping-insights`
- **Apify Store:** [https://apify.com/crawlerbros/google-shopping-insights](https://apify.com/crawlerbros/google-shopping-insights)
- **SEO title:** Google Shopping Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Google Shopping search results. Extract product titles, prices, merchant names, ratings, reviews, images, and shipping info for any search query.

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

# Google Shopping Scraper — Product Prices, Merchants & Reviews

Extract product data from Google Shopping search results. Get prices, merchant names, ratings, reviews, delivery info, and discount details for any search query across 39 countries.

## What does this scraper do?

This actor searches Google Shopping for your queries and extracts structured product data from the results. Each result includes the product title, current price, original price (if discounted), merchant name, rating, review count, and delivery information.

## Features

- Search Google Shopping for any product query
- Extract product prices with currency detection
- Get merchant/store names for each listing
- Collect ratings and review counts
- Detect discounted items with original prices
- Support for 39 countries with localized pricing
- Filter by condition (New, Used, Refurbished)
- Sort by relevance, review score, or price
- Price range filtering (min/max)
- Automatic retry with proxy rotation for reliability

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `queries` | Array | Yes | — | Product search queries (e.g., "iPhone 15 Pro Max") |
| `maxResultsPerQuery` | Integer | No | 20 | Maximum products per query (1-100) |
| `countryCode` | String | No | "us" | Country for localized results (39 countries) |
| `languageCode` | String | No | "en" | Language for results |
| `sortBy` | String | No | "" | Sort: relevance, review_score, price_low, price_high |
| `condition` | String | No | "" | Filter: new, used, refurbished |
| `minPrice` | Integer | No | — | Minimum price filter |
| `maxPrice` | Integer | No | — | Maximum price filter |
| `proxyConfiguration` | Object | No | GOOGLE_SERP proxy | Proxy config (GOOGLE_SERP proxy provides reliable Google access) |

### Example Input

```json
{
    "queries": ["iPhone 15 Pro Max"],
    "maxResultsPerQuery": 10,
    "countryCode": "us",
    "languageCode": "en"
}
```

### Multiple Queries

```json
{
    "queries": ["laptop", "wireless headphones", "running shoes"],
    "maxResultsPerQuery": 20
}
```

## Output

Each result represents one product from Google Shopping search results:

| Field | Type | Description |
|-------|------|-------------|
| `query` | String | Search query used |
| `position` | Integer | Position in results (1-based) |
| `title` | String | Product title |
| `price` | String | Current price with currency (e.g., "$999.00") |
| `originalPrice` | String | Original price if discounted (e.g., "$1,200") |
| `currency` | String | Currency code (USD, EUR, GBP, etc.) |
| `merchant` | String | Store or merchant name |
| `rating` | String | Average rating (e.g., "4.5") |
| `reviewCount` | String | Number of reviews (e.g., "1,234") |
| `imageUrl` | String | Product thumbnail image URL |
| `delivery` | String | Delivery info (e.g., "Free delivery") |
| `isSponsored` | Boolean | Whether this is a sponsored/ad result |
| `searchUrl` | String | Google Shopping search URL |
| `scrapedAt` | String | ISO timestamp when scraped |

### Example Output

```json
{
    "query": "laptop",
    "position": 1,
    "title": "HP Victus 15.6 inch FHD 144Hz Gaming Laptop Intel Core i5-13420H",
    "price": "$736.00",
    "originalPrice": "$1,020",
    "currency": "USD",
    "merchant": "Best Buy",
    "rating": "4.6",
    "reviewCount": "1.4K",
    "imageUrl": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSwhzmT1uDz...",
    "delivery": "Free delivery",
    "isSponsored": false,
    "searchUrl": "https://www.google.com/search?q=laptop&tbm=shop&hl=en&gl=us",
    "scrapedAt": "2026-04-08T12:09:58.291853+00:00"
}
```

## Use Cases

- **Price Monitoring**: Track product prices across merchants over time
- **Competitive Analysis**: Compare pricing strategies of different sellers
- **Market Research**: Discover product trends, pricing patterns, and merchant landscapes
- **Deal Detection**: Find discounted products by tracking original vs current prices
- **Product Catalog Building**: Build databases of products with pricing and reviews
- **Merchant Intelligence**: Analyze which merchants sell which products at what prices

## How much does it cost?

The scraper uses residential proxy for reliable access to Google Shopping. Cost depends on the number of queries and results requested.

| Scenario | Estimated Cost |
|----------|----------------|
| 1 query, 5 results | ~$0.10 |
| 5 queries, 20 results each | ~$0.50 |
| 10 queries, 50 results each | ~$1.50 |

Costs vary based on proxy usage and retry attempts needed.

## Tips for Best Results

1. **Use specific queries** for more relevant results (e.g., "iPhone 15 Pro Max 256GB" instead of just "iPhone")
2. **Set country code** to get localized prices and merchants
3. **Use filters** (condition, price range) to narrow results
4. **Keep maxResultsPerQuery reasonable** (20-50) for faster runs
5. **Proxy is required** — Google blocks datacenter IPs. GOOGLE_SERP proxy is recommended

## Supported Countries

United States, United Kingdom, Canada, Australia, Germany, France, Spain, Italy, Brazil, Mexico, India, Japan, South Korea, Netherlands, Belgium, Austria, Switzerland, Sweden, Norway, Denmark, Finland, Poland, Czech Republic, Portugal, Ireland, New Zealand, South Africa, Singapore, Hong Kong, Taiwan, Philippines, Thailand, Indonesia, Malaysia, Vietnam, Argentina, Chile, Colombia, Peru, Turkey, Russia, Ukraine, Israel, UAE, Saudi Arabia, Egypt, Nigeria, Kenya.

## FAQ

### Does this actor need cookies or login?

No. The scraper works with publicly available Google Shopping search results and does not require any authentication.

### Why is proxy required?

Google blocks automated access from datacenter IPs. The GOOGLE_SERP proxy is optimized for Google search and provides reliable access to Shopping results. Residential proxy also works as a fallback.

### How many results can I get per query?

Google Shopping typically shows 40-100 products per search page. The scraper supports pagination and can extract up to 100 results per query.

### What happens if Google blocks a request?

The scraper automatically retries with a fresh proxy session (different IP address). It makes up to 3 attempts per page, with increasing delays between retries.

### Can I scrape product detail pages?

This actor focuses on search results, which provide the key data (title, price, merchant, rating, reviews). The `productUrl` field (when available) links to Google's product comparison page for additional details.

### Does this support international pricing?

Yes. Set the `countryCode` parameter to get results in local currency. The `currency` field indicates the detected currency code (USD, EUR, GBP, etc.).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-shopping-insights)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
