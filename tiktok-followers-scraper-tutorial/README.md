# TikTok Followers & Following Scraper Tutorial: Run This Apify Actor with Python

Scrape the followers and following lists for TikTok profiles. Input usernames or profile URLs. Supports pagination up to thousands of users. No cookies required.

This repository shows how to run [TikTok Followers & Following Scraper](https://apify.com/crawlerbros/tiktok-followers-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-followers-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-followers-scraper](https://apify.com/crawlerbros/tiktok-followers-scraper)
- **SEO title:** TikTok Followers & Following Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape the followers and following lists for TikTok profiles. Input usernames or profile URLs. Supports pagination up to thousands of users. No cookies required.

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

# TikTok Followers Scraper

Scrape the followers or following list for any TikTok account. Returns one row per user with full profile info and engagement stats. The following list (who the account follows) works without any cookie. The followers list (who follows the account) requires a `sessionCookie` because TikTok's followers API enforces authentication.

## What this actor does

- Accepts TikTok usernames (with or without @) and/or full profile URLs
- Scrapes the following list — accounts the target user follows — without any authentication
- Scrapes the followers list — accounts that follow the target user — when a `sessionCookie` is provided
- Can scrape both lists in a single run
- Returns username, display name, bio, avatar, verification status, and organization flag per user
- Optionally includes follower/following/heart/video counts from statsV2 for each user
- Paginates up to 5,000 users per profile
- Empty fields are omitted

## Output per user

- `sourceUsername` — the profile that was queried
- `sourceUserId` — TikTok user ID of the queried profile
- `listType` — `"followers"` or `"following"`
- `userId` — TikTok user ID (18–19 digit string)
- `secUid` — TikTok secUid for API calls
- `username` — TikTok @handle
- `displayName` — display name / nickname
- `verified` — whether this user has a verified badge
- `isOrganization` — whether this is a business/organization account
- `privateAccount` — whether this account is private
- `bio` — profile bio/signature text
- `avatarUrl` — avatar image URL
- `followerCount` — number of followers (from statsV2)
- `followingCount` — number of accounts this user follows (from statsV2)
- `heartCount` — total likes received across all videos (from statsV2)
- `videoCount` — number of public videos posted (from statsV2)
- `scrapedAt` — ISO 8601 timestamp when the record was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `usernames` | array | — | TikTok usernames to scrape (with or without @) |
| `profileUrls` | array | — | Full TikTok profile URLs as alternative or additional input |
| `listType` | string | `"following"` | `"following"` (no cookie needed), `"followers"` (requires sessionCookie), or `"both"` |
| `maxUsersPerProfile` | integer | `100` | Maximum users to fetch per profile (up to 5,000) |
| `includeStats` | boolean | `true` | Include follower/following/heart/video counts per user |
| `sessionCookie` | string | — | TikTok `sessionid` cookie value — required for followers mode |

### Example: Following list — no cookie needed

```json
{
  "usernames": ["natgeo"],
  "listType": "following",
  "maxUsersPerProfile": 30,
  "includeStats": true
}
```

### Example: Followers list — requires sessionCookie

```json
{
  "usernames": ["natgeo"],
  "listType": "followers",
  "maxUsersPerProfile": 500,
  "includeStats": true,
  "sessionCookie": "your_sessionid_value_here"
}
```

### Example: Both lists for multiple profiles

```json
{
  "usernames": ["natgeo", "bbcnews"],
  "listType": "both",
  "maxUsersPerProfile": 200,
  "includeStats": true,
  "sessionCookie": "your_sessionid_value_here"
}
```

### Example: Following list — lightweight, no stats

```json
{
  "usernames": ["khaby.lame"],
  "listType": "following",
  "maxUsersPerProfile": 1000,
  "includeStats": false
}
```

## Use cases

- **Influencer scouting** — discover which accounts top creators follow to find emerging talent before they go viral
- **Audience research** — export a brand account's follower list for CRM enrichment or lookalike audience building
- **Competitive analysis** — identify follower overlap between competing accounts or creators in the same niche
- **Partnership vetting** — check whether a target influencer follows brand accounts or competitor handles
- **Community mapping** — map the follow graph around a specific creator or brand to understand their ecosystem
- **Social analytics export** — build structured datasets of TikTok user profiles for social media intelligence platforms

## FAQ

**Do I need a TikTok account or cookies?**
It depends on the mode. `listType: "following"` is fully public — no cookie needed. `listType: "followers"` requires a `sessionCookie` because TikTok's followers API (`scene=151`) ignores the target account parameters without authentication and returns a generic regional list.

**How do I get my sessionCookie?**
Install the Cookie-Editor browser extension, log into TikTok at tiktok.com, click the icon, find the cookie named `sessionid`, and copy its value. Paste that value into the `sessionCookie` field.

**Why does `heartCount` come from statsV2?**
TikTok's legacy `stats.heart` field uses a 32-bit integer that overflows to negative values for large creators with billions of likes. `statsV2.heartCount` is a string and never overflows.

**Can I scrape the following list of a private account?**
The following list of a private account is not publicly accessible via TikTok's API.

**Can I get more than 5,000 users?**
5,000 is the practical limit per profile enforced by TikTok's pagination. Set `maxUsersPerProfile` to 5,000 for the maximum.

**How long does it take to scrape 1,000 users?**
Approximately 5 minutes per 1,000 users due to API pagination delays.

**Can I scrape multiple profiles at once?**
Yes. Add multiple entries to `usernames` or `profileUrls`. Profiles are scraped sequentially.

**Are TikTok usernames case-sensitive?**
No. TikTok usernames are case-insensitive and the actor normalizes them automatically.

**What happens if `listType: "followers"` is used without a sessionCookie?**
Without a cookie, TikTok's followers API ignores `targetUserId` and returns a generic regional user list unrelated to the queried account. Always provide a `sessionCookie` for followers mode.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
| TikTok Post Scraper | https://apify.com/crawlerbros/tiktok-post-scraper |
| TikTok Profile Scraper | https://apify.com/crawlerbros/tiktok-profile-scraper |
| TikTok Comments Scraper | https://apify.com/crawlerbros/tiktok-comments-scraper |
| TikTok Search Scraper | https://apify.com/crawlerbros/tiktok-search-scraper |
| TikTok Hashtag Scraper | https://apify.com/crawlerbros/tiktok-hashtag-scraper |
| TikTok Music Scraper | https://apify.com/crawlerbros/tiktok-music-scraper |
| TikTok Transcript Scraper | https://apify.com/crawlerbros/tiktok-transcript-scraper |
| TikTok Mention Scraper | https://apify.com/crawlerbros/tiktok-mention-scraper |
| TikTok Profile Mention Scraper | https://apify.com/crawlerbros/tiktok-profile-mention-scraper |
| TikTok Playlist Scraper | https://apify.com/crawlerbros/tiktok-playlist-scraper |
| TikTok Explore Scraper | https://apify.com/crawlerbros/tiktok-explore-scraper |
| TikTok For You Scraper | https://apify.com/crawlerbros/tiktok-for-you-scraper |
| TikTok Downloader | https://apify.com/crawlerbros/tiktok-downloader-api |
| TikTok Ads Library Scraper | https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro |
| TikTok Top Ads Scraper | https://apify.com/crawlerbros/tiktok-top-ads-scraper |
| TikTok Hashtag Trends Scraper | https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper |
| TikTok LIVE Scraper | https://apify.com/crawlerbros/tiktok-live-scraper |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-followers-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
