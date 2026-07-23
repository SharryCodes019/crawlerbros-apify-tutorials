# Property Finder Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings from Property Finder (UAE, Saudi Arabia, Qatar, Bahrain, Egypt). Extract prices, locations, photos, agent info, and 50+ fields per listing. No proxy required.

This repository shows how to run [Property Finder Scraper](https://apify.com/crawlerbros/propertyfinder-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/propertyfinder-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/propertyfinder-scraper](https://apify.com/crawlerbros/propertyfinder-scraper)
- **SEO title:** Property Finder Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings from Property Finder (UAE, Saudi Arabia, Qatar, Bahrain, Egypt). Extract prices, locations, photos, agent info, and 50+ fields per listing. No proxy required.

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

# Property Finder Scraper

Scrape property listings from [Property Finder](https://www.propertyfinder.ae) — the leading real estate portal in UAE, Saudi Arabia, Qatar, Bahrain and Egypt. Extract prices, locations, photos, agent info, amenities, and 50+ fields per listing.

## What This Actor Does

This actor scrapes Property Finder across all supported countries and categories. Provide search URLs directly or use city + purpose filters to find listings across sale, rent, and commercial property segments.

The scraper uses Property Finder's public sitemaps for discovery and extracts structured data directly from server-rendered pages. No proxy required, no browser needed.

## Key Features

- **50+ fields per listing** — price, bedrooms, bathrooms, size, location hierarchy, agent info, broker info, amenities, RERA permit, status flags, and more
- **5 countries** — UAE, Saudi Arabia, Qatar, Bahrain, Egypt
- **All UAE emirates + Saudi cities** — Dubai, Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah, Fujairah, Umm Al Quwain, Al Ain, Riyadh, Jeddah, Dammam and more
- **4 purposes** — For Sale, For Rent, Commercial For Sale, Commercial For Rent
- **Two input modes** — paste URLs or use city + purpose filters
- **Location hierarchy** — city → community → sub-community → tower with IDs and slugs
- **Agent & broker contacts** — name, email, phone, WhatsApp, profile image
- **No null fields** — every output field is populated or set to a safe default
- **Automatic deduplication** — same property won't appear twice even across different landing pages
- **No proxy required** — runs reliably on any Apify plan

## Supported Property Types

Apartments, Villas, Townhouses, Penthouses, Duplexes, Hotel Apartments, Compounds, Floors, Land, Villa Compounds, Offices, Shops, Warehouses, Factories, Labour Camps, Bulk Units.

## Supported Locations

### UAE
Dubai, Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah, Fujairah, Umm Al Quwain, Al Ain

### Saudi Arabia
Riyadh, Jeddah, Dammam, Makkah, Madinah, Khobar

### Also Supported
Qatar (propertyfinder.qa), Bahrain (propertyfinder.bh), Egypt (propertyfinder.eg)

## Input Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startUrls` | array | — | Property Finder URLs to scrape (landing pages, sitemaps, or sitemap index) |
| `country` | enum | `ae` | Country to search in (ae, sa, bh, eg, qa) |
| `city` | enum | `dubai` | City to search in |
| `purpose` | enum | `buy` | buy, rent, commercial-buy, commercial-rent |
| `max_items` | integer | 20 | Maximum unique properties to scrape |
| `max_retries` | integer | 2 | Retry attempts per failed request |
| `ignore_url_failures` | boolean | true | Continue on errors |

## Usage Examples

### Scrape properties from a specific landing page

```json
{
    "startUrls": [
        "https://www.propertyfinder.ae/en/buy/dubai/2-bedroom-apartments-for-sale-dubai-land-ghaf-woods-cilia-at-ghaf-woods-cilia-tower-2.html"
    ],
    "max_items": 20
}
```

### Scrape all Dubai apartments for sale (filter mode)

```json
{
    "city": "dubai",
    "purpose": "buy",
    "max_items": 100
}
```

### Scrape Saudi Arabia listings

```json
{
    "country": "sa",
    "city": "riyadh",
    "purpose": "buy",
    "max_items": 50
}
```

### Scrape rentals in Abu Dhabi

```json
{
    "city": "abu-dhabi",
    "purpose": "rent",
    "max_items": 100
}
```

### Expand from sitemap index (maximum coverage)

```json
{
    "startUrls": [
        "https://www.propertyfinder.ae/sitemaps/index-sitemap.xml"
    ],
    "max_items": 500
}
```

## Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | number | Property Finder numeric ID |
| `listingId` | string | Alphanumeric listing identifier |
| `reference` | string | Agency reference number |
| `rera` | string | RERA permit number |
| `url` | string | Canonical detail URL |
| `title` | string | Listing title |
| `description` | string | Full description |
| `propertyType` | string | Type (Apartment, Villa, etc.) |
| `offeringType` | string | e.g. "Residential for Sale" |
| `categoryId` | number | 1=Sale, 2=Rent, 3=Commercial Sale, 4=Commercial Rent |
| `price` | number | Price value |
| `priceCurrency` | string | AED/SAR/QAR/BHD/EGP |
| `priceDuration` | string | sell/yearly/monthly/weekly/daily |
| `pricePerArea` | number | Price per unit area |
| `pricePerAreaUnit` | string | sqft/sqm |
| `bedrooms` | number | Number of bedrooms |
| `bathrooms` | number | Number of bathrooms |
| `size` | number | Size value |
| `sizeUnit` | string | Size unit (sqft/sqm) |
| `furnished` | string | YES/NO/PARTLY |
| `completionStatus` | string | completed/off_plan |
| `city` | string | City name |
| `community` | string | Community/area |
| `subCommunity` | string | Sub-community |
| `tower` | string | Tower/building name |
| `locationTree` | array | Hierarchical `[{id, name, type, slug, level}]` |
| `latitude` | number | GPS latitude |
| `longitude` | number | GPS longitude |
| `coverImage` | string | Main photo URL |
| `images` | array | All photo URLs |
| `imagesCount` | number | Number of images |
| `amenities` | array | Amenity codes |
| `amenityNames` | array | Human-readable amenity names |
| `agentName` | string | Agent full name |
| `agentEmail` | string | Agent email |
| `agentPhone` | string | Agent phone |
| `agentWhatsapp` | string | Agent WhatsApp |
| `agentImage` | string | Agent profile photo URL |
| `brokerName` | string | Agency/broker name |
| `brokerLogo` | string | Agency logo URL |
| `brokerPhone` | string | Agency phone |
| `brokerEmail` | string | Agency email |
| `isVerified` | boolean | Verified listing |
| `isDirectFromDeveloper` | boolean | Direct from developer |
| `isNewConstruction` | boolean | New construction |
| `isFeatured` | boolean | Featured listing |
| `isPremium` | boolean | Premium placement |
| `isExclusive` | boolean | Exclusive listing |
| `isAvailable` | boolean | Currently available |
| `leadValue` | number | Lead quality score |
| `listingLevel` | string | Listing tier |
| `videoUrl` | string | Video URL |
| `has360View` | boolean | Has 360° view |
| `listedDate` | string | Date listed (ISO 8601) |
| `scrapedAt` | string | Scrape timestamp (ISO 8601) |

## Sample Output

```json
{
    "id": 75010975,
    "listingId": "9WYS2AVTMRJP9HKQHEDEY797BM",
    "rera": "71149781518",
    "title": "Luxury 2BR | Downtown Dubai | Sea View",
    "propertyType": "Apartment",
    "offeringType": "Residential for Sale",
    "categoryId": 1,
    "price": 2600000,
    "priceCurrency": "AED",
    "priceDuration": "sell",
    "pricePerArea": 2126,
    "pricePerAreaUnit": "sqft",
    "bedrooms": 2,
    "bathrooms": 3,
    "size": 1250,
    "sizeUnit": "sqft",
    "furnished": "YES",
    "completionStatus": "completed",
    "city": "Dubai",
    "community": "Downtown Dubai",
    "subCommunity": "Boulevard Walk",
    "tower": "Tower A",
    "latitude": 25.0762,
    "longitude": 55.1358,
    "coverImage": "https://img.pf.ae/cover.jpg",
    "images": ["https://img.pf.ae/1.jpg", "https://img.pf.ae/2.jpg"],
    "imagesCount": 8,
    "amenityNames": ["Central A/C", "Built in Wardrobes", "Shared Pool", "Shared Gym"],
    "agentName": "Jane Agent",
    "agentEmail": "jane@agency.ae",
    "agentPhone": "+971501234567",
    "brokerName": "Best Realty",
    "brokerLogo": "https://img.pf.ae/logo.jpg",
    "isVerified": true,
    "isAvailable": true,
    "listedDate": "2025-03-15T10:30:00+00:00",
    "url": "https://www.propertyfinder.ae/en/plp/buy/apartment-for-sale-dubai-downtown-dubai-75010975.html",
    "scrapedAt": "2026-04-10T12:00:00+00:00"
}
```

## FAQs

### How do I find URLs to paste?

Browse Property Finder normally and copy URLs from the address bar. The scraper supports landing pages, sitemap URLs, and the sitemap index. Or use the city + purpose filters to let the actor discover URLs for you.

### Can I scrape all Dubai listings at once?

Yes — provide the sitemap index URL `https://www.propertyfinder.ae/sitemaps/index-sitemap.xml` and set a high `max_items`. The actor will expand it into all available landing pages.

### Does it support Saudi Arabia?

Yes — use `country=sa` and a Saudi city (Riyadh, Jeddah, Dammam, etc.), or pass a propertyfinder.sa URL.

### Can I filter by bedrooms, price, or area?

Directly — no. The filter mode uses city + purpose only. For fine-grained filtering, browse Property Finder's website with your desired filters applied, then paste the resulting URLs into `startUrls`.

### What if a URL returns no results?

The actor logs a warning and continues with the remaining URLs. Set `ignore_url_failures` to `false` to stop on first failure.

### Does this work on the Apify FREE plan?

Yes. The scraper runs entirely without residential proxies and without browsers, so it fits comfortably within free plan compute limits.

### How do I get verified listings only?

All listings include an `isVerified` boolean — filter the output downstream (e.g., in a Google Sheet or database) to keep only `isVerified=true` entries.

### How fresh is the data?

The actor fetches live data on each run. Schedule daily runs on Apify to track new listings, price changes, and delistings.

## Use Cases

- **Real estate market analysis** — Track price trends and inventory across UAE and Saudi markets
- **Lead generation** — Extract agent and agency contact info for business outreach
- **Price monitoring** — Schedule daily runs to detect price changes in specific areas
- **Investment research** — Compare properties by location, size, amenities, and RERA status
- **Competitive analysis** — Monitor agency listings and market share
- **Data enrichment** — Combine with other sources for comprehensive market intelligence
- **Off-plan tracking** — Identify new construction and direct-from-developer properties

## About Property Finder

[Property Finder](https://www.propertyfinder.ae) is the leading property portal in the United Arab Emirates and the wider Middle East region, listing millions of residential and commercial properties for sale and rent across Dubai, Abu Dhabi, Sharjah, and other major cities. It operates dedicated sites for UAE, Saudi Arabia, Qatar, Bahrain, and Egypt.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/propertyfinder-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
