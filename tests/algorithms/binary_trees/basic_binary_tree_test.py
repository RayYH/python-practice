from src.algorithms.binary_trees.basic_binary_tree import Node, display, \
    is_full_binary_tree, depth_of_tree
from src.helper.ioh import captured_output, to_string


def test_case_one():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    with captured_output() as (out, err):
        display(tree)
    assert to_string(out) == "4 2 6 5 1 8 9 7 3"
    assert not is_full_binary_tree(tree)
    assert depth_of_tree(tree) == 5
