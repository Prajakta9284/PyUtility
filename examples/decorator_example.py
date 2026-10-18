from pyutility.decorators import (
    cache_result,
    retry,
    validate_arguments,
)


# 1. Demonstrate caching
@cache_result
def add(a: int, b: int) -> int:
    print("Calculating...")
    return a + b


print("=== Caching Example ===")
print("First call:", add(10, 20))
print("Second call:", add(10, 20))


# 2. Demonstrate retry
attempts = 0


@retry(attempts=3, exceptions=(ValueError,))
def unreliable_task() -> str:
    global attempts
    attempts += 1

    if attempts < 3:
        print(f"Attempt {attempts} failed.")
        raise ValueError("Temporary error")

    return "Task completed successfully!"


print("\n=== Retry Example ===")
print(unreliable_task())


# 3. Demonstrate argument validation
@validate_arguments(amount=lambda value: value > 0)
def calculate_total(amount: int) -> int:
    return amount * 2


print("\n=== Validation Example ===")
print("Total:", calculate_total(100))

try:
    calculate_total(-10)
except ValueError as error:
    print("Validation error:", error)
