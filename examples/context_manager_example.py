from pathlib import Path
from tempfile import TemporaryDirectory

from pyutility.context import sqlite_connection


def main() -> None:
    # Create a temporary folder and database
    with TemporaryDirectory() as directory:
        database_path = str(Path(directory) / "example.db")

        # Open the database using PyUtility's context manager
        with sqlite_connection(database_path) as connection:
            connection.execute(
                """
                CREATE TABLE products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                )
                """
            )

            connection.executemany(
                "INSERT INTO products (name, price) VALUES (?, ?)",
                [
                    ("Laptop", 50000.0),
                    ("Mouse", 800.0),
                    ("Keyboard", 1500.0),
                ],
            )

            results = connection.execute(
                "SELECT id, name, price FROM products ORDER BY id"
            ).fetchall()

            print("=== Product Records ===")
            for product_id, name, price in results:
                print(f"ID: {product_id}, Name: {name}, Price: ₹{price:.2f}")

        print("\nDatabase context manager closed successfully.")


if __name__ == "__main__":
    main()
