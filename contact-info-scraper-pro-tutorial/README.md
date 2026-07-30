# Contact Info Scraper Pro Tutorial: Run This Apify Actor with Python

Crawl any website and extract emails, phones, and social media profiles. Pro: domain allow/blocklists, role-prefix exclusion (info@/support@), per-site dedup, first.last format filter, prioritises /contact, /about, /team. HTTP-only.

This repository shows how to run [Contact Info Scraper Pro](https://apify.com/crawlerbros/contact-info-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/contact-info-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/contact-info-scraper-pro](https://apify.com/crawlerbros/contact-info-scraper-pro)
- **SEO title:** Contact Info Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Crawl any website and extract emails, phones, and social media profiles. Pro: domain allow/blocklists, role-prefix exclusion (info@/support@), per-site dedup, first.last format filter, prioritises /contact, /about, /team. HTTP-only.

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

# Contact Info Scraper Pro

Crawl websites and extract emails, phone numbers, and social media profiles. The actor is HTTP-first and works well on server-rendered pages, static sites, and contact pages that expose data directly in HTML.

## What this actor extracts

Per-domain record with:

- `websiteUrl` - normalized start URL
- `domain` - extracted hostname
- `emails` - unique list of cleaned emails
- `phones` - unique list of cleaned phone numbers
- `socialLinks` - first discovered profile URL per supported platform
- `contactPageUrl` - direct contact-page link when discovered
- `pagesCrawled`
- `crawledAt`

Supported social platforms include Facebook, Instagram, LinkedIn, X/Twitter, YouTube, TikTok, Pinterest, GitHub, Threads, Telegram, Discord, Mastodon, WhatsApp, and Reddit.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `urls` | string[] | `["https://apify.com"]` | Websites to scan. Empty-input cloud runs use this default. |
| `maxPagesPerSite` | integer | `20` | Max pages to crawl per domain. |
| `maxConcurrency` | integer | `5` | Parallel fetches per site. |
| `requestTimeoutSecs` | integer | `15` | HTTP timeout per page. |
| `useProxy` | boolean | `false` | Enable Apify proxy for sites that block datacenter IPs. |
| `smartPrioritise` | boolean | `true` | Visit likely contact/about/team pages first. |
| `maxDepth` | integer | `2` | Maximum link depth from the start URL. |
| `domainAllowlist` | array | `[]` | Pro filter: only crawl matching hosts. |
| `domainBlocklist` | array | `[]` | Pro filter: skip matching hosts. |
| `excludeRolePrefixes` | array | `[]` | Pro filter: drop emails whose local part starts with any of these prefixes. |
| `requireFirstAndLastName` | boolean | `false` | Pro filter: keep only personal-looking dotted names such as `jane.doe@example.com`. |
| `outputDedupBy` | enum | `domain` | Pro dedup mode: `domain`, `email`, or `none`. |

### Example input

```json
{
  "urls": ["https://example.com", "https://another.com"],
  "maxPagesPerSite": 10,
  "smartPrioritise": true,
  "excludeRolePrefixes": ["info", "support", "hello"],
  "requireFirstAndLastName": true,
  "outputDedupBy": "email"
}
```

## Output

One record per domain by default, or one record per email when `outputDedupBy=email`.

```json
{
  "recordType": "contact_domain",
  "websiteUrl": "https://example.com",
  "domain": "example.com",
  "emails": ["jane.doe@example.com", "john.smith@example.com"],
  "phones": ["+1 (555) 867-5309"],
  "socialLinks": {
    "linkedin": "https://www.linkedin.com/company/example",
    "twitter": "https://x.com/example",
    "instagram": "https://www.instagram.com/example"
  },
  "contactPageUrl": "https://example.com/contact",
  "pagesCrawled": 7,
  "crawledAt": "2026-04-30T14:00:00Z"
}
```

Empty fields are omitted. `recordType` is `contact_domain` for per-domain output and `contact_email` for per-email output.

## Reliability notes

- No browser is required for the standard flow.
- The actor extracts emails from visible text, `mailto:` links, Cloudflare `data-cfemail`, and simple `[at]` / `[dot]` obfuscation.
- Placeholder values from form fields are intentionally ignored.
- If every discovered value is filtered out, the actor still finishes cleanly and sets a status message instead of pushing placeholder error rows.

## FAQ

**Do I need a proxy?**  
Usually no. Enable `useProxy` for sites that return 403 or otherwise block cloud IPs.

**Does it render JavaScript?**  
Not in the HTTP-first path. It works best on pages that expose contact data directly in HTML.

**Why are some emails missing?**  
Some sites only reveal them after client-side rendering, login, or anti-bot challenges. Increasing crawl depth can help for multi-page sites, but JS-only contact data may still stay hidden.

**What does `requireFirstAndLastName` do?**  
It keeps dotted personal-style addresses like `jane.doe@company.com` and drops generic role addresses such as `info@`, `hello@`, or `support@`.

**What happens when emails are filtered out?**  
The actor can still emit phones, socials, and `contactPageUrl`. Fields with no data are omitted.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/contact-info-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
