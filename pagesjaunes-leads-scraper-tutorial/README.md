# French Business Directory Leads Scraper Tutorial: Run This Apify Actor with Python

Unofficial: Scrape business listings from PagesJaunes.fr (French Yellow Pages) with full contact details: emails, phone numbers, addresses, geolocation, ratings, opening hours, and business metadata.

This repository shows how to run [French Business Directory Leads Scraper](https://apify.com/crawlerbros/pagesjaunes-leads-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/pagesjaunes-leads-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/pagesjaunes-leads-scraper](https://apify.com/crawlerbros/pagesjaunes-leads-scraper)
- **SEO title:** French Business Directory Leads Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Unofficial: Scrape business listings from PagesJaunes.fr (French Yellow Pages) with full contact details: emails, phone numbers, addresses, geolocation, ratings, opening hours, and business metadata.

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

# PagesJaunes.fr Leads Scraper with Emails & Phones

Extract business leads from PagesJaunes.fr (French Yellow Pages) including emails, phone numbers, full addresses, geolocation, ratings, opening hours, and business metadata.

## What does PagesJaunes.fr Leads Scraper do?

This actor scrapes business listings from PagesJaunes.fr, the largest French business directory. It extracts complete contact information for lead generation, market research, and business intelligence.

Search by business type and location, or provide direct PagesJaunes URLs. Each listing includes full contact details extracted from the business detail page.

## Input

| Parameter | Type | Description |
|-----------|------|-------------|
| `search` | String | What or who to search for (e.g., "plombier", "restaurant") |
| `location` | String | City or area (e.g., "Paris", "Lyon", "Marseille") |
| `startUrls` | Array | Direct PagesJaunes search URLs (alternative to search/location) |
| `maxItems` | Number | Maximum number of results (default: 100) |

Provide either `search` + `location` or `startUrls` (or both).

## Output

Each result contains the following fields:

| Field | Description |
|-------|-------------|
| `name` | Business name |
| `phone` | Phone number |
| `email` | Email address |
| `website` | Business website URL |
| `address` | Full street address |
| `city` | City |
| `zipCode` | Postal code |
| `category` | Business type/activity |
| `description` | Business description |
| `rating` | Average rating (out of 5) |
| `reviewCount` | Number of reviews |
| `openingHours` | Business hours |
| `latitude` | GPS latitude |
| `longitude` | GPS longitude |
| `siret` | French business registration (SIRET) |
| `photos` | Business photo URLs |
| `socialMedia` | Social media profile links |
| `pagesJaunesUrl` | Direct PagesJaunes listing URL |
| `scrapedAt` | When the data was scraped |

Only fields with actual data are included — no empty or null values.

## Example Output

```json
{
    "name": "Plomberie Martin",
    "phone": "01 23 45 67 89",
    "email": "contact@plomberie-martin.fr",
    "website": "https://www.plomberie-martin.fr",
    "address": "12 Rue de la Paix",
    "city": "Paris",
    "zipCode": "75002",
    "category": "Plombier",
    "description": "Plomberie générale, dépannage et installation",
    "rating": 4.5,
    "reviewCount": 42,
    "openingHours": "Lun-Ven: 8h-18h; Sam: 9h-12h",
    "latitude": 48.8698,
    "longitude": 2.3311,
    "siret": "12345678901234",
    "photos": ["https://example.com/photo1.jpg"],
    "socialMedia": {"facebook": "https://facebook.com/plomberie-martin"},
    "pagesJaunesUrl": "https://www.pagesjaunes.fr/pros/12345678",
    "scrapedAt": "2026-04-08T10:30:00.000Z"
}
```

## Use Cases

- **Lead Generation**: Find business contacts in any French city by industry
- **Market Research**: Analyze business density, ratings, and reviews by area
- **Competitor Analysis**: Map competitors in specific locations
- **Business Directory**: Build local business databases with verified contact info
- **Sales Prospecting**: Generate prospect lists with phone numbers and emails

## FAQ

**How many results can I scrape?**
You can scrape up to thousands of listings per run. Use the `maxItems` parameter to control the volume.

**What locations are supported?**
Any location in France — cities, departments, postal codes, and neighborhoods.

**How fresh is the data?**
Data is scraped in real-time from PagesJaunes.fr. Each result includes a `scrapedAt` timestamp.

**Are all fields always available?**
Not all businesses have every field (e.g., email, website, SIRET). Only fields with actual data are included in the output.

**Can I search for specific business types?**
Yes, use the `search` field with any business type, service, or company name in French (e.g., "avocat", "dentiste", "restaurant italien").

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/pagesjaunes-leads-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
