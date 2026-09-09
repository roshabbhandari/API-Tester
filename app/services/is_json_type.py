JSON_TYPES = frozenset({"application/json", "application/problem+json"})


def is_json_content_type(value: str) -> bool:
    return value.strip().lower() in JSON_TYPES
