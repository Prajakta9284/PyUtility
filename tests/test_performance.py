from time import perf_counter

from pyutility.pipeline import filter_items


def test_pipeline_performance() -> None:
    values = range(100_000)

    start = perf_counter()
    result = sum(filter_items(values, lambda value: value % 2 == 0))
    elapsed = perf_counter() - start

    assert result == 2_499_950_000
    print(f"Processed 100,000 items in {elapsed:.4f} seconds")
