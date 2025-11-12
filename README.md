# VCS-test-repository
To test the triggered event

## Issue Parser - VCS1 New

This repository includes an issue parser that extracts and analyzes reference links from issue descriptions.

### Features
- Parses plain text URLs
- Extracts links from HTML anchor tags
- Supports markdown format links
- Deduplicates URLs across different formats

### Files
- `issue_parser.py` - Main parser implementation
- `test_issue_parser.py` - Unit tests for the parser
- `ISSUE_PARSER_RESULTS.md` - Parsed results from the first issue

### Usage
```bash
# Run the parser on the first issue
python3 issue_parser.py

# Run tests
python3 -m unittest test_issue_parser.py -v
```
