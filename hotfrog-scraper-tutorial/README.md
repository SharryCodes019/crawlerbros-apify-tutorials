# HotFrog Scraper Tutorial: Run This Apify Actor with Python

Scrape HotFrog.com - US local business directory with millions of business listings. Search by keyword and location to get business names, phone numbers, addresses, categories, and descriptions.

This repository shows how to run [HotFrog Scraper](https://apify.com/crawlerbros/hotfrog-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/hotfrog-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/hotfrog-scraper](https://apify.com/crawlerbros/hotfrog-scraper)
- **SEO title:** HotFrog Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape HotFrog.com - US local business directory with millions of business listings. Search by keyword and location to get business names, phone numbers, addresses, categories, and descriptions.

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

# HotFrog Business Directory Scraper

Extract US local business listings from [hotfrog.com](https://www.hotfrog.com) — one of the largest local business directories with millions of listings across the United States. Find businesses by keyword and location with phone numbers, addresses, descriptions, websites, and category information. No login or API key required.

## Features

- **Keyword + Location Search** — Find any type of business in any US city or state
- **Rich Business Data** — Phone number, address, city, state, description, website, category, and profile URL
- **Verified Badge Detection** — Identifies DesignRush verified businesses
- **Automatic Pagination** — Fetches multiple pages of results to reach your `maxItems` target
- **No Login Required** — All data is publicly available

## Use Cases

- Local business lead generation
- Business contact database building
- Market research and competitor analysis
- Local SEO auditing and citation tracking
- Building city-specific business directories

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `searchQuery` | String | No | `plumber` | Type of business to search for (e.g., `dentist`, `HVAC repair`) |
| `location` | String | No | `new-york` | City or location slug (e.g., `los-angeles`, `Chicago, IL`) |
| `maxItems` | Integer | No | `30` | Maximum businesses to return (1–500) |

### Example Input — Plumbers in New York

```json
{
  "searchQuery": "plumber",
  "location": "new-york",
  "maxItems": 50
}
```

### Example Input — Dentists in Los Angeles

```json
{
  "searchQuery": "dentist",
  "location": "Los Angeles, CA",
  "maxItems": 30
}
```

## Output

| Field | Type | Description |
|-------|------|-------------|
| `businessName` | String | Business display name |
| `businessId` | String | HotFrog internal business ID |
| `phone` | String | Business phone number |
| `address` | String | Street address |
| `city` | String | City name |
| `state` | String | 2-letter state code (e.g., `NY`) |
| `description` | String | Business description (up to 500 characters) |
| `website` | String | Business website URL |
| `category` | String | Business category derived from profile URL |
| `profileUrl` | String | Full HotFrog profile URL |
| `logoUrl` | String | Business logo URL (when available) |
| `verified` | Boolean | Whether the listing is verified |
| `searchQuery` | String | Search term used |
| `searchLocation` | String | Location searched |
| `recordType` | String | Always `business` |
| `scrapedAt` | String | ISO 8601 timestamp |
| `sourceUrl` | String | Source search results page URL |

### Example Output

```json
{
  "businessName": "Joe's Plumbing",
  "phone": "(212) 555-1234",
  "address": "123 Main St",
  "city": "New York",
  "state": "NY",
  "description": "Expert plumbing services available 24/7.",
  "website": "https://www.joesplumbing.com",
  "category": "Plumbers",
  "profileUrl": "https://www.hotfrog.com/find/united-states/new-york/plumber/joes-plumbing",
  "searchQuery": "plumber",
  "searchLocation": "new-york",
  "recordType": "business",
  "scrapedAt": "2025-01-15T10:23:45+00:00",
  "sourceUrl": "https://www.hotfrog.com/search/new-york/plumber"
}
```

## FAQ

**Does this require an API key or login?**
No. All listings on HotFrog are publicly accessible.

**How do I specify the location?**
You can use city names like `New York`, city-state like `Chicago, IL`, or URL slugs like `new-york`. The actor normalizes these into the correct URL format automatically.

**What types of businesses can I search for?**
Any business category works — `plumber`, `electrician`, `dentist`, `lawyer`, `restaurant`, `hair salon`, etc.

**How many results per page does HotFrog show?**
Typically 10–20 businesses per search results page. The actor automatically paginates to reach your `maxItems` limit.

**Are phone numbers always available?**
Not all listings include a phone number — the `phone` field is only included in the output when present.

**Is the data current?**
HotFrog business listings are maintained by business owners. Data freshness varies by listing; this scraper always fetches live data from HotFrog.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/hotfrog-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
