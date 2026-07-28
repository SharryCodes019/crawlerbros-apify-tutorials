# NHS Jobs Scraper Tutorial: Run This Apify Actor with Python

Extract UK NHS job vacancies from jobs.nhs.uk including title, employer, salary, band, pay scheme, location, contract type, closing date, full description, and more.

This repository shows how to run [NHS Jobs Scraper](https://apify.com/crawlerbros/nhs-jobs-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/nhs-jobs-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/nhs-jobs-scraper](https://apify.com/crawlerbros/nhs-jobs-scraper)
- **SEO title:** NHS Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract UK NHS job vacancies from jobs.nhs.uk including title, employer, salary, band, pay scheme, location, contract type, closing date, full description, and more.

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

# NHS Jobs Scraper

Extract UK NHS job vacancies from **jobs.nhs.uk** — title, employer, location, salary, band, pay scheme, contract type, working pattern, closing date, full description and more. No cookies, no proxy, no rate-limits on datacenter IPs.

## Features

- **20 output fields** per vacancy — complete job data in a flat schema
- **Search by keyword, or provide any jobs.nhs.uk search URL** with filters (location, band, pay scheme, staff group, specialty)
- **Full detail page enrichment** — pay scheme, band, reference number, job summary, main duties, full description
- **Parsed salary ranges** (GBP min/max) in addition to the raw formatted text
- **ISO-8601 dates** for posted and closing dates
- **Pagination** — walks `?page=N` until `maxItems` is reached
- **No proxy required** — jobs.nhs.uk is publicly accessible
- **No nulls** — every field has a typed default

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | Array | NHS Jobs search-result URLs. Any filter applied in the URL (e.g., `payScheme=AGENDA`, `payBand=Band+6`, `staffGroup=Nursing+and+Midwifery`) is preserved. |
| `search` | String | Alternative shortcut — a plain keyword (e.g., `"nurse"`) that builds a default search URL. |
| `maxItems` | Integer | Maximum number of vacancies to return (default 50, max 500). |

### Example Input

```json
{
    "startUrls": [
        "https://www.jobs.nhs.uk/candidate/search/results?keyword=nurse&payBand=Band+6"
    ],
    "maxItems": 50
}
```

or with a free-text keyword:

```json
{
    "search": "midwife",
    "maxItems": 20
}
```

## Output

Each job has **20 fields**. All fields are always present — empty strings or zero for missing data, never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `jobRef` | String | NHS reference number (e.g., `C9371-26-0259`) |
| `url` | String | Full job advert URL |
| `title` | String | Job title |

### Employer & Location
| Field | Type | Description |
|---|---|---|
| `employer` | String | Employing NHS Trust or organisation |
| `location` | String | Full location text |
| `postcode` | String | UK postcode |

### Pay & Contract
| Field | Type | Description |
|---|---|---|
| `salary` | String | Formatted salary (e.g., `"£39,959 to £48,117 a year"`) |
| `salaryMin` | Number | Minimum salary in GBP |
| `salaryMax` | Number | Maximum salary in GBP |
| `salaryPeriod` | String | Pay period (`a year`, `per annum`, `per hour`, etc.) |
| `payScheme` | String | Pay scheme (e.g., `"Agenda for change"`) |
| `payBand` | String | Pay band (e.g., `"Band 6"`) |
| `contractType` | String | Contract type (e.g., `Permanent`, `Fixed term`) |
| `workingPattern` | String | Working pattern (e.g., `Full-time`, `Part-time`) |

### Dates
| Field | Type | Description |
|---|---|---|
| `postedDate` | String | Date posted (ISO 8601 `YYYY-MM-DD`) |
| `closingDate` | String | Closing date (ISO 8601 `YYYY-MM-DD`) |

### Description
| Field | Type | Description |
|---|---|---|
| `jobSummary` | String | Short job summary (truncated to 2,000 chars) |
| `mainDuties` | String | Main duties text (truncated to 2,000 chars) |
| `description` | String | Full job description (truncated to 4,000 chars) |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "jobRef": "C9371-26-0259",
    "url": "https://www.jobs.nhs.uk/candidate/jobadvert/C9371-26-0259",
    "title": "District Nurse/Community Nursing Sister/Charge Nurse",
    "employer": "Berkshire Healthcare Foundation Trust",
    "location": "Community Nursing West Berkshire",
    "postcode": "RG18 3HD",
    "salary": "£39,959 to £48,117 a year",
    "salaryMin": 39959.0,
    "salaryMax": 48117.0,
    "salaryPeriod": "a year",
    "payScheme": "Agenda for change",
    "payBand": "Band 6",
    "contractType": "Permanent",
    "workingPattern": "Full-time",
    "postedDate": "2026-04-09",
    "closingDate": "2026-04-16",
    "jobSummary": "...",
    "mainDuties": "...",
    "description": "...",
    "scrapedAt": "2026-04-10T17:40:00+00:00"
}
```

## FAQ

**Q: Do I need a proxy?**
No. jobs.nhs.uk serves pages directly over HTTPS without bot protection. This scraper runs fine from Apify datacenter IPs.

**Q: How do I filter by pay band or staff group?**
Apply the filter on the NHS Jobs site, then copy the URL from the address bar into `startUrls`. All query parameters (including `payBand`, `payScheme`, `staffGroup`, `specialty`, `location`) are passed through verbatim.

**Q: Are closed / expired jobs included?**
Only currently-listed vacancies from the search results are returned. Historical closed jobs aren't accessible via search.

**Q: What's the maximum throughput?**
NHS search pages return 10 results each. The scraper walks pages sequentially and enriches details in parallel (concurrency 4) — expect ~40 jobs/minute.

**Q: Why are some `salaryMin` / `salaryMax` values the same?**
When a job has a fixed salary (not a range), both fields are set to the same value.

## Use Cases

- **Healthcare recruitment research** — monitor NHS hiring trends by band, speciality, region
- **Job alerts** — daily runs to watch new nursing, medical, or admin postings in specific trusts
- **Salary benchmarking** — aggregate pay data across NHS bands and locations
- **Workforce planning** — pull open positions into HR/ATS systems
- **Regional healthcare analysis** — compare vacancy counts across regions or trusts

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/nhs-jobs-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
