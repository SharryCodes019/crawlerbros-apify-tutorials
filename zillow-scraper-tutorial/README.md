# Zillow Property Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings from Zillow. Get prices, descriptions, photos, agent details, schools, tax history, price history, and 30+ fields per property.

This repository shows how to run [Zillow Property Scraper](https://apify.com/crawlerbros/zillow-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/zillow-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/zillow-scraper](https://apify.com/crawlerbros/zillow-scraper)
- **SEO title:** Zillow Property Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings from Zillow. Get prices, descriptions, photos, agent details, schools, tax history, price history, and 30+ fields per property.

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

# Zillow Property Scraper

Scrape property listings from Zillow.com. Get prices, Zestimates, descriptions, photos, agent details, schools, price and tax history, HOA fees, and 30+ fields per property. Search for sale, rent, or recently sold properties across the United States.

## What is Zillow Property Scraper?

Zillow Property Scraper is an Apify actor that extracts property listing data from Zillow.com. Enter a city and state, choose a search mode (buy, rent, or sold), and receive structured data for every property found. Each listing includes everything from basic details like price and square footage to enriched data such as nearby schools, tax history, price history, and property features.

## Features

- **Search by location** — Find properties in any US city or state (e.g., "Houston, TX", "San Francisco, CA")
- **Three search modes** — For sale (BUY), for rent (RENT), or recently sold (SOLD)
- **Comprehensive property data** — Price, Zestimate, rent Zestimate, beds, baths, sqft, lot size, year built, stories, parking
- **Full descriptions** — Complete property marketing text and listing details
- **Photo URLs** — All listing photos with direct image links
- **Agent and broker info** — Agent name, phone number, and brokerage name
- **Nearby schools** — School name, rating, distance, grades, and type
- **Price history** — Price changes, listing events, and price-per-sqft trends over time
- **Tax history** — Assessment values, tax amounts, and year-over-year changes
- **Property features** — Heating, cooling, flooring, roofing, pool, fireplace, construction materials, and more
- **HOA fees** — Monthly homeowner association fees when applicable
- **Direct URL support** — Paste Zillow property or search page URLs for targeted scraping
- **Automatic deduplication** — No duplicate listings when combining search and direct URLs

## Use Cases

- **Real estate investment analysis** — Compare listing prices, Zestimates, and price history to find undervalued properties
- **Market research** — Track listing prices, sold prices, and days on market across neighborhoods
- **Property comparison** — Build side-by-side comparison sheets for multiple properties in a target area
- **Rental market analysis** — Compare rental prices, rent Zestimates, and availability by location
- **School district research** — Find properties near top-rated schools with rating and distance data
- **Agent and broker research** — Identify active listing agents and brokerages in your target market
- **Tax assessment tracking** — Monitor property tax changes and assessment values over time
- **Price trend monitoring** — Track price reductions, relists, and sold prices for market timing
- **HOA cost analysis** — Factor in monthly HOA fees when comparing investment opportunities
- **Data enrichment** — Augment your existing property database with fresh Zillow listing data

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| Search Location | String | — | City and state to search (e.g., "Houston, TX", "Miami, FL") |
| Search Mode | Select | BUY | BUY (for sale), RENT (for rent), or SOLD (recently sold) |
| Maximum Properties | Integer | 50 | Max property listings to scrape (1-500) |
| Maximum Pages | Integer | 5 | Max search result pages to scrape (1-20). Each page returns approximately 40 properties. |
| Scrape Full Details | Boolean | true | Fetch full detail pages for enriched data (schools, history, features, etc.). Disable for faster runs. |
| Start URLs | URL List | — | Direct Zillow property detail URLs or search page URLs |

**Note:** At least one of **Search Location** or **Start URLs** must be provided.

### Example input — Buy properties

```json
{
    "search": "Houston, TX",
    "mode": "BUY",
    "maxItems": 50,
    "scrapeDetails": true
}
```

### Example input — Rental search

```json
{
    "search": "Miami, FL",
    "mode": "RENT",
    "maxItems": 25
}
```

### Example input — Recently sold

```json
{
    "search": "Denver, CO",
    "mode": "SOLD",
    "maxItems": 30,
    "endPage": 3
}
```

### Example input — Direct property URLs

```json
{
    "startUrls": [
        { "url": "https://www.zillow.com/homedetails/123-Main-St-Houston-TX-77001/12345678_zpid/" }
    ],
    "scrapeDetails": true
}
```

## Output

Each property produces one item in the output dataset. Fields with no available data are automatically excluded from the output.

### Core Property Data

| Field | Type | Description |
|-------|------|-------------|
| url | String | Property detail URL on Zillow.com |
| zpid | String | Zillow property ID |
| status | String | Listing status (e.g., for_sale, for_rent, sold) |
| price | Number | Current listing price |
| zestimate | Number | Zillow's estimated market value |
| rentZestimate | Number | Zillow's estimated monthly rent value |
| beds | Number | Number of bedrooms |
| baths | Number | Number of bathrooms |
| sqft | Number | Living area in square feet |
| lotSize | String | Lot size (e.g., "8,000 sqft") |
| yearBuilt | Number | Year the property was constructed |
| propertyType | String | Property type (e.g., SINGLE_FAMILY, CONDO, TOWNHOUSE) |
| stories | Number | Number of stories |
| parking | String | Parking details (e.g., "2 garage spaces") |
| hoaFee | Number | Monthly HOA fee |
| pricePerSqft | Number | Price per square foot |
| daysOnZillow | Number | Days the property has been listed on Zillow |

### Location

| Field | Type | Description |
|-------|------|-------------|
| address | String | Street address |
| city | String | City name |
| state | String | State code (e.g., "TX") |
| zipCode | String | ZIP code |
| latitude | Number | Latitude coordinate |
| longitude | Number | Longitude coordinate |

### Agent and Broker

| Field | Type | Description |
|-------|------|-------------|
| brokerName | String | Brokerage company name |
| agentName | String | Listing agent name |
| agentPhone | String | Listing agent phone number |

### Rich Data (from detail pages)

| Field | Type | Description |
|-------|------|-------------|
| description | String | Full property description text |
| photos | Array | Photo URLs for the property listing |
| priceHistory | Array | Price change events — date, event type, price, price per sqft, source |
| taxHistory | Array | Tax records — year, tax paid, assessed value, change rate |
| schools | Array | Nearby schools — name, level, grades, distance, rating, type |
| features | Object | Property features — heating, cooling, flooring, roofing, pool, fireplace, construction, and more |
| scrapedAt | String | ISO timestamp when data was collected |

### Sample output

```json
{
    "url": "https://www.zillow.com/homedetails/46-Kingwood-Greens-Dr-Kingwood-TX-77339/28065573_zpid/",
    "zpid": "28065573",
    "status": "for_sale",
    "price": 318000,
    "zestimate": 325000,
    "rentZestimate": 2400,
    "beds": 5,
    "baths": 4,
    "sqft": 5526,
    "lotSize": "22,346 sqft",
    "yearBuilt": 2000,
    "propertyType": "SINGLE_FAMILY",
    "stories": 2,
    "parking": "3 garage spaces",
    "hoaFee": 150,
    "pricePerSqft": 58,
    "daysOnZillow": 14,
    "address": "46 Kingwood Greens Dr",
    "city": "Kingwood",
    "state": "TX",
    "zipCode": "77339",
    "latitude": 30.033194,
    "longitude": -95.180402,
    "brokerName": "REALHome Services and Solutions, Inc.",
    "agentName": "Lori Brown",
    "agentPhone": "(979) 255-0702",
    "description": "Spacious 5 bedroom home in Kingwood with pool and 3-car garage. Updated kitchen, hardwood floors throughout, and large backyard with mature trees...",
    "photos": [
        "https://photos.zillowstatic.com/fp/example1.jpg",
        "https://photos.zillowstatic.com/fp/example2.jpg"
    ],
    "priceHistory": [
        {
            "date": "2026-03-01",
            "event": "Listed",
            "price": 318000,
            "pricePerSqft": 58,
            "priceChangeRate": 0,
            "source": "HAR"
        },
        {
            "date": "2002-01-03",
            "event": "Sold",
            "price": 215000,
            "pricePerSqft": 39,
            "priceChangeRate": 0,
            "source": "Public Record"
        }
    ],
    "taxHistory": [
        {
            "year": 2025,
            "taxPaid": 8500,
            "value": 310000,
            "taxIncreaseRate": 0.02,
            "valueIncreaseRate": 0.03
        }
    ],
    "schools": [
        {
            "name": "Kingwood Park High School",
            "level": "High",
            "grades": "9-12",
            "distance": 1.2,
            "rating": 7,
            "type": "public"
        }
    ],
    "features": {
        "heating": ["Central"],
        "cooling": ["Central Air"],
        "flooring": ["Hardwood", "Tile"],
        "roofType": "Composition",
        "poolFeatures": ["In Ground"],
        "parkingFeatures": ["Attached Garage"]
    },
    "scrapedAt": "2026-03-25T12:00:00.000000+00:00"
}
```

## FAQ

**Do I need a proxy to scrape Zillow?**
No configuration is needed on your part. The scraper automatically uses a residential proxy to access Zillow.com reliably.

**What is the difference between BUY, RENT, and SOLD modes?**
BUY searches active for-sale listings, RENT searches rental apartments and homes, and SOLD returns recently sold properties with their final sale prices.

**What is a Zestimate?**
A Zestimate is Zillow's proprietary estimated market value for a property. The rent Zestimate is a similar estimate for what a property could rent for monthly. Both are included in the output when available.

**How many properties can I scrape per run?**
You can scrape up to 500 properties per run. Each search page returns approximately 40 listings, and you can configure up to 20 pages per search.

**Why are some fields missing from certain properties?**
The scraper automatically removes empty fields from the output. Not all Zillow listings have complete data — some may lack Zestimates, tax history, school data, or HOA fees depending on the property and location.

**What happens if I set Scrape Full Details to false?**
Disabling detail enrichment produces a significantly faster run. You will still receive core listing data (price, beds, baths, sqft, address, Zestimate) from search results, but you will not get schools, tax history, price history, full descriptions, or property features.

**Can I scrape a specific ZIP code or neighborhood?**
Yes. Enter the location in the Search Location field using formats like "77339" (ZIP code), "Kingwood, TX" (neighborhood and state), or any location Zillow recognizes.

**Can I scrape specific Zillow URLs directly?**
Yes. Paste any Zillow property detail URL or search results page URL into the Start URLs field. You can combine direct URLs with a location search in the same run.

**How fast is the scraper?**
Speed depends on whether detail enrichment is enabled. With details enabled, expect approximately 5-10 properties per minute. With details disabled, each search page (approximately 40 properties) loads in a few seconds.

**How current is the data?**
The scraper extracts live data directly from Zillow.com at the time of each run. Every output item includes a scrapedAt timestamp so you know exactly when the data was collected.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/zillow-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
