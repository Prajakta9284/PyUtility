import unittest
from dataclasses import dataclass

from pyutility.decorators import (
    cache_result,
    retry,
    validate_arguments,
)
from pyutility.pipeline import chunk_items, filter_items, map_items
from pyutility.registry import GreetingPlugin, PluginMeta
from pyutility.serialization import from_json, to_json


class TestDecorators(unittest.TestCase):

    def test_cache_result(self):
        calls = []

        @cache_result
        def add(a: int, b: int) -> int:
            calls.append(1)
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(len(calls), 1)

    def test_retry(self):
        calls = []

        @retry(attempts=3, exceptions=(ValueError,))
        def unreliable() -> str:
            calls.append(1)
            if len(calls) < 3:
                raise ValueError("Temporary error")
            return "success"

        self.assertEqual(unreliable(), "success")
        self.assertEqual(len(calls), 3)

    def test_validation(self):
        @validate_arguments(amount=lambda value: value > 0)
        def calculate(amount: int) -> int:
            return amount * 2

        self.assertEqual(calculate(10), 20)

        with self.assertRaises(ValueError):
            calculate(-5)


class TestPipeline(unittest.TestCase):

    def test_filter_items(self):
        result = list(filter_items([1, 2, 3, 4], lambda x: x > 2))
        self.assertEqual(result, [3, 4])

    def test_map_items(self):
        result = list(map_items([1, 2, 3], lambda x: x * 2))
        self.assertEqual(result, [2, 4, 6])

    def test_chunk_items(self):
        result = list(chunk_items([1, 2, 3, 4, 5], 2))
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_invalid_chunk_size(self):
        with self.assertRaises(ValueError):
            list(chunk_items([1, 2], 0))


class TestRegistry(unittest.TestCase):

    def test_plugin_registration(self):
        self.assertIn("GreetingPlugin", PluginMeta.registry)
        plugin = GreetingPlugin()
        self.assertEqual(plugin.run(), "Hello from the plugin!")


class TestSerialization(unittest.TestCase):

    def test_json_round_trip(self):
        @dataclass
        class Product:
            name: str
            price: float

        original = Product("Laptop", 50000.0)
        encoded = to_json(original)
        decoded = from_json(encoded, Product)

        self.assertEqual(decoded, original)


if __name__ == "__main__":
    unittest.main()
