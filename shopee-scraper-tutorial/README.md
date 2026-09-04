# Shopee Scraper Tutorial: Run This Apify Actor with Python

Scrape Shopee - Southeast Asia's leading marketplace (MY, SG, TH, PH, VN, ID). Shop profiles with ratings and followers, public shop product feeds, full item detail pages (price, discounts, ratings, sold, stock, variations, images) and category browsing.

This repository shows how to run [Shopee Scraper](https://apify.com/crawlerbros/shopee-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/shopee-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/shopee-scraper](https://apify.com/crawlerbros/shopee-scraper)
- **SEO title:** Shopee Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Shopee - Southeast Asia's leading marketplace (MY, SG, TH, PH, VN, ID). Shop profiles with ratings and followers, public shop product feeds, full item detail pages (price, discounts, ratings, sold, stock, variations, images) and category browsing.

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

# Shopee Scraper

Scrape **Shopee** — Southeast Asia's leading e-commerce marketplace — across 6 markets (Malaysia, Singapore, Thailand, Philippines, Vietnam, Indonesia). Pull shop profiles (ratings, followers, response time), public shop product feeds, full item detail pages (prices, discounts, ratings, sold counts, stock, variations, images, category paths) and category listings. Browser-based (Playwright). No login, no cookies required.

## What this actor does

- **Four modes:** `shopProducts` (shop profile + product feed), `itemByUrl` (full item detail), `browseByCategory` (curated categories), `shopProfile` (shop profile only)
- **6 markets:** `MY` / `SG` / `TH` / `PH` / `VN` / `ID` domains with correct local currencies (MYR, SGD, THB, PHP, VND, IDR)
- **Shop profiles:** name, rating, followers, item count, response time, official/verified badges, description, account age
- **Item details:** price range, original price, discount %, sold & 30-day sold, stock, ratings, likes, variations, images, category path, listing date
- **Filters:** min/max price, minimum rating, keyword in title
- **Anti-bot resilience:** when Shopee blocks an item feed (error `90309999`), the mode still emits its verified public record (shop profile or category taxonomy) instead of failing, and an optional Apify proxy is engaged automatically
- **Empty fields are omitted**

## Data Source

Shopee (shopee.com.my and the SG/TH/PH/VN/ID domains). Shop profiles, item pages and category data are public; the actor reads them through Shopee's public API surface and pages.

## Limitations

- **Keyword search is login-gated on Shopee and is deliberately NOT supported.** Shopee requires an account to serve keyword search results to automated clients, so this actor is built around what is public without login: shop profiles, shop product feeds, item detail pages and category browsing.
- Shopee's anti-bot layer (error `90309999`) intermittently blocks the *item-feed* endpoints (`shop/search_items`, `search/search_items`, `item/get`) from datacenter IPs. When this happens the actor still emits the mode's verified public record — the shop profile in `shopProducts`/`shopProfile`, the category taxonomy record in `browseByCategory` — and reports what was blocked. Enabling the optional **Apify proxy** (engaged automatically only on a detected block) significantly improves feed success.
- Shopee's API also answers `service_err` (error `1000000`) on some domain/IP combinations — an API-level block that affects *every* shop on that domain, not a not-found. The actor treats it as a block (proxy escalation) rather than a missing shop. Only `invalid_username` (error `2003013`) is reported as "shop not found".
- Shop detail and shop-page SSR data may be market-gated by the requesting IP (e.g. a datacenter IP in the MY region typically sees only the MY market; SG/TH/PH/VN/ID APIs return `service_err`). Use a proxy located in the target market for non-MY domains.
- Item detail mode (`itemByUrl`) tries the API first and the SSR item page second (both are independent paths); if both are blocked, zero records are emitted with a clear status message.
- Prices are in the market's local currency (e.g. MYR on shopee.com.my). Range prices (`priceMin`/`priceMax`) are kept separate from the single `price` shown on the card.
- Category IDs are shared across Shopee's SEA domains; sub-categories differ per market.

## Output

### Per shop (`recordType: "shop"`)

- `shopId`, `shopName`, `username`, `country`
- `ratingStar`, `ratingGood`, `ratingBad`, `ratingNormal`
- `followerCount`, `itemCount`, `responseTimeSeconds`
- `createdTimestamp`, `lastActiveTimestamp`, `cancellationRate`
- `isOfficialShop`, `isShopeeVerified`, `isPreferredPlusSeller`, `showOfficialShopLabel`
- `hasFlashSale`, `hasInShopFlashSale`, `hasBrandSale`, `hasJoinedMembership`
- `showLiveTab`, `isSemiInactive`, `vacation`, `isFollowed`, `status`
- `description`, `sourceUrl`, `scrapedAt`, `recordType`

### Per item (`recordType: "item"`)

- `itemId`, `shopId`, `shopName`, `shopUsername`, `title`
- `price`, `priceMin`, `priceMax`, `priceOriginal`, `discountPercent`, `currency`
- `sold` (historical sold), `soldLast30Days`, `stock`
- `ratingStar`, `ratingCount`, `likeCount`
- `categoryId`, `category`, `categoryPath`, `location`, `listedTimestamp`, `itemStatus`
- `variations[]` (e.g. `Colour: Red, Blue, Green`), `description`
- `images[]`, `imageCover` (Shopee CDN URLs)
- `sourceUrl`, `scrapedAt`, `recordType`

### Per category (`recordType: "category"`)

- `categoryId`, `category`, `sourceUrl`, `scrapedAt`, `recordType`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `shopProducts` | `shopProducts` / `itemByUrl` / `browseByCategory` / `shopProfile` |
| `shopUrl` | string | `appleflagship.store` | Shop username or page URL (mode=shopProducts/shopProfile) |
| `itemUrl` | string | – | Item page URL (mode=itemByUrl) |
| `category` | string | – | Curated Shopee category (26 options, mode=browseByCategory) |
| `domain` | string | `MY` | `MY` / `SG` / `TH` / `PH` / `VN` / `ID` |
| `minPrice` | int | – | Drop items below this (local currency) |
| `maxPrice` | int | – | Drop items above this (local currency) |
| `minRating` | number | `0` | Keep items rated at least this (0–5) |
| `containsKeyword` | string | – | Keep items whose title contains this text |
| `maxItems` | int | `50` | Hard cap (1–500) |
| `proxyConfiguration` | object | off | Optional Apify proxy, engaged automatically on block |

### Example: shop products (Malaysia)

```json
{
  "mode": "shopProducts",
  "shopUrl": "appleflagship.store",
  "domain": "MY",
  "maxItems": 30
}
```

### Example: shop profile only

```json
{
  "mode": "shopProfile",
  "shopUrl": "https://shopee.sg/sony.os",
  "domain": "SG"
}
```

### Example: item detail by URL

```json
{
  "mode": "itemByUrl",
  "itemUrl": "https://shopee.com.my/extended-waterproof-gloves--i.169104911.6601357248",
  "domain": "MY"
}
```

### Example: category browse with filters

```json
{
  "mode": "browseByCategory",
  "category": "Mobile & Accessories",
  "domain": "MY",
  "minPrice": 50,
  "maxPrice": 2000,
  "minRating": 4.5,
  "containsKeyword": "samsung",
  "maxItems": 40
}
```

## Use cases

- **Marketplace monitoring** — track shops, products, prices and discounts across SEA markets
- **Brand intelligence** — follower growth, rating trends and item counts for official stores
- **Competitor pricing** — price ranges, original prices and discount patterns per category
- **Product research** — ratings, sold counts and stock for demand estimation
- **Localized data pipelines** — currency-aware (MYR/SGD/THB/PHP/VND/IDR) e-commerce datasets

## FAQ

**What is the data source?** Shopee (shopee.com.my / .sg / .co.th / .ph / .vn / .co.id). This actor is a third-party tool and is not affiliated with or endorsed by Shopee.

**Why can't I scrape keyword search results?** Shopee gates keyword search behind a login wall for automated access. This actor deliberately avoids search and uses the public storefront surfaces instead — shop profiles, shop product feeds, item pages and category browse.

**Why did I get only a shop profile (or category) record and no items?** Shopee's anti-bot layer intermittently blocks the item-feed endpoints from datacenter IPs. The actor always emits the verified public record first, then attempts the feed. Enable the optional Apify proxy and retry — it is engaged automatically on the retry after a block.

**Do I need an account or cookies?** No. Everything this actor reads is public.

**What currency are prices in?** The market's local currency: MYR (MY), SGD (SG), THB (TH), PHP (PH), VND (VN), IDR (ID).

**What are `priceMin`/`priceMax` vs `price`?** Shopee items can show a price range (e.g. size-based). The range is kept in `priceMin`/`priceMax`; `price` is the displayed card price (range minimum when they differ).

**Why are some fields missing?** Empty fields are omitted by design — e.g. items without a discount have no `priceOriginal`/`discountPercent`, and unrated items have no `ratingStar`.

**Is this free to run?** The actor uses the free Playwright base image. The optional proxy is only used after a block is detected, so most runs cost nothing extra.

**How fresh is the data?** Live — shop profiles, items and categories are fetched at run time.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/shopee-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
