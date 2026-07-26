# Facebook Photos Scraper Tutorial: Run This Apify Actor with Python

Extract data from one or multiple Facebook images. Get image ID, Facebook photo URL, image URL, OCR text, and more. Download the data in JSON, CSV, and Excel and use it in apps, spreadsheets, and reports.

This repository shows how to run [Facebook Photos Scraper](https://apify.com/crawlerbros/facebook-photos-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-photos-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-photos-scraper](https://apify.com/crawlerbros/facebook-photos-scraper)
- **SEO title:** Facebook Photos Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract data from one or multiple Facebook images. Get image ID, Facebook photo URL, image URL, OCR text, and more. Download the data in JSON, CSV, and Excel and use it in apps, spreadsheets, and reports.

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

# Facebook Photos Scraper

Extract data from one or multiple Facebook page photo grids. Get image ID, Facebook photo URL, full-resolution image URL, alt text (OCR/image description), author info, and more. Download in JSON, CSV, or Excel.

## What does Facebook Photos Scraper do?

Facebook Photos Scraper extracts publicly available photo data from Facebook pages, profiles, and albums — without requiring Facebook login or cookies.

For each photo, the scraper always extracts:
- **Photo ID** — Unique Facebook photo identifier
- **Photo URL** — Direct link to the photo on Facebook
- **Image URL** — Full-resolution image file URL from Facebook's CDN
- **Alt Text** — Facebook's auto-generated image description (accessibility caption / OCR)
- **Author Name** — Page or profile name that posted the photo
- **Author URL** — Link to the author's Facebook page/profile

When available (more reliably with residential proxy):
- **Caption** — Photo description/caption text
- **Timestamp** — When the photo was uploaded (ISO 8601)
- **Likes Count** — Number of reactions
- **Comments Count** — Number of comments

## How to use Facebook Photos Scraper

1. **Provide Facebook URLs** — Enter one or more URLs of Facebook pages, profiles, or photo albums
2. **Set results limit** (optional) — Limit the maximum number of photos to extract (default: all available)
3. **Configure proxy** — Apify Proxy AUTO group works for core data; residential proxy provides caption and engagement data
4. **Run the scraper** — Click "Start" and wait for results
5. **Download data** — Export results in JSON, CSV, or Excel format

### Supported URL formats

| URL Type | Example |
|----------|---------|
| Page URL | `https://www.facebook.com/humansofnewyork` |
| Photos section | `https://www.facebook.com/humansofnewyork/photos` |
| Individual photo | `https://www.facebook.com/photo/?fbid=123456789` |
| Photo album | `https://www.facebook.com/media/set/?set=a.123456789` |
| Profile URL | `https://www.facebook.com/profile.php?id=123456789` |
| Mobile URL | `https://m.facebook.com/humansofnewyork/photos` |

## Input example

```json
{
    "startUrls": [
        { "url": "https://www.facebook.com/humansofnewyork/photos" }
    ],
    "resultsLimit": 10
}
```

## Output example

```json
{
    "photoId": "1547667900257527",
    "photoUrl": "https://www.facebook.com/photo/?fbid=1547667900257527",
    "imageUrl": "https://scontent-dfw6-1.xx.fbcdn.net/v/t39.30808-6/photo.jpg",
    "altText": "May be an image of 2 people, outdoors, standing",
    "authorName": "Humans of New York",
    "authorUrl": "https://www.facebook.com/humansofnewyork",
    "inputUrl": "https://www.facebook.com/humansofnewyork/photos",
    "scrapedAt": "2024-03-20T10:15:30.123456"
}
```

With residential proxy, you also get:
```json
{
    "caption": "Today I met someone extraordinary at the park...",
    "timestamp": "2024-03-15T14:30:00",
    "likesCount": 15230,
    "commentsCount": 842
}
```

## How much does it cost to scrape Facebook photos?

| Resource | Usage |
|----------|-------|
| Compute | ~0.02 CU per photo |
| Proxy | Apify AUTO (free datacenter) for core data; residential for full details |
| Memory | 2048 MB recommended |

## Proxy requirements

- **Apify Proxy AUTO (default)** — Works for extracting photo grid data (image URLs, alt text, author info). Free with all Apify plans.
- **Residential proxy** — Required to extract captions, timestamps, and engagement metrics from individual photo pages, which Facebook gates behind login walls for datacenter IPs.

## Tips for best results

- **Provide the `/photos` page URL** — e.g. `https://www.facebook.com/humansofnewyork/photos` — for the most complete results
- **Use public pages** — Works best with public Facebook pages (businesses, public figures, organizations)
- **Set a results limit** — Start with 10–20 to test, then increase as needed
- **No login needed** — The scraper does not require Facebook cookies or credentials

## Limitations

- Only works with **publicly accessible** Facebook content
- Private profiles and restricted content cannot be scraped
- Caption, timestamp, and engagement data require residential proxy (Facebook's login wall on individual photo pages)
- Only output fields that have actual data are included — fields with no value are omitted

## FAQ

### Can I scrape photos without a Facebook account?
Yes. The scraper does not require Facebook login, cookies, or API keys. It only accesses publicly available content.

### What image quality do I get?
The scraper extracts the highest-resolution image URL from Facebook's CDN, typically the full-resolution version.

### Why are caption and engagement fields missing?
Facebook requires login to view individual photo pages from datacenter IPs. Use residential proxy in the proxy configuration to unlock caption, timestamp, and engagement data.

### Why are some output fields not present?
Fields are only included when they contain real data. A photo without an accessible caption, for example, simply won't have a `caption` key in its record.

### Can I scrape photos from private profiles?
No. Only publicly accessible content is supported.

### How many photos can I scrape?
No hard limit. Use `resultsLimit` to control how many to extract — higher limits take more time and compute.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-photos-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
