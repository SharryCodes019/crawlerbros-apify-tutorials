# ESPN News Tutorial: Run This Apify Actor with Python

Scrape ESPN news articles and headlines across 16 leagues and 5 sports. Optional team filter. No account or proxy required.

This repository shows how to run [ESPN News](https://apify.com/crawlerbros/espn-news) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/espn-news`
- **Apify Store:** [https://apify.com/crawlerbros/espn-news](https://apify.com/crawlerbros/espn-news)
- **SEO title:** ESPN News Tutorial: Run This Apify Actor with Python
- **Description:** Scrape ESPN news articles and headlines across 16 leagues and 5 sports. Optional team filter. No account or proxy required.

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

# ESPN News Scraper

Scrape news articles and headlines from [ESPN](https://www.espn.com) — no account or subscription required. Supports 16 leagues across 5 sports including the NBA, NFL, MLB, NHL, MLS, WNBA, NCAA basketball and football, Premier League, La Liga, Champions League, Bundesliga, Serie A, Ligue 1, and Liga MX.

## What This Scraper Does

This actor fetches news articles from ESPN's public JSON API and returns one flat record per article with headline, description, full HTML body, author, publication timestamp, image URLs, and related team/athlete references. Optional team filter fetches additional team-specific articles.

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
| **Teams** | List of strings (optional) | Filter by team abbreviation (case-insensitive, e.g. `"LAL"`) or ESPN numeric team ID (e.g. `"13"`). Team-filtered articles are fetched IN ADDITION to league-wide articles. Unknown entries log a warning and are skipped. |
| **Fetch Full Article Body** | Boolean | If enabled, makes one extra API call per article to fetch the full HTML body (`story` field). Without this, only headlines and summaries are returned. Adds ~300ms per article. Default: `false`. |
| **Max Items** | Integer | Maximum number of article records across all leagues (1–10,000). Default: 100. |

### Team Filter Examples
- Just Lakers: `"teams": ["LAL"]`
- By ID: `"teams": ["13"]`
- Multiple: `"teams": ["LAL", "BOS", "GS"]`
- Mixed: `"teams": ["LAL", "17"]`

### Why ~10 Articles Per League?

ESPN's public news endpoint returns a fixed feed of approximately 10 articles per request and does NOT support pagination, offset, or date filtering. To get more articles per league, use the **Teams** filter — each team adds another ~10 team-specific articles to the fetch.

## Output

Each record represents one article. Fields marked `?` are optional and appear only when ESPN returns data for them. Duplicates (same article fetched via both league-wide and team filters) are automatically deduped by `articleId`.

| Field | Type | Description |
|---|---|---|
| `articleId` | string | ESPN article ID (dedup key) |
| `league` | string | League code e.g. `"nba"` |
| `sport` | string | e.g. `"basketball"` |
| `type` | string? | e.g. `"Story"`, `"Preview"`, `"HeadlineNews"`, `"Media"` |
| `headline` | string | Always present |
| `description` | string? | Short summary |
| `story` | string? | Full HTML body of the article (only when **Fetch Full Article Body** is enabled) |
| `byline` | string? | Author name |
| `published` | string? | ISO 8601 publication timestamp |
| `lastModified` | string? | ISO 8601 last-modified timestamp |
| `premium` | boolean? | If `true`, ESPN+ paid content |
| `url` | string? | Web URL to the article |
| `mobileUrl` | string? | Mobile web URL |
| `images` | object[]? | Array of `{url, caption?, credit?, width?, height?}` |
| `keywords` | string[]? | ESPN keyword tags |
| `relatedTeams` | object[]? | Array of `{teamId, teamName, abbreviation}` |
| `relatedAthletes` | object[]? | Array of `{athleteId, athleteName}` |
| `inputTeam` | string? | The team-filter entry that fetched this article (only on team-filtered results) |
| `scrapedAt` | string | ISO 8601 UTC scrape timestamp |

Fields only appear when ESPN returns data — no nulls.

### Error Records

If a league news feed fails to fetch after retries, an error record is emitted:

| Field | Description |
|---|---|
| `inputLeague` | League code attempted |
| `inputTeam` | Team (if team-filtered fetch failed) |
| `error` | Human-readable message |
| `scrapedAt` | Timestamp |

## Frequently Asked Questions

**Do I need an ESPN account?**
No. This scraper only uses ESPN's public JSON API.

**Is a proxy required?**
No. ESPN's public API has no bot protection for typical use.

**Can I get articles from a specific date?**
No — ESPN's public news endpoint does not support date filtering. Articles are returned in reverse chronological order (newest first). To capture daily news, run the actor on a schedule (e.g., hourly or daily) and dedupe downstream by `articleId`.

**How many articles can I get per league per run?**
ESPN returns ~10 articles for the league-wide feed. Use the **Teams** filter to get ~10 more per team — so for NBA with all 30 teams, you can get up to ~310 articles per run. Duplicates are auto-removed.

**What's the difference between the `story` field and `description`?**
`description` is a one-sentence summary; `story` is the full article HTML body (with `<p>`, `<a>`, etc.).

**When does the `story` field appear?**
Only when you enable the **Fetch Full Article Body** input option. ESPN's main news feed returns only headlines and summaries. The body requires an additional API call per article, so it's opt-in. Enable it if you need the full article HTML for downstream processing.

**How do I handle the HTML body?**
The `story` field contains raw HTML. You can strip tags downstream (e.g., BeautifulSoup for plain text), render it in an HTML viewer, or extract specific elements like paragraphs or links.

**Why are some articles marked `premium: true`?**
Those are ESPN+ paid content. The API returns the same metadata (headline, description, body) but you'd need an ESPN+ account to read the article on espn.com. The scraped data itself is fully available.

**How do dedup + team filters work together?**
If you specify `teams: ["LAL"]` and `leagues: ["nba"]`, the scraper fetches the NBA league feed AND the Lakers team feed. An article appearing in both is returned once (with `inputTeam` set to `LAL` if it was seen via the team feed first). Use this to maximize coverage without duplicates.

**What's the difference between this actor and the other ESPN actors?**
- **Scores & Schedules** — game results, live scores, upcoming schedules
- **Standings** — team rankings and W/L records
- **Rosters & Player Stats** — team rosters and player career stats
- **News** — articles and headlines (this actor)

**Can I combine multiple leagues?**
Yes. Pass multiple codes in `leagues`, e.g. `["nba", "epl", "mlb"]`. Each record is tagged with its league.

**How often is ESPN updating the news?**
News is near real-time. ESPN publishes new articles throughout the day, so a hourly schedule will usually pick up 5–20 fresh articles per league.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/espn-news)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
