# Redfin Real Estate Scraper Tutorial: Run This Apify Actor with Python

Extract property listings from Redfin including price, beds, baths, sqft, address, coordinates, photos, listing remarks, and more. Uses Redfin's internal GIS API for reliable structured data.

This repository shows how to run [Redfin Real Estate Scraper](https://apify.com/crawlerbros/redfin-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/redfin-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/redfin-scraper](https://apify.com/crawlerbros/redfin-scraper)
- **SEO title:** Redfin Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract property listings from Redfin including price, beds, baths, sqft, address, coordinates, photos, listing remarks, and more. Uses Redfin's internal GIS API for reliable structured data.

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

# Redfin Real Estate Scraper

Extract property listings from **Redfin.com** — prices, beds, baths, sqft, addresses, coordinates, photos, listing descriptions, and 30+ more fields. Uses Redfin's internal GIS API for 100% reliable structured data.

## Features

- **38 output fields** per property — complete real-estate data
- **Search by city, state or ZIP** — or provide Redfin region URLs directly
- **For sale and for rent** modes (separate dedicated endpoints)
- **Coordinates, MLS ID, days on market** — all included
- **HOA fees, garage spaces, pool type** — detail fields
- **3D/video/virtual tour flags**
- **US RESIDENTIAL proxy hardcoded** — Redfin is geo-restricted
- **No nulls** — every field has a typed default

## Input

| Field | Type | Description |
|---|---|---|
| `search` | String | City, state or ZIP code to search (e.g., `"Los Angeles, CA"`) |
| `searchMode` | String | `SALE` or `RENT` (default `SALE`) |
| `startUrls` | Array | Redfin region URLs (e.g., `https://www.redfin.com/city/11203/CA/Los-Angeles`) |
| `maxItems` | Integer | Max properties to return (default 50, max 500) |

### Example Input

```json
{
    "search": "Los Angeles, CA",
    "searchMode": "SALE",
    "maxItems": 50
}
```

or

```json
{
    "startUrls": [
        "https://www.redfin.com/city/11203/CA/Los-Angeles",
        "https://www.redfin.com/zipcode/90210"
    ],
    "maxItems": 100
}
```

## Output

Each property has **38 fields**:

### Identity
| Field | Type | Description |
|---|---|---|
| `propertyId` | Integer | Redfin property ID |
| `listingId` | Integer | Redfin listing ID |
| `mlsId` | String | MLS listing number |
| `mlsStatus` | String | MLS status |
| `url` | String | Full Redfin URL |

### Address
| Field | Type | Description |
|---|---|---|
| `address` | String | Street address |
| `unitNumber` | String | Unit number |
| `city` | String | City |
| `state` | String | State code |
| `zip` | String | ZIP code |
| `countryCode` | String | Country code |
| `latitude` | Number | Latitude |
| `longitude` | Number | Longitude |
| `location` | String | Neighborhood |

### Pricing & Specs
| Field | Type | Description |
|---|---|---|
| `price` | Integer | List / sale price |
| `pricePerSqFt` | Integer | Price per square foot |
| `beds` | Number | Number of bedrooms |
| `baths` | Number | Total bathrooms |
| `fullBaths` | Integer | Full bathrooms |
| `sqFt` | Integer | Square footage |
| `lotSize` | Integer | Lot size (sq ft) |
| `stories` | Number | Number of stories |
| `yearBuilt` | Integer | Year built |
| `propertyType` | String | Single Family / Condo / etc. |
| `hoaFee` | Integer | HOA fee |
| `garageSpaces` | Integer | Garage spaces |
| `parkingSpaces` | Integer | Parking spaces |
| `poolType` | String | Pool type |

### Listing Info
| Field | Type | Description |
|---|---|---|
| `listingStatus` | String | Active/Pending/Sold |
| `daysOnRedfin` | Integer | Days on market |
| `listingRemarks` | String | Full listing description |
| `numPictures` | Integer | Number of photos |
| `coverPhoto` | String | Primary photo URL |
| `isNewConstruction` | Boolean | New construction |
| `has3DTour` | Boolean | 3D tour available |
| `hasVideoTour` | Boolean | Video tour available |
| `hasVirtualTour` | Boolean | Virtual tour available |

| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "propertyId": 7066577,
    "mlsId": "BB26074621",
    "mlsStatus": "Active",
    "url": "https://www.redfin.com/CA/Los-Angeles/2621-Silver-Ridge-Ave-90039/home/7066577",
    "address": "2621 Silver Ridge Ave",
    "city": "Los Angeles",
    "state": "CA",
    "zip": "90039",
    "latitude": 34.1035752,
    "longitude": -118.25645,
    "price": 999000,
    "pricePerSqFt": 959,
    "beds": 2,
    "baths": 1.0,
    "sqFt": 1042,
    "lotSize": 3622,
    "yearBuilt": 1925,
    "propertyType": "Single Family",
    "daysOnRedfin": 1,
    "location": "671 - Silver Lake",
    "listingRemarks": "Attention investors, developers...",
    "scrapedAt": "2026-04-10T12:00:00+00:00"
}
```

## FAQ

**Q: Why does it need US RESIDENTIAL proxy?**
Redfin's stingray API is geo-restricted to US IPs and rate-limits aggressively by IP address. Apify RESIDENTIAL proxy with US country provides fresh IPs per session. The proxy is hardcoded — no configuration needed.

**Q: How do I find a region ID / URL?**
Go to redfin.com, search for a city or ZIP. The URL will look like `https://www.redfin.com/city/11203/CA/Los-Angeles` — that's a valid start URL. Or just use the `search` field to have the scraper resolve it automatically.

**Q: Are detail page photos included?**
Only the cover photo is included. Full photo galleries require additional detail-page scraping which is rate-limited.

**Q: How fresh is the data?**
Redfin's GIS API returns live MLS data, typically updated within minutes of listing changes.

**Q: Can I scrape sold listings?**
No — sold-listing data on Redfin is rendered client-side via JavaScript that requires a full browser session. The supported modes are `SALE` (for-sale listings) and `RENT` (active rentals), each hitting a dedicated Redfin API endpoint.

## Use Cases

- **Real estate research** — track prices and inventory in specific markets
- **Investment analysis** — find undervalued properties in target ZIP codes
- **Market trends** — aggregate data across cities for analysis
- **Rental market monitoring** — pull for-rent listings for yield analysis
- **Property alerts** — monitor new listings matching criteria

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/redfin-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
