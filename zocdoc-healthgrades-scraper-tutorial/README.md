# ZocDoc + Healthgrades Doctors & Reviews Scraper Tutorial: Run This Apify Actor with Python

Scrape physicians, specialists, ratings, reviews, accepted insurance, locations, and bio data from ZocDoc.com and Healthgrades.com. Single actor with platform switch (zocdoc | healthgrades). No login required.

This repository shows how to run [ZocDoc + Healthgrades Doctors & Reviews Scraper](https://apify.com/crawlerbros/zocdoc-healthgrades-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/zocdoc-healthgrades-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/zocdoc-healthgrades-scraper](https://apify.com/crawlerbros/zocdoc-healthgrades-scraper)
- **SEO title:** ZocDoc + Healthgrades Doctors & Reviews Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape physicians, specialists, ratings, reviews, accepted insurance, locations, and bio data from ZocDoc.com and Healthgrades.com. Single actor with platform switch (zocdoc | healthgrades). No login required.

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

# ZocDoc + Healthgrades Doctors & Reviews Scraper

Scrape physicians, dentists, mental-health providers, surgeons, and 80+ other
healthcare specialists from **ZocDoc.com** and **Healthgrades.com** in a
single Apify actor. Pick a platform with the `platform` switch and a mode
with `mode` — the rest of the input adapts to the platform.

## What you get per provider

- Provider name, credentials, gender (canonical `Male` / `Female` / `Non-binary` when listed)
- Medical specialty / sub-specialties
- Office address (street, city, state, ZIP) + phone
- Star rating (1-5) and aggregate review count
- Free-text reviews (author, rating, body, date) — capped per provider
- Languages spoken
- Profile image URL and canonical profile URL
- Bio / description (when published on the profile)

Empty / unknown fields are omitted entirely from the dataset row — you never
get `null`, `""`, `[]` keys.

## Modes

| Mode | What it does | Inputs |
|---|---|---|
| `search` | Search providers by city + specialty (+ optional insurance, gender, language, rating filters) | `specialty`, `city`, `state` |
| `byProvider` | Scrape one or more provider profiles directly | `providerUrlsOrSlugs` |
| `bySpecialty` | Browse a specialty hub page | `specialty` |
| `byCity` | List top providers in a city | `city`, `state` |
| `byInsurance` | Filter by accepted insurance plan (**ZocDoc only**) | `insurance` |
| `byUrl` | Scrape arbitrary listing or profile URLs | `urls` |

## Filters

- `specialty` — 80+ medical / dental / mental-health specialty dropdown.
- `state` — US state code dropdown (50 states + DC).
- `gender` — any / female / male.
- `language` — provider-spoken language dropdown (50 languages, ISO 639-1).
- `acceptsNewPatients` — boolean.
- `minRating` — minimum 1-5 star rating.
- `minReviewCount` — minimum review count.
- `insurance` — accepted insurance plan (top 50 US insurers, ZocDoc only).

## Anti-bot

- **Healthgrades** works from Apify datacenter IPs without any proxy, since
  Apify already runs in the US. From other regions the actor pins the proxy
  to `country=US` to bypass the geo-block (`This page is not available in
  your area`).
- **ZocDoc is fronted by DataDome and is currently blocked even from Apify
  Residential US.** All datacenter and residential tiers return the
  `Please enable JS and disable any ad blocker` 403 challenge page. The
  actor still ships ZocDoc URL builders, JSON-LD parsers, and the full mode
  surface — if you bring your own clean US-residential proxy pool that
  DataDome hasn't fingerprinted, the actor will use it transparently. For
  most users, **Healthgrades is the recommended platform.**

If proxy escalation fails the actor emits a typed `error` record with the
HTTP status and reason, and a status-message summary.

## Daily test prefill

```json
{
  "platform": "healthgrades",
  "mode": "search",
  "specialty": "primary-care-doctor",
  "city": "New York, NY",
  "maxItems": 10,
  "fetchProviderDetails": true,
  "autoEscalateOnBlock": true
}
```

## Output sample

Both platforms emit the same flat record shape — keys are uniform across
`zocdoc` and `healthgrades`. A platform-agnostic `entityId` (URL slug) is
exposed alongside the platform-specific `slug` for cross-platform joins.

### ZocDoc

```json
{
  "platform": "zocdoc",
  "entityId": "jane-doe-12345",
  "providerName": "Dr. Jane Doe, MD",
  "specialty": "Primary Care Doctor",
  "city": "New York",
  "state": "NY",
  "address": {
    "addressStreet": "123 Main St",
    "addressLocality": "New York",
    "addressRegion": "NY",
    "postalCode": "10001"
  },
  "phone": "+1-212-555-0100",
  "rating": 4.8,
  "reviewCount": 124,
  "languages": ["English", "Spanish"],
  "url": "https://www.zocdoc.com/doctor/jane-doe-12345",
  "slug": "jane-doe-12345",
  "imageUrl": "https://...",
  "reviews": [
    {
      "author": "Patient ID 5532",
      "rating": 5,
      "body": "Excellent bedside manner.",
      "datePublished": "2025-09-12"
    }
  ],
  "recordType": "provider",
  "scrapedAt": "2026-05-08T..."
}
```

### Healthgrades

```json
{
  "platform": "healthgrades",
  "entityId": "dr-john-smith-xyz",
  "providerName": "Dr. John Smith, MD",
  "specialty": "Cardiologist",
  "city": "Boston",
  "state": "MA",
  "rating": 4.6,
  "reviewCount": 88,
  "url": "https://www.healthgrades.com/physician/dr-john-smith-xyz",
  "slug": "dr-john-smith-xyz",
  "recordType": "provider",
  "scrapedAt": "2026-05-08T..."
}
```

## FAQ

**Do I need a ZocDoc / Healthgrades login?**
No. Both platforms expose all listing/profile data on public pages — no auth,
no API key.

**How many providers per run?**
Up to 1000 (`maxItems`). Practical limit per search is constrained by the
platform's own page count (~100-200 results for a city + specialty).

**Will Healthgrades work outside the US?**
Yes — the actor auto-pins the Apify proxy to `country=US` regardless of where
the actor itself is running.

**Is this legal?**
This actor only fetches public, unauthenticated, non-PHI directory data
(provider names, specialties, addresses, public reviews) — the same data any
visitor sees on the website. No patient or PHI data is collected. You are
responsible for complying with each platform's Terms of Service in your
jurisdiction.

**Why are some fields missing on certain provider profiles?**
The actor never emits empty fields — if Healthgrades didn't list a phone for
a provider, that key is simply absent in the record (instead of `null` or
`""`). Use the present-keys list to filter dataset rows.

## High-churn output fields

Some fields evolve rapidly between runs and should be treated as snapshot-in-time:

- **`rating` / `reviewCount`** — Provider aggregate scores update as new
  reviews are posted; expect minor drift on every re-scrape. Match providers by
  `entityId` / `slug`, not by `(name, rating)` tuple.
- **`reviews[]`** — Both ZocDoc and Healthgrades expose only a recent window of
  reviews; an older review present on one run may roll off on the next. Use
  `reviewCount` as the canonical aggregate, not `len(reviews)`.
- **`acceptsNewPatients`** — Heuristic from Healthgrades bio text; can flip
  between runs as providers update their availability blurb.
- **`affiliation` / `awards`** — Self-reported on Healthgrades profile bio;
  occasionally rotates as the provider edits their bio.
- **`imageUrl`** — CDN URLs may rotate; use the URL as a reference, not a key.

Stable fields safe for diff/dedup: `entityId`, `slug`, `providerName`, `url`,
`address`, `specialty`, `gender`, `languages`, `phone`.

## Limitations

- **ZocDoc is currently blocked from Apify datacenter and residential
  pools (DataDome).** Cloud-verification rounds returned 0 ZocDoc records
  across 4 attempts — the platform is shipped as a code path but not
  daily-test viable. Use Healthgrades unless you supply your own clean
  residential proxy.
- Healthgrades exposes review *counts* + first-page reviews on profile
  pages; deeper review pages are not paginated by this actor.
- Healthgrades fuzzy-matches the `what=<specialty>` query — searching for
  "Dentist" can occasionally surface providers named "Dennis". This is the
  upstream platform's behavior, not the actor's.
- Healthgrades plan-level filtering is not exposed by the site, so
  `byInsurance` is ZocDoc-only.

## Pricing

Charge model (pay-per-result) is configured at the Apify UI level. This actor
emits one row per provider profile (plus optional review children inline).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/zocdoc-healthgrades-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
