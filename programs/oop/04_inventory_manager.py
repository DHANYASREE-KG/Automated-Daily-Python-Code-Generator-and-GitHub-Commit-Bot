"""
Inventory Stock Management.

Tracks warehouse products, pricing, stock levels, and automated reorder alerts.
"""


class Product:
    def __init__(self, sku: str, name: str, price: float, quantity: int, reorder_level: int = 10):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity
        self.reorder_level = reorder_level

    @property
    def total_value(self) -> float:
        return self.price * self.quantity

    def needs_reorder(self) -> bool:
        return self.quantity <= self.reorder_level


class Warehouse:
    def __init__(self):
        self.items: dict[str, Product] = {}

    def add_product(self, p: Product) -> None:
        self.items[p.sku] = p

    def total_valuation(self) -> float:
        return sum(p.total_value for p in self.items.values())

    def get_reorder_alerts(self) -> list[str]:
        return [p.name for p in self.items.values() if p.needs_reorder()]


if __name__ == "__main__":
    print("=== Warehouse Inventory ===")
    wh = Warehouse()
    wh.add_product(Product("SKU-1", "Wireless Keyboard", 45.0, 5, reorder_level=10))
    wh.add_product(Product("SKU-2", "USB-C Hub", 29.99, 40, reorder_level=15))

    print(f"Total Valuation: ${wh.total_valuation():.2f}")
    print(f"Items needing reorder: {wh.get_reorder_alerts()}")
