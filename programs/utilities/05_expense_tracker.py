"""
Expense Tracker Utility.

Tracks categorized expenses and generates category percentage totals.
"""

from collections import defaultdict


class ExpenseTracker:
    def __init__(self):
        self.expenses: list[dict] = []

    def add_expense(self, category: str, amount: float, description: str) -> None:
        self.expenses.append({"category": category.lower(), "amount": amount, "description": description})

    def total_spending(self) -> float:
        return sum(e["amount"] for e in self.expenses)

    def category_breakdown(self) -> dict[str, float]:
        totals = defaultdict(float)
        for e in self.expenses:
            totals[e["category"]] += e["amount"]
        return dict(totals)


if __name__ == "__main__":
    print("=== Expense Tracker ===")
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 24.50, "Lunch")
    tracker.add_expense("Transport", 15.00, "Bus Pass")
    tracker.add_expense("Food", 42.00, "Dinner")
    tracker.add_expense("Books", 35.00, "Python Book")

    print(f"Total: ${tracker.total_spending():.2f}")
    for cat, amt in tracker.category_breakdown().items():
        print(f" - {cat.title():10s}: ${amt:.2f}")
