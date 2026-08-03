# PeoplePerHour Jobs & Freelancers Scraper Tutorial: Run This Apify Actor with Python

Scrape service listings (hourlies), project jobs, and freelancer profiles from PeoplePerHour. Search by keyword, category, or browse top freelancers

This repository shows how to run [PeoplePerHour Jobs & Freelancers Scraper](https://apify.com/crawlerbros/peopleperhour-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/peopleperhour-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/peopleperhour-scraper](https://apify.com/crawlerbros/peopleperhour-scraper)
- **SEO title:** PeoplePerHour Jobs & Freelancers Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape service listings (hourlies), project jobs, and freelancer profiles from PeoplePerHour. Search by keyword, category, or browse top freelancers

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

# PeoplePerHour Jobs & Freelancers Scraper

Scrape listings from [PeoplePerHour](https://www.peopleperhour.com) — one of the largest freelance marketplaces. Extract hourlie services, freelance job posts, and freelancer profiles with full details including pricing, ratings, locations, and skills.

## Features

- **Search Services (Hourlies)** — find fixed-price freelance services/packages
- **Search Jobs** — browse freelance job postings from buyers
- **Search Freelancers** — discover freelancer profiles by skill or keyword
- **13 categories** supported: Design & Art, Technology, Writing & Translation, Digital Marketing, Video, Music & Audio, Business, and more
- **4 sort options**: Featured, Recommended, Latest, Price (ascending/descending)
- Filters: min/max price, min rating, category
- Automatic pagination up to 500 results

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | select | `searchServices`, `searchJobs`, or `searchFreelancers` |
| `searchQuery` | string | Keyword to search (e.g. 'logo design', 'Python developer') |
| `category` | select | Category filter (Design & Art, Technology, etc.) |
| `sortBy` | select | Sort order: featured, recommended, latest, price_low, price_high, rating |
| `minPrice` | number | Minimum price filter |
| `maxPrice` | number | Maximum price filter |
| `minRating` | number | Minimum rating filter (0–5) |
| `maxItems` | integer | Maximum results to return (1–500, default 20) |

## Output

### Services (Hourlies)
| Field | Description |
|-------|-------------|
| `hourlieId` | Unique service ID |
| `title` | Service title |
| `description` | Full service description |
| `price` | Service price (in original currency) |
| `currency` | Price currency code |
| `deliveryDays` | Estimated delivery time in days |
| `rating` | Average rating (0–5 scale) |
| `sales` | Number of sales/orders |
| `tags` | Service tags/skills |
| `category` | Category name |
| `freelancer` | Sub-object with name, URL, location, hourly rate, level, avatar |
| `url` | Direct link to the service |

### Jobs
| Field | Description |
|-------|-------------|
| `projId` | Unique project ID |
| `title` | Job title |
| `description` | Job description |
| `budget` | Budget amount |
| `currency` | Budget currency |
| `projectType` | Project type |
| `locationType` | Remote/local/hybrid |
| `postedAt` | Posting date |
| `category` | Category name |
| `url` | Direct link to the job |

### Freelancers
| Field | Description |
|-------|-------------|
| `memId` | Member ID |
| `name` | Freelancer name |
| `jobTitle` | Professional headline |
| `location` | City/country |
| `hourlyRate` | Hourly rate |
| `currency` | Rate currency |
| `certLevel` | Certification level |
| `reviewCount` | Number of reviews |
| `feedbackRating` | Overall feedback rating (0–5 scale) |
| `projectsCompleted` | Total projects completed |
| `skills` | List of skill tags |
| `photoUrl` | Profile photo URL |
| `url` | Direct link to profile |

## Example Output (Service)

```json
{
  "hourlieId": "12345678",
  "title": "Professional logo design",
  "description": "I will create a modern logo for your brand.",
  "price": 50.0,
  "currency": "GBP",
  "deliveryDays": 3,
  "rating": 4.8,
  "sales": 127,
  "category": "Design & Art",
  "freelancer": {
    "name": "Jane Smith",
    "url": "https://www.peopleperhour.com/freelancer/jane-smith",
    "location": "London, UK",
    "certLevel": "Top Seller"
  },
  "url": "https://www.peopleperhour.com/hourlie/professional-logo-design/12345678",
  "scrapedAt": "2026-05-22T10:00:00+00:00",
  "recordType": "service"
}
```

## FAQ

**Does this require a PeoplePerHour account?**
No — all data is extracted from public search pages. No login required.

**How reliable is the scraper?**
The scraper uses browser impersonation (Chrome 131) to access public pages and automatically retries on rate limits.

**What does the rating represent?**
Ratings are on a 0–5 scale converted from the platform's internal 0–100 scale.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/peopleperhour-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
