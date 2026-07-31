# Seek.com.au Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape Seek.com.au job listings with titles, companies, locations, salaries, work arrangements, and full descriptions. HTTP-only, no login required.

This repository shows how to run [Seek.com.au Jobs Scraper](https://apify.com/crawlerbros/seek-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/seek-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/seek-jobs-scraper](https://apify.com/crawlerbros/seek-jobs-scraper)
- **SEO title:** Seek.com.au Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Seek.com.au job listings with titles, companies, locations, salaries, work arrangements, and full descriptions. HTTP-only, no login required.

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

# Seek.com.au Jobs Scraper

Scrape jobs from [Seek.com.au](https://www.seek.com.au) — titles, companies, locations, salaries, work types, arrangements, classifications, and full descriptions. HTTP-only; no login, no cookies, no proxy required.

## Output (per job)

- `type` = `job_seek`
- `id`, `url`, `jobLink` (alias of `url`)
- `title`, `company`, `companyLogo`
- `location` = `{ city, state, postCode, country }`
- `locationDescription` — human-readable label (e.g. `"Mulgrave, Melbourne VIC"`)
- `locationArea` — Seek tracking area (e.g. `"Eastern Suburbs"`)
- `broaderLocationName` — parent region (e.g. `"Melbourne"`)
- `workType` — e.g. `"Full Time"`, `"Contract/Temp"`
- `workTypeLabels` — raw enum list (e.g. `["FULL_TIME"]`)
- `workArrangement` — display text (e.g. `"On-site"`, `"Hybrid"`, `"Remote"`)
- `workArrangementTypes` — enum list (e.g. `["ONSITE"]`)
- `salary`, `salaryDetails` = `{ min, max, currency, type }`
- `postedAt`, `postedAtLabel` (e.g. `"2d ago"`), `expiresAt`
- `classification`, `subClassification`
- `normalisedRoleTitle`, `normalisedOrganisationName`
- `descriptionHtml`, `descriptionText`
- `teaser` — short 1-line summary
- `bulletPoints` (list)
- `questionnaire` (list of screening questions, when present)
- `recruiterName`, `recruiterAgency`, `recruiterProfile`
- `advertiserId`, `advertiserName`, `advertiserVerified`
- `isPrivateAdvertiser` (true when advertiser posts without a company identity)
- `isLinkOut` (true = external direct-apply flow)
- `isVerified`, `isExpired`, `status`, `sourceZone`
- `displayType`, `isFeatured`, `isPremium`, `isStandout`, `isBranded` (listing promo flags)
- `applyUrl`, `applyLink` (alias), `directApplyUrl` (when external)
- `phoneNumber` (when recruiter provides one)
- `videoUrl`, `videoPosition` (when job includes an advertiser video)
- `branding` = `{ logoUrl, coverImageUrl, thumbnailCoverImageUrl, id }`
- `companyId`, `companySlug`, `companyIndustry`, `companySize`, `companyWebsite`
- `companyDescription`, `companyRating`, `companyReviewCount`, `companyPerks`
- `companyProfile` (raw nested profile object, when returned)
- `emails`, `phoneNumbers` (extracted from description text)
- `scrapedAt`

If a search returns zero matching jobs, a single `job_seek_blocked` sentinel record is emitted.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | Seek search or job URLs. Prefill: `https://www.seek.com.au/python-jobs`. |
| `searchTerm` | string | Keywords used to build a search URL when `searchUrls` are missing. |
| `location` | string | Optional location, e.g. `"Sydney NSW"`. Combined with `searchTerm`. |
| `workTypes` | string[] | Filter by work type (`Full Time`, `Part Time`, `Contract/Temp`, `Casual/Vacation`). |
| `workArrangements` | string[] | Filter by work arrangement (`On-site`, `Hybrid`, `Remote`). |
| `dateRange` | enum | Filter by posted date (`any`, `1`, `3`, `7`, `14`, `30` days). |
| `salaryMin` / `salaryMax` | integer | Filter by parsed salary range. |
| `sortBy` | enum | `KeywordRelevance` or `ListedDate`. |
| `maxItems` | integer | Max jobs per run. Default 3. |
| `scrapeJobDetails` | boolean | Fetch each job's detail page for the full description. Default `true`. |

## How it works

1. Fetch each `searchUrls` entry (or build one from `searchTerm` + `location` + `sortBy`).
2. Parse the inline `window.SEEK_REDUX_DATA` JSON blob and read `results.results.jobs[]` — Seek ships the full job list as embedded JSON (no browser, no GraphQL auth, no pagination needed for the first page).
3. For each job, fetch `https://www.seek.com.au/job/<id>` to get the full description and apply link.
4. Apply client-side filters (`workTypes`, `workArrangements`, `dateRange`, `salaryMin`, `salaryMax`) before emitting each row.

## FAQ

**Do I need a proxy?** No. Seek serves clean HTML to datacenter IPs.

**Do I need login / cookies?** No.

**Why is the sentinel emitted?** When the given URL / filters match no jobs, we still emit one record so downstream pipelines never see an empty output.

**Are salaries always populated?** No — Seek advertisers often omit salary. When it's missing the scraper simply doesn't include the `salary` / `salaryDetails` keys (no nulls).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/seek-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
