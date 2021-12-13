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