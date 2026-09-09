from urllib.parse import parse_qsl


def query_pairs(query: str) -> list[tuple[str, str]]:
    """Preserve duplicate query keys while parsing a query string."""
    return parse_qsl(query.lstrip("?"), keep_blank_values=True)
