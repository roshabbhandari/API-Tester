from collections.abc import Mapping


def merge_headers(*sources: Mapping[str, str] | None) -> dict[str, str]:
    """Merge headers in order, replacing duplicate keys case-insensitively."""
    result: dict[str, str] = {}
    for source in sources:
        if not source:
            continue
        for key, value in source.items():
            old = next((k for k in result if k.lower() == key.lower()), None)
            if old is not None:
                del result[old]
            result[str(key)] = str(value)
    return result
