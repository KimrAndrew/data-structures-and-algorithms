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

def test_value_not_found_raises_error():
    l_list = Linked_List()
    l_list.insert(5)
    with pytest.raises(ValueError):
        l_list.insert_before(10,7)

def test_insert_after():
    l_list = Linked_List()
    l_list.insert(3)
    l_list.insert(1)
    l_list.insert_after(1,2)
    assert l_list.get_index(1) == 2

def test_append():
    l_list = Linked_List()
    l_list.insert(3)
    l_list.insert(2)
    l_list.insert(1)
    l_list.append(4)
    assert l_list.get_index(3) == 4

def test_append_to_empty():
    l_list = Linked_List()
    l_list.append(1)
    assert l_list.get_index(0) == 1

def test_kth_from_end_middle_value():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    expected = 12
    actual = l_list.kth_from_end(3)
    assert actual == expected
    
def test_k_greater_than_length():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    with pytest.raises(IndexError):
        l_list.kth_from_end(6)

def test_k_negative_value():
    l_list = Linked_List()
    with pytest.raises(IndexError):
        l_list.kth_from_end(-1)

def test_k_equals_length():
    l_list = Linked_List()
    l_list.insert(5)
    l_list.insert(7)
    l_list.insert(12)
    l_list.insert(19)
    l_list.insert(31)
    expected = 31
    actual = l_list.kth_from_end(5)
    assert actual == expected

def test_k_equals_0():
    l_list = Linked_List()
    l_list.append(5)
    l_list.append(4)
    expected = 4
    actual = l_list.kth_from_end(0)
    return expected == actual

def kth_from_end_on_length_one():
    l_list = Linked_List()
    l_list.append(1)
    expected = 1
    actual = l_list.kth_from_end(0)
    assert expected == actual