# Instagram Keyword Search Scraper Tutorial: Run This Apify Actor with Python

Extract posts from Instagram keyword search results. Scrape post URLs, captions, usernames, media URLs, hashtags, engagement metrics, and more. Supports multiple keywords with anti-detection features.

This repository shows how to run [Instagram Keyword Search Scraper](https://apify.com/crawlerbros/instagram-keyword-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-keyword-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-keyword-search-scraper](https://apify.com/crawlerbros/instagram-keyword-search-scraper)
- **SEO title:** Instagram Keyword Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract posts from Instagram keyword search results. Scrape post URLs, captions, usernames, media URLs, hashtags, engagement metrics, and more. Supports multiple keywords with anti-detection features.

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

# Instagram Keyword Search Scraper

Search Instagram by keyword or hashtag and extract fully enriched post data — captions, engagement metrics, author details, tagged users, sponsor tags, and more. Supports single-word and multi-word queries, and each discovered post is enriched with the same level of detail as a direct post scrape.

## What this actor does

- **Keyword & hashtag search** — works for single-word (e.g. `travel`) and multi-word (e.g. `sunset photography`) queries via Instagram's search results
- **Full post enrichment** — every discovered post is enriched with complete details (captions, media, engagement, author info) via a multi-tier fallback so results stay complete even when one data source is incomplete
- **Author metadata** — nested author details including follower count and total post count, not just username
- **Sponsor & ad detection** — flags paid partnerships, ads, and sponsor tags when present
- **Age-gate detection** — posts behind an account-level age restriction are reported with a distinct status instead of failing silently
- **Multiple keywords per run** — process a batch of keywords or hashtags in a single run
- **Reliable** — built-in retry logic and automatic managed session rotation

## Authentication

This actor requires Instagram session cookies for the keyword search step (Instagram's search does not work for logged-out sessions). You can either:

1. **Paste your own cookies** — export from a logged-in browser session using a tool such as [Cookie-Editor](https://cookie-editor.cgagnier.ca/) and paste the JSON into the `cookies` field.
2. **Leave the cookies field blank** — the actor will automatically use a managed pool of shared Instagram sessions. This is the recommended option for most users.

Post enrichment (the second step, after posts are discovered) does not require cookies.

If your cookies expire mid-run, re-export them from your browser and restart the actor.

## Output per post record

**Always present**

- `input_keyword` — the keyword or hashtag that produced this post
- `post_url` — full URL to the Instagram post
- `shortcode` — the Instagram post shortcode
- `post_id` — Instagram's internal media ID
- `username` — the author's Instagram username
- `author_meta` — nested author details: `id`, `username`, `full_name`, `is_verified` (`true` if the account has a verified badge), `profile_pic_url`, `profile_url`, `followers`, `post_count`
- `caption` — the post caption text
- `hashtags` — hashtags extracted from the caption
- `mentions` — @mentions extracted from the caption
- `pub_date` — post creation time, ISO 8601 format
- `media_type` — one of `Photo`, `Video`, `Reel`, `Carousel`, or `IGTV`
- `media_count` — number of media items (greater than 1 for carousels)
- `thumbnail_url` — CDN URL of the thumbnail/display image
- `media_items` — per-item media details: `url` (CDN URL), `width`, `height`, and for videos `duration`, `has_audio`, `play_count`
- `likes_hidden` — `true` if the author has hidden the like count
- `comments_disabled` — `true` if comments are disabled on the post
- `tagged_users` — usernames tagged in the post
- `collaborators` — co-author/collaborator usernames
- `sponsor_tags` — usernames tagged as paid-partnership sponsors
- `status` — `success`, `not_found`, `age_restricted`, `error`, `blocked`, or `invalid_url`
- `scraped_at` — ISO 8601 timestamp of when the post was scraped

**Present only when available**

- `like_count` — number of likes (omitted when the author has hidden likes)
- `comment_count` — number of comments
- `is_paid_partnership` — `true` if the post is marked as a paid partnership
- `is_ad` — `true` if the post is a sponsored ad
- `caption_is_edited` — `true` if the caption was edited after posting
- `location` — tagged location: `name`, `id`, `lat`, `lng` (present only if a location is tagged)
- `music` — attached audio/music info such as `artist`, `title`, `audio_id` (present only on Reels with attached audio)

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `keywords` | array | required | List of keywords or hashtags to search. Works for single-word and multi-word queries. |
| `maxPosts` | integer | `100` | Maximum number of posts to collect per keyword. Max `10000` |
| `cookies` | string | — | Instagram authentication cookies (JSON array). Leave blank to use the managed session pool |
| `sessionName` | string | — | Name for saving/loading cookies between runs. Use different names for different Instagram accounts |

### Example: search a single keyword

```json
{
  "keywords": ["travel"],
  "maxPosts": 100
}
```

### Example: multiple keywords and hashtags

```json
{
  "keywords": ["sunset photography", "streetfood", "#nature"],
  "maxPosts": 50
}
```

### Example: full crawl with your own cookies

```json
{
  "keywords": ["architecture"],
  "maxPosts": 0,
  "cookies": "[{\"name\":\"sessionid\",\"value\":\"YOUR_SESSION_ID\",\"domain\":\".instagram.com\"}]",
  "sessionName": "my_instagram_session"
}
```

## Example output

```json
{
  "input_keyword": "travel",
  "post_url": "https://www.instagram.com/p/ABC123/",
  "shortcode": "ABC123",
  "post_id": "3711296250294340356",
  "username": "john_travels",
  "author_meta": {
    "id": "123456789",
    "username": "john_travels",
    "full_name": "John Smith",
    "is_verified": false,
    "profile_pic_url": "https://scontent.cdninstagram.com/v/example.jpg",
    "profile_url": "https://www.instagram.com/john_travels/",
    "followers": 12500,
    "post_count": 340
  },
  "caption": "Exploring the streets of Lisbon #travel #portugal",
  "hashtags": ["travel", "portugal"],
  "mentions": [],
  "pub_date": "2024-11-15T14:23:10+00:00",
  "media_type": "Photo",
  "media_count": 1,
  "thumbnail_url": "https://scontent.cdninstagram.com/v/example-thumb.jpg",
  "media_items": [
    {
      "index": 0,
      "type": "Photo",
      "url": "https://scontent.cdninstagram.com/v/example-full.jpg",
      "width": 1080,
      "height": 1350
    }
  ],
  "like_count": 1842,
  "comment_count": 34,
  "likes_hidden": false,
  "comments_disabled": false,
  "tagged_users": [],
  "collaborators": [],
  "sponsor_tags": [],
  "is_paid_partnership": false,
  "is_ad": false,
  "status": "success",
  "scraped_at": "2026-07-03T10:00:00+00:00"
}
```

## Use cases

- **Trend monitoring** — track how a hashtag or topic is trending in real time across Instagram
- **Competitor content research** — see what content ranks for keywords relevant to your industry
- **Influencer discovery** — find accounts posting popular content around a niche keyword
- **Sponsored content tracking** — identify paid partnerships and ads surfaced for a given keyword
- **Content inspiration** — pull top-performing posts for a topic to inform your own content strategy
- **Market research** — analyze caption language, hashtag usage, and engagement patterns by keyword
- **Brand mention tracking** — search branded keywords to see how creators are covering your product
- **Dataset building** — collect labeled post data by topic for downstream analysis or ML pipelines

## FAQ

**Do I need an Instagram account to use this actor?**
No. Keyword search uses a managed pool of shared Instagram sessions by default, so you don't need to provide your own account. You can optionally paste your own cookies for the search step if you prefer.

**Will this work on private accounts?**
No. Only posts from public accounts appear in Instagram's search results and can be scraped.

**How many posts can I scrape per keyword?**
Up to 10,000 posts per keyword. The actor paginates through Instagram's search results automatically, and safely stops early if a keyword runs out of unique posts before reaching that limit.

**What does the `status` field mean?**
`success` — the post was fully enriched. `not_found` — the post was deleted or private. `age_restricted` — the post is behind an account-level age gate. `error`/`blocked` — enrichment failed after retries. `invalid_url` — the discovered URL didn't match Instagram's post URL format.

**How fresh is the data?**
Data is scraped live at the time of the run. Post details reflect the current state of Instagram at the moment of scraping.

**Is this actor affiliated with Instagram or Meta?**
No. This is an independent third-party tool that automates interaction with the public Instagram website. It is not endorsed by or affiliated with Meta Platforms, Inc.

## Other Instagram Scrapers

Want to get other data from Instagram? Check out our complete suite of Instagram scrapers:

| Actor | Description |
|---|---|
| [Instagram Post Scraper](https://apify.com/crawlerbros/instagram-post-scraper) | Scrape public posts, reels, IGTV, and carousel posts from direct URLs — no login or cookies required |
| [Instagram Comment Scraper](https://apify.com/crawlerbros/instagram-comment-scraper) | Scrape comments from any Instagram post or reel |
| [Instagram Profile Scraper](https://apify.com/crawlerbros/instagram-profile-scraper) | Extract profile data, bio, follower counts, and more |
| [Instagram Followers & Following Scraper](https://apify.com/crawlerbros/instagram-follower-scraper) | Scrape followers and following lists from any profile |
| [Instagram Tagged Posts Scraper](https://apify.com/crawlerbros/instagram-tagged-posts-scraper) | Collect posts where a user has been tagged |
| [Instagram Hashtag Scraper](https://apify.com/crawlerbros/instagram-hashtag-scraper) | Scrape posts and profiles by hashtag |
| [Instagram Story Downloader](https://apify.com/crawlerbros/instagram-story-downloader) | Download stories from Instagram profiles |
| [Instagram Downloader API](https://apify.com/crawlerbros/instagram-downloader-api) | Download photos, videos, and reels from Instagram |
| [Instagram Keyword Scraper](https://apify.com/crawlerbros/instagram-keyword-scraper) | Search and scrape posts by keyword |
| [Instagram Transcript Scraper](https://apify.com/crawlerbros/instagram-transcript-scraper) | Extract transcripts from Instagram video content |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-keyword-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
