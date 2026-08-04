# Mercari + Poshmark + Depop Scraper Tutorial: Run This Apify Actor with Python

Tri-platform fashion-resale scraper. Pull listings, sellers, brand pages, categories, and individual items from Mercari (US), Poshmark, and Depop with one actor, search by keyword, browse a category, fetch a single item, or list everything in a seller's closet/profile.

This repository shows how to run [Mercari + Poshmark + Depop Scraper](https://apify.com/crawlerbros/mercari-poshmark-depop-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/mercari-poshmark-depop-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/mercari-poshmark-depop-scraper](https://apify.com/crawlerbros/mercari-poshmark-depop-scraper)
- **SEO title:** Mercari + Poshmark + Depop Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Tri-platform fashion-resale scraper. Pull listings, sellers, brand pages, categories, and individual items from Mercari (US), Poshmark, and Depop with one actor, search by keyword, browse a category, fetch a single item, or list everything in a seller's closet/profile.

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

# Mercari + Poshmark + Depop Scraper

Tri-platform fashion-resale scraper. Pull listings, sellers, brand pages, categories, and individual items from **Mercari (US)**, **Poshmark**, and **Depop** with a single actor — no login required.

Use it to track competitor pricing, monitor a brand's secondhand availability, audit a seller's catalog, or build a multi-marketplace dataset of secondhand fashion in one place.

## What you can scrape

| Platform | Search by query | By item URL | By seller / closet | By brand | By category | Auto-detect URL |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Depop**     | yes | yes | yes | yes | — | yes |
| **Poshmark**  | yes | yes | yes | yes | yes | yes |
| **Mercari**   | yes | yes | yes | — | yes | yes |

Every mode pushes flat, omit-empty records to the dataset — no nested null/empty fields.

## Output fields

Listing records (the most common shape — fields populated when available):

- **Identity**: `platform`, `id`, `title`, `slug`, `url`, `recordType` (`listing`)
- **Pricing**: `price`, `currency`, `originalPrice`, `discountedPrice`
- **Photos**: `coverImageUrl`, `imageUrls[]`
- **Attributes**: `brand`, `category`, `categoryPath[]`, `categoryFeatures[]`, `condition`, `sizes[]`, `colors[]`
- **State**: `status` (e.g. `on_sale`, `published`, `sold`), `available`, `multiItem`
- **Engagement**: `likesCount`, `commentsCount`
- **Timestamps**: `createdAt`, `updatedAt`, `createdAtUnix`, `updatedAtUnix`
- **Seller** (nested): `id`, `username`, `displayName`, `url`, `avatarUrl`, `country`, `ratingScore`, `reviewCount`, `numItemsOnSale`, `isAmbassador`, `isBoutique`
- **Mercari extras**: `shippingPayer`, `shippingFromArea`
- **Depop extras**: `fullDescription`

Seller records (`recordType: "seller"`):

- `platform`, `id`, `username`, `displayName`, `url`, `avatarUrl`
- `bio`, `city`, `state`, `country`
- `followersCount`, `followingCount`, `listingCount`, `soldCount`
- `ratingScore`, `reviewCount`, `verified`, `isAmbassador`, `isBoutique`

Error records (`recordType: "error"`):

- `platform`, `url`, `httpStatus`, `reason`, `scrapedAt`

## Modes — quick reference

### `searchListings`
Search by free-text query. All three platforms support this.

```jsonc
{
  "platform": "depop",
  "mode": "searchListings",
  "query": "vintage levis",
  "sortBy": "relevance",
  "maxItems": 50
}
```

Filters available:
- All — `query`, `minPrice`, `maxPrice`, `sortBy`, `maxItems`
- Poshmark — `department`, `nwtOnly`, `availableOnly`
- Mercari — `categoryId`, `itemStatus`
- Depop — `category`, `discountedOnly`

### `byItem`
Fetch a fixed list of items by URL or ID. The most reliable mode — no listing page parsing.

```jsonc
{
  "platform": "mercari",
  "mode": "byItem",
  "urls": ["https://www.mercari.com/us/item/m86443601198/"],
  "maxItems": 50
}
```

Mercari accepts either `urls` or `itemIds` (e.g. `m86443601198`).

### `bySeller`
Fetch a seller's profile + their listings.

```jsonc
{
  "platform": "poshmark",
  "mode": "bySeller",
  "usernames": ["dr_dolittle"],
  "includeSellerProfile": true,
  "maxItems": 50
}
```

Mercari uses numeric seller IDs — pass them in `sellerIds` instead of `usernames`.

### `byBrand` (Poshmark, Depop)
Listings under a specific brand.

```jsonc
{
  "platform": "poshmark",
  "mode": "byBrand",
  "brands": ["Nike", "Levi's"],
  "maxItems": 50
}
```

### `byCategory` (Mercari, Poshmark)
Listings in a top-level category.

```jsonc
{
  "platform": "poshmark",
  "mode": "byCategory",
  "category": "Women-Shoes",
  "maxItems": 50
}
```

For Mercari, pass `categoryId` (e.g. `1` for Women, `2` for Men).

### `byUrl` (auto-detect)
Drop in any URL — listing page, closet/profile, brand page, category page — and the actor figures out what to fetch.

```jsonc
{
  "platform": "depop",
  "mode": "byUrl",
  "urls": ["https://www.depop.com/products/awesome-vintage-jacket-12345/"],
  "maxItems": 50
}
```

## Anti-bot strategy

| Platform | Default tier | Auto-escalate |
|---|---|---|
| **Depop**     | Apify residential proxy (Depop's Cloudflare hard-blocks datacenter IPs on the public web API) | No further escalation needed |
| **Poshmark**  | curl_cffi Chrome-131 (no proxy)                                                              | On 403/429: datacenter → residential |
| **Mercari**   | curl_cffi for `byItem` / `byUrl`-of-item; **headless Chromium** routed through Apify residential for `searchListings` / `byCategory` / `bySeller` listings | Yes |

You can disable auto-escalation by setting `autoEscalateOnBlock: false` (the run will fail fast on first block). Pass custom proxy groups via `proxyGroups`.

## FAQ

**Why does Mercari `searchListings` use a browser?**
Mercari's search results are 100% client-rendered. The XHR is a Bearer-JWT-signed Apollo persisted query, and the JWT issuer (`/v1/initialize`) is gated by Cloudflare — so we drive a real Chromium that Mercari's React app can sign requests through. Item-detail pages are server-rendered, so `byItem` is HTTP-only and fast.

**Why is Depop on residential proxy by default?**
Depop's `webapi.depop.com` returns HTTP 403 to every datacenter IP we've tested (curl_cffi chrome131/120/116/safari17, all the same). Apify's residential proxy bypasses this reliably.

**Daily test runs?**
The actor's prefill is set to `platform=depop`, `mode=searchListings`, `query="vintage levis"`, `maxItems=10` — Depop reliably returns ≥10 records on residential proxy.

**Do I need to provide cookies?**
No. None of the three platforms require login for the modes shipped here.

**What's the max items per run?**
1000 (`maxItems` upper bound). Each platform paginates differently — Depop and Poshmark return up to ~48 per page, Mercari ~20 per page.

**What currencies are returned?**
Mercari is always USD. Poshmark is USD by default. Depop returns the seller's local currency (USD/GBP/EUR/AUD/etc.) via the `currency` field.

**Image URLs — are they accessible?**
Yes. CDN images from `mercdn.net` (Mercari), `di2ponv0v5otw.cloudfront.net` (Poshmark), and Depop's CDN are all hotlinkable. No KV-rehosting required.

## Tips

- **Search-listing mode is paginated**. Mercari's browser-driven path scrolls to load more items; Depop paginates via `offset_id`; Poshmark returns 48 in `__INITIAL_STATE__`.
- **`byItem` is the fastest and most stable mode** — use it whenever you already have a list of item URLs/IDs.
- **`byUrl` is the most ergonomic** — drop in 10 mixed URLs (some listings, some closets, some brand pages) and the actor dispatches each correctly.
- **Boundary checks**: minPrice/maxPrice filters apply to `price` after parsing; if `currency` differs across listings (Depop with global sellers), the comparison is done in the listing's native units.

## Limitations

- **Mercari API is gated** — the official internal `/v1/api` requires a Bearer JWT issued from `/v1/initialize`, which we can only obtain by driving a real browser. We've documented the headers if you want to extend this actor with a captured-token mode in the future.
- **Poshmark seller profile bio + recent reviews** require additional XHR calls we don't currently make — only the basic profile fields are emitted.
- **Depop product pages from datacenter IP** are 403 — even with the SSR HTML fallback, you'll need residential proxy. The actor handles this for you.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/mercari-poshmark-depop-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
