# Odysee Video Scraper Tutorial: Run This Apify Actor with Python

Scrape videos from Odysee.com - a decentralized video platform. Search by keyword, browse by channel, or filter by tag. Returns title, channel, thumbnail, description, duration, tags, and publication date.

This repository shows how to run [Odysee Video Scraper](https://apify.com/crawlerbros/odysee-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/odysee-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/odysee-scraper](https://apify.com/crawlerbros/odysee-scraper)
- **SEO title:** Odysee Video Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape videos from Odysee.com - a decentralized video platform. Search by keyword, browse by channel, or filter by tag. Returns title, channel, thumbnail, description, duration, tags, and publication date.

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

# Odysee Video Scraper

Scrape videos from [Odysee.com](https://odysee.com) — a decentralized video platform powered by the LBRY blockchain. Search by keyword, browse by channel, or filter by tag.

## Features

- **Search mode**: Full-text search across the entire Odysee catalog
- **Channel mode**: Fetch all videos from a specific channel
- **Tag mode**: Browse videos by category tag (science, technology, gaming, etc.)
- Sort by newest, trending, or most-supported
- Structured output: title, channel, thumbnail, description, duration, tags, and publication date

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | string | `search`, `byChannel`, or `byTag` |
| `keyword` | string | Search term (mode=search) |
| `channel` | string | Channel name, e.g. `@veritasium` (mode=byChannel) |
| `tag` | string | Tag to browse, e.g. `technology` (mode=byTag) |
| `orderBy` | string | Sort: `release_time`, `effective_amount`, `trending_group` |
| `maxItems` | integer | Maximum results (1–500) |

## Output

| Field | Type | Description |
|-------|------|-------------|
| `claimId` | string | Odysee unique claim ID |
| `title` | string | Video title |
| `description` | string | Video description (up to 2000 chars) |
| `channelName` | string | Publisher channel name |
| `channelUrl` | string | Direct link to channel page |
| `thumbnailUrl` | string | Thumbnail image URL |
| `durationSeconds` | integer | Video duration in seconds |
| `mediaType` | string | MIME type (e.g., video/mp4) |
| `tags` | array | Content tags |
| `languages` | array | Language codes |
| `publishedAt` | string | ISO 8601 publication date |
| `views` | integer | View count (when available) |
| `viewUrl` | string | Direct link to video page |

## FAQs

**Is authentication required?**
No. The scraper uses Odysee's public LBRY proxy API — no login or API key needed.

**What content is available?**
Odysee hosts educational, news, entertainment, technology, and political content from independent creators.

**Can I get videos from a specific creator?**
Yes — use `mode=byChannel` with the channel name (e.g., `@veritasium` or `@LinusTechTips`).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/odysee-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
