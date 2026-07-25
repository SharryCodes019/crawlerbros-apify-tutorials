# Best Buy Scraper Tutorial: Run This Apify Actor with Python

Scrape Best Buy product listings by search keyword or product URL. Extracts SKU, price, sale price, rating, review count, model, brand, availability, and seller info. HTTP-only with hardcoded residential-proxy fallback.

This repository shows how to run [Best Buy Scraper](https://apify.com/crawlerbros/bestbuy-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bestbuy-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bestbuy-scraper](https://apify.com/crawlerbros/bestbuy-scraper)
- **SEO title:** Best Buy Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Best Buy product listings by search keyword or product URL. Extracts SKU, price, sale price, rating, review count, model, brand, availability, and seller info. HTTP-only with hardcoded residential-proxy fallback.

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

# Best Buy Scraper

Scrape Best Buy product listings by search keyword or specific product URLs. Each result is a flat record with SKU, regular + sale price, rating, brand, model, availability, and seller info. Routes through Apify residential proxy automatically when Best Buy's bot challenge fires (no proxy input needed).

## What it does

You provide a search keyword and / or a list of product URLs; the actor:

1. (If `keyword` set) Walks Best Buy's `searchpage.jsp` for matching products, paginating up to ~24 results per page.
2. Hits each product detail page and parses `application/ld+json` Product schema + `__NEXT_DATA__` prices.
3. Optionally drops out-of-stock SKUs.
4. Auto-rotates Apify residential-proxy sessions when the direct request is fingerprinted as a bot.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `keyword` | string | `sony headphones` | Free-text search — product name, brand, category. Use `keyword` *or* `productUrls`, or both. |
| `productUrls` | array of strings | `[]` | Specific Best Buy product URLs (e.g. `https://www.bestbuy.com/site/.../6505729.p?skuId=6505729`). |
| `maxResults` | integer | `24` (1–240) | Hard cap on records. |
| `skipOutOfStock` | boolean | `false` | Drop products marked out-of-stock / sold-out. |

### Example input

```json
{
  "keyword": "sony headphones",
  "productUrls": [
    "https://www.bestbuy.com/site/sony-wh-1000xm5-wireless-noise-canceling-over-the-ear-headphones-black/6505729.p?skuId=6505729"
  ],
  "maxResults": 24,
  "skipOutOfStock": false
}
```

## Output

One record per product. Empty fields are omitted (no nulls).

```json
{
  "sku": "6505729",
  "url": "https://www.bestbuy.com/site/sony-wh-1000xm5-wireless-noise-canceling-over-the-ear-headphones-black/6505729.p?skuId=6505729",
  "name": "Sony - WH-1000XM5 Wireless Noise Canceling Over-the-Ear Headphones - Black",
  "brand": "Sony",
  "model": "WH1000XM5/B",
  "image": "https://pisces.bbystatic.com/.../6505729_sd.jpg",
  "imageUrl": "https://pisces.bbystatic.com/.../6505729_sd.jpg",
  "currentPrice": 299.99,
  "regularPrice": 399.99,
  "salePrice": 299.99,
  "savings": 100.00,
  "savingsPercent": 25,
  "onSale": true,
  "currency": "USD",
  "currencySymbol": "$",
  "availability": "InStock",
  "seller": "Best Buy",
  "rating": 4.7,
  "reviewCount": 6420,
  "description": "Industry-leading noise cancellation…",
  "scrapedAt": "2026-04-26T14:23:11+00:00"
}
```

### Output fields

- **`sku`** — Best Buy's stable product SKU (extracted from `…/<sku>.p` path).
- **`url`** — direct link to the product detail page.
- **`name`** / **`description`** — product title and marketing description.
- **`brand`** / **`model`** — manufacturer + model number.
- **`image`** / **`imageUrl`** — primary product image URL. `imageUrl` is an alias for downstream-pipeline compatibility.
- **`currentPrice`** — price currently shown to the shopper.
- **`regularPrice`** / **`salePrice`** — non-sale price + sale price when on promotion.
- **`savings`** — derived: `regularPrice - salePrice` (only when both are present and sale price is lower).
- **`savingsPercent`** — derived: `round(100 * savings / regularPrice)`.
- **`onSale`** — derived boolean: `true` when `salePrice < regularPrice`.
- **`currency`** — ISO currency (always `USD` at .com).
- **`currencySymbol`** — display symbol (`$`, `€`, `£`, etc.) corresponding to `currency`.
- **`availability`** — `InStock`, `OutOfStock`, `PreOrder`, `BackOrder`, `LimitedAvailability`.
- **`seller`** — usually `Best Buy`; third-party marketplace sellers also appear.
- **`rating`** / **`reviewCount`** — aggregate review stats from Best Buy's customer reviews.
- **`scrapedAt`** — ISO-8601 UTC timestamp.

## Use cases

- **Price monitoring** — track regular vs sale price across a watch-list of SKUs.
- **Stock alerts** — combine with `skipOutOfStock: false` to detect when an item flips back to `InStock`.
- **Product research** — pull every Sony headphone on Best Buy in one run.
- **Competitive analysis** — compare Best Buy face-value with other retailers.
- **Review aggregation** — collect rating / review-count snapshots for trend analysis.

## FAQ

**Does it need a proxy?**
Not as input — the actor automatically uses Apify's residential proxy whenever Best Buy's bot-challenge fires. Keyword search renders Best Buy's React shell in a headless Chromium with the residential proxy attached; product detail pages prefer a faster HTTP-only fetch and fall back to the proxy on block.

**Is it the official API?**
No — this scraper extracts from the Best Buy website's embedded JSON-LD + `__NEXT_DATA__`. Best Buy does ship a developer API for affiliates (developer.bestbuy.com) for high-volume programmatic access.

**Why are some fields missing?**
Best Buy doesn't always populate every field. The actor follows an omit-empty contract: fields that aren't present on the source page are simply absent from the record (no nulls).

**How many results can it return?**
Up to `maxResults` (max 240, ~10 pages of results). Each product page is fetched individually — expect ~1.5–3s per product including the proxy retry budget.

**Can I scrape category pages?**
Yes — paste any Best Buy category / collection URL into `productUrls` (the actor walks anchor links on the page). Or use the `keyword` field for the standard search experience.

**Why was a specific SKU skipped?**
- `skipOutOfStock: true` drops items flagged out-of-stock.
- Bot-challenge persisted across all proxy retries (rare, ~5% of requests).
- The page didn't ship JSON-LD nor `__NEXT_DATA__` (very rare, malformed listing).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bestbuy-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
