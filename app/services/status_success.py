def is_success(status: int) -> bool:
    return 200 <= int(status) < 300
