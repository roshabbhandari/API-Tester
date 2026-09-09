from urllib.parse import urlsplit


def url_origin(url: str) -> str:
    """Build the scheme://host[:port] origin for a URL."""
    parsed = urlsplit(url.strip())
    if not parsed.scheme or not parsed.netloc:
        return ""
    return f"{parsed.scheme}://{parsed.netloc}"
