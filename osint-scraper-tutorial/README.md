# OSINT Scraper Tutorial: Run This Apify Actor with Python

Search paste sites and code sharing platforms (Pastebin, GitHub Gist, Ideone, Paste.org, Textbin) for leaked keywords, credentials, and sensitive data using Google SERP-based discovery.

This repository shows how to run [OSINT Scraper](https://apify.com/crawlerbros/osint-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/osint-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/osint-scraper](https://apify.com/crawlerbros/osint-scraper)
- **SEO title:** OSINT Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search paste sites and code sharing platforms (Pastebin, GitHub Gist, Ideone, Paste.org, Textbin) for leaked keywords, credentials, and sensitive data using Google SERP-based discovery.

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

# OSINT Scraper

Search paste sites and code-sharing platforms for keywords using Google Search's `site:` operator. Ideal for security researchers, threat intelligence analysts, and compliance teams looking for leaked credentials, sensitive data, or public mentions of specific terms.

## Supported Sources

| Source | Domain | Description |
|---|---|---|
| **Pastebin** | pastebin.com | The most popular paste site |
| **GitHub Gist** | gist.github.com | GitHub's snippet sharing platform |
| **Ideone** | ideone.com | Online code compiler with shareable pastes |
| **Paste.org** | paste.org | General-purpose paste site |
| **Textbin** | textbin.net | Simple text sharing site |

## How It Works

Many paste sites actively block direct scraping or require paid API access. This scraper sidesteps that by searching Google for indexed paste URLs matching your keywords — Google has already crawled the public content, making it freely discoverable. No authentication, no per-site rate limits, and no residential proxies required.

## Input

| Field | Type | Description |
|---|---|---|
| `searchKeywords` | array of strings | Keywords to search across OSINT sources |
| `sources` | array of strings | Sources to search (default: all). Valid values: `pastebin`, `gist`, `ideone`, `paste_org`, `textbin` |
| `maxItemsPerSource` | integer | Maximum results per source per keyword (default: 10) |

### Example Input

```json
{
    "searchKeywords": ["api_key", "password"],
    "sources": ["pastebin", "gist"],
    "maxItemsPerSource": 5
}
```

## Output

Each dataset item represents one discovered paste or gist:

| Field | Type | Description |
|---|---|---|
| `source` | string | Source platform identifier |
| `url` | string | Direct URL to the paste |
| `title` | string | Paste title or identifier |
| `snippet` | string | Excerpt from the paste content (as indexed by Google) |
| `matchedKeyword` | string | The keyword that matched this result |
| `scrapedAt` | string | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "source": "pastebin",
    "url": "https://pastebin.com/ABC12345",
    "title": "Example Configuration Dump",
    "snippet": "api_key = example_key_value_here, connecting to production environment...",
    "matchedKeyword": "api_key",
    "scrapedAt": "2026-04-10T12:00:00+00:00"
}
```

## FAQ

**Q: Does this scrape paste sites directly?**
No — it searches Google for indexed paste URLs. This avoids anti-bot protection and API rate limits on the individual sites.

**Q: Can I scrape the full paste content?**
The scraper returns the snippet Google shows in search results (typically 100–500 characters). Fetching the full paste is out of scope because many paste sites block it.

**Q: Is this legal?**
Searching publicly indexed content via Google is legal. However, use this scraper responsibly — only search for information you are authorized to look up (e.g., your own leaked credentials, authorized security research).

**Q: Why are some sources missing (Dumpz, Codepad)?**
Those sites are either defunct or no longer publicly accessible as of 2026. This scraper only includes live sources.

## Use Cases

- **Threat intelligence** — monitor for leaked company credentials
- **Breach detection** — search for employee emails across paste sites
- **Security research** — discover public proof-of-concept code
- **Compliance monitoring** — detect data exfiltration via public pastes

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/osint-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
