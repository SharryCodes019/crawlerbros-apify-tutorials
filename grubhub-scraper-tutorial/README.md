# Grubhub Restaurant Scraper Tutorial: Run This Apify Actor with Python

Scrape Grubhub restaurant listings and menus. Search by address, fetch a single restaurant with full menu, or scrape from a Grubhub restaurant URL. Extracts ratings, delivery info, cuisine types, and menu items.

This repository shows how to run [Grubhub Restaurant Scraper](https://apify.com/crawlerbros/grubhub-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/grubhub-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/grubhub-scraper](https://apify.com/crawlerbros/grubhub-scraper)
- **SEO title:** Grubhub Restaurant Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Grubhub restaurant listings and menus. Search by address, fetch a single restaurant with full menu, or scrape from a Grubhub restaurant URL. Extracts ratings, delivery info, cuisine types, and menu items.

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

# Grubhub Restaurant Scraper

Scrape Grubhub restaurant listings and menus. Search by address or city to find nearby restaurants, fetch a single restaurant with its full menu, or scrape from a Grubhub URL. Extracts ratings, delivery info, cuisine types, menu items, and more.

## What data can you scrape?

- **Search restaurants** — find restaurants near any US address or city with cuisine and rating filters
- **Single restaurant + menu** — full restaurant details plus all menu items with prices
- **From URL** — paste any Grubhub restaurant URL to scrape its data and menu

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | select | `search`, `byRestaurantId`, or `byUrl` |
| `address` | string | Address or city for search (e.g. "New York, NY") |
| `cuisine` | select | Cuisine filter (American, Italian, Chinese, etc.) |
| `sortBy` | select | Sort: default, rating, delivery_time, minimum_order_amount |
| `openNow` | boolean | Only open restaurants (default: true) |
| `minRating` | float | Minimum rating 0-5 |
| `maxDeliveryTime` | integer | Max estimated delivery time in minutes |
| `restaurantId` | string | Restaurant ID for byRestaurantId mode |
| `url` | string | Grubhub URL for byUrl mode |
| `maxItems` | integer | Max records to emit (default: 50) |

## Output — Restaurant record

```json
{
  "restaurantId": "987654",
  "name": "The Great Burger Joint",
  "slug": "great-burger-joint",
  "cuisines": ["American", "Burgers"],
  "categories": ["Fast Food"],
  "rating": 4.7,
  "ratingCount": 1250,
  "deliveryFee": 1.99,
  "deliveryTime": 35,
  "minimumOrder": 10.00,
  "address": "456 Burger Ave, New York, NY",
  "city": "New York",
  "state": "NY",
  "zip": "10002",
  "phone": "+12125551234",
  "isOpen": true,
  "acceptsPickup": true,
  "acceptsDelivery": true,
  "promoText": "Free delivery on orders over $15",
  "imageUrl": "https://res.cloudinary.com/grubhub/...",
  "restaurantUrl": "https://www.grubhub.com/restaurant/great-burger-joint/987654",
  "recordType": "restaurant",
  "siteName": "Grubhub",
  "scrapedAt": "2026-05-10T12:00:00+00:00"
}
```

## Output — Menu item record (byRestaurantId mode)

```json
{
  "itemId": "item_001",
  "name": "Classic Cheeseburger",
  "description": "A juicy beef patty with melted cheese",
  "price": 12.99,
  "calories": 650,
  "categoryName": "Burgers",
  "imageUrl": "https://res.cloudinary.com/grubhub/...",
  "recordType": "menuItem",
  "siteName": "Grubhub",
  "scrapedAt": "2026-05-10T12:00:00+00:00"
}
```

## FAQs

**Do I need a Grubhub account?**
No account is required, but anonymous search access is session- and geo-sensitive. Direct restaurant lookups via `byRestaurantId` or `byUrl` are the most reliable modes.

**Which cities are supported?**
Grubhub operates in the US. Provide a US address or city for search mode, and use a US residential proxy for the best chance of success.

**Does byRestaurantId return menu items?**
Yes. When using `byRestaurantId` or `byUrl`, both the restaurant record and all menu items are emitted.

**What should I use for scheduled smoke tests?**
Use `byRestaurantId` with a known restaurant. `byUrl` usually works too, but direct restaurant IDs are the most stable choice for monitoring. Search mode depends on Grubhub's current anonymous geolocation/session gating and is best treated as best-effort.

**How many restaurants can I scrape?**
Set `maxItems` up to 1000. Pagination is handled automatically.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/grubhub-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
