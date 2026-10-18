import csv
from pathlib import Path

from pyutility import chunk_items, filter_items, map_items


def load_sales(file_path: str) -> list[dict]:
    """Load retail sales records from a CSV file."""
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def analyze_sales(records: list[dict]) -> None:
    """Analyze sales records and display basic business KPIs."""

    # Keep records with valid positive sales
    valid_records = filter_items(
        records,
        lambda row: float(row["Sales"]) > 0,
    )
    valid_records = list(valid_records)

    # Calculate total revenue
    revenue_values = map_items(
        valid_records,
        lambda row: float(row["Sales"]),
    )
    total_revenue = sum(revenue_values)

    # Count orders and customers
    total_orders = len({row["Order_ID"] for row in valid_records})
    total_customers = len({row["Customer_ID"] for row in valid_records})

    print("\nRETAIL SALES ANALYSIS")
    print("-" * 30)
    print(f"Valid sales records: {len(valid_records)}")
    print(f"Total revenue: {total_revenue:,.2f}")
    print(f"Total orders: {total_orders}")
    print(f"Unique customers: {total_customers}")

    # Process records in chunks
    print("\nProcessing records in chunks:")
    for number, chunk in enumerate(chunk_items(valid_records, 100), start=1):
        print(f"Chunk {number}: {len(chunk)} records")


if __name__ == "__main__":
    # Change this path if your CSV file is stored elsewhere.
    csv_path = (
        Path.home()
        / "OneDrive"
        / "Desktop"
        / "Retail Project"
        / "retail_sales_cleaned.csv"
    )

    if csv_path.exists():
        sales_records = load_sales(str(csv_path))
        analyze_sales(sales_records)
    else:
        print(f"CSV file not found: {csv_path.resolve()}")
        print("Place retail_sales_cleaned.csv in the project root.")
