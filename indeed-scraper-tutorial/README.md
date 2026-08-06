# Indeed Keyword Scraper Tutorial: Run This Apify Actor with Python

Scrape job listings from Indeed. Search by keywords and location or provide direct Indeed URLs. Extract job titles, companies, salaries, locations, ratings, and more. No login or API key needed.

This repository shows how to run [Indeed Keyword Scraper](https://apify.com/crawlerbros/indeed-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/indeed-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/indeed-scraper](https://apify.com/crawlerbros/indeed-scraper)
- **SEO title:** Indeed Keyword Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape job listings from Indeed. Search by keywords and location or provide direct Indeed URLs. Extract job titles, companies, salaries, locations, ratings, and more. No login or API key needed.

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

# Indeed Scraper

Extract job listings from Indeed at scale. Search by keywords and location or provide direct Indeed search URLs. Get job titles, companies, salaries, locations, company ratings, remote work indicators, benefits, and more. No login, API key, or Indeed account needed.

## What can this scraper do?

- **Job search** — Search Indeed by keywords and location (e.g. "software engineer in New York")
- **Direct URL support** — Use any Indeed search URL with custom filters applied
- **Job snippets** — Short description previews for all listings
- **Salary data** — Extract salary ranges, types (yearly/hourly), and currency
- **Company info** — Get company names, ratings, and review counts
- **Remote work detection** — Identify remote, hybrid, and on-site positions
- **Benefits & job types** — Extract listed benefits and employment types
- **Bulk scraping** — Scrape hundreds of jobs across multiple searches
- **Deduplication** — Automatically removes duplicate listings across searches

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `searchQueries` | String list | No* | - | Job search queries. Use "in" to specify location: "software engineer in New York", "data scientist remote", "nurse in Chicago, IL". |
| `startUrls` | String list | No* | - | Direct Indeed search URLs. Use for advanced searches with specific filters. |
| `maxItems` | Integer | No | 50 | Maximum number of jobs to scrape (1-1000). |

*At least one of `searchQueries` or `startUrls` is required.

## Example Input

### Search by keyword and location
```json
{
    "searchQueries": ["software engineer in New York"],
    "maxItems": 50
}
```

### Multiple searches
```json
{
    "searchQueries": [
        "data scientist in San Francisco",
        "machine learning engineer remote"
    ],
    "maxItems": 100
}
```

### Direct Indeed URL with filters
```json
{
    "startUrls": [
        "https://www.indeed.com/jobs?q=nurse&l=Chicago%2C+IL&sc=0kf%3Ajt%28fulltime%29%3B&fromage=7"
    ],
    "maxItems": 30
}
```

## Output

Each job listing produces one row in the dataset:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `jobTitle` | String | Job title | `Senior Software Engineer` |
| `company` | String | Company name | `Google` |
| `location` | String | Full location | `New York, NY 10001` |
| `city` | String | City | `New York` |
| `state` | String | State | `NY` |
| `postalCode` | String | ZIP code | `10001` |
| `salaryMin` | Number | Minimum salary | `150000` |
| `salaryMax` | Number | Maximum salary | `220000` |
| `salaryType` | String | Salary period | `YEARLY` |
| `salaryCurrency` | String | Currency | `USD` |
| `salaryText` | String | Formatted salary | `$150,000 - $220,000 a year` |
| `companyRating` | Number | Company rating (0-5) | `4.2` |
| `companyReviewCount` | Number | Review count | `12543` |
| `remoteWork` | String | Remote type | `REMOTE_ALWAYS` |
| `jobTypes` | String (JSON) | Job types | `["Full-time"]` |
| `benefits` | String (JSON) | Benefits | `["Health insurance", "401(k)"]` |
| `postedTime` | String | When posted | `3 days ago` |
| `isSponsored` | Boolean | Sponsored listing | `false` |
| `indeedApply` | Boolean | Indeed Apply available | `true` |
| `jobKey` | String | Unique job ID | `6d573cd5d8e7a1fe` |
| `jobUrl` | String | Indeed job URL | `https://www.indeed.com/viewjob?jk=...` |
| `snippet` | String | Short description preview | `We are looking for a skilled...` |
| `datePosted` | String | Posted date (ISO) | `2026-03-10T05:00:00+00:00` |
| `validThrough` | String | Expiry date (ISO) | `` |
| `employmentType` | String | Employment type | `Full-time` |
| `searchQuery` | String | Search that found this | `software engineer in New York` |
| `scrapeTimestamp` | String | When scraped | `2026-03-11T12:00:00+00:00` |

**Note:** All listings include a short `snippet` preview, `datePosted`, and `employmentType`.

## Sample Output

```json
{
    "jobTitle": "Junior Software Engineer",
    "company": "Aspire Tech IT solution",
    "location": "New York, NY 10040",
    "city": "New York",
    "state": "NY",
    "postalCode": "10040",
    "salaryMin": 70000,
    "salaryMax": 95000,
    "salaryType": "YEARLY",
    "salaryCurrency": "USD",
    "salaryText": "$70,000 - $95,000 a year",
    "companyRating": 0,
    "companyReviewCount": 0,
    "remoteWork": "",
    "jobTypes": "[\"Full-time\"]",
    "benefits": "[\"Dental insurance\", \"401(k) matching\", \"Vision insurance\", \"Paid time off\"]",
    "postedTime": "20 days ago",
    "isSponsored": false,
    "indeedApply": true,
    "jobKey": "caa601f76d19adff",
    "jobUrl": "https://www.indeed.com/viewjob?jk=caa601f76d19adff",
    "snippet": "Debug, troubleshoot, and resolve software defects. Understanding of cloud-native application development...",
    "datePosted": "2026-02-19T06:00:00+00:00",
    "validThrough": "",
    "employmentType": "Full-time",
    "searchQuery": "software engineer in New York",
    "scrapeTimestamp": "2026-03-12T06:12:42.060352+00:00"
}
```

## FAQ

### Do I need an Indeed account or API key?
No. This scraper works without any login, API key, or Indeed account. It uses residential proxies (included in usage costs) to access Indeed job listings.

### What is the difference between searchQueries and startUrls?
`searchQueries` are simple text queries like "nurse in Chicago" that the scraper converts into Indeed search URLs. `startUrls` are full Indeed URLs that you copy from your browser after applying specific filters (experience level, date posted, job type, etc.).

### How many jobs can I scrape?
Each search query typically yields 40-50 unique job listings. To collect more jobs, add multiple search queries — for example, 3 queries can yield 100-150 unique listings. The maximum per run is 1,000 jobs.

### Why did the scraper return fewer jobs than expected?
Indeed uses anti-bot protection that can limit automated access. The scraper uses multiple strategies to maximize results, but the actual number may vary between runs. For best results, use specific search queries with location.

### What is the remoteWork field?
Possible values include `REMOTE_ALWAYS` (fully remote), `REMOTE_HYBRID` (partially remote), or empty (on-site/not specified).

### What are the salary fields?
`salaryMin` and `salaryMax` are numeric values. `salaryType` indicates the period: `YEARLY`, `HOURLY`, `MONTHLY`, or `WEEKLY`. `salaryText` is the human-readable format like "$150,000 - $220,000 a year". Not all listings include salary data.

### Can I search for jobs in specific countries?
This scraper uses indeed.com (US). For other countries, provide a direct `startUrls` from the country-specific Indeed site (e.g. indeed.co.uk).

### Are duplicate listings removed?
Yes. Each job has a unique `jobKey`. If the same job appears across multiple searches or search variations, it's only included once in the output.

### How fast is the scraper?
A typical search for 50 jobs completes in about 2 minutes.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/indeed-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
