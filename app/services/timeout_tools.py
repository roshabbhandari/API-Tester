DEFAULT_TIMEOUT = 30.0
MAX_TIMEOUT = 300.0


def normalize_timeout(value: float | int | None) -> float:
    if value is None:
        return DEFAULT_TIMEOUT
    timeout = float(value)
    if timeout <= 0:
        raise ValueError("timeout must be greater than zero")
    return min(timeout, MAX_TIMEOUT)
