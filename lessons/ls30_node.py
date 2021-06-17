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


def min(head: Optional[Node]) -> Optional[int]:
    """Return the smallest value in a linked list."""
    # base case
    if head is None:
        return None
    else:
        # find the min of the rest of the list
        min_rest = min(head.next)
        if min_rest is None:
            return head.data
        # compare the min of the rest of the list to our current data
        else:   
            if head.data < min_rest:
                return head.data
        # return the smaller of the two
            else:
                return min_rest
    return None



def includes(head: Optional[Node], needle: int) -> bool:
    """Searching for a given value in a linked list."""
    if head is None:
        return False
    elif head.data == needle:
        return True
    else:
        return includes(head.next, needle)
    return False


def count(a_node: Optional[Node]) -> int:
    """Counting up the elements of a linked list."""
    if a_node is None:
        return 0
    else:
        return 1 + count(a_node.next)


def __eq__(self, rhs: Optional[Node]) -> bool:
    # both lists None at the same time
    if self is None and rhs is None:
        return True
    elif self is None or rhs is None or self.data != rhs.data:
        return False
    else:
        return self.next == rhs.next
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