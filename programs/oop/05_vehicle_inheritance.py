"""
Vehicle Inheritance Hierarchy.

Demonstrates OOP inheritance, polymorphism, and abstract method patterns.
"""


class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self) -> str:
        return f"{self.year} {self.brand} {self.model}"

    def fuel_type(self) -> str:
        return "Unknown"


class ElectricCar(Vehicle):
    def __init__(self, brand: str, model: str, year: int, battery_kwh: float):
        super().__init__(brand, model, year)
        self.battery_kwh = battery_kwh

    def fuel_type(self) -> str:
        return f"Electric ({self.battery_kwh} kWh)"


class GasolineCar(Vehicle):
    def fuel_type(self) -> str:
        return "Gasoline"


if __name__ == "__main__":
    print("=== Vehicle Polymorphic Hierarchy ===")
    fleet: list[Vehicle] = [
        ElectricCar("Tesla", "Model 3", 2024, 75.0),
        GasolineCar("Toyota", "Camry", 2023),
    ]
    for v in fleet:
        print(f"{v.describe()} -> Fuel: {v.fuel_type()}")
