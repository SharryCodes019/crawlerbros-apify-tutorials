# Dice.com Tech Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape US tech jobs from Dice.com with titles, companies, salaries, skills, descriptions, and remote-work flags. HTTP-only, no login required.

This repository shows how to run [Dice.com Tech Jobs Scraper](https://apify.com/crawlerbros/dice-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/dice-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/dice-jobs-scraper](https://apify.com/crawlerbros/dice-jobs-scraper)
- **SEO title:** Dice.com Tech Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape US tech jobs from Dice.com with titles, companies, salaries, skills, descriptions, and remote-work flags. HTTP-only, no login required.

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

# Dice.com Tech Jobs Scraper

Scrape US tech jobs from [Dice.com](https://www.dice.com) — titles, companies, salaries, skills, descriptions, and remote-work flags. Parses `JobPosting` JSON-LD on each `/job-detail/<uuid>` page. HTTP-only; no login, no cookies required.

## Output (per job)

- `type` = `job_dice`
- `id`, `url`, `positionId` (Dice internal ID from `__NEXT_DATA__`)
- `title`, `jobTitleOverride` (Dice-side override, when present)
- `company`, `companyUrl`, `companyLogo`, `companyIdentifier`
- `hiringOrganizationUrl` — from JSON-LD `hiringOrganization.url`
- `location` — `{city, state, postalCode, country}`
- `applicantCountry` — required applicant country (`applicantLocationRequirements.name`)
- `jobLocationType` — `TELECOMMUTE` / `ONSITE` (JSON-LD)
- `salary` / `salaryDetails` (min, max, currency, unit — when published)
- `salaryUnit` — `HOUR` / `DAY` / `WEEK` / `MONTH` / `YEAR`
- `employmentType` — `FULL_TIME`, `PART_TIME`, `CONTRACTS`, `THIRD_PARTY`
- `employmentDetail` — extra employment metadata (Dice inline state)
- `postedAt`, `datePosted` (raw JSON-LD string), `datePostedLocal`
- `applyBefore`, `validThrough`
- `occupationalCategory`, `industry`
- `educationRequirements`, `experienceRequirements`, `experienceMonths`
- `qualifications`, `responsibilities`, `jobBenefits`, `specialCommitments`
- `incentives` — e.g. "Sign-on bonus", "401k match" (from inline state)
- `totalJobOpenings` — number of openings (when published)
- `descriptionHtml`, `descriptionText`
- `skills` (array)
- `isRemote`, `easyApply` (when signaled on page)
- `directApply` — from JSON-LD `directApply` when present
- `scrapedAt`

If no jobs match, a single `job_dice_blocked` sentinel record is emitted so runs exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | string[] | Dice search or `/job-detail/<uuid>` URLs. Prefill: `https://www.dice.com/jobs?q=python`. |
| `searchTerm` | string | Used when no `startUrls` — builds `https://www.dice.com/jobs?q=<term>`. |
| `location` | string | City / ZIP added as `location` query param. |
| `employmentType` | enum | `any / FULL_TIME / PART_TIME / CONTRACTS / THIRD_PARTY` — applied client-side. |
| `workType` | enum | `any / remote / hybrid / on-site` — matched against title + description. |
| `maxItems` | integer | Max jobs per run. Default 3. |
| `salaryMin` | integer | Minimum salary — matched against JSON-LD `baseSalary.value.minValue`. |
| `datePostedDays` | integer | Only include jobs posted within the last N days (from JSON-LD `datePosted`). |
| `includeKeywords` | string[] | Title/description must contain at least one of these (case-insensitive). |
| `excludeKeywords` | string[] | Drop jobs whose title/description contains any of these (case-insensitive). |
| `proxyConfiguration` | object | Apify proxy (datacenter by default). |

## How it works

1. For each `startUrls` entry, classify as search page or direct `/job-detail/` URL.
2. Search pages: extract every `/job-detail/<uuid>` href.
3. For each job URL, fetch detail page and parse `JobPosting` JSON-LD (title, company, salary, location, description). Apply client-side `employmentType` / `workType` filters.
4. Rotate Apify-proxy session per retry on 403 / 429 / 5xx.

## FAQ

**Do I need a proxy?** The default Apify proxy is enabled to avoid 403s on detail pages. Free datacenter proxy is sufficient.
**Why a sentinel record?** When the search has no matches or the provided URL 404s, the actor still emits one record so downstream pipelines never see an empty output.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/dice-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
