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
    actual = Stack._top.value
    expected = 5
    assert actual == expected
