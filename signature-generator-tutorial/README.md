# Signature Generator Tutorial: Run This Apify Actor with Python

Create professional email signatures in seconds! Choose from multiple templates, customize with your brand colors and logo, add social media icons, and export to HTML (copy-paste ready for Gmail/Outlook), PNG, JPG, or SVG. All outputs are saved to the dataset and downloadable from the Storage tab.

This repository shows how to run [Signature Generator](https://apify.com/crawlerbros/signature-generator) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/signature-generator`
- **Apify Store:** [https://apify.com/crawlerbros/signature-generator](https://apify.com/crawlerbros/signature-generator)
- **SEO title:** Signature Generator Tutorial: Run This Apify Actor with Python
- **Description:** Create professional email signatures in seconds! Choose from multiple templates, customize with your brand colors and logo, add social media icons, and export to HTML (copy-paste ready for Gmail/Outlook), PNG, JPG, or SVG. All outputs are saved to the dataset and downloadable from the Storage tab.

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

# Email Signature Generator

Generate professional email signatures with customizable templates, branding, and multi-format export (HTML, PNG, JPG, SVG). Perfect for businesses, freelancers, and professionals.

## Overview

Creating a professional email signature can be a time-consuming task, especially for businesses that need consistent branding across multiple employees. The **Email Signature Generator Actor** simplifies this process by automating the creation of customized email and digital signatures. Users can input their name, title, contact information, company details, and branding preferences to generate personalized signature templates.

## Key Features

### Multiple Templates

Choose from a variety of professional designs to match your brand personality:

- **Minimalist** - Clean and simple design with minimal styling
- **Corporate** - Professional with company logo emphasis
- **Creative** - Modern with color accents and visual hierarchy
- **Modern** - Balanced design with social icons and branding

### Social Media Integration

Automatically includes clickable icons for platforms like:

- LinkedIn
- Twitter/X
- GitHub
- Facebook
- Instagram

### Brand Customization

- Upload logos via URL
- Select custom color schemes (primary and secondary colors)
- Choose custom fonts (web-safe or Google Fonts)
- Add company details and contact information

### Multi-Format Export

Export signatures in multiple formats for maximum compatibility:

- **HTML** - Email-ready with inline CSS, compatible with Gmail, Outlook, Apple Mail
- **PNG** - High-quality raster image (400-1200px width)
- **JPG** - Compressed image format
- **SVG** - Scalable vector graphics for print and web

### Additional Features

- Optional email disclaimer text
- Customizable image dimensions
- Responsive design for mobile email clients
- Email client compatibility (tested with major providers)

## Target Audience

This Actor is perfect for:

- **Small business owners** looking to maintain professional branding
- **Freelancers and consultants** who need polished email signatures
- **Marketing professionals** managing multiple client signatures
- **HR departments** setting up consistent formats for new employees
- **Agencies** creating signatures for multiple clients

## Benefits

✅ **Time-saving** - Automates the design process, saving hours of manual work

✅ **Brand consistency** - Ensures uniform branding across all company communications

✅ **Professional image** - Enhances credibility in email correspondence

✅ **User-friendly** - Reduces the technical barrier for non-designers to create attractive signatures

✅ **Scalable solutions** - Provides options for businesses needing multiple signature variations for different departments or team members

## Input Parameters

### Required Fields

| Field      | Type   | Description                                                                 |
| ---------- | ------ | --------------------------------------------------------------------------- |
| `name`     | String | Your full name as it will appear in the signature                           |
| `email`    | String | Your professional email address                                             |
| `template` | String | Signature design template (`minimalist`, `corporate`, `creative`, `modern`) |

### Optional Fields

| Field     | Type   | Description                          |
| --------- | ------ | ------------------------------------ |
| `title`   | String | Your professional title or position  |
| `company` | String | Your company or organization name    |
| `phone`   | String | Your contact phone number            |
| `website` | String | Your personal or company website URL |
| `address` | String | Your business address                |

### Social Media Links

Provide URLs for your social media profiles:

```json
{
  "socialMedia": {
    "linkedin": "https://www.linkedin.com/in/yourprofile",
    "twitter": "https://twitter.com/yourhandle",
    "github": "https://github.com/yourusername",
    "facebook": "https://facebook.com/yourpage",
    "instagram": "https://instagram.com/yourhandle"
  }
}
```

### Branding Options

```json
{
  "branding": {
    "logoUrl": "https://example.com/logo.png",
    "primaryColor": "#0066cc",
    "secondaryColor": "#666666",
    "fontFamily": "Arial, Helvetica, sans-serif"
  }
}
```

### Output Configuration

| Field               | Type    | Default    | Description                                       |
| ------------------- | ------- | ---------- | ------------------------------------------------- |
| `outputFormats`     | Array   | `["html"]` | Formats to generate (`html`, `png`, `jpg`, `svg`) |
| `imageWidth`        | Integer | `600`      | Width for image exports (400-1200 pixels)         |
| `includeDisclaimer` | Boolean | `false`    | Add a legal disclaimer                            |
| `disclaimerText`    | String  | -          | Custom disclaimer text                            |

## Usage Examples

### Example 1: Minimalist Signature

```json
{
  "name": "Sarah Johnson",
  "title": "Senior Marketing Manager",
  "company": "Digital Innovations Inc.",
  "email": "sarah.johnson@digitalinnovations.com",
  "phone": "+1 (555) 123-4567",
  "website": "https://www.digitalinnovations.com",
  "template": "minimalist",
  "socialMedia": {
    "linkedin": "https://www.linkedin.com/in/sarahjohnson",
    "twitter": "https://twitter.com/sarahj_marketing"
  },
  "branding": {
    "primaryColor": "#2c3e50"
  },
  "outputFormats": ["html", "png"]
}
```

### Example 2: Corporate Signature with Logo

```json
{
  "name": "Michael Chen",
  "title": "Chief Technology Officer",
  "company": "TechCorp Solutions",
  "email": "michael.chen@techcorp.com",
  "phone": "+1 (555) 987-6543",
  "website": "https://www.techcorp.com",
  "address": "123 Innovation Drive, Silicon Valley, CA 94025",
  "template": "corporate",
  "socialMedia": {
    "linkedin": "https://www.linkedin.com/in/michaelchen",
    "twitter": "https://twitter.com/mchen_tech",
    "github": "https://github.com/mchen"
  },
  "branding": {
    "logoUrl": "https://www.techcorp.com/logo.png",
    "primaryColor": "#0066cc",
    "secondaryColor": "#666666"
  },
  "outputFormats": ["html", "png", "svg"]
}
```

### Example 3: Creative Signature

```json
{
  "name": "Emma Rodriguez",
  "title": "Creative Director",
  "company": "Pixel Perfect Studio",
  "email": "emma@pixelperfect.design",
  "phone": "+1 (555) 246-8135",
  "website": "https://www.pixelperfect.design",
  "template": "creative",
  "socialMedia": {
    "linkedin": "https://www.linkedin.com/in/emmarodriguez",
    "instagram": "https://instagram.com/emmacreates"
  },
  "branding": {
    "primaryColor": "#ff6b6b",
    "secondaryColor": "#4ecdc4"
  },
  "outputFormats": ["html", "png", "jpg"]
}
```

## Output

The Actor generates and stores files in the Apify Key-Value Store and pushes structured data to the dataset:

### Dataset Output

```json
{
  "name": "Sarah Johnson",
  "email": "sarah.johnson@digitalinnovations.com",
  "title": "Senior Marketing Manager",
  "company": "Digital Innovations Inc.",
  "phone": "+1 (555) 123-4567",
  "website": "https://www.digitalinnovations.com",
  "template": "minimalist",
  "outputFormats": ["html", "png"],
  "htmlContent": "<table>...</table>",
  "htmlUrl": "https://api.apify.com/v2/key-value-stores/.../signature_Sarah_Johnson_20250106_143022.html",
  "imageUrl": "https://api.apify.com/v2/key-value-stores/.../signature_Sarah_Johnson_20250106_143022.png",
  "socialMedia": {...},
  "branding": {...},
  "createdAt": "2025-01-06T14:30:22.123Z"
}
```

### File Storage

Generated files are stored in the Key-Value Store with public URLs:

- `signature_[Name]_[Timestamp].html` - Full HTML document
- `signature_[Name]_[Timestamp].png` - PNG image
- `signature_[Name]_[Timestamp].jpg` - JPG image
- `signature_[Name]_[Timestamp].svg` - SVG vector file

## Email Client Compatibility

The generated HTML signatures are optimized for:

✅ **Gmail** (Web and Mobile)
✅ **Outlook** (Windows, Mac, Web)
✅ **Apple Mail** (macOS, iOS)
✅ **Yahoo Mail**
✅ **Thunderbird**
✅ **Mobile Email Apps** (iOS Mail, Android Gmail)

### Installation Tips

#### For Gmail:

1. Copy the HTML content from the output
2. Go to Settings > See all settings > General > Signature
3. Paste the HTML (use "Insert HTML" option or paste directly)
4. Save changes

#### For Outlook (Windows):

1. Download the HTML file
2. Open Outlook > File > Options > Mail > Signatures
3. Click "New" and paste the HTML content
4. Save

#### For Apple Mail:

1. Download the HTML file
2. Open the file in a web browser
3. Select all content (Cmd+A) and copy (Cmd+C)
4. Go to Mail > Preferences > Signatures
5. Create new signature and paste (Cmd+V)

## Local Testing

Test the signature generator locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Run tests
python test_signatures.py
```

Test outputs will be saved to `test_output/` directory.

## Technical Details

### Architecture

- **Language**: Python 3.12
- **Framework**: Apify SDK 2.1+
- **Browser**: Playwright (Chromium)
- **Validation**: Pydantic v2
- **Templating**: Native Python with inline CSS

### Dependencies

- `apify` - Apify SDK for actor development
- `playwright` - Browser automation for image generation
- `pydantic` - Data validation and type safety
- `svgwrite` - SVG generation
- `beautifulsoup4` - HTML parsing
- `pillow` - Image processing

### Project Structure

```
Signature-Generator/
├── .actor/
│   ├── actor.json              # Actor metadata
│   ├── input_schema.json       # Input parameters schema
│   ├── output_schema.json      # Output structure
│   └── test_inputs/            # Test cases
├── src/
│   ├── __main__.py             # Entry point
│   ├── main.py                 # Main orchestrator
│   ├── templates/              # Signature templates
│   │   ├── minimalist.py
│   │   ├── corporate.py
│   │   ├── creative.py
│   │   └── modern.py
│   ├── generators/             # Format generators
│   │   ├── html_generator.py
│   │   ├── image_generator.py
│   │   └── svg_generator.py
│   └── validators/
│       └── input_validator.py  # Pydantic models
├── Dockerfile
├── requirements.txt
├── test_signatures.py          # Local testing
└── README.md
```

## Best Practices

1. **Logo Images**: Use high-resolution logos (PNG or SVG) with transparent backgrounds
2. **Color Codes**: Always use hex color codes (e.g., `#0066cc`)
3. **Fonts**: Stick to web-safe fonts for maximum compatibility
4. **Image Width**: Use 600px for optimal email client rendering
5. **Social Links**: Include only active, professional social media profiles
6. **Disclaimer**: Keep legal text concise (under 200 characters recommended)

## Troubleshooting

### Issue: Images not displaying in email

**Solution**: Ensure logo URLs are publicly accessible and use HTTPS

### Issue: Signature too wide in mobile

**Solution**: Reduce `imageWidth` to 500-550px

### Issue: Colors not matching brand

**Solution**: Verify hex color codes are valid (6 characters after #)

### Issue: Fonts not rendering correctly

**Solution**: Use web-safe fonts like Arial, Helvetica, Georgia, or Times New Roman

## Support

For issues, questions, or feature requests:

- Check the [Apify Documentation](https://docs.apify.com)
- Review test input examples in `.actor/test_inputs/`
- Contact your Apify account manager

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/signature-generator)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
