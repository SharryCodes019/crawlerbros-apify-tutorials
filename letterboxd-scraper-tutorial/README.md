# Letterboxd Scraper Tutorial: Run This Apify Actor with Python

Scrape Letterboxd, the cinephile community's film database. Pull film metadata (directors, cast, genres, runtime, ratings, tagline), search by title, browse popular films, or fetch a member's profile. Pure HTTP, no login required.

This repository shows how to run [Letterboxd Scraper](https://apify.com/crawlerbros/letterboxd-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/letterboxd-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/letterboxd-scraper](https://apify.com/crawlerbros/letterboxd-scraper)
- **SEO title:** Letterboxd Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Letterboxd, the cinephile community's film database. Pull film metadata (directors, cast, genres, runtime, ratings, tagline), search by title, browse popular films, or fetch a member's profile. Pure HTTP, no login required.

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

# Letterboxd Scraper

Scrape **Letterboxd** — the cinephile community's film database. Pull rich metadata for any film (directors, cast, genres, runtime, average rating, ratings count, tagline, plot summary, languages, countries), search films by title, browse popular films and lists, scrape film reviews, browse films by director / actor / studio / country, or fetch a member's profile with their public stats and watchlist. No login, no cookies required.

Letterboxd's React frontend is fronted by Cloudflare; the actor uses Chrome 131 TLS impersonation to fetch the public-by-default pages exactly as a browser would.

## Modes

| Mode | What it returns |
| --- | --- |
| `film` | Full metadata for one or more film slugs (`recordType=film`) |
| `search` | Films matching a title query (`recordType=film`) |
| `userProfile` | Public profile + activity stats (`recordType=user`) |
| `lists` | Popular lists index OR contents of a single list (`recordType=list` + `recordType=film`) |
| `popular` | Films ranked by popularity in a chosen window (week / month / year / all-time) |
| `filmReviews` | Reviews for a film (paginated, sorted by activity) (`recordType=review`) |
| `byCrew` | Films attached to a director, actor, studio, or country (`recordType=crewMember` + `recordType=film`) |
| `userWatchlist` | A user's public watchlist, paginated (`recordType=film`) |

## What you get

### Film records (`recordType=film`)

| Field | Description |
| --- | --- |
| `slug` | Letterboxd film slug (`parasite-2019`) |
| `url` | Public film URL |
| `title` | Film title |
| `year` | Release year |
| `directors` | Array of director names |
| `cast` | Array of leading cast names (top ~10) |
| `genres` | Array of genres (e.g. `Drama`, `Thriller`) |
| `countries` | Array of country names |
| `productionCompanies` | Array of producing companies |
| `runtimeMinutes` | Runtime in minutes |
| `tagline` | Marketing tagline |
| `description` | Plot summary (from og:description) |
| `originalLanguages` | Primary language(s) |
| `posterUrl` | Poster image URL |
| `averageRating` | Letterboxd average rating (0-5 scale, e.g. `4.53`) |
| `ratingsCount` | Total user ratings cast |
| `reviewsCount` | Total user reviews |

### User records (`recordType=user`)

| Field | Description |
| --- | --- |
| `username` | Letterboxd handle |
| `url` | Profile URL |
| `displayName` | Display name |
| `bio` | Profile bio |
| `avatarUrl` | Avatar image URL |
| `filmsLogged` | Total films logged |
| `filmsThisYear` | Films logged in the current year |
| `followersCount` | Follower count |
| `followingCount` | Following count |

Empty fields are dropped from every record at every depth — the dataset never contains nulls.

## Input

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `mode` | Enum | `film` | One of `film` / `search` / `userProfile` / `lists` / `popular` / `filmReviews` / `byCrew` / `userWatchlist` |
| `filmSlugs` | Array | `["parasite-2019"]` | Slugs (`parasite-2019`) or full URLs. Used when `mode=film` |
| `filmSlug` | String | — | Single film slug for `mode=filmReviews` |
| `searchQuery` | String | — | Film title query. Used when `mode=search` |
| `enrichSearchResults` | Boolean | `false` | When `mode=search`, also visit each film's page for full metadata. Slower but enables year / rating / genre filters |
| `username` | String | — | Letterboxd handle. Used when `mode=userProfile` or `mode=userWatchlist` |
| `listUrl` | String | — | Letterboxd list URL for `mode=lists` (single list). Leave empty to fetch popular lists index |
| `popularPeriod` | Enum | `week` | `week` / `month` / `year` / `all-time` — used by `mode=popular` and `mode=lists` (popular lists index) |
| `crewType` | Enum | `director` | `director` / `actor` / `studio` / `country` — used by `mode=byCrew` |
| `crewSlug` | String | — | Letterboxd slug for the crew person/entity (e.g. `christopher-nolan`, `a24`, `japan`) |
| `minYear` / `maxYear` | Integer | — | Drop films outside the year range |
| `minRating` | Integer | — | Drop films with average rating below this. Scale is `0-500` (i.e. `350` = `3.5/5`) |
| `genre` | Enum | — | Drop films missing this genre. One of 19 Letterboxd genres (Action, Adventure, Animation, Comedy, Crime, Documentary, Drama, Family, Fantasy, History, Horror, Music, Mystery, Romance, Science Fiction, TV Movie, Thriller, War, Western) |
| `maxItems` | Integer | `25` | Hard cap on emitted records (1-500) |

### Example input — single film

```json
{
  "mode": "film",
  "filmSlugs": ["parasite-2019", "the-godfather", "dune-part-two"]
}
```

### Example input — search by title

```json
{
  "mode": "search",
  "searchQuery": "Dune",
  "maxItems": 25
}
```

### Example input — search with full metadata enrichment

```json
{
  "mode": "search",
  "searchQuery": "Christopher Nolan",
  "enrichSearchResults": true,
  "minYear": 2000,
  "minRating": 350,
  "maxItems": 50
}
```

### Example input — user profile

```json
{
  "mode": "userProfile",
  "username": "dave"
}
```

### Example input — popular films this week

```json
{
  "mode": "popular",
  "popularPeriod": "week",
  "maxItems": 50
}
```

### Example input — list contents

```json
{
  "mode": "lists",
  "listUrl": "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/",
  "maxItems": 50
}
```

### Example input — popular lists index

```json
{
  "mode": "lists",
  "popularPeriod": "week",
  "maxItems": 25
}
```

### Example input — film reviews

```json
{
  "mode": "filmReviews",
  "filmSlug": "parasite-2019",
  "maxItems": 50
}
```

### Example input — films by director / studio / country

```json
{
  "mode": "byCrew",
  "crewType": "director",
  "crewSlug": "christopher-nolan",
  "maxItems": 50
}
```

```json
{
  "mode": "byCrew",
  "crewType": "studio",
  "crewSlug": "a24",
  "maxItems": 50
}
```

```json
{
  "mode": "byCrew",
  "crewType": "country",
  "crewSlug": "japan",
  "maxItems": 100
}
```

### Example input — user watchlist

```json
{
  "mode": "userWatchlist",
  "username": "dave",
  "maxItems": 100
}
```

## Example output

```json
{
  "recordType": "film",
  "slug": "parasite-2019",
  "url": "https://letterboxd.com/film/parasite-2019/",
  "title": "Parasite",
  "year": 2019,
  "directors": ["Bong Joon Ho"],
  "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"],
  "genres": ["Thriller", "Comedy", "Drama"],
  "countries": ["South Korea"],
  "runtimeMinutes": 133,
  "tagline": "Act like you own the place.",
  "description": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy and glamorous Parks…",
  "originalLanguages": ["Korean"],
  "averageRating": 4.53,
  "ratingsCount": 5323455,
  "reviewsCount": 700624,
  "posterUrl": "https://a.ltrbxd.com/resized/sm/upload/oi/ha/78/z8/parasite-1200-1200-675-675-crop-000000.jpg",
  "scrapedAt": "2026-05-06T05:42:18Z"
}
```

## Use cases

- **Film recommendation engines** — Pull rich metadata + community ratings for any film catalogue.
- **Entertainment research** — Track average rating and review count over time for industry analysis.
- **Content discovery** — Search Letterboxd's index and filter by year / rating / genre.
- **Competitive review analysis** — Pair with our IMDb / Rotten Tomatoes scrapers for full-spectrum film coverage.
- **CRM enrichment** — Augment cinephile lead records with public Letterboxd activity (films logged, follower counts).
- **Academic / film studies** — Snapshot community-driven ratings + tags for sociological analysis.

## FAQ

**Do I need a Letterboxd account?**
No. The Letterboxd film pages, search endpoint, and public profiles all serve anonymous traffic.

**Why Chrome 131 TLS impersonation?**
Letterboxd is fronted by a Cloudflare WAF that fingerprints the TLS handshake and rejects vanilla Python clients. Chrome 131 impersonation matches the fingerprint of a real desktop Chrome browser and passes through cleanly.

**How does search work?**
The actor uses Letterboxd's `/s/autocompletefilm?q=...` JSON endpoint, which is much richer (and more reliable) than scraping the React-rendered search page. Each result includes slug, title, release year, runtime, and director. Set `enrichSearchResults=true` to follow each result with a full film-page fetch (needed for year / rating / genre filters and to get genres, cast, ratings count).

> The autocomplete endpoint refuses unauthenticated requests from many datacenter IP ranges. The actor's input default is `proxy: {useApifyProxy: true, apifyProxyGroups: ["RESIDENTIAL"]}` which routes through residential IPs and works reliably. `mode=film` and `mode=userProfile` work without proxy too — proxy is only mandatory for `mode=search`.

**How do `minYear` / `maxYear` / `minRating` / `genre` filters interact with search?**
Filters require full film metadata to evaluate. If any filter is set in `mode=search`, the actor automatically enriches each search result with a film-page fetch (slower but accurate).

**Can I scrape reviews?**
Yes — set `mode=filmReviews` and provide a `filmSlug`. Each record has the reviewer's username + display name, the rating they gave, the review text, the review date, the like / comment counts, and the canonical review URL. Pagination is automatic up to `maxItems`.

**How do I list a director's / actor's / studio's filmography?**
Set `mode=byCrew`, choose `crewType` (`director` / `actor` / `studio` / `country`) and provide the matching `crewSlug` (Letterboxd's URL slug — e.g. `christopher-nolan`, `timothee-chalamet`, `a24`, `japan`).

**How do I scrape a list's contents?**
Set `mode=lists` and pass the full list URL in `listUrl`. The first record is the list's metadata (`recordType=list`); subsequent records are the films in the list (`recordType=film`) preserving original order via `listPosition`. Leaving `listUrl` empty returns the **popular lists index** for the chosen `popularPeriod`.

**How current is the data?**
Live — every run hits Letterboxd at request time. Schedule the actor for daily / hourly refreshes to track rating drift on a film catalogue.

**Do I need a proxy?**
No. The Cloudflare WAF accepts datacenter IPs as long as the TLS fingerprint is real (which Chrome 131 impersonation provides). The actor sets a polite User-Agent and stays well under any rate limit.

## Limitations

- `mode=search` and the listing-based modes (`popular`, `lists`, `byCrew`, `userWatchlist`) work best with Apify Residential Proxy (input default). `mode=film`, `mode=userProfile`, and `mode=filmReviews` work without proxy from most IPs.
- Letterboxd lists pages return up to 100 films per page (multiple pages auto-paginated up to `maxItems`).
- TLS fingerprints can shift; if a future Cloudflare update breaks Chrome 131 impersonation, we'll bump to the latest supported impersonation profile.
- Country `crewSlug` uses Letterboxd's slug format (e.g. `japan`, `south-korea`, `usa`), not ISO-2.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/letterboxd-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
