# Vrbo Vacation Rentals Tutorial: Run This Apify Actor with Python

Scrape Vrbo vacation-rental listings by destination and dates. Extract property names, nightly/total prices, ratings, reviews, bedrooms, bathrooms, amenities, host info and images.

This repository shows how to run [Vrbo Vacation Rentals](https://apify.com/crawlerbros/vrbo-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/vrbo-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/vrbo-scraper](https://apify.com/crawlerbros/vrbo-scraper)
- **SEO title:** Vrbo Vacation Rentals Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Vrbo vacation-rental listings by destination and dates. Extract property names, nightly/total prices, ratings, reviews, bedrooms, bathrooms, amenities, host info and images.

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

# Vrbo Vacation Rentals Scraper

Extract vacation-rental listings from [Vrbo](https://www.vrbo.com/) (Expedia Group) by destination and travel dates. Pulls property details, nightly/total pricing, guest ratings, review counts, bedrooms/bathrooms, amenities, host info, and images — using an automated Chromium browser that bypasses Vrbo's Akamai bot protection.

## What you get

- Property ID, name, full Vrbo URL
- Nightly price, total stay price, strikethrough original price + inferred currency
- Number of nights and whether taxes/fees are included in the total
- Discount percentage and distance-from-landmark text (when shown on the card)
- Guest rating (0-10 scale) and review count
- Bedrooms, bathrooms (may be fractional), sleeps
- Property type (Condo, Villa, House, Cabin, etc.)
- Neighborhood / location breakdown
- Latitude and longitude (only when the Apollo fallback path engages)
- Up to 20 image URLs per property
- Amenity badges and detected feature keywords (Pool, Wifi, Kitchen, etc.)
- Listing flags (Premier Host, Guest Favorite, Rare Find, Free Cancellation, etc.)
- Premier-host flag and instant-book flag
- Urgency / scarcity messages ("In high demand", "Only 1 left")
- Cancellation policy label
- Host name (only when the Apollo fallback path engages)
- Search context (destination, check-in, check-out) + scrape timestamp

## Input

| Field | Type | Description |
|---|---|---|
| `destination` | string | City, region, or area (e.g., `"Orlando, FL"`, `"Paris, France"`). **Required.** |
| `checkIn` | string | Check-in date `YYYY-MM-DD`. Optional — past/blank dates auto-roll to today + 30 days. |
| `checkOut` | string | Check-out date `YYYY-MM-DD`. Optional — defaults to check-in + 2 days. |
| `adults` | integer | Number of adult guests (1–16). Default `2`. |
| `children` | integer | Number of child guests (0–20). Default `0`. Affects pricing and availability. |
| `maxItems` | integer | Max number of properties to return (1–500). Default `3`. |

### Example input

```json
{
    "destination": "Orlando, FL",
    "checkIn": "2026-06-15",
    "checkOut": "2026-06-17",
    "adults": 2,
    "children": 0,
    "maxItems": 10
}
```

## Output

Each dataset item is a flat JSON object with the property fields listed above. Fields that Vrbo does not render on a given card are omitted (never `null`). Example:

```json
{
    "type": "vrbo_property",
    "propertyId": "1234567",
    "name": "3BR Disney Villa with Pool",
    "url": "https://www.vrbo.com/1234567",
    "price": "$189",
    "totalPrice": "$452 for 2 nights",
    "originalPrice": "$229",
    "currency": "USD",
    "nights": 2,
    "totalIncludesTaxes": true,
    "discountPercent": 17,
    "distance": "19.93 mi from Orlando",
    "rating": "9.4",
    "reviewCount": "312",
    "bedrooms": 3,
    "bathrooms": 2.0,
    "sleeps": 8,
    "propertyType": "Villa",
    "location": {"neighborhood": "Kissimmee"},
    "images": ["https://odis.homeaway.com/odis/listing/..."],
    "amenities": ["Pool", "Free cancellation"],
    "propertyFeatures": ["Pool", "Kitchen", "Wifi"],
    "listingFlags": ["Premier Host", "Guest Favorite", "Free Cancellation"],
    "hostIsSuperhost": true,
    "isInstantBook": true,
    "urgencyMessage": "In high demand",
    "cancellationPolicy": "Free cancellation before May 30",
    "destination": "Orlando, FL",
    "checkIn": "2026-06-15",
    "checkOut": "2026-06-17",
    "scrapedAt": "2026-04-20T12:34:56Z"
}
```

`hostName`, `latitude`, and `longitude` only appear when the Apollo state fallback path engages (rare); the primary DOM extraction path does not surface them.

If Vrbo blocks the run or returns no listings for the search, the dataset contains a single diagnostic item:

```json
{
    "type": "vrbo_blocked",
    "reason": "upstream_error",
    "message": "Vrbo returned no listings.",
    "destination": "...",
    "checkIn": "...",
    "checkOut": "...",
    "scrapedAt": "..."
}
```

The actor exits `0` in this case so Apify's scheduled health checks stay green.

## FAQ

**Do I need a proxy?**
Yes. A US Residential proxy is required. Vrbo is protected by Akamai Bot Manager, which reliably blocks datacenter IP ranges. The actor enforces Apify's `RESIDENTIAL` group with country `US` — enable "Use Apify Proxy" with those settings (the default prefill already does this). Residential proxy groups require a paid Apify plan.

**Does it need login or cookies?**
No. Vrbo search results are publicly accessible without authentication.

**How fresh is the pricing?**
Pricing is rendered live by Vrbo's website at the time of the request, reflecting the same availability and totals shown to a logged-out visitor.

**Can I scrape a single property page?**
This actor targets search results. For property detail pages, open an issue with a sample URL and we can extend it.

**What about filters — property type, price range, amenities?**
Not in v1. Filter pills can be exposed on request.

**Why was my date prefill rewritten?**
Vrbo rejects past check-in dates. The actor auto-rolls stale dates to today + 30 days so Apify's daily auto-tests don't fail purely because of a stale prefill.

## Legal

This actor scrapes publicly available search results. Respect Vrbo's Terms of Service and the volume of requests you send.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/vrbo-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
