import pytest
from stack_and_queue.stack_and_queue import Node, Stack

def test_node_exists():
    assert Node(5)

def test_node_has_next():
    node_one = Node(1)
    node_one.next = Node(2)
    actual = node_one.next.value
    expected = 2
    assert actual == expected

def test_stack_exists():
    assert Stack()

def test_stack_push():
    stack = Stack()
    stack.push(5)
    actual = stack._top.value
    expected = 5
    assert actual == expected

def test_stack_is_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_stack_is_not_empty():
    stack = Stack()
    stack.push(1)
    actual = stack.is_empty()
    expected = False
    assert actual == expected

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    popped = stack.pop()
    assert popped == 3 and stack._top.value == 2

def test_stack_pop_on_empty_raises_exception():
    stack = Stack()
    with pytest.raises(OverflowError):
        stack.pop()
