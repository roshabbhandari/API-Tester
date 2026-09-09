from urllib.parse import urlsplit


def url_fragment(url: str) -> str:
    """Return a URL fragment without the leading #."""
    return urlsplit(url.strip()).fragment
