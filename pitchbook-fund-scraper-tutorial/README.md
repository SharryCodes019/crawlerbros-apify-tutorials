# PitchBook Fund Data Scraper Tutorial: Run This Apify Actor with Python

Scrape public fund profile metadata from PitchBook without a subscription. Supports text search, direct profile URLs, and bulk sitemap discovery. Returns fund name, strategy, size, vintage year, manager, status, location, and more.

This repository shows how to run [PitchBook Fund Data Scraper](https://apify.com/crawlerbros/pitchbook-fund-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/pitchbook-fund-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/pitchbook-fund-scraper](https://apify.com/crawlerbros/pitchbook-fund-scraper)
- **SEO title:** PitchBook Fund Data Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public fund profile metadata from PitchBook without a subscription. Supports text search, direct profile URLs, and bulk sitemap discovery. Returns fund name, strategy, size, vintage year, manager, status, location, and more.

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

# PitchBook Fund Data Scraper

Extract publicly available fund profile data from [PitchBook](https://pitchbook.com) — no subscription or login required. Supports three modes: scrape specific fund profiles by URL, search by keyword, or bulk-collect thousands of funds via PitchBook's sitemap.

## What This Scraper Does

This actor fetches fund profile pages from PitchBook and extracts all publicly visible metadata: fund name, strategy, size, vintage year, manager details, status, location, investment counts, and more. It does **not** require a PitchBook account.

## Input

| Field | Type | Description |
|---|---|---|
| **Profile URLs** | List of strings | Direct fund profile URLs (e.g. `https://pitchbook.com/profiles/fund/11295-73F`) or bare IDs (e.g. `11295-73F`). When provided, Search Query is ignored. |
| **Search Query** | String | Keyword search (e.g. `venture capital`, `buyout europe`). Used when no Profile URLs are given. |
| **Max Items** | Integer | Maximum number of fund records to return (1–100,000). Ignored in direct URL mode. Default: 10. |
| **Proxy Configuration** | Proxy object | Residential proxy is **required** for reliable scraping. PitchBook's Cloudflare protection rate-limits repeated requests from the same IP. |

### Input Modes

1. **Direct** — Provide one or more fund profile URLs. All are processed regardless of Max Items.
2. **Search** — Provide a search query. The scraper paginates PitchBook search results and returns up to Max Items funds matching your query.
3. **Bulk** — Leave both fields empty. The scraper streams fund URLs from PitchBook's public sitemaps and returns up to Max Items funds.

## Output

Each record represents one fund profile. Fields marked with `?` are optional — they appear only when PitchBook makes them publicly available.

| Field | Type | Description |
|---|---|---|
| `name` | string | Fund name |
| `profileUrl` | string | Canonical PitchBook fund profile URL |
| `description` | string? | Fund description |
| `logoUrl` | string? | Fund manager logo URL |
| `socialLinks` | object? | Social profiles (twitter, linkedin, facebook) |
| `fundStrategy` | string? | Investment strategy (e.g. Buyout, Venture Capital) |
| `fundStatus` | string? | Fund lifecycle status (e.g. Active, Liquidated) |
| `fundSize` | string? | Total committed capital (e.g. $6.11B) |
| `vintageYear` | integer? | Year the fund was raised |
| `fundCategory` | string? | Asset class (e.g. Private Equity, Venture Capital) |
| `fundFamily` | string? | Fund family name |
| `fundManager` | string? | Managing firm name |
| `fundManagerUrl` | string? | PitchBook profile URL of the managing firm |
| `fundManagerWebsite` | string? | Managing firm's external website URL |
| `fundDomiciles` | string? | Domicile jurisdiction(s) of the fund (e.g. United States: Delaware) |
| `nativeCurrency` | string? | Fund's reporting currency (e.g. USD, EUR) |
| `totalInvestments` | integer? | Number of portfolio investments |
| `totalLimitedPartners` | integer? | Number of limited partners |
| `streetAddress` | string? | Manager street address |
| `postalCode` | string? | Manager postal code |
| `city` | string? | Manager city |
| `state` | string? | Manager state / region |
| `country` | string? | Fund domicile country |
| `scrapedAt` | string | ISO 8601 UTC timestamp of when the record was scraped |

### Error Records

If a profile cannot be fetched or parsed, the record will contain:

| Field | Description |
|---|---|
| `inputUrl` | The URL or ID that was attempted |
| `error` | Human-readable error message |
| `scrapedAt` | Timestamp |

## Frequently Asked Questions

**Do I need a PitchBook account?**
No. This scraper only extracts data from public PitchBook pages that are visible to any visitor without logging in.

**Why is a proxy required?**
PitchBook uses Cloudflare to protect its pages. Without rotating residential proxies, repeated requests from the same IP address will be blocked. The scraper uses Apify's residential proxy pool by default.

**What data is NOT available?**
Fields that require a PitchBook subscription are not included: IRR, DPI, RVPI, TVPI fund returns, dry powder, deal sizes, LP commitment amounts, investment strategy charts, fund terms & fees, and full contact phone numbers.

**How many funds are available in bulk mode?**
PitchBook's public sitemaps contain approximately 150,000+ fund profiles. Use Max Items to control how many are scraped per run.

**Can I search for funds by strategy or geography?**
Yes. Use Search Query with terms like `buyout europe`, `venture capital berlin`, or `growth equity asia`.

**What fund URL format does PitchBook use?**
Fund profile URLs follow the pattern `https://pitchbook.com/profiles/fund/{id}F` where the ID ends with a capital `F` (e.g. `11295-73F`). This distinguishes fund profiles from investor profiles (`/profiles/investor/11295-73`).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/pitchbook-fund-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
