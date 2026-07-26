# Booking.com Hotel Scraper Tutorial: Run This Apify Actor with Python

Comprehensive scraper for Booking.com hotel listings. Extract prices, ratings, reviews, amenities, breakfast info, and more.

This repository shows how to run [Booking.com Hotel Scraper](https://apify.com/crawlerbros/booking-hotel-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/booking-hotel-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/booking-hotel-scraper](https://apify.com/crawlerbros/booking-hotel-scraper)
- **SEO title:** Booking.com Hotel Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Comprehensive scraper for Booking.com hotel listings. Extract prices, ratings, reviews, amenities, breakfast info, and more.

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

# Booking.com Hotel Scraper

Comprehensive scraper for Booking.com hotel listings. Extract detailed hotel data including prices, ratings, amenities, cancellation policies, breakfast info, and more.

## What does it do?

This scraper searches Booking.com for accommodations and extracts rich listing data including pricing, guest ratings, amenities, cancellation policies, and breakfast availability. Filter by property type and minimum rating.

## Features

- Search any destination worldwide
- Filter by property type (hotels, apartments, hostels, villas, resorts, etc.)
- Filter by minimum guest rating
- Extract amenities, cancellation policy, and breakfast info
- Detect original/discounted prices
- Customize dates, guests, rooms, and currency
- Automatic retry with fresh sessions on blocking

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| location | string | Yes | — | City or destination |
| checkinDate | string | No | Tomorrow | Check-in date (YYYY-MM-DD) |
| checkoutDate | string | No | Tomorrow + 3 days | Check-out date (YYYY-MM-DD) |
| adults | integer | No | 2 | Number of adults |
| rooms | integer | No | 1 | Number of rooms |
| currency | string | No | USD | Currency for prices |
| propertyType | string | No | all | Filter: all, hotels, apartments, hostels, etc. |
| minRating | number | No | 0 | Minimum guest rating (0-10) |
| maxResults | integer | No | 50 | Maximum hotels to return |
| proxyConfiguration | object | Yes | Residential | Proxy settings |

## Output

| Field | Type | Description |
|-------|------|-------------|
| name | string | Hotel name |
| url | string | Direct Booking.com link |
| price | number | Nightly price |
| currency | string | Price currency symbol |
| originalPrice | number | Original price before discount (0 if no discount) |
| rating | number | Guest rating (0-10) |
| reviewCount | integer | Number of reviews |
| reviewWord | string | Rating label (e.g., "Excellent") |
| stars | integer | Star rating (0-5) |
| propertyType | string | Hotel, Apartment, Hostel, etc. |
| address | string | Location/district |
| city | string | City name |
| distance | string | Distance from downtown |
| amenities | array | List of amenities (WiFi, Parking, Pool, etc.) |
| freeCancellation | boolean | Whether free cancellation is offered |
| breakfastIncluded | boolean | Whether breakfast is included |
| latitude | number | GPS latitude (when available) |
| longitude | number | GPS longitude (when available) |
| photoUrl | string | Main photo URL |
| checkin | string | Check-in date |
| checkout | string | Check-out date |
| scrapedAt | string | Extraction timestamp |

## FAQ

**Does it require a Booking.com account?**
No. All data is extracted from public search results.

**Why is residential proxy required?**
Booking.com uses Akamai Bot Manager which blocks datacenter IPs.

**What property types can I filter?**
Hotels, Apartments, Hostels, Guest houses, Villas, Resorts, or all types.

**How accurate are the prices?**
Prices reflect what Booking.com shows for the specified dates and guest count. They may vary based on availability.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/booking-hotel-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
