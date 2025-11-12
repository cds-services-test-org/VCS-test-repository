#!/usr/bin/env python3
"""
Issue Parser - VCS1 New
Parses issue descriptions and extracts reference links
"""

import re
from typing import List, Dict


def parse_markdown_links(text: str) -> List[str]:
    """Extract URLs from markdown format links."""
    # Match markdown links: [text](url)
    markdown_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    matches = re.findall(markdown_pattern, text)
    return [url for _, url in matches]


def parse_html_links(text: str) -> List[Dict[str, str]]:
    """Extract URLs from HTML anchor tags."""
    # Match HTML links: <a href="url">text</a>
    html_pattern = r'<a\s+href=["\'](.*?)["\']>(.*?)</a>'
    matches = re.findall(html_pattern, text)
    return [{'url': url, 'text': text} for url, text in matches]


def parse_plain_urls(text: str) -> List[str]:
    """Extract plain URLs from text."""
    # Match plain URLs (http/https), excluding trailing punctuation
    url_pattern = r'https?://[^\s<>"\']+[^\s<>"\'\.,;:!?\)]'
    matches = re.findall(url_pattern, text)
    return matches


def parse_issue(title: str, description: str) -> Dict:
    """
    Parse an issue and extract all reference links.
    
    Args:
        title: Issue title
        description: Issue description text
        
    Returns:
        Dictionary containing parsed information
    """
    result = {
        'title': title,
        'description': description,
        'links': {
            'markdown': parse_markdown_links(description),
            'html': parse_html_links(description),
            'plain': parse_plain_urls(description)
        }
    }
    
    # Get all unique URLs
    all_urls = set()
    all_urls.update(result['links']['plain'])
    all_urls.update(result['links']['markdown'])
    all_urls.update(link['url'] for link in result['links']['html'])
    result['all_urls'] = sorted(list(all_urls))
    
    return result


def main():
    """Main function to parse the first issue."""
    # Issue data from the problem statement
    issue_title = "First Issue created.."
    issue_description = """This is a sample discription of an issue.. it has reference link like : https://github.com/puppetlabs/cds-inventory-collector/actions/workflows/ci.yml

Or like <a href="https://github.com/puppetlabs/cds-commons/pulls">this</a>"""

    # Parse the issue
    parsed = parse_issue(issue_title, issue_description)
    
    # Display results
    print("=" * 60)
    print("ISSUE PARSER - VCS1 NEW")
    print("=" * 60)
    print(f"\nTitle: {parsed['title']}")
    print(f"\nDescription:\n{parsed['description']}")
    print("\n" + "=" * 60)
    print("PARSED LINKS:")
    print("=" * 60)
    
    if parsed['links']['plain']:
        print("\nPlain URLs:")
        for url in parsed['links']['plain']:
            print(f"  - {url}")
    
    if parsed['links']['html']:
        print("\nHTML Links:")
        for link in parsed['links']['html']:
            print(f"  - {link['url']} (text: '{link['text']}')")
    
    if parsed['links']['markdown']:
        print("\nMarkdown Links:")
        for url in parsed['links']['markdown']:
            print(f"  - {url}")
    
    print("\n" + "=" * 60)
    print("ALL UNIQUE URLs:")
    print("=" * 60)
    for url in parsed['all_urls']:
        print(f"  - {url}")
    print()
    
    return parsed


if __name__ == "__main__":
    main()
