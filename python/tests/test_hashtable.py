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
    hash.add('Cta','Cta_val')
    assert hash.storage[hash.hash('Cta')].get('Cta').value == 'Cta_val'

def test_hash_add_same_key():
    hash = HashTable()
    hash.add('Cat', 'Cat_val')
    with pytest.raises(KeyError):
        hash.add('Cat','Hopefully an exception')

def test_hash_get():
    hash = HashTable()
    hash.add('Cat','Cat_val')
    hash.add('Cta','Cta_val')
    assert hash.get('Cat').value == 'Cat_val'
    assert hash.get('Cta').value == 'Cta_val'

def test_hash_contains():
    hash = HashTable()
    hash.add('Cat','Cat_val')
    hash.add('Cta','Cta_val')
    assert hash.contains('Cta')
    assert hash.contains('Cat')
    assert not hash.contains('atC')

def test_hash_repeated_word():
    hash_one = HashTable()
    repeat = hash_one.repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    assert repeat == 'it'