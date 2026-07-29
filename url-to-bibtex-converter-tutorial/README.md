# URL to BibTeX Converter Tutorial: Run This Apify Actor with Python

Convert any URL (academic papers, articles, books, web pages) to properly formatted BibTeX citations. Automatically extracts metadata from arXiv, PubMed, IEEE, ACM, and general web pages. Supports multiple citation types.

This repository shows how to run [URL to BibTeX Converter](https://apify.com/crawlerbros/url-to-bibtex-converter) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/url-to-bibtex-converter`
- **Apify Store:** [https://apify.com/crawlerbros/url-to-bibtex-converter](https://apify.com/crawlerbros/url-to-bibtex-converter)
- **SEO title:** URL to BibTeX Converter Tutorial: Run This Apify Actor with Python
- **Description:** Convert any URL (academic papers, articles, books, web pages) to properly formatted BibTeX citations. Automatically extracts metadata from arXiv, PubMed, IEEE, ACM, and general web pages. Supports multiple citation types.

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

# URL to BibTeX Converter

**Apify Actor for converting URLs to properly formatted BibTeX citations**

Convert any URL (academic papers, articles, books, web pages) to BibTeX format for use in LaTeX documents and reference managers.

## Features

✅ **Multiple Source Support**
- arXiv papers (specialized parser)
- PubMed articles (specialized parser)
- IEEE, Nature, and other academic journals
- Generic web pages with metadata

✅ **Batch Processing**
- Convert single URL or multiple URLs at once
- Efficient browser reuse
- Progress logging

✅ **Smart Extraction**
- Auto-detects entry type (@article, @book, @misc, etc.)
- Generates citation keys automatically
- Extracts all available metadata
- Handles missing fields gracefully

✅ **Valid BibTeX Output**
- Proper syntax and formatting
- Special character escaping
- Title capitalization preservation
- Ready for LaTeX/BibTeX

## Input

### Single URL
```json
{
  "url": "https://arxiv.org/abs/1706.03762",
  "includeAbstract": true,
  "includeUrl": true
}
```

### Batch Mode
```json
{
  "urls": [
    "https://arxiv.org/abs/1706.03762",
    "https://arxiv.org/abs/2103.15348",
    "https://www.nature.com/articles/s41586-021-03819-2"
  ],
  "includeAbstract": false,
  "includeUrl": true
}
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `url` | string | No* | - | Single URL to convert |
| `urls` | array | No* | [] | Multiple URLs for batch mode |
| `citationKey` | string | No | auto | Custom citation key |
| `entryType` | string | No | "auto" | Force entry type |
| `includeAbstract` | boolean | No | false | Include abstract in output |
| `includeUrl` | boolean | No | true | Include source URL |

*Either `url` or `urls` is required

## Output

### Dataset (per URL)
```json
{
  "url": "https://arxiv.org/abs/1706.03762",
  "citation_key": "vaswani2017attention",
  "entry_type": "article",
  "source": "arxiv",
  "title": "Attention Is All You Need",
  "authors": "Ashish Vaswani and Niki Parmar and ...",
  "year": "2017",
  "venue": "arXiv",
  "doi": null,
  "bibtex": "@article{vaswani2017attention,\n  title = {{Attention Is All You Need}},\n  author = {Ashish Vaswani and ...},\n  year = {2017},\n  journal = {arXiv},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/1706.03762},\n  arxivid = {1706.03762}\n}",
  "metadata": { ... },
  "scraped_at": "2025-11-03T12:14:14.392189"
}
```

### BibTeX Format
```bibtex
@article{vaswani2017attention,
  title = {{Attention Is All You Need}},
  author = {Ashish Vaswani and Niki Parmar and Llion Jones and Lukasz Kaiser},
  year = {2017},
  journal = {arXiv},
  note = {arXiv preprint},
  url = {https://arxiv.org/abs/1706.03762},
  arxivid = {1706.03762}
}
```

## Test Results

**100% Success Rate** (8/8 tests passed)

### Tested Sources
- ✅ arXiv papers (Attention is All You Need, LayoutParser)
- ✅ PubMed articles
- ✅ IEEE Xplore papers
- ✅ Nature articles (AlphaFold)
- ✅ Batch mode (3 URLs)

### Validation
- ✅ All BibTeX entries syntactically valid
- ✅ Proper field extraction
- ✅ Special character handling
- ✅ Citation key generation
- ✅ Entry type detection

See [TEST_RESULTS.txt](./TEST_RESULTS.txt) for comprehensive test report.

## Usage Examples

### Command Line (Apify)
```bash
apify run
```

### Python Script
```python
from apify import Actor

async with Actor:
    actor_input = {
        "url": "https://arxiv.org/abs/1706.03762",
        "includeAbstract": True
    }
    # ... scraping logic
```

### Test Suite
```bash
python3 test_bibtex.py
```

## Supported Entry Types

- `@article` - Journal/magazine articles
- `@book` - Books
- `@inproceedings` - Conference papers
- `@misc` - Miscellaneous (fallback)
- `@techreport` - Technical reports
- `@phdthesis` - PhD dissertations
- `@mastersthesis` - Master's theses
- `@unpublished` - Unpublished works

## Citation Key Generation

**Format:** `firstauthor + year + titleword`

**Examples:**
- `vaswani2017attention`
- `shen2021layoutparser`
- `smith2023deep`

**Fallback:** If metadata is incomplete, generates timestamp-based key

## Metadata Extraction

### arXiv Papers
- Title, authors, abstract, year
- arXiv ID
- DOI (if published)
- Preprint notation

### PubMed Articles
- Title, authors, journal
- Volume, issue, pages
- DOI, PMID
- Publication date

### Generic Sites
- JSON-LD structured data
- OpenGraph meta tags
- Twitter Card meta tags
- Dublin Core metadata
- Citation meta tags

## Error Handling

- ✅ Missing metadata fields (uses defaults/nulls)
- ✅ Page load failures (returns error object)
- ✅ Timeout scenarios (30s timeout)
- ✅ Special characters (proper escaping)
- ✅ Invalid URLs (validation error)

## Use Cases

1. **Academic Writing**
   - Generate BibTeX for LaTeX papers
   - Build bibliographies for theses
   - Organize references

2. **Literature Review**
   - Batch convert multiple papers
   - Extract metadata for databases
   - Automate citation management

3. **Integration**
   - API for citation generation
   - Workflow automation
   - Reference manager sync

## Performance

- **Average time per URL:** 5-8 seconds
- **Batch mode (3 URLs):** ~30 seconds
- **Success rate:** 100%
- **Memory:** Efficient (reuses browser)

## Requirements

```
apify>=2.1.0,<3.0.0
playwright~=1.40.0
beautifulsoup4~=4.12.0
lxml~=4.9.0
```

## Files

```
URL-to-BibTeX/
├── src/
│   ├── __main__.py          # Entry point
│   └── main.py              # Main scraper logic
├── .actor/
│   ├── actor.json           # Actor configuration
│   ├── input_schema.json    # Input schema
│   └── INPUT.json           # Test input
├── test_bibtex.py           # Comprehensive tests
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker configuration
├── README.md                # This file
└── TEST_RESULTS.txt         # Detailed test report
```

## Status

**Production Ready ✅**

- Comprehensive testing complete
- All validations passed
- Error handling robust
- Documentation complete
- Ready for deployment

## License

See parent project license.

## Support

For issues or questions, please refer to the test results or check the source code comments.

---

**Built with:** Apify SDK, Playwright, BeautifulSoup
**Test Date:** November 3, 2025
**Test Coverage:** 100% (8/8 tests passed)

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/url-to-bibtex-converter)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
