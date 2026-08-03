# ResearchGate Academic Scraper Tutorial: Run This Apify Actor with Python

Scrape ResearchGate for academic publications and researcher profiles. Search papers by query, browse researcher profiles, and fetch detailed publication metadata including citations, reads, DOI, and PDF availability.

This repository shows how to run [ResearchGate Academic Scraper](https://apify.com/crawlerbros/researchgate-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/researchgate-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/researchgate-scraper](https://apify.com/crawlerbros/researchgate-scraper)
- **SEO title:** ResearchGate Academic Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape ResearchGate for academic publications and researcher profiles. Search papers by query, browse researcher profiles, and fetch detailed publication metadata including citations, reads, DOI, and PDF availability.

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

# ResearchGate Academic Scraper

Scrape academic publications and researcher profiles from [ResearchGate](https://www.researchgate.net) — one of the world's largest academic social network platforms. No login required.

## Features

- **Search Publications** — find academic papers by keyword with title, abstract, authors, DOI, citations, and PDF availability
- **Search Researchers** — find researcher profiles by name or field with institution, h-index, and research interests
- **By Profile** — fetch detailed data for a specific ResearchGate researcher profile
- **By Publication ID** — fetch detailed metadata for a single publication by its ID
- Filter by keyword, minimum citations, and publication year
- Parses JSON-LD structured data (`ScholarlyArticle`, `Person`) embedded in ResearchGate HTML
- Supplemental extraction from HTML text for reads, citations, h-index, and follower counts

## Output Fields

### Publication Records (`recordType: "publication"`)

| Field | Type | Description |
|-------|------|-------------|
| `publicationId` | string | ResearchGate publication ID |
| `title` | string | Publication title |
| `abstract` | string | Abstract or description (up to 2000 chars) |
| `authors` | array | Full list of author names |
| `primaryAuthor` | string | First/primary author |
| `journal` | string | Journal or conference name |
| `publishedDate` | string | Publication year or full date |
| `doi` | string | Digital Object Identifier |
| `reads` | integer | Number of reads on ResearchGate |
| `citations` | integer | Number of citations |
| `recommendations` | integer | ResearchGate recommendations count |
| `publicationUrl` | string | Full ResearchGate URL |
| `pdfAvailable` | boolean | Whether a PDF download link was found |
| `keywords` | array | Keywords from the publication |
| `recordType` | string | Always `"publication"` |
| `siteName` | string | Always `"ResearchGate"` |
| `scrapedAt` | string | ISO-8601 scrape timestamp |

### Researcher Records (`recordType: "researcher"`)

| Field | Type | Description |
|-------|------|-------------|
| `researcherId` | string | ResearchGate profile username/ID |
| `name` | string | Full name |
| `username` | string | Profile URL slug |
| `institution` | string | Affiliated institution |
| `department` | string | Department within institution |
| `researchInterests` | array | Research interests/expertise areas |
| `publicationsCount` | integer | Number of publications on ResearchGate |
| `citationsCount` | integer | Total citation count |
| `hIndex` | integer | h-index |
| `followersCount` | integer | Number of followers |
| `profileUrl` | string | Full ResearchGate profile URL |
| `avatarUrl` | string | Profile photo URL |
| `recordType` | string | Always `"researcher"` |
| `siteName` | string | Always `"ResearchGate"` |
| `scrapedAt` | string | ISO-8601 scrape timestamp |

## Input Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | select | `searchPublications` | `searchPublications`, `searchResearchers`, `byProfile`, `byPublicationId` |
| `query` | string | `deep learning` | Search query for `searchPublications` or `searchResearchers` |
| `profileUsername` | string | — | Profile slug for `byProfile` mode (e.g. `Alice-Smith-42`) |
| `publicationId` | string | — | Publication ID for `byPublicationId` mode (e.g. `379417897`) |
| `containsKeyword` | string | — | Case-insensitive filter on title/abstract |
| `minCitations` | integer | — | Minimum citation count (0–9,999,999) |
| `fromYear` | integer | — | Only include publications from this year onwards (1900–2030) |
| `maxItems` | integer | `20` | Maximum records to return (1–1000) |

## Example Use Cases

**Search for papers on deep learning:**
```json
{"mode": "searchPublications", "query": "deep learning", "maxItems": 20}
```

**Find highly-cited papers on cancer treatment from 2020+:**
```json
{"mode": "searchPublications", "query": "cancer treatment", "minCitations": 100, "fromYear": 2020}
```

**Search for machine learning researchers:**
```json
{"mode": "searchResearchers", "query": "machine learning", "maxItems": 20}
```

**Get a specific researcher's profile:**
```json
{"mode": "byProfile", "profileUsername": "Yann-LeCun"}
```

**Get a single publication's details:**
```json
{"mode": "byPublicationId", "publicationId": "379417897"}
```

## FAQs

**Do I need a ResearchGate account?**
No authentication is required. The actor uses public HTML pages and JSON-LD structured data.

**Why might some fields be missing?**
ResearchGate doesn't always embed all data in machine-readable JSON-LD. Fields like reads, citations, and h-index are extracted from page text using pattern matching and may vary by page.

**Are full paper PDFs downloaded?**
No. The `pdfAvailable` field indicates whether ResearchGate shows a download link. The actor does not download or store PDF files.

**How reliable is this scraper?**
ResearchGate uses Cloudflare but serves most pages without JavaScript challenges for standard requests. The actor retries on 429/5xx responses with exponential backoff (10/20/40s delays, 3 attempts).

**What is the `publicationId`?**
It is the numeric ID from the ResearchGate URL: `researchgate.net/publication/379417897_...` — just the digits.

**What is the `profileUsername`?**
It is the slug from the ResearchGate profile URL: `researchgate.net/profile/Alice-Smith-42` — the `Alice-Smith-42` part.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/researchgate-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
