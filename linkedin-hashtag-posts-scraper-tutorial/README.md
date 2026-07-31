# LinkedIn Hashtag Posts Scraper Tutorial: Run This Apify Actor with Python

Scrape posts tagged with any LinkedIn hashtag (e.g. #AI, #marketing). Returns author, content, engagement metrics. Cookie optional for public access, recommended for more results.

This repository shows how to run [LinkedIn Hashtag Posts Scraper](https://apify.com/crawlerbros/linkedin-hashtag-posts-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-hashtag-posts-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-hashtag-posts-scraper](https://apify.com/crawlerbros/linkedin-hashtag-posts-scraper)
- **SEO title:** LinkedIn Hashtag Posts Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape posts tagged with any LinkedIn hashtag (e.g. #AI, #marketing). Returns author, content, engagement metrics. Cookie optional for public access, recommended for more results.

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

# LinkedIn Hashtag Posts Scraper

Scrape posts tagged with any LinkedIn hashtag (e.g. `#AI`, `#marketing`, `#python`). Returns post content, author information, and engagement metrics for each post.

Cookie is **optional** — public hashtag pages work without authentication, but providing a LinkedIn session cookie unlocks significantly more results and higher pagination limits.

## Features

- Scrape posts for one or more hashtags in a single run
- Accepts hashtags in any format: `#AI`, `AI`, `artificial-intelligence`
- Returns author name, headline, profile URL, post content, media type, and full engagement counts
- Optional LinkedIn cookie for higher result volumes (Voyager API mode)
- Automatic fallback to public HTML mode when no cookie is supplied
- Handles rate limiting with automatic retries and exponential backoff
- Proxy support via Apify proxy configuration

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `hashtags` | array | Yes | List of hashtags to scrape (e.g. `["AI", "marketing"]`) |
| `maxPostsPerHashtag` | integer | No | Max posts per hashtag (default: 50, max: 500) |
| `cookie` | string | No | LinkedIn `li_at` cookie or full browser cookies JSON. Optional but recommended for more results. |
| `proxyConfiguration` | object | No | Apify proxy configuration. Residential proxy recommended. |

### Hashtag Formats Accepted

The actor normalizes hashtag input — the following are all equivalent:
- `#AI`
- `AI`
- `#artificial-intelligence`
- `artificial-intelligence`

### Cookie Format

Two formats are supported:

**Plain `li_at` value** (copy from DevTools → Application → Cookies):
```
AQEDATVc5uMEM5s_AAABnro67c...
```

**Full cookies JSON array** (export from a browser extension like EditThisCookie):
```json
[
  {"name": "li_at", "value": "AQEDATVc5uMEM5s_...", "domain": ".linkedin.com", ...},
  {"name": "JSESSIONID", "value": "ajax:67453...", "domain": ".linkedin.com", ...}
]
```

## Output

Each item in the dataset represents one LinkedIn post:

| Field | Type | Description |
|---|---|---|
| `postId` | string | LinkedIn activity ID |
| `postUrl` | string | Direct link to the post |
| `authorName` | string | Full name of the post author |
| `authorProfileUrl` | string | Author's LinkedIn profile URL |
| `authorHeadline` | string | Author's LinkedIn headline |
| `postedAt` | string | ISO 8601 UTC timestamp of publication |
| `content` | string | Full post text |
| `mediaType` | string | Media type: `text`, `image`, `video`, `article`, `document`, `carousel`, `repost`, `poll`, `event` |
| `reactionsCount` | integer | Total reactions count |
| `commentsCount` | integer | Total comments count |
| `repostsCount` | integer | Total reposts/shares count |
| `hashtag` | string | Normalized hashtag that produced this result (e.g. `ai`) |
| `scrapedAt` | string | ISO 8601 UTC timestamp when scraped |

### Example Output

```json
{
  "postId": "7381299540293623808",
  "postUrl": "https://www.linkedin.com/feed/update/urn:li:activity:7381299540293623808/",
  "authorName": "Jane Doe",
  "authorProfileUrl": "https://www.linkedin.com/in/janedoe",
  "authorHeadline": "AI Product Manager at Acme Corp",
  "postedAt": "2025-05-23T09:23:20+00:00",
  "content": "Excited to share our latest research on large language models! #AI #MachineLearning",
  "mediaType": "text",
  "reactionsCount": 842,
  "commentsCount": 67,
  "repostsCount": 34,
  "hashtag": "ai",
  "scrapedAt": "2025-05-24T14:00:00.000000+00:00"
}
```

## Cookie vs. Public Mode

| Mode | Cookie | Results Volume | Notes |
|---|---|---|---|
| **Voyager API** | Required | Up to 500 posts per hashtag | Uses authenticated LinkedIn API |
| **Public HTML** | Not needed | Limited (typically 10-20 per hashtag) | Parses embedded SSR JSON from public page |

For best results, provide a valid LinkedIn cookie.

## FAQ

**Do I need to log in to LinkedIn?**
No — the actor works without a cookie by scraping the public hashtag page. However, results will be limited. For full scraping capability, provide your `li_at` cookie.

**How do I get my LinkedIn cookie?**
1. Log in to LinkedIn in your browser
2. Open DevTools (F12) → Application → Cookies → `www.linkedin.com`
3. Copy the value of the `li_at` cookie

**Will this get my account banned?**
The actor uses LinkedIn's official Voyager API with realistic request rates and delays. We recommend using residential proxies for higher volumes to reduce risk.

**How many posts can I scrape per hashtag?**
With a cookie: up to 500. Without a cookie: typically 10-20 posts from the public page.

**What hashtag formats does the actor accept?**
`#AI`, `AI`, `#machine-learning`, `machine-learning` — all are normalized automatically.

**Why are some fields missing from some posts?**
The actor only includes fields that can be reliably populated. Posts with missing author headlines or media types will omit those optional fields.

**Can I scrape multiple hashtags at once?**
Yes — provide a list in the `hashtags` field: `["AI", "marketing", "python"]`.

## Explore the rest of the LinkedIn suite

Need a different LinkedIn surface? Pair this actor with any of the others in the LinkedIn Suite — all published under the same publisher and built to share the same cookie format and output conventions.

| Actor | What it scrapes |
|---|---|
| [LinkedIn Comments Scraper](https://apify.com/crawlerbros/linkedin-comments-scraper) | All comments + reply threads on a post |
| [LinkedIn Company Employees Scraper](https://apify.com/crawlerbros/linkedin-company-employees-scraper) | Employee list for any company (by URN) |
| [LinkedIn Company Info Scraper](https://apify.com/crawlerbros/linkedin-company-info-scraper) | Company About page (size, HQ, industry, specialties) |
| [LinkedIn Company Posts Scraper](https://apify.com/crawlerbros/linkedin-company-posts-scraper) | Posts published from a company page |
| [LinkedIn Events Scraper](https://apify.com/crawlerbros/linkedin-events-scraper) | Events by keyword/URL with full event detail |
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
| [LinkedIn Top Content Scraper](https://apify.com/crawlerbros/linkedin-top-content-scraper) | Trending / top-engagement posts by topic |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-hashtag-posts-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
