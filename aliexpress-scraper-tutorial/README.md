# AliExpress Scraper Tutorial: Run This Apify Actor with Python

Scrape AliExpress search results, product details, store profiles, and customer reviews. Multi-region (com / us / ru / es / fr / de / it / nl / pt / pl / ar / tr / ko / ja / vi / th / id / he), multi-currency, with sort, price, rating, and ship-from/ship-to filters.

This repository shows how to run [AliExpress Scraper](https://apify.com/crawlerbros/aliexpress-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/aliexpress-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/aliexpress-scraper](https://apify.com/crawlerbros/aliexpress-scraper)
- **SEO title:** AliExpress Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape AliExpress search results, product details, store profiles, and customer reviews. Multi-region (com / us / ru / es / fr / de / it / nl / pt / pl / ar / tr / ko / ja / vi / th / id / he), multi-currency, with sort, price, rating, and ship-from/ship-to filters.

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

# AliExpress Scraper

Scrape AliExpress search results, product listings, store profiles, and customer reviews — across every regional storefront (global, US, RU, ES, FR, DE, IT, NL, PT, PL, AR, TR, KO, JA, VI, TH, ID, HE).

No login. No cookies required. The actor pulls the public SSR JSON state embedded in every search/store page and the public `feedback.aliexpress.com/pc/searchEvaluation.do` reviews JSON endpoint, with TLS-fingerprint-aware HTTP and an automatic Apify-residential-proxy fallback if AliExpress rate-limits the request.

---

## Features

- **5 modes**:
  - `search` — text query (e.g. *"phone case"*) → up to 60 products per page, paginated.
  - `byProduct` — fetch product detail records by numeric AliExpress item ID.
  - `byStore` — fetch store profile records by numeric store ID.
  - `byReviews` — fetch customer reviews for one or more product IDs.
  - `byUrl` — paste any AliExpress URL (search, item, store, or feedback API URL); the actor auto-detects the kind and region.
- **18 regional storefronts**: global, United States, Russia, Spain, France, Germany, Italy, Netherlands, Portugal, Poland, Arabic, Turkey, Korea, Japan, Vietnam, Thailand, Indonesia, Hebrew.
- **42 currencies**: USD, EUR, GBP, JPY, CNY, RUB, BRL, INR, AUD, CAD, HKD, TWD, KRW, SGD, MXN, ARS, CLP, COP, PEN, UYU, ILS, TRY, AED, SAR, ZAR, PLN, CHF, SEK, NOK, DKK, CZK, HUF, RON, THB, VND, PHP, IDR, MYR, NZD, PKR, EGP, NGN.
- **18 UI languages** that AliExpress localizes responses in.
- **Filters**: sort order, minimum/maximum price, minimum rating, ship-from country, ship-to country.
- **Optional review enrichment**: attach up to 200 reviews to each product record.
- **Resilient fetcher**: retries with exponential backoff; auto-escalates from datacenter IP to Apify residential proxy on rate-limit / connection-reset.

---

## Sample input

```json
{
  "mode": "search",
  "searchQuery": "phone case",
  "region": "com",
  "currency": "USD",
  "language": "en_US",
  "sortBy": "orders_desc",
  "priceMin": 0,
  "priceMax": 10,
  "ratingMin": 4,
  "shipFrom": "CN",
  "maxItems": 50,
  "maxPages": 2
}
```

## Sample output (mode=search)

```json
{
  "productId": "1005010155028387",
  "title": "Bowknot Kitty Cat 3D Silicone Soft Phone Case For iPhone 17 Pro Max",
  "productUrl": "https://www.aliexpress.com/item/1005010155028387.html",
  "imageUrl": "https://ae-pic-a1.aliexpress-media.com/kf/Se78d305732ec4f97ba23188ebce0e368X.jpg",
  "salePrice": { "amount": 4.39, "currencyCode": "USD", "formatted": "$4.39", "discountPercent": 55 },
  "originalPrice": { "amount": 9.84, "currencyCode": "USD", "formatted": "$9.84" },
  "discountPercent": 55,
  "currencyCode": "USD",
  "rating": 4.9,
  "ordersText": "5,000+ sold",
  "ordersCount": 5000,
  "sellingPoints": [
    "Free shipping over $10.00",
    "New shoppers save $5.45"
  ],
  "listedAt": "2025-10-14 00:00:00",
  "productType": "natural",
  "shipFromCountry": "CN",
  "region": "com",
  "recordType": "product",
  "siteName": "AliExpress",
  "scrapedAt": "2026-05-08T12:34:56.000+00:00"
}
```

## Sample output (mode=byReviews)

```json
{
  "productId": "1005005883203176",
  "reviewId": "5000043517822",
  "rating": 5,
  "reviewText": "Excellent quality, fast shipping, recommend!",
  "reviewerName": "M***a",
  "reviewerCountry": "BR",
  "reviewedAt": "2025-09-12 14:23:45",
  "skuInfo": "Color:Black",
  "imageUrls": ["https://ae01.alicdn.com/kf/...jpg"],
  "helpfulCount": 4,
  "recordType": "review",
  "siteName": "AliExpress",
  "scrapedAt": "2026-05-08T12:34:56.000+00:00"
}
```

---

## Modes — when to use which

| Mode | Use case | Required input |
| --- | --- | --- |
| `search` | Discover products by free-text query | `searchQuery` |
| `byProduct` | Enrich known products with metadata (title, image, store id, rating) | `productIds` |
| `byStore` | Get a store / seller profile (name, ID, follower count, opening date) | `storeIds` |
| `byReviews` | Pull customer reviews for known products | `productIds` |
| `byUrl` | One-shot — paste any AliExpress URL and the actor classifies it | `urls` |

---

## FAQ

**Do I need an AliExpress account or cookies?**
No. Every endpoint the actor uses is public.

**Do I need a proxy?**
Not for typical use. The actor speaks AliExpress's TLS fingerprint via curl_cffi and works from datacenter IPs. If you hit rate limits, enable `useProxy` (or rely on `autoEscalateOnBlock`, which is on by default and switches the actor to Apify residential proxy mid-run).

**Why is the product detail record sparser than the search-card record?**
AliExpress migrated product pages to client-side rendering — the full product JSON is fetched via signed API calls after page load, which a stateless scraper can't replicate without cookies. The actor still surfaces title, canonical URL, image, store ID, and JSON-LD price/rating when AliExpress includes them in the SSR HTML. For the richest dataset, use `mode=search` (every search-card carries title + price + rating + sales count + selling points).

**How does pricing work across regions?**
The `currency` and `language` inputs are sent via the `aep_usuc_f` cookie. AliExpress ultimately determines the currency server-side based on the exit IP's geolocation, so the returned `currencyCode` may differ from what you requested when requests are routed through a proxy in an unrelated country. Regional sub-domains (e.g. `es.aliexpress.com`) localize text but the same products appear across regions. For deterministic currency, enable `useProxy` with a residential proxy in a country that uses your target currency.

**What happens if I set price min > price max?**
The filter is dropped with a log warning and the run continues without bounds — no crash, no infinite loop.

**Can I scrape a category?**
AliExpress's `/category/{id}/...` URLs redirect to the corresponding wholesale search; pass the category as a `searchQuery` (e.g. `"cellphones"`) for the same effect.

**How many records per page?**
60 products per search page, up to 60 pages. Reviews are 20 per page; the actor paginates automatically up to your `maxReviewsPerProduct` cap.

---

## Limitations

- Product detail page is client-side rendered; only OG meta tags + JSON-LD (when present) are extracted. Use `mode=search` for the richest per-product fields.
- Variation/SKU details (color, size, dimensions) are loaded via signed mtop calls after page load — not captured.
- Shipping calculation is per-buyer / per-IP and not surfaced in the SSR HTML.
- AliExpress can rate-limit aggressive crawls; `autoEscalateOnBlock` mitigates this with residential proxy fallback. For sustained scraping, enable `useProxy` with a residential group up front.
- **Currency localisation is best-effort.** The `currency` input is sent via the `aep_usuc_f` cookie, but AliExpress may override it based on the proxy IP's geolocation (e.g. an unrelated-country proxy can return prices in the local currency of the egress IP). For deterministic pricing, enable `useProxy=true` and configure a residential proxy in a country aligned with the requested currency.
- **Some regional storefronts (e.g. `ja`, `ko`, `he`) sometimes serve a CSR-only page** that omits the `_init_data_` JSON state used for parsing; in that case the run finishes with 0 records and a status message. The `com`, `us`, `de`, `fr`, `es`, `it`, `nl`, `pt`, `pl`, `tr`, `ar`, `vi`, `th`, `id` storefronts ship SSR JSON reliably. The `ru` region (`aliexpress.ru`) uses a different site structure and is redirected internally to `www.aliexpress.com`; use `language=ru_RU` alongside `region=ru` if you want Russian-language results on the global storefront.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/aliexpress-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
