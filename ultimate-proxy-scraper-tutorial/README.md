# Ultimate Free Proxy Scraper Tutorial: Run This Apify Actor with Python

Aggregate thousands of free public HTTP, HTTPS, SOCKS4 and SOCKS5 proxies from 8+ reliable sources in a single run. Dedupe, validate format, and output ready-to-use proxy lists.

This repository shows how to run [Ultimate Free Proxy Scraper](https://apify.com/crawlerbros/ultimate-proxy-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ultimate-proxy-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ultimate-proxy-scraper](https://apify.com/crawlerbros/ultimate-proxy-scraper)
- **SEO title:** Ultimate Free Proxy Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Aggregate thousands of free public HTTP, HTTPS, SOCKS4 and SOCKS5 proxies from 8+ reliable sources in a single run. Dedupe, validate format, and output ready-to-use proxy lists.

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

# Ultimate Free Proxy Scraper

Aggregate thousands of free public **HTTP, HTTPS, SOCKS4 and SOCKS5** proxies from 11 reliable sources in a single run. Get a deduplicated proxy list ready for use in your scrapers, bots, or privacy tools.

## Features

- **~9,000–12,000 unique proxies per run** — aggregated from 11 curated sources
- **All proxy types supported** — HTTP, HTTPS, SOCKS4, SOCKS5
- **Auto-deduplicated** — same `host:port` never appears twice even if in multiple sources
- **Parallel fetching** — all sources queried concurrently for fast runs
- **Fresh daily** — sources are community-maintained GitHub repos that update continuously
- **No proxy or auth needed** — works directly from datacenter IPs

## Sources

| Source | Repo / URL | Types |
|--------|-----------|-------|
| TheSpeedX | [github.com/TheSpeedX/PROXY-List](https://github.com/TheSpeedX/PROXY-List) | HTTP, SOCKS4, SOCKS5 |
| ShiftyTR | [github.com/ShiftyTR/Proxy-List](https://github.com/ShiftyTR/Proxy-List) | SOCKS4, SOCKS5 |
| clarketm | [github.com/clarketm/proxy-list](https://github.com/clarketm/proxy-list) | HTTP |
| spys.me | [spys.me](https://spys.me) | HTTP, SOCKS4 |
| roosterkid | [github.com/roosterkid/openproxylist](https://github.com/roosterkid/openproxylist) | HTTPS |
| hideip.me | [github.com/zloi-user/hideip.me](https://github.com/zloi-user/hideip.me) | HTTPS |
| mmpx12 | [github.com/mmpx12/proxy-list](https://github.com/mmpx12/proxy-list) | HTTPS |

## Input

| Field | Type | Description |
|-------|------|-------------|
| `maxItems` | Integer | Maximum number of unique proxies to output (default 500) |
| `types` | Array | Which proxy types to include (`HTTP`, `HTTPS`, `SOCKS4`, `SOCKS5`; default all) |

### Example Input

```json
{
    "maxItems": 1000,
    "types": ["HTTP", "SOCKS5"]
}
```

## Output

Each dataset item represents one unique proxy:

| Field | Type | Description |
|-------|------|-------------|
| `host` | String | Proxy IP address |
| `port` | String | Proxy port |
| `full` | String | `host:port` combined |
| `type` | String | `HTTP`, `HTTPS`, `SOCKS4`, or `SOCKS5` |
| `source` | String | Source list where the proxy came from |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "host": "192.168.1.1",
    "port": "8080",
    "full": "192.168.1.1:8080",
    "type": "HTTP",
    "source": "TheSpeedX",
    "scrapedAt": "2026-04-10T12:00:00+00:00"
}
```

## FAQ

**Q: Are these proxies working / valid?**
No — this scraper aggregates raw proxy lists without validation. You should validate proxies yourself before using them (e.g., by sending a test request via each proxy). Most free proxies have a high failure rate.

**Q: How often are the lists updated?**
The GitHub sources (TheSpeedX, ShiftyTR, clarketm) are community-maintained and update hourly to daily. Each run fetches the latest data.

**Q: Are these proxies safe to use?**
Free public proxies come with no guarantees of privacy, security, or availability. Do not send sensitive data through them. For production use cases, consider paid proxy services.

**Q: Why are my results fewer than 7,500?**
Sources occasionally overlap (same proxy in multiple lists). Deduplication reduces the raw total. If you set `types` to only some types, the count will drop further.

**Q: Can I filter by country?**
Not in this version. The raw sources don't include country information reliably across all lists.

## Use Cases

- **Scraper rotation** — feed into your web scrapers as a free proxy pool
- **Privacy testing** — test how your app handles different proxy types
- **Bot networks** — rotate IPs for crawlers, monitors, or automation
- **Security research** — analyze free proxy infrastructure

## Limitations

- **No validation** — raw lists only, you must test proxies yourself
- **No country data** — not all sources provide it
- **Quality varies** — free proxies have high failure rates; expect 5–20% working at any time

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ultimate-proxy-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
