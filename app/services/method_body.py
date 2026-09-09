BODY_METHODS = frozenset({"POST", "PUT", "PATCH"})


def allows_body(method: str) -> bool:
    return method.strip().upper() in BODY_METHODS
