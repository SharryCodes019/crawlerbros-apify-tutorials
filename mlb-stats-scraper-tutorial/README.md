# MLB Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape the official MLB Stats API, comprehensive baseball data including teams, players, schedules, standings, and detailed statistics. Official MLB data source, no authentication required.

This repository shows how to run [MLB Stats Scraper](https://apify.com/crawlerbros/mlb-stats-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/mlb-stats-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/mlb-stats-scraper](https://apify.com/crawlerbros/mlb-stats-scraper)
- **SEO title:** MLB Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape the official MLB Stats API, comprehensive baseball data including teams, players, schedules, standings, and detailed statistics. Official MLB data source, no authentication required.

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

# MLB Stats Scraper

Access comprehensive baseball data from the **official MLB Stats API** — teams, players, schedules, standings, and detailed statistics. No authentication required. Official MLB data source updated in real-time during the season.

## Features

- **Teams** — list all 30 MLB teams with league, division, venue, and location info
- **Players** — get full rosters for any team, or all active players in the league
- **Schedule** — fetch game schedules by date, date range, or team
- **Standings** — current division standings with win/loss records, GB, and streak info
- **Player Stats** — hitting, pitching, or fielding statistics for any player by season
- **Game Details** — detailed linescore, run/hit/error totals, and inning-by-inning data for any game

## Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mode` | Select | `teams`, `players`, `schedule`, `standings`, `playerStats`, `gameDetails` |
| `season` | Integer | MLB season year (default: current year) |
| `teamId` | Integer | MLB team ID (e.g. 147 = Yankees, 111 = Red Sox) |
| `playerId` | Integer | MLB player ID (e.g. 660271 = Juan Soto) |
| `gamePk` | Integer | Game primary key (required for mode=gameDetails) |
| `date` | Text | Game date as YYYY-MM-DD (mode=schedule) |
| `fromDate` | Text | Start date for schedule range |
| `toDate` | Text | End date for schedule range |
| `leagueId` | Select | `AL`, `NL`, or `both` (mode=standings) |
| `statGroup` | Select | `hitting`, `pitching`, or `fielding` (mode=playerStats) |
| `gameType` | Select | `R` (Regular), `S` (Spring), `P` (Playoffs), `W` (World Series), etc. |
| `maxItems` | Integer | Maximum records to return (1–10,000, default 100) |

## Output Fields

### Teams mode
| Field | Description |
|-------|-------------|
| `teamId` | MLB team identifier |
| `name` | Full team name |
| `abbreviation` | 2–3 letter abbreviation (e.g. NYY) |
| `teamName` | Short team name (e.g. Yankees) |
| `locationName` | City/location name |
| `leagueName` | American League or National League |
| `divisionName` | Division name (e.g. AL East) |
| `venueName` | Home stadium name |
| `active` | Whether the team is active |
| `mlbUrl` | Official MLB team page URL |

### Players mode
| Field | Description |
|-------|-------------|
| `playerId` | MLB player identifier |
| `fullName` | Player's full name |
| `primaryNumber` | Jersey number |
| `birthDate` | Date of birth |
| `birthCity` | City of birth |
| `birthCountry` | Country of birth |
| `height` | Player height |
| `weight` | Player weight (lbs) |
| `primaryPosition` | Primary fielding position |
| `currentTeam` | Current team name |
| `batSide` | Batting side (Left/Right/Switch) |
| `pitchHand` | Throwing hand |
| `mlbUrl` | Official MLB player page URL |

### Schedule mode
| Field | Description |
|-------|-------------|
| `gamePk` | Game primary key |
| `gameDate` | Full game date/time (ISO 8601) |
| `homeTeam` | Home team name |
| `awayTeam` | Away team name |
| `homeScore` | Home team runs scored |
| `awayScore` | Away team runs scored |
| `status` | Game status (Final, In Progress, Postponed, etc.) |
| `venue` | Stadium name |

### Standings mode
| Field | Description |
|-------|-------------|
| `teamName` | Team name |
| `divisionName` | Division name |
| `wins` | Total wins |
| `losses` | Total losses |
| `pct` | Winning percentage |
| `divisionRank` | Rank within division |
| `gamesBack` | Games behind division leader |
| `streakCode` | Current streak (e.g. W5, L2) |

### Player Stats mode
| Field | Description |
|-------|-------------|
| `playerId` | MLB player identifier |
| `season` | Season year |
| `gamesPlayed` | Games played |
| `homeRuns` | Home runs |
| `rbi` | Runs batted in |
| `avg` | Batting average |
| `obp` | On-base percentage |
| `slg` | Slugging percentage |
| `ops` | On-base plus slugging |
| `era` | Earned run average (pitchers) |
| `whip` | Walks plus hits per inning pitched |
| `wins` | Pitcher wins |

## Example Use Cases

**Get all 30 MLB teams for 2024:**
```json
{
  "mode": "teams",
  "season": 2024,
  "maxItems": 30
}
```

**Get New York Yankees roster:**
```json
{
  "mode": "players",
  "teamId": 147,
  "season": 2024
}
```

**Get July 4th 2024 schedule:**
```json
{
  "mode": "schedule",
  "date": "2024-07-04",
  "gameType": "R"
}
```

**Get 2024 AL East standings:**
```json
{
  "mode": "standings",
  "season": 2024,
  "leagueId": "AL"
}
```

**Get Juan Soto 2024 hitting stats:**
```json
{
  "mode": "playerStats",
  "playerId": 660271,
  "season": 2024,
  "statGroup": "hitting"
}
```

## Common Team IDs

| Team | ID | Team | ID |
|------|----|------|----|
| New York Yankees | 147 | New York Mets | 121 |
| Boston Red Sox | 111 | Los Angeles Dodgers | 119 |
| Chicago Cubs | 112 | San Francisco Giants | 137 |
| Houston Astros | 117 | Atlanta Braves | 144 |
| Los Angeles Angels | 108 | Philadelphia Phillies | 143 |

## Data Source

All data is sourced from the [official MLB Stats API](https://statsapi.mlb.com/api/v1/) — the same data feed used by MLB.com, the Statcast system, and major sports analytics platforms. The API is completely free and requires no authentication.

## FAQs

**Q: How current is the data?**
A: Schedule, scores, and standings update in real-time during games. Player stats may have slight delays.

**Q: What seasons are available?**
A: Historical data goes back to 1876. Not all stats are available for very old seasons.

**Q: How do I find a player's ID?**
A: Use mode=players to list all players. Player IDs are also visible in MLB.com profile URLs (e.g. mlb.com/player/660271).

**Q: What game types are available?**
A: Regular Season (R), Spring Training (S), Playoffs (P), World Series (W), League Championship (L), and All-Star (A).

**Q: Is there a cost to use this scraper?**
A: No. The official MLB Stats API is free and public. This scraper uses only standard Apify datacenter proxies (included in the free tier).

**Q: Can I get historical standings?**
A: Yes — provide the `season` parameter (e.g. `season: 2020`) for any past season.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/mlb-stats-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
