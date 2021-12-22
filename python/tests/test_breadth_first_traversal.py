from abc import ABC
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
    tree.root.right = BTreeNode('B')
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

def test_three_high():
    tree = BinaryTree(BTreeNode('A'))
    left = BTreeNode('B')
    left.left = BTreeNode('C')
    left.right = BTreeNode('D')
    tree.root.left = left
    right = BTreeNode('E')
    right.left = BTreeNode('F')
    tree.root.right = right
    
    expected = ['A','B','E','C','D','F']
    actual = breadth_first(tree)
    assert actual == expected
