# B2B Sales Trigger Intelligence Tutorial: Run This Apify Actor with Python

Detect high-intent B2B sales triggers hiring surges, funding rounds, executive changes, and news momentum from a list of company names. Produces a graded (A/B/C/D) priority list with rationale and source signals.

This repository shows how to run [B2B Sales Trigger Intelligence](https://apify.com/crawlerbros/b2b-sales-triggers) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/b2b-sales-triggers`
- **Apify Store:** [https://apify.com/crawlerbros/b2b-sales-triggers](https://apify.com/crawlerbros/b2b-sales-triggers)
- **SEO title:** B2B Sales Trigger Intelligence Tutorial: Run This Apify Actor with Python
- **Description:** Detect high-intent B2B sales triggers hiring surges, funding rounds, executive changes, and news momentum from a list of company names. Produces a graded (A/B/C/D) priority list with rationale and source signals.

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

# B2B Sales Trigger Intelligence

Identify which accounts in your pipeline are showing **real buying signals right now** — without spending hours digging through LinkedIn, Crunchbase, and news feeds by hand.

Paste a list of companies. Get back a **graded priority list** (A / B / C / D) with a one-line rationale, a composite 0–100 score, and the strongest signal detected across hiring, funding, and news.

## Why use this actor

Sales teams waste a huge amount of time researching accounts. Most of the intent signals that matter are public:

- A company just raised a Series B? They are hiring, buying tools, and have budget.
- A company opened 30 new engineering roles this quarter? They are scaling, and scaling teams need vendors.
- A company is dominating headlines with a new product launch? Reach out while momentum is high.

This actor automates the "is this account worth a touch right now?" question for every company on your list.

## What you get

For each company, the output includes:

- **Grade** (A / B / C / D) — an at-a-glance priority flag
- **Composite score** (0–100) combining hiring, funding, and news signals
- **Priority flag** — true for A-graded companies or those funded in the last 180 days
- **Top signal** — the single strongest trigger, in plain English
- **Rationale** — why this company got its grade
- **Per-source breakdown** (in Full mode) — job posting counts, funding rounds, news volume and sentiment

## Input

| Field | Description |
|---|---|
| **Companies (one per line)** | Paste company names into a textarea, one per row |
| **Companies (advanced)** | Optional: structured array with `companyName` + `domain`. Overrides the text list |
| **Output format** | `compact` for a scannable priority list; `full` for per-source details |
| **Max concurrency** | How many companies to process in parallel (1–10) |
| **Include raw signals** | Adds top headlines and sample job titles to the output |
| **Proxy** | Residential proxy recommended (Google News RSS is always direct) |

## Output fields (compact mode)

- `companyName` — company as provided
- `domain` — inferred primary domain
- `grade` — A / B / C / D
- `score` — 0–100 composite
- `priorityFlag` — boolean
- `topSignal` — strongest buying signal
- `rationale` — short explanation
- `runTimestamp` — ISO 8601

Full mode adds: `scoreBreakdown`, `hiringSignal`, `fundingSignal`, `newsSignal`.

## Dataset views

- **Overview** — the priority list (one row per company, grade + top signal)
- **Hiring Signals** — focus on LinkedIn hiring activity
- **Funding Signals** — focus on Crunchbase funding rounds
- **News Signals** — focus on Google News volume and sentiment

## FAQ

**How do you decide the grade?**
The score is a weighted sum of three pillars: hiring (up to 40 points), funding (up to 40 points), and news momentum (up to 20 points). A ≥ 70, B = 45–69, C = 20–44, D < 20.

**What counts as a hiring signal?**
Active LinkedIn job postings, the mix of roles (eng/sales/exec), and the rate of new posts in the last 30 days.

**What if a company has a private or locked-down Crunchbase page?**
That pillar is skipped silently and the grade is computed from the remaining pillars. We never fabricate data.

**How is news sentiment measured?**
A fast keyword classifier tags each headline as positive / neutral / negative. Companies with positive coverage momentum score higher.

**Do you need cookies or logins?**
No. All three sources are scraped from publicly accessible endpoints.

**How fresh are the signals?**
Every run fetches live data. Nothing is cached server-side.

**What if a company name is ambiguous (e.g., "Apple")?**
Provide the domain in the advanced input to disambiguate. Otherwise the actor uses the best web match it finds.

**Can I feed this into my CRM?**
Yes — the compact output is designed to map directly onto CRM fields. Pipe the dataset URL into Zapier / Make / your warehouse.

**Will all three sources always return data?**
No. If all three sources fail for a company, that company is emitted as a `company_error` row with the specific failures so you can retry or investigate.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/b2b-sales-triggers)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
