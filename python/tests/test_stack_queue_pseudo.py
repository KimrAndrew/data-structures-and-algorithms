from stack_queue_pseudo.stack_queue_pseudo import Queue

def test_import():
    assert Queue()

def test_enqueue_one():
    pq = Queue()
    pq.enqueue(1)

    expected = 1
    actual = pq._stack_one.peek()
    assert expected == actual


