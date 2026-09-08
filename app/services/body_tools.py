import json


def is_json_compatible(body: object) -> bool:
    try:
        json.dumps(body)
    except (TypeError, ValueError):
        return False
    return True


def body_preview(body: object, limit: int = 500) -> str:
    text = json.dumps(body, ensure_ascii=False, default=str) if isinstance(body, (dict, list)) else str(body)
    return text[:limit] + ("…" if len(text) > limit else "")
