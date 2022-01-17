from tree_intersection.tree_intersection import tree_intersection
from trees.trees import BinaryTree
import pytest

@pytest.mark.skip()
def test_no_matches():
    #TODO: Add basic add method to BinaryTree class
    tree_one = BinaryTree()
    tree_two = BinaryTree()
    tree_one.add(1)
    tree_one.add(2)
    tree_one.add(3)
    tree_two.add(4)
    tree_two.add(5)
    tree_two.add(6)
    actual_matches = tree_intersection(tree_one,tree_two)
    expected_matches = []
    assert actual_matches == expected_matches

@pytest.mark.skip()
def test_one_match():
    tree_one = BinaryTree()
    tree_two = BinaryTree()
    tree_one.add(5)
    tree_one.add(6)
    tree_one.add(7)
    tree_two.add(3)
    tree_two.add(4)
    tree_two.add(5)
    actual_matches = tree_intersection(tree_one,tree_two)
    expected_matches = [5]
    assert actual_matches == expected_matches

@pytest.mark.skip()
def test_identical_trees():
    tree_one = BinaryTree()
    tree_two = BinaryTree()
    tree_one.add(1)
    tree_one.add(2)
    tree_one.add(3)
    tree_two.add(1)
    tree_two.add(2)
    tree_two.add(3)
    actual_matches = tree_intersection(tree_one,tree_two)
    expected_matches = [1,2,3]
    assert actual_matches == expected_matches


