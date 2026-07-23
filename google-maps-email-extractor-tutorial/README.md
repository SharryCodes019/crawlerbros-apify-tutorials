# Google Maps Email Extractor Tutorial: Run This Apify Actor with Python

Extract business emails, phone numbers, and social media links from Google Maps. Search for businesses by query, get contact details, addresses, ratings, and websites enriched with email addresses.

This repository shows how to run [Google Maps Email Extractor](https://apify.com/crawlerbros/google-maps-email-extractor) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-email-extractor`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-email-extractor](https://apify.com/crawlerbros/google-maps-email-extractor)
- **SEO title:** Google Maps Email Extractor Tutorial: Run This Apify Actor with Python
- **Description:** Extract business emails, phone numbers, and social media links from Google Maps. Search for businesses by query, get contact details, addresses, ratings, and websites enriched with email addresses.

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

# Google Maps Email Extractor

Extract business emails, phone numbers, social media links, and contact details from Google Maps. Search for any type of business in any location and get enriched lead data including email addresses scraped from business websites.

## What does Google Maps Email Extractor do?

This actor searches Google Maps for businesses matching your queries, extracts detailed business information (name, address, phone, rating, website), and then visits each business website to find email addresses and social media profiles. Perfect for lead generation, sales prospecting, and market research.

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `searchQueries` | string[] | Yes | `["restaurants in New York"]` | Search terms for Google Maps. Each query is searched separately. |
| `maxPlacesPerSearch` | integer | No | 20 | Maximum businesses to extract per search query (1-100). |
| `language` | string | No | `"en"` | Language code for Google Maps results (e.g., `en`, `es`, `fr`). |
| `deepEnrichment` | boolean | No | `true` | Visit business websites to extract emails and social links. Disable for faster Google Maps-only data. |

## Example Input

```json
{
    "searchQueries": [
        "restaurants in New York",
        "dentists in Los Angeles"
    ],
    "maxPlacesPerSearch": 20,
    "language": "en",
    "deepEnrichment": true
}
```

## Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Business name |
| `categoryName` | string | Primary business category |
| `address` | string | Full address |
| `phone` | string | Phone number |
| `website` | string | Business website URL |
| `totalScore` | number | Google Maps rating (1-5) |
| `reviewsCount` | integer | Number of Google reviews |
| `placeId` | string | Google Place ID |
| `url` | string | Google Maps URL |
| `location` | object | `{lat, lng}` coordinates |
| `priceLevel` | string | Price range (e.g., `$$`) |
| `plusCode` | string | Google Plus Code |
| `emails` | string[] | Email addresses found on website |
| `socialLinks` | object | Social media profile URLs |
| `scrapedAt` | string | ISO 8601 timestamp |

### Social Links Object

| Field | Description |
|-------|-------------|
| `socialLinks.facebook` | Facebook page URL |
| `socialLinks.instagram` | Instagram profile URL |
| `socialLinks.linkedin` | LinkedIn company/profile URL |
| `socialLinks.twitter` | Twitter/X profile URL |
| `socialLinks.youtube` | YouTube channel URL |
| `socialLinks.tiktok` | TikTok profile URL |

## Example Output

```json
{
    "title": "Joe's Pizza",
    "categoryName": "Pizza restaurant",
    "address": "7 Carmine St, New York, NY 10014",
    "phone": "+1 212-366-1182",
    "website": "https://www.joespizzanyc.com",
    "totalScore": 4.4,
    "reviewsCount": 12500,
    "placeId": "ChIJd3dF_VBZwokRAAFm3WMspbk",
    "url": "https://www.google.com/maps/place/Joe's+Pizza/...",
    "location": {
        "lat": 40.7306,
        "lng": -74.0022
    },
    "priceLevel": "$$",
    "plusCode": "P295+HJ New York",
    "emails": ["info@joespizzanyc.com"],
    "socialLinks": {
        "facebook": "https://facebook.com/joespizzanyc",
        "instagram": "https://instagram.com/joespizzanyc",
        "linkedin": null,
        "twitter": "https://twitter.com/joespizzanyc",
        "youtube": null,
        "tiktok": null
    },
    "scrapedAt": "2026-03-16T12:00:00+00:00"
}
```

## How It Works

1. **Search** — Searches Google Maps for businesses matching your queries
2. **Extract** — Visits each business listing to get name, address, phone, rating, website, and more
3. **Enrich** — Scans each business website for email addresses and social media links
4. **Output** — Saves all data to the dataset in a flat, easy-to-use format

## Use Cases

- **Lead generation** — Build targeted contact lists for sales outreach
- **Sales prospecting** — Find business emails and phone numbers by industry and location
- **Market research** — Analyze businesses, ratings, and categories in specific areas
- **Competitor analysis** — Map competitors and their online presence
- **Local SEO** — Audit business listings and contact information

## Tips

- **Search query format**: Use natural language like "restaurants in New York" or "plumbers near Chicago, IL"
- **Specific queries work better**: "Italian restaurants in Manhattan" yields more relevant results than just "restaurants"
- **Deep enrichment**: Disable `deepEnrichment` if you only need Google Maps data (name, phone, address, rating) — this makes the scraper significantly faster
- **Deduplication**: When using multiple queries that may overlap, results are automatically deduplicated by Google Place ID

## Limitations

- Google Maps shows a maximum of ~120 businesses per search area
- Some businesses don't have websites, so email extraction won't work for those
- Email addresses are extracted from publicly visible website content only
- Social media links are found by scanning website HTML for known social media URLs
- Results depend on Google Maps' search relevance for your query

## FAQ

**How many businesses can I scrape per run?**
You can scrape up to 100 businesses per search query. Use multiple queries to cover more businesses.

**Does this actor need cookies or login?**
No. Google Maps search results are publicly accessible without authentication.

**Why are some email fields empty?**
Not all businesses have websites, and not all websites display email addresses publicly. The scraper checks the main page and common contact pages (e.g., /contact, /about).

**Can I search in languages other than English?**
Yes, set the `language` parameter to your preferred language code (e.g., `es` for Spanish, `fr` for French).

**How long does a typical run take?**
A search for 20 businesses with email enrichment typically takes 2-5 minutes. Without enrichment, it's about 1-2 minutes.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-email-extractor)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
