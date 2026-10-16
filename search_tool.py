
from ddgs import DDGS


def search_web(query, max_results=5):
    """Search the web and return relevant results."""

    try:
        results = DDGS().text(
            query,
            max_results=max_results
        )

        search_results = []

        for result in results:
            search_results.append({
                "title": result.get("title", ""),
                "url": result.get("href", ""),
                "snippet": result.get("body", "")
            })

        return search_results

    except Exception as error:
        print("Search error:", error)
        return []
      