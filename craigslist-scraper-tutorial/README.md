# Craigslist Scraper Tutorial: Run This Apify Actor with Python

Scrape Craigslist search results and individual posts across any city subdomain (sfbay, newyork, chicago, etc.). Extracts titles, prices, descriptions, attributes, coordinates, images, and posted/updated timestamps. HTTP-only, no login, no proxy required.

This repository shows how to run [Craigslist Scraper](https://apify.com/crawlerbros/craigslist-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/craigslist-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/craigslist-scraper](https://apify.com/crawlerbros/craigslist-scraper)
- **SEO title:** Craigslist Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Craigslist search results and individual posts across any city subdomain (sfbay, newyork, chicago, etc.). Extracts titles, prices, descriptions, attributes, coordinates, images, and posted/updated timestamps. HTTP-only, no login, no proxy required.

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

# Craigslist Scraper

Scrape [Craigslist](https://craigslist.org) search results and individual posts across any city subdomain — `sfbay`, `newyork`, `chicago`, `losangeles`, `london`, and hundreds more. Returns titles, prices, descriptions, attributes, coordinates, images, and posted/updated timestamps. HTTP-only; no login, no cookies, no proxy required for normal volume.

## Output (per post)

- `type` = `craigslist_listing`
- `url`, `id` (numeric post id parsed from `<id>.html`)
- `title`, `category`, `subcategory`, `location`, `region`
- `postingType` — category slug from the URL path (`cto`, `apa`, `lab`, `fud`, ...)
- `price`, `priceQualifier` — e.g. `/ 2br - 1083ft²`, `OBO`, `/ month`
- `postedAt`, `updatedAt`
- `description` — plain-text `#postingbody`
- `images` — large image URLs (`_600x450.jpg`) from the gallery
- `latitude`, `longitude` — from the embedded map
- `mapAddress` — street address displayed next to the map
- `attributes` — raw dict parsed from `.attrgroup` (full key → value set)
- `phoneNumbers`, `notices`, `replyUrl`
- Jobs: `compensation`, `employmentType`, `jobTitle`
- For-sale (generic): `condition`, `size`
- Autos: `yearManufactured`, `makeManufacturer`, `modelName`, `odometer`, `transmission`, `fuelType`, `titleStatus`, `cylinders`, `paintColor`, `drive`, `vehicleType`, `vin`
- Housing: `bedroomCount`, `bathroomCount`, `sqft`, `availableDate`, `housingType`, `laundry`, `parking`, `rentPeriod`, `listedBy`, `applicationFee`, `brokerFee`, `openHouseDates`, `catsOk`, `dogsOk`, `furnished`, `smoking`
- `scrapedAt`

Fields that are absent on the source page are simply omitted (no nulls). If zero posts are scrapeable, a single `craigslist_blocked` sentinel is emitted so the run exits with data.

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | object[] | Craigslist search URLs or direct post URLs. Prefill: `https://sfbay.craigslist.org/search/jjj`. |
| `searchTerm` | string | Optional keyword. Appended to each search URL as `?query=<term>`. Ignored for direct post URLs. |
| `maxItems` | integer | Maximum posts per run. Default 3. Max 1000. |
| `scrapeDetails` | boolean | Fetch each post's page for full description + attributes. Default `true`. |
| `minPrice` | integer | Minimum price filter (USD). |
| `maxPrice` | integer | Maximum price filter (USD). |
| `hasImage` | boolean | When true, only include posts with at least one image. |
| `proxyConfiguration` | object | Apify proxy config. Default off — Craigslist accepts datacenter IPs. |

## How it works

1. For each `startUrls` entry, the scraper classifies the URL as either a **search page** (`/search/<cat>`) or a **direct post** (`.../<id>.html`).
2. Search pages are paginated by incrementing the `s=N` query offset; post URLs are extracted from `<li class="cl-static-search-result">` cards.
3. For each post URL (deduplicated by numeric id), the detail page is fetched and parsed:
   - Title from `#titletextonly`
   - Price from `.price`
   - Description from `#postingbody`
   - Attributes from `.attrgroup` (label → value pairs)
   - Coordinates from `.mapbox[data-latitude]`
   - Images from `#thumbs a[data-imgid]` (large `_600x450` URLs)
   - Posted / updated timestamps from `.postinginfos time[datetime]`
4. Phone numbers and warning notices are extracted via regex / DOM.

## FAQ

**Do I need a proxy?** No. Craigslist responds fine from Apify's datacenter IPs. If you hit a 403 wall, toggle on Apify proxy.

**Does this bypass login walls?** Craigslist has no login wall for public listings — this actor works out of the box.

**Can I scrape just one specific post?** Yes. Put the direct post URL (ending in `<id>.html`) into `startUrls` and set `maxItems: 1`.

**What cities are supported?** Every Craigslist subdomain — the scraper detects the region automatically from the URL.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/craigslist-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
