# Product Hunt Scraper Tutorial: Run This Apify Actor with Python

Scrape Product Hunt launches, makers, hunters, votes, and topics. Daily leaderboard, by topic, by user, or single product detail.

This repository shows how to run [Product Hunt Scraper](https://apify.com/crawlerbros/producthunt-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/producthunt-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/producthunt-scraper](https://apify.com/crawlerbros/producthunt-scraper)
- **SEO title:** Product Hunt Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Product Hunt launches, makers, hunters, votes, and topics. Daily leaderboard, by topic, by user, or single product detail.

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

# Product Hunt Scraper

Scrape launches, makers, hunters, votes, comments, and topics from [Product Hunt](https://www.producthunt.com). Two paths: a **no-token web path** (default — works out of the box) and an **official GraphQL API path** (free token unlocks richer fields and advanced modes). HTTP-only. No proxy. No cookies.

## Two paths

### 1. No-token (default) — `dailyLeaderboard` mode only

Just run with `mode=dailyLeaderboard`. Scrapes the public daily leaderboard pages and returns id, name, slug, tagline, votes, comments, daily/weekly/monthly rank, topics, dates, thumbnail. Doesn't include description, makers, hunter, or media.

### 2. Free Product Hunt API token — full launch metadata + all modes

Get a free Bearer token (instant — no payment, no review):

1. Sign in at https://www.producthunt.com
2. Go to https://api.producthunt.com/v2/oauth/applications
3. Click **Add application**, fill in any name/redirect URL
4. Copy the **Developer Token** (not the OAuth secret)
5. Paste into this actor's `apiToken` field

With a token: full launch metadata (description, makers, hunter, media), and unlocks `topic`, `userLaunches`, `productDetail` modes.

## What this actor does

- Four fetch modes: daily / all launches, by topic, by user (made posts), single product detail
- Returns full launch metadata: name, tagline, description, votes, comments, topics, hunter, makers, media
- Filters: featured-only, date range, min votes / comments, tag intersection
- Sorts: RANKING (daily-rank), VOTES, NEWEST, FEATURED_AT
- Pagination via cursors — fetches up to 5,000 launches per run
- Honors Product Hunt API rate limits (free tier: 50 complexity/15s, 1k/day)

## Output per launch

- `id`, `slug`, `name`, `tagline`, `description`
- `productUrl` — direct link to the product's website
- `phUrl` — the launch page on Product Hunt
- `votesCount`, `commentsCount`, `reviewsCount`
- `featuredAt`, `createdAt` — ISO timestamps
- `topics[]` — slugs (e.g. `["productivity", "saas"]`)
- `topicDetails[]` — full topic objects with `id`, `slug`, `name`
- `hunter` — `{id, username, name, headline, profileImage}`
- `makers[]` — array of users (when `includeMakers=true`)
- `media[]` — screenshots / videos (when `includeMedia=true`)
- `recordType: "post"`, `scrapedAt`

Empty fields are omitted (no nulls).

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `apiToken` | string (secret) | – | Optional. Bearer token from PH OAuth applications page. Without it, only `mode=dailyLeaderboard` works (with limited fields). |
| `mode` | string | `dailyLeaderboard` | `dailyLeaderboard` / `topic` / `userLaunches` / `productDetail` |
| `topicSlugs` | array | `[]` | Required for `mode=topic` (e.g. `["artificial-intelligence"]`) |
| `userSlugs` | array | `[]` | Required for `mode=userLaunches` (e.g. `["rrhoover"]`) |
| `productSlugs` | array | `[]` | Required for `mode=productDetail` (e.g. `["notion","figma"]`) |
| `sortBy` | string | `RANKING` | `RANKING` / `VOTES` / `NEWEST` / `FEATURED_AT` |
| `featuredOnly` | bool | `false` | Only emit launches that were officially featured |
| `dateRangeFrom` | string | – | ISO date — drop launches before this |
| `dateRangeTo` | string | – | ISO date — drop launches after this |
| `minVotes` | int | – | Drop launches below this vote count |
| `minComments` | int | – | Drop launches below this comment count |
| `tagAnyOf` | array | `[]` | Only emit launches tagged with at least one of these topic slugs |
| `includeMakers` | bool | `true` | Include the makers array |
| `includeMedia` | bool | `false` | Include screenshots / videos |
| `maxItems` | int | `50` | Hard cap (1–5000) |

### Example: top AI launches this year

```json
{
  "apiToken": "<your-token>",
  "mode": "topic",
  "topicSlugs": ["artificial-intelligence"],
  "sortBy": "VOTES",
  "dateRangeFrom": "2025-01-01",
  "minVotes": 500,
  "maxItems": 100
}
```

### Example: daily leaderboard

```json
{
  "apiToken": "<your-token>",
  "mode": "dailyLeaderboard",
  "sortBy": "RANKING",
  "featuredOnly": true,
  "maxItems": 30
}
```

### Example: a maker's portfolio

```json
{
  "apiToken": "<your-token>",
  "mode": "userLaunches",
  "userSlugs": ["rrhoover"],
  "maxItems": 50
}
```

### Example: lookup specific products by slug

```json
{
  "apiToken": "<your-token>",
  "mode": "productDetail",
  "productSlugs": ["notion", "figma", "linear"]
}
```

### Example: developer-tools launches with media + makers

```json
{
  "apiToken": "<your-token>",
  "mode": "topic",
  "topicSlugs": ["developer-tools"],
  "sortBy": "VOTES",
  "includeMakers": true,
  "includeMedia": true,
  "minVotes": 100,
  "maxItems": 200
}
```

## Use cases

- **VC deal flow** — daily monitor of new launches in your verticals (AI, fintech, dev tools, etc.)
- **Founder competitor research** — track every product launching in your category
- **Product manager benchmarking** — analyze tagline patterns of top-voted launches
- **Growth marketing** — identify emerging tools to integrate or partner with
- **Indie hacker discovery** — find solo-founders and early-stage products
- **Content / newsletter automation** — daily digest of top launches with descriptions
- **Topic / category trend analysis** — vote distributions over time per topic
- **Hunter / maker network mapping** — find prolific hunters / makers in your domain

## FAQ

**Does it require a Product Hunt account?**  Only if you want full fields and access to topic/user/productDetail modes. The default `dailyLeaderboard` mode works without any token — just run it.

**What's the difference between the two paths?**  No-token (web path): id, slug, name, tagline, votes, comments, ranks, topics, dates, thumbnail. With token (GraphQL): all of the above PLUS description, makers, hunter, full media, reviewsCount.

**Is the token paid?**  No, the developer token is free. The free tier is 50 complexity points / 15 seconds (~1k requests/day for typical queries).

**What's the difference between hunter and maker?**  The **hunter** is the person who submitted the launch to Product Hunt (often a community member, not the founder). **Makers** are the people who actually built the product.

**Why are some `productUrl` fields missing?**  Some launches don't list an external website (rare). The actor omits empty fields rather than emit nulls.

**Can I get launches from before Product Hunt's GraphQL API existed?**  Yes — the API has full historical data going back to the site's launch in 2013.

**What does `featured` mean?**  Product Hunt selects a subset of submitted launches to feature on the homepage. Featured launches are eligible for the daily leaderboard. Unfeatured launches still exist in the API but get less visibility.

**How fresh is the data?**  Real-time. New launches appear in the API within seconds of submission.

**Can I scrape comments?**  Comment-count is included; comment text/threads is not part of v1. Use the `phUrl` field to link out to the comment thread.

**What about user reviews?**  `reviewsCount` is included. Per-review text is not part of v1.

**Is there a topic catalog?**  Common topic slugs: `artificial-intelligence`, `developer-tools`, `productivity`, `saas`, `marketing`, `design-tools`, `health-fitness`, `social-media`, `analytics`, `ecommerce`, `mobile`, `chrome-extensions`, `slack-apps`, `crypto`, `web3`. Browse the full catalog at https://www.producthunt.com/topics.

**What's the rate limit?**  Free tier: 50 complexity points / 15s (~1k requests/day). The actor backs off automatically on `429`. For higher throughput, request a quota upgrade from Product Hunt.

**Is this affiliated with Product Hunt?**  No, this actor is third-party and uses the public, official Product Hunt GraphQL API.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/producthunt-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
