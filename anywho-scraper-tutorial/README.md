# AnyWho People Search Scraper Tutorial: Run This Apify Actor with Python

Find phone numbers, addresses, and age for US individuals by name or phone number using AnyWho.com.

This repository shows how to run [AnyWho People Search Scraper](https://apify.com/crawlerbros/anywho-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/anywho-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/anywho-scraper](https://apify.com/crawlerbros/anywho-scraper)
- **SEO title:** AnyWho People Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Find phone numbers, addresses, and age for US individuals by name or phone number using AnyWho.com.

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

# AnyWho People Search Scraper

Find phone numbers, addresses, and age for US individuals using [AnyWho.com](https://www.anywho.com). Given a name (with state) or a phone number, this actor searches AnyWho and returns structured contact records.

## What This Actor Does

- Look up people by **name + state** (optionally with city) or by **phone number**
- Returns name, age, current address, phone numbers, and a direct AnyWho profile URL
- Supports bulk input — look up multiple people in a single run
- No proxy required — AnyWho is accessible from standard datacenter IPs

## Input

| Field | Description | Default |
|-------|-------------|---------|
| `searches` | List of people to look up. Each entry needs `type` (`name` or `phone`) and matching fields | Required |
| `maxResultsPerSearch` | Maximum matched people to return per query (1–20) | 5 |
| `delayBetweenSearchesMs` | Milliseconds to wait between queries in a bulk run | 3000 |

### Search Query Examples

```json
[
  {"type": "name",  "name": "John Smith", "city": "Dallas", "state": "TX"},
  {"type": "name",  "name": "Jane Doe",   "state": "CA"},
  {"type": "phone", "phone": "2145551234"}
]
```

**Name search** — `name` and `state` are required; `city` is optional but improves relevance.

**Phone search** — `phone` accepts 10-digit US numbers with or without country code/formatting.

## Output

One record per matched person per input query. Fields appear only when data is available — no null values.

| Field | Description | Example |
|-------|-------------|---------|
| `inputQuery` | The original search query | `"John Smith, Dallas TX"` |
| `name` | Full name | `"John Smith IV"` |
| `age` | Age | `61` |
| `currentAddress` | Current address object | `{"street": "5036 Hummingbird Ln", "city": "Plano", "state": "TX"}` |
| `phones` | All phone numbers | `[{"number": "(214) 555-1234", "type": "mobile"}]` |
| `phoneCount` | Total phones found | `2` |
| `mobilePhones` | Phones classified as mobile (when source provides `type`) | `[{"number": "(214) 555-1234", "type": "mobile"}]` |
| `landlinePhones` | Phones classified as landline / home | `[{"number": "(972) 555-9876", "type": "landline"}]` |
| `relatives` | Relatives of this person (when listed) | `["Jane Smith", "Bob Smith"]` |
| `relativeCount` | Number of relatives found | `2` |
| `associates` | Known associates (when listed) | `["Mary Doe"]` |
| `associateCount` | Number of associates found | `1` |
| `sources` | Sites that returned this person | `["anywho"]` |
| `profileUrls` | Profile page URL | `{"anywho": "https://www.anywho.com/people/john+smith/texas/plano/a781523027536"}` |
| `scrapedAt` | Scrape timestamp (UTC) | `"2026-04-26T10:00:00Z"` |

### Example Output Record

```json
{
  "inputQuery": "John Smith, Dallas TX",
  "name": "John Smith IV",
  "age": 61,
  "currentAddress": {
    "street": "5036 Hummingbird Ln",
    "city": "Plano",
    "state": "TX"
  },
  "phones": [],
  "sources": ["anywho"],
  "profileUrls": {
    "anywho": "https://www.anywho.com/people/john+smith/texas/plano/a781523027536"
  },
  "scrapedAt": "2026-04-26T10:00:00Z"
}
```

## FAQ

**Is this US-only?**
Yes. AnyWho covers US public records only.

**How many results will I get?**
Coverage depends on what AnyWho has indexed. Common names in major cities return multiple results; uncommon names or rural areas may return zero. `maxResultsPerSearch` caps the output per query.

**Can I search multiple people at once?**
Yes. The `searches` field accepts a list of any length. Queries run in sequence with a configurable delay between them.

**What data is this based on?**
Public records aggregated by AnyWho. This actor does not access private databases.

**Why might a search return no results?**
The person may not be listed on AnyWho, or the name/state combination may be too broad or too specific. Try without city if you included one, or verify the state abbreviation.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/anywho-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
