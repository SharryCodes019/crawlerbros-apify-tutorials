# Email Verifier Tutorial: Run This Apify Actor with Python

Verify email addresses for deliverability. Check syntax, MX records, disposable domains, role-based addresses, and SMTP mailbox existence.

This repository shows how to run [Email Verifier](https://apify.com/crawlerbros/email-verifier) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/email-verifier`
- **Apify Store:** [https://apify.com/crawlerbros/email-verifier](https://apify.com/crawlerbros/email-verifier)
- **SEO title:** Email Verifier Tutorial: Run This Apify Actor with Python
- **Description:** Verify email addresses for deliverability. Check syntax, MX records, disposable domains, role-based addresses, and SMTP mailbox existence.

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

# Email Verifier

Verify email addresses for deliverability — check syntax, MX records, disposable domains, role-based addresses, free providers, and SMTP mailbox existence.

## What is Email Verifier?

A fast, free email verification tool that checks whether email addresses are valid and deliverable. No external paid APIs are used — all verification is performed locally using DNS lookups, SMTP handshakes, and built-in databases of 55,000+ disposable domains.

Perfect for cleaning email lists, validating sign-up forms, and reducing bounce rates before sending campaigns.

## What data can you extract?

**Verification results per email:**
- Verdict: valid, invalid, risky, disposable, or unknown
- Confidence score (0-100)
- Detailed checks: syntax, MX record, SMTP, disposable, role-based, free provider, catch-all
- Primary MX server hostname
- Human-readable reason for non-valid results

## Input

### Email Addresses

Provide a list of email addresses to verify.

```json
{
    "emails": ["user@example.com", "test@gmail.com", "info@company.org"]
}
```

### Verification Depth

Choose how thoroughly each email is checked:

| Depth | Checks Performed | Speed | Use Case |
|-------|-----------------|-------|----------|
| **Basic** | Syntax + MX records | Fastest | Quick format validation |
| **Standard** (default) | + Disposable, role-based, free provider detection | Fast | Email list cleaning |
| **Deep** | + SMTP mailbox verification, catch-all detection | Slower | Maximum accuracy |

### Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| emails | string[] | — | Email addresses to verify (required) |
| verificationDepth | string | `"standard"` | Verification depth: basic, standard, or deep |
| concurrency | integer | `10` | Parallel verifications (1-50) |

## Output

Each item in the dataset represents one verified email:

```json
{
    "email": "test@gmail.com",
    "verdict": "valid",
    "confidence": 85,
    "checks": {
        "syntax": true,
        "mxRecord": true,
        "smtp": null,
        "disposable": false,
        "roleBased": false,
        "freeProvider": true,
        "catchAll": null
    },
    "mxHost": "gmail-smtp-in.l.google.com",
    "reason": null,
    "verifiedAt": "2025-03-16T12:00:00.000000+00:00"
}
```

### Output Fields

| Field | Type | Description |
|-------|------|-------------|
| email | string | Normalized email address |
| verdict | string | Verification result: valid, invalid, risky, disposable, or unknown |
| confidence | integer | Confidence score from 0 to 100 |
| checks | object | Detailed check results (see below) |
| mxHost | string/null | Primary MX server hostname |
| reason | string/null | Human-readable explanation for non-valid verdicts |
| verifiedAt | string | ISO 8601 timestamp of verification |

### Check Details

| Check | Type | Description |
|-------|------|-------------|
| syntax | boolean | Email follows RFC 5322 format |
| mxRecord | boolean | Domain has valid MX records |
| smtp | boolean/null | SMTP server accepts the address (deep mode only) |
| disposable | boolean/null | Domain is a known disposable email provider (standard/deep) |
| roleBased | boolean/null | Address is role-based like admin@, info@, support@ (standard/deep) |
| freeProvider | boolean/null | Domain is a free email provider like Gmail, Yahoo (standard/deep) |
| catchAll | boolean/null | Domain accepts all addresses (deep mode only) |

### Verdict Meanings

| Verdict | Meaning |
|---------|---------|
| **valid** | Email passed all checks and appears deliverable |
| **invalid** | Email failed syntax, MX, or SMTP verification |
| **risky** | Email exists but domain is catch-all (accepts any address) |
| **disposable** | Email uses a known disposable/temporary domain |
| **unknown** | Could not determine deliverability (SMTP blocked or timeout) |

## How to use

### Quick validation

1. Enter email addresses in the **Email Addresses** field
2. Leave depth as **Standard**
3. Click **Save & Start**

### Maximum accuracy

1. Enter email addresses
2. Set **Verification Depth** to **Deep**
3. Click **Save & Start**

Deep mode performs SMTP mailbox verification and catch-all detection for the most accurate results.

### Large batches

For 100+ emails, increase the **Concurrency** setting (up to 50) for faster processing. Domain-level caching ensures MX lookups and catch-all checks are only performed once per domain.

## Frequently Asked Questions

### How accurate is the verification?

Standard depth provides reliable syntax, MX, disposable, and role-based detection. Deep mode adds SMTP verification for the highest accuracy, but some mail servers may block or rate-limit verification attempts from cloud IPs.

### Why is Gmail showing as "risky" in deep mode?

Gmail and some other major providers accept all addresses at the SMTP level (catch-all behavior). This means SMTP verification cannot distinguish between real and fake Gmail addresses, so they are marked as "risky" rather than "valid".

### What does "unknown" verdict mean?

Unknown means the verifier could not definitively determine if the email is valid or invalid. This typically happens when SMTP servers block the connection, timeout, or return temporary errors.

### Does this use any external paid APIs?

No. All verification is performed locally using DNS lookups, SMTP handshakes, and a built-in database of 55,000+ disposable email domains. No proxy or authentication is required.

### Can I verify emails in bulk?

Yes. You can verify hundreds of emails in a single run. Use the concurrency setting to control parallel processing speed. Results are pushed in batches for efficient data handling.

### What are role-based emails?

Role-based emails are addresses like admin@, info@, support@ that are typically shared by teams rather than belonging to individuals. These are flagged because they often have higher bounce rates and lower engagement.

### Is the data accurate for all email providers?

Syntax and MX checks work universally. Disposable detection covers 55,000+ known domains. SMTP verification accuracy varies by provider — some servers always accept (catch-all) or block verification attempts. The confidence score reflects this uncertainty.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/email-verifier)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
