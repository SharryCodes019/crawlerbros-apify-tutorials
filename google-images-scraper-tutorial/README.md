# Google Images Scraper Tutorial: Run This Apify Actor with Python

Extract image data from Google Images search. Scrape image URLs, dimensions, thumbnails, page titles, origins, and content URLs for any search query.

This repository shows how to run [Google Images Scraper](https://apify.com/crawlerbros/google-images-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-images-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-images-scraper](https://apify.com/crawlerbros/google-images-scraper)
- **SEO title:** Google Images Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract image data from Google Images search. Scrape image URLs, dimensions, thumbnails, page titles, origins, and content URLs for any search query.

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

# Google Images Scraper

Scrape image data from Google Images search results at scale. Extract full-resolution image URLs, dimensions, thumbnails, page titles, source domains, and content page URLs for any search query.

Perfect for building image datasets, monitoring brand visuals, competitor research, content curation, and training data collection.

## What data can you extract from Google Images?

For every image result, the scraper returns:

| Field             | Type      | Description                                          |
| ----------------- | --------- | ---------------------------------------------------- |
| `query`           | `string`  | The search query used                                |
| `imageUrl`        | `string`  | Direct URL to the full-resolution image              |
| `imageWidth`      | `integer` | Width of the full-resolution image in pixels         |
| `imageHeight`     | `integer` | Height of the full-resolution image in pixels        |
| `thumbnailUrl`    | `string`  | URL of the Google-cached thumbnail                   |
| `thumbnailWidth`  | `integer` | Width of the thumbnail in pixels                     |
| `thumbnailHeight` | `integer` | Height of the thumbnail in pixels                    |
| `title`           | `string`  | Page title of the website containing the image       |
| `origin`          | `string`  | Domain of the website where the image is hosted      |
| `contentUrl`      | `string`  | URL of the web page containing the image             |

## How to use Google Images Scraper

1. **Add your search queries** - Enter one or more image search terms (e.g., "sunset landscape", "product packaging design")
2. **Set the result limit** - Choose how many images to extract per query (1 to 500)
3. **Run the scraper** - Click Start and the scraper will collect all image data automatically
4. **Export your data** - Download results as JSON, CSV, Excel, or connect via API

## Input

| Field                | Type       | Description                                          | Default    |
| -------------------- | ---------- | ---------------------------------------------------- | ---------- |
| `queries`            | `string[]` | List of image search queries                         | _required_ |
| `maxResultsPerQuery` | `integer`  | Maximum number of image results to extract per query | `100`      |

### Example Input

```json
{
  "queries": ["sunset landscape", "modern architecture"],
  "maxResultsPerQuery": 100
}
```

## Output

### Example Output

```json
[
  {
    "query": "sunset landscape",
    "imageUrl": "https://images.pexels.com/photos/694636/pexels-photo-694636.jpeg",
    "imageWidth": 750,
    "imageHeight": 1123,
    "thumbnailUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXLRmm...",
    "thumbnailWidth": 193,
    "thumbnailHeight": 262,
    "title": "Mountain Ranges during Golden Hour - Free Stock Photo",
    "origin": "www.pexels.com",
    "contentUrl": "https://www.pexels.com/photo/mountain-ranges-during-golden-hour-694636/"
  }
]
```

### Output Schema

```json
{
  "query": { "type": "string", "description": "The search query used" },
  "imageUrl": { "type": "string", "description": "Direct URL to the full-resolution image" },
  "imageWidth": { "type": "integer", "description": "Width of the full-resolution image in pixels" },
  "imageHeight": { "type": "integer", "description": "Height of the full-resolution image in pixels" },
  "thumbnailUrl": { "type": "string", "description": "URL of the Google-cached thumbnail" },
  "thumbnailWidth": { "type": "integer", "description": "Width of the thumbnail in pixels" },
  "thumbnailHeight": { "type": "integer", "description": "Height of the thumbnail in pixels" },
  "title": { "type": "string", "description": "Page title of the website containing the image" },
  "origin": { "type": "string", "description": "Domain of the website where the image is hosted" },
  "contentUrl": { "type": "string", "description": "URL of the web page containing the image" }
}
```

## Use cases

- **Image dataset building** - Collect large sets of images for research, analysis, or machine learning training
- **Brand monitoring** - Track how your brand visuals appear across the web
- **Competitor research** - Analyze competitor product images, marketing materials, and visual strategies
- **Content curation** - Find high-quality images for blogs, presentations, and social media
- **SEO & visual search analysis** - Monitor which images rank for specific keywords
- **E-commerce** - Research product photography trends and competitor listings

## Integrations

Connect Google Images Scraper with your existing tools and workflows:

- **Webhooks** - Get notified when a scrape finishes
- **API access** - Integrate results directly into your application
- **Scheduled runs** - Set up recurring scrapes to monitor image results over time
- Export to **Google Sheets**, **Slack**, **Zapier**, **Make**, and more

## FAQ

### How many images can I scrape per query?

You can extract up to 500 images per search query. The default is 100. For most queries, Google Images returns hundreds of results.

### What image data is included?

Every result includes the full-resolution image URL with dimensions, a Google-cached thumbnail URL with dimensions, the page title and domain of the source website, and a link to the web page containing the image.

### Can I search for images in different languages?

Yes. You can use search queries in any language, including non-Latin scripts like Japanese, Chinese, Korean, Arabic, and more.

### Can I run multiple queries at once?

Yes. Pass an array of queries and the scraper will process them sequentially, returning results for each query in a single dataset.

### How fast is it?

The scraper typically extracts 100 images per query in under 15 seconds. Larger result sets (200-500) take proportionally longer due to pagination.

### What format can I export the data in?

Results can be exported as JSON, CSV, Excel, XML, or accessed via the Apify API. You can also connect to Google Sheets, Slack, Zapier, and other integrations.

### Does it handle Google's anti-bot protection?

Yes. The scraper uses stealth browser techniques to avoid detection and works reliably without requiring proxies.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-images-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
