"""A basic recursive data type."""

from __future__ import annotations
from typing import Optional

class Node:
    """A single link in a linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor initializes a node."""
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """Producing a string representation of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def count(a_node: Optional[Node]) -> int:
    """Counting up the elements of a linked list."""
    if a_node is None:
        return 0
    else:
        return 1 + count(a_node.next)
# a: Node = Node(10, None)
# print(a)
# b: Node = Node(20, a)
# print(b)

head: Node = Node(210, None)
head = Node(110, head)
# print(head.data)
# print(head.next)
# print(head.next.data)
head = Node(101, head)
print(count(head))