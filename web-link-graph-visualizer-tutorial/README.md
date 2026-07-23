# Website Links Graph Generator Tutorial: Run This Apify Actor with Python

Creates an oriented graph visualizing links between webpages. Outputs: graph.png (visual network diagram) and graph.json (structured data) saved to Key-Value Store, plus detailed dataset of all crawled pages. Configure depth, boundaries, and layout.

This repository shows how to run [Website Links Graph Generator](https://apify.com/crawlerbros/web-link-graph-visualizer) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/web-link-graph-visualizer`
- **Apify Store:** [https://apify.com/crawlerbros/web-link-graph-visualizer](https://apify.com/crawlerbros/web-link-graph-visualizer)
- **SEO title:** Website Links Graph Generator Tutorial: Run This Apify Actor with Python
- **Description:** Creates an oriented graph visualizing links between webpages. Outputs: graph.png (visual network diagram) and graph.json (structured data) saved to Key-Value Store, plus detailed dataset of all crawled pages. Configure depth, boundaries, and layout.

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

# Web Link Graph Visualizer

**Creates oriented graphs visualizing links between webpages**

Crawl a website starting from a URL, extract all links, build a directed graph of the link structure, and export it as a PNG image or JSON file.

---

## 📥 What You'll Get

After the actor completes, you'll receive:

### 🖼️ **graph.png** - Visual Network Diagram
- **Location:** Key-Value Store → `graph.png`
- **Format:** High-resolution PNG (2000x1600px)
- **Content:** Visual graph with color-coded nodes and directed edges
- **Download:** Click "Actions" → "Download" in Key-Value Store tab

### 📊 **graph.json** - Structured Data
- **Location:** Key-Value Store → `graph.json`
- **Format:** JSON file with complete graph structure
- **Content:** All nodes, edges, and statistics
- **Use:** Import into analysis tools or custom visualizations

### 📑 **Dataset** - All Crawled Pages
- **Location:** Dataset tab (Storage section)
- **Format:** JSON records (one per page)
- **Content:** URL, title, depth, all links per page
- **Export:** CSV, JSON, or Excel from Dataset tab

### 🔍 **Where to Find in Apify Console:**

1. After actor finishes, go to **"Storage"** section
2. **Key-Value Store tab:**
   - Download `graph.png` (your visual graph image)
   - Download `graph.json` (data for analysis)
3. **Dataset tab:**
   - View/export all crawled pages
   - See links extracted from each page

---

## Features

✅ **Smart Crawling:**
- Start from any URL
- Follow links matching a boundary regex
- Configurable depth and page limits
- Respects robots.txt (via Playwright)
- Adjustable request delays

✅ **Graph Building:**
- Directed graph (oriented edges)
- Track internal vs external links
- URL normalization (remove fragments, trailing slashes)
- Depth tracking for each node
- Duplicate link detection

✅ **Visualization:**
- Multiple layout algorithms (hierarchical, spring, circular, random)
- Customizable node labels (URL, path, title, or index)
- Color-coded nodes (internal=blue, external=red)
- High-resolution PNG export
- JSON export for programmatic use

✅ **Statistics:**
- Total nodes and edges
- Average outgoing links per page
- Max depth reached
- Internal vs external link counts

---

## Input Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startUrl` | String | **Required** | The URL to start crawling from |
| `boundaryRegex` | String | `.*` | Regex to limit which URLs to crawl |
| `maxDepth` | Integer | `3` | Maximum crawl depth (1-10) |
| `maxPages` | Integer | `50` | Maximum pages to crawl (1-1000) |
| `exportFormat` | Select | `both` | Output format: `both`, `image`, or `json` |
| `graphLayout` | Select | `hierarchical` | Layout: `hierarchical`, `spring`, `circular`, `random` |
| `nodeLabels` | Select | `path` | Label type: `url`, `path`, `title`, `index` |
| `includeExternal` | Boolean | `true` | Show external links in graph |
| `waitForSelector` | String | - | CSS selector to wait for (optional) |
| `requestDelay` | Integer | `1000` | Delay between requests (ms) |

---

## Example Inputs

### Example 1: Small Website
```json
{
  "startUrl": "https://example.com",
  "boundaryRegex": "^https://example\\.com/.*",
  "maxDepth": 2,
  "maxPages": 20,
  "exportFormat": "both",
  "graphLayout": "hierarchical",
  "nodeLabels": "path"
}
```

### Example 2: Documentation Site
```json
{
  "startUrl": "https://docs.python.org/3/",
  "boundaryRegex": "^https://docs\\.python\\.org/3/tutorial/.*",
  "maxDepth": 3,
  "maxPages": 50,
  "exportFormat": "image",
  "graphLayout": "spring",
  "nodeLabels": "title",
  "includeExternal": false,
  "requestDelay": 500
}
```

### Example 3: Blog with Subdomains
```json
{
  "startUrl": "https://blog.example.com",
  "boundaryRegex": "^https://.*\\.example\\.com/.*",
  "maxDepth": 2,
  "maxPages": 30,
  "exportFormat": "both",
  "graphLayout": "circular",
  "nodeLabels": "path"
}
```

---

## Output

### Dataset
Each crawled page is saved to the dataset with:
- `url` - Page URL
- `title` - Page title
- `depth` - Depth from start URL
- `links` - All extracted links
- `internal_links` - Links matching boundary
- `external_links` - Links outside boundary
- `crawled_at` - Timestamp

### Key-Value Store

**graph.json** (if JSON export enabled):
```json
{
  "graph": {
    "nodes": [
      {
        "id": "https://example.com",
        "url": "https://example.com",
        "title": "Example Domain",
        "depth": 0,
        "is_internal": true,
        "outgoing_links": 3
      }
    ],
    "edges": [
      {
        "source": "https://example.com",
        "target": "https://example.com/page1"
      }
    ],
    "directed": true
  },
  "statistics": {
    "nodes": 15,
    "edges": 42,
    "crawled_pages": 15,
    "external_links": 3,
    "avg_outgoing_links": 2.8,
    "max_depth_reached": 2
  }
}
```

**graph.png** (if image export enabled):
- High-resolution PNG image (2000x1600px)
- Color-coded nodes (blue=internal, red=external)
- Directed edges with arrows
- Legend and statistics

**OUTPUT**:
```json
{
  "start_url": "https://example.com",
  "statistics": {
    "nodes": 15,
    "edges": 42,
    "crawled_pages": 15
  },
  "exports": {
    "json": true,
    "image": true
  }
}
```

---

## Boundary Regex Examples

| Pattern | Matches |
|---------|---------|
| `^https://example\\.com/.*` | All pages on example.com |
| `^https://example\\.com/blog/.*` | Only blog section |
| `^https://.*\\.example\\.com/.*` | All subdomains |
| `^https://example\\.com/(?!admin).*` | Exclude admin section |
| `.*` | Everything (no boundary) |

---

## Use Cases

🔍 **SEO Analysis:**
- Visualize site structure
- Find orphan pages
- Identify link depth issues

📊 **Content Strategy:**
- Map content relationships
- Find hub pages
- Identify external dependencies

🔗 **Link Building:**
- Discover internal linking opportunities
- Find broken link paths
- Analyze link distribution

🛠️ **Site Migration:**
- Document current structure
- Plan URL redirects
- Validate link integrity

---

## Graph Layouts

### Hierarchical (Default)
Best for: Sites with clear hierarchy (docs, blogs)
- Top-down structure
- Shows depth clearly

### Spring (Force-Directed)
Best for: Discovering clusters
- Nodes repel/attract based on connections
- Reveals natural groupings

### Circular
Best for: Small sites
- Nodes arranged in a circle
- Shows connections clearly

### Random
Best for: Quick visualization
- Fast to generate
- Good for dense graphs

---

## Node Label Types

| Type | Example | Best For |
|------|---------|----------|
| `url` | `https://example.com/page` | Small graphs |
| `path` | `/blog/post-title` | Medium graphs (default) |
| `title` | `My Blog Post` | Readable labels |
| `index` | `1`, `2`, `3` | Large graphs |

---

## Performance Tips

1. **Start Small:**
   - Use `maxPages: 20` for initial runs
   - Increase gradually

2. **Tight Boundaries:**
   - Use specific regex patterns
   - Avoid crawling entire domains

3. **Adjust Depth:**
   - Depth 2-3 is usually sufficient
   - Depth 4+ can explode exponentially

4. **Request Delays:**
   - Use 1000ms+ for courtesy
   - Reduce for fast sites

5. **External Links:**
   - Set `includeExternal: false` for cleaner graphs
   - Enable to see dependencies

---

## Limitations

- **Max Pages:** 1000 (configurable limit)
- **Max Depth:** 10 (configurable limit)
- **JavaScript:** Rendered via Playwright (may be slow)
- **Image Size:** Large graphs (100+ nodes) may have small labels

---

## Technical Details

**Built With:**
- Python 3.11
- Apify SDK
- Playwright (browser automation)
- BeautifulSoup4 (HTML parsing)
- NetworkX (graph algorithms)
- Matplotlib (visualization)

**Graph Type:**
- Directed graph (DiGraph)
- Nodes = URLs
- Edges = Links (from → to)

**URL Normalization:**
- Removes fragments (#section)
- Removes trailing slashes
- Preserves query strings
- Converts relative to absolute

---

## Example Output

### Small Site (10 pages)
```
Nodes: 10
Edges: 28
Crawled pages: 10
External links: 3
Avg links per page: 2.8
Max depth reached: 2
```

### Documentation Site (50 pages)
```
Nodes: 53 (50 internal + 3 external)
Edges: 142
Crawled pages: 50
External links: 3
Avg links per page: 2.7
Max depth reached: 3
```

---

## Troubleshooting

**Issue: No links found**
- Check `waitForSelector` for dynamic sites
- Verify boundary regex matches start URL

**Issue: Too many nodes**
- Reduce `maxPages` or `maxDepth`
- Tighten boundary regex

**Issue: Image labels too small**
- Use `nodeLabels: "index"` for large graphs
- Reduce number of nodes

**Issue: Slow crawling**
- Reduce `requestDelay`
- Decrease `maxPages`
- Check site performance

---

## Support

For issues or questions:
1. Check input parameters
2. Verify boundary regex
3. Test with small `maxPages` first
4. Review dataset for crawl results

---

## License

MIT License - Free for commercial and personal use

---

*Built with ❤️ using Apify SDK*

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/web-link-graph-visualizer)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
