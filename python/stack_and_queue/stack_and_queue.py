class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack():
    def __init__(self,_top=None) -> None:
        self._top = _top
    
    def push(self, value):
        self._top = Node(value, self._top)

    def is_empty(self):
        return self._top is None

    def pop(self):
        popped = self._top
        if popped is None:
            raise OverflowError("Cannot pop on empty Stack")
        self._top = self._top.next
        return popped.value

    def peek(self):
        if self.is_empty():
            raise OverflowError("Cannot peek on empty Stack")
        return self._top.value

class Queue():
    def __init__(self,_front=None,_rear=None):
        self._front = _front
        self._rear = _rear

    def enqueue(self,value):
        if self._rear is None:
            self._front = Node(value,self._front)
            self._rear = self._front
            return
        self._rear.next = Node(value)
        self._rear = self._rear.next

    def is_empty(self):
        return self._front is None

    def dequeue(self):
        if self.is_empty():
            raise OverflowError("Cannot dequeue from empty Queue")
        dequeued = self._front
        self._front = self._front.next
        return dequeued.value

    def peek(self):
        if self.is_empty():
            raise OverflowError("Cannot peek on empty Queue")
        return self._front.value