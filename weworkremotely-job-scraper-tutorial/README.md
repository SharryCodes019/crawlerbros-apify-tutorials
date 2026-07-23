# We Work Remotely Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape remote job listings from WeWorkRemotely.com with titles, companies, locations, salaries, full descriptions, and company profiles. HTTP-only, no login required.

This repository shows how to run [We Work Remotely Jobs Scraper](https://apify.com/crawlerbros/weworkremotely-job-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/weworkremotely-job-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/weworkremotely-job-scraper](https://apify.com/crawlerbros/weworkremotely-job-scraper)
- **SEO title:** We Work Remotely Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape remote job listings from WeWorkRemotely.com with titles, companies, locations, salaries, full descriptions, and company profiles. HTTP-only, no login required.

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

# We Work Remotely Jobs Scraper

Scrape remote jobs from [WeWorkRemotely.com](https://weworkremotely.com) — titles, companies, locations, salaries, full descriptions, and company profiles. HTTP-only; no login, no cookies, no proxy required.

## Output (per job)

- `type` = `job_wwr`
- `url`, `id`, `slug`
- `title`, `company`, `companyLogo`, `companyLogoFull`, `companyHq`
- `companyWebsite` — company homepage / social URL (`hiringOrganization.sameAs`)
- `hiringOrganizationSameAs` — full list when multiple `sameAs` entries are present
- `companyBio` — about-the-company text block when the sidebar provides one
- `category`, `occupationalCategory` (string or list per JSON-LD)
- `employmentType` — raw schema.org value (e.g. `FULL_TIME`)
- `employmentTypeNormalized` — lower-case hyphenated form (e.g. `full-time`, `contract`)
- `jobLocationType` — `TELECOMMUTE` / `ONSITE`
- `postedAt`, `applyBefore`, `validThrough`
- `salary`, `salaryDetails` (min / max / currency / unit)
- `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryUnit` — exposed at top level for easy filtering
- `applicantCountries`, `applicantLocationRequirements` — parsed from `applicantLocationRequirements[].name`
- `directApply` — JSON-LD boolean flag (Google structured-data hint)
- `skills` — list extracted from Skills / Requirements bullet list when present
- `descriptionHtml`, `descriptionText` (when `includeDescription = true`)
- `applyUrl`
- `applicationCount` — when the detail page shows "N applicants"
- `companyFoundedYear` — when the company block shows a founded year
- `scrapedAt`

If the listing / search returns zero results, a single `job_wwr_blocked` sentinel record is emitted so runs exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `categoryUrls` | string[] | WWR category or search URLs. Prefill: `https://weworkremotely.com/categories/remote-programming-jobs`. |
| `searchTerm` | string | Optional keyword used when no `categoryUrls` are supplied (builds `/remote-jobs/search?term=…`). |
| `maxItems` | integer | Max jobs per run. Default 3. |
| `includeDescription` | boolean | Fetch each job's detail page for full description + company metadata. Default `true`. |
| `cleanHtml` | boolean | Strip scripts / tracking images from `descriptionHtml`. Default `true`. |
| `regions` | string[] | Optional region substrings (case-insensitive). Example: `["USA", "Europe"]`. |
| `jobTypes` | string[] | Optional employment-type filter: `full-time`, `contract`, `part-time`. |
| `minSalary` | integer | Minimum salary in USD. Only applied when a listing has numeric salary data. |

## How it works

1. Fetch each `categoryUrls` entry (or build a search URL from `searchTerm`).
2. Extract `/remote-jobs/<slug>` links from the listing page.
3. For each job, fetch the detail page and parse the embedded `JobPosting` JSON-LD schema (Google-compatible structured data). Fall back to DOM selectors where the schema lacks fields.
4. Clean HTML: unescape entities, strip `<script>` and 1×1 tracking images when `cleanHtml = true`.

## FAQ

**Do I need a proxy?** No.
**Why is the sentinel emitted?** When the given URL / search has no matching jobs, we still emit one record so downstream pipelines never see an empty output.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/weworkremotely-job-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
