def clamp_page(value: int, maximum: int = 100) -> int:
    if maximum < 1:
        raise ValueError("maximum must be positive")
    return max(1, min(value, maximum))
