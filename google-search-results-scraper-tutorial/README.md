# Google Search Results Scraper Tutorial: Run This Apify Actor with Python

Scrape Google Search result pages (SERPs) and extract structured data: organic results, paid ads, related queries, and People Also Ask. Supports country/language targeting, time filters, pagination, and CSV-friendly output.

This repository shows how to run [Google Search Results Scraper](https://apify.com/crawlerbros/google-search-results-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-search-results-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-search-results-scraper](https://apify.com/crawlerbros/google-search-results-scraper)
- **SEO title:** Google Search Results Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Google Search result pages (SERPs) and extract structured data: organic results, paid ads, related queries, and People Also Ask. Supports country/language targeting, time filters, pagination, and CSV-friendly output.

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

# Google Search Results (SERP) Scraper

Scrape Google Search result pages and get structured data from any query. Extract organic results, related searches, People Also Ask questions, and more — all in clean JSON or CSV format.

## What does Google Search Results Scraper do?

This scraper lets you search Google at scale and collect structured data from the results. Just enter your search queries and get back organized results including:

- Organic search results (title, URL, description, position)
- Related search queries
- People Also Ask questions
- Result counts and pagination info
- Product info (ratings, prices) when available
- Site links for brand results

It works across 48 countries and supports language targeting, time filters, mobile results, and multi-page pagination.

## How to use

1. **Enter your search queries** — Add one or more search terms
2. **Choose a country** — Select from 48 countries (US by default)
3. **Set filters** — Optionally filter by time period, language, or mobile view
4. **Run the scraper** — Results appear in the dataset within seconds

No login or API key needed. The scraper handles proxy rotation and rate limiting automatically.

## Input options

| Option | Description | Default |
|--------|-------------|---------|
| Search Queries | List of queries to search | Required |
| Country | Target country (determines Google domain) | United States |
| Language | Result language (e.g., en, de, fr) | Default |
| Max Results | Maximum results per query (1-200) | 100 |
| Max Pages | Pages to crawl per query (1-10) | 1 |
| Results Per Page | Results per page (10-100) | 10 |
| Time Period | Filter: any time, past hour/day/week/month/year | Any time |
| Mobile Results | Get mobile version of search results | Off |
| CSV Friendly Output | One result per row (for CSV/Excel export) | Off |

## Output example

Each run produces a dataset with structured results. Here's what a typical result looks like:

```json
{
  "searchQuery": {
    "term": "Hotels in NYC",
    "page": 1,
    "type": "SEARCH",
    "domain": "google.com",
    "countryCode": "us",
    "languageCode": "en",
    "resultsPerPage": 10
  },
  "url": "https://www.google.com/search?q=Hotels+in+NYC&num=10&hl=en&gl=us",
  "hasNextPage": true,
  "resultsTotal": 1380000000,
  "organicResults": [
    {
      "position": 1,
      "title": "THE 10 BEST Hotels in New York City",
      "url": "https://www.tripadvisor.com/Hotels-g60763-New_York_City-Hotels.html",
      "displayedUrl": "https://www.tripadvisor.com › Hotels",
      "description": "Some of the best hotels in New York City are...",
      "emphasizedKeywords": ["best hotels in New York City"],
      "siteLinks": []
    }
  ],
  "paidResults": [],
  "relatedQueries": [
    {
      "title": "Cheap hotels in NYC",
      "url": "https://www.google.com/search?q=Cheap+hotels+in+NYC"
    }
  ],
  "peopleAlsoAsk": [
    {
      "question": "What is the best area to stay in NYC?",
      "answer": "",
      "url": "",
      "title": ""
    }
  ]
}
```

## Use cases

- **SEO monitoring** — Track your website's ranking position for target keywords over time
- **Competitor analysis** — See who ranks for the same keywords and what their listings look like
- **Market research** — Discover what questions people ask about your industry (People Also Ask)
- **Content ideas** — Find related search queries to plan your content strategy
- **Price monitoring** — Collect product pricing data from search results
- **Lead generation** — Find businesses and websites ranking for specific services

## Supported countries

United States, United Kingdom, Canada, Australia, Germany, France, Spain, Italy, Brazil, Mexico, India, Japan, South Korea, Netherlands, Belgium, Austria, Switzerland, Sweden, Norway, Denmark, Finland, Poland, Czech Republic, Portugal, Ireland, New Zealand, South Africa, Singapore, Hong Kong, Taiwan, Philippines, Thailand, Indonesia, Malaysia, Vietnam, Argentina, Chile, Colombia, Peru, Turkey, Russia, Ukraine, Israel, UAE, Saudi Arabia, Egypt, Nigeria, Kenya

## Export options

Results can be exported as JSON, CSV, Excel, HTML, XML, or RSS. Enable **CSV Friendly Output** to get one result per row — ideal for spreadsheet analysis.

## Integrations

Connect this scraper with your existing tools using the Apify API. Automate your workflow by integrating with Zapier, Make, Google Sheets, Slack, and more. Schedule runs to collect data on a regular basis.

## FAQ

**How many results can I get?**
Up to 200 results per query across up to 10 pages of search results.

**Does it work for non-English searches?**
Yes. Set the country and language to get localized results in any supported language.

**Can I filter results by date?**
Yes. Use the Time Period option to limit results to the past hour, day, week, month, or year.

**What about Google Ads / paid results?**
Google loads ads via JavaScript after the initial page load. Since this scraper uses fast HTTP requests, paid ads are not captured. All organic results, related queries, and People Also Ask data are fully extracted.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-search-results-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
