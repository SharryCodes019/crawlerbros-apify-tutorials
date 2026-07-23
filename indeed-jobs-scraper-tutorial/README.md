# Indeed Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape jobs from Indeed worldwide. Search by keywords and location across 60+ countries. Get full job descriptions, salaries, company info, ratings, and more. No login or API key needed.

This repository shows how to run [Indeed Jobs Scraper](https://apify.com/crawlerbros/indeed-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/indeed-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/indeed-jobs-scraper](https://apify.com/crawlerbros/indeed-jobs-scraper)
- **SEO title:** Indeed Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape jobs from Indeed worldwide. Search by keywords and location across 60+ countries. Get full job descriptions, salaries, company info, ratings, and more. No login or API key needed.

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

# Indeed Jobs Scraper

Scrape job listings from Indeed across 60+ countries. Extract full job descriptions, salaries, company ratings, employment types, and more. No login or API key required.

## Features

- Search by job title/keywords and location
- Support for 60+ countries (US, UK, Canada, Germany, France, India, Australia, and more)
- Full job descriptions from detail pages
- Company ratings and review counts
- Salary information when available
- Optional company details (size, industry, overview)
- Optional external apply link resolution
- Automatic deduplication of results
- Direct Indeed URL support with pre-applied filters

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `position` | String | - | Job title or keywords (e.g., "web developer", "nurse") |
| `location` | String | - | City, state, ZIP code, or "remote" |
| `country` | Enum | US | Country to search (60+ supported) |
| `maxItemsPerSearch` | Integer | 100 | Maximum jobs to scrape (1-10,000) |
| `startUrls` | URL List | - | Direct Indeed search URLs with filters |
| `parseCompanyDetails` | Boolean | false | Fetch company size and overview |
| `saveOnlyUniqueItems` | Boolean | true | Remove duplicate job listings |
| `followApplyRedirects` | Boolean | false | Resolve external application URLs |

At least one of `position` or `startUrls` is required.

### Example Inputs

**Basic search:**
```json
{
    "position": "software engineer",
    "location": "New York",
    "country": "US",
    "maxItemsPerSearch": 50
}
```

**UK search with company details:**
```json
{
    "position": "data analyst",
    "location": "London",
    "country": "GB",
    "maxItemsPerSearch": 100,
    "parseCompanyDetails": true
}
```

**Direct URL with filters:**
```json
{
    "startUrls": [
        "https://www.indeed.com/jobs?q=nurse&l=Chicago%2C+IL&jt=fulltime&fromage=7"
    ],
    "maxItemsPerSearch": 50
}
```

**Combined search and URLs:**
```json
{
    "position": "marketing manager",
    "location": "Los Angeles",
    "country": "US",
    "startUrls": [
        "https://uk.indeed.com/jobs?q=marketing+manager&l=Manchester"
    ],
    "maxItemsPerSearch": 100
}
```

## Output

Each job listing contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `positionName` | String | Job title |
| `company` | String | Company name |
| `location` | String | Job location (city, state, ZIP) |
| `salary` | String | Salary range (e.g., "$80,000 - $120,000 a year") |
| `jobType` | String | Employment type (Full-time, Part-time, Contract) |
| `rating` | Number | Company rating on Indeed (0-5) |
| `reviewsCount` | Integer | Number of company reviews |
| `url` | String | Direct link to the job on Indeed |
| `description` | String | Full job description text |
| `companyInfo` | Object | Company details (when enabled) |
| `companyLogo` | String | URL to company logo |
| `companySize` | String | Company employee count range (when enabled) |
| `id` | String | Indeed's unique job identifier |
| `postedAt` | String | Relative posting time (e.g., "3 days ago") |
| `scrapedAt` | String | ISO timestamp of when data was collected |
| `postingDateParsed` | String | Posting date in YYYY-MM-DD format |
| `isExpired` | Boolean | Whether the listing has expired |
| `externalApplyLink` | String | External application URL (when enabled) |

### Sample Output

```json
{
    "positionName": "Senior Software Engineer",
    "company": "TechCorp Inc.",
    "location": "San Francisco, CA 94105",
    "salary": "$150,000 - $220,000 a year",
    "jobType": "Full-time",
    "rating": 4.2,
    "reviewsCount": 1250,
    "url": "https://www.indeed.com/viewjob?jk=abc123def456",
    "description": "We are looking for a Senior Software Engineer to join our team...",
    "companyInfo": null,
    "companyLogo": "https://d2q79iu7y748jz.cloudfront.net/s/_logo/64x64/techcorp.png",
    "companySize": "",
    "id": "abc123def456",
    "postedAt": "3 days ago",
    "scrapedAt": "2026-03-13T10:00:00+00:00",
    "postingDateParsed": "2026-03-10",
    "isExpired": false,
    "externalApplyLink": ""
}
```

## Supported Countries

United States, United Kingdom, Canada, Australia, India, Germany, France, Japan, Brazil, Mexico, Italy, Spain, Netherlands, Belgium, Switzerland, Austria, Ireland, New Zealand, Singapore, Hong Kong, Philippines, Pakistan, South Africa, Nigeria, South Korea, Taiwan, Thailand, Vietnam, Indonesia, Poland, Romania, Czech Republic, Hungary, Greece, Denmark, Norway, Sweden, Finland, Portugal, Israel, Turkey, Ukraine, UAE, Saudi Arabia, Qatar, Kuwait, Oman, Bahrain, Egypt, Morocco, Argentina, Chile, Colombia, Peru, Venezuela, Ecuador, Uruguay, Costa Rica, Panama, Luxembourg, China, and Antarctica.

## FAQ

**Do I need an Indeed account?**
No. This scraper works without any login or API key.

**How many jobs can I scrape?**
You can scrape up to 10,000 jobs per run. Each search typically yields 30-60 unique listings through multiple search strategies.

**Are full job descriptions included?**
Yes. The scraper visits each job's detail page to extract the complete description, not just the search result snippet.

**What is parseCompanyDetails?**
When enabled, the scraper visits each company's Indeed profile page to extract additional information like company size and industry. This increases run time.

**What is followApplyRedirects?**
When enabled, the scraper follows Indeed's apply redirect links to find the final external application URL (e.g., the company's careers page).

**Why did I get fewer jobs than maxItemsPerSearch?**
The number of available jobs depends on your search criteria. Niche positions or small locations may have fewer listings. The scraper collects all available unique results.

**Can I use startUrls from different countries?**
Yes. Each startUrl is processed using the domain in the URL (e.g., `uk.indeed.com` for UK jobs), regardless of the country setting.

**Which fields are always available?**
`positionName`, `company`, `location`, `url`, `id`, `postedAt`, and `scrapedAt` are available for every listing. Other fields like `salary`, `rating`, and `description` depend on what the employer provides.

**How fast is the scraper?**
Typical run: 50 jobs in 3-5 minutes (including description enrichment). Enabling company details or apply redirects increases run time.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/indeed-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
