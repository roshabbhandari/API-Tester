from urllib.parse import parse_qsl, urlsplit


def url_query(url: str) -> dict[str, str]:
    """Parse the first value for each query key."""
    return dict(parse_qsl(urlsplit(url.strip()).query, keep_blank_values=True))
