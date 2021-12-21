from trees.trees import BinaryTree, BTreeNode
from breadth_first_traversal.breadth_first_traversal import breadth_first
import pytest

def test_empty():
    tree = BinaryTree()
    assert breadth_first(tree) == []


@pytest.fixture
def three_high_tree():
    tree = BinaryTree(BTreeNode('A'))
    left = BTreeNode('B')
    left.left = BTreeNode('D')
    left.right = BTreeNode('E')
    tree.root.left = left
    right = BTreeNode('C')
    right.left = BTreeNode('F')
    tree.root.right = right
    return tree
