# Expedia Hotels Scraper Tutorial: Run This Apify Actor with Python

Scrape hotel listings from Expedia search results. Extract hotel names, prices, ratings, reviews, neighborhoods, descriptions and images for any destination and travel dates.

This repository shows how to run [Expedia Hotels Scraper](https://apify.com/crawlerbros/expedia-hotels-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/expedia-hotels-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/expedia-hotels-scraper](https://apify.com/crawlerbros/expedia-hotels-scraper)
- **SEO title:** Expedia Hotels Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape hotel listings from Expedia search results. Extract hotel names, prices, ratings, reviews, neighborhoods, descriptions and images for any destination and travel dates.

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

# Expedia Hotels Scraper

Scrape hotel listings from Expedia search results for any destination worldwide. Extract hotel names, nightly prices, guest ratings, review counts, neighborhoods, descriptions, images, and special offers like VIP Access or free breakfast.

## What can this scraper do?

- **Search any destination** -- Enter a city, neighborhood, or region to find available hotels on Expedia
- **Extract hotel pricing** -- Get current nightly rates as displayed on Expedia search results
- **Ratings and reviews** -- Collect guest ratings (out of 10) and total review counts
- **Neighborhood info** -- See which area or district each hotel is located in
- **Hotel descriptions** -- Get the short description or tagline shown in search results
- **Property images** -- Extract the main listing image URL for each hotel
- **Special offers and badges** -- Capture VIP Access, breakfast included, free cancellation, and other promotions
- **Date-specific search** -- Set check-in/check-out dates and guest count for accurate pricing and availability
- **Direct hotel links** -- Get direct Expedia URLs for each hotel's information page

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `destination` | string | Yes | -- | Destination city or area (e.g., "New York", "London", "Tokyo, Japan") |
| `checkIn` | string | Yes | -- | Check-in date in YYYY-MM-DD format (e.g., "2026-06-01") |
| `checkOut` | string | Yes | -- | Check-out date in YYYY-MM-DD format (e.g., "2026-06-03") |
| `adults` | integer | No | 2 | Number of adult guests (1-10) |
| `rooms` | integer | No | 1 | Number of rooms (1-5) |
| `maxItems` | integer | No | 20 | Maximum number of hotels to scrape |
| `proxy` | object | No | -- | Proxy configuration. Residential proxy recommended for datacenter IPs |

### Example input

```json
{
    "destination": "New York",
    "checkIn": "2026-06-01",
    "checkOut": "2026-06-03",
    "adults": 2,
    "maxItems": 10
}
```

```json
{
    "destination": "Paris, France",
    "checkIn": "2026-07-15",
    "checkOut": "2026-07-20",
    "adults": 2,
    "rooms": 1,
    "maxItems": 30
}
```

## Output

### Hotel fields

| Field | Type | Description |
|-------|------|-------------|
| `hotelId` | string | Unique Expedia hotel identifier |
| `name` | string | Hotel name |
| `url` | string | Direct link to the hotel page on Expedia |
| `price` | string | Nightly price as displayed (e.g., "$671 nightly") |
| `totalPrice` | string | Total price with taxes and fees (e.g., "$1,639 total") |
| `rating` | string | Guest rating out of 10 (e.g., "9.2") |
| `ratingText` | string | Rating descriptor (e.g., "Wonderful", "Excellent") |
| `reviewCount` | string | Total number of guest reviews |
| `neighborhood` | string | Hotel neighborhood or area (e.g., "Theater District") |
| `description` | string | Short description or tagline from the listing |
| `imageUrl` | string | URL of the hotel's main listing image |
| `badges` | array | Special offers and badges (e.g., "VIP Access", "Breakfast included") |
| `destination` | string | The search destination used |
| `checkIn` | string | Check-in date used for the search |
| `checkOut` | string | Check-out date used for the search |
| `searchUrl` | string | Full Expedia search URL used |
| `scrapedAt` | string | ISO 8601 timestamp of when the data was scraped |

### Sample output

```json
{
    "hotelId": "1234567",
    "name": "The Ritz-Carlton New York, Times Square",
    "url": "https://www.expedia.com/New-York-Hotels-The-Ritz-Carlton.h1234567.Hotel-Information",
    "price": "$671 nightly",
    "totalPrice": "$1,639 total",
    "rating": "9.2",
    "ratingText": "Wonderful",
    "reviewCount": "2847",
    "neighborhood": "Theater District",
    "description": "Upscale hotel with panoramic city views, a luxury spa, and fine dining in the heart of Times Square.",
    "imageUrl": "https://images.trvl-media.com/lodging/1234567/...",
    "badges": ["VIP Access", "Breakfast included"],
    "destination": "New York",
    "checkIn": "2026-06-01",
    "checkOut": "2026-06-03",
    "searchUrl": "https://www.expedia.com/Hotel-Search?destination=New+York&startDate=2026-06-01&endDate=2026-06-03&rooms=1&adults=2",
    "scrapedAt": "2026-04-07T12:00:00.000000+00:00"
}
```

## Use cases

- **Travel planning** -- Compare hotel prices, ratings, and locations before booking your trip
- **Price monitoring** -- Track hotel price changes across dates and destinations over time
- **Market research** -- Analyze hotel pricing trends and competitive positioning in specific markets
- **Competitive analysis** -- Compare hotels by rating, price range, and neighborhood within a city
- **Travel aggregation** -- Build hotel comparison tools or travel recommendation engines
- **Data journalism** -- Collect hospitality market data for reporting and analysis

## Tips

- **Residential proxy recommended** -- For the most reliable results from datacenter environments, use a residential proxy. The scraper may work without proxy from residential IPs
- **Check-in and check-out required** -- Expedia requires dates to show hotel search results with pricing
- **Results per load** -- Expedia loads 3-10 hotel cards at a time. The scraper scrolls to load more, up to your `maxItems` limit
- **Destination format** -- Use common location names like "New York", "London, UK", or "Tokyo, Japan". The scraper handles URL encoding automatically

## FAQ

**How many hotels can I scrape?**
Expedia loads hotels progressively as you scroll. The scraper scrolls up to 8 times to load more results. Typical yields are 20-50 hotels per search, depending on the destination.

**Do I need login credentials?**
No. The scraper uses public Expedia hotel search pages that don't require authentication.

**Why do I need check-in and check-out dates?**
Expedia requires travel dates to display hotel search results with pricing. Without dates, the search may not return results.

**What proxy should I use?**
Residential proxies work best. Datacenter IPs may be blocked by Expedia's bot detection. Try without a proxy first if running locally.

**Why are some fields empty?**
Not all hotel cards display every field. For example, some hotels may not show a neighborhood, description, or rating. Empty strings are returned instead of null values.

**What destinations are supported?**
Any destination that Expedia supports -- cities, regions, neighborhoods, airports, and landmarks worldwide.

**How does the scraper handle bot detection?**
The scraper uses Patchright (an undetected browser automation library) with `headless=False` to bypass Expedia's PerimeterX bot detection.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/expedia-hotels-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
