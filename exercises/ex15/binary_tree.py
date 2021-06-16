"""Basic class definiton for a binary tree."""

from __future__ import annotations
from typing import Optional

__author__ = "YOUR PID HERE"


class TreeNode:
    """Recursive structure with two children."""
    # TODO: The required attributes go here

    # TODO: Your constructor will go here.

    # TODO: Uncomment when ready to test!
    # def __repr__(self) -> str:
    #     """Produce a string representation of a binary tree."""
    #     print_tree(self, 0) 
    #     return ""

# TODO: Uncomment when ready to test!
# def print_tree(root: Optional[TreeNode], num_spaces: int) -> None:
#     """A helper to display str represenation of a tree."""
#     if root is None:
#         return None
#     num_spaces += 2
#     # Process right child first 
#     print_tree(root.right, num_spaces) 
#     for i in range(2, num_spaces):
#         print(end=" ") 
#     print(root.data) 
#     # left child
#     print_tree(root.left, num_spaces) 
#     return None


def main() -> None:
    """Entrypoint of program."""
    # Tree 0 - Uncomment these lines (and lines above) when class and constructor are defined.
    # left: TreeNode = TreeNode(1, None, None)
    # right: TreeNode = TreeNode(2, None, None)
    # tree_0: TreeNode = TreeNode(0, left, right)
    # print(tree_0)

    # TODO: Define Tree 1 here.

    # TODO: Define Tree 2 here.


if __name__ == "__main__":
    main()

