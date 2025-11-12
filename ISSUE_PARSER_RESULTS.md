# Issue Parser Results - VCS1 New

## Overview
This document contains the parsed results from the first issue created in the VCS test repository.

## Issue Details

**Title:** First Issue created..

**Description:**
```
This is a sample discription of an issue.. it has reference link like : 
https://github.com/puppetlabs/cds-inventory-collector/actions/workflows/ci.yml

Or like <a href="https://github.com/puppetlabs/cds-commons/pulls">this</a>
```

## Parsed Reference Links

The issue description contains the following reference links:

### 1. CI Workflow Reference
- **URL:** https://github.com/puppetlabs/cds-inventory-collector/actions/workflows/ci.yml
- **Format:** Plain text URL
- **Type:** GitHub Actions workflow file

### 2. Pull Requests Reference
- **URL:** https://github.com/puppetlabs/cds-commons/pulls
- **Format:** HTML anchor tag (`<a href="...">this</a>`)
- **Type:** GitHub pull requests page

## Parser Implementation

The `issue_parser.py` script implements the following functionality:

1. **Plain URL Extraction:** Identifies URLs written directly in text (e.g., `https://example.com`)
2. **HTML Link Extraction:** Parses HTML anchor tags (e.g., `<a href="url">text</a>`)
3. **Markdown Link Extraction:** Parses markdown format links (e.g., `[text](url)`)
4. **Deduplication:** Ensures each unique URL is only reported once

## Testing

Unit tests are provided in `test_issue_parser.py` to validate:
- Plain URL parsing
- HTML link parsing
- Markdown link parsing
- Issue parsing with mixed formats
- Handling of issues with no links
- Proper deduplication of URLs

All tests pass successfully.

## Usage

To run the parser:
```bash
python3 issue_parser.py
```

To run the tests:
```bash
python3 -m unittest test_issue_parser.py -v
```
