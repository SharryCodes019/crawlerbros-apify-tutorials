# Tiktok Comments Scraper Tutorial: Run This Apify Actor with Python

Scrape comments from TikTok videos. Extract comment text, user ID, timestamp, number of replies and replies content, number of likes, and more. Input video URLs or usernames to get all comments.

This repository shows how to run [Tiktok Comments Scraper](https://apify.com/crawlerbros/tiktok-comments-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-comments-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-comments-scraper](https://apify.com/crawlerbros/tiktok-comments-scraper)
- **SEO title:** Tiktok Comments Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape comments from TikTok videos. Extract comment text, user ID, timestamp, number of replies and replies content, number of likes, and more. Input video URLs or usernames to get all comments.

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

# TikTok Comments Scraper

Extract all comments and replies from any TikTok video. The actor intercepts TikTok's `/api/comment/list/` endpoint and paginates through all comment pages, then fetches reply threads for each root comment. Returns one dataset row per comment or reply. No TikTok account or cookies required.

## What this actor does

- Accepts TikTok video URLs and/or numeric post IDs
- Paginates through all comment pages using TikTok's official comment API
- Fetches reply threads for each root comment (up to 19 inline, with additional pages via reply endpoint)
- Identifies pinned comments and comments hearted by the video author
- Captures commenter avatars, verification status, and user IDs
- Parses image attachments on comments where present
- Empty fields are omitted

## Output per comment

- `commentId` — unique comment ID
- `postId` — ID of the video this comment belongs to
- `postUrl` — URL of the video
- `text` — full comment text
- `createTime` — Unix timestamp when the comment was posted
- `createdAt` — ISO 8601 creation date
- `likeCount` — number of likes on the comment
- `replyCount` — total number of replies to this comment
- `isPinnedByAuthor` — whether the video creator pinned this comment
- `isLikedByAuthor` — whether the video creator hearted this comment
- `isReply` — `true` for reply comments; `false` for root comments
- `replyToCommentId` — parent comment ID (reply rows only)
- `user.id` — commenter's TikTok user ID
- `user.secUid` — commenter's secUid
- `user.username` — commenter's @handle
- `user.displayName` — commenter's display name
- `user.avatarUrl` — commenter's avatar image URL
- `images` — array of image URLs if the comment contains image attachments
- `language` — detected language code of the comment text
- `scrapedAt` — ISO 8601 timestamp when the record was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `postUrls` | array | — | TikTok video URLs to scrape comments from |
| `postIds` | array | — | Numeric post IDs (15–20 digit strings) as alternative to URLs |
| `maxCommentsPerPost` | integer | `100` | Maximum comment rows per video (includes replies when enabled) |
| `includeReplies` | boolean | `true` | Fetch and flatten reply threads into the dataset |
| `requestDelaySecs` | number | `2` | Seconds to wait between API requests |
| `maxRetries` | integer | `3` | Maximum retry attempts per post on failure |

### Example: Scrape top comments from a viral video

```json
{
  "postUrls": ["https://www.tiktok.com/@khaby.lame/video/7574844184952081686"],
  "maxCommentsPerPost": 50,
  "includeReplies": true
}
```

### Example: Comments only — skip replies

```json
{
  "postUrls": ["https://www.tiktok.com/@natgeo/video/7640880319159094559"],
  "maxCommentsPerPost": 200,
  "includeReplies": false
}
```

### Example: Multiple videos by post ID

```json
{
  "postIds": ["7574844184952081686", "7640880319159094559"],
  "maxCommentsPerPost": 100,
  "includeReplies": true
}
```

### Example: High-volume comment extraction

```json
{
  "postUrls": [
    "https://www.tiktok.com/@khaby.lame/video/7574844184952081686"
  ],
  "maxCommentsPerPost": 2000,
  "includeReplies": true,
  "requestDelaySecs": 3
}
```

## Use cases

- **Sentiment analysis** — classify audience reactions to a campaign video, product launch, or brand moment
- **Community research** — identify recurring themes, questions, and pain points in a creator's comment section
- **Influencer vetting** — evaluate comment quality and authenticity before committing to a sponsorship deal
- **Crisis monitoring** — rapidly scan high-volume comment threads during a brand PR event
- **Content moderation** — export comment datasets for policy review or third-party moderation tools
- **Academic research** — build annotated comment corpora for NLP and social media studies

## FAQ

**Do I need a TikTok account or cookies?**
No. TikTok's comment API is publicly accessible. No login is required.

**Does `maxCommentsPerPost` include replies?**
Yes. Both root comments and their replies count toward the limit when `includeReplies` is `true`. To collect only root comments, set `includeReplies` to `false`.

**What is the maximum number of comments I can collect?**
Up to 10,000 per video. TikTok's comment API paginates in batches of 20.

**How are replies structured in the output?**
Each reply is a flat dataset row with `isReply: true` and `replyToCommentId` set to the parent comment's ID. Replies are not nested inside root comment objects.

**What does `isPinnedByAuthor` mean?**
When the video creator manually pins a comment to the top of the comment section, `isPinnedByAuthor` is `true` for that comment.

**What does `isLikedByAuthor` mean?**
When the video creator taps the heart icon on a comment, `isLikedByAuthor` is `true`. This is also called a "creator heart" or "hearted comment."

**Can I scrape comments from private videos?**
No. Private videos are not accessible via TikTok's public API. Only comments on public videos can be collected.

**What does `requestDelaySecs` do?**
It controls the pause between paginated API calls. The default of 2 seconds is sufficient for most runs. Increasing this value reduces the chance of temporary rate limiting on very large extractions.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
| TikTok Post Scraper | https://apify.com/crawlerbros/tiktok-post-scraper |
| TikTok Profile Scraper | https://apify.com/crawlerbros/tiktok-profile-scraper |
| TikTok Search Scraper | https://apify.com/crawlerbros/tiktok-search-scraper |
| TikTok Hashtag Scraper | https://apify.com/crawlerbros/tiktok-hashtag-scraper |
| TikTok Music Scraper | https://apify.com/crawlerbros/tiktok-music-scraper |
| TikTok Transcript Scraper | https://apify.com/crawlerbros/tiktok-transcript-scraper |
| TikTok Followers Scraper | https://apify.com/crawlerbros/tiktok-followers-scraper |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-comments-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
