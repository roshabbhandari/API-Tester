SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})
BODY_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})


def accepts_body(method: str) -> bool:
    return method.upper() in BODY_METHODS


def is_safe_method(method: str) -> bool:
    return method.upper() in SAFE_METHODS
