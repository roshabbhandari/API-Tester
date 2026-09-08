def is_redirect(status_code: int) -> bool:
    return 300 <= status_code < 400


def location_header(headers: dict[str, str]) -> str | None:
    for key, value in headers.items():
        if key.casefold() == "location":
            return value
    return None
