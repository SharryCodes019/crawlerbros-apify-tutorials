# Google Maps Menu Scraper Tutorial: Run This Apify Actor with Python

Extract restaurant menu items, popular dishes, photos, categories, and external menu links from any Google Maps place page.

This repository shows how to run [Google Maps Menu Scraper](https://apify.com/crawlerbros/google-maps-menu) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-menu`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-menu](https://apify.com/crawlerbros/google-maps-menu)
- **SEO title:** Google Maps Menu Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract restaurant menu items, popular dishes, photos, categories, and external menu links from any Google Maps place page.

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

# Google Maps Menu Scraper

Extract restaurant menu items, popular-dish indicators, dish photos, menu categories, and external menu links from any Google Maps place page.

## What It Does

Give this actor a Google Maps URL for a restaurant or food business and it returns:

- **Menu items** with names and photos (one record per item)
- **`isPopular` indicator** — `true` when Google highlights a dish as popular
- **Menu categories** — the section names (e.g. `Appetizers`, `Ramen`, `Desserts`) that Google exposes for that restaurant
- **External menu URL** when the restaurant links to its own menu site, PDF, or ordering portal
- **Place ID** for cross-referencing with the Google Maps ecosystem
- **Graceful single fallback record** with `menuFound: false` when no menu data is available — so your dataset stays consistent

## Use Cases

- Power menu intelligence for delivery, restaurant tech, or food blog platforms
- Discover signature / popular dishes per restaurant
- Aggregate menu category coverage by cuisine, location, or chain
- Enrich CRM / lead-gen datasets with menu signals
- Build product catalogues that link back to the operator's own menu page

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `placeUrl` | String | Yes | Google Maps URL of a single restaurant |
| `maxItems` | Integer | No | Maximum menu items per run (1-500). Default `100` |
| `language` | Enum | No | UI language (`en`, `es`, `fr`, `de`, `it`, `pt`, `ja`, `ko`, `zh`, `ar`, `ru`). Default `en` |
| `proxyConfiguration` | Object | No | Apify proxy settings (optional — runs reliably without proxy by default) |

**Example input:**

```json
{
  "placeUrl": "https://www.google.com/maps/place/The+Halal+Guys/@40.7615453,-73.9794252,17z/",
  "maxItems": 50,
  "language": "en"
}
```

> **Tip:** Copy the URL straight from the address bar after opening a restaurant on Google Maps.

## Output

One record per menu item:

```json
{
  "businessName": "The Halal Guys",
  "placeId": "0x89c258ff097dbc2d:0x86df3a18a06daf7c",
  "placeUrl": "https://www.google.com/maps/place/...",
  "menuUrl": "https://example.com/menu",
  "menuCategories": ["Platters", "Sandwiches", "Sides", "Beverages", "Desserts"],
  "menuFound": true,
  "itemName": "Chicken and Beef Gyro Platter",
  "isPopular": true,
  "itemImage": "https://lh3.googleusercontent.com/...=s0",
  "rank": 1,
  "scrapedAt": "2026-06-16T12:00:00Z"
}
```

If a restaurant has no inline menu items on Google Maps, the actor pushes a single fallback record (and still surfaces the external `menuUrl` when present):

```json
{
  "businessName": "Some Restaurant",
  "placeUrl": "https://www.google.com/maps/place/...",
  "menuUrl": "https://restaurant.example.com/menu",
  "menuCategories": ["Appetizers", "Mains"],
  "menuFound": false,
  "scrapedAt": "2026-06-16T12:00:00Z"
}
```

Empty / null fields are stripped from output to keep records compact, while every record carries the same set of keys for stable column schemas.

## Field Reference

| Field | Type | Notes |
|---|---|---|
| `businessName` | String | Restaurant name from the place page heading |
| `placeId` | String | Google place feature ID (`0x...:0x...` form) |
| `placeUrl` | String | The original Google Maps URL |
| `menuUrl` | String | External menu link (restaurant site, PDF, ordering portal) when present |
| `menuCategories` | Array&lt;String&gt; | Menu section names exposed by Google for this restaurant |
| `menuFound` | Boolean | `true` when at least one inline menu item was extracted, `false` otherwise |
| `itemName` | String | Menu item name |
| `isPopular` | Boolean | `true` when Google flags the item as Popular |
| `itemImage` | String | Max-resolution photo URL of the dish (when available) |
| `rank` | Integer | Position of the item within the menu (1-based) |
| `scrapedAt` | String | ISO 8601 UTC timestamp |

## Frequently Asked Questions

**Does every restaurant on Google Maps have a menu?**
No — only restaurants where Google has indexed menu cards expose inline menu items. When inline items aren't available the actor still emits the external `menuUrl` (when the operator has linked one) so you can follow up directly.

**Why no prices on inline items?**
Google Maps does not currently render per-item prices on the place page Menu tab — it shows the dish name, image, and a "Popular" badge but the price (when published) lives behind the external menu link. The actor surfaces every signal Google exposes; if you need item-level prices, follow the `menuUrl` to the restaurant's own menu site.

**Do I need a proxy or cookies?**
No. The actor works reliably from Apify's default datacenter IPs. You can supply Apify Proxy in `proxyConfiguration` as an automatic fallback if a run yields no menu signal.

**Which languages are supported?**
Eleven languages are exposed via the `language` input: English, Spanish, French, German, Italian, Portuguese, Japanese, Korean, Chinese, Arabic, Russian. This controls the Google Maps UI language only — menu item text is returned exactly as published.

**How many items per run?**
The default cap is 100. You can request up to 500 items per run with `maxItems`. Most restaurants surface between 5 and 30 dish cards on Google Maps.

**Can I batch multiple restaurants?**
This actor accepts one `placeUrl` per run. To process many restaurants, schedule the actor with different inputs or chain it inside a workflow that iterates over URLs.

**Why are some fields missing from my records?**
Empty / null fields are stripped to keep your dataset compact. If `itemImage` or `menuUrl` is absent it simply means Google did not publish that detail for that restaurant. Every record always carries `businessName`, `placeUrl`, `menuFound`, and `scrapedAt`.

## Notes & Limitations

- **Google's inline Menu data is shallow.** Google Maps shows dish name + image + a "Popular" badge on the place page, but does not render per-item prices or descriptions inline. Where the operator publishes the full menu (prices, sizes, modifiers, etc.) it lives behind the external `menuUrl` we surface.
- **Coverage varies.** Chains and well-curated places typically expose 5-20 dish cards; many smaller venues expose only the external `menuUrl`. The actor degrades gracefully and always pushes at least one record so you can detect the no-menu case in your pipeline.
- **Place resolution is search-first.** The actor resolves the input URL via Google Maps search; very ambiguous names without coordinates may resolve to a different branch — include `@lat,lng` in the URL when targeting a specific location.

## Complete Google Maps Scraper Suite

This actor is part of a comprehensive Google Maps data extraction toolkit by **crawlerbros**. All actors run on the free Apify plan, use no proxy by default, and return clean, structured data.

| Actor | What it does |
|---|---|
| Google Maps Business Scraper | Extract business data — name, address, phone, website, rating, reviews, hours, amenities |
| Google Maps Reviews Scraper | Scrape reviews with reviewer Local Guide level, photos, mentioned items, owner replies |
| Google Maps Photos Scraper | Extract all photos from any place — max-resolution URLs, contributor info, categories |
| Google Maps Business Hours Scraper | Full 7-day hours, timezone, current local time, next open/close, holiday hours |
| Google Maps Popular Times Scraper | Busy hours histogram for all 7 days + current busyness + typical visit time |
| Google Maps Email Extractor | Find business emails + social media links by crawling websites |
| Google Maps Area Scanner | Geographic grid scanning — bypass the 120-place limit with bounding box / circle / polygon |
| Google Maps Leads Scraper | B2B lead generation with email + phone enrichment, US states + global countries |
| Google Maps Directions Scraper | A→B routing — distance, duration, traffic, route alternatives for driving/walking/transit |
| Google Maps Geocoding Scraper | Bidirectional geocoding — address ↔ coordinates, with address components |
| Google Maps Similar Places Scraper | "People also search for" / related place discovery |
| Google Maps Nearby Scraper | Find places near a coordinate point — lightweight POI search by category |
| Google Maps Place List Scraper | Extract Google's curated "Top X in Y" lists |
| Google Maps Timezone Scraper | IANA timezone + current local time from coordinates |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-menu)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
