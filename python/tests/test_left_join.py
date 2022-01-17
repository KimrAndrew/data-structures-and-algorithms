from left_join.left_join import left_join
from hashtable.hashtable import HashTable
import pytest

def test_left_join_empty():
    left_table = HashTable()
    right_table = HashTable()
    joined_tables = left_join(left_table,right_table)
    assert joined_tables == []

def test_left_join_only_left_empty():
    left = HashTable()
    right = HashTable()
    right.add('Cat','Cat_one')
    joined_tables = left_join(left,right)
    assert joined_tables == []


def test_left_join_identical_keys():
    left = HashTable()
    right = HashTable()
    left.add('Cat','left')
    left.add('Dog','left')
    right.add('Cat','right')
    right.add('Dog','right')
    joined = left_join(left,right)
    assert joined == [['Cat','left','right'],['Dog','left','right']]

@pytest.mark.skip
def test_left_join_right_has_nulls():
    left = HashTable()
    right = HashTable()
    left.add('Cat','left')
    joined = left_join(left,right)
    assert joined == [['Cat','left',None]]

@pytest.mark.skip
def test_left_join_collisions():
    left = HashTable()
    right = HashTable()
    left.add('Cat','left')
    left.add('Cta','left')
    right.add('Cat','right')
    right.add('Cta','right')
    joined = left_join(left,right)
    assert joined == [['Cat','left','right'],['Cta','left','right']]