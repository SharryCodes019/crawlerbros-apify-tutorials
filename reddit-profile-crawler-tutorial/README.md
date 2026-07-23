# Reddit Profile Crawler Tutorial: Run This Apify Actor with Python

Scrape reddit's profiles with posts and profile information.

This repository shows how to run [Reddit Profile Crawler](https://apify.com/crawlerbros/reddit-profile-crawler) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/reddit-profile-crawler`
- **Apify Store:** [https://apify.com/crawlerbros/reddit-profile-crawler](https://apify.com/crawlerbros/reddit-profile-crawler)
- **SEO title:** Reddit Profile Crawler Tutorial: Run This Apify Actor with Python
- **Description:** Scrape reddit's profiles with posts and profile information.

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

# Reddit Profile Scraper

An Apify Actor for scraping posts and information from Reddit user profiles using browser automation with Playwright.

## Features

- 👤 Scrape multiple user profiles in a single run
- 📊 Extract user information (karma, account age, etc.)
- 📝 Scrape user's posts and comments
- 🔄 Support for different profile sections (overview, submitted, comments, gilded)
- 📈 Multiple sorting options (hot, new, top, controversial)
- 🔄 Automatic pagination support
- 📦 No authentication required for public profiles
- 💾 Data saved in structured JSON format
- 🌐 Browser automation bypasses API restrictions

## Input Parameters

The actor accepts the following input parameters:

| Parameter   | Type    | Required | Default       | Description                                               |
| ----------- | ------- | -------- | ------------- | --------------------------------------------------------- |
| `usernames` | array   | Yes      | `["spez"]`    | List of Reddit usernames to scrape (without 'u/' prefix)  |
| `maxPosts`  | integer | No       | `100`         | Maximum number of posts to scrape from each user (1-1000) |
| `section`   | string  | No       | `"submitted"` | Profile section: `submitted`, `overview`, `gilded`        |
| `sort`      | string  | No       | `"new"`       | How to sort posts: `hot`, `new`, `top`, `controversial`   |

### Example Input

```json
{
  "usernames": ["spez", "example_user"],
  "maxPosts": 50,
  "section": "submitted",
  "sort": "top"
}
```

## Output Fields

The actor extracts two types of data:

### User Profile Information

- `username` - Reddit username
- `post_karma` - Total post/link karma
- `comment_karma` - Total comment karma
- `total_karma` - Combined karma score
- `account_created` - ISO 8601 formatted account creation date

### User Posts

#### Post Information

- `post_id` - Unique post ID
- `post_name` - Full post name in Reddit format (e.g., "t3_abc123")
- `title` - Post title
- `author` - Username (same as scraped user)
- `subreddit` - Subreddit where posted (without r/ prefix)
- `subreddit_prefixed` - Subreddit with r/ prefix

#### Engagement Metrics

- `score` - Post score/karma (upvotes minus downvotes)
- `num_comments` - Number of comments on the post

#### Links

- `url` - URL of the linked content (external URL or permalink)
- `permalink` - Direct link to the Reddit post

#### Metadata

- `domain` - Domain of the linked content
- `is_self_post` - Boolean indicating if it's a text post
- `link_flair` - Post flair/tag text

#### Timestamps

- `created_utc` - Unix timestamp when posted
- `created_at` - ISO 8601 formatted datetime

#### Flags

- `is_stickied` - Boolean indicating if post is stickied
- `is_nsfw` - Boolean indicating if post is NSFW

### Example Output

**User Info:**

```json
{
  "username": "spez",
  "post_karma": 155234,
  "comment_karma": 892456,
  "total_karma": 1047690,
  "account_created": "2005-06-06T04:00:00+00:00"
}
```

**User Post:**

```json
{
  "post_id": "abc123",
  "post_name": "t3_abc123",
  "title": "Announcing new Reddit features",
  "author": "spez",
  "subreddit": "announcements",
  "subreddit_prefixed": "r/announcements",
  "score": 15234,
  "num_comments": 1250,
  "url": "https://old.reddit.com/r/announcements/comments/abc123/...",
  "permalink": "https://old.reddit.com/r/announcements/comments/abc123/...",
  "domain": "self.announcements",
  "is_self_post": true,
  "link_flair": "Admin Post",
  "created_utc": 1728912645,
  "created_at": "2025-10-14T12:30:45",
  "is_stickied": true,
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

2. **Set up input** in `storage/key_value_stores/default/INPUT.json`:

   ```json
   {
     "usernames": ["spez"],
     "maxPosts": 50,
     "section": "submitted",
     "sort": "top"
   }
   ```

3. **Run the actor**:

   ```bash
   python -m src
   ```

4. **Check results** in `storage/datasets/default/`

### On Apify Platform

1. **Push to Apify**:

   - Login to Apify CLI: `apify login`
   - Initialize: `apify init` (if not already done)
   - Push to Apify: `apify push`

2. **Or manually upload**:

   - Create a new actor on Apify platform
   - Upload all files including `Dockerfile`, `requirements.txt`, and `.actor/` directory

3. **Configure and run**:
   - Set input parameters in the Apify console
   - Enter Reddit usernames
   - Select section and sort options
   - Click "Start" to run the actor
   - Download results from the dataset tab

## Profile Sections

### Overview (default)

Shows a mix of posts and comments from the user's profile. **Note:** The scraper extracts only posts from this section. Comments are skipped. Use `section="submitted"` for posts only or `section="comments"` if you need comments.

### Submitted

Shows only posts (links and self posts) submitted by the user. This is the recommended section for extracting posts.

### Comments

Shows only comments made by the user. **Note:** Currently, the scraper is optimized for posts. For comments, use the dedicated Reddit Comment Scraper actor.

### Gilded

Shows posts and comments that received Reddit awards/gilding. Only posts will be extracted from this section.

## Technical Details

### Browser Automation

- Uses **Playwright** with Chromium browser
- Scrapes `old.reddit.com/user/{username}` for better compatibility
- Implements anti-detection measures:
  - Custom User-Agent headers
  - Disabled automation flags
  - Browser fingerprint masking

### Features

- **Automatic pagination**: Clicks "next" button to load more posts
- **Smart extraction**: Handles both posts and comments
- **User info extraction**: Parses karma and account details
- **Error handling**: Gracefully handles deleted accounts and private profiles

### Performance

- Headless browser mode for efficiency
- Optimized page load strategy (`domcontentloaded`)
- Configurable wait times and timeouts
- Sequential processing with delays between users

## Limitations

- Only works with public user profiles
- Cannot scrape private/suspended accounts
- Browser automation is slower than direct API calls but more reliable
- Maximum 1000 posts per user (configurable)
- Hidden karma scores may show as 0

## Dependencies

- `apify>=2.1.0` - Apify SDK for Python
- `playwright~=1.40.0` - Browser automation framework
- `beautifulsoup4~=4.12.0` - HTML parsing library

## Troubleshooting

### Timeout Issues

If you encounter timeout errors:

- Check if the username is correct (without 'u/' prefix)
- Verify the user profile is public
- Increase timeout values if needed

### No Posts Found

If no posts are returned:

- User may have no posts in the selected section
- User account might be suspended or deleted
- Try different sections (overview, submitted, comments)

### Private/Suspended Accounts

- Private profiles cannot be scraped
- Suspended accounts show no content
- This is normal Reddit behavior

## Use Cases

- **User Activity Analysis**: Track user posting patterns and engagement
- **Content Research**: Study what type of content users post
- **Karma Analysis**: Analyze karma distribution across subreddits
- **Profile Monitoring**: Monitor specific user accounts
- **Data Collection**: Build datasets for research or analysis

## License

This actor is provided as-is for scraping public Reddit data in accordance with Reddit's terms of service.

## Notes

- This scraper uses browser automation to access Reddit's public web interface
- Always respect Reddit's robots.txt and terms of service
- Use responsibly and avoid overwhelming Reddit's servers
- Consider implementing additional rate limiting for large-scale scraping
- The actor works best with the Apify platform's infrastructure
- Users with extensive post history may take longer to scrape

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/reddit-profile-crawler)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
