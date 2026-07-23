# BizBuySell Scraper Tutorial: Run This Apify Actor with Python

Scrape business-for-sale listings from BizBuySell.com. Extract asking price, cash flow, gross revenue, location, and description from search results and category pages.

This repository shows how to run [BizBuySell Scraper](https://apify.com/crawlerbros/bizbuysell-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bizbuysell-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bizbuysell-scraper](https://apify.com/crawlerbros/bizbuysell-scraper)
- **SEO title:** BizBuySell Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape business-for-sale listings from BizBuySell.com. Extract asking price, cash flow, gross revenue, location, and description from search results and category pages.

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

# BizBuySell Scraper

Scrape business-for-sale listings from BizBuySell.com, the largest online marketplace for buying and selling small businesses. Extract asking prices, cash flow, gross revenue, locations, and descriptions — by US state, established-business filter, or the full marketplace.

## What can this scraper do?

- **Search results** — Enter a US state URL (e.g. `/california-businesses-for-sale/`) or the base marketplace URL and extract every listing
- **Asking price** — Listed price as both formatted (`$1,150,000`) and numeric (`1150000`) for sorting/filtering
- **Location data** — City and state extracted into a single `location` field
- **Business descriptions** — Full listing description, not truncated to card preview
- **Optional financial enrichment** — Set `enrichDetails: true` to also pull Cash Flow (SDE), Gross Revenue, EBITDA, Real Estate, Inventory, FF&E, Rent, Established year, and Employees
- **Listing image** — Each listing's photo is downloaded and re-hosted in this run's Apify storage so the URL works in any browser without Akamai blocking; original BBS CDN URL is preserved as `imageOriginal`
- **Automatic pagination** — Walks pages 1, 2, 3... until `maxItems` is reached or results run out
- **Fast & free of proxy** — No browser, no proxy required. Each page is one HTTP request, ~2 seconds per page

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `searchUrl` | string | Yes | `https://www.bizbuysell.com/businesses-for-sale/` | BizBuySell URL to scrape. Use state-level paths (e.g. `/california-businesses-for-sale/`) or the base `/businesses-for-sale/` URL. Auto-rewritten to the mobile subdomain. Query string filters (`?q=`, `?pmin=`, `?pmax=`) are not supported. |
| `maxItems` | integer | No | 50 | Maximum number of listings to extract (1–1,000) |
| `enrichDetails` | boolean | No | false | If true, fetches each listing's detail page to add Cash Flow, Gross Revenue, EBITDA, Real Estate, Established, Employees, FF&E, Rent. One extra HTTP request per listing. |
| `proxy` | object | No | – | Optional. The actor uses the unprotected mobile subdomain (`m.bizbuysell.com`) and works without proxy from Apify datacenter IPs. |

### Supported URL formats

The actor uses BizBuySell's mobile subdomain (`m.bizbuysell.com`), which supports path-based filters but ignores query string parameters. Use state or category path URLs — query parameters like `?q=`, `?pmin=`, `?pmax=` are not applied by the mobile subdomain.

| URL Pattern | Example | Works? |
|-------------|---------|--------|
| All businesses for sale | `https://www.bizbuysell.com/businesses-for-sale/` | ✅ |
| State filter | `https://www.bizbuysell.com/california-businesses-for-sale/` | ✅ |
| Established businesses | `https://www.bizbuysell.com/established-businesses-for-sale/` | ✅ |
| Keyword search (`?q=`) | `https://www.bizbuysell.com/businesses-for-sale/?q=laundromat` | ❌ |
| Price range (`?pmin/pmax`) | `https://www.bizbuysell.com/businesses-for-sale/?pmin=100000&pmax=500000` | ❌ |
| City sub-path | `https://www.bizbuysell.com/businesses-for-sale/los-angeles-ca/` | ❌ |
| Restaurant category | `https://www.bizbuysell.com/restaurant-businesses-for-sale/` | ❌ |
| Franchise category | `https://www.bizbuysell.com/franchise-businesses-for-sale/` | ❌ |

> **Note:** The mobile subdomain honors path-based filters (state slugs like `/california-businesses-for-sale/`, `/established-businesses-for-sale/`) but ignores query string parameters (`?q=`, `?pmin=`, `?pmax=`). City sub-paths and some category paths also return no data on the mobile subdomain.

### Example input

```json
{
    "searchUrl": "https://www.bizbuysell.com/businesses-for-sale/",
    "maxItems": 100
}
```

```json
{
    "searchUrl": "https://www.bizbuysell.com/california-businesses-for-sale/",
    "maxItems": 50,
    "enrichDetails": true
}
```

### How does it bypass Akamai?

BizBuySell's main `www.` site is fronted by Akamai Bot Manager, which blocks datacenter IPs. The actor side-steps this entirely by hitting `m.bizbuysell.com` (the unprotected mobile subdomain) with `curl_cffi`'s real-Chrome TLS fingerprint impersonation. **No browser, no proxy, no retries needed** — every run completes in a few seconds.

User-supplied `www.bizbuysell.com` URLs are auto-rewritten to `m.bizbuysell.com`. Note that the mobile subdomain honors path-based filters (state slugs) but ignores query string parameters — see the supported URL formats table above.

### Why are images re-hosted?

BizBuySell's image CDN (`images.bizbuysell.com`) is also Akamai-fronted and intermittently 403s direct browser opens from flagged IPs. The actor downloads each image during the run using its Chrome TLS fingerprint, stores it in this run's Apify key-value store, and emits a signed public URL as `image` (format: `https://api.apify.com/v2/key-value-stores/{id}/records/{key}?signature=...`). The signature makes the URL accessible to anyone without authentication. The original BBS CDN URL is kept under `imageOriginal` for traceability.

### What does `enrichDetails` add?

By default each listing record contains: title, description, url, productId, image, location, askingPrice (numeric + formatted). Set `enrichDetails: true` to also fetch each listing's detail page and pull labeled financial fields:

- `cashFlow` — Seller's Discretionary Earnings (SDE)
- `grossRevenue` — annual gross revenue
- `ebitda` — earnings before interest/taxes/depreciation/amortization
- `realEstate` — included real estate value (or "Owned" / "Leased")
- `inventory`, `ffe`, `rentMonthly` — inventory value, FF&E, monthly rent
- `established` — year the business was founded
- `employees` — headcount

## Output

Empty fields are omitted (no nulls / blank strings reach the dataset).

### Always-present fields

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Direct link to the listing on `www.bizbuysell.com` |
| `productId` | string | BizBuySell's numeric listing ID |
| `title` | string | Business listing title |
| `description` | string | Listing summary (full text, not truncated) |
| `searchUrl` | string | The search URL this listing was found on (mobile-rewritten) |
| `scrapedAt` | string | ISO 8601 UTC timestamp |

### Usually-present fields

| Field | Type | Description |
|-------|------|-------------|
| `location` | string | City, State (e.g. `Bonita Springs, FL`) |
| `image` | string | Apify-hosted URL of the listing's primary photo (mirrored for browser-friendly access) |
| `imageOriginal` | string | Original BizBuySell CDN URL (Akamai-fronted; may 403 from flagged IPs in browsers) |
| `askingPrice` | string | Formatted price (e.g. `$1,150,000`) — or `"Not Disclosed"` when the seller has hidden it |
| `askingPriceNumeric` | integer | Numeric price for filtering/sorting — omitted for "Not Disclosed" listings |

### `enrichDetails: true` — additional fields per listing

| Field | Type | Description |
|-------|------|-------------|
| `askingPriceDetail` | string | Asking price as shown on the detail page (may include qualifiers) |
| `cashFlow` | string | Seller's Discretionary Earnings (SDE) |
| `grossRevenue` | string | Annual gross revenue |
| `ebitda` | string | EBITDA |
| `realEstate` | string | Real estate value or status (`Owned`, `Leased`, `$X*`) |
| `inventory` | string | Inventory value (often "Included" or `$X`) |
| `ffe` | string | Furniture, fixtures & equipment |
| `rentMonthly` | string | Monthly rent |
| `established` | string | Year founded (or "Not Disclosed") |
| `employees` | string | Number of employees |
| `category` | string | BizBuySell business category (when populated by source) |

### Sample output (without enrichDetails)

```json
{
    "url": "https://www.bizbuysell.com/business-opportunity/outpatient-physical-therapy-practice-for-sale/2501583/",
    "productId": "2501583",
    "title": "Outpatient Physical Therapy Practice For Sale",
    "description": "A 32-year operating history, approximately $1.56M in FY 2025 revenue, and an embedded referral network that has reached 700+ physicians — this owner-operated outpatient physical therapy practice in Southwest Florida is a thriving, fully operational business...",
    "image": "https://api.apify.com/v2/key-value-stores/e3sxDlkCKsIIMTxzg/records/image-2501583.webp?signature=AbCdEfGhIjKlMnOp",
    "imageOriginal": "https://images.bizbuysell.com/shared/listings/250/2501583/895434dc-989d-4045-86b2-5f0e3396481e-W336.webp",
    "location": "Bonita Springs, FL",
    "askingPrice": "$1,150,000",
    "askingPriceNumeric": 1150000,
    "searchUrl": "https://m.bizbuysell.com/established-businesses-for-sale/",
    "scrapedAt": "2026-05-02T08:25:18.567890+00:00"
}
```

### Sample output (with `enrichDetails: true`)

Adds the financial fields by fetching each listing's detail page (one extra HTTP request per listing):

```json
{
    "url": "https://www.bizbuysell.com/business-opportunity/outpatient-physical-therapy-practice-for-sale/2501583/",
    "productId": "2501583",
    "title": "Outpatient Physical Therapy Practice For Sale",
    "location": "Bonita Springs, FL",
    "askingPrice": "$1,150,000",
    "askingPriceNumeric": 1150000,
    "askingPriceDetail": "$1,150,000",
    "cashFlow": "$319,844",
    "grossRevenue": "$1,562,370",
    "ebitda": "$233,264",
    "realEstate": "$2,095,000*",
    "established": "Not Disclosed",
    "image": "https://api.apify.com/v2/key-value-stores/e3sxDlkCKsIIMTxzg/records/image-2501583.webp?signature=AbCdEfGhIjKlMnOp",
    "imageOriginal": "https://images.bizbuysell.com/shared/listings/250/2501583/895434dc-989d-4045-86b2-5f0e3396481e-W336.webp",
    "description": "A 32-year operating history...",
    "searchUrl": "https://m.bizbuysell.com/established-businesses-for-sale/",
    "scrapedAt": "2026-05-02T08:25:18.567890+00:00"
}
```

## Tips for best results

- Start with a small `maxItems` (5–10) to verify your URL works before running large jobs
- Each search page yields ~55–58 listings, so `maxItems: 100` typically completes in 2 page fetches
- Use state-level paths (`/california-businesses-for-sale/`, `/texas-businesses-for-sale/`) to target a specific state — these are the most reliable filters
- Set `enrichDetails: true` if you need financial figures (Cash Flow, Revenue, EBITDA) — adds one HTTP request per listing
- Listings with "Not Disclosed" asking price are included in the output; they have `askingPrice: "Not Disclosed"` and no `askingPriceNumeric` field
- Empty fields are omitted from output records; downstream consumers always see a stable schema

## Limitations

- Only US-based businesses are listed on BizBuySell — the scraper does not cover international marketplaces
- **Query string filters not supported** — the mobile subdomain ignores `?q=` (keyword), `?pmin=`/`?pmax=` (price range), and similar parameters; use state-based path URLs instead
- City sub-paths (`/businesses-for-sale/los-angeles-ca/`) do not return data on the mobile subdomain
- Category paths (restaurants, franchises) return 404 on the mobile subdomain
- "Not Disclosed" prices yield no `askingPriceNumeric`; sort/filter logic should treat those records separately
- Some sponsored / featured listings may not have a `productId` and are filtered out
- Detail-page financial fields are only present when the seller has filled them in
- BizBuySell may rate-limit aggressive scraping; the actor inserts a 0.5s pause between requests to stay polite

## Frequently Asked Questions

**Do I need a BizBuySell account to use this scraper?**
No. All listing data is publicly accessible.

**How many listings can I scrape?**
Up to 1,000 per run via `maxItems`. BizBuySell pages have ~55–58 listings each, so a 1,000-item run walks ~18–19 pages.

**Why is the asking price "Not Disclosed" for some listings?**
Some sellers choose to hide their asking price. These listings are fully included in the output with `askingPrice: "Not Disclosed"` — they tend to be high-value deals where brokers intentionally omit the price. The `askingPriceNumeric` field is omitted for these records.

**Can I filter by business type, location, or price range?**
Filtering by **US state** is supported — use state-level path URLs like `https://www.bizbuysell.com/california-businesses-for-sale/` or `https://www.bizbuysell.com/texas-businesses-for-sale/`. Keyword search (`?q=`), price range (`?pmin=`/`?pmax=`), and city sub-paths are not honored by the mobile subdomain the actor uses and will return unfiltered results.

**Do I need a proxy?**
No. The actor uses BizBuySell's mobile subdomain (`m.bizbuysell.com`), which is not Akamai-protected. Runs work from any Apify datacenter IP without proxy.

**Why is the scraper so fast?**
HTTP-only — no browser launch, no anti-bot challenge wait. Each page is one request that returns a structured `SearchResultsPage` JSON-LD payload with all listing data ready to extract. Typical run: 2–10 seconds.

**What if I need cash flow / revenue but `enrichDetails` is too slow?**
At ~0.5s per listing, enrichment for 50 listings takes ~30s — well within reasonable run times. If you need bulk enrichment for thousands of listings, run multiple smaller jobs in parallel with different `searchUrl` filters.

**What happens if no listings are found?**
The actor emits a single diagnostic record (with `_status: no_data`) and sets a clear status message explaining the likely cause. This usually means the URL path is not supported on the mobile subdomain. Use a state-based URL like `https://www.bizbuysell.com/california-businesses-for-sale/` or the base `https://www.bizbuysell.com/businesses-for-sale/`.

**Why do keyword search and price filter URLs not work?**
The actor routes all requests through BizBuySell's mobile subdomain (`m.bizbuysell.com`), which processes path-based filters (state slugs) but ignores query string parameters like `?q=`, `?pmin=`, and `?pmax=`. Use state or category path URLs for targeted scraping.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bizbuysell-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
