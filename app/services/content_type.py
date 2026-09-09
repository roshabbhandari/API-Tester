def content_type(headers: dict[str, str]) -> str:
    """Read Content-Type case-insensitively."""
    for key, value in headers.items():
        if key.lower() == "content-type":
            return value.split(";", 1)[0].strip().lower()
    return ""
