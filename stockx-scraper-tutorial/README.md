# StockX Scraper Tutorial: Run This Apify Actor with Python

Scrape StockX, sneakers, apparel, accessories, electronics, collectibles, trading cards. Search by query, brand, or category, fetch by product slug, get prices, last-sale data, and sales history. Multi-currency.

This repository shows how to run [StockX Scraper](https://apify.com/crawlerbros/stockx-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/stockx-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/stockx-scraper](https://apify.com/crawlerbros/stockx-scraper)
- **SEO title:** StockX Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape StockX, sneakers, apparel, accessories, electronics, collectibles, trading cards. Search by query, brand, or category, fetch by product slug, get prices, last-sale data, and sales history. Multi-currency.

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

# StockX Scraper

Scrape **StockX** — sneakers, apparel, accessories, electronics, collectibles,
trading cards and watches — at scale. Get product listings with current
**lowest-ask** prices, follow each tile to its product page for **last-sale**,
**highest-bid**, **release date**, **retail price**, **style ID**, and
**per-size variants**, or pull a product's **recent sales history**.

This actor is purpose-built for StockX's anti-bot stack (Cloudflare +
edge-network bot scoring): it ladders through `curl_cffi` (chrome131
TLS-fingerprint impersonation) → residential proxy → Camoufox (anti-detect
Firefox) automatically when the lower tiers get challenged.

## Use cases

- **Resale-price monitoring** — pull the lowest-ask, highest-bid and last-sale
  for any product line (Jordan 4, Yeezy 350 v2, Travis Scott, etc.) on a
  schedule.
- **New-release tracking** — list "Recently Released" sneakers daily and feed
  the slugs into byProduct mode for full detail.
- **Brand / category audits** — walk every Jordan, every Yeezy, every Rolex
  Submariner with `byBrand` or `byCategory`.
- **Sales-history backtesting** — pull recent transactions for a product and
  compute volatility, weekly volume, or seasonal patterns.
- **Multi-region pricing** — request prices in USD, EUR, GBP, JPY, AUD, CAD,
  CHF, HKD, SGD or MXN; routed through a residential proxy in the matching
  country for accurate localized pricing.

## Modes

| Mode | Input | What you get |
|------|-------|--------------|
| `search` | `searchQuery` (free-text) | Up to 40 product tiles per page, paginated |
| `byBrand` | `brand` (Nike, Jordan, Adidas, …) | All products tagged to the brand |
| `byCategory` | `category` (sneakers, apparel, …) | All products in the category |
| `byProduct` | `productSlugs[]` | One detail record per slug, with full market data |
| `byUrl` | `startUrls[]` | Mix of product / search / browse URLs |
| `salesHistory` | `productSlugs[]` | Recent transactions per product |

## Inputs

### Mode & query

- `mode` — one of `search`, `byBrand`, `byCategory`, `byProduct`, `byUrl`, `salesHistory`. Default `search`.
- `searchQuery` — free-text. Default `jordan`.
- `brand` — dropdown of 50+ StockX brands (Nike, Jordan, Adidas, Yeezy,
  New Balance, ASICS, Supreme, Off-White, Louis Vuitton, Rolex, Casio, Apple,
  LEGO, Pokémon, …).
- `category` — dropdown: sneakers, apparel, accessories, electronics,
  collectibles, trading-cards, watches.
- `productSlugs` — array of slugs (the part after `stockx.com/`). Used by
  `byProduct` and `salesHistory` modes.
- `startUrls` — array of full StockX URLs (used by `byUrl`).

### Region & locale

- `currency` — USD, EUR, GBP, JPY, AUD, CAD, CHF, HKD, SGD, MXN. Default `USD`.
- `country` — US, GB, DE, FR, IT, ES, NL, JP, AU, CA, CH, HK, SG, MX. Drives
  proxy country.

### Filters

- `sortBy` — `featured`, `most_active`, `recently_released`,
  `price_high_to_low`, `price_low_to_high`. Default `featured`.
- `minPrice`, `maxPrice` — drop products outside the lowest-ask range.

### Enrichment

- `fetchProductDetails` (boolean) — when true, follow each search tile to its
  product page and merge the richer detail record. Slower but richer. Default
  `false`.

### Limits

- `maxItems` — hard cap on emitted records. 1–1000. Default 25.
- `maxPages` — pages of search/browse to walk. 1–50. Default 5.

### Proxy & anti-bot

- `useProxy` — recommended `true`. StockX is hostile to datacenter IPs.
- `proxyConfiguration` — defaults to Apify Residential (recommended).
- `useBrowser` — set `true` to skip the HTTP tiers and go straight to
  Camoufox + residential. Slower but most reliable when StockX is hostile.

## Outputs

### Product record (modes: search / byBrand / byCategory / byProduct / byUrl)

```json
{
  "recordType": "product",
  "siteName": "StockX",
  "scrapedAt": "2026-05-08T12:00:00+00:00",
  "slug": "air-jordan-4-retro-white-cement-2025",
  "productUrl": "https://stockx.com/air-jordan-4-retro-white-cement-2025",
  "title": "Jordan 4 Retro White Cement (2025)",
  "brand": "Jordan",
  "model": "Air Jordan 4",
  "productCategory": "sneakers",
  "styleId": "FV5029-100",
  "colorway": "White/Tech Grey-Fire Red-Black",
  "releaseDate": "2025-02-15",
  "retailPrice": 215.0,
  "lowestAsk": 215.0,
  "highestBid": 195.0,
  "lastSale": 225.0,
  "salesLast72Hours": 42,
  "deadstockSold": 12500,
  "annualHigh": 260.0,
  "annualLow": 205.0,
  "volatility": 0.08,
  "averageDeadstockPrice": 228.0,
  "currency": "USD",
  "region": "US",
  "imageUrl": "https://images.stockx.com/images/Air-Jordan-4-Retro-White-Cement-2025-Product.png",
  "gallery": ["https://images.stockx.com/...", "..."],
  "variants": [
    {"size": "10", "lowestAsk": 215, "highestBid": 195, "lastSale": 225},
    {"size": "10.5", "lowestAsk": 220, "highestBid": 200, "lastSale": 228}
  ]
}
```

Search-tile records (when `fetchProductDetails: false`) carry a subset:
`slug`, `productUrl`, `title`, `lowestAsk`, `currency`, `productCategory`,
`imageUrl`, `sponsored`, `sourceUrl`.

### Sale record (mode: salesHistory)

```json
{
  "recordType": "sale",
  "siteName": "StockX",
  "scrapedAt": "2026-05-08T12:00:00+00:00",
  "chainId": "abc...",
  "amount": 215.0,
  "currency": "USD",
  "shoeSize": "10",
  "createdAt": "2025-01-01T00:00:00Z",
  "productSlug": "air-jordan-4-retro-white-cement-2025",
  "productUrl": "https://stockx.com/air-jordan-4-retro-white-cement-2025"
}
```

> Records are emitted with `strip_nulls` applied — empty strings, nulls,
> empty arrays and empty objects are never present in the dataset.

## FAQ

**Q: Do I need cookies or an account?**
A: No. StockX product/search/browse pages are public. The actor injects
`stockx_selected_currency` / `stockx_selected_region` cookies automatically
based on your `currency` and `country` inputs.

**Q: Why is residential proxy strongly recommended?**
A: StockX uses Cloudflare and additional bot-detection that flags datacenter
IPs (Hetzner, OVH, AWS, GCP, etc.) within a few requests. Residential proxy
makes search/browse reliable. The actor will auto-escalate to residential on
the first datacenter block; setting `useProxy: true` is the default.

**Q: Why are some `lowestAsk` fields missing?**
A: Products with no current asks (just released, sold out, or restocking)
display `--` on StockX. The actor omits these fields rather than emitting
a sentinel value.

**Q: Are sales-history transactions complete?**
A: We pull recent sales embedded in the product page's `__NEXT_DATA__` JSON.
Coverage depends on how much StockX hydrates server-side at request time —
typically dozens of recent sales per product.

**Q: Does the actor support cookies for logged-in features (Buyer/Seller dashboard)?**
A: Not in v1. All exposed surfaces are public. If you need account features,
open an issue.

**Q: Sometimes the run returns 0 records.**
A: Cloudflare can challenge entire ASN ranges intermittently. Try:
- Setting `useBrowser: true` to use Camoufox + residential.
- Re-running 10 minutes later (the IP may be on cooldown).
- Using a different `country` (different proxy ASN).

**Q: Can I run the actor without proxy?**
A: Yes — set `useProxy: false`. Works for a small burst, then expect blocks.

## Limitations

- Product pages frequently 403 from datacenter IPs even after a successful
  homepage warmup. Residential proxy mitigates this.
- StockX rotates obfuscated `__NEXT_DATA__` keys occasionally; the parser
  searches for products by structural heuristics (`urlKey` + `brand` /
  `productCategory`) rather than hard-coded paths, so updates don't break it.
- Sales-history coverage is per-page (whatever the product page hydrates),
  not the full historical archive.
- Multi-currency pricing depends on StockX honoring the
  `stockx_selected_currency` cookie + `x-stockx-currency` header. When the
  proxy IP is in a non-matching country, prices may revert to the IP's local
  currency.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/stockx-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
