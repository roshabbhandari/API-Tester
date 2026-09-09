SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})


def is_safe_method(method: str) -> bool:
    return method.strip().upper() in SAFE_METHODS
