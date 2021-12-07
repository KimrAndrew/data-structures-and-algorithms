import linked_list, pytest
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

def test_str():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    assert str(l_list) == '{31} -> {19} -> {12} -> {7} -> {5} -> NONE'

def test_empty_list_str():
    l_list = Linked_List()
    assert str(l_list) == "NONE"

def test_get_index_no_int_raises_exception():
    l_list = Linked_List()
    with pytest.raises(TypeError):
        l_list.get_index('a')

def test_get_index_out_of_bounds_raises_exception():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    with pytest.raises(IndexError):
        l_list.get_index(5)

def test_get_index():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    assert l_list.get_index(4) == 5
    assert l_list.get_index(2) == 12


def test_insert_before_last_item():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    l_list.insert_before(5,10)
    assert l_list.get_index(4) == 10

def test_insert_before_head():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert_before(5,3)
    assert l_list.get_index(0) == 3

