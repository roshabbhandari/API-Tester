from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    value = url.strip()
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("URL must include a valid HTTP or HTTPS host")
    return value
