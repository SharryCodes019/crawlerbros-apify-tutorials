# InfoJobs Spain Jobs Scraper Tutorial: Run This Apify Actor with Python

Scrape job listings from InfoJobs.net (Spain) with titles, companies, descriptions, contract types, salaries, locations, and more. HTTP-only via embedded search JSON.

This repository shows how to run [InfoJobs Spain Jobs Scraper](https://apify.com/crawlerbros/infojobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/infojobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/infojobs-scraper](https://apify.com/crawlerbros/infojobs-scraper)
- **SEO title:** InfoJobs Spain Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape job listings from InfoJobs.net (Spain) with titles, companies, descriptions, contract types, salaries, locations, and more. HTTP-only via embedded search JSON.

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

# InfoJobs Spain Jobs Scraper

Scrape job listings from [InfoJobs.net](https://www.infojobs.net) — Spain's largest job board — including titles, companies, descriptions, contract types, salaries, locations, and more.

## Output (per job)

- `type` = `job_infojobs`
- `id` (`of-xxx`), `jobId` (bare code without prefix), `url`
- `title`
- `descriptionHtml`, `descriptionText`
- `companyName`, `companyLogo`, `companyUrl`
- `companySector`, `companySize` (when present on the detail page)
- `city`, `province`, `country`
- `contractType`, `workday`, `teleworking`, `remoteType` (canonical: `presencial` / `hibrido` / `teletrabajo`)
- `experienceMin`, `studyLevel`, `yearsOfContractExperience`
- `category`, `subcategory`
- `salary`, `salaryMin`, `salaryMax`, `salaryPeriod`, `salaryType`, `salaryCurrency`
- `skills`, `languages`, `benefits`, `processPhase` (lists, when the detail page advertises them)
- `vacancies`, `applicationsCount` / `applicantCount`
- `postedAt`, `closingDate` / `expiresAt`
- `externalId` (source reference / offer code used by the employer)
- `isPromoted`, `isExecutive`, `isVisibleToCompany`, `promotions`, `states`
- `scrapedAt`

Fields are only included when a non-empty value is available — so datasets never contain nulls. If a run extracts zero jobs (for example, a bad URL or an aggressive anti-bot block), a single `job_infojobs_blocked` sentinel record is emitted so the dataset is never empty.

## Input

| Field | Type | Description |
|---|---|---|
| `searchUrls` | string[] | InfoJobs search URLs, or direct job detail URLs (`…/of-<id>`). Default: `https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=python`. |
| `keyword` | string | Fallback keyword used to build a search URL when `searchUrls` is empty. |
| `province` | string | Client-side filter on the parsed city / province field (e.g. `Madrid`, `Barcelona`). |
| `category` | string | Extra keyword appended as `&category=` when a search URL is synthesised. |
| `contractType` | enum | `any` / `indefinido` / `temporal` / `practicas` / `autonomo` / `otros`. |
| `workday` | enum | `any` / `completa` / `parcial` / `indiferente`. |
| `teleworking` | enum | `any` / `presencial` / `hibrido` / `teletrabajo`. |
| `maxItems` | integer | Maximum jobs per run. Default 3. |
| `proxyConfiguration` | object | Apify proxy. Datacenter recommended; residential helps when Distil blocks the IP. |

## How it works

1. The actor fetches the listing URL with `curl_cffi` (chrome131 TLS impersonation) and parses the embedded `window.__INITIAL_PROPS__` JSON blob.
2. Each offer record already exposes title, description, city, company, contract type, workday, teleworking, salary, and posting date.
3. Each job's detail page is then fetched best-effort to pick up `experienceMin`, `studyLevel`, `category`, `subcategory`, `province`, and `applicationsCount` — listings stay in the dataset even when the detail fetch is blocked.
4. Client-side filters (`contractType` / `workday` / `teleworking` / `province`) run on the parsed Spanish labels.

## FAQ

**Do I need a proxy?** Not strictly — InfoJobs often serves a 200 on the search page from datacenter IPs. When you see a captcha interstitial, switch the proxy group to residential.

**Does it scrape beyond Spain?** InfoJobs is a Spain-only platform — every posting is tagged `country = "Spain"`.

**Why do some fields disappear?** Fields are omitted when empty rather than returned as `null`, so your dataset is always clean. Detail-page-only fields (`experienceMin`, `studyLevel`, `category`, `subcategory`, `skills`, `languages`, `benefits`, `vacancies`, `processPhase`, `closingDate`, `externalId`, `companySector`, `companySize`, `applicationsCount`) depend on the detail page being reachable; listing-level fields (title, company, salary, contract, city, `remoteType`, `isPromoted`, etc.) are always present when a job is returned.

**What's the `job_infojobs_blocked` sentinel?** A single row emitted when zero jobs were extracted — useful to tell the difference between "no results" and "scraper failed silently".

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/infojobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
