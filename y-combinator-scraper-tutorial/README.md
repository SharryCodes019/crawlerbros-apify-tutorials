# Y Combinator Companies Scraper Tutorial: Run This Apify Actor with Python

Scrape the full Y Combinator company directory with company profiles, founders, open jobs, batch, industry, status, and social links. HTTP-only, no login required.

This repository shows how to run [Y Combinator Companies Scraper](https://apify.com/crawlerbros/y-combinator-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/y-combinator-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/y-combinator-scraper](https://apify.com/crawlerbros/y-combinator-scraper)
- **SEO title:** Y Combinator Companies Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape the full Y Combinator company directory with company profiles, founders, open jobs, batch, industry, status, and social links. HTTP-only, no login required.

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

# Y Combinator Companies Scraper

Scrape the complete [Y Combinator company directory](https://www.ycombinator.com/companies) — 5,000+ startups across every batch from 2005 to today. Get company profiles, founders, open jobs, industry tags, batch, status, funding stage, team size, and social links. HTTP-only; no login, no cookies, no proxy required.

## Output (per company)

- `type` = `yc_company`
- `id` (slug), `slug`, `url`, `name`, `kind` (startup / non-profit / etc.)
- `shortDescription`, `longDescription`, `pitch` (full pitch text when present)
- `batch` (e.g. `S24`), `industry`, `subIndustry`, `status` (Active / Inactive / Acquired / Public), `stage` (Seed / Series A / etc.)
- `location`, `allLocations`, `regions`, `foundingYear`, `launchedAt` (unix), `teamSize`
- `website`, `linkedin`, `twitter`, `facebook`, `crunchbase`, `wellfound`, `github`
- `logo`, `logoThumb`, `demoDayVideo`
- `isHiring`, `isCompanyHiring`, `jobCount`
- `tags` — when Algolia returns them
- `formerNames` — list, when the company has rebranded
- `topCompany`, `topCompanyBadge`, `ycdcBadgeName`, `nonprofit` — when flagged
- `questionsAndAnswers` — `[{ question, answer }]` short founder Q&A blocks
- `teamHighlights` — list of blurbs about the team
- `highlightBlackFounders`, `highlightWomenFounders`, `highlightHispanicFounders` — only when Algolia explicitly flags them
- `founders` — `[{ name, title, bio, email, linkedin, twitter, hackerNews, github, instagram }]` when `scrapeFounders = true`
- `openJobs` — `[{ title, url, applyUrl, location, remote, type, role, team, yearsExperience, salaryMin, salaryMax, compensationCurrency, equity, equityRange, skills, experience, visa, visaSupported, englishFluent }]` when `scrapeOpenJobs = true`
- `scrapedAt`

If zero companies match the filters, a single `yc_company_blocked` sentinel record is emitted so runs always exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `directoryUrl` | string | YC directory URL. Default: `https://www.ycombinator.com/companies`. |
| `query` | string | Optional free-text search (`?q=<query>`). |
| `batch` | enum | `any`, `S24`, `W24`, `F24`, `S23`, `W23`, `S22`, `W22`, `S21`, `W21`. |
| `industry` | string | Exact-match industry filter (e.g. `B2B`, `Consumer`, `Fintech`, `Healthcare`). |
| `status` | enum | `any`, `Active`, `Inactive`, `Acquired`, `Public`. |
| `scrapeFounders` | boolean | Fetch founder details per company. Default `true`. |
| `scrapeOpenJobs` | boolean | Fetch open job postings per company. Default `true`. |
| `regions` | string[] | Optional region filter (case-insensitive) — matched against `location`. |
| `tags` | string[] | Optional tag filter (case-insensitive) — matched against `industry`, `subIndustry`, `tags`. |
| `highlightBlackFounders` | boolean | Only include companies flagged with Black founders. |
| `highlightWomenFounders` | boolean | Only include companies flagged with women founders. |
| `highlightHispanicFounders` | boolean | Only include companies flagged with Hispanic / Latino founders. |
| `maxItems` | integer | Max companies per run (1–5500). Default 3. |

## How it works

1. Query Y Combinator's public Algolia search index (`YCCompany_production`) for companies matching your filters. Pagination is handled transparently.
2. For each company, optionally fetch its detail page (`/companies/<slug>`) and parse the Inertia `data-page` JSON blob to get founders and open jobs.
3. Jobs expose salary range, equity, skills, visa policy, and the apply URL.
4. Output uses a strict no-nulls contract — every field present is non-empty.

## FAQ

**Do I need a proxy?** No. YC is publicly accessible from datacenter IPs.

**Does the scraper need YC credentials?** No. All data comes from public endpoints.

**How many companies are in the directory?** About 5,800 across all batches (growing each cycle). `maxItems` caps per run at 5,500.

**Are historical founders included?** Yes — every company's founder list is preserved on its public profile, including exits.

**Why does `jobCount` sometimes differ from the directory badge?** YC's directory badge counts only open job postings; we return the exact set embedded in the profile page.

**What's the `yc_company_blocked` record?** When your filter returns zero matches (e.g. a typo in `industry`), we emit one sentinel record so downstream pipelines never see an empty output.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/y-combinator-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
