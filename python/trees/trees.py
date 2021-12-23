from typing import Collection
from collections import deque


class BTreeNode():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    
class BinaryTree():
    def __init__(self, root=None):
        self.root = root

    def inorder(self):
        output = []
        def walk(root:BTreeNode):
            if root is None:
                return
            output.append(root.value)
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return output

    def preorder(self):
        output = []
        def walk(root:BTreeNode):
            if root.left is None and root.right is None:
                output.append(root.value)
                return
            walk(root.left)
            walk(root.right)
            output.append(root.value)
        walk(self.root)
        return output

class KTreeNode():

    def __init__(self,k:int,value,connections:Collection=[]) -> None:
            self.connections = list(connections)
            if len(self.connections) > k:
                raise IndexError(f'Length of connections: {connections} cannot be greater than k: {k}')
            self.value = value

class KAryTree():
    def __init__(self,k:int,root = None) -> None:
            self.k = k
            if root is None:
                self.root = root
            elif not isinstance(root,KTreeNode):
                self.root = KTreeNode(root)
            else:
                self.root = root
        
    def add(self,to_add) -> None:
        q = deque()
        if self.root is None:
            self.root = KTreeNode(self.k, to_add)
            return
        q.appendleft(self.root)
        temp = None
        while len(q) > 0:
            temp = q.pop()
            if len(temp.connections) < self.k:
                temp.connections.append(KTreeNode(self.k,to_add))
                return
            for connection in temp.connections:
                q.appendleft(connection)

    def breadth_first_to_list(self) -> list:
        q = deque()
        output = []

        if self.root is None:
            return output

        q.appendleft(self.root)

        while len(q) > 0:
            temp = q.pop()

            for connection in temp.connections:
                q.appendleft(connection)
                
            output.append(temp.value)

        return output
