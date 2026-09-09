from urllib.parse import urljoin


def join_url(base: str, path: str) -> str:
    """Resolve a relative API path against a base URL."""
    return urljoin(base.strip(), path.strip())
