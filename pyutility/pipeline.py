from collections.abc import Callable, Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")
U = TypeVar("U")


def filter_items(items: Iterable[T], predicate: Callable[[T], bool]) -> Iterator[T]:
    """Yield items that satisfy a condition."""
    for item in items:
        if predicate(item):
            yield item


def map_items(items: Iterable[T], transform: Callable[[T], U]) -> Iterator[U]:
    """Transform items lazily."""
    for item in items:
        yield transform(item)


def chunk_items(items: Iterable[T], size: int) -> Iterator[list[T]]:
    """Yield lists containing up to size items."""
    if size < 1:
        raise ValueError("size must be at least 1")

    chunk: list[T] = []

    for item in items:
        chunk.append(item)

        if len(chunk) == size:
            yield chunk
            chunk = []

    if chunk:
        yield chunk
