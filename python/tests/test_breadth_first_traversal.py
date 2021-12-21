from trees.trees import BinaryTree, BTreeNode
from breadth_first_traversal.breadth_first_traversal import breadth_first
import pytest

def test_empty():
    tree = BinaryTree()
    assert breadth_first(tree) == []

def test_root_only():
    tree = BinaryTree(BTreeNode('A'))
    actual =  breadth_first(tree)
    expected = ['A']
    assert actual == expected

def test_two_high_left_only():
    tree = BinaryTree(BTreeNode('A'))
    tree.root.left = BTreeNode('B')
    expected = ['A',"B"]
    actual = breadth_first(tree)
    assert actual == expected

def test_two_high_right_only():
    tree = BinaryTree(BTreeNode('A'))
    tree.root.right = "B"
    expected = ['A',"B"]
    actual = breadth_first(tree)
    assert actual == expected

def test_two_high_balanced():
    tree = BinaryTree(BTreeNode('A'))
    tree.root.left = BTreeNode('B')
    tree.root.right = BTreeNode('C')
    expected = ['A','B','C']
    actual = breadth_first(tree)
    assert actual == expected


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
