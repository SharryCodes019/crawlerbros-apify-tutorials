# Boxing Stats Scraper Tutorial: Run This Apify Actor with Python

Scrape boxing fighter profiles and fight records using TheSportsDB free API.

This repository shows how to run [Boxing Stats Scraper](https://apify.com/crawlerbros/boxing-stats-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/boxing-stats-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/boxing-stats-scraper](https://apify.com/crawlerbros/boxing-stats-scraper)
- **SEO title:** Boxing Stats Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape boxing fighter profiles and fight records using TheSportsDB free API.

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

# Boxing Stats Scraper

Scrape professional boxing fighter profiles, weight divisions, and career data using [TheSportsDB](https://www.thesportsdb.com/) free public API.

## Features

- **search** mode: Find any boxer by name
- **teams** mode: List all boxing weight divisions

## Input

| Field | Type | Description |
|-------|------|-------------|
| mode | select | search / teams |
| searchQuery | string | Boxer name to search |
| weightClass | select | Filter by weight class |
| maxItems | integer | Max records (1-200) |

## Output

Records include fighterId, fighterName, team, nationality, position, height, weight, birthDate, imageUrl, profileUrl.

## FAQ

**Is an API key required?** No, TheSportsDB free tier is used.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/boxing-stats-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
