from trees.trees import BTreeNode, BinaryTree
import pytest

def test_node_import(node_5):
    assert node_5

def test_node_with_value(node_5):
    assert node_5.value == 5

def test_node_no_branches(node_5):
    assert node_5.left is None and node_5.right is None

def test_add_branches():
    node = BTreeNode(5,BTreeNode(4),BTreeNode(6))
    assert node.left.value == 4
    assert node.right.value == 6

def test_tree_import():
    assert BinaryTree()

def test_tree_with_root():
    assert BinaryTree(BTreeNode(5))

def test_inorder_collection(three_high_tree):
    tree = three_high_tree
    assert tree.inorder() == [6,4,3,5,8,7,9]

def test_preorder_collection(three_high_tree):
    tree = three_high_tree
    assert tree.preorder() == [3,5,4,7,9,8,6]




@pytest.fixture
def node_5():
    return BTreeNode(5)

@pytest.fixture()
def three_high_tree():
    tree = BinaryTree(BTreeNode(6))
    left = BTreeNode(4,BTreeNode(3),BTreeNode(5))
    right = BTreeNode(8,BTreeNode(7),BTreeNode(9))
    tree.root.left = left
    tree.root.right = right
    return tree

