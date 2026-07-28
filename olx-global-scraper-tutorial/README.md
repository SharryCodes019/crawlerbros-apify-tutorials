# OLX Global Scraper Tutorial: Run This Apify Actor with Python

Scrape OLX classified-ad listings across 24 countries (Poland, Ukraine, Brazil, India, Pakistan, Indonesia, Argentina, Türkiye, Portugal, ...). Search by keyword, browse by category / city, fetch listing details, list seller ads, or accept any OLX URL.

This repository shows how to run [OLX Global Scraper](https://apify.com/crawlerbros/olx-global-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/olx-global-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/olx-global-scraper](https://apify.com/crawlerbros/olx-global-scraper)
- **SEO title:** OLX Global Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape OLX classified-ad listings across 24 countries (Poland, Ukraine, Brazil, India, Pakistan, Indonesia, Argentina, Türkiye, Portugal, ...). Search by keyword, browse by category / city, fetch listing details, list seller ads, or accept any OLX URL.

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

# OLX Global Scraper

Scrape classified-ad listings from OLX across **24 countries** — Poland, Ukraine, Brazil, Romania, Bulgaria, India, Pakistan, Indonesia, Argentina, Colombia, Chile, Peru, Türkiye, South Africa, Kazakhstan, Uzbekistan, Morocco, Algeria, Tunisia, Lebanon, Jordan, Qatar, Portugal, Dominican Republic.

Search by keyword, browse by category or city, fetch single-listing detail pages, list a seller's ads, or paste any OLX URL.

## What you can do

- **Search listings** by free-text query in any of OLX's 24 country sites.
- **Browse a category** (cars, electronics, real estate, jobs, fashion, ...).
- **Browse a city / region** within a country (with optional keyword filter).
- **Fetch single listing details** — full description, all photos, breadcrumb category, seller name, price, location.
- **List a seller's listings** — every active ad on a user profile.
- **Paste any OLX URL** — listing, search, category, city, seller — and the actor classifies it automatically.

## Supported countries

| Code | Country | Domain | Currency |
|---|---|---|---|
| pl | Poland | olx.pl | PLN |
| ua | Ukraine | olx.ua | UAH |
| ro | Romania | olx.ro | RON |
| bg | Bulgaria | olx.bg | BGN |
| kz | Kazakhstan | olx.kz | KZT |
| uz | Uzbekistan | olx.uz | UZS |
| br | Brazil | olx.com.br | BRL |
| ar | Argentina | olx.com.ar | ARS |
| co | Colombia | olx.com.co | COP |
| cl | Chile | olx.cl | CLP |
| pe | Peru | olx.com.pe | PEN |
| do | Dominican Republic | olx.com.do | DOP |
| in | India | olx.in | INR |
| pk | Pakistan | olx.com.pk | PKR |
| id | Indonesia | olx.co.id | IDR |
| tr | Türkiye | olx.com.tr | TRY |
| za | South Africa | olx.co.za | ZAR |
| ma | Morocco | olx.ma | MAD |
| dz | Algeria | olx.dz | DZD |
| tn | Tunisia | olx.com.tn | TND |
| lb | Lebanon | olx.com.lb | LBP |
| jo | Jordan | olx.com.jo | JOD |
| qa | Qatar | olx.com.qa | QAR |
| pt | Portugal | olx.pt | EUR |

## Output fields

| Field | Type | Description |
|---|---|---|
| `listingId` | string | OLX listing ID. |
| `title` | string | Listing title. |
| `price` | integer | Numeric price in the country's local currency. |
| `priceText` | string | Original price string as shown on OLX (preserves "Free" / "Swap"). |
| `currency` | string | ISO-4217 currency code. |
| `description` | string | Full description (truncated at 30k chars on detail mode). |
| `category` | string | Top-level category from breadcrumb. |
| `subcategory` | string | Second-level category. |
| `breadcrumbs` | string[] | Full breadcrumb chain. |
| `city` | string | Listing's city / region. |
| `locationDate` | string | Combined location + posted-date string from card. |
| `postedAtText` | string | Posted-date string as shown ("Yesterday", "08 May 2026"). |
| `sellerName` | string | Seller display name. |
| `sellerUrl` | string | Seller profile URL. |
| `images` | string[] | All listing image URLs (detail mode). |
| `thumbnailUrl` | string | Primary image URL. |
| `listingUrl` | string | Canonical listing URL. |
| `country` | string | Two-letter country code. |
| `countryName` | string | Full country name. |
| `recordType` | string | Always `listing`. |
| `siteName` | string | `OLX`. |
| `scrapedAt` | string (ISO-8601) | |

## Modes & input

| Mode | What it does | Required input |
|---|---|---|
| `searchListings` | Free-text search on the chosen country site. | `country`, `query` |
| `byCategory` | Browse a top-level category. | `country`, `category` |
| `byCity` | Browse a city or region. | `country`, `city` (optionally `query`/`category`) |
| `byListing` | Fetch one or more listing detail pages. | `listingUrls` |
| `bySeller` | List all of a seller's listings. | `sellerUrl` |
| `byUrl` | Mix any OLX URLs across countries. | `urls` |

### Filters

- `condition` — new / used / any.
- `priceMin`, `priceMax` — numeric, in the country's local currency.
- `fetchListingDetails` — for search/category/city modes, also fetch each listing's detail page (full description + all photos). Adds 1 HTTP request per listing.
- `maxItems` — hard cap (1–1000).
- `maxPages` — paginated listing pages (?page=N) to crawl per seed.
- `useProxy` / `proxyConfiguration` / `autoEscalateOnBlock` — proxy controls. Most countries work direct; Brazil and India auto-escalate to Apify proxy on a 403.

## Daily test prefill

`country=pl`, `mode=searchListings`, `query="laptop"`, `maxItems=10` — Poland is OLX's biggest market and always returns ≥10 listings.

## Reliability

- HTTP-only via `curl_cffi` (Chrome 131 fingerprint). No browser, no Playwright.
- Retries on 429/5xx with exponential backoff.
- Auto-escalates to Apify proxy on the first 403/429/Cloudflare challenge.
- Recursive omit-empty before every record push (no `null` / `""` / `[]` fields).

## FAQ

**Q: Some country sites return 403 from datacenter IPs — what do I do?**  
Enable `useProxy=true` (or rely on `autoEscalateOnBlock`, which is on by default). Brazil (olx.com.br) and India (olx.in) commonly need a residential proxy.

**Q: Does this work for OLX Russia?**  
No — OLX shut down `olx.ru` years ago.

**Q: Can I run multiple countries in one run?**  
Use `mode=byUrl` with URLs from different countries — the actor auto-detects the country per URL. Otherwise pick one country per run.

**Q: Are price values comparable across countries?**  
No — `price` is in the country's local currency (`currency` field). Convert externally if you need cross-country comparison.

**Q: Why don't I see seller phone numbers?**  
OLX hides phone numbers behind a click + captcha. Out of scope for this actor; consider it a separate concern.

**Q: `bySeller` returns 0 records — bug?**  
On most country sites, OLX renders the seller's listings client-side via JavaScript. The actor is HTTP-only, so it cannot execute that JS. Use `searchListings` with `query` + `fetchListingDetails=true`, then group records in your downstream pipeline by `sellerUrl`.

**Q: How is `category` filled?**  
On detail-mode records, from the page's breadcrumb. On card-mode records, the breadcrumb isn't rendered; enable `fetchListingDetails=true` if you need it on every listing.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/olx-global-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
