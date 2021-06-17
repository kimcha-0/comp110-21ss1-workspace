"""Some examples of building linked lists recursively."""

from lessons.ls30_node import Node
from typing import Optional

def only_evens(head: Optional[Node]) -> Optional[Node]:
    """Construct a list with only the even values."""
    if head is None:
        return None
    else:
        first = head.data
        if first % 2 == 0:
            # want to include this in our result!
            rest = only_evens(head.next)
            return Node(first, rest)
        else:
            # don't want to include
            return only_evens(head.next)

print(only_evens(Node(2, Node(3, Node(4, None)))))


