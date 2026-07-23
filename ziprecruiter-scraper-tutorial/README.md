# ZipRecruiter Jobs Scraper Tutorial: Run This Apify Actor with Python

Extract job postings from ZipRecruiter.com including title, company, location, salary range, city, state, and apply URL. Walks paginated search results without proxy or login.

This repository shows how to run [ZipRecruiter Jobs Scraper](https://apify.com/crawlerbros/ziprecruiter-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ziprecruiter-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ziprecruiter-scraper](https://apify.com/crawlerbros/ziprecruiter-scraper)
- **SEO title:** ZipRecruiter Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract job postings from ZipRecruiter.com including title, company, location, salary range, city, state, and apply URL. Walks paginated search results without proxy or login.

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

# ZipRecruiter Jobs Scraper

Extract job postings from **ZipRecruiter.com** — titles, companies, locations, salary ranges, remote/hybrid flags, and apply URLs. Walks search results page by page, no login, no proxy, no cookies required.

## Features

- **17 output fields** per job — complete listing data in a flat schema
- **Search by keyword and location** — or pass any ZipRecruiter search URL with filters preserved
- **Pagination** — walks `&page=N` up to `maxItems`
- **Parsed salary ranges** — `$80K - $180K/yr` → `salaryMin=80000`, `salaryMax=180000`, `salaryPeriod=year`
- **City + state extracted** from location text
- **Remote/hybrid detection** — booleans set when location text mentions these
- **No authentication, no proxy** — ZipRecruiter's public search pages accept Chrome 131 TLS impersonation from datacenter IPs
- **Deduplicated** — each card ID is output only once (ZipRecruiter renders each job twice across left/right panes)
- **No nulls** — every field has a typed default

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | Array | ZipRecruiter search-result URLs. Any filters applied in the URL (location, radius, salary, employment type) are preserved. |
| `search` | String | Keyword shortcut — combined with `location` to build a default search URL. |
| `location` | String | City / state for the keyword shortcut. |
| `maxItems` | Integer | Maximum jobs to return (default 50, max 500). |

### Example Input

```json
{
    "startUrls": [
        "https://www.ziprecruiter.com/jobs-search?search=software+engineer&location=New+York%2C+NY"
    ],
    "maxItems": 100
}
```

or keyword + location:

```json
{
    "search": "data scientist",
    "location": "San Francisco, CA",
    "maxItems": 50
}
```

## Output

Each job has **17 fields**. All fields are always present — empty strings, zero, or `false` for missing data, never `null`.

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
| `state` | String | State abbreviation (parsed) |
| `isRemote` | Boolean | `true` if location contains "remote" |
| `isHybrid` | Boolean | `true` if location contains "hybrid" |

### Salary
| Field | Type | Description |
|---|---|---|
| `salary` | String | Formatted salary text (e.g., `"$80K - $180K/yr"`) |
| `salaryMin` | Number | Minimum salary (USD, absolute, not K) |
| `salaryMax` | Number | Maximum salary (USD, absolute, not K) |
| `salaryPeriod` | String | `year` / `hour` / `month` / `week` |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

## FAQ

**Q: Do I need a proxy?**
No for search pages — ZipRecruiter's public search endpoint accepts Chrome 131 TLS impersonation from datacenter IPs directly. Detail pages (individual job posts) are more aggressively protected by Cloudflare, so this scraper only uses search-page data.

**Q: How do I construct a search URL?**
Run a search on ziprecruiter.com with your filters applied, then copy the URL. The `search` and `location` params are the minimum. Other filters (e.g. `radius`, `days`, `refine_by_salary`, `refine_by_employment`) pass through verbatim.

**Q: Does it include the full job description?**
No. The full description lives on the detail page (`/c/.../Job/...?jid=...`), which requires residential proxy access. This scraper stays on search pages only for reliable, zero-cost scraping. You can use the `url` field to fetch descriptions with a separate tool.

**Q: Why is each job returned only once if the page has 40 cards?**
ZipRecruiter renders each job twice — once in the search list pane and once in the detail pane. The scraper deduplicates by the internal card ID so you get 20 unique jobs per page (not 40).

**Q: How are salary values normalized?**
Salary text like `$80K - $180K/yr` is parsed so `salaryMin=80000.0`, `salaryMax=180000.0` (full dollar amounts, not K), `salaryPeriod=year`. If only one value is given (e.g. `$25/hr`), both min and max are set to that value.

**Q: What happens if a job has no salary?**
`salary` is an empty string and `salaryMin`/`salaryMax` are `0.0` — typed defaults, not nulls.

## Use Cases

- **Talent intelligence** — monitor hiring velocity for competitor companies
- **Compensation research** — aggregate salary ranges by role, location, or experience level
- **Remote-work trends** — filter by `isRemote=true` to track remote listings by industry
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

- [Run this actor on Apify](https://apify.com/crawlerbros/ziprecruiter-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
