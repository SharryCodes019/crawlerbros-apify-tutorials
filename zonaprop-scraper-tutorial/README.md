# ZonaProp Scraper Tutorial: Run This Apify Actor with Python

Scrape real estate listings from ZonaProp.com.ar, Argentina's leading property portal. Extract prices, locations, features, images, and publisher info.

This repository shows how to run [ZonaProp Scraper](https://apify.com/crawlerbros/zonaprop-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/zonaprop-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/zonaprop-scraper](https://apify.com/crawlerbros/zonaprop-scraper)
- **SEO title:** ZonaProp Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape real estate listings from ZonaProp.com.ar, Argentina's leading property portal. Extract prices, locations, features, images, and publisher info.

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

# ZonaProp Scraper

Extract real estate listing data from ZonaProp.com.ar — Argentina's leading property portal. Get prices, locations, property features, photos, and agent contact details for apartments, houses, land, PH units, and commercial properties across Buenos Aires and all of Argentina.

## What is ZonaProp Scraper?

ZonaProp Scraper is an Apify actor that extracts property listing data from ZonaProp.com.ar. Paste a search URL directly from the ZonaProp website or configure filters for property type, operation type, and location to collect structured data for every listing found. Each result includes everything from price and surface area to GPS coordinates, publisher contact details, and full photo galleries.

## Features

- **Search by URL or filters** — Paste any ZonaProp search URL, or configure location, property type, and operation type directly
- **Three operation types** — For sale, for rent, or temporary rentals
- **Multiple property types** — Apartments, houses, land, PH units, and commercial properties
- **Full location data** — Street address, neighborhood (barrio), city, province, and GPS coordinates
- **Pricing details** — Price, currency (USD or ARS), and price per square meter
- **Property features** — Rooms (ambientes), bedrooms, bathrooms, total area, covered area, garages, and year built
- **Photo galleries** — All listing images with direct URLs
- **Publisher contact info** — Agent or agency name, type, and phone number
- **Market timing** — Publication date and days on market for every listing
- **Covers all of Argentina** — CABA, Greater Buenos Aires, Córdoba, Rosario, Mendoza, and more

## What Data Can You Extract?

| Field | Type | Description |
|-------|------|-------------|
| title | string | Listing title |
| description | string | Full listing description |
| url | string | Direct link to listing on ZonaProp |
| listingId | string | Unique listing identifier |
| listingType | string | Operation type: sale, rent, or temporary |
| propertyType | string | Property type: apartment, house, land, ph, commercial |
| publishDate | string | Date listing was published |
| daysOnMarket | integer | Days since listing was published |
| price | number | Listing price |
| currency | string | Currency code (USD or ARS) |
| pricePerSqm | number | Price per square meter |
| address | string | Street address |
| neighborhood | string | Neighborhood (barrio) |
| city | string | City name |
| province | string | Province name |
| latitude | number | GPS latitude |
| longitude | number | GPS longitude |
| rooms | integer | Number of rooms (ambientes) |
| bedrooms | integer | Number of bedrooms |
| bathrooms | integer | Number of bathrooms |
| totalArea | number | Total surface area in m² |
| coveredArea | number | Covered surface area in m² |
| garages | integer | Number of garage spaces |
| yearBuilt | integer | Year property was built |
| images | array | Array of image URLs |
| mainImage | string | Primary image URL |
| publisherName | string | Publisher or agent name |
| publisherType | string | Publisher type: agent, owner, or agency |
| publisherPhone | string | Publisher contact phone number |

## How to Use

1. **Open ZonaProp** — Go to [zonaprop.com.ar](https://www.zonaprop.com.ar) and run a search with your desired filters (location, property type, price range, etc.)
2. **Copy the URL** — Copy the search results page URL from your browser's address bar
3. **Configure the actor** — Paste the URL into the **Search URL** field, or use the individual filter fields to set location, property type, and operation type
4. **Set result limit** — Choose how many listings to return (up to 1,000) and run the actor
5. **Download your data** — Export results as JSON, CSV, Excel, or XML from the Apify dataset

## Input Parameters

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| searchUrl | string | No | — | ZonaProp search URL. Paste any search results page URL from zonaprop.com.ar. Takes priority over all other filters. |
| propertyType | string | No | all | Property type to filter by: `all`, `apartment`, `house`, `land`, `ph`, `commercial` |
| operationType | string | No | sale | Operation type: `sale`, `rent`, or `temporary` |
| location | string | No | — | City or neighborhood slug from ZonaProp URLs (e.g., `capital-federal`, `palermo`, `cordoba`) |
| maxResults | integer | No | 100 | Maximum number of listings to return (1–1000) |
| proxyConfiguration | object | No | AR residential | Proxy settings. Defaults to Argentina residential proxies for reliable access. |

**Note:** Either `searchUrl` or at least one filter field (`location`, `propertyType`, `operationType`) should be provided to define a search.

## Output Example

```json
{
    "title": "Departamento en Venta en Palermo, Capital Federal",
    "description": "Hermoso departamento de 3 ambientes con balcón y vista al parque...",
    "url": "https://www.zonaprop.com.ar/propiedades/departamento-en-venta-palermo-12345.html",
    "listingId": "12345",
    "listingType": "sale",
    "propertyType": "apartment",
    "publishDate": "2026-03-15",
    "daysOnMarket": 25,
    "price": 150000,
    "currency": "USD",
    "pricePerSqm": 1875.0,
    "address": "Av. Santa Fe 1234",
    "neighborhood": "Palermo",
    "city": "Capital Federal",
    "province": "Buenos Aires",
    "latitude": -34.5875,
    "longitude": -58.4098,
    "rooms": 3,
    "bedrooms": 2,
    "bathrooms": 1,
    "totalArea": 80,
    "coveredArea": 70,
    "garages": 1,
    "yearBuilt": 2015,
    "images": [
        "https://imgar.zonapropcdn.com/avisos/1/00/12/345/1200x1200/img1.jpg",
        "https://imgar.zonapropcdn.com/avisos/1/00/12/345/1200x1200/img2.jpg"
    ],
    "mainImage": "https://imgar.zonapropcdn.com/avisos/1/00/12/345/1200x1200/img1.jpg",
    "publisherName": "Inmobiliaria Premium",
    "publisherType": "agency",
    "publisherPhone": "011-4567-8901"
}
```

## Use Cases

- **Argentina real estate market research** — Track property prices and trends across Buenos Aires neighborhoods and Argentine cities
- **Investment analysis** — Compare price per square meter across barrios to identify value opportunities
- **Rental market monitoring** — Collect rental listings to analyze market rates and availability in CABA and GBA
- **Lead generation** — Gather agent and agency contact information for real estate businesses
- **Price tracking** — Monitor how listing prices and days on market evolve over time
- **Portfolio management** — Track competing listings in target areas for property developers and managers
- **Academic and economic research** — Study Argentina's housing market using structured, up-to-date listing data

## FAQ

**What is ZonaProp?**
ZonaProp (zonaprop.com.ar) is Argentina's leading real estate portal, listing hundreds of thousands of properties for sale and rent across the country — from Buenos Aires and the Greater Buenos Aires area to Córdoba, Rosario, Mendoza, and beyond. It is the primary platform used by Argentine real estate agencies, individual sellers, and developers to publish property listings.

**What property types are supported?**
The scraper supports all major property types available on ZonaProp: apartments (departamentos), houses (casas), land (terrenos), PH units (casas en propiedad horizontal), and commercial properties (locales, oficinas, galpones, etc.).

**How do I use a search URL?**
Go to [zonaprop.com.ar](https://www.zonaprop.com.ar), apply your desired filters (neighborhood, price range, number of rooms, etc.), and copy the URL from your browser's address bar. Paste it into the **Search URL** input field. The scraper will follow that exact search and paginate through all results up to your specified limit.

**What locations are available?**
The scraper covers all of Argentina. This includes the Ciudad Autónoma de Buenos Aires (CABA), the entire Greater Buenos Aires metropolitan area (GBA), and major cities and provinces such as Córdoba, Rosario, Mendoza, Tucumán, Mar del Plata, and more.

**What currencies are used on ZonaProp?**
Property listings on ZonaProp are priced in either US Dollars (USD) or Argentine Pesos (ARS), depending on the seller. The `currency` field in the output indicates which currency applies to each listing's price.

**How many listings can I scrape per run?**
You can collect up to 1,000 listings per run by setting the `maxResults` parameter. For larger datasets, you can run the actor multiple times with different search filters or locations to cover more of the market.

**Can I filter by price range or number of rooms?**
Yes — the easiest way is to apply those filters directly on ZonaProp's website, then copy the resulting search URL and paste it into the **Search URL** input. The scraper will respect all filters embedded in the URL, including price range, surface area, number of rooms (ambientes), and more.

**What is "ambientes"?**
"Ambientes" is the Argentine real estate term for rooms — it refers to the total number of main living spaces in a property, typically including bedrooms, living room, and dining area (but not bathrooms or service areas). A 3-ambiente apartment, for example, generally has 2 bedrooms plus a living/dining space. This is captured in the `rooms` field in the output.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/zonaprop-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
