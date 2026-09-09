def response_preview(text: str, limit: int = 500) -> str:
    """Return a bounded response preview without splitting Unicode characters."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    return text if len(text) <= limit else text[:limit] + "…"
