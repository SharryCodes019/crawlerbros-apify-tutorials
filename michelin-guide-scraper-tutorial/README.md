# Michelin Guide Scraper Tutorial: Run This Apify Actor with Python

Scrape Michelin-starred restaurants from guide.michelin.com. Search by name, filter by city or country, browse all starred restaurants, or fetch individual restaurant pages. Returns name, stars, address, cuisine, price range, coordinates, and more

This repository shows how to run [Michelin Guide Scraper](https://apify.com/crawlerbros/michelin-guide-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/michelin-guide-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/michelin-guide-scraper](https://apify.com/crawlerbros/michelin-guide-scraper)
- **SEO title:** Michelin Guide Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Michelin-starred restaurants from guide.michelin.com. Search by name, filter by city or country, browse all starred restaurants, or fetch individual restaurant pages. Returns name, stars, address, cuisine, price range, coordinates, and more

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

## Michelin Guide Scraper

Extract restaurant data from the [Michelin Guide](https://guide.michelin.com) — the world's most prestigious restaurant rating system. Collect Michelin-starred restaurants, Bib Gourmand picks, and Michelin Selected restaurants with full details including star ratings, cuisine, address, coordinates, price range, and contact information.

### What You Can Scrape

- **Starred restaurants** (1-star, 2-star, 3-star) worldwide or filtered by country/city
- **Bib Gourmand** listings — exceptional value restaurants recognized by Michelin
- **Michelin Selected** restaurants — quality picks that don't hold stars
- **Search** restaurants by city name or keyword
- **Individual restaurant pages** from direct URLs
- **Detail pages** (optional) — phone, website, coordinates, opening hours, description

### Output Data

Each record includes:

| Field | Description |
|-------|-------------|
| `name` | Restaurant name |
| `url` | Michelin Guide URL |
| `slug` | URL slug identifier |
| `stars` | Michelin star count (1, 2, or 3) |
| `bibGourmand` | `true` if Bib Gourmand designation |
| `michelinSelected` | `true` if Michelin Selected |
| `distinction` | Raw distinction label from Michelin |
| `address` | Full address string |
| `city` | City |
| `country` | Country or region (may be ISO code, e.g. `"FRA"`) |
| `postalCode` | Postal/ZIP code |
| `countryCode` | 2-letter ISO country code (e.g. `"FR"`, `"JP"`) |
| `cuisine` | Cuisine type(s) as labeled by Michelin |
| `priceRange` | Price range: `"$"` – `"$$$$"` from listings, or text from detail pages |
| `hasOnlineBooking` | `true` if online reservations available via Michelin Guide |
| `chefName` | Head chef name |
| `district` | Neighbourhood/district |
| `phone` | Reservation phone number *(detail page)* |
| `website` | Restaurant official website *(detail page)* |
| `latitude` | GPS latitude *(detail page)* |
| `longitude` | GPS longitude *(detail page)* |
| `imageUrl` | Cover photo URL *(detail page)* |
| `description` | Short editorial description *(detail page)* |
| `openingHours` | Opening hours list *(detail page)* |
| `recordType` | Always `"restaurant"` |
| `scrapedAt` | ISO 8601 scrape timestamp |

Fields that cannot be extracted for a particular restaurant are omitted — you will never see `null` values. Detail-page fields are only populated when `includeDetails` is enabled.

### Input Options

#### Mode

| Mode | Description |
|------|-------------|
| `starredRestaurants` | Browse all starred/Bib Gourmand/Selected restaurants (default) |
| `search` | Search by city name or keyword (best for city names in our supported list) |
| `byCity` | Browse all restaurants in a specific city |
| `byUrl` | Scrape individual restaurant page(s) by URL |

#### Filters

| Filter | Description |
|--------|-------------|
| `starFilter` | Filter by distinction: `1`, `2`, `3` (stars), `bib` (Bib Gourmand), `selected` |
| `country` | Filter by country (e.g. `france`, `japan`, `united-states`) |
| `cuisineFilter` | Filter by cuisine type |
| `maxItems` | Maximum number of records to return |
| `includeDetails` | Visit each restaurant's detail page for phone, website, coordinates, etc. |

#### Cuisine Filter Notes

Michelin labels cuisines using specific terms. When filtering by cuisine, note:

- **`classic`** — matches "Classic Cuisine" (the standard label for classic French/European cooking in France and Europe)
- **`traditional`** — matches "Traditional Cuisine" (regional/traditional cooking)
- **`french`** — matches restaurants explicitly labeled "French" by Michelin (more common for French restaurants *outside* France)
- **`japanese`**, **`italian`**, **`chinese`**, **`korean`**, etc. — match nationality-based cuisine labels

#### Example Inputs

**Browse all 3-star restaurants in France:**

```json
{
  "mode": "starredRestaurants",
  "country": "france",
  "starFilter": "3",
  "maxItems": 30
}
```

**Browse Bib Gourmand restaurants in Japan:**

```json
{
  "mode": "starredRestaurants",
  "country": "japan",
  "starFilter": "bib",
  "maxItems": 50
}
```

**Browse Paris restaurants with Classic Cuisine filter:**

```json
{
  "mode": "byCity",
  "city": "Paris",
  "cuisineFilter": "classic",
  "maxItems": 20
}
```

**Browse Tokyo restaurants:**

```json
{
  "mode": "byCity",
  "city": "Tokyo",
  "maxItems": 50
}
```

**Search by city name:**

```json
{
  "mode": "search",
  "searchQuery": "Tokyo",
  "maxItems": 20
}
```

**Scrape specific restaurant pages with full details:**

```json
{
  "mode": "byUrl",
  "startUrls": [
    {"url": "https://guide.michelin.com/en/ile-de-france/paris/restaurant/guy-savoy"}
  ],
  "includeDetails": true
}
```

### Output Example

Here is a real listing record:

```json
{
  "name": "Le Bernardin",
  "url": "https://guide.michelin.com/en/new-york-state/new-york/restaurant/le-bernardin",
  "slug": "le-bernardin",
  "stars": 3,
  "city": "New York",
  "country": "New York State",
  "cuisine": "Seafood",
  "countryCode": "US",
  "hasOnlineBooking": true,
  "recordType": "restaurant",
  "scrapedAt": "2026-06-21T06:00:00.000000+00:00"
}
```

With `includeDetails: true`, additional fields are populated:

```json
{
  "name": "Benoit",
  "url": "https://guide.michelin.com/en/ile-de-france/paris/restaurant/benoit5826",
  "slug": "benoit5826",
  "stars": 1,
  "address": "20 rue Saint-Martin, Paris, Ile-de-France, 75004, FRA",
  "city": "Paris",
  "country": "FRA",
  "postalCode": "75004",
  "countryCode": "FR",
  "cuisine": "Classic Cuisine",
  "priceRange": "Special occasion",
  "phone": "+33 1 42 72 25 76",
  "latitude": 48.8584427,
  "longitude": 2.3500715,
  "imageUrl": "https://axwwgrkdco.cloudimg.io/v7/__gmpics3__/2f6afee318d3442fb9caaef752d3b232.jpeg?width=1000",
  "recordType": "restaurant",
  "scrapedAt": "2026-06-21T05:55:46.031590+00:00"
}
```

### Use Cases

- **Restaurant industry research** — analyze Michelin-starred restaurants by region, cuisine, or price
- **Travel planning** — find top restaurants for destination planning apps
- **Food & dining datasets** — build databases of fine dining establishments
- **Market analysis** — track restaurant openings, closings, and star promotions
- **Competitor analysis** — benchmark restaurant categories and pricing

### FAQ

**How often is the data updated?**
The Michelin Guide updates its listings annually (typically in February–March). This scraper always retrieves current live data from their website.

**Does this require login or cookies?**
No. All data is publicly accessible on guide.michelin.com without authentication.

**What countries are supported?**
The scraper supports all countries covered by the Michelin Guide, including France, Japan, United States, United Kingdom, Italy, Spain, Germany, Singapore, Hong Kong, South Korea, and 20+ more. Use `mode=starredRestaurants` without a `country` filter to browse globally.

**How does the star filter work?**
The scraper uses Michelin's dedicated listing pages for each distinction tier (e.g. `/en/restaurants/3-stars-michelin`). These return only restaurants of that tier, making the star filter fast and accurate. When combined with a country filter, a country-scoped URL is used (e.g. `/en/fr/restaurants/3-stars-michelin` for France).

**Why might some fields be missing?**
Fields are only emitted when Michelin provides the data. Phone, website, coordinates, and opening hours require `includeDetails: true` (visits each restaurant's detail page). Cuisine may be absent on some listing cards for certain Asian restaurants — enable `includeDetails` for complete cuisine data.

**What is the difference between Bib Gourmand and Michelin Selected?**
Bib Gourmand recognizes restaurants offering excellent quality at moderate prices. Michelin Selected (formerly "Michelin Plate") identifies restaurants serving good food that Michelin recommends, but which have not yet received a star.

**How many restaurants are in the Michelin Guide?**
The guide covers thousands of restaurants across 40+ countries. The global starred list has roughly 3,000+ establishments (1-star through 3-star combined), plus several thousand Bib Gourmand and Michelin Selected restaurants.

**Why do some country filters return restaurants from other countries?**
For certain countries (UK, South Korea), Michelin's CDN may serve the global listing from US datacenter IPs instead of the country-specific page. For these countries, use `mode=byCity` with a specific city name for reliable results.

# Actor input Schema

## `mode` (type: `string`):

What to fetch from the Michelin Guide.

## `searchQuery` (type: `string`):

Restaurant name or keyword to search for (mode=search).

## `city` (type: `string`):

City name to browse restaurants in (mode=byCity), e.g. `Paris`, `Tokyo`, `New York`.

## `country` (type: `string`):

Filter by country slug used in Michelin Guide URLs. Use lowercase slug format (e.g. 'france', 'japan', 'united-states'). The value is automatically normalized to lowercase if entered manually.

## `starFilter` (type: `string`):

Filter restaurants by Michelin distinction (applies to all modes).

## `cuisineFilter` (type: `string`):

Filter by cuisine type. Note: 'Classic Cuisine' and 'Traditional Cuisine' are how Michelin labels most French/regional cuisine in France — use those options to find French cuisine restaurants in Paris, Lyon, etc. 'French' matches restaurants explicitly labeled 'French' by Michelin, which is more common outside France.

## `startUrls` (type: `array`):

List of Michelin Guide restaurant page URLs to scrape (mode=byUrl). Each item must have a `url` key, e.g. `https://guide.michelin.com/en/ile-de-france/paris/restaurant/guy-savoy`.

## `maxItems` (type: `integer`):

Maximum number of restaurant records to emit.

## `includeDetails` (type: `boolean`):

If enabled, the scraper visits each individual restaurant page for additional data (phone, website, geo-coordinates, opening hours, full description). Note: detail pages may be rate-limited or blocked in some regions; listing data is always scraped regardless of this setting.

## `proxyConfiguration` (type: `object`):

Apify proxy settings. AUTO datacenter proxy is used by default for Michelin Guide bot-detection bypass.

## Actor input object example

```json
{
  "mode": "starredRestaurants",
  "country": "",
  "starFilter": "",
  "cuisineFilter": "",
  "startUrls": [],
  "maxItems": 5,
  "includeDetails": false,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}
```

# Actor output Schema

## `restaurants` (type: `string`):

Dataset containing all scraped Michelin Guide restaurant records. Each record includes name, URL, stars/bibGourmand/michelinSelected distinction, city, country, cuisine, priceRange, countryCode, hasOnlineBooking, and (when includeDetails=true) address, phone, website, latitude, longitude, imageUrl, description, and openingHours.

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
    "mode": "starredRestaurants",
    "country": "",
    "starFilter": "",
    "cuisineFilter": "",
    "startUrls": [],
    "maxItems": 5,
    "includeDetails": false,
    "proxyConfiguration": {
        "useApifyProxy": true
    }
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/michelin-guide-scraper").call(input);

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
    "mode": "starredRestaurants",
    "country": "",
    "starFilter": "",
    "cuisineFilter": "",
    "startUrls": [],
    "maxItems": 5,
    "includeDetails": False,
    "proxyConfiguration": { "useApifyProxy": True },
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/michelin-guide-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "mode": "starredRestaurants",
  "country": "",
  "starFilter": "",
  "cuisineFilter": "",
  "startUrls": [],
  "maxItems": 5,
  "includeDetails": false,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}' |
apify call crawlerbros/michelin-guide-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/michelin-guide-scraper",
                "--header",
                "Authorization: Bearer <YOUR_API_TOKEN>"
            ]
        }
    }
}

```

## OpenAPI specification

Download the OpenAPI definition: https://api.apify.com/v2/actors/Ax3sazoetGu3LEIE3/builds/rlBu2bQESmzhlcwk9/openapi.json

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/michelin-guide-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
