# Kworb Music Charts Scraper Tutorial: Run This Apify Actor with Python

Scrape Kworb.net music charts - Spotify daily/weekly streaming charts (global + 76 countries), the worldwide Apple Music / iTunes song chart, YouTube's most-viewed music videos, all-time top-streamed Spotify artists, and per-artist song-level streaming stats. No login or proxy required.

This repository shows how to run [Kworb Music Charts Scraper](https://apify.com/crawlerbros/kworb-music-charts-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/kworb-music-charts-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/kworb-music-charts-scraper](https://apify.com/crawlerbros/kworb-music-charts-scraper)
- **SEO title:** Kworb Music Charts Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Kworb.net music charts - Spotify daily/weekly streaming charts (global + 76 countries), the worldwide Apple Music / iTunes song chart, YouTube's most-viewed music videos, all-time top-streamed Spotify artists, and per-artist song-level streaming stats. No login or proxy required.

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

# Kworb Music Charts Scraper

Scrape music streaming charts from [Kworb.net](https://kworb.net) — Spotify daily and weekly charts for 76 countries plus the global aggregate, the worldwide Apple Music / iTunes song chart, YouTube's real-time most-viewed music videos, Shazam and Deezer discovery charts by country, the US radio airplay chart, the all-time top-streamed Spotify artists, a composite cross-platform artist ranking, and per-artist song-level streaming stats. No login, cookies, or paid proxy required.

## What this actor does

- **Nine modes:** `spotifyChart`, `appleMusicChart`, `youtubeChart`, `shazamChart`, `deezerChart`, `radioChart`, `topArtists`, `globalArtistRanking`, `artistStats`
- **Spotify charts** — daily or weekly, global or any of 76 country markets, with position change, days/weeks on chart, peak position, streams, and streams-change deltas
- **Apple Music worldwide chart** — points-based ranking with per-country chart positions (US, UK, Germany, Australia, Japan)
- **YouTube real-time chart** — today's most-viewed music videos, filterable by regional category (English, Spanish, Asian, other)
- **Shazam discovery chart** — what listeners are Shazaming, by country (87 markets + worldwide)
- **Deezer chart** — Deezer's own streaming chart, by country
- **US radio airplay chart** — Billboard-style radio audience data with cross-platform position comparison (iTunes/Spotify/Apple Music/Shazam rank for the same song)
- **Top Spotify artists** — all-time most-streamed artists with lead/solo/feature streaming breakdowns
- **Global cross-platform artist ranking** — kworb's composite "who's biggest right now" leaderboard, combining live points from Apple Music, Spotify, iTunes, YouTube, Shazam, and Deezer into one score, updated every ~15 minutes
- **Per-artist stats** — every tracked song for an artist with lifetime and daily Spotify stream counts
- Empty fields are always omitted — every record only contains data Kworb actually published

## Output: chart entry (mode=spotifyChart)

- `country`, `period` — `daily` or `weekly`
- `platform: "spotify"`
- `rank`, `rankChange` — `+N` / `-N` / `=` / `NEW`
- `artist`, `trackTitle`
- `daysOnChart` (period=daily) / `weeksOnChart` (period=weekly)
- `peakPosition`, `weeksAtPeak`
- `streams`, `streamsChange`
- `sevenDayStreams`, `sevenDayStreamsChange` — period=daily only
- `totalStreams`
- `artistSpotifyId`, `artistUrl` — Spotify artist page
- `chartDate`, `sourceUrl`
- `recordType: "chartEntry"`, `scrapedAt`

## Output: chart entry (mode=appleMusicChart)

- `platform: "apple-music"`
- `rank`, `rankChange`
- `artist`, `trackTitle`
- `daysOnChart`, `peakPosition`, `weeksAtPeak`
- `points`, `pointsChange`
- `positionUS`, `positionUK`, `positionDE`, `positionAU`, `positionJP` — per-country chart position, only present where the song also charts there
- `chartDate`, `sourceUrl`
- `recordType: "chartEntry"`, `scrapedAt`

## Output: chart entry (mode=youtubeChart)

- `category`, `platform: "youtube"`
- `rank`, `rankChange`
- `videoTitle`
- `views`, `likes`
- `videoId`, `videoUrl`
- `chartDate`, `sourceUrl`
- `recordType: "chartEntry"`, `scrapedAt`

## Output: chart entry (mode=shazamChart / deezerChart)

- `platform: "shazam"` / `"deezer"`, `country`
- `rank`, `rankChange`
- `artist`, `trackTitle`
- `chartDate`, `sourceUrl`
- `recordType: "chartEntry"`, `scrapedAt`

## Output: chart entry (mode=radioChart)

- `platform: "radio"`, `country: "us"`
- `rank` — omitted for the unranked "bubbling under" tail (still real published data, just without an official chart position)
- `rankChange`
- `artist`, `trackTitle`
- `daysOnChart`, `peakPosition`, `weeksAtPeak`
- `audienceMillions`, `audienceChange`
- `stationCount`, `peakAudienceMillions`
- `itunesPosition`, `spotifyPosition`, `appleMusicPosition`, `shazamPosition` — cross-platform position for the same song, where Kworb publishes it
- `chartDate`, `sourceUrl`
- `recordType: "chartEntry"`, `scrapedAt`

## Output: artist (mode=topArtists)

- `platform: "spotify"`
- `rank`, `artist`
- `totalStreams`, `dailyStreams` — all-time / daily Spotify streams
- `asLeadStreams`, `soloStreams`, `asFeatureStreams` — streaming breakdown by billing
- `artistSpotifyId`, `artistUrl`
- `sourceUrl`
- `recordType: "artist"`, `scrapedAt`

## Output: artist (mode=globalArtistRanking)

- `rank`, `rankChange`
- `artist`
- `points` — composite cross-platform score
- `pointsAppleMusic`, `pointsSpotify`, `pointsItunes`, `pointsYoutube`, `pointsShazam`, `pointsDeezer` — per-platform point breakdown
- `topCountry` — country where the artist charts highest
- `countriesCharting` — count of countries the artist charts in
- `kworbArtistUrl` — kworb.net's own per-artist detail page (distinct from the Spotify `artistUrl` used by other modes)
- `chartDate`, `sourceUrl`
- `recordType: "artist"`, `scrapedAt`

## Output: artistSummary + song (mode=artistStats)

One `artistSummary` record plus one `song` record per tracked song.

**`artistSummary`:**
- `artistSpotifyId`, `artistUrl`, `sourceUrl`
- `artistName`
- `totalStreams`, `totalStreamsAsLead`, `totalStreamsSolo`, `totalStreamsAsFeature`
- `dailyStreams`, `dailyStreamsAsLead`, `dailyStreamsSolo`, `dailyStreamsAsFeature`
- `trackCount`, `trackCountAsLead`, `trackCountSolo`, `trackCountAsFeature`
- `recordType: "artistSummary"`, `scrapedAt`

**`song`:**
- `rank`, `artistSpotifyId`, `artistName`
- `songTitle`
- `streams`, `dailyStreams`
- `trackUrl` — official Spotify track link
- `sourceUrl`
- `recordType: "song"`, `scrapedAt`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `spotifyChart` | `spotifyChart` / `appleMusicChart` / `youtubeChart` / `shazamChart` / `deezerChart` / `radioChart` / `topArtists` / `globalArtistRanking` / `artistStats` |
| `country` | string | `global` | Spotify chart market — 76 countries + `global` (mode=spotifyChart) |
| `period` | string | `daily` | `daily` or `weekly` (mode=spotifyChart) |
| `youtubeCategory` | string | `global` | `global` / `anglo` / `hispano` / `asian` / `other` (mode=youtubeChart) |
| `chartCountry` | string | `us` | Chart market — 87 countries + `ww` worldwide (mode=shazamChart / deezerChart) |
| `artistNames` | array | `["Taylor Swift"]` | One or more artist names to resolve via Kworb's Spotify artist directory, one per entry — batch-lookup multiple artists in one run (mode=artistStats) |
| `spotifyArtistIds` | array | `[]` | One or more direct 22-char Spotify artist IDs, one per entry; processed before `artistNames` (mode=artistStats) |
| `maxItems` | int | `25` | Hard cap on emitted records (1-1000) |

### Example: global Spotify daily Top 25

```json
{ "mode": "spotifyChart", "country": "global", "period": "daily", "maxItems": 25 }
```

### Example: UK Spotify weekly chart

```json
{ "mode": "spotifyChart", "country": "gb", "period": "weekly", "maxItems": 50 }
```

### Example: worldwide Apple Music chart

```json
{ "mode": "appleMusicChart", "maxItems": 50 }
```

### Example: today's most-viewed music videos

```json
{ "mode": "youtubeChart", "youtubeCategory": "global", "maxItems": 25 }
```

### Example: an artist's Spotify song catalog

```json
{ "mode": "artistStats", "artistNames": ["Bad Bunny"], "maxItems": 50 }
```

### Example: batch-compare multiple artists in one run

```json
{ "mode": "artistStats", "artistNames": ["Bad Bunny", "Drake"], "spotifyArtistIds": ["06HL4z0CvFAxyc27GXpf02"], "maxItems": 150 }
```

### Example: Shazam discovery chart for France

```json
{ "mode": "shazamChart", "chartCountry": "fr", "maxItems": 50 }
```

### Example: Deezer chart worldwide

```json
{ "mode": "deezerChart", "chartCountry": "ww", "maxItems": 50 }
```

### Example: US radio airplay chart

```json
{ "mode": "radioChart", "maxItems": 100 }
```

### Example: global cross-platform artist ranking

```json
{ "mode": "globalArtistRanking", "maxItems": 100 }
```

## Use cases

- **Music industry analytics** — track streaming performance across platforms and markets
- **A&R and label research** — spot rising tracks/artists by chart movement and streams-change deltas
- **Playlist curation** — surface daily/weekly top movers by country
- **Marketing & PR** — monitor a specific artist's catalog performance over time
- **Competitive benchmarking** — compare an artist's cross-platform reach (Spotify vs Apple Music vs YouTube)

## FAQ

**What's Kworb?** An independent music-data site that aggregates and republishes publicly visible Spotify, Apple Music/iTunes, and YouTube chart data, updated multiple times daily. See [kworb.net](https://kworb.net).

**What countries are supported for Spotify charts?** 76 individual country markets (ISO 3166-1 alpha-2 codes) plus `global`, e.g. `us`, `gb`, `de`, `jp`, `br`, `in`, `mx`. See the `country` dropdown for the full list.

**What does `rankChange` mean?** The position change since the previous chart update: `+N` (moved up), `-N` (moved down), `=` (unchanged), or `NEW` (newly charted).

**Why are `totalStreams` values so large for `topArtists`?** Kworb publishes all-time totals in millions (e.g. `136,904.9` = ~136.9 billion streams); the actor converts this to an absolute stream count for consistency with other modes.

**How do I find a Spotify artist ID?** Run `mode=artistStats` with `artistNames` set — the actor resolves each name against Kworb's Spotify artist directory and returns the ID in the summary record. You can then reuse `spotifyArtistIds` directly on future runs to skip the lookup.

**Can I look up more than one artist in a single run?** Yes — `artistNames` and `spotifyArtistIds` both accept multiple entries. Each artist gets its own `artistSummary` record plus its own song records, all sharing the run's single `maxItems` cap (IDs are processed first, then names, in list order).

**Why is `chartDate` today's date rather than a chart-specific date?** Kworb's chart pages are live snapshots (continuously updated, not archived by date), so `chartDate` reflects when the actor captured the data.

**Is a proxy or login required?** No — Kworb serves full chart data to plain HTTP requests with no login, cookies, or proxy of any kind.

**Are Shazam and Deezer charts available for every country?** Shazam covers 87 markets, Deezer a smaller overlapping set. If a `chartCountry` isn't published for the selected platform, the run returns 0 records with a status message rather than an error — try a different country.

**Why do Spotify daily/weekly charts cap at 200 rows even with a higher `maxItems`?** Kworb's chart pages themselves only publish the top 200 positions per country/period — that's the full dataset the source makes available, not a scraper limitation.

**Why does `globalArtistRanking` cap at 300 rows even with a higher `maxItems`?** Kworb's Global Digital Artist Ranking page itself only publishes the top 300 artists — that's the full dataset the source makes available, not a scraper limitation.

**What about per-country iTunes charts and per-country YouTube "insights" charts?** Kworb also publishes these (`kworb.net/charts/itunes/<cc>.html`, `kworb.net/youtube/insights/<cc>_daily.html`). They're not yet exposed as separate modes since the existing `appleMusicChart` (worldwide, with US/UK/DE/AU/JP position columns) and `youtubeChart` (regional-category) modes cover the same songs/videos at a coarser granularity; full per-country breakouts are a candidate for a future update.

**How is `globalArtistRanking` different from `topArtists`?** `topArtists` is all-time cumulative Spotify streams only. `globalArtistRanking` is a live "who's biggest right now" score combining points from six platforms at once (Apple Music, Spotify, iTunes, YouTube, Shazam, Deezer) — closer to a real-time cross-platform popularity leaderboard than a lifetime totals list.

**What about kworb's live "iTunes popularity bars" (`kworb.net/pop/` and per-country variants)?** This section tracks intraday relative-popularity fluctuations as a 0–1 fraction against a handful of recent snapshot timestamps rather than a clean dated chart, and kworb's own site describes it as the original, most dated part of the site. It isn't exposed as a mode — `appleMusicChart` (worldwide) and `globalArtistRanking` (includes an iTunes points column) already surface the same underlying songs/artists in a more directly usable form.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/kworb-music-charts-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
