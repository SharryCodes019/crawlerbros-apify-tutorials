# Reddit MCP Scraper Tutorial: Run This Apify Actor with Python

Unified Reddit scraper supporting 3 modes: (1) Subreddit posts with content extraction, (2) Post comments with threading, (3) User profiles with metadata. Extract comprehensive data including scores, timestamps, flairs, NSFW flags, and more.

This repository shows how to run [Reddit MCP Scraper](https://apify.com/crawlerbros/reddit-mcp-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/reddit-mcp-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/reddit-mcp-scraper](https://apify.com/crawlerbros/reddit-mcp-scraper)
- **SEO title:** Reddit MCP Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Unified Reddit scraper supporting 3 modes: (1) Subreddit posts with content extraction, (2) Post comments with threading, (3) User profiles with metadata. Extract comprehensive data including scores, timestamps, flairs, NSFW flags, and more.

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

# Reddit MCP Server

A unified Apify MCP (Model Context Protocol) server for comprehensive Reddit scraping. This actor provides a single interface to scrape subreddits, comments, and user profiles using browser automation with Playwright.

## 🚀 Features

### Multi-Mode Scraping

This MCP server supports three scraping modes:

1. **Subreddit Mode** - Scrape posts from Reddit subreddits
2. **Comments Mode** - Scrape comments from Reddit posts
3. **Profile Mode** - Scrape user profiles and their posts

### Key Capabilities

✅ **Unified Interface** - Single actor for all Reddit scraping needs  
✅ **Browser Automation** - Bypasses API restrictions using Playwright  
✅ **No Authentication Required** - Scrape public content without login  
✅ **Comprehensive Data** - Extract all relevant fields and metadata  
✅ **Automatic Pagination** - Load multiple pages automatically  
✅ **NSFW Support** - Automatically handles NSFW confirmation dialogs  
✅ **Structured Output** - Clean JSON data ready for AI consumption

## 📋 Input Parameters

### Common Parameters

| Parameter | Type   | Required | Description                                          |
| --------- | ------ | -------- | ---------------------------------------------------- |
| `mode`    | string | Yes      | Scraping mode: `subreddit`, `comments`, or `profile` |

### Subreddit Mode Parameters

| Parameter    | Type    | Default | Description                                                      |
| ------------ | ------- | ------- | ---------------------------------------------------------------- |
| `subreddits` | array   | -       | List of subreddit names (without 'r/' prefix)                    |
| `maxPosts`   | integer | `25`    | Maximum posts per subreddit (1-1000)                             |
| `sort`       | string  | `"hot"` | Sort method: `hot`, `new`, `top`, `controversial`                |
| `timeFilter` | string  | `"day"` | Time filter for top/controversial (hour/day/week/month/year/all) |

### Comments Mode Parameters

| Parameter       | Type    | Default | Description                            |
| --------------- | ------- | ------- | -------------------------------------- |
| `postUrls`      | array   | -       | List of Reddit post URLs to scrape     |
| `maxComments`   | integer | `100`   | Maximum comments per post (1-10000)    |
| `expandThreads` | boolean | `true`  | Automatically expand collapsed threads |

### Profile Mode Parameters

| Parameter   | Type    | Default       | Description                                        |
| ----------- | ------- | ------------- | -------------------------------------------------- |
| `usernames` | array   | -             | List of Reddit usernames (without 'u/' prefix)     |
| `maxPosts`  | integer | `100`         | Maximum posts per user (1-1000)                    |
| `section`   | string  | `"submitted"` | Profile section: `submitted`, `overview`, `gilded` |
| `sort`      | string  | `"new"`       | Sort method: `hot`, `new`, `top`, `controversial`  |

## 📝 Input Examples

### Example 1: Scrape Subreddits

```json
{
  "mode": "subreddit",
  "subreddits": ["python", "programming", "webdev"],
  "maxPosts": 50,
  "sort": "hot",
  "timeFilter": "day"
}
```

### Example 2: Scrape Comments

```json
{
  "mode": "comments",
  "postUrls": [
    "https://www.reddit.com/r/programming/comments/1abc123/interesting_discussion/",
    "https://old.reddit.com/r/python/comments/1def456/another_post/"
  ],
  "maxComments": 200,
  "expandThreads": true
}
```

### Example 3: Scrape User Profiles

```json
{
  "mode": "profile",
  "usernames": ["spez", "example_user"],
  "maxPosts": 100,
  "section": "submitted",
  "sort": "top"
}
```

## 📊 Output Format

### Subreddit Mode Output

Each post includes:

```json
{
  "subreddit": "python",
  "subreddit_prefixed": "r/python",
  "post_id": "1abc123",
  "post_name": "t3_1abc123",
  "title": "Interesting Python discussion",
  "author": "example_user",
  "selftext": "Post content preview...",
  "score": 456,
  "num_comments": 89,
  "url": "https://old.reddit.com/r/python/comments/...",
  "permalink": "https://old.reddit.com/r/python/comments/...",
  "domain": "self.python",
  "is_self_post": true,
  "link_flair": "Discussion",
  "thumbnail_url": null,
  "created_utc": 1747683628,
  "created_at": "2025-10-31T12:30:00",
  "is_stickied": false,
  "is_locked": false,
  "is_nsfw": false
}
```

### Comments Mode Output

Each comment includes:

```json
{
  "comment_id": "abc123xyz",
  "comment_name": "t1_abc123xyz",
  "author": "example_user",
  "text": "This is a great discussion!",
  "score": 42,
  "awards_count": 2,
  "permalink": "https://old.reddit.com/r/...",
  "post_url": "https://old.reddit.com/r/...",
  "depth": 0,
  "parent_comment_id": null,
  "is_op": false,
  "is_edited": true,
  "is_stickied": false,
  "created_utc": 1728912645,
  "created_at": "2025-10-31T12:30:45"
}
```

### Profile Mode Output

Profile data with posts:

```json
{
  "username": "spez",
  "post_karma": 0,
  "comment_karma": 0,
  "total_karma": 1047690,
  "account_created": "2005-06-06T04:00:00+00:00",
  "posts": [
    {
      "post_id": "abc123",
      "title": "Announcing new features",
      "author": "spez",
      "subreddit": "announcements",
      "score": 15234,
      "num_comments": 1250,
      "url": "https://old.reddit.com/...",
      "created_at": "2025-10-31T12:30:45",
      "is_stickied": true,
      "is_nsfw": false
    }
  ]
}
```

## 🎯 Use Cases

### Research & Analysis

- **Sentiment Analysis** - Analyze community opinions across subreddits
- **Trend Detection** - Track emerging topics and discussions
- **User Behavior** - Study posting patterns and engagement
- **Content Analysis** - Build datasets for machine learning

### Business Intelligence

- **Market Research** - Gather user feedback and discussions
- **Brand Monitoring** - Track mentions and sentiment
- **Competitive Analysis** - Monitor competitor discussions
- **Customer Insights** - Understand customer needs and pain points

### AI & ML Applications

- **Training Data** - Build high-quality datasets for AI models
- **RAG Systems** - Feed Reddit content to retrieval systems
- **Chatbot Training** - Use conversations for dialogue models
- **Content Generation** - Analyze successful content patterns

## 🛠️ Local Development

### Prerequisites

```bash
pip install -r requirements.txt
playwright install chromium
```

### Create Input File

Create `storage/key_value_stores/default/INPUT.json`:

```json
{
  "mode": "subreddit",
  "subreddits": ["python"],
  "maxPosts": 10
}
```

### Run Locally

```bash
cd Reddit/mcp
apify run
```

### Check Results

Results are saved in `storage/datasets/default/`

## 🚀 Deployment

### Using Apify CLI

```bash
# Login to Apify
apify login

# Push to Apify platform
apify push
```

### Manual Upload

1. Create a new actor on [Apify Console](https://console.apify.com/)
2. Upload all files including `Dockerfile`, `requirements.txt`, and `.actor/` directory
3. Configure input parameters
4. Run the actor

## 📚 API Integration

### JavaScript/Node.js

```javascript
const { ApifyClient } = require("apify-client");

const client = new ApifyClient({ token: "YOUR_API_TOKEN" });

const input = {
  mode: "subreddit",
  subreddits: ["python", "programming"],
  maxPosts: 50,
  sort: "hot",
};

const run = await client.actor("YOUR_ACTOR_ID").call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();

console.log(`Scraped ${items.length} posts`);
```

### Python

```python
from apify_client import ApifyClient

client = ApifyClient('YOUR_API_TOKEN')

input_data = {
    'mode': 'subreddit',
    'subreddits': ['python', 'programming'],
    'maxPosts': 50,
    'sort': 'hot'
}

run = client.actor('YOUR_ACTOR_ID').call(run_input=input_data)

for item in client.dataset(run['defaultDatasetId']).iterate_items():
    print(f"Post: {item['title']}")
    print(f"Score: {item['score']}")
```

## ⚡ Performance Tips

### Optimize Speed

- Start with lower `maxPosts` values for testing
- Use specific subreddits instead of scraping all posts
- Disable `expandThreads` in comments mode if not needed
- Process fewer URLs/usernames per run

### Avoid Rate Limiting

- Add delays between requests (built-in)
- Don't scrape the same content repeatedly
- Respect Reddit's servers - use reasonable limits
- Consider batching requests across multiple runs

## ⚠️ Limitations

- **Public Content Only** - Cannot scrape private subreddits or profiles
- **No Authentication** - Requires public access to content
- **Rate Limits** - Reddit may throttle excessive requests
- **Browser-Based** - Slower than direct API but more reliable
- **Dynamic Content** - Some features may change if Reddit updates layout

## 🐛 Troubleshooting

### No Results Returned

- Verify subreddit/username/URL is correct
- Check if content is public (not private/restricted)
- Try with smaller `maxPosts` values first
- Review logs for specific error messages

### Timeout Errors

- Content may be loading slowly
- Try with fewer items or smaller limits
- Check if Reddit is accessible from your location

### Missing Data Fields

- Some fields may be null if not available
- Deleted content shows "[deleted]" for authors
- Hidden scores may show as 0

## 📄 License

This actor is provided as-is for scraping public Reddit data in accordance with Reddit's terms of service.

## 🔗 Related Actors

- [Reddit Subreddit Scraper](../reddit/) - Dedicated subreddit scraper
- [Reddit Comment Scraper](../reddit-comment/) - Dedicated comment scraper
- [Reddit Profile Scraper](../reddit-profile/) - Dedicated profile scraper

## 💡 Notes

- This MCP server uses browser automation to access Reddit's public interface
- Always respect Reddit's robots.txt and terms of service
- Use responsibly and avoid overwhelming Reddit's servers
- Consider implementing additional rate limiting for large-scale scraping
- The actor works best with the Apify platform's infrastructure

## 🆘 Support

For issues, questions, or feature requests, please open an issue in the repository or contact support.

---

**Made with ❤️ for the AI community | Powered by Apify**

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/reddit-mcp-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
