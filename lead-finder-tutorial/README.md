# Lead Finder Tutorial: Run This Apify Actor with Python

Find B2B leads by job title, location, and industry. Extracts name, title, company, LinkedIn URL, and guessed email from public search results. No API keys or credentials needed.

This repository shows how to run [Lead Finder](https://apify.com/crawlerbros/lead-finder) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/lead-finder`
- **Apify Store:** [https://apify.com/crawlerbros/lead-finder](https://apify.com/crawlerbros/lead-finder)
- **SEO title:** Lead Finder Tutorial: Run This Apify Actor with Python
- **Description:** Find B2B leads by job title, location, and industry. Extracts name, title, company, LinkedIn URL, and guessed email from public search results. No API keys or credentials needed.

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

# Lead Finder

Find B2B leads by job title, location, and industry. Returns name, title, company, LinkedIn URL, and email. No API keys or credentials needed.

## Input

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `jobTitles` | string[] | Yes | - | Job titles to search for (e.g. "CEO", "Software Engineer") |
| `locations` | string[] | No | [] | Locations to target (e.g. "New York", "London") |
| `industries` | string[] | No | [] | Industries to filter by (e.g. "SaaS", "Healthcare") |
| `companyNames` | string[] | No | [] | Specific companies to target (e.g. "Google", "Stripe") |
| `maxLeads` | integer | No | 100 | Maximum number of leads to return (1-500) |

## Output

Each lead includes:

| Field | Description |
|-------|-------------|
| `full_name` | Person's full name |
| `first_name` | First name |
| `last_name` | Last name |
| `title` | Job title |
| `company_name` | Company name |
| `company_domain` | Company website domain |
| `location` | Location (when available) |
| `linkedin_url` | LinkedIn profile URL |
| `email` | User Email |
| `scraped_at` | Timestamp |

## Example

**Input:**
```json
{
    "jobTitles": ["VP of Marketing"],
    "locations": ["Austin"],
    "maxLeads": 5
}
```

**Output:**
```json
{
    "full_name": "Greg Brauner",
    "first_name": "Greg",
    "last_name": "Brauner",
    "title": "VP of Marketing",
    "company_name": "Thinkific",
    "company_domain": "thinkific.com",
    "location": "Austin",
    "linkedin_url": "https://www.linkedin.com/in/gregbrauner",
    "email": "greg.brauner@thinkific.com",
    "scraped_at": "2026-02-27T10:18:02.866080+00:00"
}
```

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/lead-finder)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
