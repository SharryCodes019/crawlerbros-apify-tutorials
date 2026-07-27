# Apartments.com Rental Scraper Tutorial: Run This Apify Actor with Python

Extract apartment rental listings from Apartments.com including property name, address, rent range, beds/baths, sqft, amenities, neighborhood, walk/transit scores, and more.

This repository shows how to run [Apartments.com Rental Scraper](https://apify.com/crawlerbros/apartments-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/apartments-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/apartments-scraper](https://apify.com/crawlerbros/apartments-scraper)
- **SEO title:** Apartments.com Rental Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract apartment rental listings from Apartments.com including property name, address, rent range, beds/baths, sqft, amenities, neighborhood, walk/transit scores, and more.

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

# Apartments.com Rental Scraper

Extract apartment rental listings from **Apartments.com** — property name, address, rent range, beds/baths, sqft, amenities, location, photos, and more. Uses Camoufox (anti-detect Firefox) with US residential proxy to bypass Akamai bot protection.

## Features

- **22 output fields** per property
- **Supports city listings** (e.g., `/miami-fl/`) and direct property URLs
- **Latitude/longitude** — geographic coordinates
- **Rent range** — min/max parsed from text
- **Beds, baths, sqft** — apartment size info
- **Amenities** — full amenity list
- **Photo URLs** — property images
- **US RESIDENTIAL proxy hardcoded** — Apartments.com is Akamai-protected
- **No nulls** — every field has a typed default

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | Array | Apartments.com URLs (city listing or property detail) |
| `maxItems` | Integer | Max properties to scrape (default 20) |

### Example Input

```json
{
    "startUrls": [
        "https://www.apartments.com/miami-fl/",
        "https://www.apartments.com/los-angeles-ca/"
    ],
    "maxItems": 50
}
```

## Output

Each property has **22 fields**:

| Field | Type | Description |
|---|---|---|
| `id` | String | Apartments.com property ID |
| `propertyName` | String | Property name |
| `url` | String | Property URL |
| `fullAddress` | String | Complete address |
| `streetAddress` | String | Street address |
| `city` | String | City |
| `state` | String | State code |
| `neighborhood` | String | Neighborhood |
| `postalCode` | String | ZIP code |
| `latitude` | Number | Latitude |
| `longitude` | Number | Longitude |
| `rentMin` | Integer | Minimum monthly rent |
| `rentMax` | Integer | Maximum monthly rent |
| `beds` | String | Beds range (e.g., "Studio - 2 bd") |
| `baths` | String | Baths range |
| `sqft` | String | Square footage range |
| `isVerified` | Boolean | Verified listing flag |
| `rating` | Number | Aggregate rating (0-5) |
| `phoneNumber` | String | Leasing office phone |
| `amenities` | Array | Amenity list |
| `photoUrls` | Array | Property image URLs |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

## FAQ

**Q: Why does this need US RESIDENTIAL proxy?**
Apartments.com is protected by Akamai Bot Manager which blocks all datacenter IPs and non-browser clients. Camoufox (anti-detect Firefox) combined with residential proxy is required. Both are hardcoded — no configuration needed.

**Q: How fresh is the data?**
Real-time — the scraper fetches pages live from Apartments.com on each run.

**Q: Can I filter by price or beds?**
Yes — use Apartments.com URL filters like `/miami-fl/2-bedrooms-under-2000/` as your start URL.

## Use Cases

- **Rental market research** — track rents across cities
- **Competitive analysis** — compare property amenities and pricing
- **Relocation planning** — find apartments matching specific criteria
- **Data aggregation** — build rental databases

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/apartments-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
