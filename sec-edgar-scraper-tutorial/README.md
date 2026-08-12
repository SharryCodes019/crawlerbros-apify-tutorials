# SEC EDGAR Filings Scraper Tutorial: Run This Apify Actor with Python

Scrape SEC EDGAR filings (10-K, 10-Q, 8-K, Form 4 insider trades, 13F holdings) for any US public company. HTTP-only via the SEC's public API. No login, no proxy, no auth.

This repository shows how to run [SEC EDGAR Filings Scraper](https://apify.com/crawlerbros/sec-edgar-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/sec-edgar-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/sec-edgar-scraper](https://apify.com/crawlerbros/sec-edgar-scraper)
- **SEO title:** SEC EDGAR Filings Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape SEC EDGAR filings (10-K, 10-Q, 8-K, Form 4 insider trades, 13F holdings) for any US public company. HTTP-only via the SEC's public API. No login, no proxy, no auth.

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

# SEC EDGAR Filings Scraper

Scrape SEC EDGAR — the US Securities and Exchange Commission's public database of every filing every public US company makes. Annual reports (10-K), quarterly reports (10-Q), material event disclosures (8-K), insider transactions (Form 4), hedge-fund holdings (13F), proxy statements, IPO prospectuses, and more. HTTP-only via the SEC's official JSON API. No login, no proxy.

## What this actor does

- Resolves tickers (e.g. `AAPL`) or CIKs to company records via SEC's master ticker map
- Fetches recent filings for each company from `https://data.sec.gov/submissions/CIK<padded>.json`
- Filters by filing type (32 supported types), date range, and free-text keyword
- Optionally fetches the primary document HTML and emits cleaned text (for keyword search across filing text)
- Builds direct URLs to the filing index page, primary document, and EDGAR detail page
- Honors SEC's 10-requests-per-second rate limit + required User-Agent header

## Output per filing

- `cik` (10-digit padded), `cikInt`, `companyName`, `ticker`, `tickers[]`, `exchange`, `sic`, `sicDescription`
- `filingType` — e.g. `10-K`, `10-Q`, `8-K`, `4`
- `accessionNumber` — SEC's unique filing ID
- `filedAt` — date filed
- `reportingPeriod` — fiscal period the filing covers
- `acceptedAt` — exact timestamp of acceptance
- `primaryDocFilename`, `primaryDocDescription`
- `primaryDocUrl` — direct link to the actual filing document
- `filingIndexUrl` — search results page on EDGAR
- `filingDetailUrl` — filing's detail page on EDGAR
- `sizeBytes`, `isXbrl`, `isInlineXbrl`
- `primaryDocText` (only when `fetchPrimaryDocText=true`) — plain-text content of the filing, capped at 100k chars
- `primaryDocTextLength`
- `recordType: "filing"`, `scrapedAt`

Empty fields are omitted (no nulls).

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `companies` | array | `["AAPL","MSFT"]` | Tickers (resolves automatically) or 10-digit CIKs |
| `filingTypes` | array | `["10-K","10-Q","8-K"]` | 32 supported types: 10-K, 10-Q, 8-K, DEF 14A, S-1, 13F-HR, 4, 3, 5, etc. |
| `dateRangeFrom` | string | – | Drop filings filed before this ISO date |
| `dateRangeTo` | string | – | Drop filings filed after this ISO date |
| `maxItemsPerCompany` | int | `50` | Hard cap per company (1–1000) |
| `maxItems` | int | `500` | Global hard cap (1–10000) |
| `fetchPrimaryDocText` | bool | `false` | Fetch + extract the filing document's plain text |
| `containsKeyword` | string | – | Only emit filings whose text contains this substring (implies `fetchPrimaryDocText`) |
| `userAgentEmail` | string | `apify-actor@noreply.apify.com` | Contact email for SEC's required User-Agent header |

### Example: latest annual reports for tech giants

```json
{
  "companies": ["AAPL", "MSFT", "GOOGL", "META", "AMZN", "NVDA"],
  "filingTypes": ["10-K"],
  "maxItemsPerCompany": 5
}
```

### Example: insider trades for a single company

```json
{
  "companies": ["TSLA"],
  "filingTypes": ["4"],
  "maxItemsPerCompany": 100
}
```

### Example: 8-K events with keyword search

```json
{
  "companies": ["AAPL"],
  "filingTypes": ["8-K"],
  "fetchPrimaryDocText": true,
  "containsKeyword": "acquisition",
  "dateRangeFrom": "2024-01-01"
}
```

### Example: hedge-fund holdings (13F)

```json
{
  "companies": ["0001067983"],
  "filingTypes": ["13F-HR"],
  "maxItemsPerCompany": 20
}
```

## Use cases

- **Equity research** — pull every 10-K and 10-Q for a portfolio
- **Insider trade alerts** — daily run on `Form 4` filings for executives at watched companies
- **M&A monitoring** — `S-4` registrations + `8-K` event disclosures filtered for "acquisition" keyword
- **IPO tracking** — `S-1` and `S-3` filings to spot upcoming listings
- **Hedge fund replication** — `13F-HR` filings to mirror prominent fund managers' positions
- **Compliance audits** — verify filings for portfolio companies
- **Financial journalism** — programmatic access to public filings without paying Bloomberg
- **XBRL data extraction** — `isXbrl` flag identifies machine-readable filings for downstream parsers

## FAQ

**Does it require a login or cookies?**  No. SEC EDGAR is fully public.

**Is a proxy needed?**  No. SEC accepts requests from any IP, with a soft 10 req/sec rate limit.

**Why does SEC require a User-Agent email?**  SEC's fair-access policy requires every API request to include a contact email so they can reach the operator if there's an issue. The actor uses a generic Apify-actor email by default; for production high-volume scraping, override with your own.

**How fresh is the data?**  Real-time. SEC processes filings within minutes of submission.

**What's the difference between `cik` and `accessionNumber`?**  `cik` identifies the company; `accessionNumber` identifies a specific filing. Each filing has a unique accession (e.g. `0000320193-24-000123`).

**Can I get the full filing text?**  Yes — set `fetchPrimaryDocText: true` to also fetch the primary document and emit cleaned plain text (capped at 100k chars per record). Combine with `containsKeyword` to filter to filings mentioning a specific term.

**What's the difference between 10-K and 20-F?**  10-K is for US-domiciled companies; 20-F is for foreign-domiciled companies (e.g. ADRs). Same purpose: annual report.

**Can I scrape a private company?**  No — only US public companies and foreign companies that file with the SEC. Private companies don't file.

**How is `13F-HR` different from `SC 13G`?**  `13F-HR` is a hedge fund's quarterly position list (all holdings >$100M AUM). `SC 13G` is a 5%+ ownership disclosure for any single security. Both useful for tracking institutional money flows.

**What's an XBRL filing?**  Machine-readable structured filing format. The actor's `isXbrl` and `isInlineXbrl` flags tell you which filings have parseable structured data — useful for downstream financial-data extraction.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/sec-edgar-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
