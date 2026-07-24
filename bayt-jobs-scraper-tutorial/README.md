# Bayt.com Middle East Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape Middle East job listings from Bayt.com with titles, companies, locations, salaries, career level, experience, full descriptions, skills, and apply links. HTTP-only, no login required.

This repository shows how to run [Bayt.com Middle East Jobs Scraper](https://apify.com/crawlerbros/bayt-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bayt-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bayt-jobs-scraper](https://apify.com/crawlerbros/bayt-jobs-scraper)
- **SEO title:** Bayt.com Middle East Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Middle East job listings from Bayt.com with titles, companies, locations, salaries, career level, experience, full descriptions, skills, and apply links. HTTP-only, no login required.

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

# Bayt.com Middle East Jobs Scraper

Scrape job listings from [Bayt.com](https://www.bayt.com) — the largest job board across the Middle East and North Africa. Returns titles, companies, locations, salaries, career level, experience, full descriptions, required skills, preferred-candidate details, and direct apply links. HTTP-only; no login or cookies required.

## Output (per job)

- `type` = `job_bayt`
- `jobId`, `url`
- `title`
- `company`, `companyProfileUrl`, `companyLogo`
- `location` (e.g. "Dubai · UAE")
- `postedAtRelative` (e.g. "30+ days ago"), `postedAt` (ISO 8601 UTC)
- `employmentType` (Full time / Part time / Contract …)
- `careerLevel` (Entry / Mid career / Management / Executive)
- `experience`
- `salary`
- `minSalaryUSD`, `maxSalaryUSD` — when the detail page shows a USD salary range
- `vacancies` — number of open positions, when listed
- `industryId`, `industryName`, `jobType` (Remote / Hybrid / On-site)
- `jobFunction` — broad function (e.g. Engineering, Sales) when available
- `applyUrl`, `isExternalJob`
- `descriptionHtml`, `descriptionText`
- `skillsText`
- `preferredCandidate`
- `gender` — preferred gender (Male / Female / Any)
- `nationality` — preferred nationality text
- `residenceCountry` — required residence country
- `degree` — required education level
- `languages` — list of required languages
- `benefits` — list of benefits when the detail page has a benefits block
- `candidateStatus` — boolean "Open to travel" flag (when present)
- `applicationsCount`, `viewsCount` — interaction counters when surfaced on the detail page
- `listingSummary`
- `companySize`, `companyEmployeesSize` — e.g. "50-99 Employees"
- `companyIndustry` — extracted from the industry anchor in the company row
- `companyFoundedYear` — year the company was founded (when shown on the profile)
- `datePosted` — absolute date from meta tags when present
- `scrapedAt`

If the listing / search returns zero results (or the input is invalid), a single `job_bayt_blocked` sentinel record is emitted so runs always exit with output.

## Input

| Field | Type | Description |
|---|---|---|
| `startUrl` | string | Bayt.com search or category URL. Prefill: `https://www.bayt.com/en/international/jobs/python-jobs/`. |
| `keyword` | string | Optional keyword filter. When set, merged into the start URL as `?keyword=…`. |
| `locationFilter` | string | Optional country/city slug (e.g. `uae`, `dubai-uae`, `saudi-arabia`, `qatar`). Used when no `startUrl` is supplied. |
| `resultsWanted` | integer | Maximum job listings to return. Default 3, max 500. |
| `maxPages` | integer | Maximum listing pages to iterate. Default 20. |
| `datePosted` | enum | `any`, `last_24_hours`, `last_week`, `last_month`. Appended to URL where supported, else client-side. |
| `careerLevel` | enum | `any`, `entry`, `mid_career`, `management`, `senior_executive`, `student`. Client-side match. |
| `employmentType` | enum | `any`, `full_time`, `part_time`, `contract`, `internship`, `temporary`. Client-side match. |
| `proxyConfiguration` | object | Apify proxy. Datacenter proxy is sufficient. |

### Example inputs

- Keyword + country: `keyword = "sales"`, `locationFilter = "uae"`
- Direct URL: `startUrl = "https://www.bayt.com/en/dubai-uae/jobs/"`
- Single job: `startUrl = "https://www.bayt.com/en/uae/jobs/creative-tech-ai-lead-5443062/"`

## How it works

1. Build a start URL from `startUrl` — or `keyword` + `locationFilter` when the URL is blank.
2. Iterate `?page=N` up to `maxPages` or until `resultsWanted` is reached.
3. Extract each job card (`li[data-js-job]`) to seed fields (title, company, location, salary, career level, summary, relative date).
4. For each job URL, fetch the detail page and extract structured data from `#job_card` (header), `data-automation-id` rows (employment type, career level, industry) and the H2-anchored description / skills / preferred-candidate sections.
5. Retry on `403` / `429` / `5xx` up to three times with exponential backoff and a fresh Apify-proxy session.

## FAQ

**Do I need a proxy?**
Datacenter proxy is sufficient — Bayt.com accepts datacenter IPs for both listing and detail pages.

**Can I scrape a single job URL?**
Yes — pass the direct job URL in `startUrl`. The scraper detects job URLs and skips pagination.

**What countries are supported?**
All Bayt country sub-sites (UAE, Saudi Arabia, Qatar, Kuwait, Oman, Bahrain, Egypt, Jordan, Lebanon, Morocco …). Use the country slug from the Bayt URL structure (`/en/<country>/jobs/`) in `locationFilter`.

**Why is a sentinel record emitted?**
When the given URL / search has no matching jobs, we still emit one `job_bayt_blocked` record so downstream pipelines never see an empty dataset.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bayt-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
