from collections.abc import Mapping


def request_options(timeout: float = 10.0, verify: bool = True) -> dict[str, object]:
    """Normalize common transport options for the requester layer."""
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    return {"timeout": float(timeout), "verify": bool(verify)}
