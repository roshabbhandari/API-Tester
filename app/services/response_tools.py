from collections.abc import Mapping


def response_size_bytes(body: object) -> int:
    if isinstance(body, bytes):
        return len(body)
    return len(str(body).encode("utf-8"))


def content_type(headers: Mapping[str, str]) -> str | None:
    for key, value in headers.items():
        if key.casefold() == "content-type":
            return value.split(";", 1)[0].strip().lower()
    return None
