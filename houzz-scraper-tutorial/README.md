# Houzz Scraper Tutorial: Run This Apify Actor with Python

Scrape public Houzz professional directory and profile pages. Extract business details, ratings, reviews, hires, services, location data, and profile URLs from Houzz contractors and design professionals.

This repository shows how to run [Houzz Scraper](https://apify.com/crawlerbros/houzz-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/houzz-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/houzz-scraper](https://apify.com/crawlerbros/houzz-scraper)
- **SEO title:** Houzz Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public Houzz professional directory and profile pages. Extract business details, ratings, reviews, hires, services, location data, and profile URLs from Houzz contractors and design professionals.

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

# Houzz Scraper

Scrape public Houzz professional directory and profile pages with an HTTP-first actor. Extract contractor and design professional details such as ratings, review counts, hires on Houzz, business contact fields, service lists, and location metadata.

## Modes

This actor supports four input modes — pick whichever is most convenient:

1. **Profile URLs** — paste direct Houzz pro profile URLs into `profileUrls`.
2. **Directory URLs** — paste a directory or category page URL (such as a category filtered by a city) into `directoryUrls`.
3. **By city + category** — set the `city` (e.g. `Los-Angeles--CA`, `London`, `Sydney`) and the `category` dropdown (e.g. `general-contractors`). The actor builds the directory URL automatically for the selected `country`.
4. **Hybrid** — combine any of the above; profile URLs always extract first, then directory URLs are crawled until `maxItems` is reached.

## Markets supported

Houzz operates in 16 markets and the actor supports all of them via the `country` dropdown:

US, UK, Canada, Australia, Germany, France, Ireland, Italy, Spain, New Zealand, India, Singapore, Japan, Russia, Denmark, Sweden.

When `country` + `city` + `category` are set, the actor constructs the matching country-domain directory URL (`www.houzz.com`, `www.houzz.co.uk`, `www.houzz.de`, etc.).

## Categories supported

The `category` dropdown exposes 25+ professional categories — general contractors, architects, interior designers, kitchen/bath designers, painters, landscapers, home builders, and many more.

## Anti-bot

By default, the actor runs without proxy from datacenter IPs (Houzz is normally reachable). If a fetch is blocked:

- `useProxy` (default `false`) — when enabled, all requests go through the configured `proxyConfiguration`.
- `autoEscalateOnBlock` (default `true`) — when a profile or directory fetch returns nothing, the actor automatically retries that single URL through Apify residential proxy. The directory-card data is still emitted as a fallback if the profile page itself is blocked.

## Input fields

| Field | Type | Description |
|---|---|---|
| `directoryUrls` | array | Houzz directory or category page URLs. |
| `profileUrls` | array | Direct Houzz professional profile URLs. |
| `city` | string | City + state slug, e.g. `Los-Angeles--CA`, `London`. |
| `category` | enum | Houzz professional category slug. |
| `country` | enum | Houzz market/domain (us, uk, ca, au, de, fr, ie, it, es, nz, in, sg, jp, ru, dk, se). |
| `maxItems` | integer (1-250) | Hard cap on emitted records. |
| `useProxy` | boolean | Route requests through Apify proxy. |
| `autoEscalateOnBlock` | boolean | Auto-retry blocked fetches via residential proxy. |
| `proxyConfiguration` | object | Apify proxy configuration (advanced). |

## Output

Each record can include:

- `title` / `businessName` / `description`
- `phoneNumber` / `websiteUrl` / `licenseNumber`
- `ratingValue` / `reviewCount` / `hiresOnHouzz` / `followersCount` / `projectCount`
- `verifiedLicense` / `awards`
- `typicalJobCost` / `servicesProvided` / `areaServed`
- `streetAddress` / `city` / `state` / `postalCode` / `countryCode` / `country` / `fullAddress`
- `latitude` / `longitude`
- `imageUrl` / `directorySnippet`
- `sourceUrl` / `profileUrl` / `canonicalUrl` / `slug`
- `siteName` / `recordType` / `recordSource` / `scrapedAt`

`recordSource` is `"full_profile"` when the profile page was successfully fetched (full set of fields including `description`, `licenseNumber`, `websiteUrl`, `servicesProvided`, etc.), or `"directory_card"` when only the directory-card subset was available (anti-bot fallback). Directory-card records typically lack `description`, `licenseNumber`, `websiteUrl`, `typicalJobCost`, `servicesProvided`, and `followersCount`.

Empty values are omitted from output (no `null`, blank strings, or empty arrays).

### Field notes

- `phoneNumber` is returned as a human-readable formatted string exactly as Houzz publishes it (e.g. `"(424) 280-3130"`), not a digits-only normalized form. If you need a digits-only value, strip non-digits in your downstream pipeline (e.g. `re.sub(r"\D", "", phoneNumber)`).
- `ratingValue` is a numeric (JSON number) on a `1.0`–`5.0` scale (e.g. `4.9` or `5`). Whole numbers may serialize without a decimal in JSON; cast to float in your downstream pipeline if you need a uniform numeric type.

## Limitations

- Houzz page structure varies by professional category and locale, so some fields appear only when publicly shown on the target page.
- When a profile page is blocked even after escalation, the actor falls back to the directory-card data (a smaller but still useful subset).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/houzz-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
