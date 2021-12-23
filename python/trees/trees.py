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
        
    # def add(self, value):
    #     if not isinstance(value,KTreeNode):
    #         value = KTreeNode(self.k,value)
    #     if self.root is None:
    #         self.root = value
    #         return

    #     def add_to_left(root:KTreeNode,to_add = value):
    #         if len(root.connections)  < self.k:
    #             root.connections.append(to_add)
    #         add_to_left(root.connections[0],to_add)

    #     def find_open_spot(root:KTreeNode,to_add = value):
    #         if len(root.connections) < self.k:
    #             print(len(root.connections))
    #             print('to_add', to_add.value)
    #             root.connections.append(to_add)
    #             print([connection.value for connection in root.connections])
    #             return True
    #         for node in root.connections:
    #             find_open_spot(node,to_add)

    #     find_open_spot(self.root)
    #def add(tree:KAryTree):
def breadth_first(tree:KAryTree,to_add) -> list:
    q = deque()
    if tree.root is None:
        tree.root = KTreeNode(tree.k, to_add)
    q.appendleft(tree.root)
    temp = None
    while len(q) > 0:
        temp = q.pop()
        if len(temp.connections) < tree.k:
            print(temp.value)
            print(temp.connections)
            temp.connections.append(KTreeNode(tree.k,to_add))
            return
        for connection in temp.connections:
            q.appendleft(connection)
    
    return
