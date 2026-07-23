# Reddit Keywords Tutorial: Run This Apify Actor with Python

Welcome to Reddit Keywords Scraper. Scrape Posts from Reddit through Reddit search engine by providing your desired keyword, the crawler will return post urls, number of comments, score, title, content, thumbnail and much more. Be sure to leave a review and provide feedback.

This repository shows how to run [Reddit Keywords](https://apify.com/crawlerbros/reddit-keywords) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/reddit-keywords`
- **Apify Store:** [https://apify.com/crawlerbros/reddit-keywords](https://apify.com/crawlerbros/reddit-keywords)
- **SEO title:** Reddit Keywords Tutorial: Run This Apify Actor with Python
- **Description:** Welcome to Reddit Keywords Scraper. Scrape Posts from Reddit through Reddit search engine by providing your desired keyword, the crawler will return post urls, number of comments, score, title, content, thumbnail and much more. Be sure to leave a review and provide feedback.

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

# Reddit Keywords Scraper

An **Apify Actor** built with **Python + Playwright** to automatically **search and scrape Reddit posts by specific keywords**.  
Perfect for **market research**, **trend analysis**, and **content discovery** — all without relying on the Reddit API.

## Features

- 🔍 **Search by Keywords:** Find Reddit posts matching specific words or phrases
- 🧩 **Multiple Keywords:** Search multiple keywords in a single run
- 📊 **Detailed Post Data:** Extract post titles, authors, scores, timestamps, flairs, and more
- ⚙️ **Sorting Options:** Sort by `relevance`, `hot`, `top`, `new`, or `comments`
- 📈 **Result Limit Control:** Fetch up to 1000 posts per keyword
- 🌐 **Browser-Based Crawling:** Avoid API limits using Playwright automation
- 💾 **Structured JSON Output:** Get clean, ready-to-use JSON data
- 🔄 **Pagination Support:** Automatically loads additional search results

## 🧠 Use Cases

Use the **Reddit Keyword Scraper** to:

- 📢 **Perform Market Research** — Track discussions around your product, brand, or niche
- 💬 **Conduct Sentiment Analysis** — Collect Reddit data for NLP or public opinion analysis
- 📰 **Discover Trending Content** — Identify viral or high-performing posts
- 📈 **Monitor Trends** — Follow emerging topics across subreddits
- 🕵️ **Gather Competitive Intelligence** — Find mentions of competitors or products
- 🎓 **Support Academic Research** — Build Reddit-based datasets for studies

## Input Parameters

The actor accepts the following input parameters:

| Parameter     | Type    | Required | Default     | Description                                               |
| ------------- | ------- | -------- | ----------- | --------------------------------------------------------- |
| `keywords`    | array   | Yes      | -           | List of keywords to search for on Reddit                  |
| `resultLimit` | integer | No       | `25`        | Maximum number of results to return per keyword (1-1000)  |
| `sort`        | string  | No       | `relevance` | Sort method: `relevance`, `hot`, `top`, `new`, `comments` |

### Example Input

```json
{
  "keywords": ["python programming", "machine learning", "web scraping"],
  "resultLimit": 50,
  "sort": "top"
}
```

### Sorting Options

- **`relevance`** - Most relevant to the search query (default)
- **`hot`** - Currently trending/hot posts
- **`top`** - Top-scoring posts of all time
- **`new`** - Newest posts first
- **`comments`** - Posts with the most comments

## 📤 Output Data Fields

Each Reddit post result includes:

| Field             | Description                                            |
| ----------------- | ------------------------------------------------------ |
| `keyword`         | The searched keyword that matched this post            |
| `post_id`         | Unique Reddit post ID (e.g., `1ntdzya`)                |
| `post_name`       | Full Reddit post identifier (e.g., `t3_1ntdzya`)       |
| `title`           | Post title                                             |
| `author`          | Username of the author (`[deleted]` if removed)        |
| `subreddit`       | Subreddit name                                         |
| `content`         | Text content for self/text posts (null for link posts) |
| `score`           | Post score/upvotes                                     |
| `num_comments`    | Number of comments                                     |
| `url`             | Direct link to the post                                |
| `old_reddit_url`  | Link to the old Reddit version of the post             |
| `thumbnail_image` | Thumbnail image URL (if available)                     |
| `link_flair`      | Post flair text                                        |
| `created_utc`     | Unix timestamp when the post was created               |
| `created_at`      | ISO 8601 formatted creation date/time                  |
| `is_stickied`     | Boolean indicating if the post is pinned               |
| `is_nsfw`         | Boolean indicating if the post is marked NSFW          |

### 🧾 Example Output

```json
{
  "keyword": "putin",
  "post_id": "1ntdzya",
  "post_name": "t3_1ntdzya",
  "title": "All hopes of reasoning with Putin are gone - war is coming",
  "author": "theipaper",
  "subreddit": "r/geopolitics",
  "content": null,
  "score": 743,
  "num_comments": 354,
  "url": "https://reddit.com/r/geopolitics/comments/1ntdzya/all_hopes_of_reasoning_with_putin_are_gone_war_is/",
  "old_reddit_url": "https://old.reddit.com/r/geopolitics/comments/1ntdzya/all_hopes_of_reasoning_with_putin_are_gone_war_is/",
  "thumbnail_image": "https://external-preview.redd.it/gBVLJovs7dZbfvD14Q2tZiSlEMt_26iIluaegGWD-mM.jpeg",
  "link_flair": null,
  "created_utc": 1759140117,
  "created_at": "2025-09-29T10:01:57+00:00",
  "is_stickied": false,
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

2. **Set up input**:

   Create a `.actor/INPUT.json` file or use environment variables:

```json
{
  "keywords": ["python programming", "machine learning"],
  "resultLimit": 10,
  "sort": "relevance"
}
```

3. **Run locally**:

   ```bash
   apify run
   ```

### Running on Apify Platform

1. **Create an Actor** on the [Apify Platform](https://console.apify.com/)
2. **Upload the code** or connect your Git repository
3. **Configure the input** in the Actor's input tab
4. **Run the Actor** and view results in the dataset

### Example: Searching Multiple Topics

```json
{
  "keywords": [
    "artificial intelligence",
    "climate change",
    "space exploration",
    "cryptocurrency"
  ],
  "resultLimit": 100,
  "sort": "hot"
}
```

This will search for 100 hot posts about each topic and return a total of up to 400 posts.

## Notes

- The actor uses old.reddit.com for better reliability and performance
- Results are limited to publicly accessible posts
- Rate limiting is handled with delays between searches
- Some very old posts may have incomplete data
- The actor respects Reddit's structure and uses browser automation

## Technical Details

- **Runtime**: Python 3.12
- **Browser**: Chromium (via Playwright)
- **HTML Parser**: BeautifulSoup4
- **Framework**: Apify SDK

## Limitations

- Maximum result limit per keyword: 1000 posts
- Only returns posts (not comments) from search results
- Requires stable internet connection
- Processing time increases with result limit and number of keywords

## Troubleshooting

### No Results Found

- Verify the keywords are spelled correctly
- Try more general or popular keywords
- Check if Reddit is accessible in your region
- Try a different sort method

### Incomplete Data

- Some older posts may have missing fields
- Deleted posts will show "[deleted]" as author
- Private/removed posts won't appear in results

## Related Actors

- **Reddit Comment Scraper** - Scrape comments from specific Reddit posts
- **Reddit Profile Scraper** - Scrape posts from specific user profiles
- **Reddit Scraper** - General Reddit data scraper

## Support

For issues, questions, or contributions, please open an issue in the repository.

## License

This actor is provided as-is for use on the Apify platform.

```

```

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/reddit-keywords)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
