from urllib.parse import urlsplit


def url_path(url: str) -> str:
    """Extract a URL path while keeping the root slash meaningful."""
    path = urlsplit(url.strip()).path
    return path or "/"
