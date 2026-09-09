import json


def pretty_json(value: object) -> str:
    """Serialize JSON for readable API response presentation."""
    return json.dumps(value, indent=2, ensure_ascii=False)
