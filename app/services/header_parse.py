def parse_header_lines(text: str) -> dict[str, str]:
    """Parse simple one-header-per-line input, ignoring malformed lines."""
    headers: dict[str, str] = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key:
            headers[key] = value.strip()
    return headers
