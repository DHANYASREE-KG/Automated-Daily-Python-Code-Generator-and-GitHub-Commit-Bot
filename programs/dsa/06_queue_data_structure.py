"""
Queue Data Structure (FIFO).

First-In, First-Out collection with O(1) enqueue and dequeue operations.
"""

from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self):
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self) -> T:
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    print("=== Queue (FIFO) ===")
    q = Queue[str]()
    q.enqueue("Alice")
    q.enqueue("Bob")
    q.enqueue("Charlie")
    print(f"Front: {q.front()}")
    print(f"Dequeued: {q.dequeue()}")
    print(f"Next front: {q.front()}")
