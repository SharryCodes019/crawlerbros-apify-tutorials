# Radaris People Search (SkipTrace Lookup) Tutorial: Run This Apify Actor with Python

Look up US people by name and return matching profiles with addresses, relatives, alternate names, and geo coordinates. Powered by radaris.com (public Person JSON-LD). HTTP-only via Apify RESIDENTIAL US proxy; name-based search only.

This repository shows how to run [Radaris People Search (SkipTrace Lookup)](https://apify.com/crawlerbros/radaris-people-search) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/radaris-people-search`
- **Apify Store:** [https://apify.com/crawlerbros/radaris-people-search](https://apify.com/crawlerbros/radaris-people-search)
- **SEO title:** Radaris People Search (SkipTrace Lookup) Tutorial: Run This Apify Actor with Python
- **Description:** Look up US people by name and return matching profiles with addresses, relatives, alternate names, and geo coordinates. Powered by radaris.com (public Person JSON-LD). HTTP-only via Apify RESIDENTIAL US proxy; name-based search only.

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

# SkipTrace People Lookup

Look up people by name (optionally narrowed by city/state) against
[radaris.com](https://radaris.com) and export matching public profile
records — known addresses, relatives, alternate name spellings, and
geo-coordinates — as a structured Apify dataset.

Powered by radaris.com. The scraper returns public name-based people
records with addresses and relatives. **Phone / email reverse lookup is
not supported** — radaris indexes people by name only.

The scraper is lightweight, HTTP-only (`curl_cffi` + BeautifulSoup), and
does not require cookies, login, or a browser runtime. Pair it with
Apify's built-in schedules to run recurring skip-trace enrichments
against your own lead lists.

## Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fullName` | string | yes | Full name to look up, e.g. `John Smith`. |
| `city` | string | no | City to narrow the search, e.g. `Dallas`. |
| `state` | string | no | US state abbreviation, e.g. `CA`, `TX`, `NY`. |
| `phone` | string | no | Accepted for compatibility but unused — radaris does not support phone reverse-lookup. |
| `email` | string | no | Accepted for compatibility but unused — radaris does not support email reverse-lookup. |
| `maxItems` | integer | no | Max person records to return (default `3`, max `500`). |

`fullName` is required. If it is blank — even when a phone or email is
provided — the actor emits an `invalid_input` sentinel row instead of
failing the run.

### Example input

```json
{
    "fullName": "John Smith",
    "state": "CA",
    "maxItems": 3
}
```

## Output

Each matched person is pushed as a single row with the following
fields. Only populated fields are included — no `null` values.

| Field | Type | Description |
| --- | --- | --- |
| `type` | string | Always `skip_trace_person` for person rows. |
| `id` | string | Stable radaris identifier (e.g. `John-Smith`). |
| `url` | string | Canonical radaris.com profile URL. |
| `fullName` | string | Matched person's full name. |
| `firstName` | string | Given name. |
| `lastName` | string | Family name. |
| `age` | integer | Age if radaris exposes it. |
| `addresses` | object[] | Known locations (`{street, city, state, zip, country}`). |
| `relatives` | object[] | Family members and known associates (`{name, relation?, url?}`). |
| `alternateNames` | string[] | Alternate name spellings / known aliases. |
| `latitude` | number | Geo-coordinate latitude of the primary home location. |
| `longitude` | number | Geo-coordinate longitude of the primary home location. |
| `scrapedAt` | string | ISO-8601 UTC timestamp of scrape. |

### Example output

```json
{
    "type": "skip_trace_person",
    "id": "John-Smith",
    "url": "https://radaris.com/p/John/Smith/",
    "fullName": "John Smith",
    "firstName": "John",
    "lastName": "Smith",
    "addresses": [
        {"city": "Bossier City", "state": "LA", "country": "USA"}
    ],
    "alternateNames": ["John R Smith", "Jonathan Smith"],
    "relatives": [
        {"name": "Tracy L Smith"},
        {"name": "Monica M Smith"}
    ],
    "latitude": 32.5159852,
    "longitude": -93.7321228,
    "scrapedAt": "2026-04-20T12:34:56Z"
}
```

## How It Works

1. Reads the input and splits `fullName` into first + last name.
2. Fetches `https://radaris.com/p/<First>/<Last>/` (optionally narrowed
   by `?ql=<state>&city=<city>`) with a chrome131 TLS fingerprint.
3. Parses every `<script type="application/ld+json">` block on the page
   and collects every `@type: Person` entry.
4. Maps each Person to the output schema above and pushes up to
   `maxItems` clean rows (no nulls) into the run dataset.

## Error Records

The actor never throws; every failure mode is recorded as a sentinel
row on the dataset so downstream tooling can decide how to react.

| `reason` | When it is emitted |
| --- | --- |
| `invalid_input` | `fullName` was missing, or only `phone`/`email` was supplied (radaris doesn't support reverse-lookup). |
| `upstream_error` | radaris.com returned a non-200 response or the HTTP request failed. |
| `empty_result` | The page loaded but contained no `Person` LD+JSON records. |

Sentinel shape:

```json
{
    "type": "skip_trace_blocked",
    "reason": "upstream_error",
    "message": "radaris.com request failed (status=503, ...).",
    "url": "https://radaris.com/p/John/Smith/?ql=CA",
    "scrapedAt": "2026-04-20T12:34:56Z"
}
```

## FAQ

**Does this scraper require cookies or login?**
No. It performs a plain HTTP GET against radaris.com's public profile
pages.

**Do I need a proxy?**
No. The actor runs fine from Apify's default datacenter IPs — radaris
does not block datacenter ranges.

**Can I look up phone numbers or email addresses?**
No. radaris.com indexes people by name only. Supplying `phone` or
`email` without a `fullName` returns an `invalid_input` sentinel.

**Why do I sometimes get only one result for a common name?**
radaris aggregates all profiles with the same first + last name on a
single `/p/<First>/<Last>/` page. Use `state` / `city` to disambiguate
when multiple people share a name.

**What is `maxItems` for?**
It caps the number of person rows written to the dataset. The default
is `3`, which is a good fit for lead-enrichment workflows where you
only want the top match(es).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/radaris-people-search)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
