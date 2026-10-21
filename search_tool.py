
from ddgs import DDGS


def search_web(query, max_results=5):
    """Search the web and return cleaned, unique search results."""
    if not query or not query.strip():
        return []
    if not isinstance(max_results, int) or max_results < 1:
        return []

    try:
        results = DDGS().text(
            query.strip(),
            max_results=max_results,
            safesearch="moderate"
        )

        search_results = []
        seen_urls = set()

        for result in results:
            title = (result.get("title") or "").strip()
            url = (result.get("href") or "").strip()
            snippet = (result.get("body") or "").strip()

            if not title or not url or url in seen_urls:
                continue

            seen_urls.add(url)

            search_results.append({
                "title": title,
                "url": url,
                "snippet": snippet
            })

        return search_results

    except Exception as error:
        print("Search error:", error)
        return []

import requests
from html.parser import HTMLParser


class WebpageTextParser(HTMLParser):
    """Extract readable text from webpage HTML."""

    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_content = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip_content = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip_content = False

    def handle_data(self, data):
        if not self.skip_content:
            text = data.strip()
            if text:
                self.text_parts.append(text)


def fetch_webpage_text(url, max_chars=2000):
    """Fetch limited readable text from a webpage."""
    if not isinstance(url, str) or not url.strip():
        return ""

    if not url.strip().lower().startswith(("http://", "https://")):
        return ""
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "ResearchAgent/1.0"},
            allow_redirects=True
        )
        response.raise_for_status()

        if "text/html" not in response.headers.get("Content-Type", "").lower():
            return ""

        parser = WebpageTextParser()
        parser.feed(response.text)

        return " ".join(parser.text_parts)[:max_chars]

    except requests.RequestException:
        return ""
    except Exception:
        return ""
