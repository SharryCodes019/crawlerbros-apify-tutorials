# PitchBook Investors Scraper Tutorial: Run This Apify Actor with Python

Scrape public investor profile metadata from PitchBook without a subscription. Supports text search, direct profile URLs, and bulk sitemap discovery. Returns name, description, location, investor type, status, metrics, social links, and more.

This repository shows how to run [PitchBook Investors Scraper](https://apify.com/crawlerbros/pitchbook-investors-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/pitchbook-investors-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/pitchbook-investors-scraper](https://apify.com/crawlerbros/pitchbook-investors-scraper)
- **SEO title:** PitchBook Investors Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public investor profile metadata from PitchBook without a subscription. Supports text search, direct profile URLs, and bulk sitemap discovery. Returns name, description, location, investor type, status, metrics, social links, and more.

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

# PitchBook Investors Scraper

Extract public investor profile data from PitchBook — no subscription required. Scrape venture capital firms, private equity funds, angel investors, and more from PitchBook's database of 200,000+ publicly accessible investor profiles.

## What It Does

This actor fetches investor profiles from PitchBook's public profile pages and extracts structured metadata including firm name, location, investor type, investment metrics, social links, and more. No login or PitchBook subscription needed.

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `profileUrls` | string[] | No | Direct PitchBook investor profile URLs or bare IDs |
| `searchQuery` | string | No | Text search (e.g. `"venture capital Berlin"`) |
| `maxItems` | integer | No | Max records to return (default: 10) |
| `proxyConfiguration` | object | Yes | Apify proxy (residential recommended — required to bypass Cloudflare) |

**Input mode selection:**
- If `profileUrls` are provided → scrape those specific profiles
- If only `searchQuery` is provided → paginate search results
- If neither is provided → bulk mode: stream from PitchBook's public sitemaps (229,000+ investors)

### Example Input

```json
{
  "searchQuery": "andreessen horowitz",
  "maxItems": 5
}
```

### Direct URL Example

```json
{
  "profileUrls": [
    "https://pitchbook.com/profiles/investor/11295-73",
    "11295-73"
  ]
}
```

## Output

One record per investor profile. Empty fields are omitted.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Investor/firm name |
| `profileUrl` | string | PitchBook profile URL |
| `description` | string | Firm description |
| `website` | string | Company website |
| `city` | string | HQ city |
| `state` | string | HQ state/region |
| `country` | string | HQ country |
| `streetAddress` | string | Street address |
| `postalCode` | string | Postal code |
| `yearFounded` | integer | Year the firm was founded |
| `investorStatus` | string | e.g. `Actively Seeking New Investments` |
| `primaryInvestorType` | string | e.g. `Venture Capital` |
| `otherInvestorTypes` | string[] | Additional investor type classifications |
| `tradeAssociation` | string | Industry trade association |
| `professionalCount` | integer | Number of investment professionals |
| `totalInvestments` | integer | Total number of investments made |
| `activePortfolio` | integer | Number of active portfolio companies |
| `totalExits` | integer | Number of exits |
| `logoUrl` | string | Firm logo image URL |
| `socialLinks` | object | `{ twitter, linkedin, facebook }` |
| `scrapedAt` | string | ISO 8601 UTC timestamp |

### Example Output

```json
{
  "name": "Sequoia Capital",
  "profileUrl": "https://pitchbook.com/profiles/investor/11295-73",
  "description": "Founded in 1972, Sequoia Capital is a venture capital investment firm based in Menlo Park, California.",
  "website": "https://sequoiacap.com",
  "city": "Menlo Park",
  "state": "California",
  "country": "United States",
  "streetAddress": "2800 Sand Hill Road",
  "postalCode": "94025",
  "yearFounded": 1972,
  "investorStatus": "Actively Seeking New Investments",
  "primaryInvestorType": "Venture Capital",
  "otherInvestorTypes": ["Growth/Expansion"],
  "tradeAssociation": "Indian Venture Capital Association (INVCA)",
  "professionalCount": 45,
  "totalInvestments": 2998,
  "activePortfolio": 896,
  "totalExits": 990,
  "logoUrl": "https://image.pitchbook.com/3m9ATgSWiMb...",
  "socialLinks": {
    "facebook": "https://www.facebook.com/SequoiaCap",
    "twitter": "https://twitter.com/sequoia",
    "linkedin": "https://www.linkedin.com/company/sequoia"
  },
  "scrapedAt": "2026-04-16T12:00:00+00:00"
}
```

### Error Record

When a profile cannot be scraped:

```json
{
  "inputUrl": "https://pitchbook.com/profiles/investor/00000-00",
  "error": "Profile not found",
  "scrapedAt": "2026-04-16T12:00:00+00:00"
}
```

## FAQ

**Does this require a PitchBook subscription?**
No. All data is extracted from PitchBook's publicly accessible investor profile pages.

**What data is NOT available?**
AUM (assets under management), contact details (email, phone, contact name), and preferred investment criteria are behind PitchBook's paywall and are not included.

**How many investors can I scrape?**
PitchBook's public sitemap contains ~229,000 investor profile URLs. Set `maxItems` up to 100,000 for large runs.

**What is bulk mode?**
When you provide no `profileUrls` and no `searchQuery`, the actor streams investor URLs directly from PitchBook's public gzipped sitemap files.

**Do I need a proxy?**
Yes. PitchBook uses Cloudflare protection that blocks repeated requests from the same IP. The actor defaults to Apify residential proxy, which rotates IPs automatically to bypass this. Without proxy, only 1–2 profiles can be scraped before requests are blocked.

**How long does it take?**
Each profile takes 1–3 seconds to fetch. A run of 100 profiles takes approximately 2–5 minutes.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/pitchbook-investors-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
