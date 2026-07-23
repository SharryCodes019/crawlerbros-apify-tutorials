# FlashScore Live Sports Scraper Tutorial: Run This Apify Actor with Python

Scrape live matches from FlashScore for football, basketball, tennis, hockey, baseball and 11 other sports. Returns match ID, teams, live score, status, league, start time and optional event timeline.

This repository shows how to run [FlashScore Live Sports Scraper](https://apify.com/crawlerbros/flashscore-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/flashscore-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/flashscore-scraper](https://apify.com/crawlerbros/flashscore-scraper)
- **SEO title:** FlashScore Live Sports Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape live matches from FlashScore for football, basketball, tennis, hockey, baseball and 11 other sports. Returns match ID, teams, live score, status, league, start time and optional event timeline.

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

# FlashScore Live Sports Scraper

Scrape live (or same-day) matches from **[FlashScore.com](https://www.flashscore.com)** for 14 sports including football (soccer), tennis, basketball, hockey, baseball, cricket, and more. Returns match ID, home / away teams, live score, status, league, country, start time, and match URL — all in one fast HTTP request.

## What it does

- Fetches matches from FlashScore's internal live-feed endpoint (no browser, no proxy, no cookies)
- Supports **14 sports** via a simple `sport` enum
- Optional **live-only filter** to return only matches currently in progress
- Clean, non-null output — empty fields are omitted so every record has only populated keys
- Hardcoded `X-Fsign` token + Chrome 131 TLS impersonation — runs from any datacenter IP

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `sport` | enum | `football` | One of: `football`, `tennis`, `basketball`, `hockey`, `american-football`, `baseball`, `handball`, `rugby-union`, `rugby-league`, `futsal`, `volleyball`, `cricket`, `darts`, `snooker` |
| `liveOnly` | boolean | `true` | If true, only matches currently in progress. If false, return all matches for today (scheduled + live + finished). |
| `maxItems` | integer | `100` | Maximum matches to return (1–1000) |

### Example input

```json
{
    "sport": "football",
    "liveOnly": false,
    "maxItems": 10
}
```

## Output

Each match is a JSON record with the following fields (missing fields are omitted, never `null`):

| Field | Type | Always present | Description |
|---|---|---|---|
| `matchId` | string | ✓ | FlashScore match ID |
| `sport` | string | ✓ | The sport slug (same as the input) |
| `homeTeam` | string | ✓ | Home team name |
| `awayTeam` | string | ✓ | Away team name |
| `status` | string | ✓ | `scheduled`, `live`, `finished`, `half-time`, etc. |
| `statusCode` | number | ✓ | FlashScore's raw status code (`AB`) |
| `scrapedAt` | string | ✓ | UTC ISO 8601 scrape timestamp |
| `homeScore` | number | — | Current home score (omitted before kick-off) |
| `awayScore` | number | — | Current away score |
| `league` | string | — | League or tournament name, e.g. `ENGLAND: Premier League` |
| `country` | string | — | Country label from FlashScore's tree |
| `leaguePath` | string | — | Relative league URL path |
| `startTime` | string | — | ISO 8601 UTC kick-off time |
| `homeTeamShort` | string | — | 3-letter home team abbreviation |
| `awayTeamShort` | string | — | 3-letter away team abbreviation |
| `url` | string | — | Full match summary URL |

### Sample output

```json
{
    "matchId": "bN6cMaFq",
    "sport": "football",
    "homeTeam": "Lanus",
    "awayTeam": "Banfield",
    "homeScore": 1,
    "awayScore": 0,
    "status": "finished",
    "statusCode": 3,
    "league": "ARGENTINA: Liga Profesional - Apertura",
    "country": "Argentina",
    "leaguePath": "/football/argentina/liga-profesional/",
    "startTime": "2026-04-13T13:20:00Z",
    "homeTeamShort": "LAN",
    "awayTeamShort": "BAN",
    "url": "https://www.flashscore.com/football/argentina/liga-profesional/lanus-banfield/#/match-summary",
    "scrapedAt": "2026-04-14T05:54:44Z"
}
```

## FAQ

**Do I need a proxy or cookies?**
No. FlashScore's internal feed accepts standard HTTP requests from any datacenter IP with just the `X-Fsign` token (which is hardcoded in the scraper) plus a Chrome 131 TLS fingerprint.

**How fresh is the data?**
Every run hits the live feed at request time. Live match scores update within seconds of the event.

**What does `liveOnly` do?**
Setting `liveOnly=true` filters the response to matches with a status code in the in-progress range (live, half-time, etc). Setting it to `false` returns all matches scheduled for today including finished ones — useful for overnight historical pulls.

**Why do some sports return 0 matches?**
Not every sport has live events running at every moment. For example, `american-football` will be empty outside the NFL season, and `cricket` will be empty outside the main test windows. The scraper returns `0 items` with `exit_code=0` in that case — it is not a failure.

**Are event timelines included?**
Not in the current release. The scraper returns match headers only. The per-match event timeline (goals, cards, substitutions) requires a second API call which is not yet implemented.

## Use cases

- **Sports betting signals** — monitor live score changes across 14 sports
- **Fantasy sports feeds** — ingest live scores into a fantasy scoring engine
- **Media sites** — power live score widgets for a sports publication
- **Stats research** — build historical datasets by running `liveOnly=false` daily
- **Notification services** — trigger alerts on specific team / league events

## Notes

- Pricing is configured in the Apify UI (pay-per-event or pay-per-result).
- The scraper uses a single HTTP request per run — very cheap to operate at the default `maxItems=100`.
- The daily Apify test run uses `sport=football`, `liveOnly=false`, `maxItems=5` against the live feed.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/flashscore-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
