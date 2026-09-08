from collections.abc import Mapping


def normalize_params(params: Mapping[str, object] | None) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in (params or {}).items():
        name = str(key).strip()
        if not name:
            continue
        result[name] = str(value)
    return result
