def accepts_json(headers: dict[str, str]) -> bool:
    value = next((v for k, v in headers.items() if k.casefold() == "accept"), "")
    return "application/json" in value.lower() or "*/*" in value
