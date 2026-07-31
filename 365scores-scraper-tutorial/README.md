# 365Scores Sports Data Scraper Tutorial: Run This Apify Actor with Python

Scrape 365Scores (365scores.com) public API for live sports scores, standings, and competition data. Covers football, basketball, baseball, hockey, tennis, cricket, and more.

This repository shows how to run [365Scores Sports Data Scraper](https://apify.com/crawlerbros/365scores-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/365scores-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/365scores-scraper](https://apify.com/crawlerbros/365scores-scraper)
- **SEO title:** 365Scores Sports Data Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape 365Scores (365scores.com) public API for live sports scores, standings, and competition data. Covers football, basketball, baseball, hockey, tennis, cricket, and more.

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

# 365Scores Sports Data Scraper

Scrape **365Scores** (365scores.com) public API for live sports scores, league standings, and competition listings. Covers 9 sports including football, basketball, baseball, hockey, tennis, cricket, rugby, golf, and MMA.

## What This Actor Does

Fetches sports data from the 365Scores public API including:
- **Live Scores**: Today's games with real-time scores and status for any sport/competition
- **Recent Games**: Latest results with final scores and match details
- **Standings**: League tables with points, wins, draws, losses, goals
- **Competitions**: Full list of competitions/leagues available for a sport

## Supported Sports

| Sport | Code |
|-------|------|
| Football (Soccer) | `football` |
| Basketball | `basketball` |
| Baseball | `baseball` |
| Ice Hockey | `hockey` |
| Tennis | `tennis` |
| Cricket | `cricket` |
| Rugby | `rugby` |
| Golf | `golf` |
| MMA | `mma` |

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | string | `liveScores`, `recentGames`, `standings`, or `competitions` |
| `sport` | string | Sport to fetch (default: `football`) |
| `competition` | string | Competition slug (e.g. `premier-league`, `bundesliga`) |
| `competitionId` | integer | Direct 365Scores competition ID (overrides slug) |
| `maxItems` | integer | Max records to return (default: 10) |

### Example Input

```json
{
  "mode": "liveScores",
  "sport": "football",
  "competition": "premier-league",
  "maxItems": 10
}
```

## Output

### Game Record (liveScores / recentGames)

| Field | Description |
|-------|-------------|
| `gameId` | 365Scores game ID |
| `sport` | Sport name |
| `competition` | Competition name |
| `competitionId` | Competition ID |
| `country` | Country of competition |
| `homeTeam` | Home team name |
| `homeTeamId` | Home team ID |
| `homeScore` | Home team score |
| `homeTeamImageUrl` | Home team logo URL |
| `awayTeam` | Away team name |
| `awayTeamId` | Away team ID |
| `awayScore` | Away team score |
| `awayTeamImageUrl` | Away team logo URL |
| `statusText` | Game status (e.g. "Final", "In Progress") |
| `gameTime` | Scheduled start time |
| `gameUrl` | Link to game on 365scores.com |

### Standing Record (standings mode)

| Field | Description |
|-------|-------------|
| `teamName` | Team name |
| `position` | League table position |
| `played` | Matches played |
| `wins` / `draws` / `losses` | Results breakdown |
| `goalsFor` / `goalsAgainst` / `goalDifference` | Goal stats |
| `points` | Points total |

### Example Output

```json
{
  "gameId": "12345",
  "sport": "football",
  "competition": "Premier League",
  "country": "England",
  "homeTeam": "Arsenal",
  "awayTeam": "Chelsea",
  "homeScore": 2,
  "awayScore": 1,
  "statusText": "Final",
  "gameUrl": "https://www.365scores.com/football/match/12345"
}
```

## FAQs

**Is this free to use?**
Yes. 365Scores provides a public REST API used by their website with no API key required.

**Why is this actor built instead of WhoScored?**
WhoScored uses Cloudflare Bot Management that blocks datacenter IPs. 365Scores offers a comparable set of sports data via a fully public API.

**How often is data updated?**
365Scores updates live scores in real-time during games. Historical data is always available.

**How do I find a specific competition ID?**
Run the `competitions` mode to list all competitions for your sport, then use the `competitionId` field in your next run.

**Can I get data for leagues outside the defaults?**
Yes — use `competitions` mode to discover all available competition IDs for any sport, then pass the `competitionId` directly.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/365scores-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
