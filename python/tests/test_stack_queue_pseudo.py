from stack_queue_pseudo.stack_queue_pseudo import Queue
import pytest

def test_import():
    assert Queue()

def test_enqueue_one():
    pq = Queue()
    pq.enqueue(1)

    expected = 1
    actual = pq._stack_one.peek().value
    assert expected == actual

def test_enqueue_three():
    pq = Queue()
    pq.enqueue(1)
    pq.enqueue(2)
    pq.enqueue(3)

    expected = 3
    actual = pq._stack_one.peek().value

    assert actual == expected

@pytest.mark.skip("TODO")
def test_dequeue_one():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.dequeue()
    expected = 1
    assert actual == expected