# Google Keywords Suggest Scraper Pro Tutorial: Run This Apify Actor with Python

Scrape Google Suggest autocomplete keywords for any seed term. Pro modes: exact, all (related), questions (who/what/why), prepositions (with/for/vs), comparisons, alphabet expansion (a-z). Multi-keyword + multi-language + 200+ Google country codes.

This repository shows how to run [Google Keywords Suggest Scraper Pro](https://apify.com/crawlerbros/google-keywords-suggest-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-keywords-suggest-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/google-keywords-suggest-scraper-pro](https://apify.com/crawlerbros/google-keywords-suggest-scraper-pro)
- **SEO title:** Google Keywords Suggest Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Google Suggest autocomplete keywords for any seed term. Pro modes: exact, all (related), questions (who/what/why), prepositions (with/for/vs), comparisons, alphabet expansion (a-z). Multi-keyword + multi-language + 200+ Google country codes.

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

# Google Keywords Suggest Scraper Pro

Pull Google Suggest autocomplete keywords for any seed term — exactly what shows up in the Google search box as you type. Perfect for SEO research, content planning, and long-tail keyword discovery.

## Modes

- **exact** — just the seed
- **all** — Google's default related suggestions
- **questions** — appends `who/what/when/where/why/how/which/whose` for question-style queries
- **prepositions** — appends `for/with/vs/like/near/...` for intent-rich keywords
- **comparisons** — appends `vs/or/versus`
- **alphabet** — appends each letter `a-z` to surface long-tail variants (one query per letter, all 26)

## Output (flat mode — one record per suggestion)

```json
{
  "recordType": "suggestion",
  "text": "python tutorial for beginners",
  "source_keyword": "python tutorial",
  "expansion_query": "python tutorial f",
  "mode": "alphabet",
  "country": "US",
  "language": "en",
  "relevance": 601,
  "suggestion_type": "QUERY",
  "sub_types": [512],
  "scrapedAt": "2026-04-29T..."
}
```

## Output (tree mode — one record per seed)

```json
{
  "recordType": "keyword_tree",
  "source_keyword": "python tutorial",
  "mode": "alphabet",
  "country": "US",
  "language": "en",
  "suggestion_count": 124,
  "suggestions": [
    {"text": "python tutorial for beginners", "relevance": 601, ...},
    ...
  ]
}
```

## Input

| Field | Type | Description |
|---|---|---|
| `keywords` | array (required) | One or more seed keywords |
| `mode` | enum | `exact`, `all`, `questions`, `prepositions`, `comparisons`, `alphabet` |
| `country` | enum | Google `gl=` market code such as `US`, `GB`, `DE`, `IN`, `BR`, or `ALL` |
| `language` | enum | Google `hl=` language code such as `en`, `es`, `fr`, `de`, `ja`, `zh-CN` |
| `maxItemsPerKeyword` | int | Cap per seed (1-5000, default 200) |
| `minLength` | int | Drop suggestions shorter than N chars |
| `maxLength` | int | Drop suggestions longer than N chars |
| `containsKeyword` | string | Substring filter on suggestion text. Prefix `!` to invert. |
| `outputFormat` | enum | `flat` (one record per suggestion) or `tree` (one record per seed) |

## Use cases

- **SEO research** — find the long-tail variants real users search for
- **Content planning** — group suggestions by question modes to map "people also ask" topics
- **PPC research** — discover negative-match candidates with `containsKeyword: "!free"`
- **Competitor analysis** — combine `<brand> alternative`, `<brand> vs`, `<brand> for` modes
- **Multi-market SEO** — run the same seeds across different `country` + `language` combinations

## FAQ

**Does it require a login?** No. Google Suggest is a public endpoint. No cookies, no proxy.

**How many suggestions per seed?** Google returns up to ~10 per query. With `mode=alphabet` you get up to 260 (10 × 26), `questions` up to 80, etc.

**What's the difference between `country` and `language`?** `country` (gl=) influences geographic ranking — `python` in `IN` returns Indian programming-related suggestions; in `BR` returns more cooking ones. `language` (hl=) affects which language Google translates suggestions to.

**Can I get search volumes?** Volume requires Google Ads Keyword Planner (paid + OAuth). This actor returns Suggest's `relevance` score (~600 typical, higher = more popular) which is a useful proxy.

**What happens when filters drop everything?** The actor finishes without fake rows and sets a status message with the active filters so you can loosen them.

**What is `expansion_query`?** It's the generated query that was sent to Google Suggest for that batch of results, such as `python tutorial a` or `what openai api`. Google can still return nearby variants, so the suggestion text is not guaranteed to start with that exact string.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-keywords-suggest-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
