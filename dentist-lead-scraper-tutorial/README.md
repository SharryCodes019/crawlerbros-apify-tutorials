# Dentist & Healthcare Provider Lead Scraper Tutorial: Run This Apify Actor with Python

Scrape dentist, doctor, clinic, orthodontist, and other healthcare provider leads from Google Maps. Enriches each lead with emails and social media profiles via website crawl.

This repository shows how to run [Dentist & Healthcare Provider Lead Scraper](https://apify.com/crawlerbros/dentist-lead-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/dentist-lead-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/dentist-lead-scraper](https://apify.com/crawlerbros/dentist-lead-scraper)
- **SEO title:** Dentist & Healthcare Provider Lead Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape dentist, doctor, clinic, orthodontist, and other healthcare provider leads from Google Maps. Enriches each lead with emails and social media profiles via website crawl.

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

# Dentist & Healthcare Lead Scraper

Scrape **dentist, doctor, clinic, orthodontist, chiropractor, veterinarian, pharmacy, physical therapist, dermatologist, optometrist** (or any custom query) leads from Google Maps. Each lead is enriched with **email addresses** and **social media profiles** from the business's website.

## Input

| Field | Type | Description |
|---|---|---|
| `businessType` | enum | Dentist / Doctor / Clinic / Orthodontist / Chiropractor / Veterinarian / Pharmacy / Physical Therapist / Dermatologist / Optometrist / Custom |
| `location` | string | City, state, or ZIP (e.g. "Austin, TX"). Required. |
| `searchQuery` | string | Custom query used when businessType = "Custom". |
| `maxResults` | integer | Max leads per run (1-500, default 50). |
| `enrichEmails` | boolean | Visit each website to extract emails. Default on. |
| `enrichSocials` | boolean | Extract social-profile URLs. Default on. |
| `outputFormat` | enum | `full`, `hubspot`, `salesforce`. |
| `language` | enum | Google Maps language (`en`, `es`, `fr`, `de`, `it`, `nl`, `pt`, `pl`, `ja`). |

## Output (full format)

Per lead: `name`, `category`, `address`, `mapsUrl`, `phone`, `website`, `rating`, `reviewCount`, `placeId`, `cid`, `latitude`, `longitude`, `email`, `allEmails`, `socialLinks` (object with facebook / instagram / linkedin / twitter / youtube / tiktok), `businessType`, `scrapedAt`.

**HubSpot format**: `company`, `address`, `phone`, `website`, `email`, `industry`, `hs_lead_status`, `hs_object_source`, `hs_latitude`, `hs_longitude`, `facebook_url`, `linkedin_url`, `instagram_url`, `twitter_url`.

**Salesforce format**: `Company`, `Street`, `Phone`, `Website`, `Email`, `Industry`, `LeadSource`, `Latitude__c`, `Longitude__c`, `Facebook__c`, `LinkedIn__c`.

## How it works

1. Build the Google Maps search query from `businessType` + `location` (or custom).
2. Launch stealth Chromium and collect up to `maxResults` place cards (name, address, phone, rating, website, coordinates).
3. For each place with a website, crawl the homepage + common contact pages (`/contact`, `/about`) via `httpx` and extract `mailto:` emails, plain-text emails, and social profile links.
4. Normalise into the selected output format and push one record per lead.

## FAQ

**Do I need a proxy?** No — the scraper tries direct first and auto-escalates to Apify RESIDENTIAL US if Google blocks the datacenter.
**Why some leads have no email?** Not every business has an email on their website, and placeholder / `noreply@…` values are filtered out.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/dentist-lead-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
