# ESPN NFL Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape NFL statistics from ESPN's public API - team rosters with player profiles, team standings, team schedules, game scoreboards, and NFL news. Covers all 32 NFL teams with player bio data. No API key required.

This repository shows how to run [ESPN NFL Stats Scraper](https://apify.com/crawlerbros/espn-nfl-stats-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/espn-nfl-stats-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/espn-nfl-stats-scraper](https://apify.com/crawlerbros/espn-nfl-stats-scraper)
- **SEO title:** ESPN NFL Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape NFL statistics from ESPN's public API - team rosters with player profiles, team standings, team schedules, game scoreboards, and NFL news. Covers all 32 NFL teams with player bio data. No API key required.

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

# ESPN NFL Stats Scraper

Scrape NFL statistics from **[ESPN's public API](https://site.api.espn.com/apis/site/v2/sports/football/nfl)** — team rosters with player profiles, league standings, team schedules, game scoreboards, and the latest NFL news. Covers all 32 NFL teams with no API key required.

> **Data source:** ESPN public API (site.api.espn.com/nfl) — free, no registration required. Replaces Pro Football Reference (pro-football-reference.com) which blocks all Apify datacenter IPs.

## Features

- **Team rosters** — full player roster with bio data (name, position, age, college, physical stats)
- **League standings** — wins, losses, win percentage, points for/against, streak, division/conference records
- **Team schedule** — all games for a season with scores, venues, dates
- **Scoreboard** — current/recent NFL game scores and status
- **NFL news** — latest articles with headlines, descriptions, related teams/athletes
- **All teams** — list of all 32 NFL teams with logos and URLs

## Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mode` | select | `roster`, `standings`, `schedule`, `scoreboard`, `news`, or `teams` |
| `teamId` | integer | ESPN team ID (required for roster/schedule; see description for all 32 IDs) |
| `season` | integer | Season year (e.g., 2024 for 2024-25 season) |
| `maxItems` | integer | Max records to return (1–500, default 50) |

## Team IDs Reference

| ID | Team | ID | Team |
|----|------|----|------|
| 1 | Atlanta Falcons | 17 | New England Patriots |
| 2 | Buffalo Bills | 18 | New Orleans Saints |
| 3 | Chicago Bears | 19 | New York Giants |
| 4 | Cincinnati Bengals | 20 | New York Jets |
| 5 | Cleveland Browns | 21 | Philadelphia Eagles |
| 6 | Dallas Cowboys | 22 | Arizona Cardinals |
| 7 | Denver Broncos | 23 | Pittsburgh Steelers |
| 8 | Detroit Lions | 24 | Los Angeles Chargers |
| 9 | Green Bay Packers | 25 | San Francisco 49ers |
| 10 | Tennessee Titans | 26 | Seattle Seahawks |
| 11 | Indianapolis Colts | 27 | Tampa Bay Buccaneers |
| 12 | Kansas City Chiefs | 28 | Washington Commanders |
| 13 | Las Vegas Raiders | 29 | Carolina Panthers |
| 14 | Los Angeles Rams | 30 | Jacksonville Jaguars |
| 15 | Miami Dolphins | 33 | Baltimore Ravens |
| 16 | Minnesota Vikings | 34 | Houston Texans |

## Output Fields

### Player record (mode=roster)
| Field | Description |
|-------|-------------|
| `playerId` | ESPN player ID |
| `playerName` | Full name |
| `position` | Position abbreviation (QB, WR, RB, etc.) |
| `jersey` | Jersey number |
| `age` | Player age |
| `weightLbs` | Weight in pounds |
| `heightInches` | Height in inches |
| `college` | College/university |
| `birthPlace` | City, state, country |
| `headshotUrl` | Player headshot image URL |
| `playerUrl` | ESPN player page URL |

### Standing record (mode=standings)
| Field | Description |
|-------|-------------|
| `teamName` | Team name |
| `conference` | AFC or NFC |
| `division` | Division name |
| `wins` | Wins |
| `losses` | Losses |
| `winPercentage` | Win percentage |
| `pointsFor` | Points scored |
| `pointsAgainst` | Points allowed |
| `streak` | Current streak |

## Frequently Asked Questions

**Is an API key required?**
No. ESPN's site API is publicly accessible without authentication.

**How often is data updated?**
ESPN updates game scores in real time during games. Rosters and standings are updated daily.

**What seasons are available?**
The ESPN API has historical data going back to 2000. Use the `season` parameter to specify the year.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/espn-nfl-stats-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
