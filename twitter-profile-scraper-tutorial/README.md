# Twitter Profile Scraper Tutorial: Run This Apify Actor with Python

Extract comprehensive Twitter/X profile data and tweets including all engagement metrics (likes, retweets, replies, quotes, bookmarks, views), profile details, media URLs, hashtags, and mentions with anti-detection features and authenticated scraping support.

This repository shows how to run [Twitter Profile Scraper](https://apify.com/crawlerbros/twitter-profile-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/twitter-profile-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/twitter-profile-scraper](https://apify.com/crawlerbros/twitter-profile-scraper)
- **SEO title:** Twitter Profile Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract comprehensive Twitter/X profile data and tweets including all engagement metrics (likes, retweets, replies, quotes, bookmarks, views), profile details, media URLs, hashtags, and mentions with anti-detection features and authenticated scraping support.

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

# Twitter Profile Scraper

Scrape tweets, engagement metrics, and full profile data from any public Twitter/X account. Extract likes, retweets, replies, views, bookmarks, media, hashtags, mentions, and more — no official API key required.

Twitter/X authentication cookies are **required**. See the **Authentication** section below for how to export your session cookies.

---

## Features

- **Full profile metadata** — display name, bio, location, website, joined date, follower/following counts, profile image, banner image, verification status
- **Complete tweet data** — text, timestamp, tweet ID & URL, all engagement metrics (likes, retweets, replies, quotes, bookmarks, views)
- **Media extraction** — images and video thumbnails from each tweet
- **Rich tweet context** — hashtags, mentions, external URLs, reply-to username, is-reply / is-retweet flags
- **Filtering** — include or exclude replies and retweets
- **Multi-profile** — scrape multiple usernames in a single run
- **Block recovery** — automatically detects rate limits and pauses before retrying
- **Stealth mode** — Firefox with anti-detection headers, randomised delays, human-like mouse/scroll behaviour

---

## Input Parameters

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `usernames` | array of strings | ✅ | — | Twitter/X usernames to scrape (with or without @ prefix) |
| `cookies` | string (secret) | ✅ | — | Twitter/X session cookies in JSON format (see Authentication below) |
| `maxTweets` | integer | | 50 | Max tweets to collect per profile (1–500) |
| `includeReplies` | boolean | | false | Include reply tweets |
| `includeRetweets` | boolean | | true | Include retweets |
| `proxyConfiguration` | object | | disabled | Proxy settings — enable if you hit IP-based blocks |

### Minimal Input

```json
{
  "usernames": ["elonmusk"]
}
```

### With Multiple Profiles and Filters

```json
{
  "usernames": ["elonmusk", "openai", "github"],
  "maxTweets": 100,
  "includeReplies": false,
  "includeRetweets": true
}
```

### With Your Own Cookies (Recommended for Large Runs)

```json
{
  "usernames": ["elonmusk"],
  "maxTweets": 200,
  "cookies": "[{\"name\":\"auth_token\",\"value\":\"your_token\",\"domain\":\".x.com\",\"path\":\"/\",\"httpOnly\":true,\"secure\":true}]"
}
```

---

## Output Format

Each item in the dataset represents one tweet, enriched with the author's profile metadata. Empty fields (null, blank string, empty array, empty object) are omitted — the dataset never contains nulls.

```json
{
  "tweet_id": "1881234567890123456",
  "tweet_url": "https://twitter.com/elonmusk/status/1881234567890123456",
  "text": "Tweet content here",
  "timestamp": "2025-01-20T14:32:00.000Z",
  "likes_count": 42000,
  "retweets_count": 8500,
  "replies_count": 1200,
  "bookmarks_count": 3100,
  "views_count": 9800000,
  "is_retweet": false,
  "is_reply": false,
  "reply_to": null,
  "media_urls": [
    "https://pbs.twimg.com/media/AbCdEf123.jpg"
  ],
  "hashtags": ["AI", "Tesla"],
  "mentions": ["openai"],
  "urls": ["https://tesla.com"],
  "scrapedProfile": "elonmusk",
  "authorMeta": {
    "username": "elonmusk",
    "display_name": "Elon Musk",
    "bio": "Tesla, SpaceX, Neuralink, The Boring Company",
    "location": "Texas, USA",
    "website": "https://tesla.com",
    "joined_date": "Joined June 2009",
    "birth_date": null,
    "followers_count": 228100000,
    "following_count": 1219,
    "tweets_count": 47800,
    "verified": true,
    "profile_image_url": "https://pbs.twimg.com/profile_images/xyz/photo_400x400.jpg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/xyz/banner.jpg",
    "scraped_at": "2025-01-20T15:00:00.000000"
  }
}
```

### Output Fields Reference

**Tweet fields**

| Field | Type | Description |
|---|---|---|
| `tweet_id` | string | Unique tweet ID |
| `tweet_url` | string | Direct URL to the tweet |
| `text` | string | Full tweet text |
| `timestamp` | string | ISO 8601 timestamp |
| `likes_count` | integer | Number of likes |
| `retweets_count` | integer | Number of retweets/reposts |
| `replies_count` | integer | Number of replies |
| `bookmarks_count` | integer | Number of bookmarks |
| `views_count` | integer | Number of views |
| `is_retweet` | boolean | Whether this is a retweet |
| `is_reply` | boolean | Whether this is a reply |
| `reply_to` | string / null | Username being replied to |
| `media_urls` | array | Image/video URLs attached to the tweet |
| `hashtags` | array | Hashtags used (without #) |
| `mentions` | array | Usernames mentioned (without @) |
| `urls` | array | External URLs in the tweet |
| `scrapedProfile` | string | Username that was scraped |
| `authorMeta` | object | Full profile data (see below) |

**authorMeta fields**

| Field | Type | Description |
|---|---|---|
| `username` | string | Twitter/X handle |
| `display_name` | string | Full display name |
| `bio` | string | Profile biography |
| `location` | string | Location text from profile |
| `website` | string | Website URL from profile |
| `joined_date` | string | When the account was created |
| `birth_date` | string / null | Birth date if set publicly |
| `followers_count` | integer | Number of followers |
| `following_count` | integer | Number of accounts followed |
| `tweets_count` | integer | Total post count |
| `verified` | boolean | Whether the account is verified |
| `profile_image_url` | string | Profile picture URL (400×400) |
| `profile_banner_url` | string | Header/banner image URL |
| `scraped_at` | string | ISO 8601 timestamp of when data was collected |

---

## Authentication

The actor ships with built-in session cookies so it works immediately without any configuration. For runs collecting 100+ tweets or scraping many profiles, providing your own fresh cookies reduces the chance of hitting rate limits.

### How to Export Your Cookies

1. Log into [x.com](https://x.com) in your browser
2. Install the [Cookie-Editor](https://cookie-editor.com) extension
3. Click the extension icon and choose **Export → Export as JSON**
4. Paste the JSON array into the `cookies` input field

### Minimum Required Cookies

| Cookie | Purpose |
|---|---|
| `auth_token` | Authenticates your session |
| `ct0` | CSRF protection token |

### Cookie Format

```json
[
  {
    "name": "auth_token",
    "value": "your_auth_token",
    "domain": ".x.com",
    "path": "/",
    "httpOnly": true,
    "secure": true
  },
  {
    "name": "ct0",
    "value": "your_ct0_value",
    "domain": ".x.com",
    "path": "/",
    "httpOnly": false,
    "secure": true
  }
]
```

> **Note:** Keep your cookies private. They give full access to your Twitter/X account.

---

## Frequently Asked Questions

**Why am I getting old tweets instead of recent ones?**

Without valid authentication, Twitter shows a "Highlights" feed of popular old tweets rather than recent chronological posts. The actor's built-in cookies handle this automatically, but if they have expired, provide your own fresh cookies.

**Can I scrape private/protected profiles?**

Only if you are authenticated as an account that follows the private profile. Provide cookies from that account.

**How many tweets can I scrape per run?**

Up to 500 tweets per profile (`maxTweets` maximum). For very large profiles, multiple runs with different date ranges via the `maxTweets` limit are recommended.

**Will my account get banned?**

The actor uses randomised delays and human-like behaviour to minimise risk. Avoid running large jobs (500 tweets × many profiles) repeatedly in quick succession. Start with smaller batches to test.

**What happens if I get rate limited?**

The actor automatically detects rate-limit signals, navigates away, waits 45–55 seconds, then resumes. If a second block is detected, it saves what it has collected and stops gracefully.

**Does this work without a proxy?**

Yes — proxy is disabled by default. Enable `proxyConfiguration` only if you encounter persistent IP-based blocks.

---

## Running Locally

### Prerequisites

```bash
pip install apify-client playwright beautifulsoup4
playwright install firefox
```

### Input File

Create `storage/key_value_stores/default/INPUT.json`:

```json
{
  "usernames": ["elonmusk"],
  "maxTweets": 20
}
```

### Run

```bash
apify run
```

---

## Limitations

- Cannot access truly private accounts without being an authenticated follower
- Twitter's DOM structure may change and require updates to selectors
- Very high `maxTweets` values (300+) take significantly longer and carry higher block risk
- Engagement counts for very old tweets may differ slightly from the official API

---

## Legal & Compliance

This actor scrapes publicly available data. Always comply with [Twitter/X Terms of Service](https://twitter.com/en/tos) and applicable data protection regulations (GDPR, CCPA) when storing or processing scraped data.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/twitter-profile-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
