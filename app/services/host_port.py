from urllib.parse import urlsplit


def host_port(url: str) -> tuple[str, int | None]:
    """Return hostname and explicit port from a URL."""
    parsed = urlsplit(url.strip())
    return parsed.hostname or "", parsed.port
