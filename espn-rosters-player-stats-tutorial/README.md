# ESPN Rosters & Player Stats Tutorial: Run This Apify Actor with Python

Scrape team rosters and player career statistics from ESPN across 16 leagues and 5 sports. No account or proxy required.

This repository shows how to run [ESPN Rosters & Player Stats](https://apify.com/crawlerbros/espn-rosters-player-stats) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/espn-rosters-player-stats`
- **Apify Store:** [https://apify.com/crawlerbros/espn-rosters-player-stats](https://apify.com/crawlerbros/espn-rosters-player-stats)
- **SEO title:** ESPN Rosters & Player Stats Tutorial: Run This Apify Actor with Python
- **Description:** Scrape team rosters and player career statistics from ESPN across 16 leagues and 5 sports. No account or proxy required.

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

# ESPN Rosters & Player Stats Scraper

Scrape team rosters and player career statistics from [ESPN](https://www.espn.com) — no account or subscription required. Supports 16 leagues across 5 sports including the NBA, NFL, MLB, NHL, MLS, WNBA, NCAA basketball and football, Premier League, La Liga, Champions League, Bundesliga, Serie A, Ligue 1, and Liga MX.

## What This Scraper Does

This actor fetches team rosters from ESPN's public JSON API and returns one flat record per player with bio fields (name, jersey, position, height, weight, date of birth, college, etc.). With **Fetch Player Career Stats** enabled, it also adds sport-specific career totals — points, rebounds, passing yards, goals, etc. Supports current and historical seasons.

## Supported Leagues

| Code | Sport | League |
|---|---|---|
| `nba` | Basketball | NBA |
| `wnba` | Basketball | WNBA |
| `ncaam` | Basketball | NCAA Men's |
| `ncaaw` | Basketball | NCAA Women's |
| `nfl` | Football | NFL |
| `ncaaf` | Football | NCAA Football |
| `mlb` | Baseball | MLB |
| `nhl` | Hockey | NHL |
| `mls` | Soccer | Major League Soccer |
| `epl` | Soccer | English Premier League |
| `laliga` | Soccer | La Liga (Spain) |
| `ucl` | Soccer | UEFA Champions League |
| `bundesliga` | Soccer | Bundesliga (Germany) |
| `seriea` | Soccer | Serie A (Italy) |
| `ligue1` | Soccer | Ligue 1 (France) |
| `ligamx` | Soccer | Liga MX (Mexico) |

## Input

| Field | Type | Description |
|---|---|---|
| **Leagues** | List of strings | League codes to scrape. Defaults to `["nba"]`. |
| **Teams** | List of strings (optional) | Filter by team abbreviation (case-insensitive, e.g. `"LAL"`) or ESPN numeric team ID (e.g. `"13"`). Omit for all teams. |
| **Season** | Integer (optional) | Year the season ends (e.g. `2026` for NBA 2025-26). Omit for current season. |
| **Fetch Player Career Stats** | Boolean | If true, fetches career totals per player. Adds one API call per player (slow for large leagues). Default: `false`. |
| **Max Items** | Integer | Maximum number of player records across all leagues (1–50,000). Default: 500. |

### Team Filter Examples
- Just Lakers and Celtics: `"teams": ["LAL", "BOS"]`
- By ID: `"teams": ["13", "2"]`
- Mixed: `"teams": ["LAL", "17"]`
- Unknown entries log a warning and are skipped.

### Season Encoding

Use the ending year for cross-year seasons:
- NBA 2025-26 → `season: 2026`
- EPL 2025-26 → `season: 2026`
- NFL 2025 → `season: 2025`
- MLB 2025 → `season: 2025`

Historical support varies by sport. ESPN's public API typically returns the **current roster** even when a past season is requested; historical rosters are sparsely available for most leagues. Invalid or unavailable seasons are silently skipped (empty result, no error). If you need past-season rosters, verify availability on ESPN's website for your specific league + season before running.

## Output

Each record represents one player. Fields marked `?` are optional and appear only when ESPN returns data for them.

### Core bio fields

| Field | Type | Description |
|---|---|---|
| `league` | string | League code e.g. `"nba"` |
| `sport` | string | e.g. `"basketball"` |
| `season` | integer? | Season year (when provided) |
| `teamId` | string | ESPN team ID |
| `teamName` | string | Full team name |
| `teamAbbreviation` | string? | e.g. `"LAL"` |
| `teamLogo` | string? | Logo URL |
| `playerId` | string | ESPN athlete ID |
| `firstName` | string? | |
| `lastName` | string? | |
| `fullName` | string | |
| `displayName` | string? | |
| `shortName` | string? | |
| `jersey` | string? | |
| `position` | string? | e.g. `"Small Forward"` |
| `positionAbbreviation` | string? | e.g. `"SF"` |
| `height` | integer? | Inches |
| `displayHeight` | string? | e.g. `"6' 9\""` |
| `weight` | integer? | Pounds |
| `displayWeight` | string? | e.g. `"250 lbs"` |
| `age` | integer? | |
| `dateOfBirth` | string? | ISO date |
| `birthPlace` | string? | e.g. `"Akron, Ohio"` |
| `debutYear` | integer? | First pro year |
| `experience` | integer? | Years in league |
| `college` | string? | For NBA/NFL/NCAA |
| `headshot` | string? | Headshot URL |
| `status` | string? | e.g. `"Active"` |
| `statsUrl` | string? | Link to ESPN stats page |
| `scrapedAt` | string | ISO 8601 UTC |

### Career stats fields (when Fetch Player Career Stats is enabled)

Sport-specific fields are added to the same record:

**Basketball (NBA, WNBA, NCAAM/W):** `gamesPlayed`, `points`, `rebounds`, `assists`, `steals`, `blocks`, `fieldGoalPct`, `threePointPct`, `freeThrowPct`, `minutes`, `turnovers`

**Football (NFL, NCAAF):** `gamesPlayed`, `passingYards`, `passingTouchdowns`, `interceptions`, `passerRating`, `rushingYards`, `rushingTouchdowns`, `receptions`, `receivingYards`, `receivingTouchdowns`, `tackles`, `sacks`

**Baseball (MLB):** `gamesPlayed`, `battingAverage`, `homeRuns`, `rbis`, `hits`, `runs`, `stolenBases`, `era`, `wins`, `losses`, `strikeouts`, `inningsPitched`

**Hockey (NHL):** `gamesPlayed`, `goals`, `assists`, `points`, `plusMinus`, `penaltyMinutes`, `shotsOnGoal`, `savePct`, `goalsAgainstAverage`

**Soccer:** `appearances`, `goals`, `assists`, `minutesPlayed`, `yellowCards`, `redCards`, `shotsOnTarget`, `shots`

Fields only appear when ESPN returns data — no nulls.

### Error Records

If a league's team list or a team's roster fails to fetch, an error record is emitted:

| Field | Description |
|---|---|
| `inputLeague` | League code attempted |
| `inputTeam` | Team (if applicable) |
| `inputSeason` | Season attempted |
| `error` | Human-readable message |
| `scrapedAt` | Timestamp |

## Frequently Asked Questions

**Do I need an ESPN account?**
No. This scraper only uses ESPN's public JSON API.

**Is a proxy required?**
No. ESPN's public API has no bot protection for typical use.

**How do I get a single player?**
Use the Teams filter to narrow to the player's team, then filter the output by `fullName` in your downstream pipeline. ESPN doesn't have a public name-search endpoint, but rosters are small so this is fast.

**Why is NCAA slow?**
NCAA basketball has 365 teams and NCAA football has 136. Pulling all rosters can return thousands of players. Use the Teams filter (e.g. `["DUKE", "KY"]`) to narrow. With Fetch Player Career Stats enabled, each player adds one more API call — for NCAA, the Teams filter is strongly recommended.

**Why are some stat fields missing?**
ESPN returns different stats per sport and per player role. For example, a defensive back won't have `passingYards`; a reliever may not have `wins`. Per the no-null rule, fields only appear when ESPN has data.

**What's the difference between this actor and the other ESPN actors?**
- **Scores & Schedules** returns game-by-game data (final scores, schedules, leaders).
- **Standings** returns team-level standings (W/L, rank, points).
- **Rosters & Player Stats** returns player-level data (who is on each team + career stats).

**Does ESPN return salary data?**
No. ESPN's public API does not expose salary information.

**Can I combine multiple leagues in one run?**
Yes. Pass multiple codes in `leagues`, e.g. `["nba", "nfl", "mlb"]`. Each record is tagged with its league.

**How often is roster data updated?**
ESPN updates rosters in near real-time as transactions happen. Running the actor returns the latest state at fetch time.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/espn-rosters-player-stats)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
