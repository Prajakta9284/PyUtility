from dataclasses import dataclass

from pyutility import (
    GreetingPlugin,
    cache_result,
    chunk_items,
    filter_items,
    map_items,
    to_json,
)


# 1. Decorator: cache function results
@cache_result
def square(number: int) -> int:
    print(f"Calculating square of {number}")
    return number * number


print("1. Caching decorator")
print(square(5))
print(square(5))  # Uses the cached result


# 2. Data pipeline: filter and transform
print("\n2. Data pipeline")
numbers = [10, 20, 30, 40, 50]

filtered = filter_items(numbers, lambda n: n >= 30)
doubled = list(map_items(filtered, lambda n: n * 2))

print("Doubled values:", doubled)


# 3. Chunking
print("\n3. Chunking")
for chunk in chunk_items(numbers, 2):
    print(chunk)


# 4. Plugin registry
print("\n4. Plugin")
plugin = GreetingPlugin()
print(plugin.run())


# 5. JSON serialization
print("\n5. JSON serialization")


@dataclass
class Student:
    name: str
    marks: int


student = Student(name="Prajakta", marks=85)
json_data = to_json(student)
print(json_data)
