from .url_tools import normalize_url

ALLOWED_METHODS = frozenset({"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"})


def validate_method(method: str) -> str:
    normalized = method.strip().upper()
    if normalized not in ALLOWED_METHODS:
        raise ValueError(f"Unsupported HTTP method: {normalized}")
    return normalized


def validate_request_url(url: str) -> str:
    return normalize_url(url)
