def response_charset(content_type: str, default: str = "utf-8") -> str:
    """Extract charset from a Content-Type value."""
    for part in content_type.split(";")[1:]:
        key, sep, value = part.strip().partition("=")
        if sep and key.lower() == "charset" and value.strip():
            return value.strip().strip('"').lower()
    return default
