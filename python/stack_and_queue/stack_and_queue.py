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