"""Web search integration — pluggable search providers for the research pipeline.

Supports:
1. Brave Search API (recommended — generous free tier)
2. Tavily Search API
3. SerpAPI
4. Fallback stub for offline/testing
"""

from __future__ import annotations

import json
import logging
import os
from typing import Optional

logger = logging.getLogger(__name__)


def brave_search(query: str, api_key: Optional[str] = None, count: int = 5) -> str:
    """Search using Brave Search API."""
    import requests

    key = api_key or os.environ.get("BRAVE_API_KEY", "")
    if not key:
        raise ValueError("BRAVE_API_KEY not set")

    resp = requests.get(
        "https://api.search.brave.com/res/v1/web/search",
        headers={"X-Subscription-Token": key, "Accept": "application/json"},
        params={"q": query, "count": count},
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()

    results = data.get("web", {}).get("results", [])
    if not results:
        return f"[No results found for: {query}]"

    lines = []
    for r in results[:count]:
        title = r.get("title", "")
        desc = r.get("description", "")
        url = r.get("url", "")
        lines.append(f"- {title}\n  {url}\n  {desc}")
    return "\n".join(lines)


def tavily_search(query: str, api_key: Optional[str] = None, max_results: int = 5) -> str:
    """Search using Tavily Search API."""
    import requests

    key = api_key or os.environ.get("TAVILY_API_KEY", "")
    if not key:
        raise ValueError("TAVILY_API_KEY not set")

    resp = requests.post(
        "https://api.tavily.com/search",
        json={"api_key": key, "query": query, "max_results": max_results},
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()

    results = data.get("results", [])
    if not results:
        return f"[No results found for: {query}]"

    lines = []
    for r in results[:max_results]:
        title = r.get("title", "")
        content = r.get("content", "")
        url = r.get("url", "")
        lines.append(f"- {title}\n  {url}\n  {content}")
    return "\n".join(lines)


def serp_search(query: str, api_key: Optional[str] = None, num: int = 5) -> str:
    """Search using SerpAPI."""
    import requests

    key = api_key or os.environ.get("SERPAPI_KEY", "")
    if not key:
        raise ValueError("SERPAPI_KEY not set")

    resp = requests.get(
        "https://serpapi.com/search",
        params={"q": query, "api_key": key, "num": num, "engine": "google"},
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()

    results = data.get("organic_results", [])
    if not results:
        return f"[No results found for: {query}]"

    lines = []
    for r in results[:num]:
        title = r.get("title", "")
        snippet = r.get("snippet", "")
        link = r.get("link", "")
        lines.append(f"- {title}\n  {link}\n  {snippet}")
    return "\n".join(lines)


def get_search_fn():
    """Auto-detect and return the best available search function.

    Priority: Brave > Tavily > SerpAPI > stub
    """
    if os.environ.get("BRAVE_API_KEY"):
        logger.info("Using Brave Search API")
        return brave_search
    if os.environ.get("TAVILY_API_KEY"):
        logger.info("Using Tavily Search API")
        return tavily_search
    if os.environ.get("SERPAPI_KEY"):
        logger.info("Using SerpAPI")
        return serp_search
    logger.warning(
        "No search API key found. Set BRAVE_API_KEY, TAVILY_API_KEY, or SERPAPI_KEY. "
        "Using offline stub."
    )
    return _stub_search


def _stub_search(query: str) -> str:
    """Offline stub — returns a message that no search is available."""
    return f"[No search API configured. Query: {query}]"
