# Similarweb Scraper Tutorial: Run This Apify Actor with Python

Get website traffic analytics, rankings, traffic sources, top keywords, and AI traffic data from SimilarWeb. Analyze any domain - no API key or authentication needed.

This repository shows how to run [Similarweb Scraper](https://apify.com/crawlerbros/similarweb-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/similarweb-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/similarweb-scraper](https://apify.com/crawlerbros/similarweb-scraper)
- **SEO title:** Similarweb Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Get website traffic analytics, rankings, traffic sources, top keywords, and AI traffic data from SimilarWeb. Analyze any domain - no API key or authentication needed.

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

# SimilarWeb Scraper

Extract website traffic analytics, rankings, traffic sources, top keywords, and AI traffic insights from SimilarWeb. Analyze any domain in bulk — no API key, login, or SimilarWeb account required.

## What can this scraper do?

- **Traffic analytics** — Get total monthly visits, bounce rate, pages per visit, and average time on site
- **Global and category rankings** — See where a website ranks globally, in its country, and within its category
- **Traffic source breakdown** — Understand how much traffic comes from direct, search, social, referrals, email, and paid sources
- **Top keywords** — Discover the top search keywords driving traffic, with search volume and CPC data
- **AI traffic insights** — See which AI chatbots (ChatGPT, Perplexity, etc.) are sending traffic to a website
- **Top AI prompts** — Find out what prompts users ask AI chatbots that mention this website
- **Historical data** — Get 3 months of estimated monthly visit history
- **Bulk analysis** — Analyze hundreds of domains in a single run
- **Geographic distribution** — See the top 5 countries by traffic share

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domains` | String list | Yes | List of website domains to analyze. Accepts various formats: `google.com`, `https://google.com`, `www.google.com` — the scraper normalizes them automatically. |
| `maxItems` | Integer | No | Maximum number of domains to process (default: 100, max: 5000). Use this to limit a large input list. |

## Example Input

### Single domain
```json
{
    "domains": ["google.com"]
}
```

### Multiple domains for competitive analysis
```json
{
    "domains": [
        "google.com",
        "bing.com",
        "duckduckgo.com",
        "yahoo.com"
    ]
}
```

### Various URL formats (all normalized automatically)
```json
{
    "domains": [
        "https://www.reddit.com/r/popular",
        "facebook.com",
        "www.twitter.com",
        "http://apify.com"
    ]
}
```

## Output

Each domain produces one row in the dataset with the following fields:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `domain` | String | The analyzed domain | `google.com` |
| `title` | String | Website title | `Google` |
| `description` | String | Website description | `Learn about Google...` |
| `category` | String | SimilarWeb category | `computers_electronics_and_technology/search_engines` |
| `globalRank` | Integer | Global traffic rank | `1` |
| `countryRank` | Integer | Rank in the site's top country | `1` |
| `countryRankCountry` | String | Country code for country rank | `US` |
| `categoryRank` | Integer | Rank within category | `1` |
| `categoryName` | String | Category name for ranking | `Computers_Electronics_and_Technology/Search_Engines` |
| `totalVisits` | Number | Total monthly visits | `85756574615` |
| `bounceRate` | Number | Bounce rate (0-1 decimal) | `0.283585` |
| `pagesPerVisit` | Number | Average pages per visit | `8.52` |
| `timeOnSite` | Number | Average time on site (seconds) | `610.41` |
| `engagementMonth` | String | Engagement data month | `2026-01` |
| `estimatedMonthlyVisits` | String (JSON) | 3 months of visit history | `{"2025-11-01": 82284033110, ...}` |
| `trafficSourceDirect` | Number | Direct traffic share (0-1) | `0.858270` |
| `trafficSourceSearch` | Number | Search traffic share (0-1) | `0.083459` |
| `trafficSourceSocial` | Number | Social traffic share (0-1) | `0.007599` |
| `trafficSourceReferrals` | Number | Referral traffic share (0-1) | `0.044567` |
| `trafficSourceMail` | Number | Email traffic share (0-1) | `0.002837` |
| `trafficSourcePaidReferrals` | Number | Paid referral share (0-1) | `0.003267` |
| `topCountries` | String (JSON) | Top 5 countries by traffic | `[{"countryCode": "US", "share": 0.2459}, ...]` |
| `topKeywords` | String (JSON) | Top keywords with metrics | `[{"name": "gemini", "volume": 100378910, "cpc": 0.42, ...}]` |
| `aiTrafficSplit` | String (JSON) | AI platforms sending traffic | `[{"name": "chatgpt.com", "rank": 1}, ...]` |
| `aiChatbotDistribution` | String (JSON) | AI chatbot traffic distribution | `[{"name": "chatgpt.com", "value": 59.83}, ...]` |
| `aiTotalVisits` | Number | Total AI-sourced visits | `500000000` |
| `topPrompts` | String (JSON) | AI prompts mentioning this site | `["What is the most popular search engine?", ...]` |
| `isSmall` | Boolean | Small/low-traffic site flag | `false` |
| `screenshot` | String | Website screenshot URL | `https://site-images.similarcdn.com/...` |
| `snapshotDate` | String | Data snapshot date | `2026-01-01T00:00:00+00:00` |
| `scrapeTimestamp` | String | When data was scraped | `2026-03-11T12:00:00+00:00` |

## Sample Output

```json
{
    "domain": "google.com",
    "title": "Google",
    "description": "Learn about the Certified Publisher Program...",
    "category": "computers_electronics_and_technology/search_engines",
    "globalRank": 1,
    "countryRank": 1,
    "countryRankCountry": "US",
    "categoryRank": 1,
    "categoryName": "Computers_Electronics_and_Technology/Search_Engines",
    "totalVisits": 85756574615,
    "bounceRate": 0.283585,
    "pagesPerVisit": 8.52,
    "timeOnSite": 610.41,
    "engagementMonth": "2026-01",
    "trafficSourceDirect": 0.858270,
    "trafficSourceSearch": 0.083459,
    "trafficSourceSocial": 0.007599,
    "trafficSourceReferrals": 0.044567,
    "trafficSourceMail": 0.002837,
    "trafficSourcePaidReferrals": 0.003267,
    "topCountries": "[{\"countryCode\": \"US\", \"share\": 0.2459}, ...]",
    "topKeywords": "[{\"name\": \"gemini\", \"volume\": 100378910, \"cpc\": 0.42, \"estimatedValue\": 151798290}]",
    "aiTrafficSplit": "[{\"name\": \"chatgpt.com\", \"rank\": 1}]",
    "aiChatbotDistribution": "[{\"name\": \"chatgpt.com\", \"value\": 59.83}]",
    "aiTotalVisits": 500000000,
    "topPrompts": "[\"What is the most popular search engine?\"]",
    "isSmall": false,
    "screenshot": "https://site-images.similarcdn.com/image?url=...",
    "snapshotDate": "2026-01-01T00:00:00+00:00",
    "scrapeTimestamp": "2026-03-11T12:00:00.000000+00:00"
}
```

## FAQ

### Do I need a SimilarWeb account or API key?
No. This scraper works without any authentication, API key, or SimilarWeb account. It uses publicly available SimilarWeb data.

### How accurate is the data?
The data comes directly from SimilarWeb's analytics platform, the same source used by marketing professionals and analysts worldwide. Traffic estimates are based on SimilarWeb's panel-based methodology.

### What does the `isSmall` flag mean?
When `isSmall` is `true`, SimilarWeb does not have enough data for the domain. This typically happens with very small websites that don't have enough traffic to generate reliable estimates. The output row will still be created but metrics may be zero.

### How often is the data updated?
SimilarWeb updates their data monthly. The `snapshotDate` field shows the date of the most recent data snapshot. The `engagementMonth` field shows which month the engagement metrics correspond to.

### Can I analyze any domain?
Yes, you can analyze any website domain. Large, well-known websites will have the most comprehensive data. Smaller sites may return limited data (indicated by `isSmall: true`).

### What is AI traffic data?
SimilarWeb now tracks traffic that comes from AI chatbots like ChatGPT, Perplexity, and others. The `aiTrafficSplit` shows which AI platforms send traffic to the analyzed domain, and `aiChatbotDistribution` shows the percentage breakdown. The `topPrompts` field reveals what users ask AI chatbots that results in mentions of this website.

### What formats can I use for domain input?
The scraper accepts domains in many formats and normalizes them automatically:
- `google.com` (bare domain)
- `https://google.com` (with protocol)
- `www.google.com` (with www prefix)
- `https://www.google.com/search?q=test` (with path and query — stripped automatically)

### How many domains can I analyze in one run?
You can analyze up to 5,000 domains in a single run. The scraper processes them sequentially with a small delay between requests to ensure reliability.

### What are the traffic source percentages?
Traffic source values are decimals between 0 and 1 (not percentages). For example, `trafficSourceDirect: 0.858270` means 85.83% of traffic comes from direct visits. The six traffic sources (Direct, Search, Social, Referrals, Mail, Paid Referrals) sum to approximately 1.0.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/similarweb-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
