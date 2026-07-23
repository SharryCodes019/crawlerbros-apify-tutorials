# ZipRecruiter Jobs Scraper Pro Tutorial: Run This Apify Actor with Python

Extract job postings from ZipRecruiter.com with FULL job descriptions. Returns title, company, location, salary, skills, and the full job description body per listing. Walks paginated search results.

This repository shows how to run [ZipRecruiter Jobs Scraper Pro](https://apify.com/crawlerbros/ziprecruiter-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ziprecruiter-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/ziprecruiter-scraper-pro](https://apify.com/crawlerbros/ziprecruiter-scraper-pro)
- **SEO title:** ZipRecruiter Jobs Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Extract job postings from ZipRecruiter.com with FULL job descriptions. Returns title, company, location, salary, skills, and the full job description body per listing. Walks paginated search results.

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

# ZipRecruiter Jobs Scraper Pro

Extract job postings from **ZipRecruiter.com** with **full job descriptions** — titles, companies, locations, salary ranges, remote/hybrid flags, apply URLs, and the complete job description body per listing.

## Features

- **Full job descriptions** — visits each job detail page to extract the complete description text
- **18 output fields** per job — includes all search-card data plus the full description
- **Search by keyword and location** — or pass any ZipRecruiter search URL directly
- **Employment type, days posted, radius, remote** filters available
- **Pagination** — walks `&page=N` up to `maxItems`
- **Parsed salary ranges** — `$80K - $180K/yr` → `salaryMin=80000`, `salaryMax=180000`, `salaryPeriod=year`
- **City + state extracted** from location text
- **Remote/hybrid detection** — boolean flags set when location mentions these
- **Deduplicated** — each card ID output only once (ZipRecruiter renders each job twice)
- **Omit-empty output** — fields absent in source data are omitted rather than set to null or zero

## Requirements

**RESIDENTIAL US proxy required.** ZipRecruiter uses Cloudflare with aggressive datacenter IP blocking. The proxy is pre-configured in the input — do not disable it.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `startUrls` | Array | — | ZipRecruiter search-result URLs with filters preserved |
| `search` | String | — | Keyword shortcut (e.g., "nurse", "data scientist") |
| `location` | String | — | City/state for keyword shortcut (e.g., "Austin, TX") |
| `jobType` | Enum | `any` | Employment type: `any`, `full_time`, `part_time`, `contract`, `internship`, `temporary` |
| `daysPosted` | Integer | `0` | Posted within N days (0 = any, max 30) |
| `radiusMiles` | Integer | `0` | Search radius in miles (0 = ZR default, max 100) |
| `remoteOnly` | Boolean | `false` | Restrict to remote-eligible positions |
| `maxItems` | Integer | `50` | Maximum jobs to return (1–500) |
| `proxyConfiguration` | Object | RESIDENTIAL US | Pre-configured; do not disable |

### Example Input — Keyword search

```json
{
    "search": "data scientist",
    "location": "San Francisco, CA",
    "maxItems": 25
}
```

### Example Input — Direct URL

```json
{
    "startUrls": [
        "https://www.ziprecruiter.com/jobs-search?search=nurse&location=Chicago%2C+IL&radius=25"
    ],
    "maxItems": 50
}
```

### Example Input — With filters

```json
{
    "search": "software engineer",
    "location": "Austin, TX",
    "jobType": "full_time",
    "daysPosted": 7,
    "remoteOnly": false,
    "maxItems": 100
}
```

## Output

Each job record contains the following fields (omit-empty — fields without data are not included):

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | String | ZipRecruiter job-card ID token |
| `jid` | String | Short job ID parsed from URL `jid` param |
| `url` | String | Full job posting URL |
| `title` | String | Job title |

### Company
| Field | Type | Description |
|---|---|---|
| `company` | String | Hiring company name |
| `companyUrl` | String | Company profile URL |
| `companyLogo` | String | Company logo image URL |

### Location
| Field | Type | Description |
|---|---|---|
| `location` | String | Full location text (incl. Remote/Hybrid suffix) |
| `city` | String | City (parsed) |
| `state` | String | 2-letter state abbreviation (parsed) |
| `isRemote` | Boolean | `true` if location contains "remote" |
| `isHybrid` | Boolean | `true` if location contains "hybrid" |

### Salary
| Field | Type | Description |
|---|---|---|
| `salary` | String | Formatted salary text (e.g., `"$80K - $180K/yr"`) |
| `salaryMin` | Number | Minimum salary (USD, absolute) |
| `salaryMax` | Number | Maximum salary (USD, absolute) |
| `salaryPeriod` | String | `year` / `hour` / `month` / `week` |

### Description (Pro)
| Field | Type | Description |
|---|---|---|
| `description` | String | Full job description text extracted from the detail page |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 UTC scrape timestamp |

### Example Output

```json
{
  "id": "abc123",
  "jid": "f4a8b2c1d",
  "title": "Senior Software Engineer",
  "company": "Acme Corp",
  "companyUrl": "https://www.ziprecruiter.com/c/Acme-Corp",
  "location": "Austin, TX",
  "city": "Austin",
  "state": "TX",
  "salary": "$130K - $160K/yr",
  "salaryMin": 130000,
  "salaryMax": 160000,
  "salaryPeriod": "year",
  "description": "We are looking for a senior software engineer to join our team...",
  "url": "https://www.ziprecruiter.com/c/Acme-Corp/Job/...",
  "scrapedAt": "2026-01-15T12:34:56Z"
}
```

## FAQ

**Q: Why does this require a residential proxy?**
ZipRecruiter is protected by Cloudflare which aggressively blocks datacenter IPs. The Pro version visits individual job detail pages to extract full descriptions, which requires a residential US proxy. The proxy is pre-configured in the input schema.

**Q: How do I get the full job description?**
It's included automatically in the `description` field. The Pro version visits each job detail page after collecting search results.

**Q: How do I construct a search URL?**
Run a search on ziprecruiter.com with your filters applied, then copy the URL. Or use the `search` + `location` + filter inputs to have the actor build the URL automatically.

**Q: Why is each job returned only once if the page shows 40 cards?**
ZipRecruiter renders each job twice — in both the search list pane and the detail pane. The scraper deduplicates by card ID so you get ~20 unique jobs per page.

**Q: How are salary values normalized?**
Salary text like `$80K - $180K/yr` is parsed so `salaryMin=80000.0`, `salaryMax=180000.0` (full dollar amounts, not K), `salaryPeriod=year`. If only one value appears, both min and max are set to that value. If no salary is available, salary fields are omitted.

**Q: What happens if ZipRecruiter blocks all sessions?**
A sentinel record `{"type":"job_ziprecruiter_blocked", ...}` is emitted so the run exits with code 0. You can detect this in downstream pipelines by checking the `type` field.

## Use Cases

- **Talent intelligence** — monitor hiring velocity for competitor companies
- **Compensation research** — aggregate salary ranges by role, location, and experience level
- **Remote-work trends** — filter and track remote listings across industries
- **Job description analysis** — full text available for NLP, skills extraction, or AI pipelines
- **Market entry analysis** — see how many companies are hiring in a specific region
- **Labor-market dashboards** — feed directly into BI tools without post-processing nulls

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ziprecruiter-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
