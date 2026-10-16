
from ddgs import DDGS


def search_web(query, max_results=5):
    """Search the web and return cleaned, unique search results."""

    if not query or not query.strip():
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
