# Instagram Profile Scraper Tutorial: Run This Apify Actor with Python

Extract comprehensive data from Instagram profiles including posts, reels, photos, and engagement metrics.

This repository shows how to run [Instagram Profile Scraper](https://apify.com/crawlerbros/instagram-profile-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-profile-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-profile-scraper](https://apify.com/crawlerbros/instagram-profile-scraper)
- **SEO title:** Instagram Profile Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract comprehensive data from Instagram profiles including posts, reels, photos, and engagement metrics.

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

# Instagram Profile Scraper

Extract complete profile information and posts from any public Instagram account. Get follower counts, bio, verification status, and detailed post data including captions, engagement metrics, media URLs, and more.

Perfect for influencer research, competitor analysis, content auditing, and brand monitoring.

## What data can you extract?

For every post the scraper returns:

| Field           | Type      | Description                                                             |
| --------------- | --------- | ----------------------------------------------------------------------- |
| `username`      | `string`  | Instagram username of the post author                                   |
| `post_url`      | `string`  | Direct URL to the Instagram post                                        |
| `description`   | `string`  | Full caption text of the post                                           |
| `post_type`     | `string`  | Type of post: `image`, `video`, or `carousel`                           |
| `like_count`    | `integer` | Number of likes on the post                                             |
| `comment_count` | `integer` | Number of comments on the post                                          |
| `view_count`    | `integer` | Number of views (video and reel posts only, `null` for images)          |
| `pub_date`      | `string`  | Publication date in ISO 8601 format                                     |
| `media_urls`    | `array`   | Direct URLs to all images and/or videos in the post                     |
| `scraped_at`    | `string`  | Timestamp when this record was collected                                |
| `authorMeta`    | `object`  | Full profile data of the post author (see fields below)                 |

The `authorMeta` object contains:

| Field                    | Type      | Description                                          |
| ------------------------ | --------- | ---------------------------------------------------- |
| `username`               | `string`  | Instagram username                                   |
| `full_name`              | `string`  | Full display name                                    |
| `biography`              | `string`  | Profile bio text                                     |
| `profile_pic_url`        | `string`  | URL of the profile picture                           |
| `is_verified`            | `boolean` | Whether the account has a verified badge             |
| `is_private`             | `boolean` | Whether the account is private                       |
| `is_business`            | `boolean` | Whether the account is a business account            |
| `followers_count`        | `integer` | Number of followers                                  |
| `following_count`        | `integer` | Number of accounts followed                          |
| `posts_count`            | `integer` | Total posts on the profile                           |
| `profile_url`            | `string`  | Full URL to the Instagram profile                    |
| `external_url`           | `string`  | Link in bio (when present)                           |
| `email`                  | `string`  | Public business email (when present)                 |
| `phone`                  | `string`  | Public business phone (when present)                 |
| `category`               | `string`  | Account category e.g. "Nutritionist" (when present)  |

When `maxPosts` is set to `0`, only a single profile record is returned (no post-level fields, just `authorMeta`).

## How to use

1. **Enter the username** — paste the Instagram username, with or without the `@`
2. **Set how many posts to scrape** — use `0` for profile-only, or any number up to 500
3. **Run the scraper** — click Start and results appear in the dataset automatically
4. **Export your data** — download as JSON, CSV, or Excel, or connect via API

No cookies or authentication setup required — the scraper handles access automatically.

## Input

| Field         | Type      | Required | Default            | Description                                           |
| ------------- | --------- | -------- | ------------------ | ----------------------------------------------------- |
| `username`    | `string`  | Yes      | —                  | Instagram username to scrape (with or without `@`)    |
| `maxPosts`    | `integer` | No       | `12`               | Posts to extract (0–500). Set to `0` for profile only |
| `cookies`     | `string`  | No       | —                  | Custom Instagram cookies in JSON format (optional)    |
| `sessionName` | `string`  | No       | `default_session`  | Name used to persist the session between runs         |

### Example input

```json
{
  "username": "cristiano",
  "maxPosts": 50
}
```

## Output

### Example output (posts)

```json
[
  {
    "username": "instagram",
    "post_url": "https://www.instagram.com/instagram/reel/DXxFT1zPFQC/",
    "description": "Make your pics look like film with @meta.ai ✨",
    "post_type": "video",
    "like_count": 131990,
    "comment_count": 3600,
    "view_count": null,
    "pub_date": "2026-04-30T19:06:13",
    "media_urls": [
      "https://scontent.cdninstagram.com/.../video.mp4",
      "https://scontent.cdninstagram.com/.../thumbnail.jpg"
    ],
    "scraped_at": "2026-05-01T12:32:03.229693",
    "authorMeta": {
      "username": "instagram",
      "full_name": "Instagram",
      "biography": "Discover what's new on Instagram 🔎✨",
      "profile_pic_url": "https://scontent.cdninstagram.com/.../profile.jpg",
      "is_verified": true,
      "is_private": false,
      "is_business": false,
      "followers_count": 700870854,
      "following_count": 175,
      "posts_count": 8423,
      "profile_url": "https://www.instagram.com/instagram/",
      "external_url": "http://help.instagram.com/"
    }
  }
]
```

### Example output (profile only, `maxPosts: 0`)

```json
[
  {
    "authorMeta": {
      "username": "abbysnutritionhub",
      "full_name": "Abby's Nutrition Hub",
      "biography": "Better ingredients, better you🍀",
      "profile_pic_url": "https://scontent.cdninstagram.com/.../profile.jpg",
      "is_verified": true,
      "is_private": false,
      "is_business": true,
      "followers_count": 30213,
      "following_count": 12,
      "posts_count": 89,
      "profile_url": "https://www.instagram.com/abbysnutritionhub/",
      "category": "Nutritionist"
    }
  }
]
```

## Use cases

- **Influencer vetting** — verify follower counts, engagement rates, and account authenticity
- **Competitor analysis** — track competitor content strategy and posting frequency
- **Content research** — analyze what post types and topics drive the most engagement
- **Brand monitoring** — audit brand accounts and measure content performance over time
- **Audience insights** — understand posting patterns and community engagement
- **Media archival** — collect and store post media URLs for backup or legal purposes

## Integrations

Connect results to your existing tools and workflows:

- **Webhooks** — get notified instantly when a run finishes
- **Apify API** — pull data directly into your application
- **Scheduled runs** — monitor profiles on a recurring schedule
- Export to **Google Sheets**, **Slack**, **Zapier**, **Make**, and more

## FAQ

### Do I need to provide cookies or an Instagram account?

No. The scraper authenticates automatically — you can leave the `cookies` field empty and it will work out of the box.

### Can I scrape private accounts?

No. Only publicly accessible profiles and their posts can be scraped. Private accounts return only the profile metadata with a note that posts are not accessible.

### How many posts can I extract per run?

Up to 500 posts per run. Set `maxPosts` to any value from 1 to 500. To fetch only the profile data without any posts, set it to `0`.

### What post types are supported?

All post types: images, videos, reels, and carousels. For carousel posts all individual media URLs are included in the `media_urls` array.

### Why is `view_count` null on some posts?

Instagram does not expose view counts for image posts. The `view_count` field is populated for video and reel posts only. A `null` value means the post is not a video — it is not an error.

### What happens if a profile does not exist?

The scraper fails with a clear error message: `Profile @username does not exist or is not available`. No dataset record is pushed.

### What format can I export the data in?

JSON, CSV, Excel, XML, or via the Apify API. You can also stream results directly into Google Sheets, Slack, or other integrations using Apify's built-in connectors.

### How often can I run it?

As often as needed. Use Apify's built-in scheduler to monitor profiles on a daily, weekly, or custom cadence.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-profile-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
