# Quora Search Scraper Tutorial: Run This Apify Actor with Python

Search Quora by keywords and extract questions, answers, author info, upvotes, and engagement metrics. Find relevant Q&A content across any topic.

This repository shows how to run [Quora Search Scraper](https://apify.com/crawlerbros/quora-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/quora-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/quora-search-scraper](https://apify.com/crawlerbros/quora-search-scraper)
- **SEO title:** Quora Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search Quora by keywords and extract questions, answers, author info, upvotes, and engagement metrics. Find relevant Q&A content across any topic.

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

# Quora Search Scraper

Search Quora by keywords and extract questions, answers, author info, upvotes, and engagement metrics. Find relevant Q&A content across any topic — no Quora account or login required. A powerful Quora search API alternative for extracting structured data from the world's largest Q&A platform.

## What can this scraper do?

- **Search by keywords** — Enter any search term and the scraper finds relevant Quora questions automatically, then extracts all the data from each one
- **Scrape direct URLs** — Provide Quora question, profile, topic, or space URLs to scrape specific pages
- **Extract full answers** — Get complete answer text, author details, upvotes, comments, and engagement metrics
- **Detect AI answers** — Automatically identifies Quora AI-generated answers vs. human answers
- **Multiple content types** — Questions, answers, user profiles, topics, and spaces all in one scraper

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| **Search Keywords** | string[] | No | — | Keywords to search for on Quora. Finds relevant questions automatically. |
| **Direct Quora URLs** | string[] | No | — | Direct Quora URLs to scrape (questions, profiles, topics, spaces) |
| Max Results | integer | No | 50 | Maximum number of results per search query or answers per question (1–5,000) |
| Proxy Configuration | object | No | Residential | Proxy settings. Residential proxy is recommended. |

At least one of **Search Keywords** or **Direct Quora URLs** is required.

### Example input

```json
{
    "searchQueries": ["python programming", "machine learning"],
    "maxResults": 10,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}
```

```json
{
    "directUrls": [
        "https://www.quora.com/What-is-Python-used-for",
        "https://www.quora.com/topic/Python-programming-language-1",
        "https://www.quora.com/profile/Guido-van-Rossum-1"
    ],
    "maxResults": 20
}
```

## Output

Each run produces a dataset with flat rows. Every row includes a `content_type` field so you can filter by type.

### Question results

| Field | Type | Example |
|-------|------|---------|
| `content_type` | string | `"question"` |
| `title` | string | `"What is Python primarily used for?"` |
| `url` | string | `"https://www.quora.com/What-is-Python-primarily-used-for"` |
| `answer_count` | integer | `100` |
| `follow_count` | integer | `42` |
| `topics` | string[] | `["Python programming language", "Software Development"]` |
| `source_url` | string | `"https://www.quora.com/What-is-Python-used-for"` |
| `source_query` | string | `"python programming"` (empty if from direct URL) |
| `scrape_timestamp` | string | `"2026-03-08T18:28:03.140078+00:00"` |

### Answer results

| Field | Type | Example |
|-------|------|---------|
| `content_type` | string | `"answer"` |
| `title` | string | `"What is Python primarily used for?"` |
| `url` | string | `"https://www.quora.com/What-is-Python-primarily-used-for/answer/John-Smith"` |
| `answer_text` | string | Full answer text (not truncated) |
| `answer_url` | string | Direct link to the answer |
| `author_name` | string | `"John Smith"` |
| `author_url` | string | `"https://www.quora.com/profile/John-Smith"` |
| `author_credentials` | string | `"Software Engineer at Google"` |
| `upvotes` | integer | `89` |
| `comments_count` | integer | `4` |
| `shares_count` | integer | `2` |
| `answer_timestamp` | string | `"2y"` |
| `is_ai_answer` | boolean | `false` |
| `question_title` | string | `"What is Python primarily used for?"` |
| `question_url` | string | `"https://www.quora.com/What-is-Python-primarily-used-for"` |
| `source_url` | string | Original input URL |
| `source_query` | string | Search keyword (empty if from direct URL) |
| `scrape_timestamp` | string | ISO 8601 timestamp |

### Profile results

| Field | Type | Example |
|-------|------|---------|
| `content_type` | string | `"profile"` |
| `title` | string | `"Guido van Rossum"` |
| `name` | string | `"Guido van Rossum"` |
| `url` | string | `"https://www.quora.com/profile/Guido-van-Rossum-1"` |
| `bio` | string | User biography |
| `credentials` | string | Professional credentials |
| `profile_image_url` | string | Profile picture URL |
| `follower_count` | integer | `3100` |
| `following_count` | integer | `15` |
| `answer_count` | integer | `42` |
| `question_count` | integer | `5` |
| `total_views` | integer | `1200000` |
| `source_url` | string | Original input URL |
| `scrape_timestamp` | string | ISO 8601 timestamp |

### Topic results

| Field | Type | Example |
|-------|------|---------|
| `content_type` | string | `"topic"` |
| `title` | string | `"Python (programming language)"` |
| `name` | string | `"Python (programming language)"` |
| `url` | string | `"https://www.quora.com/topic/Python-programming-language-1"` |
| `description` | string | Topic description |
| `follower_count` | integer | `1600000` |
| `question_count` | integer | `5000` |
| `source_url` | string | Original input URL |
| `scrape_timestamp` | string | ISO 8601 timestamp |

### Space results

| Field | Type | Example |
|-------|------|---------|
| `content_type` | string | `"space"` |
| `title` | string | `"Data Science"` |
| `name` | string | `"Data Science"` |
| `url` | string | `"https://www.quora.com/q/data-science"` |
| `description` | string | Space description |
| `follower_count` | integer | `104000` |
| `post_count` | integer | `500` |
| `contributor_count` | integer | `25` |
| `source_url` | string | Original input URL |
| `scrape_timestamp` | string | ISO 8601 timestamp |

### Sample output

```json
{
    "content_type": "answer",
    "title": "What is Python primarily used for?",
    "url": "https://www.quora.com/What-is-Python-primarily-used-for/answer/Pratima-Yadav-117",
    "answer_text": "Python is used for various purposes due to its versatile nature...",
    "answer_url": "https://www.quora.com/What-is-Python-primarily-used-for/answer/Pratima-Yadav-117",
    "author_name": "Pratima Yadav",
    "author_url": "https://www.quora.com/profile/Pratima-Yadav-117",
    "author_credentials": "",
    "upvotes": 4,
    "comments_count": 0,
    "shares_count": 2,
    "answer_timestamp": "4y",
    "is_ai_answer": false,
    "question_title": "What is Python primarily used for?",
    "question_url": "https://www.quora.com/What-is-Python-primarily-used-for",
    "source_url": "https://www.quora.com/What-is-Python-used-for",
    "scrape_timestamp": "2026-03-08T18:28:03.140078+00:00"
}
```

## How much does it cost?

The Quora Scraper uses pay-per-event pricing at **$5 per 1,000 results**. Each question, answer, profile, topic, or space counts as one result.

A typical run scraping 1 search query with 10 answers costs approximately **$0.05–0.10** in platform credits (including compute and proxy).

## FAQs

### Do I need a Quora account or cookies?

No. The scraper works entirely without authentication. Both keyword search and direct URL scraping work without logging in.

### How does keyword search work?

The scraper searches for your keywords and finds relevant Quora question pages. It then visits each question page and extracts the full content including all answers, author details, and engagement metrics.

### What proxy should I use?

Residential proxy is recommended for the best results. The scraper works with Apify's built-in residential proxy group. Datacenter proxies may work but have a higher chance of being blocked.

### How many results can I get per run?

You can extract up to 5,000 results per search query or direct URL. For questions with many answers, the scraper automatically scrolls to load more content.

### Can I scrape private or restricted profiles?

No. The scraper only extracts publicly visible content. Private profiles, restricted answers, and Quora+ paywalled content are not accessible.

### What does `is_ai_answer` mean?

Quora generates AI-powered answers for some questions. The scraper automatically detects these and marks them with `is_ai_answer: true` and `author_name: "Quora AI"` so you can filter them.

### What memory setting should I use?

Use **1024 MB** or higher. Quora's pages are resource-intensive and require more memory than typical websites.

### Why are some fields empty?

Some fields like `follow_count`, `author_credentials`, or `description` may be empty when Quora doesn't display that information on the page. This is normal and depends on the specific content being scraped.

### What types of Quora URLs are supported?

- **Questions**: `https://www.quora.com/What-is-Python-used-for`
- **Profiles**: `https://www.quora.com/profile/Username`
- **Topics**: `https://www.quora.com/topic/Topic-Name`
- **Spaces**: `https://www.quora.com/q/space-name` or `https://spacename.quora.com/`

## Limitations

- Requires **1024 MB memory** minimum (Quora's pages are JavaScript-heavy)
- Keyword search returns 1–5 relevant question URLs per query
- Only publicly visible content can be scraped — no login-restricted or Quora+ content
- Answer timestamps are relative (e.g., "2y", "6mo") rather than exact dates
- Quora may occasionally restrict access from data center IPs — residential proxy recommended

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/quora-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
