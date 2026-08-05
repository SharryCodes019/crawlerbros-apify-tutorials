# Yandex Maps Scraper Tutorial: Run This Apify Actor with Python

Scrape business listings, reviews, and place details from Yandex Maps. Extract name, address, phone, website, rating, reviews, working hours, photos and coordinates. Supports 6 regional domains

This repository shows how to run [Yandex Maps Scraper](https://apify.com/crawlerbros/yandex-maps-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/yandex-maps-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/yandex-maps-scraper](https://apify.com/crawlerbros/yandex-maps-scraper)
- **SEO title:** Yandex Maps Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape business listings, reviews, and place details from Yandex Maps. Extract name, address, phone, website, rating, reviews, working hours, photos and coordinates. Supports 6 regional domains

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

# Yandex Maps Scraper

Extract business listings, reviews, place details, ratings, phone numbers, websites, working hours, and photos from [Yandex Maps](https://yandex.com/maps/) — Russia and CIS's dominant map platform. Supports 6 regional domains and 8 languages.

## What data can you scrape?

- **Business name, address, city, country**
- **Phone numbers and website URLs**
- **Star rating and total review count**
- **Business categories** (e.g. "Restaurant", "Coffee shop")
- **Working hours** (structured by day)
- **Photos** (up to 20 per business)
- **Coordinates** (latitude and longitude)
- **Customer reviews** — author, star rating, text, date, likes

## Use cases

- **Lead generation** — build lists of local businesses in Russia, Turkey, Kazakhstan, and other CIS countries
- **Market research** — find competitors, analyze ratings, and map business density
- **Price monitoring** — track businesses in Yandex Market categories
- **Brand monitoring** — find all your branded locations and monitor customer reviews
- **Real estate & site selection** — discover nearby amenities, transport links, and service density
- **Academic research** — study business ecosystems in Russian-speaking markets

## Modes

### `searchPlaces` (default)
Search Yandex Maps for businesses matching a keyword and/or location. Returns a list of place records.

**Example queries:**
- `coffee shops Moscow`
- `sushi restaurant Istanbul`
- `hotel near Red Square`
- `pharmacy Almaty`

### `getDetails`
Fetch complete details for specific Yandex Maps business URLs. Useful when you already know which businesses to target.

### `getReviews`
Scrape customer reviews from specific business pages, sorted by date, rating, or relevance.

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | select | `searchPlaces`, `getDetails`, or `getReviews` |
| `searchQueries` | string[] | Search queries (mode=searchPlaces). Combine type + location. |
| `businessUrls` | string[] | Yandex Maps business URLs (mode=getDetails or getReviews) |
| `yandexDomain` | select | Regional domain: `yandex.com`, `yandex.ru`, `yandex.com.tr`, etc. |
| `language` | select | UI language: `en`, `ru`, `tr`, `de`, `fr`, `uk`, `kk`, `uz` |
| `maxItems` | integer | Max records to return (1–500, default 20) |
| `minRating` | select | Minimum rating filter: `any`, `3`, `3.5`, `4`, `4.5` (searchPlaces only) |
| `reviewsSortOrder` | select | Sort reviews: `by_date_desc`, `by_rating_desc`, `by_relevance` (getReviews only) |
| `proxyConfiguration` | proxy | Residential proxies recommended for best results |

## Output

Each record in the dataset has a `recordType` field:

### Place record (`recordType: "place"`)

```json
{
  "recordType": "place",
  "placeId": "123456789",
  "name": "Шоколадница",
  "url": "https://yandex.com/maps/org/shokoladnitsa/123456789/",
  "address": "Tverskaya St, 15, Moscow, 125009",
  "city": "Moscow",
  "coordinates": { "lat": 55.7644, "lng": 37.6055 },
  "phone": "+7 495 123-45-67",
  "website": "https://shokoladnitsa.ru",
  "rating": 4.5,
  "reviewCount": 2341,
  "categories": ["Coffee shop", "Cafe", "Bakery"],
  "workingHours": {
    "Monday": "08:00–22:00",
    "Tuesday": "08:00–22:00",
    "Saturday": "09:00–23:00",
    "Sunday": "09:00–23:00"
  },
  "photos": [
    "https://avatars.mds.yandex.net/get-altay/...",
    "https://avatars.mds.yandex.net/get-altay/..."
  ],
  "scrapedAt": "2026-05-17T10:00:00+00:00"
}
```

### Review record (`recordType: "review"`)

```json
{
  "recordType": "review",
  "placeId": "123456789",
  "placeName": "Шоколадница",
  "placeUrl": "https://yandex.com/maps/org/shokoladnitsa/123456789/",
  "reviewId": "abc123",
  "author": "Ivan Petrov",
  "authorUrl": "https://yandex.com/profile/ivan",
  "rating": 5,
  "text": "Great coffee and friendly staff. The croissants are fresh every morning.",
  "date": "2024-01-15",
  "likes": 7,
  "scrapedAt": "2026-05-17T10:00:00+00:00"
}
```

## Supported Yandex Domains

| Domain | Region |
|--------|--------|
| `yandex.com` | International |
| `yandex.ru` | Russia |
| `yandex.com.tr` | Turkey |
| `yandex.kz` | Kazakhstan |
| `yandex.uz` | Uzbekistan |
| `yandex.by` | Belarus |

## Tips for best results

- **Use residential proxies** — Yandex may trigger CAPTCHA on datacenter IPs. The default proxy configuration uses Apify residential proxies.
- **Combine type + location** in your search query for precise results (e.g., `Italian restaurant Saint Petersburg` rather than just `restaurant`).
- **Use the matching domain** for your target country — `yandex.ru` for Russian cities, `yandex.com.tr` for Turkish cities.
- **Set language to `ru`** when searching Russian-language businesses for more complete results.
- **Use `getReviews` mode with `by_date_desc`** to get the most recent customer feedback.

## Frequently Asked Questions

**Can I scrape businesses from any city in Russia?**  
Yes. Yandex Maps covers all major Russian cities and thousands of smaller towns. Specify the city name in your search query, e.g., `restaurants Novosibirsk`.

**Does this work for Turkish businesses?**  
Yes. Use `yandex.com.tr` as the domain and `tr` as the language for best results with Turkish locations.

**How many results can I get per search query?**  
Yandex Maps typically returns up to 200–500 results per search. Set `maxItems` accordingly.

**Can I get reviews in Russian?**  
Yes. Reviews are scraped in whatever language they were written. Set `language: ru` to ensure the UI is in Russian.

**Is there a limit on how many reviews I can get per business?**  
You can set `maxItems` up to 500. Most businesses have fewer reviews than that; the scraper stops when there are no more reviews to load.

**Can I filter by minimum star rating?**  
Yes. Use `minRating` to exclude businesses below a threshold (e.g., `4.5` for only top-rated places).

**Why does the scraper use a proxy?**  
Yandex Maps may show a CAPTCHA for automated access from datacenter IP addresses. Residential proxies significantly reduce this. Proxy costs are separate from actor usage.

**How is this different from the Yandex Search Scraper?**  
The Yandex Search Scraper extracts web search results (links, snippets). This actor specializes in Yandex Maps — structured business data including coordinates, phone numbers, hours, photos, and reviews that do not appear in web search results.

**Can I get the coordinates of each business?**  
Yes. Latitude and longitude are included in each place record under the `coordinates` field.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/yandex-maps-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
