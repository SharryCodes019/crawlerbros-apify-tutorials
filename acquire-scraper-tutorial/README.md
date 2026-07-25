# Acquire.com Startup Marketplace Scraper Tutorial: Run This Apify Actor with Python

Scrape public startup acquisition listings from Acquire.com with titles, asking price, annual revenue/profit, category, and descriptions. HTTP-only via the public sitemap + SSR listing pages; no login required.

This repository shows how to run [Acquire.com Startup Marketplace Scraper](https://apify.com/crawlerbros/acquire-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/acquire-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/acquire-scraper](https://apify.com/crawlerbros/acquire-scraper)
- **SEO title:** Acquire.com Startup Marketplace Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public startup acquisition listings from Acquire.com with titles, asking price, annual revenue/profit, category, and descriptions. HTTP-only via the public sitemap + SSR listing pages; no login required.

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

# Acquire.com Startup Marketplace Scraper

Scrape public startup acquisition listings from **[Acquire.com](https://acquire.com)** — headline, category, asking price, annual revenue, annual profit, description, derived revenue / profit multiples, and canonical URL. HTTP-only; **no login, no cookies, no browser**.

## What this scrapes

Acquire's marketplace has two surfaces:

| Surface                                 | URL shape                       | Auth | Scrapable? |
|-----------------------------------------|----------------------------------|------|------------|
| **Public SEO listing page**            | `/startup/<slug>`               | No   | Yes        |
| Internal SPA marketplace (SPA with filters) | `/startups/<id>` / `/startups?categories=...` | Yes (login required) | No |

This actor targets the public listing pages — the same URLs Acquire exposes to Google via `robots.txt` and `sitemap.xml`. The auth-gated SPA variant (asking-price history, customers, churn, GA analytics, tech stack, etc.) is **not** accessible without an authenticated Acquire account and is intentionally out of scope.

## Output (per listing)

| Field               | Always present? | Description |
|---------------------|:---------------:|-------------|
| `type`              | Yes | `"acquire_listing"` |
| `url`               | Yes | Canonical `/startup/<slug>` URL |
| `id`                | Yes | 10-character short ID from the slug |
| `scrapedAt`         | Yes | ISO-8601 UTC timestamp |
| `listingHeadline`   | Yes | Listing title (e.g. "Turnkey Calendly Alternative — 500+ Users …") |
| `listingType`       | When category known | Always `"startup_acquisition"` |
| `category`          | When present | `SaaS`, `Ecommerce`, `Content`, `Services`, `Mobile Apps`, etc. |
| `askingPrice`       | When present | USD integer |
| `priceCurrency`     | When present | ISO currency from JSON-LD `offers.priceCurrency` (e.g. `"USD"`) |
| `revenueAnnual`     | When present | USD integer |
| `profitAnnual`      | When present | USD integer |
| `revenueMultiple`   | When derivable | `askingPrice / revenueAnnual` |
| `profitMultiple`    | When derivable | `askingPrice / profitAnnual` |
| `about`             | When present | Full description (long form, with bullet points) |
| `status`            | When known | `"available"` or `"sold"` |
| `image`             | When present | Preview image URL from JSON-LD `image` / `og:image` |
| `brand`             | When present | Brand name from JSON-LD `brand.name` (typically `"Acquire.com"`) |
| `source`            | When present | Site name from `og:site_name` (typically `"Acquire.com"`) |
| `canonicalUrl`      | When present | Canonical URL from JSON-LD `url` / `<link rel="canonical">` / `og:url` |
| `pageType`          | When present | Open Graph `og:type` (typically `"website"`) |

Fields are omitted rather than emitted as `null` — if you see a key, the value is real.

If zero listings match your filters, a single `acquire_blocked` sentinel row is emitted so runs always exit 0.

## Input

| Field | Type | Description |
|---|---|---|
| `urls` | string[] | Direct `/startup/<slug>` URLs. Overrides sitemap / filter search. |
| `categories` | string[] | Filter by category (e.g. `SaaS`, `Ecommerce`). |
| `minPrice` | integer | Minimum asking price (USD). |
| `maxPrice` | integer | Maximum asking price (USD). |
| `minAnnualRecurringRevenue` | integer | Minimum annual revenue (USD). |
| `locations` | string[] | Location substring filter (case-insensitive). |
| `verifiedBusiness` | boolean | Only return listings whose copy mentions "verified". Default `false`. |
| `sortBy` | enum | `newest` (default), `oldest`, `price-low`, `price-high`. Based on sitemap `lastmod`. |
| `maxItems` | integer | 1 – 500. Default 3. |
| `proxyConfiguration` | object | Apify proxy. Default Residential US. |

## How it works

1. Fetch the public sitemap at `https://app.acquire.com/sitemap.xml` (≈1,300 listing URLs with `<lastmod>`).
2. Sort entries by `lastmod` (newest / oldest) or over-fetch + sort by price (for `price-low` / `price-high`).
3. For each `/startup/<slug>` URL, fetch the server-rendered page via `curl_cffi` with Chrome-131 TLS impersonation. Proxy rotates per retry.
4. Parse the `application/ld+json` `Product` schema + the hidden `#ssr-content` block (`<h1>`, `<p>`, `<dl>` with Category / Asking Price / Annual Revenue / Annual Profit) + meta tags (`article:section`, `og:description`).
5. Apply post-filters (category, price bounds, annual revenue, locations, verified).
6. Emit up to `maxItems`; emit a sentinel on zero matches.

## FAQ

**Do I need to log into Acquire?** No — we only scrape the public pages exposed to search engines.

**Can you scrape churn, customer count, tech stack, GA analytics, team size?** No — those live behind the authenticated SPA (`/startups/<id>`) and are not part of the public SSR payload. We only emit fields we can populate.

**Why does `/startups/<id>` not work?** The app's internal route is JS-rendered and redirects unauthenticated visitors to `/signin`. The public `/startup/<slug>` route (note the singular) is the one Acquire ships for crawlers.

**What counts as "verified"?** The public SSR pages don't expose a structured verified flag. When `verifiedBusiness = true` we keep listings whose headline or description literally mentions "verified".

**Why does `sortBy` use `lastmod`?** The sitemap is the only cross-category public index we have — `lastmod` is the closest proxy to listing freshness. Price sorts over-fetch and re-sort in-process.

## Reliability notes

- Residential US proxy is the default — Acquire's origin is polite to datacenter IPs too, but residential keeps long-running daily tests consistent.
- Per-retry proxy rotation (fresh session_id each attempt) to shake off any transient 403 / rate limit.
- Sentinel emitted on zero pushes so daily Apify test runs always exit 0.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/acquire-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
