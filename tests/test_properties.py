from hypothesis import given
from hypothesis import strategies as st

from pyutility.pipeline import chunk_items, filter_items


@given(st.lists(st.integers()))
def test_chunking_preserves_items(items):
    chunks = list(chunk_items(items, 3))
    flattened = [item for chunk in chunks for item in chunk]

    assert flattened == items


@given(st.lists(st.integers()))
def test_filter_nonnegative(items):
    result = list(filter_items(items, lambda value: value >= 0))

    assert all(value >= 0 for value in result)
    assert result == [value for value in items if value >= 0]
