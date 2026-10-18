from functools import wraps
from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def cache_result(func: F) -> F:
    """Cache function results for repeated hashable arguments."""
    cache: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return cast(F, wrapper)


def retry(
    attempts: int = 3,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[F], F]:
    """Retry a function when selected exceptions occur."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts - 1:
                        raise

            raise RuntimeError("Unreachable")

        return cast(F, wrapper)

    return decorator


def validate_arguments(
    **validators: Callable[[Any], bool],
) -> Callable[[F], F]:
    """Validate selected arguments using supplied predicate functions."""

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            from inspect import signature

            bound = signature(func).bind(*args, **kwargs)
            bound.apply_defaults()

            for name, validator in validators.items():
                if name not in bound.arguments:
                    raise ValueError(f"Unknown argument: {name}")

                if not validator(bound.arguments[name]):
                    raise ValueError(f"Invalid value for {name}")

            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator
