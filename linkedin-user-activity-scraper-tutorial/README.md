# LinkedIn User Activity Scraper Tutorial: Run This Apify Actor with Python

Scrape the recent activity of any LinkedIn user â€" posts they liked, commented on, or reshared. Ideal for sales intelligence and competitive research.

This repository shows how to run [LinkedIn User Activity Scraper](https://apify.com/crawlerbros/linkedin-user-activity-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-user-activity-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-user-activity-scraper](https://apify.com/crawlerbros/linkedin-user-activity-scraper)
- **SEO title:** LinkedIn User Activity Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape the recent activity of any LinkedIn user â€" posts they liked, commented on, or reshared. Ideal for sales intelligence and competitive research.

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

# LinkedIn User Activity Scraper

Scrape the recent activity of any LinkedIn user — the posts they **liked**, **commented on**, or **reshared**. Perfect for sales intelligence (understand what prospects engage with) and competitive research (track what influencers in your space react to).

---

## What it does

For each LinkedIn profile URL you provide, this actor fetches:

| Activity Type | Description |
|---|---|
| **Likes** | Posts the user reacted to with any emoji reaction |
| **Comments** | Posts the user left a comment on |
| **Posts / Reposts** | Original posts and reposts the user published |
| **All** | All three categories in a single run |

---

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `profileUrls` | Array of strings | Yes | LinkedIn profile URLs. Accepts `https://www.linkedin.com/in/username/`, regional variants (`uk.linkedin.com`), or bare usernames. |
| `cookie` | String | Yes | LinkedIn session cookie. Accepts a plain `li_at` value or a full JSON array from a cookie export extension (EditThisCookie, etc.). |
| `activityType` | Enum | No | `all` (default), `likes`, `comments`, or `posts`. |
| `maxActivitiesPerProfile` | Integer | No | Max items per profile per activity type. Default: `50`, max: `500`. |
| `proxyConfiguration` | Object | No | Apify proxy settings. Residential proxy recommended for best reliability. |

### Cookie setup

The easiest way to get your cookie:

1. Log into LinkedIn in your browser.
2. Open **DevTools → Application → Cookies → linkedin.com**.
3. Copy the value of `li_at` and paste it into the **LinkedIn Cookie** field.

For a full cookie export (more reliable): use the [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) extension → Export → paste the entire JSON array.

---

## Output

Each result row represents a single activity item:

| Field | Type | Description |
|---|---|---|
| `activityType` | String | `like`, `comment`, `post`, or `repost` |
| `originalPostUrl` | String | URL of the post on LinkedIn |
| `originalPostId` | String | LinkedIn activity ID |
| `originalAuthorName` | String | Display name of the original post author |
| `originalAuthorProfileUrl` | String | LinkedIn profile URL of the original author |
| `content` | String | Text content of the post |
| `reactedAt` | String | ISO 8601 timestamp of the activity |
| `inputProfileUrl` | String | The profile that was scraped |
| `scrapedAt` | String | ISO 8601 timestamp of when scraping occurred |

### Sample output item

```json
{
  "activityType": "like",
  "originalPostUrl": "https://www.linkedin.com/feed/update/urn:li:activity:7234567890123456789/",
  "originalPostId": "7234567890123456789",
  "originalAuthorName": "Satya Nadella",
  "originalAuthorProfileUrl": "https://www.linkedin.com/in/satyanadella",
  "content": "Excited to share our latest AI innovations...",
  "reactedAt": "2024-11-15T09:32:10.000+00:00",
  "inputProfileUrl": "https://www.linkedin.com/in/williamhgates",
  "scrapedAt": "2024-11-20T14:00:00.000+00:00"
}
```

---

## Use cases

- **Sales intelligence** — See which topics and vendors your prospects engage with before outreach.
- **Competitive research** — Track what content competitors react to; uncover their interests.
- **Influencer analysis** — Identify which posts resonate with thought leaders in your space.
- **Lead enrichment** — Enrich CRM contacts with their recent LinkedIn engagement signals.
- **Content strategy** — Discover what types of posts generate engagement from your target audience.

---

## Limitations

- Requires a valid LinkedIn session cookie (`li_at`). The cookie owner must be able to view the target profile.
- LinkedIn limits how far back activity history goes. Older activity may not be returned.
- LinkedIn may throttle requests. The actor implements automatic retry with exponential backoff.
- Private profiles may not return activity if the cookie owner is not connected.

---

## FAQs

**Q: Will this work on any public LinkedIn profile?**  
A: Activity data is accessible as long as your session cookie can view the profile. Most public profiles work. For private profiles (1st-degree connections only), you need a cookie from an account connected to the target.

**Q: How many activities can I scrape?**  
A: Up to 500 per profile per activity type. For `activityType: all`, this means up to 500 likes + 500 comments + 500 posts = 1,500 items per profile.

**Q: Is a proxy required?**  
A: Optional. The actor works from datacenter IPs, but residential proxy improves reliability. Configure under `proxyConfiguration`.

**Q: My cookie expired — what happens?**  
A: The actor will detect a 401/403 response and stop immediately with a clear error message. Refresh your cookie and re-run.

**Q: Can I scrape multiple profiles?**  
A: Yes. Add all profile URLs to the `profileUrls` array. The actor processes them sequentially to avoid rate limits.

**Q: Why do some items not have `content`?**  
A: Some posts are purely media (images, videos) with no text. Empty fields are omitted from output.

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
| [LinkedIn Top Content Scraper](https://apify.com/crawlerbros/linkedin-top-content-scraper) | Trending / top-engagement posts by topic |

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

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-user-activity-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
