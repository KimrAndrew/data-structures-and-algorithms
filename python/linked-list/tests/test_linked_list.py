import linked_list
from linked_list.linked_list import Node, Linked_List

def test_node():
    assert Node(5)

def test_Linked_List():
    assert Linked_List()

def test_create_node():
    node = Node(5)
    assert node.data == 5 and node.next == None

def test_create_empty_linked_list():
    l_list = Linked_List()
    assert l_list.head == None

def test_insert_node():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    assert l_list.head.data == 7

def test_contains_true():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    assert l_list.contains(12) is True

def test_contains_false():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    assert l_list.contains(15) is False