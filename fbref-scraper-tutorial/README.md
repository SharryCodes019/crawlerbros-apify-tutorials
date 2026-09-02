# FBref Football Statistics Scraper Tutorial: Run This Apify Actor with Python

Scrape FBref (fbref.com) - the Football Reference site. Get league stats, match results, and player statistics for Premier League, La Liga, Bundesliga, Serie A, and Ligue 1.

This repository shows how to run [FBref Football Statistics Scraper](https://apify.com/crawlerbros/fbref-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/fbref-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/fbref-scraper](https://apify.com/crawlerbros/fbref-scraper)
- **SEO title:** FBref Football Statistics Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape FBref (fbref.com) - the Football Reference site. Get league stats, match results, and player statistics for Premier League, La Liga, Bundesliga, Serie A, and Ligue 1.

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

# FBref Football Statistics Scraper

Scrape player statistics, match results, and league tables from **FBref** (fbref.com) — the most comprehensive football statistics database, covering all major European leagues.

## What This Actor Does

Fetches football data from FBref including:
- **League Stats**: All player stats for a full season (goals, assists, xG, minutes played, pass completion, cards)
- **Match Results**: Fixture results with scores, xG, venues, attendance, and referees
- **Player Stats**: Career statistics by season for any FBref player

## Supported Leagues

| League | Country |
|--------|---------|
| Premier League | England |
| La Liga | Spain |
| Bundesliga | Germany |
| Serie A | Italy |
| Ligue 1 | France |

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | string | `leagueStats`, `matchResults`, or `playerStats` |
| `league` | string | League slug (e.g. `premier-league`, `bundesliga`) |
| `season` | string | Season in FBref format, e.g. `2024-2025` |
| `playerName` | string | Player name for `playerStats` mode (e.g. `Erling Haaland`) |
| `maxItems` | integer | Max records to return (default: 10) |

### Example Input

```json
{
  "mode": "leagueStats",
  "league": "premier-league",
  "season": "2024-2025",
  "maxItems": 10
}
```

## Output

Each record contains:

| Field | Description |
|-------|-------------|
| `playerId` | FBref player ID |
| `playerName` | Player's full name |
| `team` | Current club |
| `position` | Playing position |
| `league` | League name |
| `season` | Season string |
| `appearances` | Matches played |
| `goals` | Goals scored |
| `assists` | Assists |
| `yellowCards` | Yellow cards |
| `redCards` | Red cards |
| `minutesPlayed` | Total minutes on pitch |
| `passCompletion` | Pass completion percentage |
| `xg` | Expected goals |
| `xga` | Expected goal assists |
| `playerUrl` | Link to player's FBref page |

### Example Output

```json
{
  "playerName": "Erling Haaland",
  "team": "Manchester City",
  "position": "FW",
  "league": "Premier League",
  "season": "2024-2025",
  "appearances": 28,
  "goals": 22,
  "assists": 5,
  "xg": 19.8,
  "minutesPlayed": 2340,
  "playerUrl": "https://fbref.com/en/players/..."
}
```

## FAQs

**Is this free to use?**
Yes. FBref is a publicly accessible website and this actor uses standard HTTP requests without any paid proxies or API keys.

**How fresh is the data?**
Data is scraped live from FBref on each run. FBref typically updates stats within 24-48 hours of matches.

**Why might some stats be missing?**
FBref only shows xG/xGA for the Big 5 leagues. Some older seasons may have fewer advanced stats.

**Can I get historical seasons?**
Yes — set the `season` field to any past season like `2020-2021`.

**What is the daily test prefill?**
The actor's default test runs `leagueStats` for Premier League 2024-2025 with maxItems=10, which should always return data during an active season.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/fbref-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
