"""
Geometric Shape Polymorphism.

Demonstrates Abstract Base Classes (ABC) and method overrides.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate shape area."""

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate shape perimeter."""


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    print("=== Shape Polymorphism ===")
    shapes: list[Shape] = [Circle(5.0), Rectangle(4.0, 6.0)]
    for s in shapes:
        print(f"{s.__class__.__name__:10s} -> Area: {s.area():.2f}, Perimeter: {s.perimeter():.2f}")
