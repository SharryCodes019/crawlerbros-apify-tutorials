# Youtube Comment Scraper Tutorial: Run This Apify Actor with Python

Scrape YouTube video comments with full metadata. Extracts comment text, author info, likes, timestamps, pinned/hearted status, and reply threads. Supports sorting by Top comments or Newest first.

This repository shows how to run [Youtube Comment Scraper](https://apify.com/crawlerbros/youtube-comment-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/youtube-comment-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/youtube-comment-scraper](https://apify.com/crawlerbros/youtube-comment-scraper)
- **SEO title:** Youtube Comment Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape YouTube video comments with full metadata. Extracts comment text, author info, likes, timestamps, pinned/hearted status, and reply threads. Supports sorting by Top comments or Newest first.

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

# YouTube Comment Scraper

Scrape YouTube video comments with full metadata including author info, likes, timestamps, pinned/hearted status, and reply threads. Supports sorting by Top comments or Newest first.

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `videoUrls` | array | *required* | YouTube video URLs, short links (youtu.be), shorts URLs, or plain video IDs |
| `maxComments` | integer | 100 | Max top-level comments per video (1–50,000). Replies don't count toward this limit |
| `includeReplies` | boolean | true | Whether to fetch reply threads for each comment |
| `maxRepliesPerComment` | integer | 5 | Max replies to fetch per comment (0–100) |
| `sortBy` | string | "top" | Sort order: "top" (most relevant) or "newest" (chronological) |

### Supported URL Formats

- `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- `https://youtu.be/dQw4w9WgXcQ`
- `https://www.youtube.com/shorts/dQw4w9WgXcQ`
- `https://www.youtube.com/embed/dQw4w9WgXcQ`
- `https://www.youtube.com/live/dQw4w9WgXcQ`
- `dQw4w9WgXcQ` (bare video ID)

### Example Input

```json
{
    "videoUrls": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "maxComments": 100,
    "includeReplies": true,
    "maxRepliesPerComment": 5,
    "sortBy": "top"
}
```

## Output

Each row in the dataset is either a top-level comment (`replyDepth: 0`) or a reply (`replyDepth: 1`). Replies appear immediately after their parent comment.

| Field | Type | Description |
|-------|------|-------------|
| `commentId` | string | Unique comment identifier |
| `text` | string | Comment text content |
| `authorName` | string | Author's display name |
| `authorChannelId` | string | Author's YouTube channel ID |
| `authorChannelUrl` | string | Author's channel URL |
| `authorProfileImageUrl` | string | Author's profile image URL |
| `authorIsChannelOwner` | boolean | Whether the author is the video's channel owner |
| `likeCount` | integer | Number of likes on the comment |
| `replyCount` | integer | Number of replies (top-level comments only) |
| `publishedTimeText` | string | Relative publish time (e.g., "2 days ago") |
| `isHearted` | boolean | Whether the creator hearted this comment |
| `isPinned` | boolean | Whether this comment is pinned |
| `isReply` | boolean | Whether this is a reply (true) or top-level comment (false) |
| `parentCommentId` | string/null | Parent comment ID (replies only, null for top-level) |
| `replyDepth` | integer | 0 for top-level comments, 1 for replies |
| `videoId` | string | YouTube video ID |
| `videoUrl` | string | Full video URL |
| `videoTitle` | string | Video title |
| `videoChannelName` | string | Video channel name |
| `videoChannelId` | string | Video channel ID |
| `scrapedAt` | string | ISO 8601 timestamp of when the data was scraped |

### Example Output

```json
{
    "commentId": "UgxB...",
    "text": "Great video!",
    "authorName": "John Doe",
    "authorChannelId": "UCxxx...",
    "authorChannelUrl": "https://www.youtube.com/@johndoe",
    "authorProfileImageUrl": "https://yt3.ggpht.com/...",
    "authorIsChannelOwner": false,
    "likeCount": 42,
    "replyCount": 3,
    "publishedTimeText": "2 days ago",
    "isHearted": false,
    "isPinned": false,
    "isReply": false,
    "parentCommentId": null,
    "replyDepth": 0,
    "videoId": "dQw4w9WgXcQ",
    "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "videoTitle": "Rick Astley - Never Gonna Give You Up",
    "videoChannelName": "Rick Astley",
    "videoChannelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "scrapedAt": "2026-02-11T12:00:00.000000+00:00"
}
```

## Cost

- Average run: ~$0.01–0.05 per video (100 comments)
- Uses HTTP requests (no browser) for comment fetching, keeping costs low
- Reply fetching adds minimal cost per reply thread

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/youtube-comment-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
