from hashtable.hashtable import Node, LinkedList, HashTable
import pytest

def test_node():
    node = Node('Key','Value')
    assert node
    assert node.key == 'Key'
    assert node.value == 'Value'

def test_ll_add():
    ll = LinkedList()
    ll.add('first','first_val')
    ll.add('second','second_val')
    ll.add('third','third_val')
    assert ll.head.key == 'first'
    assert ll.head.value == 'first_val'
    assert ll.head.next.key == 'second'
    assert ll.head.next.value == 'second_val'
    assert ll.head.next.next.key == 'third'
    assert ll.head.next.next.value == 'third_val'

def test_ll_get():
    ll = LinkedList()
    ll.add('first','first_val')
    ll.add('second','second_val')
    ll.add('third','third_val')
    assert ll.get('first').value == 'first_val'
    assert ll.get('second').value == 'second_val'
    assert ll.get('third').value == 'third_val'

def test_hash_add():
    hash = HashTable()
    hash.add('Cat','Cat_val')
    assert hash.storage[hash.hash('Cat')].get('Cat').value == 'Cat_val'

    # Check for same key different value - should overwrite

    # hash.add('Cat','New_Cat_val')
    # assert hash.storage[hash.hash('Cat')].get('Cat').value == 'New_Cat_val'

    # Check for collision handling
    hash.add('Cta','Cta_val')
    assert hash.storage[hash.hash('Cta')].get('Cta').value == 'Cta_val'

def test_hash_get():
    hash = HashTable()
    hash.add('Cat','Cat_val')
    hash.add('Cta','Cta_val')
    assert hash.get('Cat').value == 'Cat_val'
    assert hash.get('Cta').value == 'Cta_val'