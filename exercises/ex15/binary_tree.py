"""Basic class definiton for a binary tree."""

from __future__ import annotations
from typing import Optional

__author__ = "730407570"


class TreeNode:
    """Recursive structure with two children."""
    # TODO: The required attributes go here
    data: int
    left: Optional[TreeNode]
    right: Optional[TreeNode]
    
    # TODO: Your constructor will go here.
    def __init__(self, data: int, left: Optional[TreeNode], right: Optional[TreeNode]) -> None:
        """Constructor for TreeNode attributes."""
        self.data = data
        self.left = left
        self.right = right
    # TODO: Uncomment when ready to test!
    
    def __repr__(self) -> str:
        """Produce a string representation of a binary tree."""
        print_tree(self, 0) 
        return ""


def print_tree(root: Optional[TreeNode], num_spaces: int) -> None:
    """A helper to display str represenation of a tree."""
    if root is None:
        return None
    num_spaces += 2
    # Process right child first 
    print_tree(root.right, num_spaces) 
    for i in range(2, num_spaces):
        print(end=" ") 
    print(root.data) 
    # left child
    print_tree(root.left, num_spaces) 
    return None


def main() -> None:
    """Entrypoint of program."""
    # Tree 0 - Uncomment these lines (and lines above) when class and constructor are defined.
    left: TreeNode = TreeNode(1, None, None)
    right: TreeNode = TreeNode(2, None, None)
    tree_0: TreeNode = TreeNode(0, left, right)
    print(tree_0)

    # TODO: Define Tree 1 here.
    left_1: TreeNode = TreeNode(2, None, None)
    left_2: TreeNode = TreeNode(1, left_1, None)
    tree_1: TreeNode = TreeNode(0, left_2, None)
    print(tree_1)
    # TODO: Define Tree 2 here.
    tree_2_left: TreeNode = TreeNode(1, None, None)
    tree_2_left_1: TreeNode = TreeNode(4, None, None)
    tree_2_right_2: TreeNode = TreeNode(4, None, None)
    tree_2_right: TreeNode = TreeNode(2, tree_2_left_1, tree_2_right_2)
    tree_2: TreeNode = TreeNode(0, tree_2_left, tree_2_right)
    print(tree_2)


if __name__ == "__main__":
    main()