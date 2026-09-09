SUPPORTED_METHODS = frozenset({"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"})


def normalize_method(method: str) -> str:
    value = method.strip().upper()
    if value not in SUPPORTED_METHODS:
        raise ValueError(f"unsupported HTTP method: {method}")
    return value
