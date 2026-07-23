# Zillow Agent & Premier Agent Directory Scraper Tutorial: Run This Apify Actor with Python

Scrape Zillow's agent directory by city. Returns full profiles: name, brokerage, phone, ratings, reviews, sales stats, specialties, languages, service areas, active listings, and past sales.

This repository shows how to run [Zillow Agent & Premier Agent Directory Scraper](https://apify.com/crawlerbros/zillow-agent-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/zillow-agent-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/zillow-agent-scraper](https://apify.com/crawlerbros/zillow-agent-scraper)
- **SEO title:** Zillow Agent & Premier Agent Directory Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Zillow's agent directory by city. Returns full profiles: name, brokerage, phone, ratings, reviews, sales stats, specialties, languages, service areas, active listings, and past sales.

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

# Zillow Agent & Premier Agent Directory Scraper

Scrape Zillow's real estate agent directory by city. Returns full agent profiles including contact info, ratings, reviews, recent sales statistics, specialties, languages, service areas, active listings, and past sales.

## What This Actor Does

- Search agents by **city + state** with optional filters (specialty, language, agent type)
- Collect **full profiles**: name, brokerage, phone, email, photo, review rating, review text
- Capture **sales performance**: sales last year, all-time count, 3-year price range
- Extract **active listings** and **past sales** from each agent's profile
- Supports **direct profile or directory URLs** via startUrls
- Handles PerimeterX bot protection with automatic Playwright fallback

## Input

| Field | Description | Default |
|-------|-------------|---------|
| `location` | City and state (e.g. "Dallas, TX") | Required (or startUrls) |
| `specialty` | Agent specialty filter | Any |
| `language` | Language spoken filter | Any |
| `agentType` | Agent type filter | Any |
| `maxAgents` | Max agents to return (1–500) | 50 |
| `endPage` | Max directory pages (1–25, ~15/page) | 5 |
| `startUrls` | Direct profile or directory URLs | — |

## Output

One record per agent. Fields only present when data is available.

| Field | Example |
|-------|---------|
| `name` | `"Lori Brown"` |
| `businessName` | `"RE/MAX EDGE"` |
| `phone` | `"(214) 555-0102"` |
| `reviewRating` | `4.9` |
| `reviewCount` | `284` |
| `saleCountLastYear` | `47` |
| `salePriceRangeMin` | `180000` |
| `salePriceRangeMax` | `2400000` |
| `specialties` | `["Luxury", "First-time buyers"]` |
| `languages` | `["English", "Spanish"]` |
| `activeListings` | `[{"address": "...", "price": 450000, "beds": 3, "baths": 2}]` |
| `pastSales` | `[{"address": "...", "price": 350000, "date": "2024-01-15"}]` |

## Use Cases

- **Lead generation** — build prospecting lists for B2B outreach to top agents in a market
- **Recruiting** — identify high-performing agents for brokerage recruitment
- **Competitive research** — analyze agent performance distribution by city or specialty
- **Market analysis** — quantify agent density, language coverage, and specialty mix per region
- **CRM enrichment** — augment existing contact databases with verified Zillow profile data

## Examples

**Top luxury agents in Beverly Hills, CA:**
```json
{
  "location": "Beverly Hills, CA",
  "specialty": "luxury",
  "agentType": "top-agents",
  "maxAgents": 100
}
```

**Spanish-speaking buyer agents in Miami, FL:**
```json
{
  "location": "Miami, FL",
  "language": "es",
  "agentType": "buyer-agents",
  "maxAgents": 50
}
```

**Pull a specific agent profile by URL:**
```json
{
  "startUrls": ["https://www.zillow.com/profile/agent-jane-doe/"]
}
```

## FAQ

**How many agents per city?**
Up to 375 (25 pages × 15 agents). Use `maxAgents` and `endPage` to limit.

**Is a proxy required?**
Residential proxy is strongly recommended — Zillow blocks datacenter IPs. The actor automatically uses Apify's residential proxy pool.

**What if an agent's profile fails to load?**
The directory-level data (name, phone, ratings, sales stats) is still returned as a partial record.

**Is this US-only?**
Yes. Zillow's agent directory covers US markets only.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/zillow-agent-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
