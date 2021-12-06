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
    assert l_list.head.data == 5