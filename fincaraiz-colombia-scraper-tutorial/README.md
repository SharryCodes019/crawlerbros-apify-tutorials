# FincaRaiz Colombia Real Estate Scraper Tutorial: Run This Apify Actor with Python

Scrape property listings from FincaRaiz.com.co - Colombia's largest real estate portal with 100K+ active listings. Get apartments, houses, offices, and commercial spaces for sale or rent. Includes price, bedrooms, bathrooms, area, coordinates, agent details, and images.

This repository shows how to run [FincaRaiz Colombia Real Estate Scraper](https://apify.com/crawlerbros/fincaraiz-colombia-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/fincaraiz-colombia-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/fincaraiz-colombia-scraper](https://apify.com/crawlerbros/fincaraiz-colombia-scraper)
- **SEO title:** FincaRaiz Colombia Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape property listings from FincaRaiz.com.co - Colombia's largest real estate portal with 100K+ active listings. Get apartments, houses, offices, and commercial spaces for sale or rent. Includes price, bedrooms, bathrooms, area, coordinates, agent details, and images.

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

# FincaRaiz Colombia Real Estate Scraper

Scrape property listings from **FincaRaiz.com.co** — Colombia's largest real estate portal with 180,000+ active listings. Extract apartments, houses, offices, commercial spaces, warehouses, and land plots for sale or rent across all Colombian cities.

## What You Get

Each property listing includes:

| Field | Description |
|---|---|
| `listingId` | Unique FincaRaiz listing ID |
| `title` | Property title/name |
| `description` | Full description text |
| `operationType` | "Venta" (for sale) or "Arriendo" (for rent) |
| `propertyType` | Apartment, Casa, Oficina, Local, Bodega, Finca, Lote, etc. |
| `price` | Listing price in COP (Colombian Pesos) |
| `currencyCode` | COP, USD, or EUR |
| `priceUsd` | Price estimate in USD |
| `administrationFee` | Monthly administration fee (COP) if applicable |
| `city` | City/municipality name |
| `neighborhood` | Neighborhood or sector name |
| `address` | Full address (when available) |
| `latitude` | GPS latitude |
| `longitude` | GPS longitude |
| `stratum` | Colombian socioeconomic stratum (1–6) |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `garages` | Number of garage spaces |
| `areaSqm` | Property area in square meters |
| `terrainSqm` | Terrain/lot area (houses and land) |
| `floor` | Floor number in building |
| `floorsCount` | Total floors in building |
| `constructionState` | "Nuevo", "Usado", "Sobre planos", etc. |
| `antiquity` | Age of the property |
| `isProject` | Whether it's a new construction project |
| `amenities` | List of amenities (pool, gym, security, etc.) |
| `agent` | Agent/agency name, type, phone, agency URL |
| `images` | List of high-resolution image URLs |
| `thumbnail` | Cover image URL |
| `listingUrl` | Direct URL to the listing on FincaRaiz |
| `listedAt` | Date the property was listed |
| `updatedAt` | Date the listing was last updated |
| `scrapedAt` | UTC timestamp when the record was scraped |

## Input Options

| Parameter | Type | Default | Description |
|---|---|---|---|
| `mode` | select | `searchForSale` | `searchForSale` (Venta) or `searchForRent` (Arriendo) |
| `propertyType` | select | all | Filter by property type: Apartamento, Casa, Oficina, Bodega, Lote, etc. |
| `city` | text | all | Filter by city name (partial match, e.g. "Bogotá", "Medellín", "Cali") |
| `priceMin` | number | — | Minimum price in COP |
| `priceMax` | number | — | Maximum price in COP |
| `bedroomsMin` | number | — | Minimum number of bedrooms |
| `bedroomsMax` | number | — | Maximum number of bedrooms |
| `bathroomsMin` | number | — | Minimum number of bathrooms |
| `areaMin` | number | — | Minimum area in m² |
| `areaMax` | number | — | Maximum area in m² |
| `maxItems` | number | 50 | Maximum results to return (1–1000) |

## Example Use Cases

### Apartments for rent in Bogotá
```json
{
  "mode": "searchForRent",
  "propertyType": "Apartamento",
  "city": "Bogotá",
  "maxItems": 100
}
```

### Houses for sale under 500M COP in Medellín
```json
{
  "mode": "searchForSale",
  "propertyType": "Casa",
  "city": "Medellín",
  "priceMax": 500000000,
  "maxItems": 50
}
```

### 2–3 bedroom apartments for sale in Cali
```json
{
  "mode": "searchForSale",
  "propertyType": "Apartamento",
  "city": "Cali",
  "bedroomsMin": 2,
  "bedroomsMax": 3,
  "maxItems": 50
}
```

### Commercial spaces for rent nationwide
```json
{
  "mode": "searchForRent",
  "propertyType": "Local",
  "maxItems": 200
}
```

## Data Source

Property data is sourced directly from **FincaRaiz.com.co** — Colombia's leading real estate marketplace operated by InfoCasas Group. The platform provides publicly accessible listing data without requiring authentication.

**Coverage:** All Colombian cities and municipalities including Bogotá, Medellín, Cali, Barranquilla, Cartagena, Bucaramanga, Pereira, Manizales, and hundreds more.

**No API key or registration required.**

## Frequently Asked Questions

**How many listings are available?**
FincaRaiz has 180,000+ active sale listings and 100,000+ active rental listings as of 2025.

**Can I filter by specific neighborhood?**
Use the `city` filter to narrow to a city, then use post-processing to filter by neighborhood. The actor returns `neighborhood` in each record.

**Does this require a proxy?**
No — FincaRaiz serves public listing data without bot protection that requires proxy or residential IPs.

**How fresh is the data?**
Each run fetches live data directly from FincaRaiz. The `updatedAt` field shows when the property owner last updated the listing.

**What currencies are supported?**
Most listings are in COP (Colombian Pesos). Some commercial/luxury properties are listed in USD or UF. The `currencyCode` and `priceUsd` fields always clarify.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/fincaraiz-colombia-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
