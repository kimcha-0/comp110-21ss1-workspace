"""Linked list utility functions part 1."""

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


def last(head: Optional[Node]) -> Optional[int]:
    """Returns the last value of a linked list, or None if the list is empty."""
    if head is None:
        return None
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> Optional[int]:
    """Returns the value at the given index of a linked list, or None if the list is empty."""
    if head is None:
        return None
    else:
        if index == 0:
            return head.data
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> Optional[int]:
    """Return the smallest value in a linked list."""
    if head is None:
        return None
    else:
        max_rest = max(head.next)
        if max_rest is None:
            return head.data
        else:
            if head.data > max_rest:
                return head.data
            else:
                return max_rest