import json
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any


@contextmanager
def open_text_file(path: str, mode: str = "r") -> Iterator[Any]:
    """Open a text file and close it automatically."""
    with open(path, mode, encoding="utf-8") as file:
        yield file


@contextmanager
def sqlite_connection(path: str) -> Iterator[sqlite3.Connection]:
    """Manage a SQLite connection and transaction."""
    connection = sqlite3.connect(path)

    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


@contextmanager
def load_config(path: str) -> Iterator[dict[str, Any]]:
    """Load a JSON configuration file."""
    config = json.loads(Path(path).read_text(encoding="utf-8"))
    yield config
