# Markdownify MCP Server Tutorial: Run This Apify Actor with Python

Convert any webpage to clean, formatted Markdown perfect for AI consumption. Ideal for building knowledge bases, documentation scrapers, and content migration tools.

This repository shows how to run [Markdownify MCP Server](https://apify.com/crawlerbros/markdownify-mcp-server) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/markdownify-mcp-server`
- **Apify Store:** [https://apify.com/crawlerbros/markdownify-mcp-server](https://apify.com/crawlerbros/markdownify-mcp-server)
- **SEO title:** Markdownify MCP Server Tutorial: Run This Apify Actor with Python
- **Description:** Convert any webpage to clean, formatted Markdown perfect for AI consumption. Ideal for building knowledge bases, documentation scrapers, and content migration tools.

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

# Markdownify MCP Server

Convert any webpage to clean, formatted Markdown perfect for AI consumption. This Actor is ideal for building knowledge bases, documentation scrapers, and content migration tools.

## Features

✅ **Convert any webpage to Markdown** - Clean, formatted output  
✅ **CSS Selector Support** - Include/exclude specific sections  
✅ **JavaScript Rendering** - Optional Playwright support for dynamic content  
✅ **Authentication Support** - HTTP Basic Auth for restricted content  
✅ **Customizable Output** - Configure heading styles, strip tags, etc.  
✅ **Error Handling** - Graceful failures with detailed error messages  
✅ **MCP Server Ready** - Structured output for AI consumption

## How It Works

1. **Input** - Provide URL(s) and optional configuration
2. **Fetch** - Download webpage content (HTTP or Playwright)
3. **Extract** - Apply include/exclude selectors
4. **Convert** - Transform HTML to clean Markdown
5. **Output** - Save to Apify dataset with metadata

## Input Parameters

### Required

- **`urls`** (array of strings) - List of webpage URLs to convert

### Optional

- **`includeSelectors`** (array of strings) - CSS selectors to include specific sections  
  Example: `["article", ".main-content", "#documentation"]`

- **`excludeSelectors`** (array of strings) - CSS selectors to exclude  
  Example: `["nav", "footer", ".advertisement", "script", "style"]`

- **`useJavaScript`** (boolean) - Enable Playwright for JavaScript-heavy pages  
  Default: `false`

- **`headingStyle`** (string) - Markdown heading style  
  Options: `"ATX"` (# Heading) or `"SETEXT"` (Heading\n=======)  
  Default: `"ATX"`

- **`stripTags`** (array of strings) - HTML tags to completely remove  
  Default: `["script", "style", "iframe", "noscript"]`

- **`auth`** (object) - HTTP Basic Authentication credentials  
  Example: `{"username": "user", "password": "pass"}`

- **`timeout`** (integer) - Request timeout in seconds  
  Default: `30`, Range: `10-120`

## Input Example

```json
{
  "urls": ["https://apify.com/docs", "https://en.wikipedia.org/wiki/Markdown"],
  "excludeSelectors": ["nav", "footer", ".advertisement"],
  "useJavaScript": false,
  "headingStyle": "ATX",
  "timeout": 30
}
```

## Output Format

Each converted page is saved as a separate record in the dataset:

```json
{
  "url": "https://example.com",
  "title": "Example Domain",
  "markdown": "# Example Domain\n\nThis domain is for use...",
  "markdown_length": 1234,
  "success": true,
  "error": null,
  "scraped_at": "2025-10-24T10:30:00.000Z",
  "meta": {
    "method": "http",
    "heading_style": "ATX",
    "stripped_tags": ["script", "style"],
    "used_include_selectors": false,
    "used_exclude_selectors": true
  }
}
```

## Use Cases

### 📚 Build AI-Ready Knowledge Bases

Convert documentation, wikis, and help centers into Markdown for AI training or RAG systems.

### 📝 Content Migration

Migrate existing web content to Markdown for static site generators (Jekyll, Hugo, etc.).

### 🤖 AI Agent Integration

Enable AI agents to consume web content in a clean, structured format.

### 📄 Documentation Scraping

Extract and format technical documentation from multiple sources.

### 🔄 Content Synchronization

Keep Markdown versions of web pages up-to-date automatically.

## API Integration

### JavaScript/Node.js

```javascript
const { ApifyClient } = require("apify-client");

const client = new ApifyClient({ token: "YOUR_API_TOKEN" });

const input = {
  urls: ["https://example.com"],
  excludeSelectors: ["nav", "footer"],
};

const run = await client.actor("YOUR_ACTOR_ID").call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();

items.forEach((item) => {
  console.log(`Title: ${item.title}`);
  console.log(`Markdown length: ${item.markdown_length}`);
  console.log(item.markdown);
});
```

### Python

```python
from apify_client import ApifyClient

client = ApifyClient('YOUR_API_TOKEN')

input_data = {
    'urls': ['https://example.com'],
    'excludeSelectors': ['nav', 'footer']
}

run = client.actor('YOUR_ACTOR_ID').call(run_input=input_data)

for item in client.dataset(run['defaultDatasetId']).iterate_items():
    print(f"Title: {item['title']}")
    print(f"Markdown length: {item['markdown_length']}")
    print(item['markdown'])
```

### cURL

```bash
curl -X POST https://api.apify.com/v2/acts/YOUR_ACTOR_ID/runs \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://example.com"],
    "excludeSelectors": ["nav", "footer"]
  }'
```

## Tips & Best Practices

### 🚀 Performance

- Use `useJavaScript: false` for static pages (much faster)
- Only enable `useJavaScript: true` for dynamic content
- Use `includeSelectors` to extract only what you need
- Batch multiple URLs in a single run

### 🎯 Accuracy

- Test selectors in browser DevTools first
- Use specific `includeSelectors` for precise extraction
- Combine `include` and `exclude` for best results
- Add common noise elements to `excludeSelectors`

### 🔧 Troubleshooting

- **Empty markdown?** Check if selectors are correct
- **Missing content?** Try enabling `useJavaScript`
- **Timeout errors?** Increase `timeout` value
- **Authentication issues?** Verify `auth` credentials

## Development

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Run locally
python -m src
```

### Project Structure

```
markdownify-mcp/
├── .actor/
│   ├── actor.json          # Actor configuration
│   ├── input_schema.json   # Input validation
│   └── output_schema.json  # Output structure
├── src/
│   ├── __main__.py         # Main entry point
│   ├── fetcher.py          # HTTP & Playwright fetchers
│   ├── extractor.py        # Content extraction
│   └── converter.py        # HTML to Markdown
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## License

Apache 2.0

## Support

For issues, questions, or feature requests, please contact support or open an issue in the repository.

---

**Made with ❤️ for the AI community**

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/markdownify-mcp-server)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
