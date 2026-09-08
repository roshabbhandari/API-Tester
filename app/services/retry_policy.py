def retry_delay(attempt: int, base: float = 0.25, maximum: float = 4.0) -> float:
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    return min(maximum, base * (2 ** attempt))
