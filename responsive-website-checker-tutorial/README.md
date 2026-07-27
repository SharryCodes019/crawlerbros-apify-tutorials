# Responsive Website Checker Tutorial: Run This Apify Actor with Python

Test and verify how websites render across multiple devices and screen sizes. Capture screenshots on real iOS/Android devices, tablets, and desktops. Analyze responsive breakpoints, interactive elements, and performance metrics.

This repository shows how to run [Responsive Website Checker](https://apify.com/crawlerbros/responsive-website-checker) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/responsive-website-checker`
- **Apify Store:** [https://apify.com/crawlerbros/responsive-website-checker](https://apify.com/crawlerbros/responsive-website-checker)
- **SEO title:** Responsive Website Checker Tutorial: Run This Apify Actor with Python
- **Description:** Test and verify how websites render across multiple devices and screen sizes. Capture screenshots on real iOS/Android devices, tablets, and desktops. Analyze responsive breakpoints, interactive elements, and performance metrics.

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

# Responsive Website Checker

Test and verify how websites render across multiple devices and screen sizes. Capture screenshots on real iOS/Android devices, tablets, and desktops. Analyze responsive breakpoints, interactive elements, and performance metrics.

## Features

- **40+ Device Presets**: Automatically test on iPhone, Samsung Galaxy, Google Pixel, iPad, and desktop devices
- **Dual Orientation**: Mobile and tablet devices tested in both portrait and landscape modes
- **Full-Page Screenshots**: Capture complete page screenshots with direct download URLs
- **Performance Metrics**: DOM load time, First Contentful Paint, and transfer size
- **Layout Analysis**: Detect horizontal overflow and touch target sizing issues
- **Interactive Element Testing**: Count buttons, links, and identify usability issues

## Input

Simple configuration - just provide the URLs to test:

```json
{
  "urls": [
    "https://www.example.com",
    "https://www.mywebsite.com"
  ]
}
```

## Output

Each device test generates one output row with comprehensive data:

```json
{
  "url": "https://www.example.com",
  "device_name": "iPhone 14",
  "orientation": "portrait",
  "category": "mobile",
  "brand": "Apple",
  "viewport_width": 390,
  "viewport_height": 844,
  "device_pixel_ratio": 3,
  "screenshot_url": "https://api.apify.com/v2/key-value-stores/{storeId}/records/iPhone_14_portrait_abc123.png",
  "page_width": 390,
  "page_height": 2400,
  "issues": "Horizontal overflow: 420px > 390px",
  "buttons_count": 15,
  "links_count": 42,
  "small_touch_targets": 2,
  "dom_load_ms": 1250,
  "page_load_ms": 2100,
  "first_contentful_paint_ms": 1050,
  "transfer_size_bytes": 524288,
  "tested_at": "2024-01-15T10:30:15.123Z",
  "status": "success"
}
```

### Screenshot URLs

Each test includes a `screenshot_url` field with a direct link to the full-page screenshot:
- Click the URL to view the screenshot in your browser
- Download programmatically via Apify API
- Screenshots are stored in the run's key-value store

## Supported Devices

### Mobile Phones (Portrait + Landscape)

**Apple iPhone**
- iPhone SE, 12, 12 Pro, 13, 13 Pro Max, 14, 14 Pro Max, 15 Pro, 15 Pro Max

**Samsung Galaxy**
- Galaxy S20, S21, S22, S23, S23 Ultra

**Google Pixel**
- Pixel 5, 6, 6 Pro, 7, 7 Pro, 8, 8 Pro

### Tablets (Portrait + Landscape)

**Apple iPad**
- iPad Mini, iPad Air, iPad Pro 11", iPad Pro 12.9"

**Android Tablets**
- Galaxy Tab S7, Nexus 7, Nexus 10, Kindle Fire HDX

### Desktop (Portrait Only)

**Windows Desktop**
- 1920x1080 (Full HD), 1920x1200 (WUXGA), 1440x900 (WXGA+), 1366x768 (HD)

**Mac Desktop**
- MacBook Pro 13", 14", 16", iMac 27"

**Total**: 66 device tests per URL (37 portrait + 29 landscape)

## Output Fields

| Field | Description |
|-------|-------------|
| `url` | The tested website URL |
| `device_name` | Device model name |
| `orientation` | `portrait` or `landscape` |
| `category` | `mobile`, `tablet`, or `desktop` |
| `brand` | Device manufacturer |
| `viewport_width` | Viewport width in pixels |
| `viewport_height` | Viewport height in pixels |
| `device_pixel_ratio` | Device pixel ratio (e.g., 2 for Retina) |
| `screenshot_url` | Direct URL to full-page screenshot |
| `page_width` | Actual page content width |
| `page_height` | Actual page content height |
| `issues` | Layout issues detected (if any) |
| `buttons_count` | Number of buttons/clickable elements |
| `links_count` | Number of links |
| `small_touch_targets` | Count of elements smaller than 44px |
| `dom_load_ms` | DOM content loaded time (ms) |
| `page_load_ms` | Full page load time (ms) |
| `first_contentful_paint_ms` | First Contentful Paint (ms) |
| `transfer_size_bytes` | Total data transferred |
| `tested_at` | ISO timestamp of test |
| `status` | `success` or `error` |

## Use Cases

### Web Development
- Pre-launch testing across all target devices
- Continuous monitoring after updates
- Design validation against mockups

### Quality Assurance
- Automated responsive testing in CI/CD
- Regression testing for layout breaks
- Visual documentation for stakeholders

### SEO & Mobile-First
- Verify mobile experience meets Google's requirements
- Identify issues affecting mobile users
- Ensure cross-device consistency

## Performance

- **Parallel Execution**: Tests run in batches of 5 devices simultaneously
- **Fast Results**: ~66 device tests complete in under 2 minutes
- **Full Coverage**: Automatically tests all devices without configuration

## Interpreting Results

### Layout Issues

**Horizontal Overflow**
- Content is wider than viewport
- Common causes: fixed-width elements, large images, tables
- Solution: Use responsive units (%, vw) and max-width

**Small Touch Targets**
- Buttons/links smaller than 44x44px recommended size
- Can cause frustration on mobile devices
- Solution: Increase padding, use larger hit areas

### Performance Guidelines

- **First Contentful Paint < 1.5s**: Good mobile performance
- **DOM Content Loaded < 2s**: Page is interactive quickly
- **Transfer Size**: Watch mobile data usage

## Integration

### Apify SDK (JavaScript)

```javascript
const { ApifyClient } = require('apify-client');

const client = new ApifyClient({ token: 'YOUR_API_TOKEN' });

const run = await client.actor('YOUR_ACTOR_ID').call({
  urls: ['https://www.example.com']
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();

// Each item is one device test
items.forEach(test => {
  console.log(`${test.device_name} (${test.orientation}): ${test.screenshot_url}`);
});
```

### Python

```python
from apify_client import ApifyClient

client = ApifyClient('YOUR_API_TOKEN')

run = client.actor('YOUR_ACTOR_ID').call(
    run_input={'urls': ['https://www.example.com']}
)

dataset = client.dataset(run['defaultDatasetId']).list_items()

# Each item is one device test
for test in dataset.items:
    print(f"{test['device_name']} ({test['orientation']}): {test['screenshot_url']}")
```

## Troubleshooting

### Screenshots are blank
- Website may block automation/headless browsers
- Check if website requires authentication
- Verify website is publicly accessible

### Tests failing
- Check URL is valid and accessible
- Some websites have anti-bot protection
- Try testing on a simpler website first

## Example Output

For one URL, you'll get 66 output rows:
- 9 iPhone models × 2 orientations = 18 tests
- 4 iPad models × 2 orientations = 8 tests
- 5 Galaxy models × 2 orientations = 10 tests
- 7 Pixel models × 2 orientations = 14 tests
- 3 Tablet models × 2 orientations = 6 tests
- 8 Desktop models × 1 orientation = 8 tests
- 1 Kindle × 2 orientations = 2 tests

**Total: 66 comprehensive device tests per URL**

## License

Apache 2.0 License

---

Built with Playwright and Apify for comprehensive responsive testing

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/responsive-website-checker)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
