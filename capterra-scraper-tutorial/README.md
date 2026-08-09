# Capterra Software Scraper Tutorial: Run This Apify Actor with Python

Scrape software product data from Capterra.com, extract product details, ratings, reviews, pricing, features, deployment options, and more from the world's largest software directory.

This repository shows how to run [Capterra Software Scraper](https://apify.com/crawlerbros/capterra-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/capterra-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/capterra-scraper](https://apify.com/crawlerbros/capterra-scraper)
- **SEO title:** Capterra Software Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape software product data from Capterra.com, extract product details, ratings, reviews, pricing, features, deployment options, and more from the world's largest software directory.

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

# Capterra Software Scraper

Extract **comprehensive software product data** from **Capterra.com** — the world's largest software directory. Get 39 fields per product including pricing plans, 100+ features, 3000+ integrations, pros/cons, vendor info, and more.

## How It Works

Capterra is protected by aggressive Cloudflare Turnstile and blocks direct scraping. But **Capterra, GetApp, and SoftwareAdvice are all owned by Gartner Digital Markets (GDM)** and share a **single product catalog**. This scraper takes advantage of that:

1. **Google SERP** — resolves the Capterra product URL to the equivalent GetApp URL
2. **GetApp direct fetch** — GetApp exposes the full GDM catalog via `__NEXT_DATA__` (~500KB of structured JSON per product)
3. **Rich extraction** — parses 39 fields: name, tagline, pricing plans, features, integrations, platforms, support, training, pros/cons, vendor, and more

Result: you get the same rich Capterra data **without touching Capterra** — free, reliable, and faster than fighting anti-bot systems.

## Features

- **39 output fields** per product — the most complete Capterra data available
- **Pricing plans** with starting prices and feature lists
- **101+ features** list + total count
- **3000+ integrations** list + total count
- **Pros/cons** with sentiment topics and summaries
- **Vendor info** — name, location, website, founded year
- **Platforms, support options, training options, typical customers**
- **Screenshots** URLs
- **100% reliable** — no Cloudflare challenges to solve
- **No nulls** — every field has a typed default

## Input

| Field | Type | Description |
|---|---|---|
| `productUrl` | String | Single Capterra product URL |
| `productUrls` | Array | Capterra product URLs (e.g., `https://www.capterra.com/p/135003/Slack/`) |
| `startUrls` | Array | Apify-style URL objects or strings with Capterra product URLs |
| `maxItems` | Integer | Max products to scrape (default 20) |

### Example Input

```json
{
    "productUrl": "https://www.capterra.com/p/135003/Slack/",
    "productUrls": [
        "https://www.capterra.com/p/228385/Notion/"
    ],
    "startUrls": [
        { "url": "https://www.capterra.com/p/155043/Asana/" }
    ],
    "maxItems": 10
}
```

## Output

Each product has **39 fields**:

### Identity
| Field | Type | Description |
|---|---|---|
| `productId` | String | Capterra numeric product ID |
| `slug` | String | Product slug |
| `recordType` | String | `product` for product rows, `status` for no-data rows |
| `name` | String | Product name |
| `url` | String | Capterra product URL |
| `sourceUrl` | String | Canonical source Capterra URL |
| `getAppUrl` | String | Resolved GetApp URL used for extraction |
| `reviewsUrl` | String | Capterra reviews page URL |
| `tagline` | String | Product tagline |
| `description` | String | Short description |
| `overview` | String | Longer product overview |
| `logo` | String | Product logo URL |

### Ratings
| Field | Type | Description |
|---|---|---|
| `rating` | Number | Overall rating (0–5) |
| `reviewCount` | Integer | Total number of reviews |

### Pricing
| Field | Type | Description |
|---|---|---|
| `startingPrice` | String | Starting price with currency & period (e.g., `$8.75 / month`) |
| `pricingModel` | String | Pricing model (e.g., `Per User`, `Flat Rate`) |
| `priceCurrency` | String | Currency code |
| `pricePeriodicity` | String | Billing period |
| `freeTrial` | Boolean | Free trial available |
| `freeVersion` | Boolean | Free version available |
| `pricingPlans` | Array | Pricing plans with name, price, attributes |
| `licensingModel` | String | Licensing model (e.g., `Proprietary`) |

### Categories & Features
| Field | Type | Description |
|---|---|---|
| `categories` | Array | Software categories |
| `primaryCategory` | String | Primary category |
| `features` | Array | Up to 50 feature names |
| `featureCount` | Integer | Total feature count |
| `integrationsCount` | Integer | Total integrations count |
| `integrations` | Array | Up to 20 integration names |
| `platforms` | Array | Supported platforms |
| `supportOptions` | Array | Customer support options |
| `trainingOptions` | Array | Training options |
| `typicalCustomers` | Array | Target customer sizes |

### Pros / Cons / Visuals
| Field | Type | Description |
|---|---|---|
| `pros` | Array | Positive sentiment topics with summary |
| `cons` | Array | Negative sentiment topics with summary |
| `screenshots` | Array | Screenshot image URLs |

### Vendor
| Field | Type | Description |
|---|---|---|
| `vendorName` | String | Vendor company name |
| `vendorCity` | String | Vendor city |
| `vendorState` | String | Vendor state |
| `vendorCountry` | String | Vendor country |
| `vendorWebsite` | String | Vendor website URL |
| `vendorFoundedYear` | Integer | Vendor founding year |

| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Status Rows

If an input is missing, invalid, or cannot be resolved/fetched, the actor writes a dataset row instead of returning an empty dataset:

| Field | Type | Description |
|---|---|---|
| `recordType` | String | `status` |
| `sourceUrl` | String | Input URL when available |
| `_status` | String | `no_data` |
| `_reason` | String | Machine-readable reason |
| `_message` | String | Human-readable explanation |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "productId": "135003",
    "slug": "Slack",
    "recordType": "product",
    "name": "Slack",
    "url": "https://www.capterra.com/p/135003/Slack/",
    "sourceUrl": "https://www.capterra.com/p/135003/Slack/",
    "getAppUrl": "https://www.getapp.com/collaboration-software/a/slack/",
    "reviewsUrl": "https://www.capterra.com/p/135003/reviews",
    "tagline": "A single place for team communication and workflows",
    "description": "Slack is a single workspace that connects users with the people and tools they work with...",
    "logo": "https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/...",
    "rating": 4.66,
    "reviewCount": 24046,
    "startingPrice": "$8.75 / month",
    "pricingModel": "Per User",
    "freeTrial": true,
    "freeVersion": true,
    "pricingPlans": [
        {"name": "Free", "attributes": ["1 workspace", "10 Integrations"]},
        {"name": "Pro", "attributes": ["Unlimited message history", "..."]}
    ],
    "licensingModel": "Proprietary",
    "primaryCategory": "Team Communication",
    "categories": ["Unified Communications", "Content Collaboration", "..."],
    "featureCount": 101,
    "integrationsCount": 3180,
    "platforms": ["Web-based", "iPad", "Mac"],
    "typicalCustomers": ["Small Business", "Mid-size Business", "Large Enterprises"],
    "vendorName": "Slack",
    "vendorCountry": "United States",
    "vendorFoundedYear": 2014,
    "scrapedAt": "2026-04-10T12:00:00+00:00"
}
```

## FAQ

**Q: Why doesn't the scraper fetch Capterra directly?**
Capterra is protected by Cloudflare Turnstile, which blocks all datacenter and most residential IPs. We instead fetch the same product data from GetApp (a sister site in the GDM catalog), which exposes everything via its `__NEXT_DATA__` JSON.

**Q: How accurate is the GetApp data compared to Capterra?**
100% accurate — Capterra, GetApp, and SoftwareAdvice all query the same Gartner Digital Markets (GDM) catalog. The underlying product, rating, review count, and feature data are identical across all three sites.

**Q: Does this scraper collect individual user reviews?**
No — this scraper extracts product metadata + aggregated pros/cons sentiment topics. For individual review text, you'd need a separate scraper.

**Q: How do I find Capterra product URLs?**
Go to [capterra.com](https://www.capterra.com), search for a software product, and copy the URL from the product page. URLs follow the pattern `https://www.capterra.com/p/{id}/{name}/`.

## Use Cases

- **Competitive research** — compare products across pricing, features, integrations
- **Market analysis** — track category trends, pricing models
- **Feature-based product discovery** — filter by platforms, integrations, support
- **Vendor intelligence** — identify software companies by location and size
- **Due diligence** — gather structured data for software selection

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/capterra-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
