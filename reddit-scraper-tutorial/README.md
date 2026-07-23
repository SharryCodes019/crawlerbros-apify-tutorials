# Reddit Scraper Tutorial: Run This Apify Actor with Python

Scrape entire subreddits with this crawler. Returns the posts in a subreddit along with their title, text, scores and timestamps etc.

This repository shows how to run [Reddit Scraper](https://apify.com/crawlerbros/reddit-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/reddit-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/reddit-scraper](https://apify.com/crawlerbros/reddit-scraper)
- **SEO title:** Reddit Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape entire subreddits with this crawler. Returns the posts in a subreddit along with their title, text, scores and timestamps etc.

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

An Apify Actor for scraping posts from Reddit subreddits using Reddit's JSON API.

## Features

- 🎯 Scrape multiple subreddits in a single run
- 📊 Extract comprehensive post data (title, author, score, comments, etc.)
- 🔄 Support for different sorting methods (hot, new, top, rising)
- ⏰ Time filters for "top" posts
- 📦 No authentication required for public subreddits
- 💾 Data saved in structured JSON format

## Input Parameters

The actor accepts the following input parameters:

| Parameter    | Type    | Required | Default      | Description                                                                  |
| ------------ | ------- | -------- | ------------ | ---------------------------------------------------------------------------- |
| `subreddits` | array   | Yes      | `["python"]` | List of subreddit names to scrape (without 'r/' prefix)                      |
| `maxPosts`   | integer | No       | `25`         | Maximum number of posts to scrape from each subreddit (1-1000)               |
| `sort`       | string  | No       | `"hot"`      | How to sort posts: `hot`, `new`, `top`, or `rising`                          |
| `timeFilter` | string  | No       | `"day"`      | Time filter for 'top' sort: `hour`, `day`, `week`, `month`, `year`, or `all` |

### Example Input

```json
{
  "subreddits": ["python", "programming", "webdev"],
  "maxPosts": 50,
  "sort": "hot",
  "timeFilter": "day"
}
```

## Output

The actor extracts the following data for each post:

- `subreddit` - Subreddit name
- `subreddit_prefixed` - Subreddit name with r/ prefix
- `title` - Post title
- `author` - Username of the author
- `author_fullname` - Full name/ID of the author
- `score` - Post score (upvotes - downvotes)
- `upvote_ratio` - Ratio of upvotes
- `num_comments` - Number of comments
- `created_utc` - Creation timestamp (UTC)
- `permalink` - Full URL to the post
- `url` - URL of the linked content
- `is_self` - Whether it's a self/text post
- `selftext` - Text content (for self posts)
- `link_flair_text` - Post flair text
- `post_id` - Unique post ID
- `post_name` - Full post name (t3_xxx)
- `domain` - Domain of the linked content
- `is_video` - Whether the post is a video
- `over_18` - NSFW flag
- `spoiler` - Spoiler flag
- `stickied` - Whether the post is stickied
- `locked` - Whether the post is locked
- `thumbnail` - Thumbnail URL
- `gilded` - Number of gildings
- `total_awards_received` - Total awards received

### Example Output

```json
{
  "subreddit": "Python",
  "subreddit_prefixed": "r/Python",
  "title": "Advice on logging libraries: Logfire, Loguru, or just Python",
  "author": "example_user",
  "score": 133,
  "upvote_ratio": 0.96,
  "num_comments": 66,
  "created_utc": 1760227231.0,
  "permalink": "https://www.reddit.com/r/Python/comments/...",
  "url": "https://www.reddit.com/r/Python/comments/...",
  "is_self": true,
  "selftext": "Post content here...",
  "link_flair_text": "Discussion",
  "post_id": "abc123",
  "domain": "self.Python",
  "is_video": false,
  "over_18": false,
  "spoiler": false,
  "stickied": false,
  "locked": false
}
```

## Usage

### Local Development

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
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

   - Initialize git: `git init` (if not already done)
   - Login to Apify CLI: `apify login`
   - Push to Apify: `apify push`

2. **Or manually upload**:
   - Create a new actor on Apify platform
   - Upload all files including `Dockerfile`, `requirements.txt`, and `.actor/` directory
3. **Configure and run**:
   - Set input parameters in the Apify console
   - Click "Start" to run the actor
   - Download results from the dataset tab

## Technical Details

- Uses Reddit's public JSON API (`.json` endpoint)
- No authentication required for public subreddits
- Implements pagination to handle large result sets
- Respects Reddit's rate limiting
- Maximum 100 posts per API request (Reddit's limit)
- Uses browser-like User-Agent for better compatibility

## Limitations

- Only works with public subreddits
- Cannot scrape private or restricted communities
- Subject to Reddit's rate limiting
- Maximum 1000 posts per subreddit (configurable)

## Dependencies

- `apify` - Apify SDK for Python
- `httpx` - Async HTTP client
- `beautifulsoup4` - HTML parsing (dependency of Apify)
- `lxml` - XML/HTML parser (dependency of BeautifulSoup)

## License

This actor is provided as-is for scraping public Reddit data in accordance with Reddit's terms of service.

## Notes

- This scraper uses Reddit's public JSON API
- Always respect Reddit's robots.txt and terms of service
- Use responsibly and avoid overwhelming Reddit's servers
- Consider implementing rate limiting for large-scale scraping

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/reddit-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
