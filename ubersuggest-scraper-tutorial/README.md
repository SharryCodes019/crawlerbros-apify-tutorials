# Ubersuggest Keyword Scraper Tutorial: Run This Apify Actor with Python

Scrape keyword suggestions from Ubersuggest / Neil Patel. Given a seed keyword or domain, returns related keyword suggestions per country + language.

This repository shows how to run [Ubersuggest Keyword Scraper](https://apify.com/crawlerbros/ubersuggest-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ubersuggest-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ubersuggest-scraper](https://apify.com/crawlerbros/ubersuggest-scraper)
- **SEO title:** Ubersuggest Keyword Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape keyword suggestions from Ubersuggest / Neil Patel. Given a seed keyword or domain, returns related keyword suggestions per country + language.

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

# Ubersuggest Keyword Scraper — Related Keyword Suggestions Across 22 Countries

Get related-keyword suggestions for any seed keyword or domain across 22 countries and 9 languages — powered by the same public Google Suggest feed that Ubersuggest and most free keyword tools ingest as their base list.

## What this actor does

Supply a seed keyword (`"coffee"`) or one or more domains (`["make.com"]`) and the actor returns a list of related search terms that real users are typing into Google right now, scoped to the country and language you pick. It uses **Google Suggest** — Google's public keyword suggestion API — as its data source, which means the suggestions are fresh, real, and don't require any Ubersuggest login or paid subscription to retrieve.

A convenience flag called `autoMatchLanguageToCountry` (on by default) upgrades the default English language to the country's native language when you pick a non-US market — so selecting `country: de` automatically pulls German suggestions, `country: jp` pulls Japanese, and so on. You can override this at any time by setting `language` explicitly. When datacenter IPs get rate-limited, the actor rotates sessions up to 8 times and can fall back through a residential proxy to keep suggestion responses flowing.

v1 of this actor is deliberately focused on **real, verifiable data**: the related-keyword list. Ubersuggest's famous metric numbers — search volume, CPC, SEO difficulty, paid difficulty, domain authority, traffic estimates, backlinks, top pages — are walled off behind a paid Neil Patel subscription and cannot be extracted without authenticating as a paying user. This actor refuses to fabricate those numbers; if you enable the walled sections, it emits an honest sentinel record instead. See the **Known limitations** section for details.

## Key features

- **Google Suggest-backed** related-keyword lists — real data, no login required.
- **22 countries** — `us`, `uk`, `de`, `fr`, `jp`, `br`, `es`, `it`, `au`, `ca`, `in`, `mx`, `nl`, `ru`, `cn`, `kr`, `tr`, `pl`, `se`, `ch`, `at`, `be`.
- **9 languages** — `en`, `de`, `fr`, `es`, `it`, `ja`, `pt`, `ko`, `zh`.
- **Auto language-to-country matching** (default true) — picking `country: de` upgrades `language` from `en` to `de` automatically; override anytime.
- **Seed from keyword or domain** — pass a seed keyword directly, or let the actor convert a domain (`make.com` → seed `make`).
- **Session rotation** — up to 8 retry sessions on upstream rate limits.
- **Honest output** — walled metric numbers (volume, CPC, etc.) are simply absent rather than fabricated.
- **Apify-friendly timing** — overall run capped at ~4.5 minutes so daily platform test runs stay well under the ceiling.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `urls` | array | `["make.com"]` | Domains converted into keyword seeds. `make.com` becomes the seed `make`. |
| `keyword` | string | `"coffee"` | Direct seed keyword. Takes precedence over `urls` when both are provided. |
| `country` | enum | `us` | Country geo. 22 supported markets (see list above). |
| `language` | enum | `en` | Language for suggestions. 9 supported languages. |
| `autoMatchLanguageToCountry` | boolean | `true` | When true, upgrades `language` from `en` to the country's native language if you picked a non-US country without overriding language yourself. |
| `proxyConfiguration` | proxy | Apify Residential US | Residential proxy — helps when datacenter IPs get rate-limited. |

**Example input**

```json
{
  "keyword": "coffee",
  "country": "de",
  "autoMatchLanguageToCountry": true
}
```

## Output

**Keyword record (success)**

```json
{
  "type": "keyword",
  "keyword": "coffee",
  "country": "de",
  "language": "de",
  "suggestions": [
    { "type": "keyword", "keyword": "coffee fellows", "country": "de", "language": "de" },
    { "type": "keyword", "keyword": "coffee circle", "country": "de", "language": "de" }
  ],
  "updated_at": "2026-04-24T10:15:00+00:00",
  "scrapedAt": "2026-04-24T10:15:00+00:00"
}
```

**Field descriptions**

- `type` — always `"keyword"` for success records, or `"ubersuggest_error"` for sentinels.
- `keyword` — the seed you supplied.
- `country` / `language` — the geo/language actually used for the request.
- `suggestions` — list of related-keyword objects, each with its own `keyword`, `country`, `language`.
- `updated_at` / `scrapedAt` — ISO 8601 UTC timestamps.

Fields that cannot be populated without a paid login (`volume`, `cpc`, `currency`, `competition`, `seo_difficulty`, `paid_difficulty`, `searchIntent`) are **omitted entirely** from the record rather than filled with nulls or zeros.

**Upstream-blocked sentinel**

```json
{
  "type": "ubersuggest_error",
  "reason": "upstream_blocked",
  "message": "Google Suggest returned empty results for every session attempt. Try again later or narrow the seed.",
  "keyword": "very long ambiguous query",
  "scrapedAt": "2026-04-24T10:15:00+00:00"
}
```

**Error sentinel** — emitted on invalid input or when every suggestion session returned empty:

```json
{
  "type": "ubersuggest_error",
  "reason": "upstream_blocked",
  "message": "Google Suggest returned empty / blocked responses across all 8 sessions. Re-run to get fresh IPs or try a different seed keyword.",
  "scrapedAt": "2026-04-24T10:15:00+00:00"
}
```

## Use cases

- **SEO keyword research** — generate a wide net of long-tail suggestions around a seed term before running deeper analysis in a paid tool.
- **Content planning** — find adjacent topics and phrasings users are searching for in your target market.
- **Ad copy ideation** — discover real search phrasings to inform Google Ads keyword targeting.
- **Multilingual market research** — flip `country` across your target geos (with `autoMatchLanguageToCountry` on) to see how search intent differs by region.
- **Domain-based seeding** — feed a list of competitor domains and convert each one into a related-keyword map.

## FAQ

**Why can't you scrape search volume / CPC / SEO difficulty?**
Ubersuggest's metric numbers are fetched client-side via authenticated API calls to `app.neilpatel.com`. Without a paid-subscription bearer token, every such call returns HTTP 401/403. Those numeric fields are simply absent from our output rather than fabricated.

**Where do the `suggestions` come from then?**
Google Suggest — the same public keyword-suggestion API that Google's search box uses for autocomplete and that most free keyword tools (including Ubersuggest) ingest as their base suggestion list. The actor calls it with the country and language you specified.

**What does `autoMatchLanguageToCountry` actually do?**
If you pick `country: de` but leave `language` at its default `en`, the actor upgrades `language` to `de` so you get German suggestions for the German market. If you explicitly set both, your choice wins — no override happens. This prevents the common mistake of getting English suggestions for a non-English market.

**Will a residential proxy help?**
Usually not needed for keyword suggestions — Google Suggest is open. Proxy rotation is configured for cases where the datacenter IP gets rate-limited; the actor rotates sessions up to 8 times on empty/blocked responses.

**Can I pass my Ubersuggest cookie to unlock the walled sections?**
Not in v1. A future version may add optional cookie-based authentication for the paid sections, but it would effectively be a bring-your-own-subscription tool.

**Does this scrape `neilpatel.com` or `app.neilpatel.com`?**
No. Those app pages are pure single-page-app shells with no data in the HTML, and the API requires a bearer token. This actor does not hit Ubersuggest's infrastructure.

**How many suggestions do I get per seed?**
Google Suggest typically returns about 10 phrases per query. For broader coverage, re-run with alphabetic seed expansion (e.g. `"coffee a"`, `"coffee b"`, …) — this is a standard SEO technique.

## Known limitations

- **Metric numbers** (volume, CPC, SEO difficulty, domain authority, backlinks, top pages) **cannot be extracted** without a paid Ubersuggest subscription cookie. Those toggles were removed from the input form because they always returned an empty sentinel in v1 — if you need those metrics you'll need a paid data source.
- **22 countries and 9 languages** are currently supported. If your target market is outside this list, pick the closest neighbor or submit a feature request.
- **~10 suggestions per seed** is Google Suggest's cap per call. For deeper coverage use alphabetic seed expansion.
- **Session rotation retries** are capped at 8 attempts per run; if Google Suggest persistently blocks all sessions, the actor emits an error sentinel and exits rather than retrying forever.
- **No historical data** — Google Suggest reflects the current suggestion list, not suggestions from the past. Run the actor on a schedule if you want to track change over time.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ubersuggest-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
