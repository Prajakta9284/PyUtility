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

# Example Applications

PyUtility includes example applications demonstrating its main features.

# 1. Decorators

File: `examples/decorator_example.py`

Demonstrates:
- Caching function results using `cache_result`
- Retrying failed operations using `retry`
- Validating function arguments using `validate_arguments`

Run:

python examples/decorator_example.py

# 2. Generator Pipelines

File: `examples/pipeline_example.py`

Demonstrates:
- Transforming data using `map_items`
- Filtering data using `filter_items`
- Dividing data into chunks using `chunk_items`

Run:

python examples/pipeline_example.py

# 3. Database Context Manager

File: `examples/context_manager_example.py`

Demonstrates:
- Creating a temporary SQLite database
- Creating a table and inserting records
- Retrieving records using SQL
- Managing database resources with a context manager

Run:

python examples/context_manager_example.py

# 4. Plugin Registration

File: `examples/plugin_example.py`

Demonstrates:
- Automatic plugin registration using `PluginMeta`
- Creating custom plugin classes
- Executing registered plugins

Run:

python examples/plugin_example.py

# Running the Examples

Run these commands from the project's root directory after installing the project dependencies and activating the virtual environment.
