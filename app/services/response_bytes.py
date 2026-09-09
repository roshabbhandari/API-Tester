def response_bytes(text: str, encoding: str = "utf-8") -> int:
    """Estimate response body size using the selected encoding."""
    return len(text.encode(encoding, errors="replace"))
