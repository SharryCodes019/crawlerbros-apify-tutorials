# Psychology Today Scraper | Therapist & Psychiatrist Leads Tutorial: Run This Apify Actor with Python

Scrape Psychology Today's therapist, psychiatrist, group practice, and treatment-rehab directories by US state. Returns name, credentials, specialties, insurance, address, and contact info per professional. No login required.

This repository shows how to run [Psychology Today Scraper | Therapist & Psychiatrist Leads](https://apify.com/crawlerbros/psychology-today-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/psychology-today-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/psychology-today-scraper](https://apify.com/crawlerbros/psychology-today-scraper)
- **SEO title:** Psychology Today Scraper | Therapist & Psychiatrist Leads Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Psychology Today's therapist, psychiatrist, group practice, and treatment-rehab directories by US state. Returns name, credentials, specialties, insurance, address, and contact info per professional. No login required.

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

# Psychology Today Scraper

Extract structured records of therapists, psychiatrists, group practices, and rehab centers from the Psychology Today professional directory — across all 50 US states plus DC.

## What this actor does

Psychology Today operates the largest publicly searchable directory of mental-health providers in the United States. This actor walks that directory by category and by state, returning one clean record per professional, with all the information a user would see on the provider's listing and profile pages.

You choose one of four categories — **therapists**, **psychiatrists**, **groups**, or **treatment-rehab** — and one or more US states. In `LIST_ONLY` mode the actor extracts everything visible on the listing pages (name, credentials, photo, short description, city, state) and is the fastest option for enumerating a state. In `LIST_AND_DETAILS` mode it additionally opens each provider's profile page and enriches the record with phone, website, specialties, treatment approaches, insurances accepted, languages, client focus, years in practice, gender, and a full street-level address.

The result is a ready-to-use dataset for lead generation, market research, referral directories, or any workflow that needs a structured snapshot of the mental-health provider landscape in a given region.

## Key features

- Four directory categories: `therapists`, `psychiatrists`, `groups`, `treatment-rehab`
- All 50 US states plus Washington, DC
- Two scrape modes: `LIST_ONLY` (fast, listing-level) and `LIST_AND_DETAILS` (full profile)
- Fine-grained scope controls: `maxItems` global cap and `maxPagesPerState` per-state cap
- Configurable polite delay window (`minDelayMs` / `maxDelayMs`) between requests
- Transparent residential-proxy fallback — direct requests first, proxy only when blocked
- No login, no cookies, no API key required
- Zero-null output — empty fields are omitted from each record

## Input

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `category` | enum | yes | `therapists` | Directory to crawl. One of `therapists`, `psychiatrists`, `groups`, `treatment-rehab`. |
| `states` | string[] | no | `["new-york"]` | State slugs to crawl (50 US states + DC). Example: `"california"`, `"new-york"`, `"district-of-columbia"`. |
| `scrapeMode` | enum | no | `LIST_ONLY` | `LIST_ONLY` for listing-level fields only; `LIST_AND_DETAILS` to also open each profile. |
| `maxItems` | integer | no | `10` | Global cap on records emitted across all selected states. |
| `maxPagesPerState` | integer | no | `5` | Number of listing pages to walk per state (~20 profiles per page). |
| `minDelayMs` | integer | no | `150` | Lower bound (milliseconds) of the random delay between requests. |
| `maxDelayMs` | integer | no | `300` | Upper bound (milliseconds) of the random delay between requests. |
| `autoProxyFallback` | boolean | no | `true` | Automatically retry through Apify residential proxy when a page looks blocked. |

**Example input**

```json
{
  "category": "therapists",
  "states": ["new-york", "california", "texas"],
  "scrapeMode": "LIST_AND_DETAILS",
  "maxItems": 200,
  "maxPagesPerState": 10,
  "minDelayMs": 200,
  "maxDelayMs": 500,
  "autoProxyFallback": true
}
```

## Output

One record per provider. Fields without data are omitted so every key has a real value.

```json
{
  "profileUrl": "https://www.psychologytoday.com/us/therapists/jane-doe-new-york-ny/111111",
  "professionalName": "Jane Doe",
  "credentials": "LCSW",
  "profileId": "111111",
  "shortDescription": "Compassionate therapist helping adults...",
  "longDescription": "Welcome! I am a licensed clinical social worker...",
  "phone": "+12125551234",
  "website": "https://janedoetherapy.com",
  "imageUrl": "https://cdn.psychologytoday.com/profile-photos/111111.jpg",
  "primaryAddress": {
    "street": "123 W 45th St",
    "city": "New York",
    "state": "NY",
    "zip": "10036"
  },
  "specialties": ["Anxiety", "Depression", "Trauma and PTSD"],
  "expertise": ["Grief", "Relationship Issues"],
  "treatmentApproaches": ["Cognitive Behavioral (CBT)", "EMDR"],
  "insuranceAccepted": ["Aetna", "BlueCross BlueShield", "Cigna"],
  "clientFocus": ["Adults", "Elders (65+)"],
  "languages": ["English", "Spanish"],
  "gender": "Female",
  "yearsInPractice": 12,
  "category": "therapists",
  "stateSlug": "new-york",
  "scrapedAt": "2026-04-24T12:34:56+00:00"
}
```

**Field descriptions**

- **`profileUrl`** — canonical Psychology Today profile URL
- **`professionalName`** / **`credentials`** — name and credential letters (e.g. LCSW, PhD, MD)
- **`profileId`** — stable numeric ID used by Psychology Today
- **`shortDescription`** / **`longDescription`** — the listing card blurb and the full profile bio
- **`phone`** / **`website`** / **`imageUrl`** — contact details and provider photo (detail mode). For most modern profiles `website` is Psychology Today's interstitial redirect URL (e.g. `https://www.psychologytoday.com/us/profile/{id}/website`) — clicking it in a browser bounces the user to the therapist's external site.
- **`emails`** — array of contact emails when the therapist publishes a `mailto:` link directly on their Psychology Today profile or on an externally-linked website that resolves over HTTP without JavaScript (detail mode). Often absent — Psychology Today increasingly hides external website URLs behind a JavaScript-only interstitial that this HTTP-only scraper cannot crack without a full browser.
- **`primaryAddress`** — structured address with `street`, `city`, `state`, `zip` (detail mode)
- **`specialties`**, **`expertise`**, **`treatmentApproaches`**, **`insuranceAccepted`**, **`clientFocus`**, **`languages`** — taxonomy arrays (detail mode)
- **`gender`**, **`yearsInPractice`** — provider demographics (detail mode)
- **`category`** / **`stateSlug`** — echo of the input, so each record is self-describing
- **`scrapedAt`** — ISO-8601 timestamp of this run

## Use cases

- **Lead generation** — build targeted lists of independent practitioners for CRM, EHR, or billing products
- **Referral network building** — seed a clinic's referral database with local provider coverage by specialty
- **Market research** — map provider density by state, insurance coverage, and specialty mix
- **Academic / public-health research** — study therapist distribution, wait-list availability, and access to care
- **Directory and aggregator sites** — populate a white-label directory with verified, normalised provider records

## FAQ

**Do I need a login or an API key?**
No. Psychology Today's directory is publicly accessible. The actor is login-free and cookie-free.

**Do I need a proxy?**
Not usually. Runs start on Apify's direct egress; the `autoProxyFallback` toggle (on by default) only provisions residential proxy traffic when a direct fetch looks blocked — so you only pay for proxy on pages that need it.

**What's the difference between `LIST_ONLY` and `LIST_AND_DETAILS`?**
`LIST_ONLY` returns everything visible on the state listing page — fast, and plenty for name / city / specialty counts. `LIST_AND_DETAILS` additionally opens each profile and adds phone, website, full address, specialties, treatment approaches, insurance accepted, languages, client focus, gender, and years in practice. Expect detail-mode runs to take roughly twice as long per profile.

**Which categories are supported?**
Four: `therapists`, `psychiatrists`, `groups` (group practices), and `treatment-rehab` (inpatient and outpatient treatment centers).

**Which states are supported?**
All 50 US states plus Washington, DC. Pass the directory slug (e.g. `new-york`, `california`, `district-of-columbia`).

**How many results can I expect per state?**
Psychology Today shows about 20 profiles per listing page. Large states (California, New York, Texas) have tens of thousands of profiles across hundreds of pages; smaller states may only have a few hundred. Use `maxPagesPerState` and `maxItems` to control scope.

**Can I filter by city, specialty, or insurance?**
The current version scopes by category and state. City-, specialty-, and insurance-level filters are on the roadmap.

**Why is the email field missing?**
Psychology Today does not expose therapist email addresses on public profile pages. The actor only populates an email when an explicit `mailto:` link is present, which is uncommon.

**Is this compliant with Psychology Today's terms?**
The actor reads only publicly accessible directory pages, with a configurable polite delay between requests to avoid hammering. Responsibility for downstream use of the data rests with the caller — please respect Psychology Today's terms and applicable regulations such as CAN-SPAM, TCPA, and GDPR.

## Known limitations

- **US-only directory.** Psychology Today also operates country-specific directories (Canada, UK, Australia) — those are not covered by this actor.
- **No city-level filter (yet).** Scope is category + state; narrow the results downstream by filtering on `primaryAddress.city` or `shortDescription`.
- **Email addresses are usually absent** because Psychology Today does not publish therapist emails on their profile pages.
- **Detail mode is roughly 2x slower** than list-only mode because it fetches each profile page individually (with the configured polite delay).
- **Very large states** can produce hundreds of pages of results. Set `maxPagesPerState` and `maxItems` generously for exhaustive crawls, or slice by region in post-processing.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/psychology-today-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
