
import unittest
from unittest.mock import patch, Mock

from search_tool import search_web, fetch_webpage_text


class TestSearchWeb(unittest.TestCase):

    def test_empty_query_returns_empty_list(self):
        self.assertEqual(search_web(""), [])

    def test_whitespace_query_returns_empty_list(self):
        self.assertEqual(search_web("   "), [])

    def test_invalid_limit_returns_empty_list(self):
        self.assertEqual(search_web("AI agents", max_results=0), [])

    @patch("search_tool.DDGS")
    def test_duplicate_urls_are_removed(self, mock_ddgs):
        mock_ddgs.return_value.text.return_value = [
            {
                "title": "First result",
                "href": "https://example.com",
                "body": "First snippet",
            },
            {
                "title": "Duplicate result",
                "href": "https://example.com",
                "body": "Duplicate snippet",
            },
        ]

        results = search_web("AI agents")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "First result")


class TestFetchWebpageText(unittest.TestCase):

    @patch("search_tool.requests.get")
    def test_empty_url_does_not_make_request(self, mock_get):
        self.assertEqual(fetch_webpage_text(""), "")
        mock_get.assert_not_called()

    @patch("search_tool.requests.get")
    def test_invalid_scheme_does_not_make_request(self, mock_get):
        self.assertEqual(fetch_webpage_text("ftp://example.com"), "")
        mock_get.assert_not_called()

    @patch("search_tool.requests.get")
    def test_non_html_response_returns_empty_string(self, mock_get):
        response = Mock()
        response.headers = {"Content-Type": "application/json"}
        response.raise_for_status.return_value = None
        mock_get.return_value = response

        self.assertEqual(
            fetch_webpage_text("https://example.com/data"),
            "",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
