# ATP Live Rankings Scraper Tutorial: Run This Apify Actor with Python

Scrape ATP men's professional tennis live rankings from live-tennis.eu. Get singles, doubles, race to ATP Finals, Next Gen race, and prize money standings with player names, countries, ages, and points.

This repository shows how to run [ATP Live Rankings Scraper](https://apify.com/crawlerbros/atp-live-tennis-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/atp-live-tennis-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/atp-live-tennis-scraper](https://apify.com/crawlerbros/atp-live-tennis-scraper)
- **SEO title:** ATP Live Rankings Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape ATP men's professional tennis live rankings from live-tennis.eu. Get singles, doubles, race to ATP Finals, Next Gen race, and prize money standings with player names, countries, ages, and points.

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

# ATP Live Rankings Scraper

Extract ATP men's professional tennis live rankings from [live-tennis.eu](https://live-tennis.eu) — a comprehensive tennis statistics site with real-time ATP standings. Get singles, doubles, Race to ATP Finals, Next Gen race, and year-to-date prize money rankings with player names, countries, ages, and points. No login or API key required.

## Data Source

This actor scrapes data from **live-tennis.eu**, which provides real-time ATP live rankings updated as match results come in — often more current than the official ATP weekly release.

## Features

- **5 Ranking Types** — Singles, doubles, Race to ATP Finals, Next Gen race, and YTD prize money
- **Complete Player Data** — Rank, player name, country, age, and points for every player
- **Country Filtering** — Filter results to show only players from a specific country
- **No Login Required** — All data is publicly available

## Use Cases

- Tennis analytics and betting research
- Sports media and editorial applications
- Fantasy tennis tools and player comparison dashboards
- Academic sports science research
- Tracking ATP player ranking changes in real time

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `rankType` | Select | No | `singles` | Ranking type: `singles`, `doubles`, `race`, `race-next-gen`, `prize-money` |
| `countryCode` | String | No | — | 3-letter country code filter (e.g., `ITA`, `ESP`, `USA`) |
| `maxItems` | Integer | No | `100` | Maximum records to return (1–2000) |

### Example Input — Top 50 Singles Rankings

```json
{
  "rankType": "singles",
  "maxItems": 50
}
```

### Example Input — Spanish Players Only

```json
{
  "rankType": "singles",
  "countryCode": "ESP",
  "maxItems": 100
}
```

### Example Input — Race to ATP Finals

```json
{
  "rankType": "race",
  "maxItems": 20
}
```

## Output

| Field | Type | Description |
|-------|------|-------------|
| `rank` | Integer | Current ATP ranking position |
| `playerName` | String | Full player name |
| `country` | String | 3-letter country code (e.g., `ITA`) |
| `age` | Integer | Player age |
| `points` | Integer | ATP ranking points (or prize money in USD for `prize-money` type) |
| `rankType` | String | Ranking table type scraped |
| `profileUrl` | String | Player profile URL on live-tennis.eu |
| `recordType` | String | Always `ranking` |
| `scrapedAt` | String | ISO 8601 timestamp |
| `sourceUrl` | String | Source page URL |

### Example Output

```json
{
  "rank": 1,
  "playerName": "Jannik Sinner",
  "country": "ITA",
  "age": 24,
  "points": 13500,
  "rankType": "singles",
  "recordType": "ranking",
  "scrapedAt": "2025-01-15T10:23:45+00:00",
  "sourceUrl": "https://live-tennis.eu/en/atp-live-ranking"
}
```

## FAQ

**Does this require an API key or login?**
No. All data is scraped from publicly available live-tennis.eu pages.

**What are "live" rankings vs official ATP rankings?**
Live rankings are updated in real time as match results come in during tournaments, while official ATP rankings are released weekly on Mondays. Live rankings may differ during active tournaments.

**Can I filter by country?**
Yes — set `countryCode` to a 3-letter country code (e.g., `ITA` for Italy, `ESP` for Spain, `USA` for United States).

**What is the Race to ATP Finals?**
Set `rankType` to `race` to get year-to-date performance standings used to qualify for the ATP Finals (formerly held in Turin/Nitto ATP Finals).

**What does the `prize-money` ranking type return?**
Year-to-date earnings for all ATP players, with `points` representing total USD prize money earned.

**How many players are in the full ATP rankings?**
The full ATP singles rankings contain over 1,000 active players. Set `maxItems` to 2000 to retrieve all of them.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/atp-live-tennis-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
