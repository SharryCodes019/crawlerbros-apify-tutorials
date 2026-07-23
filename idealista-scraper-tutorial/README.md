# Idealista Scraper Tutorial: Run This Apify Actor with Python

Scrape real estate listings from Idealista.com. Extract property prices, locations, features, photos, and agent contacts for Spain, Italy, and Portugal.

This repository shows how to run [Idealista Scraper](https://apify.com/crawlerbros/idealista-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/idealista-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/idealista-scraper](https://apify.com/crawlerbros/idealista-scraper)
- **SEO title:** Idealista Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape real estate listings from Idealista.com. Extract property prices, locations, features, photos, and agent contacts for Spain, Italy, and Portugal.

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

# Idealista Scraper

Extract real estate listing data from Idealista.com across Spain, Italy, and Portugal. Get property prices, sizes, locations, features, photos, and agent contacts for homes, offices, garages, new developments, and more.

## What It Does

- Scrape property listings for **sale or rent** across all property types
- Support for **Spain** (idealista.com), **Italy** (idealista.it), and **Portugal** (idealista.pt)
- **30+ data fields** per listing including price, size, location, features, and agency info
- All property types: homes, offices, premises, garages, lands, storage rooms, buildings, bedrooms
- Automatic **pagination** — collects all available pages up to your configured maximum
- Bypass Idealista's DataDome anti-bot protection with residential proxy rotation
- Export to **JSON, CSV, Excel, or XML**

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `location` | string | Yes* | madrid-madrid | City or area slug from Idealista URLs (e.g., `madrid-madrid`, `barcelona-barcelona`, `lisboa`, `roma-roma`) |
| `operation` | string | No | sale | Listing type: `sale` or `rent` |
| `propertyType` | string | No | homes | Property type (see list below) |
| `country` | string | No | es | Target country: `es` (Spain), `pt` (Portugal), `it` (Italy) |
| `maxItems` | integer | No | 100 | Maximum listings to scrape (max 1,800 per search) |
| `startUrls` | array | Yes* | — | Direct Idealista search URLs — overrides location/operation/propertyType |
| `proxyConfiguration` | object | Yes | RESIDENTIAL | Residential proxy is required |

\* At least one of `location` or `startUrls` is required.

### Property Types

| Value | Description |
|-------|-------------|
| `homes` | Apartments, houses, villas |
| `newDevelopments` | Off-plan and new-build developments |
| `offices` | Office spaces |
| `premises` | Commercial premises / retail units |
| `garages` | Garages and parking spaces |
| `lands` | Plots and land |
| `storageRooms` | Storage rooms (trasteros) |
| `buildings` | Entire buildings |
| `bedrooms` | Rooms for rent |

### Example Input

```json
{
    "location": "madrid-madrid",
    "operation": "sale",
    "propertyType": "homes",
    "country": "es",
    "maxItems": 50
}
```

### Location Slug Reference

Find your slug by searching on Idealista and copying the location segment from the URL:

| Country | Location | Slug |
|---------|----------|------|
| Spain | Madrid | `madrid-madrid` |
| Spain | Barcelona | `barcelona-barcelona` |
| Spain | Seville | `sevilla-sevilla` |
| Spain | Valencia | `valencia-valencia` |
| Spain | Marbella | `marbella-malaga` |
| Spain | Málaga | `malaga-malaga` |
| Portugal | Lisbon | `lisboa` |
| Portugal | Porto | `porto` |
| Portugal | Faro | `faro` |
| Italy | Rome | `roma-roma` |
| Italy | Milan | `milano-milano` |
| Italy | Florence | `firenze-firenze` |

You can also paste a full Idealista URL directly into the `location` field, or use `startUrls` to scrape multiple search pages at once.

## Output

Each property listing produces one dataset record. This version scrapes search-result cards (not individual property detail pages), so fields are split below into what the search page reliably exposes vs. what would need a detail-page visit (see [Limitations](#limitations)).

### Core Fields (reliably populated)

| Field | Type | Description |
|-------|------|-------------|
| `propertyCode` | string | Idealista property ID |
| `url` | string | Full URL to the property listing page |
| `price` | integer | Listing price in EUR |
| `priceByArea` | integer | Price per square meter in EUR |
| `currency` | string | Currency code (EUR) |
| `size` | integer | Property size in m² |
| `rooms` | integer | Number of bedrooms |
| `bathrooms` | integer | Number of bathrooms (from the card, or parsed from the description text) |
| `floor` | string | Floor level (e.g., `4ª planta exterior con ascensor`) |
| `exterior` | boolean | Exterior-facing property |
| `description` | string | Listing description text as shown on the search card |

### Location Fields (reliably populated)

| Field | Type | Description |
|-------|------|-------------|
| `address` | string | Street address or location label as shown on the card |
| `municipality` | string | City or municipality, parsed from the address |
| `district` | string | District or neighbourhood, parsed from the address |
| `country` | string | Country code: `es`, `pt`, or `it` |

### Media Fields (reliably populated)

| Field | Type | Description |
|-------|------|-------------|
| `thumbnail` | string | Primary listing photo URL |
| `numPhotos` | integer | Total number of photos in the card's gallery |

### Feature Fields (reliably populated)

| Field | Type | Description |
|-------|------|-------------|
| `hasLift` | boolean | Building has an elevator |
| `hasSwimmingPool` | boolean | Property has a pool |
| `hasTerrace` | boolean | Property has a terrace |
| `hasAirConditioning` | boolean | Property has air conditioning |
| `hasBoxRoom` | boolean | Includes a storage room (trastero) |
| `hasGarden` | boolean | Property has a garden |
| `hasParkingSpace` | object | `{ hasParkingSpace, isParkingSpaceIncludedInPrice }` — detected from card text |

### Contact Fields (reliably populated)

| Field | Type | Description |
|-------|------|-------------|
| `contactInfo` | object | Agency details: `{ commercialName, agencyLogo }` |

### Status & Classification Fields (reliably populated)

| Field | Type | Description |
|-------|------|-------------|
| `propertyType` | string | Property type (homes, offices, etc.) — from your search input |
| `operation` | string | `sale` or `rent` — from your search input |
| `newDevelopment` | boolean | New construction development, detected from card text |
| `topPlus` | boolean | Top Plus premium placement, detected from card styling |
| `scrapedAt` | string | ISO 8601 UTC timestamp of scrape |

### Fields not available from search cards

Idealista's search-result cards don't expose these — they require visiting each property's individual detail page, which this version doesn't do yet (see [Limitations](#limitations)):

`province`, `latitude`, `longitude`, `showAddress`, `locationId`, `multimedia`, `hasVideo`, `has3DTour`, `has360`, `hasStaging`, `hasPlan`, `status`, `newProperty`, `externalReference`, `detailedType`, `topNewDevelopment`, `visualHighlight`, `urgentVisualHighlight`, `preferenceHighlight`, `topHighlight`.

### Sample Output

```json
{
    "propertyCode": "107795847",
    "url": "https://www.idealista.com/inmueble/107795847/",
    "price": 1160000,
    "priceByArea": 5321,
    "currency": "EUR",
    "size": 218,
    "rooms": 3,
    "bathrooms": 2,
    "floor": "4ª planta exterior con ascensor",
    "exterior": true,
    "description": "Espectacular piso en venta en el barrio de Salamanca...",
    "address": "Piso en Calle de Jorge Juan, Recoletos, Madrid",
    "municipality": "Madrid",
    "district": "Recoletos",
    "country": "es",
    "thumbnail": "https://img3.idealista.com/blur/WEB_LISTING/0/id.pro.es.image.master/...",
    "numPhotos": 24,
    "hasLift": true,
    "hasTerrace": true,
    "hasAirConditioning": true,
    "hasParkingSpace": {
        "hasParkingSpace": true,
        "isParkingSpaceIncludedInPrice": false
    },
    "contactInfo": {
        "commercialName": "Engel & Völkers Madrid",
        "agencyLogo": "https://img3.idealista.com/..."
    },
    "propertyType": "homes",
    "operation": "sale",
    "newDevelopment": false,
    "topPlus": false,
    "scrapedAt": "2026-06-23T10:00:00+00:00"
}
```

## When the run finds nothing

If a run ends with 0 listings, the dataset stays empty (no fabricated placeholder records) and the run's status message explains why:

- **All attempts blocked** — Idealista's DataDome anti-bot protection blocked every session attempt. This is usually temporary; try again, and make sure a residential proxy is configured (the default).
- **No listings extracted** — a session got past anti-bot but the page had no results, most often because the location slug is wrong. Check the [Location Slug Reference](#location-slug-reference) table above — Italy requires Italian names (`roma-roma`, not `rome`), and Portugal uses Portuguese names (`lisboa`, not `lisbon`).
- **No URLs to process** — `startUrls` only contained individual property detail pages, which this actor doesn't scrape yet (search result pages only).

Check the run's Status Message in the Apify Console for the specific reason.

## Use Cases

- **Market analysis**: Track property prices and trends across Spanish, Italian, and Portuguese cities
- **Investment research**: Compare prices per square meter across neighbourhoods and districts
- **Competitive monitoring**: Track competitor agency listings and pricing strategies
- **Lead generation**: Collect agency contact details for real estate businesses
- **Portfolio management**: Monitor listings in specific areas for property management firms
- **Price alerts**: Run on a schedule to detect new listings or price changes

## Limitations

- **Residential proxy required**: Idealista uses DataDome anti-bot protection that blocks all datacenter IPs.
- **Search result cap**: Idealista caps search results at ~1,800 listings (60 pages) per query. Split large cities into districts for broader coverage.
- **Rate limits**: The scraper uses 2–4 second delays between pages to avoid detection. Expect ~30 listings per minute.
- **No individual property pages**: This version scrapes search result cards. Full detail pages (phone numbers, more photos) require navigating to each property URL individually.

## FAQ

**Do I need a login or cookies?**
No. Idealista listings are publicly accessible — no account required.

**Why is a residential proxy required?**
Idealista uses DataDome, an enterprise anti-bot platform that blocks all datacenter IP ranges instantly. Residential proxies mimic real user traffic and are the only way to reliably access the site programmatically.

**Which countries are supported?**
Spain (`idealista.com`), Portugal (`idealista.pt`), and Italy (`idealista.it`).

**What property types can I scrape?**
Homes, new developments, offices, commercial premises, garages, plots/land, storage rooms, entire buildings, and rooms for rent.

**How do I find the location slug?**
Search on Idealista and look at the URL. For `idealista.com/venta-viviendas/madrid-madrid/`, the slug is `madrid-madrid`. For Portugal: `idealista.pt/comprar-casas/lisboa/` → `lisboa`. For Italy: `idealista.it/vendita-case/roma-roma/` → `roma-roma`.

**Why are some fields missing from the output?**
Fields are omitted when they have no value. For example, coordinates appear only when Idealista exposes them, and features like pool or terrace are only included when they are mentioned in the listing card.

**How many listings can I scrape?**
Up to 1,800 per search query (Idealista's hard cap). For large cities, split the search by district or neighbourhood to get broader coverage.

**How fast is the scraper?**
Each page takes 30–60 seconds (browser warmup + page load). A run of 100 listings typically takes 5–10 minutes depending on DataDome response time.

**Can I scrape multiple cities in one run?**
Yes — use `startUrls` to provide multiple search page URLs (one per city or district). The actor scrapes them in sequence up to `maxItems` total.

**What if the run finishes with 0 listings?**
Check the run's Status Message — it explains whether Idealista blocked every attempt (temporary; try again) or the location slug returned no results.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/idealista-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
