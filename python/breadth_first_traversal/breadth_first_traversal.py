from typing import List
from trees.trees import BinaryTree
from stack_and_queue.stack_and_queue import Queue

def breadth_first(tree:BinaryTree) -> list:
    q = Queue()
    output = []
    if tree.root is None:
        return output
    q.enqueue(tree.root)
    while not q.is_empty():
        temp = q.dequeue()
        if temp.left is not None:
            q.enqueue(temp.left)
        if temp.right is not None:
            q.enqueue(temp.right)
        output.append(temp.value)
    return output
    