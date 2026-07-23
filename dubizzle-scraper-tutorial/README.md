# Dubizzle Listings Scraper (Unofficial) Tutorial: Run This Apify Actor with Python

Scrape product listings from Dubizzle UAE for motors, real estate, jobs, electronics, and more. Extract prices, photos, seller info, location, and 70+ fields per listing.

This repository shows how to run [Dubizzle Listings Scraper (Unofficial)](https://apify.com/crawlerbros/dubizzle-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/dubizzle-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/dubizzle-scraper](https://apify.com/crawlerbros/dubizzle-scraper)
- **SEO title:** Dubizzle Listings Scraper (Unofficial) Tutorial: Run This Apify Actor with Python
- **Description:** Scrape product listings from Dubizzle UAE for motors, real estate, jobs, electronics, and more. Extract prices, photos, seller info, location, and 70+ fields per listing.

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

# Dubizzle Listings Scraper (Unofficial)

> **Disclaimer:** This Actor is an independent third-party tool and is **not affiliated with, endorsed by, or sponsored by Dubizzle** or any of its subsidiaries. All trademarks mentioned (including "Dubizzle") are the property of their respective owners. This scraper accesses publicly available data only.

Extract structured product listings from Dubizzle UAE classifieds pages. Scrape listings across all categories including motors, real estate, jobs, electronics, furniture, pets, fashion, and more. Get 70+ fields per listing: prices, photos, seller info, location, contact flags, and full multilingual data in English and Arabic.

---

## What This Actor Does

This scraper lets you collect large volumes of listing data from Dubizzle UAE without a browser or manual browsing. It supports two modes:

- **URL mode** — paste any Dubizzle category or search URL and the actor will paginate through and extract all matching listings.
- **Keyword + location mode** — enter a search term and a UAE city to find listings across all categories.

The actor returns structured, JSON-formatted data for each listing — ready for analysis, price monitoring, lead generation, market research, or integration into your own apps.

---

## Key Features

- **70+ output fields** per listing including price, location, photos, seller details, and more
- **Multilingual data** — both English and Arabic for names, descriptions, and URLs
- **All 9 UAE cities**: Dubai, Abu Dhabi, Sharjah, Ras Al Khaimah, Ajman, Al Ain, Fujairah, Umm Al Quwain, and UAE-wide
- **Two scraping modes**: direct URL or keyword + city search
- **Sorting options**: default relevance, newest first, or price low-to-high
- **Pagination** with a configurable per-URL item limit
- **Fast and lightweight** — no browser required, runs purely on HTTP requests
- **Retry logic** with configurable retry attempts per URL
- **Fault tolerant** — optionally continue on individual URL failures instead of stopping

---

## Supported Categories

| Category | Examples |
|---|---|
| **Motors** | Used Cars, New Cars, Motorcycles, Trucks, Boats, Heavy Equipment |
| **Property for Rent** | Apartments, Villas, Offices, Shops, Warehouses, Rooms |
| **Property for Sale** | Apartments, Villas, Land, Commercial Properties |
| **Jobs** | Full-time, Part-time, Freelance, all industries |
| **Electronics & Appliances** | Mobile Phones, Computers, TVs, Cameras, Networking |
| **Furniture & Garden** | Home Furniture, Office Furniture, Garden & Outdoor |
| **Pets** | Dogs, Cats, Birds, Fish, Pet Accessories |
| **Fashion & Beauty** | Clothing, Shoes, Bags, Accessories, Jewelry |
| **Sports Equipment** | Gym Equipment, Outdoor Sports, Water Sports |
| **Gaming** | Consoles, Games, Accessories |
| **Kids & Baby Products** | Toys, Strollers, Clothing, Nursery |
| **Business & Industrial** | Machinery, Tools, Catering, Agriculture |
| **Books, Music & Movies** | Books, CDs, DVDs, Instruments |
| **Free Stuff** | Items listed at no cost |

---

## Input Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `urls` | array of strings | `[]` | One or more Dubizzle listing or category URLs to scrape. Takes priority over keyword mode. |
| `keyword` | string | `""` | Search term to find listings (e.g., `"laptop"`, `"honda civic"`). Used when no URLs are provided. |
| `location` | enum | `"uae"` | UAE city to filter results. Options: `uae`, `dubai`, `abudhabi`, `sharjah`, `rak`, `ajman`, `fujairah`, `uaq`, `alain`. |
| `sort_by` | enum | `""` | Sort order for results. Options: `""` (default/relevance), `"date_desc"` (newest first), `"price_asc"` (price low to high). |
| `page` | integer | `1` | Starting page number (1-based). Useful for resuming or targeting a specific page. |
| `max_items_per_url` | integer | `20` | Maximum number of listings to collect per URL or search task. |
| `max_retries_per_url` | integer | `2` | Number of retry attempts before giving up on a failed request. |
| `ignore_url_failures` | boolean | `true` | If `true`, the actor continues processing remaining URLs when one fails. If `false`, it stops on the first failure. |

> **Note:** You must provide either `urls` or `keyword`. If both are provided, `urls` takes priority.

---

## Usage Examples

### Example 1 — URL Mode: Scrape Dubai Used Cars

```json
{
  "urls": ["https://dubai.dubizzle.com/motors/used-cars/"],
  "max_items_per_url": 50,
  "sort_by": "date_desc"
}
```

### Example 2 — Keyword Mode: Search "laptop" in Abu Dhabi

```json
{
  "keyword": "laptop",
  "location": "abudhabi",
  "max_items_per_url": 30,
  "sort_by": "price_asc"
}
```

### Example 3 — Multiple URLs with Custom Settings

```json
{
  "urls": [
    "https://dubai.dubizzle.com/property-for-rent/residential/apartment/",
    "https://dubai.dubizzle.com/property-for-sale/residential/apartment/"
  ],
  "max_items_per_url": 100,
  "sort_by": "date_desc",
  "max_retries_per_url": 3,
  "ignore_url_failures": true
}
```

---

## Output Fields

Each scraped listing is saved as a JSON object to the Apify dataset. Below are the key fields grouped by category.

### Identification

| Field | Description |
|---|---|
| `id` | Internal Dubizzle listing ID |
| `uuid` | Unique listing UUID |
| `objectID` | Search index object identifier |
| `name` | Listing title as an object with `en` (English) and `ar` (Arabic) keys |
| `name_en` | Convenience field — English listing title |
| `permalink` | Canonical URL of the listing |
| `absolute_url` | Multilingual URL object with `en` and `ar` versions |

### Pricing

| Field | Description |
|---|---|
| `price` | Listed price (number or structured object with currency) |

### Location

| Field | Description |
|---|---|
| `site` | City/emirate the listing belongs to (object with `en`/`ar`) |
| `city` | Convenience field — English city name |
| `location_list` | Hierarchical location array (country > city > area) |
| `neighbourhood` | Neighbourhood or sub-area name |
| `_geoloc` | Geolocation object with `lat` and `lng` coordinates |

### Category

| Field | Description |
|---|---|
| `category` | Top-level category object with slug, name (en/ar) |
| `category_v2` | Full category hierarchy with `slug_paths` |
| `category_slug` | Convenience field — top-level category slug string |

### Media

| Field | Description |
|---|---|
| `photos` | Array of full-resolution photo URLs |
| `photo_thumbnails` | Array of thumbnail photo URLs |
| `photos_count` | Total number of photos |
| `has_video` | Boolean — whether the listing includes a video |
| `video_url` | Video URL if available |

### Seller Information

| Field | Description |
|---|---|
| `seller_type` | Type of seller: `individual`, `business`, `agent` |
| `user` | Seller user profile object |
| `business` | Business profile details (if applicable) |
| `is_verified` | Whether the seller is verified |
| `is_trusted_seller` | Whether the seller has a trusted seller badge |

### Contact Flags

| Field | Description |
|---|---|
| `has_phone_number` | Whether a phone number is available |
| `has_whatsapp_number` | Whether WhatsApp contact is available |
| `has_sms_number` | Whether SMS contact is available |
| `can_chat` | Whether in-app chat is enabled |

### Listing Details

| Field | Description |
|---|---|
| `details` | Array of key-value attribute pairs specific to the listing type. Examples: `bedrooms`, `bathrooms`, `size` for property; `body_type`, `color`, `year` for motors; `salary`, `company_name` for jobs. |

### Promotion & Visibility

| Field | Description |
|---|---|
| `is_premium` | Whether the listing has a premium placement |
| `is_super_ad` | Whether the listing is marked as a super ad |
| `featured_listing` | Whether the listing is featured |

### Timestamps

| Field | Description |
|---|---|
| `added` | Unix timestamp when the listing was published |
| `created_at` | ISO 8601 creation datetime |

---

## Sample Output

```json
{
  "id": "123456789",
  "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "name_en": "Toyota Camry 2021 - Excellent Condition",
  "price": 75000,
  "city": "Dubai",
  "site": { "en": "Dubai", "ar": "دبي" },
  "neighbourhood": "Al Barsha",
  "_geoloc": { "lat": 25.1080, "lng": 55.1754 },
  "category_slug": "motors",
  "photos": [
    "https://images.dubizzle.com/listings/123456789/photo1.jpg"
  ],
  "photos_count": 8,
  "has_video": false,
  "seller_type": "individual",
  "is_verified": true,
  "has_phone_number": true,
  "has_whatsapp_number": true,
  "can_chat": true,
  "details": [
    { "key": "Year", "value": "2021" },
    { "key": "Kilometers", "value": "45,000 km" },
    { "key": "Body Type", "value": "Sedan" },
    { "key": "Color", "value": "White" }
  ],
  "is_premium": false,
  "is_super_ad": false,
  "added": 1712345678,
  "created_at": "2024-04-05T12:34:56Z",
  "permalink": "https://dubai.dubizzle.com/motors/used-cars/toyota/camry/2024/04/05/toyota-camry-2021/",
  "absolute_url": {
    "en": "https://dubai.dubizzle.com/motors/used-cars/toyota/camry/2024/04/05/toyota-camry-2021/",
    "ar": "https://dubai.dubizzle.com/ar/motors/used-cars/toyota/camry/2024/04/05/toyota-camry-2021/"
  }
}
```

---

## FAQs

### What categories are supported?

The actor supports all major Dubizzle categories including Motors (cars, motorcycles, trucks, boats), Property for Rent, Property for Sale, Jobs, Electronics & Appliances, Furniture & Garden, Pets, Fashion & Beauty, Sports Equipment, Gaming, Kids & Baby Products, Books, Music & Movies, Business & Industrial, and Free Stuff. If a Dubizzle URL exists for a category, it can be scraped.

### Which UAE cities and locations can I search?

You can search across the entire UAE or filter by specific emirate: Dubai, Abu Dhabi, Sharjah, Ras Al Khaimah (RAK), Ajman, Fujairah, Umm Al Quwain (UAQ), and Al Ain. In keyword mode, set the `location` field to one of the values in the input table above. In URL mode, the city is automatically detected from the URL subdomain (e.g., `dubai.dubizzle.com`).

### Can I scrape multiple pages of results?

Yes. The actor automatically paginates through all available pages until it reaches the `max_items_per_url` limit or runs out of results. You can also set the `page` parameter to start from a specific page number, which is useful for resuming interrupted runs or targeting later pages.

### How do I search for a specific product?

Use keyword mode: set `keyword` to your search term (e.g., `"iPhone 15 Pro"`, `"2-bedroom apartment"`, `"treadmill"`) and optionally set `location` to narrow results to a specific city. For more targeted scraping, find the relevant category page on Dubizzle, copy its URL, and use URL mode instead.

### What format is the output data in?

All results are stored in the Apify dataset as structured JSON objects with 70+ fields per listing. You can export the data in JSON, CSV, Excel, XML, or HTML formats directly from the Apify platform. The data is flat enough for spreadsheet analysis while also preserving nested objects for programmatic use.

### Is a proxy required?

No proxy is required to run this actor. Dubizzle listing data is publicly accessible and the actor is designed to work reliably without a proxy, keeping your usage cost minimal.

### How reliable is the scraper?

The actor includes automatic retry logic (configurable up to several attempts per request), exponential backoff on failures, and fault tolerance options that allow it to skip failed URLs and continue. For maximum reliability, start with conservative `max_items_per_url` values and increase as needed.

---

## Use Cases

- **Price monitoring** — track used car or real estate prices across UAE cities over time
- **Market research** — analyze listing volumes, price distributions, and trends by category
- **Lead generation** — collect seller contact availability data for outreach campaigns
- **Competitive analysis** — monitor competitor listings and pricing strategies
- **Real estate intelligence** — gather rental and sale prices by neighbourhood and city
- **Data enrichment** — augment your own database with Dubizzle listing metadata

---

## About This Actor

This is an independent scraper built and maintained by the `crawlerbros` team on Apify. It is not affiliated with Dubizzle. Use it to collect publicly available listing data for analysis, market research, or integration with your own tooling. All data extracted remains subject to the source site's terms of service — please review them before commercial use.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/dubizzle-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
