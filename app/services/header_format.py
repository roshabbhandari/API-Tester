def format_headers(headers: dict[str, str]) -> str:
    """Format headers deterministically for display or logging."""
    return "\n".join(f"{key}: {headers[key]}" for key in sorted(headers, key=str.lower))
