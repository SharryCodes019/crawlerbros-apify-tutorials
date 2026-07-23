# Facebook Comments Scraper Tutorial: Run This Apify Actor with Python

Scrape public comments from Facebook posts, Watch videos, and photo stories. Extract comment text, author info, reactions, timestamps, and nested replies via GraphQL pagination.

This repository shows how to run [Facebook Comments Scraper](https://apify.com/crawlerbros/facebook-comments-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-comments-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-comments-scraper](https://apify.com/crawlerbros/facebook-comments-scraper)
- **SEO title:** Facebook Comments Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public comments from Facebook posts, Watch videos, and photo stories. Extract comment text, author info, reactions, timestamps, and nested replies via GraphQL pagination.

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

# Facebook Comments Scraper

Extract public comments from Facebook posts, Reels, Watch videos, and photo stories. Get comment text, author info, reactions, timestamps, and nested reply threads — no login or cookies required.

## Features

- Scrape comments from any public Facebook post, Watch video, or page video
- Support for group posts, shared posts, and page video URLs
- Three comment sorting modes: All, Newest, or Most Relevant
- Nested reply extraction with full parent/reply threading metadata
- Author details: name, profile picture, profile URL, ID
- Reaction counts and reply counts per comment
- ISO 8601 timestamps
- Anti-blocking: headless Chromium browser, residential proxy support, request delays
- Export to JSON, CSV, Excel, or XML

## Input

| Field                   | Type     | Required | Default     | Description                                                                                                       |
| ----------------------- | -------- | -------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| Start URLs              | string[] | Yes      | —           | Facebook post, Reel, Watch, or photo URLs to scrape comments from                                                 |
| Max items per URL       | integer  | No       | 100         | Maximum number of comments to collect per URL                                                                     |
| Comments mode           | string   | No       | ALL         | Sort order: `ALL` (chronological), `NEWEST` (reverse chronological), or `MOST_RELEVANT` (Facebook's ranked order) |
| Include nested comments | boolean  | No       | true        | Also scrape reply threads under top-level comments                                                                |
| Max request retries     | integer  | No       | 3           | Number of retries per failed request                                                                              |
| Proxy Configuration     | object   | No       | Residential | Proxy settings. Residential IPs strongly recommended                                                              |

### Supported URL Formats

- **Posts**: `https://www.facebook.com/PageName/posts/1234567890`
- **Posts (pfbid)**: `https://www.facebook.com/PageName/posts/pfbid0...`
- **Reels**: `https://www.facebook.com/reel/1234567890` *(requires login — not supported)*
- **Watch videos**: `https://www.facebook.com/watch?v=1234567890`
- **Photos**: `https://www.facebook.com/photo?fbid=1234567890`
- **Photo (legacy)**: `https://www.facebook.com/photo.php?fbid=1234567890`
- **Group posts**: `https://www.facebook.com/groups/groupname/permalink/1234567890/`
- **Page videos**: `https://www.facebook.com/PageName/videos/1234567890`
- **Shared posts**: `https://www.facebook.com/share/p/abc123/`

### Example Input

```json
{
  "startUrls": [
    { "url": "https://www.facebook.com/NASA/posts/1234567890" },
    { "url": "https://www.facebook.com/reel/9876543210" }
  ],
  "maxItems": 200,
  "commentsMode": "MOST_RELEVANT",
  "includeNestedComments": true,
  "proxy": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## Output

Each comment record contains the following fields:

| Field              | Type    | Description                                                      |
| ------------------ | ------- | ---------------------------------------------------------------- |
| `facebookUrl`      | string  | Canonical URL of the post                                        |
| `commentUrl`       | string  | Direct permalink to the comment                                  |
| `commentId`        | string  | Legacy numeric comment ID                                        |
| `id`               | string  | Internal relay ID                                                |
| `feedbackId`       | string  | Feedback ID for the comment                                      |
| `date`             | string  | Comment timestamp (ISO 8601)                                     |
| `text`             | string  | Full comment text                                                |
| `profilePicture`   | string  | Author's profile picture URL                                     |
| `profileId`        | string  | Author's numeric profile ID                                      |
| `profileName`      | string  | Author's display name                                            |
| `profileUrl`       | string  | Author's profile URL                                             |
| `likesCount`       | integer | Number of reactions on the comment                               |
| `threadingDepth`   | integer | 0 = top-level comment, 1+ = reply depth                         |
| `commentsCount`    | integer | Number of replies (0 for replies themselves)                     |
| `facebookId`       | string  | Post/story ID                                                    |
| `inputUrl`         | string  | Original URL provided in input                                   |
| `replyToCommentId` | string  | Parent comment legacy ID (empty string for top-level comments)   |
| `postTitle`        | string  | Post title extracted from page metadata (empty if not available) |

### Example Output

**Top-level comment:**

```json
{
  "facebookUrl": "https://www.facebook.com/NASA/posts/pfbid025kwyoB...",
  "commentUrl": "https://www.facebook.com/NASA/posts/pfbid025kwyoB...?comment_id=809453025548580",
  "commentId": "809453025548580",
  "id": "Y29tbWVudDoxNDg3...",
  "feedbackId": "ZmVlZGJhY2s6MTQ4...",
  "date": "2026-03-26T23:31:17.000Z",
  "text": "Ah I remember the moon landing of 1969 on the eve of my 9th birthday!",
  "profilePicture": "https://scontent.xx.fbcdn.net/v/...",
  "profileId": "pfbid0248UufsteCx...",
  "profileName": "Gwen Weidell",
  "profileUrl": "https://www.facebook.com/gwen.weidell.9",
  "likesCount": 26,
  "threadingDepth": 0,
  "commentsCount": 2,
  "replyToCommentId": "",
  "facebookId": "1487017912793580",
  "inputUrl": "https://www.facebook.com/NASA/posts/pfbid025kwyoB...",
  "postTitle": "Our Artemis II crew will be the first to fly around the Moon in more than 50 years..."
}
```

**Reply to a comment (threadingDepth 1):**

```json
{
  "facebookUrl": "https://www.facebook.com/NASA/posts/pfbid025kwyoB...",
  "commentUrl": "https://www.facebook.com/NASA/posts/pfbid025kwyoB...?comment_id=810234567890123",
  "commentId": "810234567890123",
  "id": "Y29tbWVudDo4MDk0...",
  "feedbackId": "ZmVlZGJhY2s6ODA5...",
  "date": "2026-03-26T15:10:22.000Z",
  "text": "Totally agree with you!",
  "profilePicture": "https://scontent.xx.fbcdn.net/v/...",
  "profileId": "100012345678901",
  "profileName": "John Doe",
  "profileUrl": "https://www.facebook.com/john.doe",
  "likesCount": 2,
  "threadingDepth": 1,
  "commentsCount": 0,
  "replyToCommentId": "809453025548580",
  "facebookId": "1487017912793580",
  "inputUrl": "https://www.facebook.com/NASA/posts/pfbid025kwyoB...",
  "postTitle": "Our Artemis II crew will be the first to fly around the Moon in more than 50 years..."
}
```

## Use Cases

- **Brand monitoring** — Track what people say about your brand on Facebook posts
- **Market research** — Analyze audience sentiment and topics in post comments
- **Content analysis** — Study engagement patterns across different types of posts
- **Community insights** — Understand audience reactions to news, announcements, or campaigns
- **Competitor analysis** — Monitor comments on competitor pages and posts
- **Lead generation** — Identify engaged users from comment activity

## Tips for Best Results

1. **Use residential proxies** — Facebook blocks datacenter IPs aggressively. Select "Residential" proxy group for best results
2. **Start with fewer URLs** — Test with 1-2 URLs first, then scale up
3. **Public posts only** — The scraper can only access comments on public posts accessible without login
4. **Comment limits** — Set `maxItems` per URL to control costs and runtime. Each URL fetches up to the specified limit

## Limitations

- Only public posts are supported. Private, friends-only, or restricted posts cannot be accessed
- **Reels require Facebook login** — Reels (`/reel/` URLs) are not accessible without a Facebook session. Use post or video URLs instead
- **Video URLs need residential proxy** on Apify — Facebook blocks video pages from datacenter IPs. Standard posts work without proxy
- Facebook may occasionally block requests — use residential proxies and keep concurrency low
- Comment ordering depends on Facebook's API. The `MOST_RELEVANT` mode uses Facebook's own ranking algorithm
- Some older posts may have limited data availability
- Nested reply depth is limited to what Facebook's API returns (typically 1-2 levels)

## FAQ

**Q: Do I need a Facebook account or cookies to use this scraper?**
A: No. The scraper works with public posts and videos without any login or authentication. The only exception is Reels, which Facebook requires login to access.

**Q: Can I scrape comments from Facebook Reels?**
A: No. Facebook Reels require login to view, which this scraper does not support. Use the post URL or video URL format instead.

**Q: Why are some comments missing?**
A: Facebook may restrict access to certain comments based on privacy settings, regional blocking, or content moderation. Only publicly visible comments can be scraped.

**Q: What happens if Facebook blocks my requests?**
A: The scraper includes automatic retry logic and uses a headless Chromium browser to bypass anti-bot protections. Using residential proxies significantly reduces blocking. If you still experience issues, try spacing out your runs.

**Q: Can I scrape comments from private groups?**
A: No. Only public group posts where comments are visible without login can be scraped.

**Q: How does the comment sorting work?**
A: `ALL` returns comments in chronological order (oldest first), `NEWEST` returns newest first, and `MOST_RELEVANT` uses Facebook's ranking algorithm which prioritizes popular and engaging comments.

**Q: What is `threadingDepth`?**
A: It indicates the nesting level. `0` means it's a top-level comment directly on the post. `1` means it's a reply to a top-level comment. Higher values indicate deeper nesting.

**Q: How many comments can I scrape per run?**
A: You can set `maxItems` up to 10,000 per URL. The actual number depends on how many public comments exist on the post.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-comments-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
