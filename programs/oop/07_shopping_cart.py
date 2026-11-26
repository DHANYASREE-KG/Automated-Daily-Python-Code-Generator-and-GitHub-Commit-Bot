"""
E-Commerce Shopping Cart.

Calculates subtotal, discounts, tax, and final checkout totals.
"""


class CartItem:
    def __init__(self, name: str, unit_price: float, quantity: int = 1):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.unit_price * self.quantity


class ShoppingCart:
    def __init__(self, tax_rate: float = 0.08):
        self.items: list[CartItem] = []
        self.tax_rate = tax_rate

    def add_item(self, item: CartItem) -> None:
        self.items.append(item)

    @property
    def subtotal(self) -> float:
        return sum(item.total_price for item in self.items)

    def calculate_total(self, discount_percent: float = 0.0) -> dict[str, float]:
        sub = self.subtotal
        disc = sub * (discount_percent / 100)
        tax = (sub - disc) * self.tax_rate
        final = (sub - disc) + tax
        return {"subtotal": sub, "discount": disc, "tax": tax, "final": final}


if __name__ == "__main__":
    print("=== Shopping Cart ===")
    cart = ShoppingCart(tax_rate=0.07)
    cart.add_item(CartItem("Wireless Mouse", 25.0, 2))
    cart.add_item(CartItem("Mechanical Keyboard", 80.0, 1))

    receipt = cart.calculate_total(discount_percent=10.0)
    for k, v in receipt.items():
        print(f"{k.capitalize():10s}: ${v:.2f}")
