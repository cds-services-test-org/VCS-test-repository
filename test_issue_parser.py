#!/usr/bin/env python3
"""
Unit tests for issue parser
"""

import unittest
from issue_parser import parse_markdown_links, parse_html_links, parse_plain_urls, parse_issue


class TestIssueParser(unittest.TestCase):
    """Test cases for issue parser functions."""

    def test_parse_plain_urls(self):
        """Test parsing of plain URLs."""
        text = "Check this link: https://github.com/example/repo and this https://example.com"
        urls = parse_plain_urls(text)
        self.assertEqual(len(urls), 2)
        self.assertIn("https://github.com/example/repo", urls)
        self.assertIn("https://example.com", urls)

    def test_parse_html_links(self):
        """Test parsing of HTML anchor tags."""
        text = 'Visit <a href="https://github.com">GitHub</a> or <a href="https://example.com">example</a>'
        links = parse_html_links(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0]['url'], "https://github.com")
        self.assertEqual(links[0]['text'], "GitHub")

    def test_parse_markdown_links(self):
        """Test parsing of markdown format links."""
        text = "Check [GitHub](https://github.com) and [Example](https://example.com)"
        urls = parse_markdown_links(text)
        self.assertEqual(len(urls), 2)
        self.assertIn("https://github.com", urls)
        self.assertIn("https://example.com", urls)

    def test_parse_issue_with_mixed_formats(self):
        """Test parsing issue with multiple link formats."""
        title = "First Issue created.."
        description = """This is a sample discription of an issue.. it has reference link like : https://github.com/puppetlabs/cds-inventory-collector/actions/workflows/ci.yml

Or like <a href="https://github.com/puppetlabs/cds-commons/pulls">this</a>"""
        
        result = parse_issue(title, description)
        
        self.assertEqual(result['title'], title)
        self.assertEqual(result['description'], description)
        self.assertEqual(len(result['all_urls']), 2)
        self.assertIn("https://github.com/puppetlabs/cds-inventory-collector/actions/workflows/ci.yml", result['all_urls'])
        self.assertIn("https://github.com/puppetlabs/cds-commons/pulls", result['all_urls'])

    def test_parse_issue_no_links(self):
        """Test parsing issue with no links."""
        title = "Test Issue"
        description = "This is a simple issue with no links"
        
        result = parse_issue(title, description)
        
        self.assertEqual(result['title'], title)
        self.assertEqual(len(result['all_urls']), 0)

    def test_parse_issue_duplicate_urls(self):
        """Test that duplicate URLs are deduplicated."""
        title = "Test"
        description = "Link: https://example.com and again <a href='https://example.com'>here</a>"
        
        result = parse_issue(title, description)
        
        # Should only have one unique URL
        self.assertEqual(len(result['all_urls']), 1)
        self.assertIn("https://example.com", result['all_urls'])


if __name__ == '__main__':
    unittest.main()
