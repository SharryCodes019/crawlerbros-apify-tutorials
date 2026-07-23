# StreetEasy Scraper Tutorial: Run This Apify Actor with Python

Scrape NYC real estate listings from StreetEasy including sales and rentals with prices, addresses, amenities, agent info, and more.

This repository shows how to run [StreetEasy Scraper](https://apify.com/crawlerbros/streeteasy-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/streeteasy-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/streeteasy-scraper](https://apify.com/crawlerbros/streeteasy-scraper)
- **SEO title:** StreetEasy Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape NYC real estate listings from StreetEasy including sales and rentals with prices, addresses, amenities, agent info, and more.

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

# StreetEasy Scraper

Comprehensive scraper for StreetEasy NYC real estate listings. Extract prices, addresses, property details, amenities, agent info, and more from any StreetEasy search URL — for both sales and rentals.

## What does it do?

This scraper collects real estate listings from StreetEasy across all five NYC boroughs. Paste any StreetEasy search URL — with whatever filters you have applied — and the scraper will paginate through all matching results and return structured data. Enable detailed mode to visit each individual listing page for richer data such as building amenities, agent details, transit access, and floor plans.

## Features

- Scrape sales and rental listings from any StreetEasy search URL
- Apply any StreetEasy filter (price range, bedrooms, neighborhood, property type, etc.) via URL
- Optional detailed mode extracts rich data from individual listing pages
- Automatic pagination to collect all matching results
- All output fields guaranteed non-null
- Built-in retry logic for reliability

## How to build a search URL

Browse to [streeteasy.com](https://streeteasy.com), set your search filters, and copy the URL from your browser. Paste it into `startUrls`. A few examples:

| Goal | URL |
|------|-----|
| All Manhattan sales | `https://streeteasy.com/for-sale/manhattan` |
| Brooklyn rentals under $3,000/mo | `https://streeteasy.com/for-rent/brooklyn/price:-3000` |
| NYC sales $500K–$1M, 2+ beds | `https://streeteasy.com/for-sale/nyc/price:500000-1000000|beds>=2` |
| East Village no-fee 1+ bed rentals | `https://streeteasy.com/for-rent/east-village|beds>=1|no_fee:1` |

Any filter combination you can build on StreetEasy's website will work here.

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| startUrls | array | Yes | — | StreetEasy search URLs. Build your search on streeteasy.com with any filters, then paste the URL. |
| maxResults | integer | No | 50 | Maximum listings to scrape per search URL (1–500). |
| detailedMode | boolean | No | false | Visit each listing page for rich details. Slower but more comprehensive. |
| proxyConfiguration | object | Ignored | Residential | Ignored — a US RESIDENTIAL proxy is hardcoded inside the scraper because StreetEasy's PerimeterX bot protection blocks Apify datacenter IPs. Left in the schema only for legacy compatibility. |

### Example input

```json
{
    "startUrls": [
        { "url": "https://streeteasy.com/for-sale/manhattan/price:500000-1500000|beds>=2" }
    ],
    "maxResults": 50,
    "detailedMode": true
}
```

## Output

### Search result fields (always present)

| Field | Type | Description |
|-------|------|-------------|
| url | string | Direct link to the listing page |
| price | number | Listed price (sale price or monthly rent) |
| address | string | Full street address including unit |
| neighborhood | string | StreetEasy neighborhood label |
| bedrooms | number | Number of bedrooms |
| bathrooms | number | Number of bathrooms |
| squareFeet | number | Interior square footage |
| propertyType | string | Co-op, Condo, Townhouse, etc. |
| photoUrl | string | Main listing photo URL |
| listingType | string | `sale` or `rental` |
| searchUrl | string | The search URL that produced this result |
| scrapedAt | string | ISO 8601 extraction timestamp |

### Additional fields in detailed mode

| Field | Type | Description |
|-------|------|-------------|
| description | string | Full listing description |
| amenities | array | Building/unit amenities (doorman, gym, laundry, etc.) |
| buildingName | string | Name of the building |
| agentName | string | Listing agent's name |
| agentBrokerage | string | Agent's brokerage firm |
| latitude | number | GPS latitude |
| longitude | number | GPS longitude |
| daysOnStreetEasy | number | Days the listing has been active |
| photos | array | All listing photo URLs |
| nearbyTransit | array | Nearby subway lines and stops |
| maintenanceFee | number | Monthly maintenance or HOA fee |
| taxes | number | Annual property taxes |
| pricePerSqFt | number | Price per square foot |
| status | string | Listing status (e.g., Resale, New Development) |
| yearBuilt | number | Year the building was constructed |

### Example output

```json
{
    "url": "https://streeteasy.com/building/example-building/1a",
    "price": 850000,
    "address": "123 West 72nd Street #1A",
    "neighborhood": "Upper West Side",
    "bedrooms": 2,
    "bathrooms": 1,
    "squareFeet": 950,
    "propertyType": "Co-op",
    "photoUrl": "https://photos.zillowstatic.com/example.webp",
    "listingType": "sale",
    "description": "Charming pre-war two-bedroom in the heart of the Upper West Side...",
    "amenities": ["doorman", "elevator", "laundry", "gym"],
    "buildingName": "The Chatsworth",
    "agentName": "Jane Smith",
    "agentBrokerage": "Compass",
    "latitude": 40.7789,
    "longitude": -73.9784,
    "daysOnStreetEasy": 14,
    "photos": ["https://photos.zillowstatic.com/1.webp", "https://photos.zillowstatic.com/2.webp"],
    "nearbyTransit": ["1, 2, 3 at 72nd St", "B, C at 72nd St"],
    "maintenanceFee": 1200,
    "taxes": 0,
    "pricePerSqFt": 895,
    "status": "Resale",
    "yearBuilt": 1928,
    "searchUrl": "https://streeteasy.com/for-sale/upper-west-side",
    "scrapedAt": "2026-04-12T15:30:00.000Z"
}
```

## Use cases

- **Market analysis** — Track price trends and inventory across neighborhoods over time
- **Investment research** — Identify undervalued properties by comparing price per square foot
- **Lead generation** — Build targeted lists of listings matching specific criteria
- **Competitive analysis** — Monitor how long comparable properties sit on the market
- **Academic research** — Study housing affordability and market dynamics in NYC

## FAQ

**Does this require a StreetEasy account?**
No. All data is extracted from publicly visible listings without any login.

**Why is a residential proxy required?**
StreetEasy uses PerimeterX bot protection that blocks Apify datacenter IPs. The scraper hardcodes a US RESIDENTIAL Apify proxy and applies it automatically — no configuration needed. PerimeterX still occasionally challenges a session, so the scraper retries up to 3 times with exponential backoff (8s, 16s, 24s) before failing the URL.

**Can I scrape listings from all five NYC boroughs?**
Yes. StreetEasy covers Manhattan, Brooklyn, Queens, The Bronx, and Staten Island. Use the appropriate neighborhood or borough in your search URL.

**What is the difference between normal mode and detailed mode?**
Normal mode collects data shown on search result cards — price, address, bedrooms, bathrooms, and a photo. Detailed mode also visits each individual listing page to extract descriptions, amenities, agent info, transit details, floor plans, and more. Detailed mode is slower due to the additional page visits.

**How many results can I get per search URL?**
Up to 500 listings per URL. For larger datasets, split your search into multiple narrower URLs (e.g., by neighborhood or price band) and add them all to `startUrls`.

**How fresh is the data?**
The scraper fetches live data directly from StreetEasy at the time of the run, so results reflect what is currently listed on the platform.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/streeteasy-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
