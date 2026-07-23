# SocialBlade Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape public SocialBlade creator stats for YouTube, TikTok, Instagram, Twitch, and Facebook. Returns followers, views, grade, rank, history, creator metadata. HTTP-only, no login.

This repository shows how to run [SocialBlade Stats Scraper](https://apify.com/crawlerbros/socialblade-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/socialblade-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/socialblade-scraper](https://apify.com/crawlerbros/socialblade-scraper)
- **SEO title:** SocialBlade Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public SocialBlade creator stats for YouTube, TikTok, Instagram, Twitch, and Facebook. Returns followers, views, grade, rank, history, creator metadata. HTTP-only, no login.

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

# SocialBlade Stats Scraper

Scrape public SocialBlade creator stats across **YouTube, TikTok, Instagram, Twitch, and Facebook**. HTTP-only, no login, no API key.

## What this actor extracts

Per profile:

- `type`, `platform`, `input`, `url`
- `id`, `displayName`, `avatar`, `banner`
- `country`, `description`
- `channelType`, `category` (platform-dependent)
- `createdAt`
- Platform-appropriate primary metric: `subscribers` (YouTube) or `followers` (TikTok / Instagram / Twitch / Facebook)
- `views`, `videos`
- `grade` (SocialBlade letter grade)
- `ranks` — `sb`, `subscribers`/`followers`, `views`, `country`, `category`
- `socials` — linked social accounts
- `history` — up to 15 days of daily snapshots (subscribers/followers, views, videos)
- `scrapedAt`

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | string[] | List of SocialBlade profile URLs. Any form: `/youtube/handle/...`, `/youtube/channel/...`, `/youtube/user/...`, `/tiktok/user/...`, `/instagram/user/...`, `/twitch/user/...`, `/facebook/page/...` |
| `profiles` | object[] | Alternative: `[{platform, username}]`. YouTube usernames auto-fall back from `/user/` to `/handle/` if the first lookup returns nothing. |
| `platform` | enum | Default platform for bare strings. |
| `includeHistory` | bool | Include last 15 days of daily snapshots. Default `true`. |
| `maxItems` | integer | Max profiles to process. Default 50, cap 500. |

At least one of `startUrls` / `profiles` required.

## How it works

SocialBlade is a Next.js app that hydrates profile pages from tRPC queries embedded in the `__NEXT_DATA__` JSON script block. The actor issues a single HTTP GET per profile, parses that script, and extracts the `{platform}.user` / `{platform}.page` / `{platform}.history` query states.

Chrome TLS fingerprinting is emulated via `curl_cffi` (chrome131). No cookies, no login, no proxy configuration. If the Apify datacenter IP ever gets blocked, the actor transparently escalates to the Apify RESIDENTIAL US pool with per-profile session rotation.

## FAQ

**Which URL form should I use?** For YouTube, prefer `/handle/<name>` or `/channel/<UCxxxx>` — the `/user/<name>` form uses SocialBlade's legacy username index and often maps to the wrong account. TikTok / Instagram / Twitch use `/user/<name>`. Facebook uses `/page/<name>`.

**Do I need a proxy?** No — it's baked into the actor if ever needed.

**Does it include paid Social Blade Pro data?** No — only publicly visible metrics.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/socialblade-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
