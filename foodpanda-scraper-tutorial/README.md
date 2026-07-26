# Foodpanda Restaurant & Menu Scraper Tutorial: Run This Apify Actor with Python

Scrape Foodpanda restaurants by URL or location. Extracts name, rating, cuisines, delivery details, and full nested menus. Supports Singapore, Bangladesh, Pakistan, Hong Kong, and Malaysia.

This repository shows how to run [Foodpanda Restaurant & Menu Scraper](https://apify.com/crawlerbros/foodpanda-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/foodpanda-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/foodpanda-scraper](https://apify.com/crawlerbros/foodpanda-scraper)
- **SEO title:** Foodpanda Restaurant & Menu Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Foodpanda restaurants by URL or location. Extracts name, rating, cuisines, delivery details, and full nested menus. Supports Singapore, Bangladesh, Pakistan, Hong Kong, and Malaysia.

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

# Foodpanda Restaurant & Menu Scraper

Extract restaurant data from Foodpanda — including menus, ratings, delivery details, cuisines, and locations — using direct API access. No browser, no cookies, no manual proxy configuration: a country-targeted Apify residential proxy is hardcoded and applied automatically (required for Foodpanda's PerimeterX bot protection).

## What is this?

The Foodpanda Scraper is an [Apify](https://apify.com) actor that scrapes restaurant and menu data from Foodpanda in two modes:

- **URL Mode** — Paste one or more Foodpanda restaurant URLs to get their full details and menus
- **Discovery Mode** — Enter a location (city, coordinates, or Foodpanda city page URL) and the actor finds all nearby restaurants within your chosen radius

Supported countries: Singapore · Bangladesh · Pakistan · Hong Kong · Malaysia

## What data does it extract?

| Field | Description |
|-------|-------------|
| `vendorCode` | Foodpanda's internal restaurant ID |
| `vendorUrl` | Direct link to the restaurant page |
| `name` | Restaurant name |
| `rating` | Aggregate star rating (e.g. 4.9) |
| `reviewCount` | Number of customer reviews |
| `cuisines` | Cuisine tags (e.g. Fast Food, Halal, Chicken) |
| `vendorType` | Vendor category (restaurant, grocery, etc.) |
| `isOpen` | Whether currently open for delivery |
| `address` | Full street address |
| `city` | City (when available) |
| `country` | Country code (sg, bd, pk, hk, my) |
| `latitude` / `longitude` | Venue coordinates |
| `deliveryFee` | Delivery fee in local currency |
| `minimumOrder` | Minimum order value |
| `estimatedDeliveryTime` | Delivery ETA (e.g. "30-45 min") |
| `currency` | Currency code (SGD, BDT, PKR, HKD, MYR) |
| `heroImageUrl` | Restaurant banner/logo image URL |
| `menu` | Full nested menu (when enabled) |
| `menuCategoryCount` | Number of menu categories |
| `menuItemCount` | Total menu items |
| `itemsWithImageCount` | Items that have images |
| `itemsWithDescCount` | Items that have descriptions |
| `scrapedAt` | Scrape timestamp (UTC ISO-8601) |

### Menu item fields

| Field | Description |
|-------|-------------|
| `itemId` | Product ID |
| `name` | Item name |
| `description` | Item description |
| `price` | Price in local currency (e.g. 9.70) |
| `currency` | Currency code |
| `imageUrl` | Item image URL |
| `isAvailable` | Whether currently available |
| `dietaryAttributes` | Dietary tags (e.g. halal, vegetarian) |

## How to use

### URL Mode

1. Open any Foodpanda restaurant page in your browser
2. Copy the URL (e.g. `https://www.foodpanda.sg/restaurant/en/m3jj-mcdonalds-ang-mo-kio`)
3. Paste it into the **Restaurant URLs** field
4. Enable **Include Menu** if you want full menu data
5. Click **Start**

### Discovery Mode

1. Leave **Restaurant URLs** empty
2. Set your location using one of:
   - **Latitude + Longitude + Country** — most precise
   - **City Page URL** — paste a Foodpanda city listing URL (e.g. `https://www.foodpanda.sg/restaurants/new/`)
   - **City + Country** — type a city name and select country
3. Set **Search Radius** (km) and **Max Restaurants**
4. Optionally filter by **Vendor Types** (restaurant, grocery, etc.)
5. Click **Start**

## Input parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `restaurantUrls` | string[] | — | One or more Foodpanda restaurant URLs (URL mode) |
| `latitude` | number | — | Decimal latitude (Discovery mode) |
| `longitude` | number | — | Decimal longitude (Discovery mode) |
| `country` | select | — | Country code: sg, bd, pk, hk, my (required with lat/lon or city) |
| `cityPageUrl` | string | — | Foodpanda city listing URL (Discovery mode) |
| `city` | string | — | City name, e.g. "Karachi", "Singapore", "Dhaka" (Discovery mode) |
| `radiusKm` | number | 3 | Search radius in km (0.5–50) |
| `maxRestaurants` | integer | 50 | Max restaurants to return (1–500) |
| `includeMenu` | boolean | true (URL) / false (Discovery) | Fetch full menu data |
| `maxItemsPerRestaurant` | integer | 200 | Max menu items per restaurant (1–2000) |
| `vendorTypes` | string[] | ["restaurant"] | Filter by type: restaurant, grocery, convenience |

## Example output

```json
{
  "vendorCode": "m3jj",
  "vendorUrl": "https://www.foodpanda.sg/restaurant/en/m3jj",
  "name": "McDonald's (Ang Mo Kio)",
  "rating": 4.9,
  "reviewCount": 11601,
  "cuisines": ["Fast Food", "Beverages", "Chicken", "Halal", "Western"],
  "vendorType": "restaurants",
  "isOpen": true,
  "address": "51 Ang Mo Kio Avenue 3, #01-09, AMK Hub, Singapore 569922",
  "country": "sg",
  "latitude": 1.3696,
  "longitude": 103.8487,
  "deliveryFee": 0.0,
  "minimumOrder": 25.0,
  "currency": "SGD",
  "heroImageUrl": "https://images.deliveryhero.io/image/fd-sg/...",
  "menu": [
    {
      "categoryName": "Burgers & Wraps",
      "items": [
        {
          "itemId": "12345",
          "name": "Big Mac",
          "description": "Two all-beef patties, special sauce...",
          "price": 9.70,
          "currency": "SGD",
          "imageUrl": "https://images.deliveryhero.io/image/...",
          "isAvailable": true,
          "dietaryAttributes": ["halal"]
        }
      ]
    }
  ],
  "menuCategoryCount": 8,
  "menuItemCount": 10,
  "itemsWithImageCount": 10,
  "itemsWithDescCount": 8,
  "scrapedAt": "2026-04-14T10:00:00Z"
}
```

## Supported countries

| Country | Code | Domain | Cities supported |
|---------|------|--------|-----------------|
| Singapore | `sg` | foodpanda.sg | Singapore |
| Bangladesh | `bd` | foodpanda.com.bd | Dhaka, Chittagong |
| Pakistan | `pk` | foodpanda.com.pk | Karachi, Lahore, Islamabad |
| Hong Kong | `hk` | foodpanda.com.hk | Hong Kong |
| Malaysia | `my` | foodpanda.com.my | Kuala Lumpur, Penang |

## Use cases

- **Menu database** — Build a database of restaurant menus for comparison or analysis
- **Competitor research** — Track competitor pricing, menu changes, and delivery fees over time
- **Delivery fee monitoring** — Monitor delivery fees and minimum orders across restaurants
- **Restaurant discovery** — Find all restaurants in a neighbourhood with their ratings and cuisines
- **Price intelligence** — Track menu item prices for market research and trend analysis
- **Food tech & AI** — Dataset creation for food recommendation systems and NLP projects

## FAQ

**Do I need a proxy?**
No configuration needed. A country-targeted Apify residential proxy is hardcoded and applied automatically — required for Foodpanda's PerimeterX bot protection.

**Do I need to log in or provide credentials?**
No. The actor uses Foodpanda's public API — no login required.

**How often can I run this?**
For large discovery runs (500+ restaurants), we recommend running no more than once per hour. The actor uses session-based rate limiting with built-in delays.

**Why is my restaurant not found in Discovery mode?**
Discovery mode searches within a radius around a single point. Try increasing `radiusKm` or use URL mode with the exact restaurant URL.

**Can I scrape grocery stores and convenience stores too?**
Yes — set `vendorTypes` to include `grocery` or `convenience`, or leave it empty to include all vendor types.

**What currency are prices in?**
Prices are in the local currency of the country: SGD for Singapore, BDT for Bangladesh, PKR for Pakistan, HKD for Hong Kong, MYR for Malaysia.

**Why are some menu items missing descriptions or images?**
Not all restaurants provide complete menu data. Items with missing descriptions or images will simply not have those fields in the output.

**Is menu data available for all restaurants?**
Most restaurants support menus, but some (especially grocery stores) may have limited menu data.

## Legal notice

This actor extracts publicly visible data from Foodpanda's website. Use it responsibly and in accordance with Foodpanda's Terms of Service. Do not use scraped data for unauthorized commercial purposes. The actor does not bypass authentication, access private data, or perform any action that would harm Foodpanda's infrastructure.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/foodpanda-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
