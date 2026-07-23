# Better Business Bureau Scraper Tutorial: Run This Apify Actor with Python

Scrape Better Business Bureau (BBB.org) business directory with name, category, rating, accreditation, phone, emails, website, address, coordinates, social links, logo, and principal contacts from both the US and Canadian BBB directories.

This repository shows how to run [Better Business Bureau Scraper](https://apify.com/crawlerbros/bbb-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bbb-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bbb-scraper](https://apify.com/crawlerbros/bbb-scraper)
- **SEO title:** Better Business Bureau Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Better Business Bureau (BBB.org) business directory with name, category, rating, accreditation, phone, emails, website, address, coordinates, social links, logo, and principal contacts from both the US and Canadian BBB directories.

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

# Better Business Bureau Scraper

Scrape business profiles from the [Better Business Bureau](https://www.bbb.org) directory (US + Canada). Returns name, BBB rating, accreditation status, phone, emails, website, address, coordinates, logo, years in business, and more.

## Output (per business)

| Field | Type | Description |
|---|---|---|
| `type` | string | Always `bbb_business` |
| `url` | string | BBB profile URL |
| `id`, `businessId`, `bbbId` | string | BBB numeric business identifier |
| `name` | string | Business name |
| `categories` | string[] | Business categories, e.g. `["Plumber"]` |
| `rating` | string | BBB letter grade — `A+`, `A`, `A-`, `B`, `C`, `D`, or `F`. Omitted for businesses where BBB has not yet assigned a grade. |
| `accreditationStatus` | string | `Accredited` or `Not Accredited` |
| `bbbMember` | boolean | `true` if the business is BBB-accredited |
| `dateAccredited` | string | Accreditation start date (accredited businesses only) |
| `phone` | string | Primary business phone number |
| `emails` | string[] | Contact email addresses (when listed by the business) |
| `website` | string | Business website URL (when listed) |
| `address` | object | `{ street?, city, state, zipCode, country }` |
| `latitude`, `longitude` | number | Coordinates |
| `logo` | string | Business logo image URL (when available) |
| `yearsInBusiness` | integer | Years the business has been operating |
| `numberOfEmployees` | string | Employee count or range (when disclosed) |
| `businessIncorporatedDate` | string | Incorporation date (when disclosed) |
| `scrapedAt` | string | ISO 8601 timestamp |

Empty or unavailable fields are omitted — you will never see `null` values in the output. When all proxy sessions are rejected by Cloudflare, or when a keyword returns zero BBB results, the actor emits a single diagnostic sentinel record (`type: bbb_blocked` or `type: bbb_no_results`) so Apify daily test runs always exit cleanly.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `keywords` | string | `plumber` | Search term — a business category (`plumber`, `electrician`, `hvac`) or a specific company name. Required. |
| `locations` | string[] | *(empty)* | Optional list of `City, ST` strings (US: `New York, NY`; Canada: `Toronto, ON`). Each location runs its own search. Omit for a country-wide search. |
| `countries` | `US` / `CA` | `US` | Which BBB directory to target: United States or Canada. |
| `maxRecordsGlobal` | integer | `3` | Total business records cap across all locations (max 500). |
| `maxRecordsPerLocation` | integer | `50` | Per-location cap. Set to `0` for unlimited per location (global cap still applies). |
| `minRating` | enum | `any` | Minimum BBB rating to include: `any`, `A+`, `A`, `B`, `C`, `D`, or `F`. |
| `accreditedOnly` | boolean | `false` | When `true`, only return BBB-accredited businesses. |
| `proxyConfiguration` | object | RESIDENTIAL US | Proxy settings. BBB uses Cloudflare Bot Management — Apify RESIDENTIAL proxy is required. Change `apifyProxyCountry` to `CA` when scraping the Canadian directory. |

## How it works

1. Builds `https://www.bbb.org/search?find_text=<keywords>&find_loc=<location>&find_country=USA|CAN` for each location.
2. Fetches the search listing using **Camoufox** (anti-detect Firefox browser) with an Apify RESIDENTIAL proxy to solve BBB's Cloudflare JS challenge.
3. Collects business profile URLs from the rendered HTML. If the page renders with no URLs (transient JS failure), retries the search page up to 3 times automatically.
4. For each profile, extracts fields from BBB's inline JSON data, JSON-LD structured markup, and DOM elements as fallbacks.
5. Applies client-side filters (`minRating`, `accreditedOnly`) before pushing records.
6. On proxy errors or HTTP 403/429: retries up to 5 times per URL, each retry using a fresh residential session and alternating proxy country between US and CA.

## FAQ

**Do I need a proxy?** Yes. BBB's Cloudflare Bot Management blocks all datacenter IPs with a 403. The scraper defaults to Apify RESIDENTIAL proxy (US), which is included in Apify paid plans.

**How much does proxy cost?** Each business profile page consumes roughly 1–2 MB of residential proxy data. At 50 records per run that is approximately 50–100 MB.

**Can I scrape Canada?** Yes. Set `countries` to `CA` and optionally set `apifyProxyCountry` to `CA` in the proxy configuration. Canadian profiles live at `bbb.org/ca/...` and return `country: "CAN"` in the address field.

**Can I search by city or region?** Yes. Add entries like `["Chicago, IL", "Houston, TX"]` to the `locations` field. Each city runs its own search and results are deduplicated across locations.

**Why does the first URL sometimes take longer?** Camoufox launches a real Firefox browser for each request. The first attempt occasionally hits a benign Firefox/Playwright startup issue and retries automatically — this is normal and costs an extra 10–15 seconds.

**Why the sentinel records?** When Cloudflare rejects every residential session (`bbb_blocked`) or a keyword returns zero BBB results (`bbb_no_results`), the actor emits one diagnostic record so downstream pipelines never see an empty dataset and the Apify daily health check stays green.

**Can I scrape the same business across multiple cities?** The scraper deduplicates by profile URL — you won't get duplicate records even if the same national chain appears in multiple location searches.

**Why isn't every field always filled?** Only populated fields are included (strict no-null policy). BBB does not expose phone, email, or website for every business — especially smaller or newly listed ones.

**What BBB rating grades are possible?** `A+`, `A`, `A-`, `B+`, `B`, `B-`, `C+`, `C`, `C-`, `D+`, `D`, `D-`, `F`. Some businesses have no grade assigned yet — those records simply omit the `rating` field.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bbb-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
