# Airbnb Scraper Tutorial: Run This Apify Actor with Python

Scrape Airbnb listings, prices, ratings, host info, coordinates and photos for any location. Extract vacation rental data including nightly rates, superhost status, property types and guest reviews.

This repository shows how to run [Airbnb Scraper](https://apify.com/crawlerbros/airbnb-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/airbnb-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/airbnb-scraper](https://apify.com/crawlerbros/airbnb-scraper)
- **SEO title:** Airbnb Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Airbnb listings, prices, ratings, host info, coordinates and photos for any location. Extract vacation rental data including nightly rates, superhost status, property types and guest reviews.

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

# Airbnb Scraper

Scrape Airbnb listings for any location worldwide. Extract property names, prices, ratings, host information, GPS coordinates, and photos from Airbnb search results.

## What can this scraper do?

- **Search any location** -- Enter a city, neighborhood, or region to find available Airbnb listings
- **Extract pricing** -- Get current prices, original prices, and price qualifiers (e.g., "for 5 nights")
- **Ratings and reviews** -- Collect average ratings and review counts for each listing
- **Host details** -- Identify Superhost status, verified hosts, and host profile photos
- **GPS coordinates** -- Get precise latitude and longitude for every listing
- **Property photos** -- Extract up to 10 listing photo URLs per property
- **Date-specific search** -- Set check-in/check-out dates and guest count for accurate pricing
- **No browser needed** -- Fast HTTP-based scraping without Playwright or browser overhead

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `location` | string | Yes | — | Location to search (e.g., "New York", "Paris, France", "Tokyo") |
| `checkIn` | string | No | — | Check-in date in YYYY-MM-DD format |
| `checkOut` | string | No | — | Check-out date in YYYY-MM-DD format |
| `adults` | integer | No | 1 | Number of adult guests (1-16) |
| `maxItems` | integer | No | 20 | Maximum number of listings to return (1-100) |
| `proxy` | object | No | — | Proxy configuration for avoiding rate limits |

### Example input

```json
{
    "location": "New York",
    "maxItems": 10
}
```

```json
{
    "location": "Paris, France",
    "checkIn": "2025-07-01",
    "checkOut": "2025-07-05",
    "adults": 2,
    "maxItems": 18
}
```

## Output

### Listing fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique Airbnb listing ID |
| `url` | string | Direct link to the listing page |
| `name` | string | Property name |
| `type` | string | Property type and location (e.g., "Hotel in New York") |
| `subtitle` | string | Short description snippet |
| `price` | string | Current displayed price (e.g., "$722") |
| `originalPrice` | string | Original price before discount, if applicable |
| `priceQualifier` | string | Price context (e.g., "for 5 nights", "per night") |
| `rating` | string | Average rating with review count (e.g., "4.68 (4274)") |
| `isSuperhost` | boolean | Whether the host has Superhost status |
| `isVerified` | boolean | Whether the host is verified |
| `hostPhoto` | string | URL of the host's profile photo |
| `latitude` | number | GPS latitude coordinate |
| `longitude` | number | GPS longitude coordinate |
| `photos` | array | Up to 10 listing photo URLs |
| `searchUrl` | string | The Airbnb search URL used |
| `scrapedAt` | string | ISO 8601 timestamp of when the data was scraped |

### Sample output

```json
{
    "id": "12345678",
    "url": "https://www.airbnb.com/rooms/12345678",
    "name": "Cozy Studio in Midtown Manhattan",
    "type": "Room in New York",
    "subtitle": "Stay Near NYC Icons and Top-Rated Attractions",
    "price": "$150",
    "originalPrice": "$180",
    "priceQualifier": "per night",
    "rating": "4.85 (312)",
    "isSuperhost": true,
    "isVerified": true,
    "hostPhoto": "https://a0.muscache.com/im/pictures/user/...",
    "latitude": 40.7549,
    "longitude": -73.9840,
    "photos": [
        "https://a0.muscache.com/im/pictures/...",
        "https://a0.muscache.com/im/pictures/..."
    ],
    "searchUrl": "https://www.airbnb.com/s/New-York/homes",
    "scrapedAt": "2025-06-01T12:00:00.000000+00:00"
}
```

## Use cases

- **Market research** -- Analyze Airbnb pricing trends across different neighborhoods and cities
- **Competitive analysis** -- Compare property types, prices, and ratings in a target area
- **Travel planning** -- Find the best-rated and most affordable listings for your trip
- **Real estate insights** -- Identify popular short-term rental areas using GPS coordinates
- **Price monitoring** -- Track pricing changes for specific locations over time
- **Data journalism** -- Collect rental market data for reporting and analysis

## Tips

- **Proxy recommended** -- For consistent results, use a residential proxy to avoid rate limiting
- **Date-specific pricing** -- Set check-in and check-out dates to get accurate total prices instead of per-night estimates
- **Results per page** -- Airbnb returns up to 18 listings per search page
- **Location format** -- Use common location names. The scraper handles URL encoding automatically

## FAQ

**How many listings can I scrape?**
Each search page returns up to 18 listings. Set `maxItems` to control how many you want (max 100).

**Do I need to set check-in and check-out dates?**
No. Without dates, Airbnb shows general pricing. With dates, you get exact total prices for your stay.

**What proxy should I use?**
Residential proxies work best. Datacenter proxies may be blocked by Airbnb. You can also try without a proxy first.

**Why are some fields empty?**
Not all listings have discounted prices, subtitles, or host photos. Empty strings are returned instead of null values.

**Does this scraper need login credentials?**
No. The scraper uses public Airbnb search pages that don't require authentication.

**What locations are supported?**
Any location that Airbnb supports -- cities, neighborhoods, regions, countries, and specific addresses worldwide.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/airbnb-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
