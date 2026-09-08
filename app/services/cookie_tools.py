def response_cookies(headers: dict[str, str]) -> list[str]:
    return [value for key, value in headers.items() if key.casefold() == "set-cookie"]
