# Mobile.de Car Scraper Tutorial: Run This Apify Actor with Python

Extract used car listings from mobile.de with make, model, price, mileage, year, fuel, transmission, dealer info, and photos.

This repository shows how to run [Mobile.de Car Scraper](https://apify.com/crawlerbros/mobile-de-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/mobile-de-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/mobile-de-scraper](https://apify.com/crawlerbros/mobile-de-scraper)
- **SEO title:** Mobile.de Car Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract used car listings from mobile.de with make, model, price, mileage, year, fuel, transmission, dealer info, and photos.

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

# Mobile.de Car Scraper

Extract used and new car listings from **mobile.de** — Germany's largest vehicle marketplace with 1.5+ million listings. Returns **38 structured fields** per vehicle including make, model, year, price, mileage, power, fuel type, transmission, CO2 class, dealer contact, and preview image.

> ⚠️ **Residential Proxy Required**
>
> Mobile.de uses Akamai Bot Manager to block all datacenter and VPN IPs. A **German residential proxy** (Apify RESIDENTIAL group, country DE) is required for this actor to return any results. This is pre-configured as the default — you only need an **Apify subscription that includes residential proxies** (Starter plan or above). Without a residential proxy the actor will return no data.

## Features

- **38 output fields** per vehicle — complete flat schema with typed defaults (zero nulls)
- **1.5M+ listings indexed** — cars, vans, estate cars, sedans, SUVs, and more
- **Full filter pass-through** — make, model, price, mileage, year, fuel type, transmission, postal-code radius
- **Pagination** — walks pages automatically via `pageNumber` query parameter (27 results per page)
- **Price ratings** — each car has an "is this a good price?" rating from mobile.de's pricing engine
- **Dealer details** — name, postcode, city, country, phone, seller type
- **Preview image** per listing
- **Browser fallback** — Playwright + Camoufox stealth browser chain if the primary request path is challenged
- **No login, no cookies** — works via Chrome 131 TLS impersonation + residential proxy

## Requirements

| Requirement | Details |
|---|---|
| **Residential Proxy** | Apify RESIDENTIAL proxy, country: DE. Included in Apify **Starter** plan and above. |
| **Apify Platform** | Must run on Apify platform (not locally) to access the residential proxy pool. |

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `startUrls` | Array | No | Mobile.de spec page URLs (`suchen.mobile.de/auto/*.html`) or legacy search URLs. Defaults to VW Golf listings. |
| `maxItems` | Integer | No | Maximum vehicles to return (default 50, max 500). |
| `proxyConfiguration` | Object | **Yes** | Proxy settings. Defaults to Apify RESIDENTIAL (DE). Must be a residential proxy — datacenter IPs are blocked by mobile.de. |

### Example Input

```json
{
    "startUrls": [
        "https://suchen.mobile.de/auto/volkswagen-golf.html"
    ],
    "maxItems": 100,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "DE"
    }
}
```

With legacy search URL and filters:

```json
{
    "startUrls": [
        "https://suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&s=Car&vc=Car&ms=1900;17;;;&fr=2020&ft=DIESEL&mnp=30000"
    ],
    "maxItems": 200,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "DE"
    }
}
```

## Output

Each vehicle has **38 fields**. All fields are always present with typed defaults — never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | Integer | Mobile.de listing ID |
| `url` | String | Full listing URL (suchen.mobile.de/auto-inserat/...) |
| `title` | String | Full title (make + model + variant) |
| `shortTitle` | String | Short title (make + model only) |
| `subTitle` | String | Variant / trim level |
| `make` | String | Manufacturer (BMW, Audi, Volkswagen, etc.) |
| `model` | String | Model name |
| `category` | String | Body category (Estate car, Sedan, SUV, etc.) |
| `vehicleClass` | String | Vehicle class code (Car) |

### Price
| Field | Type | Description |
|---|---|---|
| `price` | Integer | Gross price (native currency, integer) |
| `currency` | String | Currency code (typically EUR) |
| `priceFormatted` | String | Formatted price (e.g., `€41,390`) |
| `priceRating` | String | `VERY_GOOD_PRICE`, `GOOD_PRICE`, `FAIR_PRICE`, `INCREASED_PRICE`, `HIGH_PRICE` |

### Specifications
| Field | Type | Description |
|---|---|---|
| `mileageKm` | Integer | Mileage in kilometers |
| `powerKw` | Integer | Engine power in kW |
| `powerHp` | Integer | Engine power in HP |
| `firstRegistration` | String | First registration date (`MM/YYYY`) |
| `yearConstructed` | Integer | Year of first registration |
| `fuelType` | String | `Petrol`, `Diesel`, `Electric`, `Hybrid`, `LPG`, etc. |
| `transmission` | String | `Manual gearbox`, `Automatic`, `Semiautomatic` |
| `bodyType` | String | Body category (duplicate of `category`) |
| `exteriorColor` | String | Exterior color |
| `doors` | String | Door configuration (e.g., `4/5`) |
| `seats` | Integer | Seat count |
| `previousOwners` | Integer | Number of previous owners |
| `emissionClass` | String | German emission class (`Euro 6e`, `Euro 5`, etc.) |
| `co2Class` | String | CO₂ class (A-G) |
| `consumption` | String | Combined consumption (`5.7 l/100km (comb.)`, etc.) |
| `displacementCcm` | Integer | Engine displacement in ccm |

### Media & Dealer
| Field | Type | Description |
|---|---|---|
| `numImages` | Integer | Number of photos on listing |
| `previewImage` | String | Preview image URL |
| `location` | String | Dealer town |
| `postalCode` | String | Dealer postal code |
| `country` | String | Country code (DE, AT, etc.) |
| `dealerName` | String | Dealer name |
| `dealerType` | String | `DEALER` or `PRIVATE` |
| `dealerPhone` | String | Dealer phone number |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "id": 444796340,
    "url": "https://www.mobile.de/auto-inserat/bmw-m3-touring/444796340.html",
    "title": "BMW M3 Touring M xDrive Competition LED HUD NAVI H/K",
    "shortTitle": "BMW M3",
    "subTitle": "Touring M xDrive Competition LED HUD NAVI H/K",
    "make": "BMW",
    "model": "M3",
    "category": "Estate car",
    "vehicleClass": "Car",
    "price": 110000,
    "currency": "EUR",
    "priceFormatted": "€110,000",
    "priceRating": "GOOD_PRICE",
    "mileageKm": 11340,
    "powerKw": 390,
    "powerHp": 530,
    "firstRegistration": "03/2025",
    "yearConstructed": 2025,
    "fuelType": "Petrol",
    "transmission": "Automatic",
    "bodyType": "Estate car",
    "exteriorColor": "Grey",
    "doors": "4/5",
    "seats": 5,
    "previousOwners": 1,
    "emissionClass": "Euro 6e",
    "co2Class": "G",
    "consumption": "10.5 l/100km (comb.)",
    "displacementCcm": 2993,
    "numImages": 29,
    "previewImage": "https://img.classistatic.de/api/v1/mo-prod/images/3f/3fbc5257.jpg",
    "location": "Wermelskirchen",
    "postalCode": "42929",
    "country": "DE",
    "dealerName": "Autohaus Kaltenbach GmbH Co.KG BMW und MINI Vertragshändler",
    "dealerType": "DEALER",
    "dealerPhone": "+49 (0)2196 76796970",
    "scrapedAt": "2026-04-11T12:05:00+00:00"
}
```

## FAQ

**Q: Why do I need a residential proxy?**
Mobile.de uses **Akamai Bot Manager** to protect their listing pages. Akamai blocks all datacenter IPs (including Apify's standard datacenter proxy pool) with HTTP 403. A German residential IP is required to pass Akamai's checks. The actor is pre-configured to use Apify's `RESIDENTIAL` proxy group with country `DE` — you just need an Apify plan that includes residential proxies (Starter plan or above).

**Q: Which Apify plan do I need?**
Residential proxies are available on the **Starter plan** ($49/month) and above. The Free plan only includes datacenter proxies, which will not work with mobile.de. See [Apify Pricing](https://apify.com/pricing) for details.

**Q: Can I use my own proxy?**
Yes. Set `proxyConfiguration` to point to any residential proxy service you have access to — just make sure to use a German IP (`DE`). For example:
```json
{
    "proxyConfiguration": {
        "useApifyProxy": false,
        "proxyUrls": ["http://user:pass@your-proxy-host:port"]
    }
}
```

**Q: How do I construct a search URL?**
Apply filters on the mobile.de website, copy the URL from your browser (`suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&s=Car&vc=Car&...`), and paste it into `startUrls`. All filters (`ms=` for make/model, `fr=` for year, `ft=` for fuel type, `mnp=`/`mxp=` for price, `mnlm=`/`mxlm=` for mileage, `pgn=` for postcode radius) pass through verbatim. Alternatively, use a spec page URL like `https://suchen.mobile.de/auto/volkswagen-golf.html`.

**Q: How many cars per page?**
27 results per page (fixed by mobile.de). The scraper paginates automatically via `pageNumber=N` up to mobile.de's hard cap of 50 pages per search, giving you up to 1,350 unique cars per query.

**Q: Why is my run returning fewer unique cars than expected?**
Mobile.de promotes certain "top ads" and "eyecatcher ads" that appear on every page of a given search, so pages 2+ often have ~15–20 duplicates of page 1. The scraper deduplicates by listing ID so you only get unique vehicles.

**Q: How fresh is the data?**
The scraper hits the same data source as the mobile.de website — data is live and reflects the current state of listings at the time of the run.

## Use Cases

- **Used-car market research** — track inventory, prices, and age distribution across makes/models
- **Dealer monitoring** — watch specific dealers for new inventory
- **Investment analysis** — find underpriced listings using the `priceRating` field
- **Regional price comparisons** — filter by postal code radius to compare local markets
- **EV market analysis** — filter `fuelType=Electric` to track the EV market's growth
- **Price alerts** — daily runs with narrow filters (make + model + max price) for deal hunting
- **Data pipelines** — feed structured JSON into CRMs, BI tools, or ML models without post-processing

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/mobile-de-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
