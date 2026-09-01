# Football Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape football statistics from ESPN's public API, standings, match results, team stats, and player profiles for all major leagues worldwide including Premier League, La Liga, Bundesliga, Serie A, Ligue 1, MLS, and more. No API key required.

This repository shows how to run [Football Stats Scraper](https://apify.com/crawlerbros/football-stats-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/football-stats-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/football-stats-scraper](https://apify.com/crawlerbros/football-stats-scraper)
- **SEO title:** Football Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape football statistics from ESPN's public API, standings, match results, team stats, and player profiles for all major leagues worldwide including Premier League, La Liga, Bundesliga, Serie A, Ligue 1, MLS, and more. No API key required.

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

# Football Stats Scraper

Scrape football statistics from ESPN's public API — **no API key required**. Covers all major leagues worldwide including Premier League, La Liga, Bundesliga, Serie A, Ligue 1, MLS, UEFA Champions League, and 20+ more.

## What does Football Stats Scraper do?

This actor retrieves comprehensive football data including:
- **League Standings** — full table with points, wins, losses, draws, goals for/against, goal difference, and qualification zones
- **Match Results** — recent and historical match scores with venue, attendance, and team form
- **Team Stats** — team profiles with season records and league information
- **Player Search** — search for player profiles by name to get position, age, nationality, and team info

Data source: ESPN's public sports API, fully accessible with no authentication required.

## Supported Leagues

| League | ID |
|--------|-----|
| English Premier League | `eng.1` |
| Spanish La Liga | `esp.1` |
| German Bundesliga | `ger.1` |
| Italian Serie A | `ita.1` |
| French Ligue 1 | `fra.1` |
| US Major League Soccer | `usa.1` |
| UEFA Champions League | `uefa.champions` |
| UEFA Europa League | `uefa.europa` |
| UEFA Conference League | `uefa.europa.conf` |
| Dutch Eredivisie | `ned.1` |
| Portuguese Primeira Liga | `por.1` |
| Brazilian Série A | `bra.1` |
| Argentine Primera División | `arg.1` |
| Mexican Liga MX | `mex.1` |
| Scottish Premiership | `sco.1` |
| Turkish Süper Lig | `tur.1` |
| Japanese J1 League | `jpn.1` |
| + 12 more | |

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | select | What to fetch: `standings`, `matchResults`, `teamStats`, or `playerSearch` |
| `league` | select | League to scrape (see table above, default: `eng.1`) |
| `fromDate` | text | Match results start date in `YYYYMMDD` format (mode=matchResults) |
| `toDate` | text | Match results end date in `YYYYMMDD` format (mode=matchResults) |
| `playerQuery` | text | Player name to search for (mode=playerSearch) |
| `maxItems` | integer | Maximum records to return (1–500, default: 50) |

## Output

### Standings record
```json
{
  "teamName": "Arsenal",
  "teamAbbreviation": "ARS",
  "teamId": "359",
  "leagueId": "eng.1",
  "leagueName": "English Premier League",
  "season": "2024-25 English Premier League",
  "rank": 1,
  "played": 38,
  "won": 26,
  "drawn": 7,
  "lost": 5,
  "points": 85,
  "goalsFor": 71,
  "goalsAgainst": 27,
  "goalDifference": 44,
  "standingNote": "Champions League",
  "teamLogoUrl": "https://a.espncdn.com/i/teamlogos/soccer/500/359.png",
  "teamUrl": "https://www.espn.com/soccer/club/_/id/359/arsenal",
  "scrapedAt": "2025-05-25T10:00:00+00:00"
}
```

### Match result record
```json
{
  "matchId": "727459",
  "leagueId": "eng.1",
  "leagueName": "English Premier League",
  "matchDate": "2025-01-15T15:00Z",
  "matchDateLocal": "2025-01-15",
  "status": "FT",
  "isCompleted": true,
  "homeTeamName": "Arsenal",
  "homeScore": 2,
  "homeWinner": true,
  "awayTeamName": "Chelsea",
  "awayScore": 1,
  "awayWinner": false,
  "venue": "Emirates Stadium",
  "venueCity": "London",
  "attendance": 60000,
  "scrapedAt": "2025-05-25T10:00:00+00:00"
}
```

## Use Cases

- **Fantasy football** — track player performance and team form
- **Sports analytics** — build datasets for league comparison and trend analysis
- **News monitoring** — extract live and historical match scores
- **Research** — compile season statistics for any major league
- **Dashboards** — power live league tables for websites and apps

## FAQ

**Q: Does this require an API key or registration?**
A: No. This actor uses ESPN's public sports API which is freely accessible with no authentication required.

**Q: How current is the data?**
A: Standings and match results reflect ESPN's live data, typically updated within minutes of matches ending.

**Q: Can I get historical match results?**
A: Yes. Use `mode=matchResults` with `fromDate` and `toDate` parameters in `YYYYMMDD` format to query any date range.

**Q: Which leagues are supported?**
A: 29 leagues spanning Europe, Americas, Asia, and global tournaments. See the supported leagues table above.

**Q: What's the data limit?**
A: Up to 500 records per run. For standings, you typically get all 20 teams in one run.

**Q: Is this free to run?**
A: Yes. No proxy, no API key, no paid add-ons required. Runs on the Apify free plan.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/football-stats-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
