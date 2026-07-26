# Zomato Scraper Tutorial: Run This Apify Actor with Python

Scrape restaurant data from Zomato for major Indian and UAE cities. Get cuisine, ratings, cost for two, location, phones, timings, features, and images.

This repository shows how to run [Zomato Scraper](https://apify.com/crawlerbros/zomato-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/zomato-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/zomato-scraper](https://apify.com/crawlerbros/zomato-scraper)
- **SEO title:** Zomato Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape restaurant data from Zomato for major Indian and UAE cities. Get cuisine, ratings, cost for two, location, phones, timings, features, and images.

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

# Zomato Scraper

Scrape restaurant data from [Zomato](https://www.zomato.com) for major Indian and UAE cities. Get structured JSON with cuisines, ratings, cost-for-two, location, phones, timings, features, photos, and more — up to 9 restaurants per URL, ready for food-tech research, market analysis, lead lists, and directory building.

---

## What This Actor Does

The **Zomato Scraper** extracts restaurant listings and full details from Zomato.com using two complementary modes:

- **URL mode** — paste any Zomato city, cuisine, locality, or search URL.
- **Filter builder mode** — pick a city and optional filters (cuisine, category, rating, sort, cost range) and the actor constructs the URL for you.

Both modes can be combined in a single run. Optional **Expand Cuisines** and **Expand Localities** toggles fan out across dozens of URLs for wider coverage of a single city.

---

## Key Features

- **Structured JSON output** — 30+ fields per restaurant, grouped by topic
- **India + UAE coverage** — 13 supported cities verified live (Mumbai, NCR/Delhi, Bangalore, Pune, Hyderabad, Chennai, Kolkata, Ahmedabad, Jaipur, Lucknow, Dubai, Abu Dhabi, Sharjah)
- **Four surfaces** — Dining Out, Delivery, Cafes, Drinks & Nightlife
- **Rich filters** — cuisine ID, category ID, minimum rating, sort order, cost range
- **Full restaurant detail** — address, lat/long, phones, cost for two, top dishes, known-for, features, timings
- **Expand modes** — auto-fan-out across top cuisines or locality pages for a city
- **Fault tolerant** — per-URL retries, optional continue-on-failure
- **No browser** — pure HTTP, fast and lightweight

---

## Supported Cities

| Country | Cities |
|---|---|
| **India** | Mumbai, NCR (Delhi), Bangalore, Pune, Hyderabad, Chennai, Kolkata, Ahmedabad, Jaipur, Lucknow |
| **UAE** | Dubai, Abu Dhabi, Sharjah |

> Zomato withdrew from other international markets in 2020. URLs for London, NYC, Sydney, etc. are rejected with a clear error.

---

## How to Use

### URL mode

Paste any of these URL shapes:

- `https://www.zomato.com/mumbai/restaurants`
- `https://www.zomato.com/ncr/delivery`
- `https://www.zomato.com/dubai/cafes`
- `https://www.zomato.com/bangalore/drinks-and-nightlife`
- `https://www.zomato.com/mumbai/restaurants/biryani`
- `https://www.zomato.com/mumbai/bandra-west-restaurants`
- `https://www.zomato.com/mumbai/restaurants?cuisine=55&rating=4.5`

Each URL returns **up to 9 restaurants** (Zomato's server-side cap). Use Expand modes or supply multiple URLs for wider coverage.

### Filter builder mode

1. Pick a **City** (e.g. `mumbai`).
2. Pick a **Search Mode** (`dining`, `delivery`, `cafes`, `nightlife`).
3. Optionally set **Cuisine**, **Category**, **Min Rating**, **Sort**, **Min/Max Cost**.
4. Run. The actor constructs a single URL under the hood and scrapes it.

### Expand modes

- **Expand Cuisines** — fans out across ~15 top cuisines for the chosen city (≈135 restaurants).
- **Expand Localities** — fans out across locality pages Zomato exposes for the chosen city.

---

## Output Fields

Every field below is guaranteed present — missing data is represented as `""`, `0`, `[]`, or empty object — never `null`.

| Field | Type | Description |
|---|---|---|
| `id` | int | Zomato restaurant ID |
| `name` | string | Restaurant name |
| `url` | string | Absolute Zomato URL |
| `type` | string | Always `"restaurant"` |
| `cuisines` | string | Comma-joined cuisine names |
| `establishments` | array | `[{id, name}]` establishment types |
| `status` | string | Human-readable (e.g. `"Open now"`) |
| `timing` | string | Opening hours description |
| `is_delivery_only` | bool | |
| `is_perm_closed` | bool | |
| `location.address` | string | |
| `location.locality` | string | |
| `location.locality_verbose` | string | |
| `location.city` | string | |
| `location.city_id` | int | |
| `location.country` | string | |
| `location.country_id` | int | |
| `location.zipcode` | string | |
| `location.latitude` | float | |
| `location.longitude` | float | |
| `location.map_url` | string | Static map image URL |
| `ratings.aggregate` | float | Overall rating |
| `ratings.text` | string | e.g. `"Very Good"` |
| `ratings.votes` | int | Review count |
| `ratings.dining` | float | Dining-only rating |
| `ratings.delivery` | float | Delivery rating (0 if not offered) |
| `reviews.count` | int | |
| `price.for_two` | int | Cost for two |
| `price.currency` | string | `"₹"` for India, `"AED"` for UAE |
| `price.cft_text` | string | Formatted cost for two |
| `phones` | array of string | |
| `photo.url` / `photo.thumb` | string | Main restaurant photo |
| `images` | array | `[{url, thumb}]` |
| `image_count` | int | |
| `features` | object | `{feature_slug: bool}` |
| `highlights` | array of string | |
| `known_for` | string | |
| `top_dishes` | array of string | |
| `social.website` | string | |
| `search_context.source_url` | string | Which input URL produced this record |
| `search_context.city_slug` | string | |
| `search_context.scraped_at` | string | ISO8601 UTC |

---

## Cuisine & Category ID Reference

Common cuisine IDs for the `cuisine` filter:

| ID | Cuisine | ID | Cuisine |
|---|---|---|---|
| 1 | American | 60 | Japanese |
| 25 | Chinese | 66 | Lebanese |
| 35 | Continental | 73 | Mexican |
| 40 | Fast Food | 82 | Pizza |
| 50 | North Indian | 85 | South Indian |
| 55 | Italian | 95 | Thai |

Common category IDs for the `category` filter:

| ID | Category | ID | Category |
|---|---|---|---|
| 1 | Delivery | 7 | Daily Menus |
| 2 | Fine Dining | 8 | Breakfast |
| 3 | Nightlife | 10 | Dinner |
| 4 | Catching-Up | 11 | Pubs and Bars |
| 5 | Takeaway | 13 | Pocket-Friendly Delivery |
| 6 | Cafes | 14 | Clubs and Lounges |

---

## FAQ

**Why is the max 9 restaurants per URL?**
Zomato's public search surface caps at 9 results per page and does not honour pagination parameters. This is a server-side constraint. To get wider coverage, supply more URLs (one per cuisine/locality/category) or use the **Expand Cuisines** / **Expand Localities** toggles.

**Why are some cities not supported?**
Zomato withdrew from many international markets (US, UK, Australia, etc.) in 2020. Only India and UAE have active, reliable data today. The actor validates city input against a live-verified allow-list.

**Does the actor use proxies or cookies?**
No. It runs purely on unauthenticated HTTP against Zomato's public endpoints.

**What happens if a URL fails?**
By default, the actor retries twice with exponential backoff. If retries are exhausted, it logs a warning and continues with the next URL (`ignore_url_failures=true`). Set `ignore_url_failures=false` to fail the run on any URL failure.

**Why are menu items and review text not in the output?**
Zomato's current public webroutes API no longer exposes dish-level data, review text, or wishlist counts. They were available on the deprecated v2 developer API. The actor only emits fields we can populate reliably so the output is never `null`.

**How do I scrape reviews?**
Review scraping is out of scope for this actor — it would require a separate, dedicated review-fetcher with cursor-based pagination.

**Can I batch multiple cities in one run?**
Yes. Pass multiple URLs in `start_urls`, or combine `start_urls` + a `city` selection.

---

## Output Example

```json
{
  "id": 22244281,
  "name": "Luna Et Sol",
  "url": "https://www.zomato.com/mumbai/luna-et-sol-lower-parel/info",
  "type": "restaurant",
  "cuisines": "Italian, Continental",
  "establishments": [{"id": 18, "name": "Fine Dining"}],
  "status": "Open now",
  "timing": "12midnight – 1am, 12noon – 1am (Mon-Sun)",
  "is_delivery_only": false,
  "is_perm_closed": false,
  "location": {
    "address": "Lower Parel, Mumbai",
    "locality": "Lower Parel",
    "locality_verbose": "Lower Parel, Mumbai",
    "city": "Mumbai",
    "city_id": 3,
    "country": "India",
    "country_id": 1,
    "zipcode": "",
    "latitude": 19.004,
    "longitude": 72.830,
    "map_url": "https://maps.zomato.com/php/staticmap?..."
  },
  "ratings": {
    "aggregate": 4.4, "text": "Very Good", "votes": 903,
    "dining": 4.4, "delivery": 0
  },
  "reviews": {"count": 903},
  "price": {"for_two": 3500, "currency": "₹", "cft_text": "₹3,500 for two"},
  "phones": ["+91 22XXXXXXXX"],
  "photo": {"url": "https://b.zmtcdn.com/...", "thumb": "https://b.zmtcdn.com/..."},
  "images": [{"url": "…", "thumb": "…"}],
  "image_count": 12,
  "features": {"outdoor-seating": true, "credit-card": true},
  "highlights": ["Fine Dining", "Rooftop"],
  "known_for": "Ambience, Italian Food",
  "top_dishes": ["Truffle Pasta", "Tiramisu"],
  "social": {"website": "https://www.zomato.com/mumbai/luna-et-sol-lower-parel/info"},
  "search_context": {
    "source_url": "https://www.zomato.com/mumbai/restaurants",
    "city_slug": "mumbai",
    "scraped_at": "2026-04-11T10:30:00+00:00"
  }
}
```

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/zomato-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
