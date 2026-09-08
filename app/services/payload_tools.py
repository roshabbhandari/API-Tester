import json


def payload_size_bytes(payload: object) -> int:
    return len(json.dumps(payload, default=str, ensure_ascii=False).encode("utf-8"))
