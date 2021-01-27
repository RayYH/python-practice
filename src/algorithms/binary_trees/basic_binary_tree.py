from typing import Optional


class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


# Inorder traversal of the tree
def display(tree: Optional[Node]) -> None:
    if tree:
        display(tree.left)
        print(tree.data, end=' ')
        display(tree.right)


def depth_of_tree(tree: Optional[Node]) -> int:
    """
    The depth of a node is the number of edges from the node to the tree's root
    node. A root node will have a depth of 0.

    The height of a node is the number of edges on the longest path from the
    node to a leaf. A leaf node will have a height of 0.

    The height of a tree would be the height of its root node, or equivalently,
    the depth of its deepest node.
    """
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(
        tree.right)) if tree else 0


def is_full_binary_tree(tree: Optional[Node]) -> bool:
    """
    A full binary tree is a tree in which every node has either 0 or 2 children.
    """
    if not tree:
        return True
    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(
            tree.right)
    else:
        return not tree.left and not tree.right
