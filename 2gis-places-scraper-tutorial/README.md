# 2GIS Places Scraper Tutorial: Run This Apify Actor with Python

Search 2GIS business directory across 11 country domains (RU, KZ, UAE, UZ, BY, AM, AZ, GE, TJ, KG, .com). Extract place name, address, postcode, structured address, rating, category, reviews, photos, contacts, working hours, and social links via the Catalog API.

This repository shows how to run [2GIS Places Scraper](https://apify.com/crawlerbros/2gis-places-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/2gis-places-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/2gis-places-scraper](https://apify.com/crawlerbros/2gis-places-scraper)
- **SEO title:** 2GIS Places Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search 2GIS business directory across 11 country domains (RU, KZ, UAE, UZ, BY, AM, AZ, GE, TJ, KG, .com). Extract place name, address, postcode, structured address, rating, category, reviews, photos, contacts, working hours, and social links via the Catalog API.

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

# 2GIS Places Scraper

Extract business listings, restaurants, hotels, shops, and services from **2GIS** — the leading map and business directory for Russia, UAE, Kazakhstan, and 10+ countries. Get place names, addresses, GPS coordinates, ratings, phone numbers, websites, working hours, reviews, and photos.

## What is 2GIS?

[2GIS](https://2gis.com) is a mapping and business directory platform used by millions across Russia, the UAE, Kazakhstan, Kyrgyzstan, Uzbekistan, Belarus, Armenia, Azerbaijan, Georgia, and Tajikistan. It lists millions of businesses with detailed information including contacts, hours, and user reviews.

## What This Actor Does

- Searches 2GIS for any category (restaurants, hotels, shops, services, etc.) in any supported city
- Accepts both **2GIS search URLs** and free-text **query + city** inputs
- Returns structured data for every matching place
- Optionally fetches phone numbers, emails, websites, social media links, reviews, and photos

## Input

| Field | Description | Default |
|-------|-------------|---------|
| Start URLs | 2GIS search URLs to scrape (e.g. `https://2gis.ae/dubai/search/restaurant`) | Required |
| Search Queries | Search terms to run against each city — overrides URL's embedded query | — |
| Location | City name when not using URLs (e.g. "Dubai", "Moscow", "Almaty") | — |
| Max Items | Maximum places per query+location combination | 50 |
| 2GIS API Key | API key for higher limits. Use `demo` for up to ~50 results for free | `demo` |
| Include Contacts | Fetch phones, website, email, social links | Yes |
| Include Reviews | Fetch user reviews per place — requires a registered API key | No |
| Include Photos | Include photo URLs — requires a registered API key | No |
| Sort By | `relevance`, `rating`, or `distance` | relevance |
| Has Website Only | Only return places with a website | No |
| Has Photos Only | Only return places with photos | No |
| Open Now Only | Only return currently open places | No |
| Category IDs | Filter by 2GIS rubric/category IDs | — |

### How to Get a Start URL

1. Go to [2gis.ae](https://2gis.ae) (or [2gis.ru](https://2gis.ru), [2gis.kz](https://2gis.kz), etc.)
2. Search for a category in any city (e.g. "restaurant" in Dubai)
3. Copy the URL from your browser address bar
4. Paste it into the Start URLs field

**Example URLs:**
- `https://2gis.ae/dubai/search/restaurant`
- `https://2gis.ru/moscow/search/кофе`
- `https://2gis.kz/almaty/search/hotel`

## Output

Each place is one JSON record. Fields appear only when the data exists — no null values.

| Field | Description | Example |
|-------|-------------|---------|
| `id` | 2GIS place ID | `"70000001035586092"` |
| `name` | Place name | `"Nobu Restaurant"` |
| `city` | City | `"Dubai"` |
| `country` | Country | `"UAE"` |
| `address` | Street address (single line) | `"Al Wasl Rd, 10"` |
| `street` | Street name only (when API exposes structured address) | `"Al Wasl Rd"` |
| `houseNumber` | Building number (when API exposes structured address) | `"10"` |
| `postcode` | Postal code (when API exposes it) | `"00000"` |
| `addressComment` | Floor, entrance, etc. | `"3rd floor"` |
| `latitude` | GPS latitude | `25.1972` |
| `longitude` | GPS longitude | `55.2744` |
| `categories` | Place categories | `["Restaurant", "Japanese"]` |
| `categoryIds` | Category IDs | `["281", "6780"]` |
| `rating` | Average rating (1–5) | `4.7` |
| `ratingCategory` | Bucketed rating: `"Excellent"` (≥4.5), `"Good"` (≥4.0), `"Average"` (≥3.0), `"Poor"` (<3.0) | `"Excellent"` |
| `reviewCount` | Total review count | `312` |
| `workingHours` | Opening hours by day | `[{"day": "Mon", "hours": [{"from": "10:00", "to": "22:00"}]}]` |
| `phones` | Phone numbers | `["+971 4 560 1234"]` |
| `website` | Website URL | `"https://nobu.ae"` |
| `emails` | Email addresses | `["info@nobu.ae"]` |
| `socialLinks` | Social media links | `{"instagram": "https://instagram.com/nobu_dubai"}` |
| `reviews` | User reviews (when enabled) | `[{"rating": 5, "text": "..."}]` |
| `photos` | Photo URLs (when enabled) | `["https://disk.2gis.com/..."]` |
| `url` | 2GIS place page URL | `"https://2gis.ae/dubai/firm/..."` |
| `scrapedAt` | Scrape timestamp (UTC) | `"2026-04-22T10:00:00Z"` |

## Supported Countries and Domains

| Domain | Country |
|--------|---------|
| 2gis.ae | UAE |
| 2gis.ru | Russia |
| 2gis.kz | Kazakhstan |
| 2gis.kg | Kyrgyzstan |
| 2gis.uz | Uzbekistan |
| 2gis.by | Belarus |
| 2gis.am | Armenia |
| 2gis.az | Azerbaijan |
| 2gis.ge | Georgia |
| 2gis.tj | Tajikistan |

## FAQ

**Do I need a proxy?**
No. The 2GIS API is publicly accessible without a proxy. The actor connects directly from Apify servers.

**Do I need an API key?**
No signup is required. The built-in `demo` key works out of the box for up to ~50 results per search. For more results, register a free key at [platform.2gis.ru](https://platform.2gis.ru) (no credit card required) and enter it in the API Key field.

**How many results can I get?**
With the `demo` key: up to ~50 results per search query+city combination. With a registered free key: hundreds or thousands depending on how many places exist for that query in the city.

**Can I search in Russian or Arabic?**
Yes. Paste 2GIS URLs with Cyrillic or Arabic queries directly into Start URLs, or type a query in any language in the Search Queries field alongside a Location (e.g. Location: "Москва", Query: "кофе").

**Can I scrape reviews?**
Reviews require a registered API key (the demo key does not support the reviews endpoint). Enable "Include Reviews", set "Max Reviews per Place", and provide your registered key in the API Key field.

**Can I get photos?**
Photo URLs require a registered API key. Enable "Include Photos" and provide your registered key.

**Can I filter by category?**
Yes. Use the Category IDs (Rubric IDs) field. Find IDs by browsing 2GIS categories at 2gis.com/catalog and noting the ID in the URL.

**What cities are supported?**
Any city listed on 2GIS — over 500 cities across 10+ countries in Russia, CIS, and the Middle East.

**Why are some fields missing for some places?**
2GIS listings vary in completeness. The actor only outputs fields that contain real data — no null or empty values appear in the output.

**Can I scrape a specific place directly?**
Yes. Paste a 2GIS firm URL (e.g. `https://2gis.ae/dubai/firm/nobu/70000001035586092`) into Start URLs to fetch data for that specific place.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/2gis-places-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
