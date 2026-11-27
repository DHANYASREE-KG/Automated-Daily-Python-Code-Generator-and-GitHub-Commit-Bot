"""
Singly Linked List.

Basic node pointer structure supporting traversal and in-place reversal.
"""

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, next_node: Optional["Node"] = None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self) -> list[Any]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


if __name__ == "__main__":
    print("=== Singly Linked List ===")
    ll = LinkedList()
    for val in [10, 20, 30, 40]:
        ll.append(val)
    print(f"Original: {ll.to_list()}")
    ll.reverse()
    print(f"Reversed: {ll.to_list()}")
