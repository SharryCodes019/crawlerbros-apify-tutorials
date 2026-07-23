# Social Media Finder Tutorial: Run This Apify Actor with Python

Find social media profiles across 400+ platforms by username. Search Instagram, TikTok, YouTube, LinkedIn, GitHub, Twitter/X, Reddit, Snapchat, Steam, Twitch, Pinterest, Medium, Discord, Telegram, Spotify, and hundreds more.

This repository shows how to run [Social Media Finder](https://apify.com/crawlerbros/social-media-finder) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/social-media-finder`
- **Apify Store:** [https://apify.com/crawlerbros/social-media-finder](https://apify.com/crawlerbros/social-media-finder)
- **SEO title:** Social Media Finder Tutorial: Run This Apify Actor with Python
- **Description:** Find social media profiles across 400+ platforms by username. Search Instagram, TikTok, YouTube, LinkedIn, GitHub, Twitter/X, Reddit, Snapchat, Steam, Twitch, Pinterest, Medium, Discord, Telegram, Spotify, and hundreds more.

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

# Social Media Finder

Find social media profiles across **400+ platforms** by username or nickname. Search Instagram, TikTok, YouTube, LinkedIn, GitHub, Twitter/X, Reddit, Snapchat, Steam, Twitch, Pinterest, Medium, Discord, Telegram, Spotify, SoundCloud, Mastodon, Bluesky, and hundreds more — all in a single run.

## Features

- Search **400+ social media platforms** simultaneously
- Find all public profiles linked to a username or nickname
- Filter to specific platforms or search everywhere
- Batch processing — search multiple usernames at once
- Wildcard support — `john{?}doe` expands to `john_doe`, `john-doe`, `john.doe`
- No login or API keys required
- Export results in JSON, CSV, Excel, or XML

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| Usernames | string[] | Yes | — | List of usernames or nicknames to search |
| Platforms | string[] | No | All 400+ | Filter to specific platforms (e.g., Instagram, GitHub) |
| Max Results | integer | No | No limit | Maximum total results to return |

### Example Input

```json
{
  "queries": ["johndoe", "jane_smith"],
  "platforms": ["Instagram", "GitHub", "Twitter", "YouTube"],
  "maxResults": 100
}
```

## Output

Each result row contains:

| Field | Type | Description |
|-------|------|-------------|
| `username` | string | The searched username |
| `platform` | string | Platform name where profile was found |
| `url` | string | Direct URL to the profile |
| `status` | string | "Found" or "Not Found" |

### Example Output

```json
[
  {
    "username": "johndoe",
    "platform": "GitHub",
    "url": "https://github.com/johndoe",
    "status": "Found"
  },
  {
    "username": "johndoe",
    "platform": "Instagram",
    "url": "https://instagram.com/johndoe",
    "status": "Found"
  },
  {
    "username": "johndoe",
    "platform": "Reddit",
    "url": "https://www.reddit.com/user/johndoe",
    "status": "Found"
  }
]
```

## Supported Platforms

Searches **400+** platforms including:

**Social Media:** Instagram, TikTok, Twitter/X, Snapchat, Reddit, Mastodon, Bluesky, Threads

**Video:** YouTube, Twitch, Vimeo, Dailymotion

**Music:** Spotify, SoundCloud, Last.fm, Bandcamp

**Professional:** LinkedIn, GitHub, GitLab, Stack Overflow, Kaggle, LeetCode, Behance

**Gaming:** Steam, Roblox, Chess.com, Lichess, Xbox Gamertag

**Messaging:** Discord, Telegram, Signal

**Other:** Pinterest, Medium, DeviantArt, Flickr, Gravatar, Keybase, Patreon, and hundreds more

## Use Cases

- **Lead enrichment** — Find all social accounts for a prospect by their username
- **Competitive analysis** — Map a competitor's social media presence
- **Background checks** — Verify someone's digital footprint
- **Brand monitoring** — Check if your brand name is taken across platforms
- **Username availability** — See where a username is already claimed
- **OSINT research** — Investigate online presence systematically

## Limitations

- Only finds **public** profiles — private or hidden accounts are not detected
- Username matching is exact — "johndoe" won't find "john.doe" unless you use the `{?}` wildcard
- Some platforms may rate-limit requests, causing occasional misses
- Facebook is not currently supported in the search database

## FAQ

**Q: Do I need any API keys or login credentials?**
A: No. The tool checks publicly accessible profile URLs directly — no authentication needed.

**Q: How long does a search take?**
A: Typically 1-2 minutes per username when searching all 400+ platforms. Filtering to specific platforms is faster.

**Q: What does the {?} wildcard do?**
A: It expands to three common username separators: underscore (`_`), hyphen (`-`), and period (`.`). So `john{?}doe` searches for `john_doe`, `john-doe`, and `john.doe`.

**Q: Why is Facebook not supported?**
A: Facebook does not expose public profile pages in a way that allows username-based lookup without authentication.

**Q: Can I search for email addresses or phone numbers?**
A: No. This tool searches by username/nickname only.

**Q: How accurate are the results?**
A: The tool verifies each profile URL with an HTTP request. "Found" means the profile page exists and returns a valid response. False positives are rare but possible on some platforms.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/social-media-finder)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
