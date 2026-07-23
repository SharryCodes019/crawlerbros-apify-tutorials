# Glassdoor Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape job listings from Glassdoor by keyword, location, or company URL. Extracts job title, company, salary estimates, location, skills, and more.

This repository shows how to run [Glassdoor Jobs Scraper](https://apify.com/crawlerbros/glassdoor-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/glassdoor-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/glassdoor-jobs-scraper](https://apify.com/crawlerbros/glassdoor-jobs-scraper)
- **SEO title:** Glassdoor Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape job listings from Glassdoor by keyword, location, or company URL. Extracts job title, company, salary estimates, location, skills, and more.

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

# Glassdoor Jobs Scraper

Scrape job listings from Glassdoor by keyword, location, or company page URL. Get job titles, companies, salary estimates, locations, skills, and more.

## What is Glassdoor Jobs Scraper?

Glassdoor Jobs Scraper is an Apify actor that extracts job listings from Glassdoor's job search. Enter a keyword, optional location, or a direct company jobs URL, and get structured job data including salary estimates, company ratings, skills, and application details.

## Features

- **Search by keyword** — Find jobs matching any title, skill, or role
- **Location filtering** — Narrow results to a specific city, state, or country
- **Company page support** — Scrape jobs directly from a company's Glassdoor page
- **Salary estimates** — Get min, median, and max salary data with currency and period
- **Company ratings** — Overall employer rating included with each listing
- **Skills extraction** — Key skills required for each position
- **Pagination** — Automatically scrape multiple pages of results
- **Easy Apply flag** — Identify jobs with Glassdoor Easy Apply

## Use Cases

- **Job market research** — Analyze hiring trends, salary ranges, and in-demand skills
- **Salary benchmarking** — Compare compensation across companies, roles, and locations
- **Competitive analysis** — Monitor competitor hiring patterns and open positions
- **Lead generation** — Find companies actively hiring in your target industry
- **Career monitoring** — Track new job postings matching your criteria
- **Recruitment intelligence** — Identify expanding companies in specific locations

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| Search Keyword | String | — | Job search keyword (e.g., "software engineer", "data scientist"). Required unless Company Jobs URL is provided. |
| Location | String | — | Location to search in (e.g., "New York, NY", "London"). Leave empty for worldwide results. |
| Company Jobs URL | String | — | Direct Glassdoor company jobs page URL. If provided, keyword and location are ignored. |
| Maximum Items | Integer | 50 | Max job listings to scrape (1–500). |
| Proxy Configuration | Object | RESIDENTIAL (US) | Proxy settings. Glassdoor requires residential proxy to bypass DataDome bot protection. Defaults to Apify RESIDENTIAL proxy group (US). |

**Note:** At least one of **Search Keyword** or **Company Jobs URL** must be provided.

### Example input — Keyword search

```json
{
    "keyword": "software engineer",
    "location": "New York, NY",
    "maxItems": 50
}
```

### Example input — Company page

```json
{
    "companyUrl": "https://www.glassdoor.com/Jobs/Google-Jobs-E9079.htm",
    "maxItems": 100
}
```

## Output

Each job listing produces one item in the output dataset:

| Field | Type | Description |
|-------|------|-------------|
| jobListingId | Integer | Glassdoor's unique job listing ID |
| jobTitle | String | Job position title |
| companyName | String | Hiring company name |
| companyId | Integer | Glassdoor company ID |
| companyRating | Number | Overall employer rating (1.0–5.0) |
| companyLogo | String | URL to the company logo image |
| location | String | Job location |
| ageInDays | Integer | Days since the job was posted |
| easyApply | Boolean | Whether Glassdoor Easy Apply is available |
| isSponsored | Boolean | Whether the listing is a sponsored/promoted result |
| salary_min | Integer | Estimated minimum annual salary |
| salary_median | Integer | Estimated median annual salary |
| salary_max | Integer | Estimated maximum annual salary |
| salaryCurrency | String | Salary currency code (e.g., "USD") |
| salaryPeriod | String | Pay period (e.g., "ANNUAL", "HOURLY") |
| salarySource | String | Source of salary data (e.g., "ESTIMATED", "EMPLOYER") |
| description | String | Job description snippet |
| jobUrl | String | Direct link to the job listing on Glassdoor |
| skills | Array | List of required skills extracted from the listing |

### Sample output

```json
{
    "jobListingId": 1234567890,
    "jobTitle": "Senior Software Engineer",
    "companyName": "Google",
    "companyId": 9079,
    "companyRating": 4.3,
    "companyLogo": "https://media.glassdoor.com/sql/9079/google-squarelogo.png",
    "location": "Mountain View, CA",
    "ageInDays": 3,
    "easyApply": false,
    "isSponsored": false,
    "salary_min": 150000,
    "salary_median": 185000,
    "salary_max": 220000,
    "salaryCurrency": "USD",
    "salaryPeriod": "ANNUAL",
    "salarySource": "ESTIMATED",
    "description": "We are looking for a Senior Software Engineer to join our team...",
    "jobUrl": "https://www.glassdoor.com/job-listing/senior-software-engineer-google-JV_IC1234.htm",
    "skills": ["Python", "Java", "Distributed Systems", "Cloud Computing"]
}
```

## How to use

### Quick start

1. Enter a job title or keyword in the **Search Keyword** field
2. Optionally enter a **Location** to narrow results
3. Set **Maximum Items** to control how many listings to scrape
4. Click **Start** and wait for results

### Scrape a specific company's jobs

1. Go to a company's Glassdoor page (e.g., glassdoor.com/Jobs/Google-Jobs-E9079.htm)
2. Copy the URL from your browser
3. Paste it into the **Company Jobs URL** field
4. Click **Start**

## How many jobs can I scrape?

Glassdoor typically shows 30 jobs per page and up to ~30 pages. With pagination, you can scrape up to approximately **500–900 jobs per search query**. To get more results:

- Use different keyword variations
- Search different locations separately
- Use specific company page URLs

## Tips

- **Start small** — Use `maxItems: 5` for your first run to verify the output
- **Keyword + location is the most reliable** — Combining a keyword with a specific city gives the best success rate against DataDome
- **Retry on failure** — If a run returns no jobs, try again — residential IP rotation often resolves transient blocks
- **Salary data is estimated** — Most salary figures are Glassdoor estimates, not employer-provided

## FAQ

**Do I need a Glassdoor account?**
No. The scraper works without any login or cookies.

**Why does the scraper use residential proxy?**
Glassdoor uses DataDome anti-bot protection. Residential proxy is required to bypass this on Apify's data center IPs. The proxy is automatically configured.

**How fast is the scraper?**
Approximately 30 jobs per 30–60 seconds. The first page takes longer due to browser startup and anti-bot challenge resolution.

**Why are salary fields missing from some listings?**
Not all job listings have salary data. When salary information is unavailable, the `salary_min`, `salary_median`, and `salary_max` fields are simply omitted rather than set to zero.

**Why did I get fewer jobs than maxItems?**
The search may have fewer matching results, or some pages may be blocked by anti-bot measures. The scraper retries with new sessions automatically.

**Can I search without a location?**
Yes. Leave the Location field empty to get worldwide results.

**What if the scraper fails?**
Glassdoor's anti-bot protection means some sessions will be blocked. The scraper automatically retries with new browser sessions (up to 5 attempts). If it consistently fails, try again later — the IP rotation provides fresh sessions each run.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/glassdoor-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
