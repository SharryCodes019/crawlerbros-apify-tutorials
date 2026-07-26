# Flippa Scraper Tutorial: Run This Apify Actor with Python

Scrape digital asset listings from Flippa.com including websites, ecommerce stores, SaaS, apps, and domains. Extract price, revenue, profit, traffic, verification, seller, and industry data.

This repository shows how to run [Flippa Scraper](https://apify.com/crawlerbros/flippa-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/flippa-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/flippa-scraper](https://apify.com/crawlerbros/flippa-scraper)
- **SEO title:** Flippa Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape digital asset listings from Flippa.com including websites, ecommerce stores, SaaS, apps, and domains. Extract price, revenue, profit, traffic, verification, seller, and industry data.

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

# Flippa Scraper

Extract digital asset listings from [Flippa.com](https://flippa.com) — the marketplace for buying and selling websites, ecommerce stores, SaaS products, mobile apps, domains, and online businesses. This scraper returns clean, structured data including price, revenue, profit, traffic, verification, seller details, and industry — all in one run.

Perfect for **deal sourcing**, **due diligence**, **market research**, **competitor monitoring**, and building your own **acquisition opportunity feed**.

## What it does

- Scrapes Flippa search results from a URL or from structured filter fields
- Returns complete listing data: financials, traffic, verification, seller, and listing metadata
- Works without cookies or proxies — fast, reliable, low cost
- Supports all major property types: websites, ecommerce stores, SaaS, iOS/Android apps, domains, newsletters, digital products
- Handles Flippa's pagination automatically up to 10,000 results per query

## Input

### Option A — Paste a Flippa URL (easiest)

Set **Flippa Search URL** to any Flippa search page URL, e.g.:

```
https://flippa.com/search?filter[property_type][]=ecommerce_store&filter[status]=open
https://flippa.com/search?filter[property_type][]=saas&filter[price][min]=10000
https://flippa.com/search?search[query]=shopify
```

Filters in the URL are mapped directly to Flippa's API.

### Option B — Use structured filters

Leave **Flippa Search URL** empty and configure any combination of:

| Field | Description |
|---|---|
| **Property Type** | website, ecommerce_store, saas, ios_app, android_app, domain, newsletter, digital_product, content, service |
| **Status** | open, under_offer, closed |
| **Sale Method** | auction, classified |
| **Price Min / Max** | Asking price range in USD |
| **Revenue Min** | Minimum monthly revenue in USD |
| **Profit Min** | Minimum monthly profit in USD |
| **Verified Revenue Only** | Only listings with Flippa-verified revenue |
| **Verified Traffic Only** | Only listings with Flippa-verified traffic |
| **Search Query** | Keyword search (e.g. "shopify", "blog", "saas") |
| **Sort Order** | Newest, oldest, highest price, lowest price, highest revenue, highest profit |
| **Max Items** | Maximum number of listings to return (default 50) |

## Output

Each listing is a single JSON record with the following fields (empty fields are omitted to keep the output clean):

| Field | Description |
|---|---|
| `id` | Flippa listing ID |
| `title` | Listing title |
| `url` | Full Flippa listing URL |
| `property_name` | Property / brand name |
| `property_type` | Type of asset (website, saas, app, etc.) |
| `industry` | Industry / niche |
| `hostname` | Primary hostname of the property |
| `external_url` | External URL of the property |
| `summary` | Seller's short description |
| `price` | Current / display price in USD |
| `buy_it_now_price` | Buy-it-now price (auctions) |
| `sale_method` | `auction` or `classified` |
| `status` | Listing status |
| `bid_count` | Number of bids (auctions) |
| `reserve_met` | Whether auction reserve has been met |
| `revenue_per_month` | Monthly revenue in USD |
| `profit_per_month` | Monthly profit in USD |
| `average_revenue` | Average monthly revenue |
| `average_profit` | Average monthly profit |
| `revenue_multiple` | Price ÷ annualized revenue |
| `profit_multiple` | Price ÷ annualized profit |
| `page_views_per_month` | Monthly page views |
| `uniques_per_month` | Monthly unique visitors |
| `app_downloads_per_month` | Monthly downloads (apps) |
| `has_verified_revenue` | Revenue verified by Flippa |
| `has_verified_traffic` | Traffic verified by Flippa |
| `established_at` | When the property was established |
| `age_years` | Age of the property in years |
| `starts_at` | Listing start time |
| `ends_at` | Listing end time |
| `seller_location` | Country of the seller |
| `super_seller` | Seller is a Flippa Super Seller |
| `turnkey_listing` | Tagged as turnkey |
| `confidential` | Listing is marked confidential |
| `revenue_sources` | Revenue source tags |
| `image_url` | Listing thumbnail URL |
| `scraped_at` | UTC timestamp when scraped |

### Sample output

```json
{
  "id": "12294434",
  "title": "Profitable Shopify auto parts business",
  "url": "https://flippa.com/12294434-profitable-shopify-auto-parts-business",
  "property_name": "247 Car Spares",
  "property_type": "ecommerce_store",
  "industry": "automotive",
  "hostname": "247carspares.com",
  "price": 400000,
  "sale_method": "classified",
  "status": "open",
  "revenue_per_month": 18669,
  "profit_per_month": 8849,
  "revenue_multiple": 1.78,
  "profit_multiple": 3.77,
  "uniques_per_month": 1000,
  "established_at": "2021-01-01T00:00:00+11:00",
  "age_years": 5.28,
  "seller_location": "India",
  "image_url": "https://static2.flippa.com/thumbnail2x_68a5a412.png",
  "scraped_at": "2026-04-13T11:22:33Z"
}
```

## FAQ

**Do I need a Flippa account or API key?**
No. The scraper works against Flippa's public catalog — no login, cookies, or authentication.

**Does it need a proxy?**
No. The scraper runs without proxies in most cases and handles rate limits automatically with retries and backoff.

**Can I scrape sold listings?**
No. Flippa does not expose sold listings through its public API, so this scraper only returns active listings (open, under offer, closed).

**How many listings can I get per run?**
Flippa caps each search at 10,000 results. If you need more, split your query using narrower filters (e.g. price ranges).

**How fresh is the data?**
Every run pulls live data directly from Flippa, so the data is as current as Flippa's marketplace.

**Which property types are supported?**
All of them: websites, ecommerce stores (Shopify, WooCommerce, etc.), SaaS, iOS and Android apps, domains, newsletters, digital products, content sites, and services.

**Can I filter by category or niche?**
Yes — use the Search Query field or paste a Flippa URL with the category filter already applied.

**What happens if a listing has missing data?**
Missing fields are omitted from the record entirely — no empty or null values pollute the dataset.

**Why does an auction listing's `price` sometimes exceed my `priceMax` filter?**
Flippa's `filter[price][max]` is applied against the listing's asking / buy-it-now price, not the current bid price. Auctions that were inside the filter range at listing time can rise above it as bidding progresses — the scraper faithfully returns Flippa's current price in the `price` field, and the original asking price in `buy_it_now_price`. If you only want listings whose current price is inside a band, combine `saleMethod: "classified"` with your price filters.

**Why does a record's `property_type` sometimes differ from the category I filtered by?**
Flippa's API accepts high-level category slugs for filtering (e.g. `newsletter`, `ecommerce_store`) but returns the platform / sub-type in each record's `property_type` field (e.g. `beehiiv` for a newsletter hosted on Beehiiv, `shopify` for a Shopify store). The filter still targets the category correctly; the output field just carries more granular platform information. If you need the high-level category for grouping, dedupe by the filter you passed in rather than by the response field.

**Which `status` values actually return listings?**
Only `open`. Flippa's public API suppresses `under_offer` and `closed` listings entirely — querying those returns zero records. The schema still exposes them for completeness, but do not expect data back.

**Which `propertyType` values are populated right now?**
`ecommerce_store`, `saas`, `ios_app`, `android_app`, `domain`, `newsletter`, `service`, and `website` all return listings. `digital_product` and `content` are valid enum values but currently return zero records — Flippa has them enabled in the filter set even though no active listings exist. The scraper handles this correctly (returns an empty dataset and exits 0).

## Use cases

- **Flip hunters**: find under-priced listings by filtering on profit multiple and verified revenue
- **Content investors**: monitor the newsletter, content, and blog categories for deal flow
- **SaaS acquirers**: track SaaS listings filtered by MRR and age
- **App buyers**: scan iOS and Android app listings with verified downloads
- **Market researchers**: analyze pricing and multiples across industries
- **Agencies**: build acquisition target feeds for clients

## Notes

- Pricing is configured in the Apify UI (pay-per-event or pay-per-result).
- The scraper logs progress per page and retries automatically on transient errors and rate limits.
- The daily Apify test run uses `maxItems=5` against the default ecommerce search — verify it in the actor's Monitoring tab.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/flippa-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
