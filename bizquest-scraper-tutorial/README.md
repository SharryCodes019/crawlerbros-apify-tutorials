# BizQuest Scraper Tutorial: Run This Apify Actor with Python

Scrape business-for-sale listings from BizQuest.com. Supports URL-based input and filter-based input (keyword, location). Optional per-listing detail enrichment.

This repository shows how to run [BizQuest Scraper](https://apify.com/crawlerbros/bizquest-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bizquest-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bizquest-scraper](https://apify.com/crawlerbros/bizquest-scraper)
- **SEO title:** BizQuest Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape business-for-sale listings from BizQuest.com. Supports URL-based input and filter-based input (keyword, location). Optional per-listing detail enrichment.

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

## BizQuest Scraper

Scrape business-for-sale listings from [BizQuest](https://www.bizquest.com) — no account or subscription required. Supports filters for keyword and US state, plus direct URL pasting for any custom filter combination. Access 50+ listings per run, with optional enrichment of each listing's detail page.

### What This Scraper Does

This actor fetches BizQuest listing pages and extracts publicly visible data: listing title, asking price, cash flow, gross revenue, city, state, industry, listing ID, images, and more. With **Fetch Listing Details** enabled, it retrieves additional fields from each listing's detail page (full description, financial breakdowns, broker info, photo gallery).

### Input

Two input modes — use either or both:

#### Mode 1: Paste BizQuest URLs (Start URLs)

Apply filters on BizQuest.com (state, city, industry, price range, etc.), then copy the URL from your browser and paste it as a Start URL.

**Examples:**

- All California businesses: `https://www.bizquest.com/businesses-for-sale-in-california-ca/`
- Miami businesses: `https://www.bizquest.com/businesses-for-sale-in-miami-fl/`
- Restaurants nationwide: `https://www.bizquest.com/restaurants-for-sale/`
- California restaurants: `https://www.bizquest.com/restaurants-for-sale-in-california-ca/`
- A single listing: `https://www.bizquest.com/business-for-sale/thriving-turnkey-daycare-center/BW2417284/`

#### Mode 2: Use Filter Fields

Provide any combination of:

- **Keyword** — `"pizza"`, `"franchise"`, `"daycare"`
- **Location** — US state full name (`"California"`) or 2-letter abbreviation (`"CA"`)

For city/county/industry/price filters, use Mode 1.

#### Input Fields

| Field | Type | Description |
|---|---|---|
| **Start URLs** | List of strings | BizQuest search or listing URLs. Default: `["https://www.bizquest.com/businesses-for-sale/"]`. |
| **Keyword** | String (optional) | Keyword search term. |
| **Location** | String (optional) | US state name or 2-letter abbreviation. |
| **Fetch Listing Details** | Boolean | If `true`, fetches each listing's detail page for richer output. Doubles HTTP requests. Default: `false`. |
| **Max Items** | Integer | Maximum listings to return (1–10,000). Default: 50. |
| **Proxy Configuration** | Proxy object | Apify proxy. **Residential proxy required for reliable detail-page fetching** — BizQuest uses Akamai bot protection that blocks datacenter IPs. |

### Output

Each record represents one business listing. Fields marked `?` are optional and appear only when BizQuest publishes the data.

#### Core Fields (always when available)

| Field | Type | Description |
|---|---|---|
| `url` | string | Canonical detail URL |
| `listingId` | string | BizQuest ID (e.g. `"BW2398228"`) |
| `title` | string | Listing title |
| `priceLabel` | string? | Formatted price as shown (e.g. `"$485,000"` or `"Contact for Price"`) |
| `askingPrice` | integer? | Price in USD (omitted for "Undisclosed") |
| `cashFlowLabel` | string? | Formatted cash flow / EBITDA label |
| `cashFlow` | integer? | Cash flow in USD (omitted when "Sign In to View" or undisclosed) |
| `location` | string? | Full location label (e.g. `"Miami, FL"`) |
| `city` | string? | City |
| `state` | string? | 2-letter US state abbreviation |
| `shortDescription` | string? | Teaser text from listing card |
| `thumbnail` | string? | Primary image URL |
| `scrapedAt` | string | ISO 8601 UTC timestamp |

#### Additional Fields (when **Fetch Listing Details** is enabled)

| Field | Type | Description |
|---|---|---|
| `description` | string? | Full listing description |
| `reasonForSelling` | string? | |
| `grossRevenue` | integer? | USD |
| `ebitda` | integer? | USD |
| `inventoryValue` | integer? | USD |
| `ffeValue` | integer? | Furniture, fixtures & equipment |
| `realEstateValue` | integer? | USD |
| `monthlyRent` | integer? | USD |
| `yearEstablished` | integer? | |
| `employees` | string? | |
| `sellerFinancing` | boolean? | |
| `buildingSqft` | integer? | |
| `lotSize` | string? | |
| `franchiseBrand` | string? | |
| `trainingOffered` | string? | |
| `support` | string? | |
| `brokerName` | string? | |
| `brokerCompany` | string? | |
| `brokerPhone` | string? | Only when publicly visible |
| `photos` | string\[]? | Array of image URLs |
| `listingType` | string? | `"business"` or `"franchise"` |

Fields are included only when BizQuest returns data — no nulls in the output.

#### Error Records

If a URL can't be fetched/parsed, the record contains:

| Field | Description |
|---|---|
| `inputUrl` | The attempted URL |
| `error` | Human-readable error message |
| `scrapedAt` | Timestamp |

### Frequently Asked Questions

**Do I need a BizQuest account?**
No. The scraper only uses publicly visible listing data.

**Is a proxy required?**
Strongly recommended. BizQuest uses Akamai bot protection that blocks Apify datacenter IPs more aggressively than residential IPs. The actor defaults to Apify Residential proxy — no extra configuration needed. Local testing may work without proxy depending on your IP, but detail-page fetches are especially prone to blocks.

**Why are some prices "Undisclosed" or "Sign In to View"?**
Sellers often choose not to publish asking price, cash flow, or EBITDA publicly — or BizQuest requires an account to see them. The scraper preserves BizQuest's label in `priceLabel` / `cashFlowLabel` and omits the numeric field when the value isn't a real number.

**How many listings can I get?**
BizQuest shows ~50 listings per search page. The scraper paginates automatically via BizQuest's `/page-N/` URLs. Typical state-level searches return 100–2,000+ listings. Use `maxItems` to cap.

**What's the difference between Start URLs and Filters?**

- **Start URLs** — paste any BizQuest URL (search or detail). Supports every filter combination BizQuest offers.
- **Filters** — convenience fields for keyword + US state. Builds the search URL internally.
- Both can be combined in one run.

**Can I filter by city or industry?**
Yes, but via Start URLs. On BizQuest.com, navigate to your desired city/industry/combination, copy the URL, paste it as a Start URL. E.g. `https://www.bizquest.com/restaurants-for-sale-in-california-ca/`.

**Can I filter by price or cash flow range?**
Apply the filters on BizQuest.com's search UI, then paste the resulting URL into Start URLs.

**How fresh is the data?**
Near real-time. BizQuest publishes listings as sellers submit them.

**Difference vs. BizBuySell actor?**
Different source websites with partially overlapping listing pools. Some brokers post to both; many list on only one. Run both scrapers if you need comprehensive coverage.

**Why is broker phone sometimes missing?**
BizQuest brokers often hide their phone behind a "Contact Broker" form. The scraper only extracts publicly visible contact info.

**Can I run this on a schedule?**
Yes. Set up an Apify Schedule (daily/hourly) and dedupe downstream by `listingId`.

# Actor input Schema

## `startUrls` (type: `array`):

BizQuest search result URLs (e.g. https://www.bizquest.com/businesses-for-sale-in-california-ca/) or individual listing URLs. Apply filters on BizQuest.com first, then paste the URL here.

## `keyword` (type: `string`):

Optional keyword filter (e.g. 'pizza'). NOTE: BizQuest's own search often ignores the ?q= parameter on the default browse URL — results may be the same regardless. For reliable keyword search, use a BizQuest industry URL in Start URLs (e.g. '/restaurants-for-sale/') which filters by category.

## `location` (type: `string`):

Optional US state filter — full name ('California') or 2-letter abbreviation ('CA'). For city/county filters, paste the URL from BizQuest directly into Start URLs.

## `fetchDetails` (type: `boolean`):

EXPERIMENTAL — attempts to fetch each listing's detail page for additional fields (description, broker info, photos, financials). BizQuest's Akamai bot protection currently blocks most detail-page fetches even from residential proxies; when a fetch fails the record is emitted with card-level data only. Doubles HTTP request count. Default: false.

## `maxItems` (type: `integer`):

Maximum number of listings to return (1–10,000).

## `proxyConfiguration` (type: `object`):

Proxy configuration. BizQuest uses Akamai bot protection. Residential proxy is strongly recommended — detail pages often fail from datacenter IPs.

## Actor input object example

```json
{
  "startUrls": [
    "https://www.bizquest.com/businesses-for-sale/"
  ],
  "fetchDetails": false,
  "maxItems": 50,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ]
  }
}
```

# API

You can run this Actor programmatically using our API. Below are code examples in JavaScript, Python, and CLI, as well as the OpenAPI specification and MCP server setup.

## JavaScript example

```javascript
import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with your Apify API token
// Replace the '<YOUR_API_TOKEN>' with your token
const client = new ApifyClient({
    token: '<YOUR_API_TOKEN>',
});

// Prepare Actor input
const input = {
    "startUrls": [
        "https://www.bizquest.com/businesses-for-sale/"
    ],
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ]
    }
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/bizquest-scraper").call(input);

// Fetch and print Actor results from the run's dataset (if any)
console.log('Results from dataset');
console.log(`💾 Check your data here: https://console.apify.com/storage/datasets/${run.defaultDatasetId}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.forEach((item) => {
    console.dir(item);
});

// 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/js/docs

```

## Python example

```python
from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
# Replace '<YOUR_API_TOKEN>' with your token.
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the Actor input
run_input = {
    "startUrls": ["https://www.bizquest.com/businesses-for-sale/"],
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
    },
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/bizquest-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print(f"💾 Check your data here: https://console.apify.com/storage/datasets/{run.default_dataset_id}")
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "startUrls": [
    "https://www.bizquest.com/businesses-for-sale/"
  ],
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ]
  }
}' |
apify call crawlerbros/bizquest-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "type": "http",
            "url": "https://mcp.apify.com/?tools=fetch-actor-details,crawlerbros/bizquest-scraper"
        }
    }
}

```

The hosted server signs you in with OAuth on first connect, so no API token belongs in this config. Clients without OAuth support can send an `Authorization: Bearer <APIFY_API_TOKEN>` header instead, using a token from API & Integrations in Apify Console (https://console.apify.com/settings/integrations).

## OpenAPI specification

Download the OpenAPI definition: https://api.apify.com/v2/actors/htktd1gg2uQScXbo9/builds/hSDdnVwb2aoWgU2Va/openapi.json

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bizquest-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
