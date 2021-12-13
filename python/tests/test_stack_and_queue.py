from stack_and_queue.stack_and_queue import Node

def test_node_exists():
    assert Node(5)

def test_node_has_next():
    node_one = Node(1)
    node_one.next = Node(2)
    actual = node_one.next.value
    expected = 2
    assert actual == expected