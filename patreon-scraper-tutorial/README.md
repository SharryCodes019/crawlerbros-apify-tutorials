# Patreon Scraper Tutorial: Run This Apify Actor with Python

Scrape Patreon creators (campaigns) with campaign metadata, tier pricing, public posts, and patron counts.

This repository shows how to run [Patreon Scraper](https://apify.com/crawlerbros/patreon-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/patreon-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/patreon-scraper](https://apify.com/crawlerbros/patreon-scraper)
- **SEO title:** Patreon Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Patreon creators (campaigns) with campaign metadata, tier pricing, public posts, and patron counts.

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

# Patreon Scraper

Scrape **Patreon** creators (campaigns) — name, summary, patron count, paid-member count, total post count, currency, tier pricing (with USD conversion), and recent public posts. No login required, pure HTTP using Patreon's `__NEXT_DATA__` payload + public posts API.

Built for creator-economy analytics, brand-deal teams, and competitive research on Patreon-monetised creators.

## What you get

### Creator records (`recordType=creator`)

| Field | Description |
| --- | --- |
| `id` | Patreon campaign ID |
| `vanity` | Vanity slug (`PhilosophyTube`) |
| `url` | Public Patreon URL |
| `name` | Campaign name |
| `summary` | Plain-text campaign description |
| `oneLiner` | Short tagline |
| `creationName` | What the creator makes (e.g. "Creating Philosophy Videos") |
| `currency` | Currency code (USD / EUR / GBP / …) |
| `patronCount` | Total patron count (free + paid) |
| `paidMemberCount` | Paid-member count |
| `creationCount` | Total post count |
| `payPerName` | "month" / "video" / "creation" |
| `isMonthly` | `true` if billing is monthly |
| `isNsfw` | `true` for adult content |
| `offersFreeMembership` | Whether a free tier exists |
| `offersPaidMembership` | Whether paid tiers exist |
| `publishedAt` | ISO 8601 launch date |
| `avatarPhotoUrl` | Avatar image URL |
| `coverPhotoUrl` | Banner image URL |
| `pledgeUrl` | Direct checkout URL |
| `creator` | `{fullName, vanity, url}` for the underlying user |
| `tiers` | Array of paid tiers (sorted by price ascending) |
| `scrapedAt` | ISO 8601 UTC timestamp |

Each tier in `tiers`:

| Field | Description |
| --- | --- |
| `id` | Tier (reward) ID |
| `title` | Tier title |
| `description` | Tier description (plain text) |
| `amountCents` | Price in cents |
| `amountUsd` | Price as a decimal USD/local-currency value |
| `currency` | Currency code |
| `patronCount` | Patrons on this tier |
| `requiresShipping` | `true` if physical fulfilment required |
| `imageUrl` | Tier illustration URL |

### Post records (`recordType=post`)

| Field | Description |
| --- | --- |
| `id` | Post ID |
| `vanity` | Creator vanity (added by us) |
| `title` | Post title |
| `publishedAt` | ISO 8601 publish timestamp |
| `url` | Public post URL |
| `postType` | `video_external_file`, `image_file`, `text_only`, `audio_file`, `link`, … |
| `isPaid` | `true` if patron-only |
| `isPublic` | `true` if visible to anonymous users |
| `patronCount` | Number of patrons who can see the post |
| `commentCount` | Comment count |
| `likeCount` | Like count |
| `teaserText` | Plain-text teaser (when paid post has a public teaser) |
| `content` | Plain-text body (when public) |
| `thumbnailUrl` | Thumbnail image URL |

Empty fields are dropped from every record at every depth.

## Input

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `mode` | Enum | `creator` | `creator` (campaign + tiers + posts) / `posts` (posts only) / `search` (creators by keyword) / `explore` (browse by category) / `postByUrl` (single post by URL) |
| `creators` | Array | `["PhilosophyTube"]` | Vanity slugs or full URLs (mode=creator/posts) |
| `searchQuery` | String | — | Keyword for `mode=search` |
| `category` | Enum | — | Patreon Explore category — `podcasts`, `video-film`, `music`, `visual-arts`, `comedy`, `games`, `writing`, `drawing-painting`, `comics-graphic-novels`, `tabletop-games`, `science`, `education`, `crafts-diy`, `lifestyle` |
| `postUrls` | Array | — | Patreon post URLs (`https://www.patreon.com/posts/<id>`) for `mode=postByUrl` |
| `includePosts` | Boolean | `true` | When `mode=creator`, also fetch posts |
| `maxPostsPerCreator` | Integer | `20` | Hard cap per-creator post emission (1-200) |
| `minPatronCount` | Integer | — | Drop creators with fewer patrons |
| `excludeNsfw` | Boolean | `false` | Drop NSFW creators |
| `maxItems` | Integer | `50` | Hard cap on total emitted records (1-5000) |

### Example input — single creator + posts

```json
{
  "mode": "creator",
  "creators": ["PhilosophyTube"],
  "includePosts": true,
  "maxPostsPerCreator": 20
}
```

### Example input — batch creators

```json
{
  "mode": "creator",
  "creators": ["jordanbpeterson", "PhilosophyTube"],
  "includePosts": false,
  "minPatronCount": 1000
}
```

### Example input — posts only

```json
{
  "mode": "posts",
  "creators": ["PhilosophyTube"],
  "maxPostsPerCreator": 100
}
```

### Example input — search creators

```json
{
  "mode": "search",
  "searchQuery": "philosophy",
  "minPatronCount": 500,
  "maxItems": 50
}
```

### Example input — explore by category

```json
{
  "mode": "explore",
  "category": "podcasts",
  "maxItems": 50
}
```

### Example input — fetch post by URL

```json
{
  "mode": "postByUrl",
  "postUrls": [
    "https://www.patreon.com/posts/85614999",
    "https://www.patreon.com/posts/welcome-to-the-12345"
  ]
}
```

## Example output

```json
{
  "recordType": "creator",
  "id": "114875",
  "vanity": "PhilosophyTube",
  "url": "https://www.patreon.com/PhilosophyTube",
  "name": "Philosophy Tube",
  "creationName": "Creating Philosophy Videos",
  "oneLiner": "Giving away a philosophy degree one video at a time.",
  "summary": "When the British government tripled university tuition in 2010 …",
  "currency": "USD",
  "patronCount": 15382,
  "paidMemberCount": 5233,
  "creationCount": 756,
  "payPerName": "month",
  "offersFreeMembership": true,
  "offersPaidMembership": true,
  "publishedAt": "2014-09-21T17:34:46.000+00:00",
  "creator": {
    "fullName": "Philosophy Tube",
    "vanity": "PhilosophyTube",
    "url": "https://www.patreon.com/PhilosophyTube"
  },
  "tiers": [
    { "id": "...", "title": "Patron", "amountCents": 200, "amountUsd": 2.00, "currency": "USD" },
    { "id": "...", "title": "Producer", "amountCents": 500, "amountUsd": 5.00 }
  ],
  "scrapedAt": "2026-05-06T05:42:18Z"
}
```

## Use cases

- **Creator-economy analytics** — Track patron growth and tier pricing across a portfolio of creators.
- **Brand-deal targeting** — Identify creators with N+ patrons in a niche for sponsorship outreach.
- **Competitive research** — Compare your creator's pricing/post-cadence with peers.
- **Investor due-diligence** — Patron counts are a public approximation of MRR; compare across creators.
- **Content audits** — Pull every public post from a Patreon creator for analysis or archival.

## FAQ

**Do I need a Patreon account?**
No. Every endpoint this actor uses is part of Patreon's public-facing site (the campaign page that any visitor can see) and the public posts JSON API.

**Why does `paidMemberCount` differ from `patronCount`?**
`patronCount` includes free-tier members. `paidMemberCount` is paying patrons only — usually a much smaller number for creators that offer a free tier.

**Are full post bodies included?**
Only for posts marked `is_public=true`. Patron-only posts return a public teaser (when set) but the full body is locked. Each post's `isPaid` / `isPublic` flags tell you which type you have.

**How many posts can I scrape per creator?**
Up to 200 per run via `maxPostsPerCreator`. The Patreon posts API paginates 20 at a time — large pulls take ~1 second per page.

**How current is the data?**
Live — every run hits Patreon at request time. Schedule the actor for hourly / daily refreshes to track patron-growth curves.

**Do I need a proxy?**
No. Patreon's public site is happy to serve datacenter IPs.

**What if Patreon does block me?**
The actor has built-in auto-escalation: on the first HTTP 403 / anti-bot block it lazily engages Apify Proxy (datacenter group first, residential as a second-stage fallback) and retries the failed URL transparently. All subsequent fetches in the same run continue through the proxied session. To disable, set `autoEscalateOnBlock=false`. To force a specific group set, populate `proxyGroups`.

## Limitations

- Patron-only post bodies are not accessible without a logged-in account.
- Some creators hide `patronCount` (set `member_count_preference` to TIER_BREAKDOWN); those records will still emit but with the count omitted.
- Earnings are not exposed unless the creator explicitly publishes them (`show_earnings`); we don't surface this field by default.
- Comments are not included in this version (each post would need a follow-up fetch); we surface `commentCount` for sentiment-trend approximation.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/patreon-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
