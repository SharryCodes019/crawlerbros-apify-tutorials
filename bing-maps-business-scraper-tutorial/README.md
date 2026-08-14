# Bing Maps Business Listings Scraper Tutorial: Run This Apify Actor with Python

Scrape business listings from Bing Maps. Search for restaurants, shops, hotels, and services by name and location. Returns name, address, phone, website, rating, review count, coordinates, and more

This repository shows how to run [Bing Maps Business Listings Scraper](https://apify.com/crawlerbros/bing-maps-business-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bing-maps-business-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bing-maps-business-scraper](https://apify.com/crawlerbros/bing-maps-business-scraper)
- **SEO title:** Bing Maps Business Listings Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape business listings from Bing Maps. Search for restaurants, shops, hotels, and services by name and location. Returns name, address, phone, website, rating, review count, coordinates, and more

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

# Bing Maps Business Listings Scraper

Extract business listings from **Bing Maps** using Playwright browser automation. Search for restaurants, coffee shops, hotels, dentists, or any local business by keyword and location.

> **Note on Bing Maps API:** The official Bing Maps Local Search REST API was retired by Microsoft on August 11, 2025. This actor scrapes the Bing Maps website directly, which continues to serve comprehensive business listing data.

## Features

- Search businesses by **keyword** (e.g. "coffee shops", "Italian restaurant", "dentist")
- Filter by **location** (city, area, or full address)
- Returns: name, category, address, phone, website, rating, review count, coordinates, opening hours
- Automatic pagination to collect more results
- JSON-LD structured data extraction for richer results
- Apify Proxy AUTO group support to avoid rate limits

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | select | `search` (keyword + location) or `nearbySearch` |
| `searchQuery` | string | Business type to search (e.g. "coffee shops") |
| `location` | string | City or area (e.g. "London", "Paris, France") |
| `maxItems` | integer | Max results to return (1–200, default 20) |
| `proxyConfiguration` | proxy | Proxy settings (recommended: Apify AUTO) |

## Output

| Field | Description |
|---|---|
| `name` | Business name |
| `category` | Business category (e.g. "Coffee Shop") |
| `address` | Full address |
| `phone` | Phone number |
| `website` | Business website |
| `rating` | Rating (0–5) |
| `reviewCount` | Number of reviews |
| `lat` | Latitude |
| `lon` | Longitude |
| `openingHours` | Opening hours |
| `priceLevel` | Price level |
| `thumbnailUrl` | Business photo URL |
| `url` | Bing Maps listing URL |
| `scrapedAt` | ISO 8601 timestamp |

## Example Input

```json
{
  "mode": "search",
  "searchQuery": "coffee shops",
  "location": "London",
  "maxItems": 10,
  "proxyConfiguration": {"useApifyProxy": true}
}
```

## Example Output

```json
{
  "name": "The Coffee House",
  "category": "Coffee Shop",
  "address": "123 Oxford Street, London W1D 1BS",
  "phone": "+44 20 7946 0000",
  "website": "https://www.thecoffeehouse.co.uk",
  "rating": 4.5,
  "reviewCount": 1234,
  "lat": 51.5074,
  "lon": -0.1278,
  "openingHours": "Mo-Su 07:00-22:00",
  "url": "https://www.bing.com/maps?q=coffee+house+london",
  "recordType": "business",
  "scrapedAt": "2026-05-22T10:00:00+00:00"
}
```

## FAQ

**Why use this instead of the Bing Maps API?** Microsoft retired the Bing Maps Local Search API in August 2025. This actor scrapes the Bing Maps website which still provides full business listing data.

**Do I need a Bing account?** No. Bing Maps search results are publicly accessible.

**How many results can I get?** Up to 200 per run. Bing Maps typically shows 10–20 results per page.

**Will it get blocked?** We recommend enabling Apify Proxy (AUTO group) for best results.

**What data sources does Bing Maps use?** Bing Maps aggregates data from multiple sources including Yelp, TripAdvisor, and its own local business database.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bing-maps-business-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
