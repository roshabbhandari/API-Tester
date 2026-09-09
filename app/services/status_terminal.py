def is_terminal_status(status: int) -> bool:
    """Whether a status should normally end a request flow."""
    return int(status) >= 400 or 200 <= int(status) < 300
