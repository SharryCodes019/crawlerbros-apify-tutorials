# Linkedin Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape job listings from LinkedIn without login. Get job titles, companies, locations, salaries, full descriptions, seniority levels, employment types, and more.

This repository shows how to run [Linkedin Jobs Scraper](https://apify.com/crawlerbros/linkedin-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-jobs-scraper](https://apify.com/crawlerbros/linkedin-jobs-scraper)
- **SEO title:** Linkedin Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape job listings from LinkedIn without login. Get job titles, companies, locations, salaries, full descriptions, seniority levels, employment types, and more.

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

# LinkedIn Jobs Scraper

Scrape job listings from LinkedIn without login. Get job titles, companies, locations, salaries, full descriptions, seniority levels, employment types, and more. No API key, cookies, or LinkedIn account needed.

## What is LinkedIn Jobs Scraper?

LinkedIn Jobs Scraper is an Apify actor that extracts job listings from LinkedIn's public job search. Simply enter keywords and a location, apply optional filters, and the scraper returns structured job data ready for analysis, lead generation, or job market research.

## Features

- **Search by keywords and location** — Find jobs matching any title, skill, or company name
- **Full job descriptions** — Get both HTML and plain text versions for NLP or analysis
- **Rich metadata** — Seniority level, employment type, job function, industry, salary, applicant count
- **Advanced filters** — Time posted, experience level, job type, remote/hybrid/on-site, Easy Apply
- **Direct URL support** — Paste LinkedIn search URLs with your own custom filters
- **Automatic deduplication** — No duplicate listings when combining multiple searches
- **No login required** — Uses LinkedIn's public job search, no account or cookies needed
- **No proxy needed** — Works from standard IPs for most use cases

## Use Cases

- **Job market research** — Analyze hiring trends, salary ranges, and in-demand skills
- **Lead generation** — Find companies actively hiring in your target industry
- **Competitive analysis** — Monitor competitor hiring patterns and open roles
- **Career monitoring** — Track new job postings matching your criteria
- **Recruitment intelligence** — Identify companies expanding in specific locations or functions
- **Salary benchmarking** — Compare compensation data across companies and locations

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| Search Keywords | String | — | Job title, skills, or company to search (e.g., "software engineer", "data scientist") |
| Location | String | — | City, state, country, or "remote" (e.g., "San Francisco", "United States") |
| Maximum Jobs | Integer | 100 | Max job listings to scrape (1-1000). LinkedIn limits ~1000 results per query. |
| Scrape Full Job Details | Boolean | true | Fetch full descriptions, seniority, employment type, etc. Disable for faster runs. |
| Time Posted | Select | Any time | Filter: Past 24 hours, Past week, Past month |
| Experience Level | Select | Any | Filter: Internship, Entry, Associate, Mid-Senior, Director, Executive |
| Job Type | Select | Any | Filter: Full-time, Part-time, Contract, Temporary, Volunteer, Internship |
| Work Type | Select | Any | Filter: On-site, Remote, Hybrid |
| Easy Apply Only | Boolean | false | Only show jobs with LinkedIn Easy Apply |
| Search URLs | URL List | — | Direct LinkedIn job search URLs with filters pre-applied |

**Note:** At least one of **Search Keywords** or **Search URLs** must be provided.

### Example input — Basic search

```json
{
    "keywords": "software engineer",
    "location": "United States",
    "maxItems": 50
}
```

### Example input — Filtered search

```json
{
    "keywords": "data scientist",
    "location": "New York",
    "jobType": "F",
    "workType": "2",
    "experienceLevel": "4",
    "timePosted": "r604800",
    "maxItems": 100
}
```

### Example input — Direct URL

```json
{
    "searchUrls": [
        { "url": "https://www.linkedin.com/jobs/search/?keywords=python%20developer&location=London&f_JT=F&f_WT=2" }
    ],
    "maxItems": 50
}
```

## Output

Each job listing produces one item in the output dataset:

| Field | Type | Description |
|-------|------|-------------|
| id | String | LinkedIn's unique job identifier |
| title | String | Job position title |
| companyName | String | Hiring company name |
| companyUrl | String | LinkedIn company page URL |
| location | String | Job location (city, state, country) |
| salary | String | Salary range if provided by employer (e.g., "$110,000.00/yr - $155,000.00/yr") |
| postedDate | String | ISO date when the job was posted |
| postedDateText | String | Relative posting time (e.g., "3 days ago") |
| applicantCount | String | Number of applicants (e.g., "Over 200 applicants") |
| jobUrl | String | Direct link to the job on LinkedIn |
| descriptionHtml | String | Full job description in HTML format |
| descriptionText | String | Full job description in plain text |
| seniorityLevel | String | Required seniority (e.g., "Mid-Senior level") |
| employmentType | String | Full-time, Part-time, Contract, etc. |
| jobFunction | String | Job function category (e.g., "Engineering") |
| industries | String | Industry sector (e.g., "Technology, Information and Internet") |
| scrapedAt | String | ISO timestamp when data was collected |

### Sample output

```json
{
    "id": "3876543210",
    "title": "Senior Software Engineer",
    "companyName": "Google",
    "companyUrl": "https://www.linkedin.com/company/google",
    "location": "Mountain View, CA",
    "salary": "$150,000.00/yr - $200,000.00/yr",
    "postedDate": "2026-03-20",
    "postedDateText": "4 days ago",
    "applicantCount": "Over 200 applicants",
    "jobUrl": "https://www.linkedin.com/jobs/view/3876543210",
    "descriptionHtml": "<p>We are looking for a Senior Software Engineer...</p>",
    "descriptionText": "We are looking for a Senior Software Engineer to join our team...",
    "seniorityLevel": "Mid-Senior level",
    "employmentType": "Full-time",
    "jobFunction": "Engineering and Information Technology",
    "industries": "Technology, Information and Internet",
    "scrapedAt": "2026-03-24T10:30:00.000000+00:00"
}
```

## How to use

### Quick start

1. Enter a job title or keyword in the **Search Keywords** field
2. Enter a location (city, country, or "remote")
3. Set **Maximum Jobs** to control how many listings to scrape
4. Click **Start** and wait for results

### Use filters for targeted results

Apply filters like **Job Type** (Full-time), **Work Type** (Remote), or **Time Posted** (Past week) to narrow your search. This mirrors the filters available on LinkedIn's job search page.

### Use LinkedIn search URLs

1. Go to [LinkedIn Jobs](https://www.linkedin.com/jobs/) in your browser
2. Search for jobs and apply any filters you want
3. Copy the URL from your browser's address bar
4. Paste it into the **Search URLs** field

### Combine both modes

You can provide both keywords and search URLs. The scraper processes all searches and deduplicates results automatically.

## How many jobs can I scrape?

LinkedIn limits public search results to approximately **1,000 jobs per unique search query**. To get more results:

- Use different keyword variations (e.g., "software engineer" and "software developer")
- Search different locations separately
- Apply different filters to get distinct result sets
- Use multiple search URLs with different parameters

## Tips

- **Start small** — Use `maxItems: 10` for your first run to verify the output format
- **Disable details for speed** — Set `scrapeJobDetails: false` for a 5-10x faster run when you only need titles, companies, and locations
- **Use specific keywords** — Narrow keywords produce more relevant results
- **Combine with location** — Adding a location improves result quality significantly

## FAQ

**Do I need a LinkedIn account?**
No. The scraper uses LinkedIn's public job search which is accessible without any login.

**Do I need a proxy?**
No. The scraper works without proxy for most use cases. It will automatically use a proxy only if needed.

**How fast is the scraper?**
With job details enabled: approximately 25 jobs per 15-20 seconds. Without details: 25 jobs per 3-5 seconds.

**Why are some fields empty?**
Fields like `salary` and `applicantCount` depend on whether the employer provided that information. LinkedIn only shows salary when the employer explicitly includes a pay range in the listing.

**What is "Scrape Full Job Details"?**
When enabled (default), the scraper visits each job's detail page to get the full description, seniority level, employment type, job function, and industry. Disabling it returns only the data visible in search results (title, company, location, date, salary).

**Can I scrape jobs from a specific company?**
Yes. Either search for the company name as a keyword, or find the company's LinkedIn ID and use a search URL with the `f_C` parameter.

**Why did I get fewer jobs than maxItems?**
LinkedIn may have fewer matching jobs than your limit, or the search may have hit LinkedIn's ~1000 result cap. Try broader keywords or different locations.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
