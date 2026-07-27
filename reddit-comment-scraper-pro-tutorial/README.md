# Reddit Comment Scraper Pro Tutorial: Run This Apify Actor with Python

Scrape comments from any Reddit post with advanced filters (minScore, maxDepth, excludeDeleted, authorFilter, keywordFilter) and rich per-comment fields: awards, gildedCount, controversiality, repliesCount, parentCommentId, body, bodyHtml, subreddit, permalink. No login required.

This repository shows how to run [Reddit Comment Scraper Pro](https://apify.com/crawlerbros/reddit-comment-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/reddit-comment-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/reddit-comment-scraper-pro](https://apify.com/crawlerbros/reddit-comment-scraper-pro)
- **SEO title:** Reddit Comment Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Scrape comments from any Reddit post with advanced filters (minScore, maxDepth, excludeDeleted, authorFilter, keywordFilter) and rich per-comment fields: awards, gildedCount, controversiality, repliesCount, parentCommentId, body, bodyHtml, subreddit, permalink. No login required.

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

# Reddit Comment Scraper

An Apify Actor for scraping comments from Reddit posts using browser automation with Playwright.

## Features

- 💬 Scrape comments from multiple Reddit posts
- 📊 Extract comprehensive comment data (text, author, score, timestamps, etc.)
- 🔄 Automatically expand collapsed threads and "load more" sections
- 🌳 Capture nested comment structure with depth levels
- 📦 No authentication required for public posts
- 💾 Data saved in structured JSON format
- 🌐 Browser automation bypasses API restrictions

## Input Parameters

The actor accepts the following input parameters:

| Parameter       | Type    | Required | Default | Description                                                     |
| --------------- | ------- | -------- | ------- | --------------------------------------------------------------- |
| `postUrls`      | array   | Yes      | -       | List of Reddit post URLs to scrape comments from                |
| `maxComments`   | integer | No       | `100`   | Maximum number of comments to scrape from each post (1-10000)   |
| `expandThreads` | boolean | No       | `true`  | Automatically expand collapsed threads and "load more" sections |

### Example Input

```json
{
  "postUrls": [
    "https://www.reddit.com/r/programming/comments/1abc123/interesting_discussion/",
    "https://old.reddit.com/r/python/comments/1def456/another_post/"
  ],
  "maxComments": 200,
  "expandThreads": true
}
```

## Output Fields

The actor extracts the following data for each comment:

### Comment Information

- `comment_id` - Unique comment ID (e.g., "abc123xyz")
- `comment_name` - Full comment name in Reddit format (e.g., "t1_abc123xyz")
- `author` - Username of the comment author (or "[deleted]")
- `text` - Full comment text/content

### Engagement Metrics

- `score` - Comment score/karma (upvotes minus downvotes)
- `awards_count` - Number of awards/gildings the comment received

### Links

- `permalink` - Direct link to the comment
- `post_url` - URL of the parent post

### Metadata

- `depth` - Nesting level/depth in the comment thread (0 = top-level)
- `parent_comment_id` - ID of the parent comment (null for top-level comments)
- `is_op` - Boolean indicating if the author is the Original Poster
- `is_edited` - Boolean indicating if the comment was edited
- `is_stickied` - Boolean indicating if the comment is stickied/pinned

### Timestamps

- `created_utc` - Unix timestamp when the comment was created
- `created_at` - ISO 8601 formatted datetime (e.g., "2025-10-14T12:30:45")

### Example Output

```json
{
  "comment_id": "abc123xyz",
  "comment_name": "t1_abc123xyz",
  "author": "example_user",
  "text": "This is a great discussion! I totally agree with your points about...",
  "score": 42,
  "awards_count": 2,
  "permalink": "https://old.reddit.com/r/programming/comments/1abc123/_/abc123xyz/",
  "post_url": "https://old.reddit.com/r/programming/comments/1abc123/interesting_discussion/",
  "depth": 0,
  "parent_comment_id": null,
  "is_op": false,
  "is_edited": true,
  "is_stickied": false,
  "created_utc": 1728912645,
  "created_at": "2025-10-14T12:30:45"
}
```

## Usage

### Local Development

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

2. **Set up input** in `storage/key_value_stores/default/INPUT.json`:

   ```json
   {
     "postUrls": ["https://www.reddit.com/r/programming/comments/1example/"],
     "maxComments": 100,
     "expandThreads": true
   }
   ```

3. **Run the actor**:

   ```bash
   python -m src
   ```

4. **Check results** in `storage/datasets/default/`

### On Apify Platform

1. **Push to Apify**:

   - Login to Apify CLI: `apify login`
   - Initialize: `apify init` (if not already done)
   - Push to Apify: `apify push`

2. **Or manually upload**:

   - Create a new actor on Apify platform
   - Upload all files including `Dockerfile`, `requirements.txt`, and `.actor/` directory

3. **Configure and run**:
   - Set input parameters in the Apify console
   - Paste Reddit post URLs
   - Click "Start" to run the actor
   - Download results from the dataset tab

## Technical Details

### Browser Automation

- Uses **Playwright** with Chromium browser
- Scrapes `old.reddit.com` for better compatibility and simpler HTML structure
- Implements anti-detection measures:
  - Custom User-Agent headers
  - Disabled automation flags
  - Browser fingerprint masking

### Features

- **Automatic thread expansion**: Clicks "load more" and "continue this thread" buttons
- **Smart extraction**: Handles nested comments and preserves thread structure
- **Depth tracking**: Captures comment nesting levels
- **Parent-child relationships**: Links comments to their parents
- **Error handling**: Gracefully handles deleted comments and missing data

### Comment Expansion

The scraper automatically:

1. Clicks "load more comments" buttons (up to 10 per attempt)
2. Clicks "continue this thread" links (up to 5 per attempt)
3. Makes up to 3 expansion attempts to maximize comment coverage
4. Waits for new comments to load after each expansion

### Performance

- Headless browser mode for efficiency
- Optimized page load strategy (`domcontentloaded`)
- Configurable wait times and timeouts
- Parallel processing of multiple posts (sequential with delays)

## Limitations

- Only works with public Reddit posts
- Cannot scrape private or restricted posts
- Browser automation is slower than direct API calls but more reliable
- Hidden scores show as 0 (when "[score hidden]" is displayed)
- Maximum 10,000 comments per post (configurable)

## Dependencies

- `apify>=2.1.0` - Apify SDK for Python
- `playwright~=1.40.0` - Browser automation framework
- `beautifulsoup4~=4.12.0` - HTML parsing library

## Troubleshooting

### Timeout Issues

If you encounter timeout errors:

- Check if the post URL is valid and accessible
- Increase timeout values in the code if needed
- Verify the post has comments

### Missing Comments

If some comments are missing:

- Enable `expandThreads` to load collapsed comments
- Increase `maxComments` limit
- Some comments may be deleted or removed by moderators

### "[deleted]" Authors

- Comments from deleted accounts show "[deleted]" as author
- This is normal Reddit behavior
- The comment text may still be available or show as "[removed]"

## Use Cases

- **Sentiment Analysis**: Analyze community opinions on topics
- **Market Research**: Gather user feedback and discussions
- **Content Moderation**: Monitor discussions for moderation
- **Academic Research**: Study online community interactions
- **Data Analysis**: Build datasets for machine learning

## License

This actor is provided as-is for scraping public Reddit data in accordance with Reddit's terms of service.

## Notes

- This scraper uses browser automation to access Reddit's public web interface
- Always respect Reddit's robots.txt and terms of service
- Use responsibly and avoid overwhelming Reddit's servers
- Consider implementing additional rate limiting for large-scale scraping
- The actor works best with the Apify platform's infrastructure
- Posts with thousands of comments may take longer to scrape

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/reddit-comment-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
