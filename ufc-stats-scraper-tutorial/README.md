# UFC Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape UFC fighter rankings, fight results, and event data from ESPN's public MMA API. Search fighters, browse weight-class rankings, and fetch completed event fight cards with results.

This repository shows how to run [UFC Stats Scraper](https://apify.com/crawlerbros/ufc-stats-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ufc-stats-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ufc-stats-scraper](https://apify.com/crawlerbros/ufc-stats-scraper)
- **SEO title:** UFC Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape UFC fighter rankings, fight results, and event data from ESPN's public MMA API. Search fighters, browse weight-class rankings, and fetch completed event fight cards with results.

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

# UFC Stats Scraper

Scrape UFC fighter rankings, fight results, and event data using ESPN's free public MMA API. No authentication, no proxy required.

## What Does This Actor Do?

This actor collects UFC data including fighter rankings by weight class, completed event results with fight-by-fight breakdowns, and fighter search by name.

**Data Source:** ESPN's public MMA/UFC API (`site.api.espn.com/apis/site/v2/sports/mma/ufc/`)

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | select | `topRanked`, `byEvent`, or `searchFighters` |
| `weightClass` | select | Weight class for `topRanked` mode (e.g. Lightweight, Heavyweight) |
| `searchQuery` | string | Fighter name for `searchFighters` mode |
| `season` | integer | Year for `byEvent` mode (e.g. 2025) |
| `maxItems` | integer | Max records to return (default: 50) |

### Modes

- **topRanked** — Get ranked fighters for a specific weight class (champion + top 15). Returns fighter bios including record, height, weight, reach, stance, and country.
- **byEvent** — Get all completed UFC events for a given year with full fight cards, results, and methods.
- **searchFighters** — Search for a UFC fighter by name.

## Output

### Fighter Record (topRanked / searchFighters)

```json
{
  "recordType": "fighter",
  "sourceUrl": "https://site.api.espn.com/...",
  "scrapedAt": "2025-01-01T00:00:00+00:00",
  "athleteId": "3088812",
  "name": "Kamaru Usman",
  "nickname": "Nigerian Nightmare",
  "weightClass": "Welterweight",
  "rank": 1,
  "record": "21-4-0",
  "wins": 21,
  "losses": 4,
  "draws": 0,
  "isChampion": true,
  "titleDefenses": 2,
  "height": "6'1\"",
  "weight": "171 lbs",
  "reach": "76.0\"",
  "stance": "Southpaw",
  "country": "NGR",
  "age": 37,
  "headshotUrl": "https://a.espncdn.com/...",
  "espnProfileUrl": "https://www.espn.com/mma/fighter/_/id/3088812/kamaru-usman",
  "active": true
}
```

### Event Record (byEvent)

```json
{
  "recordType": "event",
  "sourceUrl": "https://www.espn.com/mma/event/_/id/600057024",
  "scrapedAt": "2025-01-01T00:00:00+00:00",
  "eventId": "600057024",
  "eventName": "UFC 324: Gaethje vs. Pimblett",
  "date": "2026-01-24T22:30Z",
  "venue": "T-Mobile Arena",
  "location": "Las Vegas, NV, USA",
  "fightCount": 12,
  "fights": [
    {
      "weightClass": "Lightweight",
      "fighter1": "Justin Gaethje",
      "fighter1Record": "25-5-0",
      "fighter2": "Paddy Pimblett",
      "fighter2Record": "22-3-0",
      "winner": "Paddy Pimblett",
      "round": 3,
      "time": "4:59"
    }
  ]
}
```

## Supported Weight Classes

Heavyweight, Light Heavyweight, Middleweight, Welterweight, Lightweight, Featherweight, Bantamweight, Flyweight, Women's Bantamweight, Women's Strawweight, Women's Flyweight, Men's Pound for Pound, Women's Pound for Pound.

## FAQs

**Q: Does this require any API keys or authentication?**
A: No. ESPN's public MMA API is completely free with no authentication.

**Q: How many fighters are in each ranking?**
A: Typically 16 (champion + top 15), matching the official UFC rankings.

**Q: Can I get historical event results?**
A: Yes — use `byEvent` mode and set `season` to the desired year (e.g. 2023, 2024).

**Q: Does this include stats like strikes, takedowns, etc.?**
A: Basic win/loss records, rounds, and fight outcome are included. Granular per-fight strike statistics are not available via this endpoint.

**Q: How often is the data updated?**
A: ESPN's API updates in near real-time after each event.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ufc-stats-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
