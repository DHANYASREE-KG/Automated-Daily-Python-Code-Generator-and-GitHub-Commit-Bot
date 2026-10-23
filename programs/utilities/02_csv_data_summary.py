"""
CSV Summary and Aggregation Utility.

Parses comma-separated text and aggregates numerical columns.
"""

import csv
import io


def summarize_csv_column(csv_data: str, column_name: str) -> dict[str, float]:
    """Calculate sum, mean, min, and max of a numerical CSV column."""
    reader = csv.DictReader(io.StringIO(csv_data.strip()))
    values = []

    for row in reader:
        if column_name in row and row[column_name]:
            try:
                values.append(float(row[column_name]))
            except ValueError:
                pass

    if not values:
        raise ValueError(f"No numeric data found for column: {column_name}")

    return {
        "count": len(values),
        "sum": round(sum(values), 2),
        "mean": round(sum(values) / len(values), 2),
        "min": min(values),
        "max": max(values),
    }


if __name__ == "__main__":
    print("=== CSV Data Summarizer ===")
    sample_csv = """product,price,units
Laptop,1200.50,5
Mouse,25.00,40
Monitor,299.99,12
Keyboard,79.99,25
"""
    results = summarize_csv_column(sample_csv, "price")
    for stat, val in results.items():
        print(f"{stat.title():8s}: {val}")
