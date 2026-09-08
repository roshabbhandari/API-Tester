import hashlib
import json


def request_cache_key(method: str, url: str, params: dict | None = None, body: object = None) -> str:
    payload = json.dumps({"method": method.upper(), "url": url, "params": params or {}, "body": body}, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
