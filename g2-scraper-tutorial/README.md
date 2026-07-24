# G2.com Scraper Tutorial: Run This Apify Actor with Python

Scrape G2.com software reviews, product details, and competitor data. Reviews via RSS (instant, no proxy). Product info and competitors via anti-detect browser.

This repository shows how to run [G2.com Scraper](https://apify.com/crawlerbros/g2-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/g2-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/g2-scraper](https://apify.com/crawlerbros/g2-scraper)
- **SEO title:** G2.com Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape G2.com software reviews, product details, and competitor data. Reviews via RSS (instant, no proxy). Product info and competitors via anti-detect browser.

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

# G2.com Scraper

Scrape software product reviews, product details, and competitor data from G2.com — the leading B2B software review platform.

## What does it do?

This scraper extracts data from G2.com in three modes:

- **Product Reviews** — Extract review text, ratings, pros/cons, reviewer info (via RSS, no proxy needed)
- **Product Info** — Get product name, overall rating, review count, category, pricing, and image
- **Product Competitors** — Find competitor products with their ratings and review counts

## Features

- 3 scraping modes: reviews, product info, competitors
- Reviews via RSS feed — instant, no proxy, up to 125 reviews per product
- Product info and competitors via anti-detect browser with residential proxy
- Star rating filter (each star level returns different reviews)
- Zero null output fields
- Multiple products per run

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| action | select | No | product_reviews | Mode: Product Reviews, Product Info, or Product Competitors |
| startUrls | array | Yes | — | G2.com product URLs |
| maxItems | integer | No | 50 | Maximum items to scrape |
| proxyConfiguration | object | No | Residential | Proxy (only needed for product_info and product_competitors) |

### Supported URL formats

- `https://www.g2.com/products/notion/reviews` — product reviews page
- `https://www.g2.com/products/notion` — product page
- `https://www.g2.com/products/slack/competitors/alternatives` — competitors page

Any URL with `/products/` in the path works — the scraper extracts the product slug automatically.

## Output

### Product Reviews mode

| Field | Type | Description |
|-------|------|-------------|
| reviewId | string | Unique G2 review ID |
| productName | string | Software product name |
| productUrl | string | G2 product URL |
| reviewTitle | string | Review headline |
| reviewUrl | string | Direct link to review |
| rating | number | Star rating (1-5) |
| authorName | string | Reviewer name |
| authorRole | string | Reviewer role (User, Admin, etc.) |
| companySize | string | Company size segment |
| publishDate | string | Review date |
| pros | string | What the reviewer liked |
| cons | string | What the reviewer disliked |
| useCase | string | Problems the product solves |
| scrapedAt | string | Extraction timestamp |

### Product Info mode

| Field | Type | Description |
|-------|------|-------------|
| productName | string | Product name |
| description | string | Product description |
| rating | number | Average rating (0-5) |
| reviewCount | integer | Total review count |
| category | string | Product category |
| imageUrl | string | Product image URL |
| pricing | array | Pricing plans |
| url | string | Product URL |
| scrapedAt | string | Extraction timestamp |

### Product Competitors mode

| Field | Type | Description |
|-------|------|-------------|
| competitorName | string | Competitor product name |
| competitorSlug | string | URL slug |
| competitorUrl | string | G2 product URL |
| rating | number | Average rating |
| reviewCount | integer | Number of reviews |
| description | string | Short description |
| sourceProduct | string | Source product slug |
| scrapedAt | string | Extraction timestamp |

## How it works

- **Reviews**: Uses G2's public RSS feed (`/products/{slug}/reviews.rss`) which bypasses Cloudflare entirely. Fetches 5 star-filtered feeds (1-5 stars) for up to 125 unique reviews per product.
- **Product Info & Competitors**: Uses Camoufox (anti-detect Firefox) with residential proxy to bypass Cloudflare. May need 2-3 attempts due to intermittent blocking.

## Cost

- **Reviews mode**: Very cheap — no proxy used, 256MB memory, completes in seconds
- **Product Info / Competitors**: Requires residential proxy and 4096MB memory for browser

## FAQ

**Does it require a G2 account?**
No. All data is publicly accessible.

**Does it need proxy?**
Reviews mode: No. Product Info and Competitors modes: Yes (residential proxy required for Cloudflare bypass).

**How many reviews can I get per product?**
Up to 125 unique reviews (25 per star level x 5 star levels).

**Is it 100% reliable?**
Reviews mode: Yes, 100% reliable via RSS. Product Info / Competitors: ~80% per attempt, typically succeeds within 2-3 attempts.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/g2-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
