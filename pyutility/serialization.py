import json
from dataclasses import asdict, is_dataclass
from typing import Any, TypeVar

T = TypeVar("T")


def to_json(value: Any) -> str:
    """Serialize a dataclass or JSON-compatible value."""
    if is_dataclass(value) and not isinstance(value, type):
        value = asdict(value)

    return json.dumps(value)


def from_json(data: str, cls: type[T]) -> T:
    """Deserialize a JSON object into a dataclass or class."""
    values = json.loads(data)

    if not isinstance(values, dict):
        raise ValueError("Expected a JSON object")

    return cls(**values)
