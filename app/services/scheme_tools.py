from urllib.parse import urlsplit


def url_scheme(url: str) -> str:
    return urlsplit(url).scheme.lower()


def is_secure_url(url: str) -> bool:
    return url_scheme(url) == "https"
