# Tripadvisor Scraper Tutorial: Run This Apify Actor with Python

Scrape hotels, restaurants, attractions, and vacation rentals from TripAdvisor. Search by keyword or provide direct URLs. Extract names, ratings, rankings, addresses, contact info, prices, and more. No login required.

This repository shows how to run [Tripadvisor Scraper](https://apify.com/crawlerbros/tripadvisor-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tripadvisor-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tripadvisor-scraper](https://apify.com/crawlerbros/tripadvisor-scraper)
- **SEO title:** Tripadvisor Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape hotels, restaurants, attractions, and vacation rentals from TripAdvisor. Search by keyword or provide direct URLs. Extract names, ratings, rankings, addresses, contact info, prices, and more. No login required.

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

# TripAdvisor Scraper

Extract structured data from TripAdvisor for hotels, restaurants, and attractions. Search by keyword or provide direct TripAdvisor URLs to get detailed place information including ratings, rankings, contact details, prices, and more. No login or API key required.

## What can this scraper do?

- **Search for places** — Find hotels, restaurants, and attractions by keyword (e.g. "hotels in Paris", "restaurants NYC")
- **Scrape direct URLs** — Extract data from specific TripAdvisor place pages
- **Filter by place type** — Limit results to hotels, restaurants, or attractions only
- **Extract rich metadata** — Get ratings, rankings, addresses, phone numbers, emails, websites, prices, operating hours, cuisine types, hotel star ratings, and more

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `searchQueries` | string[] | No | — | Search terms to find places on TripAdvisor |
| `startUrls` | string[] | No | — | Direct TripAdvisor place URLs |
| `maxItems` | integer | No | 50 | Maximum results per search query (1-100) |
| `placeType` | enum | No | `all` | Filter: `all`, `hotel`, `restaurant`, `attraction` |
| `proxyConfiguration` | object | No | — | Proxy settings (residential proxy recommended for search) |

At least one of `searchQueries` or `startUrls` is required.

### Example inputs

**Scrape specific places by URL (recommended — fastest, no proxy needed):**
```json
{
    "startUrls": [
        "https://www.tripadvisor.com/Hotel_Review-g60763-d675616-Reviews-The_Plaza_New_York-New_York_City_New_York.html",
        "https://www.tripadvisor.com/Restaurant_Review-g60763-d457808-Reviews-Daniel-New_York_City_New_York.html"
    ]
}
```

**Search for hotels (residential proxy recommended):**
```json
{
    "searchQueries": ["hotels in Paris"],
    "maxItems": 10,
    "placeType": "hotel",
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}
```

**Mixed search and URLs:**
```json
{
    "searchQueries": ["best restaurants London"],
    "startUrls": ["https://www.tripadvisor.com/Attraction_Review-g60763-d104365-Reviews-Empire_State_Building-New_York_City_New_York.html"],
    "maxItems": 15,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}
```

## Output

Each result contains structured place data. Fields vary by place type.

### Output fields

| Field | Description | Example |
|-------|-------------|---------|
| `locationId` | TripAdvisor location ID | `"675616"` |
| `name` | Place name | `"The Plaza New York"` |
| `type` | Place type | `"hotel"` |
| `subcategory` | Subcategory label | `"Hotel"` |
| `address` | Full address | `"5th Avenue, New York City, NY 10019"` |
| `street` | Street address | `"5th Avenue At Central Park South"` |
| `city` | City | `"New York City"` |
| `state` | State/province | `"NY"` |
| `country` | Country | `"United States"` |
| `postalCode` | ZIP/postal code | `"10019"` |
| `latitude` | Latitude | `"40.764645"` |
| `longitude` | Longitude | `"-73.97432"` |
| `rating` | Rating (0-5) | `"4.5"` |
| `numberOfReviews` | Total reviews | `"5309"` |
| `rankingPosition` | Rank number | `"20"` |
| `rankingString` | Full ranking text | `"#20 of 583 hotels in New York City"` |
| `priceLevel` | Price symbols | `"$$$$"` |
| `priceRange` | Price range | `"$1,207 - $2,096"` |
| `phone` | Phone number | `"0016466634630"` |
| `email` | Email address | `"theplaza@fairmont.com"` |
| `website` | Official website | `"https://www.theplazany.com/"` |
| `hotelClass` | Star rating (hotels) | `"5.0"` |
| `cuisine` | Cuisine types (restaurants) | `"French, European"` |
| `hours` | Operating hours | `"Tue - Sun: 5:00 PM - 9:30 PM"` |
| `description` | Place description | `"The Empire State Building is..."` |
| `neighborhoods` | Neighborhood names | `"Midtown, Manhattan"` |
| `webUrl` | TripAdvisor page URL | `"https://www.tripadvisor.com/..."` |
| `isClosed` | Permanently closed | `"False"` |
| `photoUrl` | Main photo URL | `"https://media-cdn.tripadvisor.com/..."` |
| `searchQuery` | Source search query | `"hotels in Paris"` |
| `scrapeTimestamp` | ISO timestamp | `"2026-03-10T12:00:00+00:00"` |

### Sample output

```json
{
    "locationId": "675616",
    "name": "The Plaza New York - A Fairmont Managed Hotel",
    "type": "hotel",
    "subcategory": "Hotel",
    "address": "5th Avenue At Central Park South, New York City, NY 10019",
    "street": "5th Avenue At Central Park South",
    "city": "New York City",
    "state": "NY",
    "country": "United States",
    "postalCode": "10019",
    "latitude": "40.764645",
    "longitude": "-73.97432",
    "rating": "4.5",
    "numberOfReviews": "5309",
    "rankingPosition": "20",
    "rankingString": "#20 of 583 hotels in New York City",
    "priceLevel": "$$$$",
    "priceRange": "$1,207 - $2,096",
    "phone": "0016466634630",
    "email": "theplaza@fairmont.com",
    "website": "https://www.theplazany.com/",
    "hotelClass": "5.0",
    "cuisine": "",
    "hours": "",
    "description": "",
    "neighborhoods": "Midtown, Midtown West, Manhattan",
    "webUrl": "https://www.tripadvisor.com/Hotel_Review-g60763-d675616-Reviews-The_Plaza...",
    "isClosed": "False",
    "photoUrl": "",
    "searchQuery": "hotels in New York",
    "scrapeTimestamp": "2026-03-10T12:00:00.000000+00:00"
}
```

## Frequently Asked Questions

**Do I need a TripAdvisor account or API key?**
No. This scraper uses TripAdvisor's public APIs and does not require any login credentials or API keys.

**Does it need a proxy?**
Direct URLs work without any proxy. For search queries, a residential proxy is recommended for best results because TripAdvisor uses anti-bot protection (DataDome) on search pages.

**How many results can I get per search?**
Each search query returns up to 15 matching places from TripAdvisor's search. Use direct URLs for specific places.

**Which fields are available for each place type?**
Some fields are type-specific: `hotelClass` is only populated for hotels, `cuisine` and `hours` only for restaurants, `description` appears for some attractions and locations. Core fields (name, address, rating, ranking, contact info) are available for all types.

**Can I scrape vacation rentals and tours?**
The search supports vacation rentals when using `placeType: "all"`. For specific vacation rentals or tours, provide their direct TripAdvisor URL.

**What URL formats are supported?**
Any TripAdvisor URL containing a location ID works, including:
- Hotel pages: `/Hotel_Review-g...-d...-Reviews-...`
- Restaurant pages: `/Restaurant_Review-g...-d...-Reviews-...`
- Attraction pages: `/Attraction_Review-g...-d...-Reviews-...`
- Vacation rental pages: `/VacationRentalReview-g...-d...-...`

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tripadvisor-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
