# Kickstarter Project Scraper Tutorial: Run This Apify Actor with Python

Extract crowdfunding project data from Kickstarter like name, blurb, goal, pledged amount, backers, deadline, creator, category, country, and more. Uses the public search API for reliable results.

This repository shows how to run [Kickstarter Project Scraper](https://apify.com/crawlerbros/kickstarter-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/kickstarter-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/kickstarter-scraper](https://apify.com/crawlerbros/kickstarter-scraper)
- **SEO title:** Kickstarter Project Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract crowdfunding project data from Kickstarter like name, blurb, goal, pledged amount, backers, deadline, creator, category, country, and more. Uses the public search API for reliable results.

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

# Kickstarter Project Scraper

Extract crowdfunding project data from **Kickstarter.com** — name, description, funding goal, pledged amount, backers, deadline, creator, category, country, and more. Uses the public Kickstarter search API for 100% reliable structured data.

## Features

- **31 output fields** per project — complete API data in clean flat format
- **Search by keyword** with filters for state, sort order, category
- **Pagination** — fetch up to 2000 projects per run
- **No proxy needed** — Kickstarter's public search API is accessible with Chrome TLS impersonation
- **Fast** — ~20 projects/second via the official API
- **No nulls** — every field has a typed default

## Input

| Field | Type | Description |
|---|---|---|
| `searchQueries` | Array | Keywords to search on Kickstarter (e.g., `"smartwatch"`) |
| `state` | String | Filter by state: `any`, `live`, `successful`, `failed`, `canceled`, `submitted` (default `any`) |
| `sort` | String | Sort order: `popularity`, `newest`, `end_date`, `most_funded`, `most_backed` (default `popularity`) |
| `maxResults` | Integer | Max projects to return (default 50, max 2000) |

### Example Input

```json
{
    "searchQueries": ["smartwatch", "board game"],
    "state": "live",
    "sort": "popularity",
    "maxResults": 100
}
```

## Output

Each project has **31 fields**:

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | Integer | Kickstarter project ID |
| `url` | String | Project URL |
| `slug` | String | URL slug |
| `name` | String | Project name |
| `blurb` | String | Short description |

### Funding
| Field | Type | Description |
|---|---|---|
| `goal` | Number | Funding goal |
| `pledged` | Number | Amount pledged |
| `usdPledged` | Number | Amount pledged (USD) |
| `percentFunded` | Number | % of goal funded |
| `currency` | String | Currency code |
| `currencySymbol` | String | Currency symbol |
| `backersCount` | Integer | Number of backers |

### Status
| Field | Type | Description |
|---|---|---|
| `state` | String | `live`, `successful`, `failed`, `canceled`, `submitted` |
| `staffPick` | Boolean | Featured as staff pick |
| `spotlight` | Boolean | Featured in spotlight |

### Dates
| Field | Type | Description |
|---|---|---|
| `deadline` | String | Campaign deadline (ISO 8601) |
| `launchedAt` | String | Launch date (ISO 8601) |
| `createdAt` | String | Creation date (ISO 8601) |

### Location & Category
| Field | Type | Description |
|---|---|---|
| `country` | String | Country code |
| `countryName` | String | Country name |
| `location` | String | City/region |
| `category` | String | Category name |
| `categorySlug` | String | Category slug |

### Creator & Media
| Field | Type | Description |
|---|---|---|
| `creatorName` | String | Creator name |
| `creatorUrl` | String | Creator profile URL |
| `creatorAvatar` | String | Creator avatar image |
| `photoFull` | String | Full-size project photo |
| `photoThumb` | String | Thumbnail photo |
| `videoUrl` | String | Project video URL |

| `query` | String | Search query that matched |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "id": 1399308374,
    "url": "https://www.kickstarter.com/projects/ridebeeline/beeline-moto-ii-...",
    "slug": "beeline-moto-ii-beautifully-simple-nav-for-motorcyclists",
    "name": "Beeline Moto II | Beautifully Simple Motorcycle Navigation",
    "blurb": "Easily plan, navigate and track fantastic motorcycling routes...",
    "state": "successful",
    "staffPick": true,
    "goal": 50000,
    "pledged": 516295,
    "usdPledged": 651140.5,
    "percentFunded": 1032.59,
    "currency": "GBP",
    "currencySymbol": "£",
    "backersCount": 2645,
    "deadline": "2024-03-15T11:20:01+00:00",
    "country": "GB",
    "countryName": "United Kingdom",
    "category": "Product Design",
    "creatorName": "Beeline",
    "photoFull": "https://ksr-ugc.imgix.net/...",
    "scrapedAt": "2026-04-10T12:00:00+00:00"
}
```

## FAQ

**Q: Does this need an API key?**
No — Kickstarter's `search.json` endpoint is publicly accessible. The scraper uses Chrome TLS impersonation to bypass basic bot detection.

**Q: How many projects can I scrape per run?**
Up to 2000 per run (with pagination). For larger datasets, run multiple searches with different queries.

**Q: Can I filter by category or country?**
Filter by category by including the category name in your search query (e.g., `"board game"` or `"tabletop"`). Country filtering requires post-processing.

**Q: How fresh is the data?**
Live — each run queries the Kickstarter API directly, returning real-time project data.

## Use Cases

- **Crowdfunding market research** — track trends in product categories
- **Competitive intelligence** — monitor similar projects before launching yours
- **Investment research** — discover high-growth crowdfunded products
- **Product discovery** — find innovative projects before they go mainstream
- **Creator outreach** — identify active creators for partnerships

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/kickstarter-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
