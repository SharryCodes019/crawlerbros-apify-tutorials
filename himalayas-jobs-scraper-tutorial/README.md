# Himalayas Remote Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape Himalayas.app, a remote-first startup job board with 100k+ listings. Search by keyword, filter by employment type, remote policy, and salary. Fetch all jobs for a company or enrich specific job URLs.

This repository shows how to run [Himalayas Remote Jobs Scraper](https://apify.com/crawlerbros/himalayas-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/himalayas-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/himalayas-jobs-scraper](https://apify.com/crawlerbros/himalayas-jobs-scraper)
- **SEO title:** Himalayas Remote Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Himalayas.app, a remote-first startup job board with 100k+ listings. Search by keyword, filter by employment type, remote policy, and salary. Fetch all jobs for a company or enrich specific job URLs.

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

# Himalayas Remote Jobs Scraper

Scrape job listings from [Himalayas.app](https://himalayas.app) — one of the largest remote-first startup job boards, with 100,000+ active remote positions across engineering, product, design, marketing, and more.

Extract structured data on job titles, companies, salary ranges, employment types, tech stacks, categories, posting dates, and direct application links — all without requiring login or API credentials.

---

## What You Can Do

- **Search jobs by keyword** — find roles matching "python backend", "product manager", "data engineer", etc.
- **Get all jobs for a company** — pull every open role at Stripe, GitLab, Zapier, or any company with a Himalayas profile.
- **Enrich job URLs** — pass a list of specific Himalayas job URLs and get back fully structured data.
- **Filter results** — narrow by employment type (full-time, part-time, contract, internship) and minimum salary.

---

## Output Fields

Each scraped job record contains the following fields:

| Field | Type | Description |
|---|---|---|
| `jobId` | string | Unique job identifier (from URL slug) |
| `title` | string | Job title |
| `company` | string | Hiring company name |
| `companyUrl` | string | Link to the company's Himalayas profile |
| `jobUrl` | string | Direct link to the job listing on Himalayas |
| `location` | string | Country restrictions, or "Worldwide" if no restrictions |
| `remotePolicy` | string | Always `"remote"` — all Himalayas jobs are remote |
| `salaryMin` | integer | Annual salary minimum (when available) |
| `salaryMax` | integer | Annual salary maximum (when available) |
| `salaryCurrency` | string | ISO 4217 currency code (e.g. USD, EUR, GBP) |
| `employmentType` | string | `full-time`, `part-time`, `contract`, or `internship` |
| `techStack` | array | Skill/technology category tags |
| `categories` | array | Broad function areas (e.g. Developer, Product, Design) |
| `postedAt` | string | ISO 8601 UTC timestamp of when the job was posted |
| `description` | string | Full job description (HTML) |
| `applyUrl` | string | Direct application link |
| `recordType` | string | Always `"job"` |
| `scrapedAt` | string | ISO 8601 UTC timestamp of when the record was scraped |

---

## Input Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | select | `searchJobs` | What to scrape: `searchJobs`, `byCompany`, or `byJobUrls` |
| `searchQuery` | string | — | Keyword search query (used in `searchJobs` mode) |
| `companySlug` | string | — | Company slug for `byCompany` mode (e.g. `stripe`, `gitlab`) |
| `jobUrls` | array | `[]` | List of Himalayas job URLs for `byJobUrls` mode |
| `remotePolicy` | select | _(any)_ | Filter by remote policy: `remote`, `hybrid`, `in-person` |
| `employmentType` | select | _(any)_ | Filter by type: `full-time`, `part-time`, `contract`, `internship` |
| `minSalary` | integer | — | Minimum salary threshold (USD/year) — skips jobs below this |
| `maxItems` | integer | `20` | Maximum number of job records to return |

---

## Example Inputs

### Search for software engineering roles
```json
{
  "mode": "searchJobs",
  "searchQuery": "software engineer",
  "employmentType": "full-time",
  "maxItems": 50
}
```

### Get all open roles at a company
```json
{
  "mode": "byCompany",
  "companySlug": "stripe",
  "maxItems": 100
}
```

### Enrich specific job URLs
```json
{
  "mode": "byJobUrls",
  "jobUrls": [
    "https://himalayas.app/companies/stripe/jobs/backend-engineer-123",
    "https://himalayas.app/companies/gitlab/jobs/product-manager-456"
  ]
}
```

### Find high-paying contract roles
```json
{
  "mode": "searchJobs",
  "searchQuery": "data scientist",
  "employmentType": "contract",
  "minSalary": 120000,
  "maxItems": 30
}
```

---

## Use Cases

- **Monitor startup hiring trends** — track which companies are growing and in what roles
- **Find remote jobs in tech** — filter by keyword, employment type, and salary to find your next role
- **Build a job aggregator** — combine Himalayas data with other job boards for comprehensive coverage
- **Salary benchmarking** — analyze compensation ranges for specific roles, companies, and tech stacks
- **Competitive intelligence** — watch what competitors or target companies are hiring for
- **Academic research** — study remote work trends, demand for skills, and salary distributions
- **Recruiting automation** — identify passive candidate pipelines by tracking who's hiring in a tech stack
- **Career tools** — power job recommendation engines, resume analyzers, or career coaching platforms

---

## Frequently Asked Questions

**Does this require login or API keys?**
No. The Himalayas API is publicly accessible without authentication. This actor uses the official public API.

**How fresh is the data?**
Himalayas refreshes their job data every 24 hours. Each run of this actor fetches the latest available data.

**What does the `remotePolicy` field show?**
All listings on Himalayas are remote or remote-friendly by definition of the platform, so `remotePolicy` is always `"remote"`. The `location` field shows any geographic restrictions (e.g., "United States, Canada") or "Worldwide" if there are none.

**How do I find a company's slug?**
The slug is the part of the Himalayas company URL after `/companies/`. For example, `https://himalayas.app/companies/stripe` → slug is `stripe`.

**What employment types does Himalayas have?**
Full Time, Part Time, Contractor, Temporary, Intern, Volunteer, and Other. This actor normalizes them to: `full-time`, `part-time`, `contract`, `internship`.

**Why are some salary fields missing?**
Many job listings on Himalayas do not include salary information. Records without salary data will simply omit `salaryMin`, `salaryMax`, and `salaryCurrency` rather than showing null values.

**Can I scrape all available jobs?**
Yes — use `mode=searchJobs` with no `searchQuery` and set `maxItems` to a high value. Himalayas has 100,000+ active listings. Note: the API returns up to 20 jobs per request, so large scrapes take time.

**Does this work with proxy?**
No proxy is needed. Himalayas's public API is accessible from standard IP addresses without restrictions.

**What is the rate limit?**
Himalayas enforces a rate limit of 60 requests per minute. This actor includes automatic retry with back-off if rate limits are hit.

---

## Legal

This actor uses Himalayas's public API as documented at [himalayas.app/docs/remote-jobs-api](https://himalayas.app/docs/remote-jobs-api). Always credit Himalayas as the data source when displaying results publicly. Review [Himalayas Terms of Service](https://himalayas.app/terms) before using scraped data commercially.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/himalayas-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
