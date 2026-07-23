# Workday Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape jobs from any Workday-hosted careers site (*.myworkdayjobs.com). Titles, descriptions, locations, requisition IDs, posting dates etc. HTTP-only, no login.

This repository shows how to run [Workday Jobs Scraper](https://apify.com/crawlerbros/workday-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/workday-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/workday-jobs-scraper](https://apify.com/crawlerbros/workday-jobs-scraper)
- **SEO title:** Workday Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape jobs from any Workday-hosted careers site (*.myworkdayjobs.com). Titles, descriptions, locations, requisition IDs, posting dates etc. HTTP-only, no login.

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

# Workday Jobs Scraper

Scrape jobs from any [Workday](https://www.workday.com/)-hosted careers site — those on `*.myworkdayjobs.com` (NVIDIA, Salesforce, Citi, Capital One, and thousands more). HTTP-only, no login, no cookies.

## What it outputs (per job)

- `type` = `job_workday`
- `id` (requisition ID), `requisitionId`, `jobPostingId`, `url`, `title`
- `jobDescription` (HTML), `descriptionText` (stripped)
- `location`, `primaryLocation` (full descriptor + country block), `additionalLocations`, `country`, `countryCode`
- `postedOn`, `postingDate` (ISO), `startDate`, `endDate`, `endDateText`, `applicationCloseDate`, `applicationTimeRemaining`
- `timeType`, `remoteType` (when the tenant publishes it — e.g. `Office - Flexible`, `Onsite`, `Remote`)
- `compensationRangeMin`, `compensationRangeMax`, `compensationCurrency`, `compensationFrequency` (parsed best-effort from the description)
- `canApply`, `hiringOrganization`, `jobRequisitionUrl`
- `questionnaireId`, `secondaryQuestionnaireId`
- `similarJobs` (list of `{title, url}`)
- `logoImage` (absolute URL, when the tenant exposes one)
- `videoInfo` (when present)
- `tenant`, `site`, `externalPath`
- `scrapedAt`

If the given URL has zero matching jobs (or Workday's global maintenance page is up for that tenant), a single `job_workday_blocked` sentinel record is emitted so runs exit `0`.

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | string[] | Workday tenant career URLs (e.g. `https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite`) or direct job URLs (contain `/job/...`). |
| `searchText` | string | Optional keyword filter (`engineer`, `marketing`, …). |
| `locations` | string[] | Optional list of Workday location UUIDs (facet values returned by the `/jobs` API under `facets[].values[].id`). |
| `postedAt` | string | Optional cutoff. Either ISO date (`2026-04-01`) or a relative string (`7 days`, `30 days`). |
| `startAt` | string | Optional start-date cutoff, same format as `postedAt`. |
| `scrapeDetails` | boolean | Fetch the detail endpoint for full HTML descriptions + country + canApply. Default `true`. |
| `maxItems` | integer | Max jobs per run. Default `3`, max `10000`. |
| `proxyConfiguration` | object | Apify proxy. Datacenter is enough; Workday's public API is unauthenticated. |

## How it works

1. Parse `tenant`, `region`, `site` from each Workday URL.
2. POST the public API `https://<tenant>.<region>.myworkdayjobs.com/wday/cxs/<tenant>/<site>/jobs` with `{ limit, offset, searchText, appliedFacets }` — paginated until `maxItems` or `total` is exhausted.
3. If `scrapeDetails = true`, GET each job's detail endpoint for the full `jobPostingInfo` (description HTML, country, canApply, startDate, timeType).
4. Apply `postedAt` / `startAt` cutoffs in-process.

## FAQ

**Does this work for every Workday tenant?** Yes — every `*.myworkdayjobs.com` site exposes the same public `/wday/cxs/` JSON API without auth.

**What about bot blocking?** Workday's public careers API does not challenge datacenter IPs. A small retry loop handles the occasional 429/503.

**What's a location UUID?** When you open a Workday careers site and expand the Locations filter, each entry has a stable UUID. The first API response's `facets` array returns them.

**Why are some runs emitting only the sentinel?** Individual tenants occasionally redirect to `community.workday.com/maintenance-page` during Workday's rolling deploys. The sentinel lets the caller retry later without a hard failure.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/workday-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
