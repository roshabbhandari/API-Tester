from collections.abc import Mapping


def normalize_headers(headers: Mapping[str, str] | None) -> dict[str, str]:
    return {str(key).strip(): str(value) for key, value in (headers or {}).items() if str(key).strip()}


def get_header(headers: Mapping[str, str], name: str) -> str | None:
    target = name.casefold()
    for key, value in headers.items():
        if key.casefold() == target:
            return value
    return None
