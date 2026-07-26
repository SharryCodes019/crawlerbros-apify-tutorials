# PromptBase Scraper Tutorial: Run This Apify Actor with Python

Extract comprehensive data from PromptBase.com, the world's largest AI prompt marketplace with 220k+ prompts for AI models. This actor scrapes detailed prompt content, pricing data , creator profiles, AI model classifications, and high-quality prompt images.

This repository shows how to run [PromptBase Scraper](https://apify.com/crawlerbros/PromptBase) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/PromptBase`
- **Apify Store:** [https://apify.com/crawlerbros/PromptBase](https://apify.com/crawlerbros/PromptBase)
- **SEO title:** PromptBase Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract comprehensive data from PromptBase.com, the world's largest AI prompt marketplace with 220k+ prompts for AI models. This actor scrapes detailed prompt content, pricing data , creator profiles, AI model classifications, and high-quality prompt images.

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

# PromptBase AI Prompts Marketplace Scraper

This Apify actor scrapes AI prompts from PromptBase.com, extracting comprehensive information about prompts, their creators, pricing, usage statistics, and more.

## Features

- **Comprehensive Prompt Data**: Scrapes detailed information about AI prompts
- **Pricing Information**: Extracts pricing details, currency, and pricing models
- **Creator Profiles**: Collects creator information, social links, and profiles
- **Usage Statistics**: Gathers views, downloads, favorites, and ratings
- **Content Analysis**: Extracts full prompt content, instructions, and examples
- **Media Files**: Collects images, videos, and other media associated with prompts
- **Filtering Options**: Supports filtering by categories, pricing, and sorting
- **HTML Debugging**: Saves HTML content for selector analysis during development

## Input Parameters

| Parameter       | Type    | Default   | Description                                    |
| --------------- | ------- | --------- | ---------------------------------------------- |
| `maxPrompts`    | Integer | 100       | Maximum number of prompts to scrape            |
| `scrapeDetails` | Boolean | true      | Whether to scrape detailed prompt pages        |
| `categories`    | Array   | []        | List of categories to filter by                |
| `pricingModel`  | String  | "all"     | Filter by pricing model (free, paid, all)      |
| `sortBy`        | String  | "popular" | Sort method (popular, newest, trending, price) |

## Output Data

Each prompt record includes:

### Basic Information

- `title`: Prompt title
- `detail_url`: URL to prompt's detail page
- `image_url`: Prompt thumbnail/preview image URL (filtered to exclude UI elements)

### Pricing Information

- `price`: Prompt price (numeric, null for free prompts)
- `currency`: Currency code (USD for paid prompts)
- `pricing_model`: Pricing model (free, paid)

### Creator Information

- `creator_name`: Creator's username/name
- `creator_url`: URL to creator's profile

### Categorization

- `category`: AI model category (Midjourney, ChatGPT, DALL-E, etc.)
- `tags`: Array of tags and labels (discounts, etc.)

### Statistics

- `rating`: Prompt rating (numeric, if available)

### Timestamps

- `scraped_at`: When the data was scraped

### Detailed Information (if scrapeDetails=true)

- `full_content`: Complete prompt content
- `creator_profile`: Object containing:
  - `name`: Creator's full name
  - `bio`: Creator's bio/description
  - `avatar_url`: Creator's avatar image URL
- `ai_models`: Array of compatible AI models detected
- `prompt_images`: Array of prompt-related images (max 5, filtered to exclude UI elements)

### Metadata

- `source`: Source website (promptbase.com)

## Usage Examples

### Basic Usage

```json
{
  "maxPrompts": 50,
  "scrapeDetails": true
}
```

### Filtered by Category and Pricing

```json
{
  "maxPrompts": 200,
  "scrapeDetails": true,
  "categories": ["writing", "marketing"],
  "pricingModel": "paid",
  "sortBy": "newest"
}
```

### Free Prompts Only

```json
{
  "maxPrompts": 100,
  "scrapeDetails": false,
  "pricingModel": "free",
  "sortBy": "popular"
}
```

### Specific Categories

```json
{
  "maxPrompts": 150,
  "scrapeDetails": true,
  "categories": ["chatgpt", "midjourney", "dalle"],
  "sortBy": "trending"
}
```

## Development Features

### HTML Debugging

During development, the scraper saves HTML content to the key-value store for selector analysis:

- `debug_promptbase_html`: Contains the HTML content of the search page

### Error Handling

- Comprehensive error handling with detailed logging
- Graceful handling of missing elements
- Retry logic for failed requests

### Browser Automation

- Uses Playwright for reliable browser automation
- Handles dynamic content loading
- Implements proper delays and waits

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:

```bash
playwright install chromium
```

3. Run the scraper:

```bash
python -m src
```

## Docker Usage

```bash
docker build -t promptbase-scraper .
docker run -e APIFY_TOKEN=your_token promptbase-scraper
```

## Notes

- The scraper respects rate limits and implements delays between requests
- HTML content is saved for debugging purposes during development
- The scraper handles various prompt listing layouts and structures
- All URLs are properly resolved and normalized
- Pricing information is extracted and normalized across different currencies

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/PromptBase)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
