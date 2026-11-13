"""
Stack Data Structure (LIFO).

Last-In, First-Out collection with constant O(1) operations.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    print("=== Stack (LIFO) ===")
    s = Stack[int]()
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Top element (peek): {s.peek()}")
    print(f"Popped: {s.pop()}")
    print(f"Remaining size: {s.size()}")
