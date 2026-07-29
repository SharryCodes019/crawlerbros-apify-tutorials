# Instagram Post Scraper Tutorial: Run This Apify Actor with Python

Scrape public Instagram posts, reels, IGTV and carousel posts from direct URLs with no login, no cookies, no browser required. Supply a list of Instagram links and receive a structured dataset with author details, caption, media URLs, engagement counts, publish date, music, location, and more.

This repository shows how to run [Instagram Post Scraper](https://apify.com/crawlerbros/instagram-post-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-post-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-post-scraper](https://apify.com/crawlerbros/instagram-post-scraper)
- **SEO title:** Instagram Post Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public Instagram posts, reels, IGTV and carousel posts from direct URLs with no login, no cookies, no browser required. Supply a list of Instagram links and receive a structured dataset with author details, caption, media URLs, engagement counts, publish date, music, location, and more.

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

# Instagram Post Scraper

Scrape public Instagram posts, reels, IGTV and carousel posts from direct URLs — no login, no cookies, no browser required. Supply a list of Instagram links (`/p/`, `/reel/`, `/reels/`, `/tv/`, or the canonical `username/p/shortcode` format) and receive a structured dataset with author details, caption, media URLs, engagement counts, publish date, music, location, and more. Handles batches of 10,000 URLs per run with per-IP proxy rotation that keeps pace fast even under rate limiting.

## What this actor does

- **Scrape posts by URL** — accepts any mix of `/p/`, `/reel/`, `/reels/`, `/tv/`, and canonical `username/p/shortcode` links in a single run
- **Full media extraction** — returns direct CDN URLs for every photo, video, reel and carousel item, including per-item resolution and duration
- **Rich author data** — username, display name, verified status, and profile picture URL
- **Engagement metrics** — like count, comment count, per-item video duration, and whether likes are publicly hidden
- **Captions, hashtags, and mentions** — caption text parsed with hashtags and @mentions extracted as separate arrays
- **Location and music** — tagged location (name, coordinates) and reel music (artist, title, audio ID) when present
- **Status tracking** — every input URL produces a record; inaccessible, deleted, age-restricted, and invalid URLs each carry a clear `status` value so no URL is silently lost
- **Scale without blocks** — per-IP cooldown with exponential back-off, automatic slot recycling, and UUID-prefixed sessions that guarantee fresh IPs on every run

## Output per post record

**Always present**

- `status` — scrape outcome: `success`, `not_found`, `age_restricted`, `invalid_url`, `error`, or `blocked` (see Status values section below)
- `post_url` — full Instagram post URL (`https://www.instagram.com/p/{shortcode}/`)

Records with any `status` other than `success` contain only these two fields — no other keys are present.

**Present on successfully scraped posts (`status: success`)**

- `shortcode` — the post's unique shortcode identifier
- `scraped_at` — ISO 8601 timestamp of when the record was scraped, UTC (no `+00:00` suffix)
- `post_id` — Instagram's internal numeric post ID
- `username` — author's Instagram username (also included in `author_meta` below)
- `author_meta` — object with the author's `id`, `username`, `full_name`, `is_verified`, `profile_pic_url`, `profile_url`, `followers`, and `post_count`
- `pub_date` — ISO 8601 publish timestamp, UTC (no `+00:00` suffix)
- `media_type` — one of `Photo`, `Video`, `Reel`, `IGTV`, or `Carousel`
- `media_count` — number of media items (always `1` except for carousels)
- `thumbnail_url` — CDN URL of the post thumbnail image
- `like_count` — number of likes (`null` when `likes_hidden` is `true`)
- `comment_count` — number of comments
- `likes_hidden` — `true` if the author has hidden like counts, `false` otherwise
- `comments_disabled` — `true` if comments are turned off on the post, `false` otherwise
- `caption` — full caption text (empty string `""` when there is no caption)
- `hashtags` — array of hashtags found in the caption (empty array `[]` when none)
- `mentions` — array of @mentioned usernames in the caption (empty array when none)
- `tagged_users` — array of usernames tagged in the post media (empty array when none)
- `collaborators` — array of co-author usernames (empty array when none)
- `media_items` — array of per-item objects, each with `index`, `type`, `url`, `width`, `height`. Single-item array for photos, videos, reels, and IGTV; multi-item array for carousels. Video items also include `duration` (seconds), `has_audio`, and `play_count`

**Present only when location is tagged**

- `location` — object with `name`, `id`, `slug`, `lat`, `lng`

**Present only for reels with music attribution**

- `music` — object with `artist`, `title`, `audio_id`, `is_trending`

**Present only for posts with accessibility captions**

- `accessibility_caption` — auto-generated accessibility description of the image

## Status values

Every input URL — whether valid or not — produces exactly one output record with a `status` field:

| Status | Meaning |
|---|---|
| `success` | Post scraped successfully; all fields populated |
| `age_restricted` | Post is gated behind Instagram's age/login wall |
| `not_found` | Post is deleted or otherwise nonexistent |
| `invalid_url` | The URL is not a recognisable Instagram post link |
| `error` | Unexpected failure after all retry attempts |
| `blocked` | All proxy IPs were exhausted before the post could be fetched |

### Age-restricted content

Instagram age-gates some posts, either at the post level (alcohol brands, adult content) or at the account level (accounts with a minimum-age setting, e.g. "People under 18 can't see this content"). Both cases render an identical, generic error page on the logged-out post HTML — indistinguishable from a deleted post — but Instagram's public oEmbed API exposes the real reason (`400 geoblock_required` for a gated post vs `404` for a deleted one), so the scraper checks that endpoint as a last resort and reports `status: "age_restricted"` for either kind of gate. This cannot be bypassed without an authenticated session, so no further post data is returned for these posts.

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `post_urls` | array | yes | Instagram post, reel, or IGTV URLs. Accepts `/p/`, `/reel/`, `/reels/`, `/tv/`, and `username/p/shortcode` formats. Duplicates are silently de-duplicated. Up to 10,000 URLs per run |

### Example: scrape a single post

```json
{
  "post_urls": [
    "https://www.instagram.com/p/DUtk38cj2TA/"
  ]
}
```

### Example: mixed batch of posts, reels, and canonical URLs

```json
{
  "post_urls": [
    "https://www.instagram.com/p/DUtk38cj2TA/",
    "https://www.instagram.com/reel/C9uzjsSpHJC/",
    "https://www.instagram.com/leomessi/p/DZifppZj_cB/",
    "https://www.instagram.com/tv/CQa7HaGlRPD/"
  ]
}
```

### Example: large batch

```json
{
  "post_urls": [
    "https://www.instagram.com/p/DUtk38cj2TA/",
    "... (up to 10,000 URLs)"
  ]
}
```

## Example output

```json
{
  "status": "success",
  "post_url": "https://www.instagram.com/p/DUtk38cj2TA/",
  "shortcode": "DUtk38cj2TA",
  "post_id": "3672810928374650123",
  "username": "natgeo",
  "author_meta": {
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "is_verified": true,
    "profile_pic_url": "https://scontent.cdninstagram.com/v/...",
    "profile_url": "https://www.instagram.com/natgeo/",
    "followers": 284000000,
    "post_count": 32400
  },
  "caption": "The ancient forest at dawn. #nature #wildlife #photography",
  "hashtags": ["nature", "wildlife", "photography"],
  "mentions": [],
  "pub_date": "2025-11-12T08:30:00",
  "media_type": "Photo",
  "media_count": 1,
  "media_items": [
    { "index": 1, "type": "Photo", "url": "https://scontent.cdninstagram.com/v/...jpg", "width": 1080, "height": 1350 }
  ],
  "thumbnail_url": "https://scontent.cdninstagram.com/v/...jpg",
  "like_count": 482910,
  "comment_count": 3204,
  "likes_hidden": false,
  "comments_disabled": false,
  "tagged_users": [],
  "collaborators": [],
  "scraped_at": "2025-11-12T09:14:33.421000"
}
```

Records for inaccessible or invalid URLs carry only `status` and `post_url` — no other keys are present:

```json
{ "status": "not_found",      "post_url": "https://www.instagram.com/p/DELETED123/" }
{ "status": "age_restricted", "post_url": "https://www.instagram.com/p/DLAIK1ayfg3/" }
{ "status": "invalid_url",    "post_url": "https://www.google.com/" }
```

## Age-restricted and private content

Instagram does not expose age-gated content through its anonymous API. Any gated post — whether gated at the post level (alcohol brands, adult content) or at the account level (accounts restricted to viewers of a minimum age) — returns `status: "age_restricted"` instead of a data record. Private account posts and deleted posts both return `status: "not_found"`. This is a server-side restriction enforced by Instagram and cannot be bypassed without authenticated session cookies.

| Content type | `status` | Data returned |
|---|---|---|
| Public post | `success` | All fields |
| Deleted post | `not_found` | `status`, `post_url` only |
| Private post | `not_found` | `status`, `post_url` only |
| Age-restricted post (post-level or account-level) | `age_restricted` | `status`, `post_url` only |
| Invalid URL format | `invalid_url` | `status`, `post_url` only |

## Use cases

- **Competitor content analysis** — track post frequency, engagement rates, media types and captions across competitor accounts to benchmark your own content strategy
- **Influencer vetting** — verify follower counts, engagement ratios and posting history before signing a partnership deal
- **Brand monitoring** — collect all posts tagged with your brand name or product from any source URL and feed them into a monitoring dashboard
- **Social media archiving** — create a permanent structured archive of a campaign's posts before content is deleted or made private
- **Research and journalism** — gather public post metadata at scale for academic studies on misinformation, trends, or audience behaviour
- **Content repurposing** — extract caption text and media URLs from your own posts to migrate or republish content across platforms
- **Hashtag performance tracking** — scrape posts sharing a known hashtag to measure reach and identify top-performing formats
- **E-commerce product research** — collect posts from brand accounts to analyse product launches, promotions and customer response

## FAQ

**Do I need an Instagram account or cookies to use this actor?**
No. This actor scrapes public posts anonymously without any login, cookies, or account credentials. No authentication is required for publicly accessible content.

**Why do some posts return `status: "not_found"`?**
A `not_found` status means Instagram's API returned no data for that URL. This happens when a post has been deleted or made private. These are server-side restrictions that cannot be bypassed without an authenticated session.

**Why do some posts return `status: "age_restricted"`?**
An `age_restricted` status means Instagram gated the post behind an age/login wall, either at the post level (e.g. alcohol brands, adult content) or at the account level (accounts with a minimum-age setting). Both are detectable from Instagram's server response even without a login session, but cannot be bypassed without one.

**Why is `like_count` null on some posts?**
When an author hides their like counts, Instagram does not return the figure in the API response. The record will have `likes_hidden: true` and `like_count: null`.

**How many URLs can I submit in one run?**
Up to 10,000 URLs per run. The actor automatically uses residential proxies with per-IP session rotation to handle large batches reliably — no proxy configuration is required on your end.

**How fresh is the data?**
Data is scraped live at the time of the run. Post metadata reflects the current state of Instagram at the moment of scraping — including the latest like and comment counts.

**What URL formats are supported?**
The actor accepts `/p/`, `/reel/`, `/reels/`, and `/tv/` links, as well as canonical `username/p/shortcode` URLs (e.g. `https://www.instagram.com/natgeo/p/DUtk38cj2TA/`). Duplicate URLs pointing to the same post are automatically de-duplicated.

**Is this actor affiliated with Instagram or Meta?**
No. This is an independent third-party tool that automates interaction with the public Instagram website. It is not endorsed by or affiliated with Meta Platforms, Inc.

## Other Instagram Scrapers

Want to get other data from Instagram? Check out our complete suite of Instagram scrapers:

| Actor | Description |
|---|---|
| [Instagram Comment Scraper](https://apify.com/crawlerbros/instagram-comment-scraper) | Scrape comments from any Instagram post or reel |
| [Instagram Profile Scraper](https://apify.com/crawlerbros/instagram-profile-scraper) | Extract profile data, bio, follower counts, and more |
| [Instagram Followers & Following Scraper](https://apify.com/crawlerbros/instagram-follower-scraper) | Scrape followers and following lists from any profile |
| [Instagram Tagged Posts Scraper](https://apify.com/crawlerbros/instagram-tagged-posts-scraper) | Collect posts where a user has been tagged |
| [Instagram Hashtag Scraper](https://apify.com/crawlerbros/instagram-hashtag-scraper) | Scrape posts and profiles by hashtag |
| [Instagram Story Downloader](https://apify.com/crawlerbros/instagram-story-downloader) | Download stories from Instagram profiles |
| [Instagram Downloader API](https://apify.com/crawlerbros/instagram-downloader-api) | Download photos, videos, and reels from Instagram |
| [Instagram Keyword Scraper](https://apify.com/crawlerbros/instagram-keyword-scraper) | Search and scrape posts by keyword |
| [Instagram Keyword Search Scraper](https://apify.com/crawlerbros/instagram-keyword-search-scraper) | Search Instagram accounts and posts by keyword |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-post-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
