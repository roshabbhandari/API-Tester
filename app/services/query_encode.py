from urllib.parse import urlencode


def encode_query(pairs: list[tuple[str, str]]) -> str:
    """Encode query pairs without losing duplicate keys."""
    return urlencode(pairs, doseq=True)
