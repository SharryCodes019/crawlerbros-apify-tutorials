# Company Domain & Social Links Finder Tutorial: Run This Apify Actor with Python

Given a company name, return the company's official website domain and its social media links (LinkedIn, X/Twitter, Facebook, Instagram, YouTube, TikTok, GitHub).

This repository shows how to run [Company Domain & Social Links Finder](https://apify.com/crawlerbros/company-domain) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/company-domain`
- **Apify Store:** [https://apify.com/crawlerbros/company-domain](https://apify.com/crawlerbros/company-domain)
- **SEO title:** Company Domain & Social Links Finder Tutorial: Run This Apify Actor with Python
- **Description:** Given a company name, return the company's official website domain and its social media links (LinkedIn, X/Twitter, Facebook, Instagram, YouTube, TikTok, GitHub).

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

# Company Domain & Social Links Finder — Website + Social Handles From a Company Name

Give this actor a list of company names and it returns each company's official website plus its LinkedIn, X/Twitter, Facebook, Instagram, YouTube, TikTok, and GitHub links.

## What this actor does

Supply one or more company names — "OpenAI", "Stripe", "Porsche AG" — and the actor resolves each one to its canonical root domain and social media presence. It works by running a public web search for the official site, picking the most likely corporate result, and then parsing that homepage for outbound links to known social platforms. The result is one flat record per company you asked about.

An optional **country hint** (`"US"`, `"Germany"`, `"Japan"`…) biases the search towards the local version of the company when the name is ambiguous — useful for chains and brands that operate under different domains per region. When the target homepage is protected by an anti-bot wall, the actor's **auto proxy fallback** kicks in automatically: if the first direct HTTP fetch is blocked, the request is retried through a residential proxy session so the social link extraction still succeeds. This happens transparently — you don't need to flip a switch.

The actor is cookie-free, login-free, API-key-free, and LLM-free by design. It is built for bulk use: feed it hundreds of companies and get clean, structured output you can drop straight into a CRM, a lead list, or an enrichment pipeline.

## Key features

- **Company name → official website** resolution via public web search.
- **Flat per-platform columns** — `linkedin`, `twitter`, `facebook`, `instagram`, `youtube`, `tiktok`, `github` — ready for spreadsheets and CRMs.
- **Country hint** for region-specific resolution (useful for multinational brands).
- **Auto proxy fallback** — when a company website blocks datacenter IPs, the actor retries through residential proxy automatically. No manual configuration required.
- **No cookies, no API keys, no LLMs** — just HTTP fetch + HTML parsing.
- **Bulk-friendly** — process long company lists in one run.
- **Clean output** — empty fields are omitted, so you don't post-process `null` values.

## Input

| Field | Type | Description |
|---|---|---|
| `companies` | array | One company name per entry (e.g. `"OpenAI"`, `"Porsche AG"`). |
| `country` | string | Optional country hint, e.g. `"US"`, `"Germany"`, `"Japan"`. Disambiguates multinational brands. |
| `maxSocialLinks` | integer | Cap on extra social links per company (default 10). |
| `autoProxyFallback` | boolean | When true (default), retry via residential proxy if the homepage blocks the direct fetch. |

**Example input**

```json
{
  "companies": ["OpenAI", "Stripe", "Porsche AG"],
  "country": "US",
  "maxSocialLinks": 10,
  "autoProxyFallback": true
}
```

## Output

Each record maps one input company to its web + social footprint:

```json
{
  "companyName": "OpenAI",
  "officialWebsite": "https://openai.com",
  "linkedin": "https://www.linkedin.com/company/openai",
  "twitter": "https://twitter.com/openai",
  "youtube": "https://www.youtube.com/@OpenAI",
  "github": "https://github.com/openai",
  "socialLinks": [
    { "platform": "linkedin", "url": "https://www.linkedin.com/company/openai" },
    { "platform": "twitter", "url": "https://twitter.com/openai" }
  ],
  "searchQuery": "\"OpenAI\" official site",
  "scrapedAt": "2026-04-24T10:15:00+00:00"
}
```

**Field descriptions**

- `companyName` — the company name you provided, echoed back verbatim.
- `officialWebsite` — canonical root URL of the company's primary site.
- `linkedin`, `twitter`, `facebook`, `instagram`, `youtube`, `tiktok`, `github` — flat per-platform columns, each holding the company's profile URL on that platform.
- `socialLinks` — full list of `{platform, url}` objects including any platforms not covered by the flat columns.
- `searchQuery` — the exact query string used to resolve the site (useful for debugging).
- `scrapedAt` — ISO 8601 UTC timestamp of extraction.

Fields that cannot be populated (e.g. a company without a TikTok account) are omitted from the record, so you never have to filter out `null` values downstream.

## Use cases

- **Lead generation & sales enrichment** — take a raw list of company names from a conference attendee sheet or LinkedIn export and enrich each one with its website and handles.
- **CRM hygiene** — fill in missing domain/social fields across thousands of existing CRM accounts.
- **Investor / market research** — map the online presence of an industry's key players in one run.
- **Competitive tracking** — pull every competitor's social handles so you can follow them in a monitoring tool.
- **Recruiting outreach** — resolve target-employer domains so you can find work emails via a downstream pattern checker.

## FAQ

**Do I need a proxy?**
Not usually. The actor runs cookieless and succeeds on most sites direct. When a specific company homepage blocks datacenter IPs, `autoProxyFallback` (on by default) silently retries through a residential session so the run keeps going.

**What happens if a company has no website?**
The record is still emitted with `officialWebsite` omitted and `socialLinks` empty. This makes it easy to filter down to "unresolved" companies for manual follow-up.

**What if my company has multiple legitimate domains (e.g. regional sites)?**
Provide the `country` hint to bias the search. Setting `country: "Germany"` for "Porsche" returns `porsche.de` rather than `porsche.com`.

**Does the actor check that the social links are still active?**
No. It extracts links that appear on the company's homepage. Defunct accounts can still appear if the homepage still references them.

**How accurate is the official-website detection?**
Directory sites (Wikipedia, LinkedIn company pages, Crunchbase, etc.) are filtered out so the top "real" corporate result wins. For extremely generic names ("Apple", "Shell") a country hint improves accuracy significantly.

**Can I pass domains instead of names?**
Use the [Sitemap URL Extractor](https://apify.com/) or a direct crawler if you already have the domain — this actor specifically solves the name → domain step.

**Is this using an AI model?**
No. The actor uses deterministic HTML parsing and a curated list of social platform domains. Costs are predictable and outputs are reproducible.

## Known limitations

- **Ambiguous brand names** ("Apollo", "Fusion", "Nova") may resolve to the wrong company without a `country` hint — always supply one when processing high-risk names.
- **Companies without a homepage** (pre-launch startups, stealth companies) cannot be resolved; you'll get an empty `officialWebsite` and empty `socialLinks`.
- **Aggressive anti-bot walls** on a minority of corporate sites can block both direct and residential fetches; in those cases the social links may be partial.
- **The actor does not verify social handle ownership** — it only extracts links the homepage itself publishes. A homepage that links to a wrong/third-party handle will be echoed faithfully.
- **Language-specific social platforms** (VK, Weibo, Line) are not included in the flat columns but may appear in `socialLinks` if the homepage links them.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/company-domain)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
