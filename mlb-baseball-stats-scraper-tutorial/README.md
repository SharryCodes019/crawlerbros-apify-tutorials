# MLB Baseball Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape the official MLB Stats API - comprehensive baseball data including teams, player batting/pitching stats, schedules, and standings. Official MLB data source, no authentication required.

This repository shows how to run [MLB Baseball Stats Scraper](https://apify.com/crawlerbros/mlb-baseball-stats-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/mlb-baseball-stats-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/mlb-baseball-stats-scraper](https://apify.com/crawlerbros/mlb-baseball-stats-scraper)
- **SEO title:** MLB Baseball Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape the official MLB Stats API - comprehensive baseball data including teams, player batting/pitching stats, schedules, and standings. Official MLB data source, no authentication required.

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

# MLB Baseball Stats Scraper

Access comprehensive baseball data from the **official MLB Stats API** — player batting and pitching statistics, team standings, game schedules, and team info. No authentication required. Official MLB data updated in real-time during the season.

## What You Can Scrape

| Mode | Data |
|------|------|
| `getPlayerStats` | Season batting or pitching statistics for all players |
| `getStandings` | Division standings for AL and NL |
| `getSchedule` | Game schedule and results for a date range |
| `getTeams` | List all 30 MLB teams with league and division info |

## Input Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mode` | select | `getPlayerStats` | What data to retrieve |
| `statGroup` | select | `hitting` | Type of stats: `hitting`, `pitching`, or `fielding` |
| `season` | integer | `2024` | MLB season year (2019–2024) |
| `teamId` | integer | — | Filter by MLB team ID (e.g. 147 = Yankees). Optional. |
| `startDate` | text | — | Start date YYYY-MM-DD for `getSchedule` mode |
| `endDate` | text | — | End date YYYY-MM-DD for `getSchedule` mode |
| `maxItems` | integer | `50` | Maximum records to return (1–500) |

## Output Fields

### Player Stats (getPlayerStats)

| Field | Description |
|-------|-------------|
| `playerId` | MLB player identifier |
| `playerName` | Player full name |
| `teamId` | Team identifier |
| `teamName` | Team name |
| `position` | Primary field position |
| `season` | Season year |
| `gamesPlayed` | Games played |
| `atBats` | At bats |
| `hits` | Hits |
| `doubles` | Doubles |
| `triples` | Triples |
| `homeRuns` | Home runs |
| `rbi` | Runs batted in |
| `battingAverage` | Batting average (e.g. ".304") |
| `onBasePercentage` | On-base percentage |
| `sluggingPct` | Slugging percentage |
| `ops` | On-base plus slugging |
| `era` | Earned run average (pitchers) |
| `wins` | Pitcher wins |
| `losses` | Pitcher losses |
| `strikeouts` | Strikeouts |
| `mlbUrl` | Official MLB player page URL |
| `scrapedAt` | Timestamp of scraping |

### Standings (getStandings)

| Field | Description |
|-------|-------------|
| `teamName` | Team name |
| `divisionName` | Division name (e.g. AL East) |
| `leagueName` | American League or National League |
| `wins` | Total wins |
| `losses` | Total losses |
| `pct` | Winning percentage |
| `gamesBack` | Games behind division leader |
| `divisionRank` | Rank within division |
| `streakCode` | Current streak (e.g. W5, L2) |
| `runsScored` | Total runs scored |
| `runsAllowed` | Total runs allowed |
| `runDifferential` | Run differential |

### Schedule (getSchedule)

| Field | Description |
|-------|-------------|
| `gamePk` | Game primary key |
| `gameDate` | Game date/time (ISO 8601) |
| `officialDate` | Official game date (YYYY-MM-DD) |
| `homeTeam` | Home team name |
| `awayTeam` | Away team name |
| `homeScore` | Home team runs scored |
| `awayScore` | Away team runs scored |
| `status` | Game status (Final, In Progress, etc.) |
| `venue` | Stadium name |
| `mlbUrl` | Official MLB gameday page URL |

### Teams (getTeams)

| Field | Description |
|-------|-------------|
| `teamId` | MLB team identifier |
| `name` | Full team name |
| `abbreviation` | 2–3 letter abbreviation (e.g. NYY) |
| `teamName` | Short team name (e.g. Yankees) |
| `locationName` | City/location |
| `leagueName` | American League or National League |
| `divisionName` | Division (e.g. AL East) |
| `venueName` | Home stadium name |
| `active` | Whether the team is active |
| `mlbUrl` | Official MLB team page URL |

## Example Configurations

**Get top 2024 batting stats (default, works for daily test):**
```json
{
  "mode": "getPlayerStats",
  "statGroup": "hitting",
  "season": 2024,
  "maxItems": 30
}
```

**Get 2024 pitching leaders:**
```json
{
  "mode": "getPlayerStats",
  "statGroup": "pitching",
  "season": 2024,
  "maxItems": 50
}
```

**Get Yankees 2024 batting stats:**
```json
{
  "mode": "getPlayerStats",
  "statGroup": "hitting",
  "season": 2024,
  "teamId": 147,
  "maxItems": 50
}
```

**Get 2024 final standings:**
```json
{
  "mode": "getStandings",
  "season": 2024,
  "maxItems": 30
}
```

**Get opening week 2024 schedule:**
```json
{
  "mode": "getSchedule",
  "season": 2024,
  "startDate": "2024-03-20",
  "endDate": "2024-03-27",
  "maxItems": 50
}
```

**Get all 30 MLB teams:**
```json
{
  "mode": "getTeams",
  "season": 2024,
  "maxItems": 30
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
| Chicago White Sox | 145 | Seattle Mariners | 136 |
| Toronto Blue Jays | 141 | Washington Nationals | 120 |

## Use Cases

- **Fantasy baseball** — pull hitting and pitching stats for player evaluation
- **Sports analytics** — aggregate season stats for modeling and predictions
- **Sports dashboards** — build standings and stats leaderboards
- **Historical research** — analyze player and team performance across seasons (2019–2024)
- **Data pipelines** — feed official MLB data into BI tools or databases

## Data Source

All data comes from the [official MLB Stats API](https://statsapi.mlb.com/api/v1/) — the same API used by MLB.com and major sports analytics platforms. The API is completely free and requires no authentication.

## FAQs

**Q: How current is the data?**
A: Standings and schedules update in real-time during the season. Player stats may have slight delays (typically updated daily).

**Q: What seasons are available?**
A: This scraper supports 2019–2024. The MLB Stats API has historical data going back to 1876, but stat coverage varies for older seasons.

**Q: How do I filter by team?**
A: Set `teamId` to the MLB team ID. For example, `teamId: 147` returns only New York Yankees stats. Leave blank for all teams.

**Q: What does `statGroup` control?**
A: It switches between `hitting` (batting stats), `pitching` (ERA, WHIP, wins), and `fielding` (errors, putouts, assists).

**Q: Is there a cost to use this scraper?**
A: No. The MLB Stats API is free and public. This scraper requires no proxy or API credentials and runs on the Apify free plan.

**Q: Can I get playoff stats?**
A: The `getPlayerStats` mode uses regular season (`R`) data. For playoff-specific stats, adjust the game type via the API parameters if needed in a custom setup.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/mlb-baseball-stats-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
