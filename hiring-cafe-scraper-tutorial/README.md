# Hiring Cafe Jobs Scraper Tutorial: Run This Apify Actor with Python

Extract global job postings from hiring.cafe including title, company, salary, location, remote status, seniority, visa sponsorship, and more.

This repository shows how to run [Hiring Cafe Jobs Scraper](https://apify.com/crawlerbros/hiring-cafe-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/hiring-cafe-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/hiring-cafe-scraper](https://apify.com/crawlerbros/hiring-cafe-scraper)
- **SEO title:** Hiring Cafe Jobs Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract global job postings from hiring.cafe including title, company, salary, location, remote status, seniority, visa sponsorship, and more.

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

# Hiring Cafe Jobs Scraper

Extract global job postings from **hiring.cafe** — an AI-powered job aggregator that indexes 2.9+ million listings from Greenhouse, Lever, Workable, Workday, SuccessFactors, Hirebridge, BambooHR, and 14,000+ direct company career pages. Returns **32 structured fields** per job including title, company, workplace type, seniority, salary (when disclosed), geolocation, required technical tools, company industries, and a direct apply URL.

## Features

- **32 output fields** per job — complete flat schema with typed defaults (zero nulls)
- **Direct apply URLs** — every job links back to the original ATS posting
- **Rich metadata** — workplace type (Remote/Hybrid/Onsite), seniority, commitment, category, required technical tools, min years experience, salary range when disclosed
- **Geolocation** — latitude/longitude per listing
- **Company enrichment** — hiring company name, website, industries, HQ country, employee count bucket
- **Filter support** — keyword search, workplace type, seniority level, commitment type, date range
- **Hardcoded RESIDENTIAL US proxy** — required to bypass Cloudflare Managed Challenge
- **Automatic Cloudflare bypass** — Patchright Chromium session with session rotation (typically solves in 8–20 seconds)

## Input

| Field | Type | Description |
|---|---|---|
| `searchQueries` | Array of strings | Keywords to search on hiring.cafe (e.g., `"software engineer"`, `"data scientist"`). Empty array returns unfiltered results. |
| `locations` | Array | Filter to jobs in these locations. Plain strings like `["San Francisco","London"]` or full `{label, value, countryCode, lat, lng}` dicts. |
| `workplaceTypes` | Array | Filter by workplace type: `Remote`, `Hybrid`, `Onsite` (default: all three) |
| `seniorityLevels` | Array | `No Prior Experience Required`, `Entry Level`, `Mid Level`, `Senior Level`, `Director`, `Executive` (default: all six) |
| `commitmentTypes` | Array | `Full Time`, `Part Time`, `Contract`, `Internship`, `Temporary`, `Seasonal`, `Volunteer` (default: all seven) |
| `dateFetchedPastNDays` | Integer | Only include jobs fetched within the last N days (default 30, max 365) |
| `maxItems` | Integer | Maximum jobs to return across all queries (default 50, max 1000) |
| `jobTitleQuery` | String | Filter to jobs whose **title** contains this phrase. |
| `jobDescriptionQuery` | String | Filter to jobs whose **description** contains this phrase. |
| `technologyKeywordsQuery` | String | Match against parsed tech-stack tags (e.g. `python`, `react`). |
| `requirementsKeywordsQuery` | String | Match against parsed requirement bullets. |
| `companyNames` | Array | Whitelist — only jobs from these companies. |
| `excludedCompanyNames` | Array | Blacklist — exclude jobs from these companies. |
| `companyKeywords` | Array | Substring-match the company name (whitelist). |
| `excludedCompanyKeywords` | Array | Substring-match (blacklist). |
| `industries` | Array | Limit to companies in these industries. |
| `excludedIndustries` | Array | Exclude companies in these industries. |
| `salaryCurrency` | Select | `USD` / `EUR` / `GBP` / `CAD` / `AUD` / `INR` / `JPY` / `CNY` / `MXN` / `BRL` (or empty for any). |
| `salaryFrequency` | Select | `Yearly` / `Monthly` / `Weekly` / `Daily` / `Hourly`. |
| `minSalary` | Integer | Lower bound for compensation, in the chosen currency + frequency. |
| `maxSalary` | Integer | Upper bound for compensation. |
| `onlyTransparentSalaries` | Boolean | Drop jobs that don't publish a salary range (default false). |
| `minYearsExperience` | Integer | Filter to jobs requiring at least this many years (default 0). |
| `maxYearsExperience` | Integer | Filter to jobs requiring at most this many years (default 20). |
| `securityClearances` | Array | `None`, `Confidential`, `Secret`, `Top Secret`, `Top Secret/SCI`, `Public Trust`, `Interim Clearances`, `Other`. |
| `sortBy` | Select | `default` (relevance) / `newest` / `oldest` / `salary_high_to_low` / `salary_low_to_high`. |

### Example Input

```json
{
    "searchQueries": ["software engineer", "data scientist"],
    "workplaceTypes": ["Remote", "Hybrid"],
    "seniorityLevels": ["Mid Level", "Senior Level"],
    "commitmentTypes": ["Full Time"],
    "dateFetchedPastNDays": 7,
    "maxItems": 100
}
```

Minimal input (just a keyword):

```json
{
    "searchQueries": ["nurse"],
    "maxItems": 20
}
```

## Output

Each job has **32 fields**. Every field is always present with a typed default (empty string, zero, empty list, or `false`) — **never `null`**.

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | String | Unique job ID |
| `objectID` | String | Search index object ID |
| `source` | String | Source ATS (`greenhouse`, `lever`, `workable`, `successfactors`, `hirebridge`, ...) |
| `boardToken` | String | Job board token on that ATS |
| `applyUrl` | String | Direct apply URL (redirects to original source) |
| `title` | String | Job title |
| `description` | String | Job description (HTML stripped, truncated to 2,000 chars) |
| `isExpired` | Boolean | Whether the listing is expired |

### Classification
| Field | Type | Description |
|---|---|---|
| `coreJobTitle` | String | Canonicalized core job title |
| `category` | String | Job category (e.g., `Engineering`, `Data and Analytics`, `Marketing`) |
| `seniorityLevel` | String | Comma-joined seniority tags (e.g., `"Mid Level"`, `"Senior Level"`) |
| `roleType` | String | `Individual Contributor` or `People Manager` |
| `commitment` | String | Commitment type (e.g., `"Full Time"`) |
| `workplaceType` | String | `Remote`, `Hybrid`, or `Onsite` |

### Location
| Field | Type | Description |
|---|---|---|
| `workplaceCountries` | Array | Country codes (e.g., `["US", "GB"]`) |
| `workplaceStates` | Array | State / region names |
| `workplaceCities` | Array | City names |
| `latitude` | Number | Primary location latitude |
| `longitude` | Number | Primary location longitude |

### Compensation & Requirements
| Field | Type | Description |
|---|---|---|
| `salaryMin` | Number | Minimum salary (yearly, if disclosed; `0` otherwise) |
| `salaryMax` | Number | Maximum salary (yearly, if disclosed) |
| `salaryCurrency` | String | Salary currency code |
| `salaryFrequency` | String | `Yearly`, `Hourly`, `Monthly`, etc. |
| `technicalTools` | Array | Required technologies / tools |
| `minYearsExperience` | Integer | Minimum YoE required (`0` if not specified) |
| `bachelorsDegreeRequirement` | String | Bachelor's degree requirement level |

### Company
| Field | Type | Description |
|---|---|---|
| `companyName` | String | Hiring company name |
| `companyWebsite` | String | Company homepage URL |
| `companyIndustries` | Array | Industry tags |
| `companyEmployees` | String | Employee count bucket (e.g., `"1001-5000"`) |
| `companyHqCountry` | String | Company HQ country code |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "id": "greenhouse___acme___4567890",
    "objectID": "greenhouse_acme_4567890",
    "source": "greenhouse",
    "boardToken": "acme",
    "applyUrl": "https://boards.greenhouse.io/acme/jobs/4567890",
    "title": "Senior Software Engineer, Backend",
    "description": "We are looking for a senior backend engineer to join our Platform team...",
    "coreJobTitle": "Software Engineer",
    "category": "Engineering",
    "seniorityLevel": "Senior Level",
    "roleType": "Individual Contributor",
    "commitment": "Full Time",
    "workplaceType": "Remote",
    "workplaceCountries": ["US"],
    "workplaceStates": ["California", "New York"],
    "workplaceCities": ["San Francisco", "New York"],
    "latitude": 37.7749,
    "longitude": -122.4194,
    "salaryMin": 160000.0,
    "salaryMax": 220000.0,
    "salaryCurrency": "USD",
    "salaryFrequency": "Yearly",
    "technicalTools": ["Python", "PostgreSQL", "Kubernetes", "Django"],
    "minYearsExperience": 5,
    "bachelorsDegreeRequirement": "Required",
    "companyName": "Acme Corp",
    "companyWebsite": "https://acme.example.com",
    "companyIndustries": ["Software", "SaaS"],
    "companyEmployees": "1001-5000",
    "companyHqCountry": "US",
    "isExpired": false,
    "scrapedAt": "2026-04-11T11:05:00+00:00"
}
```

## FAQ

**Q: Why is a RESIDENTIAL proxy required?**
Hiring.cafe uses Cloudflare Managed Challenge (Turnstile) which blocks all Apify datacenter IPs with `403 Just a moment...`. A real residential IP + a Chrome browser session with a ~10–20 second challenge-solve wait is needed. The proxy is hardcoded and applied automatically — no configuration needed from your side.

**Q: How does the Cloudflare bypass work?**
The scraper launches a Patchright Chromium browser on a RESIDENTIAL US proxy session, navigates to hiring.cafe, and waits for the Cloudflare managed challenge to self-solve (typically 8–20 seconds). Once `document.title` changes from `"Just a moment..."` to `"HiringCafe - AI Job Search"`, the browser has a valid `cf_clearance` cookie. All API calls are then made via in-browser `fetch()` so the Cloudflare session cookies are reused. If the first attempt doesn't solve within 60 seconds, the scraper rotates the proxy session and tries again (up to 6 attempts).

**Q: How does pagination work?**
The API returns ~120–160 jobs per page. The scraper walks pages via `&page=N` until `maxItems` is reached or results run out.

**Q: Why are some `salaryMin` / `salaryMax` values zero?**
Fewer than half of listings disclose salary on hiring.cafe. When not disclosed, both fields are `0.0` (typed default, not `null`).

**Q: Can I search by company?**
Yes — use `companyNames` (whitelist), `excludedCompanyNames` (blacklist), or `companyKeywords` (substring match). You can also still drop the company name into `searchQueries`, which matches against title, description, AND company name.

**Q: What's the difference between `seniorityLevel` and `minYearsExperience`?**
`seniorityLevel` is the categorical tag (`Mid Level`, `Senior Level`, etc.) assigned by hiring.cafe's classifier. `minYearsExperience` is the numeric minimum YoE extracted from the job description (may be `0` if not specified).

**Q: Are expired jobs included?**
No — by default hiring.cafe only returns active listings (`isExpired: false`). The field is preserved in the output for consistency.

**Q: How fresh is the data?**
`dateFetchedPastNDays` controls freshness. Default is 30 days. Set to `7` for last-week postings, or `1` for last-24-hours monitoring.

## Use Cases

- **Talent intelligence** — monitor hiring velocity for specific roles, companies, or regions
- **Compensation research** — aggregate salary ranges by role, seniority, and location (where disclosed)
- **Remote-work trends** — filter by `workplaceTypes: ["Remote"]` to track the remote-first market
- **ATS market share analysis** — group by `source` to see which ATS platforms are most used
- **Skills demand tracking** — aggregate `technicalTools` frequencies to spot rising technologies
- **Job alerts** — daily runs with narrow filters (e.g., `["python developer", "Remote"]`) to monitor new postings
- **Recruitment pipelines** — bulk-import matching listings into CRMs with all 32 fields ready to use

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/hiring-cafe-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
