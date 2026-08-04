# Arbeitsagentur (German Job Board) Scraper Tutorial: Run This Apify Actor with Python

Extract German job listings from arbeitsagentur.de with title, employer, location, contract type, posted date.

This repository shows how to run [Arbeitsagentur (German Job Board) Scraper](https://apify.com/crawlerbros/arbeitsagentur-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/arbeitsagentur-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/arbeitsagentur-scraper](https://apify.com/crawlerbros/arbeitsagentur-scraper)
- **SEO title:** Arbeitsagentur (German Job Board) Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract German job listings from arbeitsagentur.de with title, employer, location, contract type, posted date.

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

# Arbeitsagentur Job Scraper

Extract German job listings from **arbeitsagentur.de** (Bundesagentur für Arbeit) — Germany's official federal employment agency. Returns titles, employers, locations, contract types, geocoordinates, and external apply URLs from 1.5M+ live listings.

## Features

- **18 output fields** per job — complete flat schema with typed defaults (zero nulls)
- **1.5M+ German jobs indexed** — covers all federal states + Austria
- **Public JSON API** — uses the official Bundesagentur für Arbeit `jobboerse-jobsuche` API
- **Filter by keyword, location, radius, contract type, working time, freshness**
- **No proxy, no cookies, no login** — works directly from datacenter IPs
- **Pagination** — walks pages until `maxItems` reached (up to 100 results per request)
- **Geocoordinates** — every job has lat/lng for mapping

## Input

| Field | Type | Description |
|---|---|---|
| `search` | String | Keyword (e.g., `"Softwareentwickler"`, `"Krankenpfleger"`, `"Lehrer"`) |
| `location` | String | City, postal code, or region (e.g., `"Berlin"`, `"10115"`, `"Bayern"`). Empty = all of Germany. |
| `radius` | Integer | Search radius in km around the location (default 25, max 200) |
| `contractType` | String | `all`, `permanent`, `fixed-term`, `any` |
| `workingTime` | String | `all`, `full-time`, `part-time`, `shift`, `homework` |
| `publishedSince` | Integer | Only jobs posted within last N days (1, 3, 7, 14, 28; 0 = all) |
| `maxItems` | Integer | Maximum jobs to return (default 50, max 1000) |

### Example Input

```json
{
    "search": "Softwareentwickler",
    "location": "Berlin",
    "radius": 25,
    "contractType": "permanent",
    "workingTime": "full-time",
    "publishedSince": 7,
    "maxItems": 100
}
```

## Output

Each job has **18 fields**. All fields are always present — empty strings or zero for missing data, never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | String | Reference number (Refnr) |
| `title` | String | Job title |
| `occupation` | String | Occupation classification (Beruf) |
| `employer` | String | Company / organisation name |

### Location
| Field | Type | Description |
|---|---|---|
| `city` | String | Job city (Ort) |
| `postalCode` | String | Postal code (PLZ) |
| `street` | String | Street address |
| `region` | String | Federal state (Bundesland) |
| `country` | String | Country (Deutschland / Österreich) |
| `latitude` | Number | Latitude |
| `longitude` | Number | Longitude |
| `distanceKm` | Integer | Distance from search location in km |

### Dates
| Field | Type | Description |
|---|---|---|
| `publishedDate` | String | Date posted (YYYY-MM-DD) |
| `modifiedTimestamp` | String | Last modified ISO 8601 |
| `startDate` | String | Job start date (YYYY-MM-DD) |

### URLs
| Field | Type | Description |
|---|---|---|
| `externalUrl` | String | External apply URL (employer's website) |
| `portalUrl` | String | Arbeitsagentur portal URL |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

## FAQ

**Q: Do I need a proxy?**
No. Arbeitsagentur exposes a public JSON API at `rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs` that requires only a public `X-API-Key` header (`jobboerse-jobsuche`). This key is shared by all official Arbeitsagentur frontends. The scraper works from any datacenter IP.

**Q: What's the maximum results per query?**
The API returns up to 100 results per page. The scraper paginates automatically until `maxItems` is reached or results run out.

**Q: Are Austrian jobs included?**
Yes. Arbeitsagentur cooperates with the Austrian AMS, so listings include both German and Austrian jobs. The `country` field shows `Deutschland` or `Österreich`.

**Q: Why is `street` sometimes empty?**
Many employers don't disclose the street address. The API returns the literal string `"null"` in that case — the scraper converts it to an empty string.

**Q: How fresh is the data?**
The API serves the live Arbeitsagentur index. New jobs typically appear within 1-2 hours of being published.

## Use Cases

- **Recruitment market research** — track open positions by industry / region
- **Salary benchmarking** — aggregate by occupation and region
- **Job alerts** — daily runs with narrow filters for specific roles
- **Candidate sourcing** — discover companies actively hiring in your area
- **Career coaching** — help job seekers find relevant openings
- **Labor-market dashboards** — feed structured German job data into BI tools

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/arbeitsagentur-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
