RETRYABLE = frozenset({408, 425, 429, 500, 502, 503, 504})


def is_retryable_status(status: int) -> bool:
    return int(status) in RETRYABLE
