def response_line_count(text: str) -> int:
    """Count logical lines in a response body."""
    return 0 if not text else len(text.splitlines())
