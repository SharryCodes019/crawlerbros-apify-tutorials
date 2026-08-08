# LinkedIn Top Content Scraper Tutorial: Run This Apify Actor with Python

Scrape LinkedIn's trending and top-performing posts. Extracts viral content, Top Voice posts, and trending articles with engagement metrics, author details, and media type.

This repository shows how to run [LinkedIn Top Content Scraper](https://apify.com/crawlerbros/linkedin-top-content-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-top-content-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-top-content-scraper](https://apify.com/crawlerbros/linkedin-top-content-scraper)
- **SEO title:** LinkedIn Top Content Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape LinkedIn's trending and top-performing posts. Extracts viral content, Top Voice posts, and trending articles with engagement metrics, author details, and media type.

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

# LinkedIn Top Content Scraper

Scrape LinkedIn's trending and top-performing posts — including viral content, LinkedIn Top Voice posts, and trending articles — with full engagement metrics, author details, and media information.

## What It Does

This actor fetches posts from LinkedIn's top content feeds using a multi-strategy cascade:

1. **Top Content Feed** (`/voyager/api/feed/topContent`) — LinkedIn's dedicated trending posts endpoint
2. **Content Search** (`/voyager/api/search/blended`) — search for top posts by category keyword
3. **Flagship Feed** (`/voyager/api/feed/flagshipFeed`) — feed filtered to `TOP_CONTENT` context
4. **Public Trending Page** (`/feed/trending/`) — cookieless fallback using public embedded data

The strategies are tried in order; results are deduplicated and capped at your `maxPosts` limit.

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `maxPosts` | integer | No | Maximum posts to scrape (default: 50, range: 1–500) |
| `category` | string | No | Topic keyword like `AI`, `leadership`, `marketing` |
| `cookie` | string | No | LinkedIn `li_at` cookie or full cookies JSON array |
| `proxyConfiguration` | object | No | Apify proxy settings |

### Cookie

For best results, provide a LinkedIn session cookie. Without it, only the public trending page is scraped (fewer results).

**Accepted formats:**
- Plain `li_at` value: `AQEDxxx...`
- Full cookies JSON array from browser export: `[{"name":"li_at","value":"AQEDxxx..."},...]`

### Category

Use `category` to focus on a specific topic. Examples:
- `AI` — artificial intelligence posts
- `leadership` — leadership content
- `marketing` — marketing insights
- `data science` — data science posts
- Leave empty for general trending content

## Output

Each item in the dataset represents one LinkedIn post:

| Field | Type | Description |
|---|---|---|
| `postId` | string | LinkedIn activity ID |
| `postUrl` | string | Direct URL to the post |
| `authorName` | string | Author's full name |
| `authorProfileUrl` | string | Author's LinkedIn profile URL |
| `authorHeadline` | string | Author's headline / job title |
| `postedAt` | string | ISO 8601 UTC timestamp of publication |
| `content` | string | Full text of the post |
| `mediaType` | string | `text`, `image`, `video`, `article`, `document`, `carousel`, `repost`, `poll`, or `event` |
| `mediaUrls` | array | CDN image URLs (when `mediaType=image`) |
| `articleTitle` | string | Article title (when `mediaType=article`) |
| `articleUrl` | string | Article URL (when `mediaType=article`) |
| `reactionsCount` | integer | Total reaction count |
| `commentsCount` | integer | Total comment count |
| `repostsCount` | integer | Total repost/share count |
| `reactionBreakdown` | object | Per-type counts: `like`, `celebrate`, `love`, `insightful`, `support`, `funny`, `curious` |
| `scrapedAt` | string | ISO 8601 UTC timestamp when scraped |

## Example Output

```json
{
  "postId": "7234567890123456789",
  "postUrl": "https://www.linkedin.com/feed/update/urn:li:activity:7234567890123456789/",
  "authorName": "Satya Nadella",
  "authorProfileUrl": "https://www.linkedin.com/in/satyanadella",
  "authorHeadline": "Chairman and CEO at Microsoft",
  "postedAt": "2025-05-15T14:30:00+00:00",
  "content": "Excited to share our latest breakthroughs in AI...",
  "mediaType": "text",
  "reactionsCount": 42500,
  "commentsCount": 1230,
  "repostsCount": 3400,
  "reactionBreakdown": {
    "like": 30000,
    "celebrate": 8000,
    "insightful": 3500,
    "love": 1000
  },
  "scrapedAt": "2025-05-20T10:00:00+00:00"
}
```

## Use Cases

- **Trend analysis**: Identify what topics and formats are performing best on LinkedIn
- **Competitor research**: See what content your industry peers are posting
- **Content strategy**: Find inspiration from viral posts in your niche
- **Influencer discovery**: Identify LinkedIn Top Voices in specific categories
- **Market research**: Track sentiment and trending topics over time

## FAQs

**Do I need a LinkedIn account?**
No, the actor can run without a cookie and will scrape the public trending feed. However, providing a cookie gives access to more posts and enables category-based filtering.

**How many posts can I scrape?**
Up to 500 posts per run. The actual number depends on what LinkedIn surfaces in its trending feeds.

**Why are some posts missing fields like `postedAt` or `authorHeadline`?**
LinkedIn omits some data for certain posts. Fields are only included when data is available — no null or empty values are pushed.

**Will this get my LinkedIn account banned?**
The actor uses the same Voyager API endpoints that LinkedIn's own mobile app uses, with realistic delays between requests. Proxy configuration is recommended for high-volume usage.

**What is the `reactionBreakdown` field?**
It shows how many reactions of each type the post received: `like` (thumbs up), `celebrate` (clapping), `love` (heart), `insightful` (lightbulb), `support` (hug), `funny` (laughing), and `curious` (curious face).

## Explore the rest of the LinkedIn suite

Need a different LinkedIn surface? Pair this actor with any of the others in the LinkedIn Suite — all published under the same publisher and built to share the same cookie format and output conventions.

| Actor | What it scrapes |
|---|---|
| [LinkedIn Comments Scraper](https://apify.com/crawlerbros/linkedin-comments-scraper) | All comments + reply threads on a post |
| [LinkedIn Company Employees Scraper](https://apify.com/crawlerbros/linkedin-company-employees-scraper) | Employee list for any company (by URN) |
| [LinkedIn Company Info Scraper](https://apify.com/crawlerbros/linkedin-company-info-scraper) | Company About page (size, HQ, industry, specialties) |
| [LinkedIn Company Posts Scraper](https://apify.com/crawlerbros/linkedin-company-posts-scraper) | Posts published from a company page |
| [LinkedIn Events Scraper](https://apify.com/crawlerbros/linkedin-events-scraper) | Events by keyword/URL with full event detail |
| [LinkedIn Hashtag Posts Scraper](https://apify.com/crawlerbros/linkedin-hashtag-posts-scraper) | Posts ranked under a `#hashtag` |
| [LinkedIn Jobs Scraper](https://apify.com/crawlerbros/linkedin-jobs-scraper) | Job listings via the public jobs-guest API |
| [LinkedIn Jobs Scraper Ultra](https://apify.com/crawlerbros/linkedin-jobs-scraper-ultra) | Same as jobs-scraper + full detail enrichment |
| [LinkedIn Learning Courses Scraper](https://apify.com/crawlerbros/linkedin-learning-courses-scraper) | LinkedIn Learning course catalog by keyword |
| [LinkedIn People Search Scraper](https://apify.com/crawlerbros/linkedin-people-search-scraper) | People search with every LinkedIn facet (role, company, school, location, etc.) |
| [LinkedIn Post Reactions Scraper](https://apify.com/crawlerbros/linkedin-post-reactions-scraper) | Reactors on a post (name, headline, reaction type) |
| [LinkedIn Post Scraper](https://apify.com/crawlerbros/linkedin-post-scraper) | Full post (text, media, engagement counts, author) |
| [LinkedIn Post Search Scraper](https://apify.com/crawlerbros/linkedin-post-search-scraper) | Posts matching a keyword (with date/author/network filters) |
| [LinkedIn Profile Posts Scraper](https://apify.com/crawlerbros/linkedin-profile-posts-scraper) | All posts/reposts/articles for one profile |
| [LinkedIn Profile Scraper](https://apify.com/crawlerbros/linkedin-profile-scraper) | Public profile fields (name, headline, positions, education, skills) |
| [LinkedIn Profile Scraper Pro](https://apify.com/crawlerbros/linkedin-profile-scraper-pro) | Profile fields + extras (recommendations, organizations, languages) |
| [LinkedIn Profile Scraper Pro Ultra](https://apify.com/crawlerbros/linkedin-profile-scraper-pro-ultra) | Pro + premium fields (contact info, followers list when allowed) |
| [LinkedIn Profile Scraper Ultra](https://apify.com/crawlerbros/linkedin-profile-scraper-ultra) | Profile + the full upstream dash-120 surface |
| [LinkedIn Profile Search by Name](https://apify.com/crawlerbros/linkedin-profile-search-by-name) | Search profiles by person name (great for matching CSVs of names) |
| [LinkedIn Schools Alumni Scraper](https://apify.com/crawlerbros/linkedin-schools-alumni-scraper) | Alumni list for any LinkedIn school page |
| [LinkedIn User Activity Scraper](https://apify.com/crawlerbros/linkedin-user-activity-scraper) | Reactions + comments + posts feed for one profile |

All actors share the same `cookie` input format (plain `li_at` OR full cookies JSON array) and the same omit-empty output convention.
<!-- /linkedin-suite -->

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-top-content-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
