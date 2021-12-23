from trees.trees import KTree,KTreeNode

def tree_fizz_buzz(tree:KTree):
    new_tree = KTree
    def walk(root:KTreeNode):
        for connection in root.connections:
            if root.value % 3 == 0:
                root.value = 'Fizz'
            elif root.value % 5 == 0:
                root.value = 'Buzz'
            elif root.value % 15 == 0:
                root.value = 'FizzBuzz'
            walk(connection)
    
