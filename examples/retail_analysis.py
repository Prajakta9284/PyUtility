import csv
from pathlib import Path
from typing import Any, Iterator


def load_sales_data(file_path: str) -> Iterator[dict[str, Any]]:
    """Load retail sales records from a CSV file."""
    with Path(file_path).open(
        mode="r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield dict(row)


def analyze_sales(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Calculate basic retail sales metrics."""
    total_sales = 0.0
    total_profit = 0.0
    total_quantity = 0
    valid_records = 0

    for record in records:
        try:
            sales = float(record.get("Sales", 0) or 0)
            profit = float(record.get("Profit", 0) or 0)
            quantity = int(float(record.get("Quantity", 0) or 0))
        except (TypeError, ValueError):
            continue

        total_sales += sales
        total_profit += profit
        total_quantity += quantity
        valid_records += 1

    return {
        "valid_records": valid_records,
        "total_sales": round(total_sales, 2),
        "total_profit": round(total_profit, 2),
        "total_quantity": total_quantity,
        "average_sales": (
            round(total_sales / valid_records, 2) if valid_records else 0.0
        ),
    }


def main() -> None:
    """Run the retail sales analysis."""
    file_path = "retail_sales_cleaned.csv"

    if not Path(file_path).exists():
        print(f"Dataset not found: {file_path}")
        print("Place the CSV file in the project root directory.")
        return

    records = list(load_sales_data(file_path))
    results = analyze_sales(records)

    print("RETAIL SALES ANALYSIS")
    print("-" * 30)

    for metric, value in results.items():
        print(f"{metric.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
