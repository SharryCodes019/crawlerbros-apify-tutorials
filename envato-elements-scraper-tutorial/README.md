# Envato Elements Asset Scraper Tutorial: Run This Apify Actor with Python

Scrape Envato Elements, search or browse fonts, graphic templates, presentations, web templates, video, music, photos, add-ons, and 3D assets. Extract titles, authors, tags, thumbnails, previews, and full asset metadata.

This repository shows how to run [Envato Elements Asset Scraper](https://apify.com/crawlerbros/envato-elements-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/envato-elements-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/envato-elements-scraper](https://apify.com/crawlerbros/envato-elements-scraper)
- **SEO title:** Envato Elements Asset Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Envato Elements, search or browse fonts, graphic templates, presentations, web templates, video, music, photos, add-ons, and 3D assets. Extract titles, authors, tags, thumbnails, previews, and full asset metadata.

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

# Envato Elements Asset Scraper

Extract creative asset metadata from [Envato Elements](https://elements.envato.com) — the subscription-based creative library with millions of fonts, graphic templates, presentations, web templates, video, music, photos, add-ons, and 3D assets. All metadata is publicly accessible without authentication.

## What it scrapes

- **Asset title and author**
- **Asset type** (font, graphic template, presentation, web template, video, music, photo, add-on, 3D)
- **Thumbnail and preview images**
- **Tags** (up to 15 keywords per item)
- **Publish date** (when the asset was made available)
- **License type** (Envato Elements License)
- **File formats** (AI, EPS, PSD, etc. when available)
- **Compatible software versions** (where applicable)
- **Supported languages** (for fonts)
- **Author profile URL**
- **Canonical asset URL**
- **New/featured flags**

## Modes

| Mode | Description |
|------|-------------|
| `search` | Search for assets by keyword across all types or a specific asset type |
| `byCategory` | Browse all assets of a specific type (fonts, templates, photos, etc.) |
| `byItemUrls` | Enrich specific item page URLs with full metadata |

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `mode` | Select | Scraping mode | `search` |
| `searchQuery` | Text | Search keyword (mode=search) | `logo design` |
| `assetType` | Select | Asset type filter: `all`, `fonts`, `graphic-templates`, `presentations`, `web-templates`, `video`, `music`, `photos`, `add-ons`, `3d` | `all` |
| `sortBy` | Select | Sort order: `relevance`, `newest`, `popular`, `trending` | `relevance` |
| `startUrls` | List | Item page URLs for byItemUrls mode | — |
| `maxItems` | Integer | Maximum number of assets (1–5000) | `50` |

## Output

Each item in the dataset contains:

| Field | Type | Description |
|-------|------|-------------|
| `itemId` | String | Envato Elements humane ID (e.g., `6DUJ7AF`) |
| `title` | String | Asset title |
| `url` | String | Canonical asset page URL |
| `thumbnailUrl` | String | Main thumbnail image URL |
| `previewUrl` | String | Preview image URL |
| `assetType` | String | Asset type slug (e.g., `fonts`, `graphic-templates`) |
| `category` | String | Human-readable asset type name (e.g., `Fonts`) |
| `author` | String | Creator username |
| `authorUrl` | String | Author profile URL |
| `tags` | Array | Asset tags/keywords |
| `publishDate` | String | Date when asset was published (YYYY-MM-DD) |
| `license` | String | `"Envato Elements License"` |
| `fileFormats` | Array | Available file formats (e.g., `["AI", "EPS"]`) |
| `compatibleWith` | Array | Compatible software versions |
| `supportedLanguages` | Array | Supported languages (fonts only) |
| `isNew` | Boolean | Whether this is a recently added asset |
| `isFeatured` | Boolean | Whether this is a featured asset |
| `isFree` | Boolean | Whether this is currently free to download |
| `recordType` | String | Always `"envatoElement"` |
| `scrapedAt` | String | ISO 8601 timestamp of scrape |

## Example output

```json
{
  "itemId": "6DUJ7AF",
  "title": "Binders Stylish Signature",
  "url": "https://elements.envato.com/binders-stylish-signature-6duj7af",
  "thumbnailUrl": "https://elements-resized.envatousercontent.com/elements-cover-images/6983a221...",
  "assetType": "fonts",
  "category": "Fonts",
  "author": "aqrstudio",
  "authorUrl": "https://elements.envato.com/user/aqrstudio",
  "tags": ["signature", "script", "fashion", "branding", "vintage", "logo"],
  "publishDate": "2021-10-04",
  "license": "Envato Elements License",
  "supportedLanguages": ["Czech", "Danish", "Dutch", "English"],
  "isNew": false,
  "isFeatured": false,
  "isFree": false,
  "recordType": "envatoElement",
  "scrapedAt": "2026-05-15T12:00:00+00:00"
}
```

## FAQ

**Q: Does this scraper require an Envato Elements subscription?**
A: No. All metadata (titles, authors, thumbnails, tags, publish dates) is publicly accessible without any subscription or login.

**Q: What is the Envato Elements License?**
A: All assets on Envato Elements are covered by the Envato Elements License, which permits use in unlimited projects for subscribers. The scraper returns this standard license for all items.

**Q: How many assets are on Envato Elements?**
A: Millions. The library grows daily. Individual categories like fonts have 1,000+ items; graphic templates have tens of thousands.

**Q: Can I download assets with this scraper?**
A: No. This actor scrapes metadata only (titles, thumbnails, tags, author info). Actual file downloads require an Envato Elements subscription.

**Q: What asset types can I scrape?**
A: Fonts, Graphic Templates, Presentation Templates, Website Templates, Video Templates, Music & Audio, Photos, Add-ons, and 3D assets.

**Q: How do I find assets by a specific author?**
A: Use `mode=search` with `searchQuery` set to the author's username. Alternatively, use `mode=byItemUrls` to enrich specific known URLs.

**Q: Can I use `sortBy=newest` to track newly added assets?**
A: Yes. Set `mode=byCategory`, `assetType=fonts` (or any type), and `sortBy=newest` to get the most recently added assets first.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/envato-elements-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
