# Yelp Scraper Tutorial: Run This Apify Actor with Python

Extract business data, reviews, ratings, and contact information from Yelp. Search by keyword and location or scrape specific business pages

This repository shows how to run [Yelp Scraper](https://apify.com/crawlerbros/yelp-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/yelp-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/yelp-scraper](https://apify.com/crawlerbros/yelp-scraper)
- **SEO title:** Yelp Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract business data, reviews, ratings, and contact information from Yelp. Search by keyword and location or scrape specific business pages

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

# Yelp Scraper

Extract business data, reviews, ratings, contact information, and more from Yelp. Search by keyword and location or provide direct business URLs to scrape detailed information including customer reviews.

## Features

- **Search by keyword and location** - Find businesses matching your search terms across any location on Yelp
- **Direct URL scraping** - Provide specific Yelp business URLs for targeted data extraction
- **Business details** - Name, rating, review count, price range, phone, address, website, cuisine, categories
- **Customer reviews** - Review text, rating, date, photos, and reaction counts (Useful, Funny, Cool)
- **Structured output** - Clean JSON output with consistent field names and no null values
- **Configurable limits** - Control how many search results and reviews to collect
- **Proxy support** - Optional proxy configuration for large-scale scraping

## Input Parameters

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `searchTerms` | Array of strings | `[]` | Search queries (e.g., "pizza", "plumber", "hair salon") |
| `locations` | Array of strings | `[]` | Locations to search (e.g., "New York, NY", "Los Angeles, CA") |
| `directUrls` | Array of URLs | `[]` | Direct Yelp business page URLs to scrape |
| `searchLimit` | Integer | `10` | Maximum results per search query (1-100) |
| `reviewLimit` | Integer | `5` | Maximum reviews per business (0-50, set 0 to skip reviews) |
| `proxy` | Object | - | Proxy configuration (residential recommended for scale) |

You must provide at least one of `searchTerms` or `directUrls`.

## Output Fields

Each business in the dataset contains:

| Field | Type | Description |
|-------|------|-------------|
| `directUrl` | String | Full Yelp URL of the business page |
| `bizId` | String | Yelp business slug identifier |
| `name` | String | Business name |
| `description` | String | Business description from meta tags |
| `categories` | Array | List of business categories (e.g., "Pizza", "Italian") |
| `type` | String | Business type from structured data (e.g., "Restaurant") |
| `phone` | String | Business phone number |
| `reviewCount` | String | Total number of reviews |
| `aggregatedRating` | String | Average star rating (e.g., "4.5") |
| `priceRange` | String | Price level (e.g., "$", "$$", "$$$") |
| `cuisine` | String | Cuisine type if applicable |
| `website` | String | Business website URL |
| `images` | Array | List of business image URLs |
| `address` | Object | Address with streetAddress, addressLocality, addressRegion, postalCode, addressCountry |
| `reviews` | Array | List of review objects |

### Review Object Fields

| Field | Type | Description |
|-------|------|-------------|
| `date` | String | Review date |
| `rating` | String | Star rating (1-5) |
| `text` | String | Review text content |
| `photos` | Array | URLs of photos attached to the review |
| `isUsefulCount` | Integer | Number of "Useful" reactions |
| `isFunnyCount` | Integer | Number of "Funny" reactions |
| `isCoolCount` | Integer | Number of "Cool" reactions |

## Supported URL Formats

- Business pages: `https://www.yelp.com/biz/business-name-city`
- Business pages with location: `https://www.yelp.com/biz/business-name-city-2`

## Example Input

### Search for businesses
```json
{
    "searchTerms": ["pizza", "sushi"],
    "locations": ["New York, NY", "San Francisco, CA"],
    "searchLimit": 5,
    "reviewLimit": 3
}
```

### Scrape specific businesses
```json
{
    "directUrls": [
        { "url": "https://www.yelp.com/biz/prince-street-pizza-new-york-2" },
        { "url": "https://www.yelp.com/biz/joes-pizza-new-york" }
    ],
    "reviewLimit": 10
}
```

## Example Output

```json
{
    "directUrl": "https://www.yelp.com/biz/prince-street-pizza-new-york-2",
    "bizId": "prince-street-pizza-new-york-2",
    "name": "Prince Street Pizza",
    "description": "Famous NYC pizza spot known for their spicy spring pepperoni square slice.",
    "categories": ["Pizza", "Italian"],
    "type": "Restaurant",
    "phone": "(212) 966-4100",
    "reviewCount": "5432",
    "aggregatedRating": "4.3",
    "priceRange": "$",
    "cuisine": "Pizza, Italian",
    "website": "https://princestreetpizza.com",
    "images": ["https://s3-media0.fl.yelpcdn.com/bphoto/example.jpg"],
    "address": {
        "streetAddress": "27 Prince St",
        "addressLocality": "New York",
        "addressRegion": "NY",
        "postalCode": "10012",
        "addressCountry": "US"
    },
    "reviews": [
        {
            "date": "Oct 15, 2024",
            "rating": "5",
            "text": "Best pizza in NYC! The spicy spring is a must-try...",
            "photos": [],
            "isUsefulCount": 12,
            "isFunnyCount": 2,
            "isCoolCount": 5
        }
    ]
}
```

## Use Cases

- **Market research** - Analyze competitor businesses, ratings, and customer feedback in any area
- **Competitor analysis** - Compare reviews, ratings, and pricing across similar businesses
- **Location intelligence** - Evaluate business density and quality in specific neighborhoods
- **Customer sentiment** - Aggregate and analyze customer reviews for trend detection
- **Lead generation** - Collect business contact information for outreach campaigns
- **Review monitoring** - Track reviews for specific businesses over time

## Tips for Best Results

- **Start with low limits** - Use `searchLimit: 3` and `reviewLimit: 2` for initial test runs
- **Use residential proxies** for large-scale scraping to avoid rate limiting
- **Direct URLs are faster** - If you already know which businesses to scrape, use `directUrls` instead of search
- **Each search term + location combination** counts as a separate search, so plan your queries accordingly
- **Reviews are from the first page** of the business listing; Yelp shows approximately 10 reviews per page

## Limitations

- Only publicly visible data is extracted
- Yelp uses Cloudflare protection which may occasionally block requests
- Reviews are limited to those visible on the business page (first page of reviews)
- Some business fields may be empty if not provided by the business owner
- Search results depend on Yelp's ranking algorithm and may vary

## FAQ

**How many businesses can I scrape in one run?**
There is no hard limit, but we recommend keeping runs under 100 businesses for reliability. Use multiple smaller runs for larger datasets.

**Do I need a proxy?**
For small runs (under 10 businesses), the scraper works without a proxy. For larger runs, residential proxies are recommended to avoid Cloudflare blocks.

**Why are some review fields empty?**
Yelp uses dynamic class names that can change. The scraper uses multiple extraction strategies, but some fields may occasionally be empty if Yelp changes their HTML structure.

**Can I scrape all reviews for a business?**
The scraper extracts reviews visible on the first page load. Set `reviewLimit` up to 50, but only reviews rendered on the page will be captured.

**What locations are supported?**
Any location that Yelp supports. Use the format "City, State" for US locations (e.g., "New York, NY") or city names for international locations.

**How often is the data updated?**
Each run fetches live data from Yelp. Schedule recurring runs on the Apify platform to keep your dataset up to date.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/yelp-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
