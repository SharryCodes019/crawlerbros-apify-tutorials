# Vinted Scraper Tutorial: Run This Apify Actor with Python

Unofficial Scraper for Vinted second-hand fashion marketplace listings across 19 countries. Search items by keyword, brand, catalog, price, color, condition, or scrape user closets, item URLs, brand pages, and seller feedbacks.

This repository shows how to run [Vinted Scraper](https://apify.com/crawlerbros/vinted-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/vinted-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/vinted-scraper](https://apify.com/crawlerbros/vinted-scraper)
- **SEO title:** Vinted Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Unofficial Scraper for Vinted second-hand fashion marketplace listings across 19 countries. Search items by keyword, brand, catalog, price, color, condition, or scrape user closets, item URLs, brand pages, and seller feedbacks.

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

# Vinted Scraper

Scrape **Vinted**, the second-hand fashion marketplace, across 19 country
domains (US, UK, FR, DE, IT, ES, PL, CZ, NL, LT, LU, AT, BE, PT, RO, SK, FI,
SE, GR). Search items by keyword, filter by brand / catalog / size /
color / material / condition / price; scrape user closets; brand registries;
and seller feedbacks — all without login.

## What you can scrape

- **Items** — search by keyword + filters across any country domain
- **Per-user closets** — every public item a seller has listed
- **Per-brand items** — all items in a Vinted brand registry
- **Per-catalog items** — all items in a Vinted category (catalog) ID
- **Brand registry** — search Vinted's brand directory by keyword
- **Seller feedbacks** — public reviews left for a user

## Modes

| Mode               | Required input                  | Output                       |
|--------------------|---------------------------------|------------------------------|
| `search`           | `searchText` (or any filter)    | Items                        |
| `byUrl`            | `urls[]`                        | Items / users / brand items  |
| `byUser`           | `userId`                        | User profile + closet items  |
| `byBrand`          | `brandId`                       | Brand items                  |
| `byCatalog`        | `catalogId`                     | Catalog items                |
| `byBrandSearch`    | `brandKeyword`                  | Brand registry results       |
| `byUserFeedbacks`  | `userId`                        | Seller feedbacks             |

## Inputs

- `mode` — one of the modes above
- `country` — Vinted country domain (`com`, `co.uk`, `fr`, `de`, …)
- `searchText` — keyword (search mode)
- `order` — `relevance`, `newest_first`, `price_high_to_low`, `price_low_to_high`
- `urls[]` — direct Vinted URLs (item / member / brand / catalog)
- `userId`, `brandId`, `catalogId`, `brandKeyword` — per-mode IDs / keyword
- `brandIds[]`, `catalogIds[]`, `sizeIds[]`, `colorIds[]`, `materialIds[]`,
  `statusIds[]` — search filters
- `priceFrom`, `priceTo` — price range (in the country's local currency)
- `minRating` — drop sellers with feedback rating below this (0.0 – 5.0)
- `containsKeyword` — substring filter on item title/description
- `maxItems` — hard cap on emitted records (1 – 1000)
- `perPage` — Vinted page size (1 – 96)
- `useProxy`, `autoEscalateOnBlock`, `proxyConfiguration` — proxy controls
- `cookieHeader` — optional logged-in cookie header (only needed if you see
  persistent 401/403; public endpoints work without it)

## Output fields

Per-item record fields include:

- `itemId`, `title`, `description`, `brandTitle`, `brandId`, `catalogId`
- `sizeTitle`, `sizeId`, `statusId`, `status`
- `priceAmount`, `priceCurrency`, `totalPriceAmount`, `serviceFeeAmount`
- `isVisible`, `isClosed`, `isReserved`, `isPromoted`
- `favouriteCount`, `viewCount`, `createdAt`, `updatedAt`
- `itemUrl`, `canonicalUrl`, `imageUrl`, `photos[]`
- `sellerId`, `sellerLogin`, `sellerCountryCode`, `sellerProfileUrl`,
  `sellerAvatarUrl`, `sellerFeedbackCount`, `sellerFeedbackReputation`,
  `sellerIsBusiness`
- `recordType`, `siteName`, `sourceCountry`, `sourceCountryCode`, `scrapedAt`

User records include feedback counts, reputation, country, profile URL,
avatar, item count.

Empty / null fields are stripped before pushing — every emitted field carries
a real value.

## FAQ

**Do I need a Vinted account?** No. All endpoints used here are public.
A `cookieHeader` input is exposed for advanced cases where you've hit
persistent 401/403, but daily defaults work without it.

**Which country should I pick?** `com` is the US domain. Use `fr`, `de`, `it`,
`es`, `co.uk`, etc. for European inventory. Each country has its own
inventory, currency, and slugs. (Vinted does not currently operate a
`com.au` storefront; the actor lists the 19 supported domains in the
`country` input.)

**Does it use Apify proxy?** Off by default — Vinted is generally accessible
from datacenter IPs. If a Cloudflare challenge appears, the actor
auto-escalates to Apify proxy (datacenter then residential) without
intervention.

**How are price filters applied?** `priceFrom`/`priceTo` are passed directly to
Vinted's `/api/v2/catalog/items` endpoint, so the filter is enforced
server-side. Currency is whatever the chosen country uses.

**Can I scrape a single Vinted item URL?** Yes — `byUrl` mode accepts item,
member, brand, or catalog URLs and dispatches accordingly. Item URLs use the
public JSON-LD `Product` block from the HTML page.

**Why do some items show fewer fields?** Vinted's API only returns the rich
field set on items still active. Closed, reserved, or hidden items return a
trimmed payload — and we omit empty fields rather than emit nulls.

## Limitations

- **Member URLs require the numeric ID.** Vinted's canonical member URL is
  `vinted.com/member/<numeric-id>` or `vinted.com/member/<numeric-id>-<slug>`.
  Slug-only URLs like `vinted.com/member/<login>` resolve to a generic page on
  Vinted and cannot be scraped — when given such a URL the actor logs a clear
  warning and skips it. Use the canonical numeric URL (visible on any seller's
  item card via `sellerProfileUrl`) or call `byUser` mode with the numeric
  `userId` directly.
- **No login-walled fields.** Buyer-side data (chat history, your own
  favourites, hidden draft items) requires a logged-in cookie and is not in
  scope of the public API surface.
- **`/api/v2/items/{id}` (logged-in detail endpoint) is gated.** When you scrape
  a single item URL, we use the public HTML page's JSON-LD instead — this
  yields title, description, brand, price, currency, image, category, color,
  condition. Some richer fields (favourite count, view count) are only
  available on items found through `search` / `byBrand` / `byCatalog` modes.
- **Cloudflare challenges** can occasionally appear from a single IP. The
  actor auto-rotates Apify proxy sessions to recover; if challenges persist
  enable `useProxy` with `RESIDENTIAL` group.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/vinted-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
