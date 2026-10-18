# PyUtility

A reusable Python utility library demonstrating decorators, generator-based data processing, context managers, plugin registration, JSON serialization, and automated testing.

# Features

- Caching, retry, and argument validation decorators
- Lazy filtering, mapping, and chunking
- File and SQLite context managers
- Metaclass-based plugin registration
- JSON serialization and deserialization
- Unit, integration, and property-based tests

# Installation

Clone the repository, create and activate a virtual environment, then run:

python -m pip install -e .

For development tools:

python -m pip install pytest mypy black isort hypothesis coverage

# Usage

from pyutility import filter_items, chunk_items

numbers = [10, 20, 30, 40, 50]

print(list(filter_items(numbers, lambda x: x >= 30)))
print(list(chunk_items(numbers, 2)))

# Testing

python -m pytest -v
python -m coverage run -m pytest
python -m coverage report -m

# Project status

Educational project for learning Python package development, testing, type hints, and code quality practices.
