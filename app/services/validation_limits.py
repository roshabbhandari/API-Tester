MAX_URL_LENGTH = 2048
MAX_HEADERS = 100
MAX_PARAMS = 100


def validate_collection_size(items: dict, maximum: int, label: str) -> None:
    if len(items) > maximum:
        raise ValueError(f"{label} exceeds the maximum of {maximum} items")
