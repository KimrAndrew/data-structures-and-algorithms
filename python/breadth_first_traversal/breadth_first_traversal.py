from typing import List
from trees.trees import BinaryTree
from collections import deque

def breadth_first(tree:BinaryTree) -> list:
    q = deque()
    output = []
    if tree.root is None:
        return output
    q.appendleft(tree.root)
    while len(q) > 0:
        temp = q.pop()
        if temp.left is not None:
            q.appendleft(temp.left)
        if temp.right is not None:
            q.appendleft(temp.right)
        output.append(temp.value)
    return output
    