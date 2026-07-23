# Instagram Keyword Scraper Tutorial: Run This Apify Actor with Python

Search Instagram by keywords and extract detailed post data at scale. Get usernames, captions, engagement metrics, media URLs, hashtags, mentions, location data, music info, and more for every matching post.

Perfect for market research, brand monitoring, competitor analysis and etc.

This repository shows how to run [Instagram Keyword Scraper](https://apify.com/crawlerbros/instagram-keyword-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-keyword-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-keyword-scraper](https://apify.com/crawlerbros/instagram-keyword-scraper)
- **SEO title:** Instagram Keyword Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search Instagram by keywords and extract detailed post data at scale. Get usernames, captions, engagement metrics, media URLs, hashtags, mentions, location data, music info, and more for every matching post.

Perfect for market research, brand monitoring, competitor analysis and etc.

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

# Instagram Keyword Scraper

Search Instagram by keywords and extract detailed post data at scale. Get usernames, captions, engagement metrics, media URLs, hashtags, mentions, location data, music info, and more for every matching post.

Perfect for market research, brand monitoring, competitor analysis, influencer discovery, and trend tracking on Instagram.

## What data can you extract from Instagram keyword search?

For every post found, the scraper returns:

| Field            | Type      | Description                                              |
| ---------------- | --------- | -------------------------------------------------------- |
| `username`       | `string`  | Instagram username of the post author                    |
| `full_name`      | `string`  | Full display name of the post author                     |
| `profile_url`    | `string`  | URL to the author's Instagram profile                    |
| `collaborators`  | `array`   | List of collaborator usernames on the post               |
| `post_url`       | `string`  | Direct URL to the Instagram post                         |
| `pub_date`       | `string`  | Publication date in ISO 8601 format                      |
| `caption`        | `string`  | Full caption text of the post                            |
| `mentions`       | `array`   | Usernames @mentioned in the caption                      |
| `hashtags`       | `array`   | Hashtags used in the caption                             |
| `media_urls`     | `array`   | Direct URLs to media files (images and videos)           |
| `thumbnail_url`  | `string`  | URL of the post thumbnail image                          |
| `media_type`     | `string`  | Type of media: Photo, Video, Reel, IGTV, or Carousel    |
| `media_count`    | `integer` | Number of media items in the post                        |
| `likes_hidden`   | `boolean` | Whether like counts are hidden on this post              |
| `like_count`     | `integer` | Number of likes (null if hidden by the author)           |
| `comment_count`  | `integer` | Number of comments on the post                           |
| `location`       | `object`  | Location tagged in the post (name, latitude, longitude)  |
| `music`          | `object`  | Music/audio used in the post (artist and title)          |
| `search_keyword` | `string`  | The keyword that was used to find this post              |
| `scraped_at`     | `string`  | Timestamp when the data was collected                    |
| `status`         | `string`  | `"success"` when a post was extracted, `"No posts found"` when a keyword has no results |

## How to use Instagram Keyword Scraper

1. **Add your search keywords** - Enter one or more keywords or phrases (e.g., "living in dubai", "travel photography")
2. **Provide Instagram cookies** - Paste your Instagram session cookies (required for search access)
3. **Set the result limit** - Choose how many posts to extract per keyword (1 to 500, default 20)
4. **Run the scraper** - Click Start and the scraper collects all post data automatically
5. **Export your data** - Download results as JSON, CSV, Excel, or connect via API

## Input

| Field         | Type       | Description                                                  | Default             |
| ------------- | ---------- | ------------------------------------------------------------ | ------------------- |
| `keywords`    | `string[]` | List of keywords or phrases to search for on Instagram       | _required_          |
| `maxPosts`    | `integer`  | Maximum number of posts to extract per keyword (1-500)       | `20`                |
| `cookies`     | `string`   | Instagram authentication cookies in JSON format (required)   | -                   |
| `sessionName` | `string`   | Name for saving/loading cookies between runs                 | `"default_session"` |

### Example Input

```json
{
  "keywords": ["living in dubai", "travel photography"],
  "maxPosts": 50,
  "cookies": "[{\"name\":\"sessionid\",\"value\":\"YOUR_SESSION_ID\",\"domain\":\".instagram.com\",\"path\":\"/\",\"secure\":true,\"httpOnly\":true}]",
  "sessionName": "my_session"
}
```

## Output

### Example Output

```json
[
  {
    "username": "travel_creator",
    "full_name": "Travel Creator",
    "profile_url": "https://www.instagram.com/travel_creator/",
    "collaborators": ["co_creator"],
    "post_url": "https://www.instagram.com/p/ABC123/",
    "pub_date": "2025-11-20T15:25:01.000Z",
    "caption": "Amazing sunset in Dubai! #dubai #travel @friend",
    "mentions": ["friend"],
    "hashtags": ["dubai", "travel"],
    "media_urls": ["https://instagram.com/video.mp4"],
    "thumbnail_url": "https://instagram.com/thumbnail.jpg",
    "media_type": "Reel",
    "media_count": 1,
    "likes_hidden": false,
    "like_count": 175908,
    "comment_count": 42,
    "location": {
      "name": "Dubai, United Arab Emirates",
      "lat": 25.1994,
      "lng": 55.2741
    },
    "music": {
      "artist": "Artist Name",
      "title": "Song Title"
    },
    "search_keyword": "living in dubai",
    "scraped_at": "2025-11-21T12:28:25.052408",
    "status": "success"
  }
]
```

When a keyword returns no results, a single record is pushed instead:

```json
[
  {
    "search_keyword": "very obscure query with no results",
    "status": "No posts found"
  }
]
```

## How to get Instagram cookies

Instagram requires authentication to access keyword search results. You need to provide cookies from an active Instagram session.

**Using a cookie export extension (recommended):**

1. Install a cookie export extension like [Cookie-Editor](https://cookie-editor.cgagnier.ca/) or EditThisCookie for your browser
2. Log in to Instagram
3. Click the extension icon and export cookies as JSON
4. Paste the entire JSON into the `cookies` input field

The scraper automatically converts browser cookie formats - no manual cleanup needed.

**Important:** Use a dedicated Instagram account for scraping. Never share your cookies. Cookies expire periodically and need to be refreshed.

## Use cases

- **Market research** - Analyze trending topics and popular content for any niche or industry
- **Brand monitoring** - Track how your brand, products, or campaigns are discussed on Instagram
- **Competitor analysis** - Monitor competitor content, engagement rates, and posting patterns
- **Influencer discovery** - Find creators in specific niches by searching relevant keywords
- **Trend tracking** - Identify emerging trends, popular hashtags, and viral content
- **Content inspiration** - Discover high-performing posts for content strategy planning
- **Location intelligence** - Analyze posts tagged at specific locations or mentioning places

## Integrations

Connect Instagram Keyword Scraper with your existing tools and workflows:

- **Webhooks** - Get notified when a scrape finishes
- **API access** - Integrate results directly into your application
- **Scheduled runs** - Set up recurring scrapes to monitor keywords over time
- Export to **Google Sheets**, **Slack**, **Zapier**, **Make**, and more

## FAQ

### How many posts can I scrape per keyword?

You can extract up to 500 posts per search keyword. The default is 20. Instagram's search results are limited by their algorithm, so available results may vary by keyword.

### What types of posts are supported?

The scraper extracts all post types: Photos, Videos, Reels, IGTV, and Carousels. For carousel posts, all individual media URLs are included.

### Does the scraper extract engagement metrics?

Yes. Like counts, comment counts, and view data are extracted for each post. If the post author has hidden like counts, the `likes_hidden` field will be `true` and `like_count` will be null.

### Can I search for multiple keywords at once?

Yes. Pass an array of keywords and the scraper will process each one, returning all results in a single dataset. Each result includes a `search_keyword` field so you can filter by keyword.

### Why do I need cookies?

Instagram requires authentication to access keyword search results. Without valid cookies, the search page won't load any posts. Use a cookie export extension to get your session cookies easily.

### How often do cookies expire?

Instagram session cookies typically last a few weeks to a few months. If the scraper stops returning results, try refreshing your cookies. Use the `sessionName` field to manage cookies between runs.

### What format can I export the data in?

Results can be exported as JSON, CSV, Excel, XML, or accessed via the Apify API. You can also connect to Google Sheets, Slack, Zapier, and other integrations.

### Does it extract location and music data?

Yes. If a post is tagged with a location, the scraper returns the location name, latitude, and longitude. For Reels and videos with music, the artist name and song title are included.

### Can I scrape posts from private accounts?

No. Only publicly visible posts that appear in Instagram's keyword search results can be scraped. Posts from private accounts are not accessible.

### What does the `status` field mean?

Every record in the output includes a `status` field. For successfully extracted posts it's `"success"`. When a keyword returns no results from Instagram's search, the scraper pushes a single record with `status: "No posts found"` so you can tell the difference between a failed run and a keyword that legitimately has no matches.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-keyword-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
