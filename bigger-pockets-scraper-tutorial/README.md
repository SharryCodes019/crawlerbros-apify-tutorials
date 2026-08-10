# BiggerPockets Scraper Tutorial: Run This Apify Actor with Python

Scrape BiggerPockets, the largest real estate investing community. Pull forum topics, full post bodies + replies, and user profiles across 50+ investing categories. No login or proxy required.

This repository shows how to run [BiggerPockets Scraper](https://apify.com/crawlerbros/bigger-pockets-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bigger-pockets-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bigger-pockets-scraper](https://apify.com/crawlerbros/bigger-pockets-scraper)
- **SEO title:** BiggerPockets Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape BiggerPockets, the largest real estate investing community. Pull forum topics, full post bodies + replies, and user profiles across 50+ investing categories. No login or proxy required.

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

# BiggerPockets Scraper

Scrape the largest real estate investing community on the web. Pull forum topics with full post bodies, comment threads, vote/reply/view stats, and user profiles across 50+ investing categories — **no login, no cookies, no paid proxy required**.

Whether you're prospecting investor leads, researching market sentiment around BRRRR or house hacking, monitoring a competitor's username, or building a knowledge base from real-world deal analyses, this actor gives you structured JSON access to BiggerPockets' public discussion surface.

## What this scrapes

- **Forum topics** — title, full body text, author, dates, vote / reply / view counts, category
- **Forum replies (comments)** — body, author, dates, like counts, parent comment ID, threaded
- **User profiles** — display name, bio, job title, avatar, posts written, likes given, follower / following counts

## Modes

| Mode | Description |
|---|---|
| `forumLatest` | Newest topics from a chosen forum (default) |
| `forumTrending` | Trending-now topics from a chosen forum |
| `forumUnanswered` | Topics with no replies — investor-question lead gen |
| `multiForum` | Scan a list of forum IDs with any sort order |
| `byTopicIds` | Lookup specific topics by numeric ID |
| `byTopicUrls` | Lookup specific topics by full BiggerPockets URL |
| `byUsernames` | Pull user profiles by username |

## Forum catalog

The actor ships with all 50 active BiggerPockets forums as a dropdown enum, including:

- Real estate strategy — **BRRRR**, **House Hacking**, **Wholesaling**, **Rehabbing & House Flipping**, **Multi-Family**, **Mobile Home Parks**, **Commercial**, **Short-Term Rentals**, **Medium-Term Rentals**, **Land & New Construction**, **Tax Liens & Notes**, **Syndications & Passive Investing**
- Operations — **General Landlording**, **Managing Your Property**, **Marketing Your Property**, **Tenant Screening**
- Finance — **Creative Financing**, **Personal Finance**, **Insurance**, **Private Lending**, **Mortgage Brokers & Lenders**, **Tax / SDIRA / Cost Seg**, **1031 Exchanges**, **Foreclosures**
- Community — **Starting Out**, **First-Time Home Buyer**, **New Member Introductions**, **Success Stories**, **Horror Stories**, **Off Topic**
- News / data — **Real Estate News & Current Events**, **Market Trends & Data**, **Out of State Investing**
- Services — **Contractors**, **Real Estate Agent**, **Ask About A Real Estate Company**
- Reviews — **Guru, Book, & Course Reviews**, **Real Estate Technology**
- Marketplace — **Classifieds**, **Real Estate Events & Meetups**, **Buying & Selling Small Businesses**

## Filters

- `minReplies`, `minVotes`, `minViews` — engagement thresholds
- `containsKeyword` — title/body substring match
- `includeComments` + `maxCommentsPerTopic` — pull full reply threads
- `maxItems`, `maxPagesPerForum` — output and traversal limits

## Output fields

### Topic record (`recordType: "topic"`)

```json
{
  "recordType": "topic",
  "topicId": 1288127,
  "forumId": 311,
  "category": "Buying & Selling Real Estate",
  "title": "Thinking about this property",
  "slug": "thinking-about-this-property",
  "body": "I'm a first-time buyer looking to use an FHA loan to house hack...",
  "authorName": "Eddie Germosen",
  "authorUsername": "eddieg118",
  "authorUrl": "https://www.biggerpockets.com/users/eddieg118",
  "createdAt": "2026-05-12T17:48:36-07:00",
  "publishedAt": "2026-05-20T19:43:43-07:00",
  "modifiedAt": "2026-05-20T19:43:43-07:00",
  "commentCount": 16,
  "likeCount": 2,
  "viewCount": 144,
  "topicUrl": "https://www.biggerpockets.com/forums/311/topics/1288127-thinking-about-this-property",
  "scrapedAt": "2026-05-21T03:14:15.972+00:00"
}
```

### Comment record (`recordType: "comment"`)

```json
{
  "recordType": "comment",
  "commentId": 7217617,
  "topicId": 1288127,
  "forumId": 311,
  "category": "Buying & Selling Real Estate",
  "body": "Hello Eddie, Are both units the same size?...",
  "authorName": "Abel Curiel",
  "authorUsername": "abelc2",
  "authorUrl": "https://www.biggerpockets.com/users/abelc2",
  "createdAt": "2026-05-12T18:31:22-07:00",
  "likeCount": 0,
  "commentUrl": "https://www.biggerpockets.com/forums/311/topics/1288127-thinking-about-this-property#post_7217617",
  "scrapedAt": "2026-05-21T03:14:16.124+00:00"
}
```

### User record (`recordType: "user"`)

```json
{
  "recordType": "user",
  "userId": 547389,
  "username": "sparkrental",
  "name": "G. Brian Davis",
  "description": "G. Brian Davis cofounded SparkRental, which manages a real estate investment club...",
  "jobTitle": "Investor",
  "avatarUrl": "https://bpimg.biggerpockets.com/no_overlay/uploads/social_user/user_avatar/547389/...",
  "profileUrl": "https://www.biggerpockets.com/users/sparkrental",
  "postsMade": 2599,
  "likesGiven": 208,
  "followingCount": 259,
  "followerCount": 178,
  "scrapedAt": "2026-05-21T03:14:16.512+00:00"
}
```

All output is **omit-empty** — never null, empty string, empty list, or empty dict at any depth.

## Example inputs

### Get the 50 newest deal-analysis topics

```json
{
  "mode": "forumLatest",
  "forumId": "88",
  "maxItems": 50
}
```

### Scan multiple investing forums for trending topics with engagement filter

```json
{
  "mode": "multiForum",
  "forumIds": ["48", "853", "311", "922", "432"],
  "sortBy": "trending",
  "minVotes": 3,
  "maxItems": 100,
  "maxPagesPerForum": 3
}
```

### Pull a specific topic with full reply thread

```json
{
  "mode": "byTopicUrls",
  "topicUrls": [
    "https://www.biggerpockets.com/forums/311/topics/1288127-thinking-about-this-property"
  ],
  "includeComments": true,
  "maxCommentsPerTopic": 100,
  "maxItems": 200
}
```

### Find unanswered questions (lead-gen for agents / lenders / wholesalers)

```json
{
  "mode": "forumUnanswered",
  "forumId": "12",
  "maxItems": 50
}
```

### Pull user profiles

```json
{
  "mode": "byUsernames",
  "usernames": ["sparkrental", "abelc2"],
  "maxItems": 50
}
```

### Keyword research — finance topics mentioning "DSCR"

```json
{
  "mode": "multiForum",
  "forumIds": ["49", "22", "50"],
  "sortBy": "newest",
  "containsKeyword": "DSCR",
  "includeComments": false,
  "maxItems": 100,
  "maxPagesPerForum": 5
}
```

## Data source

This actor reads publicly accessible BiggerPockets pages (forum index, topic pages, user profiles) and parses the embedded **schema.org JSON-LD `DiscussionForumPosting` / `ProfilePage` blocks** that BiggerPockets serves for SEO. No login, no cookies, no paid proxy required — works from the free Apify plan with zero configuration.

## FAQ

### Do I need a BiggerPockets account?
No. The actor reads publicly indexed pages.

### Do I need a proxy?
No. BiggerPockets serves anonymous datacenter IPs without bot protection. Proxy support is included as optional — pass `proxyConfiguration: { useApifyProxy: true }` if you want to rotate IPs.

### Why aren't blog articles / market insights pages supported?
Those surfaces are React-rendered client-side without server-side data hooks, and Insights pages are gated behind a `BiggerPockets PRO` paywall. This actor focuses on the publicly accessible forum + user surface, which covers the bulk of investor discussion.

### Why aren't search results supported?
BiggerPockets' search endpoint (`/search?q=...`) is bot-protected and returns 403 from anonymous traffic. The actor exposes equivalent functionality via `containsKeyword` filtering across forum listings, which works reliably.

### Can I get a user's full posting history?
Currently the actor returns the profile metadata. For per-user post histories, use `byUsernames` to identify high-volume posters by `postsMade` count, then scan their forum activity via the forum-listing modes.

### How fresh is the data?
Forum listings are updated in real-time. Topic detail JSON-LD reflects the latest state when fetched.

### Are votes / likes / view counts accurate?
Yes. Counts are pulled from BiggerPockets' own `schema.org/InteractionCounter` blocks, identical to what they expose to Google.

### What happens if a topic is locked or deleted?
The actor returns `null` for that record and continues. No partial / corrupted data.

### What's the maximum throughput?
The actor self-throttles to ~3 requests/second with retries on 429/5xx, comfortably under BiggerPockets' tolerance. A `maxItems=1000` run with `includeComments=false` completes in ~5 minutes.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bigger-pockets-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
