TEXT_TYPES = frozenset({"application/json", "application/xml", "text/plain", "text/html", "text/xml"})


def is_text_content(content_type: str | None) -> bool:
    if not content_type:
        return False
    normalized = content_type.split(";", 1)[0].strip().lower()
    return normalized.startswith("text/") or normalized in TEXT_TYPES
