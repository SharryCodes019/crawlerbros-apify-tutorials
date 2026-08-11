# Google Maps Area Scanner Tutorial: Run This Apify Actor with Python

Comprehensive geographic area scanner that bypasses Google Maps' 120-place limit using grid-based systematic coverage. Supports polygon, circle, and bounding box inputs for complete market mapping and saturation analysis.

This repository shows how to run [Google Maps Area Scanner](https://apify.com/crawlerbros/google-maps-area-scanner) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-area-scanner`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-area-scanner](https://apify.com/crawlerbros/google-maps-area-scanner)
- **SEO title:** Google Maps Area Scanner Tutorial: Run This Apify Actor with Python
- **Description:** Comprehensive geographic area scanner that bypasses Google Maps' 120-place limit using grid-based systematic coverage. Supports polygon, circle, and bounding box inputs for complete market mapping and saturation analysis.

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

# Google Maps Area Scanner

Comprehensive geographic area scanner that bypasses Google Maps' 120-place result limit. Perfect for complete market mapping, competitor analysis, and saturation studies.

## What It Does

Google Maps typically limits search results to 120 places. This actor overcomes that limitation by:

1. Dividing your target area into a grid of smaller zones
2. Searching each zone independently
3. Combining and deduplicating all results
4. Returning comprehensive coverage of the entire area

## Input Options

You must provide **one** geographic area definition:

### Bounding Box (Recommended)
Define a rectangular area using coordinates:
- `north` - Northern latitude boundary
- `south` - Southern latitude boundary
- `east` - Eastern longitude boundary
- `west` - Western longitude boundary

### Circle
Define a circular area:
- `circleCenter` - Center point with `lat` and `lng`
- `radiusKm` - Radius in kilometers

### GeoJSON Polygon
For irregular shapes, provide a GeoJSON Polygon with coordinates.

## Input Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| Search Query | Yes | pharmacy | What to search for (pharmacy, restaurant, hotel, etc.) |
| Bounding Box | One of three | - | Rectangular area coordinates |
| Circle Center | One of three | - | Center point for circular search |
| Radius (km) | No | 5 | Circle radius in kilometers |
| Custom Geolocation | One of three | - | GeoJSON Polygon |
| Zoom Level | No | 15 | Grid detail level (12-18). Higher = more thorough |
| Max Places Per Cell | No | 120 | Maximum results per grid cell |
| Deduplicate Results | No | true | Remove duplicate places |
| Proxy Configuration | No | Apify Proxy | Recommended for reliable scraping |

### Zoom Level Guide

| Zoom | Cell Size | Best For |
|------|-----------|----------|
| 12 | ~5 km | Large rural areas, quick overview |
| 13 | ~2.5 km | Suburban regions |
| 14 | ~1.25 km | Mixed urban/suburban |
| **15** | **~625 m** | **Recommended - balanced coverage** |
| 16 | ~312 m | Dense urban areas |
| 17 | ~156 m | Very dense areas |
| 18 | ~78 m | Maximum detail |

## Output Fields

Each business result includes:

| Field | Description |
|-------|-------------|
| name | Business name |
| rating | Star rating (1-5) |
| review_count | Number of reviews |
| category | Business type |
| address | Full street address |
| phone | Phone number with country code |
| website | Business website URL |
| description | Business description (when available) |
| price_level | Price indicator ($, $$, $$$) when available |
| place_id | Google Maps unique identifier |
| plus_code | Google Plus Code location |
| latitude | Geographic latitude |
| longitude | Geographic longitude |
| images | Array of image URLs |
| url | Direct Google Maps link |
| scraped_at | Timestamp of extraction |
| searchGridCell | Grid cell metadata (row, col, bounds, center) |

## Example Use Cases

- **Market Research**: Find all pharmacies in a city district
- **Competitor Analysis**: Map all restaurants in a neighborhood
- **Site Selection**: Analyze business density for new locations
- **Lead Generation**: Extract contact details for businesses in an area

## Tips for Best Results

1. **Start with a small test area** to verify the search query returns expected results
2. **Use zoom level 15** for most use cases - good balance of coverage and speed
3. **Enable proxy** for reliable scraping without rate limits
4. **Keep deduplication on** to avoid counting businesses twice

## Limitations

- Results depend on Google Maps data availability
- Some business details (description, price level) may not be available for all listings
- Large areas with high zoom levels will take longer to process

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-area-scanner)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
