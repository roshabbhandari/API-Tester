SENSITIVE_HEADERS = frozenset({"authorization", "proxy-authorization", "cookie", "set-cookie", "x-api-key"})


def redact_headers(headers: dict[str, str]) -> dict[str, str]:
    return {key: ("[REDACTED]" if key.casefold() in SENSITIVE_HEADERS else value) for key, value in headers.items()}
