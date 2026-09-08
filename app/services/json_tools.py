import json


def format_json(value: object, indent: int = 2) -> str:
    return json.dumps(value, indent=indent, ensure_ascii=False, default=str)


def parse_json(text: str) -> object:
    return json.loads(text)
