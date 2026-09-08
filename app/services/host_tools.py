from urllib.parse import urlsplit


def request_host(url: str) -> str:
    host = urlsplit(url).hostname
    if not host:
        raise ValueError("URL has no hostname")
    return host.lower()
