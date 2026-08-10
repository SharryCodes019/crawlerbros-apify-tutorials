# LinkedIn Post Search Scraper Tutorial: Run This Apify Actor with Python

Search LinkedIn for posts by keyword, topic, or hashtag. Filter by date posted and sort by relevance or recency.

This repository shows how to run [LinkedIn Post Search Scraper](https://apify.com/crawlerbros/linkedin-post-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-post-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-post-search-scraper](https://apify.com/crawlerbros/linkedin-post-search-scraper)
- **SEO title:** LinkedIn Post Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search LinkedIn for posts by keyword, topic, or hashtag. Filter by date posted and sort by relevance or recency.

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

# LinkedIn Post Search Scraper

Search LinkedIn for posts by keyword, topic, or hashtag using the LinkedIn Voyager API (HTTP-only — no browser required). Returns matching posts with full content, author details, and engagement metrics. Supports filtering by date posted and sorting by relevance or recency.

---

## What It Does

- Searches LinkedIn posts using any keyword, phrase, or hashtag
- Returns post content, author name, headline, profile URL, and post URL
- Includes engagement metrics: reactions count and comments count
- Filters by date posted: past 24 hours, past week, past month, or any time
- Sorts by most relevant or most recent
- Deduplicates results automatically
- Requires a valid LinkedIn session cookie (`li_at`)

---

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `searchQuery` | String | Yes | Keywords, phrase, or hashtag to search. E.g. `artificial intelligence`, `#MachineLearning`, `product launch` |
| `cookie` | String | Yes | LinkedIn session cookie. Accepts plain `li_at` value or full browser cookies JSON array |
| `sortBy` | Select | No | `relevance` (default) or `recency` |
| `datePosted` | Select | No | `""` Any time (default), `r86400` Past 24h, `r604800` Past week, `r2592000` Past month |
| `maxResults` | Integer | No | Max posts to return. Default: 25, max: 100 |
| `proxyConfiguration` | Object | No | Apify proxy configuration. Defaults to residential then datacenter AUTO |

---

## Output

Each item in the dataset represents one LinkedIn post:

| Field | Type | Description |
|---|---|---|
| `postId` | String | Numeric LinkedIn activity ID |
| `postUrl` | String | Direct URL to the post |
| `authorName` | String | Display name of the post author |
| `authorProfileUrl` | String | Author's LinkedIn profile URL |
| `authorHeadline` | String | Author's headline (job title, company, location) |
| `postedAt` | String | When the post was published (e.g. "1 day ago", "2 weeks ago") |
| `content` | String | Post text content (may be truncated for long posts) |
| `mediaType` | String | Always `text` for search results (detailed media info not available via search API) |
| `reactionsCount` | Integer | Number of reactions on the post |
| `commentsCount` | Integer | Number of comments on the post |
| `scrapedAt` | String | ISO 8601 UTC timestamp when the record was collected |

### Example Output

```json
{
  "postId": "7329761432933134337",
  "postUrl": "https://www.linkedin.com/feed/update/urn:li:activity:7329761432933134337/",
  "authorName": "Jane Doe",
  "authorProfileUrl": "https://www.linkedin.com/in/janedoe/",
  "authorHeadline": "Senior AI Engineer at Acme Corp | San Francisco",
  "postedAt": "1 day ago",
  "content": "Excited to share that we just launched our new AI-powered product! After 18 months of development...",
  "mediaType": "text",
  "reactionsCount": 347,
  "commentsCount": 42,
  "scrapedAt": "2026-06-08T12:34:56.789000+00:00"
}
```

---

## Cookie Setup Guide

LinkedIn requires authentication to access search results. You need to provide your `li_at` session cookie.

### Option 1: Plain `li_at` value (simplest)

1. Open [linkedin.com](https://www.linkedin.com) in your browser and log in
2. Open **DevTools** (`F12` or right-click → Inspect)
3. Go to **Application** → **Cookies** → `https://www.linkedin.com`
4. Find the cookie named `li_at`
5. Copy the **Value** and paste it into the `cookie` input field

### Option 2: Full browser cookies JSON array

1. Install a browser extension like [EditThisCookie](https://www.editthiscookie.com/) or [Cookie-Editor](https://cookie-editor.com/)
2. Log into LinkedIn
3. Export all cookies as JSON from the extension
4. Paste the full JSON array into the `cookie` input field

> **Note**: Your cookie is used only for authentication with LinkedIn's API. Never share it publicly. Cookies typically expire after 1 year or when you log out of LinkedIn.

---

## Keyword Search vs Hashtag Search

| Search Type | Example Input | What It Finds |
|---|---|---|
| Keyword phrase | `artificial intelligence` | Posts mentioning the exact phrase or related terms |
| Single keyword | `startup` | Posts containing the word startup |
| Hashtag | `#MachineLearning` | Posts tagged with that hashtag |
| Multi-word | `product launch announcement` | Posts about product launches |
| Person mention | `Elon Musk Tesla` | Posts mentioning Elon Musk in context of Tesla |

---

## Sort and Filter Combinations

| `sortBy` | `datePosted` | What You Get |
|---|---|---|
| `relevance` | (empty) | Most relevant posts of all time |
| `relevance` | `r86400` | Most relevant posts from last 24 hours |
| `recency` | (empty) | Newest posts first, no date filter |
| `recency` | `r86400` | Most recent posts from last 24 hours |
| `recency` | `r604800` | Most recent posts from last week |
| `recency` | `r2592000` | Most recent posts from last month |

---

## FAQs

**How many posts can I scrape per run?**
Up to 100 posts per run (set via `maxResults`). LinkedIn's search API returns results in pages of 10.

**Why are some engagement counts zero?**
LinkedIn's search API does not always return engagement data in search result previews. When the `socialProofText` field is absent from the result, counts default to 0. Use the [LinkedIn Post Scraper](https://apify.com/crawlerbros/linkedin-post-scraper) actor to get full engagement data for specific posts.

**Why is post content sometimes truncated?**
Search results return a content snippet, not the full post text. Long posts are cut off by LinkedIn's search API. To retrieve the full text, visit the post URL directly.

**What causes rate limiting?**
LinkedIn throttles search requests. The actor automatically adds delays between requests (2–5 seconds) and retries on 429 responses. If you need to scrape large volumes, increase the delay by reducing `maxResults` and running multiple actors.

**Do I need a proxy?**
A proxy is recommended but not required. The actor first tries a residential proxy (best for LinkedIn), then falls back to datacenter proxy, then direct connection. You can also supply a custom `proxyConfiguration`.

**Why does the actor fail with "cookie is invalid or expired"?**
Your `li_at` cookie has expired or LinkedIn invalidated the session. Log out and back into LinkedIn, then copy the fresh `li_at` value.

**Can I search posts in other languages?**
Yes. Enter your search query in any language. LinkedIn returns results in the language of the posts matching your query.

**Is logging in or a paid LinkedIn account required?**
No paid subscription is required. Any standard LinkedIn account works. The `li_at` session cookie from a free account is sufficient.

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

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-post-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
