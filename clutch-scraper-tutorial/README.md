# Clutch.co B2B Agency Scraper Tutorial: Run This Apify Actor with Python

Extract agency profiles, ratings, reviews, and verified client data from Clutch.co. Get ratings, pricing, services, location, and reviews for B2B service providers.

This repository shows how to run [Clutch.co B2B Agency Scraper](https://apify.com/crawlerbros/clutch-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/clutch-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/clutch-scraper](https://apify.com/crawlerbros/clutch-scraper)
- **SEO title:** Clutch.co B2B Agency Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract agency profiles, ratings, reviews, and verified client data from Clutch.co. Get ratings, pricing, services, location, and reviews for B2B service providers.

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

# Clutch.co B2B Agency Scraper

Extract complete agency profiles from **Clutch.co** — the leading B2B marketplace for business services. Get ratings, verified client reviews, service breakdowns, industry focus, pricing, location, and 20+ more fields per agency.

## Features

- **26 output fields** per profile — the most complete Clutch data available
- **Services breakdown** with percentage weights (e.g., 30% Web Dev, 25% Mobile)
- **Industry focus** with percentage weights
- **Client size breakdown** (Small Business / Midmarket / Enterprise)
- **Technology focus areas** (AI expertise, frameworks, mobile platforms, etc.)
- **Verification status**, min project size, hourly rate, employee count
- **Recent reviews** with project details and ratings
- **100% reliable** — uses Chrome TLS impersonation + Apify RESIDENTIAL proxy
- **No nulls** — every field is populated with a typed default

## Input

| Field | Type | Description |
|-------|------|-------------|
| `companyUrls` | Array | Clutch profile URLs (e.g., `https://clutch.co/profile/toptal`) |
| `maxItems` | Integer | Max profiles to scrape (default: 20) |

### Example Input

```json
{
    "companyUrls": [
        "https://clutch.co/profile/toptal",
        "https://clutch.co/profile/cleveroad"
    ],
    "maxItems": 5
}
```

## Output

Every profile includes the following **26 fields**:

### Core Identity
| Field | Type | Description |
|-------|------|-------------|
| `name` | String | Agency name |
| `url` | String | Clutch profile URL |
| `tagline` | String | Agency tagline / headline |
| `website` | String | Agency website URL |
| `logo` | String | Logo image URL |
| `description` | String | Full company description |

### Ratings & Pricing
| Field | Type | Description |
|-------|------|-------------|
| `rating` | Number | Overall rating (0–5) |
| `reviewCount` | Integer | Number of reviews |
| `verificationStatus` | String | Verification status (e.g., "Verified") |
| `minProjectSize` | String | Minimum project size (e.g., `$50,000+`) |
| `averageHourlyRate` | String | Hourly rate range (e.g., `$100 - $149 / hr`) |
| `priceRange` | String | Price range from JSON-LD |
| `employees` | String | Employee count (e.g., `1-10 Employees`) |
| `foundingDate` | String | Year founded |

### Location
| Field | Type | Description |
|-------|------|-------------|
| `country` | String | Country code (e.g., `US`) |
| `city` | String | City |
| `region` | String | State / region |
| `postalCode` | String | Postal code |
| `streetAddress` | String | Street address |
| `telephone` | String | Contact phone |

### Services & Focus (arrays)
| Field | Type | Description |
|-------|------|-------------|
| `services` | Array | Service lines with `{name, percent}` breakdown |
| `focus` | Array | Technology focus groups `{title, values: [{name, percent}]}` — AI expertise, mobile platforms, frameworks, etc. |
| `industries` | Array | Industries served with `{name, percent}` |
| `clientSizes` | Array | Client size breakdown: Small Business (<$10M), Midmarket ($10M–$1B), Enterprise (>$1B) |

### Reviews & Metadata
| Field | Type | Description |
|-------|------|-------------|
| `reviews` | Array | Up to 10 recent reviews `{name, datePublished, author, rating, reviewBody}` |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
  "name": "Toptal",
  "url": "https://clutch.co/profile/toptal",
  "tagline": "Hire the Top 3% of Freelance Talent®",
  "website": "https://www.toptal.com",
  "logo": "https://img.shgstatic.com/...",
  "description": "Toptal is the world's largest fully remote workforce...",
  "rating": 4.8,
  "reviewCount": 53,
  "verificationStatus": "Verified",
  "minProjectSize": "$50,000+",
  "averageHourlyRate": "$100 - $149 / hr",
  "employees": "1-10 Employees",
  "priceRange": "$100 - $149",
  "telephone": "(888) 604-3188",
  "foundingDate": "2010",
  "country": "US",
  "city": "San Francisco, United States",
  "region": "CA",
  "postalCode": "94104",
  "streetAddress": "548 Market St #36879",
  "services": [
    {"name": "Custom Software Development", "percent": 0.16},
    {"name": "AI Development", "percent": 0.15},
    {"name": "Mobile App Development", "percent": 0.15}
  ],
  "focus": [
    {"title": "AI Expertise", "values": [{"name": "Machine Learning", "percent": 0.2}]}
  ],
  "industries": [
    {"name": "Financial services", "percent": 0.1}
  ],
  "clientSizes": [
    {"name": "Small Business (<$10M)", "percent": 0.5},
    {"name": "Midmarket ($10M - $1B)", "percent": 0.3},
    {"name": "Enterprise (>$1B)", "percent": 0.2}
  ],
  "reviews": [
    {"name": "...", "datePublished": "...", "author": "...", "rating": 5, "reviewBody": "..."}
  ],
  "scrapedAt": "2026-04-10T08:00:00+00:00"
}
```

## How It Works

Clutch.co is protected by Cloudflare, so this scraper uses **curl_cffi with Chrome TLS impersonation** over **Apify RESIDENTIAL proxy** to reliably fetch profile HTML. It then extracts:

1. **Core data** from JSON-LD `LocalBusiness` structured data
2. **Services, focus, industries, clientSizes** from embedded `window.chartPie` and `window.serviceLines` JavaScript globals
3. **Tagline, verification, employees, hourly rate, min project size** from DOM selectors and regex patterns

## FAQ

**Q: Why is RESIDENTIAL proxy required?**
Clutch blocks datacenter IPs with Cloudflare challenges. Apify RESIDENTIAL proxy bypasses this reliably. The proxy is hardcoded in the actor — no configuration needed.

**Q: How many reviews can I get?**
Up to 10 recent reviews per profile, parsed from JSON-LD structured data. The full review count is in the `reviewCount` field.

**Q: What if a profile URL is invalid?**
Invalid URLs (redirects to listing or homepage) are detected and skipped with a warning — no junk records are saved.

**Q: Can I scrape category listings?**
Not in this version — this scraper focuses on individual profile pages. Provide a list of profile URLs directly.

## Use Cases

- **B2B lead generation** — discover high-rated agencies by service line
- **Competitive intelligence** — compare pricing, size, and specialization
- **Market research** — analyze service / industry / client size trends
- **Partnership discovery** — find verified agencies in specific industries
- **Procurement & vendor research** — gather structured data for RFQs

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/clutch-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
