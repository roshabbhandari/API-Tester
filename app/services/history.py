from collections import deque


class RequestHistory:
    def __init__(self, limit: int = 100):
        if limit < 1:
            raise ValueError("limit must be positive")
        self._items = deque(maxlen=limit)

    def add(self, item: dict) -> None:
        self._items.append(dict(item))

    def latest(self) -> list[dict]:
        return list(reversed(self._items))
