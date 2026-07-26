# Instagram Tagged Posts Scraper Tutorial: Run This Apify Actor with Python

Extracts posts where a specific Instagram user is tagged by others. Returns complete post data including likes, comments, captions, media URLs, and author details with profile pictures and verification status.

This repository shows how to run [Instagram Tagged Posts Scraper](https://apify.com/crawlerbros/instagram-tagged-posts-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-tagged-posts-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-tagged-posts-scraper](https://apify.com/crawlerbros/instagram-tagged-posts-scraper)
- **SEO title:** Instagram Tagged Posts Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extracts posts where a specific Instagram user is tagged by others. Returns complete post data including likes, comments, captions, media URLs, and author details with profile pictures and verification status.

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

# Instagram Tagged Posts Scraper

Extract posts where a user is tagged on Instagram. This scraper navigates to the "Tagged" tab of any Instagram profile and extracts all posts where the target user has been tagged by others.

## Features

- 🏷️ **Tagged Posts Extraction**: Scrapes posts from the `/tagged/` tab of any Instagram profile
- 📊 **Engagement Metrics**: Extracts likes, comments, and views for each post
- 📸 **Media URLs**: Collects image and video URLs from posts
- 👤 **Author Information**: Gets details about who posted/tagged the user
- 🔐 **Cookie Authentication**: Supports MongoDB cookie rotation and file-based cookies
- 🛡️ **Anti-Detection**: Human behavior simulation, stealth scripts, and random delays
- 📧 **Email Alerts**: Automatic notifications when cookies fail or are exhausted

## Input Parameters

| Parameter                 | Type    | Required | Default           | Description                                     |
| ------------------------- | ------- | -------- | ----------------- | ----------------------------------------------- |
| `username`                | String  | Yes      | -                 | Instagram username whose tagged posts to scrape |
| `maxPosts`                | Integer | No       | 12                | Maximum number of tagged posts to extract       |
| `cookies`                 | String  | No       | -                 | Instagram cookies in JSON format                |
| `sessionName`             | String  | No       | "default_session" | Session name for cookie persistence             |
| `minDelayBetweenRequests` | Integer | No       | 3                 | Minimum delay between requests (seconds)        |
| `maxDelayBetweenRequests` | Integer | No       | 7                 | Maximum delay between requests (seconds)        |
| `humanizeBehavior`        | Boolean | No       | true              | Enable human-like behavior simulation           |

## Example Input

```json
{
  "username": "instagram",
  "maxPosts": 20,
  "humanizeBehavior": true
}
```

## Output Format

Each tagged post is returned with the following structure:

```json
{
  "tagged_username": "instagram",
  "post_url": "https://www.instagram.com/p/ABC123/",
  "description": "Post caption here...",
  "post_type": "image",
  "like_count": 12345,
  "comment_count": 234,
  "view_count": 0,
  "pub_date": "2024-01-15T10:30:00",
  "media_urls": ["https://instagram.com/..."],
  "scraped_at": "2024-01-20T15:30:00.000Z",
  "authorMeta": {
    "username": "photographer",
    "full_name": "John Photographer",
    "profile_url": "https://www.instagram.com/photographer/",
    "is_verified": false
  }
}
```

## Cookie Authentication

### Option 1: MongoDB Cookie Rotation (Automatic)

The scraper automatically connects to MongoDB for cookie rotation. This provides:

- Round-robin cookie selection
- Automatic failover when cookies fail
- Usage tracking and failure detection
- Email alerts for cookie failures

### Option 2: Manual Cookie Input

Export cookies from your browser and provide them in the `cookies` parameter:

1. Install a browser extension like "Cookie-Editor" or "EditThisCookie"
2. Log into Instagram in your browser
3. Export cookies as JSON
4. Paste the JSON into the `cookies` input parameter

### Option 3: File-Based Cookies

Place a cookies file in the scraper directory:

- `www.instagram.com.cookies (1).json`
- `www.instagram.com.cookies.json`
- `cookies.json`
- `IG_Cookies.json`

## Anti-Blocking Measures

This scraper includes multiple anti-detection features:

1. **Stealth Scripts**: Override navigator properties to avoid bot detection
2. **Human Behavior Simulation**: Random mouse movements, scrolling, and delays
3. **Cookie Rotation**: Automatic rotation through multiple accounts
4. **Random Delays**: Variable delays between requests
5. **Firefox Browser**: Uses Firefox which has better anti-detection properties

## Error Handling

The scraper handles various error scenarios:

- **Profile Not Found**: Returns error message if profile doesn't exist
- **Private Account**: Tagged posts are not accessible for private accounts
- **No Tagged Posts**: Returns message if user has no tagged posts
- **Rate Limiting**: Automatically stops if Instagram blocks access
- **Cookie Failure**: Rotates to next cookie and sends email alert

## Limitations

- Tagged posts are only visible if the target profile is public
- Instagram may limit access without authentication
- Rate limits apply - avoid scraping too many posts too quickly
- Some posts may be restricted based on account settings

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install firefox

# Run locally
apify run
```

## Deployment to Apify

```bash
# Login to Apify
apify login

# Push to Apify
apify push
```

## Support

If you encounter issues:

1. Ensure cookies are valid and not expired
2. Check if the target profile is public
3. Reduce `maxPosts` to avoid rate limiting
4. Enable `humanizeBehavior` to reduce detection risk

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-tagged-posts-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
