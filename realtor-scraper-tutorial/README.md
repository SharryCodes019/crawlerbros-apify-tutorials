# Realtor Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings from Realtor.com. Get prices, beds, baths, sqft, photos, agents, schools, tax history, flood/wildfire risk data, and 40+ fields per property.

This repository shows how to run [Realtor Scraper](https://apify.com/crawlerbros/realtor-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/realtor-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/realtor-scraper](https://apify.com/crawlerbros/realtor-scraper)
- **SEO title:** Realtor Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings from Realtor.com. Get prices, beds, baths, sqft, photos, agents, schools, tax history, flood/wildfire risk data, and 40+ fields per property.

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

# Realtor.com Property Scraper

Scrape property listings from Realtor.com. Get prices, descriptions, photos, agent details, schools, tax history, flood/noise/wildfire risk data, and 40+ fields per property. Search for sale, rent, or recently sold properties.

## What is Realtor.com Property Scraper?

Realtor.com Property Scraper is an Apify actor that extracts property listing data from Realtor.com. Enter a location, choose a search mode (buy, rent, or sold), and get structured data for every property — from basic listing details to comprehensive information including nearby schools, tax history, and environmental risk scores.

## Features

- **Search by location** — Find properties in any US city, state, or neighborhood
- **Three search modes** — For sale (BUY), for rent (RENT), or recently sold (SOLD)
- **Comprehensive property data** — Price, beds, baths, sqft, lot size, year built, garage, stories
- **Full descriptions** — Property marketing text and listing details
- **Photo URLs** — All listing photos with direct image links
- **Agent and office info** — Agent name, phone, email, and brokerage office
- **Nearby schools** — School name, rating, distance, grades, and type
- **Environmental risk data** — Flood factor, wildfire risk, and noise scores
- **Listing history** — Price changes, sales events, and source data
- **Tax history** — Assessment values, market values, and tax amounts by year
- **Property features** — Cooling, heating, roofing, construction, pool, fireplace, zoning
- **Direct URL support** — Paste Realtor.com property detail URLs for targeted scraping
- **Automatic deduplication** — No duplicates when combining search and direct URLs

## Use Cases

- **Real estate investment analysis** — Compare prices, tax history, and environmental risks
- **Market research** — Track listing prices, sold prices, and days on market across neighborhoods
- **Property comparison** — Side-by-side data for multiple listings in a target area
- **Rental market analysis** — Compare rental prices and availability by location
- **School district analysis** — Find properties near top-rated schools
- **Risk assessment** — Evaluate flood, wildfire, and noise risks before buying
- **Agent/broker research** — Identify active listing agents in your target market
- **Data enrichment** — Augment your property database with fresh listing data

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| Search Location | String | — | City and state to search (e.g., "Houston, TX", "San Francisco, CA") |
| Search Mode | Select | BUY | BUY (for sale), RENT (for rent), or SOLD (recently sold) |
| Maximum Properties | Integer | 50 | Max property listings to scrape (1-500) |
| Maximum Pages | Integer | 5 | Max search result pages to scrape per search (1-20) |
| Scrape Full Details | Boolean | true | Fetch full detail pages for schools, history, tax, etc. Disable for faster runs. |
| Start URLs | URL List | — | Direct Realtor.com property or search URLs |

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
    "maxItems": 30
}
```

### Example input — Direct property URLs

```json
{
    "startUrls": [
        { "url": "https://www.realtor.com/realestateandhomes-detail/123-Main-St_Houston_TX_77001_M12345-67890" }
    ],
    "scrapeDetails": true
}
```

## Output

Each property produces one item in the output dataset:

### Core Property Data

| Field | Type | Description |
|-------|------|-------------|
| url | String | Property detail URL on Realtor.com |
| id | String | Realtor.com property ID |
| listingId | String | MLS listing ID |
| status | String | for_sale, for_rent, sold, pending, etc. |
| listPrice | Number | Current listing price |
| lastSoldPrice | Number | Last recorded sale price |
| soldOn | String | Date property was last sold |
| priceReduced | Number | Price reduction amount (if applicable) |
| beds | Number | Number of bedrooms |
| baths | String | Total bathrooms (e.g., "4.5") |
| bathsFull | Number | Full bathrooms |
| bathsHalf | Number | Half bathrooms |
| sqft | Number | Living area in square feet |
| lotSqft | Number | Lot size in square feet |
| yearBuilt | Number | Year the property was constructed |
| type | String | Property type (single_family, condo, townhouse, etc.) |
| subType | String | Property sub-type |
| stories | Number | Number of stories |
| garage | Number | Garage spaces |
| name | String | Property or community name |
| text | String | Full property description |
| listDate | String | Date when listed |

### Location

| Field | Type | Description |
|-------|------|-------------|
| address.street | String | Street address |
| address.city | String | City |
| address.state | String | State code (e.g., "TX") |
| address.postalCode | String | ZIP code |
| coordinates.lat | Number | Latitude |
| coordinates.lng | Number | Longitude |

### Rich Data (from detail pages)

| Field | Type | Description |
|-------|------|-------------|
| photos | Array | Photo URLs for the property |
| features | Object | Property features — cooling, heating, roofing, construction, pool, fireplace, zoning |
| agents | Array | Listing agents — name, phone, email, office, type |
| nearbySchools | Array | Nearby schools — name, rating, distance, grades, type |
| local.flood | Object | Flood factor score, severity, FEMA zone |
| local.noise | Object | Noise score and categories |
| local.wildfire | Object | Wildfire factor score and severity |
| history | Array | Listing history — date, event, price, price per sqft |
| taxHistory | Array | Tax records — year, tax amount, assessment and market values |
| yearRenovated | Number | Year of last renovation |
| rooms | Number | Total room count |
| scrapedAt | String | ISO timestamp when data was collected |

### Sample output

```json
{
    "url": "https://www.realtor.com/realestateandhomes-detail/46-Kingwood-Greens-Dr_Kingwood_TX_77339_M71671-24763",
    "id": "7167124763",
    "listingId": "2989700820",
    "status": "for_sale",
    "listPrice": 318000,
    "lastSoldPrice": null,
    "soldOn": "2002-01-03",
    "priceReduced": null,
    "beds": 5,
    "baths": "4.5",
    "bathsFull": null,
    "bathsHalf": null,
    "sqft": 5526,
    "lotSqft": 22346,
    "yearBuilt": 2000,
    "type": "single_family",
    "subType": "",
    "stories": null,
    "garage": 3,
    "name": "",
    "text": "Spacious 5 bedroom home in Kingwood with pool and 3-car garage...",
    "listDate": "2025-12-23T15:21:17.000000Z",
    "address": {
        "street": "46 Kingwood Greens Dr",
        "city": "Kingwood",
        "state": "TX",
        "postalCode": "77339"
    },
    "coordinates": {
        "lat": 30.033194,
        "lng": -95.180402
    },
    "photos": [
        "https://ap.rdcpix.com/1751b6c594d6451bf2a78323162ed623l-m1516646319s.jpg"
    ],
    "agents": [
        {
            "name": "Lori Brown",
            "email": "lori.brown@rhss.com",
            "phone": "9792550702",
            "office": "REALHome Services and Solutions, Inc.",
            "type": "seller"
        }
    ],
    "features": {
        "cooling": "Central Air",
        "heating": "Central",
        "pool": "Yes",
        "roofing": "Composition"
    },
    "nearbySchools": [
        {
            "name": "Kingwood Park High School",
            "rating": 7,
            "distance": 1.2,
            "grades": ["9", "10", "11", "12"],
            "type": "public",
            "levels": ["high"],
            "studentCount": 2100
        }
    ],
    "local": {
        "flood": {
            "floodFactorScore": 3,
            "severity": "Minor",
            "femaZone": ["X"],
            "insuranceRequired": "No"
        },
        "noise": {
            "score": 72,
            "categories": ["traffic"]
        }
    },
    "history": [
        {
            "date": "2025-12-23",
            "event": "Listed",
            "price": 318000,
            "pricePerSqft": 58,
            "source": "HOTX"
        }
    ],
    "taxHistory": [
        {
            "year": 2024,
            "tax": 8500,
            "assessmentTotal": 310000,
            "assessmentLand": 95000,
            "assessmentBuilding": 215000,
            "marketTotal": 325000,
            "marketLand": 100000,
            "marketBuilding": 225000
        }
    ],
    "scrapedAt": "2026-03-25T12:00:00.000000+00:00"
}
```

## How to use

### Quick start

1. Enter a US city and state in the **Search Location** field (e.g., "Houston, TX")
2. Select a **Search Mode** — BUY, RENT, or SOLD
3. Set **Maximum Properties** to control how many listings to scrape
4. Click **Start** and wait for results

### Scrape specific properties

1. Go to [Realtor.com](https://www.realtor.com) in your browser
2. Navigate to the property listing you want
3. Copy the URL from your browser's address bar
4. Paste it into the **Start URLs** field

### Combine search and direct URLs

You can provide both a location search and direct URLs. The scraper processes all sources and deduplicates results automatically.

### Faster runs without detail enrichment

Set **Scrape Full Details** to `false` for a significantly faster run. You'll get core property data (price, beds, baths, sqft, address, photos, agents) from search results without visiting each property's detail page. This skips schools, tax history, listing history, risk data, and full descriptions.

## How many properties can I scrape?

Realtor.com shows up to **42 properties per search page**, with a maximum of 20 pages (840 properties per search). Use the **Maximum Properties** and **Maximum Pages** inputs to control how many to scrape.

## Tips

- **Start small** — Use `maxItems: 5` with `scrapeDetails: false` for your first run to verify the output format
- **Disable details for speed** — Set `scrapeDetails: false` for 3-5x faster runs when you only need listing-level data
- **Use specific locations** — "Houston, TX" works better than just "Houston"
- **Recently sold data** — Use SOLD mode for historical price data and market analysis

## FAQ

**Do I need a proxy?**
The scraper automatically uses a residential proxy, which is required to access Realtor.com. This is handled internally — no configuration needed.

**Why are some detail fields empty?**
Detail enrichment depends on what Realtor.com provides for each listing. Not all properties have school data, tax records, or environmental risk scores. Some newer listings may not have history yet.

**What's the difference between BUY, RENT, and SOLD modes?**
BUY searches active for-sale listings, RENT searches rental apartments and homes, and SOLD shows recently sold properties with final sale prices.

**Can I scrape a specific neighborhood or ZIP code?**
Yes. Use formats like "77339" (ZIP code), "Kingwood, TX" (neighborhood + state), or a full address.

**How fast is the scraper?**
With details enabled: approximately 5-10 properties per minute. Without details: approximately 42 properties per page every 5-8 seconds.

**Why did I get fewer properties than maxItems?**
The location may have fewer listings than your limit, or the search may have reached the last page of results.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/realtor-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
