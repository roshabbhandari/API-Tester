import json


def looks_like_json(text: str) -> bool:
    """Return True when text parses as a JSON object or array."""
    try:
        value = json.loads(text)
    except (TypeError, ValueError):
        return False
    return isinstance(value, (dict, list))
