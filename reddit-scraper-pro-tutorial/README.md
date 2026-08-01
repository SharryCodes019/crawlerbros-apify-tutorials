# Reddit Scraper Pro Tutorial: Run This Apify Actor with Python

Scrape Reddit subreddit posts with advanced filters (keywordFilter, minScore, maxAgeDays, excludeStickied, excludeNsfw, authorBlocklist, domainAllowlist/Blocklist). Adds is_video / awards / gilded / upvote_ratio / media_metadata to every post. Browser-based, no login.

This repository shows how to run [Reddit Scraper Pro](https://apify.com/crawlerbros/reddit-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/reddit-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/reddit-scraper-pro](https://apify.com/crawlerbros/reddit-scraper-pro)
- **SEO title:** Reddit Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Reddit subreddit posts with advanced filters (keywordFilter, minScore, maxAgeDays, excludeStickied, excludeNsfw, authorBlocklist, domainAllowlist/Blocklist). Adds is_video / awards / gilded / upvote_ratio / media_metadata to every post. Browser-based, no login.

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

# Reddit Subreddit Scraper

An Apify Actor for scraping posts from Reddit subreddits using browser automation with Playwright.

## Features

- 🎯 Scrape multiple subreddits in a single run
- 📊 Extract comprehensive post data (title, author, score, comments, etc.)
- 🔄 Support for different sorting methods (hot, new, top, rising, controversial)
- ⏰ Time filters for "top" and "controversial" posts
- 📦 No authentication required for public subreddits
- 💾 Data saved in structured JSON format
- 🌐 Browser automation bypasses API restrictions
- 🔄 Automatic pagination support

## Input Parameters

The actor accepts the following input parameters:

| Parameter    | Type    | Required | Default      | Description                                                                          |
| ------------ | ------- | -------- | ------------ | ------------------------------------------------------------------------------------ |
| `subreddits` | array   | Yes      | `["python"]` | List of subreddit names to scrape (without 'r/' prefix)                              |
| `maxPosts`   | integer | No       | `25`         | Maximum number of posts to scrape from each subreddit (1-1000)                       |
| `sort`       | string  | No       | `"hot"`      | How to sort posts: `hot`, `new`, `top`, `rising`, or `controversial`                 |
| `timeFilter` | string  | No       | `"day"`      | Time filter for 'top'/'controversial': `hour`, `day`, `week`, `month`, `year`, `all` |

### Example Input

```json
{
  "subreddits": ["islamabad", "pakistan", "programming"],
  "maxPosts": 50,
  "sort": "hot",
  "timeFilter": "day"
}
```

## Output Fields

The actor extracts the following data for each post:

### Subreddit Information

- `subreddit` - Subreddit name (e.g., "islamabad")
- `subreddit_prefixed` - Subreddit name with r/ prefix (e.g., "r/islamabad")

### Post Content

- `post_id` - Unique post ID (e.g., "1kql1t5")
- `post_name` - Full post name in Reddit format (e.g., "t3_1kql1t5")
- `title` - Post title
- `author` - Username of the post author
- `selftext` - Text content preview (first 1000 chars, for self posts only)

### Engagement Metrics

- `score` - Post score/karma (upvotes minus downvotes)
- `num_comments` - Number of comments on the post

### Links

- `url` - URL of the linked content (external URL or permalink for self posts)
- `permalink` - Direct link to the Reddit post

### Metadata

- `domain` - Domain of the linked content (e.g., "self.islamabad" for text posts)
- `is_self_post` - Boolean indicating if it's a text post (true) or link post (false)
- `link_flair` - Post flair/tag text (if any)
- `thumbnail_url` - URL of the post thumbnail image (if any)

### Timestamps

- `created_utc` - Unix timestamp when the post was created
- `created_at` - ISO 8601 formatted datetime (e.g., "2025-05-19T19:40:28")

### Flags

- `is_stickied` - Boolean indicating if the post is stickied/pinned
- `is_locked` - Boolean indicating if the post is locked (no new comments)
- `is_nsfw` - Boolean indicating if the post is marked as NSFW (over 18)

### Example Output

```json
{
  "subreddit": "islamabad",
  "subreddit_prefixed": "r/islamabad",
  "post_id": "1kql1t5",
  "post_name": "t3_1kql1t5",
  "title": "Everyone's always asking what to do in Islamabad - I made a list",
  "author": "hafmaestro",
  "selftext": "Note: I have not mentioned normal restaurants and cafes...",
  "score": 595,
  "num_comments": 101,
  "url": "https://old.reddit.com/r/islamabad/comments/1kql1t5/...",
  "permalink": "https://old.reddit.com/r/islamabad/comments/1kql1t5/...",
  "domain": "self.islamabad",
  "is_self_post": true,
  "link_flair": "Islamabad",
  "thumbnail_url": null,
  "created_utc": 1747683628,
  "created_at": "2025-05-19T19:40:28",
  "is_stickied": false,
  "is_locked": false,
  "is_nsfw": false
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
     "subreddits": ["python"],
     "maxPosts": 25,
     "sort": "hot"
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

- **Automatic pagination**: Clicks "next" button to load more posts
- **Smart selectors**: Multiple fallback CSS selectors for reliability
- **Error handling**: Screenshots saved on errors for debugging
- **Rate limiting**: Built-in delays between requests

### Performance

- Headless browser mode for efficiency
- Optimized page load strategy (`domcontentloaded`)
- Configurable wait times and timeouts

## Limitations

- Only works with public subreddits
- Cannot scrape private or restricted communities
- Browser automation is slower than direct API calls but more reliable
- Selftext preview limited to first 1000 characters

## Dependencies

- `apify>=2.1.0` - Apify SDK for Python
- `playwright~=1.40.0` - Browser automation framework
- `beautifulsoup4~=4.12.0` - HTML parsing library

## Troubleshooting

### Timeout Issues

If you encounter timeout errors:

- Check the debug screenshots in the key-value store
- Increase timeout values in the code
- Verify the subreddit exists and is public

### No Posts Found

- Verify the subreddit name is correct (without 'r/' prefix)
- Check if the subreddit has posts for the selected sort method
- Review logs for detailed error messages

## License

This actor is provided as-is for scraping public Reddit data in accordance with Reddit's terms of service.

## Notes

- This scraper uses browser automation to access Reddit's public web interface
- Always respect Reddit's robots.txt and terms of service
- Use responsibly and avoid overwhelming Reddit's servers
- Consider implementing additional rate limiting for large-scale scraping
- The actor works best with the Apify platform's infrastructure

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/reddit-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
