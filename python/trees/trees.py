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
            


