# Yelp Scraper Pro Tutorial: Run This Apify Actor with Python

Fast Yelp business scraper with hours, menu, services, photo categories, owner replies, and coordinates.

This repository shows how to run [Yelp Scraper Pro](https://apify.com/crawlerbros/yelp-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/yelp-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/yelp-scraper-pro](https://apify.com/crawlerbros/yelp-scraper-pro)
- **SEO title:** Yelp Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Fast Yelp business scraper with hours, menu, services, photo categories, owner replies, and coordinates.

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

# Yelp Scraper Pro

Fast, HTTP-based Yelp business scraper with richer data than browser-based tools. Extract business details, customer reviews, hours of operation, services & amenities, photo galleries by category, menu items, claim status, owner replies, and geographic coordinates from any Yelp business page or search result.

Built for speed: no browser, no JavaScript rendering, no wasted compute. Ideal for lead generation, competitive analysis, market research, and review monitoring at scale.

## Why Yelp Scraper Pro?

- Significantly faster than browser-based Yelp scrapers — pure HTTP extraction
- Richer output: hours, services, photos by category, owner replies, coordinates, claim status, menu (restaurants)
- Clean output — fields are omitted when data is unavailable, no null placeholders
- Robust session and proxy rotation for Cloudflare-protected pages
- No login, no cookies required — only public data is collected

## Features

- Search Yelp by keyword and location across the US and international markets
- Scrape specific businesses via direct URL input
- Business profile data — name, phone, address, categories, price range, cuisine, website, description
- Customer reviews — text, star rating, per-review date, attached photos, Useful/Funny/Cool reactions
- Hours of operation — one entry per weekday, normalized to 12-hour format
- Services & amenities — takeout, delivery, accepts credit cards, and more
- Geographic coordinates — latitude and longitude for mapping
- Photo galleries grouped by category (food, inside, outside, menu)
- Owner replies — when the business has publicly responded to reviews
- Menu items — name, price, description (restaurants only, when available)
- Claim status — whether a business has been claimed by its owner on Yelp

## Input Parameters

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `searchTerms` | Array of strings | `[]` | Search queries (e.g., "pizza", "plumber", "hair salon") |
| `locations` | Array of strings | `[]` | Locations to search (e.g., "New York, NY", "Los Angeles, CA") |
| `directUrls` | Array of URLs | `[]` | Direct Yelp business page URLs to scrape |
| `searchLimit` | Integer | `10` | Maximum results per search query (1-100) |
| `reviewLimit` | Integer | `5` | Maximum reviews per business (0-50) |
| `fetchPhotos` | Boolean | `true` | Extract gallery photos grouped by category |
| `fetchHours` | Boolean | `true` | Extract hours of operation |
| `fetchMenu` | Boolean | `false` | Attempt to extract menu items (restaurants only) |
| `proxy` | Object | Apify residential | **REQUIRED.** Residential proxy configuration |

You must provide at least one of `searchTerms` or `directUrls`.

## Output Fields

Each business record includes the fields that are available on Yelp. Fields with no data are omitted from the record — there are no empty strings, empty arrays, or null values in the output.

| Field | Type | Description |
|-------|------|-------------|
| `directUrl` | String | Full Yelp URL of the business page |
| `bizId` | String | Yelp business slug identifier |
| `name` | String | Business name |
| `description` | String | Business description from structured data |
| `categories` | Array | Business categories (e.g., "Pizza", "Italian") |
| `type` | String | Business type (e.g., "Restaurant", "LocalBusiness") |
| `phone` | String | Business phone number |
| `reviewCount` | String | Total number of reviews |
| `aggregatedRating` | String | Average star rating (e.g., "4.5") |
| `priceRange` | String | Price level ("$", "$$", "$$$") |
| `cuisine` | String | Cuisine type (restaurants) |
| `website` | String | Business website URL |
| `images` | Array | Business hero image URLs |
| `address` | Object | streetAddress, addressLocality, addressRegion, postalCode, addressCountry |
| `coordinates` | Object | latitude, longitude |
| `hours` | Object | Mon-Sun → opening range (e.g., `"Mon": "11:00 AM - 10:00 PM"`) |
| `services` | Array | Amenities and services (Takeout, Delivery, Parking, etc.) |
| `photoCategories` | Object | Photo URLs grouped by category (food, inside, outside, menu) |
| `menu` | Array | Menu items `{name, price, description}` (restaurants) |
| `claimStatus` | String | `"claimed"` or `"unclaimed"` |
| `ownerReplies` | Array | Business responses to reviews `{reviewDate, reply, replyDate}` |
| `reviews` | Array | Customer reviews — see below |
| `scrapedAt` | String | ISO 8601 UTC timestamp |

### Review Object

| Field | Type | Description |
|-------|------|-------------|
| `date` | String | Review date (per-review, correctly anchored) |
| `rating` | String | Star rating ("1"-"5") |
| `text` | String | Review text content |
| `photos` | Array | URLs of photos attached to the review |
| `isUsefulCount` | Integer | Number of "Useful" reactions |
| `isFunnyCount` | Integer | Number of "Funny" reactions |
| `isCoolCount` | Integer | Number of "Cool" reactions |

## Supported URL Formats

- Business pages: `https://www.yelp.com/biz/business-name-city`
- Business pages with disambiguation suffix: `https://www.yelp.com/biz/business-name-city-2`

## Example Input

### Search for businesses

```json
{
    "searchTerms": ["pizza", "sushi"],
    "locations": ["New York, NY", "San Francisco, CA"],
    "searchLimit": 5,
    "reviewLimit": 3,
    "fetchPhotos": true,
    "fetchHours": true,
    "fetchMenu": false,
    "proxy": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}
```

### Scrape specific businesses with menus

```json
{
    "directUrls": [
        { "url": "https://www.yelp.com/biz/prince-street-pizza-new-york-2" },
        { "url": "https://www.yelp.com/biz/joes-pizza-new-york" }
    ],
    "reviewLimit": 10,
    "fetchMenu": true,
    "proxy": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}
```

## Use Cases

- **Lead generation** — collect business contact information with phone, website, and address
- **Competitive analysis** — compare ratings, price points, and services across similar businesses
- **Market research** — evaluate business density, pricing, and customer sentiment by neighborhood
- **Restaurant intelligence** — track menus, cuisine types, and hours across competitors
- **Review monitoring** — track customer sentiment and owner responses over time
- **Local SEO** — audit how businesses appear in Yelp search results for target keywords

## Tips for Best Results

- **Start small** — run with `searchLimit: 3` and `reviewLimit: 3` for initial testing
- **Use direct URLs when possible** — faster than search and more reliable for known businesses
- **Residential proxies are mandatory** — Yelp blocks datacenter IPs via Cloudflare
- **Daily recurring runs** — schedule on Apify to keep your dataset current
- **Menu extraction** — only works for US restaurants that have enabled Yelp Menu

## Limitations

- Only publicly visible data is collected
- Yelp caps public review visibility at approximately 30 reviews per business; `reviewLimit` is capped at 50
- Cloudflare protection may occasionally throttle requests despite proxy rotation
- Menu extraction is best-effort and only succeeds for restaurants that have configured a Yelp Menu
- Question & Answer content is not included in this version

## FAQ

**Do I need a proxy?**
Yes. Yelp uses Cloudflare and blocks datacenter IPs. The default input uses Apify's residential proxy group and this is strongly recommended.

**How many reviews can I get per business?**
Up to 50, subject to Yelp's public review page limit (usually around 30).

**Why are some businesses missing a menu?**
Yelp's menu feature is opt-in, US-only, and not available for every restaurant. When no menu is published on Yelp, the `menu` field is omitted from the output.

**Why are some fields missing from my output?**
Yelp Scraper Pro omits fields when data is not available, so every field you see contains real data. This makes downstream processing easier and avoids null checks.

**Can I scrape businesses outside the US?**
Yes. Yelp operates in many countries; international business pages work the same way. Some fields (menu, certain services) are US-centric.

**How is this different from the basic Yelp Scraper?**
Yelp Scraper Pro is faster (no browser), extracts more fields (hours, services, photo categories, owner replies, coordinates, claim status, menu), and correctly anchors review dates per review (avoiding cross-review date bleed in simpler extractors).

**Is my data fresh?**
Every run fetches live data directly from Yelp. Schedule recurring runs on Apify to keep datasets updated.

**Does this require login or cookies?**
No. Yelp Scraper Pro extracts only publicly available data. No authentication is needed.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/yelp-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
