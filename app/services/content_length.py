def content_length(headers: dict[str, str]) -> int | None:
    """Parse Content-Length safely from response headers."""
    for key, value in headers.items():
        if key.lower() == "content-length":
            try:
                length = int(value.strip())
            except (TypeError, ValueError):
                return None
            return length if length >= 0 else None
    return None
