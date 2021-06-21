"""Linked list utility functions part 2."""

from __future__ import annotations
from typing import Optional

__author__ = "730407570"

class Node:
    """A single link in a linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor initializes a Node."""
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

def linkify(items: list[int]) -> Optional[Node]:
    """Converts a list into a linked list."""
    # edge case
    if len(items) == 0:
        return None
    # base case
    elif len(items) == 1:
        return Node(items[0], None)
    return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a new linked list with elements multiplied by 'factor'."""
    if head is None:
        return None
    else:
        first = head.data * factor
        rest = scale(head.next, factor)
        return Node(first, rest)


def concat(lhs: Optional[Node], rhs: Optional[Node]) -> Optional[Node]:
    """Returns a new linked list where the first list is followed by the second."""
    # base case
    if lhs is None:
        return rhs
    if rhs is None:
        return lhs
    elif lhs is None and rhs is None:
        return None
    # recursive case
    else:
        first = lhs.data
        rest = concat(lhs.next, rhs)
        return Node(first, rest)

x: Optional[Node] = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
y: list[int] = [1, 2, 3, 4, 5]
z: Optional[Node] = Node(6, Node(7, Node(8, Node(9, None))))
print(linkify(y))
print(scale(x, 2))
print(concat(x, z))