# Naukri Scraper Tutorial: Run This Apify Actor with Python

Scrape job listings from Naukri.com, India's largest job board. Extract title, company, location, experience, salary, skills, and description from search results.

This repository shows how to run [Naukri Scraper](https://apify.com/crawlerbros/naukri-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/naukri-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/naukri-scraper](https://apify.com/crawlerbros/naukri-scraper)
- **SEO title:** Naukri Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape job listings from Naukri.com, India's largest job board. Extract title, company, location, experience, salary, skills, and description from search results.

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

# Naukri Scraper

Extract job listings from [Naukri.com](https://www.naukri.com) — India's largest job board. Scrape job titles, companies, locations, experience, salary, skills, descriptions, and more from any Naukri search. Perfect for **recruitment analytics**, **market research**, **salary benchmarking**, and **competitor hiring intelligence**.

## What it does

- Scrapes Naukri search results from a URL or from structured filter fields
- Returns 23 fields per job: title, company, rating, location, experience, salary, skills, description, industry, role, posted date, logo, vacancies
- **RESIDENTIAL/IN proxy hardcoded** — Naukri's Akamai bot protection blocks Apify datacenter IPs, so the scraper applies an India residential proxy automatically. No configuration needed from you.
- Patchright stealth Chromium with up to 5 retries on session-level blocks
- Clean, non-null output — empty fields are omitted from records
- Supports Naukri filters: keyword, location, experience, salary, job age, job type, work mode (remote/hybrid)

## Input

### Option A — Paste a Naukri URL (easiest)

Set **Naukri Search URL** to any Naukri search page URL, for example:

```
https://www.naukri.com/python-developer-jobs
https://www.naukri.com/data-scientist-jobs-in-bangalore
https://www.naukri.com/java-developer-jobs-in-delhi-ncr
```

The scraper parses the URL slug and filters automatically.

### Option B — Use structured filters

Leave **Naukri Search URL** empty and configure:

| Field | Description |
|---|---|
| **Keyword** | Job title or keyword (e.g., "python developer") |
| **Location** | City name (e.g., "bangalore", "delhi-ncr", "mumbai") |
| **Experience (years)** | Years of experience (0–30) |
| **Salary Range (Lakhs)** | 0-3, 3-6, 6-10, 10-15, 15-25, 25+ lakhs per year |
| **Job Age (days)** | 1, 3, 7, 15, 30 days |
| **Job Type** | Full-time, Part-time, Internship, Contractual |
| **Work Mode** | Remote (work from home) or Hybrid. Naukri does not have an explicit "office" filter — office is the default state of every listing, so leave this empty for office jobs. |
| **Sort By** | Relevance, Date, Salary |
| **Max Items** | Maximum number of jobs to return (default 50) |

## Output

Each job is a JSON record with the following fields (empty fields are omitted to keep the dataset clean):

| Field | Description |
|---|---|
| `id` | Naukri job ID |
| `title` | Job title |
| `url` | Full Naukri job listing URL |
| `companyName` | Company name |
| `companyId` | Naukri company ID |
| `companyRating` | AmbitionBox rating (out of 5) |
| `companyReviewCount` | Number of reviews |
| `location` | Job location (may list multiple cities) |
| `experience` | Required experience range |
| `salary` | Salary range as displayed |
| `description` | Job description snippet |
| `skills` | Array of skill tags |
| `industry` | Industry |
| `role` | Job role category |
| `jobTypeFlags` | Flags such as `premium`, `easy_apply`, `walk_in` |
| `postedDate` | When the job was posted |
| `logoUrl` | Company logo URL |
| `vacancies` | Number of vacancies |
| `applyCount` | How many people applied |
| `recruiterName` | Recruiter name |
| `scrapedAt` | UTC timestamp when scraped |

### Sample output

```json
{
  "id": "110924500001",
  "title": "Python Developer - Django / FastAPI",
  "url": "https://www.naukri.com/job-listings-python-developer-django-fastapi-110924500001",
  "companyName": "Infosys",
  "companyRating": 3.6,
  "companyReviewCount": 42850,
  "location": "Bangalore, Hyderabad",
  "experience": "3 - 7 Yrs",
  "salary": "8-15 Lacs PA",
  "skills": ["Python", "Django", "FastAPI", "REST API", "PostgreSQL"],
  "industry": "IT Services & Consulting",
  "role": "Software Development - Back End",
  "postedDate": "2 days ago",
  "logoUrl": "https://img.naukimg.com/logo_images/groups/v1/infosys.gif",
  "vacancies": 5,
  "applyCount": 147,
  "scrapedAt": "2026-04-13T12:00:00Z"
}
```

## FAQ

**Do I need a Naukri account?**
No. The scraper works against Naukri's public search — no login, cookies, or authentication.

**Do I need to configure a proxy?**
No configuration needed — an India RESIDENTIAL proxy is hardcoded and applied automatically. Naukri uses Akamai bot protection that blocks Apify datacenter IPs and most non-Indian residential pools, so the scraper combines patchright stealth Chromium with `RESIDENTIAL/IN` traffic. Sessions are rotated automatically (up to 5 attempts) on transient blocks.

**How many jobs can I get per run?**
Up to 800 jobs per run (40 pages × 20 jobs). For more, split your search by location, keyword, or salary range.

**How fresh is the data?**
Every run pulls live data directly from Naukri, so the data is as current as Naukri's search results.

**Can I filter by experience or salary?**
Yes — use the structured filter fields or paste a Naukri URL that already has the filters applied.

**What cities are supported?**
All Naukri-supported cities — bangalore, delhi-ncr, mumbai, hyderabad, chennai, pune, kolkata, ahmedabad, and many more.

**What happens if a job has missing data?**
Missing fields are omitted entirely — no null or empty values pollute the dataset.

## Use cases

- **Recruitment agencies**: build talent pipelines and track competitor openings
- **Job seekers**: automate job discovery matching your skills
- **HR analytics**: salary benchmarking and market demand analysis
- **Data science projects**: train ML models on India's hiring trends
- **Market researchers**: monitor hiring activity across industries and cities

## Notes

- Pricing is configured in the Apify UI (pay-per-event or pay-per-result).
- The scraper visits the Naukri homepage as a warmup before each search to seed Akamai cookies, then navigates to the search URL and intercepts the `jobapi/v3/search` response. If the homepage warmup is blocked or the API call fails to fire, the session is rotated to a fresh residential IP automatically.
- The Apify daily test run uses `maxItems=5` against the default python-developer-in-bangalore search.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/naukri-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
