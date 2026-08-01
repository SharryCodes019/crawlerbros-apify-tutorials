# Furnished Finder Scraper Tutorial: Run This Apify Actor with Python

Extract furnished rental listings from FurnishedFinder.com by city and state. Scrape price, bedrooms, bathrooms, amenities, photos, coordinates, ratings, and optional landlord contact info and reviews.

This repository shows how to run [Furnished Finder Scraper](https://apify.com/crawlerbros/furnished-finder-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/furnished-finder-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/furnished-finder-scraper](https://apify.com/crawlerbros/furnished-finder-scraper)
- **SEO title:** Furnished Finder Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract furnished rental listings from FurnishedFinder.com by city and state. Scrape price, bedrooms, bathrooms, amenities, photos, coordinates, ratings, and optional landlord contact info and reviews.

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

## Furnished Finder Scraper

Extract furnished rental listings from [FurnishedFinder.com](https://www.furnishedfinder.com) by city and state. Fast, reliable, and handles FurnishedFinder's 72-per-page cap automatically — get hundreds of listings per city in a single run.

Whether you're tracking the mid-term rental market, building a rental aggregator, or doing real estate research, this scraper returns clean structured data for every listing: price, location, bedrooms, amenities, photos, and more.

### What It Scrapes

For every listing, you get:

- **Identity** — listing ID, canonical URL, title, property type (Apartment, House, Room, etc.)
- **Location** — city, state, latitude, longitude
- **Pricing** — monthly rent parsed to an integer USD value plus the raw display text, and fees such as deposit, cleaning, and pet fees
- **Specs** — bedrooms, bathrooms, square footage, minimum stay days
- **Content** — space description, neighborhood description, house rules
- **Amenities** — wifi, kitchen, laundry, pool, pet-friendly, and more
- **Bed and bath breakdown** — per-room list of bed types and bathroom types
- **Photos** — full-size image URLs
- **Ratings** — average rating and review count (when listed)
- **Metadata** — UTC `scrapedAt` timestamp on every record

#### Optional extras

- **`moreDetails` flag** — also attach the landlord profile: display name, profile image, username, tenure on the platform, verification badges (email, phone, ID), and a list of nearby hospitals with distances. Actual landlord email and phone are **not** included because FurnishedFinder gates direct contact behind a logged-in on-site messaging form.
- **`includeReviews` flag** — best-effort inclusion of individual reviews for properties where they are publicly embedded on the listing page.

### Inputs

| Field | Required | Description | Example |
|---|---|---|---|
| `city` | yes (unless `startUrls`) | City name to search | `"Austin"` |
| `state` | yes (unless `startUrls`) | US state — full name or 2-letter code | `"Texas"` or `"TX"` |
| `maxItems` | no | Max listings to scrape (default `20`, up to `1000`) | `50` |
| `minPrice` | no | Minimum monthly rent in USD | `1000` |
| `maxPrice` | no | Maximum monthly rent in USD | `3000` |
| `moveInDate` | no | Target move-in date (`YYYY-MM-DD`) | `"2026-09-01"` |
| `propertyType` | no | Filter by type — multi-select from `room` (private room) and `entire_unit` (whole unit). The granular type (`Apartment`, `House`, `Condo`, …) appears in the output `propertyType` field of every record regardless. | `["room","entire_unit"]` |
| `moreDetails` | no | Attach landlord profile fields (default `false`) | `true` |
| `includeReviews` | no | Attach reviews array when available (default `false`) | `true` |
| `startUrls` | no | Override search by passing FurnishedFinder URLs directly — search pages or `/property/{id}_{unit}` URLs. When set, `city` and `state` are ignored. | `[{"url":"https://www.furnishedfinder.com/property/979582_1"}]` |

### Output Example

Each dataset record is a flat JSON object. Here is a real record from a live run:

```json
{
  "id": "979582_1",
  "url": "https://www.furnishedfinder.com/property/979582_1",
  "title": "Redriver Haven",
  "propertyType": "Apartment",
  "city": "Austin",
  "state": "Texas",
  "latitude": 30.3024655,
  "longitude": -97.7216704,
  "monthlyPrice": 2000,
  "monthlyPriceText": "$2,000/month",
  "bedrooms": 1,
  "bathrooms": 1,
  "minimumStayDays": 30,
  "spaceDescription": "Quiet, fully furnished apartment near Red River St...",
  "utilitiesIncluded": true,
  "amenities": ["washeranddryeronpremises"],
  "houseRules": [{"name": "petsNotAllowed", "description": "Not Allowed"}],
  "bedList": [{"title": "Bedroom 1", "type": "Queen Bed"}],
  "bathList": [{"title": "Bathroom 1", "type": "Private Bath"}],
  "fees": [
    {"type": "Deposit (Refundable)", "amount": 300},
    {"type": "Cleaning Fee", "amount": 100}
  ],
  "photos": [
    "https://www.furnishedfinder.com/_pdp_/979582/1/979582_1_62490947-full.png"
  ],
  "scrapedAt": "2026-04-11T12:46:26.648593+00:00"
}
```

Fields that cannot be extracted for a particular listing are simply omitted from that record — you will never see `null` values.

### FAQ

**Do I need a proxy?**
An Apify datacenter proxy is enabled by default and is recommended — FurnishedFinder uses Cloudflare, which can block plain unauthenticated requests at scale. For large runs (100+ listings) or if you see 0 results, switch to **Residential** in the proxy configuration to improve reliability. Free-plan Apify accounts include datacenter proxies; residential proxies require the Starter plan or above.

**Does it use cookies or run a headless browser?**
No. It is a pure HTTP scraper using TLS impersonation, which makes it fast and cost-efficient to run.

**Can I scrape a single property by URL?**
Yes — pass it in `startUrls` as `[{"url": "https://www.furnishedfinder.com/property/<id>_<unit>"}]` and the scraper will fetch just that one listing.

**Which states are supported?**
All 50 US states plus the District of Columbia. Enter the full name (`"Texas"`) or the 2-letter code (`"TX"`).

**How many listings can I get per city?**
Up to the `maxItems` value (default `20`, max `1000`). FurnishedFinder returns at most 72 listings per search request — the scraper automatically subdivides the price range into smaller slices and merges the results, so you can collect hundreds of listings per city in a single run without any extra configuration.

**What happens if a listing is missing a field?**
Fields that cannot be extracted for a particular listing are omitted from that record's JSON — no nulls. Your downstream pipeline always sees clean, well-typed data.

**Are duplicate listings possible?**
No. Results are deduplicated by property and unit ID within a single run.

**Does the scraper return landlord email and phone?**
No. FurnishedFinder does not publicly expose landlord email and phone — contacting a landlord goes through their on-site messaging form, which requires a login. The `moreDetails` flag still gives you the landlord's display name, profile image, verification badges (email/phone/ID verified), tenure on the platform, and a list of nearby hospitals, which is the public-facing contact information FurnishedFinder surfaces.

**How fresh is the data?**
Every run fetches live data from FurnishedFinder at the moment the actor runs. There is no cache — each record includes a `scrapedAt` UTC timestamp so you always know when it was captured.

**Can I filter by multiple property types at once?**
Yes. `propertyType` accepts an array. The two filter classes FurnishedFinder exposes are `room` (private room in a shared place) and `entire_unit` (whole apartment, house, or condo). To include both, pass `["room", "entire_unit"]`. The granular type — `Apartment`, `House`, `Condo`, etc. — is returned in the output `propertyType` field of every record so you can filter further downstream.

**Can I combine a price range with a move-in date?**
Yes. All filters (`minPrice`, `maxPrice`, `moveInDate`, `propertyType`) stack and are applied together.

### Use Cases

- **Real estate analytics** — track mid-term rental prices and inventory by city
- **Relocation research** — find furnished rentals meeting your price and move-in criteria
- **Competitive intelligence** — monitor what's listed in a particular market
- **Data enrichment** — augment your own property database with live market listings
- **Lead generation** — build a list of properties by area for outreach and marketing
- **Travel nursing and corporate housing** — surface 30+ day stays in target hospital markets

### Getting Started

1. Enter a `city` and `state` — that's all you need for a basic run.
2. Optional: add filters like `minPrice`, `maxPrice`, `moveInDate`, or `propertyType` to narrow results.
3. Optional: toggle `moreDetails` or `includeReviews` for richer output.
4. Click **Start** and get clean JSON listings in your dataset.

# Actor input Schema

## `city` (type: `string`):

City name to search for rentals (e.g. 'Phoenix', 'New York'). Required unless `startUrls` is provided.

## `state` (type: `string`):

US state — full name (e.g. 'Arizona') or two-letter code (e.g. 'AZ'). Required unless `startUrls` is provided.

## `startUrls` (type: `array`):

Override city/state with explicit FurnishedFinder URLs — search pages or /property/{id}\_{unit} URLs. When set, city and state are ignored.

## `maxItems` (type: `integer`):

Maximum number of listings to scrape

## `minPrice` (type: `integer`):

Minimum monthly rent in USD

## `maxPrice` (type: `integer`):

Maximum monthly rent in USD

## `moveInDate` (type: `string`):

Target move-in date in YYYY-MM-DD format

## `propertyType` (type: `array`):

Filter by property type. FurnishedFinder only exposes two filter classes: 'room' (private room in a shared place) and 'entire\_unit' (whole apartment/house/condo). The granular type (House, Condo, Apartment) appears in the output `propertyType` field of every record.

## `moreDetails` (type: `boolean`):

Extract landlord name, biography, profile image, verification status, and nearby hospitals from the property page.

## `includeReviews` (type: `boolean`):

Try to extract individual review text, ratings, and dates when FurnishedFinder embeds them in the property page. Note: only a small fraction of FurnishedFinder properties expose reviews in the page payload — most only expose `avgRating` and `totalReviewCount`. The rating/count fields are extracted regardless of this toggle when present.

## `proxyConfiguration` (type: `object`):

Proxy configuration. Apify Proxy (datacenter) is enabled by default — FurnishedFinder uses Cloudflare which blocks plain datacenter requests without proxy rotation.

## Actor input object example

```json
{
  "city": "Phoenix",
  "state": "AZ",
  "maxItems": 5,
  "moreDetails": false,
  "includeReviews": false,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}
```

# Actor output Schema

## `listings` (type: `string`):

No description

# API

You can run this Actor programmatically using our API. Below are code examples in JavaScript, Python, and CLI, as well as the OpenAPI specification and MCP server setup.

## JavaScript example

```javascript
import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with your Apify API token
// Replace the '<YOUR_API_TOKEN>' with your token
const client = new ApifyClient({
    token: '<YOUR_API_TOKEN>',
});

// Prepare Actor input
const input = {
    "city": "Phoenix",
    "state": "AZ",
    "maxItems": 5,
    "moreDetails": false,
    "includeReviews": false,
    "proxyConfiguration": {
        "useApifyProxy": true
    }
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/furnished-finder-scraper").call(input);

// Fetch and print Actor results from the run's dataset (if any)
console.log('Results from dataset');
console.log(`💾 Check your data here: https://console.apify.com/storage/datasets/${run.defaultDatasetId}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.forEach((item) => {
    console.dir(item);
});

// 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/js/docs

```

## Python example

```python
from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
# Replace '<YOUR_API_TOKEN>' with your token.
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the Actor input
run_input = {
    "city": "Phoenix",
    "state": "AZ",
    "maxItems": 5,
    "moreDetails": False,
    "includeReviews": False,
    "proxyConfiguration": { "useApifyProxy": True },
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/furnished-finder-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "city": "Phoenix",
  "state": "AZ",
  "maxItems": 5,
  "moreDetails": false,
  "includeReviews": false,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}' |
apify call crawlerbros/furnished-finder-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/furnished-finder-scraper",
                "--header",
                "Authorization: Bearer <YOUR_API_TOKEN>"
            ]
        }
    }
}

```

## OpenAPI specification

Download the OpenAPI definition: https://api.apify.com/v2/acts/dkjY2R662M7IEUCw5/builds/k9u9VthG32puveqla/openapi.json

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/furnished-finder-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
