import sqlite3
import tempfile
import unittest
from pathlib import Path

from pyutility.context import sqlite_connection
from pyutility.pipeline import filter_items, map_items


class TestIntegration(unittest.TestCase):

    def test_pipeline_and_database(self):
        sales = [100, 200, 300, 400]

        high_sales = filter_items(sales, lambda value: value >= 200)

        doubled_sales = list(map_items(high_sales, lambda value: value * 2))

        with tempfile.TemporaryDirectory() as directory:
            database = str(Path(directory) / "test.db")

            with sqlite_connection(database) as connection:
                connection.execute("CREATE TABLE sales (amount INTEGER)")

                connection.executemany(
                    "INSERT INTO sales (amount) VALUES (?)",
                    [(amount,) for amount in doubled_sales],
                )

            # the SQLite connection
            connection = sqlite3.connect(database)

            try:
                rows = connection.execute(
                    "SELECT amount FROM sales ORDER BY amount"
                ).fetchall()
            finally:
                connection.close()

            self.assertEqual(rows, [(400,), (600,), (800,)])


if __name__ == "__main__":
    unittest.main()
