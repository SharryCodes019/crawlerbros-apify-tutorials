# Eventbrite Events Scraper Tutorial: Run This Apify Actor with Python

Extract events from Eventbrite like title, date, venue, organizer, ticket price, image, tags. Filter by location, category, or keyword. No proxy required.

This repository shows how to run [Eventbrite Events Scraper](https://apify.com/crawlerbros/eventbrite-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/eventbrite-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/eventbrite-scraper](https://apify.com/crawlerbros/eventbrite-scraper)
- **SEO title:** Eventbrite Events Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract events from Eventbrite like title, date, venue, organizer, ticket price, image, tags. Filter by location, category, or keyword. No proxy required.

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

# Eventbrite Events Scraper

Extract events from **Eventbrite** — name, dates, venue, organizer, geocoordinates, image, category, tags, and ticket URL. Browse by location, category, or paste any Eventbrite browse URL. No proxy required.

## Features

- **28 output fields** per event — flat schema with typed defaults (zero nulls)
- **Filter by location** (city / state / country / online)
- **Filter by category** (music, business, food-and-drink, sports, etc.)
- **Pagination** — walks `?page=N` until `maxItems` reached (~20 events per page)
- **Geocoordinates** for every event with a venue
- **No proxy, no cookies, no login** — works directly from datacenter IPs

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | Array | Eventbrite browse URLs (e.g., `https://www.eventbrite.com/d/ny--new-york/all-events/`). Filters in the URL pass through. |
| `location` | String | City/region slug used when no startUrls (e.g., `ny--new-york`, `ca--san-francisco`, `united-states`, `online`) |
| `category` | String | Category slug (e.g., `music`, `business`, `food-and-drink`, `sports`) |
| `maxItems` | Integer | Maximum events to return (default 50, max 500) |

### Example Input

```json
{
    "location": "ny--new-york",
    "category": "music",
    "maxItems": 100
}
```

Or with a direct URL:

```json
{
    "startUrls": ["https://www.eventbrite.com/d/online/business/"],
    "maxItems": 50
}
```

## Output

Each event has **28 fields**. All fields are always present — empty strings, zero, `false`, or empty array as typed defaults, never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | String | Eventbrite event ID |
| `name` | String | Event name |
| `summary` | String | Short summary (truncated to 1,000 chars) |
| `url` | String | Event page URL |
| `ticketsUrl` | String | Direct checkout URL |

### Dates
| Field | Type | Description |
|---|---|---|
| `startDate` | String | Start date (`YYYY-MM-DD`) |
| `startTime` | String | Start time (`HH:MM`) |
| `endDate` | String | End date (`YYYY-MM-DD`) |
| `endTime` | String | End time (`HH:MM`) |
| `timezone` | String | IANA timezone (e.g., `America/New_York`) |

### Venue
| Field | Type | Description |
|---|---|---|
| `isOnline` | Boolean | Whether it's a virtual event |
| `isCancelled` | Boolean | Whether the event is cancelled |
| `venueName` | String | Primary venue name |
| `venueAddress` | String | Full street address |
| `venueCity` | String | City |
| `venueRegion` | String | State / region code |
| `venueCountry` | String | Country code (`US`) |
| `venuePostalCode` | String | ZIP / postal code |
| `latitude` | Number | Latitude |
| `longitude` | Number | Longitude |

### Classification
| Field | Type | Description |
|---|---|---|
| `category` | String | Eventbrite category (e.g., `Music`, `Business`) |
| `format` | String | Event format (e.g., `Concert`, `Workshop`) |
| `tags` | Array | Organizer tags / keywords |
| `language` | String | Language code |

### Other
| Field | Type | Description |
|---|---|---|
| `imageUrl` | String | Event cover image URL |
| `primaryOrganizerId` | String | Organizer ID |
| `ticketsBy` | String | Ticket provider name |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

## FAQ

**Q: Do I need a proxy?**
No. Eventbrite browse pages are publicly accessible from datacenter IPs via Chrome 131 TLS impersonation. The scraper extracts the embedded `window.__SERVER_DATA__` JSON which contains all event data — no auth or cookies needed.

**Q: How do I filter by city?**
Use the `location` slug Eventbrite uses in its URLs. Examples:
- `ny--new-york`, `ca--san-francisco`, `tx--austin`
- `united-kingdom`, `germany`, `united-states`
- `online` (for virtual events)

You can also paste any Eventbrite browse URL into `startUrls` directly.

**Q: How do I filter by category?**
Use the category slug from Eventbrite URLs:
- `music`, `business`, `food-and-drink`, `community`, `arts`
- `sports-and-fitness`, `health`, `science-and-tech`, `family-and-education`

**Q: How fresh is the data?**
Eventbrite browse pages are served from their live database — events appear immediately after publication.

**Q: Are paid and free events both included?**
Yes. Both ticketed and free events appear in browse results.

## Use Cases

- **Event marketing research** — track competitor events in your category / region
- **Venue analytics** — map events by venue to understand utilization
- **Calendar aggregation** — feed event data into calendars or city guides
- **Lead generation** — identify event organizers in target markets
- **Travel planning** — find events happening in destination cities
- **Trend analysis** — spot rising tags / categories over time

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/eventbrite-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
