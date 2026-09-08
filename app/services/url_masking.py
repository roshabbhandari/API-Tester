from urllib.parse import urlsplit, urlunsplit


def mask_url_credentials(url: str) -> str:
    parts = urlsplit(url)
    if not parts.username and not parts.password:
        return url
    host = parts.hostname or ""
    if parts.port:
        host += f":{parts.port}"
    return urlunsplit((parts.scheme, f"***:***@{host}", parts.path, parts.query, parts.fragment))
