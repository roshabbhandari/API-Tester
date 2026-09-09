def request_tag(method: str, url: str) -> str:
    """Create a short human-readable request label."""
    return f"{method.strip().upper()} {url.strip()}".strip()
