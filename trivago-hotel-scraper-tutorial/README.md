# Trivago Hotel Scraper Tutorial: Run This Apify Actor with Python

Scrape hotel listings, prices, ratings, and deals from Trivago. Search by destination, compare OTA prices, and extract hotel details at scale

This repository shows how to run [Trivago Hotel Scraper](https://apify.com/crawlerbros/trivago-hotel-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/trivago-hotel-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/trivago-hotel-scraper](https://apify.com/crawlerbros/trivago-hotel-scraper)
- **SEO title:** Trivago Hotel Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape hotel listings, prices, ratings, and deals from Trivago. Search by destination, compare OTA prices, and extract hotel details at scale

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

# Trivago Hotel Scraper

Extract hotel listings, prices, ratings, and amenities from [Trivago](https://www.trivago.com) — the world's largest hotel price comparison platform. Search by destination, compare prices from 400+ booking sites, and collect rich hotel data at scale.

## What data does this scraper extract?

| Field | Description |
|-------|-------------|
| `hotelId` | Unique hotel identifier |
| `name` | Hotel name |
| `url` | Trivago hotel page URL |
| `imageUrl` | Hotel main image URL |
| `destination` | Search destination |
| `checkIn` | Check-in date |
| `checkOut` | Check-out date |
| `price` | Best available price (per night) |
| `currency` | Price currency (e.g., USD) |
| `rating` | Trivago rating (0–10 scale) |
| `reviewCount` | Number of reviews |
| `starRating` | Star category (1–5) |
| `address` | Hotel address |
| `latitude` | Geographical latitude |
| `longitude` | Geographical longitude |
| `amenities` | List of amenities (WiFi, pool, gym, etc.) |
| `providers` | OTA providers with their prices (Booking.com, Hotels.com, etc.) |
| `recordType` | Always "trivagoHotel" |
| `scrapedAt` | Timestamp of scraping |

## Input Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `mode` | Select | Scraping mode: searchHotels, byHotelUrls, topDeals | `searchHotels` |
| `destination` | Text | City or region to search (e.g., "New York", "Paris") | `New York` |
| `checkIn` | Text | Check-in date YYYY-MM-DD | Tomorrow |
| `checkOut` | Text | Check-out date YYYY-MM-DD | Day after check-in |
| `adults` | Integer | Number of adult guests (1–20) | `2` |
| `rooms` | Integer | Number of rooms (1–10) | `1` |
| `sortBy` | Select | Sort: relevance, price, rating, stars | `relevance` |
| `starRating` | Select | Minimum star rating: all, 1–5 | `all` |
| `startUrls` | List | Hotel URLs for byHotelUrls mode | — |
| `maxItems` | Integer | Maximum results (1–1000) | `50` |

## Modes

### `searchHotels` (default)
Search hotels by destination with date and guest filters. Returns a list of hotels matching your search criteria with prices from multiple booking providers.

### `byHotelUrls`
Enrich specific Trivago hotel URLs. Provide a list of Trivago hotel page URLs and extract detailed information for each.

### `topDeals`
Fetch currently featured hotel deals from popular destinations worldwide. Great for monitoring price trends.

## Example Input

```json
{
  "mode": "searchHotels",
  "destination": "New York",
  "checkIn": "2026-08-01",
  "checkOut": "2026-08-05",
  "adults": 2,
  "rooms": 1,
  "sortBy": "price",
  "starRating": "4",
  "maxItems": 50
}
```

## Example Output

```json
{
  "hotelId": "the-times-square-edition",
  "name": "The EDITION Times Square",
  "url": "https://www.trivago.com/en-US/odr/the-times-square-edition",
  "imageUrl": "https://cdn.trivago.com/hotels/times-square-edition.jpg",
  "destination": "New York",
  "checkIn": "2026-08-01",
  "checkOut": "2026-08-05",
  "price": 389.00,
  "currency": "USD",
  "rating": 9.1,
  "reviewCount": 4821,
  "starRating": 5,
  "address": "701 7th Avenue, New York, United States",
  "latitude": 40.7590,
  "longitude": -73.9845,
  "amenities": ["Free WiFi", "Pool", "Spa", "Gym", "Restaurant"],
  "providers": [
    {"name": "Booking.com", "price": 389.00},
    {"name": "Hotels.com", "price": 395.00},
    {"name": "Expedia", "price": 402.00}
  ],
  "recordType": "trivagoHotel",
  "scrapedAt": "2026-05-15T10:30:00+00:00"
}
```

## Frequently Asked Questions

**Q: Why am I getting 0 results for some destinations?**
A: Trivago uses Akamai bot protection on its search results API. For best results, configure a residential proxy in the `proxyConfiguration` input. Datacenter IPs may return empty results on the search API.

**Q: Which hotel booking sites does Trivago compare?**
A: Trivago compares prices from 400+ booking sites including Booking.com, Hotels.com, Expedia, Agoda, Priceline, and many more. The `providers` field in the output lists which OTAs offer the hotel and at what price.

**Q: How are prices represented?**
A: Prices are the best available rate found across all providers at the time of scraping. The `price` field shows the lowest price. The `providers` list shows all available prices per OTA.

**Q: Can I scrape multiple destinations in one run?**
A: For `topDeals` mode, the scraper automatically searches multiple popular destinations. For `searchHotels`, run the actor multiple times with different destination values.

**Q: What does the Trivago rating mean?**
A: Trivago's rating is on a 0–10 scale, aggregated from multiple review sources. Scores above 8.0 are considered "Good", above 9.0 "Superb".

**Q: Does this scraper support all countries?**
A: Yes, Trivago covers hotels worldwide. Use the destination field with any city or region name.

**Q: Can I filter by amenities?**
A: The scraper extracts amenity data as listed on Trivago. Use the `amenities` field in your downstream data pipeline to filter by specific amenities.

## Legal Notice

This scraper is intended for legitimate data collection purposes such as price monitoring, market research, and travel planning. Please comply with Trivago's Terms of Service and robots.txt when using this tool.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/trivago-hotel-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
