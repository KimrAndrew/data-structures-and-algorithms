from stack_and_queue.stack_and_queue import Stack, Node

class Queue():
    def __init__(self) -> None:
        self._stack_one = Stack()
        self._stack_two = Stack()

    def enqueue(self,value):
        if self._stack_one.is_empty():
            flipped_stack = self._stack_one
            holding_stack = self._stack_two

        else:
            holding_stack = self._stack_one
            flipped_stack = self._stack_two

        if holding_stack.is_empty():
            flipped_stack.push(Node(value))

        while not holding_stack.is_empty():
            flipped_stack.push(holding_stack.pop())

        flipped_stack.push(Node(value))

    def dequeue(self):
        if self._stack_one.is_empty():
            flipped_stack = self._stack_one
            holding_stack = self._stack_two

        else:
            holding_stack = self._stack_one
            flipped_stack = self._stack_two
    
        while not holding_stack.is_empty():
            flipped_stack.push(holding_stack.pop())

        return flipped_stack.pop()