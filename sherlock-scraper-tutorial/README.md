# Sherlock Scraper Tutorial: Run This Apify Actor with Python

Search for usernames across 400+ social networks and websites. Find all social media accounts linked to a username using the Sherlock OSINT tool.

This repository shows how to run [Sherlock Scraper](https://apify.com/crawlerbros/sherlock-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/sherlock-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/sherlock-scraper](https://apify.com/crawlerbros/sherlock-scraper)
- **SEO title:** Sherlock Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search for usernames across 400+ social networks and websites. Find all social media accounts linked to a username using the Sherlock OSINT tool.

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

# Sherlock Username Search

Search for usernames across **400+ social networks** and websites. Find all social media accounts linked to a given username using Sherlock, the most popular open-source OSINT tool for username reconnaissance.

## What does Sherlock Username Search do?

This actor takes one or more usernames and searches across 400+ popular platforms — including GitHub, Twitter/X, Instagram, Reddit, TikTok, LinkedIn, YouTube, and hundreds more — to find matching profiles. It returns a list of confirmed profile URLs for each username.

## Features

- Search **400+ social networks** in a single run
- **Batch processing** — search multiple usernames at once
- **Wildcard expansion** — use `{?}` to search username variations (e.g., `john{?}doe` searches `john_doe`, `john-doe`, `john.doe`)
- **No login required** — works with publicly available information only
- **Fast execution** — typically 1-2 minutes per username
- Export results as JSON, CSV, Excel, or other formats

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `usernames` | Array of strings | Yes | Usernames to search for. Supports `{?}` wildcard for variations. |

### Example Input

```json
{
  "usernames": ["johndoe", "alice_smith"]
}
```

### Wildcard Example

```json
{
  "usernames": ["john{?}doe"]
}
```

This expands to search for: `john_doe`, `john-doe`, `john.doe`

## Output

Each result contains the username and an array of discovered profile URLs.

| Field | Type | Description |
|-------|------|-------------|
| `username` | String | The username that was searched |
| `links` | Array of strings | URLs of social media profiles where the username was found |

### Example Output

```json
{
  "username": "johndoe",
  "links": [
    "https://github.com/johndoe",
    "https://www.reddit.com/user/johndoe",
    "https://www.instagram.com/johndoe",
    "https://twitter.com/johndoe",
    "https://www.tiktok.com/@johndoe"
  ]
}
```

## Supported Platforms

Sherlock checks 400+ platforms including:

- **Social Media**: Twitter/X, Instagram, Facebook, TikTok, Snapchat, Reddit, Mastodon, Bluesky
- **Professional**: LinkedIn, GitHub, GitLab, Stack Overflow, Kaggle, LeetCode
- **Content**: YouTube, Twitch, SoundCloud, Spotify, Medium, DeviantArt, Behance
- **Gaming**: Steam, Roblox, Chess.com, Lichess
- **Communication**: Discord, Telegram, Signal
- And 350+ more platforms

## Use Cases

- **OSINT Investigations** — Discover all online accounts associated with a username
- **Social Media Auditing** — Map a person's or brand's online presence
- **Username Availability** — Check if a username is taken across major platforms
- **Digital Forensics** — Find accounts for security research purposes
- **Brand Monitoring** — Track brand name usage across social networks

## FAQ

### How many social networks does Sherlock search?

Sherlock searches over 400 social networks and websites, including all major platforms like Twitter, Instagram, GitHub, Reddit, TikTok, and hundreds more.

### How long does a search take?

A single username search typically takes 1-2 minutes. Multiple usernames are processed sequentially.

### Does it find private or deleted accounts?

No. Sherlock only finds publicly accessible profiles. Private accounts, deleted accounts, or accounts with restricted visibility will not appear in results.

### What does the {?} wildcard do?

The `{?}` wildcard expands a username into three variations using common separators: underscore (`_`), hyphen (`-`), and period (`.`). For example, `john{?}doe` searches for `john_doe`, `john-doe`, and `john.doe`.

### Can I search for multiple usernames at once?

Yes. Simply add multiple usernames to the `usernames` array. Each username produces a separate result with its own list of found profiles.

### Are there any rate limits?

Sherlock makes one request per site per username. Some websites may temporarily block requests if they detect automated access, which may result in those sites not appearing in results.

### Does this require a login or API key?

No. Sherlock works entirely with publicly accessible information and does not require any authentication or API keys.

### Can false positives occur?

Yes, occasionally. Some websites may report a username as existing when the page actually shows an error or belongs to a different user. Review the profile links to confirm accuracy.

### What output formats are available?

Results can be exported as JSON, CSV, Excel (XLSX), HTML, RSS, or XML directly from the Apify platform.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/sherlock-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
