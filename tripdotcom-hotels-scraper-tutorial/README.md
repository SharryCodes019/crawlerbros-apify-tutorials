# Trip.com Hotels Scraper Tutorial: Run This Apify Actor with Python

Scrape hotel listings from Trip.com. Search hotels by city and date, with filters for star rating, guest score, and price. Returns hotel name, address, star rating, guest score, price per night, amenities, and booking URL

This repository shows how to run [Trip.com Hotels Scraper](https://apify.com/crawlerbros/tripdotcom-hotels-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tripdotcom-hotels-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tripdotcom-hotels-scraper](https://apify.com/crawlerbros/tripdotcom-hotels-scraper)
- **SEO title:** Trip.com Hotels Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape hotel listings from Trip.com. Search hotels by city and date, with filters for star rating, guest score, and price. Returns hotel name, address, star rating, guest score, price per night, amenities, and booking URL

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

# Trip.com Hotels Scraper

Scrape hotel listings from **Trip.com** — one of the world's largest online travel platforms. Search for hotels by city and travel dates, with filters for star rating, guest score, and price.

## Features

- Search hotels by **city name** and **travel dates**
- Filter by **star rating** (1–5 stars)
- Filter by **minimum guest score** (0–10 scale)
- Filter by **maximum price per night**
- Returns: hotel name, address, star rating, guest score, review count, price, amenities, URL, thumbnail
- Automatic API interception for fast, structured data extraction
- Apify Proxy support for reliable access

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | select | `searchHotels` (search by city) |
| `cityName` | string | City to search (e.g. "London", "Tokyo", "Paris") |
| `checkIn` | string | Check-in date (YYYY-MM-DD). Defaults to tomorrow. |
| `checkOut` | string | Check-out date (YYYY-MM-DD). Defaults to day after check-in. |
| `minStars` | select | Minimum star rating (1–5) |
| `minRating` | number | Minimum guest score (0–10) |
| `maxPrice` | number | Maximum price per night (USD) |
| `maxItems` | integer | Max hotels to return (1–200, default 20) |
| `proxyConfiguration` | proxy | Proxy settings (recommended: Apify AUTO) |

## Output

| Field | Description |
|---|---|
| `hotelId` | Trip.com hotel ID |
| `name` | Hotel name |
| `address` | Full address |
| `starRating` | Star rating (1–5) |
| `rating` | Guest score (0–10, e.g. 8.9 = "Excellent") |
| `reviewCount` | Number of guest reviews |
| `pricePerNight` | Price per night (in `currency`) |
| `currency` | Currency code (e.g. USD) |
| `amenities` | Array of amenity names |
| `url` | Trip.com hotel booking URL |
| `thumbnailUrl` | Hotel photo URL |
| `lat` | Latitude |
| `lon` | Longitude |
| `checkIn` | Check-in date used in search |
| `checkOut` | Check-out date used in search |
| `city` | City searched |
| `scrapedAt` | ISO 8601 timestamp |

## Example Input

```json
{
  "mode": "searchHotels",
  "cityName": "London",
  "maxItems": 5,
  "proxyConfiguration": {"useApifyProxy": true}
}
```

## Example Output

```json
{
  "hotelId": "12345",
  "name": "The Grand Hotel London",
  "address": "123 Strand, London WC2R 1HB",
  "starRating": 5,
  "rating": 8.9,
  "reviewCount": 1200,
  "pricePerNight": 250.0,
  "currency": "USD",
  "amenities": ["Free WiFi", "Pool", "Gym", "Restaurant", "Spa"],
  "url": "https://www.trip.com/hotels/detail/?hotelId=12345",
  "thumbnailUrl": "https://cdn.trip.com/hotel12345.jpg",
  "checkIn": "2026-05-23",
  "checkOut": "2026-05-24",
  "city": "London",
  "recordType": "hotel",
  "scrapedAt": "2026-05-22T10:00:00+00:00"
}
```

## Supported Regions

Trip.com's hotel search works best for the following regions:

- **Europe**: London, Paris, Amsterdam, Barcelona, Rome, Berlin, Prague, Vienna, Istanbul, and more
- **Asia**: Tokyo, Bangkok, Singapore, Dubai, Hong Kong, Seoul, Bali, Kuala Lumpur, and more
- **Middle East**: Dubai, Abu Dhabi, Riyadh, Doha, and more
- **Oceania**: Sydney, Melbourne, Auckland, and more

> **Note:** US and North American cities (New York, Los Angeles, Chicago, etc.) are **not supported**. Trip.com serves these markets via a different Next.js frontend that does not embed the hotel listing data in a format this actor can extract. Use a European or Asian destination instead.

## FAQ

**Do I need a Trip.com account?** No. Hotel search results are publicly accessible.

**What currency are prices shown in?** USD by default. Prices reflect the Trip.com listed price for the selected dates.

**Why do I need proxy?** Trip.com may rate-limit or block datacenter IPs. The Apify AUTO proxy group provides varied IP addresses for reliable access.

**What if no dates are provided?** The actor defaults to tomorrow and the next day, ensuring valid date-based pricing.

**How many hotels per city?** Trip.com typically lists 20–50 hotels per page. With pagination, you can collect up to 200 per run.

**Why does New York / US city return 0 results?** Trip.com migrated US and North American markets to a different frontend that does not expose hotel data in the format this actor reads. Try a European or Asian city instead.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tripdotcom-hotels-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
