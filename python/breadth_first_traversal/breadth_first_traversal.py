from typing import List
from trees.trees import BinaryTree
from stack_and_queue.stack_and_queue import Queue

def breadth_first(tree:BinaryTree) -> list:
    if tree.root is None:
        return []